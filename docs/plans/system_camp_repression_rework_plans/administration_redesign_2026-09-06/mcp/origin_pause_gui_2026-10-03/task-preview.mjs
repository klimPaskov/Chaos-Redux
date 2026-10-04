// Native MCP task retry of the archived bounded Records fixture. No source mutation.
import {createRequire} from 'node:module';
import {readFile, writeFile} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const out=path.dirname(fileURLToPath(import.meta.url));
const narrow=process.argv[2]==='narrow';
const prefix=narrow?'native-narrow':'native';
const sdkRoot='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const serverRoot='C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools';
const mod='C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const require=createRequire(path.join(sdkRoot,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const runtime=JSON.parse(await readFile(path.join(out,'runtime.json'),'utf8'));
const scenario=JSON.parse(await readFile(path.join(out,'scenario.json'),'utf8'));
const client=new Client({name:'camp-origin-native-task-preview',version:'1'});
client.registerCapabilities({tasks:{list:{},cancel:{},requests:{tools:{call:{}}}}});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(serverRoot,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:serverRoot,stderr:'pipe'});
transport.stderr?.on('data',b=>process.stderr.write(b));
await client.connect(transport);
const schemas=await client.listTools();
await writeFile(path.join(out,prefix+'-server.json'),JSON.stringify({version:client.getServerVersion(),capabilities:client.getServerCapabilities(),clientTasksRequested:true,tools:schemas.tools.filter(t=>/gui_|job_/.test(t.name))},null,2));
const files=['interface/camp_repression_ledger.gui','common/scripted_guis/camp_repression_ledger_scripted_gui.txt','common/scripted_effects/camp_administration_ui_effects.txt','common/scripted_triggers/camp_administration_ui_triggers.txt','common/scripted_localisation/camp_administration_ui_localisation.txt','common/scripted_localisation/camp_administration_country_localisation.txt','localisation/english/camp_administration_ui_l_english.yml','localisation/english/camp_administration_country_l_english.yml'];
async function hashes(){return await Promise.all(files.map(async p=>({path:p,sha256:createHash('sha256').update(await readFile(path.join(mod,p))).digest('hex')})));}
await writeFile(path.join(out,prefix+'-sources-opening.json'),JSON.stringify(await hashes(),null,2));
async function task(name,args,stem){
  await writeFile(path.join(out,stem+'-request.json'),JSON.stringify({name,arguments:args},null,2));
  console.log('START',stem);
  let last='';
  for await(const message of client.experimental.tasks.callToolStream({name,arguments:args},undefined,{task:{ttl:86400000},timeout:180000})){
    if(message.type==='taskCreated'){
      await writeFile(path.join(out,stem+'-task.json'),JSON.stringify({task:message.task,args},null,2));
      console.log('TASK',message.task.taskId);
    } else if(message.type==='taskStatus'){
      const value=JSON.stringify(message.task);
      if(last!==value){last=value;await writeFile(path.join(out,stem+'-status.json'),value);console.log('STATUS',message.task.status,message.task.statusMessage??'');}
    } else if(message.type==='result'){
      await writeFile(path.join(out,stem+'-result.json'),JSON.stringify(message.result,null,2));
      console.log('RESULT',message.result.structuredContent?.code??message.result.isError);
      for(const artifact of message.result.structuredContent?.artifacts??[]){
        const resource=await client.readResource({uri:artifact.uri});
        const bytes=Buffer.concat((resource.contents??[]).map(c=>c.blob?Buffer.from(c.blob,'base64'):Buffer.from(c.text??'','utf8')));
        if(artifact.sha256&&createHash('sha256').update(bytes).digest('hex')!==artifact.sha256)throw new Error('Artifact identity mismatch '+artifact.name);
        await writeFile(path.join(out,'task-'+artifact.name),bytes);
      }
      return message.result;
    } else if(message.type==='error')throw message.error;
  }
}
try{
  const args={workspaceId:runtime.workspaceId,windowName:narrow?'camp_admin_records_panel':'repression_ledger_window',scenario,generatedScenarios:{enabled:false}};
  await task('hoi4.gui_inspect',args,prefix+'-inspect');
  await task('hoi4.gui_render',{...args,states:['normal'],resolutions:[{width:1280,height:720,uiScale:1}]},prefix+'-render-1280');
} catch(error){await writeFile(path.join(out,prefix+'-task-error.txt'),String(error.stack??error));console.error(error.stack??error);process.exitCode=1;}
finally{await writeFile(path.join(out,prefix+'-sources-closing.json'),JSON.stringify(await hashes(),null,2));await client.close();}
