#!/usr/bin/env python3
"""Fail if any inline <script> on a site page does not parse.

A page whose inline script has a syntax error still renders, but none of its
script runs - buttons look fine and do nothing.

Usage:
  python3 scripts/check_page_scripts.py                 # every *.html in the repo
  python3 scripts/check_page_scripts.py --url URL ...   # the LIVE pages
Needs `node` on PATH. Exit 1 = a page whose script would not run.
"""
import glob
import os
import re
import subprocess
import sys
import tempfile
import urllib.request

# Inline scripts only; JSON-LD and other data blocks are not JavaScript.
SCRIPT_RE = re.compile(r"<script(?![^>]*\bsrc=)([^>]*)>(.*?)</script>", re.S | re.I)
DATA_TYPE_RE = re.compile(r"type\s*=\s*[\"'](application/(ld\+)?json|text/template)", re.I)


def check(name, html):
    bad = 0
    for i, (attrs, js) in enumerate(SCRIPT_RE.findall(html)):
        if DATA_TYPE_RE.search(attrs) or not js.strip():
            continue
        ext = ".mjs" if re.search(r"type\s*=\s*[\"']module", attrs, re.I) else ".js"
        with tempfile.NamedTemporaryFile("w", suffix=ext, delete=False, encoding="utf-8") as f:
            f.write(js)
            path = f.name
        r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        os.unlink(path)
        if r.returncode != 0:
            bad += 1
            # node prints "<file>:<line>" then the offending line and the error.
            print(f"FAIL {name} inline script #{i}:\n{r.stderr.strip()[:1500]}\n")
    return bad


def main(argv):
    bad = 0
    if argv[:1] == ["--url"]:
        for url in argv[1:]:
            req = urllib.request.Request(url, headers={"Cache-Control": "no-cache"})
            html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
            bad += check(url, html)
        total = len(argv) - 1
    else:
        files = sorted(glob.glob("**/*.html", recursive=True))
        for path in files:
            with open(path, encoding="utf-8") as f:
                bad += check(path, f.read())
        total = len(files)
    print(f"{'FAIL' if bad else 'PASS'}: {total} page(s) checked, {bad} broken script(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
