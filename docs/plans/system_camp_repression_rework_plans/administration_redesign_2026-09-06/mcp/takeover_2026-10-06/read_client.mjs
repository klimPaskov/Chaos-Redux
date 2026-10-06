// Read-only direct installed MCP client. Keeps the existing runtime config.
import {createRequire} from 'node:module';
import {readFile, writeFile} from 'node:fs/promises';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(pkg+'/package.json');
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const repo=process.cwd();
const config=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03/config.json';
const client=new Client({name:'camp-takeover-source-review',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:['C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js','--config',config],cwd:pkg,stderr:'pipe'});
try {
 await client.connect(transport);
 if(process.argv[2]==='schemas') {
  const listing=await client.listTools();
  const tools=listing.tools.filter(t=>/^hoi4\.(reference_|source_lookup|gui_|event_|script_validate)/.test(t.name));
  const result={server:client.getServerVersion(),capabilities:client.getServerCapabilities(),tools};
  await writeFile(process.argv[3],JSON.stringify(result,null,2));
  console.log(JSON.stringify({server:result.server,tools:tools.map(t=>t.name)}));
 } else {
  const requests=JSON.parse(await readFile(process.argv[2],'utf8'));
  for(const request of requests) {
   try {
    const result=await client.callTool({name:request.name,arguments:request.arguments},undefined,{timeout:60000});
    await writeFile(request.output,JSON.stringify(result,null,2));
    console.log(JSON.stringify({name:request.name,output:request.output,isError:result.isError,status:result.structuredContent?.status,code:result.structuredContent?.code,blockers:result.structuredContent?.blockers,artifacts:result.structuredContent?.artifacts}));
   } catch(error) {
    await writeFile(request.output,JSON.stringify({name:request.name,error:String(error)},null,2));
    console.log(JSON.stringify({name:request.name,error:String(error)}));
   }
  }
 }
} finally {await client.close();}
