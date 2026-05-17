# Event 005 Soviet Union Collapse Completion Audit

Current audit date: 2026-05-17

This audit maps the active clean-spec objective to current repository evidence. It is not a completion claim.

## Source Order

Required source order:

1. `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md`
2. `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md`
3. `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md`
4. `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md`
5. `AGENTS.md`
6. `chaos-redux-events`
7. `chaos-redux-event-assets`
8. `chaos-redux-super-events`

## Prompt To Artifact Checklist

| Requirement | Evidence | Status |
| --- | --- | --- |
| Event 005 remains Soviet Collapse with entry event format `chaosx.nr5.1` | `events/005_soviet_collapse.txt`; event docs in `docs/events/005_soviet_union_collapse.md` | Implemented; still needs full final audit |
| Dynamic crisis values and central tuning | `common/script_constants/005_soviet_collapse_constants.txt`, `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt` | Implemented for current systems; needs full spec-by-spec value audit |
| Soviet goal-style objectives with capacity limits | `common/decisions/005_soviet_collapse_decisions.txt` has 128 `soviet_collapse_soviet_mission_*` mission blocks | Implemented; needs final tooltip and localisation coverage audit |
| Foreign intervention categories and action-based aid | `soviet_collapse_foreign_patron_category` has 7 decision blocks; `soviet_collapse_breakaway_category` has 4 action blocks | Implemented for current layer; needs spreadsheet alignment |
| Runtime focus trees for republics and breakaways | Focus counts: Ukraine 153, Belarus 83, Kazakhstan 87, fallback breakaway 53, Baltic 36, Caucasus 33, Central Asia 34, Moldova 23 | Implemented for these trees |
| High-chaos successor focus trees | Focus counts: CFR 58, MFR 46, OGB 54, ICD 24, KRS 24, FTH 24, BBH 24, BSC 24, TNC 24, ALA 24, UDC 24, SDZ 24, RMC 24, RCD 24, ILU 24, PRA 24, TSC 24, BLT 24, NRF 24 | Implemented for these nineteen successors |
| Non-linear focus structure, route locks, branch zones, focus filters, AI behavior | Focus files use route-specific branches, `search_filters`, `ai_will_do`, and mutual exclusions; parser audit found no missing focus references, self-references, duplicate focus IDs, missing icons, missing localisation, missing `ai_will_do`, or missing/duplicated `completion_reward` blocks | Implemented for current focus trees |
| Full package for every implemented custom country | Registered special Event 005 custom tags currently found: `CFR`, `MFR`, `OGB`, `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, `NRF` | Implemented for nineteen; many planned serious splinters remain unimplemented |
| Starting divisions for appearing republics and serious splinters | `soviet_collapse_setup_breakaway_country` creates the shared `Emergency Republican Guard` template, grants base manpower/equipment, and spawns guard units for Event-created republics and the implemented CFR/MFR/OGB/ICD/KRS/FTH/BBH/BSC/TNC/ALA/UDC/SDZ/RMC/RCD/ILU/PRA/TSC/BLT/NRF successors; mobilisation decisions can add more units through the same template | Implemented for current appearing republics and implemented successors |
| Achievements | 47 Event 005 achievement definitions; 47 Event 005 NAME keys; GFX/DDS coverage previously checked clean | Implemented for current achievement surface; future-only splinter achievements depend on missing packages |
| Evolution logging | Event 005 has one `record_events_log_evolution_entry` writer, under `soviet_collapse_record_high_chaos_successor_evolution`; baseline crisis setup and objective pressure effects only change crisis variables and event flow | Implemented for current high-chaos successor logging |
| Super-events | Slots 14-27 have helpers, assets, localisation, audio references, constants, and route calls from implemented capstones | Implemented for current surfaces |
| Super-event slot 15, The Black Banner Returns | `FTH_extreme_path`, `BBH_extreme_path`, `fth_push_extreme_route`, and `bbh_push_extreme_route` call `soviet_collapse_complete_black_banner_endgame`, which fires the helper | Implemented through the Free Territory and Black Banner packages |
| Super-event slot 16, The Dead Are Citizens | `ICD_extreme_path`, `icd_push_extreme_route`, `RMC_extreme_path`, and `rmc_push_extreme_route` call dead-state or Red Martyrs endgame helpers, which fire the helper | Implemented through the Iron Commissariat and Red Martyrs packages |
| Super-event slot 17, The World as One Factory | `ILU_extreme_path` and `ilu_push_extreme_route` call `soviet_collapse_complete_iron_liturgy_endgame`, which fires the helper | Implemented through the Iron Liturgy package |
| Super-event slot 18, Every Port a Council | `KRS_extreme_path`, `krs_push_extreme_route`, `NRF_extreme_path`, and `nrf_push_extreme_route` call their port-council or northern-revenant endgame helpers, which fire the helper | Implemented through the Kronstadt and Northern Revenant packages |
| Super-event slot 24, Steppe Federation | `BSC_extreme_path`, `TNC_extreme_path`, `ALA_extreme_path`, and their push-extreme decisions call their Central Asian endgame helpers, which fire the helper | Implemented through the Basmachi, Turkestan, and Alash packages |
| Super-event slot 27, The Union Unmade | `UDC_extreme_path` and `udc_push_extreme_route` call `soviet_collapse_complete_union_defense_endgame`, which fires the helper | Implemented through the Union Defense package |
| Docs | Event doc and super-event research docs exist and are aligned with current route wiring | Implemented for current surfaces |
| Asset reuse and created assets | Current Event 005 docs record reused focus, achievement, and super-event assets; no new assets created in the latest route-wiring pass | Implemented for current surfaces |
| Spreadsheet updates | No local spreadsheet file was found by `rg --files`; README points to the external Google spreadsheet catalog | Blocked unless the sheet is provided or connector access is specified |
| Completion readiness | Dirty worktree check after last committed route pass was clean | Not complete |

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
focuses 1044
basic structural issues 0
missing icon definitions 0
missing localisation keys 0
completion_reward block count issues 0
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

- `soviet_collapse_release_initial_republics` releases and flags UKR, BLR, KAZ, UZB, KYR, TAJ, and TMS when their route conditions are met.
- `soviet_collapse_setup_southern_republic_if_valid` flags southern republics and sends them through the shared setup effect.
- `soviet_collapse_spawn_cfr_if_enabled`, `soviet_collapse_spawn_mfr_if_enabled`, and `soviet_collapse_spawn_ogb_if_enabled` transfer the successor states before calling their setup effects.
- `soviet_collapse_setup_breakaway_country` grants the base manpower, infantry equipment, support equipment, defensive ideas, one locked `Emergency Republican Guard` template, and three starting guard units at `capital_scope`.
- Chaos tier 3 and above adds another guard unit through `soviet_collapse_setup_breakaway_country`.
- `soviet_collapse_apply_breakaway_mobilization` adds manpower, equipment, defensive ideas, and additional guard units for later reinforcement.

Static package coverage:

```text
Vanilla country tags and history files found for UKR BLR KAZ UZB KYR TAJ TMS LIT LAT EST GEO ARM AZR MOL.
Chaos Redux country tags and history files found for CFR MFR OGB ICD KRS FTH BBH BSC TNC ALA.
```

The implemented high-chaos successor history files intentionally do not declare static OOBs because their military is assigned after runtime state transfer through `soviet_collapse_setup_breakaway_country`.

## Evolution Log Audit

Event 005 currently writes to the evolution log only through `soviet_collapse_record_high_chaos_successor_evolution`.

Audit evidence:

```text
common/scripted_effects/005_soviet_collapse_effects.txt
record_events_log_evolution_entry 1
events_log_evolution_event_id 4
events_log_evolution_type 4
events_log_evolution_stage 6
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
- CFR, MFR, OGB, ICD, KRS, FTH, BBH, BSC, TNC, and ALA each set their own stage before calling the shared writer, so whichever successor records first in that tier owns the visible evolution entry while later successors remain normal event notices.

Scripted localisation maps Event 005 evolution rows to the high-chaos successor type and tag-specific successor notices. General Soviet Collapse mutation localisation remains available for future mutation tracks, but the current Event 005 script does not write baseline crisis stages into the evolution log.

## Super-Event Route Coverage

Implemented route calls currently exist for:

- `soviet_collapse_show_black_banner_returns_super_event`
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
- `soviet_collapse_show_black_banner_returns_super_event`
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

The custom icon surface references 35 tag prefixes:

```text
ALA ARD BAC BBH BEC BLT BSC COU DHC DSC FEV FTH GAC ICD ILU IRA IUL KHC KRS LID MRC NLC NRF PRA RCD RLD RMC SDZ SEP SZA TNC TRS TSC UDC UWD
```

Those icon-prefix packages are not all registered country packages. `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, and `NRF` now convert sixteen previously blocked high-chaos routes into real packages, but the clean-spec objective still expects more serious splinter packages than the nineteen currently implemented tags.

## Remaining Blockers

1. Implement or explicitly defer the remaining serious splinter packages from Part 4 with full country packages, including tag, history, localisation, ideology names, leaders or councils, flags, ideas, decisions, AI, focus content, assets, and docs.
2. Update the event spreadsheet or record a concrete access blocker for the external catalog.
3. Run final parser-oriented checks after every remaining implementation pass.
