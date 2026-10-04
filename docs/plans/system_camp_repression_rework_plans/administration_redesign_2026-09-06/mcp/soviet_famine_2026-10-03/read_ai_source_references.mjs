import { createRequire } from 'node:module';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const client=new Client({name:'soviet-famine-reference-context',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});
await client.connect(transport);
async function save(name,tool,args){const result=await client.callTool({name:tool,arguments:{workspaceId:runtime.workspaceId,...args}},undefined,{timeout:60000});await writeFile(path.join(evidence,name+'-'+name.replaceAll('.','-')+'.json'),JSON.stringify(result,null,2));console.log(name,result.isError?'error':'ok',JSON.stringify(result.structuredContent?.data??result.structuredContent??{}).slice(0,1800));return result;}
try{
 await save('reference_context_decision','hoi4.reference_context',{surface:'decision',question:'Decision AI willingness score, native political-power costs, custom cost gates, and cost eligibility cadence.',limit:12});
 await save('reference_search_ai_chance','hoi4.reference_search',{query:'ai_chance proportional probability default 1 d100 event options',sources:['wiki'],limit:8});
 await save('reference_read_ai_modding_chance','hoi4.reference_read',{id:'ab2b62a1e95fe5c84560ceedca6723cea6918faf69b08fd399709a2afbf8efe6',revision:'917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818',startLine:26,maxLines:12});
 await save('reference_search_decision_ai','hoi4.reference_search',{query:'ai_will_do decision base score',sources:['wiki','game_doc'],limit:10});
}catch(error){console.error(error?.stack??error);process.exitCode=1;}finally{await client.close();}

