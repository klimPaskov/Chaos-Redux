# Event 20 Rat Focus Audit Handoff

> Historical focus-audit snapshot, superseded for current counts by the 2026-08-02 reconciliation: the body records an earlier 23/38-focus inspection. Current runtime documentation records 51 RTA and 71 RTX focus nodes. Retain the audit's valid prerequisite, layout, and icon findings, and do not use its old compact-tree counts as the current source of truth.

Date: 2026-08-01

Scope: the two live Event 20 national focus trees for `RTA` and `RTX`. This audit did not touch models, country identity, events, decisions, or the runtime rat allocator.

## Result

The focus graphs are structurally connected and use the corrected OR/AND prerequisite semantics already present in the working tree. I made one narrow icon-reference patch so three focuses use the exact custom sprites that already exist in the Event 20 GFX package.

The accepted route architecture is substantially broader than the current implementation. Those depth gaps are recorded as plan-level work rather than expanded in this bounded audit.

## Changed files and focus ids

| File | Focus id | Before | After |
| --- | --- | --- | --- |
| `common/national_focus/020_black_plague_rat_focus_tree.txt` | `black_plague_rat_first_warren` | `GFX_goal_generic_construct_infrastructure` | `GFX_goal_black_plague_rat_first_warren` |
| `common/national_focus/020_black_plague_rat_focus_tree.txt` | `black_plague_rat_field_brood` | `GFX_goal_generic_construct_infrastructure` | `GFX_goal_black_plague_rat_field_brood` |
| `common/national_focus/020_black_plague_rat_king_focus_tree.txt` | `black_plague_rat_brood_council` | `GFX_goal_generic_alliance` | `GFX_goal_black_plague_rat_brood_council` |

No localisation keys or GFX definitions changed. The referenced sprites and their shine variants were already registered in `interface/020_black_plague_rat_identity.gfx` and their DDS files already existed.

## Route coverage

### RTA Base Rat Nation

| Accepted lane | Current implementation | Evidence | Coverage |
| --- | --- | --- | --- |
| Awakening and Survival | `first_warren` -> `listen_to_the_drains` -> `feral_quarantine` and `no_human_rations` | `common/national_focus/020_black_plague_rat_focus_tree.txt:43-85` | Partial but playable |
| Origin Adaptation | Urban, Field, Dock, and War branches with three focuses each and fixed-archetype availability | `common/national_focus/020_black_plague_rat_focus_tree.txt:87-225`; archetype assignment in `common/scripted_effects/020_black_plague_rat_effects.txt:194-218` | Present at compact depth |
| Hierarchy | `brood_signal` -> `four_mouths` -> `choose_a_voice` | `common/national_focus/020_black_plague_rat_focus_tree.txt:227-259` | Simplified; no mutually exclusive hierarchy end states |
| Mutation | No mutation branch or focus | No matching focus ids in the RTA tree | Missing |
| Territorial Plague Economy | Only brood-mass and division-cap increments embedded in origin focuses | `common/national_focus/020_black_plague_rat_focus_tree.txt:94-223` | Missing as a dedicated lane |
| Military Method | Origin cap boosts and `capped_pulses` only | `common/national_focus/020_black_plague_rat_focus_tree.txt:261-276` | Simplified |
| Rival Absorption | One `annex_the_weak` convergence focus | `common/national_focus/020_black_plague_rat_focus_tree.txt:289-299` | Simplified; no rival route depth |
| Proto-Sentience and Rat King candidacy | `prepare_the_crown` sets `black_plague_rat_king_candidate` | `common/national_focus/020_black_plague_rat_focus_tree.txt:300-309` | Simplified gate |
| Convergence and immunity | `capped_pulses` -> `immune_blood` -> `annex_the_weak` | `common/national_focus/020_black_plague_rat_focus_tree.txt:261-299` | Present |

The Base tree contains 23 focuses against the accepted target of roughly 40-50. The fixed-archetype origin lock is intentional, and `capped_pulses` correctly uses one OR prerequisite block so any one eligible origin terminal can converge.

### RTX Rat King

| Accepted lane | Current implementation | Evidence | Coverage |
| --- | --- | --- | --- |
| Coronation and Stabilization | Four opening focuses plus `refuge_nodes`, `capital_seals`, and `the_four_registers` | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:36-113` | Compact |
| Government Structure | Absolute Crown, Brood Council, and Black-Breath Hierophancy, each with four focuses and symmetric mutual exclusions | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:115-260` | Present and correctly locked |
| Administration and Supply | Refuge, capital, and register setup only | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:80-113` | Simplified |
| Military Castes | Shared `royal_armouries` plus four advanced-force focuses and `royal_template_lock` | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:262-336` | Present at compact depth; not route-specific |
| Plague Mastery | No dedicated plague-mastery lane | No matching focus ids in the RTX tree | Missing |
| Captured Knowledge | `human_minds_in_chains` and `refugee_memory` after the shared template gate | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:338-398` | Simplified |
| Human Population Policy | `human_minds_in_chains` is the only explicit human-policy focus | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:362-371` | Simplified |
| Continental Campaign | Capital/refuge mapping, cryptography, roads, and terminal armature | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:400-456` | Present at compact depth |
| World-End and Evolution V | `terminal_sentience` -> `terminal_cohesion` -> `earned_terminal_route`, with meter gates and global completion flag | `common/national_focus/020_black_plague_rat_king_focus_tree.txt:458-497`; `common/scripted_triggers/020_black_plague_evolution_triggers.txt:109-116` | Present but compact |

The King tree contains 38 focuses against the accepted target of roughly 70-100. `royal_armouries` correctly uses one OR prerequisite block for the three mutually exclusive government endpoints, while `royal_template_lock` and `solve_the_first_crisis` intentionally use separate prerequisite blocks to require all shared lane focuses.

## Missing or simplified content

- RTA has no dedicated mutation, territorial plague economy, or military-method route families.
- RTA hierarchy is a forced distributed-to-dominant transition, not the accepted mutually exclusive hierarchy choice set.
- RTA rival absorption and proto-sentience are one-focus gates rather than playable route families.
- RTX administration/supply, plague mastery, captured knowledge, human population policy, and continental campaign are compact reward chains rather than deep route families.
- RTX government routes have distinct roots and mutual exclusions, but all three converge on the same royal-forces lane with limited route-specific tradeoffs.
- Both trees are far below the accepted depth ranges; adding the missing route families requires a broader design tranche and is outside this patch.

## Icon coverage

All 11 custom Event 20 focus sprites have regular and `_shine` definitions, existing DDS files, and at least one live focus reference after this patch:

| Custom sprite family | Live use after patch |
| --- | --- |
| `first_warren` | RTA `black_plague_rat_first_warren`; also reused by RTX `black_plague_rat_dominion_over_roads` |
| `urban_warren` | RTA `black_plague_rat_no_human_rations` |
| `field_brood` | RTA `black_plague_rat_field_brood` |
| `dock_brood` | RTA `black_plague_rat_dock_brood` and `black_plague_rat_wharf_raids`; RTX `black_plague_rat_sea_brood` |
| `war_brood` | RTA `black_plague_rat_annex_the_weak` |
| `brood_signal` | RTA `black_plague_rat_brood_signal` and `black_plague_rat_choose_a_voice`; RTX `black_plague_rat_king_the_four_registers` and `black_plague_rat_human_minds_in_chains` |
| `king_the_royal_basin` | RTX `black_plague_rat_king_the_royal_basin` and `black_plague_rat_hunger_court` |
| `absolute_crown` | RTX `black_plague_rat_king_first_royal_decree` and `black_plague_rat_court_of_teeth` |
| `brood_council` | RTX `black_plague_rat_brood_council` |
| `breath_hierophancy` | RTX `black_plague_rat_breath_hierophancy` |
| `earned_terminal_route` | RTX `black_plague_rat_earned_terminal_route` |

Many other focuses still use generic vanilla icons, and several custom families are reused by nearby but non-identical concepts. This is a visual-polish follow-up, not a runtime blocker. The MCP focus resolver reports generic vanilla symbols as missing because its mod-local scan does not index the game interface files; the same 24 generic symbols were verified in the vanilla `interface/goals.gfx` and `interface/goals_shine.gfx` files.

## Localisation and reward mismatch list

All 61 focus ids have title and `_desc` keys in `localisation/english/020_black_plague_rat_focus_l_english.yml`, and the file has a UTF-8 BOM. Source review found no clear title/description-to-reward mismatch in the current compact routes. No localisation keys changed in this patch.

The remaining concern is depth rather than wording: several descriptions promise a broader policy or military institution than the one meter/flag reward currently represents. Those are route-expansion items, not safe wording-only fixes.

## AI behavior gaps

- Neither focus tree defines any focus-level `ai_will_do` blocks.
- There are no Event 20 `ai_national_focuses` or `focus_factors` that prioritize RTA origin, hierarchy, or RTX government routes.
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` provides shared, archetype, and King template/front priorities, but it does not steer national-focus selection.
- The terminal route has sentience/cohesion availability gates, but no AI focus plan for preparing and completing that route.
- Adding route-aware AI should follow the broader route expansion so weights correspond to real route choices.

## High-priority follow-up

1. Expand the RTA tree to the accepted mutation, territorial economy, military method, rival absorption, and proto-sentience route families.
2. Expand the RTX tree to the accepted administration, plague mastery, captured-knowledge, human-policy, campaign, and route-specific government lanes.
3. Add route-aware focus AI after those lanes exist, including terminal-route prioritization and fixed-archetype behavior.
4. Replace the forced RTA hierarchy transition with explicit mutually exclusive hierarchy outcomes when the hierarchy route is expanded.
5. Complete remaining icon differentiation after gameplay route depth is accepted.

## Validation and artifacts

- Post-patch `hoi4.focus_inspect` reports 23 RTA focuses and 38 RTX focuses. Layout metrics report 25 and 47 connectors respectively, with zero connector crossings, zero node intersections, and no same-row spacing violations in either tree.
- Post-patch focus inspection found no missing Event 20 custom icon references. All 61 focus title/description pairs resolved, no focus prerequisite references an unknown id, and exactly the live country tags `RTA` and `RTX` are defined for this package.
- The generic icon diagnostics are a tool indexing limitation documented above; vanilla definitions were checked directly in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\goals.gfx` and `goals_shine.gfx`.
- Render artifacts: [RTA HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/996a62e8a5ae6c7834ca724bb77cff9ce4468bdc72cfb6ed3298700f80620119/451084564b91d3ee045e3655978eb7bfdc1b84620db47b3c0159312e39cdf042/black_plague_rat_focus_tree.focus.html), [RTA SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63fbe7c64aec329ca65bc40268bc3b5016a77ee5913735c18b5f6d0021d478e3/8924b0fcd6a79a2506c83f95075caf4a0fe7dd81def1cd9122fa60dc6300f902/black_plague_rat_focus_tree.focus.svg), [RTX HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d86f0f4f924147ae911606f586616a0e7366429efc9e84f6e77e8bcedb451a9f/ed5ac4c2cad557966b69480ff18202ab2675c679a4ccb9d80c62f17b68af2b50/black_plague_rat_king_focus_tree.focus.html), and [RTX SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0b106c1585d5e44c68bc9299860c1b14dd461ce68f398cd9110a627b4a08add/b59b5f46d0d8a99b796dabc455309b46973e17c38acbf10887440fe742f27b0e/black_plague_rat_king_focus_tree.focus.svg).
- Live Hearts of Iron IV execution was not run, per repository instructions. No focus-tree rewrite was used because the remaining gaps are broad route design rather than local syntax or layout defects.

## Remaining route risks

- Fixed-archetype origin branches stay visible but unavailable for nonmatching RTA countries. Adding bypasses without also locking every descendant would incorrectly expose the wrong origin rewards, so no bypass was added.
- Generic/reused icons remain on many focuses, though all custom sprite families are now registered and referenced.
- The accepted depth and route-aware AI work is still incomplete and must not be represented as finished by this handoff.
