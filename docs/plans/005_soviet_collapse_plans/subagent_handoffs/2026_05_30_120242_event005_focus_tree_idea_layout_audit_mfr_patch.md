# Event 005 Soviet Collapse Focus Tree Idea/Layout Audit And MFR Patch

Timestamp: 2026-05-30 12:02:42 UTC

Subagent role: Chaos Redux focus tree subagent.

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Context files read for mechanics and helper tracing:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `docs/events/005_soviet_collapse.md`
- Existing Event 005 focus handoffs under `docs/plans/005_soviet_collapse_plans/subagent_handoffs/`

References and skills read:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: National focus modding, Decision modding, Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, AI modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla focus examples for `prerequisite`, `mutually_exclusive`, `ai_will_do`, `add_building_construction`, `create_wargoal`, decision unlocks, and claims/cores.

No `gfx/flags`, flag sprite files, generated assets, or image files were touched.

## Patch Applied

Changed file:

- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Changed focus id:

- `MFR_german_orders`

Route behavior before and after:

- Before this pass, `MFR_german_orders` sat at `(24, 10)`. The prerequisite line from `MFR_rifles_against_the_league` at `(26, 8)` to `MFR_german_orders` ran directly through sibling focus `MFR_rifles_for_the_league` at `(25, 9)`.
- After this pass, `MFR_german_orders` is at `(25, 10)`. Rewards, prerequisites, `ai_will_do`, search filters, icon, localisation, and route locks are unchanged.
- Static pathline detector reports `straight_pathline_focus_hits 0` after the patch.

Localisation keys changed: none.

Icon ids changed: none.

## Route Coverage Table

Counts are current-worktree static counts. `Direct hooks` counts focus-level direct appearances of decision/war/core/claim/unit/faction/AI-strategy hooks; many trees also call helper effects, so a zero does not mean no transitive behavior, but it is a route-depth risk.

| Focus tree | Focuses | Direct hooks | Small reward focuses | Multi-helper idea-churn focuses | Route-depth status |
| --- | ---: | ---: | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | 8 | 53 | 0 | Broad branches exist, but political selector geometry and helper-heavy route payoffs remain high risk. |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 21 | 0 | Simplified survival baseline; needs decisions, regional ambitions, and state-targeted mechanics. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 42 | 3 | Broad but generic; compact republic identity is not mechanically distinct enough. |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 20 | 0 | Restoration/port/security themes exist, but direct decision/war/postwar hooks are absent. |
| `soviet_collapse_caucasus_focus_tree` | 40 | 2 | 21 | 0 | Partial mountain/security route surface; needs stronger neighbor and settlement mechanics. |
| `soviet_collapse_central_asia_focus_tree` | 45 | 4 | 28 | 3 | Has some claims/restoration hooks; still helper-heavy and needs postwar/integration depth. |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 31 | 1 | Present but mechanically light for a bridge/river/border state. |
| `soviet_collapse_belarus_focus_tree` | 53 | 3 | 33 | 0 | Rail/forest/corridor routes exist; branch payoffs need more units, missions, and external diplomacy. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 4 | 57 | 1 | Largest republic tree; broad routes exist but resources, federation, cavalry, and oil/rail play are too helper-dependent. |
| `FTH_soviet_collapse_focus_tree` | 47 | 0 | 26 | 3 | Full-size but lacks direct aggressive mechanics. |
| `PRA_soviet_collapse_focus_tree` | 22 | 14 | 19 | 0 | Best compact rail actor; still short for an overpowered railway authority. |
| `TSC_soviet_collapse_focus_tree` | 18 | 2 | 13 | 0 | Shallow crisis tree. |
| `RMC_soviet_collapse_focus_tree` | 18 | 2 | 12 | 0 | Shallow crisis tree. |
| `DSC_soviet_collapse_focus_tree` | 18 | 14 | 14 | 0 | Aggressive hooks exist, but route is still short for Dead Soldiers' Congress ambitions. |
| `NRF_soviet_collapse_focus_tree` | 18 | 9 | 15 | 0 | Naval identity exists but remains compact and small-reward-heavy. |
| `ICD_soviet_collapse_focus_tree` | 18 | 2 | 13 | 0 | Shallow crisis tree. |
| `BSC_soviet_collapse_focus_tree` | 47 | 0 | 28 | 1 | Full-size but direct mechanics absent. |
| `TNC_soviet_collapse_focus_tree` | 47 | 0 | 26 | 1 | Full-size but direct mechanics absent. |
| `ALA_soviet_collapse_focus_tree` | 47 | 0 | 24 | 1 | Full-size but direct mechanics absent. |
| `BBH_soviet_collapse_focus_tree` | 47 | 0 | 25 | 1 | Full-size but direct mechanics absent. |
| `KRS_soviet_collapse_focus_tree` | 47 | 0 | 27 | 2 | Full-size but direct mechanics absent. |
| `UDC_soviet_collapse_focus_tree` | 47 | 0 | 23 | 1 | Full-size but direct mechanics absent. |
| `SDZ_soviet_collapse_focus_tree` | 47 | 0 | 23 | 1 | Full-size but direct mechanics absent. |
| `GAC_soviet_collapse_focus_tree` | 47 | 0 | 25 | 1 | Full-size but direct mechanics absent. |
| `DHC_soviet_collapse_focus_tree` | 47 | 0 | 23 | 1 | Full-size but direct mechanics absent. |
| `KHC_soviet_collapse_focus_tree` | 47 | 0 | 25 | 1 | Full-size but direct mechanics absent. |
| `FEV_soviet_collapse_focus_tree` | 47 | 0 | 22 | 3 | Full-size but direct mechanics absent. |
| `SZA_soviet_collapse_focus_tree` | 47 | 0 | 21 | 3 | Full-size but direct mechanics absent. |
| `UWD_soviet_collapse_focus_tree` | 47 | 0 | 25 | 1 | Full-size but direct mechanics absent. |
| `MRC_soviet_collapse_focus_tree` | 47 | 0 | 24 | 0 | Full-size but direct mechanics absent. |
| `IUL_soviet_collapse_focus_tree` | 47 | 0 | 22 | 3 | Full-size but direct mechanics absent. |
| `BAC_soviet_collapse_focus_tree` | 47 | 0 | 23 | 3 | Full-size but direct mechanics absent. |
| `ARD_soviet_collapse_focus_tree` | 47 | 3 | 28 | 3 | Naval/arctic hooks exist, but route is still too light for the intended OP actor. |
| `NLC_soviet_collapse_focus_tree` | 47 | 0 | 29 | 1 | Full-size but direct mechanics absent. |
| `CFR_soviet_collapse_focus_tree` | 47 | 9 | 19 | 0 | Construction route has strong recent improvements; still needs more decision/mission contracts. |
| `OGB_soviet_collapse_focus_tree` | 23 | 10 | 18 | 0 | Improved with claims/wargoal hooks, but still shallow by high-impact successor standard. |
| `MFR_soviet_collapse_focus_tree` | 58 | 7 | 16 | 0 | Stronger arsenal identity than most; patched one pathline issue in this pass. |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | 6 | 7 | 0 | Compact ancient restoration, not a full route family. |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | 6 | 7 | 0 | Compact ancient restoration, not a full route family. |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | 6 | 7 | 0 | Compact ancient restoration, not a full route family. |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | 6 | 8 | 0 | Compact ancient restoration, not a full route family. |

## Idea Spam Findings

Direct focus idea spam:

- Direct `add_ideas`, `add_timed_idea`, or `swap_ideas` in the four focus files: 0.
- Direct `remove_ideas` in parsed focus rewards: 0. Prior visible `remove_ideas` lines are inside hidden cleanup blocks and were not counted as player-facing idea spam.

Helper-caused idea churn:

- `common/scripted_effects/005_soviet_collapse_effects.txt:5466`, `soviet_collapse_update_consolidated_republic_ideas`, is the main staged-idea updater.
- `common/scripted_effects/005_soviet_collapse_effects.txt:5375`, `soviet_collapse_mark_republic_staged_idea_recently_changed`, now gates staged idea swaps with a timed flag. This prevents repeated swaps inside one country-day, but the focus trees still overuse helper paths that feed the staged idea system.

High-volume helper/call-site sources:

| Helper | Definition | Current focus calls | Issue |
| --- | --- | ---: | --- |
| `soviet_collapse_apply_focus_legal_recognition` | `005_soviet_collapse_effects.txt:8115` | 305 | Generic legality reward drives many staged idea recalculations. |
| `soviet_collapse_apply_focus_depot_and_supply_control` | `005_soviet_collapse_effects.txt:8173` | 258 | Often substitutes for direct rail, supply hub, depot, or mission mechanics. |
| `soviet_collapse_apply_focus_military_consolidation` | `005_soviet_collapse_effects.txt:8151` | 254 | Often substitutes for units, templates, doctrines, or war-plan decisions. |
| `soviet_collapse_apply_focus_league_preparation` | `005_soviet_collapse_effects.txt:8494` | 220 | Often substitutes for League decisions, guarantees, or external war mandates. |
| `soviet_collapse_apply_focus_foreign_channel` | `005_soviet_collapse_effects.txt:9266` | 176 | Often substitutes for sponsor desks, relation work, aid corridors, or diplomatic missions. |
| `soviet_collapse_apply_focus_socialist_sovereignty` | `005_soviet_collapse_effects.txt:8134` | 23 | Smaller but still part of staged-idea churn. |

Exact multi-helper focus call site ids found in this pass:

- `internal_soviet_collapse_volga_ural_compact`, `internal_soviet_collapse_black_sea_compact_observers`, `internal_soviet_collapse_many_republics_common_front`
- `central_asia_soviet_collapse_turkestan_city_congress`, `central_asia_soviet_collapse_the_south_survives_together`, `central_asia_soviet_collapse_desert_republic_settlement`
- `moldova_soviet_collapse_a_small_state_between_larger_maps`
- `kaz_soviet_collapse_the_steppe_outlives_the_union`
- `FTH_diplomatic_plan`, `FTH_communes_without_capitals`, `FTH_endgame`
- `BSC_diplomatic_plan`, `TNC_diplomatic_plan`, `ALA_diplomatic_plan`, `BBH_diplomatic_plan`, `KRS_diplomatic_plan`, `KRS_endgame`
- `UDC_diplomatic_plan`, `SDZ_diplomatic_plan`, `GAC_diplomatic_plan`, `DHC_diplomatic_plan`, `KHC_diplomatic_plan`
- `FEV_diplomatic_plan`, `FEV_authority_from_the_harbor`, `FEV_endgame`
- `SZA_diplomatic_plan`, `SZA_authority_from_the_railhead`, `SZA_endgame`
- `UWD_diplomatic_plan`
- `IUL_volga_ural_endurance`, `IUL_diplomatic_plan`, `IUL_endgame`
- `BAC_diplomatic_plan`, `BAC_amur_commune_endurance`, `BAC_endgame`
- `ARD_diplomatic_plan`, `ARD_arctic_port_endurance`, `ARD_endgame`
- `NLC_diplomatic_plan`

Recommendation: do not remove these helpers blindly. For parent rework, replace high-level helper clusters with direct route mechanics first, then leave a single hidden staged-idea update at route milestones.

## Pathline And Layout Risks

Patched:

- `MFR_rifles_against_the_league` `(26, 8)` to `MFR_german_orders` previously crossed `MFR_rifles_for_the_league` `(25, 9)`. `MFR_german_orders` is now `(25, 10)`.

Current mechanical layout scan after patch:

- Duplicate coordinates by tree: 0.
- Straight prerequisite pathline passing through another focus: 0.
- Same-row prerequisite lines: 0.

Remaining layout risks that require parent-scale route movement:

- Ukraine political selector still has very wide mutual-exclusion geometry around `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, and `ukr_soviet_collapse_protectorate_debate`.
- Belarus rail/forest/League convergence still needs rendered visual review despite passing the straight-line heuristic.
- Kazakhstan remains very wide and branch-dense around the political past/resource/federation families.
- CFR/MFR have many pre-existing route movements in the dirty worktree; this pass only touched `MFR_german_orders`.

## Missing Mechanics By Country/Tree

- Ukraine: broad routes exist, but several major political/Black Sea/grain/League endpoints still depend on helpers instead of visible claims, cores, units, port/naval, or postwar mechanics.
- Breakaway/internal/Baltic/Moldova republics: several trees have 0 direct hooks. Add decisions, missions, regional claims, defensive mandates, supply work, and external diplomacy.
- Belarus: route identity should affect rail authority, forest defense, partisan/regular army missions, Baltic diplomacy, and corridor security.
- Kazakhstan: resource, Alash, socialist, federation, and foreign-patron routes need state-targeted oil/rail/supply mechanics, cavalry or motorized templates, and postwar integration.
- PRA: rail/supply hooks exist; still needs broader overpowered railway state depth.
- DSC: direct aggression exists; should receive more recurring dead-army pressure, coring/integration behavior, and neighbor aggression before being called complete.
- NRF/ARD: naval actors need more ships, ports, dockyards, naval missions, convoy warfare, and coastal expansion mechanics.
- CFR: construction identity is stronger but should gain more contract decision chains, timed construction missions, and regional building mandates.
- MFR: arsenal identity is stronger but should gain more arms export/client-state mechanics and persistent aggression.
- OGB and ancient restorations: still too short unless explicitly scoped as compact restoration actors.
- Most 47-focus custom splinters: route labels exist, but direct mechanics are absent by scan. High-chaos actors should not rely mainly on generic helper stacks.

## Icon Coverage Table

| File | Focus icons | Unique icon ids | Repeated icon groups | Repeated icon uses | Missing sprite defs |
| --- | ---: | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 501 | 458 | 22 | 65 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 885 | 99 | 219 | 0 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 113 | 11 | 26 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 42 | 8 | 30 | 0 |

Repeated icon clusters to prioritize later:

- Republics: `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_ukr_soviet_collapse_democratic`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`.
- Custom splinters: `GFX_focus_FEV_diplomatic_plan`, `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_civil_rule`, `GFX_focus_MRC_foreign`, `GFX_focus_IUL_supply`.
- Factory successors: several CFR construction icons repeat by theme; not broken, but still visually repetitive.
- Ancient restorations: shared restoration icons repeat across all four 16-focus trees.

## Localisation And Reward Mismatch List

Mechanical localisation coverage:

- Focus ids checked: 1,698.
- Missing name keys: 0.
- Missing `_desc` keys: 0.

Reward/localisation mismatch risks:

- Many `*_diplomatic_plan`, `*_industry_plan`, `*_war_plan`, `*_hidden_doctrine`, and `*_endgame` custom splinter focuses imply major route behavior but call broad helper bundles.
- Naval wording in NRF/ARD and Black Sea-adjacent Ukraine should surface ships, ports, dockyards, naval bases, convoy actions, or coastal missions more consistently.
- Rail/supply wording in PRA, Belarus, and several republic trees should surface railways, supply hubs, depot control missions, armored trains, or logistics decisions more consistently.
- Construction wording in CFR should keep moving from abstract construction bonuses toward contract decisions and state-targeted construction missions.
- Dead Soldiers' Congress wording implies direct mass aggression, cores, and war goals. It has some hooks, but its tree length and recurring pressure remain too light.

## AI Behavior Gaps

Mechanical status:

- All 1,698 focuses have `ai_will_do`.

Gaps:

- Many AI blocks remain local focus weights, not route-family strategy.
- High-chaos/custom splinters do not consistently receive persistent `add_ai_strategy` aggression toward neighbors, claims, SOV, ports, rail hubs, or postwar integration targets.
- Ukraine, Belarus, and Kazakhstan route selection needs AI behavior that follows through after political choices instead of only choosing the next weighted focus.
- Naval actors need AI priorities for dockyards, convoy production, naval invasion/raiding, and port defense.
- Rail/supply actors need AI priorities for infrastructure, railways, supply hubs, and armored train or logistics decisions.

## Priority Patch Recommendations

Immediately patchable in later small subagent passes:

1. Remove single focus pathline/layout defects like the MFR coordinate issue patched here.
2. Add missing local decision unlock tooltips where an existing decision is already gated by a focus flag.
3. Add narrow `add_ai_strategy` calls to existing aggressive endpoint focuses when a target and route are already clear.
4. Replace isolated tiny stockpile rewards with existing helper calls for rail authority, mobile columns, field defense, or legal recognition when the focus text already implies that mechanic.
5. Diversify repeated icons only when a specific existing icon id already fits. Do not create or touch image files.

Requires larger parent rework:

1. Ukraine selector/layout and route payoff rework.
2. Belarus rail/forest/corridor decision and pathline pass.
3. Kazakhstan resource/federation/Alash/socialist route mechanic pass.
4. Conversion of 47-focus custom splinter route labels into direct decisions, missions, expansion, coring/integration, and unit templates.
5. OGB and ancient restoration depth expansion or explicit compact-tree classification.
6. System-wide reduction of helper-expanded staged idea churn by moving staged-idea updates to explicit route milestones.

## Validation Run

Commands/checks run:

- Brace balance on all four scoped focus files:
  - `005_soviet_collapse_republics.txt`: opens 4240, closes 4240, final depth 0.
  - `005_soviet_collapse_custom_splinters.txt`: opens 10917, closes 10917, final depth 0.
  - `005_soviet_collapse_factory_successors.txt`: opens 1378, closes 1378, final depth 0.
  - `005_soviet_collapse_ancient_restorations.txt`: opens 610, closes 610, final depth 0.
- Unsupported operator scan across scoped focus files plus Event 005 effects/decisions: no `<=` or `>=`.
- `git diff --check --` scoped focus/effect/decision files: passed.
- Focus sanity:
  - Focus count: 1,698.
  - Tree count: 41.
  - Missing icon assignment: 0.
  - Missing `ai_will_do`: 0.
  - Direct focus `add_ideas`/`add_timed_idea`/`swap_ideas`: 0.
  - Unresolved focus icons against mod and vanilla `.gfx`: 0.
  - Straight pathline focus hits after patch: 0.
- Localisation coverage across Event 005 English localisation: 0 missing focus names, 0 missing focus descriptions.
- `git diff --name-only -- gfx/flags`: empty.

Skipped validation:

- No in-game load, screenshot, or rendered focus-tree validation was run from this subagent environment.
- No flag asset validation was run because flags and image files were explicitly out of scope.
- No commit was created because the worktree was already broadly dirty in Event 005 files; staging this patch would risk bundling parent/subagent changes in the same files.

## Remaining Route Risks

- This is not a full focus-tree rework and should not be treated as completion of the user objective.
- Helper-caused staged idea churn is guarded but still too dense and still creates sameness.
- Many custom splinter and ordinary republic trees remain route-label-heavy rather than mechanic-heavy.
- The MFR pathline patch fixed one concrete layout defect; Ukraine/Belarus/Kazakhstan still need parent-owned rendered layout work.
- Existing broad Event 005 dirty changes in the same files were preserved and not reverted.

