# Soviet Collapse Focus Full Rework Audit Current Handoff

Subagent: Chaos Redux focus tree subagent
Date: 2026-05-29
Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

This pass made one high-confidence local patch. It does not complete the requested full focus tree rework; the remaining work is broad route-family redesign.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla references: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`, and focus precedents in `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt` and `latvia.txt`.

## Changed Files

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_full_rework_audit_current_handoff.md`

Pre-existing dirty work was present in the focus files before this patch, including layout changes in `005_soviet_collapse_custom_splinters.txt` and `005_soviet_collapse_factory_successors.txt`. This handoff only claims the war-goal patch listed below.

## Changed Focus IDs

| Focus id | File | Before | After | Reason |
|---|---|---|---|---|
| `CFR_the_builder_state_marches_east` | `common/national_focus/005_soviet_collapse_factory_successors.txt` | Focus used `FOCUS_FILTER_ANNEXATION`, title implied eastward advance, and hidden AI pushed `conquer`/`antagonize` against `SOV`, but the reward did not grant a war goal. | Completion reward now grants `annex_everything` war goal on `SOV` when `SOV` exists, the country is not already at war with `SOV`, has no duplicate war goal, and can declare war. | Aligns reward, filter, title, and AI behavior with existing endpoint patterns in the same event content. |

## Route Behavior Before And After

Before: the CFR route had an aggressive eastward endpoint that only improved public works, war support, a decision tooltip, and AI hostility. The AI could want conquest without receiving the promised player-facing war goal.

After: the same route still unlocks reconstruction contract behavior and AI hostility, but now also gives a direct no-expiry annexation war goal on `SOV` when valid. No localisation keys or icon ids changed.

## Route Coverage Table

| Tree or group | Focus count | Coverage status | Main issue |
|---|---:|---|---|
| `soviet_collapse_ukraine_focus_tree` | 83 | Broad political, military, industrial, and state identity coverage. | Expansion is not a distinct enough route surface for the requested OP/aggressive chaos goal. |
| `soviet_collapse_breakaway_focus_tree` | 36 | Moderate shared breakaway coverage. | Needs stronger branch identity and less helper-led reward repetition. |
| `soviet_collapse_internal_republic_focus_tree` | 62 | Broad shared internal republic coverage. | Lacks enough visible conquest, cores, special mechanics, and route-specific end states. |
| `soviet_collapse_baltic_focus_tree` | 42 | Political and diplomatic coverage present. | Expansion and special mechanics are thin. |
| `soviet_collapse_caucasus_focus_tree` | 40 | Political and local consolidation coverage present. | Needs more state-concept mechanics, war goals, cores, and regional crisis hooks. |
| `soviet_collapse_central_asia_focus_tree` | 45 | Regional consolidation coverage present. | Needs stronger special mechanics and aggressive endpoint behavior. |
| `soviet_collapse_moldova_focus_tree` | 48 | Political, military, and corridor identity coverage present. | Needs deeper expansion/diplomacy payoff and route-specific decisions. |
| `soviet_collapse_belarus_focus_tree` | 53 | Broad route skeleton present. | Rewards remain helper-heavy and need distinct political/military/diplomatic outcomes. |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | Largest republic tree with substantial route surface. | Needs manual reward-variety audit and clearer expansion mechanics. |
| Full custom splinters `BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC` | 47 each | Political, industry, military, diplomacy, and endpoint hooks mostly exist. | Many trees still read as templated; OP chaos-country aggression is uneven. |
| Crisis/custom shallow splinters `PRA/TSC/RMC/DSC/NRF/ICD` | 18-22 each | Basic crisis identity exists. | Too shallow for the requested full country-depth rework. |
| `CFR_soviet_collapse_focus_tree` | 47 | Real political, industrial, diplomacy, and expansion branches exist. | Some reward/filter mismatch remains; icon reuse and helper patterns need cleanup. |
| `OGB_soviet_collapse_focus_tree` | 23 | Basic successor identity exists. | Too shallow for a high-chaos successor and needs military/industrial/special depth. |
| `MFR_soviet_collapse_focus_tree` | 58 | Stronger factory-successor coverage with industry/military routes. | Expansion and state-concept mechanics are still thin. |
| Ancient trees `KZR/SOG/KHW/ALN` | 16 each | Minimal ancient restoration skeletons exist. | These are stub-depth trees, not full restoration route families. |

## Missing Or Simplified Content List

High-priority issues first:

1. `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: `KZR_soviet_collapse_ancient_focus_tree`, `SOG_soviet_collapse_ancient_focus_tree`, `KHW_soviet_collapse_ancient_focus_tree`, and `ALN_soviet_collapse_ancient_focus_tree` are only 16 focuses each. They need full political, industrial, military, diplomacy, expansion, and special-mechanic branches.
2. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, and `ICD_soviet_collapse_focus_tree` are 18-focus crisis trees. `PRA_soviet_collapse_focus_tree` has 22 focuses. These are simplified compared to the requested full chaos-country depth.
3. `common/national_focus/005_soviet_collapse_factory_successors.txt`: `OGB_soviet_collapse_focus_tree` has 23 focuses and needs full successor depth, not only a compact branch set.
4. `common/national_focus/005_soviet_collapse_republics.txt`: the shared republic trees have broad size, but many rewards rely on repeated helper effects instead of concrete route-specific gameplay. The worst review targets are `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_belarus_focus_tree`, and `soviet_collapse_kazakhstan_focus_tree` because they are large enough that helper repetition hides route behavior.
5. `common/national_focus/005_soviet_collapse_custom_splinters.txt`: most 47-focus custom splinter trees need more bespoke country mechanics. Current branch coverage exists, but too many countries share similar reward rhythms.
6. All four focus files: direct idea spam is removed from the surface, but helper overuse remains heavy. Current helper counts are high: `soviet_collapse_apply_focus_legal_recognition` 299 calls, `soviet_collapse_apply_focus_depot_and_supply_control` 257 calls, `soviet_collapse_apply_focus_military_consolidation` 252 calls, `soviet_collapse_apply_focus_league_preparation` 220 calls, `soviet_collapse_apply_focus_foreign_channel` 176 calls, and `soviet_collapse_apply_focus_high_chaos_identity` 96 calls.

## Icon Coverage Table

| File or group | Missing icon assignments | Missing `.gfx` definitions | Reuse risk |
|---|---:|---:|---|
| `common/national_focus/005_soviet_collapse_republics.txt` | 0 | 0 | 22 repeated icon ids; top repeats include `GFX_ukr_soviet_collapse_democratic`, `GFX_moldova_soviet_collapse_ukrainian_corridor`, `GFX_focus_soviet_collapse_steppe_supply_congress`, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow`, `GFX_focus_soviet_collapse_guard_the_radio_stations`, `GFX_central_asia_soviet_collapse_steppe_federation`, and `GFX_central_asia_soviet_collapse_rail_and_irrigation_boards`. |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 0 | 0 | 99 repeated icon ids; top repeats include `GFX_focus_SZA_diplomatic_plan`, `GFX_focus_MRC_foreign`, `GFX_focus_MRC_civil_rule`, `GFX_focus_IUL_war_plan`, `GFX_focus_IUL_supply`, and `GFX_focus_FEV_diplomatic_plan`. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | 0 | 0 | 11 repeated icon ids; top repeats include `GFX_focus_CFR_the_builder_state`, `GFX_focus_CFR_municipal_board_elections`, `GFX_focus_CFR_concrete_republic`, and `GFX_focus_CFR_civilian_hegemony_project`. |
| `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | 0 | 0 | 8 repeated icon ids, mostly repeated once per ancient tree: `GFX_focus_soviet_collapse_ancient_workshop_compact`, `GFX_focus_soviet_collapse_ancient_symbolic_state`, `GFX_focus_soviet_collapse_ancient_returned_names_endgame`, `GFX_focus_soviet_collapse_ancient_restoration_survives`, `GFX_focus_soviet_collapse_ancient_old_border_files`, `GFX_focus_soviet_collapse_ancient_league_bargain`, and `GFX_focus_soviet_collapse_ancient_guard_old_routes`. |

## Localisation And Reward Mismatch List

| Item | File | Identifier | Status |
|---|---|---|---|
| Missing focus names/descriptions | All four scoped focus files against Soviet Collapse localisation files | 1698 focus ids audited | No missing title or description keys found in the current workspace. |
| Direct idea spam | All four scoped focus files | Direct `add_ideas` and `add_timed_idea` scan | No direct focus-surface idea additions found. Rewards now mostly flow through helper effects and concrete rewards. |
| Filter/reward mismatch patched | `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR_the_builder_state_marches_east` | Patched with `annex_everything` war goal on `SOV`. |
| Remaining filter/reward mismatch risk | `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR_build_the_border_bend_the_border` | Uses `FOCUS_FILTER_ANNEXATION` but appears to reward border-permit/public-works logic rather than a direct claim, core, war goal, or state transfer. Needs route-design decision before patching. |
| Helper-only/repeated reward risk | `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree`, `soviet_collapse_belarus_focus_tree`, `soviet_collapse_kazakhstan_focus_tree` | Large trees still need manual branch-by-branch reward matching so focus names and descriptions promise concrete gameplay that the reward delivers. |
| Helper-only/repeated reward risk | `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 47-focus custom splinter trees and crisis splinter trees | Many routes remain mechanically similar despite distinct country names. Needs bespoke decisions, state mechanics, unit/template spawns, and expansion tools. |
| Stub-depth reward risk | `common/national_focus/005_soviet_collapse_ancient_restorations.txt` | `KZR/SOG/KHW/ALN` ancient trees | Focus names imply restoration arcs, but 16-focus depth cannot support the requested political/industrial/military/diplomacy/expansion/special route spread. |

## AI Behavior Gaps

- Every audited focus has an `ai_will_do` block, so there are no missing AI-weight blocks.
- Route-aware AI is uneven. Many focuses use simple base weights or generic crisis modifiers instead of route-specific aggression, branch invalidation, sponsor behavior, target-state logic, or endpoint priorities.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: high-chaos custom countries need systematic `add_ai_strategy` support for conquest, anti-SOV behavior, regional rivals, and League/faction decisions. Current endpoint aggression exists in spots but is not comprehensive.
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: `CFR_the_builder_state_marches_east` now aligns AI conquest with a war goal, but `CFR_build_the_border_bend_the_border`, `OGB_soviet_collapse_focus_tree`, and some `MFR` branches still need deeper route-aware AI.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: ancient restoration AI is too compact to express aggressive restoration behavior beyond small endpoint choices.
- `common/national_focus/005_soviet_collapse_republics.txt`: republic AI is present but needs stronger distinction between defensive consolidation, diplomatic recognition, civil-war cleanup, and conquest routes.

## High-Priority Fixes For Parent

1. Expand ancient restoration trees `KZR/SOG/KHW/ALN` from 16-focus stubs into full route families with restoration politics, old-border claims, elite/army conflict, industrial revival, diplomacy, expansion, state mechanics, and AI aggression.
2. Deepen shallow crisis/custom splinters `PRA/TSC/RMC/DSC/NRF/ICD` and `OGB` before polishing larger trees; these are the clearest failures against the full rework requirement.
3. Replace repeated helper-only rewards with concrete gameplay per route: war goals, claims, cores, units, templates, decisions, missions, state flags, scripted state concepts, advisors, leader changes, and event hooks.
4. Audit `CFR_build_the_border_bend_the_border`; either add a concrete border/claim/war-state payoff or replace `FOCUS_FILTER_ANNEXATION` with a filter that matches its actual reward.
5. Add route-aware AI strategies to all OP chaos countries, with aggressive conquest and target selection where the focus text implies expansion.
6. Add or assign more specific icons for repeated-icon clusters, prioritizing `custom_splinters`, `CFR`, and ancient restorations.

## Validation Run

- Bracket balance check over all four scoped focus files: final depth `0`, minimum depth `0` for all files.
- Duplicate focus id audit over all four scoped focus files: `0`.
- Focus count audit over all four scoped focus files: `41` focus trees, `1698` focuses.
- Missing icon assignment audit: `0`.
- Missing `.gfx` definition audit for focus icons: `0`.
- Missing localisation name/description audit against Soviet Collapse localisation files: `0`.
- Non-downward prerequisite/pathline audit: `0` current cases found.
- Unsupported operator check across scoped focus files and directly relevant Soviet Collapse decision/effect/trigger files: no `<=` or `>=` matches.
- `git diff --check` passed for the patched focus file and this handoff.

## Skipped Validation

- No in-game launch or screenshot validation was run in this subagent scope.
- No broad route redesign implementation was attempted because it exceeds the allowed small/local patch boundary.
- No localisation validation command was rerun after writing this handoff because no localisation files were changed.

## Remaining Route Risks

- The full focus tree rework goal remains incomplete. Current content is much improved structurally, but route depth and bespoke mechanics still do not meet the full requirement across all trees.
- The broadest unresolved design risk is that many countries have route labels without enough distinct route gameplay.
- Aggression is partial. Several endpoints grant claims or war goals, but chaos countries are not yet consistently overpowered through units, templates, cores, decisions, state mechanics, and AI strategy.
- Icon coverage is technically valid, but repeated icon ids still weaken readability.
- Existing dirty work in the workspace means parent review should isolate this patch carefully before committing.

## Plan Handoff

No new broad plan was written in this pass. The existing broader implementation handoff remains relevant:

`docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
