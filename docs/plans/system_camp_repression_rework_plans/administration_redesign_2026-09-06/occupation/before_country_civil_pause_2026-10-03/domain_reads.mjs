import {createRequire} from 'node:module';import {readFile,writeFile} from 'node:fs/promises';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools'; const require=createRequire(pkg+'/package.json'); const {Client}=require('@modelcontextprotocol/sdk/client/index.js'); const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const root='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation'; const out=root+'/before_country_civil_pause_2026-10-03';const c=new Client({name:'country-civil-provenance-readonly',version:'1'});const t=new StdioClientTransport({command:process.execPath,args:['C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js','--config',root+'/origin_ambiguity_mcp_2026-10-03/config.json'],cwd:pkg,stderr:'pipe'});t.stderr?.on('data',d=>process.stderr.write(d));
try{
 await c.connect(t);const runs=[];
 async function call(name,args){try{const result=await c.callTool({name,arguments:{workspaceId:'camp_origin_architecture_oct3',...args}},undefined,{timeout:30000});runs.push({name,args,result});console.log(JSON.stringify({name,status:result.structuredContent?.status,code:result.structuredContent?.code,isError:result.isError}));return result.structuredContent;}catch(e){runs.push({name,args,error:String(e),code:e.code});console.log(JSON.stringify({name,error:String(e)}));}finally{await writeFile(out+'/domain_reads.json',JSON.stringify(runs,null,2));}}
 const search=await call('hoi4.reference_search',{query:'add_tech_bonus',sources:['game_doc','wiki'],limit:3});
 for(const ref of (search?.data?.results??[]).slice(0,2))await call('hoi4.reference_read',{id:ref.id,revision:ref.revision,startLine:ref.startLine,maxLines:40});
 for(const bounds of [4,1]){const result=await call('hoi4.event_inspect',{mode:'trace',selector:{kind:'file',sourcePath:'events/camp_administration_country_events.txt'},direction:'downstream',maxDepth:1,maxNodes:bounds,maxEdges:bounds,expandHelpers:false});if(result)break;}
 for(const bounds of [4,1]){const result=await call('hoi4.tech_inspect',{mode:'bonus_coverage',categoryId:'engineers_tech',maxDepth:1,maxNodes:bounds,includeSubTechnologies:false});if(result)break;}
}finally{await c.close();}

