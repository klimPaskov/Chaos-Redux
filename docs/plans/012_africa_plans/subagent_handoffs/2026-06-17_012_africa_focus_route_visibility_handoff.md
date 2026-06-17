# Event 012 Africa Focus Route Visibility Handoff

Date: 2026-06-17

Role: Chaos Redux focus tree subagent. Scope was audit plus safe small patching only.

## Files Changed

- `common/national_focus/012_africa_authority_focus.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_focus_route_visibility_handoff.md`

Files audited but not edited:

- `common/national_focus/012_africa_focus.txt`
- `localisation/english/012_african_union_l_english.yml`

No Event 010 files were touched. No files were staged or committed.

## High-Priority Fix Applied

### Companion-tree tag route visibility

Before: Event 012 regional authority and Bestiary companion trees used `available = { tag = ... }` for role lanes and tag-specific capstones. This prevented the wrong tag from taking the focus, but still left irrelevant grey branches visible in shared trees.

After: added matching `allow_branch` gates next to the existing `available` gates. The current availability checks, prerequisites, rewards, AI weights, icons, and localisation were preserved.

Why this is safe and bounded: this is a visibility/route-lock fix only. It does not alter the route graph for the intended tag, reward amounts, country identity, decisions, events, helper effects, or localisation.

## Changed Focus IDs

Regional authority role lanes:

- `AFR_AUTH_west_sahel_mobility`
- `AFR_AUTH_coastal_rail_links`
- `AFR_AUTH_interior_guard_posts`
- `AFR_AUTH_southern_workshops`

Regional authority tag capstones:

- `AFR_AUTH_wac_port_union`
- `AFR_AUTH_sah_oasis_routes`
- `AFR_AUTH_mag_harbor_compact`
- `AFR_AUTH_nhr_highland_survey`
- `AFR_AUTH_eac_railway_board`
- `AFR_AUTH_glk_lake_muster`
- `AFR_AUTH_cbc_river_quartermasters`
- `AFR_AUTH_zsc_stone_city_yards`
- `AFR_AUTH_slc_mine_port_liberation`
- `AFR_AUTH_ioc_monsoon_passages`

Bestiary role lanes:

- `AFR_BEST_forest_covenant`
- `AFR_BEST_river_tide_compacts`
- `AFR_BEST_ananse_signal_lines`

Bestiary actor capstones:

- `AFR_BEST_ghp_sanctuary_watch`
- `AFR_BEST_bbs_memory_speakers`
- `AFR_BEST_tdm_tidemark_harbors`
- `AFR_BEST_anw_counterfeit_threads`
- `AFR_BEST_ovn_omen_groves`
- `AFR_BEST_crr_ferry_toll_law`
- `AFR_BEST_ctl_canopy_relays`
- `AFR_BEST_okp_shadow_paths`
- `AFR_BEST_trm_citadel_surveyors`
- `AFR_BEST_hgd_route_hives`
- `AFR_BEST_ghc_migration_corridors`

## Route Behavior Before and After

| Surface | Before | After |
| --- | --- | --- |
| Regional authority role lanes | Wrong role lanes were visible but unavailable to unrelated authority tags. | Wrong role lanes are hidden by `allow_branch`; intended tags still pass the same `available` gates. |
| Regional authority capstones | All ten tag capstones were visible in the shared tree, with nine greyed out for each tag. | Only the current tag's capstone branch is shown. |
| Bestiary role lanes | Forest, river/tide, and Ananse branches were visible to actors that could never use them. | Each role lane is hidden unless the actor belongs to the matching tag group. |
| Bestiary actor capstones | All eleven actor capstones were visible in the shared tree, with ten greyed out for each actor. | Only the current Bestiary actor's capstone branch is shown. |

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Charter opening/statebuilding | `AFR_the_charter_mandate`, `AFR_continental_congress`, `AFR_charter_courts` | Present, partial | Functional trunk exists; broader survival/state-building depth remains outside this patch. |
| Federal Congress | `AFR_federal_charter_path` through `AFR_congress_of_capitals` | Present, partial | Route is real and decision-facing; richer advisors/failure states remain broader work. |
| People's Liberation Front | `AFR_peoples_liberation_front`, `AFR_port_unions_and_mine_cells`, `AFR_exile_radios`, `AFR_people_continental_army` | Present, partial | Distinct route exists but is still a compact branch. |
| Continental General Staff | `AFR_general_staff_above_parliament`, `AFR_railway_war_offices`, `AFR_askari_veteran_bureaus`, `AFR_continental_war_plan` | Present, partial | Route has military/infrastructure hooks; deeper command politics remain broader work. |
| Sovereign seats | `AFR_sovereign_seats_path`, `AFR_autonomous_regions` | Simplified | Present as route lock/payoff, but less deep than Federal/Crown. |
| Crown Congress / old thrones | `AFR_crown_congress` through `AFR_crowns_beneath_the_charter` | Present, partial | Route exists and connects to Archive/old-seat values. |
| Industry/logistics | `AFR_industrial_convergence`, `AFR_lake_and_rail_agreements`, `AFR_mandate_foundries`, regional construction lanes | Present, partial | Several rewards still use broad African state construction rather than named geography. |
| Military/liberation | Liberation office, General Staff route, RSA emergency branch, guard schools | Present, partial | Focus rewards include XP, manpower, equipment, and mission flags. |
| Diplomacy/Charter League | Congress/courts/authority charters, sponsor office, cross-continent staff | Present, partial | Decision/faction behavior must be validated outside focus files. |
| Expansion/integration | `AFR_scramble_reverse_claims`, `AFR_foreign_holder_case_files`, `AFR_scramble_counter_dockets`, integration/autonomy payoffs | Present, partial | Focuses open dockets and missions; postwar settlement behavior lives in decisions/effects. |
| Diaspora return | `AFR_return_offices` through `AFR_pan_atlantic_congress` | Present, partial | Branch exists; South Atlantic route depends on decision-set `africa_pan_atlantic_congress_held`. |
| Authority Atlas / Archive | `AFR_authority_atlas`, `AFR_archive_of_old_seats`, register, macro lanes, settlement fork | Present, partial | Old aggregate dossier focuses still remain as high-chaos gates; detailed dossier play is decision/effect-owned. |
| High-chaos Bestiary | Main Bestiary branch plus `africa_high_chaos_actor_focus_tree` | Present, patched | This patch hides irrelevant actor branches and capstones in the shared Bestiary tree. |
| Regional authority subjects | `africa_regional_authority_focus_tree` | Present, patched | This patch hides irrelevant authority role lanes and capstones in the shared authority tree. |
| RSA civil-war branch | `AFR_rsa_congress_underground` through `AFR_rsa_victory_settlement` | Present, partial | Focus branch exists; Allied white peace/aftermath validation is outside focus scope. |
| Post-unification / sponsor / World Is One | `AFR_africa_is_one` through `AFR_the_world_is_one` | Present, partial | Focus sequence exists. External continent proof and final gate behavior depend on decisions/effects/triggers outside write scope. |

## Missing or Simplified Content

- The main tree remains a large shared tree, not bespoke per unifier.
- Regional authority and Bestiary actor trees remain shared companion trees with tag-specific lanes and capstones, not full bespoke country trees.
- Several focus rewards still rely on broad `random_owned_controlled_state` or `every_owned_state` construction over African states.
- Some focuses primarily set route flags or value deltas whose actual gameplay depends on decision/effect hooks outside this write scope.
- `AFR_africa_is_one` currently requires the high-chaos/Bestiary World Root route and minimum high-chaos packages. If the intended design is a non-high-chaos Africa Is One route, this is a parent design decision rather than a safe local patch.

## Icon Coverage Table

| Icon area | Status | Notes |
| --- | --- | --- |
| Event-specific focus icons | Covered | All referenced `GFX_goal_africa_*` icons resolve in `interface/012_africa.gfx`. |
| Vanilla/generic focus icons | Covered | Generic focus icons resolve against local or vanilla interface sprite definitions. |
| Missing icon references | None found | Task-specific icon resolution check found no missing focus icon sprites. |
| Repeated icon risk | Present | Generic infrastructure, treaty, research, and Bestiary icons repeat across broad branches. This is not broken but remains visual simplification. |
| Changed icon ids | None | This patch did not change icon ids. |

## Localisation and Reward Mismatch List

- Missing focus localisation: none found for the 150 audited focus ids and `_desc` keys.
- Localisation keys changed: none.
- Reward mismatch risk: several focus descriptions refer to offices, missions, registers, or sponsor routes whose concrete behavior is implemented through decisions/effects outside this patch. Those hooks should be validated before claiming the Event 012 focus/decision package complete.

## AI Behavior Gaps

- The focus files mostly use broad constants such as `constant:africa_ai.normal`, `preferred`, `strong`, and `low`.
- Route-aware strategy exists in `common/ai_strategy/012_africa.txt`, but that file was outside write scope for this pass.
- This patch improves AI-facing route cleanliness indirectly by hiding invalid shared-tree branches, but it does not add new AI strategy plans or AI decision behavior.
- High-chaos World Is One content remains low-weighted except when the final trigger is already available; broader terminal-branch AI safety depends on out-of-scope triggers and decisions.

## Meaningful Validation Run

- Parsed both Event 012 focus files: 150 focus ids, no duplicate focus ids, and no missing prerequisite/mutual-exclusion/relative-position focus references.
- Tree-aware coordinate check: `africa_is_one_focus_tree` has 108 focuses and no duplicate coordinates; `africa_regional_authority_focus_tree` has 22 focuses and no duplicate coordinates; `africa_high_chaos_actor_focus_tree` has 20 focuses and no duplicate coordinates.
- Localisation coverage check: no missing name or `_desc` keys for all audited focus ids in `localisation/english/012_african_union_l_english.yml`.
- Icon coverage check: 29 unique focus icon references, no missing local or vanilla sprite definitions.
- Branch-lock check: every simple `available = { tag = ... }` capstone in `012_africa_authority_focus.txt` now has a matching simple `allow_branch = { tag = ... }`.
- Scoped filter/operator check: no remaining `FOCUS_FILTER_NAVY` tokens and no unsupported comparison-operator tokens in the two Event 012 focus files.
- `git diff --check -- common/national_focus/012_africa_authority_focus.txt` reported no whitespace errors.

Skipped validation:

- No full game load was run.
- No decision/effect runtime simulation was run; several focus flags intentionally depend on `common/decisions/012_africa_decisions.txt`, `common/scripted_effects/012_africa_effects.txt`, and `common/scripted_triggers/012_africa_triggers.txt`, which were outside write scope.
- No AI strategy patch was made because `common/ai_strategy/012_africa.txt` was outside write scope.

## Remaining Route Risks and Parent Follow-Ups

- Validate the decision/effect hooks for `AFR_africa_is_one`, `AFR_continental_export_office`, `AFR_south_atlantic_return_mandate`, `AFR_congress_of_continents`, `AFR_one_charter_above_nations`, and `AFR_the_world_is_one`.
- Confirm whether `AFR_africa_is_one` is intentionally high-chaos-gated through `AFR_world_root_mandate`; if not, the main route graph needs a parent-level redesign.
- Validate RSA branch aftermath hooks, especially `africa_white_peace_allies_after_rsa_continental_victory`, from the on-action/effect layer.
- Consider replacing broad state construction rewards with named-region or selected-target construction where the decision layer exposes suitable state targets.
- Consider additional focus icon art for repeated generic infrastructure/research/Bestiary icons if visual identity becomes a completion blocker.

## Plan Handoff

No new improvement plan was written. The existing broad design addendum remains the correct parent-level plan for unresolved depth:

- `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md`
