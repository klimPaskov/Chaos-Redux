# Event 35 inherited-region companion

## Purpose and scope

`great_depression_register_inherited_region = yes` is the country-scope companion to the existing synchronous `great_depression_start_or_deepen` gateway.
THIS is the exact receiving country, independently of ROOT.
The companion validates a proven Event 34 state, records its source metadata once, creates or merges an eligible Depression Center, or retains a hidden or ignored receipt.
It does not allocate another national crisis, count pacing, schedule events, delete factories, grant Event 34 legacy rewards, or select a replacement state.

The implementation is in [035_great_depression_region_effects.txt](035_great_depression_region_effects.txt).
The public identifier remains in [035_great_depression_effects.txt](035_great_depression_effects.txt).
Enums and the receipt bound are in [035_great_depression_region_constants.txt](../script_constants/035_great_depression_region_constants.txt).

## Inputs

All numeric inputs are normal variables on the exact receiving country.
Their prefix is `great_depression_region_call_`.

| Suffix | Required value |
| --- | --- |
| `contract_supplied` | `constant:great_depression_region_contract.version`, currently 1 |
| `country_id` | The exact receiving country's `THIS.id` |
| `episode_id` | Exact current Event 35 episode, or the next episode reserved by the existing new-crisis precommit branch |
| `event34_episode_id` | Positive integer Event 34 episode identity |
| `collapse_receipt_id` | Positive integer national collapse receipt matching pending or committed Event 35 source context |
| `receipt_id` | Positive integer regional receipt, unique together with Event 34 episode |
| `state_id` | Positive integral state ID in built-in `global.states`, or an explicitly proven regular state target |
| `role` | `great_depression_region_role` enum |
| `project_profile` | `great_depression_region_profile` enum, or explicit unavailable |
| `project_stage` | `great_depression_region_project_stage` enum, or explicit unavailable |
| `protection` | `great_depression_region_protection` enum, or explicit unavailable |
| `fragility` | `great_depression_region_fragility` enum, or explicit unavailable |
| `control` | Frozen `great_depression_region_control` enum |
| `damage` | Frozen `great_depression_region_damage` enum, or explicit unavailable |

Target-only calls save `great_depression_inherited_region_state` as a regular state target and set country flag `great_depression_region_call_state_target_supplied`.
The proof flag is mandatory when `state_id` is omitted.
When that proof accompanies an ID, both must identify the same existing state.
A stale regular target without this proof cannot supply an omitted ID.
Membership in built-in `global.states` is checked before constructing the literal ID scope with `meta_effect`.
No guessed ID, `scope_exists` variable test, extra state registry, or periodic scan is used.

Optional normal inputs are `legacy_receipt_id`, `corridor_receipt_id`, and `exhaustion`.
Missing optional metadata becomes `constant:great_depression_region_contract.unavailable`, which is -1.
Zero means explicit none, sound, intact, or no recorded amount as appropriate.
The two optional receipt IDs must be integral.
Exhaustion may be a nonnegative fixed-point quantity.
Negative values other than -1 reject.
An optional country flag `great_depression_region_call_conversion_forbidden` preserves an upstream conversion prohibition through delivery.

During the pending Event 34 national call, all twelve frozen regional payload fields are compared with the receiving country's `industrial_boom_snapshot_region_*` fields.
The frozen `industrial_boom_snapshot_region_conversion_forbidden` flag and supplied `great_depression_region_call_conversion_forbidden` flag must also agree.
Both present and both absent are valid.
Either mismatch rejects as invalid source before center or receipt mutation, even when the live state prohibition has cleared.
The Event 34 episode and collapse receipt also match the national request.
The national snapshot validator remains owned by the parent.

## Enums and constants

| Category | Values |
| --- | --- |
| Role | none 0, primary 1, corridor 2, secondary 3 |
| Project profile | none 0, ordinary 1, speculative 2, miracle 3, corridor 4 |
| Source project stage | none 0, unfinished 1, completed 2, failed 3, abandoned 4, liquidated 5 |
| Protection | none 0, protected 1, failed 2 |
| Fragility | sound 0, fragile 1, severe 2 |
| Frozen or live control | connected 0, temporary loss 1, transferred 2 |
| Damage | intact 0, damaged 1, heavy 2 |
| Disposition | rejected 0, created 1, merged 2, hidden 3, ignored 4 |

Unavailable -1 is accepted for profile, project stage, protection, fragility, and damage.
Role and control must be explicitly supplied.
Source project stages are separate from the existing Event 35 physical stage enum.

The companion uses the existing normal visible cap of three.
It allows the existing fourth-center cap only when the current numeric Event 35 floor or the valid pending inherited floor is III.
Historical evolution flags do not raise this cap.
The parent-owned initial selector keeps its usable-pool scaling and score coefficients.

The new country receipt ledger is capped at 256 rows.
Existing receipts are never evicted to accept another request.
An exact duplicate remains readable at full capacity.
A new receipt at capacity rejects before mutation.

The Event 34 regional freezer uses `heavy_damage_ratio = 0.5` against actual civilian, military, and naval factory levels.
It preserves the raw damaged and total factory counts as frozen source evidence.
An explicitly supplied state damage enum overrides the derived value.
This threshold encodes the mapped heavy-damage condition and needs parent tuning review.
No source probability weights, national Severity coefficients, or pacing durations are changed.

## Outputs and idempotence

All outputs use prefix `great_depression_region_call_` and are normal country variables.

| Suffix | Meaning |
| --- | --- |
| `accepted`, `rejected` | Numeric return values compatible with immediate caller reads |
| `result` | Disposition enum |
| `reject_reason` | Stable regional reject enum |
| `created`, `merged`, `hidden`, `ignored` | Disposition-specific numeric outputs |
| `center_index` | Zero-based current visible registry index, or -1 |
| `no_op` | 1 for an exact retained receipt |
| `disconnected` | 1 when the recorded live control was lost or transferred |

Every output resets before validation.
Inputs and private proof/scratch state clear on accepted and rejected companion calls.
Regular targets expire with the originating chain and cannot be manually cleared.
Cleared country proof flags prevent a surviving target from silently supplying a later request.

The receipt key is receiving country, Event 34 episode, and regional receipt.
An exact repeated payload returns its retained disposition without replaying a stage, modifier, center row, or legacy.
Changed episode association, state, metadata, or collapse linkage under the same key rejects as a receipt conflict.
A duplicate from a closed episode returns no visible index.
A duplicate whose state is no longer controlled also returns no visible index.

Reject reasons are none 0, missing contract 1, invalid country 2, invalid episode 3, invalid source 4, invalid state 5, invalid metadata 6, receipt conflict 7, ledger full 8, and unaligned ledger 9.

## Local mapping and effects

| Proven source condition | Local mapping |
| --- | --- |
| Completed and protected | Distressed, subject to explicit fragility, control, or heavy damage |
| Unfinished | Idled and retained unfinished source receipt |
| Speculative or fragile | At least Idled |
| Failed, abandoned, severe fragility, heavy damage, or disconnection | Shuttered |
| Already liquidated by Event 34 | Liquidated memory, with zero Event 35 physical deletion |
| Unavailable regional metadata | Existing evolution-based opening and documented aggregate project-pressure compatibility |
| No source role | Ignored immutable source receipt |
| Lost, transferred, non-core, forbidden, another episode's live center, or visible cap reached | Hidden exact-state receipt |

Unavailable project stage does not become a fabricated per-state project.
For the current single-state legacy caller, the existing aggregate project-unit pressure can still raise its opening to Idled.
After the national API returns, that compatibility read uses committed `great_depression_inherited_event34_project_units` with matching source episode.
It never reads cleared public project inputs after return.

Visible registration captures factory baselines in the state before returning to country scope.
The center row uses the existing fourteen aligned runtime arrays.
The companion changes the physical stage modifier without clearing the paid treatment.
It preserves project progress and Event 35 loss receipts on a merge.
A fresh proven collapse may reclose a Reopened or Restructured center and invalidates its current positive-resolution flag.
Paid completed-work receipts survive.
Abandoned, Liquidated, or Scarred outcomes are preserved when they represent a worse existing result.
Enum numeric order alone is not treated as deterioration order.

A new precommit state already seeded by the parent's selector returns created, without appending another row.
An existing active episode's state returns merged.
The state keeps the last visible source metadata and episode/receipt identities as compact history.
No unsecured or unconverted Event 34 legacy becomes a free reward.

## Receipt storage and lifecycle

The country-owned aligned arrays have prefix `great_depression_inherited_region_` and suffix `_entries`.
Their columns are episode_id, event34_episode_id, state_id, role, project_profile, project_stage, protection, fragility, control, damage, receipt_id, collapse_receipt_id, legacy_receipt_id, corridor_receipt_id, exhaustion, result, center_index, stage, live_control, civilian_baseline, and military_baseline.
All twenty-one lengths must agree.
The existing center arrays and center count must also remain aligned and bounded before registration.

Frozen control and current registration-time control are recorded separately.
A lost or transferred state does not become an active center for the source country and is not mutated under another country's episode.
The historical source receipt remains tied to the exact state.
The source country's national inherited counts and shock context remain in the parent's existing source ledger.
This companion does not create another country's national crisis or duplicate national pressure for a hidden row.

The receipt arrays are durable compact history and are intentionally retained after national recovery.
Country flags `great_depression_inherited_hidden_liability` and `great_depression_inherited_disconnected_liability` record that such historical receipts exist.
They are not current episode eligibility flags.
Active center runtime cleanup remains the existing Event 35 owner's responsibility.
No global event target is introduced.

## Helpers and call sites

| Helper | Scope | Inputs and outputs | Call sites and side effects |
| --- | --- | --- | --- |
| `great_depression_reset_region_outputs` | Country | Resets all companion outputs | Validation and Event 34 preparation |
| `great_depression_clear_region_inputs` | Country | Consumes inputs and private flags/scratch | All returns and rejected delivery, preserves receipts and outputs |
| `great_depression_validate_inherited_region` | Country | Validates exact country/state/episodes, frozen payload, arrays, capacity and receipt | Public companion and preflight, no gameplay state mutation |
| `great_depression_resolve_inherited_region_stage` | Country | Resolves stage from metadata and numeric floors | Private commit, no separate scheduling |
| `great_depression_apply_inherited_region` | Country | Creates or merges a center, or stores a hidden/ignored receipt | Public companion or existing national precommit |
| `great_depression_append_inherited_center` | Country | Appends the existing aligned center columns | Private commit only |
| `great_depression_apply_inherited_center_state` | Country entering exact state | Writes mapped physical stage and source memory | Private commit only, retains treatment/project/loss receipts |
| `great_depression_preflight_inherited_region` | Country | Rejects required regional failure through the existing main outputs | Both existing national branches before mutation |
| `great_depression_commit_inherited_region` | Country | Applies a validated region before source/history commit | Existing new-crisis success block and active deepening |
| `industrial_boom_freeze_inherited_region` | Country entering exact state | Freezes source pointer, metadata, baselines, actual control/damage and receipt | Existing collapse freezer before snapshot-frozen flag |
| `industrial_boom_prepare_inherited_region_request` | Country | Copies frozen contract and supplies target proof | Existing collapse request preparation |
| `industrial_boom_confirm_inherited_region_receipt` | Country | Verifies exact historical regional receipt on a national duplicate | Existing delivery helper before snapshot consumption |

The source snapshot survives the existing three-attempt delivery policy.
Preparation can refresh the predicted Event 35 ID for an uncommitted new crisis, but never changes the Event 34 episode, state, receipt, or frozen metadata.
Successful snapshot consumption requires both national success or a proven national duplicate and regional acceptance.
No post-return read of cleared main inputs is needed.

## Example

This example registers an additional proven state on a committed active Event 35 episode.
The example assumes its Event 34 source context is already committed on the current country.

```txt
set_variable = { great_depression_region_call_contract_supplied = constant:great_depression_region_contract.version }
set_variable = { great_depression_region_call_country_id = THIS.id }
set_variable = { great_depression_region_call_episode_id = great_depression_active_episode_id }
set_variable = { great_depression_region_call_event34_episode_id = great_depression_inherited_event34_episode_id }
set_variable = { great_depression_region_call_collapse_receipt_id = great_depression_inherited_event34_collapse_receipt_id }
set_variable = { great_depression_region_call_receipt_id = supplied_region_receipt }
set_variable = { great_depression_region_call_state_id = supplied_existing_state_id }
set_variable = { great_depression_region_call_role = constant:great_depression_region_role.primary }
set_variable = { great_depression_region_call_project_profile = constant:great_depression_region_profile.ordinary }
set_variable = { great_depression_region_call_project_stage = constant:great_depression_region_project_stage.completed }
set_variable = { great_depression_region_call_protection = constant:great_depression_region_protection.protected }
set_variable = { great_depression_region_call_fragility = constant:great_depression_region_contract.unavailable }
set_variable = { great_depression_region_call_control = constant:great_depression_region_control.connected }
set_variable = { great_depression_region_call_damage = constant:great_depression_region_damage.intact }
great_depression_register_inherited_region = yes
```

## Validation limits and integration work

Source-model scenarios and reference citations are recorded in [the implementation handoff](../../docs/plans/035_great_depression_plans/subagent_handoffs/inherited_region_contract_repair_2026-10-03.md).
They are not engine or observed campaign evidence.
MCP event lifecycle/render/compare evidence remains blocked.

The legacy Event 34 currently supplies one exact region and aggregate project, reserve, region, and shock counts.
It does not supply complete per-state project profiles/stages, protection/fragility histories, corridor rows, secured legacy receipts, or exhaustion histories.
The freezer records actual supplied actor/state fields when present, with state values taking precedence.
Missing metadata remains explicitly unavailable.
No additional state identities or regional project history are manufactured from aggregate counts.

The parent's initial selector must exclude another episode's reserved center or a conversion-forbidden state before it writes that state.
Its generic score pass currently has no such exclusion.
The companion's hidden disposition cannot undo a state already mutated by that separate selector.
This is a parent-owned integration blocker under the assigned write boundary.
The parent has accepted the regional source subject to this integration and engine evidence, and is adding one shared read-only state-permission helper across the viable pool, inherited seed, count and score gates.
That parent-owned permission integration is not independently claimed complete here.
The parent reports its new-crisis floor reset and activation/network/log deferral patch has landed.
That parent change remains outside this companion's independent engine-validation claim.
There is no new UI, icon, texture, localisation key, or workbook change in this contract.

The mapped ongoing liability, salvage, and corridor/recovery consumers remain accepted implementation requirements, not optional future extensions.
The [inherited-consumer audit](../../docs/plans/035_great_depression_plans/subagent_handoffs/inherited_consumer_completion_audit_2026-10-03.md) distinguishes those missing Event 35 consumers from the missing upstream Event 34 regional registries and secured-value payload.
Neither the missing consumers nor the missing upstream facts are implemented or claimed by this contract repair.
Engine evidence for current membership, pointer, and native modifier behavior also remains unresolved.
