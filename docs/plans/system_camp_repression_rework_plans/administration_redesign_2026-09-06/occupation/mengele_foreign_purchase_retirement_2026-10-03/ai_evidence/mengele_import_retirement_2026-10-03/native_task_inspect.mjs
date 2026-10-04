import { Client } from "file:///C:/Users/klimp/Documents/Projects/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js";
import { StdioClientTransport } from "file:///C:/Users/klimp/Documents/Projects/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js";
const transport = new StdioClientTransport({
  command: "C:\\Program Files\\nodejs\\node.exe",
  args: ["C:\\Users\\klimp\\AppData\\Roaming\\npm\\node_modules\\hoi4-agent-tools\\dist\\bin\\stdio.js"],
  env: { ...process.env, HOI4_AGENT_CONFIG: "C:\\Users\\klimp\\AppData\\Roaming\\hoi4-agent-tools\\config.json" }
});
const client = new Client({ name: "chaosx-ai-probability-auditor", version: "1.0.0" }, { capabilities: { tasks: { list: {}, cancel: {} } } });
try {
  await client.connect(transport);
  const tool = (await client.listTools()).tools.find(value => value.name === "hoi4.probability_inspect");
  console.log(JSON.stringify({ phase: "initialized", serverVersion: client.getServerVersion(), serverTaskCapabilities: client.getServerCapabilities()?.tasks ?? null, clientTaskCapabilities: { list: true, cancel: true }, probabilityInspectExecution: tool?.execution ?? null }));
  const stream = client.experimental.tasks.callToolStream({
    name: "hoi4.probability_inspect",
    arguments: {
      workspaceId: "current",
      adapter: "decision_ai_will_do",
      source: {
        path: "common/decisions/germany_mengele_decisions.txt",
        snapshotPath: "docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/before_germany_mengele_decisions.txt",
        expectedSourceHash: "c9c32f368baf263b76a013dee17508463ba330efb66ed55cf7343bd77c4e31b4"
      },
      candidatePool: ["import_subjects_from_japanese_china", "import_subjects_from_india", "import_subjects_from_africa"]
    }
  }, undefined, { task: { ttl: 1800000, pollInterval: 2000 }, timeout: 60000, maxTotalTimeout: 1800000 });
  for await (const message of stream) {
    if (message.type === "taskCreated") console.log(JSON.stringify({ phase: "taskCreated", task: message.task }));
    else if (message.type === "taskStatus") console.log(JSON.stringify({ phase: "taskStatus", task: message.task }));
    else if (message.type === "result") console.log(JSON.stringify({ phase: "result", result: message.result }));
    else if (message.type === "error") console.log(JSON.stringify({ phase: "error", error: { code: message.error.code, message: message.error.message } }));
  }
} catch (error) {
  console.log(JSON.stringify({ phase: "fatal", error: { code: error?.code ?? null, message: String(error?.message ?? error) } }));
} finally {
  await client.close().catch(() => {});
}
