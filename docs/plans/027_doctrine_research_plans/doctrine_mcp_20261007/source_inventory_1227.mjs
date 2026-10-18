import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const out=path.dirname(fileURLToPath(import.meta.url));
const mod='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const game='C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV';
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(p,d.name)):[path.join(p,d.name)]);}
function blocks(text){
 const rows=[];const re=/^\s*([a-zA-Z0-9_]+)\s*=\s*\{/gm;let match;
 while((match=re.exec(text))){let i=re.lastIndex,depth=1,quoted=false,comment=false;
  for(;i<text.length&&depth;i++){const c=text[i];if(comment){if(c==='\n')comment=false;continue;}if(c==='"'&&text[i-1]!=='\\'){quoted=!quoted;continue;}if(quoted)continue;if(c==='#'){comment=true;continue;}if(c==='{')depth++;if(c==='}')depth--;}
  rows.push({id:match[1],startLine:text.slice(0,match.index).split('\n').length,endLine:text.slice(0,i).split('\n').length,source:text.slice(match.index,i)});re.lastIndex=i;
 }return rows;
}
const evidence={kind:'source inventory only, not MCP or native runtime proof',capturedAt:new Date().toISOString(),files:[],grand:[],subdoctrines:[],folders:[],tracks:[],referenceSections:[],preservation:[],gitHead:execFileSync('git',['rev-parse','HEAD'],{cwd:mod,encoding:'utf8',windowsHide:true}).trim()};
for(const kind of ['grand_doctrines','subdoctrines','folders','tracks']){
 const rel='common/doctrines/'+kind;const files=new Map();
 for(const [owner,root] of [['game',game],['mod',mod]]){const dir=path.join(root,rel);if(!fs.existsSync(dir))continue;for(const p of walk(dir).filter(p=>p.endsWith('.txt'))){const r=path.relative(root,p).replaceAll('\\','/');files.set(r,{owner,p,r});}}
 for(const {owner,p,r} of files.values()){
  const bytes=fs.readFileSync(p),text=bytes.toString('utf8');evidence.files.push({path:p,relativePath:r,owner,size:bytes.length,sha256:hash(bytes)});
  for(const b of blocks(text)){
   const field=k=>b.source.match(new RegExp('\\b'+k+'\\s*=\\s*([^\\n\\r#]+)'))?.[1].trim();
   const rewardMatch=b.source.match(/\brewards\s*=\s*\{/);let rewards=[];
   if(rewardMatch){const nested=blocks(b.source.slice(rewardMatch.index));if(nested[0])rewards=blocks(nested[0].source.slice(nested[0].source.indexOf('{')+1,-1)).map(x=>({id:x.id,mastery:x.source.match(/\bmastery\s*=\s*([^\s#}]+)/)?.[1],source:x.source}));}
   const row={...b,path:p,owner,sha256:hash(bytes),folder:field('folder'),track:field('track'),icon:field('icon'),rewards};
   evidence[kind==='grand_doctrines'?'grand':kind].push(row);
  }
 }
}
const owned=['common/scripted_effects/027_doctrine_research_effects.txt','common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt','common/scripted_triggers/027_doctrine_research_triggers.txt','common/script_constants/027_doctrine_research_constants.txt','common/scripted_effects/cbrn_doctrine_effects.txt','common/scripted_triggers/cbrn_doctrine_triggers.txt','interface/cbrn_doctrine.gfx','interface/countrytechtreeview.gfx'];
const sprites=new Map();
for(const [owner,root] of [['game',game],['mod',mod]]){
 for(const p of walk(path.join(root,'interface')).filter(p=>p.endsWith('.gfx'))){
  const bytes=fs.readFileSync(p),text=bytes.toString('utf8');
  const containers=blocks(text);
  for(const outer of containers){for(const b of blocks(outer.source.slice(outer.source.indexOf('{')+1,-1))){
   const id=b.source.match(/\bname\s*=\s*"([^"]+)"/)?.[1];if(!id)continue;
   const texture=b.source.match(/\btexturefile\s*=\s*"([^"]+)"/i)?.[1];
   sprites.set(id,{id,path:p,sourceSha256:hash(bytes),owner,source:b.source,texture});
  }}
 }
}
const requiredIcons=new Set([...evidence.grand,...evidence.subdoctrines].map(x=>x.icon));
for(const f of evidence.folders){const m=f.source.match(/ledger_gfx\s*=\s*(\S+)/);if(m)requiredIcons.add(m[1]);}
evidence.iconOwnership=[...requiredIcons].map(id=>{
 const sprite=sprites.get(id);if(!sprite)return {id,status:'unresolved sprite definition'};
 let texturePath;if(sprite.texture){for(const root of [mod,game]){const candidate=path.join(root,sprite.texture);if(fs.existsSync(candidate)){texturePath=candidate;break;}}}
 const b=texturePath?fs.readFileSync(texturePath):null;
 return {...sprite,texturePath,textureSize:b?.length,textureSha256:b?hash(b):null,status:b?'source owner and texture present':'unresolved texture'};
});
for(const rel of owned){const p=path.join(mod,rel),b=fs.readFileSync(p);evidence.files.push({path:p,size:b.length,sha256:hash(b)});}
for(const p of walk(path.join(mod,'docs/specs/027_doctrine_research_specs'))){const b=fs.readFileSync(p);evidence.files.push({path:p,size:b.length,sha256:hash(b),kind:'user acceptance source'});}
for(const [root,rel,startLine,endLine] of [[game,'documentation/effects_documentation.md',1477,1504],[game,'documentation/effects_documentation.md',7774,7805],[game,'documentation/triggers_documentation.md',4181,4199],[game,'common/doctrines/subdoctrines/_documentation.md',1,66],[mod,'paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md',425,444],[mod,'paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md',353,361],[mod,'paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md',25,45]]){
 const p=path.join(root,rel),b=fs.readFileSync(p);evidence.referenceSections.push({path:p,startLine,endLine,sha256:hash(b),source:b.toString('utf8').split(/\r?\n/).slice(startLine-1,endLine).join('\n')});
}
for(const row of evidence.files.filter(f=>f.owner==='game')){let before;try{before=execFileSync('git',['show','bf4fa8fea^:'+row.relativePath],{cwd:mod,windowsHide:true,stdio:['ignore','pipe','ignore']});}catch{}evidence.preservation.push({relativePath:row.relativePath,vanillaSha256:row.sha256,modOverrideAtBaseline:before!==undefined,meaning:'no current same-path mod override found, preservation source identity only, not tech_compare'});}
const rel='common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt';
const old=execFileSync('git',['show','bf4fa8fea^:'+rel],{cwd:mod,windowsHide:true,maxBuffer:4000000});
const cur=fs.readFileSync(path.join(mod,rel));
fs.writeFileSync(path.join(out,'real_before_exact_mastery_bf4fa8fea_parent_1227.txt'),old);
evidence.comparisonBaseline={revision:execFileSync('git',['rev-parse','bf4fa8fea^'],{cwd:mod,encoding:'utf8',windowsHide:true}).trim(),path:rel,beforeSha256:hash(old),beforeSize:old.length,currentSha256:hash(cur),currentSize:cur.length,different:!old.equals(cur),direction:'current source graph versus historical exact mastery helper overlay'};
fs.writeFileSync(path.join(out,'source_inventory_1227.json'),JSON.stringify(evidence,null,2));
console.log(JSON.stringify({grand:evidence.grand.length,subdoctrines:evidence.subdoctrines.length,folders:evidence.folders.length,tracks:evidence.tracks.length,icons:evidence.iconOwnership.length,unresolvedIcons:evidence.iconOwnership.filter(x=>x.status!=='source owner and texture present'),baseline:evidence.comparisonBaseline}));
