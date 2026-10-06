import {createRequire} from 'node:module';
import {writeFile} from 'node:fs/promises';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(pkg+'/package.json');
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const repo='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const config=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03/config.json';
const server='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js';
const c=new Client({name:'camp-probability-source-audit-readonly',version:'1'});
const t=new StdioClientTransport({command:process.execPath,args:[server,'--config',config],cwd:pkg,stderr:'pipe'});
t.stderr?.on('data',d=>process.stderr.write(d));
try{
 await c.connect(t);const calls=[];
 for(const symbol of [
  'camp_occ_manual_transfer_country_prerequisites_ready',
  'camp_occ_manual_transfer_any_source_ready',
  'camp_admin_country_regime_valid',
  'camp_admin_ger_krakow_setup_context',
  'camp_admin_ger_krakow_setup_eligible',
  'camp_admin_country_ai_krakow_killing_role',
  'camp_occ_country_counts_as_german_authority',
  'camp_occ_state_has_german_authority',
  'camp_occ_extended_partner_order_stands',
  'camp_occ_extended_partner_country',
  'camp_occ_extended_partner_wave_window',
  'camp_occ_extended_partner_can_halt',
  'camp_occ_state_has_partner_authority'
 ]){
  const args={workspaceId:'camp_origin_architecture_oct3',symbol,includeReferences:false,maxDefinitions:1,maxReferences:0,maxLines:70};
  try{const r=await c.callTool({name:'hoi4.source_lookup',arguments:args},undefined,{timeout:60000});calls.push({symbol,args,result:r});}
  catch(e){calls.push({symbol,args,error:String(e),code:e.code});}
 }
 const vanillaArgs={workspaceId:'camp_origin_architecture_oct3',path:'common/decisions/GER.txt',line:6141,includeReferences:false,maxDefinitions:1,maxReferences:0,maxLines:50};
 try{const r=await c.callTool({name:'hoi4.source_lookup',arguments:vanillaArgs},undefined,{timeout:60000});calls.push({symbol:'vanilla_GER_generalgouvernement',args:vanillaArgs,result:r});}
 catch(e){calls.push({symbol:'vanilla_GER_generalgouvernement',args:vanillaArgs,error:String(e),code:e.code});}
 await writeFile(evidence+'/source_lookup_surface_definitions.json',JSON.stringify({server:c.getServerVersion(),calls},null,2));
 console.log(JSON.stringify({server:c.getServerVersion(),calls:calls.map(x=>({symbol:x.symbol,status:x.result?.structuredContent?.status,code:x.result?.structuredContent?.code,diagnostics:x.result?.structuredContent?.diagnostics,definitions:x.result?.structuredContent?.data?.definitions?.map(d=>({symbol:d.symbol,path:d.path,startLine:d.startLine,endLine:d.endLine,text:d.text})),error:x.error}))}));
}finally{await c.close();}
