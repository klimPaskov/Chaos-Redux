import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { Client } from 'file:///C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js';
import { StdioClientTransport } from 'file:///C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js';
const out = path.dirname(fileURLToPath(import.meta.url));
const root = 'C:\\Users\\klimp\\OneDrive\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\chaos_redux';
const client = new Client({ name:'event027-doctrine-readonly-resume', version:'2026-10-07' }, { capabilities:{} });
const transport = new StdioClientTransport({command:'C:\\Program Files\\nodejs\\node.exe',args:['C:\\Users\\klimp\\AppData\\Roaming\\npm\\node_modules\\hoi4-agent-tools\\dist\\bin\\stdio.js'],cwd:root,env:{HOI4_AGENT_CONFIG:'C:\\Users\\klimp\\AppData\\Roaming\\hoi4-agent-tools\\config.json',CHAOS_REDUX_MOD_ROOT:root},stderr:'pipe'});
const save=(name,data)=>fs.writeFileSync(path.join(out,name+'.json'),JSON.stringify(data,null,2));
await client.connect(transport);
const metadata={version:client.getServerVersion(),capabilities:client.getServerCapabilities(),clientCapabilities:{},transport:'separate read-only SDK stdio connection, windowsHide=true in installed transport',pid:transport.pid};
save('live_connection_1517',metadata); console.log(JSON.stringify(metadata));
const listing=await client.listTools(); save('live_schemas_1517',listing);
console.log('Saved live schemas for '+listing.tools.length+' routes');
save('live_resource_templates_1517',await client.listResourceTemplates());
save('live_resources_1517',await client.listResources());
try{save('server_status_1545',await client.readResource({uri:'hoi4-agent://server/status'}));}catch(error){save('server_status_error_1545',{message:String(error)});}
async function call(label,name,args,timeout=60000){
 const request={name,arguments:args};save('request_'+label,request);const started=Date.now();
 try{const result=await client.callTool(request,undefined,{timeout});save('result_'+label,{elapsedMs:Date.now()-started,result});console.log(label+' returned '+(result.structuredContent?.code??'content'));return result;}
 catch(error){save('error_'+label,{message:String(error),elapsedMs:Date.now()-started});console.log(label+' '+String(error));return null;}
}
await call('context_1545','hoi4.reference_context',{surface:'technology',question:'grand doctrines subdoctrines native mastery banked progress add_mastery set_sub_doctrine',limit:6});
await call('mastery_search_1545','hoi4.reference_search',{query:'add_mastery',limit:6});
await call('exact_validate_1545','hoi4.script_validate',{path:'common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt',kind:'effect',scope:'country',limit:32});
const domains=[['army','new_mobile_warfare','land'],['navy','new_fleet_in_being','naval'],['air','new_strategic_destruction','air'],['sf','special_forces_quantity','special_forces'],['chaos','chaos_warfare','land']];
for(const [label,id,folder] of domains){
 await call('inspect_'+label+'_1545','hoi4.tech_inspect',{mode:'explain',technologyId:id,maxNodes:8,maxDepth:1});
 await call('render_'+label+'_1545','hoi4.tech_render',{view:'doctrine',technologyId:id,folderId:folder,maxNodes:24,includeHtml:false});
}
const relativePath='common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt';
const source=execFileSync('git',['show','bf4fa8fea^:'+relativePath],{cwd:root,encoding:'utf8',windowsHide:true,maxBuffer:4000000});
await call('compare_real_guard_revision_1545','hoi4.tech_compare',{proposedSources:[{relativePath,source}],render:false,maxRenderNodes:24});
try{save('server_status_after_1545',await client.readResource({uri:'hoi4-agent://server/status'}));}catch(error){save('server_status_after_error_1545',{message:String(error)});}
await client.close();
