# Event 012 external world-package focus AI handoff

## Scope and source of truth

This bounded tranche adds route-specific AI strategy overlays for the six dormant external-continent focus packages. The gameplay scope is limited to `common/ai_strategy_plans/012_africa_focus_plans.txt`; no readiness flag, focus tree, country tag, asset, decision, event, or model surface was changed.

The route inventory was cross-checked against `docs/specs/012_africa_specs/matrices/012_africa_ai_route_matrix.csv`, `docs/specs/012_africa_specs/specs/012_africa_spec_part_5_high_chaos_world_order.md`, and the six source trees in `common/national_focus/012_africa_world_*_focus.txt`.

## Route coverage

| Package | Routes and plan IDs | Route gate | Shared priorities |
| --- | --- | --- | --- |
| Middle East | Arab federal (`africa_world_middle_east_arab_federal_focus_plan`), plural crossroads (`africa_world_middle_east_plural_crossroads_focus_plan`), royal concert (`africa_world_middle_east_royal_concert_focus_plan`), socialist republics (`africa_world_middle_east_socialist_republics_focus_plan`), desert covenant (`africa_world_middle_east_desert_covenant_focus_plan`) | `africa_world_middle_east_package` plus the exact route flag | Crossroads balance, water and food security, holy cities, corridor security, withdrawal law, settlement congress, sovereign settlement |
| Europe | Democratic federation (`africa_world_europe_democratic_federation_focus_plan`), socialist union (`africa_world_europe_socialist_union_focus_plan`), royal concert (`africa_world_europe_royal_concert_focus_plan`), continental command (`africa_world_europe_continental_command_focus_plan`), neutral confederation (`africa_world_europe_neutral_confederation_focus_plan`), mythic compact (`africa_world_europe_mythic_compact_focus_plan`) | `africa_world_europe_package` plus the exact route flag | Border guarantees, industrial and rail reconstruction, colonial reckoning, common defence, withdrawal/crisis law, post-colonial treaty, ratification |
| Asia | Plural federation (`africa_world_asia_plural_federation_focus_plan`), revolutionary union (`africa_world_asia_revolutionary_union_focus_plan`), imperial congress (`africa_world_asia_imperial_congress_focus_plan`), anti-colonial common front (`africa_world_asia_anti_colonial_common_front_focus_plan`), celestial covenant (`africa_world_asia_celestial_covenant_focus_plan`) | `africa_world_asia_package` plus the exact route flag | Four regional centres, food/river and monsoon board, rail and maritime corridors, autonomy law, Indian Ocean partnership, final settlement |
| North America | Republic of republics (`africa_world_north_america_republics_focus_plan`), continental commonwealth (`africa_world_north_america_commonwealth_focus_plan`), hemisphere command (`africa_world_north_america_hemisphere_command_focus_plan`), socialist continental union (`africa_world_north_america_socialist_union_focus_plan`), storm frontier compact (`africa_world_north_america_storm_frontier_compact_focus_plan`) | `africa_world_north_america_package` plus the exact route flag | Industrial grid, Caribbean and Central membership, indigenous settlement, citizenship and mobility, withdrawal/resource law, Atlantic/Pacific defence, diaspora treaty, final bargain |
| South America | Congress of republics (`africa_world_south_america_republics_focus_plan`), plural federation (`africa_world_south_america_federation_focus_plan`), socialist continental union (`africa_world_south_america_socialist_union_focus_plan`), continental command (`africa_world_south_america_command_focus_plan`), restored concert (`africa_world_south_america_royal_concert_focus_plan`), sun covenant (`africa_world_south_america_sun_covenant_focus_plan`) | `africa_world_south_america_package` plus the exact route flag | Andean, Amazon, and Plata systems, debt audit, resource sovereignty, continental defence/corridors, South Atlantic partnership, final settlement |
| Oceania | Maritime federation (`africa_world_oceania_maritime_federation_focus_plan`), treaty dominion (`africa_world_oceania_dominion_focus_plan`), indigenous-led ocean union (`africa_world_oceania_indigenous_union_focus_plan`), socialist maritime commonwealth (`africa_world_oceania_socialist_commonwealth_focus_plan`), deep-sea covenant (`africa_world_oceania_deep_sea_covenant_focus_plan`) | `africa_world_oceania_package` plus the exact route flag | Island sovereignty, convoy/shipping, air routes and dispersed industry, island development, anti-colonial land settlement, ocean constitution, Pacific defence, sea treaty, final network |

Every plan also requires `is_ai = yes`, `africa_world_package_is_installed = yes`, no `world_end`, and one of `africa_world_package_sponsored`, `africa_world_package_independent`, or `africa_world_package_rival`. The abort block repeats those package, route, world-end, and relationship checks so a stale overlay is removed after a settlement or status transition.

The six high-chaos plans additionally require their package review flag and `global.chaos_meter_value > constant:africa_world_order.package_high_chaos_gate`, matching the corresponding focus `available` blocks.

## Before and after behavior

Before this patch, Event 012 had 64 matrix profiles and shared constitutional, support, formation, and host-specific overlays but no route-specific strategy plan for any of the six external packages. External actors therefore relied only on focus-local `ai_will_do` values and generic world-order behavior.

After this patch, all 32 external routes have distinct factor vectors. Route plans prioritize their authored setup centres and route institution, then weight the package-specific security, autonomy, treaty, and settlement focuses. Sponsorship, independent, and rivalry status change plan weight through the shared status modifiers; ideology alignment and active war pressure add route-sensitive weight where the focus route exposes those signals.

Route plans activate after the authored route focus sets its route flag. Pre-route selection remains owned by the focus-local `ai_will_do` blocks, preserving their package-specific prerequisites and high-chaos availability checks.

## Missing or simplified content

- The six external trees remain dormant behind the existing `africa_world_package_implementation_ready` gate. This tranche intentionally does not open readiness or install incomplete packages.
- The shared capstone prerequisites in the authored trees require every route institution even though the route focuses are mutually exclusive. For example, `africa_middle_east_desert_and_mountain_command` requires all five Middle East institutions, and the analogous Europe, Asia, North America, South America, and Oceania shared laws require all route institutions. The AI overlays cannot make those AND prerequisites reachable; this is a focus-tree design risk for the parent scope.
- No package-specific decisions, missions, actors, leaders, flags, ideas, events, icons, or models were added. Existing completion audits record those deferred surfaces.
- No fallback focus route was introduced. If a route flag is absent, the plan remains inactive and the authored focus AI remains responsible for selection.

## Icon coverage

| Surface | Current state | Effect of this tranche |
| --- | --- | --- |
| Six external focus trees | The completion audit found zero authored `icon =` fields in the six trees and existing loader/icon diagnostics remain unresolved. | No icon references were changed because this tranche owns only AI strategy plans. |
| AI strategy plans | Strategy plans do not consume focus icon IDs. | No new GFX or sprite dependency. |

## Localisation and reward mismatch list

No player-facing localisation or focus rewards were changed. All 121 focus IDs referenced by the new plan factors resolve to IDs in the six external focus files. Existing focus names, descriptions, rewards, icon gaps, and route-capstone prerequisite mismatches remain owned by the broader external-package work.

## AI behavior gaps and risks

- Live AI assignment, focus timing, sponsorship debt handling, and rivalry transitions were not simulated because agents must not launch Hearts of Iron IV and the change does not alter focus-tree source.
- The plan overlays intentionally start after route commitment; they do not replace the six trees' pre-route `ai_will_do` selection logic.
- Route plans include late shared focuses as priorities, but the current authored all-institutions AND prerequisites can leave those focuses unreachable after a mutually exclusive route. The parent should resolve the tree semantics before enabling package readiness.
- External package actors remain absent until the implementation-ready gate is intentionally reviewed. These plans therefore have no current live consumer in the dormant build.

## High-priority fixes for the parent scope

1. Resolve the mutually exclusive route versus all-institutions AND prerequisite conflict in each external tree before enabling package readiness. The affected shared capstones are `africa_middle_east_desert_and_mountain_command`, `africa_europe_common_army_and_air_defence`, `africa_asia_food_river_and_monsoon_board`, `africa_north_america_resources_and_withdrawal_law`, `africa_south_america_resource_and_debt_sovereignty_law`, and `africa_oceania_ocean_constitution_and_withdrawal_law`.
2. Complete the six packages' authored icon, localisation, decision/event, actor, and asset surfaces, then rerun the focus layout and loader audit before setting `africa_world_package_implementation_ready`.
3. Run weighted AI inspection or live consumer acceptance after package actors become reachable, including sponsorship default, independent settlement, rivalry, high-chaos gate loss, and sovereign completion transitions.

## Validation

- Counted 32 new route plan blocks in `common/ai_strategy_plans/012_africa_focus_plans.txt`, with 32 unique plan IDs and 32 unique route flags.
- Cross-walked 121 unique `focus_factors` IDs against all six external trees; no missing focus IDs were found.
- Verified every route plan has package-installed, package-flag, route-flag, relationship-status, world-end abort, focus-factor, and weight blocks.
- Verified the six high-chaos routes carry both the package review flag and the shared chaos gate in enable and abort conditions.
- Skipped `hoi4.focus_rewrite` and focus rendering because no focus-tree source was edited. The prior external-package completion audit already captured the tree layout/icon diagnostics; this tranche used static AI-plan validation only.

## Changed files and identifiers

- `common/ai_strategy_plans/012_africa_focus_plans.txt`: added the external status/alignment constants and 32 route plans at lines 1809-4075.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_external_world_package_focus_ai_handoff_2026-07-30.md`: this handoff.

No commit was created. Parent review remains required before any package readiness or focus-tree prerequisite changes.
