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
const runtime = await mkdtemp(path.join(os.tmpdir(), 'soviet-famine-task-'));
await mkdir(path.join(runtime, 'storage'), { recursive: true });
const workspaceId = 'camp_famine_oct3';
const config = { version: 1, serverStateRoot: path.join(runtime, 'state'), storageRoots: [path.join(runtime, 'storage')], workspaces: [{ id: workspaceId, name: 'Soviet famine probability audit', root: mod, gameRoot: 'C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV', artifactRoot: path.join(runtime, 'storage/artifacts'), cacheRoot: path.join(runtime, 'storage/cache') }] };
const configPath = path.join(runtime, 'config.json');
await writeFile(configPath, JSON.stringify(config));
await writeFile(path.join(evidence, 'probability-runtime.json'), JSON.stringify({runtime, configPath, workspaceId, clientCapabilitiesRequested: {tasks:{list:{},cancel:{},requests:{tools:{call:{}}}}}}, null, 2));
const client = new Client({ name: 'soviet-famine-probability-audit', version: '1' });
client.registerCapabilities({ tasks: { list: {}, cancel: {}, requests: { tools: { call: {} } } } });
const transport = new StdioClientTransport({ command: process.execPath, args: [path.join(pkg, 'dist/bin/stdio.js'), '--config', configPath], cwd: pkg, stderr: 'pipe' });
await client.connect(transport);
const server = { version: client.getServerVersion(), capabilities: client.getServerCapabilities() };
const tools = await client.listTools();
const route = tools.tools.find(t => t.name === 'hoi4.probability_inspect');
await writeFile(path.join(evidence, 'probability-task-negotiation.json'), JSON.stringify({server,clientTasksRequested:{list:{},cancel:{},requests:{tools:{call:{}}}},probabilityInspectSchema:route?.inputSchema??null,tools:tools.tools.filter(t=>t.name.startsWith('hoi4.probability_')).map(t=>t.name)}, null, 2));
const args = { workspaceId, adapter: 'event_option_ai_chance', source: { path: 'events/soviet_gulag.txt', snapshotPath: 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03/before_soviet_gulag.txt', expectedSourceHash: '773c927aee19767055da26922c72b88aaa30335b751ec8b58423615081937a31' } };
const log = [];
try {
  console.log('calling task-enabled hoi4.probability_inspect on immutable baseline');
  const stream = client.experimental.tasks.callToolStream({ name: 'hoi4.probability_inspect', arguments: args }, undefined, { task: { ttl: 86400000 }, timeout: 180000 });
  for await (const message of stream) {
    if (message.type === 'taskCreated') {
      log.push({type:message.type,task:message.task});
      await writeFile(path.join(evidence, 'baseline-probability-task.json'), JSON.stringify({task:message.task,server,clientCapabilitiesRequested:{tasks:{list:{},cancel:{},requests:{tools:{call:{}}}}},source:args.source}, null, 2));
      console.log('TASK_CREATED', JSON.stringify(message.task));
    } else if (message.type === 'taskStatus') {
      log.push({type:message.type,task:message.task});
      await writeFile(path.join(evidence, 'baseline-probability-task-status.json'), JSON.stringify(log, null, 2));
      console.log('TASK_STATUS', JSON.stringify(message.task));
    } else if (message.type === 'result') {
      await writeFile(path.join(evidence, 'baseline-probability-inspect.json'), JSON.stringify(message.result, null, 2));
      console.log('TASK_RESULT', JSON.stringify({isError:message.result.isError??false,structuredContent:message.result.structuredContent??null,contentPreview:message.result.content?.filter(c=>c.type==='text').map(c=>c.text.slice(0,4000))},null,2));
    } else if (message.type === 'error') {
      await writeFile(path.join(evidence, 'baseline-probability-inspect-error.txt'), String(message.error?.stack ?? message.error));
      console.error('TASK_ERROR', message.error?.stack ?? message.error);
    }
  }
} catch (error) {
  await writeFile(path.join(evidence, 'baseline-probability-inspect-error.txt'), String(error?.stack ?? error));
  console.error('CLIENT_ERROR', error?.stack ?? error);
  process.exitCode = 1;
} finally { await writeFile(path.join(evidence, 'baseline-probability-task-log.json'), JSON.stringify(log, null, 2)); await client.close(); }
