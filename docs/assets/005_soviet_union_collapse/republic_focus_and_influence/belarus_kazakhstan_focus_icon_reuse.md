# Belarus And Kazakhstan Focus Icon Reuse Ledger

This ledger documents the implemented Belarus and Kazakhstan runtime focus icon assignments:

- Belarus: 83 focuses in `common/national_focus/005_soviet_collapse_republics.txt`, covering the clean-spec Minsk opening, first political route-lock block, rail-sovereignty branch, forest-defense branches, diplomacy/corridor branch, deeper logistics branch, late forest/military branch, and final diplomacy, League, and high-chaos finishers.
- Kazakhstan: 26 focuses in `common/national_focus/005_soviet_collapse_republics.txt`, covering the clean-spec Alma-Ata opening, southern-wire crisis, first route-lock block, decentralization convergence, and Karaganda resource-industry branch.

Both trees use branch-level sprites defined in `interface/005_soviet_collapse_blr_icons.gfx` and `interface/005_soviet_collapse_kaz_icons.gfx`. The branch-icon assignment is deliberate for the current implementation; each dedicated DDS is derived from existing generated Event 005 focus art that matches the branch gameplay subject. Belarus now satisfies the 83-focus clean-spec target.

## Belarus Sprite Mapping

| Branch | Focuses | Sprite | Final DDS | Reuse rationale |
| --- | ---: | --- | --- | --- |
| rail | 14 | `GFX_blr_soviet_collapse_rail` | `gfx/interface/goals/blr_soviet_collapse_rail.dds` | Common timetable art fits Minsk junction authority. |
| forest | 17 | `GFX_blr_soviet_collapse_forest` | `gfx/interface/goals/blr_soviet_collapse_forest.dds` | Forest corridor art fits marsh defense and partisan memory. |
| corridor | 19 | `GFX_blr_soviet_collapse_corridor` | `gfx/interface/goals/blr_soviet_collapse_corridor.dds` | Border-line art fits western passage and corridor-state outcomes. |
| legal | 7 | `GFX_blr_soviet_collapse_legal` | `gfx/interface/goals/blr_soviet_collapse_legal.dds` | Republican legality art fits statutes and civic law. |
| socialist | 2 | `GFX_blr_soviet_collapse_socialist` | `gfx/interface/goals/blr_soviet_collapse_socialist.dds` | Socialist sovereignty art fits workers' councils. |
| foreign_transit | 8 | `GFX_blr_soviet_collapse_foreign_transit` | `gfx/interface/goals/blr_soviet_collapse_foreign_transit.dds` | External mission art fits observer and relief transit. |
| counterintel | 5 | `GFX_blr_soviet_collapse_counterintel` | `gfx/interface/goals/blr_soviet_collapse_counterintel.dds` | Ministry-ledger art fits archives and security review. |
| civic | 11 | `GFX_blr_soviet_collapse_civic` | `gfx/interface/goals/blr_soviet_collapse_civic.dds` | First-orders art fits citizenship and post-corridor identity. |

## Kazakhstan Sprite Mapping

| Branch | Focuses | Sprite | Final DDS | Reuse rationale |
| --- | ---: | --- | --- | --- |
| alash | 3 | `GFX_kaz_soviet_collapse_alash` | `gfx/interface/goals/kaz_soviet_collapse_alash.dds` | Republican legality art fits the congress identity fork and Alash courts. |
| steppe_socialist | 2 | `GFX_kaz_soviet_collapse_steppe_socialist` | `gfx/interface/goals/kaz_soviet_collapse_steppe_socialist.dds` | Socialist sovereignty art fits the steppe republic and aul teachers. |
| federation | 5 | `GFX_kaz_soviet_collapse_federation` | `gfx/interface/goals/kaz_soviet_collapse_federation.dds` | Steppe congress art fits Alma-Ata, southern wires, Turkestan mandate, oasis-steppe congress, and League resource pooling. |
| resources | 8 | `GFX_kaz_soviet_collapse_resources` | `gfx/interface/goals/kaz_soviet_collapse_resources.dds` | Factory-defense art fits resource-town guards, the directorate, engineers, Karaganda boards, guarded oil, mine rail, pithead factories, and domestic resource control. |
| foreign | 3 | `GFX_kaz_soviet_collapse_foreign` | `gfx/interface/goals/kaz_soviet_collapse_foreign.dds` | External mission art fits southern guarantee diplomacy, concession debates, and technical missions. |
| myth | 0 | `GFX_kaz_soviet_collapse_myth` | `gfx/interface/goals/kaz_soviet_collapse_myth.dds` | Wired for the later high-chaos steppe branch, not used by the current opening slice. |
| military | 3 | `GFX_kaz_soviet_collapse_military` | `gfx/interface/goals/kaz_soviet_collapse_military.dds` | Field battalion art fits district inventory, resource-to-arms exchange, and the Steppe Arsenal. |
| settlement | 2 | `GFX_kaz_soviet_collapse_settlement` | `gfx/interface/goals/kaz_soviet_collapse_settlement.dds` | Steppe congress art fits distance-state and decentralized capital focuses. |

## Verification

The current tree parse confirms:

- Belarus has 83 focus blocks.
- Kazakhstan has 26 focus blocks.
- Together, the two trees have 109 implemented focuses with wired branch sprites.

## Historical Per-Focus Continuation Draft Entries

The entries below belong to the older large-tree draft ledger and should not be read as current implemented focus count evidence. The active implementation uses the compact focus files and docs as the source of truth.

## Belarus Per-Focus Continuation Reuse

| Focus | Sprite | Reuse rationale |
| --- | --- | --- |
| `blr_soviet_collapse_marsh_staff_schools` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_partisan_courier_lines` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_forest_depot_disguises` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_village_neutrality_guarantees` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_anti_raider_field_courts` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_green_depth_supply_roads` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_forest_front_rotation` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_republic_of_the_green_depth` | `GFX_blr_soviet_collapse_forest` | deliberate thematic reuse |
| `blr_soviet_collapse_corridor_inspection_service` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_western_passage_courts` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_league_ticket_offices` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_foreign_convoy_licenses` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_refugee_return_timetables` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_customs_anti_corruption_board` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_corridor_sovereignty_statute` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_state_that_controls_passage` | `GFX_blr_soviet_collapse_corridor` | deliberate thematic reuse |
| `blr_soviet_collapse_audit_emergency_oaths` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_minority_petition_chambers` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_property_claims_registry` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_military_detention_rules` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_constitutional_observer_benches` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_municipal_budget_law` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_postcrisis_election_calendar` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_law_above_the_corridor` | `GFX_blr_soviet_collapse_legal` | deliberate thematic reuse |
| `blr_soviet_collapse_archive_chain_of_custody` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_signal_authentication_rooms` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_foreign_agent_visitor_books` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_loyalist_amnesty_interrogations` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_committee_watch_limits` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_counter_sabotage_rail_cells` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_security_review_courts` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |
| `blr_soviet_collapse_quiet_state_doctrine` | `GFX_blr_soviet_collapse_counterintel` | deliberate thematic reuse |

## Kazakhstan Per-Focus Continuation Reuse

| Focus | Sprite | Reuse rationale |
| --- | --- | --- |
| `kaz_soviet_collapse_council_rotation_rules` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_trans_steppe_customs_courts` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_shared_rail_timetables` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_border_militia_arbitration` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_caspian_to_mountain_convoys` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_federation_language_services` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_equal_republic_veto_statute` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_federation_beyond_emergency` | `GFX_kaz_soviet_collapse_federation` | deliberate thematic reuse |
| `kaz_soviet_collapse_strategic_reserve_surveys` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_sovereign_concession_courts` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_mine_militia_academies` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_rail_mineral_priority_board` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_worker_safety_inspectorates` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_resource_bank_accounts` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_steppe_refinery_program` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_wealth_beneath_the_republic` | `GFX_kaz_soviet_collapse_resources` | deliberate thematic reuse |
| `kaz_soviet_collapse_consular_triangulation_desks` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_loan_treaty_review_rooms` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_border_mission_etiquette` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_observer_rotation_caps` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_mineral_credit_arbitration` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_intelligence_liaison_firebreaks` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_exile_passport_protocols` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_sovereign_multi_vector_doctrine` | `GFX_kaz_soviet_collapse_foreign` | deliberate thematic reuse |
| `kaz_soviet_collapse_long_range_staff_colleges` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_desert_winter_logistics` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_rail_junction_armor_schools` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_caspian_air_warning_net` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_frontier_signal_companies` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_settlement_reserve_cadres` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_army_depots_under_law` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
| `kaz_soviet_collapse_continental_defense_doctrine` | `GFX_kaz_soviet_collapse_military` | deliberate thematic reuse |
