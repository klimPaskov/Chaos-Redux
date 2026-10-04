import {createRequire} from 'node:module';
import {readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
const pkg='C:/Users/klimp/Documents/Projects/hoi4-agent-tools';const require=createRequire(path.join(pkg,'package.json'));
const {Client}=require('@modelcontextprotocol/sdk/client/index.js');const {StdioClientTransport}=require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence='docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';const runtime=JSON.parse(await readFile(path.join(evidence,'probability-runtime.json'),'utf8'));
const client=new Client({name:'soviet-famine-source-reference-reads',version:'1'});const transport=new StdioClientTransport({command:process.execPath,args:[path.join(pkg,'dist/bin/stdio.js'),'--config',runtime.configPath],cwd:pkg,stderr:'pipe'});await client.connect(transport);
const calls=[
 ['ai-modding-chance','hoi4.reference_read',{id:'ab2b62a1e95fe5c84560ceedca6723cea6918faf69b08fd399709a2afbf8efe6',revision:'917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818',startLine:26,maxLines:16}],
 ['decision-modding-ai','hoi4.reference_read',{id:'151bbd3b6a875558e43f67a1daa1288c5904dfbedfa09e3fca2e5e42b8ccc58f',revision:'7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162',startLine:357,maxLines:20}],
 ['vanilla-decision-gates','hoi4.reference_read',{id:'c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58',revision:'5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019',startLine:1,maxLines:46}]
];
try{const results=await Promise.allSettled(calls.map(async([label,name,args])=>{const r=await client.callTool({name,arguments:{workspaceId:runtime.workspaceId,...args}},undefined,{timeout:60000});await writeFile(path.join(evidence,label+'-reference-read.json'),JSON.stringify(r,null,2));return {label,isError:r.isError??false,data:r.structuredContent?.data??null};}));for(const item of results)console.log(JSON.stringify(item));}finally{await client.close();}
