#!/usr/bin/env python3
"""Writes console/index.html: the redirect left where the founder console used to be.

The console moved (2026-11-04) to its own private site, https://helpy-console.pages.dev.
This page:
  - REVOKES the old session this origin still holds (Supabase /auth/v1/logout?scope=local
    with its own token), then removes every helpy_console_auth* key (the session and its
    PKCE code-verifier) and sessionStorage helpy_dash_key;
  - without saved console data: sends them on, keeping a validated #tab (^[a-z]{1,20}$;
    Telegram links say help-y.com/console/#infra), never the raw hash;
  - with saved settings / internal-document notes: offers ONE click that hands them over.
    It opens <new>/migrate#n=<one-time nonce>&tab=<tab> and, when that page (exact origin)
    says ready, posts the items to that exact origin. The new page checks origin + opener +
    nonce + allow-list + sizes, stores them, and acknowledges; only acknowledged keys are
    deleted here, and only while they still hold what was sent. A document key the new
    site already had is kept on BOTH (the new site offers a restore). What could not move is
    listed, can be downloaded as JSON, moved again, or removed on a confirm. Done
    (helpy_console_migrate_done) only when nothing is left; "בלי להעביר הפעם" is for this
    visit only (sessionStorage).
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
# the flat lists the page needs (the receiver builds the same from the same file)
KF = {"prefs": K["prefs"], "keyPattern": K["keyPattern"], "maxItems": K["maxItems"], "maxValue": K["maxValue"],
      "maxTotal": K["maxTotal"], "docKeys": [k for d in K["docs"].values() for k in d.get("keys", [])],
      "docPrefixes": [p for d in K["docs"].values() for p in d.get("prefixes", [])]}
SUPA = "https://lwomstzzmyegpbidibfm.supabase.co"
ANON = "sb_publishable_4UpbPcXm8El9N91W2Lp8Gg_Pp5Vg-_S"   # Helpy's public (publishable) key, as in the console

JS = r"""
(function () {
  "use strict";
  var NEW = "%NEW%", SUPA = "%SUPA%", ANON = "%ANON%";
  var K = %KEYS%;
  var DONE = "helpy_console_migrate_done", SKIP = "helpy_console_migrate_skip";
  var tab = /^#[a-z]{1,20}$/.test(location.hash) ? location.hash.slice(1) : "";
  var go = NEW + "/" + (tab ? "#" + tab : "");   // only a validated tab, never the raw hash
  var $ = function (id) { return document.getElementById(id); };
  var ls = null;
  try { ls = window.localStorage; sessionStorage.removeItem("helpy_dash_key"); } catch (e) {}

  // 1. the old session: REVOKED at Supabase (scope=local: this session only), then removed -
  //    every helpy_console_auth* key (the session and its PKCE code-verifier)
  function revoke(done) {
    var keys = [], calls = [];
    try { for (var i = 0; i < ls.length; i++) { var k = ls.key(i); if (k && k.indexOf("helpy_console_auth") === 0) keys.push(k); } } catch (e) {}
    keys.forEach(function (k) {
      var tok = null;
      try { tok = JSON.parse(ls.getItem(k) || "null"); tok = tok && (tok.access_token || (tok.currentSession && tok.currentSession.access_token)); } catch (e) { tok = null; }
      if (typeof tok === "string" && tok.split(".").length === 3) {
        calls.push(Promise.race([
          fetch(SUPA + "/auth/v1/logout?scope=local", { method: "POST", headers: { apikey: ANON, authorization: "Bearer " + tok } }).catch(function () {}),
          new Promise(function (r) { setTimeout(r, 3000); })
        ]));
      }
    });
    Promise.all(calls).then(function () {
      keys.forEach(function (k) { try { ls.removeItem(k); } catch (e) {} });
      done();
    });
  }

  function collect() {
    var items = {}, sendable = {}, over = [], n = 0;
    if (!ls) return { n: 0 };
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
      } else over.push(k);
    }
    return { items: items, sendable: sendable, over: over, n: n };
  }

  revoke(function () {
    var c = collect(), aside = [];
    try { aside = JSON.parse(ls.getItem(DONE + "_aside") || "[]"); } catch (e) { aside = []; }
    var open = Object.keys(c.items || {}).filter(function (k) { return aside.indexOf(k) < 0; });
    var skipped = false;
    try { skipped = !!sessionStorage.getItem(SKIP); } catch (e) {}
    if (!open.length || skipped) { location.replace(go); return; }
    ask(c, open.length);
  });

  function ask(c, n) {
    $("count").textContent = String(n);
    $("ask").hidden = false; $("moved").hidden = true; $("done").hidden = true;
    $("skip").onclick = function () {            // this visit only: offered again next time
      try { sessionStorage.setItem(SKIP, "1"); } catch (e) {}
      location.replace(go);
    };
    var w = null, nonce = "", sent = false;
    $("move").onclick = function () {
      var b = new Uint8Array(16); crypto.getRandomValues(b);
      nonce = Array.prototype.map.call(b, function (x) { return ("0" + x.toString(16)).slice(-2); }).join("");
      sent = false;
      w = window.open(NEW + "/migrate#n=" + nonce + (tab ? "&tab=" + tab : ""), "_blank");
      $("msg").textContent = w ? "מעביר..." : "הדפדפן חסם את הלשונית החדשה. יש לאפשר חלונות קופצים לאתר הזה ולנסות שוב.";
    };
    window.onmessage = function (e) {
      var d = e.data;
      if (!w || e.origin !== NEW || e.source !== w || !d || typeof d !== "object" || !nonce || d.n !== nonce) return;
      if (d.type === "helpy-migrate-ready" && !sent) {
        sent = true;
        w.postMessage({ type: "helpy-migrate", n: nonce, items: c.sendable }, NEW);
      } else if (d.type === "helpy-migrate-ack" && Array.isArray(d.stored)) {
        nonce = "";
        var own = function (k) { return typeof k === "string" && Object.prototype.hasOwnProperty.call(c.sendable, k); };
        finish(c, d.stored.filter(own), (Array.isArray(d.aside) ? d.aside : []).filter(own));
      }
    };
  }

  function finish(c, stored, asideNow) {
    var moved = 0, left = c.over.slice();
    Object.keys(c.sendable).forEach(function (k) {
      if (asideNow.indexOf(k) >= 0) return;            // kept on BOTH sites (the new one offers a restore)
      // removed only if it still holds exactly what was sent
      if (stored.indexOf(k) >= 0 && ls.getItem(k) === c.sendable[k]) { try { ls.removeItem(k); moved++; } catch (err) { left.push(k); } }
      else left.push(k);
    });
    var aside = [];
    try { aside = JSON.parse(ls.getItem(DONE + "_aside") || "[]"); } catch (e) {}
    asideNow.forEach(function (k) { if (aside.indexOf(k) < 0) aside.push(k); });
    try { ls.setItem(DONE + "_aside", JSON.stringify(aside)); } catch (e) {}
    if (!left.length) { try { ls.setItem(DONE, new Date().toISOString()); } catch (e) {} }   // DONE only when nothing is left
    $("ask").hidden = true;
    $("done").hidden = false;
    $("done-k").textContent = String(moved);
    $("done-n").textContent = String(c.n);
    $("aside").hidden = !asideNow.length;
    $("aside-n").textContent = String(asideNow.length);
    $("left").hidden = !left.length;
    var ul = $("left-list"); ul.textContent = "";
    left.forEach(function (k) { var li = document.createElement("li"); li.textContent = k; li.dir = "ltr"; ul.appendChild(li); });
    if (!left.length) return;
    var data = {}; left.forEach(function (k) { var v = ls.getItem(k); if (v !== null) data[k] = v; });
    var url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 1)], { type: "application/json" }));
    $("download").href = url;
    $("again").onclick = function () { ask(collect(), left.length); };
    $("drop").onclick = function () {
      if (!window.confirm("למחוק מהדפדפן הזה את " + left.length + " הפריטים שלא הועברו? כדאי להוריד אותם קודם.")) return;
      left.forEach(function (k) { try { ls.removeItem(k); } catch (err) {} });
      try { ls.setItem(DONE, new Date().toISOString()); } catch (e) {}
      $("left").hidden = true;
      $("dropped").hidden = false;
    };
  }
})();
""".replace("%NEW%", NEW).replace("%SUPA%", SUPA).replace("%ANON%", ANON).replace("%KEYS%", json.dumps(KF, ensure_ascii=False, separators=(",", ":")))

HTML = """<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
<!-- Generated by scripts/build_console_redirect.py - edit that, not this. -->
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'sha256-{hash}'; style-src 'unsafe-inline'; connect-src {supa}; base-uri 'none'; form-action 'none'">
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
<p><button id="move" type="button">להעביר ולפתוח את הקונסולה</button> <button id="skip" class="quiet" type="button">בלי להעביר הפעם</button></p>
<p id="msg" role="status"></p>
</div>
<div id="done" hidden>
<p>הועברו <span id="done-k"></span> מתוך <span id="done-n"></span>. הקונסולה נפתחה בלשונית החדשה.</p>
<p id="aside" hidden><span id="aside-n"></span> פריטים כבר היו שמורים גם בקונסולה החדשה. הגרסה מכאן נשמרה שם בצד ואפשר לשחזר אותה מתוך המסמך, והיא נשארת גם כאן.</p>
<div id="left" hidden>
<p>אלה לא הועברו ונשארו בדפדפן הזה:</p>
<ul id="left-list"></ul>
<p><button id="again" type="button">להעביר שוב</button> <a id="download" download="helpy-console-old-data.json" href="#">להוריד אותם כקובץ</a> <button id="drop" class="quiet" type="button">למחוק את מה שלא הועבר</button></p>
</div>
<p id="dropped" hidden>נמחק.</p>
</div>
<script>{js}</script>
</body>
</html>
"""

h = base64.b64encode(hashlib.sha256(JS.encode()).digest()).decode()
out = HTML.format(hash=h, new=NEW, host=NEW.split("//")[1], js=JS, supa=SUPA)
path = os.path.join(os.path.dirname(HERE), "console", "index.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(out)
print(f"wrote {path} (script sha256-{h})")
