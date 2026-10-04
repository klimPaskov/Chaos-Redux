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
const call=async(key,name,args)=>{try{const result=await client.callTool({name,arguments:{workspaceId:'camp_origin_architecture_oct3',...args}},undefined,{timeout:45000});await writeFile(path.join(out,key+'.json'),JSON.stringify({request:{name,args},result},null,2));console.log(JSON.stringify({key,isError:result.isError,status:result.structuredContent?.status,code:result.structuredContent?.code,text:result.isError?result.content:null}));}catch(e){await writeFile(path.join(out,key+'.json'),JSON.stringify({request:{name,args},error:String(e)},null,2));console.log(JSON.stringify({key,error:String(e)}));}};
await call('decision_with_scenario','hoi4.decision_inspect',{mode:'inspect',id:'sov_release_prisoners_for_military_service',scenarios:[{id:'sov_release_declared_source_inspection',actor:'SOV',date:'1944.10.1',state:{forced_labor_quota:20,camp_admin_country_last_released_k:0,political_power:100},flags:['camp_admin_initialized'],closedFlags:false}]});
const {readFile}=await import('node:fs/promises');
const fixture=JSON.parse(await readFile(path.join(mod,'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/after/records_1944_10_01_source_sensitivity_1920.json'),'utf8'));
await call('gui_with_scenario','hoi4.gui_inspect',{windowName:'repression_ledger_window',scenario:fixture,generatedScenarios:{enabled:false}});} finally {await client.close();}

