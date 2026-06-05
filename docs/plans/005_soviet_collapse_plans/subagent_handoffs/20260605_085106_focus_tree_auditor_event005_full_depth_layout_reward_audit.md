# Event 005 Soviet Collapse Focus Tree Audit

Subagent: `chaosx_focus_tree_auditor`  
Date: 2026-06-05 08:51 UTC  
Scope: read-only audit of the four requested Event 005 focus files. No gameplay files, gfx, flags, or localisation were edited.

## References Consulted

- Repo skill: `hoi4-focus-trees`
- Related skill read for decision integration checks: `hoi4-decisions-missions`
- Offline wiki snapshot: National focus modding, Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Vanilla docs/files: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/focus_inlay_windows/documentation.md`, and focus precedents from `soviet.txt`, `baltic_shared.txt`, `china_warlord.txt`

## Counting Method

- `add_ideas count`: number of `add_ideas` payload entries in focus completion rewards.
- `duplicate add_ideas-in-same-focus`: focuses adding the same idea more than once in the same reward.
- `helper-only reward`: reward contains only scripted-effect wrapper calls and no direct concrete effects/flags/variables in the focus body. This is not automatically a bug, but it makes reward review depend on helper definitions.
- `tiny equipment/building reward`: focus reward is mainly a small equipment, manpower, or building grant without claims, cores, war goals, decisions, route flags, events, or obvious mechanic movement in the focus body.
- `expansion/mechanic unlock`: focus moves claims/cores/war goals/factions/AI aggression/decisions/events/variables/route flags, or calls an Event 005 helper that does.

## File Totals

| File | Focuses | add_ideas | Duplicate add_ideas in focus | Helper-only rewards | Tiny equipment/building rewards | Expansion/mechanic unlocks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 0 | 15 | 88 | 500 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 0 | 2 | 114 | 1005 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 0 | 2 | 9 | 128 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 0 | 32 | 0 | 64 |

Main reward finding: the current files do not spam `add_ideas`; `add_ideas =` is absent from the audited focus rewards. The main reward risk is instead review opacity and one-off reward thinness: many rewards are helper-driven, and some regional/custom splinter focuses still feel like isolated building/equipment pips rather than route payoffs.

## Tree Counts

| File | Tree | Line | Focuses | add_ideas | Dup ideas | Helper-only | Tiny rewards | Expansion/mechanic |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| republics | `soviet_collapse_ukraine_focus_tree` | 17 | 83 | 0 | 0 | 5 | 6 | 83 |
| republics | `soviet_collapse_breakaway_focus_tree` | 2313 | 36 | 0 | 0 | 2 | 7 | 36 |
| republics | `soviet_collapse_internal_republic_focus_tree` | 3125 | 62 | 0 | 0 | 0 | 19 | 62 |
| republics | `soviet_collapse_baltic_focus_tree` | 4645 | 42 | 0 | 0 | 4 | 12 | 42 |
| republics | `soviet_collapse_caucasus_focus_tree` | 5608 | 40 | 0 | 0 | 1 | 4 | 40 |
| republics | `soviet_collapse_central_asia_focus_tree` | 6529 | 45 | 0 | 0 | 1 | 12 | 45 |
| republics | `soviet_collapse_moldova_focus_tree` | 7669 | 48 | 0 | 0 | 1 | 9 | 47 |
| republics | `soviet_collapse_belarus_focus_tree` | 8820 | 53 | 0 | 0 | 1 | 1 | 53 |
| republics | `soviet_collapse_kazakhstan_focus_tree` | 10126 | 92 | 0 | 0 | 0 | 18 | 92 |
| custom splinters | `FTH_soviet_collapse_focus_tree` | 14 | 47 | 0 | 0 | 0 | 9 | 47 |
| custom splinters | `PRA_soviet_collapse_focus_tree` | 1221 | 22 | 0 | 0 | 0 | 2 | 22 |
| custom splinters | `TSC_soviet_collapse_focus_tree` | 1836 | 18 | 0 | 0 | 0 | 3 | 18 |
| custom splinters | `RMC_soviet_collapse_focus_tree` | 2346 | 18 | 0 | 0 | 0 | 1 | 18 |
| custom splinters | `DSC_soviet_collapse_focus_tree` | 2822 | 18 | 0 | 0 | 0 | 0 | 18 |
| custom splinters | `NRF_soviet_collapse_focus_tree` | 3345 | 18 | 0 | 0 | 0 | 1 | 18 |
| custom splinters | `ICD_soviet_collapse_focus_tree` | 3849 | 18 | 0 | 0 | 0 | 1 | 18 |
| custom splinters | `BSC_soviet_collapse_focus_tree` | 4317 | 47 | 0 | 0 | 0 | 11 | 47 |
| custom splinters | `TNC_soviet_collapse_focus_tree` | 5461 | 47 | 0 | 0 | 0 | 8 | 47 |
| custom splinters | `ALA_soviet_collapse_focus_tree` | 6596 | 47 | 0 | 0 | 0 | 5 | 47 |
| custom splinters | `BBH_soviet_collapse_focus_tree` | 7707 | 47 | 0 | 0 | 0 | 8 | 47 |
| custom splinters | `KRS_soviet_collapse_focus_tree` | 8901 | 47 | 0 | 0 | 0 | 7 | 47 |
| custom splinters | `UDC_soviet_collapse_focus_tree` | 10126 | 47 | 0 | 0 | 0 | 3 | 47 |
| custom splinters | `SDZ_soviet_collapse_focus_tree` | 11334 | 47 | 0 | 0 | 0 | 2 | 47 |
| custom splinters | `GAC_soviet_collapse_focus_tree` | 12584 | 47 | 0 | 0 | 0 | 2 | 47 |
| custom splinters | `DHC_soviet_collapse_focus_tree` | 13751 | 47 | 0 | 0 | 2 | 3 | 47 |
| custom splinters | `KHC_soviet_collapse_focus_tree` | 14950 | 47 | 0 | 0 | 0 | 4 | 47 |
| custom splinters | `FEV_soviet_collapse_focus_tree` | 16115 | 47 | 0 | 0 | 0 | 5 | 47 |
| custom splinters | `SZA_soviet_collapse_focus_tree` | 17306 | 47 | 0 | 0 | 0 | 6 | 47 |
| custom splinters | `UWD_soviet_collapse_focus_tree` | 18475 | 47 | 0 | 0 | 0 | 4 | 47 |
| custom splinters | `MRC_soviet_collapse_focus_tree` | 19662 | 47 | 0 | 0 | 0 | 6 | 47 |
| custom splinters | `IUL_soviet_collapse_focus_tree` | 20835 | 47 | 0 | 0 | 0 | 5 | 47 |
| custom splinters | `BAC_soviet_collapse_focus_tree` | 21975 | 47 | 0 | 0 | 0 | 7 | 47 |
| custom splinters | `ARD_soviet_collapse_focus_tree` | 23108 | 47 | 0 | 0 | 0 | 8 | 47 |
| custom splinters | `NLC_soviet_collapse_focus_tree` | 24307 | 47 | 0 | 0 | 0 | 3 | 47 |
| factory successors | `CFR_soviet_collapse_focus_tree` | 17 | 47 | 0 | 0 | 0 | 2 | 47 |
| factory successors | `OGB_soviet_collapse_focus_tree` | 1008 | 23 | 0 | 0 | 0 | 2 | 23 |
| factory successors | `MFR_soviet_collapse_focus_tree` | 1569 | 58 | 0 | 0 | 2 | 5 | 58 |
| ancient restorations | `KZR_soviet_collapse_ancient_focus_tree` | 12 | 16 | 0 | 0 | 8 | 0 | 16 |
| ancient restorations | `SOG_soviet_collapse_ancient_focus_tree` | 422 | 16 | 0 | 0 | 8 | 0 | 16 |
| ancient restorations | `KHW_soviet_collapse_ancient_focus_tree` | 826 | 16 | 0 | 0 | 8 | 0 | 16 |
| ancient restorations | `ALN_soviet_collapse_ancient_focus_tree` | 1234 | 16 | 0 | 0 | 8 | 0 | 16 |

## Top 20 Worst Focus IDs

1. `blr_soviet_collapse_the_green_border` - `common/national_focus/005_soviet_collapse_republics.txt:9735`  
   Layout bug: prerequisite `blr_soviet_collapse_belarusian_question_answered` is at `(16,9)` while this child is at `(28,8)`, so the prerequisite line has to route upward.

2. `blr_soviet_collapse_the_green_rail_pact` - `common/national_focus/005_soviet_collapse_republics.txt:10052`  
   Layout bug: same parent `blr_soviet_collapse_belarusian_question_answered` at `(16,9)` is not above the child at `(22,9)`.

3. `MFR_armorers_elect_delegates` - `common/national_focus/005_soviet_collapse_factory_successors.txt:1731`  
   Layout bug: it sits at `(12,6)` directly between mutually exclusive route siblings `MFR_officers_chair_the_board` `(2,6)` and `MFR_merchants_of_ammunition` `(24,6)`.

4. `ukr_soviet_collapse_black_sea_port_ledgers` - `common/national_focus/005_soviet_collapse_republics.txt:1208`  
   Too close to `ukr_soviet_collapse_open_the_liaison_offices` on row `y=5`; coordinates `(27,5)` and `(28,5)`.

5. `ukr_soviet_collapse_open_the_liaison_offices` - `common/national_focus/005_soviet_collapse_republics.txt:235`  
   Same too-close row as above; also appears earlier in file than surrounding diplomacy lane, which makes manual route review harder.

6. `internal_soviet_collapse_crimean_tatar_councils` - `common/national_focus/005_soviet_collapse_republics.txt:3870`  
   Too close to `internal_soviet_collapse_taiga_steppe_self_rule`; row `y=5`, coordinates `(20,5)` and `(21,5)`.

7. `internal_soviet_collapse_taiga_steppe_self_rule` - `common/national_focus/005_soviet_collapse_republics.txt:4074`  
   Same too-close layout risk.

8. `central_asia_soviet_collapse_the_cotton_question` - `common/national_focus/005_soviet_collapse_republics.txt:7267`  
   Too close to `central_asia_soviet_collapse_negotiate_with_the_mountain_bands`; row `y=4`, coordinates `(3,4)` and `(4,4)`.

9. `central_asia_soviet_collapse_negotiate_with_the_mountain_bands` - `common/national_focus/005_soviet_collapse_republics.txt:7185`  
   Same too-close layout risk.

10. `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` - `common/national_focus/005_soviet_collapse_republics.txt:7439`  
    Too close to `central_asia_soviet_collapse_desert_scout_columns`; row `y=6`, coordinates `(6,6)` and `(7,6)`.

11. `central_asia_soviet_collapse_desert_scout_columns` - `common/national_focus/005_soviet_collapse_republics.txt:6925`  
    Same too-close layout risk.

12. `moldova_soviet_collapse_river_guard_brigades` - `common/national_focus/005_soviet_collapse_republics.txt:7894`  
    Too close to `moldova_soviet_collapse_ukrainian_grain_road`; row `y=5`, coordinates `(14,5)` and `(15,5)`.

13. `moldova_soviet_collapse_ukrainian_grain_road` - `common/national_focus/005_soviet_collapse_republics.txt:8013`  
    Same too-close layout risk.

14. `kaz_soviet_collapse_the_alash_courts` - `common/national_focus/005_soviet_collapse_republics.txt:10378`  
    Too close to `kaz_soviet_collapse_the_steppe_arsenal`; row `y=5`, coordinates `(22,5)` and `(23,5)`.

15. `kaz_soviet_collapse_the_steppe_arsenal` - `common/national_focus/005_soviet_collapse_republics.txt:10590`  
    Same too-close layout risk.

16. `kaz_soviet_collapse_domestic_resource_state` - `common/national_focus/005_soviet_collapse_republics.txt:10517`  
    Crowded Kazakhstan industry/political lane: `(20,7)` next to `(21,7)` and `(22,7)`.

17. `kaz_soviet_collapse_no_concession_without_a_republic` - `common/national_focus/005_soviet_collapse_republics.txt:10911`  
    Crowded between `domestic_resource_state` and `copper_and_chrome_ledgers`.

18. `kaz_soviet_collapse_copper_and_chrome_ledgers` - `common/national_focus/005_soviet_collapse_republics.txt:11672`  
    Same crowded row; this lane likely needs horizontal spreading.

19. `FTH_village_delegate_roads` - `common/national_focus/005_soviet_collapse_custom_splinters.txt:532`  
    Reward is mostly one random infrastructure/rail bump plus generic depot/recovery helpers. It should become a decision/staged commune-road mechanic or a stronger named corridor payoff.

20. `PRA_switchyard_denial_posts` - `common/national_focus/005_soviet_collapse_custom_splinters.txt:1523`  
    For a rail authority special country, reward is only bunkers in owned states plus generic military consolidation. It should deny rail/supply to enemies, add rail-guard units, route-lock junction decisions, or change the PRA rail authority mechanic.

## Pathline and Layout Risks

Hard pathline issues:

- `soviet_collapse_belarus_focus_tree`
  - `blr_soviet_collapse_the_green_border` `(28,8)` depends on `blr_soviet_collapse_belarusian_question_answered` `(16,9)`.
  - `blr_soviet_collapse_the_green_rail_pact` `(22,9)` depends on `blr_soviet_collapse_belarusian_question_answered` `(16,9)`.
- `MFR_soviet_collapse_focus_tree`
  - `MFR_armorers_elect_delegates` `(12,6)` is between the mutex siblings `MFR_officers_chair_the_board` `(2,6)` and `MFR_merchants_of_ammunition` `(24,6)`.

Too-close node risks:

- Ukraine: `(27,5)`/`(28,5)` for `ukr_soviet_collapse_black_sea_port_ledgers` and `ukr_soviet_collapse_open_the_liaison_offices`.
- Internal republic: `(20,5)`/`(21,5)` for `internal_soviet_collapse_crimean_tatar_councils` and `internal_soviet_collapse_taiga_steppe_self_rule`.
- Central Asia: `(3,4)`/`(4,4)`, `(6,6)`/`(7,6)`, `(8,8)`/`(9,8)`.
- Moldova: `(14,5)`/`(15,5)`, `(14,7)`/`(15,7)`.
- Kazakhstan: ten too-close pairs, especially the dense rows at `y=7` and `y=8`.

No duplicate absolute coordinates were found after resolving same-line `x = ... y = ...` coordinates correctly.

## Shallow or Missing Branches

Shallow by focus count:

- `PRA_soviet_collapse_focus_tree` has 22 focuses. It has a strong rail/supply identity, but needs more political/diplomatic/expansion depth for a special country.
- `TSC`, `RMC`, `DSC`, `NRF`, `ICD` each have 18 focuses. They are compact high-chaos packages, not full trees. DSC is mechanically aggressive through helpers, but the tree is still narrow.
- `OGB_soviet_collapse_focus_tree` has 23 focuses. It has expansion/restoration identity but is short for a standalone ancient restoration successor.
- `KZR`, `SOG`, `KHW`, `ALN` each have 16 focuses. They have political/industry/military/expansion signals, but the first half of each tree is largely helper-only and compact.

Missing or weak expansion branch by heuristic:

- `soviet_collapse_breakaway_focus_tree`: only one obvious expansion-tagged focus. It has survival, sponsor, local court, and neutrality content, but no distinct expansion or settlement branch.
- `soviet_collapse_belarus_focus_tree`: only two obvious expansion-tagged focuses; the green/forest route should get clearer border, league, partisan corridor, or anti-Soviet settlement payoffs.
- `TNC`, `ALA`, `KRS`, `DHC`, `FEV`, `SZA`, `UWD`, `IUL`, `ARD`: each has 47 focuses but only one or two obvious expansion-tagged nodes. Some may route expansion through generic high-chaos helpers, but the tree surface does not clearly show a distinct expansion branch.

Trees that generally meet the branch surface requirement:

- Ukraine, internal republics, Baltic, Caucasus, Central Asia, Moldova, Kazakhstan, FTH, BSC, BBH, UDC, SDZ, GAC, KHC, MRC, BAC, NLC, CFR, MFR. These still need the layout and reward-thinness fixes above.

## Chaos/Special Country OP and Aggression Review

- `CFR`: strong construction/factory identity is present through `soviet_collapse_apply_cfr_focus_*` helpers, offsite buildings, construction mandate variables, contract decisions, and AI building strategies. Aggression exists via high-chaos helper payloads, but the focus surface reads more construction-state than conqueror until late focuses. Keep OP construction, add clearer visible expansion/neighbor pressure on the route surface.
- `MFR`: strongest special tree in this audit. It has 58 focuses, military industry, foreign arms routes, production variables, and expansion/aggression hooks. Main issue is layout: the mutually exclusive opening fork has an unrelated node between the siblings.
- `PRA`: rail/supply identity is good and `PRA_rails_over_capitals` is aggressive, but the tree is only 22 focuses. `PRA_switchyard_denial_posts` is too small for a special rail authority. Add more rail-denial, junction claims, mobile armored train formations, and supply-route war mechanics.
- `DSC`: only 18 focuses, but helper effects such as `soviet_collapse_dsc_unleash_dead_army_campaign` are aggressively overpowered: manpower, equipment, cores, assault columns, neighbor wars. It needs more tree depth, not necessarily more raw power.
- `TSC`, `RMC`, `NRF`, `ICD`: compact 18-focus high-chaos trees. They have thematic mechanics but do not meet full-depth political/industry/military/diplomatic/expansion expectations unless deliberately treated as short-lived crisis actors.
- `OGB` and the ancient restoration trees: aggression/claims exist, but tree depth is compact. Ancient-restoration helper abstraction is acceptable for reuse, but the parent should deepen at least one route-specific decision/formation lane per country if they are intended as playable successors.

## Focus-Mechanic Integration

Strong connections found:

- Focuses frequently move Event 005 variables: recognition, depot control, league support, local authority pressure, collapse threat/objective pressure, special country mandate variables.
- Focuses unlock or advertise decision families: CFR construction decisions, MFR arsenal decisions, PRA rail decisions, ancient restoration museum/archive/banner decisions, custom splinter consolidation/mobilization/extreme route decisions.
- High-chaos focus helpers connect to scenario/terminal chaos and neighbor conflict through `soviet_collapse_apply_high_chaos_focus_payload`, `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`, and custom splinter expansion helpers.

Risks:

- Many focus rewards are opaque wrappers; this is maintainable only if helper docs stay current. Ancient restorations have 32 helper-only focus rewards across 64 focuses.
- Some trees rely on generic helper names for expansion, so the visible focus tree can look less aggressive than the actual mechanics.
- Tiny building/equipment rewards remain common in custom splinters and republic regional trees. These should either be explicitly positioned as small support nodes or folded into broader mechanics/decision unlocks.

## Recommended Parent Implementation Order

1. Fix hard layout first in `common/national_focus/005_soviet_collapse_republics.txt`.
   - Move `blr_soviet_collapse_the_green_border` and `blr_soviet_collapse_the_green_rail_pact` below `blr_soviet_collapse_belarusian_question_answered`, or change the prerequisite to the intended parent if the current parent is only a route gate.

2. Fix the MFR mutex layout in `common/national_focus/005_soviet_collapse_factory_successors.txt`.
   - Move `MFR_armorers_elect_delegates` out from between `MFR_officers_chair_the_board` and `MFR_merchants_of_ammunition`.

3. Spread too-close rows in republic trees.
   - Ukraine: `ukr_soviet_collapse_black_sea_port_ledgers`, `ukr_soviet_collapse_open_the_liaison_offices`.
   - Internal republic: `internal_soviet_collapse_crimean_tatar_councils`, `internal_soviet_collapse_taiga_steppe_self_rule`.
   - Central Asia, Moldova, Kazakhstan: spread the listed close pairs by at least one more `x` unit.

4. Deepen the shallow special trees before adding more broad content.
   - Start with `PRA_soviet_collapse_focus_tree`, then `DSC`, `TSC/RMC/NRF/ICD`, then `OGB`, then `KZR/SOG/KHW/ALN`.
   - Use existing helpers: `soviet_collapse_build_pra_corridor_network`, `soviet_collapse_spawn_pra_rail_guard_columns`, `soviet_collapse_dsc_unleash_dead_army_campaign`, `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`, `soviet_collapse_apply_custom_splinter_expansion_claims`.

5. Strengthen weak expansion branches.
   - Breakaway and Belarus should get visible expansion/settlement/league lanes, not just hidden helper effects.
   - Custom splinters with weak expansion signal: `TNC`, `ALA`, `KRS`, `DHC`, `FEV`, `SZA`, `UWD`, `IUL`, `ARD`.

6. Convert thin support rewards into branch payoffs.
   - Patch examples: `FTH_village_delegate_roads`, `PRA_switchyard_denial_posts`, `BSC_road_and_well_ledger`, `BSC_caravan_supply_hubs`, `TSC_recover_the_burned_glass`.
   - Preferred patch style: unlock or upgrade a decision, add route-specific units, claims/cores, rail/supply network changes, AI aggression, or visible mechanic variables rather than just one random building.

7. Add/update helper documentation if parent expands helper usage.
   - The focus files call many `soviet_collapse_apply_*` helpers; if new dynamic helpers are added, document them in the relevant scripted effects markdown per repo rules.

## Validation Notes

- Read-only parser resolved focus blocks, same-line `x = ... y = ...` coordinates, prerequisites, mutexes, rewards, and reward keyword classes.
- Manual spot checks were performed on the worst layout and reward cases and on helper definitions in `common/scripted_effects/005_soviet_collapse_effects.txt`.
- No syntax validator or game load was run.
- No patches were made, so no patch handoff beyond this audit report is required.

## Simplifications, Omissions, and Blockers

- No gameplay patch was made because the discovered issues were broader layout/depth work or outside the allowed tiny pathline/duplicate-idea patch scope.
- No gfx/flags were touched.
- This audit did not inspect every localisation key or focus icon sprite definition; it focused on tree depth, rewards, layout, and mechanic integration as requested.

## Skills Used

- `hoi4-focus-trees`
- `hoi4-decisions-missions` for verifying focus-decision integration expectations
