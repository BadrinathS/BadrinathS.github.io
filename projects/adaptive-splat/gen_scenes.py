#!/usr/bin/env python3
"""Scan assets/<DATASET>/<scene_id>/ for context.png + rendered.png and
regenerate the scene list. Writes assets/scenes.json AND updates the inline
list inside index.html (between /*SCENES_START*/ and /*SCENES_END*/).

Run this whenever you add or remove scene folders:
    python3 gen_scenes.py
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")
# folder name on disk -> display name
DATASETS = [("RE10k", "RE10K"), ("ACID", "ACID")]

scenes = []
for dirname, display in DATASETS:
    base = os.path.join(ASSETS, dirname)
    if not os.path.isdir(base):
        continue
    ids = sorted(d for d in os.listdir(base)
                 if os.path.isdir(os.path.join(base, d)) and not d.startswith("."))
    n = 0
    for sid in ids:
        sdir = os.path.join(base, sid)
        if os.path.exists(os.path.join(sdir, "context.png")) and \
           os.path.exists(os.path.join(sdir, "rendered.png")):
            n += 1
            scenes.append({"ds": display, "dir": dirname, "id": sid,
                           "label": f"{display} · Scene {n}"})

# write manifest
with open(os.path.join(ASSETS, "scenes.json"), "w") as f:
    json.dump(scenes, f, indent=2)

# update inline fallback in index.html
idx = os.path.join(ROOT, "index.html")
html = open(idx, encoding="utf-8").read()
arr = "[\n" + ",\n".join(json.dumps(s, ensure_ascii=False) for s in scenes) + "\n]"
block = "/*SCENES_START*/" + arr + "/*SCENES_END*/"
html = re.sub(r"/\*SCENES_START\*/.*?/\*SCENES_END\*/",
              lambda m: block, html, flags=re.S)
open(idx, "w", encoding="utf-8").write(html)

print(f"{len(scenes)} scenes -> assets/scenes.json and index.html updated")
for s in scenes:
    print("  ", s["label"], s["id"])
