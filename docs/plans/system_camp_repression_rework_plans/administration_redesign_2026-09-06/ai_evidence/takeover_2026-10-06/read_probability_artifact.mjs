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
const uri='hoi4-agent://workspace/camp_origin_architecture_oct3/artifact/31da341b0dcc3f9447e8527ffa09085ef9565e30728067622fa5144445f7c217/00b9b201d5348abc541c16c87b27ae10516c410a22370e9d0ae35bee42ce36dd/probability-inspect-5cc0fb7b0a0b.json';
const c=new Client({name:'camp-probability-artifact-reader',version:'1'});
const t=new StdioClientTransport({command:process.execPath,args:[server,'--config',config],cwd:pkg,stderr:'pipe'});
t.stderr?.on('data',d=>process.stderr.write(d));
try{
 await c.connect(t);
 const r=await c.readResource({uri:uri+'?offset=0&length=4096'});
 await writeFile(evidence+'/german_transfer_inspect_range_000000.json',JSON.stringify(r,null,2));
 const contents=r.contents??[];
 console.log(JSON.stringify({contents:contents.map(x=>({uri:x.uri,mimeType:x.mimeType,textLength:x.text?.length,blobLength:x.blob?.length,textPrefix:x.text?.slice(0,700)})),meta:r._meta}));
}finally{await c.close();}
