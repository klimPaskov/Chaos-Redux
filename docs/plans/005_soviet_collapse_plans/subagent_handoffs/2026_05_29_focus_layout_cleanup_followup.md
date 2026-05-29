# Soviet Collapse Focus Layout Cleanup Follow-Up

Subagent: Chaos Redux focus tree auditor
Date: 2026-05-29
Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

Parent note honored: Ukraine and Belarus were treated as parent-owned local work. This pass prioritized non-Ukraine/non-Belarus trees and made only coordinate-only cleanup. No localisation files were changed.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Non-Ukraine/non-Belarus coordinate cleanup for mutual-exclusive marker offenders, same-row `dx = 1` spacing, and a few resulting pathline/duplicate-coordinate side effects. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Custom splinter coordinate cleanup for settlement/radical fork offenders, under-marker downstream focuses, and remaining same-row `dx = 1` pairs. |

## Follow-Up Patch IDs

Republic/non-Ukraine/non-Belarus focus ids adjusted in this pass:

- `baltic_soviet_collapse_coastal_defense_batteries`
- `central_asia_soviet_collapse_dushanbe_mountain_sovereignty`
- `central_asia_soviet_collapse_the_basmachi_amnesty_ledger`
- `central_asia_soviet_collapse_the_south_survives_together`
- `internal_soviet_collapse_black_sea_peninsula_guard`
- `internal_soviet_collapse_crimean_tatar_councils`
- `internal_soviet_collapse_far_eastern_rail_contracts`
- `internal_soviet_collapse_far_eastern_port_authority`
- `kaz_soviet_collapse_industrial_settlement_compacts`
- `kaz_soviet_collapse_lone_steppe_state`
- `kaz_soviet_collapse_tajik_mountain_guarantees`
- `kaz_soviet_collapse_teachers_of_the_new_steppe`
- `moldova_soviet_collapse_dniester_defense_directorate`

Custom splinter focus ids adjusted in this pass:

- `ARD_foreign_fleet_letters`
- `ARD_hidden_doctrine`
- `BAC_far_eastern_letters`
- `BAC_militia_training_yards`
- `BBH_non_domination_pacts`
- `DHC_propaganda`
- `FEV_hidden_doctrine`
- `FEV_industry_plan`
- `FTH_ukrainian_border_letters`
- `IUL_kazan_ufa_workshop_cordon`
- `IUL_league_corridor_bargain`
- `IUL_river_port_customs_board`
- `KHC_propaganda`
- `KRS_free_soviet_couriers`
- `MRC_foreign`
- `MRC_hidden_doctrine`
- `MRC_industry_plan`
- `NLC_heated_workshop_contracts`
- `PRA_neutral_corridor_letters`
- `SZA_hidden_doctrine`
- `SZA_industry_plan`
- `UWD_trans_ural_dispatch_board`
- `UWD_workers_canteen_compact`

The current scoped worktree also contains parent/earlier-pass edits in Ukraine, Belarus, birth-focus reward cleanup, and six custom splinter continuous-focus panel headers. Those were not reverted.

## Before And After

| Check | Before this follow-up | After this follow-up |
| --- | ---: | ---: |
| Non-Ukraine/non-Belarus mutual-exclusive layout offenders | 12 | 0 |
| Non-Ukraine/non-Belarus same-row `dx = 1` pairs | 23 | 0 |
| Duplicate coordinates per tree | 1 from current state during follow-up | 0 |
| Exact pathline hits, all scoped trees | 24 before follow-up baseline | 21 |
| Direct duplicate `add_ideas`/`add_timed_idea`/`add_equipment_to_stockpile` lines inside a focus | 0 | 0 |

## Validation

Final parser/topology audit:

- Trees: 34
- Focuses: 1506
- Duplicate focus ids: 0
- Missing prerequisites: 0
- Duplicate coordinates per tree: 0
- Exact focus-on-line path hits: 21 total, 20 outside Ukraine/Belarus
- Direct duplicate required reward lines: 0
- Broader duplicate reward warnings: 2 conditional duplicate claim lines in `central_asia_soviet_collapse_khwarazm_restoration_debate`
- Missing `ai_will_do`: 0
- Missing focus localisation names: 0
- Missing focus localisation descriptions: 0
- Missing focus icon definitions: 0
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed

The two broader duplicate reward warnings are not identical same-branch rewards. `central_asia_soviet_collapse_khwarazm_restoration_debate` grants `add_state_claim = 405` for both TMS and UZB branches, and `add_state_claim = 585` for both UZB and KYR branches.

## Remaining Risks

Remaining non-Ukraine/non-Belarus pathline crossings require a broader layout pass or route refactor:

- Baltic: `the_second_restoration` -> `the_baltic_question_resolved` crosses `baltic_shield_doctrine`.
- Baltic: `legal_continuity_government` -> `vilnius_border_statutes` crosses `the_legal_front_abroad`.
- Caucasus: `oil_emergency_directorate` -> `oil_state_command` crosses `civilian_oversight_of_oil`.
- Moldova: 4 crossings remain around `republic_of_crossings` and `black_soil_recovery_boards`.
- Kazakhstan: `the_alash_courts` -> `the_steppe_keeps_many_memories` crosses `the_written_alash_program`.
- Custom splinters: 11 crossings remain across BBH, DHC, KHC, UWD, IUL, BAC, ARD, and NLC.

Shallow decorative exclusive forks remain a design issue, not a safe coordinate patch issue. Settlement/radical or identity forks in several custom splinter trees still often differ mostly by generic helper payloads. They need route-specific decision hooks, war-plan behavior, cores/claims/wargoals, or special unit/factory packages in a parent-owned design pass.

No localisation keys or icon ids changed in this follow-up.
