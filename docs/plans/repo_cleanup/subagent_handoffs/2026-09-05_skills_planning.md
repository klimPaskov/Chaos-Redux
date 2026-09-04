# Planning skill review handoff

Disposition: implemented within the bounded documentation cleanup scope, pending parent review.
Acceptance basis: the parent assigned cleanup of the two named skills under the user's authorized instruction review and explicitly reserved source, provider, spending, model, reasoning, permissions, access, safety, and trigger gates.
This handoff records those boundaries and does not accept any event design or resolve protected policy conflicts.
After parent review, the parent explicitly assigned two ownership wording clarifications supported by existing AGENTS.md and shared routing authority.
That follow-up preserved permission, source, deletion, and trigger gates.

## Files and full reads

Fully read these files before editing, using complete consecutive chunks where the initial raw tool output was truncated:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-planning/SKILL.md`, all 2291 original lines
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`, all 287 original lines
- `.agents/skills/chaos-redux-subagents/SKILL.md`, all 363 lines at review time
- `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md`
- `.codex/agents/chaosx_improvement_loop_planner.toml`
- `.codex/agents/chaosx_skill_maintainer.toml`
- `.codex/agents/chaosx_3d_model_pipeline.toml`

Before the follow-up edits, fully reread the current improvement-loop skill and this handoff, then fully read `.codex/agents/chaosx_spreadsheet_doc_worker.toml`.
Rechecked the current AGENTS.md workbook routing and export rules and the shared subagents skill's plan-only, spreadsheet ownership, and parent-owned cleanup passages.

Opened the first 24 lines of each required offline wiki core page for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
Inventoried the installed vanilla documentation and consulted the opening Script Concepts and Bindable Localization material in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md`.
These were limited reference consultations, not full wiki or engine documentation audits.
No engine syntax, gameplay mechanic, provider workflow, or asset format was changed.

The supplied before-change baseline was `C:\Users\klimp\.codex\visualizations\2026\09\04\01a06e33-dc56-78e3-a787-850360234143\documentation_review\skills_batch02_baseline\files`.
Both owned skill files matched that baseline before editing.

| File | Baseline SHA256 |
| --- | --- |
| `.agents/skills/chaos-redux-event-planning/SKILL.md` | `DA0D646C4B939510796EE4505B85D81C6EC21FAEB33EDC93AEFE2CCAA9AD8C5A` |
| `.agents/skills/chaos-redux-improvement-loop/SKILL.md` | `A572D7E1F6E83E6AA72FCFA9FA5A0A2AEE360AEC1364154C62A24C8E2078A854` |

## Changes

| File | Disposition and exact change | Evidence |
| --- | --- | --- |
| `.agents/skills/chaos-redux-event-planning/SKILL.md` | Implemented four spawn argument corrections, clarified acceptance before promoting improvement proposals, separated parent evidence review from user live validation, and replaced one prose semicolon with a sentence boundary | Current `collaboration.spawn_agent` schema, AGENTS.md Subagents and Specs and Plans sections, shared subagents skill, and the 3D role's completion boundary |
| `.agents/skills/chaos-redux-improvement-loop/SKILL.md` | Implemented one spawn argument correction, recorded acceptance basis and queued-design dispositions, separated parent evidence review from user live validation, replaced one prose semicolon with a sentence boundary, and identified the existing workbook and temporary-workspace cleanup owners | Same instruction sources, the existing plan-only role boundary, the canonical spreadsheet role, and explicit parent follow-up |
| This handoff | Implemented the required batch evidence and unresolved-conflict report | Parent-assigned output path |

All five old `fork_context=false` tokens became Codex-specific `collaboration.spawn_agent` guidance using `fork_turns="none"`.
The affected examples still require explicit self-contained prompts and retain their existing deployment gates.
Acceptance corrections follow the existing AGENTS.md rule that a path, status label, old handoff, or implementation does not establish approval.
The skills retain parent acceptance within user-authorized scope and do not introduce another user approval step.
The live-testing correction retains parent source and MCP validation, final wiring, and review of available user-supplied evidence.
The follow-up assigns the planner an alignment handoff, the parent coordination of `chaosx_spreadsheet_doc_worker` after implementation facts exist, and that worker the authoritative workbook update and post-save CSV export.
Temporary-workspace cleanup now explicitly belongs to the parent under existing deletion authorization and completion/source rules.
All retention, provenance promotion, runtime-reference verification, whole-workspace cleanup, expected-absence, and protected-reference conditions remain intact.

## Meaningful checks

- Both updated skill folders passed `C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py`.
- The improvement-loop skill passed the same validator again after the two ownership clarifications.
- Reviewed the complete patch against the original files and confirmed four corrected spawn examples in event-planning and one in improvement-loop.
- Both frontmatter blocks are unchanged, preserving their selection descriptions and invocation behavior.
- Verified that `.tools/export_event_catalog_csv.py` and `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/` exist.
No helper-path correction was needed.
Neither helper implementation nor template contents were audited or executed.
- Used the available tool catalog only to verify exposed names for `mcp__hoi4_agent_tools__hoi4_tech_inspect`, `mcp__hoi4_agent_tools__hoi4_tech_render`, `mcp__hoi4_agent_tools__hoi4_tech_compare`, `mcp__hoi4_agent_tools__hoi4_gui_inspect`, `mcp__hoi4_agent_tools__hoi4_gui_render`, `mcp__hoi4_agent_tools__hoi4_gui_rewrite`, and the probability inspect, evaluate, sweep, simulate, sequence, compare, and render routes under the same server prefix.
No HOI4 MCP engine route, provider, Blender, game, or RunPod call was made.
Tool exposure does not establish service health or standalone viewer availability.

## External candidate copies and concurrent delta

At the parent's request, reconstructed both candidate skills from the supplied hash-verified baseline plus only this worker's exact replacements.
Event-planning used eight bounded replacements and improvement-loop used six, including the two ownership clarifications.
The candidates preserve baseline encoding and line endings.
Both external candidate skill folders passed the official skill validator.
Their root is `C:\Users\klimp\.codex\visualizations\2026\09\04\01a06e33-dc56-78e3-a787-850360234143\documentation_review\reviewed_candidates`.

| Candidate relative path | SHA256 |
| --- | --- |
| `.agents\skills\chaos-redux-event-planning\SKILL.md` | `D7368F71614B77368760733552AFA66C0A86AAB30A691058283941CDED63DC4C` |
| `.agents\skills\chaos-redux-improvement-loop\SKILL.md` | `42D9ED64A278F2D12D346258A2FDA91E0060E3DEB516BDA05C098FA7FC032F9C` |

Improvement-loop candidate content matches the current repository file after newline normalization.
Its byte differences are line-ending differences only.
The event-planning repository file contains one additional hunk near its scripted GUI handoff around line 1431 that was not authored by this worker.
That hunk adds reference-image planning through `chaos-redux-scripted-gui`, records plan or image acceptance evidence, and changes the referenced GUI layout contract from decisions-missions to scripted-gui.
The current file was preserved and this extra hunk was excluded from this worker's candidate.
Its owner and acceptance basis are unverified within this batch, so it was reported to the parent as an unknown concurrent delta for separate review.
No other content differences were found at candidate reconstruction time.

## Review findings and dispositions

The workbook and cleanup ownership findings were resolved through the parent-assigned clarification of existing authority.
Flag source, model reference source, deployment cadence, and portrait routing findings remain protected and unresolved.
A concurrent correction to the viewer wording is identified separately below.
Quoted wording is evidence, not an instruction to execute those actions during cleanup.

### Planner workbook ownership, resolved

Former improvement-loop wording in Relationship with other skills:

> When an improvement pass requires event-catalog alignment, update only the authoritative `docs/spreadsheets/chaos_redux_events_catalog.xlsx` workbook and then run `python .tools/export_event_catalog_csv.py`. The three catalog CSVs are export-only snapshots and must never be edited directly.

Improvement-loop, Subagent behavior:

> It should not edit gameplay files, localisation files, GUI files, scripted effects, focus trees, decisions, assets, or spreadsheets.

The canonical planner is plan-only and the shared routing skill assigns the catalog workbook to `chaosx_spreadsheet_doc_worker`.
The replacement explicitly requires the planner to return an alignment handoff and remain plan-only.
It names the parent as coordinator and `chaosx_spreadsheet_doc_worker` as the workbook owner after implementation facts are available.
It preserves the authoritative workbook, export-only CSV rule, and worker-run `python .tools/export_event_catalog_csv.py` after every successful workbook update from the mod root.
No workbook, export, or permission change was made in this task.

### Flag source mode

Improvement-loop, Asset and visual improvement:

> Use source-based assets for real people, real flags, real symbols, and real historical images.

Event-planning, Mandatory asset coverage and source-mode standard:

> Every new flag uses `$imagegen`.

The planning skill and shared subagents routing require historical research followed by a faithful flat ImageGen reconstruction.
The improvement-loop wording does not distinguish historical source research from final flag production.
It was not rewritten because source-policy changes are protected.

### Near-completion deployment and recursive planning

Event-planning, Mandatory near-completion improvement loop pass:

> Before any event-planning goal is treated as near complete, the coding agent must spawn `chaosx_improvement_loop_planner` for a final depth and anti-bloat pass. This is mandatory for event specs, large addenda, country packages, focus-tree plans, decision systems, super-event planning, asset-heavy plans, formable plans, custom UI plans, and any goal that creates or changes meaningful Chaos Redux design.

The same section retains:

> Tiny known-file text edits, narrow typo fixes, and direct one-line skill updates can skip the loop pass only when they do not create or change event design, mechanics, focus trees, decisions, country packages, assets, super-events, or implementation handoff rules.

Canonical planner role:

> Do not run another pass for the same event while your previous addendum is still unresolved.

The planner must read event-planning, whose large-addendum and handoff wording can be read as requiring a recursive final planner pass.
No trigger gate or exception was changed and no planner was spawned for this instruction-only batch.
The parent must retain this ambiguity in the broader cleanup disposition.

### Model reference source gate

Event-planning, 3D model and skeletal animation planning standard:

> If the user does not provide a ready reference image, plan exactly one clean Meshy-ready reference image for the asset and route it through the approved image-generation workflow before the provider gate.

Canonical 3D role, Required source discipline:

> Search and select actual Internet-sourced modern designed artwork before approving a model reference, using game concept, character or unit, production or promotional, tabletop or miniature, fantasy or horror, or professional design-sheet art.

The planning passage leaves the source-first requirement implicit.
It was preserved because this batch cannot change source or provider gates.

### Character portrait routing

Event-planning, Asset planning:

> Generated non-portrait art remains appropriate for people-free symbolic councils, invented high-chaos identities, idea icons, focus icons, decision icons, achievements, faction emblems, UI art, and fictional or alternate-history report, news, and super-event images unless the user says otherwise.

AGENTS.md requires every character portrait to use `chaosx_portrait_creator`.
The skill elsewhere treats councils and symbolic leadership as portrait surfaces, so a people-free council used as a character portrait can be misrouted by the quoted category label.
This source and ownership ambiguity is preserved.

### Viewer availability check and concurrent role correction

Canonical planner role at the time of its complete read:

> Event and Technology Tree Viewers never write, and the installed package has no Technology Tree Viewer; record that limitation.

AGENTS.md and the shared subagents skill require standalone viewer availability to be verified separately from exposed technology routes.
This batch verified exposed tool names only.
Standalone viewer availability and service health remain unverified because engine and provider calls were excluded.
The role was read-only for this worker and was not edited by this worker.
Final quote verification found that another batch had replaced the unconditional absence claim with this current wording:

> Event and Technology Tree Viewers never write. Verify standalone Technology Tree Viewer availability separately from tool exposure and service health, following the MCP evidence section of `chaos-redux-subagents`. Record verified absence as a package gap without inventing capabilities.

The wording conflict is therefore corrected concurrently, while actual service health and standalone viewer availability remain unverified in this batch.

### Temporary asset workspace deletion, resolved

Former improvement-loop wording in Asset and visual improvement:

> Before the event goal is fully complete, promote durable provenance, coverage, review, and runtime-wiring facts into permanent event or plan documentation, verify that no runtime reference points into `docs/assets/`, and delete the complete workspace.

The shared subagents skill assigns temporary-workspace cleanup to the parent, while the improvement planner is plan-only.
The replacement names the parent as cleanup owner under existing deletion authorization and completion/source rules.
It retains the active, blocked, or incomplete workspace retention condition, required durable provenance and runtime-wiring promotion, runtime-reference check, complete-workspace deletion condition, expected absence after closure, and prohibition on deleting skill-local reference assets or another event's workspace.
This is an ownership clarification, not additional deletion authorization or an approval gate.
No workspace was deleted.

## Unreviewed references and remaining parent work

Other system skills named in the planning files were not fully read in this batch, including events, event-assets, frame-animation, super-events, focus-trees, decisions-missions, and the 3D pipeline skill.
Their asset libraries, source records, consumer definitions, provider locks, generated roles, event specs, gameplay files, workbook contents, and template contents remain outside this review.
The official skill validator was executed as supplied and its implementation was not audited.
No engine or provider behavior was tested and no broad consistency claim is made for those references.

The parent should review the three owned outputs, reconcile this handoff with concurrent batches, and decide whether any protected conflict merits a separately authorized policy change.
AGENTS.md and the shared subagents skill already contain the current fork argument, acceptance rule, and user-only live-testing boundary, so these corrections need no further routing edit there.
No new skill was created.
The two named skills were updated and all other skills were left untouched by this worker.
No gameplay, asset, workbook, configuration, generated role, sync output, or commit was created or changed.
No simplifications were made to the authorized narrow corrections.
The four protected source, cadence, and portrait conflicts remain unresolved as listed above.
The two ownership wording findings are resolved, and the viewer assertion was corrected concurrently while actual availability remains unverified.
