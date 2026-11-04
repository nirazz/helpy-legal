#!/usr/bin/env python3
"""Writes console/index.html: the redirect left where the founder console used to be.

The console moved (2026-11-04) to its own private site, https://helpy-console.pages.dev.
This page:
  - removes the old session this origin still holds (every helpy_console_auth* key -
    the session and its PKCE code-verifier - and sessionStorage helpy_dash_key);
  - without saved console data (or once the visitor has answered): sends them on, keeping
    the #tab (Telegram links say help-y.com/console/#infra);
  - with saved settings / internal-document notes: offers ONE click that hands them over.
    It opens <new>/migrate#n=<one-time nonce>&tab=<tab> and, when that page (exact origin)
    says ready, posts the items to that exact origin. The new page checks origin + opener +
    nonce + allow-list + sizes, stores them, and acknowledges; only acknowledged keys are
    deleted here. What could not move is listed and removed only on a confirm. "בלי
    להעביר" remembers the answer (helpy_console_migrate_done), so later visits go straight on.
    Nothing but the nonce and the tab name is ever put in a URL.
Which keys and how much: scripts/console-migrate-keys.json, a PINNED copy of admin-console's
helpy/migrate-keys.json (the one source; admin-console's tests fail if they differ). This
page applies the receiver's limits before sending, so nothing is sent that it would refuse.
The script is inline, allowed by its sha256 in the page's CSP - so edit THIS file and re-run
(CI re-runs it and fails on any difference, so a hand edit or a stale hash cannot ship):
  python3 scripts/build_console_redirect.py [--keys path/to/migrate-keys.json]
"""
import base64
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = "https://helpy-console.pages.dev"
keys_path = os.path.join(HERE, "console-migrate-keys.json")
if "--keys" in sys.argv:
    keys_path = sys.argv[sys.argv.index("--keys") + 1]
with open(keys_path, encoding="utf-8") as f:
    K = json.load(f)
K.pop("_", None)

JS = r"""
(function () {
  "use strict";
  var NEW = "%NEW%";
  var K = %KEYS%;
  var DONE = "helpy_console_migrate_done";
  var hash = location.hash, tab = /^#[a-z]{1,20}$/.test(hash) ? hash.slice(1) : "";
  var go = NEW + "/" + hash;
  var items = {}, sendable = {}, leftover = [], n = 0, ls = null;
  try {
    ls = window.localStorage;
    // the old session: never handed over, always removed (session + PKCE verifier)
    for (var i = ls.length - 1; i >= 0; i--) {
      var a = ls.key(i);
      if (a && a.indexOf("helpy_console_auth") === 0) ls.removeItem(a);
    }
    sessionStorage.removeItem("helpy_dash_key");
    if (ls.getItem(DONE)) { location.replace(go); return; }
    var keyRe = new RegExp(K.keyPattern), total = 0, count = 0;
    for (var j = 0; j < ls.length; j++) {
      var k = ls.key(j);
      var want = K.prefs.indexOf(k) >= 0 || K.docKeys.indexOf(k) >= 0 ||
        K.docPrefixes.some(function (p) { return k.indexOf(p) === 0; });
      if (!want) continue;
      var v = ls.getItem(k); items[k] = v; n++;
      // the receiver's own limits, applied here: what it would refuse is not sent
      if (keyRe.test(k) && v.length <= K.maxValue && total + k.length + v.length <= K.maxTotal && count < K.maxItems) {
        sendable[k] = v; total += k.length + v.length; count++;
      } else leftover.push(k);
    }
  } catch (e) { n = 0; }
  if (!n) { location.replace(go); return; }

  var $ = function (id) { return document.getElementById(id); };
  $("count").textContent = String(n);
  $("ask").hidden = false;
  $("moved").hidden = true;
  $("skip").addEventListener("click", function () {
    try { ls.setItem(DONE, "skipped " + new Date().toISOString()); } catch (e) {}
    location.replace(go);
  });
  var w = null, nonce = "", sent = false;
  $("move").addEventListener("click", function () {
    var b = new Uint8Array(16); crypto.getRandomValues(b);
    nonce = Array.prototype.map.call(b, function (x) { return ("0" + x.toString(16)).slice(-2); }).join("");
    sent = false;
    w = window.open(NEW + "/migrate#n=" + nonce + (tab ? "&tab=" + tab : ""), "_blank");
    $("msg").textContent = w ? "מעביר..." : "הדפדפן חסם את הלשונית החדשה. יש לאפשר חלונות קופצים לאתר הזה ולנסות שוב.";
  });
  function finish(stored) {
    var moved = 0, left = leftover.slice();
    Object.keys(sendable).forEach(function (k) {
      if (stored.indexOf(k) >= 0) { try { ls.removeItem(k); moved++; } catch (err) { left.push(k); } }
      else left.push(k);
    });
    try { ls.setItem(DONE, "moved " + new Date().toISOString()); } catch (e) {}
    $("ask").hidden = true;
    $("done").hidden = false;
    $("done-k").textContent = String(moved);
    $("done-n").textContent = String(n);
    if (left.length) {
      $("left").hidden = false;
      var ul = $("left-list");
      left.forEach(function (k) { var li = document.createElement("li"); li.textContent = k; li.dir = "ltr"; ul.appendChild(li); });
      $("drop").addEventListener("click", function () {
        if (!window.confirm("למחוק מהדפדפן הזה את " + left.length + " הפריטים שלא הועברו?")) return;
        left.forEach(function (k) { try { ls.removeItem(k); } catch (err) {} });
        $("left").hidden = true;
        $("dropped").hidden = false;
      });
    }
  }
  window.addEventListener("message", function (e) {
    var d = e.data;
    if (!w || e.origin !== NEW || e.source !== w || !d || typeof d !== "object" || !nonce || d.n !== nonce) return;
    if (d.type === "helpy-migrate-ready" && !sent) {
      sent = true;
      w.postMessage({ type: "helpy-migrate", n: nonce, items: sendable }, NEW);
    } else if (d.type === "helpy-migrate-ack" && Array.isArray(d.stored)) {
      nonce = "";
      finish(d.stored.filter(function (k) { return typeof k === "string" && Object.prototype.hasOwnProperty.call(sendable, k); }));
    }
  });
})();
""".replace("%NEW%", NEW).replace("%KEYS%", json.dumps(K, ensure_ascii=False, separators=(",", ":")))

HTML = """<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
<!-- Generated by scripts/build_console_redirect.py - edit that, not this. -->
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'sha256-{hash}'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Helpy Console</title>
<!-- Without script a meta refresh cannot carry the #tab (it never sees the fragment), so
     it lands on the console's start page. -->
<noscript><meta http-equiv="refresh" content="0; url={new}/"></noscript>
<style>body{{font:15px system-ui,sans-serif;max-width:480px;margin:15vh auto;padding:0 16px;color:#0f1115;line-height:1.6}}
button{{font:inherit;padding:10px 16px;border-radius:10px;border:0;background:#4f46e5;color:#fff;cursor:pointer}}
button.quiet{{background:none;color:#4f46e5;padding:10px 4px;text-decoration:underline}}
a{{color:#4f46e5}} ul{{padding-inline-start:20px}}</style>
</head>
<body>
<p id="moved">הקונסולה עברה: <a href="{new}/"><bdi dir="ltr">{host}</bdi></a></p>
<div id="ask" hidden>
<p>הקונסולה עברה לאתר חדש (<bdi dir="ltr">{host}</bdi>). בדפדפן הזה נשמרו מהקונסולה הישנה הגדרות והערות במסמכים (<span id="count"></span>). להעביר אותן?</p>
<p><button id="move" type="button">להעביר ולפתוח את הקונסולה</button> <button id="skip" class="quiet" type="button">בלי להעביר</button></p>
<p id="msg" role="status"></p>
</div>
<div id="done" hidden>
<p>הועברו <span id="done-k"></span> מתוך <span id="done-n"></span>. הקונסולה נפתחה בלשונית החדשה, ואפשר לסגור את הלשונית הזו.</p>
<div id="left" hidden>
<p>אלה לא הועברו ונשארו בדפדפן הזה:</p>
<ul id="left-list"></ul>
<p><button id="drop" class="quiet" type="button">למחוק את מה שלא הועבר</button></p>
</div>
<p id="dropped" hidden>נמחק.</p>
</div>
<script>{js}</script>
</body>
</html>
"""

h = base64.b64encode(hashlib.sha256(JS.encode()).digest()).decode()
out = HTML.format(hash=h, new=NEW, host=NEW.split("//")[1], js=JS)
path = os.path.join(os.path.dirname(HERE), "console", "index.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(out)
print(f"wrote {path} (script sha256-{h})")
