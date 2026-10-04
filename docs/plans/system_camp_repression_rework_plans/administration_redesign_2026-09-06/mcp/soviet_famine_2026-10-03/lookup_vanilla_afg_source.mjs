import {createRequire} from 'node:module';
import {mkdtemp,mkdir,readFile,writeFile} from 'node:fs/promises';
import os from 'node:os';import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const client=new Client({name:'soviet-famine-vanilla-source-lookup',version:'1'});const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});await client.connect(transport);
const args={workspaceId:runtime.workspaceId,symbol:'AFG_recruit_turkestan_legion',maxDefinitions:1,maxLines:80,maxReferences:1,includeReferences:false};
try{const result=await client.callTool({name:'hoi4.source_lookup',arguments:args},undefined,{timeout:60000});await writeFile(path.join(evidence,'vanilla-afg-source-lookup.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({isError:result.isError??false,structuredContent:result.structuredContent??null,content:result.content},null,2));}
catch(error){await writeFile(path.join(evidence,'vanilla-afg-source-lookup-error.txt'),String(error?.stack??error));console.error(error?.stack??error);process.exitCode=1;}
finally{await client.close();}
