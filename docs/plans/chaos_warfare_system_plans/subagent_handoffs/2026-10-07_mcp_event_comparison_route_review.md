# Repo Explorer Handoff

## Scope read
- Parent task: Determine the installed HOI4 Agent Tools event comparison reference shape and whether a bounded `event_inspect(mode = trace)` artifact can serve as a before or after graph.
- Explicit constraints: Read-only inspection; no gameplay or tool edits, no process restart, no HOI4 launch, no native jobs or helper expansion, no large event graphs, and only this requested handoff file may be written.
- Files or ids requested: Event `cbrn_bio_lifecycle.1`; workspace `mod_chaos_redux_ea3b2d67c2c0`; supplied trace revision `c1e014cbf1fb51bebb7fb19fb52caa74e94792b53533c4817ed7c9cd38f85914` and its `event-trace-c1e014cbf1fb.json` artifact URI.
- Skills or docs read: Repository `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and the installed `hoi4-agent-tools` 3.10.0 event documentation and implementation listed below.

## Primary findings
- In the installed 3.10.0 schema, `before` and `after` each accept a strict object containing exactly one of `{ "revision": "<64-character sha256>" }` or `{ "artifactUri": "hoi4-agent://..." }`. The public `event_compare` tool metadata types these fields as `unknown`, but the running package parser validates them as graph references.
- A trace report URI is not a graph snapshot. `mode = trace` writes an `event-analysis.v1` report with a bounded `trace` payload; only `mode = scan` writes the separate `event-graph-<revision>.json` snapshot accepted by the graph validator.
- The revision-only failure `EVENT_REVISION_NOT_CACHED` is consistent with a trace result: restoration checks process-local graph history and retained `event-graph-<revision>.json` or `event-scan-<revision-prefix>.json` artifacts, not `event-trace-...` reports.
- Archived raw source captures can be supplied through `proposedSources` without touching the shared workspace, but the virtual graph is always placed on the comparison's `after` side. The API neither retains nor exports that proposed graph for a second, correctly oriented comparison.
- I attempted the supplied trace URI as both `before` and `after`, with the event selector, `render = false`, and `refresh = false`. This connection returned `ARTIFACT_NOT_FOUND` with blocker `Artifact provenance manifest is unavailable`; direct resource reading of that same URI returned the same manifest-unavailable error. This is an access failure in this connection, not runtime proof of the trace parser's rejection. The installed parser code independently shows why the trace envelope is not a valid graph.
- Live status resource `hoi4-agent://server/status` reported current process PID `24872`, transport `stdio`, version `3.10.0`. Its Node entry point resolves to `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\bin\stdio.js`; the matching package manifest also reports `3.10.0`. The artifact template advertises byte-range reads with `offset`/`length` up to 1,048,576 bytes.

## Relevant files
| Path | Why it matters | Evidence |
| --- | --- | --- |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\docs\events.md` | Installed contract for graph references, selected chain comparison, overlays, and event comparison workflow. | Lines 81–89 describe the exact accepted shapes and default refresh behavior. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\schemas\event.js` | Runtime request schema used by the connected 3.10.0 package. | Lines 79–90 define the strict one-of graph reference; lines 161–174 bind `before` and `after` to it. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\event\service.js` | Artifact creation and graph-reference resolution. | Lines 829–847 build trace reports; lines 912–965 write reports and add a graph snapshot only for scans; lines 1271–1303 resolve references and emit `EVENT_REVISION_NOT_CACHED`; lines 1320–1330 define current-source refresh and omitted-after behavior. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\event\artifact-validation.js` | Validates an artifact before event comparison or rendering. | Lines 357–369 require the event graph schema and graph identity fields. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Project evidence rule for event MCP routes and process identity. | Lines 287–294 require live health/schema evidence and caution that exposed tools or another local checkout alone do not prove the connected process capability. |

## Existing patterns
The installed event docs recommend inspecting the chain, making source edits through the normal workflow, and then using `event_compare`, lint, and `event_render` for review. The comparison service accepts a retained graph artifact, a cached revision, the current graph, or a proposed-source overlay. For a baseline-to-current comparison, the robust artifact-backed form is `before: { artifactUri: "<event-graph snapshot URI>" }`, omit `after`, and set `refresh: true`; the service uses a refreshed current graph for the omitted side. For two retained graph snapshots, pass both full graph artifact URIs and set `refresh: false`.

The URI that matters is the URI returned for the `event-graph-<full revision>.json` scan snapshot, not the sibling `event-scan-<revision prefix>.json` report and not a bounded trace, render, lint, or other report URI. A trace artifact's top-level schema is `event-analysis.v1`, and its `report` contains `graphRevision`, `sourceHashes`, `trace`, and unresolved findings, but not a graph. `parseGraphArtifact` unwraps `report.graph` only when present; otherwise it validates the artifact as a graph, which fails the graph schema requirement.

Vanilla or reference precedents: None apply because this task investigates the MCP evidence protocol rather than HOI4 script syntax or game behavior.

## Likely edit order for the parent
1. Check whether a pre-change `event-graph-<revision>.json` snapshot already exists and is readable in the parent task's connected workspace. The trace URI and its revision are insufficient as the comparison baseline.
2. If a pre-change graph snapshot exists, call `hoi4_event_compare` with that URI in `before`, omit `after` to compare against refreshed current source, retain the event selector, and request render output. For a comparison between two explicit snapshots, put each graph URI in the matching reference object.
3. If only the trace report exists, record the before/after graph comparison as blocked for lack of a retained pre-change graph. A new scan after edits can create a usable graph artifact for later comparisons, but it cannot recreate the prior graph state.

Example shape for two actual graph snapshots:

```json
{
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0",
  "before": { "artifactUri": "hoi4-agent://workspace/<workspaceId>/artifact/<sha256>/<provenanceHash>/event-graph-<before-revision>.json" },
  "after": { "artifactUri": "hoi4-agent://workspace/<workspaceId>/artifact/<sha256>/<provenanceHash>/event-graph-<after-revision>.json" },
  "selector": { "kind": "event", "eventId": "cbrn_bio_lifecycle.1" },
  "render": true,
  "maxChainNodes": 8,
  "maxRenderNodes": 80,
  "refresh": false
}
```

## Validation checks
- Confirmed exposed tool metadata for `mcp__hoi4_agent_tools__hoi4_event_compare`; its `before` and `after` fields are currently exposed as `unknown` in the connector schema.
- Read the connected server status resource and checked the local process entry point and package version; live status and package both report 3.10.0.
- Submitted the supplied partial trace URI in both reference positions with `selector = { kind: "event", eventId: "cbrn_bio_lifecycle.1" }`, `render = false`, and `refresh = false`; the call was accepted far enough to return `ARTIFACT_NOT_FOUND`, with `Artifact provenance manifest is unavailable`.
- Requested the same artifact through its resource URI; the current connection returned `Artifact provenance manifest is unavailable` again, so the trace JSON itself was not available for byte-level reading in this task.
- Confirmed from the installed service code that trace mode does not emit a graph snapshot and that graph artifact validation requires `schemaVersion`, `parserVersion`, workspace identity, revision, completeness, and graph data.

## Risks and blockers
Confirmed blocker: This task's MCP connection cannot resolve the supplied trace artifact's provenance manifest, and no pre-change full graph snapshot URI was supplied. Archived raw source captures support a reverse-oriented proposed-source comparison, but the installed API does not support turning its proposed graph into a retained before graph for a canonical pre-change-to-current comparison. The local parser evidence establishes the expected graph artifact kind, but the trace artifact itself could not be reopened here.

Ordinary risk: A fresh `mode = scan` creates a whole-workspace graph snapshot. The parent should use it only where the required task scope permits the full graph operation and should retain the returned graph artifact URI directly.

## Recommended next action
Have the parent check its own connected artifact list for a pre-change `event-graph-<revision>.json` URI. If one is absent and a reverse-oriented diff is useful, compare current source against the archived source captures through `proposedSources` and label the direction explicitly. If canonical pre-change-to-current comparison is required, mark that route unavailable and retain a scan-generated graph snapshot before the next source change.

## Addendum: archived source overlays
The installed parser supports using archived source text as a proposed overlay without editing the workspace, but the comparison direction is fixed: `proposedSources` builds the proposed graph as the `after` side. With the working tree already in its post-edit state, the only source-backed call is therefore post-edit current graph → archived pre-edit overlay graph, which is a reverse comparison.

Each strict `proposedSources` item has `{ "relativePath": "<workspace-relative .txt/.yml/.yaml>", "source": "<archived UTF-8 text>" | null, "expectedSourceHash": "<64-character sha256>"? }`. A string replaces or adds a mod source in the in-memory file copy; `null` deletes a source that currently exists in the active mod root. `expectedSourceHash`, when supplied, is checked against the current logical active file before the overlay is applied, so for an archived-before overlay it should be the SHA-256 of the post-edit file currently in the workspace. The schema accepts 1–64 overlay items, each source is bounded by the parser's 32 MiB per-file limit, and all non-null source strings together are capped at 64 MiB. Paths are portable workspace-relative text paths, and duplicate paths are rejected case-insensitively.

Example request for a reverse comparison from the current post-edit workspace to a virtual archived-before overlay:

```json
{
  "workspaceId": "mod_chaos_redux_ea3b2d67c2c0",
  "proposedSources": [
    {
      "relativePath": "events/example.txt",
      "source": "<archived pre-edit file contents>",
      "expectedSourceHash": "<sha256 of the current post-edit file>"
    },
    {
      "relativePath": "events/added_after.txt",
      "source": null,
      "expectedSourceHash": "<sha256 of the current post-edit file>"
    }
  ],
  "selector": { "kind": "event", "eventId": "cbrn_bio_lifecycle.1" },
  "render": true,
  "maxChainNodes": 8,
  "maxRenderNodes": 80,
  "refresh": true
}
```

This route builds a proposed graph in memory for that one comparison, but it does not cache that graph or write an `event-graph-<revision>.json` snapshot. The returned MCP summary exposes `beforeRevision`, `afterRevision`, graph hashes, counts, validation, and comparison artifact links. The comparison artifact stores the revisions, hashes, evidence and structural diff, but not either graph. `#resolveGraphReference` can restore only process-local remembered graphs or retained `event-graph-<revision>.json` / `event-scan-<revision-prefix>.json` artifacts, so the proposed `afterRevision` cannot be passed to a second comparison as a recoverable `{ revision }` reference. A second compare cannot turn the virtual archived graph into the required `before` graph; `after` and `proposedSources` are mutually exclusive, and no proposal graph artifact URI is returned.

Therefore, a two-step reverse-then-correctly-oriented comparison is not supported by this installed event API. The single reverse comparison is supported and can show the structural delta with the archived source evidence, but it must be recorded with its actual orientation. A canonical pre-edit → current post-edit comparison still needs a valid graph reference captured from the pre-edit source revision, or a separately supported way to analyze a virtual workspace that this parser does not expose.

| Additional installed source | Evidence |
| --- | --- |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\schemas\event.js` | Lines 91–97 define each overlay; lines 147–153 reject simultaneous `after` and `proposedSources`; lines 161–174 define the enclosing request. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\event\service.js` | Lines 293–320 validate portable paths and total bounds; lines 1182–1269 clone current cached files, apply overlays, and build the proposed graph; lines 1318–1331 route it to the `after` side; lines 1390–1479 write a comparison artifact and optional render files, then return internal graph objects to the operation wrapper. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\event\operations.js` | Lines 128–195 expose revisions, hashes, counts, links, and validation but not the `before` or `after` graph object. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\event\limits.js` | Lines 19–20 set the 64-file and 64 MiB total overlay ceilings. |
| `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools\dist\hoi4_agent_tools\core\source\limits.js` | Line 5 sets the 32 MiB per-file source ceiling. |
