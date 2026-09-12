"""Exact live adapter stdio discovery/health and immutable checkpoint inspection."""
import hashlib
import json
import sys
import time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'.tools/3d_pipeline'))
from blender_client import BlenderAdapterClient
import blender_client
from lib.mcp_stdio import call_stdio


def main():
    base=ROOT/'.tools/3d_pipeline'
    config=json.loads((base/'config/blender_hoi4_adapter.json').read_text())
    lock=json.loads((base/'config/dependencies.lock.json').read_text())['routes']['blender_hoi4_adapter']
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()
    assert config['adapter_version']==lock['version']
    assert all(sha(ROOT/p)==value for p,value in lock['source_sha256'].items())
    client=BlenderAdapterClient(ROOT)
    command=['cmd.exe','/d','/c','call',str(client.wrapper)]
    result={'adapter_version':lock['version'],'source_sha256':lock['source_sha256'],'config_sha256':sha(base/'config/blender_hoi4_adapter.json'),
        'lock_sha256':sha(base/'config/dependencies.lock.json'),'transport_sha256':sha(base/'lib/mcp_stdio.py'),'wrapper_sha256':sha(client.wrapper),
        'command':command,'tools_list':[],'health':[],'provider_calls':False,'checkpoint_saved':False}
    for index in range(6):
        lifecycle={};started=time.monotonic()
        response=call_stdio(command,list_tools=True,timeout_seconds=60,cwd=ROOT,lifecycle_receipt=lifecycle)
        names=sorted(tool['name'] for tool in response['tools'])
        assert names==sorted('chaosx_blender_hoi4_'+op for op in lock['operations'])
        assert lifecycle['exchange']=='blender_response_drained' and lifecycle['response_id_before_stdin_eof']==2 and lifecycle['surviving_process_ids']==[]
        result['tools_list'].append({'index':index+1,'tool_count':len(names),'schema_sha256':hashlib.sha256(json.dumps(response,sort_keys=True,separators=(',',':')).encode()).hexdigest().upper(),
            'seconds':time.monotonic()-started,'lifecycle':lifecycle})
        print('TOOLS_LIST_PASS',index+1,len(names),flush=True)
    result['client_exchanges']=[]
    original_call=blender_client.call_stdio
    def record_call(*args,**kwargs):
        lifecycle={}
        kwargs['lifecycle_receipt']=lifecycle
        row={'tool':kwargs.get('tool'),'lifecycle':lifecycle}
        result['client_exchanges'].append(row)
        value=original_call(*args,**kwargs)
        row['response_received']=True
        return value
    blender_client.call_stdio=record_call
    for index in range(3):
        value=client.health('mutant_zombies')
        result['health'].append(value)
        print('HEALTH_PASS',index+1,flush=True)
    source=Path(config['job_overrides']['mutant_zombies'])/'blender/checkpoints/05_v15_winding_v1_attack.blend'
    expected='138DE96AC6F0957321768ECB00805091EE7E113F176A91DD46FC0A4B3F5720A8'
    assert sha(source)==expected
    value=client.call('chaosx_blender_hoi4_inspect_scene',{'job_id':'mutant_zombies','blend_rel':'blender/checkpoints/05_v15_winding_v1_attack.blend',
        'render_previews':False,'expected_source_sha256':expected})
    assert sha(source)==expected
    assert len(result['client_exchanges'])==4
    assert all(row.get('response_received') and row['lifecycle']['response_id_before_stdin_eof']==2 and not row['lifecycle']['surviving_process_ids'] for row in result['client_exchanges'])
    result['inspection']={'source_sha256_before':expected,'source_sha256_after':sha(source),'result':value}
    result['status']='pass_no_checkpoint_save'
    path=base/'reports/adapter_stdio_1_10_48_live.json'
    path.write_bytes((json.dumps(result,indent=2)+'\n').encode())
    print('LIVE_STDIO_PASS',path,flush=True)


if __name__=='__main__':main()
