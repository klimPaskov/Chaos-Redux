# Event 005 Soviet Collapse Focus Tree Audit Handoff

Audit timestamp: 2026-06-05 07:18:59 UTC

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Mode: read-only audit. No focus files, gfx, flags, localisation, or gameplay files were patched.

## References Consulted

Repo guidance and skill:
- `AGENTS.md`
- `hoi4-focus-trees` skill: `/home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md`

Offline Paradox wiki snapshot:
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

Vanilla references:
- `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/baltic_shared.txt`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt`

Current Event 005 source specs spot-checked:
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`

## File And Tree Counts

Line counts:
- `common/national_focus/005_soviet_collapse_republics.txt`: 12,187 lines
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: 25,654 lines
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: 2,942 lines
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: 1,641 lines
- Total audited focus script: 42,424 lines

Parsed structure:
- 41 focus trees
- 1,698 focus blocks
- No duplicate focus ids found in the four audited files.
- No duplicate absolute coordinates found after resolving `relative_position_id`.
- No verified continuous focus panel overlap found by the coordinate pass.

Major tree sizes:
- `soviet_collapse_ukraine_focus_tree`: 83 focuses
- `soviet_collapse_kazakhstan_focus_tree`: 92 focuses
- `soviet_collapse_internal_republic_focus_tree`: 62 focuses
- `MFR_soviet_collapse_focus_tree`: 58 focuses
- `soviet_collapse_belarus_focus_tree`: 53 focuses
- `soviet_collapse_moldova_focus_tree`: 48 focuses
- Most custom splinters: 47 focuses each
- `PRA_soviet_collapse_focus_tree`: 22 focuses
- `OGB_soviet_collapse_focus_tree`: 23 focuses
- `TSC`, `RMC`, `DSC`, `NRF`, `ICD`: 18 focuses each
- `KZR`, `SOG`, `KHW`, `ALN`: 16 focuses each

## Top Blockers

1. Visible reward spam remains widespread. The parser found 184 focus reward warnings where rewards visibly expose multiple `soviet_collapse_* = yes` helpers or long raw reward lists without one coherent `custom_effect_tooltip` or `complete_tooltip`.
2. Helper spam is not isolated to old or minor branches. It is systemic in Ukraine, Kazakhstan, internal republics, MFR, CFR, Moldova, Belarus, the regional republic trees, PRA, and many custom splinter trees.
3. Several high-chaos special actors remain shallow by focus count and branch coverage: `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` are 18-focus trees. `PRA` and `OGB` are also compact at 22 and 23 focuses.
4. Most 47-focus custom splinters still read as under-expanded mechanically. Keyword and explicit-mechanic scans flagged weak expansion/diplomacy surfaces in `FTH`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, and `NLC`.
5. `CFR` is not aggressive or overpowered enough for the construction-state identity. Its late branch has construction-state flavor, but major payoffs around lines 820, 841, 883, and 983 are mostly helper-driven and lack explicit visible conquest, protectorate, or border-building mechanics.
6. `MFR` is stronger than `CFR`, but still has mid and late rewards that are helper-only before its explicit final wargoal sequence. It needs cleaner visible reward composition and earlier expansion mechanics.
7. `ICD` is weaker than `DSC` as a dead/zombie-style state. `ICD_claim_the_unburied_front` at line 4247 and `ICD_grave_columns_march` at line 4268 mainly add claims/objective pressure, while comparable `DSC` late branches add broader war and assault payloads.
8. One confirmed pathline/layout issue remains in Kazakhstan: `kaz_soviet_collapse_the_southern_republics_write_together` at `common/national_focus/005_soviet_collapse_republics.txt:11408` sits on the same row as prerequisite `kaz_soviet_collapse_the_steppe_arbitration_court`.
9. Many branches are disconnected from Soviet Collapse mechanics at the visible focus layer. Several trees have zero or very few explicit `unlock_decision_tooltip`, claim/core, wargoal, faction, release, autonomy, or unit-template tokens and rely on generic helper names instead.
10. Ancient restoration trees are intentionally compact but remain too thin for identity depth. `KZR`, `KHW`, and `ALN` are especially weak on industry/mechanic expansion, even if compact trees are acceptable for side actors.

## Reward Spam Findings

The audit treated a focus as spam-risk when `completion_reward` visibly contained:
- multiple scripted-effect helper calls, especially `soviet_collapse_* = yes`;
- a duplicate idea addition;
- a long visible list of raw effects without `custom_effect_tooltip` or `complete_tooltip`;
- helper calls that appear to expose implementation plumbing instead of a coherent player reward.

No duplicate same-idea additions were found by the parser, but helper spam and long visible reward lists are widespread.

Representative high-priority examples:
- `common/national_focus/005_soviet_collapse_republics.txt:97`, `ukr_soviet_collapse_seal_the_grain_ledgers`: exposes `soviet_collapse_ensure_emergency_equipment_variants` and `soviet_collapse_apply_focus_depot_and_supply_control`.
- `common/national_focus/005_soviet_collapse_republics.txt:120`, `ukr_soviet_collapse_count_the_depot_keys`: exposes equipment and rail authority helper calls.
- `common/national_focus/005_soviet_collapse_republics.txt:473`, `ukr_soviet_collapse_the_ukrainian_commune_debate`: long reward surface plus multiple helper calls, including socialist sovereignty and objective pressure helpers.
- `common/national_focus/005_soviet_collapse_republics.txt:1464`, `ukr_soviet_collapse_equipment_corridor_authority`: exposes league unit deployment and foreign supply helper calls.
- `common/national_focus/005_soviet_collapse_republics.txt:2028`, `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map`: exposes several endgame/report/helper calls instead of one final-route tooltip.
- `common/national_focus/005_soviet_collapse_republics.txt:3264`, `internal_soviet_collapse_security_council`: exposes three helper calls.
- `common/national_focus/005_soviet_collapse_republics.txt:9608`, `blr_soviet_collapse_partisans_or_army`: exposes three helper calls and a long visible reward.
- `common/national_focus/005_soviet_collapse_republics.txt:9832`, `blr_soviet_collapse_join_the_league_when_war_comes`: long visible reward surface.
- `common/national_focus/005_soviet_collapse_republics.txt:10610`, `kaz_soviet_collapse_the_steppe_arsenal`: long visible reward surface.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:424`, `FTH_radical_turn`: long visible reward surface.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1229`, `PRA_the_timetable_declares_authority`: exposes two helper calls.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1463`, `PRA_coal_water_and_spare_parts`: exposes two helper calls and a long reward.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:10122`, `KRS_every_harbor_a_soviet`: exposes two helper calls and a long reward.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:11857`, `SDZ_no_file_burned_order`: exposes two helper calls and a long reward.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:12472`, `SDZ_radical_turn`: long visible reward surface.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:14413`, `DHC_manych_rear_area`: long visible reward surface.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:16962`, `FEV_vladivostok_harbor_board`: long visible reward surface.

Tree-level helper density, by visible helper count:
- `soviet_collapse_kazakhstan_focus_tree`: 80 helper calls across 79 focuses
- `soviet_collapse_ukraine_focus_tree`: 76 across 60
- `soviet_collapse_internal_republic_focus_tree`: 58 across 54
- `MFR_soviet_collapse_focus_tree`: 56 across 54
- `CFR_soviet_collapse_focus_tree`: 50 across 45
- `soviet_collapse_moldova_focus_tree`: 45 across 45
- `soviet_collapse_belarus_focus_tree`: 44 across 39
- `soviet_collapse_caucasus_focus_tree`: 39 across 39
- `soviet_collapse_central_asia_focus_tree`: 38 across 38
- `soviet_collapse_baltic_focus_tree`: 37 across 37
- `soviet_collapse_breakaway_focus_tree`: 32 across 31

Patch recommendation:
- Batch-convert the highest-density trees first: Kazakhstan, Ukraine, internal republics, MFR, CFR, Moldova, Belarus.
- Keep real gameplay effects in `completion_reward`, but wrap implementation helpers inside `hidden_effect` when they should not be visible.
- Add one player-facing `custom_effect_tooltip` or `complete_tooltip` per complex focus, matching vanilla style.
- Do not hide genuinely important unlocks; expose the actual player consequence, not the helper implementation name.

## Shallow Or Low-Depth Trees

The focus-tree skill and Event 005 specs require meaningful political, industrial, military/security, expansion/war, diplomacy, and special-mechanic branches for important countries. Compact trees are allowed only when the country role is narrow, but high-chaos actors should still have identity mechanics and aggressive payoffs.

Highest-priority shallow trees:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1831`, `TSC_soviet_collapse_focus_tree`: 18 focuses; weak industry, expansion, and diplomacy coverage by scan.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2342`, `RMC_soviet_collapse_focus_tree`: 18 focuses; weak industry, expansion, and diplomacy coverage.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:2818`, `DSC_soviet_collapse_focus_tree`: 18 focuses; stronger than the others mechanically, but still compressed for a dead-army actor.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3409`, `NRF_soviet_collapse_focus_tree`: 18 focuses; weak expansion and diplomacy coverage.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:3913`, `ICD_soviet_collapse_focus_tree`: 18 focuses; weak industry, expansion, and diplomacy coverage, and weaker death-state aggression than `DSC`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1222`, `PRA_soviet_collapse_focus_tree`: 22 focuses; has rail decisions and one final wargoal, but remains compact for a rail-state fantasy.
- `common/national_focus/005_soviet_collapse_factory_successors.txt:1003`, `OGB_soviet_collapse_focus_tree`: 23 focuses; weak industry and expansion coverage by scan.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:13`, `KZR_soviet_collapse_ancient_focus_tree`: 16 focuses; weak industry coverage.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:827`, `KHW_soviet_collapse_ancient_focus_tree`: 16 focuses; weak industry coverage.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt:1235`, `ALN_soviet_collapse_ancient_focus_tree`: 16 focuses; weak industry coverage.

Patch recommendation:
- Expand `TSC`, `RMC`, `NRF`, and `ICD` first because they are high-chaos identity actors with the least branch depth.
- Add at least one mechanical branch per actor, not only stat focuses. Examples: strange science decisions for `TSC`, route infection or dead manpower mechanics for `ICD`, naval/republican offensive decisions for `NRF`, command/retinue/loyalty mechanics for `RMC`.
- For `DSC`, preserve the stronger late aggression but add industry/security/diplomacy depth so it is not only a compact war escalation tree.

## Chaos-Country Identity Gaps

### CFR Construction State

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`

Important focuses:
- `CFR_the_state_that_builds` at line 779: unlocks reconstruction decisions and builder buildout. This is the clearest construction-state payoff.
- `CFR_the_builder_state_marches_east` at line 820: mostly helper-driven route payoff.
- `CFR_build_the_border_bend_the_border` at line 841: flavor implies construction reshapes borders, but visible payload is not explicit enough.
- `CFR_reconstruction_protectorates` at line 883: protectorate identity is present in name but not strongly visible as release, puppet, integration, claim, or decision mechanics.
- `CFR_rebuild_russia_without_moscow` at line 983: endgame identity exists, but the path should feel more overpowered before the capstone.

Patch recommendation:
- Add visible unlocks for construction-state border, protectorate, reconstruction mandate, and rapid rail/factory expansion decisions.
- Add explicit claims, integration, protectorate, or construction-corridor mechanics where route text promises territorial transformation.
- Add a stronger military/security branch for engineers, rail guards, and emergency construction armies.

### MFR Arsenal State

File: `common/national_focus/005_soviet_collapse_factory_successors.txt`

Important focuses:
- `MFR_the_arsenal_state` at line 2627: strong hidden AI strategy and factory payload.
- `MFR_no_peace_without_orders` at line 2837: hidden neighbor wargoals under chaos pressure.
- `MFR_eternal_arsenal_marches` at line 2910: explicit final wargoal against SOV.
- `MFR_unite_russian_factories`, `MFR_a_rifle_in_every_treaty`, and `MFR_arm_all_clients`: visible surface still leans on helper calls.

Patch recommendation:
- Keep the aggressive final war path.
- Add earlier explicit expansion mechanics around factory integration, arms-client leverage, unit-template unlocks, or production mandate decisions.
- Convert mid-branch helper surfaces into coherent tooltips.

### Dead And Zombie-Style Actors

File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`

`DSC`:
- `DSC_revenant_staff_line` at line 2970: strong hidden claims/cores, assault columns, neighbor wars under chaos, and AI strategy.
- `DSC_congress_of_the_dead_army` at line 3330: final wargoal/war against SOV.
- Problem: the tree is still only 18 focuses and lacks enough industry/diplomacy/security depth for a major high-chaos fantasy.

`ICD`:
- `ICD_claim_the_unburied_front` at line 4247: only visible territorial claim in state 239.
- `ICD_grave_columns_march` at line 4268: only visible claim in state 217 plus objective pressure.
- `ICD_commissariat_without_end` at line 4321: final wargoal against SOV and hidden claims/assault payloads.
- Problem: `ICD` is materially weaker than `DSC` and should have more dead-state operational mechanics before the final capstone.

Patch recommendation:
- Bring `ICD` closer to `DSC` in aggression by adding neighbor-war decisions, dead manpower/recruitment mechanics, military-state pressure, or corpse-column offensive unlocks.
- Give both trees at least one non-war sustaining branch: grave logistics, post-mortem administration, field hospitals, or occupied-state conversion mechanics.

## Layout And Pathline Findings

Confirmed issue:
- `common/national_focus/005_soviet_collapse_republics.txt:11408`, `kaz_soviet_collapse_the_southern_republics_write_together`
  - Absolute coordinate: `(7, 7)`
  - Prerequisite: `kaz_soviet_collapse_the_steppe_arbitration_court`
  - Prerequisite absolute coordinate: `(2, 7)`
  - Problem: same-row prerequisite. The wiki warns prerequisites should be above the focus; same-row links are visually poor and can create misleading pathlines.
  - Recommendation: move `kaz_soviet_collapse_the_southern_republics_write_together` down one row or rewire it to a prerequisite that is visibly above it.

No confirmed issue from corrected coordinate pass:
- duplicate focus ids: none
- duplicate absolute coordinates: none
- continuous focus panel overlap: none verified

Important note:
- An early parser pass incorrectly treated inline `x = ... y = ...` focus definitions as missing `y`. That produced false duplicate-coordinate noise. The corrected pass resolves `x`, `y`, and `relative_position_id` and should be used for layout conclusions.

## Mechanics Disconnection Findings

Explicit mechanics were counted by searching focus blocks for visible or direct tokens such as:
- `unlock_decision_tooltip`
- `activate_mission`
- `create_wargoal`
- `declare_war_on`
- `add_state_claim`
- `add_core_of`
- `add_claim_by`
- `create_faction`
- `add_to_faction`
- `load_oob`
- `division_template`
- `release`
- `set_autonomy`
- `set_cosmetic_tag`

The count is intentionally conservative. A helper may still trigger mechanics, but when focus files rely on helper names without coherent visible tooltips, the player-facing reward remains disconnected.

Trees with especially weak explicit mechanic visibility:
- `soviet_collapse_breakaway_focus_tree`: 0 explicit mechanic focuses out of 36; 33 helper-bearing focuses.
- `soviet_collapse_baltic_focus_tree`: 0 out of 42; 41 helper-bearing focuses.
- `soviet_collapse_moldova_focus_tree`: 0 out of 48; 47 helper-bearing focuses.
- `FTH_soviet_collapse_focus_tree`: 0 out of 47.
- `BBH_soviet_collapse_focus_tree`: 0 out of 47.
- `KRS_soviet_collapse_focus_tree`: 0 out of 47.
- `SDZ_soviet_collapse_focus_tree`: 0 out of 47.
- `GAC_soviet_collapse_focus_tree`: 0 out of 47.
- `DHC_soviet_collapse_focus_tree`: 0 out of 47.
- `KHC_soviet_collapse_focus_tree`: 0 out of 47.
- `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `NLC`: 0 explicit mechanic focuses out of 47 by direct-token scan.
- `soviet_collapse_kazakhstan_focus_tree`: 4 explicit mechanic focuses out of 92.
- `soviet_collapse_internal_republic_focus_tree`: 4 explicit mechanic focuses out of 62.
- `MFR_soviet_collapse_focus_tree`: 8 explicit mechanic focuses out of 58.
- `CFR_soviet_collapse_focus_tree`: 9 explicit mechanic focuses out of 47.

Patch recommendation:
- For each major tree, make at least the route openers, midpoint payoffs, and capstones visibly unlock actual Soviet Collapse mechanics.
- Do not expose generic helper names as the only evidence of a mechanic.
- Prefer explicit `unlock_decision_tooltip`, claim/core/wargoal text, unit-template tooltip, release/influence tooltip, or mechanic-specific custom tooltip.

## Prioritized Patch Plan

1. Fix the Kazakhstan same-row pathline at `common/national_focus/005_soviet_collapse_republics.txt:11408`.
2. Run a first reward-surface cleanup tranche on Kazakhstan, Ukraine, internal republics, CFR, and MFR because those trees have the highest helper-density or highest player impact.
3. Expand or deepen `ICD`, `TSC`, `RMC`, and `NRF`; these are high-chaos actors with too little branch depth.
4. Strengthen `CFR` with construction-state conquest/protectorate/build-the-border mechanics and a military/security branch.
5. Strengthen `MFR` midgame mechanics before final war, especially arms-client and factory-integration decisions.
6. Add direct visible mechanics to the no-explicit-token custom splinters, starting with the most identity-sensitive actors: `BBH`, `KRS`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, and `NLC`.
7. Revisit regional republic trees with zero explicit mechanic visibility: breakaway, Baltic, and Moldova.
8. Give ancient restoration trees at least one unique restoration mechanic and a small industry/sustainment branch.
9. Re-run focus reward spam and explicit-mechanic scans after each tranche, because this issue is systemic and easy to reintroduce.
10. After code patches, run a localisation audit so new coherent tooltips and visible unlocks do not desync from gameplay.

## Commands Used

Reference and discovery commands:
```bash
sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md
sed -n '1,220p' AGENTS.md
sed -n '1,180p' "paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Effect - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/On actions - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md"
sed -n '1,120p' "paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md"
rg -n "add_ideas|create_wargoal|unlock_decision_tooltip|complete_tooltip|custom_effect_tooltip" "/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md"
rg -n "focus_tree|prerequisite|mutually_exclusive|relative_position_id|continuous_focus_position" "/home/klim/projects/Hearts of Iron IV/common/national_focus/soviet.txt" "/home/klim/projects/Hearts of Iron IV/common/national_focus/baltic_shared.txt" "/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt"
```

Audit commands:
```bash
wc -l common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
rg -n "focus_tree =|id =|completion_reward =|add_ideas|unlock_decision_tooltip|create_wargoal|add_state_claim|add_core_of|relative_position_id|mutually_exclusive|prerequisite|continuous_focus_position" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt
nl -ba common/national_focus/005_soviet_collapse_factory_successors.txt | sed -n '760,1010p'
nl -ba common/national_focus/005_soviet_collapse_factory_successors.txt | sed -n '2600,2940p'
nl -ba common/national_focus/005_soviet_collapse_custom_splinters.txt | sed -n '1220,1820p'
nl -ba common/national_focus/005_soviet_collapse_custom_splinters.txt | sed -n '2810,3400p'
nl -ba common/national_focus/005_soviet_collapse_custom_splinters.txt | sed -n '3910,4380p'
```

Parser commands:
```bash
python3 - <<'PY'
# Inline parser used to count focus_tree/focus blocks, duplicate ids,
# visible helper calls, long visible rewards, explicit mechanic tokens,
# absolute coordinates resolved through relative_position_id, and same-row/upward prerequisites.
# It parsed the four audited files only and did not write files.
PY
```

## Validation Notes

- This handoff is based on the current worktree at audit time.
- No old handoff reports were used as assumptions.
- No broad rewrite was made.
- No gfx or flags were touched.
- The audit did not run the game or load the mod; it is a script/static focus-tree audit.
