# 2026-05-30 Soviet Collapse Focus Audit and Endpoint Duplicate Patch

## Scope and reading

Audited the requested Event 005 focus surfaces:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

Read `AGENTS.md`, focus-tree/decision/event/asset/improvement/subagent skills, required offline wiki pages, vanilla documentation, and a vanilla national focus precedent before inspecting or patching Chaos Redux files. Flags and flag GFX were not edited.

## Changed files

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Removed duplicate final-endgame helper calls from post-endgame extreme focuses that already require the normal endgame helper path. Added high-chaos identity payoff to `IUL_extreme_path` so it does not become a flag-only focus. |

No localisation, icon, scripted effect, decision, trigger, or flag file was changed by this pass.

## Changed focus ids

| Focus id | Before | After |
| --- | --- | --- |
| `BSC_extreme_path` | Recalled `soviet_collapse_complete_basmachi_endgame` after `BSC_endgame` already called it. | Keeps high-chaos identity only; no duplicate final spirit/faction/news helper. |
| `TNC_extreme_path` | Recalled `soviet_collapse_complete_turkestan_endgame` after `TNC_endgame`. | Keeps high-chaos identity only. |
| `ALA_extreme_path` | Recalled `soviet_collapse_complete_alash_endgame` after `ALA_endgame`. | Keeps high-chaos identity only. |
| `UDC_extreme_path` | Recalled `soviet_collapse_complete_union_defense_endgame` after `UDC_endgame`. | Keeps high-chaos identity only. |
| `SDZ_extreme_path` | Recalled `soviet_collapse_complete_security_directorate_endgame` after `SDZ_endgame`. | Keeps high-chaos identity only. |
| `GAC_extreme_path` | Recalled `soviet_collapse_complete_green_army_endgame` after `GAC_endgame`. | Keeps high-chaos identity only. |
| `DHC_extreme_path` | Recalled `soviet_collapse_complete_don_host_endgame` after `DHC_endgame` and `DHC_don_endurance`. | Keeps high-chaos identity only. |
| `KHC_extreme_path` | Recalled `soviet_collapse_complete_kuban_host_endgame` after `KHC_endgame` and `KHC_kuban_endurance`. | Keeps high-chaos identity only. |
| `UWD_extreme_path` | Recalled `soviet_collapse_complete_ural_workers_endgame` after `UWD_endgame`. | Keeps high-chaos identity only. |
| `IUL_extreme_path` | Recalled `soviet_collapse_complete_idel_ural_endgame` after `IUL_endgame`; otherwise had no visible high-chaos payoff. | Uses `soviet_collapse_apply_focus_high_chaos_identity = yes`. |
| `BAC_endgame` | Recalled `soviet_collapse_complete_birobidzhan_endgame` after prerequisite `BAC_extreme_path` had already called it. | Keeps legal recognition, depot/supply, and military consolidation only. |

Validation after patch shows each affected final helper now has one focus call site in the audited focus files.

## Route coverage table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine political, industry, diplomacy, expansion, military, Black Sea/grain routes | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Partial, layout risk | Broad route labels and hooks exist, but route-selector mutual exclusions are very wide: `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, and `ukr_soviet_collapse_protectorate_debate` create 8 long mutual-exclusion geometry flags in `005_soviet_collapse_republics.txt:228`, `267`, `312`, `541`, `1708`. |
| Generic breakaway republic political/industry/expansion baseline | `soviet_collapse_breakaway_focus_tree`, 36 focuses | Simplified | 0 direct decision/war/core/unit/template hooks by scan; still mostly generic survival rewards in `005_soviet_collapse_republics.txt:2356`. |
| Internal republic differentiated compact routes | `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Simplified | 0 direct hooks and 42 small-reward-token focuses. Needs local compact decisions and regional outcomes in `005_soviet_collapse_republics.txt:3153`. |
| Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan republic routes | `soviet_collapse_baltic_focus_tree`, `soviet_collapse_caucasus_focus_tree`, `soviet_collapse_central_asia_focus_tree`, `soviet_collapse_moldova_focus_tree`, `soviet_collapse_belarus_focus_tree`, `soviet_collapse_kazakhstan_focus_tree` | Partial | Caucasus, Central Asia, Belarus, Kazakhstan have some direct hooks. Baltic and Moldova still have 0 direct hooks. Kazakhstan is broadest and densest: 92 focuses, 53 small-reward-token focuses. |
| Construction/factory/directorate countries with industry, rail, supply, expansion | `CFR_soviet_collapse_focus_tree`, `MFR_soviet_collapse_focus_tree`, `OGB_soviet_collapse_focus_tree` | Partial | CFR/MFR have real industrial routes and hooks. OGB remains shallow: 23 focuses, 18 small-reward-token focuses, only 4 direct hooks in `005_soviet_collapse_factory_successors.txt:1136`. |
| Pale Railway Authority OP rail/supply state | `PRA_soviet_collapse_focus_tree`, 22 focuses | Partial, improved by prior dirty work | 11 direct hooks and rail/supply rewards exist. Still too short for requested overpowered rail-state route depth. |
| Dead Soldiers' Congress recruitable population, war goals, cores, zombie-like expansion | `DSC_soviet_collapse_focus_tree`, 18 focuses | Partial, improved by prior dirty work | 9 direct hooks and endgame core/wargoal helper exist, but route is still shallow and should add more dead-army pressure before `DSC_congress_of_the_dead_army`. |
| Crisis splinters `TSC`, `RMC`, `ICD`, `NRF` | 18-focus trees | Shallow to partial | NRF has 5 direct hooks; TSC/RMC/ICD have 1 each. These remain compact crisis trees, not full OP high-chaos routes. |
| Full custom splinters `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | 47-focus trees | Broad but mechanic-light | Most have route labels and helper chains, but many have 0 direct decision/war/core/unit hooks. `ARD` has 3 direct hooks; most others have none. |

## Idea reward audit

Command run:

```sh
rg -n "add_ideas|remove_ideas|swap_ideas" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_decisions.txt
```

Findings:

- Direct focus `add_ideas`: 0 in the three audited focus files.
- Direct focus `swap_ideas`: 0 in the three audited focus files.
- Direct focus `remove_ideas`: 8 cleanup/removal cases, all hidden effect cleanup or route cleanup:
  - `PRA_the_board_overrules_ministers` removes `pra_dispatcher_court_tensions`.
  - `TSC_the_committee_of_instruments` removes `tsc_field_station_rivalries`.
  - `RMC_communes_of_witnesses` removes `rmc_credal_cell_rivalries`.
  - `DSC_witness_officers` removes `dsc_grave_regiment_rivalries`.
  - `NRF_living_harbor_committees` removes `nrf_drowned_crew_disputes`.
  - `ICD_commissars_of_last_addresses` removes `icd_grave_commissar_rivalries`.
  - `mrc_protect_village_autonomy` removes `mrc_pass_confederation_rivalries`.
  - `OGB_the_council_takes_the_seal` removes `ogb_disputed_restored_name`.
- Indirect idea updates are concentrated in `soviet_collapse_update_consolidated_republic_ideas` and endpoint helpers in `common/scripted_effects/005_soviet_collapse_effects.txt`.
- Patched duplicate endpoint helper focus calls. Post-patch each of these is called once from the audited focus files: `soviet_collapse_complete_basmachi_endgame`, `soviet_collapse_complete_turkestan_endgame`, `soviet_collapse_complete_alash_endgame`, `soviet_collapse_complete_union_defense_endgame`, `soviet_collapse_complete_security_directorate_endgame`, `soviet_collapse_complete_green_army_endgame`, `soviet_collapse_complete_don_host_endgame`, `soviet_collapse_complete_kuban_host_endgame`, `soviet_collapse_complete_ural_workers_endgame`, `soviet_collapse_complete_idel_ural_endgame`, `soviet_collapse_complete_birobidzhan_endgame`.

## Shallow reward patterns

Mechanical scan counted focuses containing direct small reward tokens such as `add_equipment_to_stockpile`, `add_building_construction`, `add_political_power`, `add_stability`, `add_war_support`, `add_command_power`, or `add_manpower`.

| File | Focus count | Direct decision/war/core/unit/faction hooks | Small-reward-token focuses | Audit note |
| --- | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 21 | 293 | Many route names exist, but ordinary republics still lean on helper and small reward ladders. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 31 | 524 | Full custom splinters are often 47-focus trees with many helper-only rewards and few direct mechanics. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 14 | 48 | CFR/MFR are better; OGB remains shallow and small-reward-heavy. |

Worst broad gaps by direct-hook scan:

- `soviet_collapse_baltic_focus_tree`, `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_moldova_focus_tree`: 0 direct hooks.
- `ALA`, `BAC`, `BBH`, `BSC`, `DHC`, `FEV`, `FTH`, `GAC`, `IUL`, `KHC`, `KRS`, `MRC`, `NLC`, `SDZ`, `SZA`, `TNC`, `UDC`, `UWD`: 0 direct hooks despite route labels that imply decisions, expansion, war plans, logistics, or political systems.
- `OGB_soviet_collapse_focus_tree`: high priority shallow successor; 23 focuses, 18 small reward token focuses.

These are broad design gaps and should not be bulk-fixed by a subagent with shallow generated content.

## Pathline and layout audit

Coordinate heuristic results:

- Exact duplicate focus coordinates: 0.
- Focus sitting directly on vertical/horizontal prerequisite pathline: 0.
- Long/wide mutual exclusion geometry flags: 8, all in Ukraine:
  - `ukr_soviet_collapse_socialist_republic_without_moscow` at `005_soviet_collapse_republics.txt:228` against `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_black_banner_compact`, and `ukr_soviet_collapse_protectorate_debate`.
  - `ukr_soviet_collapse_black_banner_compact` at `005_soviet_collapse_republics.txt:267` against `ukr_soviet_collapse_officers_above_parties` and `ukr_soviet_collapse_elections_under_shellfire`.
  - `ukr_soviet_collapse_elections_under_shellfire` at `005_soviet_collapse_republics.txt:312` against `ukr_soviet_collapse_officers_above_parties` and `ukr_soviet_collapse_protectorate_debate`.
  - `ukr_soviet_collapse_officers_above_parties` at `005_soviet_collapse_republics.txt:541` against `ukr_soviet_collapse_protectorate_debate`.
- Too-close diagonal/row heuristic produced 286 flags. Many are normal dense-tree diagonals, but Kazakhstan and Ukraine have the highest visible density and should be reviewed first.

Patch not attempted for these layout issues because cleaning Ukraine route geometry requires route selector repositioning and possibly prerequisite reshaping, which is broader than a safe local edit.

## Icon coverage table

Icon definitions were checked against mod and vanilla `.gfx` definitions.

| File | Focuses | Icons assigned | Unresolved icons | Repeated icon ids | Repeated uses | Notes |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 501 | 0 | 22 | 65 | Top repeats include `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`. |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 1005 | 0 | 99 | 219 | Top repeats include `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`, `GFX_focus_IUL_war_plan`. |
| `005_soviet_collapse_factory_successors.txt` | 128 | 128 | 0 | 11 | 26 | CFR repeats construction motifs; not broken, but still below the spec's distinct-icon quality bar. |

No icon reference was patched. Flags and flag sprites remained out of scope.

## Localisation and reward mismatch list

Localisation scan across `localisation/english/005_soviet_collapse*.yml`:

- Missing focus name keys: 0.
- Missing focus description keys: 0.

Reward-tone mismatches and simplifications remain:

- Many `*_war_plan`, `*_diplomatic_plan`, `*_league`, `*_industry_plan`, and `*_endgame` focuses in custom splinter trees still route through broad shared helpers rather than direct decisions, war goals, cores, units, or route-specific mechanics. Examples with 0 direct hooks by tree: `FEV_soviet_collapse_focus_tree`, `NLC_soviet_collapse_focus_tree`, `MRC_soviet_collapse_focus_tree`, `IUL_soviet_collapse_focus_tree`.
- `soviet_collapse_moldova_focus_tree` contains bridge, union, river, and Ukrainian corridor route names but has 0 direct hooks by scan.
- `soviet_collapse_baltic_focus_tree` contains restoration, ports, foreign protection, and Baltic coordination route names but has 0 direct hooks by scan.
- `OGB_soviet_collapse_focus_tree` promises a Volga restoration route but remains a compact successor with little direct decision/formable/expansion integration.

## AI behavior gaps

All audited focuses have `ai_will_do`.

| File | Focuses | Missing AI | Base-only AI blocks | Route/state-aware AI blocks |
| --- | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 219 | 238 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 84 | 891 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 0 | 119 |

Gaps:

- Republic trees still have many base-only AI blocks, especially Ukraine opening/mid-route focuses and shared republic trees.
- Custom splinters often have route-state modifiers, but many direct route choices still do not create persistent `add_ai_strategy` aggression; this weakens the "extremely overpowered and aggressive" requirement.
- The remaining 0-direct-hook splinter trees need AI behavior tied to unlocked expansion decisions and target selection once those mechanics are added.

## High-priority parent fixes

1. Ukraine route layout: clean the wide mutual-exclusion geometry around `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, and `ukr_soviet_collapse_protectorate_debate`. This should be a layout-aware route pass, not a blind x/y shuffle.
2. Add direct mechanics to 0-hook trees, starting with `soviet_collapse_moldova_focus_tree`, `soviet_collapse_baltic_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, `FEV_soviet_collapse_focus_tree`, `NLC_soviet_collapse_focus_tree`, `MRC_soviet_collapse_focus_tree`, and `IUL_soviet_collapse_focus_tree`.
3. Rework `OGB_soviet_collapse_focus_tree` into a real Volga restoration successor with decision hooks, expansion/coring or settlement mechanics, and stronger route AI.
4. For high-chaos 47-focus trees, route `*_war_plan`, `*_hidden_doctrine`, and `*_extreme_path` through direct expansion decisions, dynamic wargoal helpers, core/integration effects, and persistent aggressive AI strategies.
5. Reduce repeated small rewards by replacing isolated stockpile/building grants with route-specific decision unlocks, state-targeted missions, rail/supply programs, unit templates, and postwar coring/integration decisions.
6. Icon pass: no missing icons, but repeated icon ids remain high, especially custom splinters. Do not touch flags.

## Validation run

Commands run:

```sh
rg -n "add_ideas|remove_ideas|swap_ideas" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_decisions.txt
python3 - <<'PY'  # focus/helper/layout/localisation/icon/mechanic scans
git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml
```

Results:

- `git diff --check`: no output.
- Post-patch duplicate endpoint helper call count: 1 call each for the 11 affected helpers.
- Localisation: 0 missing focus names/descriptions across audited Event 005 localisation files.
- Icon references: 0 unresolved focus icons against mod plus vanilla `.gfx`.

Skipped validation:

- No in-game load or external HOI4 parser run from this subagent pass.
- No commit made, per instruction.

## Remaining route risks

The small patch removes one duplicate-helper class, but the full user objective remains incomplete. Broad route-depth work is still required for many republic and custom splinter trees. The parent should implement the high-priority fixes above in focused tranches and then rerun focus-tree and decision audits before any completion claim.
