import {createRequire} from 'node:module';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(pkg+'/package.json');
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const repo='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const config=repo+'/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03/config.json';
const server='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js';
const metaKey='io.github.klimpaskov/hoi4-agent-tools.artifact-byte-range';
const jobs=[];
for(const [id,file] of [
 ['partner_event_baseline','partner_event_baseline_inspect.json'],
 ['partner_decision_baseline','partner_decision_baseline_inspect.json'],
 ['german_manual_transfer_after','german_manual_transfer_after_inspect.json'],
 ['krakow_country_effects_before','krakow_country_effects_before_inspect.json'],
 ['krakow_country_effects_after','krakow_country_effects_after_inspect.json'],
 ['krakow_country_decisions_before','krakow_country_decisions_before_inspect.json'],
 ['partner_events_after','partner_events_after_inspect.json'],
 ['partner_decisions_after','partner_decisions_after_inspect.json']
]){
 const doc=JSON.parse(await readFile(evidence+'/'+file,'utf8'));
 for(const artifact of doc.response.structuredContent.artifacts??[]) jobs.push({id,artifact});
}
const c=new Client({name:'camp-probability-artifact-reader',version:'1'});
const t=new StdioClientTransport({command:process.execPath,args:[server,'--config',config],cwd:pkg,stderr:'pipe'});
t.stderr?.on('data',d=>process.stderr.write(d));
try {
 await c.connect(t);
 const output=[];
 for(const job of jobs){
  const {uri,sha256,size,name}=job.artifact;
  let next=uri+'?offset=0&length=8192',offset=0,total=null,complete=false;
  const chunks=[],ranges=[];
  while(!complete){
   const requestedUri=next;
   const response=await c.readResource({uri:requestedUri});
   if(response.contents?.length!==1)throw new Error('Expected exactly one resource content');
   const content=response.contents[0],meta=content._meta?.[metaKey];
   if(content.mimeType!=='application/json')throw new Error('Unexpected artifact MIME type');
   let bytes,encoding;
   if(typeof content.blob==='string'&&typeof content.text==='undefined'){
    const encoded=content.blob;
    if(!/^[A-Za-z0-9+/]*={0,2}$/.test(encoded))throw new Error('Invalid base64 characters');
    bytes=Buffer.from(encoded,'base64');
    if(bytes.toString('base64')!==encoded)throw new Error('Invalid or truncated base64');
    encoding='base64 blob';
   }else if(typeof content.text==='string'&&typeof content.blob==='undefined'){
    bytes=Buffer.from(content.text,'utf8');
    encoding='UTF-8 text';
   }else throw new Error('Expected exactly one text or blob representation');
   const range=meta?.returnedRange;
   if(!meta||meta.unit!=='byte'||!range||range.offset!==offset||range.length!==bytes.length||range.endExclusive!==offset+bytes.length)throw new Error('Returned byte range does not match request');
   if(total===null)total=meta.totalSize;
   if(meta.totalSize!==total)throw new Error('Artifact total size changed between chunks');
   chunks.push(bytes);
   ranges.push({requestedUri,returnedUri:content.uri,offset:range.offset,length:range.length,endExclusive:range.endExclusive,complete:meta.complete,continuationUri:meta.continuationUri??null,transportEncoding:encoding});
   offset=range.endExclusive;
   complete=meta.complete===true||offset===total;
   if(!complete){
    if(typeof meta.continuationUri!=='string')throw new Error('Missing continuation URI');
    next=meta.continuationUri;
   }
  }
  const bytes=Buffer.concat(chunks);
  const actualSha=createHash('sha256').update(bytes).digest('hex');
  if(bytes.length!==size||total!==size||actualSha!==sha256)throw new Error('Final artifact length or SHA mismatch');
  const text=bytes.toString('utf8');
  if(!text.startsWith('{')||!text.trimEnd().endsWith('}'))throw new Error('Artifact is not complete JSON');
  const parsed=JSON.parse(text);
  const artifactPath=evidence+'/'+job.id+'_'+name;
  await writeFile(artifactPath,bytes);
  const manifest={id:job.id,uri,sha256,actualSha256:actualSha,size,decodedSize:bytes.length,mimeType:'application/json',ranges,artifactPath};
  await writeFile(evidence+'/'+job.id+'_artifact_read_manifest.json',JSON.stringify(manifest,null,2));
  const surface=parsed.surface;
  output.push({id:job.id,sha256:actualSha,size:bytes.length,topKeys:Object.keys(parsed),surface:surface?{id:surface.id,sourceHash:surface.sourceHash,sourceRevision:surface.sourceRevision,candidateCount:surface.candidateCount,poolComplete:surface.poolComplete,requiredInputs:surface.requiredInputs,unsupported:surface.unsupported,candidates:surface.candidates?.map(x=>({id:x.id,analysisSupport:x.analysisSupport,hasWeightBlock:x.hasWeightBlock,hasEligibility:x.hasEligibility,sourceKind:x.sourceKind,location:x.provenance?.[0]?.location,sourceHash:x.provenance?.[0]?.sourceHash}))}:parsed});
 }
 console.log(JSON.stringify({server:c.getServerVersion(),artifacts:output}));
}finally{await c.close();}
