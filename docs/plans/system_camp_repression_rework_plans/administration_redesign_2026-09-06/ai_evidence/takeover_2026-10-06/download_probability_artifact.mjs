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
const base='hoi4-agent://workspace/camp_origin_architecture_oct3/artifact/31da341b0dcc3f9447e8527ffa09085ef9565e30728067622fa5144445f7c217/00b9b201d5348abc541c16c87b27ae10516c410a22370e9d0ae35bee42ce36dd/probability-inspect-5cc0fb7b0a0b.json';
const expectedSha='31da341b0dcc3f9447e8527ffa09085ef9565e30728067622fa5144445f7c217';
const chunkSize=16384;
const metaKey='io.github.klimpaskov/hoi4-agent-tools.artifact-byte-range';
const c=new Client({name:'camp-probability-artifact-reader',version:'1'});
const t=new StdioClientTransport({command:process.execPath,args:[server,'--config',config],cwd:pkg,stderr:'pipe'});
t.stderr?.on('data',d=>process.stderr.write(d));
try {
 await c.connect(t);
 let next=base+'?offset=0&length='+chunkSize, offset=0, total=null, complete=false;
 const chunks=[], ranges=[];
 while(!complete) {
   const requestedUri=next;
   const r=await c.readResource({uri:requestedUri});
   if(!Array.isArray(r.contents)||r.contents.length!==1) throw new Error('Expected one artifact resource content.');
   const content=r.contents[0], meta=content._meta?.[metaKey], encoded=content.blob;
   if(content.mimeType!=='application/json'||typeof encoded!=='string') throw new Error('Unexpected content MIME or encoding.');
   if(!/^[A-Za-z0-9+/]*={0,2}$/.test(encoded)) throw new Error('Invalid base64 characters.');
   const bytes=Buffer.from(encoded,'base64');
   if(bytes.toString('base64')!==encoded) throw new Error('Non-canonical or truncated base64.');
   if(!meta||meta.unit!=='byte'||!meta.returnedRange) throw new Error('Missing byte-range metadata.');
   const {returnedRange}=meta;
   if(returnedRange.offset!==offset||returnedRange.length!==bytes.length||returnedRange.endExclusive!==offset+bytes.length) throw new Error('Returned byte range does not match requested offset/decoded length.');
   if(total===null) total=meta.totalSize;
   if(meta.totalSize!==total) throw new Error('Artifact size changed between chunks.');
   chunks.push(bytes);
   ranges.push({requestedUri,returnedUri:content.uri,offset:returnedRange.offset,length:returnedRange.length,endExclusive:returnedRange.endExclusive,totalSize:meta.totalSize,complete:meta.complete,continuationUri:meta.continuationUri??null,sha256:meta.sha256??null});
   offset=returnedRange.endExclusive;
   complete=meta.complete===true||offset===total;
   if(!complete) {
     if(typeof meta.continuationUri!=='string') throw new Error('Missing continuation URI for incomplete read.');
     next=meta.continuationUri;
   }
 }
 const bytes=Buffer.concat(chunks);
 const actualSha=createHash('sha256').update(bytes).digest('hex');
 if(bytes.length!==total||actualSha!==expectedSha) throw new Error('Final length/SHA mismatch.');
 const text=bytes.toString('utf8');
 if(!text.startsWith('{')||!text.trimEnd().endsWith('}')) throw new Error('Artifact did not have JSON signature.');
 if(/(?:\[\s*truncated\s*\]|\[\s*omitted\s*\]|literal truncation marker)/i.test(text)) throw new Error('Artifact contains a transport truncation marker.');
 const parsed=JSON.parse(text);
 const artifactPath=evidence+'/probability-inspect-5cc0fb7b0a0b.json';
 await writeFile(artifactPath,bytes);
 const prior=JSON.parse(await readFile(evidence+'/installed_probability_client_schemas.json','utf8'));
 await writeFile(evidence+'/probability_inspect_german_transfer.json',JSON.stringify(prior.initialInspect,null,2));
 await writeFile(evidence+'/german_transfer_inspect_read_manifest.json',JSON.stringify({artifactUri:base,declaredSha256:expectedSha,actualSha256:actualSha,declaredSize:total,decodedSize:bytes.length,contentMimeType:'application/json',transportEncoding:'base64 blob in MCP ResourceContents',ranges,artifactPath},null,2));
 const s=parsed.surface??{};
 console.log(JSON.stringify({sha256:actualSha,size:bytes.length,surfaceKeys:Object.keys(s),surfaceId:s.id,source:s.source,sourceRevision:s.sourceRevision,adapter:s.adapter,capabilities:s.adapter?.capabilities,candidateCount:s.candidates?.length,matchingCandidates:(s.candidates??[]).filter(x=>/germany_transfer_prisoners_to_experiment_site|krakow/i.test(JSON.stringify(x))).slice(0,5),scenarioSchema:parsed.scenarioSchema??parsed.schemas?.scenario??parsed.scenario,topLevelKeys:Object.keys(parsed)}));
} finally { await c.close(); }
