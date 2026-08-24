# Event 014 Cannibalism decisions, missions, and owned GUI audit

Audit date: 2026-08-24.

Scope: Event 014 Cannibalism decision categories, decisions, missions, timed objectives, route locks, AI-facing weights, custom-unit acquisition, and the five Event-014-owned scripted GUI surfaces.

Explicit exclusions: the shared event log, shared Event Details framework, settings UI, super-event framework, shared registries, and unrelated GUIs were not inspected or changed.

This is a read-only audit. No gameplay file, GUI source file, scripted effect, localisation file, or asset was modified.

## Executive result

The most urgent proven defect is a parser failure in the Event-014 network entry GUI. The country and state entry `buttonType` definitions in `interface/014_cannibalism_frontline_hunger.gui:117` and `:127` use nested `size = { x = ... y = ... }` syntax, while the captured prelaunch error reports malformed `width` and `height` tokens near lines 119 and 129. This prevents dependable network-entry click boxes and invalidates any claim that the current network list is clickable until the Event UI worker repairs the layout and repeats MCP inspection/rendering.

The largest gameplay/UI contract issue is cost presentation and cost count. Seven gameplay-changing decisions expose five or more distinct spendable types, and most Warlord, unified, objective, and Wendigo cost strings spell resources as literal labels instead of using texticons. Several rows also mix consumed costs with non-consumed equipment, target, route, receipt, or reserve requirements. This violates the four-cost limit and makes the actual transaction unreadable.

The most serious balance/exploit risk is `cannibalism_emergency_reinforcement`. Its affordability trigger checks an infantry/support equipment reserve but does not consume that reserve, while `cannibalism_execute_warlord_recruitment_transaction` adds the workshop recovery equipment amount after every successful transaction when `cannibalism_warlord_workshop_conversion_open` is set, including the emergency template branch. The emergency tooltip says no equipment is generated. The state cooldown prevents same-day repetition, but the contradiction still permits a repeated recovery loop and must be resolved before sign-off.

The direct current GUI evidence is incomplete because fresh MCP calls timed out. Historical MCP artifacts cover the five owned windows, but they are not a substitute for a current post-source-change matrix. The current GUI parser error is independently proven by the captured prelaunch log.

## Severity-sorted issue list

### Blocker: network country/state entry hitboxes do not parse

File: `interface/014_cannibalism_frontline_hunger.gui:112-130`.

Identifiers: `cannibalism_network_country_entry_select` and `cannibalism_network_state_entry_select`.

Evidence: each entry container has a valid container `size = { width = @CANNIBALISM_NETWORK_ENTRY_WIDTH height = @CANNIBALISM_NETWORK_ENTRY_HEIGHT }`, but the nested `buttonType` uses `size = { x = @CANNIBALISM_NETWORK_ENTRY_WIDTH y = @CANNIBALISM_NETWORK_ENTRY_HEIGHT }`.

The captured log `docs/testing/live_qa/20260815_094543_startup_crash/logs/prelaunch/error.log` records `Malformed token: width` and `Malformed token: height` near line 119 and the same pair near line 129 for this file.

Impact: country/state rows can fail to load or lack a valid hitbox, so `cannibalism_network_country_entry_select_click` and `cannibalism_network_state_entry_select_click` cannot be treated as working click contracts.

Fix instruction: route this exact layout correction to `chaosx_event_ui_worker`; use the documented vanilla button hitbox form supported by the local Interface Modding reference, then run fresh `hoi4.gui_inspect` and `hoi4.gui_render` checks for the network window before any rewrite or completion claim.

### High: seven decisions exceed the four-spendable-cost limit

The following decisions and localisation keys expose five or more spendable types and need a design-level cost reduction or a split between paid costs and requirements.

| Decision | Source | Cost localisation | Count and current spendables | Required direction |
| --- | --- | --- | --- | --- |
| `cannibalism_unified_mobile_consumption` | `common/decisions/014_cannibalism_decisions.txt:1621` | `localisation/english/014_cannibalism_l_english.yml:1601` | 7: state population, command power, trucks, trains, support equipment, convoys, fuel | Reduce to at most four consumed types; move route, reserve, and target checks into a separate requirement tooltip. |
| `cannibalism_unified_build_silent_anchorage` | `common/decisions/014_cannibalism_decisions.txt:1819` | `localisation/english/014_cannibalism_l_english.yml:1671` | 5: manpower, support equipment, convoys, fuel, navy experience | Keep four meaningful paid inputs or make one input a non-consumed requirement with its own tooltip. |
| `cannibalism_unified_launch_air_interdiction` | `common/decisions/014_cannibalism_decisions.txt:1829` | `localisation/english/014_cannibalism_l_english.yml:1676` | 5: small airframes, transports, support equipment, fuel, air experience | Reduce or split; keep the air operation's target/route requirement out of the cost line. |
| `cannibalism_unified_destroy_coalition_hub` | `common/decisions/014_cannibalism_decisions.txt:1953` | `localisation/english/014_cannibalism_l_english.yml:1713` | 5: support equipment, trucks, fuel, command power, army experience | Reduce to four and expose the coalition target as a requirement. |
| `cannibalism_unified_convert_counterwar_pressure` | `common/decisions/014_cannibalism_decisions.txt:1969` | `localisation/english/014_cannibalism_l_english.yml:1719` | 5 distinct spendables in the current transaction | Reduce or split the conversion contract; do not hide the fifth input in effect text. |
| `cannibalism_wendigo_press_terminal_hunt` | `common/decisions/014_cannibalism_decisions.txt:2712` | `localisation/english/014_cannibalism_l_english.yml:2066` | 5: Wendigo Larder, command power, infantry equipment, support equipment, fuel | Reduce to four; keep terminal route and target requirements separate. |
| `cannibalism_muster_wendigo_pack_from_enemy_death_receipt` | `common/decisions/014_cannibalism_decisions.txt:2739` | `localisation/english/014_cannibalism_l_english.yml:2076` | 5: enemy-loss receipt, state population, Wendigo Larder, infantry equipment, support equipment | Treat the receipt as a requirement or replace one paid input; retain an icon-first line. |

The GUI buttons themselves are view/navigation controls and expose zero spendable costs. The four-cost audit therefore applies to decisions and their tooltips, not to the five owned scripted GUI windows.

### High: cost localisation is not icon-first and mixes costs with requirements

File: `localisation/english/014_cannibalism_l_english.yml`.

The early baseline rows around lines 42-106 are generally icon-first, but `cannibalism_trial_cost_text` at line 90 includes a literal `Evidence file`, `cannibalism_amnesty_cost_text` at line 95 includes a literal `Evidence file`, and `cannibalism_feed_selected_prisoners_cost_text` at line 111 includes a literal `state population`. These are counters or requirements rather than ordinary consumed resources and need a separate requirement clause with an Event-014 icon-first representation.

The Warlord rows around lines 541-633 use literal labels for Larder, population, equipment, manpower, support, command, convoys, and route requirements. `cannibalism_consume_controlled_state_cost_text`, the unit-raising keys, `cannibalism_emergency_reinforcement_cost_text`, `cannibalism_seed_foreign_formation_cost_text`, and the intensify, abandon, align, synchronize, island, siege, and march keys should be rewritten as concise icon-first paid-cost lines plus distinct requirement tooltips.

The unified rows around lines 1543-1726 largely use literal labels even when they have only one to four types. The `mobile`, `silent anchorage`, `air operation`, `counterwar`, and `counterwar conversion` rows are both over budget and literal-label rows. The objective rows around lines 1945-2017 are also literal-label rows. The Wendigo rows around lines 1793-2081 similarly omit icons for larder, population, receipts, equipment, support, fuel, and command in several contracts.

No Event-014-specific texticon keys for Larder, state population, or death receipts were found by the scoped localisation search. Use existing registered texticons for ordinary resources and add or route valid Event-014 icon-first keys for custom ledger values before rewriting the strings; never substitute a literal resource name for a missing icon.

### High: emergency reinforcement has a repeated equipment recovery contradiction

Files: `common/decisions/014_cannibalism_decisions.txt:2226-2247`, `common/scripted_triggers/014_cannibalism_triggers.txt:4848-4858`, and `common/scripted_effects/014_cannibalism_effects.txt:16528-16619`.

`cannibalism_warlord_can_pay_emergency_reinforcement_cost` checks the command-open flag, Larder, and infantry/support equipment reserve. The recruitment transaction consumes the exact Deaths population and Larder and adds manpower, but the equipment reserve is not subtracted. The normal unit-spawn branch is skipped for the emergency template, yet the later workshop block at approximately lines 16589-16593 adds `constant:cannibalism_warlord_contract.workshop_recovery_infantry` infantry equipment whenever `cannibalism_warlord_workshop_conversion_open` is set. That constant is 75 at `common/script_constants/014_cannibalism_constants.txt:3254`.

The emergency effect tooltip says that no unit or equipment is generated, so the player-facing contract contradicts the effect. The state recruitment cooldown limits frequency but does not remove the repeated recovery loop.

Fix instruction: either exclude the emergency template from workshop recovery and retain the no-equipment promise, or explicitly charge/consume the reserve and describe the recovery. Add a bounded recovery rule if the workshop reward is intentional, then re-audit the emergency transaction and its tooltip as one contract.

### High: category density and empty rows exceed the scan budget

File: `common/decisions/categories/014_cannibalism_categories.txt`.

The current source has 13 Event-014 categories including the read-only achievement tracker, and all categories use `visible_when_empty = yes`. The phase helpers gate decisions, but empty category rows remain visible.

The source contains 127 top-level decision or mission IDs. Maximum category counts are containment 19, Warlord command 17, unified war machine 14, Wendigo command 12, international response 10, unified Larder 9, unified global campaign 8, unified command 5, reconstruction 5, Wendigo counterwar 6, unified world end 2, network alerts 2, and the achievement tracker 18.

The highest-density categories violate the six-primary-action ceiling whenever their route flags expose the full tranche. The achievement tracker is intentionally read-only but still adds 18 non-action rows to the decision wall. Fix instruction: phase or merge low-impact rows, cap each visible tranche at six primary actions, and hide empty categories where the phase has no actionable entry; preserve the read-only tracker only if its empty-row behavior is explicitly accepted.

### Medium: four unified missions can coexist with baseline and objective missions

Files: `common/decisions/014_cannibalism_decisions.txt:1491-1517`, `:1640-1661`, `:1835-1856`, and `:1975-1996`; activation helpers are in `common/scripted_effects/014_cannibalism_effects.txt:14326-14372`.

`cannibalism_unified_record_command_operation`, `cannibalism_unified_record_larder_operation`, `cannibalism_unified_record_war_machine_operation`, and `cannibalism_unified_record_counterwar_operation` each independently activate its mission when its own active flag is absent. No global active-mission cap is visible. A route can therefore display multiple unified missions alongside the containment, international, or objective mission families.

Each family has a duplicate guard and cleanup helper, which is positive, but the presentation can still exceed the normal three active-mission budget. Fix instruction: enforce a route-phase cap or present one consolidated active objective with clearly distinct sub-stages; retain the existing per-family duplicate and cleanup guards.

### Medium: logistics and rotation missions can be materially shorter than the intended decision horizon

Files: `common/script_constants/014_cannibalism_constants.txt:811-823` and the mission blocks at `common/decisions/014_cannibalism_decisions.txt:495-590`.

The logistics hold has a minimum requirement of 21 days and a timeout buffer of 42 days, producing an actual minimum mission duration of 63 days. The rotation hold has a minimum requirement of 14 days and a 35-day buffer, producing an actual minimum of 49 days. These values are below the easy-to-maintain 90-day mission band in the decisions-and-missions skill and can encourage rapid retry loops.

Fix instruction: decide whether these are deliberately urgent operations; if not, centralize a longer dynamic buffer or phase gate. Any AI or timing weight change must receive a named probability-auditor baseline and same-scenario compare.

### Medium: the compact watchdog is auto-activated but permanently unavailable

File: `common/decisions/014_cannibalism_decisions.txt:272-305`.

`cannibalism_maintain_international_inspection_compact` activates from `cannibalism_compact_vigilance_mission_active`, has a 365-day timeout, and supplies full, partial, and failure timeout effects. Its `available = { always = no }` intentionally prevents manual completion, but the source does not explain that it is a non-selectable watchdog.

The local decision wiki states that mission `available` controls completion and defaults to true. Fix instruction: verify this automatic watchdog behavior in the engine, add an explicit non-selectable convention or dynamic tooltip if supported, and explain that only timeout evaluates progress; do not leave a player-facing mission that appears permanently disabled without context.

### Medium: animation-by-default has no visible toggle, but missing assets leave blank surfaces

File: `common/scripted_guis/014_cannibalism_scripted_gui.txt`.

All five owned scripted GUIs show animated siblings by visibility/animation state without a visible animation button or animation text in the `cannibalism.gui.*` localisation family. This satisfies the no-visible-toggle requirement. The static siblings are mostly `always = no`, however, so a missing or failed animation asset produces a blank area rather than a resilient static fallback.

Fix instruction: retain animation-by-default, validate every animation asset in the owned windows, and make the static fallback conditional on animation availability if the GUI worker can do so without introducing an animation control.

### Medium: current visual/bounds evidence is insufficient for a release claim

The historical artifacts show prior full-window SVGs, but current source and parser state have changed. Fresh current inspection/rendering did not complete, so current high-DPI scaling, hover, selected, disabled, warning, empty, long-text, click-region, and clipping behavior is unresolved. The network parser blocker makes the current click-region contract especially unsafe.

Fix instruction: after the network syntax correction, rerun `hoi4.gui_inspect` and `hoi4.gui_render` for every owned window across all supported resolutions and relevant normal, hover, selected, disabled, warning, active, completed, empty, and long-text states; record bounds and click regions, then compare against the pre-change artifacts before any rewrite.

### Low: achievement tracker adds intentional but costly read-only scanning

File: `common/decisions/014_cannibalism_decisions.txt:320-428`.

The 18 achievement entries are read-only with an always-false availability tooltip, and stage visibility is gated by achievement flags. This is mechanically safe, but it contributes to decision-wall density. Keep it only if the category is visibly labelled as a tracker and empty/locked rows are intentionally accepted.

## Decision-category lifecycle and cognitive-load notes

| Category | Source block | Visibility/GUI | Top-level IDs | Lifecycle observation |
| --- | --- | --- | ---: | --- |
| `cannibalism_containment_category` | `014_cannibalism_decisions.txt:15`, `:441`, `:837` | `cannibalism_containment_decisions_visible`; `cannibalism_early_header_scripted_gui` | 19 | Baseline, ritual, and objective tranches are phase-gated, but the category remains visible when empty. |
| `cannibalism_international_response_category` | `:41`, `:1035` | `cannibalism_international_response_category_is_visible`; no dedicated GUI | 10 | Compact and overseas/network objectives can coexist with the international response actions. |
| `cannibalism_reconstruction_category` | `:176` | `cannibalism_reconstruction_category_is_visible`; no dedicated GUI | 5 | Small category, but still remains as an empty row. |
| `cannibalism_achievement_tracker_category` | `:320` | `cannibalism_system_started`; read-only | 18 | Stage-gated tracker; all entries are unavailable by design. |
| `cannibalism_warlord_command_category` | `:1241`, `:2042` | `cannibalism_warlord_command_is_open`; `cannibalism_warlord_command_scripted_gui` | 17 | Warlord command and recruitment tranches are the densest action surface. |
| `cannibalism_wendigo_counterwar_category` | `:1291`, `:2790` | counterwar or terminal-defender helper; no dedicated GUI | 6 | Counterwar and defender actions can stay visible after route transitions unless the helper closes them. |
| `cannibalism_network_alerts_category` | `:1355` | inbound-route helper; `cannibalism_early_header_scripted_gui` | 2 | Small category, but network list click contract is blocked by GUI parsing. |
| `cannibalism_unified_command_category` | `:1425` | unified-command helper; `cannibalism_revealed_command_scripted_gui` | 5 | First revealed route tranche. |
| `cannibalism_unified_larder_category` | `:1520` | unified-Larder helper; no dedicated GUI | 9 | More than six possible actions. |
| `cannibalism_unified_war_machine_category` | `:1664` | unified-war-machine helper; no dedicated GUI | 14 | Highest unified action density and a source of simultaneous mission pressure. |
| `cannibalism_unified_global_campaign_category` | `:1859` | unified-global-campaign helper; no dedicated GUI | 8 | Campaign and counterwar actions compete for scan attention. |
| `cannibalism_unified_world_end_category` | `:1999` | unified-world-end helper; no dedicated GUI | 2 | Terminal action surface is small but should close cleanly at victory/world-end. |
| `cannibalism_wendigo_command_category` | `:2462` | `cannibalism_wendigo_command_is_open`; `cannibalism_wendigo_command_scripted_gui` | 12 | Terminal, pack, and command actions can exceed six visible primary actions. |

Player-facing values include Larder, Deaths/state population, command integrity, frenzy, field hunger, cell strength, cult cohesion, route alignment, receipts, and mission progress. The source updates these values dynamically, but many cost strings expose raw names without an icon or a concise explanation of cause, threshold, consequence, and response. The fix is not to add more prose; use a meter/state/icon with one threshold tooltip and separate requirement/effect text.

The five direct GUIs are headers, route summaries, network navigation, meters, portraits, and state/target selectors. They do not spend resources, so the action/cost overload comes from the decision categories around them rather than GUI buttons. The current source nevertheless places most map decisions outside the dedicated windows, so the worker must not solve density by adding a new shared GUI or by moving shared log/details surfaces into this scope.

## Mission and timed-objective quality

The mission source has explicit activation flags, cancellation, cleanup, and distinct timeout branches in almost every family. The table records the current owner/category, target context, duration, outcome contract, and duplicate risk.

| Mission ID | Owner/category | Region/target context | Requirement and duration | Success/failure contract | Duplicate/cleanup note |
| --- | --- | --- | --- | --- | --- |
| `cannibalism_maintain_international_inspection_compact` | Country; international response | Country-wide compact vigilance | `cannibalism_compact_vigilance_mission_active`; 365 days | Timeout resolves full, partial, or failure progress; cancels on invalid country/world-end | Auto-watchdog with `available = always no`; `cannibalism_resolve_compact_vigilance` clears state. |
| `cannibalism_restore_supply_corridor_mission` | Country; containment | Primary supply corridor/theater | Logistics active flag and hold-complete trigger; dynamic 63-168-day effective range | Complete success; timeout partial if hold exceeds minimum, otherwise failure; cancels when containment/flag disappears | `cannibalism_clear_logistics_mission` cleans the active flag/progress. |
| `cannibalism_rotate_compromised_formations_mission` | Country; containment | Primary theater formations | Rotation active flag and hold-complete trigger; dynamic 49-133-day effective range | Complete success; timeout partial/failure; cancels when containment/flag disappears | Per-family cleanup exists; short minimum encourages retries. |
| `cannibalism_investigation_mission` | Country; containment objective tranche | Targeted ritual investigation state/cell | Investigation active flag and objective-complete trigger; 120-210 days | Complete or timeout success, partial, or failure; cancels on invalid route/world-end | `cannibalism_clear/complete/partial/fail_investigation_mission` family cleans state. |
| `cannibalism_hold_prison_mission` | Country; containment objective tranche | Targeted prison/holding state | Hold-prison active flag and objective-complete trigger; 120-210 days | Complete or timeout success, partial, or failure; cancels on invalid route/world-end | Per-family cleanup is present; can overlap the investigation family. |
| `cannibalism_reach_island_mission` | Country; international response | Generated island target country/state | Active flag, target identity match, and reach objective; 150-270 days | Complete or timeout success, partial, or failure; cancels on target identity mismatch or route close | Target identity cancellation is good; duplicate target generation still needs scenario evidence. |
| `cannibalism_break_network_mission` | Country; international response | Generated network target country/state | Active flag, target identity match, and break objective; 150-240 days | Complete or timeout success, partial, or failure; cancels on target mismatch or route close | Target mismatch cancellation prevents stale targets; retain it in cleanup review. |
| `cannibalism_stop_unification_mission` | Country; international response | Unified-route target | Active flag, route-open check, target identity, and hold objective; 60-210 days | Complete or timeout success, partial, or failure; cancels after reveal/target mismatch | The short lower bound can create a retry loop if route progress is not persistent. |
| `cannibalism_stop_transformation_mission` | Country; Warlord command | Transformation route target | Active flag and transformation objective; 120-240 days | Complete or timeout success, partial, or failure; cancels when route/target closes | Verify the Warlord route closes this mission on capitulation and world-end. |
| `cannibalism_unified_command_mission` | Unified country; unified command | Unified command operation | Active flag and unified objective trigger; 120 days | Complete success; timeout partial/failure; cancels when unified decisions close | Independent recorder can coexist with the other three unified missions. |
| `cannibalism_unified_larder_mission` | Unified country; unified Larder | Larder operation | Active flag and Larder objective trigger; 150 days | Complete success; timeout partial/failure; cancels when unified decisions close | Independent recorder and cleanup helper. |
| `cannibalism_unified_war_machine_mission` | Unified country; unified war machine | War-machine operation | Active flag and war-machine objective trigger; 150 days | Complete success; timeout partial/failure; cancels when unified decisions close | Independent recorder and cleanup helper. |
| `cannibalism_unified_counterwar_mission` | Unified country; unified global campaign | Counterwar operation | Active flag and counterwar objective trigger; 120 days | Complete success; timeout partial/failure; cancels when unified decisions close | Independent recorder and cleanup helper; contributes to the concurrency issue. |
| `cannibalism_wendigo_terminal_hunt_mission` | Wendigo country; Wendigo command | Terminal hunt target/route | Active flag, success `available` trigger, and failure `cancel_trigger`; 120 days | Success on objective, failure on cancel/timeout; no partial branch | Cleanup is present, but shared `Wendigo Pack` template availability must be verified before route exposure. |

The source has central cleanup effects that remove active missions and family progress, and the unified record helpers guard duplicate activation per family. The unresolved issue is not stale-flag cleanup in the normal paths; it is simultaneous presentation and route-transition proof across all families.

## Cost and requirement audit

The audit counted distinct paid inputs in the decision cost contracts and checked whether the corresponding localisation string is icon-first. Every gameplay-changing decision must have no more than four distinct spendable types, and every spendable value must use a registered texticon.

| Surface | Current result | Required treatment |
| --- | --- | --- |
| Early ration/logistics/rotation/forensics/burial/terror rows around localisation lines 42-106 | Several rows are icon-first, but trial, amnesty, and prisoner-feed rows mix counters or requirements into the cost line | Separate requirement text and register/use an icon for custom ledger values. |
| Warlord command/recruitment rows around lines 2058-2438 and localisation lines 541-633 | Mostly literal labels; equipment and route requirements are mixed with Larder/population costs | Split consumed costs from equipment/route/reserve requirements and rewrite icon-first. |
| Unified rows around lines 1434-2024 and localisation lines 1543-1726 | Mostly literal labels; seven rows exceed four spendables | Reduce each over-budget contract and convert every remaining paid input to texticons. |
| Wendigo rows around lines 2472-2851 and localisation lines 1793-2081 | Many literal labels; press and muster exceed four spendables | Reduce/split and use icon-first paid-cost plus separate receipt/target requirements. |
| Five scripted GUI windows | Zero spendable controls | No GUI cost redesign is required; preserve view-only semantics. |

Equipment reserve, unit availability, target ownership, route flags, and death-receipt counters are often valid non-consumed requirements. They should not be printed as if they are paid costs, and they should not be hidden as a fifth cost in a secondary tooltip or effect description.

## AI validity, route locks, and custom-unit acquisition

Sampled decisions have `ai_will_do` blocks, and the Warlord, unified, and Wendigo decision families use route and target checks rather than blindly targeting dead countries. `cannibalism_warlord_command_is_open` requires the route, country existence, non-capitulation, non-world-end, and cleanup conditions. Unified target triggers check the owning/control country, subject/war/capitulation state, route flags, target identity, equipment, and Larder gates. Network GUI actions are view-only and do not bypass these decision triggers.

The Warlord recruitment transaction consumes exact state Deaths population and Larder, grants a bounded manpower conversion, creates a route-selected template, and applies a state recruitment cooldown. The generated Event-014 templates include Scavenger Warband, Feast Cohort, Bone Guard, Bone Riders, Scavenged Elephant Column, Network Cadre, Island Reavers, Siege Eaters, and March Predation Column. Template creation locks normal recruitment, and cleanup deletes the dynamic templates and clears route flags. Equipment reserve is generally a requirement rather than a consumed input, which must be stated clearly in the cost tooltip.

The unified recruitment transaction follows the same exact Deaths/Larder/manpower contract, creates route-selected Cannibal Legion, Bone Guard, Bone Riders, Scavenged Elephant, Island Reavers, Siege Eaters, or March Predation units, consumes the specialist route flags where applicable, applies a state cooldown, and records the War Machine mission. This route-lock behavior is structurally sound but still needs the cost/requirement split described above.

Wendigo acquisition checks the command route, receipt flags, receipt cooldown, Larder/population/equipment requirements, and `has_template = "Wendigo Pack"`, then spawns an empty `Wendigo Pack` batch and records the count. The template is shared rather than Event-014-owned, so the route must remain closed or show a clear blocked reason when that inherited template is absent; verify this dependency in the parent-owned runtime setup.

The direct `hoi4.probability_inspect` call for `common/decisions/014_cannibalism_decisions.txt` with adapter `decision_ai_will_do` succeeded as source discovery only: 95 candidates, 0 available scenario candidates, 32 required inputs, and 0 unresolved values. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3b2882e24c21f9e689c5d18a2be81307966d9e129d291a4101936407a1ec505/d45b363043e4136b876d59be2af8432591cff4f9906fbb23895dd92efdccb85c4/probability-inspect-f0e56bfe94bb.json`.

The required named `chaosx_ai_probability_auditor` route was not callable in this subagent context, and the direct `ai_strategy_factor` inspect for `common/ai_strategy/014_cannibalism_warlords.txt` timed out after 180 seconds. No scenario-specific AI balance conclusion is claimed. The parent must route the complex decision and strategy weights through the named auditor and run a same-scenario probability compare before changing weights.

## Localisation and tooltip gaps

Most ordinary decisions have `custom_cost_text`, `custom_effect_tooltip`, and an AI weight, which is positive. Remaining gaps are clarity and separation rather than a missing key on every decision.

The Warlord and unified custom-cost strings are long comma-separated rows with literal resource names, `and`, `plus`, and route prose. They force players to parse paid values, requirements, target conditions, and reserve checks in one line. Replace them with a concise icon-first cost line, a concise requirement tooltip, and an effect tooltip that names the unit, consumed ledger amount, cooldown, and route consequence.

The custom GUI localisations should retain short dynamic labels for current tab, selected target, meters, and mission state. Long dynamic numbers should have one cause/threshold/consequence tooltip rather than repeated prose. The network entry tooltip must state that clicking selects a target and does not spend a resource.

## Cleanup and exploit-risk notes

Normal mission families clear active flags, progress, durations, and target variables through family-specific helpers. Global cleanup effects remove active missions at `common/scripted_effects/014_cannibalism_effects.txt:3305-3318`, and route-close cancellation is present on most unified and objective missions. These are strengths to preserve.

The emergency workshop recovery loop is the only high-confidence exploit found in this pass. Other recruitment paths create empty units with zero start equipment/manpower and use equipment as a requirement, so they are not automatically equipment farms, but their tooltip must distinguish reserve checks from consumption.

Network selection effects only rebuild arrays, set selected country/state values, mark the GUI dirty, and open/close the view. They do not directly execute a gameplay decision. The parser failure still blocks the intended selection UX.

## Event-014-owned GUI inventory and MCP evidence

| Window | Scripted GUI | Context/entry | Geometry | Static controls or dynamic surface |
| --- | --- | --- | --- | --- |
| `cannibalism_early_header_window` | `cannibalism_early_header_scripted_gui` | decision category | 470x304 | Header/open control, warning/cult animation, no spend control. |
| `cannibalism_network_window` | `cannibalism_network_scripted_gui` | player context, `top_bar` parent | 860x620 | Close, five tabs, sort, refresh, country/state entry selectors, selected-target panel. |
| `cannibalism_warlord_command_window` | `cannibalism_warlord_command_scripted_gui` | decision category | 470x340 | Meters, route/larder/frenzy information, animated portrait/seal, no spend control. |
| `cannibalism_revealed_command_window` | `cannibalism_revealed_command_scripted_gui` | decision category | 470x380 | Animated portrait/seal/terminal information, no spend control. |
| `cannibalism_wendigo_command_window` | `cannibalism_wendigo_command_scripted_gui` | decision category | 470x400 | Animated portrait/anchors/terminal information, no spend control. |

Historical post-inspect artifacts exist for all five windows: early `.../artifact/08945af4664acdcd4f472b24f4079de70b7fd0d0f10d739f25962cf0b6ffb21a/9380c599e7070b01ecb1e978e844f3151346e48c840c8909485c04493835d72a/gui-inspect.efcc30d8957daab7.json`, network `.../artifact/338663721720fc06eb56d6fc53874049897ced5438ebb8b0c72cff7b60088592/09008dfb9cf897573387ffddb2eeca3a31bf1483af71f866e52b74c67e4adc6d/gui-inspect.1cbde0fb94521db9.json`, Warlord `.../artifact/36b15c40448ca90b7d26719653d683c95009ebea20442e92cd15b9cc37509236/8f702db897977f910618da0fb16e04cfee9c4a44d880b564debdabcbfec5ef3a/gui-inspect.e2c89ef80971fc61.json`, Revealed `.../artifact/b348cc69cb33aa05d8c43c90dcef988d2ad28acdf868548482e0df739f69406d/0bc3300bd2407d3932dfd776d358644a4ebb5168b324d1da3850d486b1a95c76/gui-inspect.f2c61ea8d7a79ad4.json`, and Wendigo `.../artifact/40bb57feeaa7a6f212a73acd97889e268a210df9524920ef56c5db2a23d32e8c/7717c9f189ba80ed9c24465b9ba900189310543130ef0e3896f64af8380a4479/gui-inspect.4002fcc2a0f0c76e.json`.

Historical pre-change full-window render artifacts exist for early `.../artifact/adec1d803e99ab49ecbee29f74f0268658d5b63fa7a5921be4f8da974d88d826/d862a3241106d8be28ce9cba704791dcb767b08d7ad01f3190dc962d7bac1fba/cannibalism_early_header_window-full.svg`, network `.../artifact/a0583bafca6d3c2b2b428f5660917aaa421b493fd0e375a8f82465af86b748d0/e48639254e14c53e16ea15a7a5555465d2d9432e5cb8b10fc4c66ace379466d8/cannibalism_network_window-full.svg`, Revealed `.../artifact/9c26360404c9cbefabffdc40760683904f83e6a0c824d8b2573c19b572176615/5244aff159524fac6ae57ae00dac9f42b47b0bd69855965462161a3e51323b0a/cannibalism_revealed_command_window-full.svg`, and Wendigo `.../artifact/f42ed1c98dea41b4de72a1824f77675e196afeabc744bbe2eba832f01b2cf506/35ea23c1dfdbc0e4685a5361c42b07fe9b750e5236d2867f52dd22f74c0055d3/cannibalism_wendigo_command_window-full.svg`.

Current MCP blocker: a fresh `hoi4.gui_inspect` for `cannibalism_early_header_window` with scenario `event014_early` timed out awaiting `tools/call` after 180 seconds. A fresh `hoi4.gui_render` for `cannibalism_warlord_command_window`, state `normal`, resolution 1920x1080, scenario `event014_warlord_current_layout_recheck_2026_08_24`, timed out after 180 seconds. Prior current/post-change multi-state render calls also timed out or returned `ARTIFACT_STORAGE_LIMIT`, and the four-resolution retry returned zero artifacts. Do not treat this as visual pass evidence.

`hoi4.gui_rewrite` was not used because this is an audit-only handoff and Event-014 GUI files are concurrently active. A prior rewrite attempt in the shared workspace was blocked by unrelated Event-003/Event-005 collisions and graph truncation; it made no source change. The next owner must use `chaosx_event_ui_worker` for the dedicated network layout only and must not touch shared windows or frameworks.

## Concrete recommended fixes

1. `chaosx_event_ui_worker`: repair the two network entry button definitions in `interface/014_cannibalism_frontline_hunger.gui`, then rerun current inspect/render evidence for all five owned windows, including click regions, bounds, hover, selected, disabled, warning, empty, active/completed, long-text, and all supported resolutions.
2. Decision owner: reduce the seven over-budget decisions listed above to no more than four paid inputs, and keep route, target, reserve, equipment-held, and receipt gates in a separate requirement tooltip.
3. Localisation owner: rewrite Event-014 cost strings in `localisation/english/014_cannibalism_l_english.yml` to use registered texticons for every spendable value, create valid icon-first presentation for Larder/population/receipt values, and remove filler prose.
4. Gameplay owner: resolve the emergency workshop recovery contradiction in `common/scripted_effects/014_cannibalism_effects.txt:16589-16593` and align `cannibalism_emergency_reinforcement_effect_tt` with the actual transaction.
5. Decision owner: phase or merge dense category tranches and hide empty rows where possible; keep no more than six visible primary actions in a category and no more than three simultaneous active missions without a clear staged objective presentation.
6. Mission owner: verify the compact watchdog's permanently unavailable completion contract, decide whether logistics/rotation minimums are intentionally urgent, and preserve full/partial/failure/cancel cleanup semantics.
7. AI owner: route every complex decision and strategy weight through `chaosx_ai_probability_auditor`, perform baseline and same-scenario compare, and record unresolved target/AI inputs before tuning.
8. Wendigo route owner: prove that the inherited `Wendigo Pack` template is registered before opening the acquisition decisions, and keep the route locked with a clear blocked tooltip when it is absent.

## Changed files and behavior

Changed files: only this report, `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_decision_gui_audit_2026-08-24.md`.

Changed identifiers: none in gameplay, localisation, interface, scripted GUI, scripted effects, triggers, missions, or AI strategy files.

Before/after behavior: none; this was a read-only audit. The report intentionally leaves all identified fixes for the parent/owned workers because Event-014 source files are concurrently active.

## Validation and remaining blockers

Meaningful validation completed: scoped source review of Event-014 decisions, categories, missions, scripted effects, scripted GUIs, interface geometry, localisation, constants, unit templates, AI strategy, the captured prelaunch parser log, the required offline wiki pages, and vanilla documentation; direct decision probability source inspection; historical GUI artifact review; and current GUI MCP timeout capture.

Skipped validation: current five-window GUI inspect/render state and resolution matrix, GUI rewrite/post-change comparison, and named AI probability-auditor compare remain blocked by the MCP timeouts, artifact storage failure, concurrent-source audit-only constraint, and unavailable named auditor route. No live HOI4 launch was performed.

Remaining issues: the network parser/hitbox blocker, seven over-budget costs, literal/mixed cost localisation, emergency recovery contradiction, category and mission cognitive load, mission timing/watchdog decisions, current visual evidence gap, animation fallback resilience, and unresolved probability scenarios listed above.

Handoff path: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_decision_gui_audit_2026-08-24.md`.
