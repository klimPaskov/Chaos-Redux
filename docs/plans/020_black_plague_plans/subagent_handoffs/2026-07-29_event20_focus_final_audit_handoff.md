# Event 020 focus-tree final bounded audit handoff

## Scope and outcome

This audit covers `common/national_focus/020_black_plague_rat_focus_tree.txt`, `common/national_focus/020_black_plague_rat_king_focus_tree.txt`, their Event 020 focus localisation, and `interface/020_black_plague_rat_identity.gfx` after the prerequisite and country-package repairs. The audit did not redesign either tree, add a route family, create a formable chain, or wire 3D models.

Two hard route locks were patched. The base Rat convergence focus now accepts the one origin terminal that can exist for a fixed-archetype country, and the Rat King shared military lane now accepts the one government route that can exist because the three government routes are mutually exclusive. The custom focus sprites also received the required `_shine` companions described by the offline national-focus documentation.

## Changed files and identifiers

- `common/national_focus/020_black_plague_rat_focus_tree.txt:265-271`: `black_plague_rat_capped_pulses` changed from four separate AND prerequisites to one OR prerequisite containing `black_plague_rat_city_breachers`, `black_plague_rat_long_grass_ambush`, `black_plague_rat_wharf_raids`, and `black_plague_rat_frontline_burrows`.
- `common/national_focus/020_black_plague_rat_king_focus_tree.txt:267-272`: `black_plague_rat_royal_armouries` changed from three separate AND prerequisites to one OR prerequisite containing `black_plague_rat_court_of_teeth`, `black_plague_rat_warren_charter`, and `black_plague_rat_crown_of_ash`.
- `interface/020_black_plague_rat_identity.gfx:2-22`: added `_shine` sprite definitions for the eleven Event 020 custom focus goal sprites, using the same DDS and `gfx/FX/buttonstate.lua` effect as the regular sprite.

No focus localisation keys or reward blocks were changed.

## Route coverage

| Tree | Implemented coverage | Current gate behavior | Audit result |
| --- | --- | --- | --- |
| Rat Nation | Awakening and survival; four three-focus origin lanes; hierarchy; capped pulses, immune blood, annexation, and crown preparation | Urban, field, dock, or war archetype is fixed by the emergence effect; only the matching origin lane is available | The convergence gate was impossible before the patch and is reachable after the OR correction |
| Rat King | Coronation and stabilization; three mutually exclusive government lanes; shared royal forces; four crisis/knowledge focuses; terminal preparation and cohesion; route-completion flag | Exactly one government route can complete; shared military lane now accepts any completed government terminal | The shared-lane gate was impossible before the patch and is reachable after the OR correction |

The runtime Evolution V contract remains outside the focus tree. `black_plague_evolution_v_is_ready` in `common/scripted_triggers/020_black_plague_evolution_triggers.txt:142-184` consumes `black_plague_rat_king_route_completed` together with Dominion, Sentience, Cohesion, territory, capital, refuge, chaos, and death thresholds. `black_plague_rat_earned_terminal_route` sets that route flag, so no speculative Evolution V prerequisite was added to the focus.

## Missing or simplified content

- The Rat Nation tree contains 23 focuses while the accepted architecture targets roughly 40-50. Mutation, territorial plague economy, deeper military method, rival absorption, and proto-sentience lanes are simplified or absent.
- The Rat King tree contains 38 focuses while the accepted architecture targets roughly 70-100. Brood administration and supply, military-caste depth, plague mastery, captured knowledge depth, human population policy, continental campaign objectives, and a dedicated Evolution V world-end lane are simplified or absent.
- `Crowned Brood`, `Plague Mastery`, bespoke spirit lifecycles, deeper decision hooks, and bespoke Rat/Rat King 3D models remain explicitly deferred by the country-package and asset handoffs. The prior alias handoff maps the currently referenced spirit rewards to registered ideas; it does not claim the bespoke identities are implemented.
- The current tree does not have route-aware national-focus AI weighting. This is a design gap, not a safe one-line repair, because weights need the missing route families and balance matrix.

## Icon coverage

| Surface | Coverage | Finding |
| --- | --- | --- |
| Base and King focus icon tokens | Every token resolves against either mod or installed vanilla interface definitions in a direct scan | `hoi4.focus_inspect` still reports generic vanilla sprites as missing because its scan does not resolve the installed game's generic interface collection |
| Event 020 custom focus sprites | All nine custom tokens referenced by the two trees have a regular and `_shine` sprite; all eleven generated custom goal sprites now have both definitions | No remaining custom focus-sprite load/reference gap found |
| Focus-family depth | Most nodes still reuse generic vanilla icons and several generated custom sprites are currently unused (`first_warren`, `field_brood`, and `brood_council`) | Deferred asset/focus-family depth, not a load blocker |

The direct custom-sprite check confirmed `base=True; shine=True` for `GFX_goal_black_plague_rat_absolute_crown`, `GFX_goal_black_plague_rat_breath_hierophancy`, `GFX_goal_black_plague_rat_brood_signal`, `GFX_goal_black_plague_rat_dock_brood`, `GFX_goal_black_plague_rat_earned_terminal_route`, `GFX_goal_black_plague_rat_first_warren`, `GFX_goal_black_plague_rat_king_the_royal_basin`, `GFX_goal_black_plague_rat_urban_warren`, and `GFX_goal_black_plague_rat_war_brood`.

## Localisation and reward mismatch list

- `localisation/english/020_black_plague_rat_focus_l_english.yml` covers all 23 Base Rat focus title/description pairs and all 38 Rat King title/description pairs; no missing key was found.
- Current rewards are mostly flags, variables, division-cap changes, and the four registered rat ideas, and their wording is consistent with the current simplified implementation.
- The accepted design promises more route-specific spirits and campaign decisions than the current rewards provide; those are simplifications recorded above rather than localisation mismatches.

## AI behavior gaps

`common/ai_strategy/020_black_plague_rat_ai_strategy.txt` supplies generic Rat, archetype, and Rat King strategy plans for templates, fronts, and state targets. Neither focus tree has `ai_will_do`, `focus_factors`, or route-aware focus plans, so the AI receives default national-focus selection behavior. This should be addressed with the broader route-depth pass and the accepted AI strategy matrix; it was not patched in this bounded audit.

## Validation evidence

- `hoi4.focus_inspect` after the route patches and GFX additions returned the Base Rat artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f059329db125387b0078fb6995646d90a6b980bf2f0f179452f05c1e39e782b9/c1bce9ade25e8a0f20a5ac98a27149bdb583af0d0977799ed4b28b4090661481/focus-inspect.05608fcef0aec6bc.json` with 23 focuses, 25 connectors, zero connector crossings, zero node intersections, and 41 layout diagnostics.
- `hoi4.focus_inspect` after the route patches returned the Rat King artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/885aa0ab5fe19871e60c42fbfbe141e540b0d36c3596c14bd0eadd1a2477726b/14d9e20cb32de51eac25e637bbbbafff05f730dc841b5ca45a3b8f8be48aaf42/focus-inspect.bb0a39c91a7d1bb6.json` with 38 focuses, 47 connectors, zero connector crossings, zero node intersections, and 67 layout diagnostics.
- Earlier `hoi4.focus_render` artifacts remain available for visual review: Base SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/915b73c1e2237782b6c073f71240a4e016d2d9fccf2f3ad33204574d9541eadd/7ca4eb5480241cc1ed677169d4570807bdf8e84e051863538160ac9b069c9c0a/black_plague_rat_focus_tree.focus.svg` and Rat King SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9722427d3444893ecac2218bebc1a513e7638783363e78634634100f0b9ff3c9/2764cafa4b56f3e17eb8fdd075ff228af94026fc1a0ccbd8ab6de4d2f86bdb0a/black_plague_rat_king_focus_tree.focus.svg`.
- The direct icon scan resolved all focus icon tokens against mod and vanilla GFX definitions. The remaining inspector icon diagnostics are the known generic-vanilla scan limitation, not missing source sprites.
- No Hearts of Iron IV executable was launched. Live gameplay and consumer validation remain parent/user-owned.

## Remaining risks and handoff

The high-priority load and route-lock risks found in this bounded scope are patched. Remaining risk is the intentional shallow implementation relative to the accepted focus architectures and the absence of route-aware focus AI. Broader route expansion, bespoke spirits, campaign decisions, visual families, and 3D entities should be handled by the parent implementation plan rather than added in this audit.

This file is the subagent handoff path for parent review: `docs/plans/020_black_plague_plans/subagent_handoffs/2026-07-29_event20_focus_final_audit_handoff.md`.
