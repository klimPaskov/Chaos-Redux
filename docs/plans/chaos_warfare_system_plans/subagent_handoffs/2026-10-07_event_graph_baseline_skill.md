# Event graph baseline skill handoff

Disposition: implemented as a documentation-only reusable skill addition; parent review and isolated commit remain pending.
Acceptance basis: the parent explicitly assigned this bounded rule and handoff on 2026-10-07.
Owner scope: `.agents\skills\chaos-redux-subagents\SKILL.md` plus this handoff.
No gameplay, index, commit, or other skill changes were made.

## Change and validation

Added four sentences to MCP evidence guidance immediately before the focus render-budget paragraph.
The rule requires retaining an inspect-scan graph artifact before edits, checking the connected version and live reference shape, labeling an archived-source overlay comparison with its actual reverse direction, and preserving shared source.
It distinguishes a reported revision or bounded report from a recoverable graph and prevents a proposed overlay graph from being treated as an exported baseline.
Existing instructions already cover MCP handoff evidence, so no new skill was created.
No subagent identifier, routing ownership, or `AGENTS.md` change is needed.

The exact resulting skill bytes match the saved after snapshot.
Removing the insertion reproduces the exact working-before bytes, including other actors' existing edits.
There are no skill-scope blockers or simplifications.
This worker made no additional graph calls and makes no new live-service or engine-validation claim.
The parent's cited route review supplies the existing connection evidence; this worker checked its cited installed documentation and parser directly.

## Evidence

Reviewed `docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-10-07_mcp_event_comparison_route_review.md`, supplied as committed in `079cd018` by the parent.
The installed package read was `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools`, documented by that review as version 3.10.0.
Concrete versions and package paths remain here rather than in the reusable skill.

| Installed source relative to that package | Sections read | SHA256 |
| --- | --- | --- |
| `docs\events.md` | 81–89: graph references and proposed overlays | `8E06D594FB46D0A8718CE6596FB2E8372C06A8731B481626EECF3EEEBF8E5B36` |
| `dist\hoi4_agent_tools\schemas\event.js` | 79–97, 147–174: strict graph reference and overlay request | `C9A7A3966BE58E95473EB146F4EE2A5A63221DADE5038BF5FAB500C2696E2B12` |
| `dist\hoi4_agent_tools\event\service.js` | 912–965, 1260–1479: scan-only graph artifact, graph restoration, proposed-after routing, comparison artifacts | `7004B76B5201FB8B9ECB84AC57DA00BC4D961F73D20740B0391D823B6F4C2423` |
| `dist\hoi4_agent_tools\event\artifact-validation.js` | 357–369: graph schema and identity requirements | `8E0FCBFCEAF953C4182DDAC0D1027A30625F0878627B6EC0F98A8CA448F09832` |
| `dist\hoi4_agent_tools\event\operations.js` | 128–195: public revisions, hashes, artifact links, and validation; no graph export | `5F7C3CF661A4CF2D5FBF4273DD250FB53740BD8A9D015A95C4602BBB5E03F85B` |

This is MCP evidence-protocol guidance, so wiki or vanilla script precedents do not establish the graph-reference contract.
The local parser evidence confirms the cited contract, but it does not independently establish the currently connected service's version or health.
Future callers must perform the live verification stated in the rule.

## Isolated insertion package

Snapshot directory: `C:\Users\klimp\AppData\Local\Temp\chaos-redux-event-baseline-d5f47296bd554381b01da2429fd31e31`.
Working-before file: `skill.before.bin`, SHA256 `D9379CC675100DBBE7CDEF0DE6A0579AAFF4545BE8B20DEE436864CA0225C383`.
Exact insertion file: `skill.insertion.bin`, SHA256 `019F1CAAD43735E0AB9EAFBD36ED111961E685B6116A1600DEC1E92480077B60`.
Resulting file: `skill.after.bin`, SHA256 `C0477E940B3315857C35ECF5DA6680A9B877FDA58885F32B598E7EDD701CD9D4`.
Zero-based byte offset: `40970`.
Insertion length: `779` bytes.
The insertion uses the existing line endings and ends with two line endings; it is inserted before the focus paragraph, with every original byte retained.

The skill is dirty from other actors.
The parent owns final review and the isolated commit; do not stage the entire skill merely to include this insertion.
The worker is frozen after validation.
