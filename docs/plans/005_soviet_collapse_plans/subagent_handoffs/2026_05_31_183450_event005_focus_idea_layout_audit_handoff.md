# Event005 Focus Tree Idea Spam and Layout Audit Handoff

Timestamp: 2026-05-31 18:34:50 UTC

## Scope and References

Files inspected:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt` for directly related focus reward helper source
- `common/decisions/005_soviet_collapse_decisions.txt` and `common/decisions/categories/005_soviet_collapse_categories.txt` for directly related decision unlock context
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/005_soviet_collapse_blr_focus_l_english.yml`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `docs/plans/005_soviet_collapse_plans/2026_05_31_parent_focus_release_analysis.md`
- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
- Vanilla precedent: `/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt`

Required references opened before editing:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`

Skills used:

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine emergency survival, democratic Rada, socialist, military directory, industry/grain, Dnieper/Donbas logistics, Black Sea/ports, foreign influence, League leadership, Black Banner, Bread State | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Partial | The branches exist, but repeated helper families dominate rewards: `soviet_collapse_apply_focus_military_consolidation` x9, `soviet_collapse_apply_focus_foreign_channel` x9, `soviet_collapse_apply_focus_socialist_sovereignty` x8. Route names read distinct, but mechanics still converge too often. |
| Belarus rail, forest, corridor, logistics, legal restoration, League logistics, Pale Railway/forest chaos | `soviet_collapse_belarus_focus_tree`, 53 focuses | Partial | Rail/corridor branches exist and are stronger than generic branches, but `soviet_collapse_apply_focus_depot_and_supply_control` x11 and generic legal/security/foreign helpers still carry much of the tree. |
| Kazakhstan steppe emergency, Alash, socialist, military district, resource/rail, southern cascade, Central Asian League, foreign mediation, Basmachi/high-chaos pressure | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses | Partial | Large tree with many branches, but depot/military/league/socialist helper repetition remains heavy: depot x12, military x12, League x10, socialist x9. |
| Baltic legal restoration, coast/forest defense, foreign recognition, Baltic League, exile/underground, anti-puppet, intervention pressure | `soviet_collapse_baltic_focus_tree`, 42 focuses | Partial | Shared tree is adapted by tag-gated focuses, but repeated icons and helper families still make several routes feel similar. |
| Caucasus national council, mountain/border defense, oil/infrastructure, Turkish/Iranian mediation, Caucasus League, loyalist garrison, high-chaos/restoration pressure | `soviet_collapse_caucasus_focus_tree`, 40 focuses | Partial | Distinct regional branch labels exist; rewards still lean on legal/supply/security helpers. |
| Central Asian local council, southern defense, old movement/Basmachi pressure, mediation, cotton/water/rail/pass/resource economy, League, ancient/high-chaos pressure | `soviet_collapse_central_asia_focus_tree`, 45 focuses | Partial | Regional economy exists, but `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` and `GFX_central_asia_soviet_collapse_steppe_federation` each repeat 4 times, and compact route helper use remains generic. |
| Moldova Chisinau council, Dniester defense, Romanian diplomacy, Ukraine settlement, agrarian/river economy, League observers, Dniester chaos | `soviet_collapse_moldova_focus_tree`, 48 focuses | Partial | Route coverage exists, but helper pattern is still generic and `GFX_moldova_soviet_collapse_ukrainian_corridor` repeats 4 times. |
| Internal republic compact meaningful trees | `soviet_collapse_internal_republic_focus_tree`, 62 focuses | Partial | Content exists, but shared rewards and repeated icons make tags less country-specific than required. |
| High-chaos splinters: KRS/FTH/BBH/BSC/RMC/TSC/PRA/DSC/NRF/ICD/UDC/SDZ/GAC and others | `005_soviet_collapse_custom_splinters.txt`, 25 trees | Partial | 47-focus trees have real branches; 18-22 focus actors remain shallow. Dead-state, rail-state, naval-state, and cult actors are more identity-specific than before but still need stronger OP payoffs and route-specific AI. |
| Factory states | `CFR_soviet_collapse_focus_tree` and `MFR_soviet_collapse_focus_tree` | Partial | MFR has 58 focuses and strong arsenal identity. CFR has 47 focuses and strong construction identity, but CFR repeats 11 icon IDs and several construction helpers. |
| Old Great Bulgaria | `OGB_soviet_collapse_focus_tree`, 23 focuses | Shallow | Exists with Volga legitimacy/restoration branches, but 10 standalone small rewards and only 23 focuses leave it under the requested successor depth. |
| Ancient restorations | `KZR`, `SOG`, `KHW`, `ALN` ancient focus trees, 16 focuses each | Shallow | All have compact skeletons and unique icons, but they remain stub-scale compared with the required restoration, legitimacy, army, diplomacy, expansion, and myth routes. |

## Idea Spam and Duplicate Reward Findings

Direct focus-file check:

- No direct `add_ideas =`, `swap_ideas =`, or `add_timed_idea =` was found in the four scoped focus files.
- Direct focus-file idea operations are only hidden cleanup removes:
  - `common/national_focus/005_soviet_collapse_factory_successors.txt:1239` removes `ogb_disputed_restored_name`.
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt:1368`, `1956`, `2386`, `2871`, `3424`, `3926` remove starting rival/tension ideas for PRA, TSC, RMC, DSC, NRF, and ICD.

Current source of idea spam:

- Focuses call shared reward helpers; those helpers add or refresh ideas in `common/scripted_effects/005_soviet_collapse_effects.txt`.
- The broad staged idea cleanup is already partly centralized around `soviet_collapse_clear_republic_staged_ideas` at `common/scripted_effects/005_soviet_collapse_effects.txt:5335`.
- CFR helper ideas are gated with `NOT = { has_idea = ... }`, but several independent helpers can still expose the same institution repeatedly:
  - `soviet_collapse_apply_cfr_survey_unfinished_sites` at `common/scripted_effects/005_soviet_collapse_effects.txt:10168`
  - `soviet_collapse_apply_cfr_seize_idle_construction_queues` at `common/scripted_effects/005_soviet_collapse_effects.txt:10236`
  - `soviet_collapse_apply_cfr_raise_factory_city_belt` at `common/scripted_effects/005_soviet_collapse_effects.txt:10274`
- Returned-name and ancient pressure ideas are similarly gated, but broad helper reuse means focus routes can feel like repeated idea refreshes rather than route-specific institutions:
  - `soviet_collapse_apply_returned_names_open_museum_cabinets` at `common/scripted_effects/005_soviet_collapse_effects.txt:15210`
  - `soviet_collapse_apply_returned_names_recruit_archivists` at `common/scripted_effects/005_soviet_collapse_effects.txt:15227`
  - `soviet_collapse_apply_returned_names_commission_old_banner` at `common/scripted_effects/005_soviet_collapse_effects.txt:15237`

No narrow safe focus-file duplicate idea grant was available to patch because the duplicate/spam behavior is now helper-level design debt, not literal duplicate `add_ideas` lines inside one focus.

## Generic Reward Concentrations

| Tree or tag family | Identifier references | Issue |
| --- | --- | --- |
| Ukraine | `soviet_collapse_ukraine_focus_tree`; helpers `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_foreign_channel`, `soviet_collapse_apply_focus_socialist_sovereignty` | Large route tree, but many distinct route labels converge on the same helper payloads. |
| Belarus | `soviet_collapse_belarus_focus_tree`; helpers `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_security_supply_plan`, `soviet_collapse_apply_focus_foreign_channel` | Rail/corridor flavor exists but still repeats generic route helpers. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree`; helpers `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_league_preparation`, `soviet_collapse_apply_focus_socialist_sovereignty` | Strong focus count but overuses same reward families. |
| Shared republics | `soviet_collapse_breakaway_focus_tree`, `soviet_collapse_baltic_focus_tree`, `soviet_collapse_caucasus_focus_tree`, `soviet_collapse_central_asia_focus_tree`, `soviet_collapse_internal_republic_focus_tree`, `soviet_collapse_moldova_focus_tree` | Multiple regional trees exist, but many route payoffs remain generic legal/military/depot/foreign helper calls. |
| Custom splinter 47-focus trees | `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC` | Branch skeletons are large, but many trees repeat `first_guard`, `stores`, `legitimacy`, `doctrine`, `economy`, `foreign`, `league`, `enemy_front`, and `hidden_doctrine` helper identity patterns. |
| Crisis/high-chaos short trees | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | Some identity hooks exist, but 18-22 focuses still under-deliver compared with the requested OP rail/dead/naval/cult mechanics. |
| Factory/ancient successors | `CFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN` | CFR is strong but repeats icon/reward motifs; OGB and ancient restorations remain shallow. |

Highest standalone-small-reward counts from parser:

- `OGB_soviet_collapse_focus_tree`: 10 focuses with small one-off rewards not offset by helpers/decisions/claims/buildings.
- `BSC_soviet_collapse_focus_tree`: 5.
- `KHC_soviet_collapse_focus_tree`: 4.
- `TNC_soviet_collapse_focus_tree`: 4.
- `soviet_collapse_ukraine_focus_tree`: 4.

## Pathline and Mutual-Exclusion Layout

Parser before patch found same-row mutually-exclusive midpoint collisions:

- `soviet_collapse_ukraine_focus_tree`
  - `ukr_soviet_collapse_elections_under_shellfire` ↔ `ukr_soviet_collapse_officers_above_parties` crossed through `ukr_soviet_collapse_british_caution` at `(11, 5)`.
  - `ukr_soviet_collapse_officers_above_parties` ↔ `ukr_soviet_collapse_protectorate_debate` crossed through `ukr_soviet_collapse_socialist_republic_without_moscow` at `(15, 5)`.
- `soviet_collapse_belarus_focus_tree`
  - `blr_soviet_collapse_socialist_autonomy_without_moscow` ↔ `blr_soviet_collapse_foreign_corridor_administration` crossed through `blr_soviet_collapse_military_transit_directorate` at `(18, 5)`.

Patches made:

- `common/national_focus/005_soviet_collapse_republics.txt`
  - `ukr_soviet_collapse_british_caution`: `x = 11` to `x = 23`.
  - `ukr_soviet_collapse_protectorate_debate`: `x = 21` to `x = 22`.
  - `blr_soviet_collapse_foreign_corridor_administration`: `x = 24` to `x = 25`.

After patch:

- Parser-detected same-row mutually-exclusive midpoint collisions across all four scoped focus files: 0.
- No duplicate same-tree coordinates were detected.

Remaining layout risks:

- Dense same-row pairs remain and need visual review, especially:
  - `soviet_collapse_belarus_focus_tree`: `blr_soviet_collapse_foreign_aid_through_brest` / `blr_soviet_collapse_national_council_of_minsk`.
  - `soviet_collapse_ukraine_focus_tree`: `ukr_soviet_collapse_peasant_socialist_congress` / `ukr_soviet_collapse_coalition_of_three_ministries`, `ukr_soviet_collapse_rural_deputy_bloc` / `ukr_soviet_collapse_workers_congress_in_kharkiv`, `ukr_soviet_collapse_re_register_the_party` / `ukr_soviet_collapse_black_soil_oath`.
- I did not do a full generated layout rewrite. The parser catches midpoint and duplicate-coordinate problems, not every possible in-game spline or symbol overlap.

## Icon Coverage Table

Every parsed focus has an `icon =` assignment. Missing assignments: 0.

| Tree | Focuses | Missing icon assignment | Repeated icon ids | Examples |
| --- | ---: | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | 0 | 4 | `GFX_ukr_soviet_collapse_democratic` x4, `GFX_ukr_soviet_collapse_industry` x3 |
| `soviet_collapse_belarus_focus_tree` | 53 | 0 | 2 | `GFX_blr_soviet_collapse_socialist` x2, `GFX_blr_soviet_collapse_counterintel` x2 |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 0 | 0 | None detected |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 2 | `GFX_focus_soviet_collapse_guard_the_radio_stations` x2 |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 3 | `GFX_baltic_soviet_collapse_wire_rooms` x3 |
| `soviet_collapse_caucasus_focus_tree` | 40 | 0 | 2 | `GFX_caucasus_soviet_collapse_defense_compact` x3 |
| `soviet_collapse_central_asia_focus_tree` | 45 | 0 | 2 | `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards` x4 |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 3 | `GFX_focus_soviet_collapse_steppe_supply_congress` x4 |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 2 | `GFX_moldova_soviet_collapse_ukrainian_corridor` x4 |
| `CFR_soviet_collapse_focus_tree` | 47 | 0 | 11 | `GFX_focus_CFR_municipal_board_elections` x3, `GFX_focus_CFR_concrete_republic` x3 |
| `MFR_soviet_collapse_focus_tree` | 58 | 0 | 0 | None detected |
| `OGB_soviet_collapse_focus_tree` | 23 | 0 | 0 | None detected |
| Ancient trees `KZR`, `SOG`, `KHW`, `ALN` | 64 | 0 | 0 | None detected |
| 47-focus custom splinters | 893 | 0 | Many | Worst examples: `IUL` repeated icon ids 15, `UWD` 15, `FEV` 13, `MRC` 12, `SZA` 12 |
| Short crisis splinters `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` | 112 | 0 | 0 | None detected |

Icon issue summary:

- The major violation is repeated icon use, not missing icon assignment.
- I did not edit GFX, flags, or sprite files per user instruction.

## Localisation and Reward Mismatches

Changed focus localisation keys checked:

- `ukr_soviet_collapse_british_caution` and `_desc` exist in `localisation/english/005_soviet_collapse_l_english.yml`.
- `ukr_soviet_collapse_protectorate_debate` and `_desc` exist in `localisation/english/005_soviet_collapse_l_english.yml`.
- `blr_soviet_collapse_foreign_corridor_administration` and `_desc` exist in `localisation/english/005_soviet_collapse_blr_focus_l_english.yml`.

Reward mismatch risks to parent:

- Ukraine focuses often have strong route names but rely on generic helper payloads: examples include `ukr_soviet_collapse_left_league_delegation`, `ukr_soviet_collapse_arsenal_of_the_league`, `ukr_soviet_collapse_prepare_league_liaison_rooms`, and `ukr_soviet_collapse_league_of_equals`.
- Belarus rail/corridor names are closer to their rewards, but `soviet_collapse_apply_focus_depot_and_supply_control` is still reused so heavily that several branches can feel like repeated depot progress instead of distinct rail sovereignty, forest defense, or corridor diplomacy.
- OGB focus names imply a restored Volga state, but many rewards are still small political power, stability, or variable gains rather than a stronger Volga legitimacy, rival/neighbor settlement, or future-event hook payoff.
- Ancient restoration titles read bespoke, and their helper names are bespoke, but each tree has only 16 focuses. This is a depth mismatch rather than a missing-localisation issue.

## AI Behavior Gaps

- Most focus blocks have `ai_will_do`, but route-aware behavior is shallow in many trees.
- Ukraine political route AI uses some government/stability/pressure checks, but it does not fully coordinate route, expansion, foreign patronage, League, and high-chaos validity.
- Belarus route AI has some war/foreign appetite/depot checks, but rail sovereignty and corridor diplomacy are not yet a coherent AI route plan.
- Kazakhstan has many AI weights, but repeated helper routes do not clearly prioritize steppe, Alash, military district, League, foreign mediation, or Basmachi routes based on campaign state.
- Custom splinters usually have `ai_will_do`, but OP identity behavior is incomplete. Dead-state actors should be more consistently aggressive, PRA should prioritize rail/supply expansion, NRF should prioritize ports/naval pressure, CFR should overbuild civilian industry, and MFR should overbuild arms/guards/proxy wars.
- Broad AI strategy files were not patched in this bounded pass.

## High-Priority Rework Recommendations

1. Replace broad staged idea and generic route helpers with route-specific helper wrappers for Ukraine, Belarus, Kazakhstan, and the top high-chaos actors. Keep the existing centralized idea cleanup, but make focus routes upgrade a small number of institutions instead of repeatedly touching many idea families.
2. Give OP chaos identities larger, visible map rewards:
   - CFR: more civilian factories, infrastructure, building slots, construction decisions, and protectorate/building-city decisions.
   - MFR: more military factories, equipment production, armored train/guard units, and proxy arming.
   - PRA: railways, supply hubs, rail decisions, mobile supply columns, and rail-state expansion.
   - DSC/ICD/RMC: manpower, cores/claims, war goals, aggressive AI strategies, and dead-state expansion decisions.
   - NRF/KRS/ARD: ports, dockyards, naval militia, coastal forts, and naval aggression.
3. Rework OGB and ancient restoration depth before claiming completion. OGB should not stay a 23-focus shallow successor; the ancient trees should not stay 16-focus skeletons if they are intended as meaningful playable countries.
4. Reduce repeated icon IDs in CFR, IUL, UWD, FEV, MRC, SZA, and shared republic trees. This needs asset workflow or approved icon reuse documentation, not a focus-only patch.
5. Keep mutual exclusions only where route identity changes. Several current route locks are meaningful, but repeated generic rewards make some exclusivity feel decorative in practice.
6. After route reward rework, rerun parser layout checks and in-game visual review. Parser collisions are currently clean, but dense same-row clusters remain.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_183450_event005_focus_idea_layout_audit_handoff.md`

Changed focus ids:

- `ukr_soviet_collapse_british_caution`
- `ukr_soviet_collapse_protectorate_debate`
- `blr_soviet_collapse_foreign_corridor_administration`

Localisation keys changed:

- None.

Icon ids changed:

- None.

Route behavior before and after:

- Before: three route/focus coordinates created mutually-exclusive midpoint collisions.
- After: only x-coordinate placement changed. Focus prerequisites, route locks, rewards, AI weights, filters, localisation, and icons are unchanged.

## Validation Run

Passed:

- No unsupported comparison operators in scoped focus files:
  - `rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Brace balance:
  - all four scoped focus files ended at `final_depth=0`, `min_depth=0`, `bad_closes=0`.
- Diff whitespace check for touched focus file:
  - `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`
- Changed-focus localisation presence:
  - `ukr_soviet_collapse_british_caution`, `ukr_soviet_collapse_british_caution_desc`
  - `ukr_soviet_collapse_protectorate_debate`, `ukr_soviet_collapse_protectorate_debate_desc`
  - `blr_soviet_collapse_foreign_corridor_administration`, `blr_soviet_collapse_foreign_corridor_administration_desc`
- Parser layout checks:
  - duplicate same-tree coordinates: 0.
  - same-row mutually-exclusive midpoint collisions: 0.
- Flag asset safety:
  - `git diff --name-only -- gfx/flags` returned empty.

Skipped:

- No in-game focus-tree screenshot validation. This pass used syntax/parser checks only.
- No full missing-localisation scan for all 1,484 parsed focuses; only changed focus ids were checked.
- No sprite/GFX definition validation because gfx, flags, and sprite files were explicitly out of scope.
- No full helper-level idea redesign because this is broad system design debt, not a safe local focus-file patch.

## Remaining Route Risks

- The visible idea spam is not coming from direct focus `add_ideas` lines anymore. Parent should audit helper chains and idea lifecycle design, especially `soviet_collapse_apply_focus_*` and custom splinter identity helpers.
- The user’s requested “focus trees lack depth, lore, purpose, and connection to mechanics” remains true for many trees. This pass only fixed a narrow layout blocker and documented the deeper route debt.
- The current repo already had extensive pre-existing dirty work in Event005 and unrelated Event006 files before this pass. I did not revert or touch unrelated work.

Plan handoff path:

- This file: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_183450_event005_focus_idea_layout_audit_handoff.md`
- No separate improvement plan was written because `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` and `docs/plans/005_soviet_collapse_plans/2026_05_31_parent_focus_release_analysis.md` already cover the broad redesign direction.
