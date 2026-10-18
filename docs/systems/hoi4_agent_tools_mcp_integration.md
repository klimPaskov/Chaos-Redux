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

Installed `dlc/` and `integrated_dlc/` folders are read-only layers between the base game and the mod, ordered by DLC ID; result paths name each by its folder. An installed folder does not show that a playset enables that DLC, so content that depends on it still needs its `has_dlc` check. The mod's `replace_path` entries in `descriptor.mod` apply to analysis as the game applies them.

The registration contains no credentials. Keep HTTP bearer tokens in environment variables, never in tracked config.

The Codex registration allows 120 seconds for startup and 600 seconds per tool call.
Keep source selectors and GUI scenario matrices bounded; complex source renders can take several minutes.
Use negotiated task support only after confirming it in the connected client and server.

## Tool routes

| Capability | MCP tools | Source access |
| --- | --- | --- |
| Focus Tree Workbench | `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.focus_rewrite` | inspect/render produce evidence; render includes PNG with decoded icons by default (`png: false` for vector only); rewrite writes the configured mod through the shared transaction engine |
| Scripted GUI Studio | `hoi4.gui_inspect`, `hoi4.gui_render`, `hoi4.gui_rewrite` | inspect/render do not write source (they produce artifacts); rewrite writes the configured mod |
| Agent Nudger | `hoi4.map_inspect`, `hoi4.map_rewrite` | inspect validates or renders a view selected by `layer`, `overlays`, `scale`, `tile`, or `area`; rewrite writes the configured mod |
| Event Chain Viewer | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_inspect` (`mode = compare`) | read-only |
| Technology trees | `hoi4.tech_inspect`, `hoi4.tech_render`, `hoi4.tech_inspect` (`mode = compare`) | read-only source and visual evidence |
| Local references | `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup` | read-only offline wiki, installed documentation, and exact source definitions/usages |
| Probability and AI | `hoi4.probability_inspect`, `hoi4.probability_analyze` | inspect finds and evaluates current weights (`evaluate: false` for inventory); analyze selects `analysis = compare`, `sweep`, `simulate`, `sequence`, or `render`; read-only scenario evidence |
| Cross-system analysis | `hoi4.impact_inspect`, `hoi4.decision_inspect`, `hoi4.mechanic_test`, `hoi4.package_check`, `hoi4.scenario_test` | read-only source and declared-scenario evidence |
| Mod summary and requested logs | `hoi4.mod_index`, `hoi4.error_log` | read-only descriptor/definition summary, next free numbered IDs, or user-supplied/explicitly requested log evidence |

Large JSON, SVG, PNG, HTML, diagnostics, plans, and diffs are linked through `hoi4-agent://` MCP resources. Source files remain authoritative.
When reading an artifact resource, use the configured MCP server key `hoi4_agent_tools`; the npm package name `hoi4-agent-tools` is not the resource server identifier. Follow the returned byte-range continuation until the resource is complete.

## Summary, identifiers, and requested logs

Use `hoi4.mod_index` with `mode = overview` for the descriptor, definition counts, folders, and event namespace ranges.
Use `mode = next_id` with `kind` and `namespace` or `prefix` to find the next free numbered identifier across all source layers, including the first unused gap; recheck before writing because this does not reserve it.
Use `hoi4.error_log` only for a user-supplied log or an explicit request to inspect logs, with narrow `scope`, `category`, or text filters when useful.
It groups messages and patterns from the last launch, identifies source file/line/layer and source changes since the log, and may include `sinceLastLaunch` and a cited `knownMistake` fix.
Do not seek logs or infer a fresh launch during ordinary issue review; the no-unsolicited-logs rule in AGENTS.md remains in force.

## Existing workflow ownership

Use the skill that owns the current work.
`chaos-redux-focus-trees` owns focus inspection and layout review; `chaos-redux-events` owns event-chain inspection; `chaos-redux-scripted-gui` owns GUI reference-to-native design and visual review; `chaos-redux-decisions-missions` retains GUI action costs, requirements, effects, AI, cleanup, and balance.
Choose routes that answer a concrete question about the changed surface and apply the retry limits in `AGENTS.md`.
There is no central MCP skill or router.

## Local reference workflow

Start with `hoi4.reference_context` for the work surface; use `hoi4.reference_search` and `hoi4.reference_read` for exact rule or command text not already returned. `hoi4.source_lookup` finds exact vanilla and Chaos Redux definitions, override status, and indexed usages. Keep the source path, line span, and revision with implementation notes. The offline wiki under `paradox_wiki/` and installed game documentation are the source material; do not fetch the Paradox Wiki website. Read only the sections relevant to the task. Read the source excerpts returned by MCP; use targeted search/read for needed text that the context result does not include. A source list alone is only navigation. MCP-delivered source text satisfies the reading requirement; do not reopen the same files for a separate offline-reading pass. If a reference root is unavailable or sections are skipped, inspect the local files directly and record the missing coverage. When a live context result includes `omittedSources`, raise the result limit or use targeted search/read to cover those required sources; `missing` identifies absent files instead. At a limit of 1, installed documentation can occupy the only result; a limit of 2 or more can retain both available required source kinds. Reuse already-read excerpts while their source revision and relevance are unchanged. Installed game documentation takes precedence for current syntax; verify a vanilla source precedent when possible.

When `hoi4.reference_context` returns `knownMistakes`, read the relevant source-cited rule, symptom, and fix alongside the surface references; a listed rule is not itself a finding in the current source.

Check the connected tool list and live schemas before using a route and reuse that discovery within the task unless the connection changes.
Use direct local references when retrieval fails; record a material limitation once and continue.

When supported by the live schema, use `source_lookup` with `view = structure` and a bounded `keyPath` to inspect one nested source block.
Repeated keys require their zero-based `occurrence`; structural continuation uses `nextChildOffset` as `childOffset` with the same query settings and `expectedRevision`.
Use `includeReferences = false` for definition-only event and scripted-helper reads when consumers are not needed; enable references when investigating consumers.
When the live schema accepts `path` and `line` instead of `symbol`, `source_lookup` returns the indexed definitions containing that line, innermost first, and a `keyPath` from the innermost definition; use it to cite or navigate from a diagnostic, diff, or editor position.
A lookup that finds no definition may return `suggestions`, which are near-miss identifiers to verify rather than matches.
Search results carry `matchLine`; pass it as `startLine` to `reference_read` to land on the answering line inside a long section, including a single wiki table entry.

When exposed, `hoi4.script_validate` checks an effect or trigger body under a declared scope using installed native-command documentation.
Supply external scope bindings only when their types are known.
A true result covers only `checksPerformed`; `valid = null`, unresolved helpers, unchecked argument blocks, and omitted findings require further source inspection.
These checks do not establish parameter semantics or game execution.

With a mod-relative `path` instead of a body, `hoi4.script_validate` checks every effect and trigger body of an event, decision, national focus, scripted helper, or on-action file under the scope its structure fixes, and treats Chaos Redux scripted effects and triggers as known commands.
Prefer a targeted run on changed script files when available; its findings can identify errors such as a dynamic variable compared as a trigger or a scope link outside its scopes.
When supported, file mode also performs the documented `known_mistakes` pass: verify that name in `checksPerformed` and inspect `KNOWN_MISTAKE_<RULE>` findings and their cited fixes.
Snippet mode does not establish that the file-level known-mistake pass ran; resolved rules are retained as reference history and are not applied.
If the validator cannot run or cannot resolve a construct, inspect that construct against installed documentation and source instead of waiting for game testing or repeating the same request.
If it identifies an actual script error, fix that error and recheck the changed behavior; a tool retry limit does not waive a real defect.
Its warnings cover player-facing text (colour codes in news and report events, including through scripted localisation, development wording, and unlocalised flags in decision and focus requirement tooltips) and visible events that would reach one player once per loop iteration; fix each one or record why it stays.

## Writes and recovery

Domain rewrites validate the complete proposal, generate review evidence, apply through the internal transaction journal, re-index and post-validate the result, and retain exact-byte recovery data. A proposal rejected before writing does not mutate source. After a write error or timeout, inspect the actual source and transaction result before repeating the operation; automatic recovery must not be assumed to have finished solely because the response failed. Recovery is automatic when a write or post-validation fails; intentional reversal of a successful edit is a new authorized source change (normally through Git), because the public MCP surface does not expose caller-managed transaction, apply, or rollback tools.

For scripted GUI work, `gui_rewrite` is optional; the transaction behavior above does not make its automatic post-write/index validation or transaction success a project completion gate.
An authorized reviewed GUI edit may be applied directly without another fallback approval solely because the optional rewrite blocks or rolls back.
Review source, click regions, representative affected scenarios, and available renders under `chaos-redux-scripted-gui`.
Fix known defects; disclose unavailable visual checks without treating them as missing implementation.
This workflow rule does not disable or modify the installed server's internal validation.

## Rendering limits

Focus, GUI, map, and event renders are offline evidence, not game screenshots.
Scripted GUI previews include fidelity information and do not run, launch, automate, control, or capture HOI4.
Follow `chaos-redux-scripted-gui` to review available renders and fix visible defects; do not dismiss a defect without inspecting its source and scenario.
Event analysis is bounded and static; dynamic destinations or runtime behavior may remain uncertain without blocking delivery of a documented implementation.

GUI scenarios accept `flags`, `variables`, and `closedFlags: true`, which treats undeclared flags as unset as the game does; set them so tabbed windows such as the settings window render one page at a time, and render each page as its own scenario.
`GUI_UNRESOLVED_VISIBILITY_OVERLAP` means the scenario has not decided which overlapping element is visible; supply the missing flags or variables instead of treating the stack as a layout defect.
`"background": "transparent"` renders without the preview backdrop for compositing; each element is its own `<g>` group in the full SVG, keyed by the element ids in `layout.json`.

## MCP evidence in handoffs

When a routed task touches focus trees, event chains, technology or doctrine trees, weighted logic, scripted GUI, or maps, use the relevant MCP checks under the retry limits in AGENTS.md. Pass only the diagnostics, revision, scenario hash, comparison, or linked artifact URI the parent needs instead of copying a complete graph or matrix into the prompt. Tool exposure is separate from service health and standalone viewer availability. If the relevant MCP route remains unavailable after the retry limit, report what could not be checked and continue with the relevant local documentation, source, and local tests. When a task needs the standalone Technology Tree Viewer, verify its availability separately from the exposed read-only `mcp__hoi4_agent_tools__hoi4_tech_inspect`, `mcp__hoi4_agent_tools__hoi4_tech_render`, and `mcp__hoi4_agent_tools__hoi4_tech_inspect` (`mode = compare`) routes. Do not invent viewer capabilities or treat an absent viewer as missing source implementation.

Share the failed check, attempts already used, and the condition needed to retry through the existing handoff; changing files, caller, tool name, or transport does not restart the same failure.
Use AGENTS.md to distinguish an unavailable check from a defect or missing requested output.
An advancing page offset, new result data, or completed work is progress; another `running` status or timestamp alone is not.
Useful continuation is not a failed retry, but unchanged polling and recovery requests follow the same limit.
Keep the existing job handle and continue independent work when polling cannot add information.
For a production job or a result explicitly requested by the user, follow its documented polling interval and a finite wait limit set when it starts; do not restart the job or extend that limit merely because it still says `running`.
If that limit expires, preserve the handle and completed outputs and report the missing requested result. Ordinary workflow verification does not become a requested deliverable merely because an older checklist calls it mandatory.
If the tool cannot analyze the script, evaluate the actual weights, helpers, constants, eligibility, and target scope in named cases and label score-only or uncertain conclusions accurately.
Do not change gameplay to satisfy an analyzer or treat missing tool output as evidence that behavior is absent.

### Tool availability and asynchronous jobs

Reuse capability discovery for an unchanged connection.
Before using `mode = helper_expansion`, `hoi4.job_inspect`, `hoi4.job_cancel`, or native MCP tasks, verify the connected server's reported version and health, inspect the live tool schemas for those routes, and check client task negotiation. Source code or exposed tool metadata alone does not establish support in the connected process. Use only routes confirmed for the installed server and client; otherwise follow the available domain routes and record the missing capability precisely.

Resolve each client's actual configured transport and server process before attributing capabilities to a local checkout, global binary, or exposed tool list; their versions and supported routes can differ.
Keep configuration identity, server version, live schemas, and task negotiation in task evidence.
A failure to observe a native task result does not establish that the server task failed.
Preserve configuration, task IDs, and source/scenario hashes, then query existing handles through confirmed routes before retrying; if observation remains unavailable, report the task outcome unresolved.
Do not change external tool source or dependencies to mask startup or domain failures.
Keep package paths, concrete versions, and current errors in task evidence rather than reusable skill rules.

For user-requested MCP troubleshooting after a transport closure, a separately initialized read-only stdio connection through the installed MCP SDK and configured server executable is an optional recovery route.
Use the same configured workspace, mod-root environment, and working directory; verify Windows child processes are hidden, initialize the connection, and inspect its reported version and live schemas before calls.
Plain client `capabilities: {}` does not negotiate native tasks, even when the server advertises task support; verify job-tool availability separately through live schemas.
Record the separate connection and use only confirmed read-only domain calls; this route does not authorize desktop or game launch, external dependency edits, or replay of an unresolved mutation.

On a confirmed route, use `mode = helper_expansion` with `hoi4.event_inspect` or `hoi4.tech_inspect` for bounded helper pages, and use `hoi4.job_inspect` and `hoi4.job_cancel` for persistent jobs. Request asynchronous MCP tasks only when the client negotiates support. Keep opaque job IDs and helper continuation URIs intact. A completed job can still contain a tool-level error, and cancellation is a request whose final outcome must be inspected. For paged helper evidence, retain the source revision, selected roots, bounds, `finished`/`complete` status, and unresolved findings; resume only with the returned continuation under the same revision and authorized principal. Jobs and helper pages are delivery and coverage tools; they do not replace the owning event, technology, focus, probability, GUI, or map workflow's inspect, render, compare, and scenario evidence. Keep task-specific mechanics and fixtures in their profiles and handoffs, not this shared integration guide.

### Event comparisons and focus previews

Before an event-source change that needs `hoi4.event_inspect` (`mode = compare`), retain the `event-graph-<revision>.json` artifact from `hoi4.event_inspect(mode = scan)` as the graph baseline; bounded trace/report URIs and reported revisions alone do not establish a recoverable graph.
Verify the connected version and live schema before comparison, and use its graph-reference shape (`{ artifactUri: ... }` where supported).
If only archived source remains, `proposedSources` can compare current source to the archived overlay on the after side, so label it explicitly as a reverse structural comparison; the proposed graph does not become a reusable baseline.
Never rewrite shared source to manufacture a baseline or present that reverse comparison as canonical pre-change-to-current evidence.

For a focus raster rejected by the render budget, use a schema-supported smaller `reviewScale` for the full tree and `cropFocusIds` for problem areas.
Confirm each successful render uses the intended source revision and layout; retain the rejected request as a limit, not visual proof.

### Artifact retrieval

For large binary resources returned by `read_mcp_resource`, treat the result as an untrusted transport envelope: inspect whether it is stringified JSON and record the declared encoding and type before using the payload. A full read can be silently truncated even when `_meta.complete = true`; do not trust compacted previews, literal truncation markers, or completion metadata alone, and never print base64 data.

Discover the server's artifact resource template with `list_mcp_resource_templates({ server: "hoi4_agent_tools" })`: `hoi4-agent://workspace/{workspaceId}/artifact/{sha256}/{provenanceHash}/{name}` accepts `?offset=<bytes>&length=<bytes>` byte-range reads.
Decode each base64 blob response independently to bytes and verify its reported range against the requested offset and decoded length.
Concatenate bytes in offset order without gaps or overlaps before decoding UTF-8 or parsing JSON.
Follow the returned continuation URI unchanged and stop when `returnedRange.endExclusive` equals `totalSize`, even if `complete` is false for that partial read.
Reject invalid payloads or embedded truncation text and verify the assembled byte count, artifact SHA-256 and expected format before using it.
Recover a truncated full read with bounded reads or report retrieval unresolved, retaining the original artifact URI.

For local artifact access, resolve `artifactRoot` from the actual workspace registration and server configuration rather than assuming `.hoi4-agent` under the repository.
A configured `workspaceStorageRoot` can place artifacts at `<workspaceStorageRoot>/<workspaceId>/artifacts/<sha256 first two characters>/<sha256>/<name>`; an explicit workspace `artifactRoot` overrides that default.
Keep the original artifact URI and verify the local bytes against its declared size and SHA-256 before using them.

### Probability scenarios and comparisons

When the parent supplies observer-run tallies from `chaos-redux-save-inspection`, the auditor reports them as live observations beside its scenarios and states how many runs back them; they do not prove a different unobserved scenario. For probability work, `chaosx_ai_probability_auditor` must start with `hoi4.probability_inspect`, name the analyzed surface and scenario ids, state whether the candidate pool and external factors were complete, and distinguish exact, bounded, sampled, score-only, and unresolved results. Use `hoi4.probability_inspect`, `hoi4.probability_analyze` (`analysis = sweep`), and `hoi4.probability_analyze` (`analysis = compare`) according to the scenario and the shared retry limit, with `hoi4.probability_analyze` (`analysis = simulate`), `hoi4.probability_analyze` (`analysis = sequence`), and `hoi4.probability_analyze` (`analysis = render`) only under their declared evidence conditions. For technology or doctrine work, list the affected technology, folder, unlock, grant, bonus, or asset ids and include the relevant `hoi4.tech_inspect` (`mode = compare`) result when source changed.

For `hoi4.probability_inspect`, pass a mod-relative source object, for example `source: { path: "common/decisions/camp_repression_generic_decisions.txt" }`. The 4.0 route also accepts a string `source`; `{ relativePath: ... }` is not the documented source selector. Use the connected live schema when an older route differs. Argument-validation rejection identifies an invalid request shape; correct it against the live schema before declaring the route unhealthy. For `hoi4.probability_analyze` (`analysis = compare`), check the live schema and pass real, nonempty `before.path` and `after.path` source paths with the identical saved `scenarioSet`; do not add `sourceRevision` or `sourceHash` to either source object, because the installed route rejects those fields. Keep revisions and hashes in the handoff as evidence. `beforeManifest` and `afterManifest` are for declared custom pools (`id`, `selection`, `candidates`, `transitions`), not saved probability analysis artifacts. An analysis URI cannot replace the pre-edit source. If an exact before source is missing, or a deleted candidate prevents a valid comparison, retain before/after inspect evidence, state that the numeric delta is unresolved, and never compare the current file to itself.

Indexed adapters can require a canonical gameplay `path` for discovery; an archive-path `no_weighted_surfaces` result does not establish an unsupported adapter or absent weights.
Recheck the live schema and source surface before classifying the gap.
For an immutable baseline, use live-supported `snapshotPath` and `expectedSourceHash` fields with `path` naming the logical gameplay file.
For the supported snapshot contract, `expectedSourceHash` verifies the raw snapshot-byte SHA-256, distinct from the analysis result's `sourceHash`.
Preserve exact before and after bytes outside gameplay directories and compare them with the identical saved `scenarioSet`, without replacing live source.
Reuse the complete saved fixture verbatim, including labels and descriptions; reconcile differing returned scenario hashes before claiming a matched comparison.
Shared helpers and constants remain current, so a frozen source comparison does not establish a historical whole-workspace comparison.
An empty `requiredInputPaths` discovery result does not prove complete scenario inputs.
With `technology.external_factors_complete` unbound, a zero exposed-score delta does not establish unchanged total native AI research preference.
Check evaluation requirements and unresolved findings against the live schema and installed evaluator, including its numeric/token predicate shapes and representational limits.

Probability scenario schemas vary between installed server versions and connected routes; inspect each live route schema and pass only fields it accepts. Where supported, put `date` at the scenario's top level. Explicit `controls` maps and typed scope bindings such as `{ id, type, actor, state, flags }` may be accepted by a newer direct client while the connected tool rejects them. Treat absent schema fields and `candidateOverrides` as unresolved inputs or eligibility assumptions, not live proof of campaign state. Record validation errors and artifact URIs, never invent fixture keys or add gameplay flags solely to satisfy the adapter, and never present partial score-only output as complete probability or balance validation.

## MCP event-chain pass

For long or cross-file chains, use the read-only `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_inspect` (`mode = compare`) tools to map entry points, branches, state and scope flow, impact, and structural changes. Event-owned GUI surfaces may also use `hoi4.gui_inspect` and `hoi4.gui_render`. Edit event source through the normal workflow and review changed branches once, comparing source and available MCP evidence and rechecking actual fixes under AGENTS.md. MCP evidence augments the contract in `chaos-redux-events` and does not replace source review or the completion audit.

Check the live selector schema before narrowing an event call: the full selector is `selector: { kind: "event", eventId: "namespace.id" }`; 4.0 also accepts a plain event-ID string and selectors without `kind`.

### MCP coverage and limitations

Before treating an inspection or render as lifecycle evidence, read its `analysisMode`, `complete`, indexed `counts.helpers`, `filesScanned` or source-hash inventory, unresolved entries, and diagnostics. `trace` and `explain_path` use focused analysis, and `scan`, `roots`, `lint`, or `event_render` use focused analysis when a selector is supplied. Focused analysis reads only `events/**/*.txt` and `common/on_actions/**/*.txt`, disables workspace-wide helper projections and lifecycle passes, and keeps the focused-boundary blocker even when `expandHelpers = true`. `state_flow` and `impact` request full analysis even when narrowed, while selector-free `scan` requests full analysis. Choose a bounded route that can answer the actual helper or lifecycle question, and do not treat a focused trace or a zero helper count as proof that the chain has no helpers. If the event route is unavailable or partial, record its coverage limit once and inspect the relevant event, on-action, and helper source directly after the shared retry limit; this needs no fallback approval and does not establish runtime execution.

When the connected server and live schema confirm `mode = helper_expansion` under [Tool availability and asynchronous jobs](#tool-availability-and-asynchronous-jobs), use bounded `hoi4.event_inspect` pages for large helper closures with distinct source-linked call paths. Follow a useful returned continuation within the shared retry limit, and report `complete`, source revision, depth stops, cycles, dynamic or missing references, and source coverage separately. If that route cannot answer within the retry limit, inspect relevant helper source directly and record the coverage limit. Helper pages are coverage tools; they do not replace ordinary event inspect, render, compare, or scenario evidence, clear the focused-analysis lifecycle boundary, or prove runtime outcomes. Follow the verified job/task handling in `chaos-redux-subagents`.

`hoi4.event_inspect` (`mode = compare`) accepts cached revisions, validated event-graph artifacts, or proposed source overlays. Report-only trace artifacts and render or manifest artifacts can fail `artifactUri` graph validation because their report or render schema does not contain an event-graph payload. Use a graph-bearing artifact or another supported compare input when available. If none is available, retain the limitation and compare preserved before/after source without inventing a graph conversion or tool result.

For event-option `ai_chance`, event MTTH, direct random chance, and `random_list` logic, route the audit through `chaosx_ai_probability_auditor`. Prefer `hoi4.probability_inspect` for targeted discovery, then use `hoi4.probability_inspect`, `hoi4.probability_analyze` (`analysis = sweep`), `hoi4.probability_analyze` (`analysis = simulate`), or `hoi4.probability_analyze` (`analysis = compare`) only for the surface being reviewed. Use `hoi4.probability_analyze` (`analysis = sequence`) only when a complete custom-pool manifest explicitly declares cadence, recovery, caps, cooldowns, removals, resets, timer changes, and terminal states. Use `hoi4.probability_analyze` (`analysis = render`) for timing, matrix, sensitivity, sequence, comparison, or unresolved views when they make the result easier to audit. Provide complete option or list pools when normalization applies, and provide scheduled state changes for timing questions. Treat exact, bounded, sampled, score-only, and unresolved results as different evidence. The analyzer does not choose balance targets or edit event source. If the route is unavailable, unsupported, or misclassifies the surface, inspect actual weights, MTTH, helpers, constants, and eligibility and evaluate named representative source scenarios. Retain before/after source comparison for weight changes, label score/probability assumptions, and never rewrite gameplay to appease the classifier or reset the retry budget. For `hoi4.probability_analyze` (`analysis = compare`), pass both `before` and `after` as `probabilitySourceSchema` objects with a source `identifier`/`path`, `inlineClausewitz`, or `virtualPatch`, or pass both `beforeManifest` and `afterManifest` under an identical `scenarioSet`. Do not put a cached `analysisId` in `identifier`, because `analysisId` belongs only to `hoi4.probability_analyze` (`analysis = render`) and is not a compare source.

When the live schema exposes `snapshotPath`, bind a frozen copy with `{ path: original_engine_relative_path, snapshotPath: archived_workspace_relative_path, expectedSourceHash: copied_bytes_sha256 }`.
Some domain adapters use the logical engine path to recognize weighted blocks, so selecting only a documentation path or an inline fixture can return `PROBABILITY_SURFACE_EMPTY` even when the copied script parses.
Verify the before and after source identities and matched blocks before interpreting that result as a missing capability or input-size limit.

After renames, action consolidation, or edits that shift line-based candidate ids, inspect both sides before choosing `candidatePool`.
A filter containing only current ids can empty the frozen baseline, while removed ids can empty the current side; use the union of verified ids or each side's exact local source selector where supported.
Keep decision and mission adapters separate, and report unresolved target-scope and eligibility inputs rather than treating a definition-level comparison as target-level probabilities.

For event-option audits, qualify a reused option identifier with its parent event identifier and supply every option in that event's local candidate pool. Verify the installed server version and connected tool schema before building scenarios; when supported, put each scenario's date at its top level and supply explicit state-controller maps and typed scope bindings. Inspect the returned `poolComplete` and `unresolved` fields before interpreting a normalized option share. Treat `candidateOverrides` as declared eligibility assumptions, not proof of live eligibility. A conditional option share given that the event fires does not include the event's firing chance.

For deterministic max-score selector implementation, apply [Deterministic max-score selection](../../.agents/skills/chaos-redux-events/references/scripted-systems-and-country-integration.md#deterministic-max-score-selection).

## HTTP and troubleshooting

Use stdio for local agents. A stdio server exits when its launching process exits; Codex sessions that keep one server per subagent set `HOI4_AGENT_STDIO_IDLE_EXIT_MINUTES` (30) in the server environment so idle servers exit. For a separate process, run `hoi4-agent-tools-http --config PATH` with loopback binding, a long bearer token supplied through the configured environment variable, an exact origin allowlist, and explicit workspace grants. Non-loopback deployments need HTTPS, OAuth/OIDC, isolation, and the package limits described in the standalone `docs/http.md`.

During mod implementation, missing tools call for direct source/reference review after the bounded check allowance.
Do not turn a content task into package installation, server repair, replacement-client work, or repeated health checks.
When the user specifically requests MCP setup or repair, inspect the active registration and installed package, reproduce the failing route, and use the package's own diagnostics and integration tests within that separate scope.
