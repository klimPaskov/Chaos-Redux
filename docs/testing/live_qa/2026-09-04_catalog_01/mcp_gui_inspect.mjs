import { Client } from 'file:///C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.7/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js';
import { StdioClientTransport } from 'file:///C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.7/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js';
import { writeFile, readFile, mkdir } from 'node:fs/promises';

const client = new Client({ name: 'chaos-redux-startup-qa', version: '1.0.0' });
const transport = new StdioClientTransport({
  command: 'C:/Program Files/nodejs/node.exe',
  args: ['C:/Users/klimp/AppData/Local/hoi4-agent-tools/3.0.7/node_modules/hoi4-agent-tools/dist/bin/stdio.js'],
  cwd: process.cwd(),
  stderr: 'pipe',
});
try {
  await client.connect(transport);
  const operation = process.argv[2] || 'inspect';
  const argumentPath = process.argv[3];
  const suppliedArguments = argumentPath ? JSON.parse(await readFile(argumentPath, 'utf8')) : null;
  console.log(`Production MCP connected; ${operation} repression ledger.`);
  const result = await client.callTool({
    name: `hoi4.gui_${operation}`,
    arguments: suppliedArguments || {
      windowName: 'repression_ledger_window',
      generatedScenarios: { enabled: false },
      scenario: { id: 'startup_repression_overview', flags: { camp_ledger_tab_overview: true } },
    },
  }, undefined, { timeout: 1800000, onprogress: p => console.log(JSON.stringify(p)) });
  await writeFile(new URL(`./mcp_gui_${operation}_result.json`, import.meta.url), JSON.stringify(result, null, 2));
  await mkdir(new URL(`./mcp_${operation}_artifacts/`, import.meta.url), { recursive: true });
  for (const artifact of result.structuredContent?.artifacts || []) {
    const resource = await client.readResource({ uri: artifact.uri });
    for (const content of resource.contents || []) {
      const bytes = content.blob ? Buffer.from(content.blob, 'base64') : content.text;
      if (bytes !== undefined) await writeFile(new URL(`./mcp_${operation}_artifacts/${artifact.name}`, import.meta.url), bytes);
    }
  }
  console.log(JSON.stringify({status:result.structuredContent?.status,code:result.structuredContent?.code,artifacts:result.structuredContent?.artifacts,blockers:result.structuredContent?.blockers,diagnostics:result.structuredContent?.diagnostics}));
} finally {
  await client.close();
}
