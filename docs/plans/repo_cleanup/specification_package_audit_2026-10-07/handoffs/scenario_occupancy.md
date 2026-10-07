# Repo Explorer Handoff

This is the read-only pre-allocation snapshot.
Current assignments and the disposition of its candidate proposals are in the [shared identifier registry](../../../../specs/shared_identifier_registry.md).

## Scope read

- Parent task: identify the authoritative implemented triggerable-scenario registry, workbook rows, reserved and legacy numeric identities, source-design proposals, owner systems, collisions, and unoccupied IDs.
- Explicit constraints: read-only audit. The parent owns final allocation. No gameplay, package, or workbook files were edited. The two requested report files are the only writes.
- Files and IDs requested: shared triggerable-scenario constants and initialization, Scenarios workbook sheet, SCN references in docs/specs and docs/plans, including IDs 14, 15, 17, 18, and 19.
- Skills and docs read: AGENTS.md; chaos-redux-subagents; chaos-redux-events; chaos-redux-event-planning; xlsx. The event scenario contract identifies the runtime registry; AGENTS.md and the spreadsheet skill identify the XLSX as the catalog source and CSVs as exports.

## Primary findings

The active shared scenario constants are 1, 2, 3, 5 through 16, 18, and 19. ID 14 belongs to the Fallout manual consequence sandbox and is initialized into the live shared scenario list and all four sortable views. It has no row in the authoritative workbook, even though the current system reference documents it as SCN-014. Do not reuse 14. The workbook currently holds 16 rows: SCN-001 through 003, SCN-005 through 013, SCN-015, SCN-016, SCN-018, and SCN-019. Every current workbook status is Needs Testing.

ID 15 is implemented as Missile Age for Event 032 in both runtime and workbook. Five other packages still propose or provisionally describe SCN-015: Event 030 All Times at Once; Event 038 Believers vs Nonbelievers; Event 043 Monsters from the Deep; Event 044 Yakubite Uprising; and Event 067 Generalissimo's Coup. Those are five unresolved proposals, not five reservations. Event 032 keeps its implemented identity.

ID 4 is a retired Final Silence compatibility alias. It is not present in the live registry or view lists, but the launch dispatcher redirects old ID 4 saves through the Fallout manual sweep. ID 17 has no active runtime key or workbook row, but the shared constants comment explicitly reserves it. The source does not name an owner for that reservation. Do not allocate either slot without a parent decision to release it.

The source-design scan found eight more named manual entries without numeric IDs: four Event 068 entries (First Colonies, The Empty Throne, Open Crossings, and The Reckoning of ZIN), one Event 069 Boxer challenge with four types, Event 070 Cookie Monster Uprising, Event 084 War for the Soul, and Event 085 The Ten Plagues. If all five SCN-015 proposals and all eight unnamed entries survive package review, a deterministic candidate sequence is Event 030→SCN-020; Event 038→SCN-021; Event 043→SCN-022; Event 044→SCN-023; Event 067→SCN-024; Event 068's four entries→SCN-025 through SCN-028 in the listed order; Event 069→SCN-029; Event 070→SCN-030; Event 084→SCN-031; Event 085→SCN-032. These are parent-review candidates only. No slot above 19 has been reserved or implemented by this audit.

World-end IDs use a separate world_end_scenario_id registry. Matching numerals there, including Event 043's world-end ID 15, do not collide with SCN numeric identities.

## Implemented ID and owner map

| ID | Runtime key | Current public/system name | Owner | Workbook row |
| --- | --- | --- | --- | --- |
| SCN-001 | zombie_apocalypse | Zombie Apocalypse | Event 002 | Scenarios row 2 |
| SCN-002 | mengele_clones | Army of Clones | Legacy shared clone scenario; original owner is not identified in the reviewed current docs. Event 016 only adds a connection hook. | Scenarios row 3 |
| SCN-003 | soviet_collapse | Soviet Collapse | Event 005, Union Unmade | Scenarios row 4 |
| SCN-004 | final_silence | Retired compatibility alias | Old saves redirect to Fallout; no live row | Missing |
| SCN-005 | world_in_fury | World in Fury | Event 007 | Scenarios row 5 |
| SCN-006 | death | Death | Event 010 | Scenarios row 6 |
| SCN-007 | disaster_barrage | Disaster Barrage | Event 013 | Scenarios row 7 |
| SCN-008 | independence_wave | Every Banner Rises | Event 006 | Scenarios row 8 |
| SCN-009 | coalition_unmasked | Coalition Unmasked | Event 011 | Scenarios row 9 |
| SCN-010 | cannibalism | The Hunger Lines | Event 014 | Scenarios row 10 |
| SCN-011 | africa_is_one | Africa Is One | Event 012 | Scenarios row 11 |
| SCN-012 | black_plague | Black Plague Unbound | Event 020 | Scenarios row 12 |
| SCN-013 | infantry_spawn | The Unbidden Muster | Event 019 | Scenarios row 13 |
| SCN-014 | fallout | Fallout manual consequence sandbox | Air Cleanliness/Fallout consequence system | Missing despite runtime registration |
| SCN-015 | missile_age | Missile Age | Event 032 | Scenarios row 15 |
| SCN-016 | global_jihad | Global Jihad | Event 031 | Scenarios row 16 |
| SCN-017 | no runtime key | Explicitly held; no owner found | Reservation rationale unresolved | Missing |
| SCN-018 | random_civil_war | The Fracture Cascade | Event 021 | Scenarios row 17 |
| SCN-019 | assassin_network | Assassin Network | Event 039 | Scenarios row 14 |

Owner and public-name references are in docs/systems/event_system/triggerable_scenarios.md:75–280, shared dispatch is in common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1106–1311, and event roots are in the corresponding events/<event number> files. IDs 004 and 017 are not free slots despite having no workbook rows.
## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| common/script_constants/chaosx_triggerable_scenarios_constants.txt | Source of numeric scenario keys; identifies Fallout, Missile Age, Global Jihad, Event 021, Assassin Network, and the reserved gap. | Lines 1–33; line 6 says ID 17 is reserved; lines 15–33 enumerate keys. |
| common/scripted_effects/chaosx_triggerable_scenarios_effects.txt | Builds the shared registry, sortable views, and launch dispatcher. | Initialization lines 80–214; ID 14 is added at 179–185; ID 15 at 187–193; ID 18 at 203–209; ID 19 at 211–217. ID 14 appears in all four view branches at 288, 447, 549, and 751. |
| common/scripted_effects/chaosx_triggerable_scenarios_effects.txt | Preserves old ID 4 saves. | Lines 1147–1163 dispatch IDs 14 and 4 to the same Fallout manual sweep; the comment says ID 4 is never shown in the live registry. |
| common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt | Accepts both the live Fallout ID and old Final Silence ID through the same Fallout gate. | Lines 176–185. |
| docs/spreadsheets/chaos_redux_events_catalog.xlsx | Authoritative catalog source, opened read-only with openpyxl. | Scenarios sheet rows 2–17. SHA-256: 43E4796531CB60C77CCF2B477F84CA35A643377C27D7E8D5B1CE6CA2D9997E10. |
| docs/systems/event_system/triggerable_scenarios.md | Current human-readable registry and owner map; also preserves historical identity notes. | Lines 75–280. Fallout is discussed at 199–203; Missile Age at 205–217; Global Jihad at 219–233; Fracture Cascade at 235–268; Assassin Network at 272–280. |
| docs/plans/032_missiles_plans/subagent_handoffs/032_scn015_triggerable_scenario_registry_handoff.md | Historical implementation handoff for the incumbent SCN-015 owner. | Lines 25–39 record Missile Age ID 15, Fallout ID 14, Global Jihad ID 16, and the separate world-end namespace. |
| docs/specs/030_time_traveler_specs/specs/030_time_traveler_spec_part_10_scenario_integrations_ai_balance.md | Event 030's unresolved SCN-015 working proposal. | Line 5; README line 28. |
| docs/specs/038_malta_crusaders_specs/13_triggerable_scenario.md | Event 038's provisional SCN-015 proposal. | Lines 5–14. |
| docs/specs/043_monsters_from_the_deep_specs/README.md and docs/specs/044_yakub_returns_specs/README.md | Conflicting Event 043 and 044 SCN-015 proposals. | Event 043 lines 26 and 156–157; Event 044 lines 14 and 74. |
| docs/specs/067_generalissimo_specs/README.md and docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_6_scenario_and_world_end.md | Event 067's unresolved SCN-015 proposal and obsolete catalog premise. | README lines 15 and 102; Part 6 lines 5–10. |
| docs/specs/068_zin_specs/068_zin_13_evolutions_scenarios_and_connections.md | Event 068 explicitly requires four separate scenario entries and defers numeric IDs to a registry audit. | Lines 42–53. |
| docs/specs/069_boxer_rebellion_specs/069_boxer_rebellion_spec_part_15_triggerable_scenarios.md | One Event 069 scenario with four selectable types; no numeric ID. | Lines 1–45. |
| docs/specs/070_cookie_click_specs/070_cookie_click_spec_part_12_the_final_bite_and_manual_scenarios.md | Event 070 names Cookie Monster Uprising; no numeric ID. | Lines 171–207. |
| docs/specs/084_the_peace_movement_specs/084_the_peace_movement_spec_part_11_war_for_the_soul.md | Event 084 names War for the Soul and explicitly says no exact ID is reserved. | Lines 1–6. |
| docs/specs/085_ten_plagues_of_egypt_specs/085_ten_plagues_of_egypt_spec_part_12_the_triggerable_scenario.md | Event 085 names The Ten Plagues; no numeric ID. | Lines 1–15. |
| docs/plans/039_murder_mystery_plans/validation/scenario_registration/registration_2026_10_03.md | Historical SCN-014 suggestion superseded by the authorized SCN-019 allocation. | Lines 9–10. |
| docs/plans/021_random_civil_war_plans/subagent_handoffs/test_route_inventory_2026-09-25.md | Identifies an older Event 021 SCN-014 reference as stale. | Line 17. |
| docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_7_world_reactions_and_ai.md | Prevents misattributing the legacy Army of Clones scenario to Event 016. | Lines 606–612 say Event 016 may connect to it but must not take over its identity. |

## Existing patterns

The runtime identity source is the script constant table. Shared initialization appends IDs and corresponding name-sort values; four explicit view branches provide the sortable scenario list; the dispatcher maps each ID constant to a scenario helper. A new runtime entry therefore needs one unique numeric identity through initialization, every view, eligibility, dispatch, localization, and the workbook.

Runtime keys are not always player-facing names. ID 10's key is cannibalism while the current name is The Hunger Lines; ID 13's key is infantry_spawn while the current name is The Unbidden Muster; ID 18's key is random_civil_war while the current name is The Fracture Cascade. Keep key aliases distinct from public SCN names when reconciling docs.

The XLSX is the source for catalog rows. The exported Scenarios CSV is read-only and was not used as authority. Workbook rows are appended rather than numerically sorted: SCN-019 is at Scenarios!A14, SCN-015 at A15, SCN-016 at A16, and SCN-018 at A17. Do not infer available IDs from workbook row order or from stale statements that the export reaches SCN-014.

## Vanilla or reference precedents

No vanilla or approved-mod precedent is needed for this identifier-only task. No engine syntax or gameplay behavior was changed.

## Likely edit order for the parent

1. Choose which unresolved package designs remain in scope, keeping each of the five SCN-015 proposals distinct and keeping Event 068's four specified entries separate.
2. If accepted, assign candidate slots in the JSON map or another parent-selected order. Keep implemented identities stable and do not use IDs 4, 14, 15, 17, 18, or 19.
3. Reconcile package wording that still calls SCN-015 available or describes the catalog as ending at SCN-014. Preserve unresolved acceptance claims until the parent records their basis.
4. Resolve whether Fallout ID 14 is intentionally excluded from the workbook or whether the workbook needs an authorized catalog update. Do not reassign ID 14.
5. For any later implementation, wire the chosen constant through initialization, all four sortable views, eligibility, dispatch, localization, and workbook in the same pass. Re-export CSVs only after the workbook owner edits the XLSX.

## Validation checks

After the parent chooses allocation candidates, check that each ID occurs once in the triggerable_scenario_id table, once in the initialized global.triggerable_scenario_all_ids sequence, and once per sortable view; confirm the dispatcher and launch eligibility use that same constant. Compare finalized XLSX rows against the runtime map and regenerate CSV exports only from the workbook. Search specs and plans for stale duplicate SCN labels, while distinguishing probability-fixture IDs from triggerable SCN identities and keeping world-end IDs in their separate namespace.

The source command used for identifier inventory was rg -o --no-filename SCN-[0-9]{3} across docs/specs and docs/plans, followed by focused searches for proposals and reservations. The workbook was read-only. No tests or workbook export were run because no source or workbook file was changed.

## Risks and blockers

Confirmed:

- Runtime ID 14 is owned by Fallout and visible in the shared scenario views, but the workbook has no SCN-014 row. The system document has an SCN-014 heading while also calling it not a catalog row, so catalog inclusion is unresolved; the ID itself is occupied.
- ID 4 is a retired compatibility alias that reaches Fallout, and ID 17 is explicitly held without a documented owner.
- Event 032 owns SCN-015 in runtime and workbook. Events 030, 038, 043, 044, and 067 still carry conflicting, unreserved SCN-015 proposals.
- Event 044 and Event 067 repeat the stale premise that the supplied scenario export reaches SCN-014. The current workbook already has SCN-015, 016, 018, and 019.
- The Event 032 HOI4 trace and render returned partial results with extensive unresolved diagnostics; they are useful artifact evidence, not a clean chain-validation claim.
- The Event 021 inspect request remained pending for about 62 seconds and was stopped without a result. No Event 021 render was attempted. The two source_lookup calls for the registry files also produced no observed result before their grouped request was stopped after about 3 minutes 36 seconds. No artifact or source revision was obtained from those calls.

Ordinary risk: the 13 suggested future slots rely on keeping all currently named scenario entries and the five SCN-015 proposals. They remain candidates until the parent accepts the designs and records the allocation decision.

## Recommended next action

Have the parent select a unique ID for each accepted, distinct scenario entry from the unoccupied sequence starting at SCN-020, record the allocation as a parent decision, and ask documentation curators to update only affected package reservations. Preserve current implementations, the ID 4 compatibility alias, and the ID 17 hold.

