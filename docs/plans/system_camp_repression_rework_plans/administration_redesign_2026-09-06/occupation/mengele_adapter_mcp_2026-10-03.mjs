import {createRequire} from 'node:module';
import {mkdir, readFile, writeFile} from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const installed='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools';
const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const base='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_adapter_mcp_2026-10-03';
await mkdir(base,{recursive:true});
const runtime=JSON.parse(await readFile('docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03/probability-runtime.json','utf8'));
const client=new Client({name:'mengele-exact-custody-adapter',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(installed,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:installed,stderr:'pipe'});
try {
 await client.connect(transport);
 const list=await client.listTools();
 await writeFile(path.join(base,'server.json'),JSON.stringify({version:client.getServerVersion(),capabilities:client.getServerCapabilities(),tools:list.tools},null,2));
 const workspaceId=runtime.workspaceId;
 const requests=[
  ...(process.argv.includes('--narrow') ? [
  ['source_lookup_retry',{symbol:'germany_mengele_register_experiment_deaths',kind:'scripted_effect',includeReferences:false,maxLines:12,maxDefinitions:1,workspaceId},'hoi4.source_lookup'],
  ['event_inspect_final_narrow',{mode:'trace',selector:{kind:'source',sourcePath:'common/scripted_effects/germany_mengele_effects.txt',line:181},expandHelpers:false,maxDepth:1,maxNodes:1,maxEdges:1,workspaceId},'hoi4.event_inspect'],
  ] : [
  ['reference_context_complete',{surface:'event',question:'state custody mortality scripted effect, arrays, temporary variable lifetime and scope',limit:20,workspaceId},'hoi4.reference_context'],
  ['reference_read_loop',{id:'592312368eed3983c8457abc460f8ed8fe083fedaebad1bde9c7421f1506a376',revision:'2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af',maxLines:20,workspaceId},'hoi4.reference_read'],
  ['reference_read_wiki_arrays',{id:'c3969d9492489ab0f70fb860a54b9a1aaa1f80fc78012fe3ffbc13dc4c857e72',revision:'62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4',startLine:1205,maxLines:40,workspaceId},'hoi4.reference_read'],
  ['source_lookup',{symbol:'germany_mengele_register_experiment_deaths',kind:'scripted_effect',includeReferences:false,maxLines:60,maxDefinitions:1,workspaceId},'hoi4.source_lookup'],
  ['event_inspect_retry',{mode:'trace',selector:{kind:'event',eventId:'germany_mengele.10'},expandHelpers:false,maxDepth:1,maxNodes:3,maxEdges:5,workspaceId},'hoi4.event_inspect'],
  ['map_inspect_retry',{lookupOnly:true,stateIds:[88],includeOverview:false,queryLimit:1,workspaceId},'hoi4.map_inspect'],
  ]),
 ];
 for (const [label,args,name] of requests) {
  console.log('START',label);
  try {
   const result=await client.callTool({name,arguments:args},undefined,{timeout:45000});
   await writeFile(path.join(base,label+'.json'),JSON.stringify(result,null,2));
   console.log('RESULT',label,JSON.stringify(result.structuredContent?.status??result.isError??'returned'));
  } catch(e) {await writeFile(path.join(base,label+'-error.txt'),String(e.stack??e)); console.log('ERROR',label,String(e));}
 }
} finally {await client.close();}
