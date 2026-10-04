import { createRequire } from 'node:module';
import { readFile, writeFile, mkdir, mkdtemp } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const pkg = 'C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require = createRequire(path.join(pkg, 'package.json'));
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { StdioClientTransport } = require('@modelcontextprotocol/sdk/client/stdio.js');
const mod = 'C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const out = path.dirname(fileURLToPath(import.meta.url));
const runtime = await mkdtemp(path.join(tmpdir(), 'camp-famine-mcp-'));
await mkdir(path.join(runtime, 'storage'), { recursive: true });
const workspaceId = 'camp_famine_oct3';
const config = { version: 1, serverStateRoot: path.join(runtime, 'state'), storageRoots: [path.join(runtime, 'storage')], workspaces: [{ id: workspaceId, name: 'Soviet famine source review', root: mod, gameRoot: 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV', artifactRoot: path.join(runtime, 'storage/artifacts'), cacheRoot: path.join(runtime, 'storage/cache') }] };
const configPath = path.join(runtime, 'config.json');
await writeFile(configPath, JSON.stringify(config));
const client = new Client({ name: 'camp-famine-reference-audit', version: '1' });
const transport = new StdioClientTransport({ command: process.execPath, args: [path.join(pkg, 'dist/bin/stdio.js'), '--config', configPath], cwd: pkg, stderr: 'pipe' });
await client.connect(transport);
const toolList = await client.listTools();
await writeFile(path.join(out, 'server.json'), JSON.stringify({ version: client.getServerVersion(), capabilities: client.getServerCapabilities(), clientTasksRequested: false, runtime, config, tools: toolList.tools }, null, 2));
const save = async (name, tool, args) => {
  const result = await client.callTool({ name: tool, arguments: { workspaceId, ...args } }, undefined, { timeout: 180000 });
  await writeFile(path.join(out, name + '.json'), JSON.stringify(result, null, 2));
  console.log(name, result.isError ? 'tool-error' : 'returned');
  return result.structuredContent ?? JSON.parse(result.content.find(c => c.type === 'text').text);
};
try {
  await save('complete-event-context', 'hoi4.reference_context', { surface: 'event', limit: 12 });
  const equipment = JSON.parse(await readFile(path.join(out, 'equipment-search.json'), 'utf8')).structuredContent.data.results;
  for (const item of equipment.filter(r => r.heading === 'has_equipment' || r.heading === 'Equipment')) {
    await save('read-equipment-' + item.source, 'hoi4.reference_read', { id: item.id, revision: item.revision, startLine: item.startLine, maxLines: 75 });
  }
  const options = await save('exact-option-search', 'hoi4.reference_search', { query: 'option', limit: 12, sources: ['wiki'] });
  for (const item of options.data.results.filter(r => r.title === 'Event modding' && r.startLine < 185 && r.endLine > 153)) {
    await save('read-options-' + item.startLine, 'hoi4.reference_read', { id: item.id, revision: item.revision, startLine: Math.max(item.startLine, 153), maxLines: 35 });
  }
  const costs = JSON.parse(await readFile(path.join(out, 'cost-search.json'), 'utf8')).structuredContent.data.results;
  for (const item of costs.filter(r => r.path.includes('decisions') || r.title === 'Decision modding')) {
    await save('read-costs-' + item.source + '-' + item.startLine, 'hoi4.reference_read', { id: item.id, revision: item.revision, startLine: item.startLine, maxLines: 80 });
  }
  await save('vanilla-cost', 'hoi4.source_lookup', { symbol: 'AFG_recruit_turkestan_legion', maxLines: 80, maxDefinitions: 1, maxReferences: 2 });
} finally { await client.close(); }
