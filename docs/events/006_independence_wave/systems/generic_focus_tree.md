# Event 006 generic focus tree

The imported `common/national_focus/006_independence_wave*.txt` sources define the one shared Event 006 focus tree, `independence_wave_focus_tree` (318 unique focus definitions: 184 direct `focus = {}` nodes, 134 full `shared_focus = {}` definitions, and 27 main-tree `shared_focus = <id>` import roots; 345 raw source entries when imports are counted). The shared definitions and import roots are one reusable tree surface, not additional country trees. Every admitted Event 006 release must publish either the full tree or a reviewed additive carrier overlay before package validation can succeed.

| Source surface | Direct `focus` blocks | `shared_focus` blocks | Role |
| --- | ---: | ---: | --- |
| `006_independence_wave_focus.txt` | 184 | 23 | Main tree declaration and shared roots |
| `006_independence_wave_iw043_iw058_focus.txt` | 0 | 48 | Volga/Assyria package modules |
| `006_independence_wave_iw093_iw098_focus.txt` | 0 | 43 | Asante/Sokoto package modules |
| `006_independence_wave_pacific_focus.txt` | 0 | 20 | Pacific package modules |
| **Resolved total** | **184 direct** | **134 full + 27 imports** | **One `independence_wave_focus_tree`** |

## Assignment contract

`common/scripted_effects/006_independence_wave_focus_effects.txt` is the sole assignment surface. A full-framework assignment sets `independence_wave_full_focus_framework` and `independence_wave_generic_focus_tree_assigned`, then loads `independence_wave_focus_tree`. An additive assignment never calls `load_focus_tree`; it sets `independence_wave_additive_focus_overlay` and `independence_wave_generic_focus_overlay_assigned` only after a package has registered a reviewed owning carrier. `common/scripted_triggers/006_independence_wave_focus_triggers.txt` exposes `has_independence_wave_generic_focus_contract` for validators and downstream loaders.

`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` applies the common finalization barrier. If a package adapter reports success without either contract, its final validation is changed to failure and the frozen release cannot commit. This keeps the generic tree universal without overwriting a living meaningful carrier tree.

The same assignment surface sets `independence_wave_generic_ai_profile` for every accepted full-framework or reviewed additive carrier, and generation cleanup clears it. The identity-neutral baseline profiles in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` read the public capacity, instability, recognition, host, and security values; package-specific AI remains additive. A release cannot pass final validation with the focus contract but without this baseline profile.

## Shared lanes

The tree is deliberately one dynamic framework rather than one static country template. Its regular focuses are shared by all full-framework countries, while researched regional and signature modules are gated shared-focus nodes in the same tree. There are no Event 006 country-specific `focus_tree` definitions in the release path.

| Lane | Representative focuses | Dynamic consumers |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration`, `independence_wave_inventory_the_state`, `independence_wave_complete_founding_settlement` | Capital control, Legitimacy, Government Capacity, Security, founding mission completion |
| Government and internal power | `independence_wave_prepare_first_assembly`, `independence_wave_organize_popular_councils`, `independence_wave_prepare_traditional_confirmation`, `independence_wave_establish_emergency_command`, patron, radical, and neutral-commission route families | The seven government route locks, concrete ruling-party/elections posture, power-struggle ledger, route ideas, instability, and recognition values |
| Economy and administration | `independence_wave_establish_emergency_revenue`, `independence_wave_build_regional_transport_authority`, `independence_wave_create_independent_treasury` | Capacity, Treasury idea lifecycle, anchor-state buildings, infrastructure, fuel, and transport archetype rewards |
| Military and security | `independence_wave_integrate_militia_commands`, `independence_wave_adopt_military_archetype_program`, `independence_wave_found_professional_defense_institution`, the mutually exclusive military choices | Force-profile equipment, Army Experience, doctrine reductions, Command Power, Security, and military route locks |
| Diplomacy, hosts, and patrons | `independence_wave_establish_foreign_office`, `independence_wave_seek_neighbor_recognition`, `independence_wave_define_former_host_policy`, the four host settlements, patron balance and treaty focuses | Recognition, host claim/property/population/obligation ledgers, patron influence, wars, guarantees, and diplomatic costs |
| Regional expansion | `independence_wave_survey_regional_ambition`, `independence_wave_call_regional_congress`, `independence_wave_build_postwar_integration_authority`, `independence_wave_coordinate_reclamation_fronts` | Region-family flags, border ambition, claims, integration authority, host pressure, and regional formable readiness |
| Network and league | `independence_wave_recognize_fellow_new_states`, `independence_wave_exchange_civil_servants`, `independence_wave_draft_league_charter`, `independence_wave_gather_founding_members`, `independence_wave_convene_league_congress` | Network Standing, aid corridors, charter proposals, league cohesion/defense/development/revisionism, and league actions |
| Formables and high chaos | `independence_wave_focus_discover_regional_identity`, `independence_wave_prepare_union_congress`, `independence_wave_write_formation_terms`, `independence_wave_establish_integration_commission`, `independence_wave_sponsor_further_ruptures`, `independence_wave_proclaim_open_sovereignty`, `independence_wave_rewrite_charter_of_borders`, `independence_wave_secure_durable_sovereignty` | Formable registry, paid congress/consent/integration gates, ambition factor, high-chaos mandate, revisionist pressure, and durable sovereignty |

Every lane uses the shared Event 006 scripted effects and constants. The tree does not create political-power stores, passive checklist missions, free-unit loops, or reward-only focuses. Completion rewards debit or change the visible public ledgers, host/patron/network/league values, territory preparation, ideas, force profile, or researched route state.

## Existing meaningful trees

Registered carriers with a meaningful vanilla tree keep that tree. Their Event 006 content is the additive overlay path, and the carrier trigger must prove that the overlay is actually owned by that carrier. Event 006 never assumes that a `shared_focus` declaration can inject nodes into an unrelated tree.

## Out-of-scope for this pass

Bespoke country focus trees and live/in-game testing are intentionally not part of the current implementation scope. Existing researched package modules remain gated shared nodes for compatibility and future package work; no new country-specific focus tree is added by the generic-tree contract.
