# Repo Explorer Handoff

## Scope read
- Parent task: Recover the missing live HOI4 MCP evidence route for the pending Chaos Redux CBRN work, identify the installed launcher and package, and check whether a standalone Technology Tree Viewer is installed.
- Explicit constraints: Read-only exploration; no gameplay or config edits, no shared-service restart, no game launch, no log searches, no credential reads, and no external messages. The parent later authorized an isolated temporary JSON config and stdio client; this agent did not create that config or launch a client.
- Files or ids requested: Current `hoi4-agent-tools` launcher, startup and workspace configuration behavior, MCP version/health/schema inspection, the first weighted-logic route and its request schema, and standalone viewer availability.
- Skills or docs read: `AGENTS.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; `docs/runtimes.md`; `docs/systems/hoi4_agent_tools_mcp_integration.md`; installed package `docs/setup.md`, `docs/http.md`, `docs/reference.md`, `docs/development.md`, and `docs/jobs.md`.

## Primary findings
- The current live `ALL_TOOLS` has no `mcp__hoi4_agent_tools__*` routes. The HOI4-related tools available here are under `mcp__blender_hoi4__*`; no live HOI4 version, health, schema, source, probability, or technology call was possible. No MCP artifact URI or weighted-logic result was produced.
- Both project and global Codex configs name `hoi4-agent-tools.cmd`. The project config pins the Chaos Redux working directory and allows 120 seconds for startup and 600 seconds per tool call. The launcher resolves to `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd`, which forwards to the installed global package's `dist\bin\stdio.js`; installed package version is 3.6.0.
- The installed package source defines the read-only probability and technology routes, but package code and version are not live-service evidence. MCP-level `initialize` reports the connected server's name/version, `ping` checks protocol responsiveness, and `tools/list` returns live schemas. No dedicated `hoi4.health` tool or stdio health command was found.
- Do not launch the configured shared service config for this probe. Its service config uses shared state under `%LOCALAPPDATA%\hoi4-agent-tools\state`, shared workspace storage under `%LOCALAPPDATA%\hoi4-agent-tools\workspaces`, and `modRoots` set to the parent `...\Hearts of Iron IV\mod` directory. Startup discovers its mod children and transaction-recovers every workspace before MCP negotiation; an `applying` or `rolling_back` journal can restore earlier source bytes.
- Isolated startup is supported with a separate config carrying a new absolute `serverStateRoot`, a new absolute `workspaceStorageRoot`, and one explicit `workspaces` entry for the same Chaos Redux root, with `modRoots` omitted. `setup --init` cannot set a private `serverStateRoot`; its flags default that field to the shared per-user location. The parent approved an external temporary config for this evidence probe.
- The installed package contains no separate Technology Tree Viewer executable or package. Checks found no matching command, Windows uninstall entry, or global npm viewer package. This is a standalone-viewer package gap separate from the technology MCP routes.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `.codex/config.toml` | Project Codex registration and working directory. | `mcp_servers.hoi4_agent_tools` at line 12; command/cwd/timeouts at lines 13–16. |
| `C:\Users\klimp\.codex\config.toml` | Global Codex registration, which does not pin the project cwd. | Command and timeouts at lines 124–126. |
| `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd` | Exact configured launcher resolved from PATH. | Shim starts `node_modules\hoi4-agent-tools\dist\bin\stdio.js` and forwards arguments. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\package.json` | Installed package identity, version, CLI bins, and development-only Inspector reference. | `name`/`version` at lines 2/4; bins at lines 69–73; `inspector` script at line 106. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\bin\stdio.js` | Actual service startup ordering. | `createEngine()` runs at line 7; `serveNegotiatedStdio()` follows at line 23. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\runtime.js` | Config selection and automatic local workspace defaults. | `--config`, `HOI4_AGENT_CONFIG`, and default path at lines 9–24; auto roots/workspace and engine creation at lines 167–240. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\core\configuration.js` | Supported server and workspace config fields. | Workspace registration begins at line 77; private `serverStateRoot` at line 138; `workspaceStorageRoot` and `workspaces` at lines 175–177; writable-mod private-state requirement at lines 305–310. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\core\workspace.js` | Workspace discovery, storage roots, and `current` alias resolution. | `WorkspaceResolver.create()` at lines 175–228; current-workspace resolution at lines 236–251; private storage defaulting at lines 305–315; mod-root child discovery at lines 323–365. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\core\engine.js` | Work done before the server accepts MCP requests. | Engine constructs caches/scanner at lines 95–123; `initialize()` only transaction-recovers each workspace at lines 125–129. It does not call the workspace scanner. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\core\transactions.js` | Startup recovery can affect workspace source. | `recover()` scans journal directories at lines 578–625; interrupted `applying`/`rolling_back` transactions call recovery; restoration and journal update are at lines 557–575. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\core\domain-scan-patterns.js` | Bounds a source-specific probability scan. | `probabilityDomainScanPatterns()` at lines 41–77 uses the exact requested source paths plus shared scripted effects, triggers, constants, and MTTH; no source path selects the broader weighted-source patterns. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\schemas\common.js` and `schemas\probability-requests.js` | Exact `probability_inspect` arguments. | `workspaceId` defaults to `current` at `common.js` lines 3–6; inspect schema at `probability-requests.js` lines 27–45 accepts a nested `source` object. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\schemas\probability.js` | Source selector path constraints. | `probabilitySourceSchema` at lines 263–283 supports an exact workspace-relative `path`; snapshots require additional path/hash fields. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\mcp\tools\probability.js` | Confirms package-level probability route and read-only annotation. | `hoi4.probability_inspect` at lines 82–87. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\mcp\tools\technology.js` | Confirms package-level technology route names. | `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` at lines 96, 104, and 112. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\mcp\server\create-modern-operations.js` and `version.js` | Confirms live protocol metadata and `tools/list` implementation in the installed package. | `serverInfo` uses package name/version at line 56; `tools/list` registers schemas at lines 67–75; package version is `3.6.0` at `version.js` line 3. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\node_modules\@modelcontextprotocol\sdk\dist\esm\client\index.d.ts` and `client\stdio.d.ts` | Existing MCP client API, with no project code or package install required. | `Client.connect()` automatically initializes; `getServerVersion()`, `ping()`, `listTools()`, and `callTool()` are exposed. `StdioServerParameters` accepts command, args, env, cwd, and stderr. SDK version is 1.30.0. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\dist\bin\setup.js` | Existing package CLI diagnostics and config helpers. | `--diagnose` reports installed version and workspace access at lines 111–114 and 174–202; `--init` supports `--config`, `--mod-root`, `--game-root`, and `--workspace-storage-root` at lines 111 and 244; no `--server-state-root` exists; client config output binds custom config through `HOI4_AGENT_CONFIG` at lines 217–236. |
| `C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\docs\setup.md`, `docs\http.md`, and `docs\reference.md` | Document setup arguments, separate state/storage roots, and default local references. | Setup docs cover custom config paths and `--workspace-storage-root`; HTTP example shows `serverStateRoot`/`workspaceStorageRoot`; reference docs map game documentation to `gameRoot`, wiki to `modRoot\paradox_wiki`, and script docs to `modRoot\script_docs`. |
| `docs/runtimes.md` and `docs/systems/hoi4_agent_tools_mcp_integration.md` | Repository MCP registration and runtime distinctions. | DSH registration belongs to an active profile at `runtimes.md` lines 56–79; integration lists technology and probability routes at lines 24–35 and explains missing-tool troubleshooting at line 76. `DSH_HOME` was unset in this process. |
| `AGENTS.md` and `.agents/skills/chaos-redux-subagents/SKILL.md` | Required evidence boundaries. | `AGENTS.md` lines 88–104 requires live MCP evidence and standalone viewer verification; skill lines 281–297 separates tool exposure, server health, schemas, and viewer availability and requires probability analysis through the auditor. |

## Existing patterns

The repository expects the `hoi4_agent_tools` MCP server key and direct `mcp__hoi4_agent_tools__hoi4_*` methods. Its integration document lists read-only technology tools (`tech_inspect`, `tech_render`, `tech_compare`) and weighted tools (`probability_inspect`, `probability_evaluate`, `probability_sweep`, `probability_simulate`, `probability_sequence`, `probability_compare`, `probability_render`). The installed package registers these definitions and provides JSON schemas through MCP `tools/list`, but the current agent session exposes none of them.

The installed SDK client is already present as a production dependency. `Client.connect()` automatically sends `initialize` followed by `notifications/initialized`; the first initialize selects the legacy stdio path in `serveNegotiatedStdio()`. The read-only probe needs only `getServerVersion()`, `ping()`, `listTools()`, and one `callTool()`; there is no need to negotiate or call native tasks.

The package's local `setup --diagnose` command reports its package version and workspace permissions, but it does not connect to an MCP service or retrieve live schemas. It constructs workspace/server-state objects, so use it only with the private temporary config if a local preflight is desired. The development docs mention `npm run inspector`, but the installed global package lacks `scripts/run-inspector.ts` and the Inspector dependency; it is not a usable installed-package health route.

For an isolated JSON config, the exact `workspaceRegistrationSchema` fields are: required `id`, `name`, and `root`; `kind` defaults to `mod`; optional `gameRoot`, `dependencyRoots`, `dependencies`, `replacePaths`, `roots`, `artifactRoot`, `cacheRoot`, `fixtureRoot`, absolute `wikiRoot`, and absolute `scriptDocsRoot`. At top level, use required `version: 1`, a new private absolute `serverStateRoot`, a new private `workspaceStorageRoot`, the existing game path as `gameRoot`, and one explicit `workspaces` entry. Omit `modRoots` to avoid discovering sibling mods. When `workspaceStorageRoot` is set, the resolver places that registration's generated roots below `<workspaceStorageRoot>/<id>`. `current` maps to the sole mod workspace when the process cwd is inside it; using the explicit config ID in the request is clearer.

An MCP SDK transport can be configured with `command: "cmd.exe"`, `args: ["/d", "/c", "C:\\Users\\klimp\\AppData\\Roaming\\npm\\hoi4-agent-tools.cmd"]`, `cwd` set to the Chaos Redux root, and `env: { HOI4_AGENT_CONFIG: "<private config path>" }`. The SDK merges its safe default environment with this value. A 300,000 ms timeout is supported on `Client.connect()`; the SDK default is 60,000 ms. The package setup helper can print the same custom-config environment binding without editing a client config.

The optional `roots` object accepts `localisation`, `interface`, `gfx`, `map`, `focus`, `scriptedGui`, and `states`; defaults are `['localisation', 'localisation_synced']`, `['interface']`, `['gfx']`, `['map']`, `['common/national_focus']`, `['common/scripted_guis']`, and `['history/states']`. Top-level `gameRoot` is inherited when a mod registration omits its own `gameRoot`. `wikiRoot` and `scriptDocsRoot` are per-workspace absolute overrides, defaulting at use time to `<modRoot>\paradox_wiki` and `<modRoot>\script_docs`; there is no top-level `wikiRoot` field.

Example shape for the parent-approved temporary config (placeholders intentionally left for the parent to choose; this agent did not create it):

```json
{
  "version": 1,
  "serverStateRoot": "<new private absolute state directory>",
  "workspaceStorageRoot": "<new private absolute workspace directory>",
  "gameRoot": "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV",
  "workspaces": [
    {
      "id": "chaos_redux_probe",
      "name": "Chaos Redux evidence probe",
      "root": "<exact Chaos Redux root>",
      "kind": "mod"
    }
  ]
}
```

The SDK sequence is supported directly by its `Client` and `StdioClientTransport` API:

```js
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client({ name: "chaosx-evidence-probe", version: "1.0.0" });
const transport = new StdioClientTransport({
  command: "cmd.exe",
  args: ["/d", "/c", "C:\\Users\\klimp\\AppData\\Roaming\\npm\\hoi4-agent-tools.cmd"],
  cwd: "<exact Chaos Redux root>",
  env: { HOI4_AGENT_CONFIG: "<private config path>" }
});
await client.connect(transport, { timeout: 300_000 });
const serverInfo = client.getServerVersion();
await client.ping();
const { tools } = await client.listTools();
```

`connect()` sends the SDK's current `initialize` request with `protocolVersion`, `capabilities`, and `clientInfo`, then sends `notifications/initialized`; `listTools()` issues `tools/list`. Keep client capabilities empty for this probe and do not use experimental task APIs.

The initial probability request after live schema review is:

```js
await client.callTool({
  name: "hoi4.probability_inspect",
  arguments: {
    workspaceId: "chaos_redux_probe",
    source: { path: "<actual mod-relative weighted source path>" }
  }
});
```

The installed schema defaults `workspaceId` to `current`, accepts a source object, and marks this tool read-only. The source path must be exact and workspace-relative. Without `adapter`, inspection discovers the available compatible adapters. The actual Protective Aid source file/id was not included in this route-recovery prompt, so it remains a parent-supplied input.

## Vanilla or reference precedents

Not applicable: this handoff maps MCP service startup, client negotiation, package schemas, and viewer installation. It does not inspect HOI4 gameplay syntax or engine behavior.

## Likely edit order for the parent

1. Create the parent-approved temporary JSON config outside the repository with private server-state and workspace-storage roots, one explicit Chaos Redux workspace, the existing game root, and no `modRoots`.
2. Launch one SDK stdio client in the mod cwd with `HOI4_AGENT_CONFIG` bound to that temporary file and an extended initialize timeout. Read `getServerVersion()`, call `ping()`, and inspect `listTools()` for the exact live `hoi4.probability_inspect` schema. Do not call task methods or rewrites.
3. Call `hoi4.probability_inspect` with the actual mod-relative source path. Preserve result coverage, source revision/hash, and any artifact URI, then route the detailed probability pass through `chaosx_ai_probability_auditor`.
4. Record standalone Technology Tree Viewer absence separately from technology MCP route availability.

No game, gameplay, localization, asset, or existing configuration edits were made or proposed by this agent. No transaction journal contents were read. The parent owns the temporary external config and any live client invocation.

## Validation checks

- Confirmed the local and global Codex registrations by extracting only the HOI4 server command/cwd/timeout keys; no environment or credential fields were printed.
- `Get-Command hoi4-agent-tools.cmd` resolved the launcher to `C:\Users\klimp\AppData\Roaming\npm\hoi4-agent-tools.cmd`; `npm list --global hoi4-agent-tools --depth=0` reported `hoi4-agent-tools@3.6.0`.
- Inspected the exact installed shim, package entrypoints, config schema, startup ordering, transaction-recovery code, MCP route definitions, and SDK client declarations without executing the server.
- Checked PATH commands, Windows uninstall registry entries, and the global npm module directory for a standalone Technology Tree Viewer; none was found. The package's only bins are stdio, HTTP, and setup.
- No HOI4 MCP tool call was possible, so no live server version/health, current tool schema, source revision, scenario result, or artifact URI is claimed.

## Risks and blockers

### Confirmed blockers
- This session has no live `mcp__hoi4_agent_tools__*` methods, so mandatory live probability evidence remains unresolved until the parent invokes a configured isolated client or the required route becomes available.
- Running stdio with the current shared service config is unsafe for this task because `createEngine()` runs transaction recovery for every configured/discovered workspace before MCP negotiation. Recovery of an interrupted transaction can restore old source bytes. The current `modRoots` points to the parent of multiple mods.
- `setup --init` does not offer a private `serverStateRoot` flag. The schema supports a separate private root, but the isolated probe needs the parent-approved temporary JSON config.
- No standalone Technology Tree Viewer was detected on this host; record the absent viewer as a package gap. Technology MCP source routes exist in the installed package but are also not exposed live in this session.
- The exact Protective Aid weighted source path/id was not part of the route-recovery prompt and must be supplied by the parent for the first probability query.

### Ordinary risks
- Installed source metadata (version 3.6.0 and route definitions) proves package capability only. The isolated live handshake and `tools/list` response must establish the actual connected process version, health, and accepted schemas.
- A mod `workspaces` registration remains writable in package config; there is no read-only workspace flag in this schema. Restrict the probe client to `tools/list`, `ping`, and the `probability_inspect` read-only call.

## Recommended next action

Use the parent-approved temporary config with distinct private state/storage roots and exactly one mod registration, then run the SDK sequence `connect` → `getServerVersion`/`ping` → `listTools` → `probability_inspect` with the real source path. If the live route or schema is missing, preserve the exact error and leave the CBRN probability conclusion blocked rather than substituting source-only analysis.
