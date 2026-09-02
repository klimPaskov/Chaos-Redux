# Focus Rewrite Scope Skill Note Handoff

Date: 2026-09-02

## Status

Complete for the bounded skill-maintenance scope. This subtask changed only the existing focus skill and this handoff. No gameplay, MCP configuration, generated-agent, staging, log, asset, or spreadsheet files were changed. No commit was created.

## Verification proof

- The installed production package is `hoi4-agent-tools` version `3.0.7` at `C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.7\node_modules\hoi4-agent-tools`.
- The actual rewrite route is `hoi4.focus_rewrite` (`dist\hoi4_agent_tools\mcp\tools\focus.js:848-856`). Its schema accepts `layoutMode = authored|compact`; in national mode it requires a plan unless compact, requires `treeId` for plan-free compact reflow, rejects compact mode for continuous palettes, and validates supplied plans (`focus.js:216-305`).
- The installed focus service executes the planned transaction and reports proposed/applied files and diagnostics (`mcp\tools\focus.js:1077-1161`). Focus planning sidecars are source-hash-bound metadata that the importer reads and enriches alongside focus source (`focus\planning.js:6-10`, `focus.js:510-524`), and the renderer emits a `.focus.plan.json` sidecar artifact (`focus\render.js:492-534`).
- The existing layout guidance already required MCP inspection and review, but did not explicitly stop a scope-preserving rewrite after schema rejection or distinguish a precise tool/schema blocker from permission to compact or auto-layout.

## Exact skill edit

Updated `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-focus-trees\SKILL.md` under `## 12. Layout rules`, immediately after the existing `hoi4.focus_rewrite` instruction.

Added a reusable scope-safety rule requiring agents never to switch to `layoutMode: "compact"` or auto-layout outside scope, to capture an immutable before snapshot, preserve accepted non-layout edits, and roll back only proven tool-generated drift through normal `apply_patch` with rejected/restored evidence.
Parent review clarified that reward-only changes preserving geometry require inspect/render/comparison evidence but do not require an automatic layout rewrite.
A schema error should first be corrected using the actual schema within the accepted scope; only an unavailable required identity-preserving operation is a tooling blocker.
The rule also requires comparing focus IDs, count, coordinates, prerequisites, and `HEAD` versus the dirty index.

## Caveats and parent review

- This is documentation guidance only. No live MCP call, game run, or log inspection was performed for this follow-up.
- The skill contains no event-specific identifiers, scenarios, paths, or history.
- The rule does not assume that every compact rewrite drifts layout. It limits compact or auto-layout use to explicitly in-scope work and requires evidence before any rollback.
- The parent should review the focused diff and create the meaningful closure-tranche commit separately.
