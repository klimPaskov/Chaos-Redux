# Event 080: Implementation handoff

This handoff turns the seven numbered parts into implementation contracts and owner boundaries. It does not certify implemented runtime behaviour.

## Priority and source conflicts

The current user brief overrides the stale catalog's Major classification and war-goal wording. Keep ID 80, Minor Fire-Once, Chaos 1, no cluster, and immediate war against the foreign crash controller. Update the authoritative workbook through the `chaos-redux-xlsx` workflow and then regenerate the CSV exports.

Preserve the actual route geometry and ordering. The legacy route trigger has departure index 0 and return index 121, while the old mission advances daily and ends at index 120. Those runtime behaviours must change; the route itself must not be replaced to accommodate the old code.

## The voyage record

Use one bounded voyage record and one progression authority. It persists physical position, canonical progress, pending travel time, phase, active form, Condition, current service order, actual and last-known locations, the boarding-group manifest, and a unique terminal outcome. These are conceptual responsibilities, not proposed public helper names.

A flight transition first establishes the actual new position, evaluates its single exposure, and then resolves the arrival or terminal result. The success path at 121 runs only if the arrival did not produce a terminal failure. During a diversion, actual position differs from the pending canonical connection and remains authoritative for impact and host routing.

Retain partially consumed travel time through pauses. Persist scheduled outcomes and their cause identifiers so loading, reopening a window, switching standing orders, or a second country tick cannot reroll them. Pending country reports carry the incident facts and cannot recompute a different impact controller later.

A terminal transition closes flight work exactly once. It does not clear shared fires, wars, registered deaths, or ongoing independent recovery. Repeated terminal callbacks are no-ops for mechanics and rewards.

No daily or weekly full-world loop is acceptable for a single ship. Use the unique active record, the current host, the next necessary location, and a bounded registry of participating countries. The existing broad owner-region flags are migration inputs to retire, not a new authority to preserve.

## Route binding contract

The [route crosswalk](080_airship_route_crosswalk.md) records the legacy strategic-region predicates for indices 0 through 121. It is evidence of legacy ordering only and provides no exact state IDs, stop flags, coordinates, or verified water classifications.

Recover those from the original map artwork, route assets, event source, and installed geography. Each of the 122 records needs a physical marker location, an exact state or verified open-water classification, its original stop status, service feasibility, and the next fixed connection. Pay particular attention to the positions without a land predicate, the index-1 discrepancy, and the final map frame. An emergency diversion requires the same location quality; a random owned state from a matched strategic region is not enough.

## Population and Deaths

Travellers stay resident in their origin state while aboard (Part 3), so no custody balance, in-transit population, or settlement transaction exists. The manifest is a small list of boarding groups, each with its boarding state, the controller at boarding, and a count. The required invariant is:

`boarded people + births and stowaways = aboard + disembarked + confirmed dead + presumed lost`

Deaths use the documented state-scoped `apply_exact_state_civilian_population_loss`, which accepts a requested loss, a minimum remaining population, a reason, a Deaths logging policy, and an optional target-country pair, and returns `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`. Onboard, rescue, and presumed-loss deaths are split across boarding groups in proportion to their counts and debited from each origin state once with Deaths registration. Ground deaths at the impact site are debited from the impact state. Reports always use the applied amount. Do not register any loss again through a second path.

Crew are civilians in the departure group. A service equipment cost does not remove crew from recruitable manpower. Military personnel harmed in actual divisions use their native casualty owner, with no second civilian registration.

## Physical damage and fires

`damage_state_building_dynamic` is state-scoped, with the caller supplying a building token and a bounded damage amount; it does not select a valid building or cap damage. Translate the design's percentages into verified native units and target only existing relevant capacity.

The old Airship code uses `launch_nuke` with `use_nuke = no`. Remove that shortcut; a crash must not inherit nuclear effects, pollution, casualty accounting, presentation, or camera treatment.

For eligible fires, call the public `call_natural_disaster` gateway with the targets `natural_disaster_call_target_state` and `natural_disaster_call_target_country` and their proof inputs, and read the complete current contract before coding exact arguments. Event 013 queues future impacts and owns subsequent fire losses, damage, reports, spread, and recovery. Airship applies its impact first and requests the subsequent fire once, under a no-extra-history policy. Wildfire exists; urban and industrial fire coverage must come from a verified owner or an owner-approved extension, never by bypassing a forest-eligibility check.

Nearby-unit damage must use a verified native pathway within the state, unit count, and strength limits of Part 4. Global stockpile deductions or army-wide modifiers do not satisfy it.

## Retaliation transaction

Snapshot the actual impact controller before reports, territory-changing callbacks, or later rescue transfers. Stop flight, resolve the impact and its deaths, and in the same transaction declare the American war against that foreign controller if the war does not already exist. Send reports afterwards. A popup never owns the war effect, an owner is not interchangeable with a controller, and a controller's overlord is not interchangeable with the controller.

Test ally, faction leader, faction member, American subject, American overlord, shared overlord, truce, non-aggression pact, democratic declaration restrictions, and already-at-war cases. Determine the smallest supported relationship change for blocked cases and preserve unrelated countries. When no United States or no foreign territorial controller exists, follow the explicit termination, domestic, or open-water path.

## Interfaces and shared boundaries

The event-owned GUI entry is `airship_scripted_gui` in a decision-category context, with `placeholder_airship_map` pointing to the `GFX_airship_trail_` family. Preserve that surface and the original route assets where valid. The event UI worker owns Event 80's bounded layout, presentation-only bindings, event-owned visuals, and GUI localisation; the parent keeps decision gameplay, costs, outcomes, AI, and balance. Shared event log, event details, settings, and super-event framework surfaces stay with their owners.

Resource removal helpers exist for support equipment, motorized equipment, convoys, trains, infantry equipment, and fuel. Their temporary amount inputs must be reset for every debit because helpers can negate them internally. Verify affordability inclusively and debit one payer once.

Technology rewards need the installed technology graph. No new tree is planned; the bounded Air Experience conversion in Part 5 replaces any unavailable research family.

## Specialist routing

| Role | Bounded assignment |
|---|---|
| `chaosx_repo_explorer` | Recover the 122 route records, original stop flags, final map frames, and every active legacy Airship surface |
| `chaosx_scripted_system_architect` | Review the voyage authority, boarding-group deaths, fire handoff, unit damage, and war preconditions without creating event-local duplicates of shared systems |
| `chaosx_decision_mission_auditor` | Audit services, emergencies, missions, payers, timers, partial delivery, and AI |
| `chaosx_event_ui_worker` | Implement the preserved map and task panel after reference acceptance |
| `chaosx_ai_probability_auditor` | Evaluate the probability scenarios in the validation matrix against the implemented behaviour |
| Asset roles | Reports, news, ship forms, icons, and achievements through the asset prompt |
| Super-event researchers | Final Flying City text and licensed audio through the super-event prompt |
| `chaosx_localisation_auditor`, `chaosx_event_completion_auditor`, `chaosx_documentation_curator`, `chaosx_spreadsheet_doc_worker` | Final text, independent completion review, documentation, and the workbook row |

No country package, focus tree, portrait, or 3D model is planned, so those roles are not assigned. Implementation records and specialist handoffs belong under `docs/plans/080_airship_plans/`.

## Existing Airship surfaces to reconcile

The legacy implementation spans `events/080_airship.txt`, its decisions, category, daily on-actions, scripted triggers, movement effects, scripted GUI, English localisation, and the shared decision GUI and GFX blocks. Its broad host selection, additive per-country risks, daily timing, early end, nuclear crash shortcut, fixed manpower losses, repetitive rewards, and popup-owned war do not meet this design. Reuse validated map art and route data without retaining those behaviours. A legacy save with an active voyage needs a separate explicit migration policy that keeps a single fire-once status.
