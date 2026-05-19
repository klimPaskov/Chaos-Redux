# Event 005 Soviet Union Collapse Completion Audit

Current audit date: 2026-05-19

This audit maps the active Soviet Collapse correction objective to current repository evidence after the influence/threat/focus rework, final-clean, spawn-balance, collapse-pacing, focus-layout, terminal-cleanup, and flag-orientation passes.

## Source Order

Required source order:

1. `tmp/005_soviet_union_collapse_influence_threat_focus_rework_spec.md`
2. `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md`
3. `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md`
4. `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md`
5. `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md`
6. `AGENTS.md`
7. `chaos-redux-events`
8. `chaos-redux-event-assets`
9. `chaos-redux-super-events`

The earlier `tmp/005_soviet_union_collapse_threat_mission_focus_rebalance_spec.md`, `tmp/005_soviet_union_collapse_comprehensive_correction_spec.md`, and later `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md` remain additional consulted context because they contain acceptance bullets that overlap the active source order. The historical `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` filename is not present, but it is not part of the active required source order; its named event-log, mission-balance, and focus-cleanup surfaces are covered by direct implementation evidence below.

The previously referenced `tmp/error.log` and `tmp/text.log` files are absent because the logged errors were fixed and the files were intentionally removed. They are not current completion blockers.

## Input File Audit

Requested source files as of 2026-05-19:

| Path | State | Lines | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `tmp/005_soviet_union_collapse_influence_threat_focus_rework_spec.md` | Present | 989 | 31351 | `b62d00c6a8947dd2ac2b97369b0871a611184ee27779c7342273d92f478bbdea` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md` | Present | 3418 | 162378 | `c0f474e97482a4eed3d4f9b8cbead930471f296d741e9805a0fea03b38e685e7` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md` | Present | 6327 | 191503 | `32284c8e2f424818be5dfbb81c394d9c1de7e666a93545586a1e2e1710276234` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md` | Present | 7535 | 554089 | `724a3bfb7c00aa28debf788649413da311224044fe4b0f4f8f726ee345275de7` |
| `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md` | Present | 3889 | 148956 | `60e2cac0717579afc60a3a6414558c00122d3fbae7d4e205af27671f7d6bc428` |
| `tmp/005_soviet_union_collapse_threat_mission_focus_rebalance_spec.md` | Additional consulted context | 512 | 16561 | `b91c2f0756de9210a5f1a70f5c00be39287068c6b212bea3655f4d3ab6448077` |
| `tmp/005_soviet_union_collapse_comprehensive_correction_spec.md` | Additional consulted context | 517 | 18082 | `409ed5f06819419237776a3a0dd26f60977f1b28ff2bddc041b34fd674ca8e17` |
| `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md` | Additional consulted context | 287 | 15899 | `9ac9d2553dffc54b6023c56f2dbde6efac310343b20873c77b1f50e6e5339750` |
| `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` | Historical missing continuation context; not active required input | - | - | - |
| `tmp/error.log` | Intentionally removed after fixed errors | - | - | - |
| `tmp/text.log` | Intentionally removed after fixed errors | - | - | - |

Recovery searches performed:

```text
find . -path './.git' -prune -o -type f \( -iname '*event_log*mission*balance*focus*cleanup*' -o -iname '*mission_balance_focus*' -o -iname '*005_soviet_union_collapse*cleanup*' \) -print
result: only tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md

git log --all --oneline -- tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md
result: no commits

git log --all --name-only --pretty=format: | rg '005_soviet_union_collapse.*(event_log|mission_balance|focus_cleanup|cleanup).*spec\.md'
result: no matching tracked history entry for the missing continuation spec

find . -path './.git' -prune -o -type f \( -iname 'error.log' -o -iname 'text.log' -o -iname '*event_log*mission*balance*focus*cleanup*' -o -iname '*mission_balance_focus*' \) -printf '%p %s bytes\n' | sort
result: no files
```

Present `tmp/` Event 005 spec files are:

```text
005_soviet_union_collapse_comprehensive_correction_spec.md
005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md
005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md
005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md
005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md
005_soviet_union_collapse_influence_threat_focus_rework_spec.md
005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md
```

## Concrete Success Criteria

The Event 005 correction pass is complete only if current repository evidence proves all of the following:

- weak Event 005 ideas and spirits are replaced by meaningful multi-effect packages, with small modifier values appearing only inside broader stacking packages.
- the opening release wave is randomized from structured western or eastern European, Caucasus, and Central Asian pools; Kazakhstan is separately gated; opening wave size and support scale with chaos, Soviet condition, and crisis state.
- every released republic or serious splinter, including final-collapse releases, receives dynamically scaled manpower, equipment, templates, and units.
- Union Crisis Threat and Moscow Authority use visible causes, dampening, failed objectives, rail control, command obedience, foreign penetration, League victories, chaos, and prior crisis state without trivial calm-world collapse.
- Union Unmade cannot fire during the ordinary first month and requires sustained failure signals; when it fires, unreleased ordinary Soviet republics are released and higher-chaos special actors are activated according to chaos tier.
- full-collapse cleanup cancels or hides obsolete Soviet Collapse intervention categories and active missions.
- runtime focus trees have clean layout, unique meaningful focuses, valid route content, valid icons/localisation/rewards/AI, and no one-way or repeated mutual-exclusion issues.
- Soviet Collapse flags are orientation-audited without unnecessary historical flag regeneration.
- player-facing localisation contains no removed design-language baseline wording and uses in-world crisis language instead.
- AI, docs, spreadsheet status, event log details, evolutions, super-events, assets, and the final completion report are aligned with the implemented state.
- every active source input is present and audited; historical missing continuation context is covered by direct implementation evidence and is not part of the active required source order.

## Prompt To Artifact Checklist

| Requirement | Evidence | Status |
| --- | --- | --- |
| Event 005 remains Soviet Collapse with entry event format `chaosx.nr5.1` | `events/005_soviet_collapse.txt`; event docs in `docs/events/005_soviet_union_collapse.md` | Implemented; parser audit passed |
| Dynamic crisis values and central tuning | `common/script_constants/005_soviet_collapse_constants.txt`, `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt` | Implemented; parser audit passed |
| Reference context surface | The audit context includes the offline Paradox wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding. Vanilla documentation context includes `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`. The verifier checks this as `reference_context_surface` and keeps web references out of the audit. | Implemented |
| Missing continuation direct coverage | The historical missing filename names event-log, mission-balance, and focus-cleanup surfaces. Direct implementation evidence for those surfaces is covered by `event_log_detail_surface`, `event_log_mapping_surface`, `soviet_objective_board_surface`, `terminal_mission_cleanup`, `focus_integrity`, `focus_layout_surface`, `focus_ai_surface`, and `focus_tree_map_surface`. The file is not part of the active required source order, so it is retained as recovery context rather than a final-closure blocker. | Covered by direct evidence |
| Comprehensive source-of-truth coverage | `tmp/005_soviet_union_collapse_comprehensive_correction_spec.md` is retained as additional consulted context and still maps its event log details, evolutions, mission duration, decision cost corrections, blocked localisation, design-language cleanup, threat and authority balance, stronger ideas, first-wave release logic, Kazakhstan handling, unit spawning, Union Unmade pacing/release rules, terminal cleanup, focus cleanup, flag orientation, and completion requirements to `comprehensive_source_acceptance_surface`, `event_log_detail_surface`, `evolution_logging_surface`, `soviet_objective_board_surface`, decision cost corrections, `banned_phrase_cleanup`, `crisis_balance_surface`, `crisis_cause_surface`, `idea_package_surface`, `first_wave_release_surface`, `force_scaling_surface`, `union_unmade_pacing`, `terminal_mission_cleanup`, `focus_layout_surface`, `flag_orientation_surface`, and `docs_completion_surface`. | Implemented for the available comprehensive source spec |
| Available source acceptance criteria coverage | The source-of-truth spawn-balance cleanup spec has 20 acceptance bullets. The completion audit maps them to the concrete verifier surfaces `idea_package_surface`, `first_wave_release_surface`, `force_scaling_surface`, `crisis_balance_surface`, `union_unmade_pacing`, `terminal_ordinary_republic_release_surface`, `terminal_high_chaos_successor_surface`, `terminal_mission_cleanup`, `focus_layout_surface`, `focus_tree_map_surface`, `flag_orientation_surface`, `banned_phrase_cleanup`, `event_log_mapping_surface`, `achievement_surface`, and `docs_completion_surface`. The verifier checks this map as `available_source_acceptance_surface`. | Implemented for the available source spec |
| Stronger Soviet Collapse ideas and spirits | `common/ideas/005_soviet_collapse_ideas.txt` and the crisis effects use multi-modifier packages for Union Crisis, recoverable republican startup disorder, stabilized emergency administration, defensive coordination, depot seizures, legal claims, foreign volunteers, old networks, factory states, and high-chaos successors; the current idea parser audit found no Event 005 idea with fewer than three modifier entries, no idea without modifiers, no tiny-only package, no missing idea picture sprite, no missing idea DDS, and no missing idea name/description localisation. `breakaway_recovery_surface` proves ordinary breakaway setup adds exactly one starting idea, `soviet_collapse_republican_startup_disorder`, and that four breakaway decisions plus focus helpers advance a recovery chain that swaps to mitigated disorder and then removes the negative idea for stabilized emergency administration. The remaining 2-3% components appear only inside broader 3-5 modifier spirits. | Implemented for current surface |
| Random first wave from structured pools | `soviet_collapse_release_initial_republics` clears and fills `global.soviet_collapse_first_wave_republics` through western, Caucasus, and Central Asian random pool helpers, then releases the selected scopes. Each pool can now select either nonexistent supported tags whose cores are owned and controlled by SOV or existing supported Soviet subjects, which are freed with `set_autonomy` before setup. | Implemented |
| Kazakhstan first-wave restraint | `can_soviet_collapse_open_kazakhstan_first_wave` requires southern breakaway pressure, weak obedience, war or low Soviet condition, or high chaos; Kazakhstan is outside the normal Central Asian first-wave pool | Implemented |
| Dynamic starting force packages | `soviet_collapse_apply_breakaway_setup_package` creates manpower, equipment, guard units, field brigades, and templates from central script constants. It is reached by ordinary first-wave releases, terminal ordinary republic releases, southern cascade republics, Kazakhstan, and all 38 high-chaos successor setup helpers. The package scales by republic size, chaos tier, Soviet war state, weak center conditions, declaration posture, terminal collapse, high depot vulnerability, and high foreign penetration. | Implemented; force coverage verifier passed |
| Union Crisis Threat and Moscow Authority pacing | Opening values start from central constants, apply visible condition modifiers, then use `soviet_collapse_recalculate_total_threat` with clamping and `constant:soviet_collapse_baseline.total_threat_multiplier`; scenario audit gives calm baseline Authority 62 / Threat 7.25, tier 1 opening pressure Authority 62 / Threat 9.25, and tier 5 with capital lost, war, low stability, and low war support Authority 38 / Threat 50.25. The 30-day crisis pulse applies a monthly guard before progressive releases: calm successful months without failed objectives, Soviet war, or above-baseline foreign/League pressure are capped to +1 threat, and moderate successful months are capped to +4. The mission-success pressure audit resolves all 11 successful objective helpers against the threat formula, found all 11 net non-increasing, found zero destabilizing component changes, and measured the highest successful net threat delta at -1.50. Union Unmade still uses its ordinary first-month gates in normal play, while a 100 threat ceiling immediately fires terminal collapse and releases every ordinary republic plus every eligible terminal special successor. | Implemented for current tuning |
| Soviet goal-style objectives with capacity limits | `common/decisions/005_soviet_collapse_decisions.txt` has 128 unique `soviet_collapse_soviet_mission_*` mission blocks. The direct mission-balance audit found 128 activation references, 128 terminal removal references, zero missing activation/removal refs, and zero mission block or localisation problems. | Implemented; parser audit passed |
| Longer varied Soviet mission deadlines | The 128 Soviet missions use all 11 named `@soviet_collapse_mission_days_*` constants ranging from 95 to 365 days; no mission uses a single shared `@soviet_collapse_opening_mission_days` timeout | Implemented; timeout audit passed |
| Decision cost corrections | `Send Loyalist Officers` spends army XP and command power only; `Restore Party Control` spends 2,000 infantry equipment, 200 support equipment, and 10,000 manpower through central `soviet_collapse_decision_cost` constants and matching trigger/localisation keys | Implemented |
| Blocked cost localisation | Event 005 blocked cost lines in `localisation/english/005_soviet_collapse_l_english.yml` use bare icon-and-value groups only, with no prose labels or connector words between costs. | Implemented; localisation audit passed |
| Foreign intervention categories and action-based aid | `soviet_collapse_foreign_patron_category` has 7 targeted decision blocks with `days_re_enable`; `soviet_collapse_breakaway_category` has 4 action blocks; the decision audit found no active timed foreign intervention missions outside the 128 Soviet crisis missions | Implemented for current layer; catalog row updated |
| Foreign influence sponsorship balance | `soviet_collapse_apply_foreign_influence_delta` now calls `soviet_collapse_update_sponsor_balance_pressure` on the target republic after sponsor totals change. The helper counts active sponsors, tracks the top sponsor, second sponsor, and sponsor gap, grants one-time independence resilience for two- and three-sponsor balance, and applies one-time patronage/resilience pressure when one sponsor opens a large lead. `foreign_influence_surface` verifies the constants, helper variables, flags, and docs markers. | Implemented for current influence layer |
| Crisis decision AI behavior | The four Soviet responses, four breakaway actions, seven foreign patron actions, six factory/Volga successor actions, and 105 custom-splinter action decisions use dynamic `ai_will_do` modifiers tied to crisis variables, war state, League coordination, faction state, stability, chaos tier, old-movement weirdness, and Soviet authority. Current decision parser evidence found 126 dynamic non-mission decision AI blocks, zero flat non-mission decision AI blocks, and 128 timed mission blocks without `ai_will_do` by design. | Implemented for the current decision layer |
| Runtime focus trees for republics and breakaways | Focus counts after duplicate pruning: Ukraine 81, Belarus 38, Kazakhstan 57, fallback breakaway 27, Baltic 21, Caucasus 20, Central Asia 14, Moldova 17 | Implemented for these trees |
| High-chaos successor focus trees | Focus counts after duplicate pruning: CFR 45, MFR 37, OGB 32, KRS 20, and ICD/FTH/BBH/BSC/TNC/ALA/UDC/SDZ/RMC/RCD/ILU/PRA/TSC/BLT/NRF/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/TRS/NLC/SEP/DSC/COU/BEC/RLD/LID/IRA at 21 each | Implemented for these thirty-eight successors |
| Non-linear focus structure, route locks, branch zones, focus filters, AI behavior | Focus files use route-specific branches, `search_filters`, `ai_will_do`, and mutual exclusions; parser audit over 46 focus trees and 1,123 retained focus IDs found no duplicate IDs, missing focus references, self-references, one-way mutual exclusions, unknown mutual targets, exact coordinate collisions, missing icons, missing `ai_will_do`, or missing/duplicated `completion_reward` blocks. Focus AI audit found 229 dynamic AI blocks overall and 114 dynamic mutually exclusive route-choice blocks; no mutually exclusive route-choice focus currently uses flat AI. The rebuilt graph layout has zero duplicate coordinates, zero hard-prerequisite edge crossings, zero visually detached long prerequisite jumps, no isolated focuses, exactly one terminal leaf per tree, no shallow side-focus leaves, all 46 continuous-focus boxes in right-side panels, maximum prerequisite horizontal jump 44, maximum vertical span 14, minimum mutual-exclusion distance 6, maximum row width 20, maximum column stack 11, and no exact duplicate focus reward bodies. The republic focus file only allows documented OR prerequisite pools on explicit convergence capstones and opening fork nodes that need visible links for hidden branch gates; ordinary convergence nodes use separate AND prerequisite links. | Implemented for current focus trees |
| Focus tree map documentation | `docs/events/005_soviet_union_collapse.md` contains the post-cleanup focus-tree map under `Republic Focus Trees`, listing all 46 implemented trees from Ukraine through `IRA_soviet_collapse_focus_tree`, their branch zones, route identities, and right-side continuous-focus placement. The verifier checks this as `focus_tree_map_surface`. | Implemented |
| Full package for every implemented custom country | Registered special Event 005 custom tags currently found: `CFR`, `MFR`, `OGB`, `ICD`, `KRS`, `FTH`, `BBH`, `BSC`, `TNC`, `ALA`, `UDC`, `SDZ`, `RMC`, `RCD`, `ILU`, `PRA`, `TSC`, `BLT`, `NRF`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `TRS`, `NLC`, `SEP`, `DSC`, `COU`, `BEC`, `RLD`, `LID`, and `IRA` | Implemented for thirty-eight |
| Starting divisions for appearing republics and serious splinters | `soviet_collapse_setup_breakaway_country` is an idempotent guarded wrapper; the internal setup package creates the shared `Emergency Republican Guard` template, grants manpower/equipment, and scales guard and field unit packages by major/regional tag, chaos tier, Soviet war state, weak center state, one-use declaration flags, and terminal collapse state without double-counting already-flagged breakaways | Implemented for current appearing republics and implemented successors |
| Union Unmade first-month lock | `soviet_collapse_initialize_crisis_values` sets `soviet_collapse_union_unmade_first_month_lock` for 31 days; `soviet_collapse_maybe_show_union_unmade_super_event` refuses to fire while the lock exists | Implemented |
| Terminal ordinary republic release | `soviet_collapse_show_union_unmade_super_event` calls `SOV = { soviet_collapse_apply_terminal_collapse = yes }`; terminal collapse releases unreleased supported ordinary republics under Soviet ownership/control and frees existing supported Soviet-subject republics before adding high-chaos successors | Implemented |
| Terminal high-chaos successor activation | `soviet_collapse_spawn_terminal_high_chaos_successors` retries high-chaos successor spawning and, at chaos tier 5, prepares terminal gate flags before activating all eligible special actors whose packages and territory gates pass. The current gate audit found 38 special successor spawn gates with required preparation flags and zero required flags missing from `soviet_collapse_prepare_highest_chaos_terminal_successors`. | Implemented for current successor set |
| Terminal mission and category cleanup | `is_soviet_collapse_active` excludes `soviet_collapse_terminal_collapse`; terminal cleanup clears active crisis flags, one-use declaration flags, stale loyal-unit and district war-room helper flags, removes all 128 active Soviet crisis missions from the terminal cleanup helper, blocks further objective activation, and hides Soviet, breakaway, foreign patron, regional faction, and special-actor categories after terminal collapse. Category audit found 42 Event 005 category definitions with visible gates, 41 used decision category blocks, and zero Event 005 category definitions without `is_soviet_collapse_active = yes`; regular decision audit found all non-mission decisions gated by `is_soviet_collapse_active = yes`. | Implemented |
| Mission audit table | `docs/events/005_soviet_union_collapse_mission_audit.md` contains the required `Mission / Owner / Purpose / Requirement / Success effect / Failure effect / Duplicate risk` table with all 128 Soviet crisis missions. The table links duplicate-risk claims to `mission_quality_surface`, objective-board wiring to `soviet_objective_board_surface`, concrete scripted requirements to `mission_requirement_surface`, localisation coverage to `localisation_surface`, terminal cleanup to `terminal_mission_cleanup`, named division-state tooltip coverage to the raw division-state availability check, and long-trigger readability to the long-inline availability check. | Implemented |
| Achievements | 47 Event 005 achievement definitions; 47 Event 005 NAME keys; GFX/DDS coverage previously checked clean; route flag audit checked 89 achievement flags | Implemented; route flag audit passed |
| Event log details | `GetEventsLogEventDetailDescription` maps Event ID 5 to `chaosx.events_log.window.event_details.soviet_collapse`; that localisation composes live in-world status lines through `GetEventsLogSovietCollapseDetail*` scripted localisation for crisis state, first-wave state, League status, Moscow Authority, Union Crisis Threat, foreign intervention, and old-movement or high-chaos splinter pressure. The direct event-log detail audit checked 57 conditions: Event ID 5 mapping, all seven scripted detail functions referenced by the main text, every function defined with outputs and a fallback, and all 25 output localisation keys present. | Implemented |
| Evolution logging | Event 005 has one `record_events_log_evolution_entry` writer, under `soviet_collapse_record_high_chaos_successor_evolution`; baseline crisis setup and objective pressure effects only change crisis variables and event flow | Implemented for current high-chaos successor logging |
| Super-events | Slots 14-27 have helpers, assets, localisation, audio references, constants, and route calls from implemented capstones | Implemented for current surfaces |
| Super-event slot 14, The Union Unmade | Broad breakaway pressure calls `soviet_collapse_maybe_show_union_unmade_super_event`; `UDC_extreme_path` and `udc_push_extreme_route` call `soviet_collapse_complete_union_defense_endgame`, which fires `soviet_collapse_show_union_unmade_super_event`. The direct package audit found the slot 14 script constant, show helper, visible flag emission, audio id assignment, image selector, title/description/button/quote selectors, sprite definition, DDS/source/preview assets, and manifest row all aligned. | Implemented through breakaway-count pressure and the Union Defense package |
| Super-event slot 15, The Black Banner Returns | `FTH_extreme_path`, `BBH_extreme_path`, `fth_push_extreme_route`, and `bbh_push_extreme_route` call `soviet_collapse_complete_black_banner_endgame`, which fires the helper | Implemented through the Free Territory and Black Banner packages |
| Super-event slot 16, The Dead Are Citizens | `ICD_extreme_path`, `icd_push_extreme_route`, `RMC_extreme_path`, `rmc_push_extreme_route`, `SEP_extreme_path`, `sep_push_extreme_route`, `DSC_extreme_path`, `dsc_push_extreme_route`, `COU_extreme_path`, `BEC_extreme_path`, `RLD_extreme_path`, `LID_extreme_path`, `IRA_extreme_path`, and their push-extreme decisions call dead-state or Red Martyrs endgame helpers, which fire the helper | Implemented through the Iron Commissariat, Red Martyrs, Sepulchre Soviet, Dead Soldiers, Unburied Commissariat, Black Earth, Red Lazarus, Last International, and Iron Resurrection packages |
| Super-event slot 17, The World as One Factory | `ILU_extreme_path` and `ilu_push_extreme_route` call `soviet_collapse_complete_iron_liturgy_endgame`, which fires the helper | Implemented through the Iron Liturgy package |
| Super-event slot 18, Every Port a Council | `KRS_extreme_path`, `krs_push_extreme_route`, `NRF_extreme_path`, `nrf_push_extreme_route`, `ARD_extreme_path`, and `ard_push_extreme_route` call their port-council, northern-revenant, or Arctic directorate endgame helpers, which fire the helper | Implemented through the Kronstadt, Northern Revenant, and Arctic Naval Directorate packages |
| Super-event slot 24, Steppe Federation | `BSC_extreme_path`, `TNC_extreme_path`, `ALA_extreme_path`, and their push-extreme decisions call their Central Asian endgame helpers, which fire the helper | Implemented through the Basmachi, Turkestan, and Alash packages |
| Super-event slot 27, The Eastern Buffer Coalition | `moldova_soviet_collapse_alliance_not_union` calls `soviet_collapse_show_eastern_buffer_coalition_super_event` | Implemented through the Moldova regional tree |
| Docs | Event doc and super-event research docs exist and are aligned with current route wiring | Implemented for current surfaces |
| Asset reuse and created assets | Current Event 005 docs record reused focus, achievement, super-event assets, and the 570-file custom flag orientation audit; no historical flags were regenerated in the latest pass | Implemented for current surfaces |
| Flag orientation audit | 38 Event 005 custom tags across base, communism, democratic, fascism, and neutrality variants were checked in normal, medium, and small flag folders; all 570 files exist, decode cleanly, use vanilla-matching bottom-origin TGA headers, and average-downsample comparison finds no small/medium variant closer to a vertically flipped large source | Audit passed; no binary correction required by current evidence |
| Localisation design-language cleanup | Search across `common/`, `events/`, `localisation/`, `interface/`, and `docs/` found no player-facing instance of the specified design-language sentence from the cleanup prompt | Implemented |
| Spreadsheet updates | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, row 6 / Event ID 5, summarizes the current dynamic crisis, no-baseline-evolution rule, tier 4 and tier 5 high-chaos successor mutation logs, no dedicated world-end scenario, and verified final status for the active source order | Implemented; workbook package and XML package validation passed |
| Completion readiness | Current audit records the active influence/threat/focus rework evidence, additional comprehensive and spawn-balance cleanup evidence, thirty-eight implemented custom successor packages, terminal cleanup, focus-layout cleanup, flag orientation audit, and parser validations | Implemented |

## Current Focus Counts

Command evidence:

```text
soviet_collapse_ukraine_focus_tree 81
soviet_collapse_breakaway_focus_tree 27
soviet_collapse_baltic_focus_tree 21
soviet_collapse_caucasus_focus_tree 20
soviet_collapse_central_asia_focus_tree 14
soviet_collapse_moldova_focus_tree 17
soviet_collapse_belarus_focus_tree 38
soviet_collapse_kazakhstan_focus_tree 55
CFR_soviet_collapse_focus_tree 45
OGB_soviet_collapse_focus_tree 32
MFR_soviet_collapse_focus_tree 37
FTH_soviet_collapse_focus_tree 21
BSC_soviet_collapse_focus_tree 21
TNC_soviet_collapse_focus_tree 21
ALA_soviet_collapse_focus_tree 21
BBH_soviet_collapse_focus_tree 21
ICD_soviet_collapse_focus_tree 21
KRS_soviet_collapse_focus_tree 20
UDC_soviet_collapse_focus_tree 21
SDZ_soviet_collapse_focus_tree 21
RMC_soviet_collapse_focus_tree 21
RCD_soviet_collapse_focus_tree 21
ILU_soviet_collapse_focus_tree 21
PRA_soviet_collapse_focus_tree 21
TSC_soviet_collapse_focus_tree 21
BLT_soviet_collapse_focus_tree 21
NRF_soviet_collapse_focus_tree 21
GAC_soviet_collapse_focus_tree 21
DHC_soviet_collapse_focus_tree 21
KHC_soviet_collapse_focus_tree 21
FEV_soviet_collapse_focus_tree 21
SZA_soviet_collapse_focus_tree 21
UWD_soviet_collapse_focus_tree 21
MRC_soviet_collapse_focus_tree 21
IUL_soviet_collapse_focus_tree 21
BAC_soviet_collapse_focus_tree 21
ARD_soviet_collapse_focus_tree 21
TRS_soviet_collapse_focus_tree 21
NLC_soviet_collapse_focus_tree 21
SEP_soviet_collapse_focus_tree 21
DSC_soviet_collapse_focus_tree 21
COU_soviet_collapse_focus_tree 21
BEC_soviet_collapse_focus_tree 21
RLD_soviet_collapse_focus_tree 21
LID_soviet_collapse_focus_tree 21
IRA_soviet_collapse_focus_tree 21
```

## Focus Tree Integrity Audit

Parser-oriented audit coverage for `common/national_focus/005_soviet_collapse_republics.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, and `common/national_focus/005_soviet_collapse_custom_splinters.txt`:

```text
FOCUS PARSER AUDIT PASSED
focuses 1121
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
xlsx_status Implemented - Verified
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

- `soviet_collapse_release_initial_republics` selects from western, Caucasus, and Central Asian pools, releases nonexistent selected scopes, frees selected existing Soviet subjects with `set_autonomy`, and keeps Kazakhstan behind its separate southern and high-chaos gate.
- `soviet_collapse_setup_southern_republic_if_valid` flags southern republics and sends them through the shared setup effect.
- `soviet_collapse_spawn_cfr_if_enabled`, `soviet_collapse_spawn_mfr_if_enabled`, and `soviet_collapse_spawn_ogb_if_enabled` transfer the successor states before calling their setup effects.
- `soviet_collapse_setup_breakaway_country` is guarded by `NOT = { has_country_flag = soviet_collapse_breakaway }`, so repeated callers cannot double-count the breakaway array/counters or duplicate its starting manpower, equipment, templates, and units.
- `soviet_collapse_apply_breakaway_setup_package` grants dynamic manpower, infantry equipment, support equipment, artillery, defensive ideas, one locked `Emergency Republican Guard` template, guard units, and field units at `capital_scope`.
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

Custom-splinter idea picture aliases cover 111 per-spirit `picture = ...` tokens across the 38 custom and factory successor tag DDS packages. These aliases live in `interface/005_soviet_collapse_icons.gfx` and point to the existing `gfx/interface/ideas/soviet_collapse/005_<tag>_custom_splinter_idea.dds` files.

## Latest Validation Snapshot

Command evidence from the 2026-05-19 continuation audit:

```text
brace depth/min for Event 005 focus, effect, trigger, decision, idea, constant, and event files: depth=0 min=0
focuses 1121 duplicates 0 missing_refs 0 self_refs 0 nonreciprocal_mutual 0 missing_ai 0 missing_reward 0 dynamic_ai 227 dynamic_mutual_ai 114 flat_mutual_ai 0
national_focus_repeated_mutual_blocks 0
missions 128 remove_refs 128 activate_refs 128 remove_missing 0 remove_extra 0 activate_missing 0 activate_extra 0 decision_blocks 254 timed_decisions 128 timed_outside_soviet_missions 0 categories_without_active_visible 0
non_mission_decision_ai dynamic_blocks 126 flat_blocks 0 timed_mission_missing_ai 128
idea_strength_checks ideas 146 constants 159 no_modifier 0 weak_lt3 0 tiny_only 0 min_modifiers 3 max_modifiers 7 avg_modifiers 3.24 total_modifier_entries 473 tiny_components 25 unresolved_constants 0 missing_picture 0 missing_sprite 0 missing_dds 0 missing_loc 0 missing_desc 0
modifier_count_distribution 3:118 4:23 5:4 7:1
banned_phrase_hits 0
source_context_files files 4 missing 0
reference_context_surface files 16/16 markers 19/19
source_order_surface items 9 ordered True numbered True
input_audit_surface rows 14 mismatches 0
recovery_search_surface continuation_matches 0 removed_log_hits 0
final_completion_report_surface markers 7 missing 0
strict_verifier_documentation_surface markers 2/2 forbidden 0
missing_continuation_direct_coverage_surface markers 13/13 missing 0
resume_validation_commands_surface markers 6/6 missing 0
success_criteria_surface markers 13 missing 0
available_source_acceptance_surface source_markers 20/20 audit_markers 17/17
comprehensive_source_acceptance_surface source_markers 20/20 audit_markers 17/17
prompt_artifact_checklist_surface rows 30 implemented_rows 44 blocked_rows 0
verifier_command_documentation_surface markers 6 missing 0
focus_tree_map_surface event_markers 9/9 audit_markers 3/3
validation_snapshot_freshness_surface markers 3/3 stale 0
flag_orientation_headers flags_checked 570 flags_missing 0 decode_errors 0 top_origin 570 bottom_origin 0
flag_orientation_surface comparisons 380 expected 380 orientation_mismatches 0
terminal_high_chaos_successor_surface prepare_flags 26 spawn_calls 38/38 ready_trigger_refs 38
union_unmade_super_event_checks 18 failed 0
event_log_detail_checks 57 failed 0 detail_functions 7 detail_output_localisation_keys 25
mission_balance_checks missions 128 unique 128 timeout_constants_defined 11 timeout_constants_used 11 timeout_min 95 timeout_max 365 remove_refs 128 activate_refs 128 problems 0 remove_missing 0 remove_extra 0 activate_missing 0 activate_extra 0
focus_layout_checks trees 46 focuses 1123 duplicate_ids 0 coord_collisions 0 missing_coords 0 missing_search_filters 0 repeated_mutual_blocks 0 continuous_positions 46 continuous_side_bad 0 edge_crossings 0 visual_detached_edges 0 max_edge_dx 44 terminal_leaf_trees 46/46 shallow_dead_end_focuses 0 min_x_span 18 min_y_span 5 max_col 11 max_row 20
crisis_scenarios calm_baseline authority 62 threat 7.25; modest_tier1 authority 62 threat 9.25; tier5_capital_lost_war_low_stability_low_support authority 38 threat 50.25
crisis_monthly_guard_surface guard_constants 1.0/4.0 success_regs 11 failure_regs 11 guard_blocks 1 event129 True
mission_success_pressure_surface success_helpers 11 non_increasing 11 bad_component_changes 0 max_net_delta -1.50 unresolved 0
core_crisis_meter_numeric_literals 0
git diff --check clean
unsupported operator/scope/localisation scan clean for the audited Event 005 files
```

Reusable verifier added:

```text
.tools/verify_event005_completion_gate.py
```

Verifier exit meanings:

- `0`: all implementation gates passed and every required input is present.
- `2`: implementation gates passed but one or more required active source inputs are missing.
- `1`: one or more implementation gates failed.

Strict verifier result:

```text
python3 .tools/verify_event005_completion_gate.py
result: exit 0; all implementation gates and active required-input gates passed
```

Current prompt-to-artifact spot audit:

```text
input_files rebalance_spec present bytes 16561 lines 512 sha256 b91c2f0756de9210a5f1a70f5c00be39287068c6b212bea3655f4d3ab6448077
input_files influence_rework_spec present bytes 31351 lines 989 sha256 b62d00c6a8947dd2ac2b97369b0871a611184ee27779c7342273d92f478bbdea
input_files comprehensive_spec present bytes 18082 lines 517 sha256 409ed5f06819419237776a3a0dd26f60977f1b28ff2bddc041b34fd674ca8e17
input_files spawn_spec present bytes 15899 lines 287 sha256 9ac9d2553dffc54b6023c56f2dbde6efac310343b20873c77b1f50e6e5339750
input_files historical_continuation_spec missing_not_active_required
input_files clean1 present bytes 162378 lines 3418 sha256 c0f474e97482a4eed3d4f9b8cbead930471f296d741e9805a0fea03b38e685e7
input_files clean2 present bytes 191503 lines 6327 sha256 32284c8e2f424818be5dfbb81c394d9c1de7e666a93545586a1e2e1710276234
input_files clean3 present bytes 554089 lines 7535 sha256 724a3bfb7c00aa28debf788649413da311224044fe4b0f4f8f726ee345275de7
input_files clean4 present bytes 148956 lines 3889 sha256 60e2cac0717579afc60a3a6414558c00122d3fbae7d4e205af27671f7d6bc428
input_files error_log intentionally_removed_not_blocker
input_files text_log intentionally_removed_not_blocker
ideas_audit ideas 146 no_mod 0 weak_lt3 0 tiny_only 0 min_mods 3 max_mods 7 missing_sprite 0 missing_dds 0 missing_loc_or_desc 0
idea_package_surface ideas 146 modifier_entries 473 tiny_components 25 unresolved_constants 0 missing_picture 0 missing_sprite 0 missing_dds 0 missing_name 0 missing_desc 0
breakaway_recovery_surface starting_ideas 1 setup_only_disorder True recovery_swap_remove True breakaway_decisions 4 decision_progress_refs 14 focus_progress_refs 6 constants partial 2.0 complete 4.0 decision 1.0 focus 1.0 docs True
available_source_acceptance_surface source_markers 20/20 audit_markers 17/17
comprehensive_source_acceptance_surface source_markers 20/20 audit_markers 17/17
first_wave_audit western_random 1 caucasus_random 1 central_random 1 extra_random 1 normal_pool_has_kaz False kaz_gate_southern True kaz_gate_tier4 True extra_calls 3
first_wave_release_surface pool_helpers 4 western_tags 6 caucasus_tags 3 central_tags 4 map_support_gates True extra_scaling True selected_release True kazakhstan_release True southern_cascade True
focus_reward_variety_surface focuses 1123 duplicate_reward_groups 0 duplicate_reward_focuses 0 reward_categories 9 add_idea_rewards 145
focus_ai_surface focuses 1123 ai_blocks 1123 dynamic_ai 229 mutual_route_choices 114 dynamic_mutual_ai 114 flat_mutual_ai 0
force_package_audit manpower True equipment 3 templates 2 create_unit 2 major_scaling True regional_scaling True chaos_scaling 4 war_scaling True weak_center_scaling True terminal_scaling True
force_scaling_surface base True major True regional True chaos_bands True conditions True declarations True unit_delivery True constants True
crisis_monthly_guard_surface guard_constants=1.0/4.0 success_regs=11 failure_regs=11 guard_blocks=1 event129=True
crisis_cause_surface recalculate_surface True opening_surface True first_wave_pressure_surface True pressure_families 10/10 monthly_guard True multiplier 0.25
mission_success_pressure_surface success_helpers=11 non_increasing=11 bad_component_changes=0 max_net_delta=-1.50 unresolved=0
union_unmade_audit first_month_lock_in_init True lock_blocks_fire True min_breakaways_gate True high_threat_gate True critical_authority_gate True league_or_kaz_or_chaos True
terminal_release_audit ordinary_tags_present 14 ordinary_expected 14 release_calls 1 free_subject_calls 1 setup_calls 2
cleanup_audit cleanup_helpers 1 missions 128 cleanup_remove_refs 128 activate_refs 128 category_defs 42 visible_category_defs 42 categories_gated True decision_categories 42 regular_decisions_gated True cleanup_flags True
soviet_objective_board_surface missions 128 count_helpers 1 activation_helpers 1 count_refs 128 activate_refs 128 manual_only 128 visible_gated 128 payloads 128 queue_restarts 128 done_flag_refs 128 timeout_bands 11 active_cap 10 queue_cap True
mission_quality_surface missions 128 unique_available 128/128 weak_available 0 identical_outcomes 0 raw_division_state_available 0 long_inline_available 0 map_or_state_available 127
mission_requirement_surface scripted_requirement_refs 128/128 thin_requirements 0 meter_only 0 passive_only 0 forbidden_trivial_literals 0 division_tooltips 4 missing_division_tooltip_loc 0 min_requirement_families 2
mission_audit_documentation_surface rows 128 mission_ids 128/128 header True validation_markers 4/4
focus_layout_surface focus_trees 46 continuous_positions 46 layout_bad 0 duplicate_coord_trees 0 continuous_side_bad 0 crossing_free 46 edge_crossings 0 visual_detached_edges 0 max_edge_dx 44 isolated_focuses 0 terminal_leaf_trees 46/46 shallow_dead_end_focuses 0 disconnected_trees 0 deep_trees 0 tight_mutual_trees 0 min_x_span 18 min_y_span 5 max_y_span 14 min_mutual_distance 6 max_col 11 max_row 20
focus_tree_map_surface event_markers 9/9 audit_markers 3/3
focus_surface_audit focuses 1123 continuous_positions 46
localisation_phrase_audit banned_phrase_hits 0
event_log_mapping_surface event_name True debug_name True settings_name True default_actor True detail_mapping True entry_event True detail_functions 7 detail_output_keys 25
blockers missing_inputs []
spreadsheet_row6_status L6 "Implemented - Verified" R6 "Complete"
spreadsheet_stale_status_scan stale_missing_logs_status_hits 0 stale_final_audit_passed_hits 0 formula_count 0 error_cells 0
libreoffice_catalog_csv_convert status 0
```

The reported focus error for `baltic_soviet_collapse_a_port_without_a_master` and `baltic_soviet_collapse_sponsor_fleet_rights` was caused by repeated `mutually_exclusive` keys on the sponsor focus. Event 005 focus trees now use one mutual-exclusion block per focus, and the all-focus repeated-key scan returns zero hits.

Current targeted validation rerun:

```text
focus_paths
common/national_focus/005_soviet_collapse_republics.txt 273
common/national_focus/005_soviet_collapse_factory_successors.txt 114
common/national_focus/005_soviet_collapse_custom_splinters.txt 734
focuses 1121
duplicates 0
missing_prereq 0
self_prereq 0
repeated_mutual_blocks 0
missing_mutual 0
self_mutual 0
nonreciprocal_mutual 0
pair_check baltic_soviet_collapse_a_port_without_a_master excludes baltic_soviet_collapse_sponsor_fleet_rights: True
pair_check baltic_soviet_collapse_sponsor_fleet_rights excludes baltic_soviet_collapse_a_port_without_a_master: True
unsupported_operator_scan files_scanned 561 unsupported_operator_hits 0
player_facing_banned_phrase_scan hits 0
```

Current Event 005 localisation validation:

```text
files 8
missing_bom 0
decode_errors 0
colon_zero_keys 0
leading_key_space 0
banned_phrase_hits 0
utf8_bom_prefixes
localisation/english/005_soviet_collapse_blr_focus_l_english.yml efbbbf
localisation/english/005_soviet_collapse_custom_countries_l_english.yml efbbbf
localisation/english/005_soviet_collapse_focus_decisions_l_english.yml efbbbf
localisation/english/005_soviet_collapse_focus_expansion_l_english.yml efbbbf
localisation/english/005_soviet_collapse_kaz_focus_l_english.yml efbbbf
localisation/english/005_soviet_collapse_l_english.yml efbbbf
localisation/english/005_soviet_collapse_regional_focus_l_english.yml efbbbf
localisation/english/005_soviet_collapse_ukraine_focus_l_english.yml efbbbf
```

Current Event 005 idea-strength validation:

```text
ideas 146
constants 159
modifier_entries_total 473
min_modifiers 3
max_modifiers 7
avg_modifiers 3.24
no_modifier 0
weak_lt3 0
tiny_only 0
tiny_components 25
unresolved_constants 0
missing_picture 0
missing_sprite 0
missing_texture 0
missing_dds 0
missing_loc_or_desc 0
```

Current Event 005 first-wave and force-package validation:

```text
kaz_gate_block_present True
western_pool_count 6 tags BLR,EST,LAT,LIT,MOL,UKR
caucasus_pool_count 3 tags ARM,AZR,GEO
central_asia_pool_count 4 tags KYR,TAJ,TMS,UZB
extra_pool_count 13 tags ARM,AZR,BLR,EST,GEO,KYR,LAT,LIT,MOL,TAJ,TMS,UKR,UZB
normal_pools_include_kaz False
required_pool_random_select_amount_1 all True
required_pool_array_dedupe all True
required_pool_supports_nonexistent_core_release_candidate all True
required_pool_supports_existing_subject_candidate all True
release_calls_required_pools True
release_extra_random_calls 3
release_extra_scaling_chaos_tier_mentions 21
release_extra_scaling_has_war True
release_extra_scaling_stability True
release_extra_scaling_war_support True
selected_release_nonexistent True
selected_frees_existing_subject True
selected_calls_setup_and_focus True
kaz_gate_used True
kaz_gate_requires_southern_or_high_pressure True
kaz_gate_high_chaos_escape True
southern_republic_setup_calls 8
setup_idempotent_guard True
setup_calls_package True
package_adds_breakaway_array_and_counts True
package_base_temp_variables 4
package_manpower_var True
package_equipment_var_entries 3
package_division_templates 2
package_meta_create_unit_entries 2
package_dynamic_unit_count_tokens True
package_clamps_field_units True
package_major_scaling_tags KAZ,UKR
package_regional_scaling_tag_count 7
package_chaos_scaling_bands 10
package_soviet_war_scaling True
package_weak_center_scaling True
package_one_use_declaration_scaling True
package_terminal_scaling True
package_clears_one_use_flags True
```

Current Event 005 Union Unmade and terminal-collapse validation:

```text
blocks_present True
union_unmade_first_month_lock_gate True
union_unmade_duplicate_gate True
union_unmade_min_breakaway_gate True
union_unmade_high_threat_gate True
union_unmade_critical_authority_gate True
union_unmade_contested_authority_gate True
union_unmade_league_kaz_or_chaos_gate True
union_unmade_deep_tier5_gate True
show_sets_fired_flag True
show_applies_terminal_collapse True
show_sets_super_event_id True
show_emits_super_event True
terminal_idempotent_gate True
terminal_in_progress_flag_wrap True
terminal_calls_ordinary_release True
terminal_calls_high_chaos_spawn True
terminal_calls_mission_cleanup True
ordinary_release_tags_count 14 expected_count 14 missing none extra none
ordinary_releases_nonexistent_core_under_sov True
ordinary_frees_existing_subjects True
ordinary_calls_setup_and_focus True
terminal_spawn_tier4_or_5_retry True
terminal_spawn_tier5_prepare True
highest_chaos_prepare_flags 26
highest_chaos_sets_weirdness_floor True
high_chaos_spawn_helpers 38
high_chaos_setup_successor_helpers 38
high_chaos_spawn_helpers_reach_breakaway_setup 38
high_chaos_spawn_helpers_missing_setup_path 0
mission_defs 128 cleanup_remove_refs 128 cleanup_active_refs 128 missing_remove 0 extra_remove 0 missing_active 0
cleanup_clears_active_flags True
cleanup_clears_transient_country_flags True
event005_category_defs 42 categories_without_active_gate 0
constants_union_unmade_slot True
super_event_14_loc_keys_present True
super_event_14_sprite_present True
super_event_14_dds_exists True
```

Current Event 005 crisis-balance validation:

```text
baseline_moscow_authority 62
baseline_total_threat_estimate 7.25
opening_tier1_calm_threat_estimate 9.25
opening_tier5_calm_threat_estimate 32.25
opening_tier5_disaster_threat_estimate 50.25
opening_tier5_disaster_authority_estimate 38
total_threat_multiplier 0.25
total_threat_floor 0
total_threat_ceiling 100
monthly_guard_calm_success_cap 1
monthly_guard_moderate_success_cap 4
monthly_guard_success_regs 11
monthly_guard_failure_regs 11
component_min_max 0/100
init_sets_all_components True
init_first_month_lock_days_31 True
init_chaos_tier_adjustment_blocks 5
init_uses_stability_war_support_war_capital_conditions True
init_calls_recalculate True
recalc_calls_component_clamp_helper True
component_clamp_entries 7
recalc_uses_all_components True
recalc_uses_multiplier True
recalc_clamps_total_threat True
objective_pressure_helpers_total 22
pressure_helpers_call_recalc 22 missing_recalc 0
pressure_helper_variables_touched soviet_collapse_depot_vulnerability,soviet_collapse_evolution_weirdness,soviet_collapse_foreign_appetite,soviet_collapse_league_cohesion,soviet_collapse_military_obedience,soviet_collapse_moscow_authority,soviet_collapse_republic_confidence
pressure_constants_count 72
pressure_constants_has_positive_and_negative True
decision_pressure_helper_variants_used 20
decision_pressure_helper_calls 256
opening_event_option_recalculate_calls 4
opening_event_options_touch_components soviet_collapse_depot_vulnerability,soviet_collapse_evolution_weirdness,soviet_collapse_foreign_appetite,soviet_collapse_league_cohesion,soviet_collapse_military_obedience,soviet_collapse_moscow_authority,soviet_collapse_republic_confidence
eventlog_detail_authority_function True
eventlog_detail_threat_function True
eventlog_detail_foreign_function True
eventlog_detail_league_function True
category_desc_mentions_moscow_authority True
category_desc_mentions_union_crisis_threat True
category_desc_visible_cause_hits 18
banned_low_dynamic_baseline_phrase_hits 0
```

Current Event 005 mission-duration, cost-localisation, and focus-structure validation:

```text
mission_defs 128
mission_duration_constants_used 11
mission_duration_min 95
mission_duration_max 365
mission_duration_below_90 0
missions_allowed_always_no 128 missing 0
missions_complete_timeout 128 128 missing_complete 0 missing_timeout 0
missions_success_failure_pressure 128 128 missing_success 0 missing_failure 0
missions_requeue_objectives 128 missing 0
mission_board_cap_surface count_helpers 1 activation_helpers 1 count_refs 128 activate_refs 128 active_cap 10 queue_cap True
event005_localisation_bom_prefix efbbbf
event005_localisation_colon_zero_keys 0
requires_hits_event005_loc 0
blocked_or_cost_long_over_7_words 0
banned_low_dynamic_baseline_phrase_hits 0
focus_blocks 1121 duplicate_ids 0
focus_missing_icon_reward_ai_filters 0 0 0 0
focus_x_range 2 38
focus_y_range 0 42
continuous_focus_positions 46 right_side_panel 46 y_min 180 y_max 180
```

Current Event 005 AI validation:

```text
decision_child_blocks 254
missions_manual_activation_no_ai_expected 128
regular_decisions 126
regular_decisions_with_ai 126 missing_ai 0
regular_decisions_dynamic_ai 126 flat_ai 0
decision_categories_with_regular_decisions 41
focus_blocks 1121
focus_with_ai 1121 missing_ai 0
focus_dynamic_ai 227 flat_ai 894
route_or_gate_focuses 255 dynamic 201 flat 54
mutually_exclusive_focuses 114 dynamic 114 flat 0
available_gate_focuses 112 dynamic 58 flat 54
ai_pressure_ref_counts soviet_collapse_total_collapse_threat:11,soviet_collapse_moscow_authority:45,soviet_collapse_republic_confidence:2,soviet_collapse_military_obedience:12,soviet_collapse_depot_vulnerability:15,soviet_collapse_foreign_appetite:34,soviet_collapse_league_cohesion:0,soviet_collapse_evolution_weirdness:49
ai_condition_counts has_war:60,has_war_with:52,stability:71,war_support:1,faction:4,country_flags:102,global_flags:84,SOV_scoped:160,check_variable:169,factor_zero:80
```

Current Event 005 spreadsheet status validation:

```text
catalog_workbook docs/spreadsheets/chaos_redux_events_catalog.xlsx
event005_row 6
event005_status_cell L6 Implemented - Verified
event005_cluster_status_cell R6 Complete
workbook_zip_test ok
workbook_formula_count 0
workbook_formula_error_markers 0
libreoffice_headless_convert ok
stale_missing_logs_status_hits 0
```

Current Event 005 comprehensive correction overlap validation:

```text
missing_continuation_spec_present False
removed_runtime_logs_current_blockers False
event5_detail_mapping True
event_detail_main_loc_present True file localisation/english/chaosx_gui_l_english.yml
event_detail_main_refs_count 7 missing_refs none
event_detail_functions 7 missing_funcs none
event_detail_function_fallback_missing none
event_detail_function_loc_missing 0 detail_keys_missing_all 0
event_detail_function_key_counts CrisisState:3,FirstWave:4,League:2,Authority:5,Threat:4,Foreign:4,Mutation:3
event005_direct_evolution_writer_calls 1
event005_record_helper_sets_event_type_tier True
event005_record_helper_actor_target True
event005_record_helper_duplicate_tier_flags True
event005_setup_stage_record_calls 38
event005_spawn_context_triplets 38
event005_evolution_enabled_gates 38
event005_baseline_event_file_direct_record False
restore_party_control_expected_spends True
send_loyalist_officers_expected_spends True
send_loyalist_officers_equipment_or_manpower_spend False
decision_cost_constants_missing none
```

## Final Completion Report

The requested final completion report categories are closed by current repository evidence. Historical missing continuation context remains documented: `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` is absent, but it is not part of the active required source order and its named surfaces are covered by direct implementation evidence. The strict verifier exits 0.

Current evidence exists for:

- implemented countries and packages: thirty-eight custom successors plus supported ordinary Soviet republics.
- flags: 570 Event 005 custom flag files audited; no current binary correction indicated.
- focus counts and branch maps: 1121 retained focus blocks across the Event 005 runtime focus files, with no duplicate IDs or invalid focus references.
- missions and decisions: 128 Soviet crisis missions, 128 activation entries, and 128 terminal removal entries; main Soviet, breakaway, and foreign patron crisis decisions use dynamic AI weights.
- evolutions and super-events: high-chaos successor evolution writer and super-event helpers remain wired for the current route surface.
- achievements and assets: achievement, focus, flag, leader, and super-event asset surfaces are documented in the Event 005 docs and asset manifests.
- tests and checks: brace depth, focus reference, mission wiring, idea-strength, localisation phrase, flag orientation, unsupported operator/scope, and whitespace checks passed in the latest audit.

Final checklist:

- active source inputs are present and audited.
- active influence/threat/focus rework source coverage is first in the verified source order.
- comprehensive correction source coverage maps to concrete verifier surfaces as additional consulted context.
- historical event-log/mission-balance/focus-cleanup continuation context is directly covered by implementation evidence.
- `tmp/error.log` and `tmp/text.log` runtime logs were intentionally removed after fixed errors.
- strict verifier exits 0 before marking the active Event 005 correction goal complete.

## Resume Packet

Current committed audit head should be checked on resume with:

```text
git log -1 --oneline
```

Use this source order on resume:

1. `tmp/005_soviet_union_collapse_influence_threat_focus_rework_spec.md`
2. `tmp/005_soviet_union_collapse_final_clean_spec_part_1_core_crisis.md`
3. `tmp/005_soviet_union_collapse_final_clean_spec_part_2_objectives_missions_intervention.md`
4. `tmp/005_soviet_union_collapse_final_clean_spec_part_3_republics_focus_trees.md`
5. `tmp/005_soviet_union_collapse_final_clean_spec_part_4_custom_countries_evolutions_assets_achievements.md`
6. `AGENTS.md`
7. `.agents/skills/chaos-redux-events/SKILL.md`
8. `.agents/skills/chaos-redux-event-assets/SKILL.md`
9. `.agents/skills/chaos-redux-super-events/SKILL.md`

The first file is present and remains the source of truth for this pass. `tmp/005_soviet_union_collapse_spawn_balance_collapse_pacing_cleanup_spec.md` remains additional consulted context. The historical `tmp/005_soviet_union_collapse_event_log_mission_balance_focus_cleanup_spec.md` file is still absent from `tmp/`, but it is not an active required input. The previous `tmp/error.log` and `tmp/text.log` runtime logs were intentionally removed after the reported errors were fixed and are not current blockers.

Do not redo already-passed implementation work unless a restored file contradicts current evidence. Current parser-oriented evidence covers strong ideas, randomized first-wave pools, Kazakhstan restraint, dynamic force packages, crisis meter dampening, Union Unmade first-month lock and gates, terminal ordinary republic release, terminal special-successor spawning, mission cleanup, focus layout, flag orientation, localisation phrase cleanup, AI weights, spreadsheet row status, and docs.

First resume action:

```text
python3 .tools/verify_event005_completion_gate.py
```

If a future task explicitly restores or re-requires the historical event-log/mission-balance/focus-cleanup continuation file, record its line count, bytes, and SHA-256 value in `docs/events/005_soviet_union_collapse_input_audit.md`, then audit any new requirements against the implementation.

Resume validation commands:

```text
python3 -m py_compile .tools/verify_event005_completion_gate.py
git diff --check
python3 .tools/verify_event005_completion_gate.py
git status --short
```

The strict verifier must exit 0 before marking the active Event 005 correction goal complete.
