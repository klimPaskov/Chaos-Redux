import {createRequire} from 'node:module';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const labels=['before-event-warning-probability-evaluate','after-event-warning-probability-evaluate','before-event-crisis-probability-evaluate','after-event-crisis-probability-evaluate'];
const client=new Client({name:'soviet-famine-probability-artifact-range-reader',version:'1'});const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});await client.connect(transport);
const chunkSize=48000;
async function readArtifact(label){
 const envelope=JSON.parse(await readFile(path.join(evidence,label+'.json'),'utf8'));
 const link=envelope.structuredContent.artifacts.find(a=>a.description==='Authoritative AI and MTTH scenario analysis JSON');
 const uri=link.uri;const wantHash=uri.split('/')[5];const total=link.size;const chunks=[];
 for(let offset=0;offset<total;offset+=chunkSize){const length=Math.min(chunkSize,total-offset);const chunkUri=uri+`?offset=${offset}&length=${length}`;const r=await client.readResource({uri:chunkUri},{timeout:60000});const c=r.contents?.[0];if(!c?.blob)throw new Error(`${label} offset ${offset}: no base64 blob`);if(!/^[A-Za-z0-9+/]*={0,2}$/u.test(c.blob))throw new Error(`${label} offset ${offset}: invalid base64 alphabet`);const raw=Buffer.from(c.blob,'base64');const range=c._meta?.['io.github.klimpaskov/hoi4-agent-tools.artifact-byte-range']?.returnedRange;if(!range||range.offset!==offset||range.length!==length||range.endExclusive!==offset+length)throw new Error(`${label} offset ${offset}: byte-range metadata mismatch ${JSON.stringify(range)}`);if(raw.length!==length)throw new Error(`${label} offset ${offset}: decoded length ${raw.length} != ${length}`);chunks.push(raw);}
 const bytes=Buffer.concat(chunks);if(bytes.length!==total)throw new Error(`${label}: total bytes ${bytes.length} != ${total}`);const hash=createHash('sha256').update(bytes).digest('hex');if(hash!==wantHash)throw new Error(`${label}: SHA-256 ${hash} != URI hash ${wantHash}`);const resource=JSON.parse(bytes.toString('utf8'));const out=path.join(evidence,label+'-resource.json');await writeFile(out,bytes);const scenarios=(resource.scenarios??[]).map(s=>({id:s.id,candidates:(s.candidates??[]).map(c=>({id:c.id,eligibility:c.eligibility,conditionalProbability:c.conditionalProbability,rawValue:c.rawValue,unresolved:c.unresolved,unresolvedReasons:c.unresolvedReasons,support:c.support,trace:c.trace}))}));console.log(JSON.stringify({label,uri,size:total,sha256:hash,analysisId:resource.analysisId,sourceRevision:resource.metadata?.sourceRevision,sourceHash:resource.metadata?.sourceHash,scenarioHash:resource.metadata?.scenarioHash,candidatePoolHash:resource.metadata?.candidatePoolHash,scenarioCount:scenarios.length,out,scenarios},null,2));
}
try{for(const label of labels)await readArtifact(label);}catch(error){console.error(error?.stack??error);process.exitCode=1;}finally{await client.close();}

