# Event 006 Improvement Loop v10 Acceptance-Closure Addendum

**Date:** 2026-07-26

**Role:** `chaosx_improvement_loop_planner`

**Scope:** Plan-only re-audit after commits `cf2316a9a` and `f8ca54d24`.

**Implementation state:** This addendum changes no gameplay, localisation, assets, catalog data, or accepted specification.

## Recommendation

Event 006 should not receive another broad mechanic, route family, formable family, scripted GUI surface, super-event, achievement, or decorative animation layer.

The accepted design is already broad enough.

Closure is not yet justified because the exact ten-compatible-group release band remains unreachable, DM-58 does not consume the exact witness proved by its preflight, the authoritative focus-tree inspector still reports blocking geometry diagnostics, and the accepted scenario, League, formable, super-event, achievement, animation, AI, and balance surfaces lack complete runtime evidence.

The next tranche should therefore be an acceptance-closure tranche with four ordered responsibilities:

1. Replace DM-58's random greedy completion pass with an exact witness-preserving transaction.
2. Repair the remaining shared-focus geometry by coordinates only and close it with the authoritative MCP inspector and renderer.
3. Admit at most one source-grounded package from a distinct reservation group so the ten-country band can become reachable.
4. Execute the existing runtime acceptance matrices without expanding their design.

## Authority and evidence reviewed

This addendum follows `AGENTS.md`, the accepted Event 006 specifications and matrices under `docs/specs/006_independence_wave_specs/`, the v9 completion authority, the current DM-58 preflight handoff, the current focus-geometry handoff, the v5 improvement addendum, the Event 006 source-of-truth map, and the current package and asset handoffs.

The offline wiki review covered data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, national focus modding, country creation, interface modding, and scripted GUI modding.

The vanilla documentation review covered script collections, math expressions, script constants, effects, triggers, and event targets.

Vanilla precedents reviewed included explicit formable requirements in `common/decisions/formable_nation_decisions.txt`, invitation and integration sequencing in `common/decisions/African_Union_decisions.txt`, shared-focus structure in `common/national_focus/baltic_shared.txt`, and decision-category scripted GUI binding in `common/decisions/AST_decision_categories.txt`.

Read-only HOI4 MCP evidence was used only to inspect the current focus tree and discover decision and mission AI pools.

The installed package has no Technology Tree Viewer.

Event 006 does not require a technology conclusion, so this limitation does not block the addendum.

## Evidence delta after the two commits

### `cf2316a9a`: DM-58 preflight repair is necessary but incomplete

`has_independence_wave_reclamation_front_preflight` now provides a pure three-member, three-owner feasibility proof.

That closes the old availability false-positive identified by v9.

The paid completion resolver in `common/scripted_effects/006_independence_wave_decision_effects.txt` still loops the League member ledger, chooses `random_state`, immediately adds a claim and wargoal, and only later checks whether three rows were staged.

The proof and the resolver therefore solve different allocation problems.

A valid injective matching can exist while the random greedy resolver consumes an early owner or state choice that prevents the third row.

Rollback protects the costs, claims, and wargoals, but the mission can still report a failed reclamation front and enter a League crisis when the exact witness actually existed.

The commit is accepted as a preflight tranche and must not be reverted.

The remaining gap is the witness-preserving transaction defined below.

### `f8ca54d24`: offline geometry repair is partial

The current read-only focus inspection reports 184 focuses, 14 continuous focuses, and 223 connectors.

The authoritative validation still reports 14 blocking diagnostics, including eight node intersections, 60 connector crossings, 35 long connectors, and a maximum horizontal span of 80 columns.

Observed examples include founding-trunk fan-ins crossing food, fuel, depot, ministry, and provincial-integration lanes, plus the 37-column connector from `complete_founding_settlement` to `map_internal_power_centers`.

The offline parser's zero-diagnostic result is useful local evidence but does not close the authoritative acceptance gate.

The commit is accepted as a first coordinate repair and must not be reverted.

One coordinate-only repair remains queued.

### AGX overlay

The AGX package already has its bespoke eight-focus overlay.

The v5 recommendation to add that module is superseded by implementation.

Adding more AGX focuses, routes, rewards, or route emblems is rejected as bloat.

## Current design-gap ledger

| Surface | Current evidence | Remaining gap | Disposition |
| --- | --- | --- | --- |
| Allocator and runtime matrices | 149 publishers, 126 automatic or high-chaos candidates, and 138 scenario-ranked candidates are registered | Complete runtime evidence is not assembled across release, host/join, scenario, and exact-band gates | Queue acceptance evidence; reject allocator redesign |
| Ten-country capacity | Ten attested runtime package IDs exist, but `IW-008` and `IW-010` share `RG-RHINE-SAAR`, leaving nine compatible groups | The exact ten-compatible-group band is unreachable | Queue one distinct grounded package only |
| DM-58 | Pure exact preflight exists and rollback protects paid mutations | Completion does not freeze and consume the proved witness | Queue P0 exact transaction |
| Shared focus geometry | First coordinate repair is present | Authoritative MCP still reports 14 blockers | Queue P0 coordinate-only repair |
| Country packages | AGX is implemented; HAW is structurally complete; FIJ is package-ready in registry terms; several later packages remain source-gated | One distinct grounded package is required without introducing generic portraits or flags | Queue source-first HAW, with FIJ as the accepted alternative tranche |
| Grounded assets | Existing source retry and withdrawal handoffs are explicit | Some implemented packages still lack production-safe real rosters or route assets | Retain their existing queues; do not duplicate them here |
| Scenario contract | Six scenario types and four intensities are defined | The 24-cell runtime matrix is not complete | Queue the matrix; reject new scenario types or intensities |
| League lifecycle | Formation, refusal, contribution, rescue, challenge, expulsion, rivalry, transformation, and dissolution surfaces exist | End-to-end state and cleanup evidence is incomplete | Queue lifecycle scenarios; reject another League meter or institution |
| Formables | Forty-eight registry families exist; only bounded carrier/readiness adapters are implemented | Several accepted carriers are source-gated, and generic profiles cannot substitute for exact carriers | Queue only carrier-backed families; reject bulk activation |
| Super-events | `chaosx.se.6002` has five accepted predicates and a wired source path; `6001` lacks cleared exact audio | Predicate reachability, mutual exclusion, queue order, and playback evidence are incomplete | Queue `6002` evidence; keep `6001` blocked without a substitute |
| Achievements | Sixteen definitions exist | Positive, negative, disqualifier, and blocked-path evidence is incomplete | Queue a 16-row matrix; reject new achievements or weakened conditions |
| Animation | ASSET-040 through ASSET-043 have real state sheets and animated sprite definitions | Persistent UI consumers select static states and do not prove transition playback and return-to-current-state behavior | Queue bounded transitions; reject a fifth family or decorative looping |
| AI and balance | AI profiles and constants exist; read-only discovery found 10 decision and 54 mission candidates with all referenced inputs resolved | Full profile/scenario evaluation and balance evidence is absent | Queue evaluation, sweeps, comparisons, and scenario review; reject new profiles |

## P0-A: DM-58 exact witness-preserving transaction

### Player promise

When the League starts DM-58 with an exact legal three-front proof and the legal world state still exists at mission completion, the mission must form exactly three distinct member/state/owner rows.

It must never fail merely because a random or greedy iteration consumed the wrong legal row.

### Required transaction

The completion effect must use two phases.

#### Phase one: stage a pure witness

Clear the operation-scoped staging ledger before searching.

Search the frozen League member array in its registered order.

Within each member, search legal states in stable state database order.

Use nested exact matching or bounded backtracking to find the first complete witness containing exactly three distinct members, three distinct states, and three distinct external owners.

Store the result in three aligned arrays:

- staged member at index `n`
- staged state at index `n`
- staged owner at index `n`

Do not add claims, create wargoals, set used-state flags, pay costs, apply League deltas, or set completion flags during witness construction.

The three arrays must either all have the accepted minimum length or all be cleared.

The accepted minimum remains `constant:independence_wave_decision_gate.formation_member_minimum`.

No new magic number may duplicate that constant.

#### Phase two: validate and commit

Revalidate every aligned row against the same member, state, owner, war-legality, claim-or-border, non-League-owner, and no-existing-wargoal predicates immediately before mutation.

Require the aligned arrays to have equal length and the exact accepted minimum.

Only after all rows pass may the resolver add missing claims, create finite state wargoals, set readiness flags, pay the strategic and security costs, apply League deltas, publish the revisionist action, and set the coordinated-front flag.

Commit rows by aligned index so a member cannot be paired with a state or owner from a different row.

Clear transient arrays and targets on success, strategic failure, mission cancellation, Event 006 cleanup, League dissolution, and operator invalidation.

Existing persistent arrays used for active reclamation fronts may remain only if their purpose is distinct from the transient witness ledger and their row alignment is preserved.

### Failure classes

If the pure exact matcher finds no witness at mission completion because borders, ownership, League membership, war legality, or claims changed during the mission, use the existing strategic failure and League-crisis consequence.

If the pure matcher succeeds but the transaction invariant fails before any mutation, clear the staging ledger, apply no costs, claims, wargoals, League deltas, completion flag, failure flag, or crisis, and treat the condition as an implementation defect during validation.

The second class must not be converted into player-facing strategic failure.

### Acceptance scenarios

| ID | Setup | Required result |
| --- | --- | --- |
| DM58-TX-01 | Three eligible members each have one legal state under three distinct owners | Exactly three aligned rows commit |
| DM58-TX-02 | A greedy first choice blocks the third front, but an alternate injective matching exists | The bounded matcher finds the complete witness and commits |
| DM58-TX-03 | Four or more members have overlapping legal owners | The first complete stable-order witness commits; no fourth row is mutated |
| DM58-TX-04 | Preflight passes, but one owner or state becomes illegal before timeout | No partial mutations or costs; the existing strategic failure path fires once |
| DM58-TX-05 | Two members can target the same owner and another complete three-owner solution exists | The repeated-owner branch is skipped and the complete solution commits |
| DM58-TX-06 | No exact three-owner solution exists at activation | The mission cannot start |
| DM58-TX-07 | Cancellation, League dissolution, or Event 006 cleanup occurs with transient rows present | Every transient row, target, flag, and variable is cleared |
| DM58-TX-08 | Exact proof succeeds but an aligned ledger invariant is deliberately broken in a validation fixture | No player-facing crisis or mutation occurs |

### Implementation surfaces

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- Event 006 decision localisation for exact requirement, completion, and legitimate strategic failure wording
- Event 006 decision documentation and acceptance handoff

The existing preflight should remain the visibility and activation proof unless the implementation extracts a shared exact matcher without making the trigger mutating.

## P0-B: authoritative shared-focus geometry closure

This is a coordinate-only repair.

Do not add or remove focuses, change focus IDs, prerequisites, mutual exclusions, rewards, AI weights, route assignments, availability, continuous-focus definitions, or localisation.

Move the founding settlement and downstream state-building lanes so their connectors no longer intersect nodes or cross the food, fuel, depot, ministry, province, and power-center lanes.

Shorten the long founding-trunk connectors by moving the relevant downstream subtrees rather than changing dependencies.

Preserve the implemented AGX overlay and every other package overlay.

Acceptance requires a fresh read-only `hoi4.focus_inspect` and `hoi4.focus_render` against the current source.

The gate is zero blocking diagnostics, with the same 184 focuses, 14 continuous focuses, 223 connectors, and unchanged semantic graph.

An offline parser report may supplement but cannot replace this gate.

## P0-C: one distinct source-grounded package

Only one additional compatible reservation group should be admitted in this tranche.

The goal is to make the accepted ten-country band reachable, not to begin a package-volume sprint.

### First choice: HAW source-first admission

`IW-173` already has state 629, reservation group `RG-629`, a complete gameplay package, and a distinct reservation group.

It is the shortest safe capacity path only if a production-safe real period leader or authentic provisional institution source is cleared.

The package must not ship with the currently generic visible portrait roster.

Required order:

1. Continue source clearance for a period-correct Hawaiian leader, cabinet, assembly, municipal, labor, educational, veteran, or other authentic provisional institution consumer.
2. Audit identity, date, provenance, rights, resolution, crop suitability, and duplicate use.
3. Process and wire the grounded roster and any historically required route flags.
4. Rerun tag collision, state ownership, protected-host, reservation-group, visible-roster, focus-assignment, AI, and cleanup checks.
5. Admit `IW-173` only after every gate passes.

The Hawaiian package should preserve the accepted tension between the kingdom's institutional legacy, provisional civic administration, labor and municipal interests, and external plantation and naval pressure.

Royal restoration remains a route choice rather than the default state.

Any specific person proposed beyond the already audited candidates remains historically uncertain until a source handoff clears identity, period relevance, and rights.

### Accepted alternative: FIJ full package tranche

If HAW source clearance fails again, queue `IW-177` as the next design and implementation tranche.

FIJ has state 636, `RG-PACIFIC-ISLANDS`, registered tag reuse, complete 12-of-12 flag triplets in the current candidate audit, and a force plan.

FIJ is not admitted by this addendum.

It requires a full grounded package with real leadership or institutional imagery, history, parties, ideas, advisors, commanders, units, technology state, localisation, AI, focus assignment, cleanup, and runtime evidence.

Its accepted institutional identity is a founding congress that negotiates representation, veto, autonomy, revenue, defense, mixed-community rights, and the limits of any wider island federation.

The design should distinguish chiefly and communal authority, colonial administration, labor, shipping, and defense interests rather than treating Fiji or the Pacific as institutionally monolithic.

Exact personnel and constitutional claims remain uncertain until a dedicated source dossier verifies them.

### Samoa and Micronesia dispositions

`IW-175` Samoa remains a mutually exclusive Pacific alternative if FIJ becomes blocked.

Do not admit Samoa and Fiji merely to increase volume because both use `RG-PACIFIC-ISLANDS`.

Samoa would require a source-grounded package that handles chiefly institutions, port and customs administration, labor and shipping, and the divided colonial geography without turning wider claims into release territory.

`IW-179` Micronesian federation is rejected as the active next admission target.

The 2026-07-26 Henry Nanpei retry did not produce a production-safe full-resolution source, and the fictional Elias Kihleng substitute is forbidden.

FSM may re-enter the queue only after a new rights-valid source clears a real leader or authentic provisional institution.

### Ten-band acceptance cases

| ID | Setup | Required result |
| --- | --- | --- |
| CAP-10-01 | Current nine compatible runtime groups | Exact-ten band fails closed |
| CAP-10-02 | One grounded distinct group is admitted and all ten groups pass origin and host protection | Exactly ten compatible packages can be selected |
| CAP-10-03 | `IW-008` and `IW-010` are both otherwise eligible | They are never selected together because both use `RG-RHINE-SAAR` |
| CAP-10-04 | HAW or FIJ lacks one required grounded consumer | The package remains outside the runtime pool |
| CAP-10-05 | Samoa and Fiji are both registered | Reservation-group uniqueness prevents simultaneous admission |
| CAP-10-06 | A tenth tag exists but its origin is not viable or its host cannot retain a protected state | The top band fails closed without substitution |

No Rhineland/Saar rebinding is allowed to manufacture a tenth compatible group.

## P1: execute the existing acceptance ledger

The parent should maintain one evidence ledger keyed to the accepted IDs below.

This is validation work, not a new mechanic.

### Allocator and host/join

- Prove the configured low, medium, high, and maximum release counts against viable candidate pools.
- Prove origin ownership, controller, host protection, tag collision, reservation-group uniqueness, and package-readiness gates independently.
- Prove Event 5 host and join behavior for eligible, ineligible, dead, transferred, occupied, and already-living packages.
- Prove no scenario bypasses the same base candidate pool and readiness gates.
- Prove failure closes the band rather than substituting an ungrounded package.

### Scenario matrix

Run all 24 cells formed by the six accepted scenario types and four accepted intensities:

- sovereign scatter
- common congress
- wars of separation
- universal belligerence
- patron worlds
- great partition

For every cell, record selected packages, reservation groups, origin states, host survivors, release count, starting wars or diplomatic relationships, force allocation, patron relationships, League eligibility, and cleanup result.

Scenario type may alter diplomatic and war structure.

Intensity may alter accepted release count, territory, and force scale.

Neither dimension may bypass package readiness, grounded consumers, reservation-group uniqueness, or protected-host rules.

### League lifecycle

Prove the following state transitions with positive, negative, AI, and cleanup cases:

1. founding congress availability and minimum membership
2. invitation, acceptance, refusal, and cooldown
3. contribution and free-rider pressure
4. threatened-member rescue and failure
5. leadership challenge and succession
6. charter expulsion and target cleanup
7. rival League behavior
8. radical charter and DM-58 authorization
9. charter transformation
10. dissolution, member exit, operator death, and Event 006 cleanup

No additional League currency, chamber, council, or scripted GUI page is required.

### Formables

Retain the accepted fail-closed rule.

Generic registry profiles do not authorize runtime formation.

`FORM-01` through `FORM-05` remain the established operational baseline.

`FORM-12`, `FORM-13`, and `FORM-18` remain exact but blocked while their grounded carrier packages are withdrawn.

`FORM-24` West African Federation and `FORM-25` Sahel Confederation remain queued behind the sourced DOX and SOK package tranche and its missing roster, flag, and carrier evidence.

Their design should preserve negotiated federal, republican, traditional, religious, trade, military, and infrastructure settlements instead of restoring historical institutions as unchanged museum states.

`FORM-42` remains rejected until a legal current-map founding set and legitimacy proof are specified.

No state substitute is allowed.

`FORM-48` remains source-implemented but cannot close until an admitted compatible Pacific carrier and consent path make it reachable.

All other unimplemented families remain fail closed until a grounded carrier package gives them a concrete current-map reason to exist.

Do not bulk-activate `FORM-06` through `FORM-47`.

### Super-events

Do not add a third Event 006 super-event.

For `chaosx.se.6002`, prove each of its five accepted predicates independently, prove an ordinary non-terminal outcome fires none of them, prove mutually exclusive predicates cannot duplicate the event, prove FIFO queue behavior when another super-event is pending, and prove display, dismiss, cleanup, image, quote, and audio consumers.

`chaosx.se.6001` remains blocked on exact audio clearance.

No substitute track, silence fallback, or renamed generic event is accepted.

### Achievements

Do not add achievements or weaken conditions merely to make blocked achievements reachable.

Build a 16-row matrix containing:

- exact positive path
- closest negative path
- disqualifying flags and variables
- package, scenario, League, formable, or super-event dependency
- AI relevance
- cleanup or post-event persistence
- current reachability status

An achievement that depends on a blocked package or formable must remain explicitly blocked until that carrier is implemented.

### ASSET-040 through ASSET-043

Wire only the accepted transition behavior:

- ASSET-040 recognition seal transition
- ASSET-041 dependency warning transition
- ASSET-042 League charter activation transition
- ASSET-043 formable eligibility transition

Each transition must play from the previous logical state to the new logical state and then return to the current persistent static frame.

Reopening the scripted GUI must show the current state, not restart a stale transition.

Rapid state changes must resolve to the latest state without leaving an orphaned loop.

Hidden, unavailable, ineligible, dissolved, and Event 006 cleanup states must remove the transient consumer.

Do not add a fifth family or run permanent decorative loops.

### AI and balance

Read-only probability discovery found 10 decision candidates and 54 mission candidates in the current decision file.

The discovered pools have no unresolved referenced inputs, but discovery is not behavioral proof.

Use read-only probability evaluation, sweeps, seeded simulation where relevant, sequence analysis, and comparisons against the accepted 24 AI profiles.

At minimum, evaluate:

- fragile one-state release
- viable compact release
- armed high-capacity release
- conciliatory host
- guarded host
- revanchist host
- remnant host
- League leader
- small League member
- patron-aligned client
- radical revisionist member
- formable pursuer
- package with no legal territorial target
- package with several competing legal targets

Cross those profiles with the six scenario types and the relevant intensity boundaries.

Record action eligibility, resource affordability, target availability, route compliance, expected priority, observed weight, mission timeout risk, repeated-action risk, and cleanup.

Balance acceptance requires that fragile states prefer survival and institution-building, viable states can develop into regional actors, revisionist actions remain gated by capacity and charter state, hosts react according to their route, and AI never spends on an action with no legal consumer.

No new AI personality is required.

## Existing grounded-package queues retained without redesign

The IW-043 CHU and IW-058 ASY gameplay and formable work remain blocked by withdrawn generated portrait consumers.

The IW-093 DOX and IW-098 SOK gameplay tranche remains queued behind sourced visible rosters, final flags, and `FORM-24`/`FORM-25` carrier completion.

Those are accepted implementation queues, not new v10 expansion proposals.

Cornwall remains map-blocked.

No substitute state is accepted.

## Explicit queue and reject decisions

| Item | Decision | Reason |
| --- | --- | --- |
| DM-58 pure preflight | Accept as implemented | It closes availability feasibility |
| DM-58 exact witness transaction | Queue P0 | Completion can still fail a valid matching through random greedy allocation |
| First focus geometry repair | Accept as partial | It improved coordinates but did not close authoritative diagnostics |
| Second focus geometry repair | Queue P0 | MCP still reports 14 blockers |
| AGX eight-focus overlay | Accept as implemented | The v5 module request is superseded |
| More AGX content | Reject | It adds volume without closing an acceptance gap |
| HAW admission | Queue conditionally | Shortest distinct-group path, but grounded roster clearance is mandatory |
| FIJ package | Queue as accepted alternative tranche | Strong registry and asset readiness, but full grounded package is absent |
| Samoa package | Queue behind FIJ as a mutually exclusive alternative | Same reservation group; simultaneous admission adds volume without capacity |
| FSM admission | Reject as current target | Source retry failed and fictional substitution is forbidden |
| Bulk package sprint | Reject | One compatible group is sufficient for the outstanding capacity gate |
| New scenario type or intensity | Reject | The existing 24-cell design is unproven, not shallow |
| New League meter or institution | Reject | Existing lifecycle needs evidence and cleanup |
| Bulk formable activation | Reject | Exact carriers and readiness adapters are required |
| `FORM-42` state substitute | Reject | No legal founding set is defined |
| New super-event | Reject | Existing `6002` needs proof and `6001` needs exact audio |
| Substitute `6001` audio | Reject | Fallbacks are forbidden |
| New achievements or cheaper conditions | Reject | Existing 16-row matrix is incomplete |
| Fifth animation family or decorative loops | Reject | Existing transition consumers are incomplete |
| New AI profiles | Reject | Existing profiles need evaluation |
| Technology expansion | Reject as out of scope | No Event 006 design gap requires it |

## Prior-addendum disposition

The v5 `IW-179` P0 admission recommendation is rejected as the current target because the latest grounded-source retry did not clear a production consumer.

The v5 AGX overlay recommendation is superseded by implementation.

The `cf2316a9a` DM-58 handoff is accepted for pure preflight feasibility, while the exact witness-preserving completion transaction remains unresolved in this addendum.

The `f8ca54d24` focus handoff is accepted as a partial coordinate repair, while authoritative zero-blocker closure remains unresolved in this addendum.

Existing source, roster, flag, formable, super-event audio, animation-consumer, achievement, and runtime-matrix handoffs retain their recorded queue or blocked status.

This addendum does not create a second design layer for those gaps.

## What should not be added

Do not add another release algorithm, scenario axis, League subsystem, package overlay template, formable registry family, super-event, achievement, scripted GUI page, animation family, or AI profile.

Do not admit an ungrounded package to satisfy a number.

Do not use generic or generated portraits for real historical consumers.

Do not use substitute states, reservation-group rebinding, duplicate tags, silent audio, generic route flags, or copied country packages.

Do not broaden this tranche beyond one distinct package admission.

## Promotion rule

This addendum should remain in `docs/plans/006_independence_wave_plans/` while implementation and acceptance evidence are unresolved.

Do not promote it wholesale into the accepted specification.

If the parent accepts the durable DM-58 aligned-witness transaction contract, merge that contract into the decision-mechanics specification and decision mission matrix.

If HAW or FIJ is selected as the durable tenth-band package, merge only that accepted package identity, carrier, reservation-group, source, asset, AI, and acceptance contract into the appropriate Event 006 spec, matrix, and research dossier.

Acceptance evidence and temporary implementation ordering remain plan material.

## Closure gate

A closure handoff is appropriate only after:

- the exact ten-compatible-group band is reachable without a fallback
- DM-58 consumes an exact witness and passes its transaction scenarios
- authoritative focus inspection reports zero blocking diagnostics
- all 24 scenario cells have runtime evidence
- League lifecycle and cleanup scenarios pass
- every advertised formable is either operational with an exact carrier or explicitly retained as fail closed
- `chaosx.se.6002` has predicate, exclusion, queue, and playback evidence
- `chaosx.se.6001` is either cleared with its exact accepted audio or remains an explicit completion blocker
- all 16 achievements have positive, negative, disqualifier, and reachability evidence
- ASSET-040 through ASSET-043 have transition and return-to-current-state consumers
- the accepted AI profiles and balance scenarios have recorded evidence
- all grounded roster, flag, localisation, documentation, catalog, and cleanup consumers are aligned
- no accepted addendum remains unresolved, silently superseded, or hidden behind a simplification

Until those gates are met, Event 006 remains on hold and must not be reported complete.

## Parent handoff

**Design problem:** Event 006 has sufficient breadth, but its highest release band, exact DM-58 execution, focus geometry, and cross-system runtime proof remain incomplete.

**Proposed response:** Implement the DM-58 exact transaction, perform one MCP-closed coordinate repair, admit at most one source-grounded distinct package, and execute the existing acceptance ledger.

**Research basis:** Accepted Event 006 research and matrices, package source retries, current source inspection, offline wiki and vanilla documentation, vanilla decision/focus precedents, and read-only HOI4 focus and probability inspection.

**Historical and regional connections:** HAW should preserve Hawaiian institutional continuity and external economic/naval pressure; FIJ should center a negotiated multi-community founding congress; Samoa remains a distinct chiefly, maritime, customs, and divided-colonial alternative; West African and Sahel formables should transform living regional institutions through negotiated modern settlements.

**Files written:** `docs/plans/006_independence_wave_plans/subagent_handoffs/006_improvement_loop_v10_acceptance_closure_addendum_2026_07_26.md`

**Implementation surfaces affected:** Event 006 decision triggers, decision effects, DM-58 mission, shared focus coordinates, one country package and its assets, scenario evidence, League evidence, formable carriers, super-event `6002`, achievement evidence, ASSET-040 through ASSET-043 consumers, AI evaluation, balance evidence, localisation, documentation, and catalog alignment.

**Open questions for the parent:** Whether to continue HAW source clearance before authorizing the FIJ tranche; which implementation owner will build the DM-58 aligned witness ledger; and whether `6001` exact audio clearance is required for the current completion goal or will remain an explicit blocker.

**Prior addendum unresolved:** Yes.

The unresolved work is explicitly bounded above; no new pass should be requested for Event 006 until this addendum is implemented, folded into the accepted specs, queued with a reason, or rejected with a reason.

**Promotion decision:** Keep this file in `docs/plans` until the parent accepts and implements the durable contracts.
