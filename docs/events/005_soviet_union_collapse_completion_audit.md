# Event 005 Soviet Union Collapse Completion Audit

Current audit date: 2026-05-18

This audit maps the active Soviet Collapse correction objective to current repository evidence after the spawn-balance, collapse-pacing, focus-layout, terminal-cleanup, and flag-orientation passes.

## Source Order

Required source order:

1. `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md`
2. `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md`
3. `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md`
4. `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md`
5. `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md`
6. `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md`
7. `AGENTS.md`
8. `chaos-redux-events`
9. `chaos-redux-event-assets`
10. `chaos-redux-super-events`

`tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` is not present in `tmp/` during this audit. The current implementation was checked against the available spawn-balance cleanup spec and the four final clean specs; final closure should either restore the missing continuation spec or explicitly waive it.

## Input File Audit

Requested source files as of 2026-05-18:

| Path | State | Lines | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md` | Present | 287 | 15899 | `9ac9d2553dffc54b6023c56f2dbde6efac310343b20873c77b1f50e6e5339750` |
| `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` | Missing | - | - | - |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md` | Present | 3418 | 162378 | `c0f474e97482a4eed3d4f9b8cbead930471f296d741e9805a0fea03b38e685e7` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md` | Present | 6327 | 191503 | `32284c8e2f424818be5dfbb81c394d9c1de7e666a93545586a1e2e1710276234` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md` | Present | 7535 | 554089 | `724a3bfb7c00aa28debf788649413da311224044fe4b0f4f8f726ee345275de7` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md` | Present | 3889 | 148956 | `60e2cac0717579afc60a3a6414558c00122d3fbae7d4e205af27671f7d6bc428` |

Recovery searches performed:

```text
find . -path './.git' -prune -o -type f \( -iname '*event_log*mission*balance*focus*cleanup*' -o -iname '*mission_balance_focus*' -o -iname '*005_soviet_union_collapse*cleanup*' \) -print
result: only tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md

git log --all --oneline -- tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md
result: no commits

git log --all --name-only --pretty=format: | rg '005_soviet_union_collapse.*(event_log|mission_balance|focus_cleanup|cleanup).*spec\.md'
result: no matching tracked history entry for the missing continuation spec
```

Present `tmp/` Event 005 spec files are:

```text
005_soviet_union_collapse_comprehensive_correction_spec.md
005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md
005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md
005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md
005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md
005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md
```

## Prompt To Artifact Checklist

| Requirement | Evidence | Status |
| --- | --- | --- |
| Event 005 remains Soviet Collapse with entry event format `chaosx.nr5.1` | `events/005_soviet_collapse.txt`; event docs in `docs/events/005_soviet_union_collapse.md` | Implemented; final parser audit passed |
| Dynamic crisis values and central tuning | `common/script_constants/005_soviet_collapse_constants.txt`, `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt` | Implemented; final parser audit passed |
| Stronger Soviet Collapse ideas and spirits | `common/ideas/005_soviet_collapse_ideas.txt` and the crisis effects use multi-modifier packages for Union Crisis, defensive coordination, depot seizures, legal claims, foreign volunteers, old networks, factory states, and high-chaos successors; the current idea parser audit found no Event 005 idea with fewer than three modifier entries, no idea without modifiers, and no tiny-only package. The remaining 2-3% components appear only inside broader 3-5 modifier spirits. | Implemented for current surface |
| Random first wave from structured pools | `soviet_collapse_release_initial_republics` clears and fills `global.soviet_collapse_first_wave_republics` through western, Caucasus, and Central Asian random pool helpers, then releases the selected scopes | Implemented |
| Kazakhstan first-wave restraint | `can_soviet_collapse_open_kazakhstan_first_wave` requires southern breakaway pressure, weak obedience, war or low Soviet condition, or high chaos; Kazakhstan is outside the normal Central Asian first-wave pool | Implemented |
| Union Crisis Threat and Moscow Authority pacing | Opening values start from central constants, apply visible condition modifiers, then use `soviet_collapse_recalculate_total_threat` with clamping and `constant:soviet_collapse_baseline.total_threat_multiplier`; Union Unmade uses high breakaway count plus authority, threat, League, and high-chaos gates | Implemented for current tuning |
| Soviet goal-style objectives with capacity limits | `common/decisions/005_soviet_collapse_decisions.txt` has 128 `soviet_collapse_soviet_mission_*` mission blocks | Implemented; final parser audit passed |
| Longer varied Soviet mission deadlines | The 128 Soviet missions use 11 named `@soviet_collapse_mission_days_*` constants ranging from 95 to 365 days; no mission uses a single shared `@soviet_collapse_opening_mission_days` timeout | Implemented; timeout audit passed |
| Decision cost corrections | `Send Loyalist Officers` spends army XP and command power only; `Restore Party Control` spends 2,000 infantry equipment, 200 support equipment, and 10,000 manpower through central `soviet_collapse_decision_cost` constants and matching trigger/localisation keys | Implemented |
| Blocked cost localisation | Event 005 blocked cost lines in `localisation/english/005_soviet_collapse_l_english.yml` use `Need ...` wording; the blocked-line word-count audit found zero blocked lines over seven words after stripping icons, formatting, and dynamic values | Implemented; localisation audit passed |
| Foreign intervention categories and action-based aid | `soviet_collapse_foreign_patron_category` has 7 targeted decision blocks with `days_re_enable`; `soviet_collapse_breakaway_category` has 4 action blocks; the decision audit found no active timed foreign intervention missions outside the 128 Soviet crisis missions | Implemented for current layer; catalog row updated |
| Crisis decision AI behavior | The four Soviet responses, four breakaway actions, and seven foreign patron actions use dynamic `ai_will_do` modifiers tied to crisis variables, war state, League coordination, faction state, and chaos tier; route-specific custom-country action boards keep their compact fixed weights for their foundational package | Implemented for the main crisis layer |
| Runtime focus trees for republics and breakaways | Focus counts: Ukraine 153, Belarus 83, Kazakhstan 87, fallback breakaway 53, Baltic 36, Caucasus 33, Central Asia 34, Moldova 23 | Implemented for these trees |
| High-chaos successor focus trees | Focus counts: CFR 58, MFR 46, OGB 54, ICD 24, KRS 24, FTH 24, BBH 24, BSC 24, TNC 24, ALA 24, UDC 24, SDZ 24, RMC 24, RCD 24, ILU 24, PRA 24, TSC 24, BLT 24, NRF 24, GAC 24, DHC 24, KHC 24, FEV 24, SZA 24, UWD 24, MRC 24, IUL 24, BAC 24, ARD 24, TRS 24, NLC 24, SEP 24, DSC 24, COU 24, BEC 24, RLD 24, LID 24, IRA 24 | Implemented for these thirty-eight successors |
| Non-linear focus structure, route locks, branch zones, focus filters, AI behavior | Focus files use route-specific branches, `search_filters`, `ai_will_do`, and mutual exclusions; parser audit over 46 focus trees and 1,500 focus IDs found no duplicate IDs, missing focus references, self-references, one-way mutual exclusions, unknown mutual targets, exact coordinate collisions, missing icons, missing `ai_will_do`, or missing/duplicated `completion_reward` blocks | Implemented for current focus trees |
| Full package for every implemented custom country | Registered special Event 005 custom tags currently found: `CFR`, `MFR`, `OGB`, `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, `NRF`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `TRS`, `NLC`, `SEP`, `DSC`, `COU`, `BEC`, `RLD`, `LID`, and `IRA` | Implemented for thirty-eight |
| Starting divisions for appearing republics and serious splinters | `soviet_collapse_setup_breakaway_country` creates the shared `Emergency Republican Guard` template, grants manpower/equipment, and scales guard and field unit packages by major/regional tag, chaos tier, Soviet war state, weak center state, one-use declaration flags, and terminal collapse state | Implemented for current appearing republics and implemented successors |
| Union Unmade first-month lock | `soviet_collapse_initialize_crisis_values` sets `soviet_collapse_union_unmade_first_month_lock` for 31 days; `soviet_collapse_maybe_show_union_unmade_super_event` refuses to fire while the lock exists | Implemented |
| Terminal ordinary republic release | `soviet_collapse_show_union_unmade_super_event` calls `SOV = { soviet_collapse_apply_terminal_collapse = yes }`; terminal collapse releases unreleased supported ordinary republics under Soviet ownership/control and frees existing supported Soviet-subject republics before adding high-chaos successors | Implemented |
| Terminal high-chaos successor activation | `soviet_collapse_spawn_terminal_high_chaos_successors` retries high-chaos successor spawning and, at chaos tier 5, prepares terminal gate flags before activating all eligible special actors whose packages and territory gates pass | Implemented for current successor set |
| Terminal mission and category cleanup | `is_soviet_collapse_active` excludes `soviet_collapse_terminal_collapse`; terminal cleanup clears active crisis flags, one-use declaration flags, stale loyal-unit and district war-room helper flags, removes all 128 active Soviet crisis missions, blocks further objective activation, and hides Soviet, breakaway, foreign patron, regional faction, and special-actor categories after terminal collapse | Implemented |
| Achievements | 47 Event 005 achievement definitions; 47 Event 005 NAME keys; GFX/DDS coverage previously checked clean; route flag audit checked 89 achievement flags | Implemented; route flag audit passed |
| Event log details | `GetEventsLogEventDetailDescription` maps Event ID 5 to `chaosx.events_log.window.event_details.soviet_collapse`; that localisation composes live in-world status lines through `GetEventsLogSovietCollapseDetail*` scripted localisation for crisis state, first-wave state, League status, Moscow Authority, Union Crisis Threat, foreign intervention, and old-movement or high-chaos splinter pressure | Implemented |
| Evolution logging | Event 005 has one `record_events_log_evolution_entry` writer, under `soviet_collapse_record_high_chaos_successor_evolution`; baseline crisis setup and objective pressure effects only change crisis variables and event flow | Implemented for current high-chaos successor logging |
| Super-events | Slots 14-27 have helpers, assets, localisation, audio references, constants, and route calls from implemented capstones | Implemented for current surfaces |
| Super-event slot 14, The Union Unmade | Broad breakaway pressure calls `soviet_collapse_maybe_show_union_unmade_super_event`; `UDC_extreme_path` and `udc_push_extreme_route` call `soviet_collapse_complete_union_defense_endgame`, which fires `soviet_collapse_show_union_unmade_super_event` | Implemented through breakaway-count pressure and the Union Defense package |
| Super-event slot 15, The Black Banner Returns | `FTH_extreme_path`, `BBH_extreme_path`, `fth_push_extreme_route`, and `bbh_push_extreme_route` call `soviet_collapse_complete_black_banner_endgame`, which fires the helper | Implemented through the Free Territory and Black Banner packages |
| Super-event slot 16, The Dead Are Citizens | `ICD_extreme_path`, `icd_push_extreme_route`, `RMC_extreme_path`, `rmc_push_extreme_route`, `SEP_extreme_path`, `sep_push_extreme_route`, `DSC_extreme_path`, `dsc_push_extreme_route`, `COU_extreme_path`, `BEC_extreme_path`, `RLD_extreme_path`, `LID_extreme_path`, `IRA_extreme_path`, and their push-extreme decisions call dead-state or Red Martyrs endgame helpers, which fire the helper | Implemented through the Iron Commissariat, Red Martyrs, Sepulchre Soviet, Dead Soldiers, Unburied Commissariat, Black Earth, Red Lazarus, Last International, and Iron Resurrection packages |
| Super-event slot 17, The World as One Factory | `ILU_extreme_path` and `ilu_push_extreme_route` call `soviet_collapse_complete_iron_liturgy_endgame`, which fires the helper | Implemented through the Iron Liturgy package |
| Super-event slot 18, Every Port a Council | `KRS_extreme_path`, `krs_push_extreme_route`, `NRF_extreme_path`, `nrf_push_extreme_route`, `ARD_extreme_path`, and `ard_push_extreme_route` call their port-council, northern-revenant, or Arctic directorate endgame helpers, which fire the helper | Implemented through the Kronstadt, Northern Revenant, and Arctic Naval Directorate packages |
| Super-event slot 24, Steppe Federation | `BSC_extreme_path`, `TNC_extreme_path`, `ALA_extreme_path`, and their push-extreme decisions call their Central Asian endgame helpers, which fire the helper | Implemented through the Basmachi, Turkestan, and Alash packages |
| Super-event slot 27, The Eastern Buffer Coalition | `moldova_soviet_collapse_alliance_not_union` calls `soviet_collapse_show_eastern_buffer_coalition_super_event` | Implemented through the Moldova regional tree |
| Docs | Event doc and super-event research docs exist and are aligned with current route wiring | Implemented for current surfaces |
| Asset reuse and created assets | Current Event 005 docs record reused focus, achievement, super-event assets, and the 570-file custom flag orientation audit; no historical flags were regenerated in the latest pass | Implemented for current surfaces |
| Flag orientation audit | 38 Event 005 custom tags across base, communism, democratic, fascism, and neutrality variants were checked in normal, medium, and small flag folders; all 570 files exist, decode cleanly, use vanilla-matching bottom-origin TGA headers, and average-downsample comparison finds no small/medium variant closer to a vertically flipped large source | Audit passed; no binary correction required by current evidence |
| Localisation design-language cleanup | Search across `common/`, `events/`, `localisation/`, `interface/`, and `docs/` found no player-facing instance of `starts from a low dynamic baseline in calm conditions` | Implemented |
| Spreadsheet updates | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, row 6 / Event ID 5, now summarizes the current dynamic crisis, no-baseline-evolution rule, tier 4 and tier 5 high-chaos successor mutation logs, no dedicated world-end scenario, and updated implementation status | Implemented; workbook package and LibreOffice open/convert validation passed |
| Completion readiness | Current audit records the available spawn-balance cleanup evidence, thirty-eight implemented custom successor packages, terminal cleanup, focus-layout cleanup, flag orientation audit, and parser validations | Not closed because one requested continuation spec file is absent from `tmp/` |

## Current Focus Counts

Command evidence:

```text
CFR_soviet_collapse_focus_tree 58
BBH_soviet_collapse_focus_tree 24
BSC_soviet_collapse_focus_tree 24
ALA_soviet_collapse_focus_tree 24
FTH_soviet_collapse_focus_tree 24
ICD_soviet_collapse_focus_tree 24
KRS_soviet_collapse_focus_tree 24
TNC_soviet_collapse_focus_tree 24
UDC_soviet_collapse_focus_tree 24
SDZ_soviet_collapse_focus_tree 24
RMC_soviet_collapse_focus_tree 24
RCD_soviet_collapse_focus_tree 24
ILU_soviet_collapse_focus_tree 24
PRA_soviet_collapse_focus_tree 24
TSC_soviet_collapse_focus_tree 24
BLT_soviet_collapse_focus_tree 24
NRF_soviet_collapse_focus_tree 24
GAC_soviet_collapse_focus_tree 24
DHC_soviet_collapse_focus_tree 24
KHC_soviet_collapse_focus_tree 24
FEV_soviet_collapse_focus_tree 24
SZA_soviet_collapse_focus_tree 24
UWD_soviet_collapse_focus_tree 24
MRC_soviet_collapse_focus_tree 24
IUL_soviet_collapse_focus_tree 24
BAC_soviet_collapse_focus_tree 24
ARD_soviet_collapse_focus_tree 24
TRS_soviet_collapse_focus_tree 24
NLC_soviet_collapse_focus_tree 24
SEP_soviet_collapse_focus_tree 24
DSC_soviet_collapse_focus_tree 24
COU_soviet_collapse_focus_tree 24
BEC_soviet_collapse_focus_tree 24
RLD_soviet_collapse_focus_tree 24
LID_soviet_collapse_focus_tree 24
IRA_soviet_collapse_focus_tree 24
MFR_soviet_collapse_focus_tree 46
OGB_soviet_collapse_focus_tree 54
soviet_collapse_baltic_focus_tree 36
soviet_collapse_belarus_focus_tree 83
soviet_collapse_breakaway_focus_tree 53
soviet_collapse_caucasus_focus_tree 33
soviet_collapse_central_asia_focus_tree 34
soviet_collapse_kazakhstan_focus_tree 87
soviet_collapse_moldova_focus_tree 23
soviet_collapse_ukraine_focus_tree 153
```

## Focus Tree Integrity Audit

Parser-oriented audit coverage for `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, and `common/national_focus/005_soviet_collapse_custom_splinters.txt`:

```text
FINAL AUDIT PASSED
focuses 1500
duplicates 0
missing_refs 0
self_refs 0
nonreciprocal_mutual 0
missing_ai 0
missing_reward 0
missions 128
custom_country_tags 38
achievements 47
achievement_flags 89
super_events 14
xlsx_status Implemented - Final Audit Passed
```

The audit checked:

- unique focus IDs across the Event 005 focus files
- `prerequisite` and `mutually_exclusive` focus targets
- focus self-references
- presence of `icon`, `completion_reward`, and `ai_will_do`
- focus icon sprite definitions across mod and vanilla `interface/*.gfx`
- focus name and description localisation keys across mod and vanilla English localisation
- exactly one `completion_reward` block per focus

## Starting Division And Reinforcement Audit

Event 005 uses runtime setup instead of static OOB files for mid-game republics and successors. This matches the engine model where OOB files are loaded at game start through country history or explicitly through `load_oob`, while these countries are created or converted during the event chain.

Audited runtime setup:

- `soviet_collapse_release_initial_republics` selects from western, Caucasus, and Central Asian pools, releases the selected scopes, and keeps Kazakhstan behind its separate southern and high-chaos gate.
- `soviet_collapse_setup_southern_republic_if_valid` flags southern republics and sends them through the shared setup effect.
- `soviet_collapse_spawn_cfr_if_enabled`, `soviet_collapse_spawn_mfr_if_enabled`, and `soviet_collapse_spawn_ogb_if_enabled` transfer the successor states before calling their setup effects.
- `soviet_collapse_setup_breakaway_country` grants dynamic manpower, infantry equipment, support equipment, artillery, defensive ideas, one locked `Emergency Republican Guard` template, guard units, and field units at `capital_scope`.
- Chaos tiers, major/regional identity, Soviet war state, weak center state, declaration flags, and terminal collapse state adjust the package before units are created.
- `soviet_collapse_apply_breakaway_mobilization` adds manpower, equipment, defensive ideas, and additional guard units for later reinforcement.

Static package coverage:

```text
Vanilla country tags and history files found for UKR BLR KAZ UZB KYR TAJ TMS LIT LAT EST GEO ARM AZR MOL.
Chaos Redux country tags and history files found for CFR MFR OGB ICD KRS FTH BBH BSC TNC ALA UDC SDZ RMC RCD ILU PRA TSC BLT NRF GAC DHC KHC FEV SZA UWD MRC IUL BAC ARD TRS NLC SEP DSC COU BEC RLD LID IRA.
```

The implemented high-chaos successor history files intentionally do not declare static OOBs because their military is assigned after runtime state transfer through `soviet_collapse_setup_breakaway_country`.

## Evolution Log Audit

Event 005 currently writes to the evolution log only through `soviet_collapse_record_high_chaos_successor_evolution`.

Audit evidence:

```text
common/scripted_effects/005_soviet_collapse_effects.txt
record_events_log_evolution_entry 1
events_log_evolution_event_id 39
events_log_evolution_type 39
events_log_evolution_stage 76
soviet_collapse_high_chaos_evolution_tier_4_recorded 1
soviet_collapse_high_chaos_evolution_tier_5_recorded 1

common/scripted_triggers/005_soviet_collapse_triggers.txt
soviet_collapse_high_chaos_evolution_tier_4_recorded 1
soviet_collapse_high_chaos_evolution_tier_5_recorded 1
```

Logging behavior:

- Baseline crisis setup and objective pressure effects modify crisis variables such as `soviet_collapse_moscow_authority`, `soviet_collapse_republic_confidence`, and `soviet_collapse_evolution_weirdness`; they do not record baseline stages as evolution entries.
- `soviet_collapse_record_high_chaos_successor_evolution` sets Event ID 5, high-chaos evolution type 5, the current chaos tier bucket, saves the successor actor, and records only if `can_soviet_collapse_record_high_chaos_evolution_this_tier = yes`.
- The tier gate records at most one non-tier-5 high-chaos successor evolution through `soviet_collapse_high_chaos_evolution_tier_4_recorded`.
- Chaos tier 5 can record one separate high-chaos successor evolution through `soviet_collapse_high_chaos_evolution_tier_5_recorded`.
- CFR, MFR, OGB, ICD, KRS, FTH, BBH, BSC, TNC, ALA, UDC, SDZ, RMC, RCD, ILU, PRA, TSC, BLT, NRF, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, BAC, ARD, TRS, NLC, SEP, DSC, COU, BEC, RLD, LID, and IRA each set their own stage before calling the shared writer, so whichever successor records first in that tier owns the visible evolution entry while later successors remain normal event notices.

Scripted localisation maps Event 005 evolution rows to the high-chaos successor type and tag-specific successor notices. General Soviet Collapse mutation localisation remains available for future mutation tracks, but the current Event 005 script does not write baseline crisis stages into the evolution log.

## Super-Event Route Coverage

Implemented route calls currently exist for:

- `soviet_collapse_show_black_banner_returns_super_event`
- `soviet_collapse_show_union_unmade_super_event`
- `soviet_collapse_show_world_as_one_factory_super_event`
- `soviet_collapse_show_map_larger_than_union_super_event`
- `soviet_collapse_show_steppe_beyond_history_super_event`
- `soviet_collapse_show_corridors_decide_super_event`
- `soviet_collapse_show_bread_state_super_event`
- `soviet_collapse_show_league_equal_republics_super_event`
- `soviet_collapse_show_steppe_federation_super_event`
- `soviet_collapse_show_baltic_restoration_pact_super_event`
- `soviet_collapse_show_caucasus_defense_compact_super_event`
- `soviet_collapse_show_eastern_buffer_coalition_super_event`
- `soviet_collapse_show_dead_are_citizens_super_event`
- `soviet_collapse_show_every_port_a_council_super_event`

Helpers without implemented route calls:

- None for the currently wired super-event helper surface.

## Custom Country Gap

Current registered special Event 005 custom country tags are:

- `CFR`
- `MFR`
- `OGB`
- `ICD`
- `KRS`
- `FTH`
- `BBH`
- `BSC`
- `TNC`
- `ALA`
- `UDC`
- `SDZ`
- `RMC`
- `RCD`
- `ILU`
- `PRA`
- `TSC`
- `BLT`
- `NRF`
- `GAC`
- `DHC`
- `KHC`
- `FEV`
- `SZA`
- `UWD`
- `MRC`
- `IUL`
- `BAC`
- `ARD`
- `TRS`
- `NLC`
- `SEP`
- `DSC`
- `COU`
- `BEC`
- `RLD`
- `LID`
- `IRA`

The custom icon surface references 35 tag prefixes:

```text
ALA ARD BAC BBH BEC BLT BSC COU DHC DSC FEV FTH GAC ICD ILU IRA IUL KHC KRS LID MRC NLC NRF PRA RCD RLD RMC SDZ SEP SZA TNC TRS TSC UDC UWD
```

The implemented custom country packages cover all 35 icon-prefix packages. There are no remaining custom icon-prefix reservations without registered country packages.

## Latest Validation Snapshot

Command evidence from the 2026-05-18 continuation audit:

```text
brace depth/min for Event 005 focus, effect, trigger, decision, idea, constant, and event files: depth=0 min=0
focuses 1500 duplicates 0 missing_refs 0 self_refs 0 nonreciprocal_mutual 0 missing_ai 0 missing_reward 0
missions 128 remove_refs 128 activate_refs 128 remove_missing 0 remove_extra 0 activate_missing 0 activate_extra 0
main_crisis_decision_ai dynamic_blocks 15 flat_blocks 0
ideas 124 weak_lt3 0 no_modifier 0 tiny_only 0
banned_phrase_hits 0
flags_checked 570 flags_missing 0 decode_errors 0 bottom_origin 570 top_origin 0 orientation_mismatches 0
git diff --check clean
unsupported operator/scope/localisation scan clean for the audited Event 005 files
```

The reported focus error for `baltic_soviet_collapse_a_port_without_a_master` and `baltic_soviet_collapse_sponsor_fleet_rights` is covered by the reciprocal mutual-exclusion audit above.

## Remaining Blockers

`tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` is listed in the active source order but is absent from `tmp/`. This prevents a strict final closure claim against every requested source file until the missing spec is restored or explicitly waived.

## Blocked Completion Report

The requested final completion report categories are not closed because the missing continuation spec cannot be audited. Current evidence exists for:

- implemented countries and packages: thirty-eight custom successors plus supported ordinary Soviet republics.
- flags: 570 Event 005 custom flag files audited; no current binary correction indicated.
- focus counts and branch maps: 1500 focus blocks across the Event 005 runtime focus files, with no duplicate IDs or invalid focus references.
- missions and decisions: 128 Soviet crisis missions, 128 activation entries, and 128 terminal removal entries; main Soviet, breakaway, and foreign patron crisis decisions use dynamic AI weights.
- evolutions and super-events: high-chaos successor evolution writer and super-event helpers remain wired for the current route surface.
- achievements and assets: achievement, focus, flag, leader, and super-event asset surfaces are documented in the Event 005 docs and asset manifests.
- tests and checks: brace depth, focus reference, mission wiring, idea-strength, localisation phrase, flag orientation, unsupported operator/scope, and whitespace checks passed in the latest audit.

Resume checklist:

- restore or explicitly waive `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md`.
- audit the restored spec line-by-line against current event log, mission balance, and focus cleanup artifacts.
- update this completion audit with any requirements that restored spec adds or changes.
- rerun the latest validation snapshot after any follow-up edits.
- only then mark the active Event 005 correction goal complete.
