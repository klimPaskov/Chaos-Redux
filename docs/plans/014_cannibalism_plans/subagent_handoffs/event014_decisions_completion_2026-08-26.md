# Event 014 decision and mission completion handoff

Date: 2026-08-26.

Owner: Event 014 decision and mission surfaces.

Status: bounded source patch and audit complete; parent review is still required. This handoff does not claim full completion because the fresh GUI MCP pass timed out and the installed workspace exposes no decision-specific inspector.

## Scope

Reviewed Event 014 decision categories, decisions, maintained missions, decision-owned scripted triggers and effects, and Event 014 decision localisation only. Shared event log, Event Details, settings, GUI layout source, focus trees, portraits, models, super-event art/audio, spreadsheet, and unrelated decisions were not changed.

## Issue list sorted by severity

### P1: fresh GUI engine evidence remains blocked

The required read-only `hoi4.gui_inspect` and `hoi4.gui_render` evidence exists from the preceding Event 014 audit for all five decision-owned windows, but a corrected fresh `hoi4.gui_inspect` request for `cannibalism_early_header_window` with scenario `{ id = event014_decision_gui_audit_v4 }` timed out after 180 seconds. A parallel corrected batch for all five windows was terminated after no response. No GUI source was changed, so `hoi4.gui_rewrite` was correctly skipped.

The installed MCP also exposes no `hoi4.decision_inspect` route. Exact target-array-expanded row counts for ordinary and international categories therefore remain an engine-evidence blocker rather than a source-proof claim.

### P2: category density is source-bounded by phase, but raw blocks exceed six

The current source has 127 direct entries across 13 categories: achievement tracker 18, containment 19, international response 10, network alerts 2, reconstruction 5, Unified command 5, Unified Larder 9, Unified War Machine 14, Unified Global Campaign 8, Unified world end 2, Warlord command 17, Wendigo command 12, and Wendigo counterwar 6.

The 18 tracker rows are permanently unavailable read-only context, and network alerts are a deliberate two-row alert surface. All other categories use `visible_when_empty = no` in `common/decisions/categories/014_cannibalism_categories.txt`.

Existing route and phase gates, plus the containment visibility patch below, bound active primary action families to six or fewer in the reviewed source matrix. The decision MCP gap prevents an engine-expanded proof when one decision has multiple target rows.

### P2: Unified mission concurrency is now zero/single/pair only

The shared helper `cannibalism_unified_player_mission_slots_available` has 11 explicit combinations at `common/scripted_triggers/014_cannibalism_triggers.txt:3967`: one zero-active case, four single-active cases, and six pair-active cases. No triple-active case is present. Family continuation helpers allow an already active family to continue while the other slot is occupied, while a new third family is blocked.

The automatic international compact and external counterplay missions use separate runtime flags and are intentionally outside this player-started Unified cap. A broader global cap across ordinary, Unified, and external missions remains a parent-level design decision and was not silently added.

### P2: early maintained mission minima need parent balance confirmation

The current timing constants and mission lifecycle are valid, but the preceding audit identified short emergency-response minima for logistics and formation rotation. Raising those floors is a balance change and was not repeated in this bounded pass. No AI weight was changed.

## Changed files and identifiers

### Gameplay visibility patch

Changed `common/decisions/014_cannibalism_decisions.txt`.

- `cannibalism_end_terror_exploitation` at line 16 now requires `cannibalism_public_court_martial_held` before the cleanup action appears.
- `cannibalism_forensic_recovery_teams` at line 596 is hidden while an exploitation, ritual, or network response route is active.
- `cannibalism_search_missing_burial_party` at line 630 is hidden during ritual, concealment, exploitation, humane, and network routes.
- `cannibalism_protect_burial_and_medical_details` at line 680 is hidden during ritual, concealment, exploitation, and network routes.
- `cannibalism_public_court_martial` at line 714 is hidden after Evolution I except on exploitation, ritual appropriation, or network exploitation routes.

Before these guards, the containment source could expose unrelated emergency, forensic, burial, search, trial, and exploitation choices in the same route phase. After them, emergency policy exposes the three ordinary actions plus the humane forensic/protection pair and conditional trial only when evidence allows it; concealment, exploitation, ritual, and network routes expose their own compact action family; and terror cleanup is staged behind the recorded court result.

### Semantic cost localisation patch

Changed `localisation/english/014_cannibalism_l_english.yml`. The file remains UTF-8 with BOM, and the concurrent parent fixes replacing three nonexistent train tokens with `£GFX_train_texticon` were preserved.

The cost rows now use semantic icons for every explicit concrete resource in the reviewed Event 014 surface, including Larder, consumed state population, command power, manpower, infantry equipment, support equipment, artillery, motorized equipment, trains, convoys, fuel, experience, and the three Event 014 receipt types. Evidence-file wording was removed from `cannibalism_trial_cost_text` and `cannibalism_amnesty_cost_text` because evidence is a non-consumed requirement, not a spendable cost.

Representative patched rows include `cannibalism_raise_scavenger_warband_cost_text` at line 546, `cannibalism_emergency_reinforcement_cost_text` at line 576, `cannibalism_seed_foreign_formation_cost_text` at line 603, `cannibalism_unified_mobile_consumption_cost_text` at line 1607, `cannibalism_unified_counterwar_operation_cost_text` at line 1719, and `cannibalism_wendigo_launch_terminal_hunt_cost_text` and `cannibalism_wendigo_press_terminal_hunt_cost_text` at lines 2062 and 2073.

The origin-specialist dynamic selector remains intact and its Island, Siege, March, and generic branches are icon-bearing. Held equipment and emergency readiness reserves remain requirements rather than consumed payment effects; their rows and requirement/effect descriptions identify that distinction.

### Audited concurrent files

`common/scripted_triggers/014_cannibalism_triggers.txt` contains the concurrent six pair additions to the Unified slot helper; they were preserved and verified, not overwritten. The same file's target helpers were audited for existence, route state, identity, control, capitulation, self-target, and actor-array checks.

`common/scripted_effects/014_cannibalism_effects.txt` contains concurrent cleanup and payment work; the all-runtime mission cleanup helper and emergency workshop-recovery exclusion were audited and preserved. No unrelated effect hunk was changed by this pass.

## Decision category lifecycle and cognitive-load notes

- Containment uses the route matrix above. Open-emergency has three ordinary actions, humane forensic/protection choices, and evidence-gated trial; concealment has the three ordinary actions plus record sealing; exploitation/appropriation/network-exploitation has the three ordinary actions plus public trial, terror battalion, and prisoner feeding, with terror cleanup staged after the trial; ritual purge/investigation exposes the three ordinary actions plus two route objectives; post-Evolution clean/disclosure/cordon uses the ordinary actions plus forensic/protection/amnesty as applicable.
- International response has seven primary decision types, but pre-reveal convergence interdiction and post-reveal feeding-state liberation are mutually exclusive. Target and route validity gates keep island and network actions tied to living valid actors. Engine-expanded target-array row counts remain unproven without a decision inspector.
- Reconstruction has four primary actions plus its compact mission and stays within the six-action contract. Unified command has four actions plus its status mission. Unified Larder has four setup actions plus exactly one current consumption method. Unified War Machine phases are foundation one, recruitment six, and operations six. Unified Global Campaign phases are cell one, campaign four, and counterwar two. Unified world-end has two terminal actions.
- Warlord phases are baseline six, network five, and endgame five, with one origin-specific operation and emergency reinforcement included in the phase counts. Wendigo phases are setup six, countdown six, and terminal one. These counts exclude status mission rows from primary-action counts.
- The decision-owned scripted GUI headers expose state values rather than action warehouses: Field Hunger, Command Integrity, Cult Cohesion, Larder, alignment/loyalty, capacities, anchors, countdown, and terminal pressure. The existing GUI render diagnostics prevent a fresh visual overflow claim.

## Mission quality and lifecycle notes

The maintained mission families are `cannibalism_restore_supply_corridor_mission`, `cannibalism_rotate_compromised_formations_mission`, `cannibalism_investigation_mission`, `cannibalism_hold_prison_mission`, `cannibalism_reach_island_mission`, `cannibalism_break_network_mission`, `cannibalism_stop_unification_mission`, `cannibalism_stop_transformation_mission`, the four Unified family missions, the automatic international inspection compact, and `cannibalism_wendigo_terminal_hunt_mission`.

Each reviewed mission has an owner country and route/category, a concrete state, country, anchor, or target identity where applicable, a trigger-backed requirement, a dynamic or constant-backed duration, and distinct success, partial, failure, timeout, and/or cancellation behavior. Active flags, `fire_only_once` where appropriate, target generation checks, route locks, and `cannibalism_clear_all_current_country_mission_runtime` prevent duplicate activation and stale state. The Unified families use the zero/single/pair helper above; the Wendigo terminal hunt has a separate target-aware terminal lifecycle and no partial branch by design.

## Cost, requirement, AI, secrecy, and cleanup notes

- Source references contain 91 `custom_cost_text` rows and 90 unique cost-localisation keys. All 90 resolve. All 136 explicit `custom_effect_tooltip` keys and 206 tooltip keys used by the decision source also resolve in the Event 014 localisation file.
- The current cost contracts remain at or below four distinct consumed resource types after the accepted concurrent cost reduction. Held equipment, state eligibility, evidence, route identity, and readiness reserves are non-consumed requirements and are not treated as extra payment effects.
- `cannibalism_is_valid_synchronized_warlord_partner` at `common/scripted_triggers/014_cannibalism_triggers.txt:5122` checks a live Warlord, slot/route flags, non-capitulation, non-self target, actor-array membership, and the partner's affordability. Wendigo command opening at line 5182 requires reveal, route, live merge-host identity, pre-lock state, and non-capitulation. The scoped source scan found no `Prison Host` text.
- Hannibal identifiers are confined to reveal-gated Wendigo/unification helpers and post-reveal localisation/event text. No pre-reveal decision or category row leaks a Hannibal identity; the source scan was intentionally not treated as a claim that legitimate post-reveal Hannibal prose is absent.
- Existing cooldowns, target-generation checks, receipt epochs, active flags, `fire_only_once`, route closure cancellation, and all-runtime cleanup remain in place. No free-unit, workshop-equipment, receipt-reuse, or cooldown bypass loop was proven. The concurrent emergency workshop guard excludes the emergency template from recovery.
- Every inspected costed decision retains an AI block. The direct probability inspection succeeded, but the named `chaosx_ai_probability_auditor` subagent route is not exposed in this runtime. No AI or weighted modifier was changed, so a probability comparison was not required.

## MCP evidence and validation

The preceding Event 014 decision audit recorded read-only `hoi4.gui_inspect` artifacts for all five windows: `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`. The retained inspect artifacts are:

- Early: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f9ec9cc057d1fa03b55eb3bf334ad907e100fa67b81ddbb61cfa071dc5c31d2/7313ad7dfff76ebc91e16ad09550c31f3934b8ac3cf2790c68295510e77d7c2/gui-inspect.f5d8afdbe3b7a2b9.json`.
- Network: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1088c8423e0075139f6079c5d23aa1579e932499c3dd4ee63116dc4913d01354/56516d8c3631f21cb1d49d2a6ca494ec146092ebe468e6ec53ef7f84ee3a474c/gui-inspect.c0990be4410fc5fd.json`.
- Warlord: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecdcc6f75eeb0dc612bbece8d067b1a97b9891d96d1a98a0e4d9fc09cb17ec4b/36203246191a4f49810839437d0da287057048506ac713968a1e69ff8fd347d2/gui-inspect.5b2826a09dfcd433.json`.
- Revealed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f286cdca11bf09838b578f208976707b2d242b0d381eb1460fd1a3292d1c0e15/a398bb493fb6f0f31f1725683167d3102c3d07276bc420cffab90db1d8fac034/gui-inspect.c1e1aeee9718fa0b.json`.
- Wendigo: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d34427fa962ceb58dbb7ad1f33b439d7c3bf3fd6e4c997468a5836167c1370e8/28f6823de75768ff3df7c9f254c726c1b34000d2b0b5024bde5638b223e97445/gui-inspect.e8b38fea6ca64cd3.json`.

Prior renders succeeded for early, network, and Warlord and emitted the corresponding `*-full.svg` artifacts. Revealed and Wendigo renders returned `INTERNAL_ERROR` in that pass. The renderer also reported `MCP_RESPONSE_TRUNCATED`, `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED`, and `INDEX_SYMBOL_COLLISION`, and ignored requested state/resolution variants. These artifacts establish source/model parsing only and do not replace gameplay or visual acceptance.

The fresh direct `hoi4.probability_inspect` call used adapter `decision_ai_will_do` on `common/decisions/014_cannibalism_decisions.txt` and returned 95 candidates, zero available candidates under the default scenario, 32 required inputs, zero unresolved inputs, and `poolComplete = false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a52a99372f0bd919bf7e796ed30150c12deb909fec550fe0d1b6d45a70813755/1fff17999a82a455ed4f2f9257cfe280c99ecc731d215e5cb400e7413cd98c46/probability-inspect-40b350276492.json`.

Task-specific validation completed:

- Static category parser: 127 direct entries with the category counts above.
- Unified slot parser: 11 `AND` cases with positive active-family counts `0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2`; maximum two and no triple case.
- Localisation coverage: 90 unique cost keys, 136 effect-tooltip keys, and 206 tooltip keys with zero missing keys; the BOM check remained true.
- Secrecy scan: no `Prison Host` string in the scoped decision, category, trigger, effect, or localisation files.
- `git diff --check` reported no whitespace errors on the scoped changed files.

Skipped meaningful validation: no live HOI4 launch or gameplay simulation was performed, per repository policy; fresh GUI inspect/render timed out; no `hoi4.decision_inspect` route or named probability-auditor subagent was available; no probability compare was needed because no weighted AI patch was made.

## Remaining blockers and parent follow-up

The parent should retain the fresh GUI timeout and decision-inspector absence as explicit blockers, review target-array row density when engine evidence is available, and decide whether ordinary/external mission concurrency needs a broader cap beyond the Unified player-started pair contract. The event UI worker owns any dedicated GUI layout/parser repair. No new plan handoff was written because remaining work is either GUI-worker-owned or a parent-level balance/design decision.

No model, focus, portrait, super-event, art/audio, spreadsheet, or unrelated decision changes were made. No commit was created from this shared worktree because the gameplay and localisation files contain concurrent parent/agent edits; the parent should commit the reviewed aggregate diff.
