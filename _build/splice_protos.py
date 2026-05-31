#!/usr/bin/env python3
"""Splice the rebuilt/new prototype sections into index.html and renumber the
PROTOTYPE JOURNEY labels. Usage: python3 splice_protos.py <task_output.json>"""
import json, re, sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(BASE, "index.html")

def span(html, sid):
    m = re.search(r'<section[^>]*id="%s"' % re.escape(sid), html)
    if not m: raise SystemExit("not found: " + sid)
    s = m.start(); e = html.index("</section>", s) + len("</section>")
    return s, e

def replace(html, sid, new):
    s, e = span(html, sid); return html[:s] + new.strip() + html[e:]

def insert_before(html, sid, new):
    m = re.search(r'<section[^>]*id="%s"' % re.escape(sid), html)
    if not m: raise SystemExit("anchor not found: " + sid)
    p = m.start(); return html[:p] + new.strip() + "\n\n" + html[p:]

def main():
    d = json.load(open(sys.argv[1])); res = d.get("result", d)
    secs = {s["id"]: s["html"] for s in res.get("sections", [])}
    print("got:", list(secs.keys()))
    html = open(IDX).read()
    if "s15" in secs:  html = replace(html, "s15", secs["s15"])
    if "s16" in secs:  html = replace(html, "s16", secs["s16"])
    if "s16b" in secs: html = insert_before(html, "s17", secs["s16b"])
    # renumber PROTOTYPE JOURNEY labels in DOM order
    c = {"n": 0}
    def rn(m):
        c["n"] += 1; return "PROTOTYPE JOURNEY %02d" % c["n"]
    html = re.sub(r'PROTOTYPE JOURNEY\s*\d+', rn, html)
    print("renumbered", c["n"], "prototype-journey labels")
    open(IDX, "w").write(html)
    ids = re.findall(r'<section[^>]*id="(s[0-9b]+)"', html)
    print("DOM order:", ", ".join(ids), "(", len(ids), "scenes )")
    print("bytes:", len(html))

if __name__ == "__main__":
    main()
