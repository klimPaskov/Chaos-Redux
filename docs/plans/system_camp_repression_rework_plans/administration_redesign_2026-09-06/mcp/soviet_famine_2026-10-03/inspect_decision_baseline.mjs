import { createRequire } from 'node:module';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const client=new Client({name:'soviet-famine-decision-baseline-inspect',version:'1'});
client.registerCapabilities({tasks:{list:{},cancel:{},requests:{tools:{call:{}}}}});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});
await client.connect(transport);
const source={path:'common/decisions/camp_repression_major_country_decisions.txt',snapshotPath:'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03/before_camp_repression_major_country_decisions.txt',expectedSourceHash:'0a5fe8c6b52f7137f037077c91804115cb07f6d4eae74c077a8d8fafda34a016',identifier:'sov_emergency_famine_relief'};
const args={workspaceId:runtime.workspaceId,adapter:'decision_ai_will_do',source,candidatePool:['sov_emergency_famine_relief']};
let last='';
try {
 console.log('starting baseline decision inspect');
 const stream=client.experimental.tasks.callToolStream({name:'hoi4.probability_inspect',arguments:args},undefined,{task:{ttl:86400000},timeout:180000});
 for await (const message of stream) {
  if(message.type==='taskCreated') { await writeFile(path.join(evidence,'baseline-decision-inspect-task.json'),JSON.stringify({task:message.task,source,args},null,2)); console.log('TASK_CREATED',JSON.stringify(message.task)); }
  else if(message.type==='taskStatus') { const next=JSON.stringify({status:message.task.status,statusMessage:message.task.statusMessage,lastUpdatedAt:message.task.lastUpdatedAt}); if(next!==last) {last=next; await writeFile(path.join(evidence,'baseline-decision-inspect-task-status.json'),next); console.log('TASK_STATUS',next);} }
  else if(message.type==='result') { await writeFile(path.join(evidence,'baseline-decision-probability-inspect.json'),JSON.stringify(message.result,null,2)); console.log('TASK_RESULT',JSON.stringify({isError:message.result.isError??false,structuredContent:message.result.structuredContent??null,content:message.result.content},null,2)); }
  else if(message.type==='error') { await writeFile(path.join(evidence,'baseline-decision-probability-inspect-error.txt'),String(message.error?.stack??message.error)); console.error('TASK_ERROR',message.error?.stack??message.error); }
 }
} catch(error) { await writeFile(path.join(evidence,'baseline-decision-probability-inspect-error.txt'),String(error?.stack??error)); console.error('CLIENT_ERROR',error?.stack??error); process.exitCode=1; }
finally { await client.close(); }

