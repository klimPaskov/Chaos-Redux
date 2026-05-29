# Soviet Collapse Focus Tree Full-Scope Audit and Narrow Patch Handoff

Date: 2026-05-29
Mode: focus-tree subagent, patch-capable for narrow local defects only.
Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No commit was created.

## References read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs and examples: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, plus vanilla national focus examples for prerequisites, filters, and `ai_will_do`.

## Files changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | Replaced 20 invalid `FOCUS_FILTER_ARMY` usages with vanilla-valid `FOCUS_FILTER_ARMY_XP`. |
| `common/national_focus/005_soviet_collapse_republics.txt` | Fixed exact upward/same-row pathline coordinates in Central Asia and Kazakhstan branches. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Fixed exact same-row pathline coordinate in the `NLC` branch. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_all_soviet_collapse_audit_patch_handoff.md` | This handoff. |

## Changed focus ids

Filter-only changes:

- `KZR_customs_workshop_compact`
- `KZR_volga_toll_guard`
- `KZR_guard_the_crossings`
- `KZR_expansionist_steppe_levy`
- `KZR_road_beyond_the_caspian`
- `SOG_bazaar_workshop_compact`
- `SOG_market_guard`
- `SOG_oasis_checkpoint_guard`
- `SOG_expansionist_merchant_claims`
- `SOG_cities_beyond_the_desert`
- `KHW_oasis_workshop_compact`
- `KHW_oasis_canal_guards`
- `KHW_guard_the_pumps`
- `KHW_expansionist_water_claims`
- `KHW_delta_without_a_center`
- `ALN_mountain_workshop_compact`
- `ALN_darial_guard_posts`
- `ALN_guard_the_pass_line`
- `ALN_expansionist_mountain_claims`
- `ALN_every_pass_a_border`

Coordinate changes:

| Focus id | Before | After | Reason |
| --- | --- | --- | --- |
| `central_asia_soviet_collapse_caspian_route_bargain` | `x = 22`, `y = 5` | `x = 22`, `y = 7` | Its prerequisite was at `y = 6`; the pathline ran upward. |
| `central_asia_soviet_collapse_desert_republic_settlement` | `x = 22`, `y = 6` | `x = 22`, `y = 8` | Kept the child below the moved Caspian route focus. |
| `central_asia_soviet_collapse_desert_route_to_foreign_aid` | `x = 20`, `y = 5` | `x = 20`, `y = 7` | Its prerequisite was at `y = 6`; the pathline ran upward. |
| `central_asia_soviet_collapse_liaison_missions_in_the_bazaar` | `x = 18`, `y = 5` | `x = 18`, `y = 7` | Its prerequisite was at `y = 6`; the pathline ran upward. |
| `kaz_soviet_collapse_industrial_settlement_compacts` | `x = 22`, `y = 8` | `x = 22`, `y = 10` | Same-row path from `kaz_soviet_collapse_emergency_oil_boards` crossed multiple focuses. |
| `kaz_soviet_collapse_resource_sovereignty` | `x = 20`, `y = 9` | `x = 20`, `y = 11` | Kept the child below the moved industrial settlement payoff. |
| `kaz_soviet_collapse_the_steppe_outlives_the_union` | `x = 18`, `y = 11` | `x = 18`, `y = 12` | Avoided a same-row path from `kaz_soviet_collapse_resource_sovereignty`. |
| `NLC_commune_staff_map` | `x = 4`, `y = 11` | `x = 4`, `y = 12` | Same-row path from `NLC_heated_workshop_contracts` crossed the branch. |

No localisation keys or icon ids were changed.

## Route coverage table

| Required route/content area | Implemented coverage | Status | Main references |
| --- | --- | --- | --- |
| Political branches | Present in all tree families. | Partial | All four focus files; many branches still only set flags/helpers. |
| Industry branches | Present in republics, factory successors, custom splinters, and ancient restorations. | Partial | `CFR_*`, `MFR_*`, `PRA_*`, `UWD_*`, regional republic industry focuses. |
| Military branches | Present in nearly every tree. | Partial | Many rewards are XP, equipment, or shared helper calls rather than route-specific forces. |
| Diplomacy branches | Present through foreign, League, recognition, and bargain focuses. | Partial | No focus uses `activate_decision` or `activate_mission`; recognition and League play is mostly helper-driven. |
| Expansion branches | Present but thin. Claims and war goals exist only in limited areas. | Failing full target | Only 42 `add_state_claim` effects and 10 `create_wargoal` effects across 1,698 focuses. |
| Chaos-country OP identity | Partly present through endgame war goals, special ideas, and some AI pushes. | Failing full target | `DSC`, `RMC`, `NRF`, `ICD`, `PRA`, `TSC` remain short ladders; most 47-focus splinters still feel templated. |
| Decision and mission integration | Almost absent in focus rewards. | Failing full target | 0 `activate_decision`, 0 `activate_mission` across audited focuses. |
| Layout safety | Obvious parser-detectable same-row/upward pathlines were fixed. | Pass for mechanical pass | No duplicate coordinates, missing prerequisites, same-row prerequisite paths, or upward prerequisite paths remain in the four files. |
| Icons and localisation | All focus IDs have name/description localisation and icon assignments resolving to sprite definitions. | Load-safe but artistically repetitive | Repeated icons remain in several trees. |
| AI behavior | Every focus has `ai_will_do`, but many are flat. | Partial | 352 flat AI blocks remain, heavily concentrated in republic and ancient compact trees. |

## Missing or simplified content

- The broad rework is incomplete. The focus files are large, but many branches still deliver a repeated cadence of shared helper calls, flags, small stats, equipment, and single buildings.
- Direct idea spam is mostly gone in the focus files: 0 direct `add_ideas`, 0 `swap_ideas`, 0 `add_timed_idea`; only 8 direct cleanup `remove_ideas` calls remain.
- The reward-spam problem now mostly lives in helper cadence: `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_league_preparation`, `soviet_collapse_apply_focus_foreign_channel`, and `soviet_collapse_apply_focus_high_chaos_identity` carry much of the tree identity.
- Focus-decision integration is missing at the focus-file level. Focuses should unlock or upgrade expansion, coring, integration, recognition, rail, factory, naval, veteran, and high-chaos decision families.
- Overpowered chaos-country identity is still underbuilt. `DSC`, `RMC`, `NRF`, `ICD`, `PRA`, and `TSC` need real mechanics, not just endpoint pressure and war goals.
- Ancient restoration trees are only 16 focuses each. They have claims and distinct local variables, but they do not yet meet the full political, industry, military, diplomacy, expansion, mechanic, and postwar standard.
- `OGB_soviet_collapse_focus_tree` has only 23 focuses. It has Volga identity and IUL interaction, but it remains below the required Old Great Bulgaria depth.

## Icon coverage table

| Metric | Result |
| --- | ---: |
| Focus trees parsed | 41 |
| Focuses parsed | 1,698 |
| Missing icon assignments | 0 |
| Missing sprite definitions in mod/vanilla interface scan | 0 |
| Missing focus name localisation | 0 |
| Missing focus description localisation | 0 |

Repeated icon clusters still needing asset work:

| Tree | Repeated icons |
| --- | --- |
| `soviet_collapse_ukraine_focus_tree` | `GFX_ukr_soviet_collapse_democratic` x4, `GFX_ukr_soviet_collapse_industry` x3 |
| `soviet_collapse_internal_republic_focus_tree` | `GFX_focus_soviet_collapse_steppe_supply_congress` x4, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` x3 |
| `soviet_collapse_central_asia_focus_tree` | `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` x4, `GFX_central_asia_soviet_collapse_steppe_federation` x4 |
| `soviet_collapse_moldova_focus_tree` | `GFX_moldova_soviet_collapse_ukrainian_corridor` x4 |
| `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `CFR` | Multiple repeated icons, especially diplomacy, supply, war-plan, civil-rule, and construction icons. |

## Localisation and reward mismatch list

- Missing focus localisation: none found.
- Missing focus descriptions: none found.
- Filter patch localisation: no localisation needed; changed to vanilla filter ids.
- Coordinate patch localisation: no localisation needed.
- Main mismatch: focus titles/descriptions often promise government formation, route transformation, dangerous expansion, League politics, or state-specific mechanics while the reward is still a shared helper, flat variable, small building grant, or equipment stockpile.
- Specific high-risk mismatch examples: `PRA_rails_over_capitals`, `DSC_congress_of_the_dead_army`, `NRF_northern_revenant_fleet`, `ICD_commissariat_without_end`, `RMC_resurrection_without_state`, `TSC_starfall_mandate`, `OGB_the_old_name_survives_modern_war`, and many `*_extreme_path` focuses.

## AI behavior gaps

- Every parsed focus has `ai_will_do`, but 352 focus AI blocks have no local modifier.
- Flat AI is concentrated in `soviet_collapse_kazakhstan_focus_tree` (61), Ukraine (27), internal republics (25), Caucasus (23), Moldova (20), breakaway (18), Baltic (18), Central Asia (15), and each ancient tree (12).
- Focus rewards rarely add route-specific `add_ai_strategy`; factory successors and short crisis endpoints do it, but most republics and custom splinters do not.
- AI needs tag-specific route plans for chaos actors: dead army aggression, rail expansion, northern naval behavior, Black Banner raids, Basmachi cavalry, security-zone suppression, Green Army local defense, factory rivalry, and ancient restoration claims.
- AI also needs decision equivalents once focus-unlocked decision/missions are added.

## Route-by-route rework backlog

| Tree/family | Political branch needed | Industrial/logistics branch needed | Military branch needed | Expansion/diplomacy branch needed | Mechanic hooks needed |
| --- | --- | --- | --- | --- | --- |
| Ukraine, `soviet_collapse_ukraine_focus_tree` | Make democratic, socialist, directorate, Black Banner, and League choices alter leader/advisors/laws/cosmetic identity. | Tie grain, coal, ports, and arms cities to state-targeted decisions. | Add OOB/template changes and staff consequences by route. | Add postwar settlement, League votes, border integration. | Unlock Ukrainian state-integration, grain corridor, Black Sea defense, and Black Banner decision paths. |
| Generic breakaway, `soviet_collapse_breakaway_focus_tree` | Replace generic survival politics with small-state identities selected by origin/region. | Add capital rebuilding and depot-control projects. | Add border militia templates and emergency command. | Add claims, guarantees, neutrality or League membership choices. | Origin-aware decision unlocks and AI plans. |
| Internal republics, `soviet_collapse_internal_republic_focus_tree` | Differentiate Karelia, Komi, Idel-Ural/Tatar, Bashkir, Caucasus, Siberian, Far East, Yakutia, Buryatia, and Tuva variants. | Region-specific rail/resource/supply work. | Local defense styles: forest, mountain, steppe, taiga, rail. | League, autonomy, federation, or independence settlement branches. | Per-tag route flags, state targets, integration missions, AI strategy. |
| Baltic, Caucasus, Central Asia, Moldova, Belarus | Existing compact routes need sharper ideology and regional government consequences. | Ports, oil, mountain passes, irrigation, Dniester/Prut crossings, Belarus forests. | Regional templates and defensive/offensive missions. | Postwar claims, local leagues, sponsor risk, border settlement. | Focus-unlocked decisions for League votes, fortification zones, resource concessions, border missions. |
| Kazakhstan | Route tree is large but over-helpered. Political routes need clearer Alash/socialist/resource/federation consequences. | Oil, mines, rail, Caspian, and steppe industry should unlock state-targeted projects. | Mobile steppe army, horse/truck columns, rail guard brigades need templates and AI. | Southern republics, Caspian, Alash, and resource diplomacy need postwar integration. | Add decisions for resource sovereignty, steppe federation, border cavalry, Caspian security, and old-state memory. |
| Full 47-focus custom splinters: `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | Replace template names with route-specific councils, leaders, laws, advisors, and identity flags. | Tag-specific economic loops: commune rail, caravan routes, archives, mountain passes, Arctic ports, Ural factories. | Special units: tachankas, cavalry, sailors, command districts, internal troops, partisans, host cavalry, rail guards. | Neighbor-specific war goals, League bargains, protectorates, raids, and integration. | Reduce helper cadence; add bespoke scripted effects/decisions for each tag family. |
| Shallow crisis splinters: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | Each needs full fixed-purpose internal politics around hierarchy, doctrine, economy, recruitment, expansion, and endgame. | `PRA`: rail/supply-hub construction; `TSC`: observatory labs; `RMC`: shrine economy; `DSC`: grave ordnance; `NRF`: dockyards/ports; `ICD`: archive/prison logistics. | `PRA`: armored trains; `TSC`: perimeter regiments; `RMC`: martyr columns; `DSC`: revenant army; `NRF`: naval infantry/convoys; `ICD`: commissar battalions. | Immediate dangerous expansion with cores/claims/war goals and postwar cleanup. | Major redesign needed: decision categories, unit spawns/templates, AI attack plans, integration/occupation missions. |
| Factory successors: `CFR`, `MFR`, `OGB` | `CFR` and `MFR` have identity; `OGB` needs full Volga political/religious/trade route depth. | `CFR`: much larger civilian factory/construction projects; `MFR`: arsenal quotas and proxy arming; `OGB`: Volga trade/river authority. | `CFR`: construction battalions/engineers; `MFR`: guard divisions/armored trains; `OGB`: heritage guard/steppe cavalry. | Factory merger/rivalry, reconstruction protectorates, arsenal clients, Volga claims and Idel-Ural settlement. | Add construction/arsenal decision systems, factory rivalry missions, contract pressure, route AI, and postwar protectorates. |
| Ancient restorations: `KZR`, `SOG`, `KHW`, `ALN` | Compact symbolic/expansion fork exists but is too short. Add legitimacy, scholar/religious/elite councils, modern survival politics. | River, oasis, pass, toll, bazaar, and workshop projects should be state-targeted. | Heritage guards, toll guards, canal guards, pass guards need templates and defensive missions. | Current claims need war goals, integration, League reactions, and neighbor settlement. | Add restoration legitimacy decisions, capital memory-site missions, postwar integration, AI route limits, and future-event hooks. |

## High-priority parent work

1. Redesign `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` as full crisis trees. `DSC` should receive immediate manpower, core/claim/war logic, undead-style recruitment, and aggressive AI.
2. Add focus-decision integration across all republic and custom splinter routes. The current audit found 0 `activate_decision` and 0 `activate_mission` in focus rewards.
3. Replace repeated helper/stat rewards with route-specific mechanics and fewer, better-timed idea refreshes.
4. Deepen `CFR` into the construction directorate fantasy with large civilian factory output, construction speed, housing authority, and construction-city expansion.
5. Deepen `PRA` into the rail-country fantasy with railway/supply-hub construction, rail sovereignty, transit tolls, rail expansion, and armored-train military play.
6. Deepen `NRF`/`ARD` naval branches with dockyards, convoys, naval infantry, port control, northern sea-lane expansion, and naval AI.
7. Expand `OGB` and the four ancient restoration compact trees into real restoration packages with politics, industry, army, diplomacy, expansion, and postwar handling.
8. After route redesign, rerun asset/icon audit and replace high-frequency repeated icons.

## Validation run

- Brace balance across all four focus files: final depth 0, no early-close depth.
- Unsupported operator scan: no `<=` or `>=` in the four focus files.
- Invalid generic filter scan: no `FOCUS_FILTER_ARMY`, `FOCUS_FILTER_AIR`, or `FOCUS_FILTER_NAVY` remains in the four focus files.
- Focus parser: 41 trees, 1,698 focuses.
- Missing prerequisites: 0.
- Duplicate focus coordinates: 0.
- Parser-detected same-row prerequisite lines: 0 after patch.
- Parser-detected upward prerequisite lines: 0 after patch.
- Missing focus names/descriptions: 0.
- Missing focus icons/sprite definitions: 0.
- Missing `ai_will_do`: 0.
- Missing `completion_reward`: 0.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt` passed.

## Skipped validation

- No HOI4 launch or full external parser run was performed.
- No screenshot validation was performed, so dense curved engine-routed lines still need in-game review after the parent rework.
- No localisation encoding rewrite was performed because localisation files were not edited.
- No commit was created because this is a subagent handoff in a dirty parent worktree.

## Remaining route risks

- The full Soviet Collapse focus rework is not complete. This handoff only patches narrow defects and documents the current route backlog.
- Shallow crisis trees and ancient compact trees remain below the requested full-rework standard.
- Chaos countries are not yet consistently overpowered or mechanically identity-driven.
- Repeated helper rewards still make many branches feel generic.
- Focuses do not yet unlock the decision/mission systems needed for rail expansion, factory projects, dead-army recruitment, naval aggression, restoration integration, or regional postwar handling.

## Handoff path

`docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_all_soviet_collapse_audit_patch_handoff.md`
