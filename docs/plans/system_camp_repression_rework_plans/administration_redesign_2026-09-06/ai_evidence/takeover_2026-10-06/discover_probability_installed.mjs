import {createRequire} from 'node:module';
import {readFile, writeFile} from 'node:fs/promises';
const pkg = 'C:/Users/klimp/Documents/Projects/hoi4-agent-tools';
const require = createRequire(pkg + '/package.json');
const {Client} = require('@modelcontextprotocol/sdk/client/index.js');
const {StdioClientTransport} = require('@modelcontextprotocol/sdk/client/stdio.js');
const repo = 'C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux';
const evidence = repo + '/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/ai_evidence/takeover_2026-10-06';
const config = repo + '/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_ambiguity_mcp_2026-10-03/config.json';
const server = 'C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js';
const client = new Client({name:'camp-takeover-probability-audit-readonly', version:'1'});
const transport = new StdioClientTransport({command:process.execPath, args:[server,'--config',config], cwd:pkg, stderr:'pipe'});
transport.stderr?.on('data', d => process.stderr.write(d));
try {
  await client.connect(transport);
  const listing = await client.listTools();
  const probability = listing.tools.filter(t => /^hoi4\.probability_(inspect|evaluate|sweep|compare|simulate|sequence|render)$/.test(t.name));
  const health = listing.tools.filter(t => /(?:health|ping|status|version)/i.test(t.name));
  const record = {
    clientName:'camp-takeover-probability-audit-readonly',
    transport:'stdio',
    configuredProcess:server,
    packageRoot:pkg,
    configPath:config,
    workspaceId:'camp_origin_architecture_oct3',
    serverVersion:client.getServerVersion(),
    serverCapabilities:client.getServerCapabilities(),
    sdkVersion:JSON.parse(await readFile(pkg+'/package.json','utf8')).dependencies['@modelcontextprotocol/sdk'],
    probabilitySchemas:probability,
    healthRouteSchemas:health,
    taskNegotiation:'Not requested; this audit uses only synchronous read-only domain tools.'
  };
  await writeFile(evidence+'/installed_probability_client_schemas.json', JSON.stringify(record,null,2));
  const inspect = await client.callTool({
    name:'hoi4.probability_inspect',
    arguments:{workspaceId:'camp_origin_architecture_oct3', adapter:'decision_ai_will_do', source:{path:'common/decisions/genocide_crisis_decisions.txt'}}
  }, undefined, {timeout:60000});
  record.initialInspect = inspect;
  await writeFile(evidence+'/installed_probability_client_schemas.json', JSON.stringify(record,null,2));
  console.log(JSON.stringify({server:record.serverVersion, capabilities:record.serverCapabilities, probabilityTools:probability.map(t=>t.name), healthTools:health.map(t=>t.name), inspectStatus:inspect.structuredContent?.status, inspectCode:inspect.structuredContent?.code, artifacts:inspect.structuredContent?.artifacts, blockers:inspect.structuredContent?.blockers}));
} finally {
  await client.close();
}
