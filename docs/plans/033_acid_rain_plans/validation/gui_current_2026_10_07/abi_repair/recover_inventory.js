// Read-only recovery inventory. No source/cache writes.
const fs=require('fs'),cp=require('child_process'),crypto=require('crypto');
const cache='C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts';
const scan=cp.spawnSync('rg',['-l','--glob','*.manifest.json','event033_abi_',cache],{encoding:'utf8',windowsHide:true,maxBuffer:30*1024*1024});
if(scan.status!==0&&scan.status!==1)throw Error(scan.stderr);
const groups=new Map();
for(const p of scan.stdout.trim().split(/\r?\n/).filter(Boolean)) {
 const m=JSON.parse(fs.readFileSync(p,'utf8')),rp=m.provenance?.renderProfile;
 const id=rp?.scenarioId;
 if(!id?.startsWith('event033_abi_'))continue;
 const key=id+'|'+rp.sourceRevision;
 const g=groups.get(key)||{scenarioId:id,sourceRevision:rp.sourceRevision,resolution:rp.resolution,uiScale:rp.uiScale,fidelity:rp.fidelity,artifacts:[]};
 const file=p.slice(0,p.lastIndexOf('/'))+'/'+m.name; // manifests use Windows backslashes from rg
 const actual=p.replace(/[\\/][^\\/]+$/,'')+'/'+m.name;
 if(!fs.existsSync(actual))throw Error('Missing artifact '+actual);
 const bytes=fs.readFileSync(actual),hash=crypto.createHash('sha256').update(bytes).digest('hex');
 if(hash!==m.sha256||bytes.length!==m.size)throw Error('Identity mismatch '+actual);
 const uri='hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/'+m.sha256+'/'+m.provenanceHash+'/'+encodeURIComponent(m.name);
 g.artifacts.push({name:m.name,sha256:m.sha256,size:m.size,mimeType:m.mimeType,uri,path:actual,manifestPath:p});
 if(m.name.endsWith('-scenario.json')) {
  const s=JSON.parse(bytes.toString('utf8')).scenario;
  g.outputFacts={front1x:s.variables['global.acid_rain_gui_front_1_marker_x'],storm1shown:s.variables['global.acid_rain_gui_superstorm_1_marker'],preparednessTooltip:s.values['This.GetAcidRainPreparednessTooltip']};
  g.fixtureStage=g.outputFacts.preparednessTooltip?.includes(' of 0.')?'before_outputs':'after_outputs';
 }
 if(m.name.endsWith('-source-graph.json')) {
  const source=JSON.parse(bytes.toString('utf8')).graph.sourceHashes;
  g.ownedSourceHashes=Object.fromEntries(Object.entries(source).filter(([k])=>/mod:(interface\/033_acid_rain\.(gui|gfx)|common\/scripted_(localisation|guis)\/033_acid_rain_)/.test(k)));
 }
 groups.set(key,g);
}
console.log(JSON.stringify([...groups.values()]));

