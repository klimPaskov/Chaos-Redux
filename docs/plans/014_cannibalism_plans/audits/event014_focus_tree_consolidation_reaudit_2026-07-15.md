# Event 014 Consolidated Focus-Tree Reaudit

Date: 2026-07-15

## Verdict

The consolidated Event 014 focus package passes the assigned final source, graph, route, reward, AI, gate, localisation, icon, and layout audit.

| Severity | Open |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

The live package contains exactly 68 Warlord focuses, 108 Unified CBL focuses, and 28 Wendigo focuses. All 204 IDs are unique. The three trees remain separate roots inside one current file, every prerequisite and mutual-exclusion reference resolves, every focus is reachable from its own root, all reward helpers and AI blocks are present, all focus-facing localisation and icons resolve, and the ordinary and Wendigo terminal paths retain strict chaos-above-1000 gates.

This audit also repaired the Warlord and Unified layouts. The repair changed 176 coordinate pairs only: all 68 Warlord focuses and all 108 Unified focuses. It did not change IDs, icons, costs, prerequisites, mutual exclusions, availability, bypasses, rewards, AI weights, gates, or helper calls. Wendigo coordinates and gameplay were left unchanged.

## Authorities and Audit Scope

The audit used the required repository guidance and both mandated reference sets:

- the offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, and Interface modding;
- vanilla documentation for script concepts and script constants, effects, triggers, and modifiers;
- vanilla focus precedents from the China Warlord and Austria trees;
- the Event 014 specifications and the previous Event 014 focus audit;
- the `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-events` repository skills.

The audited live focus source is:

- `common/national_focus/014_cannibalism_focus.txt`

Related consolidated constants, triggers, effects, localisation, interface registration, and texture files were inspected to prove the focus contracts. This report does not claim completion for unrelated Event 014 portrait, flag, audio, or country-package work.

## Consolidated Tree Inventory

The file contains exactly three top-level `focus_tree` blocks:

| Tree ID | Root focus | Focuses |
| --- | --- | ---: |
| `cannibalism_unified_focus_tree` | `CBL_reveal_the_command` | 108 |
| `cannibalism_warlord_focus_tree` | `cannibalism_warlord_survive_the_first_encirclement` | 68 |
| `cannibalism_wendigo_focus_tree` | `ZZZ_wendigo_bind_the_two_hungers` | 28 |
| **Total** | Three independent roots | **204** |

The offline National Focus wiki explicitly permits more than one `focus_tree` block in a file. The HOI4 focus inspector imported each tree by ID as exactly one tree, resolved every title, and returned no blocking diagnostic. Tree selection is additionally separated by the current country and identity gates described below, so the consolidation does not merge the graphs or create a loader ambiguity.

## Graph, Route, and AI Proof

| Metric | Unified | Warlord | Wendigo |
| --- | ---: | ---: | ---: |
| Focuses | 108 | 68 | 28 |
| Prerequisite blocks | 117 | 73 | 32 |
| Prerequisite edges | 132 | 79 | 32 |
| Mutual-exclusion references | 24 | 18 | 0 |
| Dangling prerequisite or mutex references | 0 | 0 | 0 |
| Asymmetric mutual exclusions | 0 | 0 | 0 |
| Parent at or below child | 0 | 0 | 0 |
| Duplicate focus positions | 0 | 0 | 0 |
| Missing completion reward/helper | 0 | 0 | 0 |
| Missing `ai_will_do` | 0 | 0 | 0 |
| Missing icon | 0 | 0 | 0 |

Every non-root node has an ancestry path to its tree root. The mutually exclusive route families are symmetric and remain satisfiable; no route lock points at an absent or downstream focus.

The current route families remain intact:

- Warlord: the survival trunk, three hierarchy routes, three Larder routes, Island/Siege/March origin overlays, and the Alignment/Manipulation/Defiance regional routes;
- Unified: warlord disposition, supreme hierarchy, continental Larder methods, army development, land/air/naval operational branches, expansion, counterwar, and ordinary terminal preparation;
- Wendigo: winter warfare, preserved cannibal inheritance, transformation anchors, acceleration/stabilisation, and the terminal hunt.

Focus costs retain the intended pacing:

| Cost class | Unified | Warlord | Wendigo |
| --- | ---: | ---: | ---: |
| Short | 74 | 45 | 7 |
| Normal | 25 | 23 | 18 |
| Terminal | 9 | 0 | 3 |

AI priority coverage is complete and uses the shared focus-priority constants:

| AI base | Unified | Warlord | Wendigo |
| --- | ---: | ---: | ---: |
| Maximum | 37 | 9 | 3 |
| Urgent | 32 | 20 | 11 |
| High | 29 | 30 | 13 |
| Standard | 10 | 9 | 1 |

These counts sum exactly to each tree's focus count. Route and capability modifiers remain attached to the authored AI blocks; the coordinate repair did not alter them.

## Reward and Decision-Hook Proof

Each of the 204 focuses calls exactly one tree-specific primary reward helper from its `completion_reward`. All 204 called helpers exist and are unique to their focus. Their normalized bodies are also unique, so no focus is a copied no-op reward alias.

The consolidated effect file contains 235 focus-prefixed helper definitions because some primary rewards delegate to subordinate finalizers. A broader current scan found 316 distinct country flags set by those focus-prefixed helpers. Every one of the 316 has at least one runtime `has_country_flag` consumer. This closes the stale façade problem recorded by the earlier focus audit: route flags now feed decisions, missions, dynamic modifiers, terminal readiness, achievements, package finalizers, or other live Event 014 control flow.

All focuses retain player-facing effect tooltips alongside their reward helper calls. No reward, helper, flag, or decision hook was changed during layout repair.

## Warlord Origin Contract

The Warlord tree has exactly three origin overlays, each with four focuses:

| Origin | Exact focus IDs |
| --- | --- |
| Island Host | `cannibalism_warlord_island_repair_the_ports`, `cannibalism_warlord_island_ambush_the_convoys`, `cannibalism_warlord_island_train_landing_cadres`, `cannibalism_warlord_island_archipelago_hunt` |
| Siege Commune | `cannibalism_warlord_siege_fortify_feeding_districts`, `cannibalism_warlord_siege_open_the_tunnels`, `cannibalism_warlord_siege_take_the_workshops`, `cannibalism_warlord_siege_city_that_eats` |
| March Host | `cannibalism_warlord_march_seize_wheels_and_mounts`, `cannibalism_warlord_march_raid_the_depots`, `cannibalism_warlord_march_sabotage_the_rails`, `cannibalism_warlord_march_moving_front` |

`constant:cannibalism_origin` retains only `none = 0`, `island_host = 1`, `siege_commune = 2`, and `march_host = 3`. No Prison Host origin constant, origin flag, idea, overlay focus ID, goal sprite, or current runtime/spec contract remains. General prisoner or depot mechanics are not origin definitions and were not incorrectly removed.

All 204 Warlord pre-reveal title, description, and tooltip values were scanned. None exposes Hannibal, Lecter, or Wendigo before the reveal.

## Country Gates and Wendigo Preservation

Tree and root gates remain canonical and disjoint:

- Unified requires CBL, `cannibalism_unified_country`, completed global reveal, and exclusion of the canonical Wendigo identity.
- Warlord requires `is_cannibalism_warlord_country`, the Event 014 focus slot, and opened Warlord decisions. Its root does not depend on or reveal the hidden Hannibal identity.
- Wendigo requires original tag ZZZ, `is_cannibalism_wendigo_hannibal_country`, completed reveal, Wendigo overlay availability, the Hannibal character, and no completed world end.

The canonical Wendigo predicate requires all three identity facts together:

- `cannibalism_wendigo_hannibal_country`;
- `weaponized_zombie_type_wendigo`;
- `original_tag = ZZZ`.

The Wendigo loader uses the same predicate and loads `cannibalism_wendigo_focus_tree` with `keep_completed = no`. It does not create a replacement country.

The pack-preservation contract is also live. `cannibalism_wendigo_focus_preserve_pack_contract` locks all division templates, disables recruitment and locks the existing Wendigo Pack template when present, and restores the zombie template priority and role ratio. Both `ZZZ_wendigo_preserve_the_pack` and `ZZZ_wendigo_drill_the_original_pack` call that helper. The original ZZZ country and its inherited pack therefore survive the route instead of being replaced by a parallel tag or generic template.

## Terminal-Gate Proof

The active terminal threshold is `constant:cannibalism_evolution_threshold.world_end_chaos = 1000`. The audited focus and terminal predicates use strict `greater_than`/`>` checks against that exact constant, so a chaos value of 1000 is insufficient.

The separate `constant:cannibalism_delta.world_end_chaos = 80` value is the active Chaos increase applied by the ordinary terminal effect. It is consumed by `cannibalism_apply_world_end_effect`; it is not an eligibility threshold and does not weaken either strict chaos-above-1000 gate.

The ordinary terminal trigger additionally requires the unified country, completed terminal route and operational packages, ordinary-scenario eligibility, no disabled/completed world end, network at least 92, more than 35 controlled states, at least 25,000,000 consumed population, and at least 750 Larder reserve. The final focus also requires mobilization preparation and repeats the strict chaos-above-1000 check.

The Wendigo countdown trigger additionally requires the canonical original-ZZZ Wendigo, completed winter network and terminal route, no locked/broken/disabled/completed world end, at least three anchors, network at least 85, more than 20 controlled states, at least 10,000,000 consumed population, at least five winter victories, authority at least 80, and at least 800 Larder reserve. The terminal lock further requires the ordinary scenario, an active countdown, the terminal route, and completed progress. No focus or hunt bypasses the lock helper to set the world end directly.

## Localisation and Icon Proof

The focus-facing localisation matrix is complete:

| Check | Result |
| --- | ---: |
| Expected title/description/tooltip keys | 612 |
| Missing keys | 0 |
| Duplicate keys | 0 |
| Empty values | 0 |
| UTF-8 BOM | Present |

The focus icon matrix is likewise complete:

| Check | Result |
| --- | ---: |
| Focus icon references | 204 |
| Unique base sprite definitions | 204 |
| Missing or duplicate base definitions | 0 |
| Missing shine definitions | 0 |
| Unique texture files | 204 |
| Missing texture files | 0 |
| Invalid DDS dimensions | 0 |
| Duplicate texture hashes | 0 |

All 204 textures are valid 94 by 86 DDS focus icons. No portrait or flag asset was changed by this audit.

## Layout Remediation

The HOI4 layout inspector and renderer were run before and after a coordinate-only repair.

### Unified CBL

| Metric | Before | After | Change |
| --- | ---: | ---: | ---: |
| Connector edges | 132 | 132 | Graph preserved |
| Connector crossings | 44 | 21 | -23 (-52.3%) |
| Connector-through-node intersections | 16 | 0 | Eliminated |
| Tool-classified long connectors | 29 | 6 | -23 (-79.3%) |
| Maximum horizontal span | 52 | 14 | -38 |
| Maximum vertical span | 16 | 13 | -3 |
| Maximum Manhattan span | 54 | 23 | -31 |
| Bounds | x 4..94, y 0..37 | x 4..44, y 0..27 | 91 to 41 columns; 38 to 28 rows |

The remaining 21 crossings do not pass through a focus node. A central subset is produced by the complete three-by-three prerequisite bridge between the three hierarchy capstones and three governance roots; that subgraph cannot be drawn crossing-free while preserving its full prerequisite topology. The other residuals occur at authored multi-parent convergence and direct gate links. Bounded coordinate-only searches did not find a lower-crossing candidate without reintroducing node intersections or materially worse connector spans. This is a structural observation under the current prerequisite contract, not a claim that every individual residual segment is independently unavoidable.

### Warlord

| Metric | Before | After | Change |
| --- | ---: | ---: | ---: |
| Connector edges | 79 | 79 | Graph preserved |
| Connector crossings | 8 | 0 | Eliminated |
| Connector-through-node intersections | 6 | 0 | Eliminated |
| Tool-classified long connectors | 11 | 2 | -9 (-81.8%) |
| Total horizontal span | 284 | 118 | -166 |
| Total vertical span | 99 | 99 | Unchanged |
| Total Manhattan span | 383 | 217 | -166 |
| Maximum horizontal span | 34 | 10 | -24 |
| Maximum vertical span | 3 | 3 | Unchanged |
| Maximum Manhattan span | 37 | 12 | -25 |
| Bounds | x 0..40, y 0..25 | x 10..30, y 0..25 | 41 to 21 columns; 26 rows retained |

The two remaining long connectors are the symmetric, unobstructed root fan from `cannibalism_warlord_the_host_endures` to the separated Island and March origin roots. They cross neither nodes nor other connectors.

### Wendigo

Wendigo was already clean and was not repositioned: 28 focuses, 32 connectors, zero crossings, zero node intersections, five tool-classified long connectors, maximum Manhattan span 37, and bounds x 22..62/y 0..12.

Fresh rendered trees were visually inspected after the repair. Unified is compact with all nodes unobstructed, Warlord is crossing-free with three legible origin columns, and Wendigo remains unchanged. All three render/inspection passes returned zero blocking diagnostics.

## Changed Files

- `common/national_focus/014_cannibalism_focus.txt` — coordinate-only layout repair for Unified and Warlord.
- `docs/plans/014_cannibalism_plans/audits/event014_focus_tree_consolidation_reaudit_2026-07-15.md` — this audit and completion evidence.

The post-repair focus file SHA-256 is `1224F1CBBA0A6A3DB40EAA1781504FBA84367F87E17F08F499FF3D5CFEB97751`.

## Simplifications, Omissions, and Blockers

None. No route, focus, reward, AI path, decision hook, gate, localisation key, icon, or preservation contract was omitted or substituted. The Unified tree's 21 residual connector crossings are disclosed above; zero connector-through-node intersections was achieved, and the requested material reduction in crossings and long connectors was achieved without changing gameplay topology.
