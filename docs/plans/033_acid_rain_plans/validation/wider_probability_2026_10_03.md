# Event033 wider probability audit, 2026-10-03

Disposition: source-review and evidence handoff complete, numerical and engine probability validation unresolved.
This report does not certify Event033 completion or balance.
The auditor did not modify gameplay, weights, costs, timing constants, target pools, achievements, GUI source, or any existing before snapshot.
The parent owns source repairs and final integration.

## Evidence identity and scope

The reviewed coding prompt, decision prompt, AI acceptance matrix, cost matrix, front-state matrix, and spec parts 3, 5, and 8 are frozen in `probability/wider_2026_10_03/spec_inputs/`.
The reviewed nine source copies and eight spec inputs are indexed in [source_manifest.json](probability/wider_2026_10_03/source_manifest.json).
The wider decision copy is SHA256 `E72D281DABD6F699A4248062AEC34817ED921C14F0DE6B541531F4306D213679`.
The wider runtime copy is `9BDFB2ABFA1A29BEA9FDF073026DB787E2597295EE7B02AA0FE7F25DA1FA8D53`.
The wider constants copy is `2AE19FA866A83B6626653B7A27C3024E6361E8B9532A901405B3D4D97D6A9425`.
The wider preparedness and trigger hashes are `CECBFFDFC281FCECA23AF4764D3C3E1C3D276BC6257C4B9E04BA4143DDEB1C6A` and `6686EC5F09D9745A51113DC6DE142AA641784AB80E178440B0DDECE194369944`.
The earlier wider script-localisation copy is retained as its own revision and is not substituted for the newer critical-quotes copy.

The fresh quote/payment dependency baseline is separately documented in [critical_quotes_baseline_2026_10_03.md](critical_quotes_baseline_2026_10_03.md).
It preserves seventeen original sources, five inputs, the exact A1-A20 fixture, the failed smaller inspect, and the concurrent Air-runtime supplement.
Parent pacing commit `292847723` is not a numerical pacing certificate.
Its prior same-scenario compares timed out and remain open.
The parent Air-only dependency commit `9d7862dcb` does not erase the original runtime before-copy or permit mixing transitive revisions silently.

## Numerical evidence classification

| Result class | This wider pass |
| --- | --- |
| Exact probabilities | None returned, unresolved |
| Bounded probabilities | None returned, unresolved |
| Seeded sampled results | None run, unresolved |
| Evaluated score-only results | None returned, unresolved |
| Source literals and mechanics | Reviewed source evidence only |
| Native engine/campaign behavior | Not executed or certified |

An unresolved or timed-out pool is not a zero-candidate pool.
Raw ai_will_do bases are willingness inputs, not effective scores or click probabilities.
Source RNG endpoints are not an evaluated quota histogram or a realized coverage bound.
The spec's planning simulations and parent synthetic suite are separate evidence and were not relabeled as MCP or campaign results.

## Live route attempts and exact errors

Requests and raw responses are persisted in [route_receipts.json](probability/wider_2026_10_03/route_receipts.json).
The live catalog exposed the probability, decision, event, reference, and source-lookup routes, but exposure did not establish service health.
No negotiated persistent-job or helper-expansion route was used.

| Narrow scope | Adapter / route | Outcome |
| --- | --- | --- |
| Runtime region lists | probability_inspect, random_list | 600-second timeout |
| Runtime chance and integer draws | probability_inspect, direct_random | 600-second timeout |
| Runtime target pools | probability_inspect, custom_weighted_pool | 600-second timeout |
| Four permanent project ids | probability_inspect, mission_ai_will_do | 600-second timeout |
| Five urgent ids | probability_inspect, mission_ai_will_do | 600-second timeout |
| Four recovery ids | probability_inspect, mission_ai_will_do | 600-second timeout |
| Event033 root lifecycle | event_inspect, state_flow, chaosx.nr33.1, depth 4 / 40 nodes / 80 edges | 600-second timeout |
| Evacuation structure without scenarios | decision_inspect, inspect | -32602 schema error |
| Corrected evacuation structure | decision_inspect, three explicit target/control scenarios | 600-second timeout |
| Fresh immutable Shelter before-copy | probability_inspect, one candidate | 600-second timeout, separate critical-quotes receipt |

The corrected evacuation scenarios were `A12_valid_severe_forecast`, `A12_stale_generation`, and `A17_previous_controller`.
They were structural retry inputs only and do not replace the full A1-A20 fixture.
Their old capacity alias and unbound equipment facts also limit their coverage independently of the timeout.

Each timed-out route returned its own route name in this exact wire form:

```text
tool call error: tool call failed for `hoi4_agent_tools/hoi4.probability_inspect`

Caused by:
    timed out awaiting tools/call after 600s
```

The event and corrected decision errors use `hoi4.event_inspect` and `hoi4.decision_inspect` in the same failure envelope.
The initial decision input error was exactly:

```text
MCP error -32602: Input validation error: Invalid arguments for tool hoi4.decision_inspect: Decision inspection requires declared scenarios at scenarios
```

None of these requests returned an analysisId, artifact URI, source/dependency revision inventory, candidate count, scenario hash, coverage certificate, or continuation.
No evaluate, sweep, simulate, sequence, or render was submitted against a fabricated analysis.
No same-file compare was performed.
The fresh single-Shelter retry was finite and narrower than the earlier family requests, and no identical 600-second loop followed it.

An earlier original decision discovery returned thirteen candidate definitions and recommended the mission adapter.
Its artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f21404bcd7ad39c3677b6cbcedcfc4e319fa8a066aaf64233f2e292776775477/28c70f3f3b44bc9ef1956bb5c07a0ed98ba93af146cefcdce100f320a635b7be/probability-inspect-75a6ff8f93d3.json`.
That original source revision was `bce1d676db905315e7aa9bd807b9219f1beff779811ce4a02cde59b99735f4ab`, with decision file SHA256 `31462E54C448EB46E947B3FE6DFF93BFC145E5C4B2BF28EBEBA527E91AED1863`.
That discovery is older provenance, not a current score, current dependency certificate, or this wider pass's numerical baseline.

## Named scenario coverage

The explicit fresh [A1-A20 fixture](probability/2026-10-03critical_quotes/A1_A20_scenarios.json) is sealed at SHA256 `4DAA3351A28A154D889F720F066EF39D6CFF856150743E252FEA7C2D8F6E9FC5`.
A1-A19 were materialized from the accepted coding/decision matrix and not inherited from the unrelated three-case pacing fixture.
A20 is a separate explicit no-active-work case and does not modify the sealed A1-A19 file.

| Matrix cases | Declared coverage |
| --- | --- |
| A1-A3 | Fragile peaceful minor, warning response, invasion and manpower/equipment reserve pressure |
| A4-A6 | Convoy island route, convoy shortage, landlocked train route |
| A7-A10 | Established long lead, great-power two warnings, war shortage, strong CBRN overlap |
| A11-A13 | Ordinary exposure, three severe target states, separate front/region ownership |
| A14-A16 | Global low/high Preparedness, capital severe forecast and target importance |
| A17-A18 | Controller transfer, dissipation with an unfinished paid project and delayed callback |
| A19-A20 | Tier-three burden with explicit receipt-gap state, empty closed state |

Each actor and target is hypothetical input, not a claim about a historical country's campaign.
The fixture retains resource quantities, control/owner facts, target identities, generations, route facts, and scheduled changes.
It does not inject missing public quote writers, helper truth, or candidateOverrides to manufacture payable decisions.
Native stockpile and effect-preparation bindings remain unverified.
A19 is an explicit missing-receipt variant, so post-dissipation receipt production remains an additional unresolved lifecycle obligation rather than an assumed native success.
The all-thirteen definition pool is declared, but current effective eligibility and external AI factors are not certified complete.

[Runtime case contracts](probability/wider_2026_10_03/runtime_case_contracts.json) materialize forty-one fresh hypothetical cases for first-pass counts 1/2/3/20/1000, second visits, all seven region candidates, two/three-front reservations, severe stale/disconnected target conditions, global storm capacity/sparse pools/slot reuse, every ordinary and global dissipation check, pressure/guarantee cases, and third-front gate/bonus/retry boundaries.
These are persisted case contracts awaiting confirmed live input binding, not accepted service-schema or numerical results.
The planned simulation seed is 33031003 with 10,000 iterations after complete source/pool/input coverage.
No such simulation was run.
Sequence work requires a verified complete manifest containing cadence, retries, caps, reservations, removals, cooldowns, resets, and terminal states.
No render was fabricated.

## Regional, severe, and global source findings

1. First-pass goal source at runtime 1183-1227 draws an integer with min 60 and exclusive max 86, rounds the count upward, applies the minimum-three/region-total clamp, and uses all states for a region smaller than three.
Second visits target remaining untouched states.
A raw percent draw and the displayed 60-85 planning range do not prove that every tiny region's realized coverage lies within that percentage range.
The requested bounded quota distribution remains unresolved.

2. Region candidate weighting at 1371-1459 has the seven-entry list, untouched/highest/majority/count bonuses, current/previous multipliers, complete/empty exclusions, and other-front current and warning reservations.
The highest-untouched scan includes excluded regions.
When correction is active and an excluded region owns the highest count, lower-count eligible regions can all lose their weight.
This is a source starvation risk, not a measured zero-probability or permanent-softlock finding.

3. The region selector consumes a child-created `acid_rain_region_candidate_weight` without caller predeclaration.
The offline helper-output contract identifies a persistence risk at this call boundary.
No engine execution establishes whether outputs are lost here, so zero weights must not be asserted as observed.

4. Front arrays and reservations are keyed by stable front ID.
The source excludes other current regions and warning destinations.
This supports separate ledger intent, not statistical independence: mutually excluding candidate pools create conditional dependence between front choices.
The source and seeded joint behavior still require the requested live checks.

5. Severe and superstorm planners build repeated state entries as integer-weighted pools and draw without replacement while growing a connected target set, with a disconnected fallback.
Declared pool coverage must include every eligible state, native logistics/controller inputs, historical penalties, and adjacency before normalizing shares.
The four-state hypothetical contracts do not represent the complete real-map pool.

6. Superstorm source at 3891-4038 recomputes active-region markers from target flags, uses bounded reusable forecast slots and capacity, and draws a target goal from min 3 to exclusive max 9.
Its commit gate accepts a positive planner result rather than requiring the authored minimum of three distinct states.
The sparse-pool case therefore needs verification.
Current count updates at 4127 and 4202-4203 are active-start/end bookkeeping, so an old lifetime-count allegation is not promoted as a current defect.

7. Ordinary dissipation reads the seven-step ladder, and global dissipation reads the eight-step ladder with pressure/active-storm penalties only on non-guaranteed checks.
The source guaranteed branch bypasses the penalty.
Caller elapsed-time gates, the increment-before-read check index, retry cadence, scheduled external pressure, and cleanup are required for cumulative timing.
No survival curve or bound was calculated here.

8. Third-front source at 3690-3743 gates on two existing fronts, multiple-front unlock, non-global state, Chaos, and retry due.
It adds the Chaos-700, strong-front, and age-180 bonuses and clamps to the authored cap.
A successful draw still requires a distinct valid region and valid front creation before the resolved receipt is set.
The roll chance alone would not be the probability of adding a third front.
No normalized or campaign-level third-front result is claimed.

## All thirteen decision surfaces

| Public id suffix after chaosx_acid_rain_ | ai_will_do source line | Raw base input | Source/payment coverage issue |
| --- | ---: | ---: | --- |
| project_shelter | 127 | 120 | Generic quote aliases, capacity, tier duration, cancellation visibility |
| project_water | 192 | 115 | Same project gates, exact train/convoy route and reserves |
| project_medical | 258 | 105 | Same gates, CBRN overlap, fuel/manpower reserves |
| project_transport | 324 | 90 | Same gates, truck archetype versus concrete debit |
| urgent_shelter | 397 | 160 | Shared quote path, double manpower, mutable return |
| urgent_water | 455 | 150 | National action marked target-required, double manpower, route binding |
| urgent_medical | 514 | 145 | Double manpower, absent fatigue gate, fuel reserve |
| urgent_transport | 573 | 135 | Paid train/truck/fuel route, stale preflight and stockpile alignment |
| urgent_evacuate | 665 | 180 | FROM not captured, target generation/control, duration/partial-effect gap |
| recovery_transport | 745 | 140 | FROM/receipt and harm gate, D two-factory mismatch |
| recovery_decontaminate | 817 | 150 | FROM/receipt and route, double manpower, mutable reservation |
| recovery_industry | 889 | 100 | FROM/receipt, double manpower, D factory mismatch, harm applicability |
| recovery_demobilize | 948 | 80 | Gate excludes active projects it cancels, local versus global quiet state |

These bases are unmodified source literals only.
The reviewed decision/runtime sources have no Event033 `mtth:` consumer, and the inspected MTTH directory has no Event033 entry.
Native ai_will_do willingness, helper reserve gates, action duration, and weather RNG are distinct surfaces.
No MTTH-based cumulative decision timing is inferred.

All thirteen public custom-cost blocks require unwritten `acid_rain_quote_duration_days` and `acid_rain_quote_civilian_factories`.
The stored per-component rows and action-resource arrays exist, but public display/availability use a disconnected generic quote.
The four project slot checks read an unwritten capacity name while initialization writes `acid_rain_project_capacity`.
Threat flags hide all four permanent project decisions while the same flags increase their AI bases, creating unreachable threat boosts in those public phases.
The exact native consequences of a false custom-cost trigger alone are not inferred from the red display.

The common action debit removes quoted manpower, start removes it again, and release returns only one reservation.
The start-time AI floor can therefore be contradicted by the second source debit.
Release reloads mutable quote caches rather than a captured paid amount.
D recovery rows quote two factories while the persistent gate supports zero/one and the added modifier commits one.
These are source mechanical findings, not measured resource losses.

The evacuation score reads a state-scoped shelter tier while the inspected tier initialization is country-scoped.
Its authored ai_will_do block lacks explicit population, lead-time, combat, and infrastructure terms requested by the matrix.
External native factors remain unknown, so a final target ordering is unresolved rather than assumed wrong in every campaign.

The shared single country action receipt serializes actions more narrowly than the documented family/evacuation caps.
Removing its guard alone would overwrite timers, targets, and payments, so no such change was suggested as a safe numerical fix.
Seven-day evacuation, three-day forecast lead, and the missing promised one-day mortality partial-effect read remain separate from the authorized core quote/payment repair.
Timing Proposal 9 remains unpatched and requires separate accepted-case baseline/compare.
Recovery `acid_rain_aftercare_unresolved` is written during final dissipation at runtime 4354.
The global claim that this flag has no writer is incorrect.
Receipt coverage on other tier-producing/local paths remains unresolved.

The companion [decision audit](../subagent_handoffs/033_acid_rain_decision_audit_2026_10_03.md) retains the exact cost matrix/loader, resource, refund, timer, and cleanup findings.
Its scalar table comparison is source agreement and cannot certify native payment, affordability, AI rank, or engine balance.
The critical-quotes archive preserves the newer closure before the owner repair.

## Reference and validation limits

The offline wiki and installed docs were read locally after retrieval gaps, without accessing the Paradox wiki on the web.
Relevant local references are Decision modding 305-355, Data structures 437-442, installed decisions/_documentation.md 1-43, installed effects_documentation.md 7910-7925, vanilla AFG.txt 1685-1747, and _exiled_governments_decisions.txt 475-484.
Reference hashes are retained in the critical/companion handoffs.
The documentation distinguishes temporary helper output storage, native availability, manual custom-cost debit, FROM state scope, and exclusive random upper endpoints.
It does not settle every native target syntax, dynamic timed-flag parameter, or asynchronous receipt behavior.

The newer A1-A20 comparison must wait for the decision worker's handoff and latest after bytes.
It must compare the immutable real before path to the actual after path under the identical fixture and disclose all transitive dependency revisions, including the separate Air gateway.
A result whose before helper closure mixes current owner-patched helpers cannot certify a numerical before/after delta.
No gameplay simplification or tuning change was made by this auditor.
Missing probability evaluation, bounded results, sweeps, simulation, sequence, render, and engine coverage are explicit omissions caused by route/input-coverage gaps.
This incomplete validation handoff was not committed into the shared index.
Skills used: chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-mtth.
No skill files were edited by this auditor.

## Resumed warning-completion and dependency audit

The read-only [Two Regions Ready follow-up](two_regions_ready_reachability_2026_10_03.md) distinguishes prestarted-action timing feasibility from the start-only warning receipt gap.
It preserves the original A1-A20 fixture and adds separate conditional traces rather than modifying the compare cases.
Its source-only before-helper walk identifies six uncaptured transitive classifier definitions and leaves full dependency isolation unresolved.
Current owner files are in progress, so the mandatory final-after comparison remains pending the finished worker handoff.
