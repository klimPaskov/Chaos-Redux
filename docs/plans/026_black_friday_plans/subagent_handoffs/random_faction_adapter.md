# Event 26 Black Friday: Random Faction owner adapter handoff

Current-status note (2026-09-02): the earlier static liaison disposition in this historical handoff is superseded by `random_faction_liaison_adapter.md`. All ten paid Random Faction actions now have bounded active-sale source adapters; the counts below that describe nine adapted actions and one static exception are retained as historical audit context only.

Date: 2026-09-02.

Scope: the Random Faction owner tranche for Event 26 Black Friday only.

The owner files are Event 17 sources, while the sale source and universal transaction helpers remain in the existing Event 26 framework and were not edited.

## Disposition summary

Ten Random Faction actions use the shared quote, payment, receipt, achievement, and settlement path during an active sale.

`random_faction_request_liaison` was previously recorded as a complete truthful static full-price variant because its command power cost is paid by the decision owner while its support-equipment cost is paid by the selected faction leader in `FROM`. That disposition is superseded by the bounded two-payer adapter in `random_faction_liaison_adapter.md`, which keeps one payer-scoped receipt in each country and settles both before the owner outcome runs.

The two Random Faction missions are unpaid objectives, so neither receives a Black Friday payment adapter.

No Event 26 helper file was edited and no dedicated scripted GUI was added.

## Severity-sorted issue list

### High

No high-severity source issue was found in the bounded Random Faction payment surface.

### Medium

- `random_faction_request_liaison` is covered by the parent-approved payer-scoped two-country adapter; see `random_faction_liaison_adapter.md` for the exact receipt and refund contract.
- The required `chaosx_decision_mission_auditor` read-only audit did not return a final status during a 120-second bounded wait, so its review remains unresolved; the probability auditor later returned a source-level and MCP comparison report, recorded below.
- The mandatory read-only GUI evidence for the ordinary `countrydecisionview` found shared-surface diagnostics including `GUI_ACCIDENTAL_CLIPPING`, several `GUI_INVALID_SIZE` entries, and unsupported texture or scroll properties; the diagnostics are not treated as renderer-only, but the shared GUI files are outside this owner write scope and were left unchanged.

### Low

- The owner natively debits `support_equipment_1`, `infantry_equipment_1`, and `convoy_1`, while the universal framework exposes exact `support_equipment_1` and generic `infantry_equipment` and `convoy` resource kinds; the adapter follows the existing framework mappings, with support exact and infantry or convoy using the framework's base-kind mapping to the native level-one stockpile.
- If the Event 26 source cache is unavailable while `black_friday_is_active` is true, each adapted action is rejected rather than silently falling back to a full-price debit; this is the safe engine-inaccessible disposition for an active sale.

## Decision category lifecycle notes

The shared category is `random_faction_bloc_pressure_category` and the production surface is the ordinary `countrydecisionview`; no layout or interface source changed.

The ten adapted decisions use the matching `random_faction_black_friday_can_pay_*_cost` wrapper for both availability and `custom_cost_trigger`, so the visible quote and the payment preflight come from the same Event 26 source snapshot.

On completion, each adapted decision calls its matching `random_faction_black_friday_pay_*` adapter and invokes the unchanged original decision effect only when `black_friday_owner_payment_succeeded = yes`.

When Black Friday is inactive, each adapter reports success without touching the ledger and the unchanged original payment helpers execute at full price.

When Black Friday is active, each adapter allocates one owner transaction, quotes every positive component with `universal_cost_quote_integer`, preflights all components, pays exact quoted amounts, records one component row per resource, settles the receipt, and records one primary achievement family.

Fixed rewards, penalties, durations, target effects, route locks, requirements, and cooldowns remain outside the quote and retain the original source behavior.

The adapter markers and payment result are temporary variables only; no persistent flag or daily scan was added and no new cleanup hook is required.

## Cognitive-load notes

The category is phase-gated by `random_faction_newly_aligned_minor_decisions_visible`, `random_faction_pressured_neutral_decisions_visible`, and `random_faction_faction_leader_decisions_visible`, so the source category does not expose all ten decisions simultaneously.

The newly aligned phase exposes at most stabilize, request liaison, and quiet opposition, with the existing alignment flags reducing the set as actions are taken.

The pressured-neutral phase exposes council, observer, and neutrality-press actions, with the border-post mission replacing the council action after activation.

The faction-leader phase exposes staff mission, radio networks, corridor, and commitment actions, with the corridor mission appearing after launch.

The active phase surfaces therefore remain below six primary actions and the tranche adds no primary action, tab, or category.

All adapted spendable values are now icon-first and quote-backed, and each displayed component identifies its resource, amount, and sale-state affordability.

Fixed stability or war-support consequences are described as strain rather than being presented as spendable sale components.

The stabilization cost remains dynamically tied to the existing country-size variables `random_faction_stabilize_pp_cost`, `random_faction_stabilize_support_cost`, and optional wartime `random_faction_stabilize_command_power_cost`.

The border-post objective continues to show its captured state, measured division target, and equipment requirement, while the corridor objective continues to show the retained convoy and train thresholds.

## Mission quality notes

`random_faction_reinforce_border_posts` is owned by the pressured neutral in `random_faction_bloc_pressure_category`, uses `random_faction_border_posts_mission_duration`, and requires control of the capital and measured border-post state, the required infantry stockpile, and the measured division threshold.

Its cancel path is `random_faction_cancel_border_posts_mission`, its success path is `random_faction_border_posts_success`, and its timeout path is `random_faction_border_posts_failure`; the existing active flag and objective cleanup are preserved.

`random_faction_guarantee_corridor_mission` is owned by the faction leader in `random_faction_bloc_pressure_category`, uses `random_faction_corridor_mission_duration`, and requires a valid corridor target, the retained convoy threshold, and the measured train target.

Its cancel path is `random_faction_cancel_corridor_mission`, its success path is `random_faction_corridor_success`, and its timeout path is `random_faction_corridor_failure`; the existing target-array, active-flag, and objective cleanup are preserved.

The missions do not consume payment resources, so they have no Black Friday quote, debit, receipt, refund, or settlement row.

The existing activation flags and target arrays prevent duplicate active mission instances within the owner surface; no new duplicate risk was introduced.

## Cost and requirement clarity

The generic owner helper is `random_faction_black_friday_pay_component_list`.

Its setup helpers are `random_faction_black_friday_begin_component_list` and `random_faction_black_friday_append_component`.

The helper uses `universal_cost_quote_integer`, `universal_cost_check_quote_affordable`, `universal_cost_pay_component`, `universal_cost_record_transaction`, `universal_cost_credit_component`, `universal_cost_refund_transaction`, `universal_cost_settle_transaction`, and `black_friday_record_achievement_transaction`.

The trigger-side quote wrappers use `black_friday_quote_custom_cost` and `black_friday_active_component_is_affordable`.

Every action is at or below four spendable component types.

| Logical action | Ordinary positive components | Framework resource kinds | Primary achievement family | Payment adapter | Trigger wrapper |
| --- | --- | --- | --- | --- | --- |
| `random_faction_stabilize_alignment` | `random_faction_stabilize_pp_cost`; `random_faction_stabilize_support_cost`; optional wartime `random_faction_stabilize_command_power_cost` | political power; `support_equipment_1`; optional command power | political power | `random_faction_black_friday_pay_stabilize_alignment` | `random_faction_black_friday_can_pay_stabilize_alignment_cost` |
| `random_faction_request_liaison` | owner command power `command_power_low`; selected leader support equipment `support_equipment_low` | command power; support equipment 1 | command power | `random_faction_black_friday_pay_request_liaison` | `random_faction_black_friday_can_pay_request_liaison_cost` |
| `random_faction_quiet_opposition` | `pp_low`; `infantry_equipment_medium` | political power; infantry equipment | political power | `random_faction_black_friday_pay_quiet_opposition` | `random_faction_black_friday_can_pay_quiet_opposition_cost` |
| `random_faction_convene_neutrality_council` | `pp_medium`; `command_power_low` | political power; command power | political power | `random_faction_black_friday_pay_convene_neutrality_council` | `random_faction_black_friday_can_pay_neutrality_council_cost` |
| `random_faction_invite_observers` | `command_power_low`; `convoy_low` | command power; convoy | command power | `random_faction_black_friday_pay_invite_observers` | `random_faction_black_friday_can_pay_invite_observers_cost` |
| `random_faction_publish_neutrality` | `pp_low` | political power | political power | `random_faction_black_friday_pay_publish_neutrality` | `random_faction_black_friday_can_pay_publish_neutrality_cost` |
| `random_faction_offer_staff_mission` | `command_power_medium`; `support_equipment_medium` | command power; `support_equipment_1` | command power | `random_faction_black_friday_pay_staff_mission` | `random_faction_black_friday_can_pay_staff_mission_cost` |
| `random_faction_radio_networks` | `pp_low`; `support_equipment_medium` | political power; `support_equipment_1` | political power | `random_faction_black_friday_pay_radio_networks` | `random_faction_black_friday_can_pay_radio_networks_cost` |
| `random_faction_guarantee_corridor` | `command_power_low`; `infantry_equipment_medium`; `convoy_low` | command power; infantry equipment; convoy | command power | `random_faction_black_friday_pay_guarantee_corridor` | `random_faction_black_friday_can_pay_corridor_cost` |
| `random_faction_demand_commitment` | `pp_high`; `command_power_medium` | political power; command power | political power | `random_faction_black_friday_pay_demand_commitment` | `random_faction_black_friday_can_pay_commitment_cost` |

The ten adapted actions use one transaction per payer scope and one component row per positive resource component. The two-payer liaison action uses the dedicated owner-local component IDs 1701 and 1702 in its ROOT and FROM ledgers.

The component counts are stabilize 3 in wartime or 2 in peace, quiet 2, council 2, invite 2, publish 1, staff 2, radio 2, corridor 3, and commitment 2.

The owner component identifiers are `owner_component_political_power`, `owner_component_command_power`, `owner_component_infantry_equipment`, `owner_component_support_equipment`, and the parent-added `owner_component_convoy` from the Event 26 constants. The observer and corridor adapters use the dedicated convoy identifier.

Each positive ordinary value is quoted with the default positive quantum and the existing universal round-up behavior before any debit.

The trigger-side wrappers use the same ordinary values and family masks as their effect-side adapters, copy the final quote into the `black_friday_random_faction_*_cost` temporary localisation variables, and require every quoted component to be affordable.

The stabilization wrapper preserves its dynamic country-size cost variables, wartime command-power component, and fixed war-support gate.

Observer, staff, corridor, and commitment adapters recheck their original `FROM` target validity before payment, while all original decision effects retain their own target checks and route behavior.

## AI validity and route-lock notes

All existing `ai_will_do` blocks and `ai_hint_pp_cost` values were retained.

All existing `days_re_enable` cooldowns were retained.

No new AI weight, target selection, route, or faction-leader preference was introduced.

The original target arrays and `FROM` validation remain in the decision definitions, and active adapters recheck the target-sensitive paths before debiting.

The exact target checks retained by adapters are `random_faction_is_valid_observer_source_for_root`, `random_faction_valid_staff_mission_target_for_root`, `random_faction_valid_corridor_target_for_root`, and `random_faction_valid_commitment_target_for_root`.

The required probability auditor route used agent `01a06298-5735-7b02-aa52-1cf0d7c4f2e2` and returned a refreshed MCP inspection for all ten candidates plus a Black Friday comparison.

The refreshed probability artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68f1bd0f858ae3239a756745ffe6d96d27f7f3a1eb3171b36897a31c2582c7e9/cde58280e298a825e8aef881954a1dde86286db73cf02a3e822f16c76a62a9ae/probability-inspect-eef5d9de34f3.json`.

The Black Friday comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe7d111d724a5688d1bdc225c0e8c83b22b40d487b9ff80a5515b691450da8e9/d4a1b8a5c9a4b405b8aa4920d3ad384b273d3def9e47aba0eb00ca729bd58ae7/probability-06fa66b4613cf8dd85127889.json`.

The named comparison scenario `RF_BLACK_FRIDAY_LEADER_COMPARE` reported `comparisonChanges: 0`, `adapterChanged: false`, `assumptionsChanged: false`, and no regressions, supporting the unchanged AI weights and hints.

The auditor's source review confirmed the ten-candidate owner pool and found no AI-weight change warranted, but resilience, stability, pressure, and some target predicates remained unresolved in the MCP scenarios; no exact selection probabilities, timing distributions, or universal balance conclusion is claimed.

The auditor also flagged the known static two-payer liaison disposition and the convoy component identifier at `common\\scripted_effects\\017_random_faction_effects.txt` around the observer adapter. The parent resolved the identifier risk by adding `constant:black_friday_event.owner_component_convoy` and updating the observer/corridor adapters; the live GUI and payment evidence remain pending.

## Localisation and tooltip gaps

The requested `common/localisation/english/017_random_faction_l_english.yml` path does not exist; the actual owner localisation path is `localisation/english/017_join_faction_l_english.yml` and it was updated in place.

The localisation file remains UTF-8 with BOM.

All ten decision `custom_cost_text` keys exist in that file.

All spendable values in the adapted costs use `£pol_power`, `£command_power`, `£infantry_equipment_text_icon`, `£support_equipment_text_icon`, or `£convoy_texticon`.

The stabilization scripted-localisation keys `GetRandomFactionStabilizeCost`, `GetRandomFactionStabilizeCostBlocked`, and `GetRandomFactionStabilizeCostTooltip` now resolve to the quote-backed temporary values through the existing owner localisation keys.

The liaison adapter keeps its owner command-power and selected-leader support-equipment values iconized and labels the two payer scopes explicitly.

The corridor objective retains the existing train icon key `£GFX_train_texticon` and does not treat its retained objective thresholds as spendable Black Friday components.

The complete ordinary cost-trigger audit covered `can_pay_random_faction_stabilize_alignment_cost`, `can_pay_random_faction_request_liaison_cost`, `can_pay_random_faction_quiet_opposition_cost`, `can_pay_random_faction_neutrality_council_cost`, `can_pay_random_faction_invite_observers_cost`, `can_pay_random_faction_publish_neutrality_cost`, `can_pay_random_faction_staff_mission_cost`, `can_pay_random_faction_radio_networks_cost`, `can_pay_random_faction_corridor_cost`, and `can_pay_random_faction_commitment_cost`.

The complete ordinary payment-helper audit found the following owner payment paths: stabilize uses `random_faction_pay_pp_cost`, `random_faction_pay_equipment_cost`, and optional `random_faction_pay_cp_cost`; liaison uses owner `random_faction_pay_cp_cost` plus `FROM`-scope `random_faction_pay_equipment_cost`; quiet uses `random_faction_pay_pp_cost` and `random_faction_pay_infantry_equipment_cost`; council uses `random_faction_pay_pp_cost` and `random_faction_pay_cp_cost`; observers uses `random_faction_pay_cp_cost` and `random_faction_pay_convoy_cost`; publish uses `random_faction_pay_pp_cost`; staff uses `random_faction_pay_cp_cost` and `random_faction_pay_equipment_cost`; radio uses `random_faction_pay_pp_cost` and `random_faction_pay_equipment_cost`; corridor uses `random_faction_pay_cp_cost`, `random_faction_pay_infantry_equipment_cost`, and `random_faction_pay_convoy_cost`; commitment uses `random_faction_pay_pp_cost` and `random_faction_pay_cp_cost`.

The only ordinary dynamic payment variables are `random_faction_stabilize_pp_cost`, `random_faction_stabilize_support_cost`, and wartime `random_faction_stabilize_command_power_cost`; all other positive components are the existing Event 17 script constants listed in the table.

## Cleanup and exploit-risk notes

All components are affordability-preflighted before the first debit, preventing a partial multi-resource charge caused by an unaffordable later component.

Each debit uses exactly the stored final quote, and each successful debit is receipted with its ordinary cost, quoted cost, actual paid cost, resource kind, and source id.

If a native payment fails or a receipt cannot be recorded, the already-paid current component is credited and previously recorded components are sent through the existing refund helper.

The receipt settles only after all component debits and receipt rows succeed, and the unchanged action effect is gated on the successful adapter result.

No delayed refundable Random Faction payment or unsupported owner payload exists in this owner file, so the external-refund acknowledgement path is not required here.

No new daily or weekly world scan, free-unit loop, equipment farm, war-goal loop, core loop, target persistence, or cooldown bypass was introduced.

The original decision effects continue to own mission activation, objective clearing, cancellation, timeout, target cleanup, and outcome effects.

## GUI evidence

Read-only inspection used workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `event026_random_faction_decision_category_current`, and window `countrydecisionview`.

The latest inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/359adb0cb86be94e3e75d811107ca463c665e8356890d875aa7f976fa49d8123/a68cd92365f0e7ca601e003af5fdb23f42fee68e7c9c94a8e4d506f894addc07/gui-inspect.3ce93f7d4ecbc251.json`.

The latest production render layout artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5d59c9d7a1fadc35927f5f4595ba0beb5a264eeb27454d56d15891a7d5a949b/cbbe45b2418ea506879f1b1797987f3378b782a1824e673ad4e7ed828e4530ef/countrydecisionview-layout.json`.

The latest production render image artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/700a77e3d21a7a0bd505e2ef764b25f062fbb50b5ea2491e1253a480b4004588/countrydecisionview-full.png`.

The latest render validation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a847f36346ae0858d69907e3efeae7662b1ea2f830a0b41300a23133b6ddf95/9662ec7b3a30ec44aa571436bf9df6f91bd2f6e6f0053eb235f1b4721d9d007e/countrydecisionview-validation.json`.

The render reported no source-graph blockers or visible-overlap diagnostic, but it also reported shared ordinary-window clipping and invalid-size diagnostics described in the issue list; no GUI rewrite was authorized by this bounded owner scope.

## Changed files

- `common/decisions/017_random_faction_decisions.txt` wires ten quote-backed wrappers into availability, custom cost, and completion gating.
- `common/scripted_effects/017_random_faction_effects.txt` adds the generic component transaction helper and ten Random Faction payment adapters, and gates the original effects on successful active-sale payment.
- `common/scripted_triggers/017_random_faction_triggers.txt` adds ten active-sale quote and affordability wrappers while retaining exact ordinary triggers for inactive play.
- `localisation/english/017_join_faction_l_english.yml` provides quote-backed cost, blocked-cost, availability, and tooltip text with texticons.
- `docs/plans/026_black_friday_plans/subagent_handoffs/random_faction_adapter.md` records this handoff.

No helper blocks were added to `common/scripted_effects/026_black_friday_effects.txt` or `common/scripted_triggers/026_black_friday_triggers.txt`.

## Validation and skipped validation

The owner-wide payment call-site audit found only the ten listed paid actions and no additional direct Random Faction voluntary payment path in the three owner source files.

The targeted coverage audit found one matching active-sale wrapper and one matching adapter for each of the ten paid actions, with the two payer scopes of `random_faction_request_liaison` covered by the dedicated liaison handoff.

The component-count audit found no shared action above four spendable component types.

The touched source files had balanced braces and no literal unsupported `<=` or `>=` operators, and the owner localisation retained its BOM.

The decision custom-cost key audit found all ten referenced keys in the actual owner localisation path.

The read-only HOI4 GUI inspect and production render were run as required for the ordinary decision surface, but no GUI source was changed.

HOI4 was not launched, and no live gameplay, save or reload, multiplayer, or universal-coverage claim is made.

The decision-mission auditor review remains skipped because agent `01a062cb-046f-7112-a5b2-64c9523190da` timed out without a final status.

The probability auditor's requested Black Friday comparison was completed, but live payment execution and save-state validation were not run.

## Remaining risks and simplifications

The earlier static `random_faction_request_liaison` disposition was the only intentional coverage omission among the ten paid actions; it is superseded by the dedicated two-payer handoff and no longer describes the current source.

The convoy component rows use the dedicated `constant:black_friday_event.owner_component_convoy` identifier added by the parent. The two-payer liaison rows use owner-local component identifiers 1701 and 1702, with the exact source and settlement evidence in `random_faction_liaison_adapter.md`.

The equipment-kind mapping between the owner level-one helpers and the universal framework base kinds remains an engine-validation risk because live HOI4 execution was prohibited for this tranche.

Shared ordinary GUI clipping and invalid-size diagnostics remain unresolved because interface files are outside the requested write scope.

No other simplification, fallback, new system, or unlisted gameplay edit was made.

Plan handoff path: no additional plan was written; this file is the implementation handoff under `docs/plans/026_black_friday_plans/subagent_handoffs/`.
