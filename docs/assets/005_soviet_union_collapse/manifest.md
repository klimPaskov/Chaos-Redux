# Soviet Union Collapse Asset Manifest

## Package Status

The event script uses stable sprite and idea names. The active news, report, and primary super-event image candidates are sourced, processed, converted, and wired. Dedicated idea, decision, and shared focus icon sprite names are wired through stable filenames, with generated source PNGs, processed previews, final DDS files, and `.gfx` entries in place for active gameplay content.

The package now contains sourced news, report, and super-event images under `docs/assets/005_soviet_union_collapse/`, event-picture DDS files under `gfx/event_pictures/`, super-event DDS files under `gfx/super_events/`, and generated active idea, decision, and shared focus icon DDS files under the normal interface folders.

The active idea, decision, and shared focus icon package is generated from scratch with Codex built-in `image_gen`, cleaned, centered, converted, and wired. Branch-specific future tags and optional branches still need their own visual packages if those branches become active full country content.


The republic focus and influence expansion asset ledger lives at `docs/assets/005_soviet_union_collapse/republic_focus_and_influence/manifest.md`. It records the Ukraine, Belarus, Kazakhstan, regional republic, foreign patron, volunteer, regional faction, custom splinter, report-image, and super-event asset state for the continuation prompt.

The sourced report and super-event image source queue lives at `docs/assets/005_soviet_union_collapse/source_image_tracking_queue.md`. It lists every wired sourced image marked `sourced`, along with source links, author or archive notes, license notes, processed previews, final DDS paths, and contact sheets.

## Latest Source-Image Tracking State

The latest continuation recheck found `16` sourced report and super-event image rows: `6` report images and `10` super-event images. The matching art-pass sheet at `docs/assets/005_soviet_union_collapse/source_image_art_pass_sheet.md` has `48` empty optional art-pass boxes and `0` checked boxes. Every sourced report and super-event image row is tracked as `sourced`.

Latest direct asset recount confirms active news sprites/files at `3/3`, active report sprites/files at `6/6`, sourced-image contact sheets at `4/4`, and super-event slots `14` through `27` at `14/14` for sprite definitions, DDS files, title/description/button/quote localisation, image selectors, show helpers, script constant IDs, and documented audio slots.

Optional source/crop choices can be recorded in the art-pass sheet, but empty boxes do not block Event 005 completion. Processed PNG previews, final DDS files, sprite definitions, and contact sheets are implementation and source evidence for the current wired rows.

## Active Wiring

| Use | Current sprite or picture | Final replacement needed |
| --- | --- | --- |
| Opening news | `GFX_news_soviet_union_collapse` | wired; art pass optional |
| League news | `GFX_news_free_republics_league` | wired; art pass optional |
| Second-seal news | `GFX_news_union_unmade` | wired; art pass optional |
| Union-war news | `GFX_news_union_unmade` | wired; a dedicated union-war variant can be added later |
| Soviet report events | `GFX_report_union_crisis`, `GFX_report_breakaway_mobilization`, `GFX_report_depot_war`, `GFX_report_foreign_liaison`, `GFX_report_old_underground`, `GFX_report_railway_sovereignty` | wired, `sourced` |
| Idea icons | dedicated `GFX_idea_*` sprites in `interface/005_soviet_collapse_icons.gfx` | complete for active ideas |
| Decision icons | dedicated `GFX_decision_*` sprites in `interface/005_soviet_collapse_icons.gfx` | complete for active decisions |
| Shared breakaway focus icons | dedicated `GFX_focus_soviet_collapse_*` sprites in `interface/005_soviet_collapse_icons.gfx` | complete for the active 53-focus shared fallback tree through deliberate icon reuse |
| Regional republic focus icons | dedicated `GFX_baltic_soviet_collapse_*`, `GFX_caucasus_soviet_collapse_*`, `GFX_central_asia_soviet_collapse_*`, and `GFX_moldova_soviet_collapse_*` sprites in `interface/005_soviet_collapse_regional_icons.gfx` | complete for active regional runtime focus trees |
| Super-event | `GFX_super_event_union_unmade`, `GFX_super_event_map_larger_than_union`, `GFX_super_event_steppe_beyond_history`, `GFX_super_event_corridors_decide`, `GFX_super_event_bread_state`, `GFX_super_event_league_equal_republics`, `GFX_super_event_steppe_federation`, `GFX_super_event_baltic_restoration_pact`, `GFX_super_event_caucasus_defense_compact`, `GFX_super_event_eastern_buffer_coalition` | sourced and wired |

## Required Active News Images

All news images target 397x153 DDS and should be black-and-white documentary style.

| Asset | Sprite | Source mode | Source PNG | Processed PNG | Final DDS | GFX file | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Opening Soviet collapse | `GFX_news_soviet_union_collapse` | internet source image | `docs/assets/005_soviet_union_collapse/source_png/news_soviet_union_collapse_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_soviet_union_collapse.png` | `gfx/event_pictures/news_soviet_union_collapse.dds` | `interface/chaosx_pictures.gfx` | wired |
| Free Republics' League | `GFX_news_free_republics_league` | internet source image | `docs/assets/005_soviet_union_collapse/source_png/news_free_republics_league_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_free_republics_league.png` | `gfx/event_pictures/news_free_republics_league.dds` | `interface/chaosx_pictures.gfx` | wired |
| Union unmade/deep collapse | `GFX_news_union_unmade` | internet source image | `docs/assets/005_soviet_union_collapse/source_png/news_union_unmade_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_union_unmade.png` | `gfx/event_pictures/news_union_unmade.dds` | `interface/chaosx_pictures.gfx` | wired |

## Required Active Report Images

All report images target 210x176 DDS and should use documentary-style source imagery marked for source tracking.

| Asset | Sprite | Source mode | Source PNG | Processed PNG | Final DDS | GFX file | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Union crisis report | `GFX_report_union_crisis` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/report_union_crisis_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/report_union_crisis.png` | `gfx/event_pictures/report_union_crisis.dds` | `interface/chaosx_pictures.gfx` | wired, `sourced` |
| Breakaway mobilization | `GFX_report_breakaway_mobilization` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/report_breakaway_mobilization_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/report_breakaway_mobilization.png` | `gfx/event_pictures/report_breakaway_mobilization.dds` | `interface/chaosx_pictures.gfx` | wired, `sourced` |
| Depot war | `GFX_report_depot_war` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/report_depot_war_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/report_depot_war.png` | `gfx/event_pictures/report_depot_war.dds` | `interface/chaosx_pictures.gfx` | wired, `sourced` |
| Foreign liaison | `GFX_report_foreign_liaison` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/report_foreign_liaison_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/report_foreign_liaison.png` | `gfx/event_pictures/report_foreign_liaison.dds` | `interface/chaosx_pictures.gfx` | wired, `sourced` |
| Old underground | `GFX_report_old_underground` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/report_old_underground_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/report_old_underground.png` | `gfx/event_pictures/report_old_underground.dds` | `interface/chaosx_pictures.gfx` | wired, `sourced` |
| Railway sovereignty | `GFX_report_railway_sovereignty` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/report_railway_sovereignty_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/report_railway_sovereignty.png` | `gfx/event_pictures/report_railway_sovereignty.dds` | `interface/chaosx_pictures.gfx` | wired, `sourced` |

## Required Active Idea Icons

All active idea icons use the vanilla national spirit card size, normally 60x68 DDS. They are generated from `image_gen` source sheets, cleaned into transparent processed PNG previews, converted to DDS, and registered in `interface/005_soviet_collapse_icons.gfx`.

| Idea | Sprite | Final DDS | Status |
| --- | --- | --- | --- |
| `soviet_collapse_union_crisis` | `GFX_idea_union_crisis` | `gfx/interface/ideas/idea_union_crisis.dds` | complete |
| `soviet_collapse_emergency_union_authority` | `GFX_idea_emergency_union_authority` | `gfx/interface/ideas/idea_emergency_union_authority.dds` | complete |
| `soviet_collapse_new_union_negotiations` | `GFX_idea_new_union_negotiations` | `gfx/interface/ideas/idea_new_union_negotiations.dds` | complete |
| `soviet_collapse_union_restored` | `GFX_idea_union_restored` | `gfx/interface/ideas/idea_union_restored.dds` | complete |
| `soviet_collapse_hollow_ministries` | `GFX_idea_hollow_ministries` | `gfx/interface/ideas/idea_hollow_ministries.dds` | complete |
| `soviet_collapse_loyalist_officer_corps` | `GFX_idea_loyalist_officer_corps` | `gfx/interface/ideas/idea_loyalist_officer_corps.dds` | complete |
| `soviet_collapse_emergency_mobilization` | `GFX_idea_emergency_mobilization` | `gfx/interface/ideas/idea_emergency_mobilization.dds` | complete |
| `soviet_collapse_popular_defense_committees` | `GFX_idea_popular_defense_committees` | `gfx/interface/ideas/idea_popular_defense_committees.dds` | complete |
| `soviet_collapse_captured_soviet_depots` | `GFX_idea_captured_soviet_depots` | `gfx/interface/ideas/idea_captured_soviet_depots.dds` | complete |
| `soviet_collapse_defensive_coordination` | `GFX_idea_defensive_coordination` | `gfx/interface/ideas/idea_defensive_coordination.dds` | complete |
| `soviet_collapse_foreign_volunteers` | `GFX_idea_foreign_volunteers` | `gfx/interface/ideas/idea_foreign_volunteers.dds` | complete |
| `soviet_collapse_exile_volunteer_rolls` | `GFX_idea_exile_volunteer_rolls` | `gfx/interface/ideas/idea_exile_volunteer_rolls.dds` | complete |
| `soviet_collapse_ideological_brigades` | `GFX_idea_ideological_brigades` | `gfx/interface/ideas/idea_ideological_brigades.dds` | complete |
| `soviet_collapse_medical_missions` | `GFX_idea_medical_missions` | `gfx/interface/ideas/idea_medical_missions.dds` | complete |
| `soviet_collapse_prisoner_volunteer_battalions` | `GFX_idea_prisoner_volunteer_battalions` | `gfx/interface/ideas/idea_prisoner_volunteer_battalions.dds` | complete |
| `soviet_collapse_high_chaos_volunteers` | `GFX_idea_high_chaos_volunteers` | `gfx/interface/ideas/idea_high_chaos_volunteers.dds` | complete |
| `soviet_collapse_legal_restoration_claim` | `GFX_idea_legal_restoration_claim` | `gfx/interface/ideas/idea_legal_restoration_claim.dds` | complete |
| `soviet_collapse_socialist_sovereignty` | `GFX_idea_socialist_sovereignty` | `gfx/interface/ideas/idea_socialist_sovereignty.dds` | complete |
| `soviet_collapse_military_defense_council` | `GFX_idea_military_defense_council` | `gfx/interface/ideas/idea_military_defense_council.dds` | complete |
| `soviet_collapse_old_underground_networks` | `GFX_idea_old_underground_networks` | `gfx/interface/ideas/idea_old_underground_networks.dds` | complete |
| `soviet_collapse_black_banner_defense_committees` | `GFX_idea_old_underground_networks` | `gfx/interface/ideas/idea_old_underground_networks.dds` | reuses complete Old Underground icon |
| `soviet_collapse_red_resistance_without_moscow` | `GFX_idea_red_resistance_without_moscow` | `gfx/interface/ideas/idea_red_resistance_without_moscow.dds` | complete |
| `soviet_collapse_local_committee_wars` | `GFX_idea_local_committee_wars` | `gfx/interface/ideas/idea_local_committee_wars.dds` | complete |
| `soviet_collapse_railway_sovereignty` | `GFX_idea_railway_sovereignty` | `gfx/interface/ideas/idea_railway_sovereignty.dds` | complete |
| `soviet_collapse_flags_return_incorrectly` | `GFX_idea_flags_return_incorrectly` | `gfx/interface/ideas/idea_flags_return_incorrectly.dds` | complete |
| `soviet_collapse_hybrid_authorities` | `GFX_idea_hybrid_authorities` | `gfx/interface/ideas/idea_hybrid_authorities.dds` | complete |

### Generated Idea Icon Records

The active idea icons were regenerated from scratch with Codex built-in `image_gen` from the Soviet-collapse-specific sheet at `docs/assets/005_soviet_union_collapse/source_png/idea_active_soviet_collapse_sheet_source.png`. Shared prompt summary: clean low-grain HOI4 national-spirit icons with centered silhouettes, Soviet crisis government and military symbols, transparent unused space requested, no colored matte, no green/chroma background, no generated text, no labels, no watermarks, no white outline, and no baked shadow. The generated sheet used fake checker transparency, so the processed icons were rebuilt with the generated icon cleanup method documented in `.agents/skills/chaos-redux-event-assets/SKILL.md`: filled subject-support masks, preserved dark interior artwork, matte/checker removal, transparent unused canvas, subtle black outline, and slight black drop shadow.

Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/soviet_collapse_idea_icons.png`

| Idea | Source PNG | Processed PNG | Final DDS | Target size | GFX file | Source status | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `soviet_collapse_emergency_union_authority` | `docs/assets/005_soviet_union_collapse/source_png/idea_emergency_union_authority_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_emergency_union_authority.png` | `gfx/interface/ideas/idea_emergency_union_authority.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_military_defense_council` | `docs/assets/005_soviet_union_collapse/source_png/idea_military_defense_council_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_military_defense_council.png` | `gfx/interface/ideas/idea_military_defense_council.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_old_underground_networks` | `docs/assets/005_soviet_union_collapse/source_png/idea_old_underground_networks_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_old_underground_networks.png` | `gfx/interface/ideas/idea_old_underground_networks.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_loyalist_officer_corps` | `docs/assets/005_soviet_union_collapse/source_png/idea_loyalist_officer_corps_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_loyalist_officer_corps.png` | `gfx/interface/ideas/idea_loyalist_officer_corps.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_union_crisis` | `docs/assets/005_soviet_union_collapse/source_png/idea_union_crisis_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_union_crisis.png` | `gfx/interface/ideas/idea_union_crisis.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_new_union_negotiations` | `docs/assets/005_soviet_union_collapse/source_png/idea_new_union_negotiations_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_new_union_negotiations.png` | `gfx/interface/ideas/idea_new_union_negotiations.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_union_restored` | `docs/assets/005_soviet_union_collapse/source_png/idea_union_restored_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_union_restored.png` | `gfx/interface/ideas/idea_union_restored.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_hollow_ministries` | `docs/assets/005_soviet_union_collapse/source_png/idea_hollow_ministries_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_hollow_ministries.png` | `gfx/interface/ideas/idea_hollow_ministries.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_emergency_mobilization` | `docs/assets/005_soviet_union_collapse/source_png/idea_emergency_mobilization_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_emergency_mobilization.png` | `gfx/interface/ideas/idea_emergency_mobilization.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_popular_defense_committees` | `docs/assets/005_soviet_union_collapse/source_png/idea_popular_defense_committees_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_popular_defense_committees.png` | `gfx/interface/ideas/idea_popular_defense_committees.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_captured_soviet_depots` | `docs/assets/005_soviet_union_collapse/source_png/idea_captured_soviet_depots_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_captured_soviet_depots.png` | `gfx/interface/ideas/idea_captured_soviet_depots.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_defensive_coordination` | `docs/assets/005_soviet_union_collapse/source_png/idea_defensive_coordination_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_defensive_coordination.png` | `gfx/interface/ideas/idea_defensive_coordination.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_foreign_volunteers` | `docs/assets/005_soviet_union_collapse/source_png/idea_foreign_volunteers_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_foreign_volunteers.png` | `gfx/interface/ideas/idea_foreign_volunteers.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_legal_restoration_claim` | `docs/assets/005_soviet_union_collapse/source_png/idea_legal_restoration_claim_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_legal_restoration_claim.png` | `gfx/interface/ideas/idea_legal_restoration_claim.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_socialist_sovereignty` | `docs/assets/005_soviet_union_collapse/source_png/idea_socialist_sovereignty_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_socialist_sovereignty.png` | `gfx/interface/ideas/idea_socialist_sovereignty.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_red_resistance_without_moscow` | `docs/assets/005_soviet_union_collapse/source_png/idea_red_resistance_without_moscow_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_red_resistance_without_moscow.png` | `gfx/interface/ideas/idea_red_resistance_without_moscow.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_local_committee_wars` | `docs/assets/005_soviet_union_collapse/source_png/idea_local_committee_wars_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_local_committee_wars.png` | `gfx/interface/ideas/idea_local_committee_wars.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_railway_sovereignty` | `docs/assets/005_soviet_union_collapse/source_png/idea_railway_sovereignty_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_railway_sovereignty.png` | `gfx/interface/ideas/idea_railway_sovereignty.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_flags_return_incorrectly` | `docs/assets/005_soviet_union_collapse/source_png/idea_flags_return_incorrectly_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_flags_return_incorrectly.png` | `gfx/interface/ideas/idea_flags_return_incorrectly.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_hybrid_authorities` | `docs/assets/005_soviet_union_collapse/source_png/idea_hybrid_authorities_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/idea_hybrid_authorities.png` | `gfx/interface/ideas/idea_hybrid_authorities.dds` | 60x68 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |

## Required Active Decision Icons

Decision icons use vanilla decision icon dimensions. Active decision DDS files are generated at 32x32, while decision category DDS files are generated at 52x40, processed, converted, and registered in `interface/005_soviet_collapse_icons.gfx`.

| Decision or category | Sprite | Final DDS | Status |
| --- | --- | --- | --- |
| `soviet_collapse_soviet_category` | `GFX_decision_category_soviet_collapse_soviet` | `gfx/interface/decisions/decision_category_soviet_collapse_soviet.dds` | complete |
| `soviet_collapse_breakaway_category` | `GFX_decision_category_soviet_collapse_breakaway` | `gfx/interface/decisions/decision_category_soviet_collapse_breakaway.dds` | complete |
| `soviet_collapse_reclaim_breakaway_republics` | `GFX_decision_reclaim_breakaway_state` | `gfx/interface/decisions/decision_reclaim_breakaway_state.dds` | complete |
| `soviet_collapse_restore_party_control` | `GFX_decision_restore_party_control` | `gfx/interface/decisions/decision_restore_party_control.dds` | complete |
| `soviet_collapse_send_loyalist_officers` | `GFX_decision_send_loyalist_officers` | `gfx/interface/decisions/decision_send_loyalist_officers.dds` | complete |
| `soviet_collapse_offer_autonomy` | `GFX_decision_offer_autonomy` | `gfx/interface/decisions/decision_offer_autonomy.dds` | complete |
| `soviet_collapse_cut_rebel_supply_routes` | `GFX_decision_cut_rebel_supply_routes` | `gfx/interface/decisions/decision_cut_rebel_supply_routes.dds` | complete |
| `soviet_collapse_arrest_separatist_leadership` | `GFX_decision_arrest_separatist_leadership` | `gfx/interface/decisions/decision_arrest_separatist_leadership.dds` | complete |
| `soviet_collapse_emergency_mobilize_reserves` | `GFX_decision_emergency_mobilization` | `gfx/interface/decisions/decision_emergency_mobilization.dds` | complete |
| `soviet_collapse_declare_union_indivisible` | `GFX_decision_declare_union_indivisible` | `gfx/interface/decisions/decision_declare_union_indivisible.dds` | complete |
| `soviet_collapse_join_free_republics_league` | `GFX_decision_join_free_republics_league` | `gfx/interface/decisions/decision_join_free_republics_league.dds` | complete |
| `soviet_collapse_request_foreign_recognition` | `GFX_decision_request_foreign_recognition` | `gfx/interface/decisions/decision_request_foreign_recognition.dds` | complete |
| `soviet_collapse_mobilize_defense_units` | `GFX_decision_mobilize_defense_units` | `gfx/interface/decisions/decision_mobilize_defense_units.dds` | complete |
| `soviet_collapse_seize_depots` | `GFX_decision_seize_depots` | `gfx/interface/decisions/decision_seize_depots.dds` | complete |
| `soviet_collapse_call_other_republics_to_rise` | `GFX_decision_call_other_republics_to_rise` | `gfx/interface/decisions/decision_call_other_republics_to_rise.dds` | complete |
| `soviet_collapse_coordinate_fronts` | `GFX_decision_coordinate_fronts` | `gfx/interface/decisions/decision_coordinate_fronts.dds` | complete |
| `soviet_collapse_bargain_black_banner_committees` | `GFX_decision_mobilize_defense_units` | `gfx/interface/decisions/decision_mobilize_defense_units.dds` | reuses complete active icon |
| `soviet_collapse_contain_black_banner_committees` | `GFX_decision_restore_party_control` | `gfx/interface/decisions/decision_restore_party_control.dds` | reuses complete active icon |
| `soviet_collapse_foreign_patron_category` | `GFX_decision_category_soviet_collapse_foreign_patron` | `gfx/interface/decisions/decision_category_soviet_collapse_foreign_patron.dds` | complete |
| `soviet_collapse_recognize_breakaway_government` | `GFX_decision_soviet_collapse_foreign_recognition` | `gfx/interface/decisions/decision_soviet_collapse_foreign_recognition.dds` | complete |
| `soviet_collapse_fund_ideological_liaison_offices` | `GFX_decision_soviet_collapse_foreign_ideology` | `gfx/interface/decisions/decision_soviet_collapse_foreign_ideology.dds` | complete |
| `soviet_collapse_ship_border_armaments` | `GFX_decision_soviet_collapse_foreign_armaments` | `gfx/interface/decisions/decision_soviet_collapse_foreign_armaments.dds` | complete |
| `soviet_collapse_dispatch_military_advisers` | `GFX_decision_soviet_collapse_foreign_advisers` | `gfx/interface/decisions/decision_soviet_collapse_foreign_advisers.dds` | complete |
| `soviet_collapse_open_republican_intelligence_channel` | `GFX_decision_soviet_collapse_foreign_intelligence` | `gfx/interface/decisions/decision_soviet_collapse_foreign_intelligence.dds` | complete |
| `soviet_collapse_sponsor_volunteer_corps` | `GFX_decision_soviet_collapse_foreign_volunteers` | `gfx/interface/decisions/decision_soviet_collapse_foreign_volunteers.dds` | complete |
| `soviet_collapse_negotiate_republican_trade_mission` | `GFX_decision_soviet_collapse_foreign_trade` | `gfx/interface/decisions/decision_soviet_collapse_foreign_trade.dds` | complete |
| `soviet_collapse_open_exile_volunteer_rolls` | `GFX_decision_soviet_collapse_exile_volunteers` | `gfx/interface/decisions/decision_soviet_collapse_exile_volunteers.dds` | complete |
| `soviet_collapse_accept_ideological_brigades` | `GFX_decision_soviet_collapse_ideological_brigades` | `gfx/interface/decisions/decision_soviet_collapse_ideological_brigades.dds` | complete |
| `soviet_collapse_host_medical_missions` | `GFX_decision_soviet_collapse_medical_missions` | `gfx/interface/decisions/decision_soviet_collapse_medical_missions.dds` | complete |
| `soviet_collapse_mobilize_prisoner_volunteers` | `GFX_decision_soviet_collapse_prisoner_volunteers` | `gfx/interface/decisions/decision_soviet_collapse_prisoner_volunteers.dds` | complete |
| `soviet_collapse_raise_high_chaos_volunteers` | `GFX_decision_soviet_collapse_high_chaos_volunteers` | `gfx/interface/decisions/decision_soviet_collapse_high_chaos_volunteers.dds` | complete |
| `soviet_collapse_regional_faction_category` | `GFX_decision_category_soviet_collapse_regional_faction` | `gfx/interface/decisions/decision_category_soviet_collapse_regional_faction.dds` | complete |
| `soviet_collapse_found_baltic_restoration_pact` | `GFX_decision_soviet_collapse_baltic_restoration_pact` | `gfx/interface/decisions/decision_soviet_collapse_baltic_restoration_pact.dds` | complete |
| `soviet_collapse_found_caucasus_defense_compact` | `GFX_decision_soviet_collapse_caucasus_defense_compact` | `gfx/interface/decisions/decision_soviet_collapse_caucasus_defense_compact.dds` | complete |
| `soviet_collapse_found_steppe_federation` | `GFX_decision_soviet_collapse_steppe_federation` | `gfx/interface/decisions/decision_soviet_collapse_steppe_federation.dds` | complete |
| `soviet_collapse_found_black_international` | `GFX_decision_soviet_collapse_black_international` | `gfx/interface/decisions/decision_soviet_collapse_black_international.dds` | complete |
| `soviet_collapse_found_free_soviet_congress` | `GFX_decision_soviet_collapse_free_soviet_congress` | `gfx/interface/decisions/decision_soviet_collapse_free_soviet_congress.dds` | complete |
| `soviet_collapse_found_eastern_buffer_coalition` | `GFX_decision_soviet_collapse_eastern_buffer_coalition` | `gfx/interface/decisions/decision_soviet_collapse_eastern_buffer_coalition.dds` | complete |
| `soviet_collapse_found_dead_international` | `GFX_decision_soviet_collapse_dead_international` | `gfx/interface/decisions/decision_soviet_collapse_dead_international.dds` | complete |
| `soviet_collapse_found_iron_production_bloc` | `GFX_decision_soviet_collapse_iron_production_bloc` | `gfx/interface/decisions/decision_soviet_collapse_iron_production_bloc.dds` | complete |
| `soviet_collapse_invite_regional_partners` | `GFX_decision_soviet_collapse_regional_invite` | `gfx/interface/decisions/decision_soviet_collapse_regional_invite.dds` | complete |
| `soviet_collapse_coordinate_regional_faction` | `GFX_decision_soviet_collapse_regional_coordinate` | `gfx/interface/decisions/decision_soviet_collapse_regional_coordinate.dds` | complete |
| `soviet_collapse_set_regional_defense_goal` | `GFX_decision_soviet_collapse_regional_goal_defense` | `gfx/interface/decisions/decision_soviet_collapse_regional_goal_defense.dds` | complete |
| `soviet_collapse_set_regional_recognition_goal` | `GFX_decision_soviet_collapse_regional_goal_recognition` | `gfx/interface/decisions/decision_soviet_collapse_regional_goal_recognition.dds` | complete |
| `soviet_collapse_set_regional_logistics_goal` | `GFX_decision_soviet_collapse_regional_goal_logistics` | `gfx/interface/decisions/decision_soviet_collapse_regional_goal_logistics.dds` | complete |
| `soviet_collapse_reduce_regional_faction_tension` | `GFX_decision_soviet_collapse_regional_tension` | `gfx/interface/decisions/decision_soviet_collapse_regional_tension.dds` | complete |
| `soviet_collapse_withdraw_from_regional_faction` | `GFX_decision_soviet_collapse_regional_withdraw` | `gfx/interface/decisions/decision_soviet_collapse_regional_withdraw.dds` | complete |

### Generated Decision Icon Records

These icons were regenerated from scratch with Codex built-in `image_gen` from a Soviet-collapse-specific decision sheet preserved at `docs/assets/005_soviet_union_collapse/source_png/decision_active_soviet_collapse_sheet_source.png`. Shared prompt summary: clean HOI4-style decision and decision category icons with one central symbol, Soviet collapse motifs, transparent unused space requested, no colored matte, no green/chroma background, no generated text, no labels, no watermarks, no white outline, low texture, and no baked shadow. The generated sheet used fake checker transparency, so the processed icons were centered with the generated icon cleanup method documented in `.agents/skills/chaos-redux-event-assets/SKILL.md`: filled subject-support masks, preserved dark interior artwork, matte/checker removal, transparent unused canvas, subtle black outline, and slight black drop shadow.

Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/soviet_collapse_decision_icons.png`

| Decision or category | Source PNG | Processed PNG | Final DDS | Target size | GFX file | Source status | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `soviet_collapse_soviet_category` | `docs/assets/005_soviet_union_collapse/source_png/decision_category_soviet_collapse_soviet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_category_soviet_collapse_soviet.png` | `gfx/interface/decisions/decision_category_soviet_collapse_soviet.dds` | 52x40 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_breakaway_category` | `docs/assets/005_soviet_union_collapse/source_png/decision_category_soviet_collapse_breakaway_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_category_soviet_collapse_breakaway.png` | `gfx/interface/decisions/decision_category_soviet_collapse_breakaway.dds` | 52x40 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_foreign_patron_category` | `docs/assets/005_soviet_union_collapse/source_png/decision_category_soviet_collapse_foreign_patron_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_category_soviet_collapse_foreign_patron.png` | `gfx/interface/decisions/decision_category_soviet_collapse_foreign_patron.dds` | 52x40 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_regional_faction_category` | `docs/assets/005_soviet_union_collapse/source_png/decision_category_soviet_collapse_regional_faction_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_category_soviet_collapse_regional_faction.png` | `gfx/interface/decisions/decision_category_soviet_collapse_regional_faction.dds` | 52x40 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_reclaim_breakaway_republics` | `docs/assets/005_soviet_union_collapse/source_png/decision_reclaim_breakaway_state_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_reclaim_breakaway_state.png` | `gfx/interface/decisions/decision_reclaim_breakaway_state.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_restore_party_control` | `docs/assets/005_soviet_union_collapse/source_png/decision_restore_party_control_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_restore_party_control.png` | `gfx/interface/decisions/decision_restore_party_control.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_send_loyalist_officers` | `docs/assets/005_soviet_union_collapse/source_png/decision_send_loyalist_officers_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_send_loyalist_officers.png` | `gfx/interface/decisions/decision_send_loyalist_officers.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_offer_autonomy` | `docs/assets/005_soviet_union_collapse/source_png/decision_offer_autonomy_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_offer_autonomy.png` | `gfx/interface/decisions/decision_offer_autonomy.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_cut_rebel_supply_routes` | `docs/assets/005_soviet_union_collapse/source_png/decision_cut_rebel_supply_routes_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_cut_rebel_supply_routes.png` | `gfx/interface/decisions/decision_cut_rebel_supply_routes.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_arrest_separatist_leadership` | `docs/assets/005_soviet_union_collapse/source_png/decision_arrest_separatist_leadership_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_arrest_separatist_leadership.png` | `gfx/interface/decisions/decision_arrest_separatist_leadership.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_emergency_mobilize_reserves` | `docs/assets/005_soviet_union_collapse/source_png/decision_emergency_mobilization_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_emergency_mobilization.png` | `gfx/interface/decisions/decision_emergency_mobilization.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_declare_union_indivisible` | `docs/assets/005_soviet_union_collapse/source_png/decision_declare_union_indivisible_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_declare_union_indivisible.png` | `gfx/interface/decisions/decision_declare_union_indivisible.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_join_free_republics_league` | `docs/assets/005_soviet_union_collapse/source_png/decision_join_free_republics_league_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_join_free_republics_league.png` | `gfx/interface/decisions/decision_join_free_republics_league.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_request_foreign_recognition` | `docs/assets/005_soviet_union_collapse/source_png/decision_request_foreign_recognition_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_request_foreign_recognition.png` | `gfx/interface/decisions/decision_request_foreign_recognition.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_mobilize_defense_units` | `docs/assets/005_soviet_union_collapse/source_png/decision_mobilize_defense_units_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_mobilize_defense_units.png` | `gfx/interface/decisions/decision_mobilize_defense_units.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_seize_depots` | `docs/assets/005_soviet_union_collapse/source_png/decision_seize_depots_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_seize_depots.png` | `gfx/interface/decisions/decision_seize_depots.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_call_other_republics_to_rise` | `docs/assets/005_soviet_union_collapse/source_png/decision_call_other_republics_to_rise_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_call_other_republics_to_rise.png` | `gfx/interface/decisions/decision_call_other_republics_to_rise.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_coordinate_fronts` | `docs/assets/005_soviet_union_collapse/source_png/decision_coordinate_fronts_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/decision_coordinate_fronts.png` | `gfx/interface/decisions/decision_coordinate_fronts.dds` | 32x32 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |

## Required Shared Focus Sprite Assets

The 53-focus shared breakaway focus tree is active gameplay content in `common/national_focus/005_soviet_collapse_republics.txt`. Shared focus sprite assets are generated at 94x86, processed, converted, registered in `interface/005_soviet_collapse_icons.gfx`, and referenced by the shared focus tree through deliberate branch and theme reuse. Several sprite asset names come from the earlier compact tree and remain stable so other Event 005 icon packages can reuse the same DDS files. The regional republic runtime trees derive dedicated focus-id assets from this generated art, but now use their own PNG/DDS files and sprite definitions recorded in the republic focus and influence expansion asset ledger.

| Sprite asset row | Current icon | Final status |
| --- | --- | --- |
| `soviet_collapse_assemble_emergency_government` | `GFX_focus_soviet_collapse_assemble_emergency_government` | complete |
| `soviet_collapse_guard_the_radio_stations` | `GFX_focus_soviet_collapse_guard_the_radio_stations` | complete |
| `soviet_collapse_secure_ministry_ledgers` | `GFX_focus_soviet_collapse_secure_ministry_ledgers` | complete |
| `soviet_collapse_factory_defense_committees` | `GFX_focus_soviet_collapse_factory_defense_committees` | complete |
| `soviet_collapse_audit_local_depots` | `GFX_focus_soviet_collapse_audit_local_depots` | complete |
| `soviet_collapse_field_emergency_battalions` | `GFX_focus_soviet_collapse_field_emergency_battalions` | complete |
| `soviet_collapse_claim_republican_legality` | `GFX_focus_soviet_collapse_claim_republican_legality` | complete |
| `soviet_collapse_commit_to_socialist_sovereignty` | `GFX_focus_soviet_collapse_commit_to_socialist_sovereignty` | complete |
| `soviet_collapse_republican_general_staff` | `GFX_focus_soviet_collapse_republican_general_staff` | complete |
| `soviet_collapse_request_external_missions` | `GFX_focus_soviet_collapse_request_external_missions` | complete |
| `soviet_collapse_open_volunteer_channels` | `GFX_focus_soviet_collapse_open_volunteer_channels` | complete |
| `soviet_collapse_convene_league_liaisons` | `GFX_focus_soviet_collapse_convene_league_liaisons` | complete |
| `soviet_collapse_common_front_timetables` | `GFX_focus_soviet_collapse_common_front_timetables` | complete |
| `soviet_collapse_survive_the_first_orders` | `GFX_focus_soviet_collapse_survive_the_first_orders` | complete |
| `soviet_collapse_ukrainian_grain_and_rails` | `GFX_focus_soviet_collapse_ukrainian_grain_and_rails` | complete |
| `soviet_collapse_huliaipole_black_flag` | `GFX_focus_soviet_collapse_huliaipole_black_flag` | complete |
| `soviet_collapse_no_masters_in_kyiv_or_moscow` | `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` | complete |
| `soviet_collapse_belarusian_forest_corridors` | `GFX_focus_soviet_collapse_belarusian_forest_corridors` | complete |
| `soviet_collapse_baltic_wire_rooms` | `GFX_focus_soviet_collapse_baltic_wire_rooms` | complete |
| `soviet_collapse_caucasus_pass_guards` | `GFX_focus_soviet_collapse_caucasus_pass_guards` | complete |
| `soviet_collapse_steppe_supply_congress` | `GFX_focus_soviet_collapse_steppe_supply_congress` | complete |
| `soviet_collapse_black_sea_dniester_line` | `GFX_focus_soviet_collapse_black_sea_dniester_line` | complete |

### Generated Shared Focus Icon Records

These icons were regenerated from scratch with Codex built-in `image_gen` from the Soviet-collapse-specific focus sheet preserved at `docs/assets/005_soviet_union_collapse/source_png/focus_active_soviet_collapse_sheet_01_source.png`. Shared prompt summary: clean HOI4-style focus icons with crisis government, military, League, regional, and Black Banner motifs, transparent unused space requested, no colored matte, no green/chroma background, no generated text, no labels, no watermarks, no white outline, low texture, and no baked shadow. The generated sheet used fake checker transparency, so the processed icons were centered with the generated icon cleanup method documented in `.agents/skills/chaos-redux-event-assets/SKILL.md`: filled subject-support masks, preserved dark interior artwork, matte/checker removal, transparent unused canvas, subtle black outline, and slight black drop shadow.

Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/generic_republic_focus_icons.png`

| Focus | Source PNG | Processed PNG | Final DDS | Target size | GFX file | Source status | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `soviet_collapse_assemble_emergency_government` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_assemble_emergency_government_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_assemble_emergency_government.png` | `gfx/interface/goals/focus_soviet_collapse_assemble_emergency_government.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_guard_the_radio_stations` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_guard_the_radio_stations_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_guard_the_radio_stations.png` | `gfx/interface/goals/focus_soviet_collapse_guard_the_radio_stations.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_secure_ministry_ledgers` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_secure_ministry_ledgers_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_secure_ministry_ledgers.png` | `gfx/interface/goals/focus_soviet_collapse_secure_ministry_ledgers.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_factory_defense_committees` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_factory_defense_committees_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_factory_defense_committees.png` | `gfx/interface/goals/focus_soviet_collapse_factory_defense_committees.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_audit_local_depots` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_audit_local_depots_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_audit_local_depots.png` | `gfx/interface/goals/focus_soviet_collapse_audit_local_depots.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_field_emergency_battalions` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_field_emergency_battalions_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_field_emergency_battalions.png` | `gfx/interface/goals/focus_soviet_collapse_field_emergency_battalions.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_claim_republican_legality` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_claim_republican_legality_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_claim_republican_legality.png` | `gfx/interface/goals/focus_soviet_collapse_claim_republican_legality.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_commit_to_socialist_sovereignty` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_commit_to_socialist_sovereignty_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_commit_to_socialist_sovereignty.png` | `gfx/interface/goals/focus_soviet_collapse_commit_to_socialist_sovereignty.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_republican_general_staff` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_republican_general_staff_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_republican_general_staff.png` | `gfx/interface/goals/focus_soviet_collapse_republican_general_staff.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_request_external_missions` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_request_external_missions_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_request_external_missions.png` | `gfx/interface/goals/focus_soviet_collapse_request_external_missions.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_open_volunteer_channels` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_open_volunteer_channels_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_open_volunteer_channels.png` | `gfx/interface/goals/focus_soviet_collapse_open_volunteer_channels.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_convene_league_liaisons` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_convene_league_liaisons_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_convene_league_liaisons.png` | `gfx/interface/goals/focus_soviet_collapse_convene_league_liaisons.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_common_front_timetables` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_common_front_timetables_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_common_front_timetables.png` | `gfx/interface/goals/focus_soviet_collapse_common_front_timetables.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_survive_the_first_orders` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_survive_the_first_orders_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_survive_the_first_orders.png` | `gfx/interface/goals/focus_soviet_collapse_survive_the_first_orders.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_ukrainian_grain_and_rails` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_ukrainian_grain_and_rails_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_ukrainian_grain_and_rails.png` | `gfx/interface/goals/focus_soviet_collapse_ukrainian_grain_and_rails.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_belarusian_forest_corridors` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_belarusian_forest_corridors_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_belarusian_forest_corridors.png` | `gfx/interface/goals/focus_soviet_collapse_belarusian_forest_corridors.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_baltic_wire_rooms` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_baltic_wire_rooms_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_baltic_wire_rooms.png` | `gfx/interface/goals/focus_soviet_collapse_baltic_wire_rooms.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_caucasus_pass_guards` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_caucasus_pass_guards_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_caucasus_pass_guards.png` | `gfx/interface/goals/focus_soviet_collapse_caucasus_pass_guards.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_steppe_supply_congress` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_steppe_supply_congress_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_steppe_supply_congress.png` | `gfx/interface/goals/focus_soviet_collapse_steppe_supply_congress.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_black_sea_dniester_line` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_black_sea_dniester_line_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_black_sea_dniester_line.png` | `gfx/interface/goals/focus_soviet_collapse_black_sea_dniester_line.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_huliaipole_black_flag` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_huliaipole_black_flag_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_huliaipole_black_flag.png` | `gfx/interface/goals/focus_soviet_collapse_huliaipole_black_flag.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |
| `soviet_collapse_no_masters_in_kyiv_or_moscow` | `docs/assets/005_soviet_union_collapse/source_png/focus_soviet_collapse_no_masters_in_kyiv_or_moscow_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/focus_soviet_collapse_no_masters_in_kyiv_or_moscow.png` | `gfx/interface/goals/focus_soviet_collapse_no_masters_in_kyiv_or_moscow.dds` | 94x86 | `interface/005_soviet_collapse_icons.gfx` | `not_needed` | complete |

## Required Super-Event Asset

| Asset | Sprite | Source mode | Source PNG | Processed PNG | Final DDS | GFX file | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The Union Unmade | `GFX_super_event_union_unmade` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_union_unmade_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_union_unmade.png` | `gfx/super_events/super_event_union_unmade.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| A Map Larger than the Union | `GFX_super_event_map_larger_than_union` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_map_larger_than_union_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_map_larger_than_union.png` | `gfx/super_events/super_event_map_larger_than_union.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Steppe Beyond History | `GFX_super_event_steppe_beyond_history` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_beyond_history_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_beyond_history.png` | `gfx/super_events/super_event_steppe_beyond_history.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Corridors Decide | `GFX_super_event_corridors_decide` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_corridors_decide_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_corridors_decide.png` | `gfx/super_events/super_event_corridors_decide.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Bread State | `GFX_super_event_bread_state` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_bread_state_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_bread_state.png` | `gfx/super_events/super_event_bread_state.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The League of Equal Republics | `GFX_super_event_league_equal_republics` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_league_equal_republics_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_league_equal_republics.png` | `gfx/super_events/super_event_league_equal_republics.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Steppe Federation | `GFX_super_event_steppe_federation` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_federation_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_federation.png` | `gfx/super_events/super_event_steppe_federation.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Baltic League | `GFX_super_event_baltic_restoration_pact` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_baltic_restoration_pact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_baltic_restoration_pact.png` | `gfx/super_events/super_event_baltic_restoration_pact.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Caucasus League | `GFX_super_event_caucasus_defense_compact` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_caucasus_defense_compact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_caucasus_defense_compact.png` | `gfx/super_events/super_event_caucasus_defense_compact.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |
| The Eastern Buffer Coalition | `GFX_super_event_eastern_buffer_coalition` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_eastern_buffer_coalition_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_eastern_buffer_coalition.png` | `gfx/super_events/super_event_eastern_buffer_coalition.dds` | `interface/chaosx_super_events.gfx` | wired, `sourced` |

## Optional Branch Super-Event Assets

These rare branch super-events are tied to custom extreme paths. Their image sheet was generated with Codex built-in `image_gen` because the branches are fictional, high-chaos, and symbolic rather than documentary scenes. The generated sheet is preserved at `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png`, processed into 457x328 previews, converted to DDS, and wired in `interface/chaosx_super_events.gfx`.

| Asset | Slot | Sprite | Source PNG | Processed PNG | Final DDS | Trigger source | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The Black Banner Returns | `15` | `GFX_super_event_black_banner_returns` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_black_banner_returns.png` | `gfx/super_events/super_event_black_banner_returns.dds` | `FTH_extreme_path`, `BBH_extreme_path` | wired, generated |
| The Northern Signals Break | `16` | `GFX_super_event_northern_signals_break` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_northern_signals_break.png` | `gfx/super_events/super_event_northern_signals_break.dds` | `ICD_extreme_path` | wired, generated |
| The Workshops Choose Their Councils | `17` | `GFX_super_event_workshops_choose_councils` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_workshops_choose_councils.png` | `gfx/super_events/super_event_workshops_choose_councils.dds` | `ILU_extreme_path` | wired, generated |
| Every Port a Council | `18` | `GFX_super_event_every_port_a_council` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_every_port_a_council.png` | `gfx/super_events/super_event_every_port_a_council.dds` | `KRS_extreme_path` | wired, generated |
| The Steppe Beyond History | `20` | `GFX_super_event_steppe_beyond_history` | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_beyond_history_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_beyond_history.png` | `gfx/super_events/super_event_steppe_beyond_history.dds` | `KAZ_steppe_beyond_history` | wired, `sourced` |
| The Corridors Decide | `21` | `GFX_super_event_corridors_decide` | `docs/assets/005_soviet_union_collapse/source_png/super_event_corridors_decide_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_corridors_decide.png` | `gfx/super_events/super_event_corridors_decide.dds` | `BLR_corridors_decide` | wired, `sourced` |
| The Bread State | `22` | `GFX_super_event_bread_state` | `docs/assets/005_soviet_union_collapse/source_png/super_event_bread_state_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_bread_state.png` | `gfx/super_events/super_event_bread_state.dds` | `UKR_bread_state` | wired, `sourced` |
| The League of Equal Republics | `23` | `GFX_super_event_league_equal_republics` | `docs/assets/005_soviet_union_collapse/source_png/super_event_league_equal_republics_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_league_equal_republics.png` | `gfx/super_events/super_event_league_equal_republics.dds` | `UKR_league_equal_republics` | wired, `sourced` |
| The Steppe Federation | `24` | `GFX_super_event_steppe_federation` | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_federation_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_federation.png` | `gfx/super_events/super_event_steppe_federation.dds` | `Steppe Federation formation`, `BSC_extreme_path`, `TNC_extreme_path`, `ALA_extreme_path` | wired, `sourced` |
| The Baltic League | `25` | `GFX_super_event_baltic_restoration_pact` | `docs/assets/005_soviet_union_collapse/source_png/super_event_baltic_restoration_pact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_baltic_restoration_pact.png` | `gfx/super_events/super_event_baltic_restoration_pact.dds` | `Baltic League formation` | wired, `sourced` |
| The Caucasus League | `26` | `GFX_super_event_caucasus_defense_compact` | `docs/assets/005_soviet_union_collapse/source_png/super_event_caucasus_defense_compact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_caucasus_defense_compact.png` | `gfx/super_events/super_event_caucasus_defense_compact.dds` | `Caucasus League formation` | wired, `sourced` |
| The Eastern Buffer Coalition | `27` | `GFX_super_event_eastern_buffer_coalition` | `docs/assets/005_soviet_union_collapse/source_png/super_event_eastern_buffer_coalition_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_eastern_buffer_coalition.png` | `gfx/super_events/super_event_eastern_buffer_coalition.dds` | `Eastern Buffer Coalition formation` | wired, `sourced` |

Research note: `docs/super_events/005_soviet_union_collapse_super_event_research.md`

## Active Image Source Notes

| Asset | Source link | Author or archive | License notes |
| --- | --- | --- | --- |
| `news_soviet_union_collapse` | `https://commons.wikimedia.org/wiki/File:RIAN_archive_848095_Signing_the_Agreement_to_eliminate_the_USSR_and_establish_the_Commonwealth_of_Independent_States.jpg` | RIA Novosti archive image #848095, U. Ivanov | CC BY-SA 3.0 |
| `news_free_republics_league` | `https://commons.wikimedia.org/wiki/File:1989_08_23_Baltijoskelias17e.jpg` | Rimantas Lazdynas | CC BY-SA 3.0 or GFDL |
| `news_union_unmade` | `https://commons.wikimedia.org/wiki/File:Boris_Yeltsin_waves.jpg` | Kremlin.ru / Press Service of the President of Russia | CC BY 4.0 |
| `report_union_crisis` | `https://commons.wikimedia.org/wiki/File:Democratic_Russia._Special_edition._20.08.1991._img_06.jpg` | Democratic Russia emergency issue, scan by Dmitry Makeev | public-domain Russian official-document exemption on Commons |
| `report_breakaway_mobilization` | `https://commons.wikimedia.org/wiki/File:Barricades_near_the_White_House_(8000383073).jpg` | Tove Knutsen / Flickr transfer reviewed by FlickreviewR 2 | CC BY-SA 2.0 |
| `report_depot_war` | `https://commons.wikimedia.org/wiki/File:Red_army_tanks_(8000380028).jpg` | Tove Knutsen / Flickr transfer reviewed by FlickreviewR 2 | CC BY-SA 2.0 |
| `report_foreign_liaison` | `https://commons.wikimedia.org/wiki/File:RIAN_archive_52076_Leonid_Kravchuk,_Stanislav_Shushkevich_and_Boris_Yeltsin.jpg` | RIA Novosti archive image #52076, Yuriy Ivanov | CC BY-SA 3.0 |
| `report_old_underground` | `https://commons.wikimedia.org/wiki/File:Nestor_Makhno_and_his_Lieutenants,_Berdyansk,_1919.jpg` | Unknown photographer, hosted on Wikimedia Commons | public domain in the United States and Ukraine per Commons tags |
| `report_railway_sovereignty` | `https://commons.wikimedia.org/wiki/File:Red_armored_train_and_raiding_party,_ca._1920.jpg` | Unknown photographer, hosted on Wikimedia Commons | public domain in Russia and the United States per Commons tags |
| `super_event_map_larger_than_union` | `https://commons.wikimedia.org/wiki/File:Kiev_Cabinet_of_Ministers.jpg` | Daniel Haussmann | CC BY-SA 3.0, with compatible additional license options listed on Commons |
| `super_event_steppe_beyond_history` | `https://commons.wikimedia.org/wiki/File:Turk-Sib_railway.jpg` | Petar Milosevic | CC BY-SA 3.0 |
| `super_event_corridors_decide` | `https://commons.wikimedia.org/wiki/File:Refugees_on_train_roof.jpg` | unknown photographer / The Ukrainian Museum Archives | public domain in Ukraine and the United States per Commons `PD-Ukraine` tag |
| `super_event_bread_state` | `https://commons.wikimedia.org/wiki/File:%D0%A1%D0%B5%D0%BB%D1%8F%D0%BD%D0%B8_%D0%B7%D0%B4%D0%B0%D1%8E%D1%82%D1%8C_%D1%85%D0%BB%D1%96%D0%B1.jpg` | unknown photographer / Central State Audiovisual and Electronic Archive of Ukraine | public domain in Ukraine and the United States per Commons `PD-Ukraine` tag |
| `super_event_league_equal_republics` | `https://commons.wikimedia.org/wiki/File:1989_08_23_Baltijoskelias17e.jpg` | Rimantas Lazdynas | CC BY-SA 3.0 or GFDL; reuses the Free Republics' League source original |
| `super_event_steppe_federation` | `https://commons.wikimedia.org/wiki/File:Turk-Sib_railway.jpg` | Petar Milosevic | CC BY-SA 3.0; reuses the Steppe Beyond History source original |
| `super_event_baltic_restoration_pact` | `https://commons.wikimedia.org/wiki/File:Lithuanian_Army_in_the_surroundings_of_Vilnius_Region,_1939.jpg` | Unknown photographer / Marija and Jurgis Slapeliai House-Museum via Europeana | CC0 / public-domain dedication on Commons |
| `super_event_caucasus_defense_compact` | `https://commons.wikimedia.org/wiki/File:CAUCASUS_MOUNTAINS.jpg` | NASA / Visible Earth | public domain in the United States as a NASA work; Commons lists PD-USGov/NASA |
| `super_event_eastern_buffer_coalition` | `https://commons.wikimedia.org/wiki/File:Soviet_invasion_on_Poland_1939.jpg` | Unknown photographer / unknown source, hosted on Wikimedia Commons | public domain in Russia and the United States per Commons `PD-Russia-1996` tags |

## Future Branch Asset Backlog

These assets belong to evolution tracks or custom tags that are not active yet. Do not wire them until the matching gameplay exists.

## Ukraine Runtime Focus Tree Branch Icons

The expanded `soviet_collapse_ukraine_focus_tree` is active gameplay and currently uses 153 focuses. Its branch-level sprites are wired in `interface/005_soviet_collapse_ukraine_icons.gfx` and point at dedicated 94x86 DDS files derived from existing generated Event 005 focus art. The expansion asset ledger records the matching processed PNG files and source art. This branch-icon package documents deliberate sprite reuse for the current expanded tree; it does not prove the literal 208-focus target from older prompt material.

| Branch sprite | Final DDS | Usage | Status |
| --- | --- | --- | --- |
| `GFX_ukr_soviet_collapse_survival` | `gfx/interface/goals/ukr_soviet_collapse_survival.dds` | survival and ministry crisis focuses | complete |
| `GFX_ukr_soviet_collapse_democratic` | `gfx/interface/goals/ukr_soviet_collapse_democratic.dds` | democratic restoration focuses | complete |
| `GFX_ukr_soviet_collapse_socialist` | `gfx/interface/goals/ukr_soviet_collapse_socialist.dds` | socialist sovereignty focuses | complete |
| `GFX_ukr_soviet_collapse_directory` | `gfx/interface/goals/ukr_soviet_collapse_directory.dds` | military directory focuses | complete |
| `GFX_ukr_soviet_collapse_foreign` | `gfx/interface/goals/ukr_soviet_collapse_foreign.dds` | foreign liaison and patronage-risk focuses | complete |
| `GFX_ukr_soviet_collapse_bread` | `gfx/interface/goals/ukr_soviet_collapse_bread.dds` | grain, ration, and bread-state focuses | complete |
| `GFX_ukr_soviet_collapse_league` | `gfx/interface/goals/ukr_soviet_collapse_league.dds` | Free Republics' League leadership focuses | complete |
| `GFX_ukr_soviet_collapse_expansion` | `gfx/interface/goals/ukr_soviet_collapse_expansion.dds` | Black Sea and beyond-Union expansion focuses | complete |
| `GFX_ukr_soviet_collapse_armed_forces` | `gfx/interface/goals/ukr_soviet_collapse_armed_forces.dds` | army, air, navy, and irregular-force focuses | complete |
| `GFX_ukr_soviet_collapse_industry` | `gfx/interface/goals/ukr_soviet_collapse_industry.dds` | industry and procurement focuses | complete |
| `GFX_ukr_soviet_collapse_black_banner` | `gfx/interface/goals/ukr_soviet_collapse_black_banner.dds` | Black Banner interaction focuses | complete |
| `GFX_ukr_soviet_collapse_identity` | `gfx/interface/goals/ukr_soviet_collapse_identity.dds` | late identity outcome focuses | complete |

Future bespoke artwork can replace these dedicated generated-reuse DDS files without changing focus IDs or gameplay script.

## Belarus Runtime Focus Tree Branch Icons

The replacement `soviet_collapse_belarus_focus_tree` is active gameplay for Event 005-created Belarus and now uses 83 focuses, matching the clean-spec target. Its branch-level sprites are wired in `interface/005_soviet_collapse_blr_icons.gfx` and point at dedicated 94x86 DDS files derived from existing generated Event 005 focus art.

| Branch sprite | Final DDS | Usage | Status |
| --- | --- | --- | --- |
| `GFX_blr_soviet_collapse_rail` | `gfx/interface/goals/blr_soviet_collapse_rail.dds` | rail authority and junction-state focuses | complete |
| `GFX_blr_soviet_collapse_forest` | `gfx/interface/goals/blr_soviet_collapse_forest.dds` | forest defense focuses | complete |
| `GFX_blr_soviet_collapse_corridor` | `gfx/interface/goals/blr_soviet_collapse_corridor.dds` | corridor and western-gate focuses | complete |
| `GFX_blr_soviet_collapse_legal` | `gfx/interface/goals/blr_soviet_collapse_legal.dds` | legal restoration focuses | complete |
| `GFX_blr_soviet_collapse_socialist` | `gfx/interface/goals/blr_soviet_collapse_socialist.dds` | socialist Belarus focuses | complete |
| `GFX_blr_soviet_collapse_foreign_transit` | `gfx/interface/goals/blr_soviet_collapse_foreign_transit.dds` | foreign transit and observer focuses | complete |
| `GFX_blr_soviet_collapse_counterintel` | `gfx/interface/goals/blr_soviet_collapse_counterintel.dds` | counterintelligence and archive focuses | complete |
| `GFX_blr_soviet_collapse_civic` | `gfx/interface/goals/blr_soviet_collapse_civic.dds` | civic-state outcome focuses | complete |

## Kazakhstan Runtime Focus Tree Branch Icons

The 56-focus `soviet_collapse_kazakhstan_focus_tree` is active gameplay for Event 005-created Kazakhstan and satisfies the clean-spec Kazakhstan focus-count target. Its branch-level sprites are wired in `interface/005_soviet_collapse_kaz_icons.gfx` and point at dedicated 94x86 DDS files derived from existing generated Event 005 focus art.

| Branch sprite | Final DDS | Usage | Status |
| --- | --- | --- | --- |
| `GFX_kaz_soviet_collapse_alash` | `gfx/interface/goals/kaz_soviet_collapse_alash.dds` | Alash restoration focuses | complete |
| `GFX_kaz_soviet_collapse_steppe_socialist` | `gfx/interface/goals/kaz_soviet_collapse_steppe_socialist.dds` | steppe socialist focuses | complete |
| `GFX_kaz_soviet_collapse_federation` | `gfx/interface/goals/kaz_soviet_collapse_federation.dds` | Steppe Federation focuses | complete |
| `GFX_kaz_soviet_collapse_resources` | `gfx/interface/goals/kaz_soviet_collapse_resources.dds` | resource-state focuses | complete |
| `GFX_kaz_soviet_collapse_foreign` | `gfx/interface/goals/kaz_soviet_collapse_foreign.dds` | foreign influence focuses | complete |
| `GFX_kaz_soviet_collapse_myth` | `gfx/interface/goals/kaz_soviet_collapse_myth.dds` | high-chaos steppe mythology focuses | complete |
| `GFX_kaz_soviet_collapse_military` | `gfx/interface/goals/kaz_soviet_collapse_military.dds` | steppe military focuses | complete |
| `GFX_kaz_soviet_collapse_settlement` | `gfx/interface/goals/kaz_soviet_collapse_settlement.dds` | industry and settlement focuses | complete |

News and report backlog:

- `GFX_news_black_banner_returns`
- `GFX_news_kronstadt_free_soviet`
- `GFX_news_basmachi_roads`
- `GFX_news_far_eastern_buffer`
- `GFX_news_old_fronts_return`
- `GFX_news_northern_signals_break`
- `GFX_news_tunguska_star_committee`
- `GFX_news_workshops_choose_councils`
- `GFX_news_every_port_a_council`
- `GFX_report_high_chaos_cult`

The Old Underground Wakes, Red Resistance without Moscow, The War of Committees, and The Flags Return Incorrectly are active event-log mutation tracks. The Ukrainian Black Banner Defense Committees contingency branch is active without branch-specific news/report imagery; those images remain unwired until the Free Territory or Black Banner branch becomes a major actor.

## Custom Country Flags

The custom splinter flags were generated from scratch with Codex built-in `image_gen` and preserved at `docs/assets/005_soviet_union_collapse/source_png/custom_splinter_flag_sheet_source.png`. They were re-cropped from the latest clean sheet, trimmed away from the magenta separators, resized into normal, medium, and small HOI4 flag sizes, checked for remaining chroma-key pixels, and converted to TGA under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. Final dimensions are normal 82x52, medium 41x26, and small 10x7. All Event 005 custom flag TGAs, including ideology variants, use 32bpp bottom-left row order so the HOI4 flag atlas does not display them upside down.


Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_flags.png`

| Tag | Normal PNG | Normal TGA | Medium TGA | Small TGA | Status |
| --- | --- | --- | --- | --- | --- |
| `FTH` | `docs/assets/005_soviet_union_collapse/processed_png/flags/FTH_normal.png` | `gfx/flags/FTH.tga` | `gfx/flags/medium/FTH.tga` | `gfx/flags/small/FTH.tga` | wired |
| `KRS` | `docs/assets/005_soviet_union_collapse/processed_png/flags/KRS_normal.png` | `gfx/flags/KRS.tga` | `gfx/flags/medium/KRS.tga` | `gfx/flags/small/KRS.tga` | wired |
| `BSC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/BSC_normal.png` | `gfx/flags/BSC.tga` | `gfx/flags/medium/BSC.tga` | `gfx/flags/small/BSC.tga` | wired |
| `TNC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/TNC_normal.png` | `gfx/flags/TNC.tga` | `gfx/flags/medium/TNC.tga` | `gfx/flags/small/TNC.tga` | wired, generated reuse |
| `ALA` | `docs/assets/005_soviet_union_collapse/processed_png/flags/ALA_normal.png` | `gfx/flags/ALA.tga` | `gfx/flags/medium/ALA.tga` | `gfx/flags/small/ALA.tga` | wired, generated reuse |
| `MRC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/MRC_normal.png` | `gfx/flags/MRC.tga` | `gfx/flags/medium/MRC.tga` | `gfx/flags/small/MRC.tga` | complete |
| `UWD` | `docs/assets/005_soviet_union_collapse/processed_png/flags/UWD_normal.png` | `gfx/flags/UWD.tga` | `gfx/flags/medium/UWD.tga` | `gfx/flags/small/UWD.tga` | complete |
| `IUL` | `docs/assets/005_soviet_union_collapse/processed_png/flags/IUL_normal.png` | `gfx/flags/IUL.tga` | `gfx/flags/medium/IUL.tga` | `gfx/flags/small/IUL.tga` | complete |
| `BAC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/BAC_normal.png` | `gfx/flags/BAC.tga` | `gfx/flags/medium/BAC.tga` | `gfx/flags/small/BAC.tga` | complete |
| `GAC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/GAC_normal.png` | `gfx/flags/GAC.tga` | `gfx/flags/medium/GAC.tga` | `gfx/flags/small/GAC.tga` | wired, generated reuse |
| `DHC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/DHC_normal.png` | `gfx/flags/DHC.tga` | `gfx/flags/medium/DHC.tga` | `gfx/flags/small/DHC.tga` | wired, generated reuse |
| `KHC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/KHC_normal.png` | `gfx/flags/KHC.tga` | `gfx/flags/medium/KHC.tga` | `gfx/flags/small/KHC.tga` | wired, generated reuse |
| `FEV` | `docs/assets/005_soviet_union_collapse/processed_png/flags/FEV_normal.png` | `gfx/flags/FEV.tga` | `gfx/flags/medium/FEV.tga` | `gfx/flags/small/FEV.tga` | complete |
| `SZA` | `docs/assets/005_soviet_union_collapse/processed_png/flags/SZA_normal.png` | `gfx/flags/SZA.tga` | `gfx/flags/medium/SZA.tga` | `gfx/flags/small/SZA.tga` | complete |
| `UDC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/UDC_normal.png` | `gfx/flags/UDC.tga` | `gfx/flags/medium/UDC.tga` | `gfx/flags/small/UDC.tga` | wired |
| `SDZ` | `docs/assets/005_soviet_union_collapse/processed_png/flags/SDZ_normal.png` | `gfx/flags/SDZ.tga` | `gfx/flags/medium/SDZ.tga` | `gfx/flags/small/SDZ.tga` | wired |
| `RMC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/RMC_normal.png` | `gfx/flags/RMC.tga` | `gfx/flags/medium/RMC.tga` | `gfx/flags/small/RMC.tga` | wired |
| `RCD` | `docs/assets/005_soviet_union_collapse/processed_png/flags/RCD_normal.png` | `gfx/flags/RCD.tga` | `gfx/flags/medium/RCD.tga` | `gfx/flags/small/RCD.tga` | wired |
| `ILU` | `docs/assets/005_soviet_union_collapse/processed_png/flags/ILU_normal.png` | `gfx/flags/ILU.tga` | `gfx/flags/medium/ILU.tga` | `gfx/flags/small/ILU.tga` | wired |
| `PRA` | `docs/assets/005_soviet_union_collapse/processed_png/flags/PRA_normal.png` | `gfx/flags/PRA.tga` | `gfx/flags/medium/PRA.tga` | `gfx/flags/small/PRA.tga` | wired |
| `TSC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/TSC_normal.png` | `gfx/flags/TSC.tga` | `gfx/flags/medium/TSC.tga` | `gfx/flags/small/TSC.tga` | wired |
| `BLT` | `docs/assets/005_soviet_union_collapse/processed_png/flags/BLT_normal.png` | `gfx/flags/BLT.tga` | `gfx/flags/medium/BLT.tga` | `gfx/flags/small/BLT.tga` | wired |
| `NRF` | `docs/assets/005_soviet_union_collapse/processed_png/flags/NRF_normal.png` | `gfx/flags/NRF.tga` | `gfx/flags/medium/NRF.tga` | `gfx/flags/small/NRF.tga` | wired |
| `ARD` | `docs/assets/005_soviet_union_collapse/processed_png/flags/ARD_normal.png` | `gfx/flags/ARD.tga` | `gfx/flags/medium/ARD.tga` | `gfx/flags/small/ARD.tga` | wired, generated reuse |
| `TRS` | `docs/assets/005_soviet_union_collapse/processed_png/flags/TRS_normal.png` | `gfx/flags/TRS.tga` | `gfx/flags/medium/TRS.tga` | `gfx/flags/small/TRS.tga` | wired, generated reuse |
| `ICD` | `docs/assets/005_soviet_union_collapse/processed_png/flags/ICD_normal.png` | `gfx/flags/ICD.tga` | `gfx/flags/medium/ICD.tga` | `gfx/flags/small/ICD.tga` | wired, generated reuse |
| `NLC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/NLC_normal.png` | `gfx/flags/NLC.tga` | `gfx/flags/medium/NLC.tga` | `gfx/flags/small/NLC.tga` | wired, generated reuse |
| `SEP` | `docs/assets/005_soviet_union_collapse/processed_png/flags/SEP_normal.png` | `gfx/flags/SEP.tga` | `gfx/flags/medium/SEP.tga` | `gfx/flags/small/SEP.tga` | wired, generated reuse |

## Custom Country Emblems And Portraits

The custom country UI emblems were regenerated from scratch with Codex built-in `image_gen` and preserved at `docs/assets/005_soviet_union_collapse/source_png/custom_splinter_emblem_sheet_source.png`. The prompt requested transparent unused space with no colored matte and no green/chroma background. The generated sheet used fake checker transparency, so the cleanup pass removes the fake matte before final alpha is built. The sheet is processed into one generated emblem per tag at focus, idea, and decision sizes. Processing follows the generated icon cleanup workflow: centered subject-support masks, transparent unused canvas, matte/checker removal, no white or colored halo, subtle black outline, and slight black drop shadow. The many focus, idea, and decision sprite names in `interface/005_soviet_collapse_custom_icons.gfx` intentionally resolve to these tag emblems so each custom country has real generated art without hundreds of low-value filler variants.

Emblem contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_emblems.png`

All-size emblem contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_emblems_all_sizes.png`

The fictional leader/council portraits were generated from scratch with Codex built-in `image_gen` and preserved at `docs/assets/005_soviet_union_collapse/source_png/custom_splinter_leader_portrait_sheet_source.png`. They are processed to the vanilla 156x210 leader portrait size and placed under `gfx/leaders/005_soviet_collapse/`.

Portrait contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_leaders.png`

| Tag | Focus emblem DDS | Idea emblem DDS | Decision emblem DDS | Leader portrait DDS | Status |
| --- | --- | --- | --- | --- | --- |
| `FTH` | `gfx/interface/goals/005_fth_custom_splinter_focus.dds` | `gfx/interface/ideas/005_fth_custom_splinter_idea.dds` | `gfx/interface/decisions/005_fth_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/FTH_leader.dds` | wired |
| `KRS` | `gfx/interface/goals/005_krs_custom_splinter_focus.dds` | `gfx/interface/ideas/005_krs_custom_splinter_idea.dds` | `gfx/interface/decisions/005_krs_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/KRS_leader.dds` | wired |
| `BSC` | `gfx/interface/goals/005_bsc_custom_splinter_focus.dds` | `gfx/interface/ideas/005_bsc_custom_splinter_idea.dds` | `gfx/interface/decisions/005_bsc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/BSC_leader.dds` | wired |
| `TNC` | `gfx/interface/goals/005_tnc_custom_splinter_focus.dds` | `gfx/interface/ideas/005_tnc_custom_splinter_idea.dds` | `gfx/interface/decisions/005_tnc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/TNC_leader.dds` | wired, generated reuse |
| `ALA` | `gfx/interface/goals/005_ala_custom_splinter_focus.dds` | `gfx/interface/ideas/005_ala_custom_splinter_idea.dds` | `gfx/interface/decisions/005_ala_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/ALA_leader.dds` | wired, generated reuse |
| `MRC` | `gfx/interface/goals/soviet_collapse/005_mrc_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_mrc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_mrc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/MRC_leader.dds` | complete |
| `UWD` | `gfx/interface/goals/soviet_collapse/005_uwd_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_uwd_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_uwd_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/UWD_leader.dds` | complete |
| `IUL` | `gfx/interface/goals/soviet_collapse/005_iul_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_iul_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_iul_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/IUL_leader.dds` | complete |
| `BAC` | `gfx/interface/goals/soviet_collapse/005_bac_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_bac_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_bac_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/BAC_leader.dds` | complete |
| `ARD` | `gfx/interface/goals/005_ard_custom_splinter_focus.dds` | `gfx/interface/ideas/005_ard_custom_splinter_idea.dds` | `gfx/interface/decisions/005_ard_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/ARD_leader.dds` | wired, generated reuse |
| `GAC` | `gfx/interface/goals/soviet_collapse/005_gac_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_gac_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_gac_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/GAC_leader.dds` | wired |
| `DHC` | `gfx/interface/goals/soviet_collapse/005_dhc_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_dhc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_dhc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/DHC_leader.dds` | wired |
| `KHC` | `gfx/interface/goals/soviet_collapse/005_khc_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_khc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_khc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/KHC_leader.dds` | wired |
| `FEV` | `gfx/interface/goals/soviet_collapse/005_fev_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_fev_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_fev_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/FEV_leader.dds` | complete |
| `SZA` | `gfx/interface/goals/soviet_collapse/005_sza_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_sza_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_sza_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/SZA_leader.dds` | complete |
| `UDC` | `gfx/interface/goals/soviet_collapse/005_udc_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_udc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_udc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/UDC_leader.dds` | wired |
| `SDZ` | `gfx/interface/goals/soviet_collapse/005_sdz_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_sdz_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_sdz_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/SDZ_leader.dds` | wired |
| `RMC` | `gfx/interface/goals/soviet_collapse/005_rmc_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_rmc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_rmc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/RMC_leader.dds` | wired |
| `RCD` | `gfx/interface/goals/soviet_collapse/005_rcd_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_rcd_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_rcd_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/RCD_leader.dds` | wired |
| `ILU` | `gfx/interface/goals/soviet_collapse/005_ilu_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_ilu_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_ilu_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/ILU_leader.dds` | wired |
| `PRA` | `gfx/interface/goals/soviet_collapse/005_pra_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_pra_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_pra_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/PRA_leader.dds` | wired |
| `TSC` | `gfx/interface/goals/soviet_collapse/005_tsc_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_tsc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_tsc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/TSC_leader.dds` | wired |
| `BLT` | `gfx/interface/goals/soviet_collapse/005_blt_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_blt_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_blt_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/BLT_leader.dds` | wired |
| `NRF` | `gfx/interface/goals/soviet_collapse/005_nrf_custom_splinter_focus.dds` | `gfx/interface/ideas/soviet_collapse/005_nrf_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_nrf_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/NRF_leader.dds` | wired |
| `TRS` | `gfx/interface/goals/005_trs_custom_splinter_focus.dds` | `gfx/interface/ideas/005_trs_custom_splinter_idea.dds` | `gfx/interface/decisions/005_trs_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/TRS_leader.dds` | wired, generated reuse |
| `ICD` | `gfx/interface/goals/005_icd_custom_splinter_focus.dds` | `gfx/interface/ideas/005_icd_custom_splinter_idea.dds` | `gfx/interface/decisions/005_icd_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/ICD_leader.dds` | wired, generated reuse |
| `NLC` | `gfx/interface/goals/005_nlc_custom_splinter_focus.dds` | `gfx/interface/ideas/005_nlc_custom_splinter_idea.dds` | `gfx/interface/decisions/005_nlc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/NLC_leader.dds` | wired, generated reuse |
| `SEP` | `gfx/interface/goals/005_sep_custom_splinter_focus.dds` | `gfx/interface/ideas/005_sep_custom_splinter_idea.dds` | `gfx/interface/decisions/005_sep_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/SEP_leader.dds` | wired, generated reuse |

Custom tag flags and tag-specific focus icons are required only for tags that are actually added. Each implemented tag needs normal, medium, and small flags plus focus icons for any focus tree content.

## Blocked Or Incomplete Final Assets

- Final generated idea icons: `complete` for active ideas. Source sheets, cropped source PNGs, processed previews, and DDS files are recorded above.
- Final generated decision icons: `complete` for active decisions. Source sheet, cropped source PNGs, processed previews, and DDS files are recorded above.
- Foreign patron category and decision icons plus volunteer decision and national spirit icons: `complete` for the implemented influence and volunteer mechanics. Processed PNG previews live in `docs/assets/005_soviet_union_collapse/processed_png/foreign_patron_decisions/`, `docs/assets/005_soviet_union_collapse/processed_png/volunteer_decisions/`, and `docs/assets/005_soviet_union_collapse/processed_png/volunteer_ideas/`; final DDS files live in `gfx/interface/decisions/` and `gfx/interface/ideas/`; sprite definitions are wired in `interface/005_soviet_collapse_icons.gfx`.
- Regional faction category and decision icons: `complete` for the implemented category, founding decisions, shared-goal decisions, mediation decision, and withdrawal decision. Processed PNG previews live in `docs/assets/005_soviet_union_collapse/processed_png/regional_faction_decisions/`, final DDS files live in `gfx/interface/decisions/`, and the sprite definitions are wired in `interface/005_soviet_collapse_icons.gfx`.
- Ukraine, Belarus, and Kazakhstan runtime branch focus icons: `complete` for the implemented branch sprite sets. Processed PNG previews live in `docs/assets/005_soviet_union_collapse/processed_png/republic_branch_focus_icons/`, final DDS files live in `gfx/interface/goals/`, and the sprite definitions are wired in `interface/005_soviet_collapse_ukraine_icons.gfx`, `interface/005_soviet_collapse_blr_icons.gfx`, and `interface/005_soviet_collapse_kaz_icons.gfx`.
- Optional branch super-event images: `complete` for Black Banner, Dead Citizens, One Factory, Port Council, Ukraine's A Map Larger than the Union branch reveal, Kazakhstan's Steppe Beyond History branch reveal, Belarus's Corridors Decide branch reveal, Ukraine's Bread State branch reveal, Ukraine's League of Equal Republics branch reveal, the Steppe Federation formation reveal, the Baltic League formation reveal, the Caucasus League formation reveal, and the Eastern Buffer Coalition formation reveal.
- Sourced report and super-event tracking sheets: labeled grids `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_report_images_tracking_sheet_labeled.png` and `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_super_event_images_tracking_sheet_labeled.png`, plus raw grids `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_report_images_tracking_sheet.png` and `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_super_event_images_tracking_sheet.png`, exist for source tracking of the `sourced` sourced-image rows.
- Optional branch news/report/super-event images: `not wired`. They remain in the backlog until matching Black Banner, necromantic, industrial, railway, Kronstadt, or naval branches exist as gameplay.

## Review Notes

- Source link: `https://commons.wikimedia.org/wiki/File:August_1991_coup_-_awaiting_the_counterattack_outside_the_White_House_Moscow_-_panoramio.jpg`
- Author/archive: David Broad, originally from Panoramio, hosted on Wikimedia Commons
- License: Creative Commons Attribution 3.0 Unported
- Ukraine map super-event source link: `https://commons.wikimedia.org/wiki/File:Kiev_Cabinet_of_Ministers.jpg`
- Ukraine map super-event author/archive: Daniel Haussmann, hosted on Wikimedia Commons
- Ukraine map super-event license: Creative Commons Attribution-Share Alike 3.0 Unported, with compatible additional license options listed on Commons
- Report and super-event images require explicit source tracking before being treated as final sourced art.
- Final DDS format should be 32-bit unsigned BGRB 8.8.8.8.
- The implementation must update this manifest in the same change that creates, processes, converts, or wires any package asset.

ICD generated-reuse asset package: `gfx/flags/ICD.tga`, `gfx/flags/medium/ICD.tga`, `gfx/flags/small/ICD.tga`, `gfx/interface/goals/005_icd_custom_splinter_focus.dds`, `gfx/interface/ideas/005_icd_custom_splinter_idea.dds`, `gfx/interface/decisions/005_icd_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/ICD_leader.dds` are wired. Source and processed previews use the corresponding `005_icd_*`, `ICD_leader_*`, and `icd_custom_splinter_*` files under `docs/assets/005_soviet_union_collapse/`.

TRS generated-reuse asset package: `gfx/flags/TRS.tga`, `gfx/flags/medium/TRS.tga`, `gfx/flags/small/TRS.tga`, `gfx/interface/goals/005_trs_custom_splinter_focus.dds`, `gfx/interface/ideas/005_trs_custom_splinter_idea.dds`, `gfx/interface/decisions/005_trs_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/TRS_leader.dds` are wired. Source and processed previews use the corresponding `005_trs_*`, `TRS_leader_*`, and `trs_custom_splinter_*` files under `docs/assets/005_soviet_union_collapse/`.

NLC generated-reuse asset package: `gfx/flags/NLC.tga`, `gfx/flags/medium/NLC.tga`, `gfx/flags/small/NLC.tga`, `gfx/interface/goals/005_nlc_custom_splinter_focus.dds`, `gfx/interface/ideas/005_nlc_custom_splinter_idea.dds`, `gfx/interface/decisions/005_nlc_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/NLC_leader.dds` are wired. Source and processed previews use the corresponding `005_nlc_*`, `NLC_leader_*`, and `nlc_custom_splinter_*` files under `docs/assets/005_soviet_union_collapse/`.



`SEP` currently reuses the generated Red Martyrs custom-splinter package as replacement-art candidate material. Stable paths are `gfx/flags/SEP.tga`, `gfx/flags/medium/SEP.tga`, `gfx/flags/small/SEP.tga`, `gfx/interface/goals/005_sep_custom_splinter_focus.dds`, `gfx/interface/ideas/005_sep_custom_splinter_idea.dds`, `gfx/interface/decisions/005_sep_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/SEP_leader.dds`. Source and processed PNG records live under `docs/assets/005_soviet_union_collapse/source_png/` and `docs/assets/005_soviet_union_collapse/processed_png/`.




### Idel-Ural League Generated-Reuse Asset Records

`IUL` currently reuses the generated Ural Workers custom-splinter package as replacement-art candidate material. Stable paths are `gfx/flags/IUL.tga`, `gfx/flags/medium/IUL.tga`, `gfx/flags/small/IUL.tga`, `gfx/interface/goals/soviet_collapse/005_iul_custom_splinter_focus.dds`, `gfx/interface/ideas/soviet_collapse/005_iul_custom_splinter_idea.dds`, `gfx/interface/decisions/soviet_collapse/005_iul_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/IUL_leader.dds`. Source and processed PNG records live under `docs/assets/005_soviet_union_collapse/source_png/` and `docs/assets/005_soviet_union_collapse/processed_png/`.

### Factory States and Volga Restoration Asset Records

`CFR`, `MFR`, and `OGB` are wired as continuation-pass playable tags with generated leader portraits, purpose-built generated flag art, processed previews, final game files, and stable interface sprite names. The full flag source sheet is `docs/assets/005_soviet_union_collapse/source_png/CFR_MFR_OGB_flag_sheet_source.png`. The final flag files are distinct per tag, exist in normal, medium, and small sizes, and are exported as 32bpp bottom-left row-order TGA files for HOI4 flag atlas loading.

| Tag | Flag source and preview | Final flag paths | Leader source and preview | Leader portrait | Interface wiring | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `CFR` | `docs/assets/005_soviet_union_collapse/source_png/CFR_flag_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/CFR_flag.png` | `gfx/flags/CFR.tga`, `gfx/flags/medium/CFR.tga`, `gfx/flags/small/CFR.tga` | `docs/assets/005_soviet_union_collapse/source_png/CFR_leader_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/CFR_leader.png` | `gfx/leaders/005_soviet_collapse/CFR_leader.dds` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | wired with dedicated leader and idea icons |
| `MFR` | `docs/assets/005_soviet_union_collapse/source_png/MFR_flag_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/MFR_flag.png` | `gfx/flags/MFR.tga`, `gfx/flags/medium/MFR.tga`, `gfx/flags/small/MFR.tga` | `docs/assets/005_soviet_union_collapse/source_png/MFR_leader_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/MFR_leader.png` | `gfx/leaders/005_soviet_collapse/MFR_leader.dds` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | wired with dedicated leader and idea icons |
| `OGB` | `docs/assets/005_soviet_union_collapse/source_png/OGB_flag_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/OGB_flag.png` | `gfx/flags/OGB.tga`, `gfx/flags/medium/OGB.tga`, `gfx/flags/small/OGB.tga` | `docs/assets/005_soviet_union_collapse/source_png/OGB_leader_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/OGB_leader.png` | `gfx/leaders/005_soviet_collapse/OGB_leader.dds` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | wired with dedicated leader and idea icons |

`CFR_soviet_collapse_focus_tree` uses 58 focuses in `common/national_focus/005_soviet_collapse_factory_successors.txt`. The tree reuses the 33 existing `GFX_focus_CFR_*` sprites and their shine variants from `interface/005_soviet_collapse_factory_ancient_icons.gfx`; no new focus DDS files are required for this pass.

`MFR_soviet_collapse_focus_tree` uses 46 focuses in `common/national_focus/005_soviet_collapse_factory_successors.txt`. The tree reuses the 46 existing `GFX_focus_MFR_*` sprites and their shine variants from `interface/005_soviet_collapse_factory_ancient_icons.gfx`; no new focus DDS files are required for this pass.

`OGB_soviet_collapse_focus_tree` uses 54 focuses in `common/national_focus/005_soviet_collapse_factory_successors.txt`. The tree reuses the 54 existing `GFX_focus_OGB_*` sprites and their shine variants from `interface/005_soviet_collapse_factory_ancient_icons.gfx`; no new focus DDS files are required for this pass.


### Returned Names Placeholder Asset Records

Returned Names decisions and ideas are wired through existing Event 005 icon reuse in `interface/005_soviet_collapse_factory_ancient_icons.gfx`. Final art can replace the referenced sprites later if the museum-cabinet, old-banner, toll-route, Sogdian, Khwarazmian, Alan, and anti-antiquarian concepts need unique DDS files.

| Asset group | Sprite names | Status |
| --- | --- | --- |
| Returned Names category and decisions | `GFX_decision_category_soviet_collapse_returned_names`, `GFX_decision_soviet_collapse_open_museum_cabinets`, `GFX_decision_soviet_collapse_recruit_archivists`, `GFX_decision_soviet_collapse_commission_old_banner`, `GFX_decision_soviet_collapse_argue_khazar_toll_claim`, `GFX_decision_soviet_collapse_argue_sogdian_city_claim`, `GFX_decision_soviet_collapse_argue_khwarazmian_oasis_claim`, `GFX_decision_soviet_collapse_argue_alan_pass_claim`, `GFX_decision_soviet_collapse_reject_antiquarians` | placeholder reuse |
| Returned Names ideas | `GFX_idea_soviet_collapse_returned_names_pressure`, `GFX_idea_soviet_collapse_archivist_claim_council`, `GFX_idea_soviet_collapse_old_banner_mobilization` | placeholder reuse |

### Continuation Achievement Placeholder Asset Records

The continuation achievements are wired with stable DDS paths and placeholder reuse until bespoke final achievement art is created.

| Achievement | DDS paths | Interface wiring | Status |
| --- | --- | --- | --- |
| `chaosx_ach_concrete_republic` | `gfx/achievements/chaosx_ach_concrete_republic.dds`, `gfx/achievements/chaosx_ach_concrete_republic_grey.dds`, `gfx/achievements/chaosx_ach_concrete_republic_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_state_as_one_arms_order` | `gfx/achievements/chaosx_ach_state_as_one_arms_order.dds`, `gfx/achievements/chaosx_ach_state_as_one_arms_order_grey.dds`, `gfx/achievements/chaosx_ach_state_as_one_arms_order_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_bulgaria_on_volga` | `gfx/achievements/chaosx_ach_bulgaria_on_volga.dds`, `gfx/achievements/chaosx_ach_bulgaria_on_volga_grey.dds`, `gfx/achievements/chaosx_ach_bulgaria_on_volga_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_southern_cascade` | `gfx/achievements/chaosx_ach_southern_cascade.dds`, `gfx/achievements/chaosx_ach_southern_cascade_grey.dds`, `gfx/achievements/chaosx_ach_southern_cascade_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_concrete_does_not_sleep` | `gfx/achievements/chaosx_ach_concrete_does_not_sleep.dds`, `gfx/achievements/chaosx_ach_concrete_does_not_sleep_grey.dds`, `gfx/achievements/chaosx_ach_concrete_does_not_sleep_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_every_order_a_rifle` | `gfx/achievements/chaosx_ach_every_order_a_rifle.dds`, `gfx/achievements/chaosx_ach_every_order_a_rifle_grey.dds`, `gfx/achievements/chaosx_ach_every_order_a_rifle_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_bolghar_on_the_volga` | `gfx/achievements/chaosx_ach_bolghar_on_the_volga.dds`, `gfx/achievements/chaosx_ach_bolghar_on_the_volga_grey.dds`, `gfx/achievements/chaosx_ach_bolghar_on_the_volga_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_returned_names` | `gfx/achievements/chaosx_ach_returned_names.dds`, `gfx/achievements/chaosx_ach_returned_names_grey.dds`, `gfx/achievements/chaosx_ach_returned_names_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
