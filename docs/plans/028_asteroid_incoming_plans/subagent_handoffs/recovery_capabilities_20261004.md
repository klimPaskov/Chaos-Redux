# Event 028 recovery capabilities and F08/F09/F10 research, 2026-10-04

## Disposition, authority, and freeze

This document persists the completed read-only supplied-garrison investigation and mission/cost research for parent review.
The user authorized this new document only after the research was returned inline.
No gameplay source, localisation, weights, archives, attributes, wrappers, or other documentation was edited during this persistence step.
The document is frozen after writing.

The Event 028 implementation scope remains partially completed.
No direct route selection, province-path repair, national network reconstruction, regional capacity restoration, dynamic quote implementation, or mission failure implementation was performed by this research tranche.
The existing six-action crater source remains WIP and uncommitted.
The parent had not integrated its recovery wrappers when these findings were returned.
The parent owns the five non-security wrapper integrations and emergency-expiry integration.
Perimeter security still requires a verified supplied-local-division contract, and no fallback was approved.

Accepted mission scopes and consequences below are taken from the user-authorized Part 6 and Part 10 contract, the decision/mission prompt, Part 3's rescue and closeout rules, and the tuning matrix.
The receipt layouts, formula shapes, ranking rules, and proposed constant names are implementation proposals for the parent.
Where the specs leave a numeric threshold, coefficient, cap, ranking metric, or duration detail open, it is a parent-owned tuning choice within the accepted contract.
No particular proposed value or ranking rule is promoted to accepted design by this handoff.
This research does not authorize changing AI weights without the required baseline, owner patch, and probability comparison.

Skills applied were `chaos-redux-decisions-missions` and `chaos-redux-events`.
Neither skill was changed.
No HOI4 launch, live test, save inspection, commit, or completion claim occurred.

## Supplied-garrison capability result

Actual state-local division iteration is verified.
The missing verified capability is a trigger or dynamic-variable reader for each division's current supplied status in that iterator's division context.
The absence of a documented or source-used getter is a scripting capability gap, not definitive proof that the engine has no undocumented implementation.

| Surface | Verified capability | Limit for the security gate |
| --- | --- | --- |
| `every_state_division` | STATE-scoped effect iterator executing child effects on every division currently in the state that passes `limit` | Physical iteration alone provides no supplied-status filter |
| `any_state_division` | STATE-scoped trigger testing whether any division meets its child triggers | Needs a verified division supply-status child predicate to meet the supplied-garrison contract |
| `divisions_in_state` | COUNTRY-scoped count of that country's divisions in a specified state, with type/unit filters | Counts physical presence and has no documented supplied filter |
| `unit_strength`, `unit_organization` | Documented unit-context numeric triggers | Strength and organization do not prove current supply |
| `division_has_battalion_in_template`, `division_has_majority_template` | Division composition predicates used by vanilla | Template composition does not prove supply |
| `is_unit_template_reserves` | Offline wiki describes a division's lowest supply-priority setting | Priority is distinct from received supply |
| `has_combat_modifier` | Installed documentation declares COMBATANT scope | No verified general division-state supply gate follows from it |
| `supply_units` | CHARACTER-scoped effect granting supply hours to units controlled by a leader | A supply grant is not a read-only supplied-status getter |
| `out_of_supply_factor` | Modifier scalar changing out-of-supply penalties | It does not report a particular division's current supply state |

The installed dynamic-variable catalogue lists global, country, state, unit-leader, military-industrial-organization, and special-project scopes, with no division catalogue section.
Its country `num_divisions` reader is a national count and does not establish local supplied divisions.
The installed unit triggers include strength and organization, so the investigation did not infer the supply gap solely from a position-count trigger.

Direct installed-source searches covered `documentation`, `common`, and relevant `interface` files for `unit_supply`, `division_supply`, `supply_ratio`, `current_supply`, `supply_status`, `is_in_supply`, `has_supply`, and `is_supplied`.
The broader source search found native internal defines including `DIVISION_SUPPLY_RATIO_TO_MOTORIZE` and supply GUI widgets.
Those show internal engine supply handling, but expose no verified Clausewitz getter invocation.
The source matches for `ITA_re_out_of_supply` are normal country variables assigned by a focus and consumed by `out_of_supply_factor` in country dynamic modifiers.
They are policy modifier values, not live division observations.

Current vanilla examples inspected were `SF_PARA_combat_effect`, which iterates state divisions and changes organization after an owner-war filter, the Norwegian decision's owner/faction test inside `any_state_division`, and the elephant-template achievement's `division_has_battalion_in_template` test.
None reads current supplied status.
No arbitrary `unit_supply` variable, national supply-average proxy, national army-size substitute, strength substitute, or organization substitute was implemented or accepted.
The existing crater position-only predicate remains explicitly insufficient for secure-perimeter acceptance.

Local state modifiers are available.
Installed `add_dynamic_modifier` documentation supports STATE scope and an optional country restriction, with an example applying a modifier to one state only for GER.
Vanilla `dam_blown_modifier` is a state modifier using `local_supply_impact_factor`.
Therefore a bounded local supply consequence is implementable, while a supplied-local-division requirement still lacks a verified script contract.

## Accepted mission scopes and current source gaps, F09

The existing source duration constants are retained below as implementation anchors, not newly selected tuning.
The specs prescribe rescue timing in the 120 to 180 day band and national network timing in the 180 to 365 day band.
The other exact source durations remain current values for parent review.

| Mission | Current anchor | Required objective proof | Accepted consequence and remaining choice |
| --- | ---: | --- | --- |
| Keep the rescue route open | 150 days | Freeze the worst surviving impact state and named route from replacement capital or safe hub, then maintain required route and supply conditions continuously | Success removes part of national burden, upgrades local recovery, and reduces later emergency costs for that state. Failure extends recovery, causes a bounded rescue-period Deaths entry, and applies temporary supply pressure. Exact supplied-flow observation remains unverified |
| Stabilize the damaged zone | 120 days | Freeze two distinct worst affected states and check the named repair thresholds in both | Success moves reconstruction earlier. Failure worsens one frozen member and keeps emergency response open. Ranking and public threshold selection remain parent tuning choices |
| Reconnect the national network | 180 days | Freeze capital, major-industry endpoints, damaged-state membership, and required links, then prove the whole defined network | Success replaces national recovery with a lighter form and closes obsolete emergency decisions. Failure extends national recovery and increases future repair costs temporarily. Endpoint selection and exact network set are not implemented |
| Restore the outer ring | 270 days | Freeze all applicable Ring 3/light-fragment members and the Ring 2 comparison group, remove the outer/light timed burdens across the full set, and meet the Ring 2 burden ceiling | The full-set completion supports the survival achievement. The Ring 2 burden metric and threshold are unselected. Part 6 does not define a distinct failure penalty |
| Rebuild the regional economy | 365 days | Original target country only, with its frozen incident region outside the permanent main crater and matching industrial/logistical percentage baselines | Success grants a lasting measured recovery legacy. Region membership, comparison shares, and a distinct failure consequence are not selected by the specification |

Government Beyond the Crater retains its specified national-network and outer-ring proofs, original-target survival, replacement-capital control, and deadline.
Current event source sets `global.asteroid_incoming_achievement_deadline_day` to impact day plus 1,095 days, and the deadline trigger uses a strict less-than comparison.
The regional economy mission is not added to that achievement's stated prerequisite map.
National completion flags must only be published after full objective proof, because the government achievement consumes those flags.

Current mission predicates all use one `asteroid_incoming_recovery_target_state`.
Stabilization therefore does not cover two states, network completion does not prove the national network, outer-ring completion does not cover all outer/light states, and regional completion does not compare a restored capacity share.
Existing deadline checks postpone those one-state tests but do not supply the missing coverage.
The current shared success helper also grants national legacy after a local success, although rescue, stabilization, national-network, and regional consequences have different accepted roles.

The source local floors are `infrastructure > 3`, `rail_way > 1`, and `supply_node > 0`, corresponding to levels 4, 2, and 1 for integer levels.
These are existing implementation anchors, not approved national or regional percentage targets.
A target that had no pre-impact railway or supply node must not be forced into an unrelated new-building requirement through automatic application of all three floors.
Applicability and exact public thresholds must follow the frozen route and pre-impact capacity contract.

`has_railway_connection` is verified as an existing-connection predicate with explicit province paths or endpoint states/provinces.
It does not document actual live supply throughput to divisions.
Operational route/hub readings and reserve checks can prove those particular requirements, but cannot silently stand in for an unverified supplied-status condition.

## Exact incident-set and reservation proposal

The existing country-local reservation remains the owner of mission state.
`asteroid_incoming_recovery_target_state` remains its selected anchor, rather than becoming a global pointer or another actor's reservation.
The proposed extension stores a country-owned objective state set, route endpoints or province paths, incident ID, mission kind, actor identity, contract receipt identity, expected member count, start date, deadline, required hold period where applicable, and one result-consumed receipt.
These fields are proposed, with no source patch or new branch ID.

Incident membership should require the exact `asteroid_incoming_state_transaction_id`, `asteroid_incoming_state_transaction_applied`, `asteroid_incoming_affected_state`, and `asteroid_incoming_preimpact_snapshot_recorded` receipts.
Use the actual assigned strongest profile once per state.
The permanent main crater is ineligible for reconstruction.
Current recovery source excludes the main crater rather than blanket-excluding surviving fragment-center states.
Do not narrow the full accepted reconstruction set to an arbitrary subset merely to simplify implementation.

Global planning footprint arrays and affected-country entry arrays are cleared by transaction cleanup.
The state transaction ID and applied/snapshot receipts remain, and `global.asteroid_incoming_last_transaction_id` retains the completed incident ID.
The mission must freeze its own incident identity and set rather than depending on cleared planning arrays or a later global selection.

Set membership and denominators must not shrink when a member is lost, annexed, or transferred.
Current control is a live validity requirement applied to the frozen membership.
Cancellation or an accepted transfer path must use the owning actor and exact contract identity.
Completed incident/group receipts must survive ownership changes so annexation cannot reopen the same reward.

The country loss totals are credited to both owner and distinct controller for occupied states.
They are report totals, not a deduplicated geographic denominator.
No durable per-state original incident-owner/controller field was found in the inspected snapshot contract.
If regional membership is based on original responsibility or territory, the parent must retain that association during the incident before transient reporting context is cleaned up.
The choice of original owner, operational controller, or explicitly defined original-target region must follow the accepted country/region interpretation.
It remains an implementation choice to resolve, rather than an assumed current-control filter that can exclude lost states.

For stabilization, at least two distinct eligible members are required.
One-state fallback completion is not accepted.
The source severity ordering is main Ring 1 at 60, fragment center at 50, main Ring 2 at 40, fragment Ring 1 at 30, main Ring 3 at 20, and fragment Ring 2 at 10, with permanent main center excluded.
A proposed deterministic ranking may start from that order, then expected preventable rescue loss, measured repair deficit, and stable state ID.
That complete ranking rule has not been selected or accepted.
For hospital/rescue selection, current surviving population, the existing rescue fraction, and remaining rescue months are available to measure expected continuing need.

For the outer-ring proof, actual main Ring 3 and fragment Ring 2 profiles define the corresponding outer/light applied burdens, with main Ring 2 forming the stated Ring 2 comparison group.
Original geometric overlap and actual strongest-profile assignment must not count a state twice or invent a second applied burden.
The Ring 2 measure itself remains unselected.
`asteroid_incoming_state_rescue_burden` stores remaining rescue months and cannot automatically represent all industrial/logistical recovery burden.

The existing no-active-recovery gate serializes Event 028 paid state projects while a mission is active.
This proposal preserves that ownership contract.
Native construction must be able to meet the frozen objective, or the parent must explicitly introduce child work inside the same mission reservation before allowing additional Event 028 paid work.
An independent new project must not overwrite the mission's anchor or set.
No such child-work or direct-route implementation was performed here.

## Matched population, industry, and logistics baselines

Current state snapshots preserve population plus eight building readers: infrastructure, railway, supply node, civilian factories, military factories, dockyards, naval bases, and airbases.
The population snapshot now prefers the measured `asteroid_incoming_state_population_before_k` receipt.
The immutable physical BEFORE blob instead assigned its population snapshot during the building stage after population mutation.
That old value must not replace the corrected current before-loss receipt.
Dead population is never restored, and population lost is not an established displaced-worker count.

Industry loss totals also include synthetic refineries and industrial infrastructure.
Logistics totals also include naval support buildings, canals, energy infrastructure, and other explicit family members beyond the smaller preserved snapshot set.
Airbases are not an excuse to fill a missing logistics baseline with a strategic category value.
The parent must retain matching before/after receipts for the complete agreed capacity families rather than pair category totals with a narrower denominator.
Persistent per-token post-impact capacity and an Event 028 repair-budget ledger are not currently present in the inspected recovery contract.

For each state/token capacity measure, use the same reader throughout:

- `B` is the measured pre-impact value.
- `A` is the measured immediate post-impact value.
- `C` is the current value capped by `B` and current engine limits.
- Capacity fraction is `sum(C) / sum(B)`.
- Recovered incident-loss fraction is `sum(clamp(C - A, 0, B - A)) / sum(B - A)`.

Industrial and logistical conditions should be checked separately unless the parent selects an accepted combined weighting.
Zero denominators require explicit handling, and a recovery mission needs an actual recoverable incident loss.
Thresholds must not be satisfied solely by retained pre-impact values before recovery work or burden transition occurs.
No 70%, 75%, or other regional percentage was selected here.
The existing `industry = 0.25` and `network = 0.40` constants are repair-grant fractions, not mission completion thresholds.

Current snapshots use installed building levels.
If the parent chooses functional capacity for an objective, matching pre-impact and post-impact non-damaged readings must also be recorded.
Using current functional capacity against an installed-level baseline without stating that distinction mixes measures and can require repair of unrelated pre-existing damage.
Province-local railway, supply-node, port, and other installation readback/removal semantics remain a dependency of the physical tranche's native verification.
Requested removal counts are not actual-loss receipts.

Current restore helpers calculate a fraction of `preimpact - current` and cap against pre-impact levels.
They do not consume an incident-specific remaining-loss budget, so a later unrelated loss can enter that gap.
The proposed bounded grant is the minimum of current baseline gap, unspent measured Event 028 loss, and current allowed-cap gap.
Only the observed native repair delta should consume the budget.
Recovery observed from other construction needs coherent reconciliation so later damage cannot reopen already-restored incident capacity.
The exact observation/high-water mechanism is parent implementation work and was not added here.

## Current payment and reserve contracts, F08

Read-only parsed comparison confirmed that current manual debits, custom-cost fields, modifiers, removal durations, all 21 AI bodies, and the recovery constants remain identical to their inspected BEFORE baselines.
The following are current tuning anchors, not completed dynamic prices.
Every listed action commits one civilian factory for 30 days.

| Actions | Ordinary manual payment | Spendable types including factory |
| --- | --- | ---: |
| Hospitals, debris, filters | 800 manpower, 80 support equipment, 60 trucks | 4 |
| Emergency rail, supply spine, transport protection | 2 trains, 80 support equipment, 300 fuel | 4 |
| Outer industry | 800 manpower, 2 trains, 80 support equipment | 4 |
| Worker rehousing | 800 manpower, 2 trains, 60 trucks | 4 |
| Factory hardening | 800 manpower, 80 support equipment | 3 |
| Observation network | 20 convoys, 80 support equipment, 300 fuel | 4 |

Prepared hospital/debris payments are 600 manpower, 60 support equipment, and 45 trucks.
Prepared rail payment is one train, 60 support equipment, and 225 fuel.
The small train quote produces a 50% reduction, requiring parent rounding/tuning review against the specified 20% to 30% first-rail discount.
Existing ordinary and prepared after-payment thresholds imply the same protected remainders:

| Resource | Protected remainder |
| --- | ---: |
| Manpower | 1,000 people |
| Support equipment | 100 |
| Trucks | 100 |
| Trains | 2 |
| Fuel | 500 |
| Convoys | 20 |
| Command power | 10 |

The source uses `>` against payment-plus-reserve constants.
A fresh quote must verify the intended exact boundary rather than assume an inclusive native comparison.
No protected civilian-factory remainder constant is currently defined.
The accepted rule against spending the last construction capacity during existential war needs a parent-selected capacity-floor contract using the documented available-project-factory reader.
No numeric civilian reserve was selected here.

A coherent four-cost quote proposal is:

1. Validate the actor, action, incident, target/set identity, and existing country-local concurrency gate.
2. Recompute all resource amounts and factory commitment/duration together from current supported readers and the applicable population, state-count, distance, industry, dust, preparedness, and failure inputs.
3. Validate all post-payment reserve remainders and construction capacity before any debit.
4. Save the country reservation and frozen quote identity/amounts, then debit once and publish the matching paid receipt.

The quote receipt should retain actor, action, incident, target/set identity, contract identity, up to four resource tokens and amounts, preparedness eligibility, factory commitment/duration, and paid/closed state.
Display calculations are previews and do not consume preparedness or become the paid receipt.
Every caller must initialize temporary quote outputs it consumes before nested helper calls, then persist the accepted quote in country-owned normal storage.
Finish, cancellation, and stale callbacks must match the owning contract before clearing it.
Failure escalation changes future quotes, not already-paid amounts.

Existing seven state projects treat upfront spending as committed work and have no automatic cancellation refund.
This research does not import the crater actions' separate refund contract.
Any later refund policy must use the exact frozen paid quote rather than a recomputed price.

Verified quote inputs include `manpower_k`, `fuel_k`, targeted `num_equipment`, supply-vehicle stockpile getters, `num_of_civilian_factories_available_for_projects`, and state distance readers.
Manpower/fuel readers in thousands must be converted consistently to the current payment units.
Vanilla NOR source uses `num_equipment@convoy` as a stockpile value.
Dynamic equipment debit amounts are documented.
Vanilla INS decisions use `days_remove = var:INS_realign_supply_chains_time`, providing a verified variable-duration precedent for factory time.
Dynamic factory-count behavior inside an ordinary decision modifier and selection-time timer/quote coherence still need native confirmation.

The proposed general price shape is a bounded anchor multiplied by a work scale, applicable preparedness factor, and active failure factor.
The work inputs must correspond to real effort rather than add extra spendable types.
Exact coefficients, minimum/maximum quotes, factory-time scaling, and dust/industry scaling values remain parent tuning choices within the accepted contract.
The medical support/truck band of 5% to 15% is an accepted tuning range, not a selected final percentage.
Reserve floors protect affordability and must not silently waive part of a quoted action price.
Rehousing already has four spendable types, so stability cannot be appended as a hidden fifth payment.
Any change to its transport/payment mix must retain the accepted action purpose and the four-type limit.

Transport preparedness currently grants one train, 40 support equipment, 15 trucks, and 75 fuel.
The current path has no at-risk stockpile snapshot and no matching prevented-loss receipt.
Full preservation requires a measured pre-disruption reserve, an accepted disruption/prevention contract, and actual prevented loss bounded by the reserve at risk.
Physical state-building/population snapshots cannot infer national movable stockpiles at risk.
No new disruption amount, preservation percentage, or free stockpile reward was selected by this research.

## Failure, Deaths, timing, and threshold gaps, F10

The current failure helper applies 90-day local `asteroid_incoming_mission_failure_pressure`, adds a 90-day timed national recovery burden, then clears the country's reservation.
The local pressure modifier uses `local_supplies = -15`, construction speed `-0.10`, and controller army speed `-0.10`.
The helper has no mapped rescue Deaths transaction, recorded recovery-extension calculation, or bounded future repair-cost multiplier.

Accepted failure mapping is specific to the mission:

- Rescue failure extends the exact local recovery burden, applies a bounded rescue-period Deaths entry, and temporarily increases supply pressure.
- Stabilization failure worsens one member of the frozen two-state set and keeps emergency response open.
- National network failure extends national recovery and increases future repair costs for a limited period.
- Part 6 does not define distinct outer-ring or regional failure penalties, so new deaths or other penalties must not be invented automatically for them.

Recovery extension needs stored expiry information or another verified remaining-duration contract.
Reapplying a short fixed duration is not proof that a longer existing burden was extended.
Proposed extension days, future-cost multiplier, and cost-pressure duration remain unselected parent tuning choices.
The existing 90-day pressure constant is a current anchor rather than a chosen value for every missing consequence.

Death handling must validate an active matching mission receipt and exact incident/state identity, use current surviving population and the existing shared protected-loss API, and record only actual applied deaths once.
The current monthly rescue contract has a 1,000-person population floor, a 25,000-person cap, profile fractions 0.0004/0.0002/0.0003/0.00015, and 6/4/6/3 month maximum receipts, with medical preparation multiplier 0.50.
The exact mission failure pulse and its relationship to scheduled monthly rescue losses remain parent implementation/tuning choices.
An expired rescue burden must not automatically create a fresh rescue-loss stream.
The unused recovery constants `rescue_death_fraction = 0.01`, `rescue_death_fraction_heavy = 0.02`, and `minimum_supply_ratio = 0.50` have no inspected consumer establishing a valid mission failure or supplied-garrison contract.
They must not silently become those missing mechanics.

The current hospital, rail, and debris action helpers call `asteroid_incoming_close_state_emergency` before their follow-up mission proof.
That helper removes five timed impact modifiers and sets local emergency resolved.
Monthly rescue deaths also stop when that resolved flag is set.
The full accepted distinction between bounded action relief, local mission proof, reconstruction transition, national lightening, and regional legacy therefore needs implementation beyond replacing one-state predicates.
The generic success helper currently removes national burden and gives the lasting legacy after local success.
Existing legacy values are +5% repair speed, +3% construction speed, and +2% stability.
Those source values do not establish that every mission is entitled to that reward.

Part 6's normally 90-day emergency phase and Part 3's national closeout when all timed impact burdens expire or resolve need a coherent phase/receipt interpretation.
Current severe recovery modifiers last 720, 405, 540, or 270 days depending on profile.
The reviewed expiry predicate closes historical-only availability after active burden disappears, but the parent still owns reconciliation of phase timing and longer recovery burdens.
This research did not alter that predicate or parent availability logic.

Current repair missions require a completion-day threshold that coincides with their native timeout.
Native success/timeout ordering remains unverified.
The parent should use one exact result resolver for the deadline boundary and preserve the intended hold requirement for rescue, while allowing repair objectives to complete from real proof as their mission contract permits.
No arbitrary extra deadline day or automatic clock-only success was introduced.

Failure and completion must be idempotent per actor/incident/mission/group receipt.
Stale or dead-actor cleanup must not punish another controller, mutate another country's reservation, publish success, or apply another Deaths pulse.
No broader periodic world scan was authorized by this research.

## Unselected proposed tuning and acceptance scenarios

Potential constant names describe proposed storage only: `regional_industry_recovery_share`, `regional_logistics_recovery_share`, `ring_two_burden_ceiling`, `minimum_civilian_factory_reserve`, `mission_failure_recovery_extension_days`, `mission_failure_cost_multiplier`, `mission_failure_cost_days`, and bounded cost-scale coefficients/caps.
No file, key, value, or ranking implementation with those names was added.
The specs leave their numerical choices to parent tuning within the mapped behavior.
Ranking tie-breaks and major-industry endpoint selection are similarly unselected.
They are not grounds to substitute one-state or national-average objectives for the accepted scopes.

Proposed meaningful acceptance cases for the future implementation are: two distinct worst states with one still unrepaired, one healthy network state with another disconnected endpoint, one cleared outer state with other outer burdens active, an unchanged regional denominator after control loss, separate industrial/logistical percentage failure, zero-loss/zero-denominator rejection, repair grants capped to measured incident loss, stockpile change between preview and debit, exact reserve boundary, preview without preparedness consumption, repeated timeout without a second Deaths entry, stale callback cleanup without foreign mutation, and success at the native timeout boundary.
These future cases were not implemented or executed by this read-only plan.
Any changed prices or eligibility can affect AI selection even when weight text stays identical, so the parent's existing probability specialist must perform the matching baseline/compare workflow before weighted-surface acceptance.

## Immutable source baselines and attribute note

The archived decision BEFORE SHA-256 remains `E28A8C05814E1A3AB646972138C4349A3B55991588D5D2498BDF42ED3271F164`.
The availability BEFORE constants SHA-256 is `1403A2F46D41CB7668393C931C10AFC98091697763ADC8C88B786CC773A8EF7E`.
The availability BEFORE triggers SHA-256 is `EFA22ACB10085504B65E1C7DF95E47931E2B980D9A3780312CE0B65F885EC08F`.
These archived bytes were rechecked without edits.

The physical BEFORE source is blob `222dbeaca37dc6118665359f8b3908389c7b8440` from commit `9d7862dcb78ae097f61eb95e07e3ff2e911f75db`, path `common/scripted_effects/028_asteroid_incoming_effects.txt`.
Its 89,045 bytes were read in memory and SHA-256 reverified as `44a5519e86a8e6fcaaf0c681f84ecc77d365383a7cd4092d3d9cb450fad08a44`.
Its snapshot lines 694 to 704 preserve the older building-stage population assignment discussed above.

`git check-attr` reported the crater decision BEFORE file's text attribute as unspecified.
The availability BEFORE constants file already reported text unset.
The parent should add `docs/plans/028_asteroid_incoming_plans/crater_actions_20261003/before/** -text` when committing byte-exact archives.
No attribute rule, staging, archive normalization, or commit was performed here.

## Source citations read for this research

`mod` resolves to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
`game` resolves to `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Line spans below identify the directly read relevant sections and are distinct from executed engine evidence.

| Source | Relevant span or helper |
| --- | --- |
| `mod\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_spec_part_6_decisions_and_missions.md` | Read in full, mission map at 108 to 180, costs at 254 to 262, cleanup/exploits at 280 to 298 |
| `mod\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_spec_part_10_achievements_and_acceptance.md` | Read in full, government recovery conditions at 43 to 55 and full acceptance/validation requirements |
| `mod\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_decision_mission_prompt.md` | Read in full, mission equivalence, four-cost cap, exact states, reserve floors, and outcome/cleanup map |
| `mod\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_tuning_matrix.md` | Read in full, continuing rescue limits, preparedness, and decision-cost bands |
| `mod\docs\specs\028_asteroid_incoming_specs\028_asteroid_incoming_spec_part_3_impact_damage_and_aftermath.md` | 90 to 121 population and rescue contract, 230 to 249 owner/controller and closeout |
| `mod\docs\plans\028_asteroid_incoming_plans\subagent_handoffs\completion_audit_20261003.md` | F08/F09/F10 at 183 to 239, used as findings to recheck against current source |
| `mod\common\scripted_effects\028_asteroid_incoming_effects.txt` | Population receipt helper, snapshots at 663 to 677, physical application at 1178 to 1229, owner/controller aggregation at 1370 to 1438, cleanup at 1631 to 1651 |
| `mod\common\scripted_effects\028_asteroid_incoming_recovery_effects.txt` | Restoration at 15 to 169, reservation at 194 to 209, cleanup/finish at 211 to 296, action relief at 299 to 410, success/failure at 632 to 720 |
| `mod\common\scripted_triggers\028_asteroid_incoming_triggers.txt` | Repair/reserve helpers in directly read 329 to 574, country pointer and all five mission predicates in 650 to 814, achievement deadline at 939 to 947 |
| `mod\common\script_constants\028_asteroid_incoming_constants.txt` | Durations/transport at 72 to 87, recovery/cost/reserve anchors at 103 to 187, unused recovery fractions at 240 to 257, profiles at 274 to 289, rescue tuning at 290 to 317 |
| `mod\common\ideas\028_asteroid_incoming_ideas.txt` | Recovery modifier constants at 54 to 60 and recovery burden/legacy definitions |
| `mod\common\dynamic_modifiers\028_asteroid_incoming_dynamic_modifiers.txt` | Failure pressure at 96 to 101 |
| `mod\events\028_asteroid_impact.txt` | Impact day at 322 and achievement deadline addition at 327 |
| `mod\common\scripted_effects\028_asteroid_incoming_runtime_effects.txt` | Rescue processing around 1012 to 1138, preparedness stockpile grants, and government proof in read span 1919 to 1962 |
| `game\documentation\effects_documentation.md` | 4173 to 4192 state division iterator, 1153 to 1170 targeted state dynamic modifier, 1252 to 1265 dynamic equipment amount, 1051 to 1081 mission/removal timer effects, 8219 to 8226 leader supply grant |
| `game\documentation\triggers_documentation.md` | 1684 to 1691 state division predicate, 2621 to 2660 division composition/local count, 3462 to 3470 COMBATANT modifier, 3835 to 3842 equipment stored, 3957 to 3965 fuel, 4603 to 4628 rail connection, 6757 to 6765 available-project factories, 7686 to 7704 unit organization/strength |
| `game\documentation\dynamic_variables_documentation.md` | Scope list at 6 to 16, fuel_k at 385 to 386, manpower_k at 469 to 470, equipment at 557 to 564, civilian capacity at 592 to 610, distance at 1127 to 1128, complete scope-heading/reader search |
| `game\common\scripted_effects\00_scripted_effects.txt` | `SF_PARA_combat_effect` at 4057 to 4068 |
| `game\common\decisions\NOR.txt` | Stockpile reader at 39 to 45 and state division owner/faction test around 2415 |
| `game\common\achievements.txt` | State division template predicate around 7232 |
| `game\common\decisions\INS.txt` | Variable `days_remove` precedent at 2300 |
| `game\common\dynamic_modifiers\wuw_dynamic_modifiers.txt` | State local-supply modifier at 39 to 48 |
| `game\common\dynamic_modifiers\bba_dynamic_modifiers.txt` | `out_of_supply_factor = ITA_re_out_of_supply` at 477 and corresponding repeated country modifier variants |
| `game\common\defines\00_defines.lua` | Internal unit-supply AI handling at 3287 and 3480, army supply-ratio handling at 4395 to 4397 |
| `game\interface\unitview.gui` | Supply widgets at 414 to 415 and 1702 to 1703, no scripted getter declaration |
| `mod\paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | Division-scoped trigger table at 2216 to 2226, including reserve priority rather than supplied status |
| `mod\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | Removal/cancellation at 336 to 356, mission lifecycle at 461 to 478, targeted actor/FROM scope at 511 to 536 |
| `mod\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | Flag targeting at 125, variable targeting at 551 to 553, global date/num_days reader section |

The retained crater handoff, recovery target-isolation handoff, and physical receipt handoff were read for ownership and dependency contracts.
Their source-model results remain attributed earlier evidence and were not rerun or promoted to native acceptance by this research.

## Fresh narrow MCP queries, returned revisions, and coverage

The current workspace ID returned by successful requests is `mod_chaos_redux_ea3b2d67c2c0`.
The client still exposes no `hoi4.script_validate` route.
No helper-expansion job, background task, or unverified server-health negotiation was used.

An initial batch of reference context, `unit_supply` search, and an 80-line failure-source lookup remained pending and was manually cancelled to avoid indefinite waiting.
The reference-context arguments were `surface = decision`, `limit = 6`, and the exact question below.

```text
STATE every_state_division and any_state_division: documented DIVISION-scoped current supply status getter or trigger for supplied local garrison; dynamic variables and has_combat_modifier limits
```

That cancelled context request returned no usable source citation or analysis.
It is not recorded as a natural 600-second timeout.
The subsequent narrower queries did return:

| Query | Exact bounded arguments | Returned evidence |
| --- | --- | --- |
| `hoi4.reference_search` | `query: every_state_division`, `sources: [game_doc]`, `limit: 1` | Installed effects documentation section 4173 to 4192, id `244b518b56bd2512c0da3275b9c3e1ea24429439b3c6ec32511472fab5533d87`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. One bounded result from total two |
| `hoi4.reference_read` | Same id/revision, `startLine: 4173`, `maxLines: 20` | Complete cited iterator section with `nextLine: null` and `nextColumn: null` |
| `hoi4.reference_search` | `query: unit_supply`, `sources: [game_doc, wiki]`, `limit: 1` | One offline Defines/NAI result, id `ade110a6edef02e76b330fd3b162e0bb0b2e6da05287d9a4d8e8591cd6aed4b3`, revision `61ae03fd36bcbe2ab6ca1304b013d3f432b88e6592856fffdd2685f792e87fcc`, path `mod\paradox_wiki\Defines - Hearts of Iron 4 Wiki.md`, section 1607 to 2436. Excerpt contains `FRONT_EVAL_UNIT_SUPPLY_AND_ORG_LACK_IMPACT`, with no callable supplied-status getter |
| `hoi4.source_lookup` | `symbol: SF_PARA_combat_effect`, `includeReferences: false`, `maxDefinitions: 1`, `maxLines: 20` | Complete vanilla definition at `game:common/scripted_effects/00_scripted_effects.txt:4057-4068`, returned MCP revision `ee16f1dacebf49d427b40f03c2885f015fed64a3675ce97783734888823d1b08` |
| `hoi4.source_lookup` | `symbol: asteroid_incoming_recovery_mission_failure`, references false, one definition, 20 lines | Definition 655 to 675 at returned MCP revision `36ca4c3be2fd6008caa6dbe1968e47a8cf185fc6e2353e026acd042f07495462`, text continuation at 675 |
| `hoi4.source_lookup` continuation | Same symbol, expected revision above, `fromLine: 675`, `maxLines: 1` | `SOURCE_REVISION_STALE`, with current revision reported as `457e553927071467f0d9292d3e43db9b5a972ec063a05b7a9de64c3ba75990be`. No continuation pass claimed |
| `hoi4.source_lookup` fresh retry | Same failure symbol, references false, one definition, 25 lines | Complete 655 to 675 definition with no continuation at revision `026e1a7061fc33333864f5720c72848f5feb02b150dfa53d5970e0f6ec4be351`, confirming local pressure, timed burden, and country cleanup only |
| `hoi4.map_inspect` | `lookupOnly: true`, `stateIds: [64]`, `includeOverview: false`, `queryLimit: 1` | `MAP_LOOKUP_COMPLETED`, one static fixture state inspected, no overview/full validation, revision `db506e6eafcd7513a9aa63f77def167ab18ed365ec83ae6fb56052b1063d1e30` |
| `hoi4.event_inspect` | `mode: trace`, selector `{kind: event, eventId: chaosx.nr28.4}`, helpers false, depth/nodes/edges one | `EVENT_INSPECTED_PARTIAL`, focused mode, zero helpers, revision `f0e16475c8407b53ed214cb41838952142f1cd8c62e083191f7d8916d82ac506` |

The `unit_supply` search reported game-document coverage of 50 files/3,281 sections, wiki coverage of 54 files/1,042 sections, and a separately unavailable script_doc inventory of zero files/sections.
Search absence is supporting coverage, not proof of undocumented engine impossibility.
The direct local file/source checks above supplied the broader division-context investigation.

The focused event result defers whole-workspace helper projections and lifecycle analysis.
Its broad index counts reported 2,193 diagnostics and 8,983 unresolved nodes, while the selected trace remained bounded.
The map result is a static lookup using a previously used state-64 source fixture and is not an incident-state plan or live division-supply observation.
Both results reported truncated inline source inventories and linked the full artifacts.
Their linked report bodies were not retrieved in this client, so only their returned metadata and boundaries are assessed here.
The aggregate resource inventory exposed only `codex_apps` entries, `list_mcp_resources` for `hoi4-agent-tools` failed as an unknown server, and the normalized `hoi4_agent_tools` server returned an empty resource list.
No full report-body coverage is claimed from that resource gap.

Map artifact, 239,750 bytes, SHA-256 `14c2ca7717c5697b74e62c9bc568408b17f9eee31ae905cae729b03a2ea083d4`:

```text
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14c2ca7717c5697b74e62c9bc568408b17f9eee31ae905cae729b03a2ea083d4/1efb85836272c72dd96a1084493414359cb050aeae8ab602fe58ab84b45ad967/map-lookup.db506e6eafcd7513.8d030eb3664782be.json
```

Focused event artifact, 1,070,855 bytes, SHA-256 `e1b4b50cbaa488d39deea5bc1326515fc059fa6bc6a4c4153df8cba5f170f1e9`:

```text
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1b4b50cbaa488d39deea5bc1326515fc059fa6bc6a4c4153df8cba5f170f1e9/c290c6dda3669299e369bcfa0d18bc3ca98ddccc3349dbd593e22a55834397b9/event-trace-f0e16475c840.json
```

## Parent review boundary

The supplied-garrison script getter remains unverified, five non-security crater outcomes await parent wrapper integration, and the full F08/F09/F10 source work has not been implemented by this research.
No route work or national/regional objective implementation is represented as completed.
The quoted current costs, reserve floors, existing duration anchors, actual state receipts, source gaps, and returned native revisions are sufficient to define the next bounded parent implementation scope without rediscovering these facts.
Parent tuning can select unprescribed constants and ranking thresholds within the accepted mission/cost/Death contracts, while preserving fixed population losses, exact armor bonuses, full objective coverage, reserve protection, and the four-cost limit.
This document does not close those gameplay gaps and does not authorize a security fallback or AI-weight patch.
