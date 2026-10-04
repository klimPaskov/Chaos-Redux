import { createRequire } from 'node:module';
import { mkdir, mkdtemp, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
const pkg = 'C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require = createRequire(path.join(pkg, 'package.json'));
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { StdioClientTransport } = require('@modelcontextprotocol/sdk/client/stdio.js');
const mod = 'C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence = path.join(mod, 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03');
const runtime = await mkdtemp(path.join(os.tmpdir(), 'soviet-famine-prob-'));
await mkdir(path.join(runtime, 'storage'), { recursive: true });
const workspaceId = 'camp_famine_oct3';
const config = { version: 1, serverStateRoot: path.join(runtime, 'state'), storageRoots: [path.join(runtime, 'storage')], workspaces: [{ id: workspaceId, name: 'Soviet famine probability audit', root: mod, gameRoot: 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV', artifactRoot: path.join(runtime, 'storage/artifacts'), cacheRoot: path.join(runtime, 'storage/cache') }] };
const configPath = path.join(runtime, 'config.json');
await writeFile(configPath, JSON.stringify(config));
const client = new Client({ name: 'soviet-famine-probability-audit', version: '1' });
const transport = new StdioClientTransport({ command: process.execPath, args: [path.join(pkg, 'dist/bin/stdio.js'), '--config', configPath], cwd: pkg, stderr: 'pipe' });
await client.connect(transport);
const server = { version: client.getServerVersion(), capabilities: client.getServerCapabilities(), clientTasksRequested: false };
const tools = await client.listTools();
const routes = tools.tools.filter(t => /hoi4\\.probability_(inspect|evaluate|sweep|compare|render)$/.test(t.name));
await writeFile(path.join(evidence, 'probability-server.json'), JSON.stringify({ ...server, probabilityRoutes: routes }, null, 2));
const args = { workspaceId, adapter: 'event_option_ai_chance', source: { path: 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03/before_soviet_gulag.txt' } };
try {
  const result = await client.callTool({ name: 'hoi4.probability_inspect', arguments: args }, undefined, { timeout: 180000 });
  await writeFile(path.join(evidence, 'baseline-probability-inspect.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify({server, routeNames: routes.map(t=>t.name), isError: result.isError ?? false, structuredContent: result.structuredContent, contentPreview: result.content?.filter(c=>c.type==='text').map(c=>c.text.slice(0,7000))}, null, 2));
} finally { await client.close(); }
