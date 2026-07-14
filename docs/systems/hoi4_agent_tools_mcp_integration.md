# HOI4 Agent Tools MCP integration

## Registration

- Server: `hoi4-agent-tools` 1.2.0 (`io.github.klimPaskov/hoi4-agent-tools`).
- Codex registration: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.codex\config.toml`.
- Server configuration: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.codex\hoi4-agent-tools-chaos-redux.json`.
- Startup: the project config starts the globally installed `hoi4-agent-tools.cmd` over stdio. Restart Codex after installing or changing the registration.
- Workspace ID: `chaos_redux`.

Install or upgrade the published package with `npm install --global hoi4-agent-tools@1.2.0`. For another checkout, copy the JSON shape, replace the absolute mod and game paths, and print a client entry with `hoi4-agent-tools-setup --print-client-config --config PATH`.

## Roots and generated data

Only the Chaos Redux mod root is a writable source root. The configured game root is read-only. Workshop mods, other mod folders, the standalone MCP repository, and unrelated directories are not registered. Generated state, artifacts, and cache are outside gameplay files:

- state: `C:\Users\klimp\AppData\Local\hoi4-agent-tools\chaos-redux\state`
- artifacts and cache: `C:\Users\klimp\AppData\Local\hoi4-agent-tools\chaos-redux\workspace-data\chaos_redux\{artifacts,cache}`

The JSON contains no credentials. Keep HTTP bearer tokens in environment variables, never in tracked config.

## Available tools

| Capability | Installed tools | Source access |
| --- | --- | --- |
| Focus Tree Workbench | `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.focus_rewrite` | inspect/render do not write source (they produce artifacts); rewrite writes the configured mod through the shared transaction engine |
| Scripted GUI Studio | `hoi4.gui_inspect`, `hoi4.gui_render`, `hoi4.gui_rewrite` | inspect/render do not write source (they produce artifacts); rewrite writes the configured mod |
| Agent Nudger | `hoi4.map_inspect`, `hoi4.map_render`, `hoi4.map_rewrite` | inspect/render do not write source (they produce artifacts); rewrite writes the configured mod |
| Event Chain Viewer | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare` | read-only |
| Technology Tree Viewer | none in installed 1.2.0 | unavailable; do not invent a wrapper or claim this check passed |

Large JSON, SVG, PNG, HTML, diagnostics, plans, and diffs are linked through `hoi4-agent://` MCP resources. Source files remain authoritative.

## Existing workflow ownership

Use the skill that owns the current work. `hoi4-focus-trees` owns focus inspection and layout evidence; `chaos-redux-events` owns event-chain inspection; `hoi4-decisions-missions` and event-owned GUI work may use Scripted GUI Studio; map-touching workflows may use Agent Nudger. Technology, doctrine, country, event, and focus work should use a Technology Tree Viewer only after a server version actually exposes one. There is no central MCP skill or router.

## Writes and recovery

Domain rewrites validate the complete proposal, generate review evidence, apply through the internal transaction journal, re-index and post-validate the result, and retain exact-byte recovery data. A blocked proposal does not mutate source. Recovery is automatic when a write or post-validation fails; intentional reversal of a successful edit is a new authorized source change (normally through Git), because the public MCP surface does not expose caller-managed transaction, apply, or rollback tools.

## Rendering limits

Focus, GUI, map, and event renders are deterministic offline evidence, not game screenshots. Scripted GUI previews include fidelity information and do not run, launch, automate, control, or capture HOI4. Event analysis is bounded and static; dynamic destinations or runtime behavior may remain unresolved and must be reported.

## HTTP and troubleshooting

Use stdio for local agents. For a separate process, run `hoi4-agent-tools-http --config PATH` with loopback binding, a long bearer token supplied through the configured environment variable, an exact origin allowlist, and explicit workspace grants. Non-loopback deployments need HTTPS, OAuth/OIDC, isolation, and the package limits described in the standalone `docs/http.md`.

If tools are missing, check `npm list --global hoi4-agent-tools --depth=0`, run `hoi4-agent-tools-setup --diagnose --config PATH`, confirm the project is trusted, and restart Codex. Call `hoi4.mods` first; it should return only `chaos_redux` for this project configuration. Re-run the Inspector or the package integration tests after upgrades. The current Technology Tree Viewer gap is a package limitation, not a Chaos Redux workflow rule.
