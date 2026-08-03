# Event 016 next actionable gap: portal calibration and detection synergy

Date: 2026-08-03

Status: read-only completion audit; one bounded non-model gameplay tranche recommended. No gameplay, localisation, asset, model, or spreadsheet file was changed by this audit.

## Executive result

Event 016 remains partial rather than whole-event complete.

The highest-priority actionable requirement found outside the blocked native CBRN callback boundary and the deferred 3D packages is the accepted Electronics plus Teleportation cross-project synergy. The specification requires stable terminal calibration and portal detection, and requires cross-project synergies to unlock an event, decision, project variant, focus branch, unit support, or countermeasure instead of existing only as small modifiers. Current source uses Electronics as a Teleportation stage prerequisite but provides no persistent Electronics plus Teleportation synergy receipt, no host decision, and no calibration or detection consumer.

A bounded host-side Directorate decision can close one concrete part of that accepted portfolio contract without adding an event chain, project family, unit, model, CBRN interaction, or world scan.

## Binding requirement and current evidence

- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_3_project_portfolio.md:134` through `:148` says Electronics prototypes may detect portals and Electronics Deployment strengthens facility protection and foreign-agent detection.
- The same specification at `:284` through `:329` requires Teleportation Deployment to operate linked facilities with serious power and security burdens and lists terminal separation, independent dual control, calibration-archive destruction, and guarding both ends as counterplay.
- The cross-project table at `:713` through `:734` names `Electronics plus teleportation` as `Stable terminal calibration and portal detection` and explicitly requires synergy consumers such as decisions or countermeasures.
- `common/script_constants/016_brilliant_scientist_constants.txt:333` through `:348` fixes Electronics as family `2` and Teleportation as family `7`; their serialized stage entries are therefore `brilliant_scientist_project_stage_entries^1` and `brilliant_scientist_project_stage_entries^6`.
- `brilliant_scientist_can_begin_teleportation_deployment` in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:716` through `:735` already requires Electronics Prototype through `project_stage_entries^1`, High Energy Deployment through `project_stage_entries^4`, and a valid secondary facility. This is a prerequisite gate, not a synergy reward or countermeasure.
- `brilliant_scientist_apply_project_stage_outputs` in `common/scripted_effects/016_brilliant_scientist_project_effects.txt:320` through `:345` creates the ordinary transit network and later military-package receipts. It does not create an Electronics plus Teleportation calibration or detection receipt.
- `brilliant_scientist_refresh_project_accident_pressure` in `common/scripted_effects/016_brilliant_scientist_effects.txt:3486` through `:3535` accounts for stage pressure and the existing facility/custody reactions, but no project-synergy countermeasure.
- The current one-time cross-project implementation is the Paleogenetics plus Xenobiological review: `brilliant_scientist_convene_cross_domain_review` in `common/decisions/016_brilliant_scientist_directorate_synthesis.txt:12`, `chaosx.nr16.14` in `events/016_brilliant_scientist_synthesis_events.txt:10`, and its receipt effects in `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt`. Targeted scans found no equivalent Electronics plus Teleportation consumer in Event 016 decisions, events, scripted triggers, scripted effects, or localisation.

This is a missing accepted mechanic, not merely missing presentation. The existing project-stage prerequisites and individual project modifiers do not satisfy the explicit synergy-consumer requirement.

## Bounded patch recommendation

Implement one paid, one-time host decision in the existing Directorate category. Working identifiers are provided to make the ownership boundary exact; the parent may rename them before implementation if the final names remain stable across all consumers.

### Required identifiers

- Trigger: `brilliant_scientist_portal_calibration_network_is_ready`
- Cost trigger: `brilliant_scientist_can_pay_portal_calibration_network`
- Decision: `brilliant_scientist_establish_portal_calibration_network`
- Completion effect: `brilliant_scientist_complete_portal_calibration_network`
- Persistent country receipt: `brilliant_scientist_portal_calibration_network_established`
- Optional active-decision flag, only if needed for transfer-safe cancellation: `brilliant_scientist_portal_calibration_network_in_progress`
- Tuning rows: `brilliant_scientist_portal_calibration_network` and `brilliant_scientist_portal_calibration_network_ai`
- Player-facing keys: decision name, description, concrete cost text used by the availability tooltip, completion tooltip, and the receipt's countermeasure explanation under the same identifier family.

### Exact gameplay contract

The readiness trigger should require all of the following:

- `brilliant_scientist_is_current_host = yes`.
- Electronics at least Prototype and Teleportation at least Prototype, read from the canonical serialized stage array rather than inferred from modifiers.
- A valid primary facility and secondary facility.
- No global `world_end`, no terminal Event 016 state, no active containment transaction, no active family project incident, and no current Event 016 project-stage transaction.
- Neither project is suspended, damaged, dismantled, or physically unusable.
- The persistent receipt is absent.

The decision should consume a constant-defined Political Power, Support Equipment, fuel, manpower, and civilian-factory-time package. It should not grant a project stage, Project Capacity, equipment stockpile, free division, extra terminal, or second prototype reward.

On completion, the effect should revalidate the readiness trigger, set `brilliant_scientist_portal_calibration_network_established`, and add one concrete countermeasure consumer:

- When `brilliant_scientist_refresh_project_accident_pressure` is calculating pressure for the Teleportation family, subtract a constant-defined bounded calibration amount before the existing clamp.

The receipt should also improve the existing foreign-operation detection surface without creating a new foreign-operation family. `brilliant_scientist_foreign_calculate_operation_outcome` already retains the actor's exact `brilliant_scientist_foreign_selected_project_family`; inside the host scope at `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt:511` through `:591`, require that value to equal `constant:brilliant_scientist_project_family.teleportation`, subtract a bounded `portal_calibration_network` constant from the actor's success score, and add the matching bounded constant to detection score. The existing clamps at `:596` through `:605` remain authoritative. This must not guarantee detection, invalidate the existing theft/sabotage ledger, or expose unrelated project families. Do not substitute a generic research-speed modifier.

### Files to touch in the implementation tranche

| Surface | File | Required work |
| --- | --- | --- |
| Decision | `common/decisions/016_brilliant_scientist_directorate_synthesis.txt` | Add the one-time paid decision to the existing Directorate category. Reuse an already registered Directorate decision icon. |
| Triggers | `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt` | Add the exact stage, facility, state, receipt, and resource gates. |
| Effects | `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt` | Add the completion effect and receipt. |
| Accident consumer | `common/scripted_effects/016_brilliant_scientist_effects.txt` | Consume the receipt only for Teleportation inside `brilliant_scientist_refresh_project_accident_pressure`. |
| Foreign detection | `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | In `brilliant_scientist_foreign_calculate_operation_outcome`, add one host-receipt and actor-selected-family gate that lowers success and raises detection only for Teleportation-targeting operations. |
| Constants | `common/script_constants/016_brilliant_scientist_directorate_constants.txt` | Centralize duration, costs, pressure reduction, and AI weights. |
| Foreign score constants | `common/script_constants/016_brilliant_scientist_foreign_constants.txt` | Add `portal_calibration_network` values under both `brilliant_scientist_foreign_score` and `brilliant_scientist_foreign_detection`. |
| Transfer and formation | `common/scripted_effects/016_brilliant_scientist_effects.txt`; `common/scripted_effects/016_brilliant_scientist_country_effects.txt` | Copy the completed receipt with Event 016 project history. Do not restart a paid in-progress decision after transfer or formation; cancellation/refund behavior must be explicit. |
| Cleanup | Existing Event 016 terminal/character cleanup owner | Clear only an in-progress transaction flag. Retain the inert completed history receipt unless the project-history contract deliberately strips it. |
| Localisation | `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` | Add name, description, exact cost text, completion tooltip, and countermeasure explanation in UTF-8 with BOM. |
| Documentation | `docs/events/016_brilliant_scientist/systems/projects.md` | Record the stage gates, costs, receipt, transfer behavior, accident-pressure consumer, and no-model/no-CBRN boundary. |

No new report event ID, Event Log entry, evolution, super-event, news event, focus, KRG country route, achievement, special project, unit definition, equipment archetype, scripted GUI, DDS, `.mesh`, `.anim`, or spreadsheet row is required for this patch.

## Acceptance checks

1. A current host with Electronics Prototype and Teleportation Prototype, two valid facilities, and sufficient resources sees the decision exactly once.
2. A host missing either family stage or either facility cannot take the decision; unrelated project combinations do not qualify.
3. Starting the decision pays the documented cost and occupies the documented civilian factories for the documented duration.
4. Completion sets exactly one persistent receipt and grants no project stage, capacity, equipment stockpile, unit, or free terminal.
5. Recomputing accident pressure for Teleportation applies the exact bounded reduction before clamp; recomputing it for every other family is unchanged.
6. The foreign-operation score applies the exact success penalty and detection bonus only when the host owns the receipt and the actor's selected family is Teleportation; all other selected families are unchanged and the result remains probabilistic under the existing clamps and rolls.
7. Suspending, damaging, dismantling, or physically invalidating either qualifying project removes or disables the active countermeasure according to the documented policy; restoring the project does not replay the paid decision.
8. Transfer before completion cancels cleanly under the chosen no-refund or explicit-refund rule and does not duplicate the receipt. Transfer after completion copies the completed receipt once with the project history.
9. Kruger State formation does not replay the host decision or create a free terminal. If the completed receipt is inherited, its KRG use must remain limited to the same calibrated-network history unless a separate accepted KRG consumer is designed.
10. Terminal resolution and `world_end` prevent new starts, leave no active transaction, and do not alter the existing terminal or Fallout handoff.
11. The existing Paleogenetics plus Xenobiological `chaosx.nr16.14` review remains unchanged and independently reachable.
12. Focused decision inspection resolves the category, icon, scripted triggers, scripted effects, cost text, and localisation without missing identifiers.

## Surface status and non-findings

| Surface | Audit result |
| --- | --- |
| Project portfolio | Partial. All fifteen stage families and the existing Paleogenetics plus Xenobiological review are present, but the accepted Electronics plus Teleportation synergy has no gameplay consumer. |
| Foreign actions | Statically covered for the mapped action set, public challenge, and counter-Kruger programme. Quantitative pool evidence and live scenarios remain incomplete. The optional Teleportation detection factor above is a synergy consumer, not a new foreign action. |
| Containment | Statically covered for the current bounded host and KRG paths. Live territory-loss and cancellation acceptance remains open. |
| KRG package and project forces | Statically broad and playable. Five families use Event 019 provider adapters; portal and temporal have native capped recruitment, production, and strategic decisions. A complete unified recovery economy remains broader work, but it is not a smaller next patch than the synergy above. |
| Focus and decisions | The 100-focus KRG tree and mapped consumers are statically present. Route balance and live AI behavior remain unaccepted. |
| Terminal and world hooks | Static causality repairs are present. Competing-Fallout, capitulation, lost-state, no-remnant, and settlement scenarios remain acceptance gaps rather than a safe new content patch. |
| Country-specific settlements | The accepted finite ten-country `.5` transaction surface is statically implemented. Broader country-specific chains and more report/news presentation are explicitly queued optional content outside the accepted core boundary. |
| Biological stockpile and delivery | Blocked. The 2026-08-03 re-audit forbids an Event 016 ledger, production decision, debit, callback, or transfer/defeat cleanup until the native CBRN system exposes idempotent reservation, outcome, cancellation, and expiry callbacks. |
| Assets and 3D | Existing 2D coverage is broad; bespoke idea art and seven model packages remain separate deferred asset work. No asset is required for the recommended decision because an existing registered Directorate icon can be reused. |
| Documentation and catalog | Current documentation distinguishes core static coverage from deferred work. This handoff adds the newly identified accepted-spec gap. No catalog wording change is justified until gameplay exists. |

## Accepted-plan disposition

- Improvement recommendations R1 through R7 are recorded as closed and dispositioned; this audit does not reopen them.
- The finite ten-country settlement addenda are statically implemented; broader country chains remain queued optional content and are not the recommended patch.
- The biological stockpile and delivery addendum remains queued and blocked by the newer native CBRN lifecycle finding. The isolated-ledger wording in `016_core_runtime_handoff_map.md:20` and `:194` must not be interpreted as implementation authorization; `subagent_handoffs/016_krg_biological_stockpile_delivery_reaudit_2026-08-03.md:17` through `:21` is the current safety disposition.
- The portal calibration and detection recommendation comes directly from the still-binding project-portfolio specification. It is not a second improvement-loop plan and does not authorize the other listed synergy combinations automatically.

## Validation performed and limits

The audit compared the accepted project-portfolio requirements with the current Event 016 project decisions, stage triggers, stage effects, synthesis review, accident-pressure calculation, KRG portal/temporal decisions, Event 019 provider bridge, current source-of-truth map, completion status, and the latest biological re-audit. Targeted identifier scans found the existing Paleogenetics plus Xenobiological synthesis consumer but no Electronics plus Teleportation calibration/detection decision, receipt, effect, or localisation.

No Hearts of Iron IV process or live scenario was run. No probability normalization, campaign balance proof, or player-facing visual acceptance is claimed. No gameplay, localisation, asset, model, spreadsheet, or existing documentation file was edited; this handoff is the only new file.
