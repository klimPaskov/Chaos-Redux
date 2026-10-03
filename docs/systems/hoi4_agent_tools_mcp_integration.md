# HOI4 Agent Tools MCP integration

## Registration

- Server: `hoi4-agent-tools` (`io.github.klimPaskov/hoi4-agent-tools`).
- Codex registration: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.codex\config.toml`.
- Startup: the project config starts the globally installed `hoi4-agent-tools.cmd` over stdio with Chaos Redux as its working directory. The server detects that mod directly; no per-mod JSON or selection call is needed. Restart Codex after installing or changing the registration.

Install or upgrade the published package with `npm install --global hoi4-agent-tools`. For another mod checkout, register the same server command with that mod as `cwd`; the server detects the current mod automatically. Use `hoi4-agent-tools-setup --init` only for a persistent multi-mod or remote configuration.

## Roots and generated data

The mod containing the MCP working directory is the writable source root. The installed game is read-only. Other mods, the standalone MCP repository, and unrelated directories are not treated as the current source. Generated state, artifacts, and cache are outside gameplay files:

- state: the per-user `hoi4-agent-tools` state directory
- artifacts and cache: the per-user `hoi4-agent-tools` workspace-data directory

The registration contains no credentials. Keep HTTP bearer tokens in environment variables, never in tracked config.

The Codex registration allows 120 seconds for startup and 600 seconds per tool call.
Keep source selectors and GUI scenario matrices bounded; complex source renders can take several minutes.
Use negotiated task support only after confirming it in the connected client and server.

## Tool routes

| Capability | MCP tools | Source access |
| --- | --- | --- |
| Focus Tree Workbench | `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.focus_raster`, `hoi4.focus_rewrite` | inspect/render/raster produce evidence; rewrite writes the configured mod through the shared transaction engine |
| Scripted GUI Studio | `hoi4.gui_inspect`, `hoi4.gui_render`, `hoi4.gui_rewrite` | inspect/render do not write source (they produce artifacts); rewrite writes the configured mod |
| Agent Nudger | `hoi4.map_inspect`, `hoi4.map_render`, `hoi4.map_rewrite` | inspect/render do not write source (they produce artifacts); rewrite writes the configured mod |
| Event Chain Viewer | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare` | read-only |
| Technology trees | `hoi4.tech_inspect`, `hoi4.tech_render`, `hoi4.tech_compare` | read-only source and visual evidence |
| Local references | `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup` | read-only offline wiki, installed documentation, and exact source definitions/usages |
| Probability and AI | `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_compare`, `hoi4.probability_render` | read-only scenario evidence |
| Cross-system analysis | `hoi4.impact_inspect`, `hoi4.decision_inspect`, `hoi4.mechanic_test`, `hoi4.package_check`, `hoi4.scenario_test` | read-only source and declared-scenario evidence |

Large JSON, SVG, PNG, HTML, diagnostics, plans, and diffs are linked through `hoi4-agent://` MCP resources. Source files remain authoritative.
When reading an artifact resource, use the configured MCP server key `hoi4_agent_tools`; the npm package name `hoi4-agent-tools` is not the resource server identifier. Follow the returned byte-range continuation until the resource is complete.

## Existing workflow ownership

Use the skill that owns the current work. `chaos-redux-focus-trees` owns focus inspection and layout evidence; `chaos-redux-events` owns event-chain inspection; `chaos-redux-scripted-gui` owns GUI reference-to-native design and mandatory visual evidence; `chaos-redux-decisions-missions` retains GUI action costs, requirements, effects, AI, cleanup, and balance. Technology and map work use their domain inspect, render, compare, and rewrite routes. There is no central MCP skill or router.

## Local reference workflow

Call `hoi4.reference_context` for the work surface, then `hoi4.reference_search` and `hoi4.reference_read` for the exact rule or command. `hoi4.source_lookup` finds exact vanilla and Chaos Redux definitions, override status, and indexed usages. Keep the source path, line span, and revision with implementation notes. The offline wiki under `paradox_wiki/` and installed game documentation are the source material; do not fetch the Paradox Wiki website. Read only the sections relevant to the task. A citation bundle is a navigation result, so read the cited sections that support each decision. If a reference root is unavailable or sections are skipped, inspect the local files directly and record the missing coverage. When a live context result includes `omittedSources`, raise the result limit or use targeted search/read to cover those required sources; `missing` identifies absent files instead. At a limit of 1, installed documentation can occupy the only result; a limit of 2 or more can retain both available required source kinds. Context excerpts select question-matching sections within required files, but still require reading the cited rules. Installed game documentation takes precedence for current syntax; verify a vanilla source precedent when possible.

Check the connected tool list and live schemas before using any route. Domain-specific inspect, render, compare, and declared scenarios remain necessary for implementation evidence; reference retrieval does not replace them.

When supported by the live schema, use `source_lookup` with `view = structure` and a bounded `keyPath` to inspect one nested source block.
Repeated keys require their zero-based `occurrence`; structural continuation uses `nextChildOffset` as `childOffset` with the same query settings and `expectedRevision`.
Use definition-only event and scripted-helper reads when consumers are not needed.

When exposed, `hoi4.script_validate` checks an effect or trigger body under a declared scope using installed native-command documentation.
Supply external scope bindings only when their types are known.
A true result covers only `checksPerformed`; `valid = null`, unresolved helpers, unchecked argument blocks, and omitted findings require further source inspection.
These checks do not establish parameter semantics or game execution.

## Writes and recovery

Domain rewrites validate the complete proposal, generate review evidence, apply through the internal transaction journal, re-index and post-validate the result, and retain exact-byte recovery data. A blocked proposal does not mutate source. Recovery is automatic when a write or post-validation fails; intentional reversal of a successful edit is a new authorized source change (normally through Git), because the public MCP surface does not expose caller-managed transaction, apply, or rollback tools.

For scripted GUI work, `gui_rewrite` is optional; the transaction behavior above does not make its automatic post-write/index validation or transaction success a project completion gate.
An authorized reviewed GUI edit may be applied directly without another fallback approval solely because the optional rewrite blocks or rolls back.
Source review, required MCP inspect/render evidence, click-region checks, matched scenario/reference comparisons, and correction of every visible in-scope defect remain mandatory under `chaos-redux-scripted-gui`.
This workflow rule does not disable or modify the installed server's internal validation.

## Rendering limits

Focus, GUI, map, and event renders are deterministic offline evidence, not game screenshots. Scripted GUI previews include fidelity information and do not run, launch, automate, control, or capture HOI4. For GUI visual acceptance, follow `chaos-redux-scripted-gui`: treat the production MCP render as the one-to-one in-game visual review surface, fix every visible in-scope defect, and never dismiss a defect as a renderer discrepancy. Event analysis is bounded and static; dynamic destinations or runtime behavior may remain unresolved and must be reported.

## HTTP and troubleshooting

Use stdio for local agents. For a separate process, run `hoi4-agent-tools-http --config PATH` with loopback binding, a long bearer token supplied through the configured environment variable, an exact origin allowlist, and explicit workspace grants. Non-loopback deployments need HTTPS, OAuth/OIDC, isolation, and the package limits described in the standalone `docs/http.md`.

If tools are missing, check `npm list --global hoi4-agent-tools --depth=0`, confirm the project is trusted, and restart Codex. Call the domain tool you need directly while the MCP `cwd` is the target mod. Verify the package with its Inspector and integration tests when a required route is absent.
