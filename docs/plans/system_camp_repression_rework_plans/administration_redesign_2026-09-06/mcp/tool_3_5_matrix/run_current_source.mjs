import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { tmpdir } from 'node:os';
import { createRequire } from 'node:module';
const require=createRequire('C:/Users/klimp/Documents/Projects/hoi4-agent-tools/package.json');
const { Client }=require('@modelcontextprotocol/sdk/client/index.js');
const { StdioClientTransport }=require('@modelcontextprotocol/sdk/client/stdio.js');
const out='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/tool_3_5_matrix/current_source_6c3a2036_4c937887';
const mod='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const game='C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV';
const fixtureRoot=path.join(mod,'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/after');
const workspaceId='camp_admin_gui_audit_35';
const windowName='repression_ledger_window';
const runtimeRoot=await (await import('node:fs/promises')).mkdtemp(path.join(tmpdir(),'camp-admin-gui-35-'));
const storageRoot=path.join(runtimeRoot,'storage');
const configPath=path.join(out,'config.json');
await Promise.all([
  mkdir(path.join(out,'requests'),{recursive:true}),
  mkdir(path.join(out,'results'),{recursive:true}),
  mkdir(path.join(out,'references'),{recursive:true}),
  mkdir(path.join(out,'inspection'),{recursive:true}),
  mkdir(path.join(out,'images'),{recursive:true}),
  mkdir(path.join(runtimeRoot,'state'),{recursive:true}),
  mkdir(path.join(storageRoot,'artifacts'),{recursive:true}),
  mkdir(path.join(storageRoot,'cache'),{recursive:true}),
]);
const config={version:1,serverStateRoot:path.join(runtimeRoot,'state'),storageRoots:[storageRoot],workspaces:[{id:workspaceId,name:'Camp Administration GUI read-only evidence',root:mod,gameRoot:game,artifactRoot:path.join(storageRoot,'artifacts'),cacheRoot:path.join(storageRoot,'cache')}]};
await writeFile(configPath,JSON.stringify(config,null,2));
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const entry=path.join(pkg,'dist/bin/stdio.js');
const client=new Client({name:'camp-admin-gui-matrix-audit',version:'1'});
const transport=new StdioClientTransport({command:process.execPath,args:[entry,'--config',configPath],cwd:pkg,stderr:'pipe'});
transport.stderr?.on('data',chunk=>process.stderr.write(chunk));
const run={runtimeRoot,workspaceId,windowName,gameRoot:game,modRoot:mod,server:null,sourceFiles:[],references:[],inspect:null,renders:[],artifactReads:[],fixtureFacts:[],unresolved:[]};
const jsonWrite=async(file,value)=>{await mkdir(path.dirname(file),{recursive:true});await writeFile(file,JSON.stringify(value,null,2));};
const sha=b=>createHash('sha256').update(b).digest('hex');
const hashFile=async(file)=>({path:file,sha256:sha(await readFile(file))});
const sourcePaths=[
  'interface/camp_repression_ledger.gui',
  'common/scripted_guis/camp_repression_ledger_scripted_gui.txt',
  'localisation/english/camp_administration_ui_l_english.yml',
];
const sourceIdentity=async()=>Promise.all(sourcePaths.map(p=>hashFile(path.join(mod,p))));
const sourceSignature=files=>files.map(f=>`${path.basename(f.path).toLowerCase()}=${f.sha256}`).sort().join('|');
const sameSurfaceSource=(a,b)=>sourceSignature(a)===sourceSignature(b);const readFixture=async(name)=>JSON.parse(await readFile(path.join(fixtureRoot,name),'utf8'));
const targets=[
  {key:'1280x720_scale1',width:1280,height:720,uiScale:1},
  {key:'1920x1080_scale1',width:1920,height:1080,uiScale:1},
  {key:'1920x1080_scale1_25',width:1920,height:1080,uiScale:1.25},
];
const fixtureFiles={
  admin:'admin_ger_1942_06_01_valid.json',
  adminPriorityHover:'admin_ger_1942_06_01_valid.json',
  pickerLocked:'picker_ger_1942_06_01_valid.json',
  pickerActive:'picker_ger_1944_radical_active_125.json',
  pickerHover:'picker_ger_1944_radical_hover_125.json',
  locationsEmpty:'locations_empty_labor_1942_current_{scale}.json',
  locationsFilterHover:'locations_empty_labor_filter_hover_1942_current_125.json',
  locationsCustodyLocked:'locations_empty_custody_locked_current_125.json',
  locationsWorkHover:'locations_empty_custody_work_hover_current_125.json',
  locationsClosed:'locations_closed_site_locked_current_125.json',
  locationsLong:'locations_long_number_hover_current_{scale}.json',
  records:'records_1944_10_01_source_sensitivity_{scale}.json',
  shortage:'shortage_ger_1942_06_01_valid.json',
  shortageActive:'shortage_active_after_{scale}.json',
  shortagePaused:'shortage_already_paused_after_{scale}.json',
};
function scaleToken(target){return target.key==='1280x720_scale1'?'1280':target.key==='1920x1080_scale1'?'1920':'125';}
function dateEvidence(description){const m=description.match(/\b(\d{4})-(\d{2})-(\d{2})\b/);return m?{date:`${m[1]}.${Number(m[2])}.${Number(m[3])}`,basis:m[0]}:null;}
function controlEvidence(description){const m=description.match(/assumed\s+GER\s+control\s+of\s+states?\s+([\d,\sand]+)/i);if(!m)return null;const ids=[...m[1].matchAll(/\d+/g)].map(x=>x[0]);return ids.length?{controls:Object.fromEntries(ids.map(id=>[id,'GER'])),basis:m[0]}:null;}
async function fixtureFor(caseKey,target){const raw=fixtureFiles[caseKey];const name=raw.includes('{scale}')?raw.replace('{scale}',scaleToken(target)):raw;const data=await readFixture(name);const sourceBytes=await readFile(path.join(fixtureRoot,name));return {name,data,sha256:sha(sourceBytes)};}
async function makeScenario(caseKey,target,{hover}={}){
  const {name,data,sha256}=await fixtureFor(caseKey,target);
  const scenario=structuredClone(data);
  const originalId=scenario.id;
  scenario.id=`${originalId}__mcp35_${caseKey}_${target.key}`;
  scenario.resolution={width:target.width,height:target.height};
  scenario.uiScale=target.uiScale;
  const date=dateEvidence(scenario.description??'');
  const controls=controlEvidence(scenario.description??'');
  if(scenario.date===undefined&&date)scenario.date=date.date;
  if(scenario.controls===undefined&&controls)scenario.controls=controls.controls;
  if(hover){scenario.elementStates={...(scenario.elementStates??{}),[hover]:'hover'};}
  const facts={caseKey,fixture:name,fixtureSha256:sha256,fixtureId:originalId,scenarioId:scenario.id,description:scenario.description??'',target:{width:target.width,height:target.height,uiScale:target.uiScale},date:scenario.date??null,dateBasis:scenario.date!==undefined?(date?.basis??'predeclared fixture field'):'missing from fixture description and fields',controls:scenario.controls??null,controlsBasis:scenario.controls!==undefined?(controls?.basis??'predeclared fixture field'):'no numeric state-controller facts in fixture description and fields',elementStates:scenario.elementStates??{}};
  run.fixtureFacts.push(facts);
  return {scenario,facts};
}
function safeStem(value){return value.replace(/[^A-Za-z0-9._-]+/g,'_');}
async function api(name,args,outputStem){
  const callDir=path.join(out,name==='hoi4.gui_inspect'?'inspection':'results',safeStem(outputStem));
  await mkdir(callDir,{recursive:true});
  await jsonWrite(path.join(out,'requests',`${safeStem(outputStem)}_request.json`),{name,arguments:args});
  process.stdout.write(`[start] ${name} ${outputStem}\n`);
  const started=Date.now();
  const result=await client.callTool({name,arguments:args},undefined,{timeout:60_000,maxTotalTimeout:900_000,resetTimeoutOnProgress:true,onprogress:()=>{}});
  await jsonWrite(path.join(callDir,'result.json'),result);
  const row={name,outputStem,elapsedMs:Date.now()-started,isError:result.isError??false,status:result.structuredContent?.status,code:result.structuredContent?.code,sourceRevision:result.structuredContent?.data?.sourceRevision??result.structuredContent?.data?.sharedRevision,scenarioId:result.structuredContent?.data?.scenarioId,artifactCount:result.structuredContent?.artifacts?.length??0,diagnostics:(result.structuredContent?.diagnostics??[]).map(d=>({severity:d.severity,code:d.code,message:d.message,scenarioId:d.details?.scenarioId,element:d.location?.symbol,path:d.location?.path,line:d.location?.start?.line}))};
  process.stdout.write(`[done] ${name} ${outputStem} ${row.elapsedMs}ms ${row.code??'no-code'} artifacts=${row.artifactCount}\n`);
  return {result,row,callDir};
}
async function bytesFromResource(uri){
  const resource=await client.readResource({uri});
  const blocks=resource.contents??[];
  const parts=[];
  for(const item of blocks){if(typeof item.blob==='string')parts.push(Buffer.from(item.blob,'base64'));else if(typeof item.text==='string')parts.push(Buffer.from(item.text,'utf8'));}
  return {bytes:Buffer.concat(parts),mimeType:blocks[0]?.mimeType??null,uri:blocks[0]?.uri??uri};
}
async function artifactBytes(meta){
  let first={bytes:Buffer.alloc(0),mimeType:null,uri:meta.uri};
  try{first=await bytesFromResource(meta.uri);}catch{}
  let bytes=first.bytes;
  let mode='whole-resource';
  if(bytes.length!==meta.size||sha(bytes)!==meta.sha256){
    const chunks=[];let offset=0;
    while(offset<meta.size){const sep=meta.uri.includes('?')?'&':'?';const part=await bytesFromResource(`${meta.uri}${sep}offset=${offset}&length=32768`);if(part.bytes.length===0)break;chunks.push(part.bytes);offset+=part.bytes.length;}
    if(offset===meta.size){bytes=Buffer.concat(chunks);mode='byte-ranges';}
  }
  const actual={bytes:bytes.length,sha256:sha(bytes),expectedBytes:meta.size,expectedSha256:meta.sha256,verified:bytes.length===meta.size&&sha(bytes)===meta.sha256,mode,mimeType:first.mimeType,uri:meta.uri,name:meta.name};
  run.artifactReads.push(actual);
  return {bytes,actual};
}
async function saveArtifact(meta,directory){
  const {bytes,actual}=await artifactBytes(meta);
  if(!actual.verified)throw new Error(`Artifact failed size/SHA verification: ${meta.name}; got ${actual.bytes}/${meta.size}, ${actual.sha256}/${meta.sha256}`);
  const file=path.join(directory,safeStem(meta.name));
  await mkdir(directory,{recursive:true});
  await writeFile(file,bytes);
  return {path:file,sha256:actual.sha256,size:actual.bytes,mimeType:meta.mimeType,uri:meta.uri,sourceArtifact:meta.name};
}
function pngDimensions(bytes){if(bytes.length<24||bytes.subarray(0,8).toString('hex')!=='89504e470d0a1a0a')return null;return {width:bytes.readUInt32BE(16),height:bytes.readUInt32BE(20)};}
function parseGalleryPngs(svgBytes){const svg=svgBytes.toString('utf8');const matches=[...svg.matchAll(/<image\b[^>]*href="data:image\/png;base64,([^"]+)"/g)];return matches.map(m=>Buffer.from(m[1],'base64'));}
function compactBounds(layoutBytes){const parsed=JSON.parse(layoutBytes.toString('utf8'));const scene=parsed.scene??parsed;const elements=scene.elements??[];return {scene:{windowName:scene.windowName,sourceRevision:scene.sourceRevision,resolution:scene.resolution,scenario:scene.scenario,bounds:scene.bounds},visibleButtons:elements.filter(e=>e.elementType==='buttonType'&&e.visible).map(e=>({name:e.name,id:e.id,rect:e.rect,unclippedRect:e.unclippedRect,clipRect:e.clipRect,clickable:e.clickable,clickThrough:e.clickThrough,disabledReason:e.disabledReason??null,state:e.state,rowIndex:e.rowIndex??null,clipped:e.clipped,sourcePath:e.sourcePath,line:e.location?.start?.line})),visibleCount:elements.filter(e=>e.visible).length,visibleClickableCount:elements.filter(e=>e.visible&&e.clickable).length,visibleDisabledButtonCount:elements.filter(e=>e.visible&&e.elementType==='buttonType'&&!e.clickable).length};}
function collectRefs(value,found=[],seen=new Set()){
  if(!value||typeof value!=='object')return found;
  if(Array.isArray(value)){for(const v of value)collectRefs(v,found,seen);return found;}
  if(typeof value.id==='string'&&/^[a-f0-9]{64}$/.test(value.id)&&typeof value.revision==='string'&&/^[a-f0-9]{64}$/.test(value.revision)){
    const key=`${value.id}:${value.revision}`;if(!seen.has(key)){seen.add(key);found.push({id:value.id,revision:value.revision,title:value.title??value.name??value.section??null,path:value.path??value.sourcePath??value.source??null,startLine:value.startLine??value.lineStart??value.start?.line??null,endLine:value.endLine??value.lineEnd??value.end?.line??null});}
  }
  for(const v of Object.values(value))collectRefs(v,found,seen);
  return found;
}
const artifactOutput={inspection:[],renders:[]};
try{
  await client.connect(transport);
  const server=client.getServerVersion();
  if(server?.version!=='3.5.0')throw new Error(`Expected hoi4-agent-tools 3.5.0, got ${server?.version??'unknown'}`);
  run.server=server;
  run.canonicalMcpCommit='d04d7eb51011461b3bb646946805a13bf5c73d2f';
  const toolList=await client.listTools();
  const required=['hoi4.gui_inspect','hoi4.gui_render','hoi4.reference_context','hoi4.reference_search','hoi4.reference_read','hoi4.source_lookup'];
  const selectedTools=toolList.tools.filter(t=>required.includes(t.name));
  const missing=required.filter(name=>!selectedTools.some(t=>t.name===name));
  if(missing.length)throw new Error(`Required v3.5 MCP routes missing: ${missing.join(', ')}`);
  await jsonWrite(path.join(out,'server_and_tool_schemas.json'),{server,toolCount:toolList.tools.length,relevantTools:selectedTools});
  run.sourceFiles=await sourceIdentity();
  const expectedSourceHashes={
    'camp_repression_ledger.gui':'6c3a20368b6e2175aa0d2024098288a0bc2a97ec549c90a73058619e99946d33',
    'camp_repression_ledger_scripted_gui.txt':'4c937887e349decd955e632c59bd119873cd1cced761f5995f5b698fee176dc2',
    'camp_administration_ui_l_english.yml':'4aac46621cd516cdbfa6ed7b45754459a4dc80a8130868bad4e515be859cc445',
  };
  const initialHashes=Object.fromEntries(run.sourceFiles.map(f=>[path.basename(f.path).toLowerCase(),f.sha256]));
  for(const [name,expected] of Object.entries(expectedSourceHashes))if(initialHashes[name]!==expected)throw new Error(`Expected current source ${name} ${expected}; got ${initialHashes[name]??'missing'}`);
  await jsonWrite(path.join(out,'source_identity.json'),{mcpVersion:server.version,canonicalSourceRevision:'d04d7eb51011461b3bb646946805a13bf5c73d2f',localFiles:run.sourceFiles});
  await jsonWrite(path.join(out,'run_setup.json'),{runtimeRoot,config,policy:'MCP state and all artifact/cache roots are task-owned OS temp; config and retained evidence live in the authorized output folder.'});

  const refsContext=await api('hoi4.reference_context',{workspaceId,surface:'gui',question:'Scripted GUI button hover, visible or disabled states, hit regions, and resolution/UI scale rendering for this inspected window.',limit:16},'reference_context_gui');
  const search1=await api('hoi4.reference_search',{workspaceId,query:'scripted GUI buttonType hover click region hitbox enabled disabled state',sources:['game_doc','script_doc','wiki'],limit:8},'reference_search_hover_hit_regions');
  const search2=await api('hoi4.reference_search',{workspaceId,query:'scripted GUI button click effect visibility trigger and interface scaling',sources:['game_doc','script_doc','wiki'],limit:8},'reference_search_click_state_scaling');
  const sourceLookup=await api('hoi4.source_lookup',{workspaceId,symbol:'camp_admin_site_work_locked_empty_visible',kind:'trigger',includeReferences:true,maxDefinitions:3,maxReferences:10,maxLines:40},'source_lookup_locked_work_visibility');
  const interfaceSearch=await api('hoi4.reference_search',{workspaceId,query:'interface modding buttons hover tooltip click region hit box',sources:['wiki'],limit:8},'reference_search_interface_buttons');
  const gameDocRead1=await api('hoi4.reference_read',{workspaceId,id:'e6d2e249edc2c6865ee3d109cfb67e3e30ebafd179ff4f2cb6b6bc2eb1494322',revision:'43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838',startLine:1,maxLines:80},'reference_read_installed_scripted_gui_1_80');
  const gameDocRead2=await api('hoi4.reference_read',{workspaceId,id:'e6d2e249edc2c6865ee3d109cfb67e3e30ebafd179ff4f2cb6b6bc2eb1494322',revision:'43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838',startLine:81,maxLines:80},'reference_read_installed_scripted_gui_81_160');
  const interfaceRefs=collectRefs(interfaceSearch.result).filter(c=>c.title==='Interface modding'&&c.startLine>4);
  if(interfaceRefs.length){const ir=await api('hoi4.reference_read',{workspaceId,id:interfaceRefs[0].id,revision:interfaceRefs[0].revision,maxLines:80},'reference_read_interface_modding');run.references.push({interfaceCitation:interfaceRefs[0],status:ir.row.status,code:ir.row.code});}
  else run.unresolved.push({kind:'interface-reference-section',message:'reference_search returned no detailed Interface modding citation.'});
  const candidates=[...collectRefs(refsContext.result),...collectRefs(search1.result),...collectRefs(search2.result)];
  const uniq=[...new Map(candidates.map(c=>[`${c.id}:${c.revision}`,c])).values()];
  const score=c=>{const s=`${c.title??''} ${c.path??''}`.toLowerCase();return (s.includes('scripted gui')?4:0)+(s.includes('interface modding')?3:0)+(s.includes('button')?2:0)+(s.includes('game')?1:0);};
  uniq.sort((a,b)=>score(b)-score(a));
  run.references.push({contextStatus:refsContext.row.status,search1Status:search1.row.status,search2Status:search2.row.status,sourceLookupStatus:sourceLookup.row.status,candidates:uniq});
  for(const [i,cite] of uniq.slice(0,4).entries()){
    try{const r=await api('hoi4.reference_read',{workspaceId,id:cite.id,revision:cite.revision,maxLines:80},`reference_read_${String(i+1).padStart(2,'0')}`);run.references.at(-1).readStatuses??=[];run.references.at(-1).readStatuses.push({citation:cite,status:r.row.status,code:r.row.code});}
    catch(error){run.references.at(-1).readStatuses??=[];run.references.at(-1).readStatuses.push({citation:cite,error:String(error)});}
  }
  const caseKeys=['admin','pickerLocked','pickerActive','pickerHover','locationsEmpty','locationsFilterHover','locationsCustodyLocked','locationsWorkHover','locationsClosed','locationsLong','records','shortage','shortageActive','shortagePaused'];
  const inspectTarget=targets[2];
  const inspectScenarios=[];
  for(const key of caseKeys){const options=key==='admin'?{}:key==='pickerHover'?{}:key==='locationsFilterHover'?{}:key==='locationsWorkHover'?{}:key==='locationsLong'?{}:{};const {scenario}=await makeScenario(key,inspectTarget,options);inspectScenarios.push(scenario);}
  const adminHover=await makeScenario('admin',inspectTarget,{hover:'camp_admin_choose_priority'});adminHover.scenario.id=`${adminHover.scenario.id}__priority_hover`;adminHover.scenario.elementStates={...(adminHover.scenario.elementStates??{}),camp_admin_choose_priority:'hover'};inspectScenarios.push(adminHover.scenario);
  const primaryInspect=inspectScenarios[0];
  const inspectArgs={workspaceId,windowName,scenario:primaryInspect,relatedScenarios:inspectScenarios.slice(1),generatedScenarios:{enabled:false}};
  const inspectSourceBefore=await sourceIdentity();
  if(!sameSurfaceSource(inspectSourceBefore,run.sourceFiles))throw new Error('GUI source changed before current-source gui_inspect.');
  const inspect=await api('hoi4.gui_inspect',inspectArgs,'gui_inspect_fixture_matrix_1920x1080_scale1_25');
  const inspectSourceAfter=await sourceIdentity();
  if(!sameSurfaceSource(inspectSourceAfter,inspectSourceBefore)){run.unresolved.push({kind:'inspect-source-drift',before:inspectSourceBefore,after:inspectSourceAfter});await jsonWrite(path.join(out,'run_manifest.partial.json'),run);throw new Error('GUI source changed during current-source gui_inspect.');}
  run.inspect=inspect.row;
  const inspectArtifacts=inspect.result.structuredContent?.artifacts??[];
  for(const meta of inspectArtifacts){try{artifactOutput.inspection.push(await saveArtifact(meta,path.join(out,'inspection','artifacts')));}catch(error){run.unresolved.push({kind:'inspect-artifact',artifact:meta.name,error:String(error)});}}
  await jsonWrite(path.join(out,'inspection','summary.json'),{row:inspect.row,fixtureScenarios:inspectScenarios.map(s=>({id:s.id,description:s.description,date:s.date??null,controls:s.controls??null,resolution:s.resolution,uiScale:s.uiScale,elementStates:s.elementStates??{}})),artifactOutput:artifactOutput.inspection});

  const groups=[
    {key:'admin_crisis',primary:'shortageActive',related:['admin','adminPriorityHover','shortage','shortagePaused']},
    {key:'picker_role',primary:'pickerHover',related:['pickerLocked','pickerActive']},
    {key:'locations',primary:'locationsLong',related:['locationsEmpty','locationsFilterHover','locationsCustodyLocked','locationsWorkHover','locationsClosed']},
    {key:'records',primary:'records',related:[]},
  ];
  for(const target of targets){
    for(const group of groups){
      const primary=await makeScenario(group.primary,target,group.primary==='admin'?[{hover:'camp_admin_choose_priority'}]:{});
      const related=[];
      for(const key of group.related){const option=key==='adminPriorityHover'?{hover:'camp_admin_choose_priority'}:{};const item=await makeScenario(key,target,option);related.push(item.scenario);}
      const args={workspaceId,windowName,scenario:primary.scenario,relatedScenarios:related,states:['normal'],resolutions:[{width:target.width,height:target.height,uiScale:target.uiScale}],generatedScenarios:{enabled:false}};
      const stem=`${group.key}_${target.key}`;
      const before=await sourceIdentity();
      if(!sameSurfaceSource(before,run.sourceFiles)){run.unresolved.push({kind:'source-changed-before-render',group:group.key,target,before});await jsonWrite(path.join(out,'run_manifest.partial.json'),run);throw new Error('GUI source changed before render.');}
      let rendered;
      try{rendered=await api('hoi4.gui_render',args,stem);}catch(error){run.renders.push({group:group.key,target,primary:primary.facts,related:related.map(s=>s.id),error:String(error),sourceBefore:before});run.unresolved.push({kind:'render-call',group:group.key,target,error:String(error)});continue;}
      const after=await sourceIdentity();
      if(!sameSurfaceSource(after,before)){run.unresolved.push({kind:'source-changed-during-render',group:group.key,target,before,after,sourceRevision:rendered.row.sourceRevision});await jsonWrite(path.join(out,'run_manifest.partial.json'),run);throw new Error('GUI source changed during render; result not counted as a consistent current-source case.');}
      rendered.row.localSourceBefore=before;
      rendered.row.localSourceAfter=after;
      const metas=rendered.result.structuredContent?.artifacts??[];
      const dir=path.join(out,'images',group.key,target.key);
      const saved=[];
      const wanted=metas.filter(m=>/-(full\.png|cropped\.png|click-regions\.png|scenario-matrix\.svg|layout\.json|validation\.json|fidelity\.json)$/.test(m.name));
      const savedByName=new Map();
      for(const meta of wanted){try{const item=await saveArtifact(meta,dir);saved.push(item);savedByName.set(meta.name,item);}catch(error){run.unresolved.push({kind:'render-artifact',group:group.key,target,artifact:meta.name,error:String(error)});}}
      const galleryMeta=metas.find(m=>m.name.endsWith('-scenario-matrix.svg'));
      if(galleryMeta&&savedByName.has(galleryMeta.name)){
        const galleryBytes=await readFile(savedByName.get(galleryMeta.name).path);
        const pngs=parseGalleryPngs(galleryBytes);
        const ordered=[primary.scenario,...related];
        const extracted=[];
        for(let i=0;i<Math.min(pngs.length,ordered.length);i++){
          const scenario=ordered[i];
          const png=pngs[i];
          const dims=pngDimensions(png);
          const file=path.join(dir,`${safeStem(scenario.id)}_full.png`);
          await writeFile(file,png);
          const record={scenarioId:scenario.id,caseKey:i===0?group.primary:group.related[i-1],path:file,sha256:sha(png),bytes:png.length,dimensions:dims};
          if(dims?.width!==target.width||dims?.height!==target.height)record.dimensionMismatch={expected:{width:target.width,height:target.height},actual:dims};
          extracted.push(record);
        }
        if(pngs.length!==ordered.length)run.unresolved.push({kind:'scenario-gallery-image-count',group:group.key,target,expected:ordered.length,actual:pngs.length,sourceArtifact:galleryMeta.name});
        rendered.row.extractedFullImages=extracted;
      }else run.unresolved.push({kind:'scenario-gallery-missing',group:group.key,target});
      const layoutMeta=metas.find(m=>m.name.endsWith('-layout.json'));
      if(layoutMeta&&savedByName.has(layoutMeta.name)){
        try{const bounds=compactBounds(await readFile(savedByName.get(layoutMeta.name).path));const boundsPath=path.join(dir,'click_bounds.json');await jsonWrite(boundsPath,bounds);rendered.row.clickBoundsPath=boundsPath;rendered.row.clickableVisibleCount=bounds.visibleClickableCount;rendered.row.disabledVisibleButtonCount=bounds.visibleDisabledButtonCount;}
        catch(error){run.unresolved.push({kind:'layout-parse',group:group.key,target,error:String(error)});}
      }
      rendered.row.artifacts=saved;
      const stateResult={group:group.key,target,primary:primary.facts,related:related.map(s=>({id:s.id,description:s.description,elementStates:s.elementStates??{},date:s.date??null,controls:s.controls??null})),row:rendered.row};
      run.renders.push(stateResult);
      artifactOutput.renders.push({group:group.key,target,artifacts:saved});
      await jsonWrite(path.join(out,'results',`${stem}_manifest.json`),stateResult);
      await jsonWrite(path.join(out,'run_manifest.partial.json'),run);
    }
  }
  run.sourceFilesAfter=await sourceIdentity();
  await jsonWrite(path.join(out,'run_manifest.json'),run);
  await jsonWrite(path.join(out,'artifact_manifest.json'),artifactOutput);
  process.stdout.write(`[complete] inspection=${run.inspect?.code??'missing'} renders=${run.renders.length} unresolved=${run.unresolved.length} runtime=${runtimeRoot}\n`);
} finally {
  try{await client.close();}catch{}
  const tempBase=path.resolve(tmpdir());
  const tempTarget=path.resolve(runtimeRoot);
  if(tempTarget.toLowerCase().startsWith((tempBase+path.sep).toLowerCase())&&path.basename(tempTarget).startsWith('camp-admin-gui-35-')){
    try{await (await import('node:fs/promises')).rm(tempTarget,{recursive:true,force:true});}catch(error){process.stderr.write(`Temporary MCP directory cleanup failed: ${String(error)}\n`);}
  }
}




