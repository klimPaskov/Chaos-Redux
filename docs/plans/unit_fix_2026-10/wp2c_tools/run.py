"""python run.py script.py '{json cfg}'  -> run script in Lab with CFG injected"""
import sys, json
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import lab
cfg = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
code = "import json\nCFG=json.loads(%r)\n" % json.dumps(cfg) + open(sys.argv[1], encoding='utf-8').read()
r = lab.run(code, timeout=3000)
for k in ("stdout","stderr"):
    if r.get(k): print(r[k])
if r.get("status") != "ok": print("ERROR:", r.get("message"))
else: print(json.dumps(r.get("result"), default=repr)[:int(sys.argv[3]) if len(sys.argv)>3 else 6000])
