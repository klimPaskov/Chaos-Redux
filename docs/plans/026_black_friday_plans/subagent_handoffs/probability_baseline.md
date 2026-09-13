# Event 26 Black Friday probability baseline

Status: incomplete and unresolved at the engine-evidence layer because the required HOI4 MCP routes are unavailable.

Audit snapshot: 2026-08-29, stable tracked source revision `0292312f9` (`Record Event 006 patron cost fix`).

The repository changed concurrently during this audit, including in-progress Event 26 and universal-cost files and later commits, so those changes were excluded from the baseline and no before/after comparison was run.

Only this handoff file is written by this audit; gameplay, AI, event, decision, mission, constant, and framework files were not edited.

## MCP evidence boundary

The required first probability operation was `hoi4.probability_inspect`; its route was checked and found unavailable.

No callable `hoi4_agent_tools` route is exposed in this environment for `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, or `hoi4.probability_render`.

The fully qualified route probes `mcp__hoi4_agent_tools__hoi4_probability_inspect`, `mcp__hoi4_agent_tools__hoi4_probability_evaluate`, `mcp__hoi4_agent_tools__hoi4_probability_sweep`, `mcp__hoi4_agent_tools__hoi4_probability_compare`, and `mcp__hoi4_agent_tools__hoi4_probability_render` were unavailable.

The structural routes `hoi4.event_inspect` and `hoi4.event_render` are also unavailable.

The corresponding structural route probes `mcp__hoi4_agent_tools__hoi4_event_inspect` and `mcp__hoi4_agent_tools__hoi4_event_render` were unavailable.

No analyzer revision, scenario hash, artifact URI, comparison id, rendered evidence path, or engine result exists for this audit.

All scenario-level probability, timing, ranking, dominance, starvation, rank-reversal, and repetition conclusions below are therefore `unresolved`, not exact, bounded, or sampled results.

The source findings marked `source-only` describe implementation inputs and do not substitute for MCP probability evidence.

## Audited Event 26 and event-pool surfaces

| Surface | Stable source and identifiers | Baseline observation | Classification |
| --- | --- | --- | --- |
| Event 26 entry | `events\026_industry_to_desert.txt:1-36`, namespace `chaosx.nr26`, root `chaosx.nr26.1` | The old desert event is hidden and `is_triggered_only`; its first option routes the owner or a random eligible country through desert-state logic before `chaosx.nr26.2`. No Black Friday reservation, Friday activation, sale snapshot, or expiry state exists. | source-only; engine availability unresolved |
| Event 26 option race | `events\026_industry_to_desert.txt:44-55`, `:101-106` | The old follow-up has `ai_chance = { base = 100 }` for the first option and `ai_chance = { base = 0 }` for the second option. This is an event-option proportional sampling surface, not an Event 26 picker weight or an `ai_will_do` score. | source-only; option result unresolved |
| Registration and base weight | `common\scripted_effects\chaosx_logic_effects.txt:224-327`, Event 26 at `:249`; `common\scripted_effects\chaosx_logic_effects.txt:365-398`; `common\script_constants\event_system_constants.txt:33-43` | Event 26 is registered in `global.fire_once_events`; the generic registry initializes non-major event weights to `constant:event_system_defaults.event_weight`, which is 1000. There is no Event-26-specific automatic weight or MTTH entry in the stable baseline. | source-only score input; normalized selection probability unresolved |
| Candidate pool construction | `common\scripted_effects\chaosx_logic_effects.txt:328-347` | `global.all_events` is assembled from the registered major, fire-once, and repeatable arrays. The source pool is complete relative to those registries, but valid candidates still depend on disabled flags, fired state, chaos, filter, and dynamic unavailability. | source-only pool shape; complete runtime candidate pool unresolved |
| Default availability | `common\scripted_effects\chaosx_logic_effects.txt:349-363`; `common\scripted_triggers\chaosx_settings_triggers.txt:10-33` | Event 26 is absent from the default-enabled rework allowlist. The initialization path therefore treats it as default-disabled when the rework queue is initialized. | source-only; runtime initialization effect unresolved |
| Chaos gate | `common\scripted_effects\chaosx_logic_effects.txt:156-202`; `common\scripted_triggers\chaosx_settings_triggers.txt:344-388`; `common\script_constants\chaos_meter_constants.txt:8-40` | The stable registry gives unqualified events the default tier 0, while the tier tables define tier 1 at 200 chaos. Event 26 has no source-specific 200-chaos gate in this revision. | source-only; Event 26 availability unresolved |
| Automatic timer selection | `common\on_actions\chaosx_on_actions_system.txt:132-156`; `common\scripted_effects\chaosx_logic_effects.txt:404-502` | On the daily system hook, a zero timer selects through `select_weighted_random_event_id` and dispatches the selected id. The timer is recalculated by generic pacing logic. There is no pending reservation or first-eligible-Friday activation path. | source-only timing path; timing distribution unresolved |
| Weighted picker | `common\scripted_effects\chaosx_settings_effects.txt:4329-4442` | The picker evaluates every `global.all_events` member, applies current filter and validity, scales valid weights, sums them, rolls an integer in the total, and selects the first cumulative weight crossing the roll. This is weight-proportional sampling over the valid pool. | source-only algorithm; probability unresolved |
| Active-pool validity | `common\scripted_effects\chaosx_logic_effects.txt:581-614`, `:821-918` | Central checks cover disabled events, already-fired non-repeatables, and dynamic unavailability including unmet chaos. No Event-26 reservation, pending, sale-active, terminal, or Friday-specific check exists in the stable baseline. | source-only; validity result unresolved |
| Fire-once dispatch | `common\scripted_effects\chaosx_logic_effects.txt:1086-1110`; generic dispatch at `common\scripted_effects\chaosx_settings_effects.txt:4789-4823` | Fire-once accounting occurs immediately when the event is dispatched, adds the id to `global.fired_events`, and invokes minor pacing outside cluster context. The handler comment says weight is set to zero, but the code writes `new_weight = 1`; fired-state exclusion still removes the event from the natural pool. This is incompatible with reservation-without-history until activation unless the new lifecycle deliberately separates reservation from dispatch. | source-only lifecycle risk; repetition and pacing effects unresolved |
| Normal manual path | `common\scripted_effects\chaosx_settings_effects.txt:1641-1705`, `:1758-1781`; event-details path `common\scripted_effects\chaosx_events_log_effects.txt:1509-1520` | Normal manual triggering checks force/bypass state, event type, required chaos, and fired state before dispatch. The event-details opener also checks the central chaos gate. No Black Friday quote or pending-state path is present. | source-only; manual availability unresolved |
| Forced path | `common\scripted_effects\chaosx_settings_effects.txt:1707-1732` | `force_trigger_selected_event` sets `temp_bypass_checks` and dispatches without the normal fired/availability checks. Forced selection is not evidence of natural selection and must remain explicitly distinct from the sale reservation path. | source-only; forced result unresolved |

The baseline therefore has a fire-once registration and generic weight, but no implemented Black Friday candidate, reservation, activation, or universal affordability surface.

## Named Black Friday AI scenarios

The following are the required scenario ids from `docs\specs\026_black_friday_specs\026_black_friday_spec_part_5_ai_multiplayer_balance_and_exploit_controls.md:33-50` and `026_black_friday_spec_part_8_acceptance_scenarios.md:121-125`.

| Scenario | Required question | Candidate pool and external factors | Baseline result |
| --- | --- | --- | --- |
| `bf_ai_01_low_reserve_advisor` | An advisor is affordable only at the sale price but post-payment would breach the protected political-power reserve. | Requires all advisor candidates, final quote, PP reserve policy, current PP, active sale state, strategy factors, and route/availability gates. | unresolved; `probability_inspect`/`probability_evaluate` unavailable |
| `bf_ai_02_valid_law_change` | A valid desired law becomes affordable and should compete above unaffordable alternatives. | Requires the complete law candidate pool, law prerequisites, current PP, final discounted quote, reserve floor, strategy factors, and cooldown/state gates. | unresolved; no score or probability ranking observed |
| `bf_ai_03_wartime_command` | A valid command ability becomes cheaper during an active battle while existing tactical logic remains decisive. | Requires all command-ability candidates, battle state, command-power/PP resources, tactical modifiers, target validity, cooldowns, and sale snapshot. | unresolved; no score or selection probability observed |
| `bf_ai_04_invalid_target` | A cheap foreign action has no valid target and must retain zero effective weight. | Requires the complete foreign-action pool, target-country validity, diplomatic/route gates, resource quote, and external strategy factors. | unresolved; zero-weight behavior not engine-tested |
| `bf_ai_05_static_variant_pool` | Normal and discounted records must not double-count one logical action; only the active record may be eligible. | Requires the complete normal/50-percent/75-percent record pool, active-sale state, record identity, and all action availability gates. | unresolved; no candidate-normalization evidence |
| `bf_ai_06_overlapping_discount` | A second active source may compose with the sale while keeping ranking explainable. | Requires the complete candidate pool, ordered source composition, source caps, final quantizer, and all resources/reserve policies. | unresolved; no sensitivity or rank result |
| `bf_ai_07_sale_expiry` | An action considered before expiry but taken after expiry must recheck ordinary price and reserve. | Requires click/confirmation timing, expiry tick, quote recomputation, current resources, candidate validity, and cooldown/route state. | unresolved; no timing sequence or transaction evidence |
| `bf_ai_08_75_percent_high_chaos` | At 600 or more chaos, the stronger discount may make more actions affordable without bypassing safety rules. | Requires the complete candidate pool, chaos transition schedule, Evolution I flag, 75-percent ratio, reserve/cooldown/route gates, and strategy factors. | unresolved; no threshold sweep or rank reversal evidence |

These rows are scenario contracts, not observed outcomes. The required MCP call sequence could not be executed, so no scenario is classified as exact, bounded, sampled, or score-only.

## BF-R and BF-X coverage boundary

`BF-R01` through `BF-R13` in `026_black_friday_spec_part_8_acceptance_scenarios.md:46-60` are quote, quantization, and family-cost cases, not selection probabilities. Their expected examples include zero remaining zero, positive costs retaining a minimum quantum, and upward quantization for 50-percent and 75-percent prices, but no universal-cost implementation exists at the stable baseline and no MCP quote adapter was available, so all are skipped as engine checks and remain unresolved.

`BF-X01`, `BF-X02`, `BF-X03`, `BF-X04`, `BF-X05`, `BF-X06`, `BF-X07`, `BF-X08`, `BF-X09`, `BF-X10`, `BF-X11`, `BF-X12`, `BF-X13`, and `BF-X14` in `026_black_friday_spec_part_8_acceptance_scenarios.md:75-90` require transaction state, expiry timing, static candidate identity, multi-resource composition, refund state, save/reload persistence, achievement-family routing, or payer isolation. No stable baseline surface implements those Black Friday states and no event or probability MCP route was callable, so they were not simulated or treated as passed.

`probability_sequence` was not used because there is no complete declared custom pool, cadence, state-transition schedule, or terminal-state implementation in the stable baseline.

`probability_simulate` was not used because no explicit uncertain input was declared and the required probability adapter is unavailable.

`probability_sweep`, `probability_render`, and `probability_compare` were not used because the required analyzer route is unavailable and no before/after patch comparison is authorized by this baseline task.

## Decision and mission AI affordability inventory

The stable tracked revision has no `common\missions` directory; missions are embedded in decision files with `selectable_mission = yes`.

A mechanical source scan found 100 tracked decision files containing both cost-related fields and `ai_will_do`, 28 `selectable_mission = yes` entries, and approximately 3,125 textual `ai_will_do` matches. These are discovery counts, not normalized candidate counts or probability results.

The exact selectable mission identifiers found were:

- `independence_wave_establish_revenue_service`, `independence_wave_hold_first_assembly`, `independence_wave_confirm_traditional_authority`, `independence_wave_establish_treasury_and_currency`, `independence_wave_build_permanent_foreign_service`, `independence_wave_integrate_militias`, `independence_wave_form_border_guards`, `independence_wave_professionalize_army`, `independence_wave_prepare_reclamation_defense`, `independence_wave_balance_patrons`, `independence_wave_convene_founding_congress`, `independence_wave_challenge_league_leadership`, `independence_wave_convene_formation_congress`, `independence_wave_coordinate_reclamation_fronts`, and `independence_wave_transform_league_charter` in `common\decisions\006_independence_wave_decisions.txt` at `:84-128`, `:212-250`, `:269-307`, `:489-527`, `:841-869`, `:3500-3822`.
- `independence_wave_form03_ratify_confederal_charter` in `common\decisions\006_independence_wave_form03_decisions.txt:596`.
- `independence_wave_rival_bloc_commit_shared_reserve` and `independence_wave_rival_bloc_challenge_leadership` in `common\decisions\006_independence_wave_shared_decisions.txt:367` and `:448`.
- `black_plague_shared_emergency_countermeasure_drive` in `common\decisions\020_black_plague_shared_response_decisions.txt:27`.
- `fallout_event_100_ration_law`, `fallout_event_100_first_hunger_mission`, `fallout_nzl_wellington_breakwater_works`, `fallout_nzl_auckland_storm_port_works`, `fallout_nzl_milk_rail_assignments`, `fallout_nzl_port_militia_training_mission`, `fallout_nzl_convoy_volunteer_corps_mission`, `fallout_nzl_refugee_fleet_admission`, and `fallout_nzl_offer_rescue_passage` in `common\decisions\fallout_consolidated_decisions.txt:1171-1819`.

Representative cost and AI surfaces for the universal framework are:

| Family | Stable source evidence | Audit implication |
| --- | --- | --- |
| Political power plus command power custom costs | `common\decisions\001_communism_spread_decisions.txt:7-12`, `:28`, `:65-68`, `:124`, `:318-341` | `custom_cost_text`, `ai_hint_pp_cost`, custom affordability triggers, and `ai_will_do` coexist; the displayed hint cannot be treated as a payment or a click probability. |
| Factory-commitment selectable missions | `common\decisions\006_independence_wave_decisions.txt:84-128`, `:212-250`, `:489-527`, `:841-869` | Availability and custom cost triggers use dynamic administration/factory obligations while AI uses separate willingness scores; the final quote must be recomputed without dropping mission, route, or cooldown constraints. |
| Equipment, train, manpower, and XP obligations | `common\decisions\019_infantry_spawn_decisions.txt:77-104`, `:106-128`, `:129-168`, `:172-189` | A single action can have multiple resource obligations and hidden state; affordability must be all-or-nothing and the sale cannot create positive weight for unresolved or invalid lot targets. |
| Native PP purchase | `common\decisions\092_greenland_sale_decisions.txt:8-22` | The decision has `cost = 250` and an `ai_will_do` factor with war and PP modifiers but no matching explicit PP availability gate in the block; this is a candidate for an engine affordability/score audit, not proof that the AI can click it. |
| Zero and nonzero doctrine decisions | `common\decisions\cbrn_doctrine_decisions.txt:18-34`, `:58-85`, `:264-355` | Native zero-cost entries, mixed PP/command-power costs, custom cost triggers, and AI weights occur in the same subsystem; family registration must not apply a sale to requirements, rewards, penalties, or cooldowns. |
| Fallout multi-resource missions | `common\decisions\fallout_consolidated_decisions.txt:1171-1283`, `:1304-1475`, `:1582-1773` | Mission costs may combine PP, equipment, manpower, and state-specific obligations, so quote composition and target validity need per-action registry entries. |

No stable tracked decision or mission call site is wired to a universal Black Friday quote, affordability, payment, or AI-cost adjustment API. The 100-file intersection and 28 mission entries therefore identify the required owner inventory only; they do not provide complete pools for probability normalization.

## Findings and recommended owner fixes

1. Add an Event 26 availability gate requiring the intended 200-chaos threshold, default-enabled status, unfired state, no reservation/active/terminal conflict, and all ordinary event validity checks.
2. Add a reservation state that is excluded from the natural event pool and does not write fired history, event pressure, or timer pacing until Friday activation.
3. Add a bounded Friday activation and next-tick expiry path that snapshots the tier and discount ratio, handles same-day chaos changes according to the specification, and cleans up pending and active state idempotently.
4. Route normal manual selection through the same reservation/activation contract, while keeping forced selection explicitly separate and preventing forced bypass from being counted as natural selection evidence.
5. Build the universal registry from the complete cost-family inventory, including all PP, command power, equipment, fuel, manpower, XP, factory, advisor, law, doctrine, technology, operation, license, production, project, and mixed-resource actions reachable through ordinary voluntary purchases.
6. Make AI affordability consume the final quote and preserve reserve floors, valid targets, route gates, tactical logic, and cooldowns; set invalid candidates to zero rather than increasing a stale score because a sale is active.
7. Represent normal, 50-percent, and 75-percent variants as one logical action and expose only the active record to AI and selection normalization.
8. Preserve one payment/refund transaction for mixed-resource actions and recompute at confirmation where the specification requires it, while retaining the quoted price for explicitly upfront-paid delayed projects.
9. Review the fire-once handler’s comment/code mismatch at `common\scripted_effects\chaosx_logic_effects.txt:1098-1099`; do not rely on raw weight `1` as the sale lifecycle marker because fired-state exclusion, not zero weight, controls natural eligibility.
10. Preserve unrelated consumers of the old desert news art during Event 26 replacement; `GFX_news_desert` is also consumed by Event 40 in `events\_chaosx_news.txt` around `:650-665` in the stable baseline.

## Unresolved risks and skipped analyses

- Natural Event 26 starvation is plausible because the stable source omits it from the default-enabled allowlist, but runtime availability was not proven without the MCP adapter.
- If Event 26 is merely enabled with the generic tier-0 gate and weight 1000, it has no measured rank relative to the rest of the valid pool and no proven 200-chaos threshold.
- Dominance, starvation after discount activation, rank reversals, threshold sensitivity, timing drift, repetition, and reserve exploitation were not measured.
- The old `ai_chance` 100/0 option pair is not evidence for event-pool selection or AI affordability.
- Forced unweighted selection intentionally bypasses ordinary validity checks and cannot validate natural event balance.
- No exact cost, normalized probability, timing distribution, score race, or transaction result is claimed.
- Structural event inspection/rendering, probability inspection/evaluation/sweep/rendering, sequence analysis, simulation, and before/after comparison were skipped for the exact route blockers stated above.
- Live HOI4 execution was not attempted because live validation belongs to the user.

## References read

- Event 26 specification package: `docs\specs\026_black_friday_specs\README.md`, `026_black_friday_goal_prompt.md`, parts 1-9, cost-surface registry template, source-reading record, subagent review record, improvement-loop closure, and package manifest.
- Offline Paradox wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Vanilla documentation: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `script_math_functions.md`, `dynamic_variables_documentation.md`, and `common\script_constants\documentation.md`.

This handoff is a read-only baseline report with MCP evidence unavailable; it is not a balance approval and does not claim Event 26 implementation completion.
