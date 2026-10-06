import {createRequire} from 'node:module';
import {writeFile} from 'node:fs/promises';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(pkg+'/package.json');
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const repo='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const after=evidence+'/after_2026-10-06';
const rel='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const config=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03/config.json';
const server='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js';
const workspaceId='camp_origin_architecture_oct3';
const cases=[
 {id:'german_manual_transfer_after',adapter:'decision_ai_will_do',path:'common/decisions/genocide_crisis_decisions.txt',snapshot:rel+'/after_2026-10-06/after__common__decisions__genocide_crisis_decisions.txt'},
 {id:'partner_events_after',adapter:'event_option_ai_chance',path:'events/camp_occ_partner_events.txt',snapshot:rel+'/after_2026-10-06/after__events__camp_occ_partner_events.txt'},
 {id:'partner_decisions_after',adapter:'decision_ai_will_do',path:'common/decisions/camp_occ_partner_decisions.txt',snapshot:rel+'/after_2026-10-06/after__common__decisions__camp_occ_partner_decisions.txt'}
];
const shaBySnapshot={
 [rel+'/after_2026-10-06/after__common__decisions__genocide_crisis_decisions.txt']:'5E1C8AEA73B0BBF5DD4ADFF4111230A9D105D329C4B95B6012110BDA28431177',
 [rel+'/after_2026-10-06/after__events__camp_occ_partner_events.txt']:'F85A916E2579A9061FD06FC61AD677770787AC05501B7422640CF4685100F73A',
 [rel+'/after_2026-10-06/after__common__decisions__camp_occ_partner_decisions.txt']:'59E2515D8C9AA219D1C9EBD4A47B7C3852DA4436546E18FA43DD53E4965779AD'
};
const c=new Client({name:'camp-probability-after-inspector-readonly',version:'1'});
const t=new StdioClientTransport({command:process.execPath,args:[server,'--config',config],cwd:pkg,stderr:'pipe'});
t.stderr?.on('data',d=>process.stderr.write(d));
try{
 await c.connect(t);const summary=[];
 for(const item of cases){
  const snapshotPath=item.snapshot;
  const request={workspaceId,adapter:item.adapter,source:{path:item.path,snapshotPath,expectedSourceHash:shaBySnapshot[item.snapshot].toLowerCase()}};
  try{
   const response=await c.callTool({name:'hoi4.probability_inspect',arguments:request},undefined,{timeout:90000});
   await writeFile(evidence+'/'+item.id+'_inspect.json',JSON.stringify({request,response},null,2));
   summary.push({id:item.id,status:response.structuredContent?.status,code:response.structuredContent?.code,artifacts:response.structuredContent?.artifacts,blockers:response.structuredContent?.blockers,diagnostics:response.structuredContent?.diagnostics});
  }catch(error){
   const rec={id:item.id,error:String(error),code:error.code};
   await writeFile(evidence+'/'+item.id+'_inspect_error.json',JSON.stringify({request,error:rec},null,2));
   summary.push(rec);
  }
 }
 console.log(JSON.stringify({server:c.getServerVersion(),summary}));
}finally{await c.close();}
