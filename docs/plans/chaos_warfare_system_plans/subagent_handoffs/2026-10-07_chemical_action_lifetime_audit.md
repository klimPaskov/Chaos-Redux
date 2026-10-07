# Chemical action-record lifetime and dispatch audit

Disposition: read-only architecture audit with a concrete insertion map for parent integration.
Only this handoff and its explicitly requested [machine-readable insertion map](2026-10-07_chemical_action_lifetime_insertion_map.json) were written.
No gameplay, tests, shared documentation, index, or commit edits were made.
Source changed during the audit, so the map is a storage contract to reconcile against a fresh owner snapshot rather than a blind patch.

## Main findings

The native land adapter consumes action fields produced in returning helpers without a complete caller-owned record frame.
Its direct `cbrn_reset_action_context` writes 38 fields and calls the 20-field reset-output helper, but neither returning reset creates storage owned by the adapter.
Classification, severity, payload requirement, protection resolution, condition profiles, preparation result, and dispatch proof are subsequently read across helper boundaries.
The existing conservative-frame VM reproduces the missing storage and loss of the one-dispatch guard.
The same public action API is used by air raids, doomsday state records, missiles and camp-method integration.

The smallest supported structure retains those existing action owners and existing nested calculators.
Allocate the public packet in the existing adapter frame that consumes the complete prepared record, and private outputs in the closest existing helper that consumes them.
Do not add a general wrapper, returning initializer helper, persistent action registry, native engine feature, neutral receipt, or payment path.

## Public packet and exact owners

The sidecar has all field names and defaults, with its 38 inputs and 20 output defaults checked against the actual reset definitions.
The two additional public fields are `cbrn_action_military_mask_only_casualty_mult` and `cbrn_action_civilian_mask_only_casualty_mult`, both initially one as in the target-protection resolver.
They are used later by the exposure calculator's same-mask death floors and are not part of the 58-field reset.

| Existing owner | Placement | Required contract |
| --- | --- | --- |
| `cbrn_resolve_chemical_land_raid_country_outcome` | Before its reset, inside the actor-valid branch | Public 60-field packet, preserving the exact actor/state/victim targets and event-owned raid tuple |
| `cbrn_resolve_chemical_air_raid_outcome` | Before `cbrn_resolve_chemical_air_raid_reservation` | Same packet plus `cbrn_raid_result`, `cbrn_raid_release_proof`, `cbrn_raid_reservation_proof` |
| `cbrn_chemical_doomsday_resolve_current_state` | Before its reset for each exact state record | Same packet. The existing outer agent/batch counters remain ancestor-owned |
| `missiles_dispatch_chemical_payload` | Before its reset | Same packet plus caller-owned `cbrn_action_civilian_deaths`, which the missile owner reads after dispatch returns |
| `camp_rework_apply_chemical_escalation_in_action_state` | Before the existing method-outcome helper and reset, with original call order intact | Same packet plus the five method outputs listed below |

The full 60-field recommendation is deliberate for these five complete-record consumers.
It reproduces the existing reset contract's exact missing/default values and preserves forwarded outputs across multiple nested returns.
It also makes the reset of optional condition inputs and one-dispatch proofs explicit when another action shares an ancestor frame.
It does not turn a missing weather, density, forecast, protection, payload, or release receipt into a supplied receipt.
Existing literal declarations that already own a field before its producer can be reused, and a parent may omit a redundant declaration only after proving that exact ownership and unchanged reset semantics in the frozen owner source.
Partial initialization based only on the values directly assigned on the successful branch would omit rejected/default branches and the nested prepared-record outputs.

Two read-only metadata consumers do not need that full packet.
`cbrn_payload_validate_request_authorization` needs caller-owned `cbrn_action_agent_class` and `cbrn_action_payload_required` before its reset/model/default helpers.
Its native model, matched flag, consumed amount, and consumed proof already have explicit local storage, and its published authorization/model/class/cost outputs are regular country variables.
The current `missiles_check_chemical_payload_stock`, if retained by its owner, needs the same two fields before classification and default-payload helpers.
Neither consumer should receive a new exposure or payment step.

## Nested producers and narrow storage

| Consuming frame | Producing helper or chain | Returned fields actually consumed | Placement and status |
| --- | --- | --- | --- |
| `cbrn_calculate_chemical_action_outputs` | Route profile | `cbrn_route_base_disruption`, `cbrn_route_civilian_exposed_fraction`, `cbrn_route_contamination_points`, `cbrn_route_medical_points`, `cbrn_route_evidence_points`, `cbrn_route_condemnation_base`, `cbrn_route_duration_days` | Seven local allocations before the profile call |
| Same calculator | Agent-class profile | `cbrn_class_disruption_mult`, `cbrn_class_contamination_mult`, `cbrn_class_medical_mult`, `cbrn_class_evidence_mult`, `cbrn_class_condemnation_mult`, `cbrn_class_duration_mult`, `cbrn_class_tactical_lethality`, `cbrn_class_strategic_lethality` | Eight local allocations before the profile call |
| Same calculator | Exact-agent profile | `cbrn_agent_potency_mult`, `cbrn_agent_persistence_mult`, `cbrn_agent_evidence_mult` | Three local allocations before the profile call |
| `cbrn_resolve_action_target_protection` | Both calls to `cbrn_calculate_action_protection` | `cbrn_action_effective_protection`, `cbrn_action_casualty_mult`, `cbrn_action_mask_only_casualty_mult`, `cbrn_action_disruption_mult`, `cbrn_action_contamination_mult`, `cbrn_action_protection_resolved_proof` | Own all six before the first calculation. The proof already had a literal declaration, so only five were previously missing |
| `cbrn_calculate_action_protection` | Protection-weight profile | Six `cbrn_protection_weight_*` values: respiratory, skin, antidote, decontamination, medical, warning | Own locally inside the valid-input branch before the weight helper |
| Accepted `cbrn_dispatch_chemical_action_record` branch | Source/context, evidence-floor, and state-consequence helpers | `cbrn_action_condemnation_context`, `cbrn_action_evidence_floor`, `cbrn_action_civilian_deaths` | Three declarations inside the existing accepted/undispatched branch before the producer calls |
| Accepted no-release attempt dispatcher | Attempt-consequence helper | `cbrn_raid_attempt_evidence_points`, `cbrn_raid_attempt_evidence_floor`, `cbrn_raid_attempt_condemnation_base` | Three declarations inside its existing gate before the producer |
| `cbrn_chemical_air_raid_apply_attempt_evidence_internal` | State evidence helper, then attribution helper | `cbrn_state_attribution_output` | Allocate unknown before the evidence helper. The ordinary successful state-consequence path already does this correctly |

At a later source read, the exposure calculator already contained all eighteen private profile declarations, and the target-protection resolver contained the six generic output allocations.
These edits appeared while this agent remained read-only.
Do not duplicate them or assume other source boundaries were fixed by their presence.
The sidecar marks those observed existing declarations explicitly.

`cbrn_prepare_chemical_action_record` does not directly invoke the profile helpers.
It calls the exposure calculator, which consumes those profiles internally.
The public result, reject reason, victim proof, retaliation status, doctrine multiplier, output fractions/points, labels, and attribution fields must survive that calculator and preparation return in the complete action owner.
The eighteen private profile values can die when the calculator returns because no adapter needs them after that return.
Historical advisor treatment multipliers are already initialized in the calculator before their modifying helpers and must not be reinitialized after the returned modification.

Temporary variables are unscoped.
Entering the exact target state, controller, or actor changes the recipient of native effects and regular country/state storage, not the temporary frame owner.
Do not write `ROOT.<temporary>` or copy the packet into permanent country variables to avoid these boundaries.

## Dispatch proof and release receipts

`cbrn_action_dispatch_proof` is an action-owner field.
It must start at the existing missing value when that action begins and survive the dispatcher setting it to supplied.
Never clear it at dispatcher entry or inside a returning dispatcher initializer, because that would let a repeated dispatch of the same prepared record pass the existing `NOT supplied` guard.
Apply the same rule to `cbrn_raid_attempt_dispatch_proof` on the no-release path.
The ordinary and failed-attempt dispatchers remain separate and retain their original gates and callback order.

The land resolver already creates `cbrn_raid_release_accepted = missing` in its own frame and sets it only after its prepared record was accepted and dispatcher proof is supplied.
`japan_resolve_chemical_campaign_raid_outcome` in `JAP_chemical_campaign_effects.txt` already allocates that receipt before calling the land resolver, so the Japan family credit boundary is correct.
The ordinary land bridge does not consume that return value after calling the resolver and needs no redundant outer declaration.
No new country-level pending scalar or marker family is needed.

This proof is one-dispatch protection within the existing action context.
It is not evidence of a persistent cross-event replay identity, and this audit adds no such design.
Native callback tuple validation still requires exact actor/state/victim pointers and exact-one route/agent/outcome/variant markers.

## Doomsday-specific boundaries

`cbrn_chemical_doomsday_release` consumes nine newly returned scalars and one temporary target array.
The scalars are `cbrn_doomsday_target_count`, four `cbrn_doomsday_stock_*` values for chlorine/phosgene/mustard/lewisite, `cbrn_doomsday_arsenal_consumed_total`, `cbrn_doomsday_stockpile_debit_proof`, `cbrn_doomsday_condemnation_total`, and `cbrn_doomsday_agent_condemnation_share`.
Allocate those in the existing release frame and create `cbrn_doomsday_target_states` there before the collection helper.
The existing collection still selects the same controlled eligible states, and capture/consumption still accounts for the same native-reserved cylinders and remaining arsenal.
No payload is debited or refunded by these declarations.

The agent-dispatch helper already owns its remaining payload, remaining target count, current allocation, and current-agent condemnation-paid flag before nested state resolution.
The release helper already owns resolved-payload total, resolved-state count, and failure proof before invoking those agent helpers.
Preserve that storage and the persistent country commitment flag before irreversible release.
No declaration is recommended for `cbrn_doomsday_last_reject_reason` solely as a return value because the bounded source scan found no subsequent consumer.

`chaosx_cbrn_doom_raid.1` in `events/cbrn_doomsday_raid_bridge.txt` reads `cbrn_doomsday_release_status` after the release helper returns.
It needs a literal missing-value declaration immediately before that helper call.
The full-resolution status is consumed inside release and does not require another bridge declaration.
Keep the existing commitment, incomplete-resolution, news, fallout, and permission behavior unchanged.

## Neighboring owner boundaries and stable outputs

`032_missiles_operations_effects.txt` changed during this audit.
Its current `missiles_consume_chemical_payload` delegates to `missiles_consume_chemical_payload_receipt`, whose durable held receipt owns the original debit.
Do not restore the earlier local reset/debit implementation or add a second stock payment.
The sidecar maps only the current read-only check and impact dispatch consumers and labels the file for active owner review.
Normal missile delivery-result and consumed-payload receipts survive helper returns, while the temporary shared action record and returned civilian-death count still need the mapped frame ownership.

The camp method-outcome helper returns `camp_rework_method_death_factor`, `camp_method_evidence_gain`, `camp_method_accident_pressure`, `camp_method_stockpile_cost`, and `cbrn_camp_action_duration_days`.
The owning escalation frame consumes them for existing payload cost, release efficiency, duration, and post-dispatch country consequences.
Allocate them in that owner before its existing method helper, preserving the source defaults and tiers.
`cbrn_try_debit_action_payload` already creates `cbrn_payload_debit_model_matched` before its nested debit helpers, so that particular internal boundary is safe.
Its returned consumed quantity and proof are covered by the complete camp-owned packet.
This existing owner payment must remain separate from native raid reservation and must never be inserted into a native land or air outcome adapter.

The unified action-record helper's temporary row index and UID are consumed inside that helper and then published as regular country last-record fields and persistent aligned global arrays.
Its caller supplies the thirteen record inputs before calling it.
No new outer UID or row-index allocation is required for the reviewed chemical history path.
The successful state-consequence path already preinitializes its exact death receipt and state attribution output before their returning helpers.
The recovery events in `cbrn_chemical_delivery_events.txt` create their day counters directly in their event frames and read regular persisted state values.
No returning action-record packet is carried across a delayed event.

## Demonstrated source-frame results and limits

The checked-in parser and conservative helper-return VM from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js` were reused without edits in an in-memory invocation.
The actual complete reset retained zero of its 58 fields with no caller storage, and all 58 with caller storage.
The military casualty default read as missing/zero in the bare model and one in the caller-owned model.
Actual unconditional output-definition prefixes retained zero versus 7 route, 8 class, 3 agent, and 6 protection-weight fields without/with caller ownership.
The exact dispatch proof assignment and exact `NOT supplied` guard allowed a second guard evaluation after the unowned proof disappeared, and blocked it when the action owner already owned the proof.

These are observed conservative source-frame results.
They do not execute native damage, deaths, equipment reservation, weather, policy, population caps, state arrays, or a complete valid/rejected callback.
No generic test count or helper-marker scan is presented as engine gameplay proof.
The profile proof was restricted to actual unconditional declarations after the small parser could not parse the anonymous nested schema portions of the profile constant blocks.
That fixture limitation is not an engine-source defect or a reason to invent profile values.

Parent regression should preserve all original AST statements, calls, and gate order while inserting only the mapped owned storage.
Meaningful cases include a valid actor/target/paid native callback, wrong actor or exact target, stale previous record, rejected preparation, repeated dispatch of the same record, no-release air attempt, reserved missile receipt, restricted camp route, and separate doomsday state allocations.
Assert one existing payment, one accepted dispatch/history row, exact fractions and state/country recipients, preserved same-mask floors, missing-condition omission, and no achievement credit from an unaccepted release.
Coordinate fresh snapshots and isolated shared-file hunks with missile and camp owners before any change.

## References and source evidence

Skills read/applied: `chaos-redux-native-raids`, `chaos-redux-events`, and `chaos-redux-subagents`.
The established lifetime rule is offline `Data structures:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, especially the scripted-return caveat at line 440 and unscoped temporaries at line 442.
The installed `set_temp_variable` reference at `effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, supports assignment in any scope but does not itself establish return lifetime.
These sections and event-target/owner scope references were already read through the live reference routes during the preceding caller-storage work.

Live reference search/read covered installed `common/raids/_documentation.md:167-173`, revision `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e`, which states that essential equipment is collected after raid creation.
Installed raid outcome scope guidance at lines 249-268 and 297-298 was read locally and places both actor/victim effects in raid-instance scope.
Vanilla `common/raids/land_infiltration_raids.txt:164-175` supplies the explicit `var:actor_country` outcome precedent.
Thus preserve the immediate actor-country bridge and exact saved pointers, and do not infer country ROOT inside a native raid callback.
No online Paradox wiki was accessed.

Bounded `hoi4.source_lookup` identified the unshadowed `cbrn_reset_action_context` definition, source-index revision `1381c6941e91ac57e0cbe302659ce20da4a4bddbeeffc27a24d10444f6dfbc08`.
It covers indexed source structure and not helper execution or native lifetime.
The parent owns domain before/after evidence, and no duplicate event/probability call was made.
The known unreadable event artifact boundary remains a validation limit rather than a completed trace claim.

Relevant source SHA-256 snapshots, which must be refreshed for owner patches because concurrent source changes were observed:

| File | SHA-256 |
| --- | --- |
| Land raid effects | `7074d859be1479310cb39d79529c3fbd40dacb7cf778d965e33202916baa9d1c` |
| Air raid effects | `b770477f77423347eeda57e644ee3acfa3eb6aae9e492347a9ff71e049c67d8c` |
| Doomsday effects | `944b45bd4facd8dc8e3648da9f8c7be41cde2fc8f5c4116fe962bbe22598ad04` |
| Exposure effects | `bb23620b4f16f62b4f808b3524b6a59e6bcf57a12f62802c816b1ceb824aae72` |
| Consequence effects | `43b8546fb77cf3086940020739f8f9f6e29d8dbe513b12b1e1387219f643692b` |
| Protection effects | `9f3b758880f3cdff6fe6a536745b36c78628d7a60e237b5b9b7f12207ef5a8d3` |
| Payload reservation effects | `b70d6868e9438cd86bf68e646f1c773677bc23275539aca90a9b30e78759d8d3` |
| Unified action-record effects | `b18cd1274fc1972ab1b670322ed5d876c9a86bbe8f582e8ed71ca760654cd78e` |
| Missile operations shared owner file | `6c64f09079fd24060879ba9ee33afd4744bdcb205d4301eba8723623c5a15434` |
| Camp repression shared owner file | `7c68d93e8097fc6a33af11ff7cd3bae3216dc9335f36b65ac0cdcf94aff5644c` |
| Land bridge event | `1c57c0e7674194b76bf9acb2034cd99ae925b9a22000d7ab35b286a93d6f6fc7` |
| Chemical recovery events | `0069266630afe853007311b0d03ddac38ff678245a035d2451aa58bcbaf21d40` |
| Doomsday bridge event | `76f4a4e29a442288f7b22ff52365c010f161a9d71801e25e3cdee3a992d6981a` |

The audit and exact insertion map are complete as implementation support.
Parent integration, actual-source transaction regressions, final mixed-file ownership review, and native interpretation remain outstanding.
No payment, authorization, target, weather-proof, weight, actor, severity, or fallback policy was changed by this agent.
