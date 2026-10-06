# Takeover skill notes

Disposition: implemented.
Acceptance basis: parent delegated a bounded reusable skill update for the verified recovery, artifact, selector, rendering, and isolated-index lessons from this pass.
The parent retains final review and commit ownership.

## Changes

- `.agents/skills/chaos-redux-events/SKILL.md`: added the discriminated event selector example, with live-schema verification.
- `.agents/skills/chaos-redux-subagents/SKILL.md`: added an optional read-only SDK stdio recovery route, explicit separation of plain client capabilities from native task negotiation, and separate live-schema checks for job tools.
Added render-budget recovery through supported scale and crops, configured artifact-root resolution, and the distinction between argument-shape rejection and service health.
- `.agents/skills/chaos-redux-shared-git-commit/SKILL.md`: added Windows PowerShell 5 `[string[]]` conversion before native Git path arguments and separate isolated add/cached-patch checks before publication.
- This handoff records evidence and review boundaries only.

Existing probability source-object instructions and binary artifact chunk/hash verification were retained rather than duplicated.
No new skill was needed.
No routing, AGENTS.md, gameplay, asset, spreadsheet, model, or audio changes were made by this worker.

## Evidence reviewed

The installed package is `C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/`.
The captured initialized connection in `docs/plans/012_africa_plans/mcp_recovery_2026-10-06/connection_and_schemas.json` reports server 3.9.0 and client capabilities `{}`; its tool schemas are the task evidence for this separate connection.
No native task negotiation or job execution is claimed.

Installed `dist/hoi4_agent_tools/schemas/event.js` lines 42-44 define `{ kind: 'event', eventId }` as a strict selector.
Installed `dist/hoi4_agent_tools/core/workspace.js` lines 392-400 derive the default workspace artifact root from `workspaceStorageRoot`; lines 575-587 resolve and validate the actual artifact root.
Installed `dist/hoi4_agent_tools/core/artifacts.js` lines 1054-1066 resolve hash-sharded artifact and manifest paths.
Installed `dist/hoi4_agent_tools/schemas/focus-requests.js` lines 64-82 expose bounded `reviewScale` and `cropFocusIds`.
Installed SDK `node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js` lines 65-73 spawn the server with `windowsHide` on Windows.
The installed configuration sets `workspaceStorageRoot` outside the repository, so repository-local artifact assumptions would miss production bytes.

The parent supplied the confirmed PowerShell 5 nested-array isolated-add failure and recovery.
This worker did not rerun Git publication or modify HEAD/index.
The updated instructions require exact path entries and an isolated cached-patch review before publication.

## Review constraints and limits

The skills already contained other agents' work when this task began.
Edits were exact anchored byte replacements after rereading; existing encoding and line endings were preserved.
Review and stage only the additions listed here, preserving prior changes, including the existing probability-scenario schema update.
No version, workspace ID, event ID, machine-specific artifact path, or event outcome was inserted into reusable skill prose.

The initialized connection and successful render results belong to the parent recovery evidence; this worker checked installed source/schema support but did not establish a new connection or rerun domain renders.
The official skill-creator quick validator accepted all three updated skills.
This checks packaging, not live engine behavior.
No simplifications were made in this bounded skill task; no requested skill item remains blocked.
No AGENTS.md or subagent routing update is required because role ownership and mandatory evidence gates are unchanged.
