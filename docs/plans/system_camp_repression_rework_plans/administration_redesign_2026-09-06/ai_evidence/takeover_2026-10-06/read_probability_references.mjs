import {createRequire} from 'node:module';import{writeFile}from'node:fs/promises';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';const require=createRequire(pkg+'/package.json');const{Client}=require('@modelcontextprotocol/sdk/client/index.js');const{StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const repo='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';const evidence=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';const config=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03/config.json';const server='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js';const w='camp_origin_architecture_oct3';
const c=new Client({name:'camp-probability-reference-readonly',version:'1'});const t=new StdioClientTransport({command:process.execPath,args:[server,'--config',config],cwd:pkg,stderr:'pipe'});t.stderr?.on('data',d=>process.stderr.write(d));
try{
 await c.connect(t);const attempts=[],searches={};
 async function call(name,args){try{const r=await c.callTool({name,arguments:{workspaceId:w,...args}},undefined,{timeout:60000});attempts.push({name,args,result:r});return r.structuredContent;}catch(e){attempts.push({name,args,error:String(e),code:e.code});return null;}}
 for(const [key,query,source] of [
  ['aiw-wiki-doc','ai_will_do decision score',['wiki','game_doc']],
  ['aic-wiki-doc','ai_chance option weight',['wiki','game_doc']],
  ['aiw-doc','ai_will_do',['game_doc']],
  ['aic-doc','ai_chance',['game_doc']]]) searches[key]=await call('hoi4.reference_search',{query,sources:source,limit:12});
 const wanted=[];
 for(const key of Object.keys(searches))for(const x of searches[key]?.data?.results??[]){
  if(/(?:Event modding|Decision modding|AI modding|decisions|ai_strategy)/i.test(x.title+' '+x.path)){
   const k=x.id+'|'+x.revision+'|'+x.matchLine;
   if(!wanted.some(y=>y.k===k))wanted.push({k,ref:x});
  }
 }
 const reads=[];
 for(const {ref} of wanted){const r=await call('hoi4.reference_read',{id:ref.id,revision:ref.revision,source:ref.source,startLine:ref.matchLine,maxLines:45});reads.push({reference:{id:ref.id,revision:ref.revision,source:ref.source,path:ref.path,startLine:ref.matchLine,title:ref.title},result:r});}
 const vanillaRefs=[
  {id:'c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58',revision:'5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019',source:'game_doc',path:'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md',startLine:1,title:'Vanilla decisions documentation'},
  {id:'355b21a102b1d749dc84b91d7cbf5f40f0cfed1ecd51b6cbfe97b24e5381c66e',revision:'7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29',source:'game_doc',path:'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md',startLine:6285,title:'Vanilla is_subject_of trigger documentation'}
 ];
 for(const ref of vanillaRefs){const r=await call('hoi4.reference_read',{id:ref.id,revision:ref.revision,source:ref.source,startLine:ref.startLine,maxLines:45});reads.push({reference:ref,result:r});}
 await writeFile(evidence+'/probability_references_targeted.json',JSON.stringify({server:c.getServerVersion(),searches,reads,attempts},null,2));
 console.log(JSON.stringify({server:c.getServerVersion(),searches:Object.fromEntries(Object.entries(searches).map(([k,v])=>[k,{status:v?.status,code:v?.code,total:v?.data?.total,omitted:v?.data?.omitted,results:(v?.data?.results??[]).map(x=>({source:x.source,title:x.title,path:x.path,startLine:x.startLine,matchLine:x.matchLine,id:x.id,revision:x.revision}))}])),reads:reads.map(x=>({reference:x.reference,status:x.result?.status,code:x.result?.code,filesScanned:x.result?.filesScanned,dataKeys:Object.keys(x.result?.data??{}),text:x.result?.data?.text?.slice?.(0,600)}))}));
}finally{await c.close();}
