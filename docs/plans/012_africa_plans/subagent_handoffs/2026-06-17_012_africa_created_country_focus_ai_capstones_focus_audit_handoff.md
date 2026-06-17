# Event 012 Created-Country Focus/AI Capstone Audit Handoff

## Scope

Audited the bounded created-country companion focus and AI capstone layer for Event 012:

- `common/national_focus/012_africa_authority_focus.txt`
- `common/ai_strategy/012_africa.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_focus_ai_capstones_parent_handoff.md`

## Patch

Changed `common/ai_strategy/012_africa.txt`.

Added `id = infantry` to every scoped `type = build_army` strategy block in this file. The offline AI modding wiki and vanilla AI strategy examples show `build_army` with an explicit unit-role `id`; the scoped file omitted it. The infantry role matches the created actors' guard and equipment setup and the existing production strategy emphasis.

## Changed AI Strategy Blocks

- `africa_unifier_charter_consolidation`
- `africa_unifier_liberation_war_posture`
- `africa_unifier_people_liberation_front`
- `africa_unifier_continental_general_staff`
- `africa_unifier_rsa_continental_emergency`
- `africa_regional_authority_survival`
- `africa_regional_authority_west_sahel_mobility`
- `africa_regional_authority_interior_guard`
- `africa_high_chaos_actor_survival`
- `africa_bestiary_great_herds_posture`
- `africa_regional_authority_sah_oasis_routes`
- `africa_regional_authority_nhr_highland_survey`
- `africa_regional_authority_glk_lake_muster`
- `africa_regional_authority_cbc_river_quartermasters`
- `africa_regional_authority_slc_mine_port_liberation`
- `africa_bestiary_ghp_sanctuary_watch`
- `africa_bestiary_anw_counterfeit_threads`
- `africa_bestiary_crr_ferry_toll_law`
- `africa_bestiary_ctl_canopy_relays`
- `africa_bestiary_ghc_migration_corridors`

## Behavior Before and After

Before: the AI strategies asked the AI to build an army without specifying the unit role target.

After: the same strategies explicitly target the `infantry` role, preserving the intended defensive/offensive army posture while matching vanilla `build_army` syntax.

No focus IDs, localisation keys, icon IDs, route locks, prerequisites, mutual exclusions, or documentation claims were changed.

## Validation

- Confirmed all 21 required created actors have one tag-specific capstone focus: ten regional authorities and eleven Bestiary/high-chaos actors.
- Confirmed all 21 required created actors have one tag-specific AI strategy block layered on top of their role-family posture.
- Confirmed every companion focus ID in `012_africa_authority_focus.txt` has both name and `_desc` localisation in `012_african_union_l_english.yml`.
- Confirmed every companion focus icon resolves in Event 012 or vanilla `.gfx`.
- Confirmed every `constant:` token used by the companion focus file resolves in `common/script_constants/012_africa_constants.txt`.
- Confirmed no duplicate companion focus IDs, no duplicate AI strategy block IDs, and no duplicate focus coordinates in the companion trees.
- Confirmed no unsupported comparison operators in the scoped script or localisation files.
- Confirmed final brace counts match for the touched companion focus and AI files.

## Remaining Risks

- The regional authority and Bestiary trees remain shared companion trees with per-tag capstones, not full bespoke country trees. This matches the bounded parent intent but remains a simplification compared with fully bespoke playable country packages.
- The scoped audit did not inspect broad Event 012 main-tree routes, country histories, decisions, assets, or live in-game behavior because those surfaces were explicitly out of scope.
