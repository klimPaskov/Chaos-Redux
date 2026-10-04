import { createRequire } from 'node:module';
import { readFile, writeFile, mkdir, mkdtemp } from 'node:fs/promises';
import path from 'node:path';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
const out = path.dirname(fileURLToPath(import.meta.url));
const phase = process.argv[2] ?? 'before';
const pkg = 'C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const serverPkg = 'C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools';
const mod = 'C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const require = createRequire(path.join(pkg,'package.json'));
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { StdioClientTransport } = require('@modelcontextprotocol/sdk/client/stdio.js');
let runtime;
try { runtime = JSON.parse(await readFile(path.join(out,'runtime.json'),'utf8')); }
catch { const root = await mkdtemp(path.join(tmpdir(),'camp-origin-gui-')); runtime={root,configPath:path.join(root,'config.json'),workspaceId:'camp_origin_gui_oct3'}; await mkdir(path.join(root,'storage'),{recursive:true}); await writeFile(runtime.configPath,JSON.stringify({version:1,serverStateRoot:path.join(root,'state'),storageRoots:[path.join(root,'storage')],workspaces:[{id:runtime.workspaceId,name:'Camp origin Records preview',root:mod,gameRoot:'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV',artifactRoot:path.join(root,'storage/artifacts'),cacheRoot:path.join(root,'storage/cache')}]})); await writeFile(path.join(out,'runtime.json'),JSON.stringify(runtime,null,2)); }
const client = new Client({name:'camp-origin-gui-preview',version:'1'});
const transport = new StdioClientTransport({command:process.execPath,args:[path.join(serverPkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:serverPkg,stderr:'pipe'});
transport.stderr?.on('data',chunk=>process.stderr.write(chunk));
await client.connect(transport);
const schema = await client.listTools();
await writeFile(path.join(out,phase+'-server.json'),JSON.stringify({version:client.getServerVersion(),capabilities:client.getServerCapabilities(),clientTasksRequested:false,tools:schema.tools.filter(t=>/gui_|reference_|source_lookup|script_validate/.test(t.name))},null,2));
const files=['interface/camp_repression_ledger.gui','common/scripted_guis/camp_repression_ledger_scripted_gui.txt','common/scripted_effects/camp_administration_ui_effects.txt','common/scripted_localisation/camp_administration_ui_localisation.txt','localisation/english/camp_administration_ui_l_english.yml'];
const identities=[];
for(const f of files){const b=await readFile(path.join(mod,f));identities.push({path:f,sha256:createHash('sha256').update(b).digest('hex')});if(phase==='before')await writeFile(path.join(out,'before_'+path.basename(f)),b);}
await writeFile(path.join(out,phase+'-sources.json'),JSON.stringify(identities,null,2));
const scenario=JSON.parse(await readFile(path.join(out,'scenario.json'),'utf8'));
async function call(name,args,stem){ await writeFile(path.join(out,stem+'-request.json'),JSON.stringify({name,arguments:args},null,2)); console.log('start',stem); try {const r=await client.callTool({name,arguments:args},undefined,{timeout:120000,maxTotalTimeout:300000,resetTimeoutOnProgress:true,onprogress:()=>{}});await writeFile(path.join(out,stem+'-result.json'),JSON.stringify(r,null,2));console.log(stem,r.isError?'error':r.structuredContent?.code??'returned');for(const a of r.structuredContent?.artifacts??[]){const resource=await client.readResource({uri:a.uri});const b=Buffer.concat((resource.contents??[]).map(c=>c.blob?Buffer.from(c.blob,'base64'):Buffer.from(c.text??'','utf8')));if(a.sha256&&createHash('sha256').update(b).digest('hex')!==a.sha256)throw new Error('Artifact checksum mismatch '+a.name);await writeFile(path.join(out,phase+'-'+a.name),b);}return r;}catch(e){await writeFile(path.join(out,stem+'-error.txt'),String(e.stack??e));console.log(stem,'failed',String(e.message??e));return null;}}
try {
 const args={workspaceId:runtime.workspaceId,windowName:'repression_ledger_window',scenario,generatedScenarios:{enabled:false}};
 const inspect=await call('hoi4.gui_inspect',args,phase+'-inspect');
 if(!inspect)await call('hoi4.gui_inspect',{...args,windowName:'camp_admin_records_panel'},phase+'-inspect-narrow');
 await call('hoi4.gui_render',{...args,states:['normal'],resolutions:[{width:1280,height:720,uiScale:1}]},phase+'-render-1280');
} finally { await client.close(); }
