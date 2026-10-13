---
name: chaos-redux-subagents
description: Use when coordinating Chaos Redux project custom subagents (the canonical Claude Code definitions or the generated Codex, Qoder, Cursor, and opencode definitions, plus DSH runtime-composed roles), routing bounded work, or defining parent/subagent ownership boundaries.
---

# Chaos Redux Subagents

Use this skill when a Chaos Redux task should be split across project custom subagents.

The parent agent remains responsible for final integration, final review, proportionate code review and local checks, and completion claims.
The user performs live-game validation; agents neither request nor await it to deliver implemented work.
Subagents inspect, patch, create assets, write addenda, or return bounded findings, and the parent carries material limitations and real blockers into the final report.

Do not use subagents to hide uncertainty or pass off responsibility. A subagent handoff is evidence for the parent, not a replacement for parent review.

## Fork context rule

All project custom subagents must be spawned with a fully explicit, self-contained prompt and no inherited parent-thread context. In the Claude Code, Qoder, Cursor, opencode, and DSH runtimes subagents are isolated by design, and the parent prompt must still carry every needed input; with the Codex `collaboration.spawn_agent` tool, set `fork_turns="none"`. Claude Code loads the canonical `.claude/agents/*.md` files as project subagents, and Cursor loads generated `.cursor/agents/*.md` files as native project subagents. Spawn them by hyphen-case name through `/name`, the Task tool, or the `Agent` tool. DSH composes each named role at runtime, so read the canonical identifier below as the role to instantiate. Do not substitute Cursor's built-in `explore`, `shell`, or `browser` agents, or Claude Code's built-in `Explore`, `Plan`, or `general-purpose` agents, for a named Chaos Redux specialist.

The parent prompt must include every path, user correction, task constraint, scope boundary, previous handoff status, accepted plan, queued plan, and design rule the subagent needs.
The role’s model comes from its runtime configuration; changing that configuration does not change an already-running agent’s model.

If the needed context only exists in conversation, summarize it into the subagent prompt or write it to the relevant spec, plan, handoff, or repo file before spawning.

This rule applies to every subagent type:

- read-only agents
- plan-only agents
- asset-production agents
- super-event research agents
- active small-patch agents
- event-owned scripted GUI implementation agents
- scripted-system agents
- documentation agents
- skill-maintenance agents

The goal is to keep subagents narrow, reproducible, and grounded in explicit inputs instead of inherited conversation state.

## Available project subagents

Identifiers below are the snake_case names of the Claude Code definitions in `.claude/agents/`, which are the canonical source and carry the hyphen-case file name (for example `chaosx_repo_explorer` is `chaosx-repo-explorer`). `python .tools/sync/sync_agents.py` generates the Codex TOMLs (snake_case), the Qoder, Cursor, and opencode definitions (hyphen-case), their maps (`.qoder/agents/README.md`, `.cursor/agent-map.md`, `.opencode/agent-map.md`), the versioned `.claude/agent-map.md`, and the `.claude/skills/` links to the canonical `.claude/skills/` folders. Generated Codex, Qoder, Cursor, and opencode files and the skill mirror are gitignored and appear after the sync runs; the Claude Code definitions, skills, and `CLAUDE.md` are versioned. Never hand-edit a generated definition: change the `.claude/agents/<name>.md` source and rerun the sync. This section remains the canonical cross-runtime mapping. Every agent file must stay `Agent`-tool and Task-tool compatible: one Markdown file per agent in the runtime's `agents/` folder, YAML frontmatter, then the prompt body, with no non-agent Markdown in that folder.

DSH composes subagents at runtime through its delegation tool and loads no agent definition files, so there is no DSH agent map and no DSH generator. DSH also does not read the generated `.codex/agents/*.toml` files, so a named role does not arrive with the model its definition names. Treat the canonical snake_case identifiers below as the named roles a DSH parent instantiates by writing the role boundaries into a fully explicit, self-contained delegation prompt.

Every DSH child runs on `deepseek-official/deepseek-flash` and nothing else, so specify no model. Naming `provider` and `model` together is allowed only as that pair; naming one alone is rejected, and effort may be named alone because the configured default already fixes the route. If a task looks like it needs a stronger model, split it into narrower bounded subagents instead. `subagent_fork` cannot select a child model, so use the ordinary delegation tool when the route matters. Model selection is sampled when a session is composed, so a session without those fields predates the opt-in rather than being misconfigured. DSH layout, skill roots, model selection, and MCP registration are documented in `docs/runtimes.md`.

Claude Code subagents run on the fixed model tier in their `model:` frontmatter, listed in the generated `.claude/agent-map.md` and governed by the routing table in `.tools/sync/agent_profiles.json`: `opus` for `chaosx_improvement_loop_planner`, `sonnet` for `chaosx_3d_model_pipeline`, `chaosx_event_completion_auditor`, `chaosx_localisation_auditor`, `chaosx_scripted_system_architect`, and `chaosx_skill_maintainer`, and `haiku` for every other specialist. The sync maps each tier to the other runtimes (Codex pins a model, Cursor uses `fast` or `inherit`, opencode and Qoder inherit), and `python .tools/sync/sync_agents.py --verify` reads the generated files back against the table. A new role needs its `.claude/agents` definition and an `agents` entry in the profile before the sync accepts it. Change a tier in the definition and the table together, rerun the sync, and override the model for a single spawn only when the task clearly exceeds or falls below the role's usual work.

Each definition also carries the Claude Code `effort:` frontmatter field. It overrides the session reasoning effort for that subagent (`CLAUDE_CODE_EFFORT_LEVEL` still takes precedence, the available levels depend on the model, and the parent may pass an `effort` for a single spawn). The table lives in `effort_policy` of `.tools/sync/agent_profiles.json`, `--verify` reads it back, and Codex receives it as `model_reasoning_effort` while Cursor, Qoder, and opencode drop it.

| Effort | Roles |
| --- | --- |
| `high` | The auditors that judge correctness (`chaosx_ai_probability_auditor`, `chaosx_country_package_auditor`, `chaosx_decision_mission_auditor`, `chaosx_event_completion_auditor`, `chaosx_focus_tree_auditor`, `chaosx_localisation_auditor`), plus `chaosx_3d_model_pipeline`, `chaosx_scripted_system_architect`, and `chaosx_improvement_loop_planner` |
| `medium` | Researchers (`chaosx_asset_source_researcher`, `chaosx_super_event_audio_researcher`, `chaosx_super_event_text_researcher`), art, icon, and portrait workers (`chaosx_generated_event_art`, `chaosx_icon_artist`, `chaosx_portrait_creator`), `chaosx_repo_explorer`, `chaosx_spreadsheet_doc_worker`, `chaosx_documentation_curator`, `chaosx_skill_maintainer`, `chaosx_event_ui_worker`, and the system workers `chaosx_equipment_units_worker`, `chaosx_technology_tree_worker`, and `chaosx_map_states_worker` |

Raise the effort for one spawn when a normally routine task carries a correctness risk; do not lower an auditor below `high`.

Use `chaosx_repo_explorer` only for read-only repo exploration when touched-file mapping, pattern search, vanilla reference mapping, missing-file recovery, dependency mapping, or edit-order planning is actually unclear. It is not a default preflight agent.

Use `chaosx_improvement_loop_planner` for event improvement loop planning, detailed expansion specs, historical and regional research notes, and implementation-ready improvement handoffs. This replaces the old mechanic-expander role. It writes plans and addenda. It does not patch gameplay files.

Use `chaosx_asset_source_researcher` for non-portrait real or archival image sourcing, historical flags, historical symbols, user-provided source photos, source-image processing, and report, news, or super-event images that must depict real historical material.

Use `chaosx_portrait_creator` for every character portrait. It researches and archives grounded sources, creates crops and placeholders, invokes the image-generation route for fictional or impossible subjects, processes PNG/DDS outputs, installs portrait-specific wiring, and writes manifests and handoffs. It validates user-supplied grounded finals and never operates RunPod. `.claude/skills/chaos-redux-event-assets/assets/visual_components/portrait_backdrops/` is reference-only and does not supply an identity source or final portrait.

Use `chaosx_generated_event_art` for generated non-icon art, including fictional or alternate-history report images, news images, super-event images, fictional flags, faction emblems, UI panels, dossier art, progression-state base art, and animated non-icon presentation pieces. It does not own final character portraits.

Use `chaosx_icon_artist` for focus icons, idea icons, national spirit icons, officer corps icons, decision icons, decision category icons, achievement icons, tech icons, formable seals, scripted GUI icons, and small animated icon or button sprites. Pass the exact vanilla or Chaos Redux consumer and canonical `gfx_references/` family first. When relevant, include the `.claude/skills/chaos-redux-event-assets/assets/visual_components/CATALOG.md` entry: focus pieces and backgrounds guide original generated composition; only `background_template` entries for idea, national-spirit, or decision-category consumers may be layered beneath an original generated subject when the consumer fits. Require a separate source layer and local catalog role in the output manifest; retain achievement-specific template and state rules.

Use `chaosx_3d_model_pipeline` for bounded Meshy 7 custom HOI4 3D model work covering geometry, provider candidates, Blender processing, model textures, rigs, skeletal actions, Internet-sourced unit-audio research, bespoke vanilla-green custom-unit counter requirements and handoffs, `.mesh`/`.anim` export, QA evidence, and runtime handoffs.

Use `chaosx_super_event_text_researcher` for super-event main quotes, exact wording checks, attribution confidence, source comparison, button text, cultural remarks, slogans, allusions, and short references.

Use `chaosx_super_event_audio_researcher` for licensed or public domain audio research, source verification, download, final `.ogg` preparation with original recordings preserved, and audio handoff notes.

Use `chaosx_focus_tree_auditor` for focus tree audits and active small patches covering branch depth, route coverage, icons, localisation, rewards, prerequisites, mutual exclusions, AI, focus-formable links, and simplification.

Use `chaosx_decision_mission_auditor` for decision and mission audits and active small patches covering category lifecycle, objective quality, costs, tooltips, scripted GUI decision hooks, AI behavior, cleanup, balance, and exploit risk.

Use `chaosx_event_ui_worker` to implement the dedicated scripted GUI window introduced by one named Chaos Redux event or event-owned mechanic under `chaos-redux-scripted-gui`.
It owns bounded layout and visual review, using targeted MCP inspect/render/comparison when available and source/local layout checks after the shared retry limit.
Fix confirmed visual defects, retain fidelity limits, and never claim a preview executes the game.
It must never audit the shared event log, event-details framework, settings UI, super-event framework, shared registries, or unrelated existing interfaces.

Use `chaosx_country_package_auditor` for country package audits and active small patches covering tags, custom-tag history, generated startup scientists, existing-country startup grants, states, leaders, portraits, flags, parties, focus loading, ideas, advisors, units, technologies, claims, cores, localisation, AI, formables, and playable setup.

Use `chaosx_localisation_auditor` for localisation and scripted localisation audits and active small patches covering missing keys, duplicate keys, encoding, tooltip quality, broken dynamic text, namespace consistency, dynamic cost text, and cross-surface text mismatch.

Use `chaosx_scripted_system_architect` for reusable scripted system design and active narrow implementation covering scripted effects, scripted triggers, script constants, event targets, meta effects, variables, tuning values, formable helpers, scripted GUI button helpers, and dynamic helper logic.

Use `chaosx_documentation_curator` for documentation cleanup and consistency during long implementation. It reconciles specs, plans, docs, handoffs, manifests, prompts, reports, and README files, writes source-of-truth maps and resume packets, marks superseded docs, records plan dispositions, and flags contradictions. It patches documentation surfaces only and does not edit gameplay files, localisation, assets, or spreadsheets.

Use `chaosx_event_completion_auditor` for read-only spec-versus-implementation audits covering events, mechanics, assets, docs, super-events, focus trees, decisions, validation, and accepted plan addenda.

Use `chaosx_ai_probability_auditor` for one bounded read-only audit of in-scope AI weights, MTTH, event `ai_chance`, random lists, focus/research selection, decision/mission scores, strategy factors, and custom weighted pools.
Prefer targeted probability tools, then use real source/helpers and named representative scenarios if the route fails, is partial, unsupported, or misclassifies the surface.
State exactly what the evidence establishes; recheck only owner-applied fixes, without repeated classification or audit-of-audit loops.

Use `chaosx_spreadsheet_doc_worker` only for the event catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. It uses the `chaos-redux-xlsx` skill, keeps the workbook player-facing, and matches event log, event detail, evolution detail, and cluster detail fields to the in-game wording.

Use `chaosx_equipment_units_worker` for bounded implementation and repair of equipment archetypes, variants, modules, CBRN payload lots, sub-units, support companies, package formations, AI templates, `script_enum_equipment_bonus_type` entries, and the test-country and Event 19 registrations a new equipment type or land sub-unit needs. It reads `chaos-redux-equipment` and `chaos-redux-units-divisions`, and hands models, counters, and art back through the parent.

Use `chaosx_technology_tree_worker` for bounded implementation and repair of technologies, technology folders and cards, project-gated and hidden technologies, grant helpers, doctrines, and the 70x70 folder grid, checked with `hoi4.tech_inspect` and `hoi4.tech_render`. It reads `chaos-redux-technology-doctrines` and hands card art to `chaosx_icon_artist` through the parent.

Use `chaosx_map_states_worker` for bounded implementation and repair of startup history grants, the generated `map/buildings.txt` override and spawn buildings, state-scope effects and iteration, exact civilian transfers, cohort registries, reception ledgers, and state map modes, checked with `hoi4.map_inspect` before any rewrite. It reads `chaos-redux-map-states`.

There is no separate worker for characters, ideas and modifiers, diplomacy, or AI: those surfaces stay with the parent, `chaosx_country_package_auditor`, `chaosx_scripted_system_architect`, `chaosx_decision_mission_auditor`, and `chaosx_ai_probability_auditor`, which load the matching `chaos-redux-*` system skill.

Use `chaosx_skill_maintainer` for skill creation, skill cleanup, routing updates, and multi-skill consistency work when a task reveals a reusable workflow, repeated mistake, repo-specific convention, validation pattern, asset or prompt pattern, or implementation rule that belongs in a repo skill. The role is runtime-neutral: it owns the skill files themselves, so it behaves the same in every runtime and is spawned by the same canonical snake_case identifier that the Qoder, Cursor, opencode, and Claude Code runtimes map to their hyphen-case equivalents.

Do not route new work to `chaosx_mechanic_expander`. Its role is merged into `chaosx_improvement_loop_planner` and the `chaos-redux-improvement-loop` skill.

## Routing gates

### Event UI worker gate

Spawn `chaosx_event_ui_worker` with a fully explicit, self-contained prompt (Codex `collaboration.spawn_agent`: `fork_turns="none"`) only when the accepted event spec or implementation explicitly introduces a dedicated scripted GUI or mechanic window. The parent prompt must provide the event id and slug, exact GUI identifiers and owning files, entry point, accepted layout brief and acceptance basis, reference-image paths or a bounded reference-production assignment, image-to-native mapping, intended states and resolutions, linked decisions and scripted-GUI identifiers, approved asset handoffs, allowed files, and handoff path.

The worker is patch-capable for the accepted event-owned `.gui`, presentation-only `common/scripted_guis` wiring, event-owned `.gfx`, and event-owned GUI localisation.
It owns hierarchy, spacing, alignment, background coverage, states, click regions, and available before/after visual evidence.
The parent and decision worker retain event outcomes, costs, AI, balance, reusable logic, and final integration; the parent reviews the bounded handoff without awaiting user live-game validation.

Do not route a GUI merely because an event appears in or opens it. The shared event log, event-details framework, settings UI, super-event framework, shared registries, utility/debug windows, and unrelated existing UIs remain out of scope. The prompt must identify the exact source or accepted specification proving event ownership.

Apply `chaos-redux-scripted-gui` for reference creation before implementation, justified native adaptations, the complete visual checklist, and exact discovered MCP schemas. Record user direction or parent acceptance within the authorized scope; document existence alone is not approval. Shared interfaces remain parent-owned even when this skill is used.

Review includes `hoi4.gui_inspect`, pre-change `hoi4.gui_render` full-window and relevant cropped, annotated, state, resolution, hierarchy, click-region, and comparison views, then post-change inspect/render comparison over matching explicit scenarios, source identities, states, resolutions, and UI scales. There is no separately exposed GUI comparison tool; preserve baseline artifacts and use the render route's supported `comparisonScenario` only for its documented scenario comparison. In the available production renders, visible alignment, spacing, clipping, overflow, background, asset, text, state, and click-region defects block completion and may not be excused as renderer differences. If inspect/render evidence remains unavailable after the AGENTS.md retry limit, review the same layout requirements from source and disclose which visual checks were unavailable; do not claim the source review was a rendered or in-game check. `gui_rewrite` is optional, and its automatic post-write/index validation or transaction success is not a completion gate; direct application of an authorized reviewed edit follows `chaos-redux-scripted-gui`.

### Repo explorer use gate

`chaosx_repo_explorer` is an optional scout for uncertain or broad work. It should save time by finding files, patterns, precedents, and edit order before the parent starts a complex implementation.

Use `chaosx_repo_explorer` when at least one of these is true:

- the parent does not know the likely touched files
- the task spans several systems and the edit order is uncertain
- the correct Chaos Redux pattern or vanilla precedent is unclear
- a named spec, prompt, source file, classification, sprite, tag, localisation key, or helper appears missing and needs recovery evidence
- the feature has enough cross-surface risk that a file map and meaningful validation plan will prevent missed work

Do not spawn `chaosx_repo_explorer` for small or already bounded work, including:

- known-file edits
- user-provided file updates
- direct skill, prompt, or TOML updates
- small bug fixes where the relevant files are already named
- localisation-only cleanup with known keys
- asset-only production that belongs to an asset subagent
- spreadsheet-only catalog updates that belong to `chaosx_spreadsheet_doc_worker`
- simple report, docs, or markdown edits where the parent can inspect the provided files directly

When the task is small, the parent should read the known files directly and proceed. Do not use repo exploration as a ritual step or as a replacement for parent review.

## Authority model

Subagents should act at the level their role requires. Do not make every subagent read-only by default.

### Read-only agents

These agents do not patch gameplay files:

- `chaosx_repo_explorer`
- `chaosx_event_completion_auditor`
- `chaosx_ai_probability_auditor`

They may write reports only when a report path is provided or obvious from the task.

Some runtimes refuse report-file writes from subagents. Ask every read-only or audit subagent to return its complete findings inline as well, and keep scratch helpers and intermediate data such as scan outputs or range lists under `.tmp/<task>/`, where the parent can read them afterwards. Do not install one-off audit/report scripts in `.tools/`.

### Plan-only agents

`chaosx_improvement_loop_planner` writes event expansion specs, improvement addenda, deep research notes, historical connection notes, and implementation handoffs. It does not edit gameplay, localisation, GUI, scripted effects, focus trees, decisions, assets, spreadsheets, or country files.

When an event mechanic needs more depth, new branches, new countries, a new formable suite, a new scripted GUI system, deeper regional logic, historical anchors, or a larger route redesign, the planner writes a plan under `docs/plans/<event_id>_<event_slug>_plans/`. The main agent decides what to implement.

The parent should use this planner after a substantial implementation stage, not after every small patch. Do not spawn it again for the same event until its previous addendum has been implemented, folded into specs, queued with a reason, or rejected with a reason.

### Documentation curation agents

`chaosx_documentation_curator` is patch-capable for documentation surfaces only. It may update Markdown specs, docs, plans, handoffs, manifests, prompt files, README files, route coverage tables, source-of-truth ledgers, resume packets, and documentation indexes inside the current task scope.

Use it after long implementation stages, after several subagent handoffs, before a major resume, or whenever docs may be stale, contradictory, duplicated, or too numerous. It should distinguish explicit user decisions, accepted design with its acceptance basis, current implementation evidence, and proposals. Apply the AGENTS.md Specs and Plans dispositions: `unresolved`, `accepted and queued` with acceptance basis and reason, `implemented` with evidence and validation limits, `promoted into an accepted spec` with acceptance basis and destination, `rejected` with recorded reason, `superseded` with a named replacement, or `blocked` with the exact limitation.

For package cleanup, apply these evidence rules:

- Identify whether a manifest or QA receipt describes an original archive, an earlier review, or the current checkout before changing it. Preserve historical bytes, hashes, and results with their scope and date; refresh a current inventory from the edited files and report only checks actually rerun.
- Consolidate a combined spec copy only after comparing its bodies with the authoritative parts, checking incoming references, and preserving any unique design, acceptance evidence, or provenance. Repair callers and leave a successor pointer where needed; a matching title alone does not prove duplication.
- Link mutable production and routing rules to their current owner skill instead of repeating them in each prompt. Check active tool arguments against the connected schema; the Codex no-inheritance argument is `fork_turns="none"`. Keep dated capability failures as history and rediscover current exposure, schemas, and health before making a present-tense capability claim.
- Decode and write Markdown/JSON explicitly as UTF-8 on Windows; do not round-trip UTF-8 without BOM through default Windows PowerShell `Get-Content`/`Set-Content`, and check introduced mojibake against immutable source files before updating manifests.

It must not edit gameplay files, localisation, scripted localisation, GUI, GFX, events, focuses, decisions, ideas, scripted effects, scripted triggers, on_actions, country setup, history, AI files, assets, audio, binary files, or the event catalog workbook. It does not replace `chaosx_event_completion_auditor`, `chaosx_localisation_auditor`, `chaosx_spreadsheet_doc_worker`, or `chaosx_repo_explorer`.

### Skill maintenance agents

`chaosx_skill_maintainer` is patch-capable for repo skills and skill assets and for the routing references that point at them.

It creates a skill under `.claude/skills/<skill-name>/SKILL.md` when the workflow is reusable and not already covered, updates an existing skill when the workflow belongs there, audits skills for overlap, unclear instructions, stale paths, event-specific leakage, and missing reusable guidance, and keeps several skills consistent when one routing rule or convention spans them. It updates skill-local reference material and the routing references that name skills, including the canonical subagent entries in this skill and the runtime agent or skill registrations that mirror them. Its edits stay reusable and non-event-specific, and each skill stays focused on one reusable workflow.

It must not edit gameplay files, localisation, events, focuses, decisions, ideas, scripted effects, scripted triggers, on_actions, country setup, history, AI files, GUI, GFX, assets, audio, binaries, spreadsheets, or docs and specs outside an explicitly granted documentation scope, and it must not hand-edit another runtime's generated agent or skill definition files.

### Asset-production agents

Asset subagents create source files, processed previews, final DDS outputs, contact sheets, manifests, and asset handoffs. During active work, event-scoped evidence belongs under the temporary `docs/assets/<event_id>_<event_slug>/` workspace. They do not wire gameplay, localisation, GFX, GUI, events, focuses, decisions, or spreadsheets unless the parent gives a narrow exception.

The parent owns temporary-workspace cleanup. Keep the event-scoped `docs/assets/` workspace while the event is active, blocked, awaiting review, or undergoing acceptance scenarios. Before declaring the event goal fully complete, promote durable provenance, licensing, attribution, coverage, review, and sprite-handoff facts into permanent event or plan documentation, verify that no runtime reference points into `docs/assets/`, then delete the complete event-scoped workspace. An absent workspace is expected for a fully complete event. Never delete a skill-local reference library or an unrelated event workspace.

#### 3D model routing

Route `chaosx_3d_model_pipeline` with the self-contained, history-free prompt required above. The parent supplies owner/event/system and asset IDs, requested operation, deterministic job root, reference path or approved brief, output folders, handoff path, profile, vanilla references and scale relationship, required action roles, component inventory, sound roles, source/licensing constraints, counter consumers/tokens and exact vanilla definition/DDS/reference family, icon-artist handoff path, planned paid operations, recorded recovery limits, dependency lock, and forbidden simplifications.

Before dispatch, read [Route selection and component completion](../chaos-redux-3d-model-pipeline/SKILL.md#route-selection-and-component-completion), [Job intake and deterministic layout](../chaos-redux-3d-model-pipeline/SKILL.md#job-intake-and-deterministic-layout), and [Bounded subagent route](../chaos-redux-3d-model-pipeline/SKILL.md#bounded-subagent-route).
Those sections own operation selection, provider/key/dependency gates, separate body/item generation, one supported rig/action attempt, already-authorized Blender fallback/component work, source integrity, and credit limits.
Do not copy the production manual into the prompt or invent live tools; pass the accepted inputs and conditional references.
For humanoids, provide the exact source-height/entity-scale/runtime-height comparison; for buildings, provide the valid state/province pair and visibility test location.

The worker owns source preparation, Meshy body/item candidates and supported rig/actions, provider ingestion, live Blender assembly/authoring/corrections, complete components, materials, geometry/weight/contact/action review, and export/reimport under the 3D skill's no-shortcut rules.
It must read [Blender authoring, processing, and PDX export](../chaos-redux-3d-model-pipeline/references/blender-processing-and-export.md) for those operations and [Custom-unit audio and counter delivery](../chaos-redux-3d-model-pipeline/references/unit-audio-and-counters.md) for every custom unit.
Require licensed Internet-sourced audio and original vanilla-green counters for each actual consumer; generated/placeholder audio, reused counters, arbitrary green, static action substitutes, and omitted components cannot satisfy delivery.

Require the complete [Evidence package and handoff](../chaos-redux-3d-model-pipeline/SKILL.md#evidence-package-and-handoff), including dependency and provider/attempt lineage, credits, checkpoints, authoring/repair basis, retained valid outputs, model/action/export results, audio attribution/synchronization, counter references/comparisons, exact runtime identifiers, meaningful checks and their limits, and remaining work.
The parent reviews that package and owns final `.asset`, entity, GFX, sound-definition, gameplay, and runtime wiring, evidence reconciliation, and the overall completion claim.
The worker may not edit those surfaces or localisation, GUI, country/history/AI, on-actions, or spreadsheets without an explicit narrow exception.
Inspectors/viewers stay read-only. The user performs in-game validation; provider success, a preview, or an export is not a claim of live completion.

### Active small-patch agents

These agents are patch-capable by default inside the current task scope:

- `chaosx_scripted_system_architect`
- `chaosx_equipment_units_worker`, `chaosx_technology_tree_worker`, and `chaosx_map_states_worker` for their own system surfaces only
- `chaosx_decision_mission_auditor`
- `chaosx_focus_tree_auditor`
- `chaosx_country_package_auditor`
- `chaosx_localisation_auditor`
- `chaosx_event_ui_worker` for an accepted event-owned UI only
- `chaosx_skill_maintainer` for skills and skill assets only
- `chaosx_documentation_curator` for documentation surfaces only
- `chaosx_spreadsheet_doc_worker` for the event catalog workbook and its exports only

They do not need a separate permission prompt to fix small, local issues that are clearly connected to the current event, mechanic, country, focus tree, decision category, GUI surface, or localisation surface.

They should inspect first, then patch only when the fix is narrow, reversible, and supported by the relevant skill. They may edit files they own for the current task surface and directly related dependency files. They must not search for unrelated cleanup outside the feature they were spawned for.

Active small patches include:

- varying decision costs inside an existing category
- making cost and requirement text clearer
- adding dynamic localisation for existing variables, targets, state names, route names, or cost values
- replacing raw trigger exposure with custom trigger tooltips
- adjusting safe AI weights or target checks
- fixing obvious availability, visibility, cooldown, bypass, and cleanup gaps
- fixing focus prerequisites, route locks, mutual exclusions, focus filters, icon references, and small reward variety
- adding a narrow scripted helper plus a few direct call sites when repeated logic is already present
- fixing an existing formable decision check, reveal condition, or state-control requirement
- correcting country package references such as focus loading, party names, leader ids, tag setup, localisation, and simple starting setup
- correcting a stale path, an unclear instruction, or a missing reusable rule inside a skill that already owns the workflow

Any patch to an AI weight, probability-bearing modifier, MTTH-backed score, random-selection weight, strategy factor, or weighted target check requires a bounded baseline and post-fix comparison using the same named scenarios.
The parent or owner preserves pre-edit source bytes and the scenario fixture; the read-only probability auditor reviews the baseline, then the owner applies the patch and the auditor compares the changed behavior.
Use `hoi4.probability_analyze` (`analysis = compare`) when supported, or retain a before/after source/helper comparison with scenario scores and stated assumptions when the tool cannot answer.
If the original source or a trustworthy snapshot cannot be recovered within the check limit, review current behavior and state that the historical change could not be measured; do not reconstruct an old workspace or block an otherwise reviewed fix solely to obtain that comparison.
A corrupt or mismatched snapshot must never be used as verified evidence, and a specifically requested exact historical comparison remains incomplete without it.
The auditor does not choose balance targets or patch source; a failed analyzer or unavailable comparison alone does not block a documented fix.

If immutable probability snapshots are committed as durable before-source evidence, preserve the copied bytes through narrowly scoped Git attributes and any clean filters.
When attributes change after staging, plain `git add` may reuse cached normalization; force path-specific `git add --renormalize` under byte-preserving attributes and filters, or explicitly promote a blob using `git hash-object -w --no-filters` and a path-specific index update.
Verify that the raw committed blob's SHA-256 matches the recorded copied-byte hash, reading it without text decoding, newline conversion, or checkout filters.
If a saved comparison file differs from its recorded source bytes or hash, preserve the original and do not rely on that comparison until the mismatch is corrected and the hashes are checked again.

Active small patches do not include:

- creating or expanding a whole mechanic
- adding a full event chain
- replacing a focus route family
- designing a new formable suite
- inventing an unplanned or shared scripted GUI system; implementing the accepted bounded UI introduced by a named event belongs to `chaosx_event_ui_worker`
- creating a new country package from scratch
- changing broad balance philosophy
- rewriting large localisation sets for tone only
- changing asset source rules
- claiming final completion of the parent feature

When a patch-capable subagent sees a broad design gap, it writes a plan handoff and stops. The main agent decides whether to implement it.

## Plan and spec paths

Full accepted event specs belong under:

```text
docs/specs/<event_id>_<event_slug>_specs/
```

Subagent plans, expansion addenda, audit follow-up notes, blocked reports, implementation handoffs, and patch handoffs belong under:

```text
docs/plans/<event_id>_<event_slug>_plans/
```

The plans folder is the working area. The specs folder holds source design whose acceptance basis must be recorded. A spec location, date, status label, or old handoff does not prove approval. Cite the explicit user decision or parent acceptance within the user-authorized scope, and keep unsupported or conflicting claims unresolved. Current implementation proves what exists, not what was accepted. The main agent should fold accepted design into the relevant spec or record it as `accepted and queued` with its acceptance basis and reason.

Do not create new planning folder names such as `docs/planning/` unless the user explicitly asks.

## Mandatory handoff after any patch

Every subagent that edits files must return one current handoff containing the complete applicable findings below.
Deliver those findings once: when a durable report is requested or useful, verify that the saved report is readable and return its path with a concise inline summary; otherwise return the complete findings inline.
If file delivery is unavailable, use complete inline delivery instead of repeatedly trying to produce the same report.
Update an existing current report rather than creating repeated status reports.
If the event id and slug are known, place a requested durable handoff under:

```text
docs/plans/<event_id>_<event_slug>_plans/subagent_handoffs/
```

The handoff should include:

- files changed
- exact gameplay surface changed
- changed ids, keys, tags, helper names, or state groups
- before and after behavior
- why the change is safe and bounded
- meaningful validation run, limited to task-specific checks that affect confidence
- skipped meaningful validation and why
- remaining issues or design gaps
- any follow-up the parent must implement

Do not fill handoffs with passing boilerplate checks that only restate AGENTS.md rules. Basic syntax hygiene can be done internally unless it found a problem or materially changed the patch.

If a patch touches localisation, list the keys changed. If it touches decisions or focuses, list affected ids. If it touches scripted helpers, list helper names and call sites. If it touches country setup, list tags and state ids or state groups.

### MCP evidence in handoffs

For a handoff involving supported MCP surfaces, include the relevant source revision, scenario, coverage, and useful results. Apply AGENTS.md retry limits; unavailable verification is not missing implementation.
Read the complete requirements in [MCP evidence in handoffs](../../../docs/systems/hoi4_agent_tools_mcp_integration.md#mcp-evidence-in-handoffs) before this work.

## Specialist routing

### System skill routing

The `chaos-redux-*` system skills (`chaos-redux-equipment`, `-technology-doctrines`, `-ai-strategies`, `-diplomacy-war`, `-units-divisions`, `-characters-leaders`, `-map-states`, `-ideas-modifiers`) combine engine guidance written from the installed documentation and vanilla files with the repository's own files, shared systems, and registrations. A subagent cannot load a skill the parent does not name, so the parent prompt lists the matching skill files by path (`.claude/skills/<name>/SKILL.md`) alongside the Chaos Redux surface skill:

- `chaos-redux-ai-strategies` for `chaosx_ai_probability_auditor` and for any auditor or architect that reviews `ai_strategy`, `ai_will_do`, `ai_chance`, AI templates, or AI equipment behaviour.
- `chaos-redux-equipment` for `chaosx_equipment_units_worker`, and for `chaosx_country_package_auditor`, `chaosx_scripted_system_architect`, and `chaosx_3d_model_pipeline` when the work touches equipment archetypes, variants, modules, stockpiles, or payload lots.
- `chaos-redux-technology-doctrines` for `chaosx_technology_tree_worker`, and for `chaosx_country_package_auditor` and `chaosx_scripted_system_architect` when the work touches technologies, doctrines, or their unlocks.
- `chaos-redux-units-divisions` for `chaosx_equipment_units_worker`, `chaosx_country_package_auditor`, and `chaosx_3d_model_pipeline` when the work touches sub-units, division templates, orders of battle, counters, or unit entities.
- `chaos-redux-characters-leaders` for `chaosx_country_package_auditor` and `chaosx_portrait_creator` when portraits are wired to characters, leaders, advisors, or unit leaders.
- `chaos-redux-map-states` (including its `references/state-ledgers.md`) for `chaosx_map_states_worker`, and for `chaosx_country_package_auditor`, `chaosx_scripted_system_architect`, and `chaosx_repo_explorer` when the work touches state history, startup grants, map files, victory points, supply, railways, state iteration, or civilian transfers and ledgers.
- `chaos-redux-ideas-modifiers` for `chaosx_focus_tree_auditor`, `chaosx_decision_mission_auditor`, and `chaosx_scripted_system_architect` when ideas, national spirits, dynamic modifiers, or modifier names are involved.
- `chaos-redux-diplomacy-war` for `chaosx_focus_tree_auditor`, `chaosx_decision_mission_auditor`, and `chaosx_country_package_auditor` when focuses, decisions, or events change diplomacy, factions, subjects, wargoals, peace, or condemnation.

Where a system skill and `CLAUDE.md` differ, `CLAUDE.md` wins.

### Asset routing

Do not use one broad asset worker for mixed visual packages.

Use:

- `chaosx_asset_source_researcher` for real, archival, historical, documentary, or public-source images when the asset must show real historical material
- `chaosx_portrait_creator` for complete grounded and fictional character portrait production; it never operates RunPod
- `chaosx_generated_event_art` for generated non-icon fictional, alternate-history, symbolic, high-chaos, or unique event art
- `chaosx_icon_artist` for generated gameplay icons, formable seals, decision category icons, and small animated icon or button sprites
- `chaosx_event_ui_worker` for the bounded layout and MCP visual pass of a dedicated UI introduced by one named event; never for the shared event log, event details, settings, or another existing framework UI

The parent agent must give each asset subagent a bounded prompt with exact asset names, target sizes, source mode, final folders, sprite names when already registered, reference folders, and constraints.

For every generated asset whose inspected consumer uses transparent unused canvas, the parent prompt must set generated-image transparency as the default and require alpha preservation through processing and DDS conversion. This includes icons, counters, emblems, overlays, decorative UI pieces, and transparent animation frames. Request an opaque or painted background only when the exact asset family requires it. Background removal is fallback-only after native transparency fails or when an inherited, sourced, or user-provided image has an unwanted opaque backdrop; require the untouched source, fallback method, edge validation, and manifest note.

Country-identity asset work must not start until the parent has audited the candidate tag against vanilla, Chaos Redux, every installed Workshop mod, and other local mods, and has checked whether the national identity already exists in vanilla. A conflicting new tag must be remapped; a vanilla country identity must reuse the vanilla tag and preserve its meaningful content. Pass the locked tag and audit evidence into the context-free subagent prompt.

Portrait prompts must inspect the canonical portrait references and route the complete package to `chaosx_portrait_creator`. Real people require portrait-worker-owned source research, an attributed source, explicit crop, durable storage under `docs/assets/portraits/`, and a wired source placeholder; the user supplies the HOI4-style final for validation and installation. Grounded identities must use sourced real people or authentic institutional material. The portrait worker invokes the image-generation route for fictional or impossible portraits and completes their processing and wiring.

For `chaosx_icon_artist`, the parent prompt must require image-generation source atlas or source PNG evidence, prompt and source-mode notes, native transparent-background generation for alpha-backed families, alpha preservation, contact sheets, dimension and alignment QA, no white matte or opaque square backgrounds, and confirmation that final generated icons are not primitive local drawings or resized unrelated icons. Background removal must be recorded only as a fallback after native transparency fails or for an inherited opaque source.

For `chaosx_generated_event_art`, distinguish alpha-backed emblems, seals, overlays, and decorative UI pieces from full-canvas report/news/super-event scenes, flags, and painted panels. Alpha-backed outputs request native transparency in the initial image-generation call; full-canvas outputs keep the background treatment required by their consumer. Do not flatten native alpha or make background removal a routine generation step.

For flags, the parent prompt must state whether each flag is a base flag, ideology variant, route variant, cosmetic-tag flag, historical flag, or fictional flag. Every final flag requires image-generation source evidence. Historical flags and attested symbols begin with `chaosx_asset_source_researcher`, then use the cited design as a strict image-generation input; fictional or alternate-history variants belong with `chaosx_generated_event_art`. Require clean flat flag designs, exact historical geometry and symbols when attested, and reject waving fabric, folds, flagpoles, scenery, painterly artwork, perspective, lighting, gradients, fake text, or invented heraldry. Flags are deliberate full-canvas opaque designs, not transparent cutouts. Base flags for existing countries must be preserved unless explicitly in scope. Ideology variants must be distinct designs, not recolors or copied emblems.

Asset subagents may create source files, PNG previews, DDS files, contact sheets, manifests, and `gfx_handoff.md`. They must not edit `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files unless the parent explicitly expands scope. The portrait worker has a standing narrow exception for portrait-specific `.gfx` entries and existing character portrait references.

### Super-event routing

Use separate research agents when the super-event package has enough work to justify it.

Use `chaosx_super_event_text_researcher` for quotes, exact wording, attribution confidence, button text, cultural remarks, slogans, allusions, and short references.

Use `chaosx_super_event_audio_researcher` for audio research, license verification, download, final `.ogg` preparation with original recordings preserved, and audio handoff notes.

Use `chaosx_portrait_creator` for every character portrait. Use `chaosx_asset_source_researcher` or `chaosx_generated_event_art` only for non-portrait image work according to the source mode required by `chaos-redux-event-assets`.

The main agent owns final non-portrait wiring, localisation, settings-aware playback, docs, and spreadsheet alignment. The portrait worker owns portrait-specific `.gfx` and existing character portrait references.

### Improvement routing

Use `chaosx_improvement_loop_planner` when an event or event-adjacent mechanic needs new design material, not just an audit finding.

The planner should read `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and relevant system skills. It should inspect actual implementation, specs, plans, docs, localisation, and asset notes when available. It should then write concrete design material that expands the event through playable mechanics, historical or regional connections, AI behavior, and visual needs. It should not patch gameplay files.

The main agent should deploy the planner often enough to keep major events from becoming shallow after new mechanics are added, but not so often that plans pile up; the same-event redeployment limit under [Plan-only agents](#plan-only-agents) applies.

Audit subagents may include compact improvement handoffs inside their reports. If a gap requires a new route family, new GUI system, new formable suite, new country package, or new event chain, they should recommend a plan-mode pass rather than trying to patch it.

### Spreadsheet catalog routing

`chaosx_spreadsheet_doc_worker` is a context-light spreadsheet worker, not a general documentation agent.

Use it when the only required output is an update to:

```text
docs/spreadsheets/chaos_redux_events_catalog.xlsx
```

The workbook is the only editable catalog source. The three catalog CSVs are export-only snapshots generated from the workbook's `Events`, `Clusters`, and `Scenarios` sheets. After the worker saves the workbook, it must run:

```text
python .tools/export_event_catalog_csv.py
```

The worker must never edit the CSVs directly or treat a stale CSV as the source of truth. If the exporter fails, report the failure and leave the workbook as the only attempted edit until the exporter can be rerun.

The parent prompt should provide event ids, row targets, source localisation keys, or the exact fields to update when possible.

The worker should read only:

- the parent prompt
- the `chaos-redux-xlsx` skill
- `docs/spreadsheets/README.md` for the catalog authority and schema contract
- the event catalog workbook
- the localisation or scripted localisation needed to mirror player-facing event log, event detail, evolution detail, or cluster wording
- named source files explicitly provided by the parent

It should not read HOI4 wiki pages, vanilla documentation, vanilla files, broad implementation guides, or unrelated repo systems. It should not edit docs, specs, plans, manifests, gameplay files, localisation files, assets, GFX, GUI, events, focuses, decisions, ideas, history, scripted effects, scripted triggers, or other spreadsheets unless the parent explicitly expands scope.

The worker must preserve workbook structure, formatting, formulas, filters, and validation unless the parent explicitly asks for structural changes.

## Parent review

The parent agent must review every subagent output before relying on it.

Before final completion, the parent should check:

- subagent changes are inside approved scope
- patch handoffs identify changed files and ids
- plan and documentation handoffs use the AGENTS.md dispositions with acceptance basis, implementation evidence, reasons, replacement paths, or exact blockers as applicable
- explicit user decisions, accepted design, implementation evidence, and proposals remain distinguishable
- assets are wired or reported as pending
- temporary event asset workspaces are retained for active or blocked work and deleted only after durable evidence and runtime wiring have been reconciled
- advisor candidates have separate manifest-linked native-plus-`4x` visual approval from a reviewer who is not the producer; automated validation alone is not approval
- validation reflects the final repo state
- docs, specs, plans, and spreadsheet surfaces agree

A subagent patch can reduce workload. It never owns the final completion claim.
