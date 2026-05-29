# Soviet Collapse focus tree subagent reward/layout audit handoff

Date: 2026-05-29

Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- narrow helper edits in `common/scripted_effects/005_soviet_collapse_effects.txt`

References used before patching:
- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- offline wiki core pages plus `National focus modding - Hearts of Iron 4 Wiki.md`
- vanilla docs/examples in `~/projects/Hearts of Iron IV/documentation` and `~/projects/Hearts of Iron IV/common/national_focus`

## High-priority findings first

| Priority | File / identifiers | Finding | Action |
| --- | --- | --- | --- |
| High | all four target focus files, all focus `completion_reward` blocks | No direct focus reward was found adding the same idea more than once in one reward. | No direct duplicate idea patch needed. |
| High | `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_update_consolidated_republic_ideas` and callers `soviet_collapse_apply_focus_legal_recognition`, `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_league_preparation`, `soviet_collapse_apply_focus_high_chaos_identity` | Helper-side staged idea updates are heavily reused. The updater clears staged republic ideas before adding the current tier, so direct stacking was not found, but the helper chain remains a reward-spam and hover-noise risk because many focuses refresh the same staged idea family. | Documented as helper-side risk; full cleanup should consolidate these into clearer route payoffs. |
| High | `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_apply_focus_high_chaos_identity` | High-chaos focus rewards were too weak and generic for the intended overpowered/aggressive countries. | Patched helper with manpower, infantry equipment, command power, war support, and SOV conquer AI strategy. |
| High | `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_complete_dead_soldiers_endgame`, `soviet_collapse_complete_northern_revenant_endgame` | DSC/death and NRF/naval endgames were mostly idea/pressure payoffs and did not strongly express their concepts. | Patched DSC with manpower, assault columns, controlled-state cores, SOV war goal/AI; patched NRF with navy XP, convoys, dockyard/coastal fort, SOV war goal/AI. |
| Medium | `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_apply_focus_rail_authority_reward` | Rail authority rewards built supply/infrastructure but not railway. | Patched to build a railway level in the selected core state. |
| Medium | `common/national_focus/005_soviet_collapse_republics.txt`, `soviet_collapse_free_republics_observer_seat`, `soviet_collapse_road_and_rail_repair_board`, `soviet_collapse_the_republic_endures`, `soviet_collapse_a_republic_worth_naming` | Four shared-republic focuses sat above their prerequisites, creating upward/crossing pathline risk. | Patched safe local y positions only. |
| Medium | `common/national_focus/005_soviet_collapse_factory_successors.txt`, `MFR_production_war_room`, `MFR_contracts_with_builders` | Two MFR prerequisite inversions remain. | Left unpatched because fixing them cleanly needs a reviewed MFR branch layout ripple. |

## Changed files

| File | Change type |
| --- | --- |
| `common/national_focus/005_soviet_collapse_republics.txt` | Small layout-only fixes for four shared-republic focuses. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Narrow helper reward improvements for rail, high-chaos, DSC, and NRF paths. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_subagent_reward_layout_audit_handoff.md` | This handoff. |

## Changed focus ids and helper ids

Focus ids changed:
- `soviet_collapse_free_republics_observer_seat`: y moved to 9.
- `soviet_collapse_road_and_rail_repair_board`: y moved to 9.
- `soviet_collapse_the_republic_endures`: y moved to 13.
- `soviet_collapse_a_republic_worth_naming`: y moved to 14.

Scripted effect ids changed:
- `soviet_collapse_apply_focus_rail_authority_reward`
- `soviet_collapse_apply_focus_high_chaos_identity`
- `soviet_collapse_complete_dead_soldiers_endgame`
- `soviet_collapse_complete_northern_revenant_endgame`

Localisation keys changed: none.

Icon ids changed: none.

## Route behavior before and after

| Identifier | Before | After |
| --- | --- | --- |
| `soviet_collapse_apply_focus_rail_authority_reward` | Increased depot/institution values and built infrastructure plus a supply node in a core state. | Also builds one railway level, making rail-themed focuses visibly affect rail/supply infrastructure. |
| `soviet_collapse_apply_focus_high_chaos_identity` | Added recognition/local authority pressure and SOV objective pressure. | Also adds manpower, infantry equipment, command power, war support, and an AI conquer strategy against SOV when SOV exists. |
| `soviet_collapse_complete_dead_soldiers_endgame` | Set endgame flags, added `dsc_dead_army_politics`, and pressured SOV objectives. | Also adds manpower, spawns custom splinter assault columns, cores controlled non-core states, creates an annex SOV war goal when legal, and adds strong SOV conquer AI strategy. |
| `soviet_collapse_complete_northern_revenant_endgame` | Set endgame flags, added `nrf_fleet_that_does_not_dock`, and pressured SOV objectives/foreign pressure. | Also adds navy XP, convoys, a coastal dockyard/coastal fort payoff where possible, creates an annex SOV war goal when legal, and adds SOV conquer AI strategy. |
| shared-republic layout ids listed above | Some children sat above their prerequisites. | The four audited links now flow downward. |

## Route coverage table

| Tree | File | Focuses | Current branch coverage | Main gaps |
| --- | --- | ---: | --- | --- |
| `soviet_collapse_ukraine_focus_tree` | republics | 83 | Political, military, diplomacy, industry, navy, League, and multiple mutually exclusive politics exist. | Deepest tree, but still uses many generic helper rewards and needs route-specific payoff review. |
| `soviet_collapse_breakaway_focus_tree` | republics | 36 | Political, army, industry, stability, manpower. | Generic shared route; expansion/diplomacy identity is thin. |
| `soviet_collapse_internal_republic_focus_tree` | republics | 62 | Political, army, industry, stability, manpower, internal tag flavor. | Some regional flavor exists, but common trunk still leans on generic helper rewards. |
| `soviet_collapse_baltic_focus_tree` | republics | 42 | Political, army, industry, stability, manpower. | Needs sharper independence/diplomacy/naval or border-state outcomes. |
| `soviet_collapse_caucasus_focus_tree` | republics | 40 | Political, army, industry, stability, manpower. | Needs mountain/ethnic/diplomatic/expansion route depth. |
| `soviet_collapse_central_asia_focus_tree` | republics | 45 | Political, army, industry, stability, manpower. | Needs stronger regional expansion and resource/logistics identity. |
| `soviet_collapse_moldova_focus_tree` | republics | 48 | Political, army, air, industry, stability, manpower. | Needs route-specific diplomacy/expansion hooks. |
| `soviet_collapse_belarus_focus_tree` | republics | 53 | Political, army, industry, stability, manpower. | Has better size, but should differentiate political choices and war aims further. |
| `soviet_collapse_kazakhstan_focus_tree` | republics | 92 | Political, army, industry, navy, stability, manpower. | Strong coverage, still needs generic reward/AI review. |
| `FTH_soviet_collapse_focus_tree` | custom splinters | 47 | Full custom-style spread with air/army/industry/political/stability/manpower. | Some repeated helper reward patterns. |
| `PRA_soviet_collapse_focus_tree` | custom splinters | 22 | Political, army, industry, annexation, stability. | Shallow; lacks distinct political/industrial/military/diplomacy/expansion depth. |
| `TSC_soviet_collapse_focus_tree` | custom splinters | 18 | Political, army, industry, annexation, stability. | Shallow; needs full route family. |
| `RMC_soviet_collapse_focus_tree` | custom splinters | 18 | Political, army, industry, annexation, manpower, stability. | Shallow; needs full route family. |
| `DSC_soviet_collapse_focus_tree` | custom splinters | 18 | Political, army, industry, annexation, manpower, stability. | Shallow, but endgame payoff was strengthened in helper. Needs full death-route depth. |
| `NRF_soviet_collapse_focus_tree` | custom splinters | 18 | Political, army, navy, industry, annexation, manpower, stability. | Shallow, but endgame payoff was strengthened in helper. Needs full naval route depth. |
| `ICD_soviet_collapse_focus_tree` | custom splinters | 18 | Political, army, industry, annexation, manpower, stability. | Shallow; needs full route family. |
| `BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/BAC/ARD/NLC` | custom splinters | 47 each | Most have broad political/industry/military/stability/manpower coverage. | Many are structurally similar and need sharper lore/mechanical identity. |
| `FEV_soviet_collapse_focus_tree` | custom splinters | 47 | Political, army, navy, industry, manpower, stability. | Only 32 unique icons for 47 focuses; repeated visuals and generic rewards. |
| `SZA_soviet_collapse_focus_tree` | custom splinters | 47 | Political, army, industry, manpower, stability. | Only 32 unique icons; needs stronger concept-specific payoff. |
| `UWD_soviet_collapse_focus_tree` | custom splinters | 47 | Political, army, air, research, industry, manpower, stability. | Only 28 unique icons; needs visual/reward differentiation. |
| `MRC_soviet_collapse_focus_tree` | custom splinters | 47 | Political, army, industry, manpower, stability. | Only 31 unique icons; route reward identity still generic. |
| `IUL_soviet_collapse_focus_tree` | custom splinters | 47 | Political, army, industry, manpower, stability. | Only 24 unique icons; high visual repetition. |
| `CFR_soviet_collapse_focus_tree` | factory successors | 47 | Political, army, industry, annexation, manpower, stability. | Factory concept exists but needs stronger production/factory payoff differentiation. |
| `OGB_soviet_collapse_focus_tree` | factory successors | 23 | Political, army, industry, annexation, manpower, stability. | Shallow; needs full route family. |
| `MFR_soviet_collapse_focus_tree` | factory successors | 58 | Political, army, industry, annexation, manpower, stability. | Stronger size, but two layout inversions remain and factory branches need payoff review. |
| `KZR_soviet_collapse_ancient_focus_tree` | ancient restorations | 16 | Political, army, navy, industry, annexation, manpower, stability. | Shallow restoration tree; needs full political/industrial/military/expansion route depth. |
| `SOG_soviet_collapse_ancient_focus_tree` | ancient restorations | 16 | Political, army, industry, annexation, manpower, stability. | Shallow restoration tree. |
| `KHW_soviet_collapse_ancient_focus_tree` | ancient restorations | 16 | Political, army, industry, annexation, manpower, stability. | Shallow restoration tree. |
| `ALN_soviet_collapse_ancient_focus_tree` | ancient restorations | 16 | Political, army, industry, annexation, manpower, stability. | Shallow restoration tree. |

## Missing or simplified content list

| File / identifiers | Issue |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `PRA/TSC/RMC/DSC/NRF/ICD_soviet_collapse_focus_tree` | 18-22 focus trees are below the requested depth and do not yet support distinct political, industrial, military/diplomacy, and expansion routes. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt`, `OGB_soviet_collapse_focus_tree` | 23 focuses; shallow relative to CFR/MFR and the requested factory-successor identity. |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt`, `KZR/SOG/KHW/ALN_soviet_collapse_ancient_focus_tree` | Each has 16 focuses; ancient restoration routes are placeholders compared with the requested full-route design. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt`, full 47-focus custom trees | Many use broad branch labels but still lean on common reward helpers. They need route-specific mechanics instead of repeated generic pressure/recovery. |
| `common/national_focus/005_soviet_collapse_republics.txt`, shared republic trees | Stronger than the shallow custom/ancient trees, but repeated helper use still reduces route purpose. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt`, `MFR_production_war_room`, `MFR_contracts_with_builders` | Pathline/prerequisite inversion remains. |

Existing broader plan retained for full rework:
- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`

No new broad redesign plan was written in this pass because a full follow-up plan already exists.

## Icon coverage table

| File | Icons used | Unique icons | Defined unique icons | Missing icon ids |
| --- | ---: | ---: | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 501 | 458 | 458 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 885 | 885 | 0 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 113 | 113 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 42 | 42 | 0 |
| All target focus files | 1698 | 1498 | 1498 | 0 |

Icon repetition risks:
- `FEV_soviet_collapse_focus_tree`: 47 focuses, 32 unique icons.
- `SZA_soviet_collapse_focus_tree`: 47 focuses, 32 unique icons.
- `UWD_soviet_collapse_focus_tree`: 47 focuses, 28 unique icons.
- `MRC_soviet_collapse_focus_tree`: 47 focuses, 31 unique icons.
- `IUL_soviet_collapse_focus_tree`: 47 focuses, 24 unique icons.
- `CFR_soviet_collapse_focus_tree`: 47 focuses, 32 unique icons.
- `KZR/SOG/KHW/ALN_soviet_collapse_ancient_focus_tree`: defined icons exist, but 16-focus trees are too shallow for final-route identity.

## Localisation and reward mismatch list

| File / identifiers | Result |
| --- | --- |
| all 1698 target focus ids | Name and `_desc` localisation keys were found for every target focus id. |
| patched ids | No localisation text changed; reward changes are helper-side and do not introduce new visible names. |
| `soviet_collapse_apply_focus_high_chaos_identity` callers | Focus text may still undersell the new overpowered/aggressive payoff on some callers because the helper is shared by 96 direct focus calls. This should be reviewed route-by-route during full rework. |
| `soviet_collapse_apply_focus_rail_authority_reward` callers | Rail-themed reward now matches rail wording better, but non-rail callers that indirectly use the helper should be checked in a full pass. |
| `soviet_collapse_complete_dead_soldiers_endgame`, `soviet_collapse_complete_northern_revenant_endgame` | Endgame rewards now better match death/naval concepts. Localisation was not rewritten because the change is narrow and visible focus text coverage already exists. |

## AI behavior gaps

| File / identifiers | Gap |
| --- | --- |
| all target focus trees | Every audited focus block had an `ai_will_do`, but most are flat base weights with limited route-aware behavior. |
| `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_apply_focus_high_chaos_identity` | Patched with SOV conquer AI strategy, but this is not a full strategy plan. |
| `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_complete_dead_soldiers_endgame`, `soviet_collapse_complete_northern_revenant_endgame` | Patched with stronger SOV conquer AI strategy. |
| custom and ancient shallow trees | Need route-aware AI paths that prioritize political choice, industry buildup, military preparation, and expansion differently. |
| factory successors | Need factory/production AI behavior beyond flat focus weights and scattered target/building strategies. |

## Validation run

Commands/checks run after patch:
- Brace depth scan on all four target focus files plus `common/scripted_effects/005_soviet_collapse_effects.txt`: all final depth 0, min depth 0.
- Duplicate focus id scan across the four target focus files: none.
- Missing prerequisite/mutual-exclusion reference scan across the four target focus files: none.
- Unsupported `<=`/`>=` scan in the four target focus files plus changed scripted effects file: no hits.
- Direct duplicate `add_ideas` scan in every target focus `completion_reward`: none.
- Helper direct `add_ideas` scan for the most-used focus helpers and patched helpers: no duplicate direct idea adds.
- Icon definition scan against `interface/**/*.gfx`: 0 missing icon ids.
- Focus localisation scan across localisation files: 0 missing name or `_desc` entries for 1698 target focus ids.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/scripted_effects/005_soviet_collapse_effects.txt`: clean.

Skipped validation:
- No in-game launch or focus UI screenshot validation was run in this subagent pass.
- No binary flag edits were made.
- No full route rewrite validation was attempted because this pass intentionally patched only bounded, reviewable issues.

## Remaining route risks

- A full Soviet Collapse focus tree rework is still incomplete. This pass does not prove full completion.
- Shallow custom, factory, and ancient trees still need real political/industrial/military/diplomacy/expansion route families.
- Many high-chaos tags remain structurally similar and reward-heavy through shared helpers.
- The staged republic idea updater does not appear to stack duplicate ideas, but repeated helper refreshes are still a design/hover-noise risk.
- Two MFR pathline inversions remain: `MFR_production_war_room` after `MFR_plate_steel_rationing`, and `MFR_contracts_with_builders` after `MFR_civilian_factory_rivalry`.
- Route-aware AI behavior remains shallow outside the patched high-chaos/endgame aggression hooks.
