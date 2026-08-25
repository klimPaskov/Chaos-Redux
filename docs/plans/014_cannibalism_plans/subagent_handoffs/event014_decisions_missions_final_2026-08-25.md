# Event 014 decisions and missions final bounded audit

Date: 2026-08-25.

Scope: Event 014 Cannibalism decision categories, decisions, missions, their scripted effects and triggers, constants, localisation, AI, and Event 014-owned GUI integration only.

Out of scope: shared event log, event-details framework, settings, super-event GUI, model assets, focus layout, country packages, and unrelated interfaces.

## Status

The bounded audit is complete and no gameplay source patch was applied in this pass.

The current source has no newly proven narrow defect that can be fixed without either inventing missing texticon assets, changing the accepted phase design, or taking ownership of the dedicated GUI layout that belongs to the event UI worker.

The only changed file from this pass is this handoff.

The existing seven-cost source patch is present in commit `a25e0045d` and was audited rather than duplicated.

## Issue list sorted by severity

### P1: cost presentation still violates the icon-first contract

- `localisation/english/014_cannibalism_l_english.yml` still presents many Event 014 spendable values as literal `Larder`, `Population`, `Manpower`, `Support Equipment`, `Trucks`, `Trains`, `Receipt`, and similar prose, including Warlord recruitment, Warlord route, Unified, and Wendigo decision surfaces.
- The seven decisions covered by `a25e0045d` no longer consume a fifth resource type, and no additional decision with more than four distinct consumed cost types was proven in the current source, but their updated strings still need proper texticons.
- The repository currently has no Event 014-specific texticon definitions for Larder, population, or death-receipt values, so this audit did not invent icons or substitute misleading vanilla icons.
- Recommended owner/fix: add or approve the required Event 014 texticons and then update the exact cost localisation keys in `localisation/english/014_cannibalism_l_english.yml` while keeping requirements separate from consumed costs.

### P1: dedicated GUI source has a parser blocker

- `interface/014_cannibalism_frontline_hunger.gui:117` and `:127` define the network country/state entry button sizes as `size = { x = ... y = ... }` instead of the `width`/`height` form used by the surrounding container definitions.
- This is the source-level blocker identified by the GUI audit; it belongs to the Event 014 dedicated GUI worker and was not patched here because concurrent edits are present in the same GUI file and this pass owns gameplay integration, not layout creation.
- Recommended owner/fix: the event UI worker should make the smallest parser correction, rerun `hoi4.gui_inspect` and `hoi4.gui_render`, and provide a post-change comparison for all five Event 014 windows.

### P1: visible category and mission density is above the decision skill contract

- Direct decision counts across the consolidated source blocks are containment 19, international response 10, reconstruction 5, achievement tracker 18, network alerts 2, unified command 5, unified larder 9, unified war machine 14, unified global campaign 8, unified world end 2, Warlord command 17, Wendigo command 12, and Wendigo counterwar 6.
- Several of these categories exceed six visible primary actions, and every one of the 13 Event 014 category blocks currently uses `visible_when_empty = yes` in `common/decisions/categories/014_cannibalism_categories.txt`.
- Many actions are phase-gated, so the raw counts do not prove that every action is simultaneously visible, but they do prove that lifecycle and empty-category hiding need a design pass rather than a cosmetic edit.
- Recommended owner/fix: phase or merge action families so the player sees no more than six primary actions per active category and hide empty categories except for the intentionally read-only tracker/context surfaces.

### P1: no global active-mission cap is enforced

- The ordinary active-objective helper `cannibalism_current_country_has_active_maintained_objective` in `common/scripted_triggers/014_cannibalism_triggers.txt:1258` covers investigation, prison, island, break-network, stop-unification, and stop-transformation, but omits the logistics and rotation missions and the inspection compact.
- That helper is used by the idle observer cleanup path, not as an activation cap, so the omission does not itself create a false availability block; it also means there is no single cap preventing overlapping ordinary and route-specific objectives.
- The four Unified mission families each use an independent active flag in `common/decisions/014_cannibalism_decisions.txt`, so up to four Unified missions can be active concurrently when their route flags allow it.
- Recommended owner/fix: decide the intended concurrency in the Event 014 plan, then add a phase-aware cap or a clearly surfaced parallel-objective rule with matching cleanup and tooltip text; do not silently add a cap in a local helper.

## Decision category lifecycle notes

- `cannibalism_achievement_tracker_category` is a read-only tracker with 18 rows and should remain a deliberate exception to the primary-action limit if it is visually separated and clearly non-interactive.
- `cannibalism_containment_category` is split across source blocks at `014_cannibalism_decisions.txt:15`, `:441`, and `:837`; its ordinary response actions and logistics/rotation actions are gated by containment visibility and route/state validity.
- `cannibalism_international_response_category` is split across `:41` and `:1035`; its target missions cancel on world end, route visibility loss, or target identity invalidation.
- `cannibalism_reconstruction_category` has five actions and is within the raw count guideline, but its category visibility still follows the global `visible_when_empty = yes` setting.
- `cannibalism_network_alerts_category` has two state-targeted actions and correctly requires an inbound route response and a valid screenable state.
- `cannibalism_warlord_command_category` is split at `:1241` and `:2042`; state-targeted Warlord actions are route-gated and use target validity checks, but the category contributes to the high-density command surface.
- `cannibalism_wendigo_command_category` has 12 actions and should be phased or grouped before adding more command buttons.
- `cannibalism_wendigo_counterwar_category` is split at `:1291` and `:2805`; counterwar and terminal-hunt actions are route-gated and target-aware.
- `cannibalism_unified_command_category`, `cannibalism_unified_larder_category`, `cannibalism_unified_war_machine_category`, `cannibalism_unified_global_campaign_category`, and `cannibalism_unified_world_end_category` are separately visible categories; this is usable only while the route phase hides inactive families, so empty-category visibility should be reviewed with the GUI state contract.

## Cognitive-load notes

- Visible actions: the raw category counts above exceed six in containment, achievement tracker, Warlord command, Wendigo command, unified larder, unified war machine, unified global campaign, and Wendigo counterwar; route gating reduces simultaneous exposure but does not remove the need for phase-specific density proof.
- Active missions: the source defines eight maintained ordinary/route mission families, four independently activatable Unified missions, one Wendigo terminal hunt, and one automatic international inspection compact; this can exceed the normal one-to-three active mission guideline.
- Player-facing values: Larder, consumed population, Network Alignment, Frenzy, contamination/spread, route pressure, counterpressure, world hostility, and death receipts are shown as dynamic values, but several decision tooltips still explain them as long numeric rows rather than a threshold, consequence, and player response.
- Text density: many cost and requirement keys combine multiple raw values with prose and literal resource names, particularly the Warlord, Unified, and Wendigo groups.
- Significance: the dedicated GUI has meter/state concepts, but direct decision surfaces do not consistently mark the threshold or the action that changes it; the next pass should use concise requirement/effect lines and state-aware icons without exposing implementation flags.

## Mission quality and lifecycle inventory

The following inventory records the current owner, category/region, requirement, duration, resolution, and duplicate risk.

- `cannibalism_maintain_international_inspection_compact` (`014_cannibalism_decisions.txt:272`) is an automatic international-response compact owned by the current country and world route, with no map target, `activation = { has_country_flag = cannibalism_compact_vigilance_mission_active }`, `available = { always = no }`, a 365-day constant-backed timeout, world-end cancellation, and explicit full/partial/failure timeout effects; the unavailable selector is intentional for an auto mission, and its active flag prevents duplicate activation.
- `cannibalism_restore_supply_corridor_mission` (`:495`) is a containment logistics mission for the current country primary theater/supply corridor, requires `cannibalism_logistics_hold_complete`, uses `cannibalism_logistics_mission_duration`, and has complete, partial timeout, failure timeout, and cancellation cleanup through `cannibalism_clear_logistics_mission`; the active flag prevents duplicate starts, but its effective minimum is about 63 days and merits balance review.
- `cannibalism_rotate_compromised_formations_mission` (`:558`) is a containment primary-theater rotation mission, requires `cannibalism_rotation_hold_complete`, uses `cannibalism_rotation_mission_duration`, and has complete, partial timeout, failure timeout, and cancellation cleanup through `cannibalism_clear_rotation_mission`; the active flag prevents duplicate starts, but its effective minimum is about 49 days and merits balance review.
- `cannibalism_investigation_mission` (`:934`) is an international-response investigation against a saved valid target, requires `cannibalism_investigation_objective_complete`, uses a dynamic 120–210-day duration, and has success, partial, failure, target-invalid cancellation, and cleanup through `cannibalism_resolve_investigation_cancellation`; `fire_only_once = yes` and the active flag limit duplicates.
- `cannibalism_hold_prison_mission` (`:984`) is an international-response prison-hold objective against its saved valid target, requires `cannibalism_prison_objective_complete`, uses a dynamic 120–210-day duration, and has success, partial, failure, target-invalid cancellation, and cleanup through `cannibalism_resolve_hold_prison_cancellation`; `fire_only_once = yes` and the active flag limit duplicates.
- `cannibalism_reach_island_mission` (`:1090`) is an international-response island/state route objective, requires `cannibalism_reach_island_objective_complete`, uses a dynamic 150–270-day duration, and has success, partial, failure, route visibility/target-identity cancellation, and cleanup through `cannibalism_resolve_reach_island_cancellation`; `fire_only_once = yes` and the active flag limit duplicates.
- `cannibalism_break_network_mission` (`:1140`) is an international-response network/state route objective, requires `cannibalism_break_network_objective_complete`, uses a dynamic 150–240-day duration, and has success, partial, failure, route visibility/target-identity cancellation, and cleanup through `cannibalism_resolve_break_network_cancellation`; `fire_only_once = yes` and the active flag limit duplicates.
- `cannibalism_stop_unification_mission` (`:1190`) is a pre-reveal international route objective against the saved unification target, requires `cannibalism_stop_unification_objective_complete`, uses a dynamic 60–210-day duration, and cancels when the reveal completes, the target identity changes, or the active flag is cleared; success, partial, failure, and cancellation each use dedicated resolution helpers, and `fire_only_once = yes` limits duplicates.
- `cannibalism_stop_transformation_mission` (`:1292`) is a Wendigo counterwar route objective against the saved transformation target, requires `cannibalism_stop_transformation_objective_complete`, uses a dynamic 120–240-day duration, and cancels when the target identity changes or the counterwar route closes; success, partial, failure, and cancellation each use dedicated resolution helpers, and `fire_only_once = yes` limits duplicates.
- `cannibalism_unified_command_mission` (`:1491`), `cannibalism_unified_larder_mission` (`:1640`), `cannibalism_unified_war_machine_mission` (`:1835`), and `cannibalism_unified_counterwar_mission` (`:1975`) are current-country route-wide Unified objectives with no map region, each requiring its own completion trigger, using a dynamic roughly 120–150-day duration, and providing success, partial timeout, failure timeout, cancellation, and clear-helper paths; each active flag prevents a duplicate within its family, but the four independent flags allow parallel mission density that needs an explicit design decision.
- `cannibalism_wendigo_terminal_hunt_mission` (`:2690`) is a Wendigo terminal-hunt route objective against the active hunt target, requires `cannibalism_wendigo_terminal_hunt_has_succeeded`, cancels on `cannibalism_wendigo_terminal_hunt_has_failed`, uses the file-local 120-day `@CANNIBALISM_WENDIGO_TERMINAL_HUNT_MISSION_DAYS`, and routes both success and failure through dedicated resolution helpers; the active flag and terminal route state prevent ordinary duplicate starts.

## Cost, requirements, and localisation

- The cost audit found no current Event 014 decision with more than four distinct consumed resource types after the seven-cost reduction commit `a25e0045d`.
- Paid values and non-consumed requirements are not consistently separated in the player-facing strings, especially for held equipment, state population, receipt evidence, and route validity.
- Native icon precedents exist in the repository for command power, manpower, support equipment, infantry equipment, convoys, and trains, but Larder, population, and receipt-specific icons are not defined for this event.
- The exact localisation surface requiring a future icon pass is `localisation/english/014_cannibalism_l_english.yml`, including the Warlord cost keys around lines 546–572, Warlord route keys around 599–619, Unified keys around 1530–1737, and Wendigo keys around 1794–1818 and 2057–2084.
- Tooltip trigger/effect coverage exists for the inspected mission blocks through `custom_trigger_tooltip` and `custom_effect_tooltip`, but the underlying text remains too verbose in several decision families and should be shortened together with the icon pass.

## AI validity and route locks

- A source scan found `ai_will_do` on all 94 costed decisions; no costed decision was found without an AI block.
- Warlord decisions use route-open checks, valid state targets, current state ownership/control checks, state population validity, and the emergency command-open gate.
- Unified target triggers and Wendigo target triggers validate live targets, route/reveal state, ownership/control or target identity, anchor/state/template/capacity constraints, and counterwar/terminal route state according to the current helper contracts.
- The emergency reinforcement availability trigger checks the Warlord command-open flag, emergency route flag, Larder, infantry equipment, and support equipment reserves.
- The concurrent source change in `common/scripted_effects/014_cannibalism_effects.txt` excludes the emergency reinforcement template from workshop recovery, so the emergency route does not regain workshop infantry equipment after paying its readiness requirement; this was verified and not reapplied here.
- No weighted AI patch was made, so no probability comparison was required after the baseline inspections.
- Baseline probability artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d03b3e58d930eddc93e1893e30856372cd307eed1015005382158a9df94a601/582d962b5490dc980d66ab80afcdb3888f2262ba9d28b0dd4062a62ee3f5b9fc/probability-inspect-0b5f0fc8f254.json` for decision AI source discovery, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f44a0e4cda4c63ecc0a28a7f4ca1e891b8a794da07f89a69d6826c963b3fe633/05b38ac83e2f8a04486ae9f5b7593ef1b0d27f745db55182d01ea6a6b35cec79/probability-inspect-0b5f0fc8f254.json` for the mission-adapter fallback, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e60c4d61904e9c1fea466a4d6517adfdddb6d91420fe55a3983b9fb897e8f69c/4bdf1c5b2697b81b0a2a99ba27bcd8a6878d218884ad9e288ad99e5d7bafca02/probability-inspect-02bd4b54a3b6.json` for the no-surface AI-strategy discovery.
- The decision source inspection found 95 candidates, 0 available candidates under the default scenario, 32 required inputs, 0 unresolved inputs, and `poolComplete = false`; the mission adapter exposed no separate mission candidates and suggested the decision adapter.

## Cleanup and exploit-risk notes

- `cannibalism_clear_all_current_country_mission_runtime` covers ordinary, compact, Unified, and Wendigo mission flags/variables and clears the corresponding runtime state.
- Every inspected mission has explicit success, partial, failure, or cancellation behavior and a cleanup helper.
- Active flags, `fire_only_once`, target identity checks, route locks, and validity triggers prevent the obvious duplicate/reward/receipt/cooldown loops in the inspected source.
- No `Prison Host` identifier or player-facing animation-control decision was found in the Event 014 decision, category, helper, trigger, localisation, or specification surfaces.
- No free-unit or workshop-equipment loop was proven in this pass; the concurrent emergency workshop-recovery guard is the relevant protection and should remain intact.
- The remaining exploit risk is design-level rather than a proven source loop: independently active Unified missions and route families can stack rewards/pressure outcomes unless the intended concurrency is documented and surfaced.

## GUI MCP evidence and limitations

The five required Event 014 decision-owned windows were inspected read-only with `hoi4.gui_inspect` and rendered with `hoi4.gui_render`: `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`.

- Inspect artifacts: early `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f9ec9cc057d1fa03b55eb3bf334ad907e100fa67b81ddbb61cfa071dc5c31d2/7313ad7dfff76ebc91e16ad09550c31f3934b8ac3cf2790c68295510e77d7c2b/gui-inspect.f5d8afdbe3b7a2b9.json`, network `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1088c8423e0075139f6079c5d23aa1579e932499c3dd4ee63116dc4913d01354/56516d8c3631f21cb1d49d2a6ca494ec146092ebe468e6ec53ef7f84ee3a474c/gui-inspect.c0990be4410fc5fd.json`, Warlord `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecdcc6f75eeb0dc612bbece8d067b1a97b9891d96d1a98a0e4d9fc09cb17ec4b/36203246191a4f49810839437d0da287057048506ac713968a1e69ff8fd347d2/gui-inspect.5b2826a09dfcd433.json`, revealed `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f286cdca11bf09838b578f208976707b2d242b0d381eb1460fd1a3292d1c0e15/a398bb493fb6f0f31f1725683167d3102c3d07276bc420cffab90db1d8fac034/gui-inspect.c1e1aeee9718fa0b.json`, and Wendigo `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d34427fa962ceb58dbb7ad1f33b439d7c3bf3fd6e4c997468a5836167c1370e8/28f6823de75768ff3df7c9f254c726c1b34000d2b0b5024bde5638b223e97445/gui-inspect.e8b38fea6ca64cd3.json`.
- Render artifacts were produced for early, network, and Warlord at the renderer's fixed output, including `cannibalism_early_header_window-full.svg`, `cannibalism_network_window-full.svg`, and `cannibalism_warlord_command_window-full.svg`; revealed and Wendigo returned `INTERNAL_ERROR` with no artifact.
- The renderer ignored requested resolutions and state variants and emitted `MCP_RESPONSE_TRUNCATED`; inspect/render diagnostics also include `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED`, `INDEX_SYMBOL_COLLISION`, and inline truncation.
- These artifacts are evidence of source/model parsing and the renderer limitation only; they are not gameplay or balance proof, and no renderer resolution/state claim is made from them.

## Validation and handoff

- Required offline wiki pages, vanilla documentation, Event 014 specifications, prior GUI/probability handoffs, and vanilla decision precedents were read before this audit.
- Source scans covered decision cost cardinality, AI presence, mission definitions, route/target helpers, cleanup helpers, Prison Host strings, animation-control strings, and Event 014 localisation cost surfaces.
- `hoi4.probability_inspect` was run before considering any weighted AI change; no weighted AI change was applied, so `hoi4.probability_compare` was correctly skipped.
- `hoi4.gui_inspect` and `hoi4.gui_render` were run for all five Event 014-owned GUI windows; `hoi4.gui_rewrite` was skipped because no GUI patch was applied and the layout worker owns the dedicated GUI source.
- No live game launch or gameplay claim was made.

Remaining issues are the icon/texticon asset and localisation pass, the dedicated GUI parser and renderer follow-up, and parent-level decisions about category phasing, mission concurrency, and emergency duration balance.

No plan handoff beyond this audit was written because each remaining change is either an event UI worker task or a broader design/balance decision requiring parent ownership.
