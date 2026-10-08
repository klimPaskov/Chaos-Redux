import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const repo=process.cwd(), base=path.resolve('docs/plans/032_missiles_plans/evidence/evolution_timing_20261007'), out=path.join(base,'after_20261008');
const pkg='C:/Users/klimp/AppData/Local/npm-cache/_npx/e5002410e5b7105a/node_modules/hoi4-agent-tools';
const req=createRequire(pkg+'/package.json');
const {Client}=req('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=req('@modelcontextprotocol/sdk/client/stdio.js');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const action=process.argv[2]??'init';
const client=new Client({name:'chaosx-event32-bounded-auditor',version:'1.0.0'},{capabilities:{}});
const transport=new StdioClientTransport({command:process.execPath,args:[pkg+'/dist/bin/stdio.js'],cwd:repo,env:{...process.env,HOI4_AGENT_CONFIG:'C:/Users/klimp/AppData/Roaming/hoi4-agent-tools/config.json'},stderr:'pipe'});
let err='';
transport.stderr?.on('data',b=>{if(err.length<12000)err+=b.toString();});
const save=(name,obj)=>{const p=path.join(out,name);fs.writeFileSync(p,typeof obj==='string'?obj:JSON.stringify(obj,null,2)+'\n',{flag:'wx'});return p;};
const fixture=()=>JSON.parse(fs.readFileSync(path.join(out,'scenarioSet.paired.v2.json'),'utf8'));
const workspaceId='mod_chaos_redux_ea3b2d67c2c0';
const pool=[201,202,203,204,205].map(x=>'chaosx.nr32.'+x);
const after={path:'events/032_missiles_evolution_events.txt',snapshotPath:path.relative(repo,path.join(out,'source/events/032_missiles_evolution_events.txt')).replaceAll('\\','/'),expectedSourceHash:'8728c998407f6bbef6c88923ee40a6a7d78dc9c4007604fb91facce501398577'};
async function artifacts(result,label){
 const rows=[];
 for(const [i,a] of (result.structuredContent?.artifacts??[]).entries()){
  if(a.size>2_000_000){rows.push({...a,status:'not_retrieved_size_limit'});continue;}
  const parts=[];let offset=0;
  try{
   while(offset<a.size){
    const n=Math.min(65536,a.size-offset);
    const r=await client.readResource({uri:a.uri+'?offset='+offset+'&length='+n});
    const c=r.contents; if(!Array.isArray(c)||c.length!==1)throw Error('Unexpected resource envelope');
    const bytes=c[0].blob!==undefined?Buffer.from(c[0].blob,'base64'):Buffer.from(c[0].text??'','utf8');
    if(bytes.length!==n)throw Error('Unexpected byte range '+bytes.length+' expected '+n);
    parts.push(bytes);offset+=bytes.length;
   }
   const b=Buffer.concat(parts);
   if(b.length!==a.size||sha(b)!==a.sha256)throw Error('Artifact checksum mismatch');
   const filename=label+'.artifact.'+i+'.'+a.name;
   fs.writeFileSync(path.join(out,filename),b,{flag:'wx'});
   rows.push({...a,status:'verified',localPath:filename});
  }catch(e){rows.push({...a,status:'retrieval_unresolved',error:String(e)});}
 }
 save(label+'.artifacts.json',rows); return rows;
}
try{
 await client.connect(transport);
 const catalog=await client.listTools();
 save(action+'.connection.json',{serverInfo:client.getServerVersion(),capabilities:client.getServerCapabilities(),clientCapabilities:{},pid:transport.pid,command:process.execPath,args:[pkg+'/dist/bin/stdio.js'],cwd:repo,config:'C:/Users/klimp/AppData/Roaming/hoi4-agent-tools/config.json',windowsHide:true,tools:catalog.tools.filter(t=>/probability|event_inspect|event_render/.test(t.name)).map(t=>({name:t.name,inputSchema:t.inputSchema}))});
 if(action==='init'){console.log(JSON.stringify({server:client.getServerVersion(),toolNames:catalog.tools.filter(t=>/probability|event_inspect|event_render/.test(t.name)).map(t=>t.name)}));}
 else{
  let name,args;
  const common={workspaceId,adapter:'event_mean_time_to_happen',candidatePool:pool};
  if(action==='inspect'){name='hoi4.probability_inspect';args={...common,source:after};}
  if(action==='evaluate'){name='hoi4.probability_evaluate';args={...common,source:after,scenarioSet:fixture(),horizonDays:365,metrics:['effective_mtth_days','cumulative_chance'],outputs:['json','matrix']};}
  if(/^curve_20[1-5]$/.test(action)){name='hoi4.probability_evaluate';args={...common,candidatePool:['chaosx.nr32.'+action.slice(6)],source:after,scenarioSet:fixture(),horizonDays:365,metrics:['effective_mtth_days','cumulative_chance'],outputs:['json','timing']};}
  if(action==='compare'||action==='compare_event_zero'){
   name='hoi4.probability_compare';
   const p=action==='compare'?'common/scripted_effects/032_missiles_operations_effects.txt':'events/032_missile_crisis.txt';
   const h=action==='compare'?'5f803dd63867d0303d19e7e7e388f00ba6440130b53237ffbe961b715d0ae67b':'2416fc6159201c6059925cd68218de159ee0f37ade4f89896403801fec99a50a';
   args={...common,before:{path:p,snapshotPath:path.relative(repo,path.join(base,'before',p)).replaceAll('\\','/'),expectedSourceHash:h},after,scenarioSet:fixture(),horizonDays:365,outputs:['json','comparison']};
  }
  if(action==='sweep'){name='hoi4.probability_sweep';args={...common,candidatePool:['chaosx.nr32.205'],source:after,scenarioSet:JSON.parse(fs.readFileSync(path.join(out,'scenarioSet.threshold.v1.json'),'utf8')),horizonDays:365,metrics:['effective_mtth_days','cumulative_chance'],sweep:{paths:['global.chaos_meter_value'],steps:2,findRankReversals:false,pairwise:false},outputs:['json','threshold']};}
  if(action==='structure'){name='hoi4.event_inspect';args={workspaceId,mode:'trace',selector:{kind:'file',sourcePath:'mod:events/032_missiles_evolution_events.txt'},maxDepth:1,maxNodes:12,maxEdges:20,expandHelpers:false};}
  if(action==='event_render'){name='hoi4.event_render';args={workspaceId,view:'timing',selector:{kind:'file',sourcePath:'mod:events/032_missiles_evolution_events.txt'},maxDepth:1,maxNodes:12,expandHelpers:false,includeHtml:false};}
  if(action==='render'){
   const ev=JSON.parse(fs.readFileSync(path.join(out,'evaluate.response.json'),'utf8')).structuredContent.data;
   name='hoi4.probability_render';args={workspaceId,analysisId:ev.analysisId,expectedScenarioHash:ev.scenarioHash,outputs:['matrix','unresolved'],includeHtml:false};
  }
  if(!name||!catalog.tools.some(t=>t.name===name))throw Error('Confirmed tool unavailable '+action);
  save(action+'.request.json',args);
  console.log(JSON.stringify({stage:'calling',name,scenarios:args.scenarioSet?.scenarios.length??0}));
  const result=await client.callTool({name,arguments:args},undefined,{timeout:180000});
  save(action+'.response.json',result);
  const retained=await artifacts(result,action);
  console.log(JSON.stringify({stage:'complete',code:result.structuredContent?.code,status:result.structuredContent?.status,data:result.structuredContent?.data,blockers:result.structuredContent?.blockers,artifacts:retained.map(a=>({name:a.name,size:a.size,status:a.status,error:a.error,localPath:a.localPath}))}));
 }
}catch(e){save(action+'.error.json',{error:String(e),stderr:err});console.log(JSON.stringify({stage:'error',error:String(e),stderr:err.slice(-1200)}));process.exitCode=1;}
finally{await client.close();}
