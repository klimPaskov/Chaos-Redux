# Event 014 CBL Focus Tree Audit Handoff

Scope: Event 014 CBL Cannibal Commune focus tree only.

Skills and references used:

- `AGENTS.md`
- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- Offline wiki pages including National focus modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding
- Vanilla documentation including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md`
- Vanilla focus precedent for multiple `focus = ...` entries inside one `prerequisite` block

## High-Priority Fixes

| Priority | File and identifier | Status | Notes |
| --- | --- | --- | --- |
| High | `common/national_focus/014_cannibalism_focus_tree.txt`, `cbl_couriers_between_tables` | Fixed | Changed two separate prerequisites into one OR prerequisite: `cbl_no_public_feasts` or `cbl_hunting_ground_doctrine`. Separate blocks were an impossible AND because the two parents are mutually exclusive. |
| High | `common/national_focus/014_cannibalism_focus_tree.txt`, `cbl_world_as_larder_gate` | Fixed | Changed two separate prerequisites into one OR prerequisite: `cbl_listen_for_hannibal` or `cbl_proclaim_the_last_table`. Separate blocks blocked the Last Table route and conflicted with the Hannibal/independent split. |
| High | `common/scripted_effects/014_cannibalism_effects.txt`, `cannibalism_create_commune_country` | Fixed | Added runtime focus-tree loading after new CBL creation. The existing-CBL reinforcement path checks `has_focus_tree = cannibalism_commune_focus_tree` and loads the tree with `keep_completed = yes` only if needed. |
| Medium | `common/national_focus/014_cannibalism_focus_tree.txt`, `cbl_proclaim_the_last_table` | Fixed | Added the existing `cannibalism_last_table_discipline` idea to the Last Table proclamation so the formable payoff uses the already implemented spirit and localisation. |

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening survival trunk | `cbl_first_table`, `cbl_seal_the_origin_state`, `cbl_night_larder_columns`, `cbl_black_kitchens` | Partial | Covers first state, first troops, first kitchen industry, and starting network pressure. Still compact compared with the spec's commander, prisoner, and supply-method opening. |
| Command hierarchy fork | No real council or warlord fork. `cbl_listen_for_hannibal` is the only hierarchy-like route hook. | Missing | Needs a broader route family. See `docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md`. |
| Hannibal discipline route | `cbl_listen_for_hannibal`, `cbl_world_as_larder_gate` | Simplified | Hook exists and is gated by `cannibalism_hannibal_or_unifier_exists`, but there is no hidden branch family, leader swap, cadre route, or Hannibal-specific mechanics. |
| Supply and economy | `cbl_black_kitchens`, `cbl_port_harvests`, `cbl_commune_ration_codes`, `cbl_no_public_feasts`, `cbl_hunting_ground_doctrine` | Partial | Has factories, port assets, manpower, and restrained/runaway choice. It does not yet implement convoy ambush plans, prisoner ledger administration as a decision family, disease avoidance, or staged economy choices. |
| Military | `cbl_night_larder_columns`, `cbl_empty_larder_war_discipline`, reinforcement helper calls | Simplified | Gives manpower/equipment/units and one war-discipline payoff. Missing butcher packs, scavenger parties, prison processions, commanders, landing methods, and template progression. |
| Expansion | `cbl_port_harvests`, `cbl_hunting_ground_doctrine`, `cbl_proclaim_the_last_table` | Simplified | Coastal support exists, but no island, coastal, and inland origin-specific branches, no gradual claims or war goals, and no post-capture handling. |
| Cannibal pact or solitary rampage | `cbl_refuse_the_wider_pact`, `cbl_listen_for_hannibal` | Partial | Independent refusal and Hannibal listener are mutually exclusive, but there is no actual pact mechanic for multiple cannibal actors. |
| Global courier routes | `cbl_couriers_between_tables` | Fixed and partial | Now reachable from either restrained or hunting-ground route. It records the global table and raises network strength, but has no decision layer for courier targets. |
| Last Table formable | `cbl_proclaim_the_last_table` | Partial | Sets `CBL_LAST_TABLE`, `cannibalism_last_table_formed`, `cannibalism_later_unifier_accepted`, achievement flag, and now `cannibalism_last_table_discipline`. It still lacks a map-control decision, integration projects, and post-formation branch. |
| World-end preparation | `cbl_world_as_larder_gate`, `cannibalism_world_end_route_available`, `cannibalism_try_world_end_route` | Fixed and partial | Focus is now reachable by Hannibal linkage or Last Table route, while the trigger still enforces global table, accepted unifier, chaos, network, cult nodes, and communes. |

## Missing or Simplified Content

- `common/national_focus/014_cannibalism_focus_tree.txt`: missing council of knives and warlord kitchen command routes promised by `docs/specs/014_cannibalism_specs/focus_graphs/014_cannibalism_focus_architecture.md`.
- `common/national_focus/014_cannibalism_focus_tree.txt`: `cbl_port_harvests` is the only origin-style expansion focus, so island, coastal, inland, prison-road, and rail-corridor expansion are not implemented.
- `common/national_focus/014_cannibalism_focus_tree.txt`: no claims, cores, war goals, postwar handling, protectorate, pact, or integration focus rewards exist in the CBL tree.
- `common/national_focus/014_cannibalism_focus_tree.txt`: no focus unlocks a CBL-specific decision family except indirectly through world-end globals and existing Event 014 decisions.
- `common/national_focus/014_cannibalism_focus_tree.txt`: Hannibal branch is an available focus, not a hidden branch. Hiding it cleanly would require layout refresh handling if the gate changes after tree load.
- `common/scripted_effects/014_cannibalism_effects.txt`: CBL creation now loads the focus tree, but the broader country package creation path still uses `transfer_state_to = CBL` rather than a formation decision or release flow. This was not changed because it is outside a focus-tree patch.

## Icon Coverage Table

| Focus id | Icon id | Sprite defined | DDS exists | Status |
| --- | --- | --- | --- | --- |
| `cbl_first_table` | `GFX_goal_cannibalism_first_table` | Yes | Yes | OK |
| `cbl_seal_the_origin_state` | `GFX_goal_cannibalism_origin_state` | Yes | Yes | OK |
| `cbl_night_larder_columns` | `GFX_goal_cannibalism_larder_columns` | Yes | Yes | OK |
| `cbl_black_kitchens` | `GFX_goal_cannibalism_black_kitchens` | Yes | Yes | OK |
| `cbl_port_harvests` | `GFX_goal_cannibalism_port_harvests` | Yes | Yes | OK |
| `cbl_commune_ration_codes` | `GFX_goal_cannibalism_ration_codes` | Yes | Yes | OK |
| `cbl_no_public_feasts` | `GFX_goal_cannibalism_empty_larder` | Yes | Yes | OK |
| `cbl_hunting_ground_doctrine` | `GFX_goal_cannibalism_hunting_ground` | Yes | Yes | OK |
| `cbl_couriers_between_tables` | `GFX_goal_cannibalism_couriers` | Yes | Yes | OK |
| `cbl_refuse_the_wider_pact` | `GFX_goal_cannibalism_table_for_one` | Yes | Yes | OK |
| `cbl_listen_for_hannibal` | `GFX_goal_cannibalism_hannibal_hook` | Yes | Yes | OK |
| `cbl_proclaim_the_last_table` | `GFX_goal_cannibalism_last_table` | Yes | Yes | OK |
| `cbl_empty_larder_war_discipline` | `GFX_goal_cannibalism_restrained_war` | Yes | Yes | OK |
| `cbl_world_as_larder_gate` | `GFX_goal_cannibalism_world_larder` | Yes | Yes | OK |

No repeated focus icons were found in the current CBL tree.

## Localisation and Reward Mismatch List

- All 14 current CBL focus ids have title and `_desc` localisation in `localisation/english/014_cannibalism_l_english.yml`.
- `cbl_proclaim_the_last_table`: before patch, the focus changed the cosmetic tag but did not use the existing `cannibalism_last_table_discipline` idea. After patch, the reward better matches the Last Table discipline localisation and icon already present in `common/ideas/014_cannibalism_ideas.txt` and `interface/014_cannibalism.gfx`.
- `cbl_port_harvests`: localisation and reward match a coastal port route, but the spec requires origin-sensitive island, coastal, and inland expansion. This is a design simplification, not a missing key.
- `cbl_listen_for_hannibal`: localisation matches the Hannibal hook, but the focus is visible as a normal focus with an `available` gate rather than hidden until the hook exists.
- `cbl_world_as_larder_gate`: localisation says "a unifier accepted". This remains accurate because `cannibalism_world_end_route_available` requires `cannibalism_hannibal_or_unifier_exists`, and the Last Table route sets `cannibalism_later_unifier_accepted`.

## AI Behavior Gaps

- Every current CBL focus has an `ai_will_do` block.
- `common/ai_strategy/014_cannibalism.txt` contains broad CBL strategies for origin survival, war reinforcement, table seeking, and world-end pressure.
- No AI strategy plan was found that orders CBL national focuses with `ai_national_focuses` or route-specific focus factors.
- The focus weights are mostly flat constants, with little route-aware behavior for coastal access, strength, Hannibal availability, Last Table viability, or restrained versus hunting-ground selection.
- `cbl_port_harvests` is gated by coastal control, but AI route logic does not compensate with an inland branch because no inland branch exists.
- `cbl_world_as_larder_gate` has safe zero base with a trigger-based crisis modifier, which is appropriate after the prerequisite fix.

## Changed Files

- `common/national_focus/014_cannibalism_focus_tree.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_cbl_focus_tree_audit_handoff.md`

## Changed Focus IDs

- `cbl_couriers_between_tables`
- `cbl_proclaim_the_last_table`
- `cbl_world_as_larder_gate`

## Route Behavior Before and After

- `cbl_couriers_between_tables`
  - Before: required both `cbl_no_public_feasts` and `cbl_hunting_ground_doctrine` because they were separate prerequisite blocks. That made the focus impossible after the mutually exclusive route choice.
  - After: requires either `cbl_no_public_feasts` or `cbl_hunting_ground_doctrine`, matching HOI4 OR prerequisite semantics.
- `cbl_proclaim_the_last_table`
  - Before: set the Last Table cosmetic route and flags but did not apply the existing Last Table national spirit.
  - After: also adds `cannibalism_last_table_discipline`.
- `cbl_world_as_larder_gate`
  - Before: required both Hannibal linkage and Last Table proclamation because they were separate prerequisite blocks. This blocked the independent Last Table route and made the gate overly strict.
  - After: requires either `cbl_listen_for_hannibal` or `cbl_proclaim_the_last_table`, while `available = { cannibalism_world_end_route_available = yes }` still enforces the real world-end conditions.
- `cannibalism_create_commune_country`
  - Before: CBL creation relied on focus-tree country scoring and did not explicitly load the runtime focus tree.
  - After: new runtime CBL creation loads `cannibalism_commune_focus_tree` directly. If CBL already exists, the reinforcement path checks `has_focus_tree = cannibalism_commune_focus_tree` and loads with `keep_completed = yes` only when the tree is missing.

## Localisation Keys and Icon IDs Changed

- Localisation keys changed: none.
- Icon ids changed: none.
- Existing idea key newly used by a focus reward: `cannibalism_last_table_discipline`.

## Meaningful Validation

- Verified HOI4 prerequisite semantics from the focus-tree skill and the local National focus modding wiki page: multiple `focus = ...` entries inside one `prerequisite` block are OR, while separate `prerequisite` blocks are AND.
- Checked current graph extraction after patch. `cbl_couriers_between_tables` now has one prerequisite block with both route parents; `cbl_world_as_larder_gate` now has one prerequisite block with both late route parents.
- Checked all 14 current CBL focus ids for title localisation, description localisation, `.gfx` sprite definitions, and final focus-icon DDS files. All current focus ids passed.
- Checked the two edited script files for brace balance after patch.
- Searched Event 014 and adjacent CBL files for `load_focus_tree` and verified the patch adds the first CBL runtime focus-tree load path.

## Skipped Meaningful Validation

- No in-game load or runtime save validation was run from this subagent environment.
- No full HOI4 parser validation was run.
- No visual icon render check was run. The audit verified sprite definitions and DDS file presence only.

## Remaining Route Risks

- The tree is still substantially shallower than the Event 014 spec. Command hierarchy, origin-sensitive expansion, military specialization, pact mechanics, and Last Table formation depth need a parent implementation pass.
- The Hannibal route is a hook, not a finished route. It should remain limited until the Hannibal event design exists.
- The Last Table route still lacks a decision that proves map control and handles post-formation integration.
- CBL route AI is broad but not focus-order aware.
- This workspace contains many unrelated dirty Event 013 and Event 015 files. They were not touched.

## Plan Handoff

Broad route-depth follow-up was written here:

`docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md`
