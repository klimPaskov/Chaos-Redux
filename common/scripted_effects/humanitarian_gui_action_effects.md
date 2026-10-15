# Humanitarian panel action lifecycle

Famine and migration keep one production action implementation shared by AI decisions and human panel controls.
The parent accepted this lifecycle within the national-policy-panel task, preserving all ten famine operations and seventeen migration operations while moving the three national policy purchases to native laws.

## Public helper map

| Helper family | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `famine_gui_start_action`, `migration_gui_start_action` | Actor COUNTRY, temporary matching `*_gui_action` enum, normal `*_panel_selected_state` exact state pointer | Submits a guarded request, clears the temporary enum, and starts only validated work | Parent panel buttons |
| `*_gui_can_start_<suffix>`, `*_gui_can_show_<suffix>` | Actor COUNTRY, matching selected state | Pure read apart from temporary scratch. Start combines live authority, phase, target, quote, generation slot and cooldown. Native requirement tooltips remain expandable | Panel visibility, enablement, hover |
| `*_gui_refresh_selected_action_status` | Actor COUNTRY and current selected state | Presentation-only `*_action_remaining_<suffix>`, `*_action_cooldown_days_<suffix>` and `*_action_active_<suffix>` country flag. No registration or payment | Panel refresh |
| `*_action_submit_request` | Current COUNTRY, request action and target normal variables | Immediate hidden country event establishes ROOT actor without relying on global-host ROOT | Native decision wrappers and GUI dispatch |
| `humanitarian_action_begin` | Actor COUNTRY inside bridge event, mandatory temporary token inputs `humanitarian_action_system_token/name_token/suffix_token`, numeric `kind/targeted/timed/duration_days/cooldown_days` inputs | Publishes exact operation proof before calling the sole production payment body, records success once and registers only a delayed operation | Subsystem enum mapper |
| `*_action_resolve_callback`, `*_action_cancel_callback` | Current COUNTRY and positive `humanitarian_action_callback_id` | Finds only the exact retained row, never the latest action or current panel target | Native callbacks and existing sparse country processor |
| `humanitarian_action_resolve`, `humanitarian_action_cancel` | Actor COUNTRY plus exact row loaded by the finder | Consume one row before resolution, use current authority and exact generation, preserve existing zero-result refunds and cancellation semantics | Subsystem resolution mapper |
| `migration_gui_publish_transfer_participants` | Actor COUNTRY and finalized `civilian_transfer_route_origin` / `civilian_transfer_route_destination` event targets | Publishes both settled endpoints only after action receipt and refund cleanup; valid result and positive measured debit are required | Transfer-backed Migration action resolvers |
| `humanitarian_action_abandon_dead_actor` | Nonexistent actor COUNTRY and exact loaded row | Clears only matching old actor/state/generation payment and operation proof, forgets its transport receipt and retires the row without refund or reward | Existing sparse country processor when a country cannot receive an event |
| `migration_national_policy_changed` | COUNTRY after native law publication, temporary previous/new policy and civilian slot | Existing closure political consequences for a pending reception issue, dirties capacity only for an already registered country and refreshes each currently open humanitarian panel without reconciling laws or registering gameplay | Native law publisher |

The hidden `humanitarian_actions.1` through `.6` events carry no timing delay.
Their purpose is to establish the actor as ROOT for existing deep relief, transfer, achievement and condemnation consumers, including when the sparse coordinator's ROOT is the global host.
A proven `humanitarian_action_context_proven = 1` temporary marker makes legacy wrappers retain the explicit actor/target envelope across deep owner calls.
Without that marker, a legacy wrapper initializes its inputs from the native ROOT/FROM contract.
The target is always an explicit stored STATE scope, and owner context variants read `humanitarian_action_actor` and `humanitarian_action_target` temporary scope pointers rather than borrowing FROM from the coordinator.
Generic helpers use bare `= yes` calls.
Their native `meta_effect` blocks replace `[SYSTEM]`, `[NAME]` and `[SUFFIX]` through the documented `[?temporary_token.GetTokenKey]` interpolation, and all duration, action, and Boolean inputs are unscoped temporary numeric variables.
No scripted helper accepts named arguments or `$PARAMETER$` placeholders.
`common/script_enums.txt` registers the two subsystem family tokens and all 27 suffix tokens in `script_enum_humanitarian_action_part`.
The same block retains three compatibility token identifiers under an explicit receipt section comment for the retired departure/border purchases, without restoring their decision definitions.
The NAME tokens remain the 27 actual native decision IDs.
Only registered enum members or native database IDs may feed these `GetTokenKey` inputs, and the source fixture rejects arbitrary scripted-helper names, undefined literals and values without the token flag.
Ordinary decision IDs, target pools, native AI weight blocks and all six native missions remain authoritative AI and mission surfaces.
Only ordinary action visibility is AI-only.

## Constants and action inventory

`common/script_constants/humanitarian_gui_action_constants.txt` owns stable `famine_gui_action` and `migration_gui_action` enums.
Every duration and cooldown reuses its original subsystem timing constant.
An immediate action with a native removal duration retains that duration in its total cooldown even though its work executes immediately.
No balance values, food laws, food ownership, transport profiles or transfer rates are introduced.

| System | Enum | Native action ID | Target | Work phase | Duration source | Re-enable source |
| --- | --- | --- | --- | --- | --- | --- |
| famine | 1 | `famine_release_reserves` | state | delayed work | `constant:famine_decision_timing.decision_standard` | `constant:famine_decision_timing.decision_reenable_short` |
| famine | 2 | `famine_emergency_imports` | state | delayed work | `constant:famine_decision_timing.decision_extended` | `constant:famine_decision_timing.decision_reenable_standard` |
| famine | 3 | `famine_repair_relief_route` | state | delayed work | `constant:famine_decision_timing.decision_route` | `constant:famine_decision_timing.decision_reenable_standard` |
| famine | 4 | `famine_escorted_relief_convoy` | state | delayed work | `constant:famine_decision_timing.decision_long` | `constant:famine_decision_timing.decision_reenable_long` |
| famine | 5 | `famine_emergency_airlift` | state | delayed work | `constant:famine_decision_timing.decision_standard` | `constant:famine_decision_timing.decision_reenable_long` |
| famine | 6 | `famine_invite_relief` | state | delayed work | `constant:famine_decision_timing.decision_extended` | `constant:famine_decision_timing.decision_reenable_long` |
| famine | 7 | `famine_evacuation` | state | delayed work | `constant:famine_decision_timing.decision_route` | `constant:famine_decision_timing.decision_reenable_route` |
| famine | 8 | `famine_requisition_safer_state` | state | delayed work | `constant:famine_decision_timing.decision_warning` | `constant:famine_decision_timing.decision_reenable_standard` |
| famine | 9 | `famine_conceal_crisis` | state | delayed work | `constant:famine_decision_timing.decision_warning` | `constant:famine_decision_timing.decision_reenable_route` |
| famine | 10 | `famine_maintain_extraction` | state | delayed work | `constant:famine_decision_timing.decision_brief` | `constant:famine_decision_timing.decision_reenable_standard` |
| migration | 1 | `migration_prepare_evacuation` | state | delayed work | `constant:migration_decision_timing.decision_brief` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 2 | `migration_evacuate_vulnerable` | state | delayed work | `constant:migration_decision_timing.decision_standard` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 3 | `migration_evacuate_civilians` | state | delayed work | `constant:migration_decision_timing.decision_standard` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 4 | `migration_evacuate_administration` | state | delayed work | `constant:migration_decision_timing.decision_standard` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 5 | `migration_evacuate_workers` | state | delayed work | `constant:migration_decision_timing.decision_route` | `constant:migration_decision_timing.decision_reenable_route` |
| migration | 6 | `migration_negotiate_corridor` | state | delayed work | `constant:migration_decision_timing.decision_standard` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 7 | `migration_accept_corridor_offer` | country | immediate work | `constant:humanitarian_corridor_timing.response_decision_days` | `constant:humanitarian_corridor_timing.response_reenable_days` |
| migration | 8 | `migration_reject_corridor_offer` | country | immediate work | `constant:humanitarian_corridor_timing.response_decision_days` | `constant:humanitarian_corridor_timing.response_reenable_days` |
| migration | 9 | `migration_open_reception` | state | immediate work | `constant:migration_decision_timing.decision_brief` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 10 | `migration_controlled_medical_reception` | country | immediate work | `constant:migration_decision_timing.decision_standard` | `constant:migration_decision_timing.decision_reenable_route` |
| migration | 11 | `migration_distribute_arrivals` | state | delayed work | `constant:migration_decision_timing.decision_standard` | `constant:migration_decision_timing.decision_reenable_short` |
| migration | 12 | `migration_transit_only` | state | delayed work | `constant:migration_decision_timing.decision_short` | `constant:migration_decision_timing.decision_reenable_short` |
| migration | 13 | `migration_enforce_closure` | state | delayed work | `constant:migration_decision_timing.decision_brief` | `constant:migration_decision_timing.decision_reenable_standard` |
| migration | 14 | `migration_local_integration` | state | immediate work | `constant:migration_decision_timing.decision_integration` | `constant:migration_decision_timing.decision_reenable_integration` |
| migration | 15 | `migration_third_country_resettlement` | state | delayed work | `constant:migration_decision_timing.decision_integration` | `constant:migration_decision_timing.decision_reenable_integration` |
| migration | 16 | `migration_voluntary_return` | state | delayed work | `constant:migration_decision_timing.decision_long` | `constant:migration_decision_timing.decision_reenable_integration` |
| migration | 17 | `migration_forced_repatriation` | state | delayed work | `constant:migration_decision_timing.decision_long` | `constant:migration_decision_timing.decision_reenable_integration` |

## Pending records and cleanup

Each actor owns aligned `famine_action_ids/types/states/dates/starts` or `migration_action_ids/types/states/dates/starts` arrays.
The country-local monotonically increasing `*_action_sequence` is both row identity and operation generation.
An exact per-action/per-state country generation, start and due field binds the slot, and the target stores the action's operation generation, actor and original positive cohort selector when present.
Native callbacks retain their own generation key so an old native timer cannot resolve or cancel a later GUI action in the same state.
Row lookup rejects nonpositive IDs and misaligned arrays.
Changing the panel selection cannot alter a pending row.
The aligned starts array records the exact start date used with the row due date for parent-owned progress presentation.
The sparse processor retains a cursor across the native 1,000-iteration loop ceiling and resumes the unvisited records on its next existing country callback.
An exact-index hint is accepted only when that index still carries the same positive callback ID, so a large pending set never depends on scanning through the newest 1,000 rows.
A selected explicit cohort must match the current unique state selector at start, and a pending operation never switches to another cohort after its recorded selector changes.
Optional `migration_panel_selected_offer_generation` must match the current mirrored offer generation when positive.
Absent or zero optional selectors retain the existing unique-cohort/current-offer behavior.

The existing sparse registered-country callbacks process pending work before ordinary phase retirement.
A positive pending row prevents otherwise quiet country retirement.
Opening a panel never enrolls a country in the gameplay registry.
Paid work remains eligible after its initiating crisis recovers, matching the previous native paid-continuation contract.
Authority-loss cancellation keeps the existing loss of committed resources and action-specific cleanup.
A nonexistent actor is handled directly in its country scope because it cannot receive the bridge event, and exact actor/state/generation proof protects every state and payer receipt cleared by that retirement.
The sole production refund helpers retain saved actual transport quantities and the original non-transport refund amounts.
Measured-zero refunds clear the scripted action cooldown, while the native AI decision's own cooldown is still governed by its unchanged engine definition.
No new recurring on_action or world scan is added.
No global event targets are introduced.
Existing short-lived transaction targets remain confined to their owner chains.

## Validation and limits

Production-source contract tests live in `.tools/test_humanitarian_gui_actions.py`.
The retained `.tools/test_famine_takeover_20261006.py` refund regression follows the same production operation path for connected and disconnected geography.
They execute the actual enum mapper, explicit temporary context wrappers, availability and quote gates, native-event bridge bodies, payment, actual native meta replacements and transport receipts, refund, pending row lookup, due/cooldown lifecycle, exact actor/state/generation guards and mission date helpers.
Native effects and unrelated presentation/initialization consumers are declared fixtures.
The model treats trigger-side temporary assignments as statements, including inside NOT, and cannot prove the engine's evaluation of those inherited transport predicates.
It does not establish native event execution ordering, native AI timer observation, live UI appearance or campaign behavior.

The read-only probability auditor found all 27 retained action weight blocks and all six mission bodies identical to the raw before-source snapshots.
Named scores include reserve release 72/108 at mild peace/war and 288/432 at catastrophic peace/war, with overload blocking evacuation through the existing shared capacity predicate.
The probability MCP misclassified the decision family and returned stale indexed hashes, so those artifacts do not verify this checkout.
File-mode script validation of the corrected meta envelope returned no findings but kept `valid = null`, with 17 outer commands inspected and 11 argument blocks unchecked.
That snapshot predates the final exact start-date and nonexistent-actor branches, which are covered by the production-source tests.
It does not validate the dynamically generated inner text.
Production tests expand the actual native meta replacements and reject named scripted-helper arguments.
Source comparison verifies all 71 retained production callback bodies against the original source after reversing explicit scope adapters and the accepted policy-write removals.
Contract execution covers the selected real dispatch and refund paths and a 1,201-row pending registry without claiming game execution.

## Presentation and future work

Existing famine and migration decision sprites remain the action icon sources.
This lifecycle reuses existing action sprites and adds no image, GFX, map or player-facing mechanic value.
The parent-owned localisation adapter supplies named selected-state requirement text and the law requirement lines.
The parent owns panel GUI, category attachment, cost rows, precise blocked messages and selected-state presentation.
Future lifecycle changes should extend the one shared pending contract and preserve exact production callbacks rather than introduce another scheduler or population-transfer path.

The shared begin, resolve, cancel, and native-law callback boundaries batch the actor country with `national_policy_panel_begin_update`/`national_policy_panel_end_update`, flushing that actor's open panel only after pending rows, owner work, receipts, and refunds settle.
