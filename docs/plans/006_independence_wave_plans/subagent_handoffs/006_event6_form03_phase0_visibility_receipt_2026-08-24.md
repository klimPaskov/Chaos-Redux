# Event 006 FORM-03 Phase-0 visibility receipt

Date: 2026-08-24

Status: **STATIC RECEIPT COMPLETE / CONDITIONAL PATCH REJECTED AS UNNECESSARY**

## Scope and method

This receipt evaluates the 23 current child actions of `independence_wave_form03_low_countries_category` against the 13 scenarios required by the accepted FORM-03 phase-docket addendum. It is a source-level truth-table receipt, not a live save or rendered GUI claim. The evaluation follows the current `visible`, `activation`, `available`, actor-scope, active-lock, cost, ownership, control, and target predicates in `common/decisions/006_independence_wave_form03_decisions.txt` and `common/scripted_triggers/006_independence_wave_form03_triggers.txt`.

The fixture defaults are explicit and conservative: Event 006 is fired; the named actor exists; cleanup is false; the actor has sufficient civilian factories, command power, equipment, stability, and the required diplomatic or League Reserve resources unless a row says otherwise; the named target is valid and controlled; and no unrelated decision or mission is active. `S` means visible and startable, `U` means visible but unavailable, `A` means currently active and retained for timer continuity, and `N` means not visible. `A` is excluded from the simultaneous startable-primary count.

## Exact action order

Every matrix row contains exactly 23 cells in this order:

1. `independence_wave_form03_authorize_core_delegation`
2. `independence_wave_form03_withhold_core_delegation`
3. `independence_wave_form03_belgium_authorize_founding_delegation`
4. `independence_wave_form03_belgium_withhold_founding_delegation`
5. `independence_wave_form03_join_as_autonomous_member`
6. `independence_wave_form03_convene_language_convention`
7. `independence_wave_form03_open_multilingual_service_examinations`
8. `independence_wave_form03_publish_member_language_codes`
9. `independence_wave_form03_establish_federal_language_appeals`
10. `independence_wave_form03_extend_protected_local_services`
11. `independence_wave_form03_reconnect_sambre_meuse_corridor`
12. `independence_wave_form03_coordinate_frisian_waterway_standards`
13. `independence_wave_form03_standardize_rail_and_customs_manifests`
14. `independence_wave_form03_request_development_compact_technical_mission`
15. `independence_wave_form03_invite_sovereign_corridor_partners`
16. `independence_wave_form03_ratify_confederal_charter`
17. `independence_wave_form03_resubmit_confederal_charter`
18. `independence_wave_form03_reopen_charter_talks`
19. `independence_wave_form03_repair_language_settlement`
20. `independence_wave_form03_repair_industrial_compact`
21. `independence_wave_form03_implement_member_language_guarantees`
22. `independence_wave_form03_fund_associate_corridor_share`
23. `independence_wave_form03_withdraw_from_autonomous_membership`

## Scenario fixtures

Each fixture declares actor/package scope, phase/outcome, language model, FORM-03 values, active locks, invitation/member flags, League route/reserve, ownership/control, resources, target validity, mission state, and cleanup state. `good` means the shared resource and target gates pass; `low` means the named cost gate fails.

| Scenario | Actor and package | Phase/outcome and language | Locks and pending flags | League, territory, resources, mission, cleanup |
| --- | --- | --- | --- | --- |
| `E6_FORM03_DOCKET_DRAFTING_PARALLEL` | AFX, IW-006, registered carrier, exact capital anchor state 34 | pre-charter founding invitation; recognized; language model `parallel_services`; accommodation/integration `preparatory` | pending carrier invitation; no consent; no autonomous member; no active language/state-works/industrial lock | constitutional route; reserve `good`; state 34 owned/controlled/capital and target valid; no mission active; cleanup false |
| `E6_FORM03_DOCKET_DRAFTING_TERRITORIAL` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter drafting; language model `territorial_administration`; accommodation/integration `recognized` | appeals examinations and industrial board unlocked; no completion flags; all three locks false | constitutional route; reserve `good`; states 34 and 36 targets valid, state 34 owned/controlled; no mission active; cleanup false |
| `E6_FORM03_DOCKET_DRAFTING_REGISTER` | AGX, IW-007, active carrier, exact capital anchor state 36 | post-charter drafting; language model `working_register`; accommodation/integration `recognized` | appeals examinations and industrial board unlocked; no completion flags; all three locks false | Development Compact route; League member; reserve `good`; state 36 owned/controlled/capital and target valid; no mission active; cleanup false |
| `E6_FORM03_DOCKET_LANGUAGE_ACTIVE` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter; language model `working_register`; language convention active | language convention decision active; examinations, codes, and protected services remain incomplete; state/industrial locks false | constitutional route; reserve `good`; state 34 owned/controlled; no mission active; cleanup false |
| `E6_FORM03_DOCKET_WORKS_ACTIVE` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter; language model `parallel_services`; state works active | industrial board unlocked; Sambre-Meuse decision active; Frisian project remains incomplete; state-works lock true | constitutional route; reserve `good`; states 34 and 36 owned/controlled and valid; no mission active; cleanup false |
| `E6_FORM03_DOCKET_INDUSTRIAL_ACTIVE` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter; language model `parallel_services`; corridor administration unlocked | rail-manifests decision active; League member with Development Compact route; Belgian autonomous associate exists; industrial lock true | reserve `good`; states 34 and 36 owned/controlled; no mission active; cleanup false |
| `E6_FORM03_DOCKET_RATIFICATION_READY` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter ratification window; accommodation/integration `ratified`; constitutional statuses resolved | ratification window open; no compromise or failure; all active locks false | constitutional route; federal language scope valid; reserve `good`; states 34 and 36 owned/controlled; ratification mission not active; cleanup false |
| `E6_FORM03_DOCKET_COMPROMISE_LANGUAGE` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter compromise; federal accommodation below `ratified`; industrial integration `ratified` | language repair unused; no industrial repair; no industrial lock | constitutional route; full ratification gate valid; reserve `good`; states 34 and 36 owned/controlled; no mission active; cleanup false |
| `E6_FORM03_DOCKET_COMPROMISE_INDUSTRY` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter compromise; federal accommodation `ratified`; industrial integration below `ratified` | industrial repair unused; no language repair; no industrial lock | constitutional route; full ratification gate valid; reserve `good`; states 34 and 36 owned/controlled; no mission active; cleanup false |
| `E6_FORM03_DOCKET_RUPTURE` | AFX, IW-006, active carrier, exact capital anchor state 34 | post-charter failed/ruptured; accommodation/integration `failed` | post-charter failed flag; no industrial lock | constitutional route; reserve `good`; states 34 and 36 owned/controlled; no mission active; cleanup false |
| `E6_FORM03_DOCKET_ASSOCIATE_PENDING` | BEL with `BEL_flanders`, sovereign associate of active AFX IW-006 | autonomous member; language vote pending; associate status unresolved | full accession requested; no language guarantees; no corridor completion; no active associate decision | carrier connection valid; state 6 owned/controlled; diplomatic and administration resources `good`; no mission active; cleanup false |
| `E6_FORM03_DOCKET_ASSOCIATE_WITHDRAWAL` | HOL, sovereign associate of active AFX IW-006 | autonomous member; constitutional status resolved; no pending vote | no withdrawal record; no language or corridor decision active | carrier connection valid; Dutch corridor target valid and controlled; diplomatic resources `good`; no mission active; cleanup false |
| `E6_FORM03_DOCKET_INVALID_CARRIER` | FRA, no Event 006 FORM-03 carrier package | no active FORM-03 family; no phase/outcome; no language model | no invitation, route, associate, or member flags; all locks false | no valid reserve, territory, or target; no mission active; cleanup false |

## 299-cell visibility matrix

The following semicolon-delimited rows are intentionally machine-readable. Each row has one scenario label followed by exactly 23 action cells in the order above.

```text
scenario;01;02;03;04;05;06;07;08;09;10;11;12;13;14;15;16;17;18;19;20;21;22;23
E6_FORM03_DOCKET_DRAFTING_PARALLEL;S;S;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N
E6_FORM03_DOCKET_DRAFTING_TERRITORIAL;N;N;N;N;N;N;S;N;S;N;S;N;N;N;N;N;N;N;N;N;N;N;N
E6_FORM03_DOCKET_DRAFTING_REGISTER;N;N;N;N;N;N;S;N;N;S;N;S;N;N;N;N;N;N;N;N;N;N;N
E6_FORM03_DOCKET_LANGUAGE_ACTIVE;N;N;N;N;N;A;U;U;N;U;N;N;N;N;N;N;N;N;N;N;N;N;N
E6_FORM03_DOCKET_WORKS_ACTIVE;N;N;N;N;N;N;N;N;N;N;A;U;N;N;N;N;N;N;N;N;N;N;N
E6_FORM03_DOCKET_INDUSTRIAL_ACTIVE;N;N;N;N;N;N;N;N;N;N;N;N;A;U;U;N;N;N;N;N;N;N;N
E6_FORM03_DOCKET_RATIFICATION_READY;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;S;N;N;N;N;N;N;N
E6_FORM03_DOCKET_COMPROMISE_LANGUAGE;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;S;N;S;N;N;N;N
E6_FORM03_DOCKET_COMPROMISE_INDUSTRY;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;S;N;N;S;N;N;N
E6_FORM03_DOCKET_RUPTURE;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;S;N;N;N;N;N
E6_FORM03_DOCKET_ASSOCIATE_PENDING;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;S;N;S
E6_FORM03_DOCKET_ASSOCIATE_WITHDRAWAL;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;S
E6_FORM03_DOCKET_INVALID_CARRIER;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N;N
```

## Counts and decision

| Scenario | Startable primary actions | Continuity rows | Startable action IDs |
| --- | ---: | ---: | --- |
| `E6_FORM03_DOCKET_DRAFTING_PARALLEL` | 2 | 0 | authorize core, withhold core |
| `E6_FORM03_DOCKET_DRAFTING_TERRITORIAL` | 3 | 0 | open examinations, federal appeals, Sambre-Meuse |
| `E6_FORM03_DOCKET_DRAFTING_REGISTER` | 3 | 0 | open examinations, protected services, Frisian waterway |
| `E6_FORM03_DOCKET_LANGUAGE_ACTIVE` | 0 | 1 | none; language convention remains active |
| `E6_FORM03_DOCKET_WORKS_ACTIVE` | 0 | 1 | none; Sambre-Meuse remains active |
| `E6_FORM03_DOCKET_INDUSTRIAL_ACTIVE` | 0 | 1 | none; rail-manifests remains active |
| `E6_FORM03_DOCKET_RATIFICATION_READY` | 1 | 0 | ratify confederal charter |
| `E6_FORM03_DOCKET_COMPROMISE_LANGUAGE` | 2 | 0 | resubmit charter, repair language settlement |
| `E6_FORM03_DOCKET_COMPROMISE_INDUSTRY` | 2 | 0 | resubmit charter, repair industrial compact |
| `E6_FORM03_DOCKET_RUPTURE` | 1 | 0 | reopen charter talks |
| `E6_FORM03_DOCKET_ASSOCIATE_PENDING` | 2 | 0 | implement language guarantees, withdraw membership |
| `E6_FORM03_DOCKET_ASSOCIATE_WITHDRAWAL` | 1 | 0 | withdraw membership |
| `E6_FORM03_DOCKET_INVALID_CARRIER` | 0 | 0 | none |

Maximum simultaneous startable primary actions: **3**. No valid fixture exceeds the accepted six-action cap. The three `U` rows in each active-lock scenario are visible by their existing phase/flag predicates and correctly unavailable because the corresponding concurrency lock is true. The associate fixture intentionally retains the existing valid withdrawal choice alongside a pending guarantee choice; this is a player choice, not an invalid duplicate, and remains below the cap.

## Result and boundary

Phase 0 closes the accepted visibility-density question without a gameplay patch. No new scripted triggers, variables, flags, decisions, missions, costs, durations, effects, AI weights, categories, icons, or GUI changes are justified. The conditional visibility/activation patch is rejected as unnecessary, and the FORM-03 addendum can be marked closed with this receipt.

This is static source evidence only. It does not claim live GUI rendering, save/load continuity, typed MCP scenario evaluation, or whole-event completion. The Event 006 boundary remains 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested rows.
