#!/usr/bin/env python3
"""Update data.json. Usage:
  update.py add-follow <regular|professionals> <handle> [name]
  update.py accepted <handle>     (they followed back / accepted)
  update.py text <handle>         (a text was sent)
  update.py chat <handle>         (mark active chat)
  update.py flag <handle> "note" [name]   (good prospect)
  update.py show
"""
import json, sys, os, datetime
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
d = json.load(open(P))
today = datetime.date.today().isoformat()
h = lambda s: s.strip().lstrip("@").lower()

def find(handle):
    for t, tr in d["tracks"].items():
        for p in tr["people"]:
            if p["handle"] == handle: return t, p
    sys.exit(f"unknown handle {handle}; add-follow first")

a = sys.argv[1:]
if not a: sys.exit(__doc__)
c = a[0]
if c == "add-follow":
    t, hd = a[1], h(a[2])
    if t not in d["tracks"]: sys.exit("track must be regular or professionals")
    for tr in d["tracks"].values():
        if any(p["handle"] == hd for p in tr["people"]): sys.exit("already tracked")
    d["tracks"][t]["people"].append({"handle": hd, "name": a[3] if len(a) > 3 else "", "followed": today, "accepted": None, "texts": [], "chat": False})
elif c in ("accepted", "text", "chat"):
    t, p = find(h(a[1]))
    if c == "accepted": p["accepted"] = p["accepted"] or today
    elif c == "text": p["texts"].append(today)
    else: p["chat"] = True
elif c == "flag":
    t, p = find(h(a[1]))
    pr = d["tracks"][t]["prospects"]
    name = a[3] if len(a) > 3 else p.get("name", "")
    pr[:] = [x for x in pr if x["handle"] != p["handle"]]
    pr.append({"handle": p["handle"], "name": name, "date": today, "note": a[2]})
elif c == "show":
    for t, tr in d["tracks"].items():
        print(t, "follows", len(tr["people"]), "accepted", sum(1 for p in tr["people"] if p["accepted"]),
              "texts", sum(len(p["texts"]) for p in tr["people"]), "chats", sum(1 for p in tr["people"] if p["chat"]), "prospects", len(tr["prospects"]))
    sys.exit()
else: sys.exit(__doc__)
d["updated"] = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
json.dump(d, open(P, "w"), indent=2)
print("ok")
