"""Bounded read-only Event 24 MCP session using the installed stdio route."""
import base64
import json
import os
import queue
import subprocess
import sys
import threading
import time

sys.path.insert(0, os.path.join(os.getcwd(), ".tools", "3d_pipeline", "lib"))
from mcp_stdio import (_create_windows_kill_job, _assign_windows_kill_job,
                       _close_windows_handle, _windows_job_process_ids,
                       _wait_windows_pids_exit)

READ_ONLY = {
    "hoi4.reference_context", "hoi4.reference_search", "hoi4.reference_read",
    "hoi4.source_lookup", "hoi4.script_validate", "hoi4.event_inspect",
    "hoi4.decision_inspect",
    "hoi4.event_render", "hoi4.event_compare", "hoi4.probability_inspect",
    "hoi4.probability_evaluate", "hoi4.probability_sweep",
    "hoi4.probability_compare", "hoi4.probability_render",
    "hoi4.probability_simulate", "hoi4.probability_sequence",
}
request = json.loads(base64.b64decode(sys.argv[1]))
timeout = min(55, request.get("timeoutSeconds", 45))
job = _create_windows_kill_job()
environment = os.environ.copy()
environment["CHAOS_REDUX_MOD_ROOT"] = os.getcwd()
process = subprocess.Popen(
    ["cmd.exe", "/d", "/c", "hoi4-agent-tools.cmd"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    text=True, encoding="utf-8", env=environment,
    creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
)
_assign_windows_kill_job(job, process)
messages = queue.Queue()
diagnostics = []

def drain_stdout():
    for line in process.stdout:
        try:
            messages.put(json.loads(line))
        except json.JSONDecodeError:
            pass

def drain_stderr():
    for line in process.stderr:
        diagnostics.append(line)

threading.Thread(target=drain_stdout, daemon=True).start()
threading.Thread(target=drain_stderr, daemon=True).start()

def send(message):
    process.stdin.write(json.dumps(message) + "\n")
    process.stdin.flush()

def receive(identifier):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            response = messages.get(timeout=max(.01, deadline - time.monotonic()))
        except queue.Empty as error:
            raise TimeoutError(f"MCP id {identifier} returned no result after {timeout}s") from error
        if response.get("id") == identifier:
            return response
    raise TimeoutError("No matching MCP response")

try:
    send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2024-11-05", "capabilities": {},
        "clientInfo": {"name": "chaosx-event24-readonly", "version": "1"}}})
    initialization = receive(1)
    print(json.dumps({"initialize": initialization}, ensure_ascii=False), flush=True)
    send({"jsonrpc": "2.0", "method": "notifications/initialized"})
    for identifier, call in enumerate(request.get("calls", []), 2):
        if call.get("method") == "tools/list":
            params = {}
        else:
            if call["name"] not in READ_ONLY:
                raise ValueError("Only read-only HOI4 tools are permitted")
            params = {"name": call["name"], "arguments": call.get("arguments", {})}
        method = call.get("method", "tools/call")
        send({"jsonrpc": "2.0", "id": identifier, "method": method, "params": params})
        response = receive(identifier)
        if method == "tools/list":
            names = request.get("schemaNames", [])
            response = {"tools": [{"name": tool["name"], "inputSchema": tool["inputSchema"]}
                for tool in response.get("result", {}).get("tools", [])
                if not names or tool["name"] in names]}
        print(json.dumps({"call": call.get("name", method), "response": response},
                         ensure_ascii=False), flush=True)
except Exception as error:
    print(json.dumps({"error": type(error).__name__ + ": " + str(error),
                      "stderrTail": "".join(diagnostics)[-1600:]}), flush=True)
finally:
    owned = _windows_job_process_ids(job)
    _close_windows_handle(job)
    if process.poll() is None:
        process.wait(timeout=5)
    print(json.dumps({"ownedSessionSurvivors": _wait_windows_pids_exit(owned)}), flush=True)
