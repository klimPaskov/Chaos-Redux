import { createRequire } from 'node:module';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const plan='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06';
const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const fixture=JSON.parse(await readFile(path.join(plan,'ai_evidence/soviet_famine_shortfall_scenario_set_2026-10-03.json'),'utf8'));
const scenarios=fixture.scenarioSet;
const beforeRoot='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const afterEventHash='40740e555c4ef9ab4b293b1fe821f7b930f10654ad76ba548bbcec4fe0e852d1';
const beforeEventHash='773c927aee19767055da26922c72b88aaa30335b751ec8b58423615081937a31';
const pools=[
 {tag:'warning',eventId:'soviet_gulag.1',beforeIds:fixture.candidatePools.before['soviet_gulag.1'],afterIds:fixture.candidatePools.after['soviet_gulag.1']},
 {tag:'crisis',eventId:'soviet_gulag.2',beforeIds:fixture.candidatePools.before['soviet_gulag.2'],afterIds:fixture.candidatePools.after['soviet_gulag.2']}
];
const requests=[];
for(const p of pools){
 requests.push(['before-event-'+p.tag+'-probability-evaluate',{workspaceId:runtime.workspaceId,adapter:'event_option_ai_chance',source:{path:'events/soviet_gulag.txt',snapshotPath:beforeRoot+'/before_soviet_gulag.txt',expectedSourceHash:beforeEventHash,identifier:p.beforeIds[0]},candidatePool:p.beforeIds,scenarioSet:scenarios,metrics:['conditional_probability','raw_value'],outputs:['json','ranking','matrix','waterfall','unresolved'],refresh:true}]);
 requests.push(['after-event-'+p.tag+'-probability-evaluate',{workspaceId:runtime.workspaceId,adapter:'event_option_ai_chance',source:{path:'events/soviet_gulag.txt',snapshotPath:beforeRoot+'/after_soviet_gulag.txt',expectedSourceHash:afterEventHash,identifier:p.afterIds[0]},candidatePool:p.afterIds,scenarioSet:scenarios,metrics:['conditional_probability','raw_value'],outputs:['json','ranking','matrix','waterfall','unresolved'],refresh:true}]);
}
const client=new Client({name:'soviet-famine-scenario-evaluations',version:'1'});
client.registerCapabilities({tasks:{list:{},cancel:{},requests:{tools:{call:{}}}}});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});
await client.connect(transport);
async function run(label,args){
 let last=''; console.log('START',label);
 const stream=client.experimental.tasks.callToolStream({name:'hoi4.probability_evaluate',arguments:args},undefined,{task:{ttl:86400000},timeout:180000});
 for await(const message of stream){
  if(message.type==='taskCreated'){await writeFile(path.join(evidence,label+'-task.json'),JSON.stringify({task:message.task,args},null,2));console.log('TASK',label,JSON.stringify(message.task));}
  else if(message.type==='taskStatus'){const now=JSON.stringify({status:message.task.status,statusMessage:message.task.statusMessage,lastUpdatedAt:message.task.lastUpdatedAt});if(now!==last){last=now;await writeFile(path.join(evidence,label+'-task-status.json'),now);console.log('STATUS',label,now);}}
  else if(message.type==='result'){await writeFile(path.join(evidence,label+'.json'),JSON.stringify(message.result,null,2));console.log('RESULT',label,JSON.stringify({isError:message.result.isError??false,structuredContent:message.result.structuredContent??null},null,2));}
  else if(message.type==='error'){await writeFile(path.join(evidence,label+'-error.txt'),String(message.error?.stack??message.error));console.error('ERROR',label,message.error?.stack??message.error);}
 }
}
try{for(const [label,args] of requests)await run(label,args);}catch(error){console.error('CLIENT_ERROR',error?.stack??error);process.exitCode=1;}finally{await client.close();}
