"""Read-only exact-wrapper handshake/EOF timing probe; no model calls."""
import json
import queue
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'.tools/3d_pipeline'))
from lib import mcp_stdio
from blender_client import BlenderAdapterClient


def probe(command, timeout=60):
    output, errors, events=[],[],queue.Queue()
    job=mcp_stdio._create_windows_kill_job()
    process=None
    def reader(stream, target, notify=False):
        for line in stream:
            target.append(line)
            if notify:
                for message in mcp_stdio._json_lines(line): events.put(message)
        if notify: events.put(None)
    started=time.monotonic()
    try:
        process=subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',errors='replace',cwd=str(ROOT))
        mcp_stdio._assign_windows_kill_job(job,process)
        threads=[threading.Thread(target=reader,args=(process.stdout,output,True),daemon=True),threading.Thread(target=reader,args=(process.stderr,errors),daemon=True)]
        for thread in threads: thread.start()
        def send(value):
            process.stdin.write(json.dumps(value,separators=(',',':'))+'\n');process.stdin.flush()
        def receive(identifier):
            while True:
                remaining=started+timeout-time.monotonic()
                if remaining<=0: raise TimeoutError('No response before deadline')
                value=events.get(timeout=remaining)
                if value is None: raise RuntimeError('EOF before matching response')
                if value.get('id')==identifier:
                    if 'error' in value: raise RuntimeError(str(value['error']))
                    return value
        send({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'chaos-redux-stdio-probe','version':'1.0.0'}}})
        initialized=receive(1)
        send({'jsonrpc':'2.0','method':'notifications/initialized'})
        send({'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})
        response=receive(2)
        process.stdin.close()
        process.wait(timeout=10)
        for thread in threads: thread.join(timeout=2)
        assert process.returncode==0
        return {'seconds':time.monotonic()-started,'tool_count':len(response['result']['tools']),'tool_names':[t['name'] for t in response['result']['tools']],
            'initialized_before_request':True,'response_before_stdin_eof':True,'exit_code':process.returncode,'server_info':initialized['result']['serverInfo']}
    finally:
        mcp_stdio._close_windows_handle(job)
        if process is not None and process.poll() is None:
            process.kill();process.wait(timeout=5)


if __name__=='__main__':
    client=BlenderAdapterClient(ROOT)
    command=['cmd.exe','/d','/c','call',str(client.wrapper)]
    result={'command':command,'adapter_source_changed':False,'attempts':[probe(command) for _ in range(6)]}
    path=ROOT/'.tools/3d_pipeline/reports/adapter_stdio_1_10_47_response_probe.json'
    path.write_bytes((json.dumps(result,indent=2)+'\n').encode())
    print(json.dumps({'report':str(path),'counts':[r['tool_count'] for r in result['attempts']]},indent=2))
