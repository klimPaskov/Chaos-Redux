# Event 014 Cannibalism focus-tree audit handoff

Audit stage: Event 014 focus trees and their linked AI, decisions, effects, ideas, localisation, icons, unit unlocks, and terminal gates.

Decision: source audit is complete; no gameplay or asset files were edited.

## Scope and evidence boundary

The primary source is `common/national_focus/014_cannibalism_focus.txt`.

Linked source surfaces reviewed are `common/script_constants/014_cannibalism_constants.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_effects/014_cannibalism_activation_effects.txt`, `common/decisions/014_cannibalism_decisions.txt`, `common/decisions/categories/014_cannibalism_categories.txt`, `common/ideas/014_cannibalism_ideas.txt`, `common/ai_strategy/014_cannibalism_warlords.txt`, `common/units/014_cannibalism_irregular_infantry.txt`, `common/technologies/014_cannibalism_irregular_activation_technologies.txt`, `interface/014_cannibalism.gfx`, and `localisation/english/014_cannibalism_l_english.yml`.

The Event 014 focus architecture, route matrix, acceptance criteria, hidden-identity audit, AI matrix, and idea lifecycle matrix under `docs/specs/014_cannibalism_specs/` were read alongside the offline `paradox_wiki/` focus, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, AI, and national-focus pages.

Vanilla focus precedents and the installed documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` were consulted, including `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.

The HOI4 MCP requirement was exercised before this report. `hoi4.focus_inspect` for the Event 014 focus source timed out after 180 seconds, including a three-tree attempt and bounded single-tree attempts. `hoi4.focus_render` for the warlord tree also timed out after 180 seconds. The current tool surface exposed no focus-specific lint or compare route. `hoi4.focus_rewrite` exposes apply/write parameters but no dry-run plan schema, so it was not called during this audit-only task. These failures are engine-evidence blockers, not proof that the source is engine-safe.

The mandatory probability route was also exercised and stopped after the parent-directed cutoff. `hoi4_probability_inspect` accepted the national-focus source shape but timed out after 180 seconds, both without and with a disposition candidate pool. The required `chaosx_ai_probability_auditor` scenario evidence for focus selection is therefore unresolved.

## Route coverage

| Family | Implemented coverage | Source identifiers and evidence |
| --- | --- | --- |
| Unified Hannibal tree | Exactly 108 focuses, within the required 96–120 range. Opening convergence, three mutually exclusive disposition routes, three mutually exclusive supreme-hierarchy routes, shared Continental Larder trunk plus four methods, army, navy, air, intelligence/cells, expansion, counterwar, and ordinary terminal are all present. | Tree starts at `CBL_reveal_the_command` line 47 and ends at `CBL_dismantle_the_ordinary_world` line 1491. Section comments at lines 43–1465 document 8/15/15/23/14/8/7/8/4/4/2 focus groups. Representative route IDs include `CBL_keep_the_lieutenants`, `CBL_break_the_warlords`, `CBL_chain_the_rivals`, `CBL_one_command`, `CBL_many_jaws`, `CBL_ritual_administration`, `CBL_burn_through_the_near_states`, `CBL_preserve_the_working_herds`, `CBL_prisoner_trains`, and `CBL_mark_the_battlefield_yields`. |
| Local warlord tree | Exactly 68 focuses. Survival trunk, personal tyranny, Feast council, Pack-captain confederacy, Larder policy, military organization, Island/Siege/March origin overlays, regional predation, terror/infiltration, and Evolution II network alignment/manipulation/defiance are present. | Tree starts at `cannibalism_warlord_survive_the_first_encirclement` line 1550 and ends at `cannibalism_warlord_independent_regional_host` line 2915. Section comments at lines 1545–2728 document the route families. Representative IDs include `cannibalism_warlord_seize_the_knives`, `cannibalism_warlord_divide_the_first_table`, `cannibalism_warlord_free_the_captains`, `cannibalism_warlord_rapid_consumption`, `cannibalism_warlord_managed_herds`, `cannibalism_warlord_mobile_larder`, `cannibalism_warlord_island_archipelago_hunt`, `cannibalism_warlord_siege_city_that_eats`, `cannibalism_warlord_march_moving_front`, `cannibalism_warlord_accept_the_common_symbols`, `cannibalism_warlord_copy_the_shared_doctrine`, and `cannibalism_warlord_execute_the_couriers`. |
| Wendigo Hannibal overlay | Exactly 28 focuses. Five merge-trunk, five winter-hunger, five recruitment, five cannibal-legacy, five transformation-countdown, and three alternate-terminal focuses preserve the existing Wendigo route and delegate final locking to the transformation pulse. | Tree starts at `ZZZ_wendigo_bind_the_two_hungers` line 2978 and ends at `ZZZ_wendigo_the_world_beneath_winter` line 3581. Section comments at lines 2973–3529 document the 5/5/5/5/5/3 split. Representative IDs include `ZZZ_wendigo_preserve_the_pack`, `ZZZ_wendigo_raise_the_first_anchors`, `ZZZ_wendigo_open_the_winter_hunt`, `ZZZ_wendigo_drill_the_original_pack`, `ZZZ_wendigo_keep_the_cannibal_legions`, `ZZZ_wendigo_all_inheritances_intact`, `ZZZ_wendigo_begin_the_countdown`, and the three terminal-hunt IDs. |

The static prerequisite graph has zero dangling focus references and zero structurally unreachable focuses in all three trees when separate prerequisite blocks are treated as AND and alternatives in one block as OR, matching the offline wiki semantics. Mutual exclusions are symmetric: ten unified nodes form the disposition, hierarchy, and four-method Larder groups; nine warlord nodes form the hierarchy, Larder, and Evolution II policy groups; Wendigo has no mutually exclusive route-choice group. Coordinates are present and no tree contains duplicate `(x, y)` pairs. Source coordinates do not establish connector, hover, or rendered-column safety without the timed-out engine render.

## Rewards, integrations, and unit preservation

The focus blocks provide completion rewards and AI blocks for all 204 focuses. Static helper review shows route-specific effects for ideas, decisions, state/map operations, claims and integration, terminal packages, and unit/template unlocks rather than a focus tree made only of small modifiers.

Warlord reward hooks are visible in `cannibalism_warlord_focus_form_the_feast_cohorts`, `cannibalism_warlord_focus_train_the_origin_specialists`, and `cannibalism_warlord_focus_raise_the_bone_guard` around `common/scripted_effects/014_cannibalism_effects.txt:17551-17565`. The corresponding focus IDs are `cannibalism_warlord_form_the_feast_cohorts`, `cannibalism_warlord_train_the_origin_specialists`, and `cannibalism_warlord_raise_the_bone_guard`.

Unified army hooks include `cannibalism_unified_focus_bone_guard_command` at `common/scripted_effects/014_cannibalism_effects.txt:15943-15948`, the terminal army package around lines 15918–15930, and the Cannibal Legion, Bone Guard, Bone Riders, Scavenged Elephant, and origin-specialist template setup around lines 14746–14827.

Wendigo preservation is explicit: `cannibalism_wendigo_focus_preserve_the_pack` is at `common/scripted_effects/014_cannibalism_effects.txt:19326`, inherited templates and support stages are wired around lines 6821–6871, `cannibalism_wendigo_focus_all_inheritances_intact` is at line 19514, and `cannibalism_wendigo_focus_the_world_beneath_winter` is at line 19592. The source keeps existing Wendigo units and technology while adding paid Pack, inherited-origin, anchor, and winter-cell progression.

## Icons and localisation

The source contains 204 focus icon references. A static cross-reference found 204 normal and 204 shine sprite definitions in `interface/014_cannibalism.gfx`; the corresponding `gfx/interface/goals/014_cannibalism/` directory contains 204 expected DDS files, with no missing reference or filename.

The localisation file `localisation/english/014_cannibalism_l_english.yml` is UTF-8 with BOM. A non-anchored source scan found all 204 focus title keys, all 204 `_desc` keys, and all 204 distinct `custom_effect_tooltip` keys with non-empty localisation entries. Representative post-reveal keys are at `014_cannibalism_l_english.yml:982-983` and the ordinary/Wendigo terminal names at lines 1318 and 1403.

No pre-reveal warlord focus title or description exposes the Hannibal identity. The unified tree is gated by `cannibalism_unified_country`, `cannibalism_reveal_complete`, and `NOT = { has_country_flag = cannibalism_wendigo_hannibal_country }` at `014_cannibalism_focus.txt:31-33`. The warlord Evolution II network branch is gated by `cannibalism_evolution_ii_active` at lines 2738–2748. The Wendigo overlay requires the original ZZZ identity, `is_cannibalism_wendigo_hannibal_country`, the reveal flag, and the live Wendigo character at lines 2953–2965.

## Terminal gates and AI

The shared world-end constant is `cannibalism_evolution_threshold.world_end_chaos = 1000` at `common/script_constants/014_cannibalism_constants.txt:947`. Both ordinary terminal focuses require strict `global.chaos_meter_value > constant:cannibalism_evolution_threshold.world_end_chaos`, readiness, and their operational prerequisites at `014_cannibalism_focus.txt:1464-1507`. The corresponding effects repeat the strict gate at `common/scripted_effects/014_cannibalism_effects.txt:16183-16205`.

The ordinary readiness trigger at `common/scripted_triggers/014_cannibalism_triggers.txt:3434-3462` additionally checks operational packages, route state, network reach, controlled states, consumed population, and Larder. The Wendigo countdown trigger at lines 5364–5408 requires strict Chaos greater than 1000 plus anchors, network reach, controlled states, consumed population, winter victories, unified authority, and Larder. The Wendigo terminal focuses at `014_cannibalism_focus.txt:3532-3601` require that countdown readiness and active countdown; the pulse-owned world-end design matches the accepted spec.

Every focus has an `ai_will_do` block. Static review found route-aware constants and conditions across the three disposition/hierarchy/Larder families, origin overlays, network alignment, unified operational packages, terminal factors, and Wendigo pre-lock priorities. Two Wendigo bridge focuses have a flat base with no modifier: `ZZZ_wendigo_bind_the_two_hungers` at line 2978 and `ZZZ_wendigo_mark_the_irreversible_road` at line 3436. This is a review item, not a confirmed defect, because both are structural transition nodes rather than route-choice nodes.

The existing Event 014 probability manifests provide useful but non-equivalent evidence. `docs/plans/014_cannibalism_plans/probability_contracts/event014_ai_strategy_profiles.json` records `ai_strategy_factor`, `no_weighted_surfaces`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f9b360bd13cf61f9ac0fdd41f53b0d1352df14146a09f19f664e35d7385f158/627558277a60af17dbafc95a9223c4458d2ae65e8ac127f9f677dd998db93cec/probability-inspect-02bd4b54a3b6.json`. `event014_selector_contracts.json` records the incomplete `custom_weighted_pool` adapter and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7113f1b2aeb4c5e416d97f989fabed2142635f729244733f8e5da5644bb5c9d/a678dd5aa1c2bcfb5be56ea0becf5f2b5471fb39d30627635c017a0591eb18c5/probability-inspect-a2195480e458.json`. Neither artifact is a focus-selection probability result.

## Findings and priority

1. **HIGH — engine focus evidence is blocked.** `hoi4.focus_inspect` and `hoi4.focus_render` each hit the MCP 180-second timeout, so rendered overlap, connector crossings, engine prerequisite interpretation, and diagnostics remain unverified. Focus-specific lint and compare were not exposed, and rewrite dry-run is unavailable.

2. **HIGH — focus AI probability evidence is blocked.** The national-focus probability inspection hit the same 180-second timeout, so route selection has not received the mandatory scenario-specific auditor baseline. Static AI coverage is present, but it is not a substitute for MCP probability evidence.

3. **LOW/REVIEW — Wendigo bridge weighting.** Review `ZZZ_wendigo_bind_the_two_hungers` and `ZZZ_wendigo_mark_the_irreversible_road` after the probability route is healthy. Add a transition factor only if the scenario audit shows they starve the intended route; do not add arbitrary weight now.

No confirmed source defect was found in counts, route presence, prerequisite references, mutual exclusions, icon wiring, localisation coverage, reveal secrecy, strict terminal gates, Wendigo preservation, or unit unlock hooks. No route was simplified or silently substituted. The unresolved engine and probability evidence are the only completion limits from this audit.

## Exact follow-up patch and validation plan

1. Restart or repair the healthy HOI4 MCP service and run `hoi4.focus_inspect` for `cannibalism_warlord_focus_tree`, `cannibalism_unified_focus_tree`, and `cannibalism_wendigo_focus_tree`, followed by `hoi4.focus_render` for all three trees with review-scale output.

2. Run the available focus lint and compare routes, or record their exact unavailability again if the server still does not expose them. Capture the returned artifact URI, layout diagnostics, overlap/connector findings, and source-to-engine node counts.

3. Route focus AI through `chaosx_ai_probability_auditor` using named scenarios for warlord hierarchy/origin/Larder/network routes, unified disposition/hierarchy/Larder/terminal routes, and Wendigo pre-lock/post-lock behavior. Run the same scenarios through `hoi4.probability_inspect`, evaluation/sweep, and `hoi4.probability_compare` for any AI patch.

4. If engine output finds a visual or route defect, patch only the affected focus IDs in `common/national_focus/014_cannibalism_focus.txt`, then rerun inspect/render/lint/compare. If the Wendigo bridge audit finds starvation, make the smallest route-aware AI change and update only its existing localisation or helper hook if required.

5. Re-run the source checks recorded here: three-tree counts 108/68/28, zero dangling prerequisites, zero structural unreachable nodes, symmetric exclusions, 204/204 icon/GFX/DDS coverage, 204/204 title/description/reward-tooltip localisation, strict `> 1000` ordinary and Wendigo terminal gates, and preservation/unlock helper references.

This handoff intentionally contains documentation only. The parent agent must review the two HIGH blockers before making any gameplay change or completion claim.
