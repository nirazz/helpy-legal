#!/usr/bin/env python3
"""Writes the /help/ guide pages and sitemap.xml from scripts/guides_content.py.

  help/index.html, help/index-he.html        the hub: every category, both languages
  help/<slug>.html, help/<slug>-he.html      one page per category
  sitemap.xml                                every public page, with hreflang pairs

Generated files - edit the content file or this script, then re-run:
  python3 scripts/build_guides.py
CI re-runs it and fails on any difference, so a hand edit cannot ship.

The pages carry no script at all (nothing for check_page_scripts to break) and no user
data: this repo is public. Store links carry a per-page campaign (App Store `ct`, Play
`utm_campaign`) so installs from organic search can be told apart from the home page.
"""
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from guides_content import CATEGORIES, HUB, SHARED_FAQ, STEPS  # noqa: E402

SITE = "https://help-y.com"
APP_STORE_ID = "6758919822"
PLAY_ID = "com.neighborlyhelp.app"
SAME_AS = [
    "https://www.facebook.com/profile.php?id=61588709264545",
    "https://www.instagram.com/helpy.community/",
    f"https://apps.apple.com/app/id{APP_STORE_ID}",
    f"https://play.google.com/store/apps/details?id={PLAY_ID}",
]

# Pages that exist outside this generator, en/he pairs, for the sitemap.
STATIC_PAIRS = [("/", "/index-he.html", "1.0")] + [
    (f"/{b}.html", f"/{b}-he.html", "0.3") for b in ("terms", "privacy", "delete-account", "accessibility")
]

T = {
    "he": {"dir": "rtl", "home": "/index-he.html?lang=he", "hub": "/help/index-he.html", "other": "English",
           "examples": "למשל", "how": "איך זה עובד", "tips": "כדאי לדעת", "faq": "שאלות נפוצות",
           "more": "עוד דרכים שבהן שכנים עוזרים", "cta": "מתחילים עכשיו", "cta_sub": "Helpy חינמית לאייפון ולאנדרואיד.",
           "crumb_home": "Helpy", "crumb_hub": "במה שכנים עוזרים", "privacy": "מדיניות פרטיות", "terms": "תנאי שימוש",
           "privacy_href": "/privacy-he.html", "terms_href": "/terms-he.html",
           "a11y": "הצהרת נגישות", "a11y_href": "/accessibility-he.html", "delete": "מחיקת חשבון", "delete_href": "/delete-account-he.html", "a_app": "הורידו את Helpy מ-App Store",
           "a_play": "הורידו את Helpy מ-Google Play", "hub_link": "במה שכנים עוזרים"},
    "en": {"dir": "ltr", "home": "/?lang=en", "hub": "/help/", "other": "עברית",
           "examples": "For example", "how": "How it works", "tips": "Good to know", "faq": "Questions",
           "more": "More ways neighbors help", "cta": "Get started", "cta_sub": "Helpy is free on iPhone and Android.",
           "crumb_home": "Helpy", "crumb_hub": "Ways neighbors help", "privacy": "Privacy", "terms": "Terms",
           "privacy_href": "/privacy.html", "terms_href": "/terms.html",
           "a11y": "Accessibility", "a11y_href": "/accessibility.html", "delete": "Delete account", "delete_href": "/delete-account.html", "a_app": "Download Helpy on the App Store",
           "a_play": "Get Helpy on Google Play", "hub_link": "Ways neighbors help"},
}

APPLE_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.05 20.28c-.98.95-2.05.86-3.08.41-1.09-.47-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.41C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg>')
PLAY_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.6 2.4c-.4.4-.6 1-.6 1.7v15.8c0 .7.2 1.3.6 1.7L13 12 3.6 2.4z" fill="#00A0FF"/>'
            '<path d="M16.6 15.6L13 12l3.6-3.6 4.6 2.6c1.3.7 1.3 1.9 0 2.6l-4.6 2.0z" fill="#FFC400"/>'
            '<path d="M16.6 15.6L13 12 3.6 21.6c.6.6 1.5.7 2.4.2l10.6-6.2z" fill="#F0284A"/>'
            '<path d="M16.6 8.4L6 2.2c-.9-.5-1.8-.4-2.4.2L13 12l3.6-3.6z" fill="#32A071"/></svg>')

e = html.escape


def page_paths(slug):
    """slug None = hub. Returns (en_path, he_path) as URL paths."""
    if slug is None:
        return "/help/", "/help/index-he.html"
    return f"/help/{slug}.html", f"/help/{slug}-he.html"


def file_for(path):
    return ROOT / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))


def badges(lang, campaign):
    t = T[lang]
    app = f"https://apps.apple.com/app/apple-store/id{APP_STORE_ID}?pt=128532406&amp;ct={campaign}&amp;mt=8"
    play = (f"https://play.google.com/store/apps/details?id={PLAY_ID}&amp;referrer="
            f"utm_source%3Dhelpy_site%26utm_medium%3Dguide%26utm_campaign%3D{campaign}")
    return (f'<div class="badges">'
            f'<a class="badge" href="{app}" aria-label="{e(t["a_app"])}">{APPLE_SVG}<span><small>Download on the</small>App Store</span></a>'
            f'<a class="badge" href="{play}" aria-label="{e(t["a_play"])}">{PLAY_SVG}<span><small>Get it on</small>Google Play</span></a>'
            f'</div>')


def head(lang, title, description, en_path, he_path, ld):
    canon = he_path if lang == "he" else en_path
    # "</" would close the script tag early; "<\/" is the same string to a JSON parser
    lds = "\n".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>" for x in ld)
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{T[lang]['dir']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{SITE}{canon}">
<link rel="alternate" hreflang="en" href="{SITE}{en_path}">
<link rel="alternate" hreflang="he" href="{SITE}{he_path}">
<link rel="alternate" hreflang="x-default" href="{SITE}{en_path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:image" content="{SITE}/app-icon-512.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}{canon}">
<link rel="icon" href="/app-icon-512.png">
<link rel="apple-touch-icon" href="/app-icon-512.png">
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/help/guide.css">
{lds}
</head>
<body>
"""


def topbar(lang, en_path, he_path):
    t = T[lang]
    other_path, other_lang = (en_path, "en") if lang == "he" else (he_path, "he")
    return (f'<header class="top"><a class="brand" href="{t["home"]}"><img src="/app-icon-512.png" alt="" width="32" height="32">Helpy</a>'
            f'<a class="lang" href="{other_path}" lang="{other_lang}" hreflang="{other_lang}">{t["other"]}</a></header>\n')


def footer(lang):
    t = T[lang]
    return (f'<footer class="foot"><a href="{t["home"]}">Helpy</a><a href="{t["hub"]}">{e(t["hub_link"])}</a>'
            f'<a href="{t["privacy_href"]}">{e(t["privacy"])}</a><a href="{t["terms_href"]}">{e(t["terms"])}</a>'
            f'<a href="{t["delete_href"]}">{e(t["delete"])}</a><a href="{t["a11y_href"]}">{e(t["a11y"])}</a>'
            f'<a href="mailto:support@help-y.com">support@help-y.com</a></footer>\n</body>\n</html>\n')


def crumbs_ld(lang, items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p.split("?")[0]}
                                for i, (n, p) in enumerate(items)]}


def category_page(cat, lang):
    c, t = cat[lang], T[lang]
    en_path, he_path = page_paths(cat["slug"])
    me = he_path if lang == "he" else en_path
    faq = c["faq"] + SHARED_FAQ[lang]
    ld = [crumbs_ld(lang, [(t["crumb_home"], t["home"]), (t["crumb_hub"], t["hub"]), (c["label"], me)]),
          {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    out = [head(lang, c["title"], c["description"], en_path, he_path, ld), topbar(lang, en_path, he_path)]
    out.append(f'<main>\n<nav class="crumbs" aria-label="breadcrumb"><a href="{t["home"]}">Helpy</a> <span aria-hidden="true">/</span> '
               f'<a href="{t["hub"]}">{e(t["crumb_hub"])}</a></nav>\n')
    out.append(f'<h1>{e(c["h1"])}</h1>\n<p class="lede">{e(c["lede"])}</p>\n{badges(lang, "guide_" + cat["slug"].replace("-", "_"))}\n')
    out.append(f'<section><h2>{e(t["examples"])}</h2><ul class="ex">' + "".join(f"<li>{e(x)}</li>" for x in c["examples"]) + "</ul></section>\n")
    out.append(f'<section><h2>{e(t["how"])}</h2><ol class="steps">' +
               "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in STEPS[lang]) + "</ol></section>\n")
    out.append(f'<section><h2>{e(t["tips"])}</h2><ul class="tips">' + "".join(f"<li>{e(x)}</li>" for x in c["tips"]) + "</ul></section>\n")
    out.append(f'<section><h2>{e(t["faq"])}</h2>' +
               "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq) + "</section>\n")
    others = [o for o in CATEGORIES if o["slug"] != cat["slug"]]
    out.append(f'<section><h2>{e(t["more"])}</h2><ul class="more">' +
               "".join(f'<li><a href="{page_paths(o["slug"])[1 if lang == "he" else 0]}">{e(o[lang]["label"])}</a></li>' for o in others) +
               "</ul></section>\n")
    out.append(f'<section class="cta"><h2>{e(t["cta"])}</h2><p>{e(t["cta_sub"])}</p>{badges(lang, "guide_" + cat["slug"].replace("-", "_"))}</section>\n</main>\n')
    out.append(footer(lang))
    return "".join(out)


def hub_page(lang):
    h, t = HUB[lang], T[lang]
    en_path, he_path = page_paths(None)
    me = he_path if lang == "he" else en_path
    ld = [crumbs_ld(lang, [(t["crumb_home"], t["home"]), (t["crumb_hub"], me)])]
    out = [head(lang, h["title"], h["description"], en_path, he_path, ld), topbar(lang, en_path, he_path)]
    out.append(f'<main>\n<h1>{e(h["h1"])}</h1>\n<p class="lede">{e(h["lede"])}</p>\n<ul class="cards">')
    for c in CATEGORIES:
        p = page_paths(c["slug"])[1 if lang == "he" else 0]
        out.append(f'<li><a href="{p}"><b>{e(c[lang]["label"])}</b><span>{e(c[lang]["description"])}</span></a></li>')
    out.append(f'</ul>\n<section class="cta"><h2>{e(t["cta"])}</h2><p>{e(t["cta_sub"])}</p>{badges(lang, "guide_hub")}</section>\n</main>\n')
    out.append(footer(lang))
    return "".join(out)


def sitemap():
    pairs = list(STATIC_PAIRS) + [page_paths(None) + ("0.6",)] + [page_paths(c["slug"]) + ("0.6",) for c in CATEGORIES]
    rows = []
    for en, he, prio in pairs:
        for loc in (en, he):
            rows.append(f"""  <url>
    <loc>{SITE}{loc}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/>
    <xhtml:link rel="alternate" hreflang="he" href="{SITE}{he}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{en}"/>
    <priority>{prio}</priority>
  </url>""")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def main():
    written = {}
    for lang in ("en", "he"):
        en_path, he_path = page_paths(None)
        written[he_path if lang == "he" else en_path] = hub_page(lang)
        for c in CATEGORIES:
            en_path, he_path = page_paths(c["slug"])
            written[he_path if lang == "he" else en_path] = category_page(c, lang)
    # a page no longer generated (category dropped or renamed) is deleted, so git shows it
    keep = {file_for(p).resolve() for p in written}
    for f in (ROOT / "help").glob("*.html"):
        if f.resolve() not in keep:
            f.unlink()
            print("removed stale", f.relative_to(ROOT))
    for path, body in written.items():
        f = file_for(path)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(body, encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    print(f"wrote {len(written)} guide pages + sitemap.xml")


if __name__ == "__main__":
    main()
