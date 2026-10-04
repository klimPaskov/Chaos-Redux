import { createRequire } from 'node:module';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
const pkg = 'C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require = createRequire(path.join(pkg, 'package.json'));
const { Client } = require('@modelcontextprotocol/sdk/client/index.js');
const { StdioClientTransport } = require('@modelcontextprotocol/sdk/client/stdio.js');
const evidence = 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/mcp/soviet_famine_2026-10-03';
const runtimeInfo = JSON.parse(await readFile(path.join(evidence, 'probability-runtime.json'), 'utf8'));
const taskInfo = JSON.parse(await readFile(path.join(evidence, 'baseline-probability-task.json'), 'utf8'));
const taskId = taskInfo.task.taskId;
const client = new Client({ name: 'soviet-famine-probability-task-reader', version: '1' });
client.registerCapabilities({ tasks: { list: {}, cancel: {}, requests: { tools: { call: {} } } } });
const transport = new StdioClientTransport({ command: process.execPath, args: [path.join(pkg, 'dist/bin/stdio.js'), '--config', runtimeInfo.configPath], cwd: pkg, stderr: 'pipe' });
await client.connect(transport);
try {
  const result = await client.experimental.tasks.getTask(taskId, { timeout: 30000 });
  await writeFile(path.join(evidence, 'baseline-probability-task-poll.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
  if (['completed','failed','cancelled'].includes(result.task?.status)) {
    const payload = await client.experimental.tasks.getTaskResult(taskId, undefined, { timeout: 30000 });
    await writeFile(path.join(evidence, 'baseline-probability-inspect.json'), JSON.stringify(payload, null, 2));
    console.log('RESULT', JSON.stringify({isError:payload.isError??false,structuredContent:payload.structuredContent??null},null,2));
  }
} catch (error) {
  await writeFile(path.join(evidence, 'baseline-probability-task-poll-error.txt'), String(error?.stack ?? error));
  console.error(error?.stack ?? error);
  process.exitCode = 1;
} finally { await client.close(); }
