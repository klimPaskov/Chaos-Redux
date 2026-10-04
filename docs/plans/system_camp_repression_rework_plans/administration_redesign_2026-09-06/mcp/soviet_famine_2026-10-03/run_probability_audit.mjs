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
const runtime = await mkdtemp(path.join(os.tmpdir(), 'soviet-famine-retry-'));
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
const route = tools.tools.find(t => t.name.endsWith('probability_inspect'));
await writeFile(path.join(evidence, 'probability-server-live.json'), JSON.stringify({ ...server, probabilityInspectSchema: route?.inputSchema ?? null, probabilityToolNames: tools.tools.filter(t => t.name.includes('probability_')).map(t=>t.name) }, null, 2));
const args = { workspaceId, adapter: 'event_option_ai_chance', source: { path: 'events/soviet_gulag.txt', snapshotPath: 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03/before_soviet_gulag.txt', expectedSourceHash: '773c927aee19767055da26922c72b88aaa30335b751ec8b58423615081937a31' } };
try {
  console.log('calling hoi4.probability_inspect on immutable baseline path');
  const result = await client.callTool({ name: 'hoi4.probability_inspect', arguments: args }, undefined, { timeout: 180000 });
  await writeFile(path.join(evidence, 'baseline-probability-inspect.json'), JSON.stringify(result, null, 2));
  const content = result.content?.filter(c=>c.type==='text').map(c=>c.text.slice(0,5000));
  console.log(JSON.stringify({isError: result.isError ?? false, structuredContent: result.structuredContent ?? null, contentPreview: content}, null, 2));
} catch (error) {
  await writeFile(path.join(evidence, 'baseline-probability-inspect-error.txt'), String(error?.stack ?? error));
  console.error('MCP_CALL_ERROR', error?.stack ?? error);
  process.exitCode = 1;
} finally { await client.close(); }

