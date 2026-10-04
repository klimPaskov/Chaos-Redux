import {createRequire} from 'node:module';
import {mkdir,writeFile,mkdtemp} from 'node:fs/promises';
import path from 'node:path';
import {tmpdir} from 'node:os';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const mod='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const out=path.join(mod,'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03');
const rt=await mkdtemp(path.join(tmpdir(),'camp-origin-architecture-'));
const storage=path.join(rt,'storage');
for(const p of ['state','storage/artifacts','storage/cache']) await mkdir(path.join(rt,p),{recursive:true});
const cfg={version:1,serverStateRoot:path.join(rt,'state'),storageRoots:[storage],workspaces:[{id:'camp_origin_architecture_oct3',name:'Camp origin containment read-only evidence',root:mod,gameRoot:'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV',artifactRoot:path.join(storage,'artifacts'),cacheRoot:path.join(storage,'cache')}]};
await writeFile(path.join(out,'config.json'),JSON.stringify(cfg,null,2));
const client=new Client({name:'camp-origin-architecture-readonly',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',path.join(out,'config.json')],cwd:pkg,stderr:'pipe'});
transport.stderr?.on('data',d=>process.stderr.write(d));
try {
await client.connect(transport);
const summary=[];
async function call(key,name,args){try{const result=await client.callTool({name,arguments:{workspaceId:'camp_origin_architecture_oct3',...args}},undefined,{timeout:45000});await writeFile(path.join(out,key+'.json'),JSON.stringify({request:{name,args},result},null,2));const data=result.structuredContent??{};summary.push({key,status:data.status,code:data.code,data:data.data,artifacts:data.artifacts,blockers:data.blockers});console.log(JSON.stringify({key,status:data.status,code:data.code,artifacts:data.artifacts,blockers:data.blockers}));return data;}catch(e){const data={key,name,args,error:String(e),code:e.code,data:e.data};summary.push(data);await writeFile(path.join(out,key+'.json'),JSON.stringify(data,null,2));console.log(JSON.stringify(data));}}
const sections=[
['population','7768c2c7f3395810eb04c60fbbcef9cbb6db0b32d8168a3ebacd35e2ce3e1d92','538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda',1168,4],
['scoping','338680a6b2bbd220717fbd8fc7571aabe2c63519431acc3aa41e5e5440df1822','62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4',444,37],
['flags','bb6c6275c19a0ee85057eeb1e04f508b6dccf68ffefaff646276d0a128b3cdcb','62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4',102,25],
['targets','0cf822e7a14ffa87db1496f17fc62e32702d4df813922c50fbe288c58385cbc2','62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4',303,26],
['constants_concept','c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238a9d1f7b355ccd0','884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7',216,7],
['constants_schema','48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68','e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c',1,34],
['target_effect','962e3b81b9bb7a23e31ce037940c39c5c0f187024628cba3fc797cbe6579e510','2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af',6496,9],
['flag_trigger','ce0d60de326c56a95cca74af1dc6f4cc669faefaddb9b5bfa28abb2103ec590e','7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29',4827,16]
];
for(const [key,id,revision,startLine,maxLines] of sections) await call('read_'+key,'hoi4.reference_read',{id,revision,startLine,maxLines});
for(const symbol of ['camp_occ_reconcile_external_population','camp_admin_refresh_capacity','apply_exact_state_civilian_population_loss']) await call('source_'+symbol,'hoi4.source_lookup',{symbol,includeReferences:false,maxLines:80});
await call('events','hoi4.event_inspect',{mode:'scan',selector:{kind:'file',sourcePath:'events/camp_administration_country_events.txt'},expandHelpers:false,maxNodes:80,maxEdges:100});
await call('decision','hoi4.decision_inspect',{mode:'inspect',id:'sov_release_prisoners_for_military_service'});
await call('gui','hoi4.gui_inspect',{windowName:'repression_ledger_window'});
await writeFile(path.join(out,'bounded_summary.json'),JSON.stringify(summary,null,2));} finally {await client.close();}

