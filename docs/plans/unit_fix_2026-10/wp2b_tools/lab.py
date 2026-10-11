"""Tiny Blender Lab socket client: python lab.py file.py  (or - for stdin). Prints stdout/result."""
import json, socket, sys
import os
PORT = int(os.environ.get("LABPORT", "9877"))
def run(code, timeout=1500):
    req = json.dumps({"type": "execute", "code": code, "strict_json": False}) + "\0"
    with socket.socket() as s:
        s.settimeout(timeout); s.connect(("127.0.0.1", PORT)); s.sendall(req.encode())
        buf = bytearray()
        while b"\0" not in buf:
            c = s.recv(65536)
            if not c: break
            buf.extend(c)
    return json.loads(bytes(buf).partition(b"\0")[0].decode())
if __name__ == "__main__":
    code = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    r = run(code)
    for k in ("stdout", "stderr"):
        if r.get(k): print(r[k])
    if r.get("status") != "ok": print("ERROR:", r.get("message"))
    else: print(json.dumps(r.get("result"), indent=1, default=repr)[:20000])
