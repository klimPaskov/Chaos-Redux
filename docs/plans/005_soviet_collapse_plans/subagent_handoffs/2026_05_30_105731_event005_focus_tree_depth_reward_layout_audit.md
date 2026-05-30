# Event 005 Soviet Collapse Focus Tree Depth, Reward, and Layout Audit

Timestamp: 2026-05-30 10:57 UTC

Auditor: Chaos Redux focus tree subagent

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Read-only helper context: `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/ai_strategy/005_soviet_collapse.txt`, Event 005 localisation files.

Hard constraint honored: no `gfx/`, `flags/`, sprites, images, or `.gfx` files were edited or inspected.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, AI focuses, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, plus `~/projects/Hearts of Iron IV/common/ai_strategy/_documentation.md`.
- Vanilla focus precedents: `soviet.txt`, `baltic_shared.txt`, `italy.txt` for prerequisite, mutual exclusion, branch layout, and AI examples.
- Source design: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`.

## Files Changed

| File | Change |
|---|---|
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_105731_event005_focus_tree_depth_reward_layout_audit.md` | Added this audit handoff. |

No gameplay, localisation, helper, GFX, flag, or sprite file was patched.

Changed focus ids: none.

Changed localisation keys: none.

Changed icon ids: none.

## Current Audit Totals

| File | Trees | Focuses | Direct `add_ideas`/`add_timed_idea`/`swap_ideas` focuses | Direct `remove_ideas` focuses | Duplicate same idea in one focus | Flat reward focuses | Tiny equipment/building focuses | Missing AI | Missing filters | Missing icon assignment |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `005_soviet_collapse_republics.txt` | 9 | 501 | 0 | 0 | 0 | 307 | 120 | 0 | 0 | 0 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | 0 | 6 | 0 | 555 | 316 | 0 | 0 | 0 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | 0 | 1 | 0 | 54 | 12 | 0 | 0 | 0 |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | 0 | 0 | 0 | 29 | 10 | 0 | 0 | 0 |
| Total | 41 | 1698 | 0 | 7 | 0 | 945 | 458 | 0 | 0 | 0 |

Direct same-idea focus spam was not reproduced in the four focus files. The current problem is reward depth and route identity: 945 focuses still use direct flat reward effects, and 458 look like tiny equipment/building reward ladders without a decision, claim, core, war goal, or equivalent direct payoff in the same focus.

The only direct idea effects in focus rewards are cleanup removes:
- `PRA_the_board_overrules_ministers`
- `TSC_the_committee_of_instruments`
- `RMC_communes_of_witnesses`
- `DSC_witness_officers`
- `NRF_living_harbor_committees`
- `ICD_commissars_of_last_addresses`
- `OGB_the_council_takes_the_seal`

## Route Coverage Table

| Tree | Focuses | Decision hooks | Direct expansion hooks | Status | Notes |
|---|---:|---:|---:|---|---|
| `soviet_collapse_ukraine_focus_tree` | 83 | 7 | 0 | Present, needs payoff pass | Broad political/industry/diplomacy surface exists, but still helper-heavy; expansion mostly runs through helpers and flags. |
| `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 0 | Fallback only | Too generic for any long-lived important country. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 0 | Present, shallow for important tags | Has regional gates, but no decision loop and many shared-helper rewards. |
| `soviet_collapse_baltic_focus_tree` | 42 | 0 | 0 | Present, under-integrated | Regional theme exists; lacks decisions and postwar settlement mechanics. |
| `soviet_collapse_caucasus_focus_tree` | 40 | 2 | 0 | Present, thin expansion | Oil/mountain identity exists; needs stronger postwar consequences. |
| `soviet_collapse_central_asia_focus_tree` | 45 | 3 | 1 | Present, reward-heavy | Has some hooks; still generic rail/league/helper rhythm. |
| `soviet_collapse_moldova_focus_tree` | 48 | 0 | 0 | Present, no decision hooks | Romanian/Dniester concepts exist but need actual route decisions and settlement outcomes. |
| `soviet_collapse_belarus_focus_tree` | 53 | 3 | 1 | Present, needs corridor payoff | Stronger structure than most, but rail/forest/corridor routes still need mechanics beyond variables/helpers. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | 4 | 0 | Present, too broad/reward-heavy | Largest tree; needs route consolidation and clearer expansion/postwar payoffs. |
| `FTH_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Needs distinct Black Banner mechanics and expansion. |
| `PRA_soviet_collapse_focus_tree` | 22 | 12 | 1 | Best compact special tree, still shallow | Rail decisions exist; needs junction-control loop, postwar rail integration, and stronger OP aggression. |
| `TSC_soviet_collapse_focus_tree` | 18 | 0 | 1 | Shallow crisis tree | Tunguska concept needs anomaly pressure, containment/escalation choices, and real conquest mechanics. |
| `RMC_soviet_collapse_focus_tree` | 18 | 0 | 1 | Shallow crisis tree | Aggressive concept exists, but no decision loop or route depth. |
| `DSC_soviet_collapse_focus_tree` | 18 | 5 | 2 | Shallow but promising | Dead-army endpoint is strong; needs manpower/revival/occupation loop behind it. |
| `NRF_soviet_collapse_focus_tree` | 18 | 5 | 1 | Shallow naval chaos tree | Needs port-control, raiding, dockyard, naval invasion, and coastal settlement mechanics. |
| `ICD_soviet_collapse_focus_tree` | 18 | 0 | 1 | Shallow death-state tree | Needs commissariat production, occupation conversion, and decision loop. |
| `BSC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Basmachi/oasis identity not translated into mechanics. |
| `TNC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Turkestan identity lacks decisions/expansion. |
| `ALA_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Alash route needs lore-specific government and steppe settlement mechanics. |
| `BBH_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Black Banner Host flavor exists; no decision/expansion hooks. |
| `KRS_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Naval/sailor concept needs port and fleet gameplay. |
| `UDC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Loyalist defense state lacks distinct mechanics. |
| `SDZ_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Security directorate lacks intelligence/security decisions. |
| `GAC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Peasant/green route needs land, requisition, and local autonomy mechanics. |
| `DHC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Don Host needs cavalry, river, and host settlement mechanics. |
| `KHC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Kuban Host needs crossing, Cossack, and Black Sea mechanics. |
| `FEV_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Far Eastern buffer needs Pacific, Sakhalin, port, and patron mechanics. |
| `SZA_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Zemstvo identity lacks administrative/depot decision play. |
| `UWD_soviet_collapse_focus_tree` | 47 | 0 | 0 | Worst tiny-reward density | Worker/industrial route should be a production system, not 23 tiny reward focuses. |
| `MRC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Mountain confederation needs pass, autonomy, and mountain defense mechanics. |
| `IUL_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Volga/Ural identity needs rivalry/integration mechanics with OGB and regional claims. |
| `BAC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Birobidzhan/Amur settlement needs local institutions and border play. |
| `ARD_soviet_collapse_focus_tree` | 47 | 3 | 0 | Full-size but reward-heavy | Arctic naval directorate needs port-control and naval decisions. |
| `NLC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Full-size but templated | Polar science/commune identity needs weather, survival, and Arctic diplomacy mechanics. |
| `CFR_soviet_collapse_focus_tree` | 47 | 5 | 2 | Better than most | Needs governance/strategy operating-model depth, not only construction payoffs. |
| `OGB_soviet_collapse_focus_tree` | 23 | 2 | 3 | Too shallow for OP successor | Volga restoration exists but needs full political/industry/expansion branches. |
| `MFR_soviet_collapse_focus_tree` | 58 | 3 | 1 | Better than most | Needs arms-market/client-war system and cleaner route fork layout. |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | 2 | 3 | Ancient stub | Too shallow; repeated restoration template. |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | 2 | 3 | Ancient stub | Too shallow; repeated restoration template. |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | 2 | 3 | Ancient stub | Too shallow; repeated restoration template. |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | 2 | 3 | Ancient stub | Too shallow; repeated restoration template. |

## Missing Or Simplified Content List

High priority:
- `PRA`, `TSC`, `DSC`, `NRF`, `ICD`, `RMC`: 18-22 focus trees are too small for the requested extremely overpowered and aggressive chaos countries. `PRA`, `DSC`, and `NRF` have useful foundations; `TSC`, `ICD`, and `RMC` need full mechanic loops.
- `OGB_soviet_collapse_focus_tree`: 23 focuses and a few claims/wargoals are not enough for a high-chaos Volga restoration. It needs separate governance, river economy, military, and expansion branches.
- Full custom splinter trees with zero decision and direct expansion hooks (`BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `NLC`) are structurally present but still read as variants of one template.
- Ancient restorations (`KZR`, `SOG`, `KHW`, `ALN`) are 16-focus packages. They need distinct legitimacy, old-border proof, route-choice, claim, integration, and AI behavior before they can be considered deep trees.
- Ordinary shared republic trees (`breakaway`, `internal`, `Baltic`, `Moldova`) need decision loops and route-specific payoff if used for long-lived player countries.

Reward simplification:
- Direct idea stacking has been cleaned from focus rewards, but helper rhythm remains repetitive. The top helper calls are `soviet_collapse_apply_focus_legal_recognition` x305, `soviet_collapse_apply_focus_depot_and_supply_control` x258, `soviet_collapse_apply_focus_military_consolidation` x254, `soviet_collapse_apply_focus_league_preparation` x220, and `soviet_collapse_apply_focus_foreign_channel` x176.
- `soviet_collapse_update_consolidated_republic_ideas` is guarded by `soviet_collapse_republic_staged_idea_recently_changed` and `NOT = { has_idea = ... }` checks, so it is not direct focus spam, but it concentrates spirit progression behind a shared helper.
- Setup helpers still add starting ideas for many successor tags. Some are guarded with `NOT = { has_idea = ... }`; some are unguarded one-time setup calls. This is outside the focus reward surface but should be kept in mind if release setup can ever be rerun.

## Icon Coverage Table

Sprite-definition validation was skipped because the user forbade GFX/sprite/asset inspection.

| File | Missing focus icon assignment | Repeated icon groups | Top repeated focus icons |
|---|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 0 | 22 | `GFX_focus_soviet_collapse_guard_the_radio_stations` x4, `GFX_ukr_soviet_collapse_democratic` x4, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` x4, `GFX_focus_soviet_collapse_steppe_supply_congress` x4 |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 99 | `GFX_focus_FEV_diplomatic_plan` x4, `GFX_focus_SZA_diplomatic_plan` x4, `GFX_focus_MRC_civil_rule` x4, `GFX_focus_MRC_foreign` x4 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 11 | `GFX_focus_CFR_municipal_board_elections` x3, `GFX_focus_CFR_concrete_republic` x3, `GFX_focus_CFR_the_builder_state` x3 |
| `005_soviet_collapse_ancient_restorations.txt` | 0 | 8 | Seven ancient restoration icon families repeat x4 across the four trees. |

Icon conclusion: no focus is missing an icon assignment in script. The unique-icon requirement is still not met because many icon families repeat, especially in templated custom splinters and ancient restorations. Actual asset work is out of scope for this pass.

## Localisation And Reward Mismatch List

Localisation:
- Missing focus names: 0.
- Missing focus descriptions: 0.
- Localisation was not edited.

Reward/content mismatches:
- `PRA_claim_the_branch_lines` promises branch-line claims, but its reward is rail/infrastructure construction plus a decision tooltip. It should either add actual rail-junction claims/objectives or be renamed around repair/control.
- `TSC_claim_the_impact_zone` does not add a claim or target-state mission; it only advances authority/high-chaos helpers. It should create impact-zone claims, anomaly decisions, or a named state objective.
- `OGB_kazan_ferry_offices` uses random core industrial construction despite a named Kazan/Volga ferry premise. It should target Volga/Kazan river states or unlock a ferry/toll decision.
- `ARD_first_guard`, `ARD_war_plan`, `ARD_diplomatic_plan`, and several later ARD/NLC naval-polar focuses still lean on convoy or generic helper rewards instead of port control, naval warfare, dockyard policy, or Arctic route mechanics.
- `UWD_soviet_collapse_focus_tree` has the highest tiny-reward density; the worker directorate should unlock production/strike/committee mechanics rather than direct factory/equipment ladders.
- Ancient restoration endpoints read as large identity shifts, but the 16-focus tree shape and repeated icon families make them feel like compact variants of one template.

## AI Behavior Gaps

- Every focus has `ai_will_do`.
- `common/ai_strategy/005_soviet_collapse.txt` has route-aware AI for Ukraine, Belarus, Kazakhstan, and broad custom/high-chaos signature-force states.
- Most full custom splinters share generic signature-force strategies instead of tag-specific AI. They do not yet understand ports, rail junctions, mountain passes, host cavalry, factory contracts, polar survival, or Far Eastern patronage as country-specific behaviors.
- Naval actors (`NRF`, `ARD`, `KRS`, `NLC`) need AI for dockyard construction, convoy raiding/escort, coastal target selection, naval invasion preparation, and port defense.
- Death/high-chaos actors (`DSC`, `ICD`, `RMC`) need AI that escalates aggressively with chaos tier, casualties, conquered states, and neighboring weakness.
- Factory actors (`CFR`, `MFR`, `UWD`) need AI strategies tied to construction, arms output, client wars, production priorities, and contract/protectorate choices.

## Pathline And Layout Audit

Mechanical scan results:
- Duplicate focus ids: 0.
- Duplicate coordinates: 0.
- Same-row prerequisite line risks: 0.
- Vertical parent-child line-through-focus risks: 0.
- Mutual-exclusion line with another focus between endpoints: 0.
- Continuous focus panel approximate overlap: 0.

Remaining layout risks are wide mutual-exclusion lines or tight-but-not-line-breaking adjacency:
- `ukr_soviet_collapse_black_banner_compact` and `ukr_soviet_collapse_anatolian_grain_mission` are adjacent on row `y = 8` (`x = 31` and `x = 30`), but they are unrelated focuses and no prerequisite or mutual-exclusion line runs between them.
- `central_asia_soviet_collapse_local_republic_council` / `central_asia_soviet_collapse_military_border_authority`: same-row mutual exclusion with `dx = 8`.
- `blr_soviet_collapse_railway_neutrality` / `blr_soviet_collapse_rail_war_state`: same-row mutual exclusion with `dx = 5`.
- `blr_soviet_collapse_decentralized_detachments` / `blr_soviet_collapse_regular_forest_brigades`: same-row mutual exclusion with `dx = 6`.
- `kaz_soviet_collapse_league_resource_pool` / `kaz_soviet_collapse_foreign_technical_missions`: same-row mutual exclusion with `dx = 7`.
- `ARD_settlement` / `ARD_radical_turn`: same-row mutual exclusion with `dx = 6`.
- `CFR` strategy/governance forks and `MFR` route forks have very wide mutual-exclusion spans (`dx = 5` to `12`) because route endpoints are separated by design. These should be cleaned during route-layout redesign, not by isolated x-coordinate nudges.

## High-Priority Fixes First

1. Deepen `PRA`, `DSC`, `NRF`, `TSC`, `ICD`, and `RMC` into real special chaos trees or explicitly classify them as short crisis trees. For the user's objective, they should be deepened.
2. Expand `OGB` into a real Volga restoration package with governance, river economy, military guard, IUL rivalry/compact, and regional expansion/integration.
3. Convert templated 47-focus custom splinters into tag-specific mechanics. Start with `UWD`, `FEV`, `ARD`, `NLC`, `KRS`, `DHC`, `KHC`, and `IUL`.
4. Add postwar handling to expansion branches: claims, cores, integration missions, occupation decisions, protectorates, or border settlements.
5. Replace repeated tiny equipment/building rewards with focus-gated decisions, missions, state-targeted construction programs, route-specific units, or scripted mechanics.
6. Add tag-specific AI after mechanics exist so AI behavior can target the new systems rather than only changing production weights.
7. Run a visual/icon pass later when asset/GFX work is allowed. Do not try to solve unique icon coverage in this no-assets pass.

## Why No Gameplay Patch Was Applied

I did not patch the focus files because the requested narrow-safe categories were not present in a safe form:
- No focus reward currently has direct duplicate `add_ideas`, `add_timed_idea`, or `swap_ideas`.
- The direct idea effects are seven hidden cleanup `remove_ideas`, not stack additions.
- No duplicate coordinates, missing pathline blockers, or mutual-exclusion lines with another focus between endpoints were found.
- The remaining pathline concerns are wide route layout choices that should be fixed alongside route redesign.
- The remaining reward problems are broad depth/design issues, not isolated one-line fixes.

## Validation Run

Commands run:

```bash
python3 - <<'PY'
# Parsed the four focus files, counted focus trees/focus blocks, direct idea effects,
# flat reward effects, helper calls, icon assignments, search filters, ai_will_do,
# coordinates, prerequisites, mutual exclusions, and layout risks.
PY
```

Result:
- 41 focus trees, 1,698 focuses.
- Duplicate focus ids: 0.
- Missing `ai_will_do`: 0.
- Missing search filters: 0.
- Missing icon assignments: 0.
- Direct duplicate same idea in one focus: 0.

```bash
python3 - <<'PY'
# Checked focus localisation against localisation/english/*005_soviet_collapse*_l_english.yml.
PY
```

Result:
- Missing focus names: 0.
- Missing focus descriptions: 0.

```bash
python3 - <<'PY'
# Checked bracket depth for all four focus files plus Event 005 scripted effects and AI strategy.
PY
```

Result:
- Final depth 0 and minimum depth 0 for all checked files.
- Unsupported `<=`/`>=`: 0 matches.

## Skipped Validation

- Sprite/GFX/icon-definition validation skipped because the user forbade touching or inspecting GFX/sprite/asset surfaces.
- In-game UI screenshot validation skipped; this pass used script and coordinate checks only.
- No gameplay-patch validation was run because no gameplay file was changed.

## Remaining Route Risks

- Current trees are mechanically present but not fully fixed against the user's quality target.
- The direct idea-spam complaint appears resolved in current focus rewards, but the user-facing "samey national-spirit progression" concern remains through shared helper rhythm.
- Ukraine, Belarus, and Kazakhstan are the best republic surfaces but still need route-specific mechanics and postwar payoffs.
- Most custom splinters are full-sized but too templated; special chaos countries are compact and need the deepest redesign.
- The existing broad plan remains valid: `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets` for asset-boundary rules only
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
