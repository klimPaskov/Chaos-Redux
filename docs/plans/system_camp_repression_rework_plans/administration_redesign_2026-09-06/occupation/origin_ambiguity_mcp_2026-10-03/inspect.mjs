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
const list=await client.listTools();
const summary=[];
async function call(key,name,args){const result=await client.callTool({name,arguments:{workspaceId:'camp_origin_architecture_oct3',...args}},undefined,{timeout:120000});await writeFile(path.join(out,key+'.json'),JSON.stringify({request:{name,args},result},null,2));const data=result.structuredContent??{};summary.push({key,status:data.status,code:data.code,data:data.data,artifacts:data.artifacts,blockers:data.blockers});console.log(JSON.stringify({key,status:data.status,code:data.code,artifacts:data.artifacts,blockers:data.blockers}));return data;}
await call('context','hoi4.reference_context',{surface:'general',question:'State cohort observation, variable arrays, state flags, event targets, scope and script constants',limit:24});
for(const q of ['state_population_k','add_state_population','has_state_flag','save_event_target_as','script constants']) await call('search_'+q.replaceAll(' ','_'),'hoi4.reference_search',{query:q,limit:6,sources:['game_doc','wiki','script_doc']});
await call('map_states','hoi4.map_inspect',{stateIds:[87,88],lookupOnly:true,includeOverview:false});
for(const symbol of ['camp_occ_reconcile_external_population','camp_admin_refresh_capacity','apply_exact_state_civilian_population_loss']) await call('source_'+symbol,'hoi4.source_lookup',{symbol,includeReferences:false,maxLines:80});
await call('events','hoi4.event_inspect',{mode:'scan',selector:{kind:'file',sourcePath:'events/camp_repression_administration.txt'},expandHelpers:false,maxNodes:80,maxEdges:100});
await call('decision','hoi4.decision_inspect',{mode:'inspect',id:'sov_release_prisoners_for_military_service'});
await call('gui','hoi4.gui_inspect',{windowName:'repression_ledger_window'});
await writeFile(path.join(out,'summary.json'),JSON.stringify(summary,null,2));} finally {await client.close();}

