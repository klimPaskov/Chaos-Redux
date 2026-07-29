# Event 016 Kruger State decision and mission audit

Date: 2026-07-24.

Scope: The eight Kruger State decision files, KRG category registration, shared KRG decision constants, triggers, effects, KRG events, decision localisation, narrow Event 016 helper call sites, and the decision-layer system note.

Status: patched locally; the parent accepted and this handoff now records the bounded four-mission pressure implementation. Nothing is staged or committed.

## Outcome

The audited KRG layer has centralized 1/2/4/6 civilian-factory bands, all 29 timed state-target decisions revalidate their selected state, all selectable decisions have AI intent, and all KRG decision/category/event text resolves in the supplied English localisation.

Two local defects were repaired. The parent rejected and corrected one proposed duration rewrite before accepting the tranche.

1. `brilliant_scientist_krg_recover_stolen_facility_archive` occupied two civilian factories but its foreign-operation availability helper did not include the matching standard-capacity gate.
2. `brilliant_scientist_krg_audit_restricted_material_custody` had the same two-factory gate omission.

The audit initially replaced the shared script-constant-to-temporary-variable duration used by `brilliant_scientist_krg_pay_expansion_maintenance` with a duplicated file-scoped literal. Parent review restored the required temporary-variable bridge, so the 180-day maintenance receipt remains sourced from `brilliant_scientist_krg_timing.reenable_long_days` without a second tuning value.

## Changed files and identifiers

- `common/decisions/016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt`
  - Preserved the engine-compatible temporary-variable bridge from `brilliant_scientist_krg_timing.reenable_long_days` into `set_country_flag.days`.
  - `brilliant_scientist_krg_recover_stolen_facility_archive` now requires `brilliant_scientist_krg_has_standard_factory_capacity = yes` in addition to the existing foreign-operation material gate.
- `common/decisions/016_brilliant_scientist_kruger_state_safeguard_decisions.txt`
  - `brilliant_scientist_krg_audit_restricted_material_custody` now requires `brilliant_scientist_krg_has_standard_factory_capacity = yes` in addition to the existing foreign-operation material gate.
- `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md`
  - Recorded the 1/2/4/6 capacity-band contract and the required timed-flag temporary-variable bridge.

Before the patch, the two foreign-operation decisions could start while fewer than two civilian factories were available despite their standard factory modifier.

After the patch, each of those workloads must have two available civilian factories, and the maintenance receipt continues to source its 180-day duration from the shared script constant through an engine-compatible temporary variable.

## Accepted hazardous-mission pressure implementation

The parent accepted the compact follow-up only for clone drift review, rogue-node containment, maintenance audit, and transit-breach closure.

Ministry consolidation and replacement remain passive by explicit parent direction.

Each accepted mission now has exactly one paid in-mission objective, shown only while that exact mission remains active:

| Mission | Objective | Operational proof | Objective cost and duration | Success and failure contract |
| --- | --- | --- | --- | --- |
| `brilliant_scientist_krg_clone_drift_review_mission` | `brilliant_scientist_krg_quarantine_and_sequence_clone_lineages` | Live cloning route, operational country receipt, and a controlled clone-growth site | Standard materials, two civilian factories, 60 days | Full result requires the objective receipt and proof; failure preserves costs, records `brilliant_scientist_krg_clone_drift_review_failed_ever`, applies a stability loss, and enforces a 90-day retry cooldown. |
| `brilliant_scientist_krg_rogue_node_containment_mission` | `brilliant_scientist_krg_isolate_rogue_machine_node` | Live robotics route, operational country receipt, and a controlled machine power node | Standard materials, two civilian factories, 60 days | Full result requires the objective receipt and proof; failure preserves costs, records `brilliant_scientist_krg_rogue_node_containment_failed_ever`, applies a stability loss, and enforces a 90-day retry cooldown. |
| `brilliant_scientist_krg_maintenance_audit_mission` | `brilliant_scientist_krg_service_primary_facility` | Intact, KRG-owned and controlled canonical primary facility target | Light materials, one civilian factory, 30 days | Full result requires the objective receipt and proof; failure preserves costs, records `brilliant_scientist_krg_maintenance_audit_failed_ever`, applies a standard stability loss, and enforces a 90-day retry cooldown. |
| `brilliant_scientist_krg_transit_breach_closure_mission` | `brilliant_scientist_krg_seal_transit_breach` | Live teleportation route, terminal-network receipt, and a controlled transit terminal | Standard materials, two civilian factories, 60 days | Full result requires the objective receipt and proof; failure preserves costs, records `brilliant_scientist_krg_transit_breach_closure_failed_ever`, applies stability and war-support losses, and enforces a 90-day retry cooldown. |

The new `brilliant_scientist_krg_timing.hazardous_mission_retry_days` is the central 90-day retry source.

The timed cooldown effects pass it through a temporary variable to `set_country_flag.days`, following the documented engine-compatible duration pattern.

World-end/category cancellation calls each objective cleanup helper and grants neither full nor failure receipts.

Objective receipts are transient and cleared at every terminal path; `*_objective_completed_ever` and `*_failed_ever` are permanent history only.

The existing full-completion receipts now also prevent rerunning their mission activators, closing the former reward-farming loop.

### Changed files and identifiers for the accepted follow-up

- `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`
  - `brilliant_scientist_krg_quarantine_and_sequence_clone_lineages`
  - `brilliant_scientist_krg_isolate_rogue_machine_node`
  - Clone-drift and rogue-node entry, cancellation, and timeout contracts.
- `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt`
  - `brilliant_scientist_krg_service_primary_facility`
  - Maintenance-audit entry, cancellation, and timeout contract.
- `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`
  - `brilliant_scientist_krg_seal_transit_breach`
  - Transit-breach entry, cancellation, and timeout contract.
- `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`
  - `brilliant_scientist_krg_timing.hazardous_mission_retry_days`.
- `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`
  - Four `*_operational_evidence_is_valid` and four `*_full_success_is_ready` readers.
- `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`
  - Four transient objective cleanup helpers and four contained-failure helpers.
- `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml`
  - Four objective title/description pairs and four public requirement tooltips.
- `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md`
  - Hazardous-mission lifecycle, requirements, history, cleanup, and retry contract.
- `docs/plans/016_brilliant_scientist_plans/016_krg_hazardous_mission_pressure_accepted_plan.md`
  - The accepted, pre-implementation bounded plan.

## Issue list, sorted by severity

| Severity | Status | Finding | Resolution |
| --- | --- | --- | --- |
| High | Corrected during parent review | The audit introduced a duplicated 180-day file-scoped literal for expansion maintenance. | Restored the required shared script-constant-to-temporary-variable bridge and removed the duplicate tuning value. |
| Medium | Fixed | The archive recovery and restricted-custody audit each used the standard two-factory modifier without a standard-capacity availability gate. | Added the shared standard-capacity trigger at both action entry points. |
| Medium | Fixed in accepted follow-up | Clone drift, rogue-node containment, maintenance audit, and transit breach closure were passive countdowns with no task-specific failure interaction after activation. | Added one paid objective, exact operational evidence, full-success proof, contained failure, history, retry cooldown, and terminal cleanup to each. |
| Low | Remaining presentation follow-up | Most factory/material availability checks are raw condition lists rather than contextual custom tooltips. | Add tier and material explanations only as a coordinated localisation pass, not as isolated one-off strings. |
| Informational | Validation limitation | `hoi4.event_inspect` did not return an artifact because the workspace reached `EVENT_ISSUE_LIMIT` at 23,525 issues, above its fixed 20,000 ceiling. | Source and caller review was used; the MCP evidence is unresolved rather than treated as a passing lint. |

## Decision category lifecycle notes

- Owner: the active sovereign KRG package only, through `brilliant_scientist_krg_decisions_are_active`; ordinary categories close under the all-actions/world-end locks.
- Reveal and pacing: ten categories are focus-flag gated, so foundation, project, foreign, integration, safeguard, and terminal actions appear as route work becomes relevant rather than as one debug-menu pool.
- Terminal exception: `brilliant_scientist_krg_terminal_program_category` uses `brilliant_scientist_krg_terminal_decisions_are_active`, preserving the required terminal-only actions after an ordinary terminal commitment closes the rest of the layer. See `016_decision_terminal_review_handoff.md` for the already accepted terminal lifecycle repair.
- State-target work: all 29 timed state-target decisions contain both a `target_trigger` and `cancel_trigger`; target ownership, control, exact facility role, and route validity are rechecked before a completion effect can write its receipt.
- Foreign targets: recognition, compact, submission, and intelligence decisions target capitals owned by the validated foreign country. The validity triggers exclude dead, invalid, subject, faction, and pending-resolution cases where applicable. KRG actor/target pointers are regular event targets for the immediate response event and do not become stale global selections.
- Temporal targets: the rescue chain uses the explicitly global `brilliant_scientist_krg_temporal_rescue_target` only while a rescue is active. Success and all failure/cancellation paths clear both the state binding and the global target.

## Mission quality notes

| Owner/category | Mission and region | Entry requirement and duration | Success | Failure, cleanup, and duplicate risk |
| --- | --- | --- | --- | --- |
| KRG / Clone and Machine | `brilliant_scientist_krg_clone_drift_review_mission`; controlled clone-growth site and country-wide registry work | Clone-drift and registry-repair focus gates, light materials and one available civilian factory; 90 days | Requires the paid 60-day standard-material lineage-sequencing objective and the controlled operational clone site, then writes the repaired-registry receipt and stability gain | Missing the objective or site proof writes the failure history, applies a stability loss, and starts the 90-day retry cooldown. World-end closure clears transient objective state without a result. The permanent full receipt prevents farming. |
| KRG / Clone and Machine | `brilliant_scientist_krg_clone_identity_pressure_mission`; clone polity | Fourth bounded clone cycle without all three institutional proofs; 90 days | The separate reconciliation action can remove the mission and write the resolved receipt | Timeout writes the permanent revolt disqualifier, applies losses, and fires event `.11`; one-time pressure/revolt flags prevent repetition. |
| KRG / Clone and Machine | `brilliant_scientist_krg_rogue_node_containment_mission`; controlled machine power node and network | Rogue-node focus gates, foreign-operation stores, and two available civilian factories; 90 days | Requires the paid 60-day standard-material machine-node isolation objective and the controlled operational node, then writes `brilliant_scientist_krg_rogue_nodes_contained` | Missing the objective or node proof writes the failure history, applies a stability loss, and starts the 90-day retry cooldown. World-end closure clears transient objective state without a result. The permanent full receipt prevents farming. |
| KRG / Clone and Machine | `brilliant_scientist_krg_ministry_replacement_mission`; country-wide machine administration | Machine-sabotage route gate and heavy materials/four available civilian factories; 180 days | Completes replacement and adds administration score | Ordinary layer closure clears the active flag; the completion receipt blocks repeats. It is a passive institutional clock. |
| KRG / Foundation | `brilliant_scientist_krg_ministry_consolidation_mission`; country-wide civil administration | Institutional-consolidation gate and two available civilian factories; 180 days | Completes consolidation and adds administration score | Ordinary layer closure clears the active flag; the completion receipt blocks repeats. It is a passive institutional clock. |
| KRG / Security and Logistics | `brilliant_scientist_krg_primary_facility_defense_mission`; exact primary facility | Intact, KRG-owned and controlled primary facility, light materials, and no active defense mission; 120 days | Writes the primary-defense completion receipt | Loss, destruction, or ownership/control change of the exact saved facility cancels with no receipt. The mission identity check prevents duplicates. |
| KRG / Foundation | `brilliant_scientist_krg_maintenance_audit_mission`; canonical primary laboratory | Maintenance focus gates and standard materials/two available civilian factories; 180 days | Requires the paid 30-day light-material primary-facility service objective and the intact controlled facility target, then writes maintenance completion and rebuilds the project-force runtime package | Missing the objective or facility proof writes the failure history, applies a standard stability loss, and starts the 90-day retry cooldown. World-end closure clears transient objective state without a result. The permanent full receipt prevents farming. |
| KRG / Portal and Temporal | `brilliant_scientist_krg_transit_breach_closure_mission`; controlled transit terminal | Breach-response focus gates and standard materials/two available civilian factories; 90 days | Requires the paid 60-day standard-material breach-sealing objective and the controlled operational terminal, then marks the breach closed and grants stability | Missing the objective or terminal proof writes the failure history, applies stability and war-support losses, and starts the 90-day retry cooldown. World-end closure clears transient objective state without a result. The permanent full receipt prevents farming. |
| KRG / Portal and Temporal | `brilliant_scientist_krg_temporal_rescue_survival_mission`; exact saved capital or singularity state | A committed bounded warning with exact target, synchronization charge, debt charge, and a valid target; 60 days | Completes rescue survival, clears the target pointer, then begins canonical stabilization | Civil war, target loss, role loss, or invalid temporal evidence fails the rescue and clears every unfinished target receipt and global target. One target ID/use record prevents farming. |
| KRG / Portal and Temporal | `brilliant_scientist_krg_temporal_stabilization_supervision_mission`; temporal anchor program | Stabilization pending plus six available civilian factories; 120 days | Completes stabilization and clears the post-rescue obligation | A rescue-linked civil war invokes the rescue failure helper; normal cancellation clears active state. The active receipt prevents duplicate missions. |
| KRG / Terminal Program | `brilliant_scientist_krg_singularity_disarmament_hold_mission`; global terminal verification | Dismantlement proof, no armed/fail-deadly state, standard materials, and six available civilian factories; 180 days | Writes the hold-complete receipt and refreshes threat state | Any loss of terminal validity, rearming, fail-deadly state, or world-end closure cancels and clears active state. The completed hold flag blocks farming. |

## Cost and requirement clarity notes

`common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt` defines exact light/standard/heavy/strategic occupancy as 1/2/4/6 factories, with availability gates 0/1/3/5 and therefore exact required free capacity of 1/2/4/6.

The material helpers correctly bundle matching capacity: light, standard, heavy, and project-batch actions use their corresponding capacity trigger. The two foreign-operation actions above needed direct standard gates because `brilliant_scientist_krg_can_pay_foreign_operation_cost` deliberately checks convoys, support equipment, and fuel but not factories.

Static coverage after the patch found 74 factory-work entries, including 63 selectable decisions and 11 hidden missions. Every selectable factory workload now carries its matching capacity either directly or through the relevant material helper, with zero mismatched tiers.

All 134 decision/mission ids and all 10 category ids have primary English localisation. Category descriptions, event title/description pairs, and six referenced custom-tooltip keys also resolve in the supplied English file. The existing strings explain the narrative action well, but generic raw material/factory conditions would be easier to understand through shared tier-specific custom tooltips in a future coordinated localisation pass.

## AI validity and route-lock notes

- All 119 selectable KRG decisions define `ai_will_do`; the 11 hidden missions deliberately have none because AI reaches them only through their activating action or event effect.
- The mission activators that consume a factory burden perform their own material/capacity checks before calling `activate_mission`, which is necessary because the effect bypasses normal mission activation logic.
- Each foreign and state-target decision contains a target-validity contract, and the saved temporal target is revalidated through its full survival window.
- The human scientific-republic exception and the canonical biological route locks remain in the existing safeguard/raid authority surface; this audit did not widen hostile biological authority or create an AI-only action.
- The terminal layer maintains the already accepted live-map audit model: `every_state` and `every_country` occur only in the explicit terminal audit helper, not in any daily, weekly, or monthly on-action.

## Cleanup and exploit-risk notes

- The clone, robot, paleogenetic, xenobiological, portal, exotic, and temporal batch actions use finite counters, stockpile-only output, canonical template/force caps, and re-enable windows. No free-unit loop was found in this layer.
- The clone crisis has a permanent historical disqualifier and one-time resolution state, so reconciliation cannot erase an already recorded revolt.
- The temporal rescue helper clears the exact global target and bound-state flag on preparation failure, mission cancellation, target loss, and mission success.
- State-target cancellation is fail-closed: no work is redirected and no completion reward is granted after a target becomes invalid.
- Terminal world-end cleanup, terminal route locks, arming/disarmment, and map-proof checks were reviewed against the accepted terminal handoff rather than altered again.
- `brilliant_scientist_krg_clone_growth_burden_active`, `brilliant_scientist_krg_machine_power_burden_active`, and similar uncleared `*_active` flags are durable route burdens or identities, not stale mission flags. They should remain documented as persistent state if player-facing presentation expands.

## Compact improvement handoff disposition

The parent accepted the exact four-mission portion of this recommendation, and its complete implementation is recorded above and in `016_krg_hazardous_mission_pressure_accepted_plan.md`.

Ministry consolidation and ministry replacement remain passive clocks; no new currency, category, scripted GUI, or broader mission system was accepted.

The player-facing promise of clone drift review, rogue-node containment, ministry transition, maintenance audit, and breach closure is active emergency management. At present, five of those actions mainly exchange an upfront resource cost and factory occupation for an automatic timeout receipt. The clone identity pressure, primary-facility defense, temporal rescue, temporal stabilization, and terminal disarmment missions already demonstrate stronger pressure through an early remediation action, exact target survival, route state, or terminal invalidation.

The accepted implementation was kept under the existing categories rather than adding a category or scripted GUI:

1. Clone drift, rogue-node, maintenance, and transit closure each received one existing-system paid objective tied to the named operational evidence.
2. Each now resolves as full success only on objective receipt plus live evidence; otherwise it applies a contained failure with sunk costs, history, consequence, and retry cooldown.
3. Ministry consolidation and replacement remain deliberate administrative clocks because no concrete domestic opposition or control value was accepted for them.
4. AI uses the same objective availability contract as the player and has no hidden auto-success path.
5. Each objective has a public custom tooltip stating the exact active-mission, operational-evidence, material, fuel, and factory requirements.

The bounded design plan, localisation, AI conditions, cleanup proof, and source-level scenario review are complete for the accepted four-mission scope.

## Meaningful validation

- Reviewed the offline decision/effects documentation and vanilla Afghanistan/Australia mission precedents before implementation. The four objective decisions use the documented active-mission gate, timed decision completion, and cancellation pattern rather than activating a second mission or adding a GUI fallback.
- Confirmed each of the four original full-completion receipts has exactly one setter and that it occurs only in the relevant objective-plus-operational-evidence timeout branch.
- Confirmed each permanent `*_failed_ever` receipt has exactly one setter and no clearer.
- Confirmed all four objectives contain active-mission visibility, active-mission cancellation, and active-mission completion checks; one public custom-tooltip block; and `brilliant_scientist_krg_ai.preferred` AI intent.
- Confirmed the four new objective IDs each have exactly one gameplay definition and one English localisation definition, and the localisation file retains its UTF-8 BOM.
- Confirmed the 90-day `hazardous_mission_retry_days` constant is passed to each timed retry flag through a temporary variable, matching the documented timed-flag compatibility pattern.
- Compared the timed-flag implementation with the offline decision/effects documentation and Event 016 Directorate precedent. Expansion maintenance and all four hazardous-mission retry cooldowns source their durations from script constants through temporary variables.
- Performed a source-level capacity coverage audit: all 74 factory-work entries were classified by modifier tier, and every one of the 63 selectable factory workloads now reaches its matching 1/2/4/6 capacity gate directly or via its material helper. No tier mismatch remains.
- Confirmed all 29 timed state-target decisions have both `target_trigger` and `cancel_trigger`.
- Confirmed all 134 KRG decision/mission IDs and all 10 category IDs have primary English localisation, all 10 categories have title and description localisation, and all 19 KRG events have title and description localisation. The localisation file retains its UTF-8 BOM.
- Confirmed the scoped `set_country_flag.days` scan no longer finds a variable-token duration in KRG decision/effect/event sources.
- Reviewed the KRG foreign event callers and event `.61`, `.63`, and `.64` scope transitions. The regular `brilliant_scientist_krg_foreign_actor` target is intentionally the KRG actor, and the `set_autonomy` call in `.64` correctly makes the foreign event root a KRG subject.

## Skipped or blocked validation

- `hoi4.event_inspect` was attempted for the scoped KRG event file and again for `chaosx.nr16.64`. Both calls stopped at `EVENT_ISSUE_LIMIT` with 23,525 workspace issues against a 20,000 maximum, produced no artifact, and cannot be cited as a pass.
- The decision-AI probability MCP could not be evaluated because its runtime source schema rejected both the scoped relative-path object and direct path string. The source-level AI contract was reviewed instead; no score, random-list, or MTTH factor was introduced by this tranche.
- No decision-owned scripted GUI is referenced by the audited KRG decision files. `hoi4.gui_inspect` and `hoi4.gui_render` were therefore not applicable, and no GUI artifact or rewrite was produced.
- No live game scenario was run. Runtime confirmation of timeout ordering where an objective finishes on the exact final mission day remains a parent/live-test responsibility.

## Remaining issues and parent actions

1. The accepted four-mission improvement is fully implemented. Ministry consolidation and replacement remain intentionally passive, as directed; they are not a missing route in this tranche.
2. Consider a shared localisation pass for factory-band and foreign-operation material requirements outside the four objectives. This should add reusable tooltips, not expose raw long triggers on dozens of buttons.
3. Re-run `hoi4.event_inspect` only after the MCP workspace issue ceiling is reduced or its scope limiter is repaired; current MCP output contains no graph or lint artifact.

No unrelated gameplay files, GUI files, assets, categories, terminal mechanics, focuses, spreadsheets, or ministry mission contracts were changed. No simplification, fallback, or replacement was used in the accepted four-mission patch.

## Parent review disposition

Parent review accepted the four hazardous-mission objectives, their exact operational-evidence triggers, sunk-cost failure branches, permanent history, 90-day retry cooldowns, and ordinary lifecycle cleanup.

The review corrected the audit's expansion-maintenance duration regression as recorded above. The two foreign-operation capacity fixes remain accepted.

The completed KRG icon package is wired to all 134 decision and mission consumers and all 10 category consumers. The four post-package objective IDs use the existing semantic families `biological_quarantine`, `emergency_containment`, `foundation_repair`, and `portal_terminal`; their assignments were added to the package generator and ledger.

The package validator reports 40 distinct decision textures, 10 distinct category textures, 134 unique decision/mission assignments, 10 unique category assignments, and status `ok`. Source review found no remaining generic KRG decision or category icon consumer, and all 50 registered sprite textures exist.

The exact-day timeout ordering noted under skipped validation remains a live-runtime uncertainty and is not represented as acceptance evidence.
