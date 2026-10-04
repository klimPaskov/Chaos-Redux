import {createRequire} from 'node:module';
import {readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
const sdk='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const installed='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools';
const require=createRequire(path.join(sdk,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const base='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03';
const runtime=JSON.parse(await readFile('docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03/probability-runtime.json','utf8'));
const client=new Client({name:'mengele-foreign-purchase-retirement',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(installed,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:installed,stderr:'pipe'});
try {
 await client.connect(transport);
 const list=await client.listTools();
 await writeFile(path.join(base,'server.json'),JSON.stringify({version:client.getServerVersion(),capabilities:client.getServerCapabilities(),tools:list.tools},null,2));
 const workspaceId=runtime.workspaceId;
 const narrow=process.argv.includes('--narrow');
 const requests=process.argv.includes('--docs') ? [
  ['reference-read-decision-gates','hoi4.reference_read',{id:'c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58',revision:'5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019',maxLines:50,workspaceId}],
  ['reference-read-wiki-cost','hoi4.reference_read',{id:'0a37b9f1ad43a16c2d85d25b307d261fcc9e60292b4e164c335c03816535e4d8',revision:'7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162',maxLines:60,workspaceId}],
  ['reference-read-wiki-gates','hoi4.reference_read',{id:'21ff847245747e215d1cb8b5ace4abb3044f2269b53952c53b9bade4b8a2d21f',revision:'7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162',maxLines:35,workspaceId}],
 ] : narrow ? [
  ['decision-inspect-retry','hoi4.decision_inspect',{id:'import_subjects_from_japanese_china',mode:'inventory',workspaceId}],
  ['event-inspect-retry','hoi4.event_inspect',{mode:'trace',selector:{kind:'source',sourcePath:'common/scripted_effects/germany_mengele_effects.txt',line:192},expandHelpers:false,maxDepth:1,maxNodes:1,maxEdges:1,workspaceId}],
 ] : [
  ['reference-context','hoi4.reference_context',{surface:'decision',question:'Decision native political power cost, complete_effect refund, allowed visible available and native cooldown',limit:20,workspaceId}],
  ['reference-search','hoi4.reference_search',{query:'complete_effect',sources:['game_doc','wiki'],limit:4,workspaceId}],
  ['reference-search-pp','hoi4.reference_search',{query:'add_political_power',sources:['game_doc'],limit:2,workspaceId}],
  ['decision-inspect','hoi4.decision_inspect',{id:'import_subjects_from_japanese_china',mode:'inspect',scenarios:[{id:'initialized_active_programme',actor:'GER',date:'1943.06.01',flags:['camp_admin_initialized','germany_mengele_program_authorized'],state:{}}],workspaceId}],
  ['event-inspect','hoi4.event_inspect',{mode:'trace',selector:{kind:'event',eventId:'germany_mengele.18'},expandHelpers:false,maxDepth:1,maxNodes:2,maxEdges:2,workspaceId}],
 ];
 for(const [label,name,args] of requests) {
  if(!list.tools.some(tool=>tool.name===name)) {
   await writeFile(path.join(base,label+'-error.txt'),'Required route '+name+' is absent from initialized installed global 3.6.0 tool list.\n');
   console.log('MISSING',name);continue;
  }
  console.log('START',label);
  try {
   const result=await client.callTool({name,arguments:args},undefined,{timeout:45000});
   await writeFile(path.join(base,label+'.json'),JSON.stringify(result,null,2));
   console.log('RESULT',label,result.structuredContent?.status??result.isError??'returned');
   if(name==='hoi4.reference_search') {
    const sections=result.structuredContent?.data?.results??[];
    for(let index=0;index<Math.min(sections.length,2);index++) {
     const section=sections[index];
     const args={id:section.id,revision:section.revision,maxLines:80,workspaceId};
     const read=await client.callTool({name:'hoi4.reference_read',arguments:args},undefined,{timeout:45000});
     await writeFile(path.join(base,label+'-read-'+index+'.json'),JSON.stringify(read,null,2));
    }
   }
  } catch(error) {
   await writeFile(path.join(base,label+'-error.txt'),String(error.stack??error));
   console.log('ERROR',label,String(error));
  }
 }
} finally {await client.close();}
