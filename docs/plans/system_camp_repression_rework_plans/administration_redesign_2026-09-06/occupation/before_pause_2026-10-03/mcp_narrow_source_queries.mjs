import {createRequire} from 'node:module';
import {readFile,writeFile} from 'node:fs/promises';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(pkg+'/package.json');
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const root='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation';
const client=new Client({name:'camp-origin-owner-integration-readonly',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:[pkg+'/dist/bin/stdio.js','--config',root+'/origin_ambiguity_mcp_2026-10-03/config.json'],cwd:pkg,stderr:'pipe'});
transport.stderr?.on('data',d=>process.stderr.write(d));
try{
 await client.connect(transport);
 const list=await client.listTools();
 const evidence={server:client.getServerVersion(),sdk:JSON.parse(await readFile(pkg+'/package.json','utf8')).dependencies['@modelcontextprotocol/sdk'],schema:list.tools.find(x=>x.name==='hoi4.source_lookup'),attempts:[]};
 for(const symbol of ['camp_occ_reconcile_external_population','camp_admin_refresh_capacity']){
  for(const maxLines of [12,1]){
   const args={workspaceId:'camp_origin_architecture_oct3',symbol,kind:'scripted_effect',includeReferences:false,maxDefinitions:1,maxReferences:0,maxLines};
   try{const result=await client.callTool({name:'hoi4.source_lookup',arguments:args},undefined,{timeout:30000});evidence.attempts.push({args,result});console.log(JSON.stringify({symbol,maxLines,result:result.structuredContent?.code,isError:result.isError}));if(!result.isError)break;}
   catch(e){evidence.attempts.push({args,error:String(e),code:e.code,timeout:e.data});console.log(JSON.stringify({symbol,maxLines,error:String(e)}));}
   await writeFile(root+'/before_pause_2026-10-03/mcp_narrow_source_queries.json',JSON.stringify(evidence,null,2));
  }
 }
 await writeFile(root+'/before_pause_2026-10-03/mcp_narrow_source_queries.json',JSON.stringify(evidence,null,2));
}finally{await client.close();}
