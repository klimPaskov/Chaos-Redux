# Event 014 decision and mission final re-audit

Date: 2026-07-12
Audit mode: read-only for gameplay, localisation, assets, and spreadsheets
Audited surface: live Event 014 decisions, categories, decision triggers and effects, constants, dynamic modifiers, lifecycle on-actions, focus unlock consumers, AI weights, localisation, and registered decision/category art

## Verdict

Event 014 is **not completion-ready on the decision/mission surface**.

Severity count:

- High: 3
- Medium: 2
- Low: 0

The frozen 39-icon unified-decision closure is complete, all existing decision/category localisation and icon references resolve, the implemented paid recruitment/consumption paths are protected against the reviewed free-unit and duplicate-population exploits, and every selectable live decision has AI weight. Completion remains blocked by missing required maintained objectives, an inert Wendigo terminal-hunt unlock, and absent route-aware campaign targeting. Two aftermath lifecycle defects also remain.

## Sources and authority used

The audit followed AGENTS.md and the read-only auditor contract in .codex/agents/chaosx_decision_mission_auditor.toml.

Primary design authority:

- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_11_achievements_scenarios_and_aftermath.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md
- docs/specs/014_cannibalism_specs/matrices/decision_mission_matrix.md
- docs/plans/014_cannibalism_plans/improvement_loop/2026-07-12_event014_post_implementation_closure_addendum.md
- the accepted implementation, remediation, spread-ledger, focus, localisation, and three unified-icon handoffs under docs/plans/014_cannibalism_plans/subagent_handoffs/

Engine references:

- the required offline Paradox wiki snapshot pages for decisions, events, data structures, triggers, effects, modifiers, localisation, scopes, on-actions, ideas, AI, national focuses, interface modding, and scripted GUI
- vanilla documentation in common/decisions/_documentation.md, common/on_actions/_documentation.md, common/script_constants/documentation.md, documentation/script_concept_documentation.md, common/scripted_guis/_documentation.md, and common/ai_strategy/_documentation.md
- vanilla mission/target precedents in common/decisions/CHI_decisions.txt, AUS.txt, ETH.txt, and INS.txt

## Findings

### High

#### H-01 — Five of the seven required core maintained-objective families are absent

The source specification defines seven named objective families: Restore the route, Screen the division, Hold the prison, Reach the island, Break the network, Stop the unification, and Stop the transformation at part 6 lines 317-427. Phase A also explicitly reserves one active investigation-mission slot at part 6 lines 29-33. Acceptance requires missions to have success, failure, and partial-success outcomes and requires active-mission caps and target selection at part 12 lines 134-135.

The complete live decision inventory contains seven timed missions total:

- two ordinary-country missions at common/decisions/014_cannibalism_decisions.txt:63-158;
- four unified-country operational missions at common/decisions/014_cannibalism_unified_decisions.txt:76-101, 225-245, 428-448, and 538-558;
- one post-defeat compact-vigilance mission at common/decisions/014_cannibalism_achievement_decisions.txt:248-272.

Only the ordinary supply-corridor and formation-rotation missions correspond to the seven required core families. There is no maintained Hold the prison, Reach the island, Break the network, Stop the unification, or Stop the transformation objective, and there is no Phase-A investigation mission.

Some related instant actions exist. For example, convergence interdiction and island operations are selectable decisions at common/decisions/014_cannibalism_achievement_decisions.txt:64-153, and Wendigo counterwar actions exist at common/decisions/014_cannibalism_wendigo_decisions.txt:184-238. They do not implement the required shared-window objectives, progress tracking, maintained conditions, or success/partial/failure mission resolution.

The decision matrix also has no direct live decision implementation for several separately specified rows, including officer replacement, infiltrate cell, break ritual economy, recon silent island, liberate feeding state, submit to network, and resist unification (matrix lines 8, 13-14, 16, 19, and 26-27). A resist-unification event option exists, but it is not the specified warlord decision family.

Impact:

- the ordinary category cannot evolve through the complete mission arc;
- prison, island, network, convergence, and transformation counterplay lacks the timed objectives promised by the source of truth;
- the Phase-A mission-cap contract is structurally incomplete.

Required closure:

1. Implement the five missing maintained-objective families with bounded target selection and explicit start, success, partial, failure, cancellation, and cleanup paths.
2. Add the Phase-A investigation mission and enforce the one-investigation-mission cap.
3. Resolve the remaining decision-matrix family gaps as actual decisions or formally amend the source specification before completion. No silent substitution is acceptable.

#### H-02 — The Wendigo terminal-hunt focus unlock has no decision consumer

Part 6 requires Launch terminal hunt in the Wendigo action family at line 547.

The two terminal-focus helpers set cannibalism_wendigo_terminal_hunt_open at common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:436-456. Player-facing focus text says these focuses open and retain terminal-hunt decisions at localisation/english/014_cannibalism_l_english.yml:1366-1370.

A repository-wide live consumer scan found:

- two setters in the Wendigo focus effects;
- one cleanup clear at common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:544;
- no trigger, decision, category, GUI action, AI block, or execution effect that reads the flag.

The entire live Wendigo decision surface is common/decisions/014_cannibalism_wendigo_decisions.txt:9-238. It has seven command actions and four counterwar actions; none is a terminal-hunt action.

Impact:

- completing the advertised focus changes no player decision surface;
- the required terminal-hunt family is missing;
- the focus reward, localisation promise, decision implementation, and AI path disagree.

Required closure:

1. Implement the terminal-hunt decision family and gate it with cannibalism_wendigo_terminal_hunt_open.
2. Give it valid pre-lock target rules, costs, AI target scoring, effects, cooldown/mission behavior as designed, and cleanup when transformation breaks or locks.
3. Re-audit the focus tooltip against the final decision behavior.

#### H-03 — Hannibal and Wendigo expansion targeting is not route-aware and does not block all invalid targets

The AI specification requires Hannibal target scoring for population, supply, cells, prisons/ports, stability, adjacency, strategic rail/naval routes, and coalition leadership, with penalties or exclusion for wasteland, actual-nonhuman territory with no usable Larder, severe contamination, impossible naval reach, and overextension at part 9 lines 236-255. Wendigo must prefer cold/high-population routes before lock and major population centers/coalition capitals after lock at lines 269-283. Acceptance requires invalid routes and targets to be blocked at part 12 line 146.

The live unified country-target gates at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:502-530 exclude self, Event 014 active actors, faction members, subjects, capitulated countries, current wars for campaign targets, and a target lock. They do not exclude or score:

- actual-nonhuman targets;
- countries with no usable Larder/population route;
- severe contamination or wasteland-dominated targets;
- impossible naval reach;
- overextended or nonadjacent fronts.

The targeted decision AI at common/decisions/014_cannibalism_unified_decisions.txt:453-524 is mostly a base value plus root/global state. Only two actions inspect a simple FROM major check. Seed Major Enemy Army and Prepare Global Campaign do not score the target's population, supply, cells, ports/prisons, stability, adjacency, route access, or contamination.

The focus flag named cannibalism_unified_dynamic_campaign_scoring_open only adds campaign capacity at common/scripted_effects/014_cannibalism_unified_decision_effects.txt:257-260 and planning speed at lines 1176-1184. It never changes target selection.

Wendigo's focus helper assigns the same conquer weight to every current enemy at common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:169-178, and both terminal focuses call that same helper at lines 436-456. At terminal lock, common/scripted_effects/014_cannibalism_super_event_effects.txt:142-161 assigns the same conquest/antagonize/front request package to every extant noncapitulated country. No cold, population-center, or coalition-capital weighting is present.

Impact:

- the AI can spend scarce Larder, command power, and equipment on strategically invalid or explicitly forbidden target classes;
- the advertised dynamic campaign scoring is operational scaling, not target scoring;
- pre-lock and post-lock Wendigo behavior does not implement the required route distinction.

Required closure:

1. Add shared target-validity triggers for nonhuman, usable-population/Larder, contamination/wasteland, adjacency/naval reach, and lifecycle safety.
2. Add target-scope ai_will_do modifiers or a bounded scored-target helper for the positive and negative factors in part 9.
3. Separate Wendigo pre-lock cold/high-population scoring from post-lock population-center/coalition-capital scoring.
4. Re-run invalid-target, unreachable-island, contaminated-major, cold-route, and coalition-capital fixtures.

### Medium

#### M-01 — International-response and reconstruction categories can remain permanently visible and empty

Both aftermath categories use visible_when_empty = yes at common/decisions/categories/014_cannibalism_categories.txt:48-60.

International response remains visible whenever cannibalism_reconstruction_system_active exists at common/scripted_triggers/014_cannibalism_achievement_triggers.txt:243-253. Reconstruction remains visible while the same global flag and cannibalism_reconstruction_participant are set at lines 364-367.

Those flags are set for the aftermath at common/scripted_effects/014_cannibalism_achievement_effects.txt:678-699 and common/scripted_effects/014_cannibalism_super_event_effects.txt:261-266. The compact completion path at common/scripted_effects/014_cannibalism_achievement_effects.txt:810-820 clears only the active mission flag; it does not retire the participant or reconstruction-system flags. The only clear of cannibalism_reconstruction_system_active is the new-runtime initialization at common/scripted_effects/014_cannibalism_core_effects.txt:511-528. There is no clear of cannibalism_reconstruction_participant.

After every state is reconstructed, the compact is ratified, and the 365-day mission resolves, all selectable entries can disappear while both categories stay visible.

Impact:

- completed players retain one or two empty decision categories indefinitely;
- category cleanup does not satisfy the source clutter-control requirement.

Required closure:

Add an explicit aftermath-complete lifecycle condition. Either retire the category visibility flags after all participating work and compact vigilance are complete, or keep a real repeatable vigilance surface. Do not leave visible_when_empty categories with no remaining action.

#### M-02 — Compact vigilance has no partial-success outcome

The compact mission at common/decisions/014_cannibalism_achievement_decisions.txt:248-272 has a 365-day success/failure branch only. Its success and failure helpers at common/scripted_effects/014_cannibalism_achievement_effects.txt:810-820 likewise provide no partial resolution.

All six other live missions implement a partial-success path:

- ordinary missions: common/decisions/014_cannibalism_decisions.txt:87-96 and 150-158;
- unified missions: common/decisions/014_cannibalism_unified_decisions.txt:91-100, 235-244, 438-447, and 548-557.

Part 12 line 134 requires mission success, failure, and partial-success outcomes. The compact is a real timed mission and is not exempted by the aftermath specification.

Impact:

- a nearly maintained year-long compact resolves identically to an immediate failure;
- the seventh live mission is the only one that violates the mission outcome contract.

Required closure:

Track meaningful maintained-vigilance progress and add a partial outcome with distinct localisation, effects, and cleanup.

## Category lifecycle table

| Category | Opens when | Closes when | Audit result |
| --- | --- | --- | --- |
| Containment | Active ordinary Event 014 country plus cannibalism_containment_decisions_open | Local victory/cleanup or world end | Pass. Gate at common/scripted_triggers/014_cannibalism_triggers.txt:1094-1098. |
| Network alerts | A normal noncannibal country controls a state with a screenable inbound spread entry | No eligible controlled state remains | Pass. Gate at common/scripted_triggers/014_cannibalism_spread_triggers.txt:315-323. |
| Warlord command | Active warlord slot with decisions open, or inherited recruitment after reveal | Capitulation, world end, or cleanup | Pass. Gate at common/scripted_triggers/014_cannibalism_warlord_triggers.txt:9-28. |
| International response | Noncannibal country during Evolution II or reconstruction | World end; otherwise reconstruction flag persists | **Fail M-01.** Gate at common/scripted_triggers/014_cannibalism_achievement_triggers.txt:243-253. |
| Reconstruction | Reconstruction-system participant | World end; no normal completion retirement | **Fail M-01.** Gate at common/scripted_triggers/014_cannibalism_achievement_triggers.txt:364-367. |
| Unified command | Revealed CBL ordinary route plus command focus capacity | Wendigo route, capitulation, world end, or cleanup | Pass. Gates at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:9-38. |
| Unified Larder | Revealed CBL ordinary route plus Larder focus capacity | Wendigo route, capitulation, world end, or cleanup | Pass. Gates at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:41-48. |
| Unified war machine | Unified or inherited Wendigo recruitment plus army/navy/air capacity | Relevant route gate closes, capitulation, or world end | Pass for lifecycle. Gate at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:21-28 and 51-57. |
| Unified global campaign | Revealed CBL plus unlocked cell/campaign/counterwar capacity | Wendigo route, capitulation, world end, or cleanup | Pass for lifecycle; target quality fails H-03. Gate at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:60-75. |
| Unified world end | Final mobilization before lock, or ordinary terminal actor after world end | Cleanup/capitulation | Pass. The terminal actor's post-world-end continuation is deliberate at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:78-100. |
| Wendigo command | Revealed Wendigo route, live merge host, pre-lock transformation | Broken/locked transformation, world end, or capitulation | Pass for lifecycle; terminal-hunt content fails H-02. Gate at common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt:9-19. |
| Wendigo counterwar | Revealed pre-lock Wendigo route and at least one reachable live anchor | No reachable anchor, broken/locked transformation, world end, or capitulation | Pass. Bounded anchor-array gate at common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt:185-209. |

No prohibited on_daily, on_weekly, or on_monthly Event 014 world iteration exists. The Event 014 on-action file uses bounded capitulation, annexation, civil-war, subject, state-control, naval-invasion, and volunteer-return hooks only at common/on_actions/014_cannibalism_on_actions.txt:13-149.

## Mission inventory and outcome audit

| Live mission | Base/dynamic duration | Objective and cap | Success / partial / failure | Cleanup | Result |
| --- | ---: | --- | --- | --- | --- |
| Restore supply corridor | Dynamic; base hold 28 days plus timeout buffer and theater modifiers | Maintains control, transport reserves, and formation presence; one logistics flag | All three | Clears flag, progress, duration, and burden modifier | Pass as Restore the route equivalent |
| Rotate compromised formations | Dynamic; base hold 21 days plus timeout buffer and war/severity modifiers | Maintains cleared formation and support reserve; one formation flag | All three | Clears flag, progress, duration, division floor, and burden modifier | Pass as Screen the division equivalent |
| Unified command | 120-day base, focus-adjusted | Complete paid command operations; one command flag | All three | Clears active flag and progress | Pass |
| Unified Larder | 150-day base, focus-adjusted | Complete paid Larder operations; one Larder flag | All three | Clears active flag and progress | Pass |
| Unified war machine | 150-day base, focus-adjusted | Complete paid recruitment/war-machine operations; one war-machine flag | All three | Clears active flag and progress | Pass |
| Unified counterwar | 120-day base, focus-adjusted | Complete paid counterwar operations; one counterwar flag | All three | Clears active flag and progress | Pass |
| Maintain international inspection compact | 365 days | Maintain compact membership and no failure flag; fire once | Success/failure only | Clears active flag and records completion/failure | **Fail M-02** |

Required named-family coverage:

| Source family | Live maintained objective | Result |
| --- | --- | --- |
| Restore the route | Restore supply corridor | Pass |
| Screen the division | Rotate compromised formations | Pass |
| Hold the prison | None | **Fail H-01** |
| Reach the island | None; instant island actions only | **Fail H-01** |
| Break the network | None; instant joint suppression only | **Fail H-01** |
| Stop the unification | None; instant convergence interdiction/event response only | **Fail H-01** |
| Stop the transformation | None; instant anchor counterwar actions only | **Fail H-01** |
| Phase-A investigation slot | None | **Fail H-01** |

Mission progress and cleanup evidence:

- ordinary mission start, dynamic duration, caps, and activation: common/scripted_effects/014_cannibalism_decision_effects.txt:147-242;
- ordinary pulse progress/reset: common/scripted_effects/014_cannibalism_decision_effects.txt:246-263;
- ordinary cleanup and three-way outcomes: common/scripted_effects/014_cannibalism_decision_effects.txt:265-365;
- unified single-family activation: common/scripted_effects/014_cannibalism_unified_decision_effects.txt:1472-1519;
- unified three-way triggers: common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:630-664;
- unified cleanup/outcomes: common/scripted_effects/014_cannibalism_unified_decision_effects.txt:1521-1624.

## Cost and balance proof

Static inventory:

- 92 live decision entries: 85 selectable decisions and 7 automatic missions.
- 84 of 85 selectable decisions use custom_cost_trigger plus custom_cost_text.
- The sole cost-free selectable entry is cannibalism_end_terror_exploitation, an explicit cleanup action rather than a repeatable reward.
- None of the 85 selectable decisions uses a plain political-power cost.
- All 85 selectable decisions have ai_will_do.

The live costs cover manpower, command power, Army/Navy Experience, fuel, convoys, trains, trucks, infantry/support/artillery equipment, Larder, real state population, state control, war/route access, and mission/capacity state. This satisfies the concrete-cost design for implemented content; H-01 concerns missing families, not a political-power-store implementation.

Population and recruitment balance:

- unusable Larder states exclude wasteland, Death-consumed states, nuclear fallout, severe chemical/biological contamination, irreversible air contamination, most actual-nonhuman owners, depleted population, and exhausted consumption stages at common/scripted_triggers/014_cannibalism_triggers.txt:349-371;
- consumption requires correct control, no cooldown, and no stabilized/liberated recovery state at common/scripted_triggers/014_cannibalism_triggers.txt:413-428;
- the canonical transaction allocates a unique request id, rejects duplicate requests, applies exact civilian population loss, records Deaths, derives Larder only from the applied loss, applies diminishing yield, and sets a state cooldown at common/scripted_effects/014_cannibalism_core_effects.txt:2926-3167;
- the protected remainder is 5,000 people at common/script_constants/014_cannibalism_core_constants.txt:891;
- unified legion/bone-guard/origin recruitment costs 25K/20K/20K population and requires 30K/25K/25K, preserving the 5K floor at common/script_constants/014_cannibalism_unified_decision_constants.txt:93-108;
- unified paid units start with zero equipment and zero manpower at common/script_constants/014_cannibalism_unified_decision_constants.txt:180-181;
- warlord recruitment costs and minimum populations preserve the same 5K remainder across its unit families at common/script_constants/014_cannibalism_country_constants.txt:262-299, and units start at zero equipment/manpower at lines 312-315;
- Wendigo Pack training consumes exactly 160K from a state requiring 165K, verifies exact applied loss before spawning, and starts packs at zero equipment/manpower at common/script_constants/014_cannibalism_wendigo_constants.txt:217-224 and common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:156-190.

No balance simplification or magic fallback was found in these reviewed population/recruitment transactions.

## AI proof

Coverage:

- 85/85 selectable decisions contain ai_will_do.
- Ordinary containment weights react to crisis meters and policy, for example common/decisions/014_cannibalism_decisions.txt:56-60 and 119-123.
- Warlord choices react to Larder, war, origin, hierarchy, and network-route disposition throughout common/decisions/014_cannibalism_warlord_decisions.txt:34-441.
- Wendigo command weights distinguish anchor count, Larder, countdown, and counterwar urgency throughout common/decisions/014_cannibalism_wendigo_decisions.txt:27-237.

Failure boundary:

- weight presence is complete;
- strategic target selection is not complete, as documented in H-03.

## Cleanup and exploit proof

Reviewed exploit classes from part 9 lines 517-530:

| Exploit/lifecycle risk | Live protection | Result |
| --- | --- | --- |
| Repeat one population loss | Per-request sequence id plus per-state last request id and exact applied-loss receipt | Pass |
| Free scripted units | Population and Larder payment precedes spawn; zero starting manpower/equipment; hard caps and state cooldowns | Pass |
| Repeated warlord/unit harvest rewards | Warlord harvested-country array at common/scripted_effects/014_cannibalism_warlord_decision_effects.txt:685-710 | Pass |
| Repeated unified battlefield receipts | Distinct defeated-country array plus receipt cap at common/scripted_effects/014_cannibalism_unified_decision_effects.txt:1426-1469 | Pass |
| Stale spread target after annexation/tag migration | Stable spread ids, expected-id equality, lifecycle invalidation, and explicit unification migration; hooks at common/on_actions/014_cannibalism_on_actions.txt:64-69, 73-138 | Pass |
| Ordinary access to cannibal recruitment | Warlord/unified/Wendigo route gates in common/scripted_triggers/014_cannibalism_warlord_triggers.txt:9-28 and common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:9-28 | Pass |
| Wendigo units without crossover | Revealed Wendigo route, merge-host identity, pre-lock state, focus/cap/cost gates | Pass |
| Invalid Hannibal campaign targets | Incomplete route/target exclusions and scoring | **Fail H-03** |
| Empty aftermath categories | No normal completion retirement | **Fail M-01** |

No new free-unit, equipment-duplication, repeat-consumption, repeated-capitulation-receipt, or spread-entry reuse exploit was identified in the implemented decision surface.

## Icon and asset proof

All existing decision/category art wiring passes.

Global Event 014 decision/category audit:

- 104 icon references across 92 decisions and 12 categories;
- 104 unique sprite references;
- 104/104 local sprite definitions found;
- 104/104 registered texture files exist;
- 104 unique texture paths and 104 unique SHA-256 hashes;
- zero missing definitions, missing files, or runtime hash collisions.

Frozen unified 39-icon closure:

- common/decisions/014_cannibalism_unified_decisions.txt contains 39 decision icon references and 39 unique tokens;
- interface/014_cannibalism.gfx:80-118 contains the matching 39 sprite definitions and exact deterministic paths;
- all 39 runtime DDS files exist;
- all 39 DDS hashes are unique;
- every DDS is 4,224 bytes with a valid DDS header and 32 by 32 dimensions;
- 39 source PNGs and 39 processed PNGs exist, with 39 unique source hashes and 39 unique processed hashes;
- the three manifests cover rows 01-09, 10-24, and 25-39 as exact 9 + 15 + 15 decision sets;
- the three contact sheets were visually inspected at original resolution; final-size silhouettes are distinct and no placeholder, shared crop, recolor, mirror, or overlay-only duplicate was observed.

This satisfies the exact one-to-one closure contract at the accepted addendum lines 191-316. There is no icon blocker.

## Localisation and secrecy proof

Completeness:

- 92/92 decision titles and descriptions resolve;
- 12/12 category titles and descriptions resolve;
- 237/237 tooltip and custom-cost localisation references used by the decision files resolve.

Pre-reveal secrecy:

- containment is restricted to active ordinary countries and never exposes the revealed unified/Wendigo categories;
- unified categories require cannibalism_reveal_complete at common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:9-19;
- Wendigo categories require reveal plus the Wendigo route at common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt:9-19 and 193-209;
- the pre-reveal convergence mission concept requires spoiler-safe wording at part 6 line 413;
- 85 player-facing localisation keys reachable from the live containment, spread-alert, and pre-reveal international-response decision surfaces were checked for Hannibal, Lecter, and Wendigo; there were zero hits.

The existing pre-reveal decision text uses field hunger, compromised ranks, ritual cells, organized routes, likely convergence hosts, island hosts, prisons, and network signs without naming the concealed actor. Secrecy passes.

## Task-specific validation summary

| Check | Result |
| --- | --- |
| Decision/category inventory | 92 decisions, 7 missions, 12 categories |
| Selectable AI coverage | 85/85 |
| Concrete custom-cost coverage | 84/85; only the explicit terror-program cleanup is cost-free |
| Mission three-way outcomes | 6/7; compact vigilance fails M-02 |
| Required core mission families | 2/7 plus no Phase-A investigation mission; fails H-01 |
| Category lifecycle | 10 clean, 2 aftermath categories fail M-01 |
| Route-aware campaign target selection | Fails H-03 |
| Wendigo terminal-hunt consumer | Missing; fails H-02 |
| Decision/category localisation | 104/104 titles and descriptions; 237/237 referenced tooltips/cost strings |
| Pre-reveal identity scan | 85 reachable keys, 0 concealed-identity hits |
| All Event 014 decision/category icon wiring | 104/104 paths exist, 104 unique hashes |
| Frozen unified icon equality | 39 decisions = 39 sprites = 39 runtime DDS = 39 sources = 39 processed PNGs = 39 manifest rows |
| Recurring global iteration | None in Event 014 on-actions |

## Simplifications, omissions, and blockers

No implementation fallback or audit simplification was used. The audit was intentionally read-only and changed no gameplay, localisation, asset, GUI, spreadsheet, or focus file.

Completion blockers:

1. H-01: five required maintained-objective families and the Phase-A investigation mission are absent.
2. H-02: Wendigo terminal hunt is advertised and unlocked but not implemented.
3. H-03: Hannibal/Wendigo target selection does not implement required route-aware scoring or invalid-target exclusions.
4. M-01: two aftermath categories do not retire after completion.
5. M-02: compact vigilance has no partial-success outcome.

The icon package, existing localisation coverage, pre-reveal secrecy, implemented unit/population exploit protections, and selectable AI-weight coverage do not block completion.

## Files changed by this audit

- docs/plans/014_cannibalism_plans/subagent_handoffs/event014_decision_mission_reaudit_2026-07-12.md

No commit was created, as required.

## Skills used

- chaos-redux-decisions-missions
- chaos-redux-events
- chaos-redux-focus-trees
- chaos-redux-event-assets
- chaos-redux-subagents
