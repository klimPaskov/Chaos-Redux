# Country Decision Kits Matrix

This matrix summarizes Part 5. Working labels are implementation ids, not final localisation.

| Kit | Primary pool | Main temptation | Main cost | Main reform route | AI cap direction | Discovery route |
| --- | --- | --- | --- | --- | --- | --- |
| U.K. and Raj | Raj, Indian Ocean, and colonial emergency pools | wartime construction, manpower, dominion control | Raj burden, autonomy resistance, U.K. legitimacy damage | postwar Raj review, prisoner release, labor administration reform, dismantlement | light wartime use, zero after exposure or postwar reform | enemy capture, Raj autonomy crisis, postwar inspection, decolonization pressure |
| U.S.A. | wartime security zones, interior relocation sites, overseas security pools | limited counter-espionage and local works | civil liberties damage, court challenge, redress pressure | court review, termination, redress commission | rare activation, reform after threat falls | court review failure, postwar legal inquiry, enemy control of overseas sites |
| France and Vichy | camp legacy, Vichy collaboration, North Africa labor pools | collaboration security and colonial rail projects | refugee pressure, resistance, tribunal severity | inspection, legacy closure, colonial labor review, post-liberation reckoning | Vichy can expand, democratic and Free France reform | liberation, Allied capture, postwar tribunal, refugee pressure |
| Italy and Libya | Libya, East Africa, Balkan occupation fallback | desert logistics, roads, forts, security battalions | resistance, fuel and convoy burden, colonial claim damage | desert camp closure and local compensation | limited fascist colonial use, reform after regime change | Allied capture, local uprising, capitulation, colonial review |
| Belgium and Congo | Congo concession and transport corridor pools | resource extraction, transport corridors, exile economy support | Congo burden, strikes, accountability pressure | inspection, concession reform, local administration recognition | wartime or exile-limited, reform if democratic or exposed | international inspection, Congo unrest, decolonization crisis, postwar inquiry |
| Generic authoritarian | occupied non-core, colonial, non-core security, political-opposition route pools | construction, extraction, coercive control | stability drag, resistance, evidence, guard and rail burden | freeze, close, reform memory | conservative unless route-gated and at war | enemy capture, defeat, tribunal, legal review |
| Generic democratic | severe emergency or inherited active sites | limited emergency control | legitimacy damage and reform pressure | immediate legal review and dismantlement | near zero expansion | domestic review or inherited-site discovery |

## Decision family coverage

| Kit | Expansion | Management | Emergency | Reform | Aftermath |
| --- | --- | --- | --- | --- | --- |
| U.K. | `uk_activate_raj_emergency_detention`, `uk_expand_raj_detention_districts` | `uk_route_colonial_labor_to_military_construction`, `uk_demand_indian_manpower_levy` | `uk_tighten_dominion_security_coordination`, `uk_allocate_additional_colonial_guards` | `uk_release_political_prisoners_for_negotiations`, `uk_reform_colonial_labor_administration` | `uk_dismantle_raj_detention_network` |
| U.S.A. | `usa_authorize_emergency_relocation_zones`, `usa_expand_interior_security_camps` | `usa_assign_detainee_labor_to_local_works`, `usa_strengthen_wartime_review_boards` | `usa_allow_court_review` | `usa_release_detainees_under_supervision`, `usa_terminate_relocation_authority` | `usa_establish_redress_commission` |
| France and Vichy | `fr_expand_vichy_internment_administration`, `fr_route_north_africa_labor_to_rail_projects` | `fr_collaboration_transfer_records`, `fr_suppress_refugee_and_rescue_networks` | `fr_refugee_pressure_response` | `fr_inspect_camp_legacy`, `fr_close_camp_legacy_sites`, `fr_open_colonial_labor_review` | `fr_dismantle_north_africa_labor_network` |
| Italy | `ita_reopen_desert_camp_administration`, `ita_force_settlement_of_rebel_districts` | `ita_redirect_colonial_labor_to_roads_and_forts`, `ita_raise_colonial_security_battalions` | `ita_expand_desert_transport_guard` | `ita_close_desert_camps` | `ita_compensate_local_communities` |
| Belgium | `bel_expand_concession_labor_quotas`, `bel_route_labor_to_rubber_and_minerals` | `bel_build_congo_transport_corridors`, `bel_suppress_colonial_strikes` | `bel_open_international_inspection` | `bel_reform_concession_system` | `bel_recognize_local_administration` |
| Generic | `generic_activate_detention_network`, `generic_expand_labor_quotas` | `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_allocate_additional_guards` | `generic_destroy_evidence_before_retreat`, `generic_restricted_contaminated_site_escalation` | `generic_dismantle_detention_network` | `generic_reform_and_dismantlement` |

## Mission duration bands

| Band | Duration | Use |
| --- | --- | --- |
| Emergency activation | 90 to 120 days | survey, first inspection, court or security review |
| Standard project | 120 to 180 days | rail, roads, forts, resource, or local works |
| Suppression or unrest response | 120 to 210 days | state security, strike response, Raj security line, colonial sweep |
| Reform and dismantlement | 180 to 365 days | network closure, inspection, court review, concession reform, closure |
| Major postwar settlement | 270 to 540 days | redress, local administration, compensation, decolonization-facing reform |

## Asset id coverage

| Kit | Decision icons | Idea icons | Report or news images |
| --- | --- | --- | --- |
| U.K. | `GFX_decision_uk_raj_detention`, `GFX_decision_uk_colonial_labor_works` | `GFX_idea_uk_imperial_detention_administration`, `GFX_idea_raj_colonial_labor_burden` | `GFX_report_event_raj_detention_discovery`, `GFX_news_event_colonial_reckoning` |
| U.S.A. | `GFX_decision_usa_emergency_relocation`, `GFX_decision_usa_court_review`, `GFX_decision_usa_redress_commission` | `GFX_idea_usa_wartime_security_authority`, `GFX_idea_usa_civil_liberties_damage` | `GFX_report_event_usa_relocation_review` |
| France and Vichy | `GFX_decision_fr_camp_legacy_review`, `GFX_decision_vichy_internment_admin`, `GFX_decision_fr_north_africa_labor` | `GFX_idea_fr_camp_legacy`, `GFX_idea_vichy_collaboration_repression` | `GFX_report_event_fr_liberated_camp_records`, `GFX_news_event_vichy_reckoning` |
| Italy | `GFX_decision_ita_desert_camp_admin`, `GFX_decision_ita_colonial_road_labor`, `GFX_decision_ita_camp_closure` | `GFX_idea_ita_desert_camp_administration`, `GFX_idea_ita_libyan_resistance_pressure` | `GFX_report_event_libyan_camp_discovery` |
| Belgium | `GFX_decision_bel_congo_concession_quota`, `GFX_decision_bel_congo_transport_corridor`, `GFX_decision_bel_colonial_inspection` | `GFX_idea_bel_congo_extraction_pressure`, `GFX_idea_congo_concession_labor_burden` | `GFX_report_event_congo_labor_discovery`, `GFX_news_event_congo_colonial_reckoning` |
| Generic | `GFX_decision_generic_expand_labor_network`, `GFX_decision_generic_dismantle_network`, `GFX_decision_generic_destroy_evidence`, `GFX_decision_generic_guard_allocation` | `GFX_idea_generic_detention_network`, `GFX_idea_generic_overextended_repression_network` | `GFX_report_event_generic_camp_discovery`, `GFX_news_event_global_atrocity_evidence` |
