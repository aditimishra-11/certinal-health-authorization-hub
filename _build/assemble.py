#!/usr/bin/env python3
"""Assemble index.html from the section JSON produced by the workflows."""
import json, re, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

def load_first_run():
    f = sys.argv[1]
    d = json.load(open(f))
    return d["result"]["sections"]

def num(sid):
    return int(re.sub(r"\D", "", sid))

def main():
    sections = {}
    # 16 from saved raw
    for s in json.load(open(os.path.join(BASE, "_sections_raw.json"))):
        sections[s["id"]] = s
    # missing-sections output passed as argv[1] (task output json)
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        d = json.load(open(sys.argv[1]))
        res = d.get("result", d)
        extra = res.get("sections", [])
        for s in extra:
            sections[s["id"]] = s

    ordered = sorted(sections.values(), key=lambda s: num(s["id"]))
    ids = [s["id"] for s in ordered]
    print("Assembling", len(ordered), "sections:", ", ".join(ids))
    missing = [f"s{i}" for i in range(1, 21) if f"s{i}" not in sections]
    if missing:
        print("!! STILL MISSING:", missing)

    head = open(os.path.join(BASE, "_shell-head.html")).read()
    foot = open(os.path.join(BASE, "_shell-foot.html")).read()
    body = "\n\n".join(s["html"] for s in ordered)
    html = head + "\n" + body + "\n" + foot
    out = os.path.join(BASE, "index.html")
    open(out, "w").write(html)
    print("Wrote", out, f"({len(html):,} bytes)")

if __name__ == "__main__":
    main()
