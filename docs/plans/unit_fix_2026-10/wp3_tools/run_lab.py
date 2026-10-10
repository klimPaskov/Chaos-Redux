"""python run_lab.py script.py 'json CFG' -> runs script in the Lab with CFG injected"""
import sys, json
sys.path.insert(0, r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.tmp/wp3_zombies")
import lab
code = "CFG = json.loads(%r)\n" % (sys.argv[2] if len(sys.argv) > 2 else '{}') 
code = "import json\n" + code + open(sys.argv[1], encoding='utf-8').read()
r = lab.run(code)
for k in ("stdout", "stderr"):
    if r.get(k): print(r[k])
if r.get("status") != "ok": print("ERROR:", r.get("message"))
else: print(json.dumps(r.get("result"), indent=1, default=repr)[:12000])
