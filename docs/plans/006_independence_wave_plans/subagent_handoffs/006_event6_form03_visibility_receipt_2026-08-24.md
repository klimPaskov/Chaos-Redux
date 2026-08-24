# Event 006 FORM-03 visibility receipt

Date: 2026-08-24

Status: **STATIC SOURCE RECEIPT COMPLETE / NO GAMEPLAY PATCH / RUNTIME MCP EVIDENCE BLOCKED**

This receipt audits every child action in `independence_wave_form03_low_countries_category` against the accepted phase docket scenarios in `006_event6_form03_phase_docket_improvement_addendum_2026_08_24.md`.

The receipt is source-static evidence derived from `common/decisions/006_independence_wave_form03_decisions.txt` and `common/scripted_triggers/006_independence_wave_form03_triggers.txt`; it is not a live-engine render or probability result.

The current decision source hash is `b8d1a30115f1b254b3e964251b5a26c7bee77329`, and the current trigger source hash is `70ccd3b169bbc739ae50ae00b363b06649186f46`.

## Status symbols

`N` means the decision is not visible, or the mission activation predicate is false.

`U` means the decision is visible, or the mission is activated, but its `available` contract is false for the fixture.

`S` means the decision is visible and startable, or the mission is activated and selectable.

`A` means the action is already active and is retained for timer continuity even though the active-work lock makes other actions unavailable.

Mission `R1` is evaluated through `activation`, because `visible` does not control selectable missions.

## Complete child inventory

The following aliases are used in every scenario row so that each of the 23 child actions is recorded exactly once per fixture.

| Alias | Child action |
|---|---|
| `D1` | `independence_wave_form03_authorize_core_delegation` |
| `D2` | `independence_wave_form03_withhold_core_delegation` |
| `D3` | `independence_wave_form03_belgium_authorize_founding_delegation` |
| `D4` | `independence_wave_form03_belgium_withhold_founding_delegation` |
| `D5` | `independence_wave_form03_join_as_autonomous_member` |
| `L1` | `independence_wave_form03_convene_language_convention` |
| `L2` | `independence_wave_form03_open_multilingual_service_examinations` |
| `L3` | `independence_wave_form03_publish_member_language_codes` |
| `L4` | `independence_wave_form03_establish_federal_language_appeals` |
| `L5` | `independence_wave_form03_extend_protected_local_services` |
| `W1` | `independence_wave_form03_reconnect_sambre_meuse_corridor` |
| `W2` | `independence_wave_form03_coordinate_frisian_waterway_standards` |
| `I1` | `independence_wave_form03_standardize_rail_and_customs_manifests` |
| `I2` | `independence_wave_form03_request_development_compact_technical_mission` |
| `I3` | `independence_wave_form03_invite_sovereign_corridor_partners` |
| `R1` | `independence_wave_form03_ratify_confederal_charter` |
| `R2` | `independence_wave_form03_resubmit_confederal_charter` |
| `R3` | `independence_wave_form03_reopen_charter_talks` |
| `R4` | `independence_wave_form03_repair_language_settlement` |
| `R5` | `independence_wave_form03_repair_industrial_compact` |
| `A1` | `independence_wave_form03_implement_member_language_guarantees` |
| `A2` | `independence_wave_form03_fund_associate_corridor_share` |
| `A3` | `independence_wave_form03_withdraw_from_autonomous_membership` |

## Fixture contract

Every valid-carrier fixture uses an admitted Event 006 FORM-03 carrier with `independence_wave_formable_family = low_countries_federation`, `independence_wave_formable_active`, `independence_wave_formable_committed`, `independence_wave_form03_lcx_identity_in_use`, and the exact AFX state 34 or AGX state 36 anchor owned and controlled by the carrier.

Every valid-carrier fixture has the second core connection, compatible constitutional or Development Compact route, no cleanup guard, no invalidation state, no war with the relevant member, and all ordinary command power, manpower, stability, civilian-factory, train, convoy, and equipment costs satisfied unless the row explicitly says that an action is unavailable because of a phase or lock.

Every valid-carrier fixture has no pending founding invitation, no unresolved founding response, no active sovereign-associate decision, and no active mission unless the row explicitly declares one.

Every valid-carrier fixture declares the League route and reserve explicitly: the Development Compact scenarios set `independence_wave_league_member`, `global.independence_wave_league_route = development_compact`, and reserve at or above the technical-mission minimum; scenarios without that route set the League-member flag or route false and therefore make `I2` not visible.

The carrier fixtures own and control only the anchor state named in that row unless a state-works action is explicitly active; an unowned second anchor makes the corresponding works child not visible.

The associate fixtures use a living BEL with `BEL_flanders` and state 6, or a living HOL with state 7, as a sovereign autonomous member connected to an active AFX carrier; their own exact state is owned and controlled by the associate.

## Scenario receipts

### `E6_FORM03_DOCKET_DRAFTING_PARALLEL`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter drafting, federal accommodation 55, industrial integration 55, language model `parallel_services`, ratification window closed, compromise and rupture flags clear, both anchor work and corridor standards unlocked.

Flags and locks: language convention complete, examinations and public-service actions unlocked, language codes and examinations incomplete, industrial board and corridor standards unlocked, all three active-work locks clear, no invitation or member response pending.

Targets and resources: state 34 valid for `W1`, state 36 invalid for `W2`, Development Compact route and reserve valid for `I2`, no sovereign member exists for `I3`, all costs and target controls valid, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L4 L5 W2 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = none`; `S = L2 L3 W1 I1 I2`; `A = none`.

Startable primary count: 5.

### `E6_FORM03_DOCKET_DRAFTING_TERRITORIAL`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter drafting, federal accommodation 55, industrial integration 55, language model `territorial_administration`, ratification window closed, compromise and rupture flags clear, both anchor work and corridor standards unlocked.

Flags and locks: language convention complete, examinations and public-service actions unlocked, language codes and federal appeals incomplete, industrial board and corridor standards unlocked, all three active-work locks clear, no invitation or member response pending.

Targets and resources: state 34 valid for `W1`, state 36 invalid for `W2`, Development Compact route and reserve valid for `I2`, no sovereign member exists for `I3`, all costs and target controls valid, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L5 W2 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = none`; `S = L3 L4 W1 I1 I2`; `A = none`.

Startable primary count: 5.

### `E6_FORM03_DOCKET_DRAFTING_REGISTER`

Actor and package: AGX, admitted IW-007, exact state 36 anchor owned and controlled, connected AFX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter drafting, federal accommodation 55, industrial integration 55, language model `working_register`, ratification window closed, compromise and rupture flags clear, both anchor work and corridor standards unlocked.

Flags and locks: language convention complete, examinations and public-service actions unlocked, language codes, examinations, and protected services incomplete, industrial board and corridor standards unlocked, all three active-work locks clear, no invitation or member response pending.

Targets and resources: state 36 valid for `W2`, state 34 invalid for `W1`, Development Compact route and reserve valid for `I2`, no sovereign member exists for `I3`, all costs and target controls valid, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L4 W1 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = none`; `S = L2 L3 L5 W2 I1 I2`; `A = none`.

Startable primary count: 6.

### `E6_FORM03_DOCKET_LANGUAGE_ACTIVE`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter drafting, federal accommodation 55, industrial integration 55, language model `working_register`, `L2` is an active timed decision, ratification window closed, compromise and rupture flags clear, both workstreams unlocked.

Flags and locks: language convention complete, examinations incomplete, public-service actions unlocked, industrial board and corridor standards unlocked, language lock set by active `L2`, state-works and industrial locks clear, no invitation or member response pending.

Targets and resources: state 34 valid for `W1`, state 36 invalid for `W2`, Development Compact route and reserve valid for `I2`, no sovereign member exists for `I3`, all costs and target controls valid, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L4 W2 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = L3 L5`; `S = W1 I1 I2`; `A = L2`.

Startable primary count: 3, with one continuity row retained.

### `E6_FORM03_DOCKET_WORKS_ACTIVE`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter drafting, federal accommodation 55, industrial integration 55, language model `parallel_services`, `W1` is an active timed decision, ratification window closed, compromise and rupture flags clear, both workstreams unlocked.

Flags and locks: language convention complete, examinations and language codes incomplete, public-service actions unlocked, industrial board and corridor standards unlocked, state-works lock set by active `W1`, language and industrial locks clear, no invitation or member response pending.

Targets and resources: state 34 valid and active for `W1`, state 36 invalid for `W2`, Development Compact route and reserve valid for `I2`, no sovereign member exists for `I3`, all costs and target controls valid, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L4 L5 W2 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = none`; `S = L2 L3 I1 I2`; `A = W1`.

Startable primary count: 4, with one continuity row retained.

### `E6_FORM03_DOCKET_INDUSTRIAL_ACTIVE`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter drafting, federal accommodation 55, industrial integration 55, language model `parallel_services`, `I1` is an active timed decision, ratification window closed, compromise and rupture flags clear, both workstreams unlocked.

Flags and locks: language convention complete, examinations and language codes incomplete, public-service actions unlocked, industrial board and corridor standards unlocked, industrial lock set by active `I1`, language and state-works locks clear, no invitation or member response pending.

Targets and resources: state 34 valid for `W1`, state 36 invalid for `W2`, Development Compact route and reserve valid for `I2`, no sovereign member exists for `I3`, all costs and target controls valid, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L4 L5 W2 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = I2`; `S = L2 L3 W1`; `A = I1`.

Startable primary count: 3, with one continuity row retained.

### `E6_FORM03_DOCKET_RATIFICATION_READY`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, all living member statuses resolved and sovereign corridor invitations already sent.

Phase and values: ratification window open, federal accommodation 75, industrial integration 75, language model `parallel_services`, post-charter complete flag clear, compromise and rupture flags clear.

Flags and locks: all language, works, manifest, and technical-mission completion flags set, all three active-work locks clear, no pending member response, all constitutional statuses resolved, federal language scope valid.

Targets and resources: no ordinary decision target remains valid, no reserve charge is pending, all ratification costs valid, `R1` activation and full ratification gate true, no active mission, cleanup clear.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R2 R3 R4 R5 A1 A2 A3`; `U = none`; `S = R1`; `A = none`.

Startable primary count: 1.

### `E6_FORM03_DOCKET_COMPROMISE_LANGUAGE`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter compromise, federal accommodation 55 below the ratified threshold, industrial integration 75 at the ratified threshold, language model `parallel_services`, ratification window closed, rupture flag clear.

Flags and locks: ordinary language, works, manifest, technical-mission, and invitation actions complete or closed, both repair-used flags clear, all three active-work locks clear, no pending member response, no active mission, cleanup clear.

Targets and resources: repair-language costs valid, repair-industrial target is not required because integration is already ratified, resubmission is visible but the full ratification gate is false, no reserve charge is pending.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R1 R3 R5 A1 A2 A3`; `U = R2`; `S = R4`; `A = none`.

Startable primary count: 1.

### `E6_FORM03_DOCKET_COMPROMISE_INDUSTRY`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter compromise, federal accommodation 75 at the ratified threshold, industrial integration 55 below the ratified threshold, language model `parallel_services`, ratification window closed, rupture flag clear.

Flags and locks: ordinary language, works, manifest, technical-mission, and invitation actions complete or closed, both repair-used flags clear, all three active-work locks clear, no pending member response, no active mission, cleanup clear.

Targets and resources: repair-industrial costs and state target valid, repair-language target is not required because accommodation is already ratified, resubmission is visible but the full ratification gate is false, no reserve charge is pending.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R1 R3 R4 A1 A2 A3`; `U = R2`; `S = R5`; `A = none`.

Startable primary count: 1.

### `E6_FORM03_DOCKET_RUPTURE`

Actor and package: AFX, admitted IW-006, exact state 34 anchor owned and controlled, connected AGX core partner, constitutional route, no sovereign autonomous member.

Phase and values: post-charter rupture, federal accommodation 30, industrial integration 30, language model `parallel_services`, ratification window closed, post-charter failed flag set.

Flags and locks: all ordinary progression actions are complete or closed, no active-work lock is set, no pending member response, no active mission, no cleanup guard, and no repair-used flag is relevant to the failed state.

Targets and resources: strategic reopening cost and civilian-factory target valid, all other ordinary targets invalidated by the failed phase, no reserve charge is pending.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R1 R2 R4 R5 A1 A2 A3`; `U = none`; `S = R3`; `A = none`.

Startable primary count: 1.

### `E6_FORM03_DOCKET_ASSOCIATE_PENDING`

Actor and package: BEL with `BEL_flanders`, admitted sovereign associate connected to an active AFX IW-006 carrier, state 6 owned and controlled, `independence_wave_form03_autonomous_member`, `independence_wave_form03_full_accession_requested`, and `independence_wave_form03_language_vote_pending` set.

Phase and values: associate scope rather than carrier scope, no carrier post-charter variables on BEL, no corridor invitation pending, no withdrawal record, all costs valid, no active decision, no mission, cleanup clear.

Flags and locks: the carrier owns state 34 and has the accepted route, BEL has no founding invitation, no founding response, no active language or corridor decision, and no invalidation or war state.

Targets and resources: BEL state 6 is a valid associate corridor target, language-guarantee cost is valid, withdrawal is legally available, and no technical-mission reserve is charged to BEL.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R1 R2 R3 R4 R5 A2`; `U = none`; `S = A1 A3`; `A = none`.

Startable primary count: 2.

### `E6_FORM03_DOCKET_ASSOCIATE_WITHDRAWAL`

Actor and package: HOL, admitted sovereign associate connected to an active AFX IW-006 carrier, state 7 owned and controlled, `independence_wave_form03_autonomous_member` set, no accession vote pending, and no corridor invitation pending.

Phase and values: associate scope rather than carrier scope, no carrier post-charter variables on HOL, no withdrawal record, no active decision, no mission, cleanup clear.

Flags and locks: the carrier owns state 34 and has the accepted route, HOL has no founding invitation, no founding response, no active language or corridor decision, and no invalidation or war state.

Targets and resources: withdrawal notice is valid, state 7 remains under HOL ownership and control, no language-guarantee or corridor-funding action is pending, and no technical-mission reserve is charged to HOL.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R1 R2 R3 R4 R5 A1 A2`; `U = none`; `S = A3`; `A = none`.

Startable primary count: 1.

### `E6_FORM03_DOCKET_INVALID_CARRIER`

Actor and package: BAX with a copied family marker but no AFX or AGX original-tag carrier identity, no valid FORM-03 registered-carrier trigger, no accepted anchor, and no active LCX identity.

Phase and values: all FORM-03 phase variables and flags are treated as absent for the source trigger contract, with no valid route, invitation, member, reserve, target, or mission state.

Flags and locks: no carrier, associate, founding, post-charter, work, repair, ratification, or withdrawal predicate can establish a valid FORM-03 scope, and cleanup is clear.

Targets and resources: even if BAX has generic resources or a copied decision-category token, no valid FORM-03 target or carrier connection exists.

Receipt: `N = D1 D2 D3 D4 D5 L1 L2 L3 L4 L5 W1 W2 I1 I2 I3 R1 R2 R3 R4 R5 A1 A2 A3`; `U = none`; `S = none`; `A = none`.

Startable primary count: 0.

## Result and disposition

All 23 child actions appear in the inventory and each of the 13 named fixtures records every child exactly once through the `N`, `U`, `S`, or `A` groups.

The maximum simultaneous startable-primary-action count is 6 in `E6_FORM03_DOCKET_DRAFTING_REGISTER`, which is at the accepted cap and does not exceed the conditional patch threshold.

The only continuity rows are the explicitly active `L2`, `W1`, and `I1` actions in their named fixtures; they remain visible as `A` while their corresponding locks suppress competing actions.

No phase-aware visibility or activation patch is justified by this receipt, so the queued addendum is closed without gameplay edits, new triggers, new flags, new categories, admission changes, AI changes, or a second progression system.

The exact 32-package attested boundary, 29 reservation groups, 40 runtime adapters, and 161 unattested selectable rows are unchanged.

The source receipt does not promote `independence_wave_form03_progression_attested` and does not claim runtime or MCP completion because the required live event/probability/GUI calls remain unavailable in this session.

## Validation and remaining blocker

The receipt was cross-checked against the 23 child blocks, their `visible` or `activation` predicates, their `available` and custom-cost predicates, the three active-work locks, and the associate trigger aliases in the current source.

Fresh HOI4 MCP event, decision, GUI, and probability evidence remains blocked by timeouts, transport closure, or incomplete adapters, so this handoff is static source evidence only.

No simplification or admission widening was made.
