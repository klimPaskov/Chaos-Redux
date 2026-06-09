# Event 005 Soviet Collapse Focus Tree Bounded Audit and OGB Tooltip Patch

Date: 2026-05-30

Subagent role: Chaos Redux focus tree subagent.

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Hard boundary followed: no flags, flag sprites, `gfx/flags`, generated assets, or asset regeneration were touched. No `.gfx` file was edited.

References read before editing:
- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and script constants docs.
- Vanilla focus examples in `~/projects/Hearts of Iron IV/common/national_focus/`.
- Event source specs: especially `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md` and part 6 country/splinter requirements.

## Route Coverage Table

| Required route or family | Implemented branch or tree | Status | Evidence |
| --- | --- | --- | --- |
| Ukraine political, military, League, grain, foreign, and high-chaos routes | `soviet_collapse_ukraine_focus_tree`, `005_soviet_collapse_republics.txt:18`, 83 focuses | Partial | Large route surface exists, but 307 flat-reward focuses across republic file show the broader reward problem still affects this family. |
| Generic breakaway republics | `soviet_collapse_breakaway_focus_tree`, `005_soviet_collapse_republics.txt:2370`, 36 focuses | Partial | Compact skeleton exists; still weak for long-lived breakaways. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree`, `005_soviet_collapse_republics.txt:3167`, 62 focuses | Partial | Economy/logistics/local government branches exist, but direct decision integration remains thin. |
| Baltic republics | `soviet_collapse_baltic_focus_tree`, `005_soviet_collapse_republics.txt:4671`, 42 focuses | Partial | Legal restoration/League/coastal identity exists; needs stronger postwar and decision payoff. |
| Caucasus republics | `soviet_collapse_caucasus_focus_tree`, `005_soviet_collapse_republics.txt:5635`, 40 focuses | Partial | Mountain/oil/compact identity exists; expansion and settlement consequences remain narrow. |
| Central Asian republics | `soviet_collapse_central_asia_focus_tree`, `005_soviet_collapse_republics.txt:6562`, 45 focuses | Partial | Pass, rail, old movement, and league hooks exist; reward repetition remains high. |
| Moldova | `soviet_collapse_moldova_focus_tree`, `005_soviet_collapse_republics.txt:7707`, 48 focuses | Partial | Dniester and neutrality branches exist; no strong decision loop surfaced in this pass. |
| Belarus rail/corridor/logistics identity | `soviet_collapse_belarus_focus_tree`, `005_soviet_collapse_republics.txt:8868`, 53 focuses | Partial | Rail/freight identity exists; needs stronger rail/supply decision payoff and screenshot pathline review. |
| Kazakhstan steppe/resource/rail pivot | `soviet_collapse_kazakhstan_focus_tree`, `005_soviet_collapse_republics.txt:10199`, 92 focuses | Partial | Large tree, still reward-heavy and too reliant on generic variables/helpers. |
| Full-size high-chaos splinters | 19 47-focus trees in `005_soviet_collapse_custom_splinters.txt`, e.g. `FTH` at line 15, `BBH` at line 7723, `ARD` at line 23238 | Partial | Counts are high, but many trees still share helper rhythm and have too little decision/formable/war payoff. |
| Compact crisis splinters | `PRA` line 1216, `TSC` line 1815, `RMC` line 2290, `DSC` line 2773, `NRF` line 3370, `ICD` line 3874 | Partial | Strong concepts; 18-22 focuses are still too narrow for OP/high-chaos actors. |
| Factory successors | `CFR` line 16, `OGB` line 1171, `MFR` line 1776 in `005_soviet_collapse_factory_successors.txt` | Partial | CFR/MFR are more developed. OGB remains the shallowest successor, but this pass added one missing focus-surfaced decision hook. |
| Ancient restorations | `KZR` line 13, `SOG` line 382, `KHW` line 752, `ALN` line 1125 in `005_soviet_collapse_ancient_restorations.txt` | Incomplete for depth | All four are 16-focus stubs with repeated icon families and similar claim/endgame rhythm. |

## Patch Applied

Changed file:
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Changed focus id:
- `OGB_open_the_volga_registers`, `common/national_focus/005_soviet_collapse_factory_successors.txt:1188`

Changed line:
- Added `unlock_decision_tooltip = ogb_consolidate_volga_registers` at `common/national_focus/005_soviet_collapse_factory_successors.txt:1195`.

Patch behavior before:
- `OGB_open_the_volga_registers` set `ogb_focus_open_the_volga_registers`, gave political power, and raised `ogb_volga_legitimacy`, but it did not surface the existing OGB register decision in its focus tooltip.
- The existing decision `ogb_consolidate_volga_registers` is defined at `common/decisions/005_soviet_collapse_decisions.txt:6840` with localisation at `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:3124`.

Patch behavior after:
- Completing `OGB_open_the_volga_registers` now advertises the existing `ogb_consolidate_volga_registers` decision, connecting the opening Volga-register focus to the OGB decision surface without changing decision logic, costs, AI, effects, localisation, icons, scripted effects, or flags.

Localisation keys changed:
- None.

Icon ids changed:
- None.

## Missing or Simplified Content

High-priority shallow/repeated reward helper call sites remaining:
- `soviet_collapse_apply_focus_legal_recognition`: still appears heavily across major republic, ancient, and custom focus routes and makes distinct routes feel similar.
- `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_league_preparation`, and `soviet_collapse_apply_focus_high_chaos_identity`: useful helpers, but overused as route payoffs.
- `soviet_collapse_apply_custom_splinter_first_guard_identity`, `soviet_collapse_apply_custom_splinter_stores_identity`, `soviet_collapse_apply_custom_splinter_league_identity`, and `soviet_collapse_apply_custom_splinter_enemy_front_identity`: repeated across full custom splinters and still the biggest source of templated feel.

Top priority shallow trees:
- `OGB_soviet_collapse_focus_tree`, `005_soviet_collapse_factory_successors.txt:1171`: 23 focuses; needs broader Volga restoration politics, river economy, Idel-Ural compact/rivalry consequences, and postwar integration.
- `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` in `005_soviet_collapse_custom_splinters.txt:1216-4327`: strong concepts but only 18-22 focuses each.
- Ancient restoration trees `KZR`, `SOG`, `KHW`, `ALN`: 16 focuses each, too similar by structure and icon family.
- `soviet_collapse_kazakhstan_focus_tree`, `005_soviet_collapse_republics.txt:10199`: 92 focuses but still too many variable/stat packets.

Top priority layout fixes remaining:
- Mechanical coordinate audit found zero duplicate coordinates and zero same-row `dx = 1` crowding in the four scoped files after this pass.
- In-game screenshot/pathline review is still needed for dense mid-tree route convergence, especially Ukraine, Belarus, Kazakhstan, Central Asia, Moldova, and OGB's multi-parent endpoints.
- Avoid adding any focus between mutually exclusive sibling pairs when expanding OGB, ancient restorations, or compact chaos splinters.

## Icon Coverage Table

| File | Focuses | Missing icon assignment | Missing `.gfx` definition | Repeated icon groups | Top repeated icons |
| --- | ---: | ---: | ---: | ---: | --- |
| `005_soviet_collapse_republics.txt` | 501 | 0 | 0 | 22 | `GFX_focus_soviet_collapse_guard_the_radio_stations` x4; `GFX_ukr_soviet_collapse_democratic` x4 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 0 | 0 | 99 | `GFX_focus_FEV_diplomatic_plan` x4; `GFX_focus_SZA_diplomatic_plan` x4 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 0 | 0 | 11 | `GFX_focus_CFR_municipal_board_elections` x3; `GFX_focus_CFR_concrete_republic` x3 |
| `005_soviet_collapse_ancient_restorations.txt` | 64 | 0 | 0 | 8 | `GFX_focus_soviet_collapse_ancient_workshop_compact` x4; `GFX_focus_soviet_collapse_ancient_guard_old_routes` x4 |

Icon conclusion: no load-breaking missing focus icon definitions were found. The unique-icon design standard is still not met because repeated icon groups remain, but no asset or `.gfx` edits were made because the user explicitly prohibited flag/asset work and this pass was focus-tree bounded.

## Localisation and Reward Mismatch List

Mechanical localisation check:
- Focus name keys missing: 0 across 1,698 focus ids.
- Focus description keys missing: 0 across 1,698 focus ids.

Reward mismatch risks:
- `OGB_kazan_ferry_offices`, `005_soviet_collapse_factory_successors.txt:1321`: named Kazan ferry focus still uses a random owned core state industrial construction reward. Better future fix: target named Volga/Kazan state logic if a stable state helper exists.
- `OGB_future_bulgaria_file`, `005_soviet_collapse_factory_successors.txt:1692`: title promises a future event/dossier hook but reward is mostly political power and legitimacy. Needs parent route work.
- `DSC_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:2773`: has some decision hooks and aggressive effects, but the Dead Soldiers Congress still needs broader recruitable-population/coring/expansion play.
- `NRF_soviet_collapse_focus_tree`, `005_soviet_collapse_custom_splinters.txt:3370`: naval theme exists, but real naval war, ship/port payoff, and post-capture port logic remain thin.
- Ancient restorations: descriptions and icons imply distinct restorations, but the four trees still share repeated structure and icon families.

## AI Behavior Gaps

Mechanical AI check:
- Missing `ai_will_do`: 0 across the four scoped files.

Remaining AI gaps:
- Route AI is still mostly scalar. It reacts to stability, war, `SOV` pressure variables, or chaos tier, but many trees do not have a durable route plan after focus completion.
- Violent/high-chaos actors need stronger aggression and target-selection behavior once their expansion route is chosen.
- Naval actors need AI behavior for dockyards, convoy escort/raiding, port defense, naval invasion preparation, and coastal target selection.
- Belarus and Kazakhstan need route-aware AI that distinguishes rail/logistics sovereignty, resource routes, foreign corridors, League leadership, and war expansion.

## Validation Run

Commands/checks run:
- Mechanical parser count over all four focus files: 41 focus trees, 1,698 focus blocks, 1,698 icons, 1,698 `ai_will_do`.
- Bracket balance check: all four scoped focus files ended at `bracket_depth=0` with no premature closes.
- Unsupported operator grep: no `<=` or `>=` found in the four scoped focus files.
- Localisation/icon check: no missing focus name keys, focus desc keys, or focus icon `.gfx` definitions found in the scoped files.
- Patch line check: confirmed `unlock_decision_tooltip = ogb_consolidate_volga_registers` at `005_soviet_collapse_factory_successors.txt:1195`.

Skipped validation:
- No in-game focus tree screenshot/pathline validation was run from this subagent pass.
- No scripted-effect validation was run because the parent is editing scripted effects and this pass avoided that surface.
- No decision-file patch validation was run because the patch did not edit decision files.

## Remaining Route Risks

- The patch is deliberately narrow. It does not solve OGB's broad 23-focus depth problem.
- Existing dirty worktree changes predate this subagent pass; they were treated as parent/user work and not reverted.
- A future parent pass should decide whether `ogb_consolidate_volga_registers` should be truly focus-gated in the decision file. This pass only surfaced the existing decision through the focus tooltip.
- No gfx/flags or flag sprites were touched.
