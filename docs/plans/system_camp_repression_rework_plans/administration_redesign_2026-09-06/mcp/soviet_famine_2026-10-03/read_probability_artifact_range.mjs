import {createRequire} from 'node:module';
import {readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const result=JSON.parse(await readFile(path.join(evidence,'before-event-warning-probability-evaluate.json'),'utf8'));
const uri=result.structuredContent.artifacts[0].uri;
const client=new Client({name:'soviet-famine-probability-artifact-reader',version:'1'});const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});await client.connect(transport);
try{const templates=await client.listResourceTemplates();await writeFile(path.join(evidence,'artifact-resource-templates.json'),JSON.stringify(templates,null,2));const part=await client.readResource({uri:uri+'?offset=0&length=4096'},{timeout:30000});await writeFile(path.join(evidence,'before-event-warning-probability-resource-part-0.json'),JSON.stringify(part,null,2));console.log(JSON.stringify({uri,templates:templates.resourceTemplates?.filter(x=>x.uriTemplate?.includes('artifact')),contents:part.contents?.map(x=>({uri:x.uri,mimeType:x.mimeType,textLength:x.text?.length,blobLength:x.blob?.length,meta:x._meta,textStart:x.text?.slice(0,1200)}))},null,2));}catch(error){console.error(error?.stack??error);process.exitCode=1;}finally{await client.close();}
