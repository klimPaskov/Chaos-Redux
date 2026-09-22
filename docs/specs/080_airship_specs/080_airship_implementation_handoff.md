# Event 080: Implementation handoff

This is a design-to-implementation handoff. It does not certify implemented runtime behaviour. All source specifications are the seven numbered parts in this folder. The source report distinguishes supplied-file reading, inspected repository excerpts, and unavailable dependencies.

## Priority and source conflicts

The current user brief overrides the stale catalog's Major classification and war-goal wording. Keep ID 80, Minor Fire-Once, Chaos 1, no cluster, and immediate war against the foreign crash controller. Update the authoritative workbook through its owner, then export the CSV. Do not edit the supplied CSV snapshot as though it were the workbook.

Preserve the actual route geometry and ordering. The inspected route trigger has departure index 0 and return index 121. The old mission advances daily and ends at index 120. Those runtime behaviours must change. The route itself must not be replaced to accommodate the old code.

## The voyage record

Use one bounded voyage record and one progression authority. It must persist physical position, canonical progress, pending travel time, phase, active form, Condition, current service order, actual and last-known locations, a manifest reference, and a unique terminal outcome. These are conceptual responsibilities, not proposed public helper names.

A flight transition first establishes the actual new position, evaluates its single exposure, and then resolves the arrival or terminal result. The success path at 121 runs only if the arrival did not produce a terminal failure. A crash at the final approach must not also award success. During a diversion, actual position differs from the pending canonical connection and remains authoritative for impact and host routing.

Retain partially consumed travel time through pauses. Persist scheduled outcomes and their cause identifiers so loading, reopening a window, switching standing orders, or a second country tick cannot reroll them. Pending country reports carry the relevant actual incident facts and cannot recompute a different impact controller later.

A terminal transition closes flight work exactly once. It does not clear shared fires, wars, settled population records, verified casualties, or ongoing independent recovery. Repeated terminal callbacks become no-ops for mechanics and rewards.

No daily or weekly full-world loop is acceptable for a single ship. Use the unique active record, the current host, the next necessary location, actual manifest cohorts, and a bounded registry of participating countries. The existing broad owner-region flags are migration inputs to retire, not a new authority to preserve.

## Route binding contract

The route crosswalk records inspected strategic-region predicates for indices 0 through 121. It is evidence of legacy ordering only. It does not provide exact state IDs, original stop flags, coordinates, or verified water classifications.

Recover those from the original map artwork, route assets, event source, and installed geography. Each canonical record needs a physical marker location, an exact state or verified open-water classification, its original stop status, service feasibility, and the next fixed connection. Map borders must be tied to geography without using a historical controller as the location key.

Validate every record. Pay particular attention to the absent land predicates at several indices, the index-1 discrepancy between the trigger and movement-effect region array, and the final map frame. `GFX_airship_trail_120` was found. A usable final 121 presentation was not verified. Do not claim it is absent without inspecting the asset registry and files.

An emergency diversion requires the same actual-location quality as a canonical point. A random owned state from a matched strategic region is not enough. Keep the route binding gate open until the 122 position records have been checked against the original map, including departure.

## Population and Deaths ownership

The required invariant is:

`resident population + live travel custody = conserved living population before births, actual deaths, and other independently owned population changes`

For each voyage cohort:

`boarded people + births = aboard + temporarily ashore + missing unconfirmed + rescued awaiting settlement + settled or returned + confirmed dead`

A person is represented in exactly one current state on the right-hand side. The cumulative settled or returned and confirmed-dead histories are not added to the live custody total.

The supplied registry documents `apply_exact_state_civilian_population_loss`. It is state-scoped and accepts a requested loss, a minimum remaining population, a reason, a Deaths logging policy, an optional target-country pair, and a supplied-contract proof. Its documented outputs include `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`. It clamps actual losses and reconciles recruitable manpower side effects.

For ground deaths, request the actual state loss with the appropriate Deaths registration policy and consume the returned applied amount. Do not register the same loss again through a separate path. For travel departure, the shared population owner must confirm a non-death transfer into persistent custody and its conservation treatment. For deaths in custody, the owner must register the real custody loss once without withdrawing those same people from a state again.

The package does not prove an existing full custody API. This adapter, the relevant reason and cause enums, country attribution, survivor settlement, births, missing-person persistence, and population-total treatment are release gates. Extend the owning shared system where necessary. Do not hide the gap by keeping an unbacked passenger integer.

Crew are civilians under this design. A service equipment cost does not remove crew from the recruitable manpower pool. Military personnel harmed in actual divisions use their native casualty owner, with no second civilian registration.

## Physical damage and fires

The supplied registry documents state-scoped `damage_state_building_dynamic`, with the caller supplying a building token and a bounded damage amount. The helper does not select a valid building or cap damage on behalf of the caller. Translate the design's percentages into verified native units and target only existing relevant capacity.

The old Airship code uses `launch_nuke` with `use_nuke = no`. Remove that shortcut. A crash is not a nuclear weapon, and its effects, pollution, casualty accounting, presentation, and camera treatment must not inherit unrelated nuclear behaviour.

For eligible fires, call the public `call_natural_disaster` gateway. The inspected owner overview uses regular targets named `natural_disaster_call_target_state` and `natural_disaster_call_target_country`, each with a corresponding supplied-proof input. It returns acceptance information, sequence identity, and resolved-target proofs. Read the complete current contract before coding exact arguments or enums.

Event 013 queues future impacts and owns its subsequent fire losses, building damage, reports, spread, and recovery. Airship applies its impact first and requests the subsequent fire once. An existing compatible fire card merges under the owner's policy. Event 80 retains history ownership of the voyage, while the external disaster sequence uses the appropriate no-extra-random-event-history policy.

Wildfire exists in the inspected owner documentation. A complete urban or industrial fire family was not verified. Resolve that through an existing verified owner or an owner-approved extension. Never bypass a forest-eligibility check or duplicate a spread engine to make the branch appear complete.

The exact native local-unit damage and casualty-reconciliation pathway also requires verification. The state, unit count, and strength limits in Part 4 are design requirements. Global stockpile deductions or army-wide modifiers do not satisfy them.

## Retaliation transaction

Snapshot the actual impact controller before reports, territory-changing callbacks, or later rescue transfers. Stop flight. Resolve the impact and its population facts. In the same crash-resolution transaction, declare the American war against that foreign controller if the war does not already exist. Send reports after the declaration is established.

A human popup is not the owner of the war effect. A news delay does not delay war. A current owner is not interchangeable with a controller. A controller's overlord is not interchangeable with the controller.

Test ally, faction leader, faction member, American subject, American overlord, shared overlord, truce, non-aggression pact, democratic declaration restrictions, and already-at-war cases. Determine the smallest supported relationship change for blocked cases and preserve unrelated countries. Do not state that all these cases work without runtime evidence.

When no United States or no foreign territorial controller exists, follow the explicit termination or domestic/open-water path. Do not spawn a replacement USA, choose the last host, or create an intermediate war goal.

## Interfaces and shared boundaries

The event-owned GUI entry is `airship_scripted_gui`, using a decision-category context. The inspected existing property points `placeholder_airship_map` to the `GFX_airship_trail_` family. Preserve that event-owned surface and original route assets where valid.

The UI worker may change Event 80's GUI, its directly required bindings, event-owned visuals, and its local decisions. It may not redesign the shared event log, event-details framework, settings, super-event framework, or unrelated country interfaces. A discovered shared defect requires an owner handoff.

Resource removal helpers documented in the supplied registry include support equipment, motorized equipment, convoys, trains, infantry equipment, and fuel. Their temporary amount inputs require careful resetting for every separate debit because helpers can negate them internally. Use only the resource types actually called for by the chosen service. Verify affordability inclusively and debit one payer once.

Technology rewards require the installed technology graph, `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare`. No new tree is planned. Verified category bonuses and the defined bounded XP conversion are preferable to a guessed technology identifier, while every unavailable research family must be reported.

## Existing Airship surfaces to reconcile

The repository inspection identified the event file, decisions, daily on-actions, scripted triggers, movement effects, scripted GUI, category definition, English localisation, and shared decision GUI and GFX files containing Airship blocks. The source report gives exact inspected paths and reading extent.

The old implementation's broad host selection, additive per-country risks, daily timing, early end, nuclear crash shortcut, fixed manpower losses, repetitive rewards, and popup-owned war do not meet this design. Reuse validated map art and route data without retaining those behaviours merely for compatibility.

No repository file was changed while preparing this package. Any migration of an active legacy save requires a separate explicit policy. A safe migration must preserve backed people and a single fire-once status, with an honest conversion report. Silently re-launching the voyage or duplicating its event record is not a migration strategy.
