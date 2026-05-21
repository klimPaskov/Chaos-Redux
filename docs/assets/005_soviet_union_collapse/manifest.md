# Soviet Union Collapse Asset Manifest

## Package Status

The event script uses stable sprite and idea names. The active news, report, and primary super-event image candidates are sourced, processed, converted, and wired. Dedicated idea, decision, and shared focus icon sprite names are wired through stable filenames, with generated source PNGs, processed previews, final DDS files, and `.gfx` entries in place for active gameplay content.

The package now contains sourced news, report, and super-event images under `docs/assets/005_soviet_union_collapse/`, event-picture DDS files under `gfx/event_pictures/`, super-event DDS files under `gfx/super_events/`, and generated active idea, decision, and shared focus icon DDS files under the normal interface folders.

The active idea, decision, and shared focus icon package is generated from scratch with Codex built-in `image_gen`, cleaned, centered, converted, and wired. Branch-specific future tags and optional branches still need their own visual packages if those branches become active full country content.


The republic focus and influence expansion asset ledger lives at `docs/assets/005_soviet_union_collapse/republic_focus_and_influence/manifest.md`. It records the Ukraine, Belarus, Kazakhstan, regional republic, foreign patron, volunteer, regional faction, custom splinter, report-image, and super-event asset state for the continuation prompt.

The sourced report and super-event image source queue lives at `docs/assets/005_soviet_union_collapse/source_image_tracking_queue.md`. It lists every wired sourced image marked `sourced`, along with source links, author or archive notes, license notes, processed previews, final DDS paths, and contact sheets.

## Latest Source-Image Tracking State

The latest continuation recheck found `16` sourced report and super-event image rows: `6` report images and `10` super-event images. The matching art-pass sheet at `docs/assets/005_soviet_union_collapse/source_image_art_pass_sheet.md` has `48` empty optional art-pass boxes and `0` checked boxes. Every sourced report and super-event image row is tracked as `sourced`.

Latest direct asset recount confirms active news sprites/files at `7/7`, active report sprites/files at `6/6`, sourced-image contact sheets at `4/4`, and active super-event slots `14`, `15`, `17`, and `18` for sprite definitions, DDS files, title/description/button/quote localisation, image selectors, show helpers, script constant IDs, and documented audio slots. Former local-league super-event slots `25` through `27` and ordinary republic capstone super-event slots `19` through `22` are preserved as sourced art history only; ordinary league, coalition, and republic-route capstone presentation now uses news events.

The 2026-05-21 news/report coverage pass added normal event IDs `chaosx.nr5.45`, `.46`, `.47`, `.48`, `.49`, and `.95`. The later super-event demotion pass added news IDs `chaosx.nr5.140`, `.141`, `.142`, and `.143` with 397x153 news crops from the same sourced route-capstone images.

Optional source/crop choices can be recorded in the art-pass sheet, but empty boxes do not block Event 005 completion. Processed PNG previews, final DDS files, sprite definitions, and contact sheets are implementation and source evidence for the current wired rows.

## Active Wiring

| Use | Current sprite or picture | Final replacement needed |
| --- | --- | --- |
| Opening news | `GFX_news_soviet_union_collapse` | wired; art pass optional |
| League news | `GFX_news_free_republics_league` | wired; art pass optional |
| Second-seal news | `GFX_news_union_unmade` | wired; art pass optional |
| Union-war news | `GFX_news_union_unmade` | wired; a dedicated union-war variant can be added later |
| Republic route capstone news | `GFX_news_map_larger_than_union`, `GFX_news_steppe_beyond_history`, `GFX_news_corridors_decide`, `GFX_news_bread_state` | wired; cropped from sourced route-capstone image packages |
| Soviet report events | `GFX_report_union_crisis`, `GFX_report_breakaway_mobilization`, `GFX_report_depot_war`, `GFX_report_foreign_liaison`, `GFX_report_old_underground`, `GFX_report_railway_sovereignty` | wired, `sourced` |
| Idea icons | dedicated `GFX_idea_*` sprites in `interface/005_soviet_collapse_icons.gfx` | complete for active ideas |
| Decision icons | dedicated `GFX_decision_*` sprites in `interface/005_soviet_collapse_icons.gfx` | complete for active decisions |
| Shared breakaway focus icons | dedicated `GFX_focus_soviet_collapse_*` sprites in `interface/005_soviet_collapse_icons.gfx` | complete for the active 53-focus shared fallback tree through deliberate icon reuse |
| Regional republic focus icons | dedicated `GFX_baltic_soviet_collapse_*`, `GFX_caucasus_soviet_collapse_*`, `GFX_central_asia_soviet_collapse_*`, and `GFX_moldova_soviet_collapse_*` sprites in `interface/005_soviet_collapse_regional_icons.gfx` | complete for active regional runtime focus trees |
| Super-event | `GFX_super_event_union_unmade`, `GFX_super_event_black_banner_returns`, `GFX_super_event_workshops_choose_councils`, `GFX_super_event_every_port_a_council` | wired for active super-event use; retired republic-route and league/federation source packages are preserved below only for traceability |

## Required Active News Images

All news images target 397x153 DDS and should be black-and-white documentary style.

| Asset | Sprite | Source mode | Source PNG | Processed PNG | Final DDS | GFX file | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Opening Soviet collapse | `GFX_news_soviet_union_collapse` | internet source image | `docs/assets/005_soviet_union_collapse/source_png/news_soviet_union_collapse_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_soviet_union_collapse.png` | `gfx/event_pictures/news_soviet_union_collapse.dds` | `interface/chaosx_pictures.gfx` | wired |
| Free Republics' League | `GFX_news_free_republics_league` | internet source image | `docs/assets/005_soviet_union_collapse/source_png/news_free_republics_league_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_free_republics_league.png` | `gfx/event_pictures/news_free_republics_league.dds` | `interface/chaosx_pictures.gfx` | wired |
| Union unmade/deep collapse | `GFX_news_union_unmade` | internet source image | `docs/assets/005_soviet_union_collapse/source_png/news_union_unmade_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_union_unmade.png` | `gfx/event_pictures/news_union_unmade.dds` | `interface/chaosx_pictures.gfx` | wired |
| A Map Larger than the Union | `GFX_news_map_larger_than_union` | sourced route-capstone image crop | `docs/assets/005_soviet_union_collapse/source_png/super_event_map_larger_than_union_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_map_larger_than_union.png` | `gfx/event_pictures/news_map_larger_than_union.dds` | `interface/chaosx_pictures.gfx` | wired |
| The Steppe Beyond History | `GFX_news_steppe_beyond_history` | sourced route-capstone image crop | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_beyond_history_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_steppe_beyond_history.png` | `gfx/event_pictures/news_steppe_beyond_history.dds` | `interface/chaosx_pictures.gfx` | wired |
| The Corridors Decide | `GFX_news_corridors_decide` | sourced route-capstone image crop | `docs/assets/005_soviet_union_collapse/source_png/super_event_corridors_decide_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_corridors_decide.png` | `gfx/event_pictures/news_corridors_decide.dds` | `interface/chaosx_pictures.gfx` | wired |
| The Bread State | `GFX_news_bread_state` | sourced route-capstone image crop | `docs/assets/005_soviet_union_collapse/source_png/super_event_bread_state_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/news_bread_state.png` | `gfx/event_pictures/news_bread_state.dds` | `interface/chaosx_pictures.gfx` | wired |

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
| A Map Larger than the Union | `GFX_super_event_map_larger_than_union` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_map_larger_than_union_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_map_larger_than_union.png` | `gfx/super_events/super_event_map_larger_than_union.dds` | retired from active super-event use; route capstone reports through `chaosx.nr5.140` | preserved, `sourced` |
| The Steppe Beyond History | `GFX_super_event_steppe_beyond_history` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_beyond_history_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_beyond_history.png` | `gfx/super_events/super_event_steppe_beyond_history.dds` | retired from active super-event use; route capstone reports through `chaosx.nr5.141` | preserved, `sourced` |
| The Corridors Decide | `GFX_super_event_corridors_decide` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_corridors_decide_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_corridors_decide.png` | `gfx/super_events/super_event_corridors_decide.dds` | retired from active super-event use; route capstone reports through `chaosx.nr5.142` | preserved, `sourced` |
| The Bread State | `GFX_super_event_bread_state` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_bread_state_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_bread_state.png` | `gfx/super_events/super_event_bread_state.dds` | retired from active super-event use; route capstone reports through `chaosx.nr5.143` | preserved, `sourced` |
| The League of Equal Republics | `GFX_super_event_league_equal_republics` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_league_equal_republics_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_league_equal_republics.png` | `gfx/super_events/super_event_league_equal_republics.dds` | retired from active super-event use; League route uses normal event/report presentation | preserved, `sourced` |
| The Steppe Federation | `GFX_super_event_steppe_federation` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_federation_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_federation.png` | `gfx/super_events/super_event_steppe_federation.dds` | retired from active super-event use; Steppe Federation endgame reports through `chaosx.nr5.36` | preserved, `sourced` |
| The Baltic League | `GFX_super_event_baltic_restoration_pact` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_baltic_restoration_pact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_baltic_restoration_pact.png` | `gfx/super_events/super_event_baltic_restoration_pact.dds` | retired from active super-event use | preserved, `sourced` |
| The Caucasus League | `GFX_super_event_caucasus_defense_compact` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_caucasus_defense_compact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_caucasus_defense_compact.png` | `gfx/super_events/super_event_caucasus_defense_compact.dds` | retired from active super-event use | preserved, `sourced` |
| The Eastern Buffer Coalition | `GFX_super_event_eastern_buffer_coalition` | internet source image, source tracking | `docs/assets/005_soviet_union_collapse/source_png/super_event_eastern_buffer_coalition_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_eastern_buffer_coalition.png` | `gfx/super_events/super_event_eastern_buffer_coalition.dds` | retired from active super-event use | preserved, `sourced` |

## Optional Branch Super-Event Assets

These rare branch super-events are tied to custom extreme paths. Their image sheet was generated with Codex built-in `image_gen` because the branches are fictional, high-chaos, and symbolic rather than documentary scenes. The generated sheet is preserved at `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png`, processed into 457x328 previews, converted to DDS, and wired in `interface/chaosx_super_events.gfx`.

| Asset | Slot | Sprite | Source PNG | Processed PNG | Final DDS | Trigger source | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The Black Banner Returns | `15` | `GFX_super_event_black_banner_returns` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_black_banner_returns.png` | `gfx/super_events/super_event_black_banner_returns.dds` | `FTH_extreme_path`, `BBH_extreme_path` | wired, generated |
| The Northern Signals Break | `16` | `GFX_super_event_northern_signals_break` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_northern_signals_break.png` | `gfx/super_events/super_event_northern_signals_break.dds` | reserved northern-port helper | wired, generated |
| The Workshops Choose Their Councils | `17` | `GFX_super_event_workshops_choose_councils` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_workshops_choose_councils.png` | `gfx/super_events/super_event_workshops_choose_councils.dds` | `MFR_state_as_one_arms_order` | wired, generated |
| Every Port a Council | `18` | `GFX_super_event_every_port_a_council` | `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/super_event_every_port_a_council.png` | `gfx/super_events/super_event_every_port_a_council.dds` | `KRS_extreme_path` | wired, generated |
| The Steppe Beyond History | `20` | `GFX_super_event_steppe_beyond_history` | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_beyond_history_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_beyond_history.png` | `gfx/super_events/super_event_steppe_beyond_history.dds` | retired; route capstone reports through `chaosx.nr5.141` | preserved, `sourced` |
| The Corridors Decide | `21` | `GFX_super_event_corridors_decide` | `docs/assets/005_soviet_union_collapse/source_png/super_event_corridors_decide_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_corridors_decide.png` | `gfx/super_events/super_event_corridors_decide.dds` | retired; route capstone reports through `chaosx.nr5.142` | preserved, `sourced` |
| The Bread State | `22` | `GFX_super_event_bread_state` | `docs/assets/005_soviet_union_collapse/source_png/super_event_bread_state_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_bread_state.png` | `gfx/super_events/super_event_bread_state.dds` | retired; route capstone reports through `chaosx.nr5.143` | preserved, `sourced` |
| The League of Equal Republics | `23` | `GFX_super_event_league_equal_republics` | `docs/assets/005_soviet_union_collapse/source_png/super_event_league_equal_republics_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_league_equal_republics.png` | `gfx/super_events/super_event_league_equal_republics.dds` | retired; League route uses normal event/report presentation | preserved, `sourced` |
| The Steppe Federation | `24` | `GFX_super_event_steppe_federation` | `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_federation_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_federation.png` | `gfx/super_events/super_event_steppe_federation.dds` | retired; Steppe Federation endgame reports through `chaosx.nr5.36` | preserved, `sourced` |
| The Baltic League | `25` | `GFX_super_event_baltic_restoration_pact` | `docs/assets/005_soviet_union_collapse/source_png/super_event_baltic_restoration_pact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_baltic_restoration_pact.png` | `gfx/super_events/super_event_baltic_restoration_pact.dds` | retired; formation uses news event `chaosx.nr5.30` | preserved, `sourced` |
| The Caucasus League | `26` | `GFX_super_event_caucasus_defense_compact` | `docs/assets/005_soviet_union_collapse/source_png/super_event_caucasus_defense_compact_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_caucasus_defense_compact.png` | `gfx/super_events/super_event_caucasus_defense_compact.dds` | retired; formation uses news event `chaosx.nr5.31` | preserved, `sourced` |
| The Eastern Buffer Coalition | `27` | `GFX_super_event_eastern_buffer_coalition` | `docs/assets/005_soviet_union_collapse/source_png/super_event_eastern_buffer_coalition_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/super_event_eastern_buffer_coalition.png` | `gfx/super_events/super_event_eastern_buffer_coalition.dds` | retired; formation uses news event `chaosx.nr5.35` | preserved, `sourced` |

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

The replacement `soviet_collapse_belarus_focus_tree` is active gameplay for Event 005-created Belarus and now uses 53 focuses. Its branch-level sprites are wired in `interface/005_soviet_collapse_blr_icons.gfx` and point at dedicated 94x86 DDS files derived from existing generated Event 005 focus art.

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

The 92-focus `soviet_collapse_kazakhstan_focus_tree` is active gameplay for Event 005-created Kazakhstan and satisfies the clean-spec Kazakhstan focus-count target. Its branch-level sprites are wired in `interface/005_soviet_collapse_kaz_icons.gfx` and point at dedicated 94x86 DDS files derived from existing generated Event 005 focus art.

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
- `GFX_news_workshops_choose_councils`
- `GFX_news_every_port_a_council`

The Old Underground Wakes, Red Resistance without Moscow, The War of Committees, and The Flags Return Incorrectly are active event-log mutation tracks. The Ukrainian Black Banner Defense Committees contingency branch is active without branch-specific news/report imagery; those images remain unwired until the Free Territory or Black Banner branch becomes a major actor. Ordinary republic-route capstone news images for Ukraine, Kazakhstan, Belarus, and the Ukrainian Bread State are now wired through `GFX_news_map_larger_than_union`, `GFX_news_steppe_beyond_history`, `GFX_news_corridors_decide`, and `GFX_news_bread_state`.

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
| `ARD` | `docs/assets/005_soviet_union_collapse/processed_png/flags/ARD_normal.png` | `gfx/flags/ARD.tga` | `gfx/flags/medium/ARD.tga` | `gfx/flags/small/ARD.tga` | wired, generated reuse |
| `NLC` | `docs/assets/005_soviet_union_collapse/processed_png/flags/NLC_normal.png` | `gfx/flags/NLC.tga` | `gfx/flags/medium/NLC.tga` | `gfx/flags/small/NLC.tga` | wired, generated reuse |

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
| `PRA` | per-focus `gfx/interface/goals/soviet_collapse/pra_*.dds` files; see mapping below | `gfx/interface/ideas/soviet_collapse/005_pra_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_pra_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/PRA_leader.dds` | wired, focus icons use themed DDS reuse |
| `TSC` | per-focus `gfx/interface/goals/soviet_collapse/tsc_*.dds` files; see mapping below | `gfx/interface/ideas/soviet_collapse/005_tsc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_tsc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/TSC_leader.dds` | wired, focus icons use themed DDS reuse |
| `ICD` | per-focus `gfx/interface/goals/soviet_collapse/icd_*.dds` files; see mapping below | `gfx/interface/ideas/soviet_collapse/005_icd_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_icd_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/ICD_leader.dds` | wired, focus icons use themed DDS reuse |
| `RMC` | per-focus `gfx/interface/goals/soviet_collapse/rmc_*.dds` files; see mapping below | `gfx/interface/ideas/soviet_collapse/005_rmc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_rmc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/RMC_leader.dds` | wired, focus icons use themed DDS reuse |
| `DSC` | per-focus `gfx/interface/goals/soviet_collapse/dsc_*.dds` files; see mapping below | `gfx/interface/ideas/soviet_collapse/005_dsc_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_dsc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/DSC_leader.dds` | wired, focus icons use themed DDS reuse |
| `NRF` | per-focus `gfx/interface/goals/soviet_collapse/nrf_*.dds` files; see mapping below | `gfx/interface/ideas/soviet_collapse/005_nrf_custom_splinter_idea.dds` | `gfx/interface/decisions/soviet_collapse/005_nrf_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/NRF_leader.dds` | wired, focus icons use themed DDS reuse |
| `NLC` | `gfx/interface/goals/005_nlc_custom_splinter_focus.dds` | `gfx/interface/ideas/005_nlc_custom_splinter_idea.dds` | `gfx/interface/decisions/005_nlc_custom_splinter_decision.dds` | `gfx/leaders/005_soviet_collapse/NLC_leader.dds` | wired, generated reuse |

### Pale Railway Authority focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable PRA-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_custom_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_PRA_the_timetable_declares_authority` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_common_front_timetables.dds` | `gfx/interface/goals/soviet_collapse/pra_the_timetable_declares_authority.dds` | 94x86 | wired |
| `GFX_focus_PRA_novosibirsk_dispatcher_court` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_POL_warsaw_main_station.dds` | `gfx/interface/goals/soviet_collapse/pra_novosibirsk_dispatcher_court.dds` | 100x88 | wired |
| `GFX_focus_PRA_omsk_station_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_state_defense_guard.dds` | `gfx/interface/goals/soviet_collapse/pra_omsk_station_guard.dds` | 94x84 | wired |
| `GFX_focus_PRA_count_the_locomotives` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_IRQ_train.dds` | `gfx/interface/goals/soviet_collapse/pra_count_the_locomotives.dds` | 100x88 | wired |
| `GFX_focus_PRA_timetable_law` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_supreme_council_for_direction_of_war.dds` | `gfx/interface/goals/soviet_collapse/pra_timetable_law.dds` | 100x88 | wired |
| `GFX_focus_PRA_ticket_courts_for_every_platform` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_freedom_council.dds` | `gfx/interface/goals/soviet_collapse/pra_ticket_courts_for_every_platform.dds` | 100x88 | wired |
| `GFX_focus_PRA_the_board_overrules_ministers` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_eng_chiefs_of_staff_committee.dds` | `gfx/interface/goals/soviet_collapse/pra_the_board_overrules_ministers.dds` | 100x88 | wired |
| `GFX_focus_PRA_armored_train_directorate` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_railway_gun.dds` | `gfx/interface/goals/soviet_collapse/pra_armored_train_directorate.dds` | 100x88 | wired |
| `GFX_focus_PRA_repair_crews_without_ministries` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CHL_connect_the_northern_railways.dds` | `gfx/interface/goals/soviet_collapse/pra_repair_crews_without_ministries.dds` | 100x88 | wired |
| `GFX_focus_PRA_coal_water_and_spare_parts` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_reinforcing_the_supply_network.dds` | `gfx/interface/goals/soviet_collapse/pra_coal_water_and_spare_parts.dds` | 100x88 | wired |
| `GFX_focus_PRA_mobile_workshops` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_HUN_expand_the_diosgyor_machinery_factory.dds` | `gfx/interface/goals/soviet_collapse/pra_mobile_workshops.dds` | 100x88 | wired |
| `GFX_focus_PRA_switchyard_denial_posts` | `gfx/interface/goals/soviet_collapse/blr_soviet_collapse_rail.dds` | `gfx/interface/goals/soviet_collapse/pra_switchyard_denial_posts.dds` | 94x86 | wired |
| `GFX_focus_PRA_armored_train_schools` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_IRQ_found_the_iraqi_state_railways.dds` | `gfx/interface/goals/soviet_collapse/pra_armored_train_schools.dds` | 100x88 | wired |
| `GFX_focus_PRA_passport_of_the_moving_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_RAJ_the_silk_road.dds` | `gfx/interface/goals/soviet_collapse/pra_passport_of_the_moving_state.dds` | 100x88 | wired |
| `GFX_focus_PRA_neutral_corridor_letters` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_request_external_missions.dds` | `gfx/interface/goals/soviet_collapse/pra_neutral_corridor_letters.dds` | 94x86 | wired |
| `GFX_focus_PRA_charge_for_safe_passage` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_supply_line.dds` | `gfx/interface/goals/soviet_collapse/pra_charge_for_safe_passage.dds` | 100x88 | wired |
| `GFX_focus_PRA_league_transit_bargain` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/pra_league_transit_bargain.dds` | 94x86 | wired |
| `GFX_focus_PRA_claim_the_branch_lines` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_NOR_build_the_northern_rail.dds` | `gfx/interface/goals/soviet_collapse/pra_claim_the_branch_lines.dds` | 100x88 | wired |
| `GFX_focus_PRA_seize_the_junction_cities` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_south_manchuria_railway.dds` | `gfx/interface/goals/soviet_collapse/pra_seize_the_junction_cities.dds` | 100x88 | wired |
| `GFX_focus_PRA_rails_over_capitals` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_NOR_complete_the_sourthern_railway_network.dds` | `gfx/interface/goals/soviet_collapse/pra_rails_over_capitals.dds` | 100x88 | wired |
| `GFX_focus_PRA_flags_on_every_station` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_the_road_of_life.dds` | `gfx/interface/goals/soviet_collapse/pra_flags_on_every_station.dds` | 100x88 | wired |
| `GFX_focus_PRA_the_pale_line_endures` | `gfx/interface/goals/soviet_collapse/005_pra_custom_splinter_focus.dds` | `gfx/interface/goals/soviet_collapse/pra_the_pale_line_endures.dds` | 94x86 | wired |

### Tunguska Star Committee focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable TSC-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_custom_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_TSC_the_sky_keeps_records` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_radio_communication.dds` | `gfx/interface/goals/soviet_collapse/tsc_the_sky_keeps_records.dds` | 100x88 | wired |
| `GFX_focus_TSC_tura_observation_presidium` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SWE_king_in_council.dds` | `gfx/interface/goals/soviet_collapse/tsc_tura_observation_presidium.dds` | 100x88 | wired |
| `GFX_focus_TSC_kirensk_field_stations` | `~/projects/Hearts of Iron IV/gfx/interface/goals/goal_generic_radar.dds` | `gfx/interface/goals/soviet_collapse/tsc_kirensk_field_stations.dds` | 86x82 | wired |
| `GFX_focus_TSC_recover_the_burned_glass` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_nuclear_development.dds` | `gfx/interface/goals/soviet_collapse/tsc_recover_the_burned_glass.dds` | 100x88 | wired |
| `GFX_focus_TSC_radio_towers_in_the_taiga` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SWE_radiotjanst.dds` | `gfx/interface/goals/soviet_collapse/tsc_radio_towers_in_the_taiga.dds` | 100x88 | wired |
| `GFX_focus_TSC_portable_laboratory_trains` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_research2.dds` | `gfx/interface/goals/soviet_collapse/tsc_portable_laboratory_trains.dds` | 100x88 | wired |
| `GFX_focus_TSC_the_committee_of_instruments` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_cze_military_research_institute.dds` | `gfx/interface/goals/soviet_collapse/tsc_the_committee_of_instruments.dds` | 100x88 | wired |
| `GFX_focus_TSC_the_committee_of_signs` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_cryptologic_bomb.dds` | `gfx/interface/goals/soviet_collapse/tsc_the_committee_of_signs.dds` | 98x82 | wired |
| `GFX_focus_TSC_observatory_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_state_defense_guard.dds` | `gfx/interface/goals/soviet_collapse/tsc_observatory_guard.dds` | 94x84 | wired |
| `GFX_focus_TSC_perimeter_regiments` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BRA_national_guard.dds` | `gfx/interface/goals/soviet_collapse/tsc_perimeter_regiments.dds` | 100x88 | wired |
| `GFX_focus_TSC_night_survey_columns` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_nighttime_bombing.dds` | `gfx/interface/goals/soviet_collapse/tsc_night_survey_columns.dds` | 100x88 | wired |
| `GFX_focus_TSC_letters_to_academies` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_university_1.dds` | `gfx/interface/goals/soviet_collapse/tsc_letters_to_academies.dds` | 100x88 | wired |
| `GFX_focus_TSC_league_of_clear_signals` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/tsc_league_of_clear_signals.dds` | 94x86 | wired |
| `GFX_focus_TSC_claim_the_impact_zone` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_rocketry.dds` | `gfx/interface/goals/soviet_collapse/tsc_claim_the_impact_zone.dds` | 89x80 | wired |
| `GFX_focus_TSC_sky_over_siberia` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_the_air_is_our_sea.dds` | `gfx/interface/goals/soviet_collapse/tsc_sky_over_siberia.dds` | 100x88 | wired |
| `GFX_focus_TSC_starfall_mandate` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_z_bomber_project.dds` | `gfx/interface/goals/soviet_collapse/tsc_starfall_mandate.dds` | 100x88 | wired |
| `GFX_focus_TSC_observatory_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_research.dds` | `gfx/interface/goals/soviet_collapse/tsc_observatory_state.dds` | 89x80 | wired |
| `GFX_focus_TSC_the_quiet_sky_settlement` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_FIN_united_under_the_north_star.dds` | `gfx/interface/goals/soviet_collapse/tsc_the_quiet_sky_settlement.dds` | 100x88 | wired |

### Iron Commissariat of the Dead focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable ICD-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_custom_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_ICD_open_the_dead_rolls` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_AFG_graveyard_of_empires.dds` | `gfx/interface/goals/soviet_collapse/icd_open_the_dead_rolls.dds` | 100x88 | wired |
| `GFX_focus_ICD_ryazan_grave_commissariat` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_supreme_council_for_direction_of_war.dds` | `gfx/interface/goals/soviet_collapse/icd_ryazan_grave_commissariat.dds` | 100x88 | wired |
| `GFX_focus_ICD_penza_memorial_workshops` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_HUN_establish_the_mavag_army_division.dds` | `gfx/interface/goals/soviet_collapse/icd_penza_memorial_workshops.dds` | 100x88 | wired |
| `GFX_focus_ICD_census_of_absent_citizens` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_PHI_bill_of_rights_for_veterans.dds` | `gfx/interface/goals/soviet_collapse/icd_census_of_absent_citizens.dds` | 100x88 | wired |
| `GFX_focus_ICD_commissars_of_last_addresses` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_eng_chiefs_of_staff_committee.dds` | `gfx/interface/goals/soviet_collapse/icd_commissars_of_last_addresses.dds` | 100x88 | wired |
| `GFX_focus_ICD_commissars_who_do_not_die` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_builder_of_the_red_army.dds` | `gfx/interface/goals/soviet_collapse/icd_commissars_who_do_not_die.dds` | 100x88 | wired |
| `GFX_focus_ICD_black_seal_requisitions` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_HUN_legacy_of_the_black_legion.dds` | `gfx/interface/goals/soviet_collapse/icd_black_seal_requisitions.dds` | 100x88 | wired |
| `GFX_focus_ICD_funeral_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_state_defense_guard.dds` | `gfx/interface/goals/soviet_collapse/icd_funeral_guard.dds` | 94x84 | wired |
| `GFX_focus_ICD_dead_roll_supply_bureau` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_army_attack.dds` | `gfx/interface/goals/soviet_collapse/icd_dead_roll_supply_bureau.dds` | 100x88 | wired |
| `GFX_focus_ICD_memorial_battalions` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_korean_volunteer_army.dds` | `gfx/interface/goals/soviet_collapse/icd_memorial_battalions.dds` | 100x88 | wired |
| `GFX_focus_ICD_archives_of_every_front` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_czechoslovak_legion_export.dds` | `gfx/interface/goals/soviet_collapse/icd_archives_of_every_front.dds` | 100x88 | wired |
| `GFX_focus_ICD_letters_to_grieving_cities` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_request_external_missions.dds` | `gfx/interface/goals/soviet_collapse/icd_letters_to_grieving_cities.dds` | 94x86 | wired |
| `GFX_focus_ICD_league_of_last_addresses` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/icd_league_of_last_addresses.dds` | 94x86 | wired |
| `GFX_focus_ICD_claim_the_unburied_front` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_the_road_of_life.dds` | `gfx/interface/goals/soviet_collapse/icd_claim_the_unburied_front.dds` | 100x88 | wired |
| `GFX_focus_ICD_grave_columns_march` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_GER_all_for_the_front.dds` | `gfx/interface/goals/soviet_collapse/icd_grave_columns_march.dds` | 100x88 | wired |
| `GFX_focus_ICD_citizens_after_death` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_focus_fra_national_resistance_council.dds` | `gfx/interface/goals/soviet_collapse/icd_citizens_after_death.dds` | 100x88 | wired |
| `GFX_focus_ICD_commissariat_without_end` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_the_glory_of_the_red_army_communism.dds` | `gfx/interface/goals/soviet_collapse/icd_commissariat_without_end.dds` | 100x88 | wired |
| `GFX_focus_ICD_state_of_last_addresses` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BEL_legacy_of_the_soldier_king.dds` | `gfx/interface/goals/soviet_collapse/icd_state_of_last_addresses.dds` | 100x88 | wired |

### Dead Soldiers' Congress focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable DSC-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_custom_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_DSC_call_the_dead_soldiers_congress` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BEL_legacy_of_the_soldier_king.dds` | `gfx/interface/goals/soviet_collapse/dsc_call_the_dead_soldiers_congress.dds` | 100x88 | wired |
| `GFX_focus_DSC_stalingrad_roll_call` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_the_glory_of_the_red_army_communism.dds` | `gfx/interface/goals/soviet_collapse/dsc_stalingrad_roll_call.dds` | 100x88 | wired |
| `GFX_focus_DSC_voronezh_rearguard_archives` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_czechoslovak_legion_export.dds` | `gfx/interface/goals/soviet_collapse/dsc_voronezh_rearguard_archives.dds` | 100x88 | wired |
| `GFX_focus_DSC_vote_by_regimental_dead` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_PHI_bill_of_rights_for_veterans.dds` | `gfx/interface/goals/soviet_collapse/dsc_vote_by_regimental_dead.dds` | 100x88 | wired |
| `GFX_focus_DSC_witness_officers` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_eng_chiefs_of_staff_committee.dds` | `gfx/interface/goals/soviet_collapse/dsc_witness_officers.dds` | 100x88 | wired |
| `GFX_focus_DSC_revenant_staff_line` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_builder_of_the_red_army.dds` | `gfx/interface/goals/soviet_collapse/dsc_revenant_staff_line.dds` | 100x88 | wired |
| `GFX_focus_DSC_grave_ordnance_claims` | `~/projects/Hearts of Iron IV/gfx/interface/goals/goal_generic_army_artillery.dds` | `gfx/interface/goals/soviet_collapse/dsc_grave_ordnance_claims.dds` | 94x77 | wired |
| `GFX_focus_DSC_field_hospital_memorials` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_bad_medical.dds` | `gfx/interface/goals/soviet_collapse/dsc_field_hospital_memorials.dds` | 100x88 | wired |
| `GFX_focus_DSC_rearguard_supply_bureau` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_reinforcing_the_supply_network.dds` | `gfx/interface/goals/soviet_collapse/dsc_rearguard_supply_bureau.dds` | 100x88 | wired |
| `GFX_focus_DSC_dead_regiment_columns` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_GER_all_for_the_front.dds` | `gfx/interface/goals/soviet_collapse/dsc_dead_regiment_columns.dds` | 100x88 | wired |
| `GFX_focus_DSC_maps_of_lost_armies` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_RAJ_the_silk_road.dds` | `gfx/interface/goals/soviet_collapse/dsc_maps_of_lost_armies.dds` | 100x88 | wired |
| `GFX_focus_DSC_letters_to_veteran_towns` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_request_external_missions.dds` | `gfx/interface/goals/soviet_collapse/dsc_letters_to_veteran_towns.dds` | 94x86 | wired |
| `GFX_focus_DSC_league_of_old_fronts` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/dsc_league_of_old_fronts.dds` | 94x86 | wired |
| `GFX_focus_DSC_claim_the_soldiers_road` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_road_investment.dds` | `gfx/interface/goals/soviet_collapse/dsc_claim_the_soldiers_road.dds` | 100x88 | wired |
| `GFX_focus_DSC_armies_that_do_not_demobilize` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_GER_german_army_invincible.dds` | `gfx/interface/goals/soviet_collapse/dsc_armies_that_do_not_demobilize.dds` | 100x88 | wired |
| `GFX_focus_DSC_republic_of_roll_calls` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SWE_the_nordic_defense_council.dds` | `gfx/interface/goals/soviet_collapse/dsc_republic_of_roll_calls.dds` | 100x88 | wired |
| `GFX_focus_DSC_congress_of_the_dead_army` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_PRC_peoples_liberation_army.dds` | `gfx/interface/goals/soviet_collapse/dsc_congress_of_the_dead_army.dds` | 100x88 | wired |
| `GFX_focus_DSC_memorial_frontier_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_AFG_graveyard_of_empires.dds` | `gfx/interface/goals/soviet_collapse/dsc_memorial_frontier_state.dds` | 100x88 | wired |

### Northern Revenant Fleet focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable NRF-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_custom_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_NRF_signal_from_lost_convoys` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_radio_guided_missiles.dds` | `gfx/interface/goals/soviet_collapse/nrf_signal_from_lost_convoys.dds` | 100x88 | wired |
| `GFX_focus_NRF_murmansk_dead_muster` | `gfx/interface/goals/soviet_collapse/005_nrf_custom_splinter_focus.dds` | `gfx/interface/goals/soviet_collapse/nrf_murmansk_dead_muster.dds` | 94x86 | wired |
| `GFX_focus_NRF_arkhangelsk_ice_registers` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_secure_ministry_ledgers.dds` | `gfx/interface/goals/soviet_collapse/nrf_arkhangelsk_ice_registers.dds` | 94x86 | wired |
| `GFX_focus_NRF_count_the_drowned_crews` | `gfx/interface/goals/soviet_collapse/005_dsc_custom_splinter_focus.dds` | `gfx/interface/goals/soviet_collapse/nrf_count_the_drowned_crews.dds` | 94x86 | wired |
| `GFX_focus_NRF_living_harbor_committees` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_form_a_regency_council.dds` | `gfx/interface/goals/soviet_collapse/nrf_living_harbor_committees.dds` | 100x88 | wired |
| `GFX_focus_NRF_revenant_admiralty` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_AUS_promote_admirals.dds` | `gfx/interface/goals/soviet_collapse/nrf_revenant_admiralty.dds` | 100x88 | wired |
| `GFX_focus_NRF_salvage_the_dark_berths` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_FIN_acquire_andros_dockyards.dds` | `gfx/interface/goals/soviet_collapse/nrf_salvage_the_dark_berths.dds` | 100x88 | wired |
| `GFX_focus_NRF_icebound_marine_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_PHI_marine_corps.dds` | `gfx/interface/goals/soviet_collapse/nrf_icebound_marine_guard.dds` | 100x88 | wired |
| `GFX_focus_NRF_dead_convoy_supply_board` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CHI_northern_naval_logistics.dds` | `gfx/interface/goals/soviet_collapse/nrf_dead_convoy_supply_board.dds` | 100x88 | wired |
| `GFX_focus_NRF_ghost_convoy_escorts` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_NOR_nortraship.dds` | `gfx/interface/goals/soviet_collapse/nrf_ghost_convoy_escorts.dds` | 100x88 | wired |
| `GFX_focus_NRF_maps_of_sunken_routes` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_ICE_securing_the_north_sea_passage.dds` | `gfx/interface/goals/soviet_collapse/nrf_maps_of_sunken_routes.dds` | 100x88 | wired |
| `GFX_focus_NRF_letters_to_sailor_towns` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_request_external_missions.dds` | `gfx/interface/goals/soviet_collapse/nrf_letters_to_sailor_towns.dds` | 94x86 | wired |
| `GFX_focus_NRF_league_of_cold_ports` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/nrf_league_of_cold_ports.dds` | 94x86 | wired |
| `GFX_focus_NRF_claim_the_white_sea_lane` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_bulgaria_on_the_three_seas.dds` | `gfx/interface/goals/soviet_collapse/nrf_claim_the_white_sea_lane.dds` | 100x88 | wired |
| `GFX_focus_NRF_fleet_that_does_not_dock` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_GER_high_seas_fleet.dds` | `gfx/interface/goals/soviet_collapse/nrf_fleet_that_does_not_dock.dds` | 100x88 | wired |
| `GFX_focus_NRF_port_republic_of_the_living` | `gfx/interface/goals/soviet_collapse/baltic_soviet_collapse_port_customs.dds` | `gfx/interface/goals/soviet_collapse/nrf_port_republic_of_the_living.dds` | 94x86 | wired |
| `GFX_focus_NRF_northern_revenant_fleet` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_PRC_naval_capstone.dds` | `gfx/interface/goals/soviet_collapse/nrf_northern_revenant_fleet.dds` | 100x88 | wired |
| `GFX_focus_NRF_memorial_convoy_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_czechoslovak_legion_export.dds` | `gfx/interface/goals/soviet_collapse/nrf_memorial_convoy_state.dds` | 100x88 | wired |

Custom tag flags and tag-specific focus icons are required only for tags that are actually added. Each implemented tag needs normal, medium, and small flags plus focus icons for any focus tree content.

### Red Martyrs' Resurrection Cult focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable RMC-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_custom_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_RMC_open_the_red_martyrology` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BRA_socialist_theologians.dds` | `gfx/interface/goals/soviet_collapse/rmc_open_the_red_martyrology.dds` | 100x88 | wired |
| `GFX_focus_RMC_tambov_witness_cells` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_POL_resistance.dds` | `gfx/interface/goals/soviet_collapse/rmc_tambov_witness_cells.dds` | 100x88 | wired |
| `GFX_focus_RMC_lipetsk_reliquary_workshops` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_HUN_expand_the_diosgyor_machinery_factory.dds` | `gfx/interface/goals/soviet_collapse/rmc_lipetsk_reliquary_workshops.dds` | 100x88 | wired |
| `GFX_focus_RMC_count_the_returning_names` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_population_growth.dds` | `gfx/interface/goals/soviet_collapse/rmc_count_the_returning_names.dds` | 100x88 | wired |
| `GFX_focus_RMC_communes_of_witnesses` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_AUS_danubian_socialist_communes.dds` | `gfx/interface/goals/soviet_collapse/rmc_communes_of_witnesses.dds` | 100x88 | wired |
| `GFX_focus_RMC_cadres_of_resurrection` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_SOV_builder_of_the_red_army.dds` | `gfx/interface/goals/soviet_collapse/rmc_cadres_of_resurrection.dds` | 100x88 | wired |
| `GFX_focus_RMC_blood_oath_requisitions` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_communist_industry.dds` | `gfx/interface/goals/soviet_collapse/rmc_blood_oath_requisitions.dds` | 100x88 | wired |
| `GFX_focus_RMC_reliquary_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_state_defense_guard.dds` | `gfx/interface/goals/soviet_collapse/rmc_reliquary_guard.dds` | 94x84 | wired |
| `GFX_focus_RMC_shrine_foundries` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_HUN_establish_the_mavag_army_division.dds` | `gfx/interface/goals/soviet_collapse/rmc_shrine_foundries.dds` | 100x88 | wired |
| `GFX_focus_RMC_dead_volunteer_columns` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_korean_volunteer_army.dds` | `gfx/interface/goals/soviet_collapse/rmc_dead_volunteer_columns.dds` | 100x88 | wired |
| `GFX_focus_RMC_hagiographers_of_every_front` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CZE_czechoslovak_legion_export.dds` | `gfx/interface/goals/soviet_collapse/rmc_hagiographers_of_every_front.dds` | 100x88 | wired |
| `GFX_focus_RMC_letters_to_mourning_towns` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_request_external_missions.dds` | `gfx/interface/goals/soviet_collapse/rmc_letters_to_mourning_towns.dds` | 94x86 | wired |
| `GFX_focus_RMC_league_of_mourning_communes` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/rmc_league_of_mourning_communes.dds` | 94x86 | wired |
| `GFX_focus_RMC_claim_the_burial_roads` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_road_investment.dds` | `gfx/interface/goals/soviet_collapse/rmc_claim_the_burial_roads.dds` | 100x88 | wired |
| `GFX_focus_RMC_procession_columns` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_PRC_revolutionary_war_of_the_masses.dds` | `gfx/interface/goals/soviet_collapse/rmc_procession_columns.dds` | 100x88 | wired |
| `GFX_focus_RMC_republic_of_witnesses` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_focus_fra_national_resistance_council.dds` | `gfx/interface/goals/soviet_collapse/rmc_republic_of_witnesses.dds` | 100x88 | wired |
| `GFX_focus_RMC_resurrection_without_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_spr_the_anti_fascist_workers_revolution.dds` | `gfx/interface/goals/soviet_collapse/rmc_resurrection_without_state.dds` | 100x88 | wired |
| `GFX_focus_RMC_shrine_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_COG_recognize_the_kimbanguist_church.dds` | `gfx/interface/goals/soviet_collapse/rmc_shrine_state.dds` | 100x88 | wired |

## Blocked Or Incomplete Final Assets

- Final generated idea icons: `complete` for active ideas. Source sheets, cropped source PNGs, processed previews, and DDS files are recorded above.
- Final generated decision icons: `complete` for active decisions. Source sheet, cropped source PNGs, processed previews, and DDS files are recorded above.
- Foreign patron category and decision icons plus volunteer decision and national spirit icons: `complete` for the implemented influence and volunteer mechanics. Processed PNG previews live in `docs/assets/005_soviet_union_collapse/processed_png/foreign_patron_decisions/`, `docs/assets/005_soviet_union_collapse/processed_png/volunteer_decisions/`, and `docs/assets/005_soviet_union_collapse/processed_png/volunteer_ideas/`; final DDS files live in `gfx/interface/decisions/` and `gfx/interface/ideas/`; sprite definitions are wired in `interface/005_soviet_collapse_icons.gfx`. The staged recognition, arms/logistics, reconstruction, volunteer, adviser, and patronage-risk ideas intentionally reuse the existing `legal_restoration_claim`, `captured_soviet_depots`, `foreign_volunteers`, and `military_defense_council` idea pictures, so `soviet_collapse_foreign_arsenal_dependency_network` requires no new DDS file.
- Regional faction category and decision icons: `complete` for the implemented category, founding decisions, shared-goal decisions, mediation decision, and withdrawal decision. Processed PNG previews live in `docs/assets/005_soviet_union_collapse/processed_png/regional_faction_decisions/`, final DDS files live in `gfx/interface/decisions/`, and the sprite definitions are wired in `interface/005_soviet_collapse_icons.gfx`.
- Ukraine, Belarus, and Kazakhstan runtime branch focus icons: `complete` for the implemented branch sprite sets. Processed PNG previews live in `docs/assets/005_soviet_union_collapse/processed_png/republic_branch_focus_icons/`, final DDS files live in `gfx/interface/goals/`, and the sprite definitions are wired in `interface/005_soviet_collapse_ukraine_icons.gfx`, `interface/005_soviet_collapse_blr_icons.gfx`, and `interface/005_soviet_collapse_kaz_icons.gfx`.
- Optional branch super-event images: `complete` for Black Banner, Northern Signals Break, Workshops Choose Their Councils, Port Council, Ukraine's A Map Larger than the Union branch reveal, Kazakhstan's Steppe Beyond History branch reveal, Belarus's Corridors Decide branch reveal, Ukraine's Bread State branch reveal, Ukraine's League of Equal Republics branch reveal, and the Steppe Federation formation reveal. Former Baltic League, Caucasus League, and Eastern Buffer Coalition super-event images are preserved as sourced art history because ordinary formation now uses news events.
- Sourced report and super-event tracking sheets: labeled grids `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_report_images_tracking_sheet_labeled.png` and `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_super_event_images_tracking_sheet_labeled.png`, plus raw grids `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_report_images_tracking_sheet.png` and `docs/assets/005_soviet_union_collapse/contact_sheets/sourced_super_event_images_tracking_sheet.png`, exist for source tracking of the `sourced` sourced-image rows.
- Optional branch news/report/super-event images: `not wired`. They remain in the backlog until matching Black Banner, industrial, railway, Kronstadt, or naval branches exist as gameplay.

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



NLC generated-reuse asset package: `gfx/flags/NLC.tga`, `gfx/flags/medium/NLC.tga`, `gfx/flags/small/NLC.tga`, `gfx/interface/goals/005_nlc_custom_splinter_focus.dds`, `gfx/interface/ideas/005_nlc_custom_splinter_idea.dds`, `gfx/interface/decisions/005_nlc_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/NLC_leader.dds` are wired. Source and processed previews use the corresponding `005_nlc_*`, `NLC_leader_*`, and `nlc_custom_splinter_*` files under `docs/assets/005_soviet_union_collapse/`.







### Idel-Ural League Generated-Reuse Asset Records

`IUL` currently reuses the generated Ural Workers custom-splinter package as replacement-art candidate material. Stable paths are `gfx/flags/IUL.tga`, `gfx/flags/medium/IUL.tga`, `gfx/flags/small/IUL.tga`, `gfx/interface/goals/soviet_collapse/005_iul_custom_splinter_focus.dds`, `gfx/interface/ideas/soviet_collapse/005_iul_custom_splinter_idea.dds`, `gfx/interface/decisions/soviet_collapse/005_iul_custom_splinter_decision.dds`, and `gfx/leaders/005_soviet_collapse/IUL_leader.dds`. Source and processed PNG records live under `docs/assets/005_soviet_union_collapse/source_png/` and `docs/assets/005_soviet_union_collapse/processed_png/`.

### Old Great Bulgaria Asset Records

`OGB` is wired as an Event 005 high-chaos package with stable sprite names in `interface/005_soviet_collapse_factory_ancient_icons.gfx`. Existing final flags remain at `gfx/flags/OGB.tga`, `gfx/flags/medium/OGB.tga`, and `gfx/flags/small/OGB.tga`. The leader portrait sprite `GFX_portrait_OGB_volga_restoration_council` uses stable OGB-specific final art at `gfx/leaders/005_soviet_collapse/OGB_leader.dds`, copied from the vanilla `MEN` restoration-council portrait source. Decision and idea sprites now use stable OGB-specific DDS paths copied from themed Event 005 and vanilla DDS sources. Focus sprites use 23 per-focus `gfx/interface/goals/soviet_collapse/ogb_*.dds` files copied from Bulgaria, Volga, trade, defense, diplomacy, and restoration-themed DDS sources.

| Asset group | Sprite names | Status |
| --- | --- | --- |
| OGB leader | `GFX_portrait_OGB_volga_restoration_council` | wired, OGB-specific final DDS copied from vanilla restoration-council portrait source |
| OGB decisions | `GFX_decision_ogb_consolidate_volga_registers`, `GFX_decision_ogb_guard_kazan_ferry_line`, `GFX_decision_ogb_declare_restoration_state` | wired, decision icons use themed DDS reuse; see mapping below |
| OGB ideas | `GFX_idea_ogb_disputed_restored_name`, `GFX_idea_ogb_volga_restoration_council`, `GFX_idea_ogb_volga_trade_road`, `GFX_idea_ogb_notable_workshop_compact`, `GFX_idea_ogb_heritage_guard`, `GFX_idea_ogb_old_capital_guard`, `GFX_idea_ogb_restored_volga_empire` | wired, idea icons use themed DDS reuse; see mapping below |
| OGB focuses | `GFX_focus_OGB_*` and `_shine` variants | wired, focus icons use themed DDS reuse; see mapping below |

#### Old Great Bulgaria leader portrait mapping

Source mode: existing vanilla leader DDS reuse copied into a stable OGB-specific final path. The source fits the Volga restoration council concept better than the previous Idel-Ural placeholder because it presents a civilian restoration-council figure rather than another Event 005 splinter leader. Sprite definition is in `interface/005_soviet_collapse_factory_ancient_icons.gfx`.

| Sprite | Source DDS | Processed preview | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- | --- |
| `GFX_portrait_OGB_volga_restoration_council` | `~/projects/Hearts of Iron IV/gfx/leaders/MEN/portrait_MEN_yondonwangchug.dds`; recorded preview `docs/assets/005_soviet_union_collapse/source_png/OGB_leader_source.png` | `docs/assets/005_soviet_union_collapse/processed_png/OGB_leader.png` | `gfx/leaders/005_soviet_collapse/OGB_leader.dds` | 156x210 | wired |

#### Old Great Bulgaria decision and idea icon mapping

Source mode: existing HOI4 or Chaos Redux DDS reuse copied into stable OGB-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Sprite definitions are in `interface/005_soviet_collapse_factory_ancient_icons.gfx`.

| Sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_decision_ogb_consolidate_volga_registers` | `gfx/interface/decisions/soviet_collapse/005_iul_custom_splinter_decision.dds` | `gfx/interface/decisions/soviet_collapse/ogb_consolidate_volga_registers.dds` | 32x32 | wired |
| `GFX_decision_ogb_guard_kazan_ferry_line` | `gfx/interface/decisions/soviet_collapse/decision_soviet_collapse_regional_goal_logistics.dds` | `gfx/interface/decisions/soviet_collapse/ogb_guard_kazan_ferry_line.dds` | 32x32 | wired |
| `GFX_decision_ogb_declare_restoration_state` | `gfx/interface/decisions/soviet_collapse/decision_soviet_collapse_regional_goal_recognition.dds` | `gfx/interface/decisions/soviet_collapse/ogb_declare_restoration_state.dds` | 32x32 | wired |
| `GFX_idea_ogb_disputed_restored_name` | `gfx/interface/ideas/soviet_collapse/idea_flags_return_incorrectly.dds` | `gfx/interface/ideas/soviet_collapse/ogb_disputed_restored_name.dds` | 60x68 | wired |
| `GFX_idea_ogb_volga_restoration_council` | `~/projects/Hearts of Iron IV/gfx/interface/ideas/idea_MEN_pailingmiao_council.dds` | `gfx/interface/ideas/soviet_collapse/ogb_volga_restoration_council.dds` | 60x68 | wired |
| `GFX_idea_ogb_volga_trade_road` | `gfx/interface/ideas/soviet_collapse/005_iul_custom_splinter_idea.dds` | `gfx/interface/ideas/soviet_collapse/ogb_volga_trade_road.dds` | 60x68 | wired |
| `GFX_idea_ogb_notable_workshop_compact` | `gfx/interface/ideas/soviet_collapse/005_cfr_custom_splinter_idea.dds` | `gfx/interface/ideas/soviet_collapse/ogb_notable_workshop_compact.dds` | 60x68 | wired |
| `GFX_idea_ogb_heritage_guard` | `~/projects/Hearts of Iron IV/gfx/interface/ideas/idea_HABSBURG_cavalry.dds` | `gfx/interface/ideas/soviet_collapse/ogb_heritage_guard.dds` | 60x68 | wired |
| `GFX_idea_ogb_old_capital_guard` | `~/projects/Hearts of Iron IV/gfx/interface/ideas/idea_bul_bulgarian_irredentism.dds` | `gfx/interface/ideas/soviet_collapse/ogb_old_capital_guard.dds` | 60x68 | wired |
| `GFX_idea_ogb_restored_volga_empire` | `~/projects/Hearts of Iron IV/gfx/interface/ideas/idea_bul_third_bulgarian_state.dds` | `gfx/interface/ideas/soviet_collapse/ogb_restored_volga_empire.dds` | 63x71 | wired |

#### Old Great Bulgaria focus icon mapping

Source mode: existing HOI4 or Chaos Redux focus DDS reuse copied into stable OGB-specific final paths. Processed PNG preview: not applicable for direct DDS reuse. Target size: source focus-icon DDS dimensions preserved. Sprite definitions are in `interface/005_soviet_collapse_factory_ancient_icons.gfx`; every row has both normal and `_shine` sprite variants.

| Focus sprite | Source DDS | Final DDS | Dimensions | Status |
| --- | --- | --- | --- | --- |
| `GFX_focus_OGB_volga_registers` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_secure_ministry_ledgers.dds` | `gfx/interface/goals/soviet_collapse/ogb_volga_registers.dds` | 94x86 | wired |
| `GFX_focus_OGB_bolghar_name` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_the_third_bulgarian_empire.dds` | `gfx/interface/goals/soviet_collapse/ogb_bolghar_name.dds` | 100x88 | wired |
| `GFX_focus_OGB_restoration_council` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_form_a_regency_council.dds` | `gfx/interface/goals/soviet_collapse/ogb_restoration_council.dds` | 100x88 | wired |
| `GFX_focus_OGB_scholars_charter` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_university_1.dds` | `gfx/interface/goals/soviet_collapse/ogb_scholars_charter.dds` | 100x88 | wired |
| `GFX_focus_OGB_clerics_charter` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_restore_the_bulgarian_patriarchate.dds` | `gfx/interface/goals/soviet_collapse/ogb_clerics_charter.dds` | 100x88 | wired |
| `GFX_focus_OGB_trade_tolls` | `~/projects/Hearts of Iron IV/gfx/interface/goals/goal_generic_trade.dds` | `gfx/interface/goals/soviet_collapse/ogb_trade_tolls.dds` | 87x66 | wired |
| `GFX_focus_OGB_kazan_ferries` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_CHI_river_crossing_studies.dds` | `gfx/interface/goals/soviet_collapse/ogb_kazan_ferries.dds` | 100x88 | wired |
| `GFX_focus_OGB_caravan_letters` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_RAJ_the_silk_road.dds` | `gfx/interface/goals/soviet_collapse/ogb_caravan_letters.dds` | 100x88 | wired |
| `GFX_focus_OGB_court_records` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_JAP_supreme_council_for_direction_of_war.dds` | `gfx/interface/goals/soviet_collapse/ogb_court_records.dds` | 100x88 | wired |
| `GFX_focus_OGB_notables_workshops` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_HUN_expand_the_diosgyor_machinery_factory.dds` | `gfx/interface/goals/soviet_collapse/ogb_notables_workshops.dds` | 100x88 | wired |
| `GFX_focus_OGB_restored_society` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_consolidate_the_third_bulgarian_state.dds` | `gfx/interface/goals/soviet_collapse/ogb_restored_society.dds` | 100x88 | wired |
| `GFX_focus_OGB_heritage_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_found_the_brannik.dds` | `gfx/interface/goals/soviet_collapse/ogb_heritage_guard.dds` | 100x88 | wired |
| `GFX_focus_OGB_volga_crossings` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_AFG_helmand_river_authority.dds` | `gfx/interface/goals/soviet_collapse/ogb_volga_crossings.dds` | 100x88 | wired |
| `GFX_focus_OGB_cavalry_registers` | `~/projects/Hearts of Iron IV/gfx/interface/goals/goal_generic_cavalry.dds` | `gfx/interface/goals/soviet_collapse/ogb_cavalry_registers.dds` | 88x78 | wired |
| `GFX_focus_OGB_treat_idel_ural` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_convene_league_liaisons.dds` | `gfx/interface/goals/soviet_collapse/ogb_treat_idel_ural.dds` | 94x86 | wired |
| `GFX_focus_OGB_two_seals` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_power_to_the_tsar.dds` | `gfx/interface/goals/soviet_collapse/ogb_two_seals.dds` | 100x88 | wired |
| `GFX_focus_OGB_kazan_ufa_letters` | `gfx/interface/goals/soviet_collapse/focus_soviet_collapse_request_external_missions.dds` | `gfx/interface/goals/soviet_collapse/ogb_kazan_ufa_letters.dds` | 94x86 | wired |
| `GFX_focus_OGB_idel_ural_question` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_the_fate_of_the_balkans.dds` | `gfx/interface/goals/soviet_collapse/ogb_idel_ural_question.dds` | 100x88 | wired |
| `GFX_focus_OGB_trade_cities` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_bulgaria_on_the_three_seas.dds` | `gfx/interface/goals/soviet_collapse/ogb_trade_cities.dds` | 100x88 | wired |
| `GFX_focus_OGB_old_capital_guard` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_guardians_of_the_balkans.dds` | `gfx/interface/goals/soviet_collapse/ogb_old_capital_guard.dds` | 100x88 | wired |
| `GFX_focus_OGB_future_bulgaria_file` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_TUR_reconfigure_turkish_foreign_policy.dds` | `gfx/interface/goals/soviet_collapse/ogb_future_bulgaria_file.dds` | 100x88 | wired |
| `GFX_focus_OGB_restoration_state` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_BUL_the_return_of_ferdinand.dds` | `gfx/interface/goals/soviet_collapse/ogb_restoration_state.dds` | 100x88 | wired |
| `GFX_focus_OGB_modern_war` | `~/projects/Hearts of Iron IV/gfx/interface/goals/focus_generic_total_war.dds` | `gfx/interface/goals/soviet_collapse/ogb_modern_war.dds` | 100x88 | wired |

### Factory State Asset Records


| Tag | Flag source and preview | Final flag paths | Leader source and preview | Leader portrait | Interface wiring | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `CFR` | `docs/assets/005_soviet_union_collapse/source_png/CFR_flag_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/CFR_flag.png` | `gfx/flags/CFR.tga`, `gfx/flags/medium/CFR.tga`, `gfx/flags/small/CFR.tga` | `docs/assets/005_soviet_union_collapse/source_png/CFR_leader_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/CFR_leader.png` | `gfx/leaders/005_soviet_collapse/CFR_leader.dds` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | wired with dedicated leader and idea icons |
| `MFR` | `docs/assets/005_soviet_union_collapse/source_png/MFR_flag_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/MFR_flag.png` | `gfx/flags/MFR.tga`, `gfx/flags/medium/MFR.tga`, `gfx/flags/small/MFR.tga` | `docs/assets/005_soviet_union_collapse/source_png/MFR_leader_source.png`, `docs/assets/005_soviet_union_collapse/processed_png/MFR_leader.png` | `gfx/leaders/005_soviet_collapse/MFR_leader.dds` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | wired with dedicated leader and idea icons |

`CFR_soviet_collapse_focus_tree` uses 47 focuses in `common/national_focus/005_soviet_collapse_factory_successors.txt`. The tree reuses the 33 existing `GFX_focus_CFR_*` sprites and their shine variants from `interface/005_soviet_collapse_factory_ancient_icons.gfx`; no new focus DDS files are required for this pass. The latest border-construction and reconstruction-protectorate focuses use previously unused CFR sprite keys already wired in the same `.gfx` file.

`MFR_soviet_collapse_focus_tree` uses 58 focuses in `common/national_focus/005_soviet_collapse_factory_successors.txt`. The tree reuses the 46 existing `GFX_focus_MFR_*` sprites and their shine variants from `interface/005_soviet_collapse_factory_ancient_icons.gfx`; no new focus DDS files are required for this pass.



### Returned Names Dynamic Host Asset Records

Returned Names decisions and ideas are active gameplay assets wired through existing Event 005 icon reuse in `interface/005_soviet_collapse_factory_ancient_icons.gfx`. The gameplay package is documented in `docs/events/005_soviet_collapse_returned_names_audit.md`. Final bespoke art can replace the referenced sprites later for the museum-cabinet, old-banner, toll-route, Sogdian, Khwarazmian, Alan, and anti-antiquarian concepts.

| Asset group | Sprite names | Status |
| --- | --- | --- |
| Returned Names category and decisions | `GFX_decision_category_soviet_collapse_returned_names`, `GFX_decision_soviet_collapse_open_museum_cabinets`, `GFX_decision_soviet_collapse_recruit_archivists`, `GFX_decision_soviet_collapse_commission_old_banner`, `GFX_decision_soviet_collapse_argue_khazar_toll_claim`, `GFX_decision_soviet_collapse_argue_sogdian_city_claim`, `GFX_decision_soviet_collapse_argue_khwarazmian_oasis_claim`, `GFX_decision_soviet_collapse_argue_alan_pass_claim`, `GFX_decision_soviet_collapse_reject_antiquarians` | placeholder reuse |
| Returned Names ideas | `GFX_idea_soviet_collapse_returned_names_pressure`, `GFX_idea_soviet_collapse_archivist_claim_council`, `GFX_idea_soviet_collapse_old_banner_mobilization` | placeholder reuse |

### Standalone Ancient Restoration Seed Assets

`KZR`, `SOG`, `KHW`, and `ALN` are wired as standalone Event 005 ancient-restoration seed tags. Their gameplay package is documented in `docs/events/005_soviet_collapse_returned_names_audit.md`. The current visual package deliberately uses placeholder reuse so the tags load with stable paths and sprite names while bespoke historical-symbol art remains pending.

| Asset surface | Current paths or sprite names | Status |
| --- | --- | --- |
| `KZR` flags | `gfx/flags/KZR.tga`, `gfx/flags/medium/KZR.tga`, `gfx/flags/small/KZR.tga` copied from `OGB` placeholder flags | placeholder reuse |
| `SOG` flags | `gfx/flags/SOG.tga`, `gfx/flags/medium/SOG.tga`, `gfx/flags/small/SOG.tga` copied from `TNC` placeholder flags | placeholder reuse |
| `KHW` flags | `gfx/flags/KHW.tga`, `gfx/flags/medium/KHW.tga`, `gfx/flags/small/KHW.tga` copied from `BSC` placeholder flags | placeholder reuse |
| `ALN` flags | `gfx/flags/ALN.tga`, `gfx/flags/medium/ALN.tga`, `gfx/flags/small/ALN.tga` copied from `MRC` placeholder flags | placeholder reuse |
| Ancient restoration portraits | `GFX_portrait_OGB_volga_restoration_council` is now OGB-specific final DDS reuse; `GFX_portrait_TNC_turkestan_civic_council`, `GFX_portrait_BSC_oasis_war_council`, and `GFX_portrait_MRC_mountain_republic_council` remain reused by three history files | partial placeholder reuse |
| Ancient restoration focus icons | `GFX_focus_soviet_collapse_ancient_*` and `_shine` variants in `interface/005_soviet_collapse_ancient_icons.gfx`, including the tag-gated `KZR`, `SOG`, `KHW`, and `ALN` branch sprites | unique sprite names with placeholder DDS reuse |

### Continuation Achievement Placeholder Asset Records

The continuation achievements are wired with stable DDS paths and placeholder reuse until bespoke final achievement art is created. The dedicated achievement icon manifest records all 40 Event 005 achievement icon rows; the rows below call out the remaining placeholder-reuse achievement assets that block final asset completion.

| Achievement | DDS paths | Interface wiring | Status |
| --- | --- | --- | --- |
| `chaosx_ach_concrete_republic` | `gfx/achievements/chaosx_ach_concrete_republic.dds`, `gfx/achievements/chaosx_ach_concrete_republic_grey.dds`, `gfx/achievements/chaosx_ach_concrete_republic_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_state_as_one_arms_order` | `gfx/achievements/chaosx_ach_state_as_one_arms_order.dds`, `gfx/achievements/chaosx_ach_state_as_one_arms_order_grey.dds`, `gfx/achievements/chaosx_ach_state_as_one_arms_order_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_southern_cascade` | `gfx/achievements/chaosx_ach_southern_cascade.dds`, `gfx/achievements/chaosx_ach_southern_cascade_grey.dds`, `gfx/achievements/chaosx_ach_southern_cascade_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_concrete_does_not_sleep` | `gfx/achievements/chaosx_ach_concrete_does_not_sleep.dds`, `gfx/achievements/chaosx_ach_concrete_does_not_sleep_grey.dds`, `gfx/achievements/chaosx_ach_concrete_does_not_sleep_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_every_order_a_rifle` | `gfx/achievements/chaosx_ach_every_order_a_rifle.dds`, `gfx/achievements/chaosx_ach_every_order_a_rifle_grey.dds`, `gfx/achievements/chaosx_ach_every_order_a_rifle_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_returned_names` | `gfx/achievements/chaosx_ach_returned_names.dds`, `gfx/achievements/chaosx_ach_returned_names_grey.dds`, `gfx/achievements/chaosx_ach_returned_names_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_deadline_state` | `gfx/achievements/chaosx_ach_deadline_state.dds`, `gfx/achievements/chaosx_ach_deadline_state_grey.dds`, `gfx/achievements/chaosx_ach_deadline_state_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_kronstadt_was_right` | `gfx/achievements/chaosx_ach_kronstadt_was_right.dds`, `gfx/achievements/chaosx_ach_kronstadt_was_right_grey.dds`, `gfx/achievements/chaosx_ach_kronstadt_was_right_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_file_that_became_country` | `gfx/achievements/chaosx_ach_file_that_became_country.dds`, `gfx/achievements/chaosx_ach_file_that_became_country_grey.dds`, `gfx/achievements/chaosx_ach_file_that_became_country_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_world_as_one_factory` | `gfx/achievements/chaosx_ach_world_as_one_factory.dds`, `gfx/achievements/chaosx_ach_world_as_one_factory_grey.dds`, `gfx/achievements/chaosx_ach_world_as_one_factory_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_every_port_a_council` | `gfx/achievements/chaosx_ach_every_port_a_council.dds`, `gfx/achievements/chaosx_ach_every_port_a_council_grey.dds`, `gfx/achievements/chaosx_ach_every_port_a_council_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_eastern_buffer_without_moscow` | `gfx/achievements/chaosx_ach_eastern_buffer_without_moscow.dds`, `gfx/achievements/chaosx_ach_eastern_buffer_without_moscow_grey.dds`, `gfx/achievements/chaosx_ach_eastern_buffer_without_moscow_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_when_archive_opens` | `gfx/achievements/chaosx_ach_when_archive_opens.dds`, `gfx/achievements/chaosx_ach_when_archive_opens_grey.dds`, `gfx/achievements/chaosx_ach_when_archive_opens_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_no_empty_borders` | `gfx/achievements/chaosx_ach_no_empty_borders.dds`, `gfx/achievements/chaosx_ach_no_empty_borders_grey.dds`, `gfx/achievements/chaosx_ach_no_empty_borders_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
| `chaosx_ach_the_world_read_the_telegram` | `gfx/achievements/chaosx_ach_the_world_read_the_telegram.dds`, `gfx/achievements/chaosx_ach_the_world_read_the_telegram_grey.dds`, `gfx/achievements/chaosx_ach_the_world_read_the_telegram_not_eligible.dds` | `interface/chaosx_achievements.gfx` | placeholder reuse |
