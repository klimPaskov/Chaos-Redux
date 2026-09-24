---
name: chaos-redux-subagents
description: Use when coordinating Chaos Redux project custom subagents (Codex TOML definitions or the generated Qoder, Cursor, opencode, and Claude Code definitions, plus DSH runtime-composed roles), routing bounded work, or defining parent/subagent ownership boundaries.
---

# Chaos Redux Subagents

Use this skill when a Chaos Redux task should be split across project custom subagents.

The parent agent remains responsible for final integration, final review, required source and MCP validation, and completion claims. The user performs live-game validation. Subagents can inspect, patch, create assets, write addenda, or produce reports. The parent must review their outputs, wire final cross-surface behavior, and carry blockers into the final report.

Do not use subagents to hide uncertainty or pass off responsibility. A subagent handoff is evidence for the parent, not a replacement for parent review.

## Fork context rule

All project custom subagents must be spawned with a fully explicit, self-contained prompt and no inherited parent-thread context. With the current Codex `collaboration.spawn_agent` tool, set `fork_turns="none"`. In the Qoder, Cursor, opencode, Claude Code, and DSH runtimes subagents are isolated by design, and the parent prompt must still carry every needed input. Cursor loads generated `.cursor/agents/*.md` files as native project subagents, and Claude Code loads generated `.claude/agents/*.md` files as project subagents. Spawn them by hyphen-case name through `/name`, the Task tool, or the `Agent` tool. DSH composes each named role at runtime, so read the canonical identifier below as the role to instantiate. Do not substitute Cursor's built-in `explore`, `shell`, or `browser` agents, or Claude Code's built-in `Explore`, `Plan`, or `general-purpose` agents, for a named Chaos Redux specialist.

Do not spawn any project subagent with inherited parent-thread context. The parent prompt must include every path, user correction, task constraint, scope boundary, previous handoff status, accepted plan, queued plan, and design rule the subagent needs.

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

Identifiers below are the canonical snake_case Codex names. The Qoder, Cursor, opencode, and Claude Code runtimes use the generated hyphen-case equivalents (for example `chaosx_repo_explorer` becomes `chaosx-repo-explorer`). Qoder mappings are written by `python .tools/sync/sync_qoder_agents.py` to the generated `.qoder/agents/README.md`. Cursor mappings are written by `python .tools/sync/sync_cursor_agents.py` to the generated `.cursor/agent-map.md`. opencode mappings are written by `python .tools/sync/sync_opencode_agents.py` to the generated `.opencode/agent-map.md`. Claude Code mappings are written by `python .tools/sync/sync_claude_agents.py` to the generated `.claude/agent-map.md`, and that same command mirrors each repo skill into `.claude/skills/` because Claude Code cannot be pointed at `.agents/skills/` directly. Every generated map file appears only after its command runs, and the generated runtime directories are gitignored, so a reader in a clean checkout has this section as the canonical mapping. Cursor agent files must stay Task-tool compatible, and Claude Code agent files must stay `Agent`-tool compatible: one Markdown file per agent in the runtime's `agents/` folder, YAML frontmatter, then the prompt body, with no non-agent Markdown in that folder.

DSH composes subagents at runtime through its delegation tool and loads no agent definition files, so there is no DSH agent map and no DSH generator. DSH also does not read `.codex/agents/*.toml`, so a named role does not arrive with the model its TOML names. Treat the canonical snake_case identifiers below as the named roles a DSH parent instantiates by writing the role boundaries into a fully explicit, self-contained delegation prompt.

Every DSH child runs on `deepseek-official/deepseek-flash` and nothing else, so specify no model. Naming `provider` and `model` together is allowed only as that pair; naming one alone is rejected, and effort may be named alone because the configured default already fixes the route. If a task looks like it needs a stronger model, split it into narrower bounded subagents instead. `subagent_fork` cannot select a child model, so use the ordinary delegation tool when the route matters. Model selection is sampled when a session is composed, so a session without those fields predates the opt-in rather than being misconfigured. DSH layout, skill roots, model selection, and MCP registration are documented in `docs/runtimes.md`.

Use `chaosx_repo_explorer` only for read-only repo exploration when touched-file mapping, pattern search, vanilla reference mapping, missing-file recovery, dependency mapping, or edit-order planning is actually unclear. It is not a default preflight agent.

Use `chaosx_improvement_loop_planner` for event improvement loop planning, detailed expansion specs, historical and regional research notes, and implementation-ready improvement handoffs. This replaces the old mechanic-expander role. It writes plans and addenda. It does not patch gameplay files.

Use `chaosx_asset_source_researcher` for non-portrait real or archival image sourcing, historical flags, historical symbols, user-provided source photos, source-image processing, and report, news, or super-event images that must depict real historical material.

Use `chaosx_portrait_creator` for every character portrait. It researches and archives grounded sources, creates crops and placeholders, invokes native ImageGen for fictional or impossible subjects, processes PNG/DDS outputs, installs portrait-specific wiring, and writes manifests and handoffs. It validates user-supplied grounded finals and never operates RunPod.

Use `chaosx_generated_event_art` for generated non-icon art, including fictional or alternate-history report images, news images, super-event images, fictional flags, faction emblems, UI panels, dossier art, progression-state base art, and animated non-icon presentation pieces. It does not own final character portraits.

Use `chaosx_icon_artist` for focus icons, idea icons, national spirit icons, officer corps icons, decision icons, decision category icons, achievement icons, tech icons, formable seals, scripted GUI icons, and small animated icon or button sprites.

Use `chaosx_3d_model_pipeline` for bounded Meshy 7 custom HOI4 3D model work covering geometry, provider candidates, Blender processing, model textures, rigs, skeletal actions, Internet-sourced unit-audio research, bespoke vanilla-green custom-unit counter requirements and handoffs, `.mesh`/`.anim` export, QA evidence, and runtime handoffs.

Use `chaosx_super_event_text_researcher` for super-event main quotes, exact wording checks, attribution confidence, source comparison, button text, cultural remarks, slogans, allusions, and short references.

Use `chaosx_super_event_audio_researcher` for licensed or public domain audio research, source verification, download, final `.wav` preparation, and audio handoff notes.

Use `chaosx_focus_tree_auditor` for focus tree audits and active small patches covering branch depth, route coverage, icons, localisation, rewards, prerequisites, mutual exclusions, AI, focus-formable links, and simplification.

Use `chaosx_decision_mission_auditor` for decision and mission audits and active small patches covering category lifecycle, objective quality, costs, tooltips, scripted GUI decision hooks, AI behavior, cleanup, balance, and exploit risk.

Use `chaosx_event_ui_worker` to create or improve the dedicated scripted GUI window that one named Chaos Redux event or event-owned mechanic specifically adds. It uses the mandatory HOI4 MCP GUI inspect, render, and post-change comparison workflow with direct reviewed edits or optional `gui_rewrite`, treats the production render as the one-to-one in-game visual view, and fixes every defect visible there under the full reference-image, native-layout, and visual-review contract from `chaos-redux-scripted-gui`. It must never audit the shared event log, event-details framework, settings UI, super-event framework, shared registries, or unrelated existing interfaces.

Use `chaosx_country_package_auditor` for country package audits and active small patches covering tags, custom-tag history, generated startup scientists, existing-country startup grants, states, leaders, portraits, flags, parties, focus loading, ideas, advisors, units, technologies, claims, cores, localisation, AI, formables, and playable setup.

Use `chaosx_localisation_auditor` for localisation and scripted localisation audits and active small patches covering missing keys, duplicate keys, encoding, tooltip quality, broken dynamic text, namespace consistency, dynamic cost text, and cross-surface text mismatch.

Use `chaosx_scripted_system_architect` for reusable scripted system design and active narrow implementation covering scripted effects, scripted triggers, script constants, event targets, meta effects, variables, tuning values, formable helpers, scripted GUI button helpers, and dynamic helper logic.

Use `chaosx_documentation_curator` for documentation cleanup and consistency during long implementation. It reconciles specs, plans, docs, handoffs, manifests, prompts, reports, and README files, writes source-of-truth maps and resume packets, marks superseded docs, records plan dispositions, and flags contradictions. It patches documentation surfaces only and does not edit gameplay files, localisation, assets, or spreadsheets.

Use `chaosx_event_completion_auditor` for read-only spec-versus-implementation audits covering events, mechanics, assets, docs, super-events, focus trees, decisions, validation, and accepted plan addenda.

Use `chaosx_ai_probability_auditor` for read-only audits of AI weights, MTTH, event `ai_chance`, random lists, focus and research selection, decision and mission scores, AI strategy factors, and declared custom weighted pools. It must use the HOI4 MCP probability workflow and return scenario-specific evidence; do not treat a focus, decision, country, or completion audit as a substitute for this specialized pass.

Use `chaosx_spreadsheet_doc_worker` only for the event catalog workbook at `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. It uses the xlsx/spreadsheet skill, keeps the workbook player-facing, and matches event log, event detail, evolution detail, and cluster detail fields to the in-game wording.

Use `chaosx_skill_maintainer` for skill creation, skill cleanup, routing updates, and multi-skill consistency work when a task reveals a reusable workflow, repeated mistake, repo-specific convention, validation pattern, asset or prompt pattern, or implementation rule that belongs in a repo skill. The role is runtime-neutral: it owns the skill files themselves, so it behaves the same in every runtime and is spawned by the same canonical snake_case identifier that the Qoder, Cursor, opencode, and Claude Code runtimes map to their hyphen-case equivalents.

Do not route new work to `chaosx_mechanic_expander`. Its role is merged into `chaosx_improvement_loop_planner` and the `chaos-redux-improvement-loop` skill.

## Routing gates

### Event UI worker gate

Spawn `chaosx_event_ui_worker` with a fully explicit, self-contained prompt (Codex `collaboration.spawn_agent`: `fork_turns="none"`) only when the accepted event spec or implementation explicitly introduces a dedicated scripted GUI or mechanic window. The parent prompt must provide the event id and slug, exact GUI identifiers and owning files, entry point, accepted layout brief and acceptance basis, reference-image paths or a bounded reference-production assignment, image-to-native mapping, intended states and resolutions, linked decisions and scripted-GUI identifiers, approved asset handoffs, allowed files, and handoff path.

The worker is patch-capable for the accepted event-owned `.gui`, presentation-only `common/scripted_guis` wiring, event-owned `.gfx`, and event-owned GUI localisation. It owns layout implementation, hierarchy, spacing, alignment, background coverage, state presentation, click-region accuracy, and MCP before-and-after evidence. The parent and decision worker retain event outcomes, costs, AI, balance, reusable logic, and final integration. The parent reviews required MCP evidence and the user performs live-game validation.

Do not route a GUI merely because an event appears in or opens it. The shared event log, event-details framework, settings UI, super-event framework, shared registries, utility/debug windows, and unrelated existing UIs remain out of scope. The prompt must identify the exact source or accepted specification proving event ownership.

Apply `chaos-redux-scripted-gui` for reference creation before implementation, justified native adaptations, the complete visual checklist, and exact discovered MCP schemas. Record user direction or parent acceptance within the authorized scope; document existence alone is not approval. Shared interfaces remain parent-owned even when this skill is used.

Mandatory evidence includes `hoi4.gui_inspect`, pre-change `hoi4.gui_render` full-window and relevant cropped, annotated, state, resolution, hierarchy, click-region, and comparison views, then post-change inspect/render comparison over matching explicit scenarios, source identities, states, resolutions, and UI scales. There is no separately exposed GUI comparison tool; preserve baseline artifacts and use the render route's supported `comparisonScenario` only for its documented scenario comparison. The production renders are the one-to-one in-game visual review surface, so visible alignment, spacing, clipping, overflow, background, asset, text, state, and click-region defects block completion and may not be excused as renderer differences. Missing required inspect/render evidence blocks visual completion; source-only review is not equivalent. `gui_rewrite` is optional, and its automatic post-write/index validation or transaction success is not a completion gate; direct application of an authorized reviewed edit follows `chaos-redux-scripted-gui`.

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

### Plan-only agents

`chaosx_improvement_loop_planner` writes event expansion specs, improvement addenda, deep research notes, historical connection notes, and implementation handoffs. It does not edit gameplay, localisation, GUI, scripted effects, focus trees, decisions, assets, spreadsheets, or country files.

When an event mechanic needs more depth, new branches, new countries, a new formable suite, a new scripted GUI system, deeper regional logic, historical anchors, or a larger route redesign, the planner writes a plan under `docs/plans/<event_id>_<event_slug>_plans/`. The main agent decides what to implement.

The parent should use this planner after a meaningful implementation tranche, not after every small patch. Do not spawn it again for the same event until its previous addendum has been implemented, folded into specs, queued with a reason, or rejected with a reason.

### Documentation curation agents

`chaosx_documentation_curator` is patch-capable for documentation surfaces only. It may update Markdown specs, docs, plans, handoffs, manifests, prompt files, README files, route coverage tables, source-of-truth ledgers, resume packets, and documentation indexes inside the current task scope.

Use it after long implementation tranches, after several subagent handoffs, before a major resume, or whenever docs may be stale, contradictory, duplicated, or too numerous. It should distinguish explicit user decisions, accepted design with its acceptance basis, current implementation evidence, and proposals. Apply the AGENTS.md Specs and Plans dispositions: `unresolved`, `accepted and queued` with acceptance basis and reason, `implemented` with evidence and validation limits, `promoted into an accepted spec` with acceptance basis and destination, `rejected` with recorded reason, `superseded` with a named replacement, or `blocked` with the exact limitation.

It must not edit gameplay files, localisation, scripted localisation, GUI, GFX, events, focuses, decisions, ideas, scripted effects, scripted triggers, on_actions, country setup, history, AI files, assets, audio, binary files, or the event catalog workbook. It does not replace `chaosx_event_completion_auditor`, `chaosx_localisation_auditor`, `chaosx_spreadsheet_doc_worker`, or `chaosx_repo_explorer`.

### Skill maintenance agents

`chaosx_skill_maintainer` is patch-capable for repo skills and skill assets and for the routing references that point at them.

It creates a skill under `.agents/skills/<skill-name>/SKILL.md` when the workflow is reusable and not already covered, updates an existing skill when the workflow belongs there, audits skills for overlap, unclear instructions, stale paths, event-specific leakage, and missing reusable guidance, and keeps several skills consistent when one routing rule or convention spans them. It updates skill-local reference material and the routing references that name skills, including the canonical subagent entries in this skill and the runtime agent or skill registrations that mirror them. Its edits stay reusable and non-event-specific, and each skill stays focused on one reusable workflow.

It must not edit gameplay files, localisation, events, focuses, decisions, ideas, scripted effects, scripted triggers, on_actions, country setup, history, AI files, GUI, GFX, assets, audio, binaries, spreadsheets, or docs and specs outside an explicitly granted documentation scope, and it must not hand-edit another runtime's generated agent or skill definition files.

### Asset-production agents

Asset subagents create source files, processed previews, final DDS outputs, contact sheets, manifests, and asset handoffs. During active work, event-scoped evidence belongs under the temporary `docs/assets/<event_id>_<event_slug>/` workspace. They do not wire gameplay, localisation, GFX, GUI, events, focuses, decisions, or spreadsheets unless the parent gives a narrow exception.

The parent owns temporary-workspace cleanup. Keep the event-scoped `docs/assets/` workspace while the event is active, blocked, awaiting review, or undergoing acceptance scenarios. Before declaring the event goal fully complete, promote durable provenance, licensing, attribution, coverage, review, and sprite-handoff facts into permanent event or plan documentation, verify that no runtime reference points into `docs/assets/`, then delete the complete event-scoped workspace. An absent workspace is expected for a fully complete event. Never delete a skill-local reference library or an unrelated event workspace.

### 3D model routing

Route `chaosx_3d_model_pipeline` only with a context-complete prompt (Codex `collaboration.spawn_agent`: `fork_turns="none"`) containing the exact deterministic job root, reference-image path or approved asset brief, output folders, handoff path, asset profile, named vanilla references, scale relationship, required action roles, custom-unit sound roles, Internet source and licensing requirements, custom-unit counter consumers/tokens, exact installed-vanilla counter definition and DDS paths, matching skill-local counter family, `chaosx_icon_artist` handoff path, baseline planned paid operations, one-attempt Meshy rig/action limits, item-free body plus separately generated equipped-item route, live Blender authoring for every item and for every anatomy the provider route does not cover, and geometry-recovery credit limits, dependency lock, and forbidden simplifications. The parent must pass the owner/asset identifiers explicitly. The subagent must not infer them from inherited conversation state.

For provider-dependent work, the parent prompt must require the MESHY_API_KEY gate, Meshy 7 geometry, and exactly one approved sourced Meshy input image, no multi-view provider board, immediate provider download and checksum, protected provider source, topology repair, PDX packed-material validation, hash-aware runtime synchronization, and `.mesh`/`.anim` reimport evidence. Blender-only non-firearm existing-model repairs require verified Blender routes and dependencies without a Meshy key or fresh provider attempt. Normal generation, planned remesh/retexture/conversion, the Meshy rig task, the Meshy animation tasks, and authorized geometry recovery remain preauthorized while live balance and provider capability permit them. The Meshy provider route is the preferred route for rigging and animating provider-eligible bipedal models, which do not have to be human: the worker generates the body, drives the Meshy rig task and the Meshy animation tasks, and ingests the provider results into the job through `import_animation_action`, `import_bvh_animation_action`, and `retime_animation_action`. Live Blender authoring covers non-bipedal and non-humanoid anatomy, creature rigs, mechanical and articulated assemblies, firearm-specific rig and attachment work, measured creature rigs, component and prop modeling, and every missing or faulty provider result. No repository Python script and no adapter operation may generate bones, skin weights, or keyframes from a declarative spec, a template, or a formula, and provider results are ingested as authored assets rather than synthesized by repository code. For custom units, require Internet sound-source research, original download preservation, licensing evidence, animation synchronization points, and a blocked state when no defensible sourced file exists; manual, generated, synthesized, recorded, placeholder, and unlicensed audio are forbidden. Also require bespoke counters for every used counter surface, exact installed-vanilla definition/DDS inspection, matching reference-family inspection, and sampled vanilla green evidence; reused counters, arbitrary green, and unreferenced imitations are forbidden. For humanoids, name the installed vanilla source mesh and entity and pass the source-height/entity-scale/effective-runtime crosswalk; for buildings, pass the valid state/province pair and entity visibility test.

Its allowed scope includes preserved sources, Meshy body candidates, the Meshy rig task and the Meshy animation tasks for a provider-eligible bipedal body, provider action ingestion, Blender component modeling/restoration, materials, rigs, weights, held props, attachments, and real skeletal actions authored live in Blender through the MCP bridge for every asset the provider route does not cover. Firearm-bearing units, including current firearm models, must receive a fresh Meshy 7 weapon-free body from exactly one weapon-free input, then the Meshy rig and its receipt-verified provider actions for that body, and live Blender firearm fitting, attachment, and prop work. Preserve source weapon identity as reconstruction evidence and validate final grip/stock/muzzle/recoil and firing-state effect/sound synchronization. Held items are never generated inside the body: the body input carries empty neutral hands, each item gets its own provider geometry task from its own single image, and the assembled whole — body plus attached item — is what gets animated and validated in Blender. Always create or restore missing required elements without renewed approval; preserve intended identity and record complete component coverage. A provider-eligible bipedal skeleton, its skin weights, and the provider actions ingested onto it arrive as authored provider results, and every other new rig, weight set, and action is authored live in Blender; no repository Python script may generate bones, skin weights, or keyframes from a declarative spec, a template, or a formula. All routes require actual modeling/authoring capability, deformation/contact and semantic-motion review, and export/reimport proof; whole-rig/static substitutes and semantic aliases remain forbidden. No shortcut may stand in for real rigging, skinning, or animation work: an incomplete or anatomy-mismatched skeleton, unreviewed bulk weights, a static or transform-only stand-in, one role's action reused for another, an omitted component, or evidence reused from another model all fail acceptance. Other provider/source substitutions need separate approval. The worker must not create audio from scratch or edit gameplay, GFX, `.gfx`, `.gui`, `.asset`, entity, sound definitions, localisation, events, focuses, decisions, country/history/AI, on-actions, or spreadsheets.

The handoff must list files, provider task lineage and credits, verified dependency versions, Blender checkpoint stages, Meshy attempt ledger, fallback/repair basis, manual Blender authoring operations, retained valid outputs, geometry/material/rig/weight/action/export results, Internet audio source URLs, attribution, licenses, sound roles and animation synchronization points, custom-unit counter consumers/tokens, installed-vanilla counter paths, sampled green-palette evidence, counter-artist outputs, reimport or parser evidence (or an explicit missing-capability blocker), proposed runtime identifiers, statuses, skipped meaningful validation, and remaining risks. Use only actual provider or Blender tool names discovered and verified by the parent; missing integrations are `required installation/verification` or `blocked`, not invented capabilities. Any viewer or inspector is read-only.

The parent alone owns `.asset`/entity/GFX/runtime source wiring, final review, evidence reconciliation, and the overall completion claim. The user performs live-consumer and in-game validation. A successful provider task, `.blend`, preview, or export never authorizes the subagent to claim the feature is complete or to silently use a fallback.

### Active small-patch agents

These agents are patch-capable by default inside the current task scope:

- `chaosx_scripted_system_architect`
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

Any patch to an AI weight, probability-bearing modifier, MTTH-backed score, random-selection weight, strategy factor, or weighted target check requires an audit-patch-compare cycle. Run `chaosx_ai_probability_auditor` first to establish named baseline scenarios, let the owning patch-capable agent or parent apply the bounded change, then run the auditor again with `hoi4.probability_compare` against the same scenarios. The probability auditor remains read-only, does not choose the intended balance target, and does not patch source.

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

Every subagent that edits files must write a handoff back to the parent. If the event id and slug are known, place it under:

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

## MCP evidence in handoffs

When a routed task touches focus trees, event chains, technology or doctrine trees, weighted logic, scripted GUI, or maps, MCP use is mandatory as the shared evidence surface. Pass only the diagnostics, revision, scenario hash, comparison, or linked artifact URI the parent needs instead of copying a complete graph or matrix into the prompt. Tool exposure is separate from service health and standalone viewer availability. If the relevant MCP route is unavailable, mark the affected work blocked or unresolved and carry the exact limitation to the parent. Verify standalone Technology Tree Viewer availability separately from the exposed read-only `mcp__hoi4_agent_tools__hoi4_tech_inspect`, `mcp__hoi4_agent_tools__hoi4_tech_render`, and `mcp__hoi4_agent_tools__hoi4_tech_compare` routes. Record an absent viewer as a package gap without inventing capabilities.

Before using `mode = helper_expansion`, `hoi4.job_inspect`, `hoi4.job_cancel`, or native MCP tasks, verify the connected server's reported version and health, inspect the live tool schemas for those routes, and check client task negotiation. Source code or exposed tool metadata alone does not establish support in the connected process. Use only routes confirmed for the installed server and client; otherwise follow the available domain routes and record the missing capability precisely.

On a confirmed route, use `mode = helper_expansion` with `hoi4.event_inspect` or `hoi4.tech_inspect` for bounded helper pages, and use `hoi4.job_inspect` and `hoi4.job_cancel` for persistent jobs. Request native MCP tasks only when the client negotiates support. Keep opaque job IDs and helper continuation URIs intact. A completed job can still contain a tool-level error, and cancellation is a request whose final outcome must be inspected. For paged helper evidence, retain the source revision, selected roots, bounds, `finished`/`complete` status, and unresolved findings; resume only with the returned continuation under the same revision and authorized principal. Jobs and helper pages are delivery and coverage tools; they do not replace the owning event, technology, focus, probability, GUI, or map workflow's inspect, render, compare, and scenario evidence. Keep task-specific mechanics and fixtures in their profiles and handoffs, not this routing skill.

For large binary resources returned by `read_mcp_resource`, treat the result as an untrusted transport envelope: inspect whether it is stringified JSON and record the declared encoding and type before using the payload. Do not trust compacted previews, literal truncation markers, or metadata claiming completion, and never print base64 data.

Use the artifact template's `?offset=<bytes>&length=<bytes>` reads with small ranges; when the payload is base64, prefer decoded-byte lengths divisible by 3 so each non-tail chunk can be independently decoded, then follow `continuationURI` through the final tail. Preserve the metadata and exact offset/length for every range, reject invalid characters or embedded truncation text, independently decode and validate chunks, concatenate in offset order, and validate the reconstructed bytes against the declared type before display or downstream processing. Treat a failed display after a one-shot read as an artifact-retrieval blocker; recover with bounded chunk reads or report unresolved rather than regenerating the artifact.

For probability work, `chaosx_ai_probability_auditor` must start with `hoi4.probability_inspect`, name the analyzed surface and scenario ids, state whether the candidate pool and external factors were complete, and distinguish exact, bounded, sampled, score-only, and unresolved results. It must use `hoi4.probability_evaluate`, `hoi4.probability_sweep`, and `hoi4.probability_compare` according to the scenario, with `hoi4.probability_simulate`, `hoi4.probability_sequence`, and `hoi4.probability_render` only under their declared evidence conditions. For technology or doctrine work, list the affected technology, folder, unlock, grant, bonus, or asset ids and include the relevant `hoi4.tech_compare` result when source changed.

The current connected probability adapter accepts only `scenarioSet = { id, scenarios = [{ id, actor: string, state: flat primitive map, flags: string[], scopes: record of { id: string, state: primitive map } }] }`. Unknown `fixture` or variable-declaration records fail validation; scope references require `{ id }` objects, and `scopes` entries require `{ id, state }` objects. Flat primitive state may not bind Clausewitz numeric variables or compound triggers; primitive comparison-string probes can reduce simple comparator unresolved items but are not typed campaign fixtures. Record exact validation errors and artifact URIs, never invent fixture keys or add gameplay flags solely to satisfy the adapter, and never present partial score-only output as balance evidence.

## Specialist routing

### Asset routing

Do not use one broad asset worker for mixed visual packages.

Use:

- `chaosx_asset_source_researcher` for real, archival, historical, documentary, or public-source images when the asset must show real historical material
- `chaosx_portrait_creator` for complete grounded and fictional character portrait production; it never operates RunPod
- `chaosx_generated_event_art` for generated non-icon fictional, alternate-history, symbolic, high-chaos, or unique event art
- `chaosx_icon_artist` for generated gameplay icons, formable seals, decision category icons, and small animated icon or button sprites
- `chaosx_event_ui_worker` for the bounded layout and MCP visual pass of a dedicated UI introduced by one named event; never for the shared event log, event details, settings, or another existing framework UI

The parent agent must give each asset subagent a bounded prompt with exact asset names, target sizes, source mode, final folders, sprite names when already registered, reference folders, and constraints.

For every generated asset whose inspected consumer uses transparent unused canvas, the parent prompt must set native ImageGen transparency as the default and require alpha preservation through processing and DDS conversion. This includes icons, counters, emblems, overlays, decorative UI pieces, and transparent animation frames. Request an opaque or painted background only when the exact asset family requires it. Background removal is fallback-only after native transparency fails or when an inherited, sourced, or user-provided image has an unwanted opaque backdrop; require the untouched source, fallback method, edge validation, and manifest note.

Country-identity asset work must not start until the parent has audited the candidate tag against vanilla, Chaos Redux, every installed Workshop mod, and other local mods, and has checked whether the national identity already exists in vanilla. A conflicting new tag must be remapped; a vanilla country identity must reuse the vanilla tag and preserve its meaningful content. Pass the locked tag and audit evidence into the context-free subagent prompt.

Portrait prompts must inspect the canonical portrait references and route the complete package to `chaosx_portrait_creator`. Real people require portrait-worker-owned source research, an attributed source, explicit crop, durable storage under `docs/assets/portraits/`, and a wired source placeholder; the user supplies the HOI4-style final for validation and installation. Grounded identities must use sourced real people or authentic institutional material. The portrait worker invokes native ImageGen for fictional or impossible portraits and completes their processing and wiring.

For `chaosx_icon_artist`, the parent prompt must require `$imagegen` source atlas or source PNG evidence, prompt and source-mode notes, native transparent-background generation for alpha-backed families, alpha preservation, contact sheets, dimension and alignment QA, no white matte or opaque square backgrounds, and confirmation that final generated icons are not primitive local drawings or resized unrelated icons. Background removal must be recorded only as a fallback after native transparency fails or for an inherited opaque source.

For `chaosx_generated_event_art`, distinguish alpha-backed emblems, seals, overlays, and decorative UI pieces from full-canvas report/news/super-event scenes, flags, and painted panels. Alpha-backed outputs request native transparency in the initial ImageGen call; full-canvas outputs keep the background treatment required by their consumer. Do not flatten native alpha or make background removal a routine generation step.

For flags, the parent prompt must state whether each flag is a base flag, ideology variant, route variant, cosmetic-tag flag, historical flag, or fictional flag. Every final flag requires imagegen source evidence. Historical flags and attested symbols begin with `chaosx_asset_source_researcher`, then use the cited design as a strict imagegen input; fictional or alternate-history variants belong with `chaosx_generated_event_art`. Require clean flat flag designs, exact historical geometry and symbols when attested, and reject waving fabric, folds, flagpoles, scenery, painterly artwork, perspective, lighting, gradients, fake text, or invented heraldry. Flags are deliberate full-canvas opaque designs, not transparent cutouts. Base flags for existing countries must be preserved unless explicitly in scope. Ideology variants must be distinct designs, not recolors or copied emblems.

Asset subagents may create source files, PNG previews, DDS files, contact sheets, manifests, and `gfx_handoff.md`. They must not edit `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files unless the parent explicitly expands scope. The portrait worker has a standing narrow exception for portrait-specific `.gfx` entries and existing character portrait references.

### Super-event routing

Use separate research agents when the super-event package has enough work to justify it.

Use `chaosx_super_event_text_researcher` for quotes, exact wording, attribution confidence, button text, cultural remarks, slogans, allusions, and short references.

Use `chaosx_super_event_audio_researcher` for audio research, license verification, download, final `.wav` preparation, and audio handoff notes.

Use `chaosx_portrait_creator` for every character portrait. Use `chaosx_asset_source_researcher` or `chaosx_generated_event_art` only for non-portrait image work according to the source mode required by `chaos-redux-event-assets`.

The main agent owns final non-portrait wiring, localisation, settings-aware playback, docs, and spreadsheet alignment. The portrait worker owns portrait-specific `.gfx` and existing character portrait references.

### Improvement routing

Use `chaosx_improvement_loop_planner` when an event or event-adjacent mechanic needs new design material, not just an audit finding.

The planner should read `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and relevant system skills. It should inspect actual implementation, specs, plans, docs, localisation, and asset notes when available. It should then write concrete design material that expands the event through playable mechanics, historical or regional connections, AI behavior, and visual needs. It should not patch gameplay files.

The main agent should deploy the planner often enough to keep major events from becoming shallow after new mechanics are added, but not so often that plans pile up. For the same event, do not deploy another planner pass until the previous addendum is implemented, promoted to specs, queued with a reason, or rejected.

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
- the xlsx/spreadsheet skill
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
