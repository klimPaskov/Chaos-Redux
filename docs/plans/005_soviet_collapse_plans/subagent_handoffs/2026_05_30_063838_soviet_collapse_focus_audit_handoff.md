# Event 005 Soviet Collapse Focus Audit Handoff - 2026-05-30 06:38 UTC

Scope:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`, helper idea lifecycle only
- `common/ideas/005_soviet_collapse_ideas.txt`, indirect idea spam trace only

Required references read before target inspection:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: `National focus modding`, `Decision modding`, `Data structures`, `Triggers`, `Effect`, `Modifiers`, `Localisation`, `Scopes`, `AI modding`, `Event modding`, `Idea modding`
- Vanilla docs: `documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`, `common/focus_inlay_windows/documentation.md`
- Vanilla focus precedent inspected via `common/national_focus/china_nationalist.txt` for prerequisites, mutual exclusions, coordinates, and `ai_will_do`.

## Patch Applied

Changed file:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus tree:

- `soviet_collapse_ukraine_focus_tree`

Changed line:

- `common/national_focus/005_soviet_collapse_republics.txt:31`

Before current audit state:

- `continuous_focus_position = { x = 50 y = 2400 }`
- Panel grid approximation was `x ~= 0.5`, `y ~= 18.5`.
- It overlapped late Ukraine layout with `ukr_soviet_collapse_league_security_zone_mandates` at line 1889, `x = 7`, `y = 18`.

After:

- `continuous_focus_position = { x = 3936 y = 180 }`
- Panel grid approximation is `x ~= 41.0`, `y ~= 1.4`.
- Recheck found `risk_count = 0` for the Ukraine continuous panel rectangle.

No localisation keys or icon ids changed.

No commit was created. The worktree was already dirty across Event 005 and Event 006 files, including the touched focus file, so a commit would mix this audit patch with preexisting uncommitted work.

Validation run:

- Brace balance for `common/national_focus/005_soviet_collapse_republics.txt`: `final_depth=0`, `min_depth=0`.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`: passed with no output.
- Continuous panel audit for Ukraine after patch: `risk_count = 0`.

Skipped validation:

- Full game load was not run in this subagent pass.
- No gfx/flag validation was run because the task explicitly said not to touch gfx/flags and no icon references were changed.

## Current Counts

| File | Focus trees | Focus blocks | Notes |
| --- | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 9 | 501 | Ukraine, generic breakaway, internal republics, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan. |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 19 full 47-focus custom splinters plus 6 compact crisis splinters at 18-22 focuses. |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | CFR 47, OGB 23, MFR 58. |
| Total scoped focus files | 37 | 1634 | All counted from current file state. |

Mechanical coverage:

- Missing `ai_will_do`: 0 / 1634.
- Missing `icon`: 0 / 1634.
- Missing `search_filters`: 0 / 1634.
- Missing focus localisation names: 0 / 1634.
- Missing focus localisation descriptions: 0 / 1634.
- Missing focus tree localisation names: 0 / 37.
- Duplicate exact coordinates: 0.
- Same-row adjacent box pairs at distance 0 or 1: 0.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Evidence and notes |
| --- | --- | --- | --- |
| Universal minimum: political, industry, expansion | Most 47+ focus trees have visible political/economy/war/diplomacy/late paths | Partial | Spec requires real branches with mechanical unlocks. Count is high, but many routes still rely on helper variables, state buildings, XP, equipment, stability, and flags instead of direct decisions, units, advisors, templates, war goals, claims, or postwar systems. |
| Ukraine large replayable tree | `soviet_collapse_ukraine_focus_tree`, 83 focuses | Mostly implemented, readability risk | Has democratic/socialist/military/League/foreign/Black Sea/Bread State content. Layout is very dense on rows 6-12; continuous panel was patched. Direct decision unlock count in tree is 7. |
| Belarus rail/forest/corridor/logistics | `soviet_collapse_belarus_focus_tree`, 53 focuses | Mostly implemented | Has rail/forest/corridor/League hooks and 3 direct decision unlocks, but branch density and helper-heavy rewards still need route readability and decision evolution review. |
| Kazakhstan steppe/resource/rail/Central Asian pivot | `soviet_collapse_kazakhstan_focus_tree`, 92 focuses | Implemented, crowded | Strong route count and 4 direct decision unlocks. Row 3 has 11 focuses across `x = 5..25`, creating a high pathline density zone. |
| Compact republic and regional shared trees | breakaway/internal/Baltic/Caucasus/Central Asia/Moldova | Partial to good | Counts range 36-62. Central Asia has 1 claim and 3 decision unlocks. Most map changes are state buildings/resources; direct claims/war goals are rare. |
| Civilian Factory of Russia | `CFR_soviet_collapse_focus_tree`, 47 focuses | Implemented but still needs OP mechanics | Has construction directorate trunk, governance fork, strategy fork, defense, foreign, dark route, expansion, late rebuild. Direct unlocks: 4 decision tooltips, 2 war goals, 4 offsite-building rewards. Missing first-priority hooks: construction capacity decisions beyond static unlocks, worker/labor pressure, consumer burden, and explicit CFR/MFR rivalry or merger outcome. |
| Military Factory of Russia | `MFR_soviet_collapse_focus_tree`, 58 focuses | Implemented but still needs arsenal mechanics | Has production board trunk, route fork, foreign orders, arsenal route, factory rivalry references. Direct unlocks: 3 decision tooltips, 1 war goal, 1 tech bonus. Missing first-priority hooks: production militia/unit or template unlock, proxy arming decisions, explicit CFR rivalry or merger, and more visible arsenal quota decision evolution. |
| Old Great Bulgaria | `OGB_soviet_collapse_focus_tree`, 23 focuses | Shallow/high priority | Has Volga legitimacy and charter choices, 2 war goals, 1 claim, no direct decision unlocks. Spec calls for Volga restoration, historical memory, old-border negotiation, heritage guard, foreign recognition, symbolic vs expansionist path. This tree needs the largest OP/lore-specific upgrade among factory-successor scope. |
| Pale Railway Authority | `PRA_soviet_collapse_focus_tree`, 22 focuses | Compact but better hooked | 11 direct decision unlocks and 1 war goal. Needs first-priority moving-state or rail-sovereignty mechanic depth, rail route missions, and train/railway guard template hooks. |
| Tunguska Star Committee | `TSC_soviet_collapse_focus_tree`, 18 focuses | Shallow/high priority | 1 war goal, no direct decision unlocks found in tree term count. Needs anomaly research decisions, signal-field missions, event/evolution hooks, air or special project style rewards. |
| Dead Soldiers' Congress | `DSC_soviet_collapse_focus_tree`, 18 focuses | Shallow/high priority | 5 direct decision unlocks, 2 war goals, high manpower/equipment rewards. Needs dead-army politics mechanic, veteran/revenant unit or template hooks, memorial legitimacy missions, and recruitment tradeoffs. |
| Iron Commissariat of the Dead | `ICD_soviet_collapse_focus_tree`, 18 focuses | Shallow/high priority | 1 war goal, no direct decision unlocks in term count. Needs death-state command structure, citizen-after-death mechanics, special recruitment, and grim bureaucracy decisions. |
| Northern Revenant Fleet | `NRF_soviet_collapse_focus_tree`, 18 focuses | Shallow/high priority | 4 direct decision unlocks, 1 war goal, heavy navy XP/convoy rewards. Needs fleet/port mechanic, naval militia or revenant-fleet unit hooks, convoy missions, and Arctic port control play. |
| Full 47-focus custom splinters | `FTH/BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC` | Mixed | They have apparent branch families, all local AI weights, and route capstones. Most still need stronger route-specific decision evolution, map claims/cores/settlements, unit/template hooks, and fewer repeated state-building/equipment rewards. |

## Idea Spam and Helper Lifecycle Audit

Direct focus additions:

- Direct `add_ideas` in the three focus files: 0.
- Direct `swap_ideas` in the three focus files: 0.
- Direct `remove_ideas` in the three focus files: 8, all cleanup or rivalry-settlement removals:
  - `PRA_the_board_overrules_ministers`, line 1383, removes `pra_dispatcher_court_tensions`.
  - `TSC_the_committee_of_instruments`, line 1973, removes `tsc_field_station_rivalries`.
  - `RMC_communes_of_witnesses`, line 2408, removes `rmc_credal_cell_rivalries`.
  - `DSC_witness_officers`, line 2899, removes `dsc_grave_regiment_rivalries`.
  - `NRF_living_harbor_committees`, line 3464, removes `nrf_drowned_crew_disputes`.
  - `ICD_commissars_of_last_addresses`, line 3969, removes `icd_grave_commissar_rivalries`.
  - `mrc_protect_village_autonomy`, line 20149, removes `mrc_pass_confederation_rivalries`.
  - `OGB_the_council_takes_the_seal`, factory file line 1199, removes `ogb_disputed_restored_name`.

Indirect helper behavior that can feel like idea spam:

- `soviet_collapse_update_consolidated_republic_ideas` is called from 100 focus reward locations. It starts at `005_soviet_collapse_effects.txt:5485`, calls `soviet_collapse_clear_republic_staged_ideas` at line 5490, and the clear helper removes 48 staged republic ideas at lines 5310-5357. It then adds exactly one first-matching staged idea through one `else_if` chain at lines 5500-5573. This is not direct duplicate adding, but it is large hidden idea churn and it prioritizes local-authority, foreign-support, League, and institution ideas as mutually exclusive display tiers.
- `soviet_collapse_check_republic_recovery` at lines 4387-4422 swaps `soviet_collapse_republican_startup_disorder` to `_mitigated`, then removes startup variants and adds `soviet_collapse_emergency_administration_stabilized` at line 4419. This is an idea lifecycle helper, not focus spam, but repeated focus calls to recovery progress can trigger a visible one-time idea transition.
- `soviet_collapse_apply_custom_splinter_doctrine_identity` is called from 19 doctrine focuses. It starts at line 13229 and contains tag-gated `if = { limit = { tag = ... } }` blocks with `NOT = { has_idea = ... }` guards, so each country can receive only its matching doctrine/internal-faction idea. Static scans see 20 possible `add_ideas`, but runtime should add at most one matching idea per country call.
- Startup helpers still intentionally give multiple starting ideas to high-chaos successors. Examples: `soviet_collapse_setup_cfr_successor` lines 15002-15013 adds `cfr_construction_mandates` and `cfr_housing_ration_boards`; `soviet_collapse_setup_mfr_successor` lines 15019-15030 adds `mfr_arsenal_quotas` and `mfr_factory_guard_state`; `soviet_collapse_setup_pra_successor` lines 15438-15451 adds three PRA ideas. These are starting packages, not focus rewards.
- CFR decision helpers are guarded before adding construction ideas: `soviet_collapse_apply_cfr_survey_unfinished_sites` lines 9656-9662 and `soviet_collapse_apply_cfr_reconstruction_contracts` lines 9669-9675 use `NOT = { has_idea = ... }`.
- MFR decision helpers at lines 10154-10169 add `mfr_arsenal_quotas` and `mfr_factory_guard_state` without visible `has_idea` guards. These are decision helpers, outside direct focus reward scope, but they are likely the next idea-spam cleanup candidate if the decisions are repeatable.

Conclusion:

- No scoped focus is directly adding the same idea multiple times.
- The perceived spam comes from broad hidden staged-idea clearing and re-adding in `soviet_collapse_update_consolidated_republic_ideas`, startup packages, and a few decision helpers. Focus hovers are mostly protected by hidden effects and custom tooltips.

## Missing or Simplified Content

High-priority design gaps:

- `OGB_soviet_collapse_focus_tree`: 23 focuses is too shallow for an OP restored historical-memory successor. It needs a Volga legitimacy mechanic with decisions, heritage guard units, old-border claim arbitration, Idel-Ural negotiation or rivalry decisions, recognition route, and symbolic-vs-expansionist settlement route.
- `PRA/TSC/DSC/NRF/ICD`: compact crisis trees have 18-22 focuses. PRA has good decision unlock count, but TSC, ICD, DSC, and NRF still need special mechanics and unit/template hooks to match their concepts.
- `CFR/MFR`: large enough, but the OP identity is still underconnected. First hooks should be existing decision-category upgrades, explicit CFR/MFR rivalry/merger checks, route-specific costs, and unit/template or offsite capacity mechanics where appropriate.
- Full custom splinters have 47-focus bodies but many rewards still read as repeated state buildings, equipment, XP, variables, and flags. Direct claims, cores, postwar settlement, advisor/leader, and unit/template hooks are sparse in the scoped term counts.
- Direct decision unlocks are uneven. PRA has 11, Ukraine has 7, Kazakhstan has 4, CFR has 4, MFR has 3, DSC has 5, NRF has 4, while several compact or full custom trees have none in direct focus reward term counts.

## OP/Lore-Specific Upgrade Queue

| Tag/tree | Urgency | First concrete hooks to add |
| --- | --- | --- |
| `OGB` | Critical | Volga legitimacy decision category; heritage guard template; old-border arbitration missions; Idel-Ural compact/rivalry branch; recognition vs conquest capstone. |
| `TSC` | Critical | Anomaly research value; signal station decisions; event/evolution incident hook; air/radar or special-project flavored rewards; containment-vs-revelation route. |
| `ICD` | Critical | Dead citizen registry mechanic; special recruitment or template; commissariat obedience value; grave-roll decisions; stability/manpower tradeoff. |
| `DSC` | High | Dead-army politics value; veteran council decisions; memorial front missions; revenant/veteran unit hook; postwar remembrance or conquest settlement. |
| `NRF` | High | Fleet/port authority value; convoy ghost-route missions; naval militia/template or ship/convoy generation hook; Arctic port control decisions. |
| `PRA` | High | Moving-state rail authority meter; train/railway guard template; rail corridor missions; rolling-stock costs; route mobility decisions. |
| `CFR` | High | Construction capacity projects; housing/labor pressure; consumer burden; foreign contract debt; explicit MFR rivalry/merger decision or focus hook. |
| `MFR` | High | Arsenal quotas as visible decision loop; production militias/template; proxy arming decisions; armored train/depot route hooks; explicit CFR rivalry/merger decision or focus hook. |
| `FTH/BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC` | Medium | Replace repeated generic rewards with route-specific decision evolution, claims/cores/settlements, advisor or commander hooks, and route-aware AI strategy plans. |

## Layout Audit

Patched:

- `soviet_collapse_ukraine_focus_tree`, line 31: continuous focus panel moved from current-state `x = 50 y = 2400` to `x = 3936 y = 180`. The old position overlapped `ukr_soviet_collapse_league_security_zone_mandates`, line 1889, `x = 7`, `y = 18`.

Exact high-priority same-row crowding clusters, distance 2 between adjacent focuses:

- `soviet_collapse_ukraine_focus_tree`, row `y = 7`: ten focuses from `x = 16` through `x = 34`, including `ukr_soviet_collapse_coalition_of_three_ministries` line 826, `ukr_soviet_collapse_peasant_socialist_congress` line 345, `ukr_soviet_collapse_black_banner_compact` line 267, and `ukr_soviet_collapse_protectorate_debate` line 1708.
- `soviet_collapse_kazakhstan_focus_tree`, row `y = 3`: eleven focuses from `x = 5` through `x = 25`, including `kaz_soviet_collapse_the_steppe_cannot_be_encircled` line 11276, `kaz_soviet_collapse_oasis_and_steppe_congress` line 10477, and `kaz_soviet_collapse_a_state_across_distances` line 10355.
- `FTH_soviet_collapse_focus_tree`, row `y = 10`: nine focuses from `x = 0` through `x = 16`, including `FTH_tachanka_front` line 957, `FTH_hidden_workshop_cells` line 801, and `FTH_crimean_port_whispers` line 626.
- `soviet_collapse_baltic_focus_tree`, row `y = 2`: seven focuses from `x = 2` through `x = 14`, lines 5166, 4711, 5210, 5187, 5365, 5126, 5246.
- `soviet_collapse_caucasus_focus_tree`, row `y = 4`: eight focuses from `x = 0` through `x = 12`, plus a second tight cluster at `x = 22..26`.
- `soviet_collapse_moldova_focus_tree`, row `y = 6`: six focuses from `x = 16` through `x = 26`.

Exact mutually exclusive same-row pathline risks:

- `OGB_scholars_guard_the_charter`, line 1214, `x = 4 y = 3`, vs `OGB_clerics_guard_the_charter`, line 1234, `x = 6 y = 3`.
- `OGB_treat_with_idel_ural`, line 1460, `x = 12 y = 4`, vs `OGB_the_volga_cannot_have_two_seals`, line 1495, `x = 14 y = 4`.
- `IUL_settlement`, line 21278, `x = 7 y = 7`, vs `IUL_radical_turn`, line 21311, `x = 5 y = 7`.
- `BAC_settlement`, line 22432, `x = 6 y = 7`, vs `BAC_radical_turn`, line 22463, `x = 4 y = 7`.

Exact wide mutually exclusive same-row pathline risks:

- `CFR_elect_the_site_committees`, line 137, `x = 2 y = 5`, vs `CFR_the_concrete_committee`, line 233, `x = 26 y = 5`, `dx = 24`.
- `CFR_publish_the_planners_charter`, line 170, `x = 7 y = 5`, vs `CFR_the_concrete_committee`, line 233, `x = 26 y = 5`, `dx = 19`.
- `CFR_rails_first`, line 397, `x = 8 y = 9`, vs `CFR_contracts_first`, line 473, `x = 22 y = 9`, `dx = 14`.
- `MFR_officers_chair_the_board`, line 1844, `x = 2 y = 6`, vs `MFR_armorers_elect_delegates`, line 1875, `x = 12 y = 6`, `dx = 10`.
- `MFR_officers_chair_the_board`, line 1844, `x = 2 y = 6`, vs `MFR_merchants_of_ammunition`, line 1905, `x = 24 y = 6`, `dx = 22`.
- `MFR_armorers_elect_delegates`, line 1875, `x = 12 y = 6`, vs `MFR_merchants_of_ammunition`, line 1905, `x = 24 y = 6`, `dx = 12`.

Exact OR-prerequisite pathline risks to review:

- `CFR_apartment_blocks_for_loyalty`, line 505, `x = 5 y = 10`, OR-parents `CFR_cities_first` line 363, `x = 3 y = 8`, and `CFR_rails_first` line 397, `x = 8 y = 9`; parents are mutually exclusive.
- `CFR_the_debt_map`, line 641, `x = 20 y = 11`, OR-parents `CFR_client_city_charters` line 567, `x = 20 y = 10`, and `CFR_the_concrete_republic` line 862, `x = 28 y = 9`; `dx = 8`.
- `CFR_buy_peace_with_concrete`, line 902, `x = 16 y = 14`, OR-parents `CFR_the_state_that_builds` line 881, `x = 18 y = 13`, and `CFR_the_first_new_district` line 587, `x = 5 y = 11`; `dx = 13`.
- `MFR_artillery_from_broken_foundries`, line 2090, `x = 4 y = 10`, OR-parents `MFR_factory_war_cabinet` line 2071, `x = 13 y = 8`, and `MFR_military_accounting_courts` line 1974, `x = 2 y = 7`; `dx = 11`.
- `FEV_endgame`, line 17318, `x = 10 y = 13`, has nine OR-parents spanning `x = 0..16`, `y = 7..12`.
- `SZA_endgame`, line 18498, `x = 10 y = 15`, has nine OR-parents spanning `x = 2..16`, `y = 7..14`.
- `BAC_endgame`, line 23187, `x = 8 y = 18`, has six OR-parents spanning `x = 0..14`, `y = 11..17`.
- `ARD_endgame`, line 24386, `x = 8 y = 18`, has six OR-parents spanning `x = 0..12`, `y = 11..17`.

## Icon Coverage

| Metric | Count | Notes |
| --- | ---: | --- |
| Focuses with icon assignment | 1634 / 1634 | No missing `icon =` in scoped files. |
| Unique icon ids | 1456 | Good raw coverage, but not one unique icon per focus. |
| Reused icon ids | 132 | Spec says every focus must have a unique icon assignment; current state still has repeated icon ids. |

Highest repeated icon ids:

- `GFX_focus_soviet_collapse_guard_the_radio_stations`: 4 uses, including `ukr_soviet_collapse_guard_the_telegraph_house` line 54 and `soviet_collapse_guard_the_radio_stations` line 2385.
- `GFX_ukr_soviet_collapse_democratic`: 4 uses, including lines 312, 826, 957, 978.
- `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`: 4 uses, lines 6600, 6801, 7263, 7286.
- `GFX_moldova_soviet_collapse_ukrainian_corridor`: 4 uses, lines 7881, 8023, 8342, 8368.
- `GFX_focus_FEV_diplomatic_plan`: 4 uses, lines 16867, 17005, 17084, 17289.
- `GFX_focus_SZA_diplomatic_plan`: 4 uses, lines 18032, 18166, 18245, 18469.
- `GFX_focus_MRC_civil_rule`: 4 uses, lines 19975, 20124, 20223, 20456.
- `GFX_focus_MRC_foreign`: 4 uses, lines 20044, 20067, 20683, 20733.
- `GFX_focus_IUL_supply`: 4 uses, lines 21176, 21376, 21694, 21906.
- `GFX_focus_IUL_war_plan`: 4 uses, lines 21487, 21621, 21821, 21938.

I did not patch icons because the user explicitly said not to touch gfx/flags, and replacing icon ids without registered sprites would be unsafe.

## Localisation and Reward Mismatches

- Missing focus localisation names/descriptions: 0.
- Missing focus tree localisation names: 0.
- Direct name/reward mismatch candidates are mostly not missing loc, but mechanical overpromises:
  - `TSC` names imply strange science/myth, but tree term count shows only 18 focuses, 1 war goal, no direct decision unlocks, and no event/special-project style hook in direct focus rewards.
  - `ICD` names imply death-state bureaucracy, but direct term count shows 18 focuses, 1 war goal, no decision unlocks, no unit/template hook.
  - `NRF` names imply fleet identity, but direct rewards heavily use navy XP/convoy/equipment terms and only 4 decision unlocks; no ship/fleet or naval militia hook was found in direct focus rewards.
  - `OGB` names imply historical restoration and Volga statecraft, but the tree has 23 focuses, no direct decision unlocks, 2 war goals, and 1 claim. It needs restoration decisions before the localisation and gameplay fully align.

## AI Behavior Gaps

- All scoped focuses have `ai_will_do`.
- The gap is route-aware strategy, not missing `ai_will_do`. Most trees use local focus weights and campaign-state modifiers, but the audit did not find a route-level AI strategy plan surface in the scoped focus files.
- CFR/MFR/OGB/PRA/TSC/DSC/ICD/NRF need AI behavior tied to their special mechanics once those mechanics are deepened. Example: CFR should choose construction routes based on labor pressure, mandates, MFR rivalry, and foreign debt; MFR should choose arsenal/client routes based on quota capacity and war pressure; NRF should prioritize fleet/port routes if it controls Arctic ports.
- Invalid-route handling should be rechecked after any layout or prerequisite rewrite, especially OR prerequisites that cross wide or mutually exclusive parent paths.

## High-Priority Fixes First

1. Deepen `OGB_soviet_collapse_focus_tree` with restoration decisions and heritage guard/unit hooks.
2. Add special mechanics to `TSC`, `ICD`, `DSC`, `NRF`, and `PRA` before further cosmetic/layout polish.
3. Add explicit CFR/MFR rivalry or merger hooks and decision evolution.
4. Replace or supplement generic 47-focus custom splinter rewards with direct decisions, missions, claims/cores/settlements, unit/template hooks, advisors, leaders, or event hooks.
5. Resolve same-row and wide mutual-exclusion pathline risks in CFR, MFR, OGB, IUL, and BAC.
6. Audit repeated focus icon ids against available registered sprites; do not change gfx/flags until sprite definitions exist.
7. Consider converting staged republic idea display into clearer category-specific ideas or dynamic localisation if the current single `else_if` display priority hides important simultaneous state.

## Remaining Route Risks

- The scoped files are not broken by missing icons, filters, AI blocks, or localisation, but several trees still risk feeling shallow because reward variety and direct mechanical hooks lag behind focus count.
- Current staged-idea helper behavior may suppress lower-priority displayed ideas because local authority, foreign support, League coordination, and institutions are in one `else_if` chain.
- Some compact crisis trees may be acceptable as crisis trees only if explicitly documented; otherwise they fall short of the universal branch-depth standard.
- Existing uncommitted work in the repository means this handoff is a current-state audit, not a clean baseline diff against `HEAD`.

## Handoff Path

This handoff is the plan/audit handoff:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_063838_soviet_collapse_focus_audit_handoff.md`
