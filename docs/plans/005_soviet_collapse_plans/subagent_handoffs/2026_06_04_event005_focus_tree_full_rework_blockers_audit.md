# Event005 Soviet Collapse Focus Tree Full-Rework Blockers Audit

Date: 2026-06-04

Subagent role: `chaosx_focus_tree_auditor`

Scope: fresh focused audit of Event005 Soviet Collapse focus trees after the current parent tranche. This handoff covers actionable remaining blockers for a full rework: reward idea/helper spam, layout/pathline blockers, branch-depth gaps, underpowered chaos-country aggression, and focus links to Soviet Collapse mechanics and decisions.

Boundary: no flag files or flag folders were opened, edited, or targeted. `gfx/flags`, `interface/flags`, and flag sprites remained out of scope.

## References Used

- Skill: `hoi4-focus-trees`
- Skill: `hoi4-decisions-missions` for focus-to-decision linkage checks
- Skill: `chaos-redux-events` for Event005 handoff alignment
- Offline wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`
- Vanilla precedents: Chinese focus-decision unlocks, Brazilian expansion/war-goal focuses, vanilla continuous focus positioning
- Event005 focus files:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Related Event005 mechanic files:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
  - `common/decisions/005_soviet_collapse_kazakhstan_route_decisions.txt`
  - `common/decisions/005_soviet_collapse_ukraine_bread_state_decisions.txt`
  - `common/decisions/005_soviet_collapse_moldova_route_decisions.txt`
  - `common/decisions/005_soviet_collapse_central_asia_league_decisions.txt`
  - `common/decisions/005_soviet_collapse_release_visibility_decisions.txt`
  - `common/decisions/categories/005_soviet_collapse_categories.txt`

## Validation Snapshot

- Parsed 1,698 focus blocks across the four Event005 focus files.
- Found no duplicate focus IDs.
- Found no exact duplicate focus coordinates inside individual focus trees.
- Found no `<=` or `>=` operators in the four Event005 focus files.
- No gameplay patch was made in this audit. The remaining problems are broad route-depth and visual-layout passes, not safe one-focus fixes.

## Top Actionable Blockers

### 1. Visible Reward Dumps Still Create Focus Reward Spam

These focuses still expose long visible reward stacks with flags, variables, random-state effects, ideas, pressure effects, or helper calls. They should be collapsed behind route-specific scripted effects plus one or two precise `custom_effect_tooltip` lines, or replaced with fewer, more distinctive rewards.

- `common/national_focus/005_soviet_collapse_republics.txt:7799` - `moldova_soviet_collapse_romanian_aid_without_annexation`
  - Problem: 12 visible top-level reward entries, including flags, temp variables, Moldova route variables, random owned state selection, and Soviet pressure.
  - Rework target: one visible diplomatic/infrastructure tooltip plus hidden helper payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:129` - `KZR_caspian_patrol_letters`
  - Problem: 11 visible reward entries for a 16-focus tree, including variables, random coastal state effects, tech bonus, convoy reward, and command power.
  - Rework target: split into a maritime-security branch follow-up or hide the implementation payload.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:526` - `SOG_scholar_envoy_rooms`
  - Problem: 10 visible reward entries on an envoy/scholar focus; reward density is much higher than the branch depth supports.
  - Rework target: make this a decision/mission unlock or a route-specific diplomatic helper, then move variables and tech bonuses under `hidden_effect`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:945` - `KHW_canal_recognition_letters`
  - Problem: 11 visible reward entries, including canal recognition variables, random infrastructure/building payload, tech bonus, and Soviet pressure.
  - Rework target: separate canal infrastructure payoff from recognition/diplomacy payoff.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1354` - `ALN_mountain_envoy_guarantees`
  - Problem: same visible envoy reward density pattern as SOG/KHW.
  - Rework target: hide implementation payload and give a unique mountain-route diplomatic or defensive decision unlock.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2870` - `DSC_witness_officers`
  - Problem: 10 visible reward entries in a compact 18-focus chaos tree.
  - Rework target: combine with rearguard/supply route mechanics or make it a unique decision unlock.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3921` - `ICD_commissars_of_last_addresses`
  - Problem: 10 visible reward entries in a compact 18-focus chaos tree.
  - Rework target: use a unique police/repression mechanic hook instead of raw visible idea/variable stacking.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1951` - `TSC_the_committee_of_instruments`
  - Problem: 9 visible reward entries in an 18-focus tree, mostly helper and tuning payload.
  - Rework target: hide implementation and add a distinctive instrumentation/equipment decision or production modifier.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2379` - `RMC_communes_of_witnesses`
  - Problem: 9 visible reward entries in an 18-focus tree.
  - Rework target: make the commune payoff visible through a route decision, not a stack of generic helper effects.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:2833` - `MFR_workers_own_the_arsenal`
  - Problem: 9 visible reward entries after recent reward cleanup elsewhere.
  - Rework target: convert the arsenal ownership payoff into a distinctive factory/arsenal mechanic or mission unlock.
- `common/national_focus/005_soviet_collapse_republics.txt:1493` - `ukr_soviet_collapse_league_founding_charter`
- `common/national_focus/005_soviet_collapse_republics.txt:1533` - `ukr_soviet_collapse_league_of_equals`
- `common/national_focus/005_soviet_collapse_republics.txt:1856` - `ukr_soviet_collapse_league_security_zone_mandates`
  - Problem: each has about 9 visible top-level reward entries in the same Ukraine league route space.
  - Rework target: move repeated league setup variables and implementation payload into hidden helper effects, then expose a smaller number of clear diplomatic/security outcomes.

### 2. Helper-Only and Repeated Identical Rewards Remain Too Common

The largest systemic reward problem is repeated visible or near-visible helper-only payoffs. The helpers are useful, but many focuses still feel like thin wrappers around identical route-initialization effects.

Most repeated helpers in focus rewards:

- `soviet_collapse_apply_focus_depot_and_supply_control` - 138 uses
- `soviet_collapse_apply_focus_military_consolidation` - 131 uses
- `soviet_collapse_apply_focus_legal_recognition` - 107 uses
- `soviet_collapse_apply_focus_republican_compact_plan` - 80 uses
- `soviet_collapse_apply_focus_foreign_channel` - 65 uses
- `soviet_collapse_apply_focus_security_supply_plan` - 57 uses
- `soviet_collapse_apply_focus_high_chaos_identity` - 57 uses
- `soviet_collapse_apply_focus_league_preparation` - 51 uses

Top exact helper-only ancient restoration examples:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:29` - `KZR_restore_itil_council`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:42` - `KZR_toll_law_debate`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:56` - `KZR_ferry_house_registers`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:70` - `KZR_caspian_road_markets`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:84` - `KZR_customs_workshop_compact`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:98` - `KZR_volga_toll_guard`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:115` - `KZR_guard_the_crossings`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:440` - `SOG_call_the_sogdian_council`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:453` - `SOG_city_scribe_registers`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:845` - `KHW_restore_the_khwarazm_shah_council`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:858` - `KHW_canal_law_records`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1254` - `ALN_restore_the_alan_war_council`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1267` - `ALN_tower_law_registers`

Rework target: each compact restoration tree needs at least one distinctive route-visible payoff before its terminal branch, such as a canal/toll/crossing decision, a unique defensive mission, or a specific expansion/coring mechanic. Do not leave the player reading only helper-equivalent outcomes.

### 3. Same-Row Prerequisites Create Pathline and Mutex-Icon Risks

There are no exact coordinate duplicates, but several focuses have prerequisites on the same row. In HOI4 focus trees, parents should be above children where possible. These same-row links are likely to draw horizontal or crossing pathlines through adjacent nodes and can make mutex/prerequisite icons sit visually close to focus boxes.

Priority layout blockers:

- `common/national_focus/005_soviet_collapse_republics.txt:914` - `ukr_soviet_collapse_appointed_governors` at `(17,13)`
  - Same-row prerequisite: `ukr_soviet_collapse_the_ukrainian_commune_debate` at `(22,13)`
  - Action: move the child below or split the commune/governor lane vertically.
- `common/national_focus/005_soviet_collapse_republics.txt:1774` - `ukr_soviet_collapse_breadbasket_empire` at `(24,7)`
  - Same-row prerequisite: `ukr_soviet_collapse_direct_national_claims` at `(20,7)`
  - Action: make the national-claims focus parent sit above the empire focus, or move the empire payoff to the next row.
- `common/national_focus/005_soviet_collapse_republics.txt:3834` - `internal_soviet_collapse_sevastopol_road_watch` at `(17,6)`
  - Same-row prerequisite: `internal_soviet_collapse_crimean_tatar_councils` at `(20,6)`
  - Action: give the Crimean route a vertical branch.
- `common/national_focus/005_soviet_collapse_republics.txt:3854` - `internal_soviet_collapse_black_sea_customs_office` at `(19,6)`
  - Same-row prerequisite: `internal_soviet_collapse_crimean_tatar_councils` at `(20,6)`
  - Action: same as above; both children should not sit beside their parent.
- `common/national_focus/005_soviet_collapse_republics.txt:6569` - `central_asia_soviet_collapse_majlis_elections` at `(1,4)`
  - Same-row prerequisite: `central_asia_soviet_collapse_local_republic_council` at `(7,4)`
  - Action: this is a long horizontal link across the route selector. Move `majlis_elections` below the council lane.
- `common/national_focus/005_soviet_collapse_republics.txt:6764` - `central_asia_soviet_collapse_border_commanders` at `(9,4)`
  - Same-row prerequisite: `central_asia_soviet_collapse_military_border_authority` at `(15,4)`
  - Action: move the child below or shift the military lane to prevent route-selector line crossings.
- `common/national_focus/005_soviet_collapse_republics.txt:7342` - `central_asia_soviet_collapse_khwarazm_and_older_names` at `(9,6)`
  - Same-row prerequisite: `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` at `(6,6)`
  - Action: make the historical-name payoff a child below the amnesty focus.
- `common/national_focus/005_soviet_collapse_republics.txt:9436` - `blr_soviet_collapse_swamp_roads_closed` at `(27,9)`
  - Same-row prerequisite: `blr_soviet_collapse_guide_companies` at `(30,9)`
  - Action: move one node vertically after the recent Belarus rail/pathline tranche.
- `common/national_focus/005_soviet_collapse_republics.txt:9962` - `blr_soviet_collapse_the_league_depot_at_minsk` at `(15,14)`
  - Same-row prerequisite: `blr_soviet_collapse_minsk_supplies_the_front` at `(24,14)`
  - Action: this is a very long same-row link and should be treated as a priority pathline cleanup item.

Continuous focus panels:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt` still places many compact-tree panels at `x = 1536`, `x = 1920`, or `x = 2112` with `y = 180`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` uses `continuous_focus_position = { x = 2304 y = 140 }` for each 16-focus restoration tree.
- No exact panel collision was mechanically proven in this audit, but these positions should be rechecked visually during the next coordinate pass, especially for dense 18-focus compact trees and the ancient trees where the panel sits close to the active tree area.

### 4. Several Trees Still Lack Full Political, Industry, and Expansion Branch Depth

The full-rework blocker is not just focus count; it is missing branch identity. Some trees still rely on compact identity chains without enough separate political, industry, military, expansion, and decision-connected play.

Highest priority shallow trees:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - `KZR_soviet_collapse_focus_tree` - 16 focuses
  - `SOG_soviet_collapse_focus_tree` - 16 focuses
  - `KHW_soviet_collapse_focus_tree` - 16 focuses
  - `ALN_soviet_collapse_focus_tree` - 16 focuses
  - Blocker: each tree has a strong concept but currently reads as a short identity/reward track. They need distinct political consolidation, industry/logistics, and expansion/coring branches.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `TSC_soviet_collapse_focus_tree` - 18 focuses
  - `RMC_soviet_collapse_focus_tree` - 18 focuses
  - `DSC_soviet_collapse_focus_tree` - 18 focuses
  - `NRF_soviet_collapse_focus_tree` - 18 focuses
  - `ICD_soviet_collapse_focus_tree` - 18 focuses
  - Blocker: these chaos splinters have compact routes but still lack full national focus depth. DSC and NRF have more mechanics than the count suggests, but their tree surface remains too shallow for full rework completion.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `PRA_soviet_collapse_focus_tree` - 22 focuses
  - Blocker: PRA has stronger decision linkage than most compact trees, but still needs route breadth and industry/expansion separation.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `OGB_soviet_collapse_focus_tree` - 23 focuses
  - Blocker: recent OGB tranches improved identity, but it remains below full political/industry/expansion branch depth.

### 5. Some Chaos Countries Are Still Not Aggressive or Overpowered Enough

The strongest chaos-country helpers exist in `common/scripted_effects/005_soviet_collapse_effects.txt`, including:

- `soviet_collapse_spawn_custom_splinter_assault_columns`
- `soviet_collapse_apply_custom_splinter_expansion_claims`
- `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`

However, several focus trees still do not expose enough direct expansion, coring, war-goal, or assault identity at the focus level.

Top actionable weak examples:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt:8135` - `BBH_enemy_front`
  - Problem: mostly identity helper payload.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:8162` - `BBH_war_plan`
  - Problem: adds war support, command power, variables, and chaos assault plan support, but lacks direct expansion claims, war-goal identity, or assault-column escalation.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:8758` - `BBH_extreme_gate`
  - Problem: gate focus has identity helper but does not visibly escalate the country.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:8816` - `BBH_extreme_path`
  - Problem: high-chaos identity reward without a concrete conquest/coring/war-goal payoff.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:11183` - `UDC_extreme_gate`
  - Problem: identity helper only.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:11213` - `UDC_endgame`
  - Problem: endgame helper completion but limited direct focus-surface aggression.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:11239` - `UDC_extreme_path`
  - Problem: high-chaos identity without enough expansion/coring payoff.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:20656` - `MRC_extreme_gate`
  - Problem: identity helper only.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:20681` - `MRC_no_border_troops_without_council`
  - Problem: defensive/logistics reward, not enough mountain-state aggression.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:20734` - `MRC_extreme_path`
  - Problem: mountain endgame completion without sufficient visible expansion/coring pressure.

Additional trees with low direct expansion/decision surface should be reviewed together: `SDZ`, `DHC`, `KHC`, `SZA`, `UWD`, `BAC`, `KRS`, `GAC`, `IUL`.

Rework target: chaos trees should feel dangerous. Add route-specific claims, coring logic, scripted war-goal preparation, assault-column unlocks, or decision missions that let them snowball. Avoid giving every tree the same high-chaos helper without a country-specific conquest identity.

### 6. Focus Links to Soviet Collapse Decisions and Mechanics Are Uneven

Decision/mechanic linkage is much stronger in Ukraine, PRA, DSC, CFR, OGB, and MFR than in many other trees. Low-link trees need focus rewards that unlock decisions, missions, menu actions, release mechanics, or route-specific collapse systems.

Focus reward decision/mechanic link counts by tree:

- Stronger: Ukraine 14, PRA 14, DSC 11, CFR 8, MFR 7, Belarus 7, Kazakhstan 6, OGB 5
- Moderate/low: Central Asia 4, Moldova 3, ARD 3, internal republic 2, Caucasus 2, BSC 2, TNC 2, ALA 2, ancient restoration trees 2 each
- Critical low-link trees:
  - `soviet_collapse_breakaway_focus_tree` - 0
  - `FTH_soviet_collapse_focus_tree` - 0
  - `BBH_soviet_collapse_focus_tree` - 0
  - `UDC_soviet_collapse_focus_tree` - 0
  - `SDZ_soviet_collapse_focus_tree` - 0
  - `DHC_soviet_collapse_focus_tree` - 0
  - `KHC_soviet_collapse_focus_tree` - 0
  - `SZA_soviet_collapse_focus_tree` - 0
  - `UWD_soviet_collapse_focus_tree` - 0
  - `MRC_soviet_collapse_focus_tree` - 0
  - `BAC_soviet_collapse_focus_tree` - 0
  - `TSC_soviet_collapse_focus_tree` - 1
  - `RMC_soviet_collapse_focus_tree` - 1
  - `ICD_soviet_collapse_focus_tree` - 1
  - `KRS_soviet_collapse_focus_tree` - 1
  - `GAC_soviet_collapse_focus_tree` - 1
  - `FEV_soviet_collapse_focus_tree` - 1
  - `IUL_soviet_collapse_focus_tree` - 1
  - `NLC_soviet_collapse_focus_tree` - 1

Rework target: each full tree should have at least one political unlock, one economic/logistics unlock, and one expansion/security unlock that ties into Event005 decisions or scripted mechanics. Low-link chaos countries should not rely only on passive focus rewards.

## Recommended Parent Priorities

1. Run a coordinated coordinate pass for the nine same-row prerequisite blockers in `005_soviet_collapse_republics.txt`, then visually recheck mutex icons and continuous focus panels.
2. Give low-link chaos countries visible route-specific aggression: claims, coring, war-goal preparation, assault columns, or conquest decisions. Start with `BBH`, `UDC`, `MRC`, `SDZ`, `DHC`, `KHC`, `SZA`, `UWD`, and `BAC`.
3. Expand the 16-to-23 focus compact trees into real political, industry/logistics, and expansion/security branches. Start with the four ancient restoration trees and the 18-focus chaos splinters.
4. Collapse remaining visible reward dumps into hidden helper payloads with clear route-specific player-facing tooltips. Start with `moldova_soviet_collapse_romanian_aid_without_annexation`, the ancient envoy/patrol focuses, `DSC_witness_officers`, `ICD_commissars_of_last_addresses`, and `MFR_workers_own_the_arsenal`.
5. Add decision/mechanic hooks to zero-link and one-link trees so the focus trees are not isolated from Soviet Collapse gameplay.

## Small Patch Status

No focus-tree patch was made. The audit found actionable blockers, but the top issues are broad layout and route-depth problems that should be handled by the parent as coordinated tranches rather than isolated coordinate or reward edits.

## Simplifications, Omissions, and Blockers

- No broad rework was attempted.
- No in-game visual validation was run by this subagent.
- No flag files, flag folders, or flag sprites were inspected.
- Continuous focus panel overlap was not proven mechanically; it remains a visual QA item after the next coordinate pass.
