import { Client } from 'file:///C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.8/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js';
import { StdioClientTransport } from 'file:///C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.8/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
const client = new Client({name:'chaos-redux-qa-artifact-reader',version:'1.0.0'});
const transport = new StdioClientTransport({command:'C:/Program Files/nodejs/node.exe',args:['C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.8/node_modules/hoi4-agent-tools/dist/bin/stdio.js'],cwd:process.cwd(),stderr:'pipe'});
try {
 await client.connect(transport);
 const result = JSON.parse(await readFile(new URL('./gui_post_repair_result.json',import.meta.url),'utf8'));
 const artifacts = result.structuredContent.artifacts;
 await mkdir(new URL('./gui_post_repair_artifacts/',import.meta.url),{recursive:true});
 for (const artifact of artifacts.filter(a=>/cropped.png|click-regions.png/.test(a.name))) {
  const response=await client.readResource({uri:artifact.uri});
  for (const content of response.contents) {
   const bytes=Buffer.from(content.blob,'base64');
   await writeFile(new URL('./gui_post_repair_artifacts/'+artifact.name,import.meta.url),bytes);
   console.log(JSON.stringify({name:artifact.name,bytes:bytes.length,metadata:content._meta}));
  }
 }
} finally { await client.close(); }
