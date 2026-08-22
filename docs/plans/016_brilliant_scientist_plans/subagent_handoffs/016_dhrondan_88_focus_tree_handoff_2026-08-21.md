# Empire of D'Rhonda 88-Focus Tree Handoff

Date: 2026-08-21

Owner: `/root/dhr_focus`

Status: Source implementation complete inside the focus-owned boundary, with binary icon production intentionally outside this assignment and HOI4 MCP visual evidence blocked by repeated server timeouts.

## Delivered scope

The dedicated tree id is `dhrondan_focus_tree` in `common/national_focus/016_dhrondan_focus_tree.txt`.
The source contains exactly 88 focuses divided into 8 survival focuses, 24 regime focuses with 8 for each leader, 10 laboratory-economy focuses, 12 army and predictive-warfare focuses, 8 orbital and air or naval support focuses, 8 diplomacy and intelligence focuses, 12 expansion and world-order focuses, and 6 enclave-crisis or late-game focuses.
The tree uses three mutually exclusive regime roots, ten Focus Navigation shortcuts, current vanilla search filters on every focus, unique icon tokens on every focus, route-specific inline AI, and four focus strategy plans.

## Changed files

- `common/national_focus/016_dhrondan_focus_tree.txt`
- `common/ideas/016_dhrondan_focus_ideas.txt`
- `common/script_constants/016_dhrondan_focus_constants.txt`
- `common/scripted_effects/016_dhrondan_focus_effects.txt`
- `common/scripted_triggers/016_dhrondan_focus_triggers.txt`
- `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`
- `interface/016_dhrondan_focus_icons.gfx`
- `localisation/english/016_dhrondan_focus_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_88_focus_tree_handoff_2026-08-21.md`

No DHR tag, history, character, event, decision, alien API, alien unit, contact-chain, model, portrait, binary image, or catalog file was edited by this worker.

## Exact branch inventory

| Family | Count | Entry | Capstone |
| --- | ---: | --- | --- |
| Survival | 8 | `DHR_beneath_an_alien_sky` | `DHR_convene_the_two_world_throne` |
| Vael IX, Imperial Continuity | 8 | `DHR_vael_ix_takes_the_throne` | `DHR_the_unbroken_imperial_line` |
| Sera Qel, Predictive Synod | 8 | `DHR_sera_qel_presents_the_calculus` | `DHR_the_government_of_certainties` |
| Ilyr Ren, Two-World Covenant | 8 | `DHR_ilyr_ren_opens_the_chamber` | `DHR_the_chamber_of_two_skies` |
| Laboratory economy | 10 | `DHR_relight_the_field_laboratories` | `DHR_a_two_world_research_complex` |
| Army and predictive warfare | 12 | `DHR_restore_the_predictive_staff` | `DHR_perfect_predictive_warfare` |
| Orbital, air, and naval support | 8 | `DHR_reassemble_the_orbital_office` | `DHR_make_near_space_ours` |
| Diplomacy and intelligence | 8 | `DHR_open_the_translation_bureaus` | `DHR_the_embassy_beyond_the_stars` |
| Expansion and world order | 12 | `DHR_define_the_two_worlds_question` | `DHR_a_place_in_the_world_order` |
| Enclave crisis and late game | 6 | `DHR_the_enclaves_refuse_the_ledger` | `DHR_the_century_beyond_exile` |

## Regime integration

`DHR_vael_ix_takes_the_throne` sets `dhrondan_imperial_route`, applies `DHR_IMPERIAL`, and calls `dhrondan_install_imperial_regime`.
`DHR_sera_qel_presents_the_calculus` sets `dhrondan_synod_route`, applies `DHR_SYNOD`, and calls `dhrondan_install_synod_regime`.
`DHR_ilyr_ren_opens_the_chamber` sets `dhrondan_covenant_route`, applies `DHR_COVENANT`, and calls `dhrondan_install_covenant_regime`.
The country-runtime owner confirmed these exact roots and helpers.
Sera's Synod intentionally maps to neutrality, while Ilyr's Covenant maps to democratic and Vael remains mechanically distinct through his leader, route, cosmetic, AI, spirit, expansion, and crisis behavior.

## Landing and unit contract

`dhrondan_focus_enable_landing_network` sets `dhrondan_landing_network_enabled`, keeps `dhrondan_alien_infantry_training_forbidden` set, and assigns `dhrondan_landing_equipment_cost` from the generic API's `constant:alien_infantry_landing.reserve_equipment`.
The shared constant is exactly 2,000.
The first survival focus also establishes the no-training flag, and the country-runtime owner independently initializes that flag before the first focus can complete.
The tree and its support effects contain no division creation, template grants, stockpile grants, free equipment, equipment production lines, or normal alien-infantry training.
`DHR_feed_the_landing_reserve` only authorizes a paid request; it does not reserve or consume equipment.

## National-spirit lifecycle

The political slot moves from fragmentation to cohesion and then to exactly one of the Imperial Mandate, Synod Calculus, or Covenant Compact.
The military slot moves from Predictive Lag to Predictive Sight and then Predictive Command.
The corridor slot moves from Off-World Isolation to the Restored Relay and then the Homeworld Corridor.
Every helper clears its full family before adding the next stage.
The maximum simultaneous focus-created spirit count is therefore three.

## Reward and balance decisions

Survival steps use 21-day to 35-day durations, institutional focuses use 35-day or 56-day durations, route and branch capstones use 70 days, and enclave-crisis steps use 49 days before 70-day late-game capstones.
The tree distributes 16 research bonuses, 15 political-power rewards, 14 army-experience rewards, 11 command-power rewards, 11 stability rewards, 7 war-support rewards, 4 air-experience rewards, 2 naval-experience rewards, four civilian-factory calls, three military-factory calls, three ground-logistics calls, one air and radar relay call, and one coastal dockyard call.
Those direct rewards are paired with lifecycle transitions and stable decision or event hooks rather than repeated modifier-only ladders.
The only focus-created research-slot grant is the laboratory capstone `DHR_a_two_world_research_complex`.
The interrupted scaffold's `add_cic = 1` was removed because it affects the CIC bank rather than constructing a civilian factory.
The malformed `add_equipment_production` block was removed because the documented effect requires a nested equipment definition and would create a free production line contrary to the paid-landing boundary.
Factory rewards now use vanilla-style state-scoped `add_building_construction` helpers.
All fourteen idea modifier names were matched to headings in the installed `modifiers_documentation.md`, and all ten research-bonus categories were matched to the installed vanilla technology-category registry.

## AI behavior

`DHR_focus_opening_plan` prioritizes the survival trunk and aborts after a route flag is set.
The Imperial plan prioritizes predictive warfare, orbital security, coercive reclamation, and cipher suppression.
The Synod plan prioritizes laboratories, predictive warfare, calculated reclamation, and cipher suppression.
The Covenant plan prioritizes diplomacy, research, orbital support, negotiated federation, and reconciliation.
The three route roots and the crisis fork also carry scenario-sensitive inline weights.

## Layout and manual review evidence

Every focus was manually reviewed for title, description, identifier, icon token, coordinates, duration, prerequisites, mutual exclusions or route availability, filters, completion reward, and AI block.
The source audit found 88 unique focus ids, 88 unique coordinates, 88 matching base icon sprites, 88 matching shine sprites, 88 title keys, 88 description keys, no missing focus references, and no duplicate localisation keys.
All 88 focuses contain a search filter, a completion reward, and an `ai_will_do` block.
A source-coordinate graph pass found 102 prerequisite edges, zero proper connector crossings, zero connectors passing through another focus node, and zero connectors exceeding the configured long-connector threshold.
The upper survival fan anchors the four outer support families, the three political routes occupy symmetric central lanes, expansion converges beneath the route capstones, and the enclave crisis remains centered below the convergence.

## Focus icon handoff

`interface/016_dhrondan_focus_icons.gfx` registers 88 base focus sprites, 88 shine sprites, and 11 lifecycle idea sprites.
The 99 unique DDS paths are currently absent by instruction because this worker was forbidden to create binary art.
Focus textures use `gfx/interface/goals/016_dhrondan_focus/<family>/goal_<focus_id>.dds`.
Idea textures use `gfx/interface/ideas/016_dhrondan_focus/<idea_id>.dds`.
Required family folders and palettes are survival amber, Imperial violet-gold, Synod cyan-silver, Covenant teal-white, laboratory electric blue, army crimson, orbital indigo, diplomacy green, expansion gold-red, and crisis white-magenta.

## Mandatory MCP focus workflow

The installed HOI4 MCP focus routes were invoked against `common/national_focus/016_dhrondan_focus_tree.txt` and `dhrondan_focus_tree`.
`hoi4.focus_inspect` timed out with `timed out awaiting tools/call after 180s`.
`hoi4.focus_render` timed out with `timed out awaiting tools/call after 180s`.
`hoi4.focus_rewrite` was first invoked in authored mode and correctly rejected the call because a complete plan payload is required for authored mode.
The supported existing-tree compact rewrite was then invoked and timed out with `timed out awaiting tools/call after 180s`.
The pre-call and post-call SHA-256 hashes were identical, and the focus count remained 88, so the timed-out rewrite did not partially modify the source.
The installed tool surface exposes no `hoi4.focus_compare` route.
Because inspect, render, and rewrite did not return artifacts, no MCP post-rewrite comparison or normal-zoom rerender could be completed, and source-side geometry checks are not claimed as equivalent engine evidence.

## Localisation and interface evidence

`localisation/english/016_dhrondan_focus_l_english.yml` contains 215 unique keys and is UTF-8 with BOM.
It uses no `:0` version suffixes and has no indented key declarations.
The paid landing tooltips explicitly state the 2,000-weapon cost and that no free unit or equipment is granted.
The interface registry and focus icon references have exact one-to-one base and shine coverage.

## Remaining work and blockers

- Produce the 88 focus DDS files and 11 lifecycle idea DDS files at the registered stable paths through the separate asset workflow.
- Re-run `hoi4.focus_inspect`, `hoi4.focus_render`, `hoi4.focus_rewrite`, and a post-change render or supported comparison when the MCP server can return within its 180-second deadline.
- Runtime acceptance remains external for loaded-tree behavior, cosmetic regime transitions, paid-landing consumption, and state-dependent factory placement.

No gameplay route, focus, localisation entry, focus AI surface, navigation shortcut, lifecycle stage, landing-cost contract, or requested cross-system hook was simplified or omitted inside the focus-owned source boundary.
The absent binary icons and unavailable MCP artifacts are explicit external blockers rather than silent fallbacks.
