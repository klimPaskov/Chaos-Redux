# Event005 Focus Tree Pathline And Prerequisite Audit

Timestamp: 2026-06-06 05:48 UTC

Role: `chaosx_focus_tree_auditor`

Scope: Event005 Soviet Collapse focus trees, with priority on pathline/prerequisite mismatches, focuses sitting on path lines, nonsensical visual branch joins, and compact/clean route alignment. Ukraine was inspected first, but no Ukraine patch was made because the parent owns `common/national_focus/005_soviet_collapse_republics.txt`.

## References Consulted

- Repo rules: `AGENTS.md`
- Skills: `hoi4-focus-trees`, `chaos-redux-subagents`
- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`
- Vanilla focus precedent scan: `~/projects/Hearts of Iron IV/common/national_focus/`

Key rules used:

- Multiple focuses inside one `prerequisite = { ... }` block are OR.
- Multiple `prerequisite = { ... }` blocks are AND.
- The national focus wiki warns that the prerequisite should be visually above the dependent focus; otherwise path sprites and line generation can be wrong.
- Duplicate focus coordinates and focus-on-line cases should be treated as layout defects unless an `allow_branch`/conditional layout system hides one side. `available` does not hide a focus.

## Files Inspected

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Existing current-state docs under `docs/plans/005_soviet_collapse_plans/`

## Files Changed

- Added this handoff only:
  - `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_06_054840_focus_tree_pathline_prereq_audit.md`

No gameplay, localisation, gfx, flag, or asset files were edited.

## High-Confidence Issues

### Ukraine, Parent-Owned

These are current in `common/national_focus/005_soviet_collapse_republics.txt`. I did not patch them.

| File | Focus id | Current x/y | Current prerequisite(s) | Expected visual/logical parent | Suggested patch |
| --- | --- | ---: | --- | --- | --- |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_german_liaison_question` | `30/6` | `ukr_soviet_collapse_foreign_courts_notice_kyiv` | Scripted parent is plausible, but the focus sits directly on the diagonal path from `ukr_soviet_collapse_black_sea_port_ledgers` (`31/5`) to `ukr_soviet_collapse_romanian_port_route` (`29/7`). | Keep prerequisite if diplomacy parent is intended; move the focus off that diagonal, e.g. to a clean German-liaison side lane, or move the Black Sea/Romanian lane so no pathline passes through it. |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_advisers_without_flags` | `29/8` | `ukr_soviet_collapse_open_the_liaison_offices` | Scripted parent is `open_the_liaison_offices`, but visible position is directly between `ukr_soviet_collapse_romanian_port_route` (`29/7`) and `ukr_soviet_collapse_anatolian_grain_mission` (`29/9`). | Move `advisers_without_flags` off the Romanian/Anatolian vertical path, or if it is meant to be part of that Black Sea chain, change the prerequisite to match that route deliberately. |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_anatolian_grain_mission` | `29/9` | `ukr_soviet_collapse_romanian_port_route` | Logical Black Sea parent is correct, but current pathline is blocked by `ukr_soviet_collapse_advisers_without_flags` at `29/8`. | Coordinate with the previous row. The cleanest patch is to move `advisers_without_flags`, not to add mutual exclusions. |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_war_without_a_declaration` | `21/4` | `ukr_soviet_collapse_first_republican_line` | Visible closest parent is `ukr_soviet_collapse_depot_motor_columns` at `21/3`; the scripted parent is offset left/up. | Parent should review intent. If this is an emergency military continuation, move it under `first_republican_line` or change prerequisite to the depot lane only if the gameplay chain should actually depend on depot motorization. |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_workers_congress_in_kharkiv` | `17/8` | `ukr_soviet_collapse_socialist_republic_without_moscow` | Visible closest parent is `ukr_soviet_collapse_peasant_socialist_congress` at `17/7`. | Parent should either move it back under the socialist route parent or make the peasant congress the prerequisite if the visible ladder is intended. |

### Belarus, Parent-Owned

These are hard layout defects in `common/national_focus/005_soviet_collapse_republics.txt`.

| File | Focus id | Current x/y | Current prerequisite(s) | Expected visual/logical parent | Suggested patch |
| --- | --- | ---: | --- | --- | --- |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_seal_the_minsk_junction` | `6/4` | `blr_soviet_collapse_the_rail_map_on_the_wall` | It shares exact coordinates with `blr_soviet_collapse_foreign_aid_through_brest`. Its `available` block suggests it is a rail/corridor convergence after `nationalize_the_rail_schedules` or `the_corridor_everyone_wants`. | Move one of the overlapping focuses. Prefer keeping Minsk near the rail lane and moving Brest under `western_corridor_switchmen`, rather than adding mutual exclusions. |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_foreign_aid_through_brest` | `6/4` | `blr_soviet_collapse_western_corridor_switchmen` | Expected visual parent is `western_corridor_switchmen` at `10/2`, but it overlaps the Minsk focus at `6/4`. | Move to a Brest/corridor lane, e.g. under x around `10`, and shift dependent Brest nodes with it. |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_timetable_state` | `6/5` | `blr_soviet_collapse_eastern_line_watch` | It is visually below `seal_the_minsk_junction`, while the scripted parent is `eastern_line_watch` at `12/2`. | Move under the eastern line watch branch or change the prerequisite only if timetable state is meant to follow the Minsk junction. Current line placement creates downstream pathline collisions. |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_brest_is_not_a_gift` | `6/6` | `blr_soviet_collapse_foreign_aid_through_brest` | Current parent is correct for the Brest route, but the focus sits directly on the vertical path from `timetable_state` (`6/5`) to `minsk_central_dispatch` (`6/7`). | Move with the Brest lane after relocating `foreign_aid_through_brest`; do not solve by adding a mutex. |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_minsk_central_dispatch` | `6/7` | `blr_soviet_collapse_timetable_state` | Parent is visually vertical, but `brest_is_not_a_gift` sits between parent and child. | After moving the Brest lane, keep this as a clean timetable vertical chain or move it with `timetable_state` if the eastern route is restored. |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_league_supply_timetables` | `10/9` | `blr_soviet_collapse_timetable_state` | The focus sits on the diagonal line from `timetable_state` (`6/5`) to `prepare_league_freight_tables` (`12/11`). | Move it one column off the diagonal or revise the league freight route row after the timetable/Brest cleanup. |

### Kazakhstan, Parent-Owned

These are exact coordinate collisions in `common/national_focus/005_soviet_collapse_republics.txt`.

| File | Focus id | Current x/y | Current prerequisite(s) | Expected visual/logical parent | Suggested patch |
| --- | --- | ---: | --- | --- | --- |
| `005_soviet_collapse_republics.txt` | `kaz_soviet_collapse_the_alash_courts` | `26/4` | `kaz_soviet_collapse_alash_memory_restored` | Alash legal branch, but shares exact coordinates with the resource-town focus. | Separate the Alash and resource lanes. Move one focus and preserve its current prerequisite unless route intent changes. |
| `005_soviet_collapse_republics.txt` | `kaz_soviet_collapse_the_resource_towns_demand_seats` | `26/4` | `kaz_soviet_collapse_resource_defense_directorate` | Resource-town branch, but overlaps `kaz_soviet_collapse_the_alash_courts`. | Move to a resource branch column under or near `resource_defense_directorate`; avoid a visual merge with Alash. |
| `005_soviet_collapse_republics.txt` | `kaz_soviet_collapse_foreign_trucks_local_drivers` | `16/7` | `kaz_soviet_collapse_foreign_technical_missions` | Foreign technical branch, but shares exact coordinates with `emergency_oil_boards`. | Separate foreign and oil-security lanes. Keep the foreign prerequisite if this is still a technical mission continuation. |
| `005_soviet_collapse_republics.txt` | `kaz_soviet_collapse_emergency_oil_boards` | `16/7` | `kaz_soviet_collapse_oil_field_protection_orders` | Oil-security branch, but overlaps `foreign_trucks_local_drivers`. | Move under the oil/security line or shift the foreign-truck node; no mutual exclusion needed. |
| `005_soviet_collapse_republics.txt` | `kaz_soviet_collapse_army_of_the_open_horizon` | `2/7` | `kaz_soviet_collapse_airstrips_on_the_steppe` | Military/airstrip branch, but shares exact coordinates with `uzbek_supply_delegates`. | Separate the military end node from the southern-congress delegate row. |
| `005_soviet_collapse_republics.txt` | `kaz_soviet_collapse_uzbek_supply_delegates` | `2/7` | `kaz_soviet_collapse_call_the_steppe_congress` | Southern-congress delegate row, but overlaps the military end node. | Move the delegate row or the military node so `call_the_steppe_congress` children read as a clean row. |

### Other Republican Trees, Parent-Owned

| File | Focus id | Current x/y | Current prerequisite(s) | Expected visual/logical parent | Suggested patch |
| --- | --- | ---: | --- | --- | --- |
| `005_soviet_collapse_republics.txt` | `internal_soviet_collapse_sevastopol_road_watch` | `17/6` | `internal_soviet_collapse_crimean_tatar_councils` | Crimea-specific lane. | Shares exact coordinates with `internal_soviet_collapse_lena_baikal_relay_posts`. Because `available` does not hide either focus, move one lane. |
| `005_soviet_collapse_republics.txt` | `internal_soviet_collapse_lena_baikal_relay_posts` | `17/6` | `internal_soviet_collapse_taiga_steppe_self_rule` | Lena/Baikal lane. | Move away from the Crimea-specific focus; use `allow_branch` only if the tree is intended to hide tag-specific lanes, otherwise just separate coordinates. |
| `005_soviet_collapse_republics.txt` | `caucasus_soviet_collapse_council_of_passes` | `12/4` | `caucasus_soviet_collapse_mountain_federal_compact` | Mountain federal/pass branch. | Shares exact coordinates with the oilfield-security compact. Move one to keep mountain and oil/security lanes distinct. |
| `005_soviet_collapse_republics.txt` | `caucasus_soviet_collapse_oilfield_security_compacts` | `12/4` | `caucasus_soviet_collapse_pipeline_guard_corps` OR `caucasus_soviet_collapse_oil_emergency_directorate` | Oilfield/security branch. | Move under the pipeline/oil branch. Do not add mutual exclusion just to untangle the line. |

### Custom Splinter Tree

| File | Focus id | Current x/y | Current prerequisite(s) | Expected visual/logical parent | Suggested patch |
| --- | --- | ---: | --- | --- | --- |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_stanitsa_autonomy_statute` | `8/8` | `DHC_settlement`; `available` requires `DHC_convoy_autonomy_guarantees` | It sits on the line from `DHC_stanitsa_mediation` (`6/6`) to `DHC_convoy_autonomy_guarantees` (`11/11`). | Move off that diagonal or make it a deliberate child of `DHC_convoy_autonomy_guarantees` if that is the real logical parent. Current scripted prerequisite and available gate disagree visually. |

### Ancient Restoration Trees

These are outside Ukraine and look mechanically high confidence, but I left them read-only because changing them affects whether the charter requirement is presented as a pathline or as an availability gate.

| File | Focus id | Current x/y | Current prerequisite(s) | Expected visual/logical parent | Suggested patch |
| --- | --- | ---: | --- | --- | --- |
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_returned_names_endgame` | `10/8` | `KZR_khazar_charter`; `available` requires flag from `KZR_expansionist_steppe_levy` | Visually sits under `KZR_expansionist_steppe_levy` at `10/6`, while the visible pathline comes from the charter at `7/7`. | If parent wants clean route lines, make the prerequisite `KZR_expansionist_steppe_levy` and keep `KZR_khazar_charter` as an `available` requirement or a second explicit prerequisite depending on desired tooltip/pathline behavior. |
| `005_soviet_collapse_ancient_restorations.txt` | `SOG_returned_names_endgame` | `10/8` | `SOG_sogdian_city_charter`; `available` requires flag from `SOG_expansionist_merchant_claims` | Visually sits under `SOG_expansionist_merchant_claims` at `10/6`. | Same pattern as KZR: align the visible parent with the expansionist route while preserving charter requirement explicitly. |
| `005_soviet_collapse_ancient_restorations.txt` | `KHW_returned_names_endgame` | `10/8` | `KHW_khwarazmian_water_charter`; `available` requires flag from `KHW_expansionist_water_claims` | Visually sits under `KHW_expansionist_water_claims` at `10/6`. | Same pattern as KZR. |
| `005_soviet_collapse_ancient_restorations.txt` | `ALN_returned_names_endgame` | `10/8` | `ALN_alan_pass_charter`; `available` requires flag from `ALN_expansionist_mountain_claims` | Visually sits under `ALN_expansionist_mountain_claims` at `10/6`. | Same pattern as KZR. |

## Lower-Confidence Candidates Not Reported As Hard Defects

The mechanical scan also found many focuses where the closest focus above them is not their scripted prerequisite. I did not list most of those as hard defects because many are valid convergence nodes, route joins, or compact-row layout choices. The high-confidence list above is limited to exact coordinate overlaps, focus-on-line cases, and route-end nodes whose visual lane clearly disagrees with their prerequisite/availability split.

## Validation Run

Commands and checks run:

- Opened required wiki pages and vanilla docs listed above.
- Parsed all four Event005 focus files for focus ids, x/y, `relative_position_id`, prerequisites, and mutual exclusions.
- Resolved absolute coordinates for 41 focus trees and 1,698 focuses.
- Checked exact coordinate duplicates.
- Checked direct vertical/horizontal/diagonal focus-on-prerequisite-line cases.
- Checked whether any direct focus-on-line case put a prerequisite path through a focus mutually exclusive with either endpoint.
- Manually inspected the high-priority candidates with `nl -ba`.
- `git diff --stat -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs`

Validation results:

- No gameplay files changed by this audit.
- Current parent worktree already has large focus-file diffs before this handoff: four focus files show existing changes in `git diff --stat`.
- Current hard findings from the parser:
  - 6 exact duplicate-coordinate groups in republican trees.
  - 7 focus-on-straight-prerequisite-line cases across current files.
  - 0 direct coordinate-level cases where a prerequisite pathline runs through a mutually exclusive focus.
  - Numerous lower-confidence visual-parent mismatches, filtered down manually.

Skipped validation:

- Did not run the game.
- Did not edit or validate localisation, gfx, flags, or assets.

## Remaining Risk

- The parser uses straight-line checks for pathline hits. HOI4 path generation uses its own sprites and may render some paths differently, but the reported cases are still coordinate-level layout defects or obvious visual conflicts.
- Some suggested fixes may require small follow-on shifts in adjacent branch rows to keep compact layout clean.
- Ukraine issues are deliberately left to the parent because the prompt reserved local Ukraine patching for the main agent.
