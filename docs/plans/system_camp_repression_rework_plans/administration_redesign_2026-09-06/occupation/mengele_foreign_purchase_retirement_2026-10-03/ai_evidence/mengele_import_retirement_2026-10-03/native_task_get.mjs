import { Client } from "file:///C:/Users/klimp/Documents/Projects/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js";
import { StdioClientTransport } from "file:///C:/Users/klimp/Documents/Projects/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js";
const transport = new StdioClientTransport({
  command: "C:\\Program Files\\nodejs\\node.exe",
  args: ["C:\\Users\\klimp\\AppData\\Roaming\\npm\\node_modules\\hoi4-agent-tools\\dist\\bin\\stdio.js"],
  env: { ...process.env, HOI4_AGENT_CONFIG: "C:\\Users\\klimp\\AppData\\Roaming\\hoi4-agent-tools\\config.json" }
});
const client = new Client({ name: "chaosx-ai-probability-auditor", version: "1.0.0" }, { capabilities: { tasks: { list: {}, cancel: {} } } });
const taskId = "mod_chaos_redux_ea3b2d67c2c0:job_7feeb5acb54a43fde08ab09950abd625fc7bd5a71590a8af5928c56c2eef60ad";
try {
  await client.connect(transport);
  const task = await client.experimental.tasks.getTask(taskId);
  console.log(JSON.stringify({ phase: "tasks/get", task }));
  if (task.status === "completed") {
    const result = await client.experimental.tasks.getTaskResult(taskId);
    console.log(JSON.stringify({ phase: "tasks/result", result }));
  }
} catch (error) {
  console.log(JSON.stringify({ phase: "fatal", error: { code: error?.code ?? null, message: String(error?.message ?? error) } }));
} finally {
  await client.close().catch(() => {});
}
