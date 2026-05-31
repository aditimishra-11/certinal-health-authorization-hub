#!/usr/bin/env python3
"""Splice pass-2 sections into index.html and renumber SECTION labels by DOM order.
Usage: python3 splice_pass2.py <task_output.json>
"""
import json, re, sys, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(BASE, "index.html")

def section_span(html, sid):
    m = re.search(r'<section[^>]*id="%s"' % re.escape(sid), html)
    if not m:
        raise SystemExit("section id=%s not found" % sid)
    start = m.start()
    end = html.index("</section>", start) + len("</section>")
    return start, end

def replace_section(html, sid, new_html):
    s, e = section_span(html, sid)
    return html[:s] + new_html.strip() + html[e:]

def insert_before(html, sid, new_html):
    m = re.search(r'<section[^>]*id="%s"' % re.escape(sid), html)
    if not m:
        raise SystemExit("anchor id=%s not found" % sid)
    p = m.start()
    return html[:p] + new_html.strip() + "\n\n" + html[p:]

def main():
    secs = {}
    d = json.load(open(sys.argv[1]))
    res = d.get("result", d)
    for s in res.get("sections", []):
        secs[s["id"]] = s["html"]
    print("got sections:", list(secs.keys()))

    html = open(IDX).read()

    # 1) replace rebuilt sections
    if "s6" in secs:  html = replace_section(html, "s6", secs["s6"])
    if "s15" in secs: html = replace_section(html, "s15", secs["s15"])
    # 2) insert new sections at narrative positions
    if "s8b" in secs:  html = insert_before(html, "s9",  secs["s8b"])   # personas before product vision
    if "s18b" in secs: html = insert_before(html, "s19", secs["s18b"])  # metrics before "why wins"

    # 3) renumber every "SECTION NN" label by DOM order
    counter = {"n": 0}
    def renum(m):
        counter["n"] += 1
        return "SECTION %02d" % counter["n"]
    html = re.sub(r'SECTION\s+\d+', renum, html)
    print("renumbered", counter["n"], "section labels")

    open(IDX, "w").write(html)
    # report DOM order of scenes
    ids = re.findall(r'<section[^>]*id="(s[0-9b]+)"', html)
    print("DOM order:", ", ".join(ids), "(", len(ids), "scenes )")
    print("wrote", IDX, "(%d bytes)" % len(html))

if __name__ == "__main__":
    main()
