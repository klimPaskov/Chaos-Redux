import { createRequire } from 'node:module';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const info=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const result=JSON.parse(await readFile(path.join(evidence,'baseline-probability-inspect.json'),'utf8'));
const uri=result.structuredContent.artifacts[0].uri;
const client=new Client({name:'soviet-famine-artifact-reader',version:'1'});
client.registerCapabilities({tasks:{list:{},cancel:{},requests:{tools:{call:{}}}}});
const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',info.configPath],cwd:pkg,stderr:'pipe'});
await client.connect(transport);
try {
 const resource=await client.readResource({uri},{timeout:30000});
 await writeFile(path.join(evidence,'baseline-probability-inspect-resource.json'),JSON.stringify(resource,null,2));
 console.log(JSON.stringify({uri,contents:resource.contents?.map(c=>({uri:c.uri,mimeType:c.mimeType,textLength:c.text?.length,blobLength:c.blob?.length})),isError:resource.isError??false},null,2));
} catch(error) { await writeFile(path.join(evidence,'baseline-probability-inspect-resource-error.txt'),String(error?.stack??error)); console.error(error?.stack??error); process.exitCode=1; }
finally {await client.close();}
