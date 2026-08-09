# Event 012 W5 certification fix handoff

Date: 2026-08-09

Owner: `chaosx_scripted_system_architect` (`/root/world_w5_certification_fix`)

Status: Source implementation complete for the bounded W5 and terminal presentation registrars. This handoff does not claim full Event 012 completion or live-save acceptance.

## Files changed

- `common/scripted_triggers/012_africa_world_order_triggers.txt`
- `common/scripted_effects/012_africa_world_order_effects.txt`
- `docs/events/012_africa/world_order.md`
- `docs/events/012_africa/overview.md`

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `africa_world_package_candidate_runtime_base_is_valid` | Country scope; current candidate runtime state | Pure live-sovereign, controlled-capital, non-African, non-successor proof | `africa_world_candidate_runtime_surfaces_are_registered` |
| `africa_world_candidate_runtime_surfaces_are_registered` | Country scope; candidate flag, continent id, and seven mapped country receipts | Pure continent-specific seven-surface proof | W5 all-package trigger and candidate receipt mapper guard |
| `africa_world_register_current_candidate_runtime_receipts` | Candidate scope; frozen continent id | Writes only the seven explicit country receipt flags for the mapped package | `africa_world_register_package_surface_receipts` array loop |
| `africa_world_terminal_super_event_runtime_surfaces_are_registered` | Host scope; four role receipt sets | Pure twenty-receipt proof for slots 101-104, audio ids 58-61, images, text, and runtime consumers | `africa_world_certify_terminal_super_event_runtime_surfaces` |
| `africa_world_register_terminal_super_event_runtime_surfaces` | Host scope; explicit Event 012 source mapping | Writes only the four role-specific five-flag receipt sets | Scramble opening before the terminal setter |
| `africa_world_certify_terminal_super_event_runtime_surfaces` | Host scope; terminal role trigger | Writes `africa_the_world_super_event_package_ready` only after the pure trigger passes | Scramble opening after the terminal registrar |

## Before and after proof

Before this change, `africa_world_register_package_surface_receipts` unconditionally wrote seven global flags (`africa_world_package_*_surfaces_registered`). `africa_world_review_runtime_surface_registry` and `africa_world_certify_all_package_runtime_surfaces` then accepted those host-wide flags, so the Scramble opening could certify its own prerequisites without a receipt on any candidate.

After this change, `africa_world_register_package_surface_receipts` iterates the frozen `africa_world_package_candidates` array and calls `africa_world_register_current_candidate_runtime_receipts`. The mapper has six explicit continent branches and writes seven country flags only on the candidate whose `africa_world_continent_id` selects that branch. `africa_world_candidate_runtime_surfaces_are_registered` requires the candidate-owned seven-flag set plus live, non-capitulated, sovereign, controlled-capital, non-African, non-successor, non-exile, non-breakup, non-terminal, non-chaos proof.

`africa_world_all_package_runtime_surfaces_are_certified` now rejects any array member without that trigger and requires exactly six candidates, one each for Middle East, Europe, Asia, North America, South America, and Oceania. The review effect only records `africa_world_package_runtime_surfaces_reviewed` after this trigger succeeds. The atomic setter then grants `africa_world_package_implementation_ready` to all six array members and records `africa_world_package_runtime_surfaces_certified`; no package installation, focus completion, tag creation, identity mutation, or territory mutation was added. Existing successor transfer still copies `africa_world_package_implementation_ready` in `africa_world_commit_package_successor`.

## Exact continent/package receipt mapping

| Continent | Route/protocol source receipts | Focus | Decision | Idea | AI | Identity | Localisation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Middle East | `africa_crossroads_apply_command_settlement`, `africa_crossroads_apply_red_sea_nile_treaty` in `common/scripted_effects/012_africa_world_crossroads_europe_effects.txt` | `africa_middle_east_convene_crossroads_balance` in `common/national_focus/012_africa_world_middle_east_focus.txt` | `africa_crossroads_convene_mandate_exit_board` in `common/decisions/012_africa_decisions.txt` | `africa_world_middle_east_founding_problem` in `common/ideas/012_africa_world_order_ideas.txt` | `africa_ai_profile_world_middle_east_is_active`; `africa_world_middle_east_arab_federal_focus_plan` in Event 012 AI sources | `africa_world_finalize_distinct_package_identity` maps Middle East route flags to the defined cosmetic identities | `africa_middle_east_world_focus_tree` and package idea keys in `localisation/english/012_africa_world_order_l_english.yml` |
| Europe | `africa_europe_apply_common_defence_law`, `africa_europe_apply_withdrawal_crisis_law` in `common/scripted_effects/012_africa_world_crossroads_europe_effects.txt` | `africa_europe_convene_continental_settlement` in `common/national_focus/012_africa_world_europe_focus.txt` | `africa_europe_arbitrate_border_and_minority_guarantees` in `common/decisions/012_africa_decisions.txt` | `africa_world_europe_founding_problem` in `common/ideas/012_africa_world_order_ideas.txt` | `africa_ai_profile_world_europe_is_active`; `africa_world_europe_democratic_federation_focus_plan` in Event 012 AI sources | `africa_world_finalize_distinct_package_identity` maps Europe route flags to the defined cosmetic identities | `africa_europe_world_focus_tree` and package idea keys in `localisation/english/012_africa_world_order_l_english.yml` |
| Asia | `africa_asia_apply_food_river_monsoon_board`, `africa_asia_apply_rail_maritime_corridors` in `common/scripted_effects/012_africa_world_asia_north_america_effects.txt` | `africa_asia_convene_regional_congresses` in `common/national_focus/012_africa_world_asia_focus.txt` | `africa_asia_seat_the_regional_centres` in `common/decisions/012_africa_decisions.txt` | `africa_world_asia_founding_problem` in `common/ideas/012_africa_world_order_ideas.txt` | `africa_ai_profile_world_asia_is_active`; `africa_world_asia_plural_federation_focus_plan` in Event 012 AI sources | `africa_world_finalize_distinct_package_identity` maps Asia route flags to the defined cosmetic identities | `africa_asia_world_focus_tree` and package idea keys in `localisation/english/012_africa_world_order_l_english.yml` |
| North America | `africa_north_america_negotiate_caribbean_central_membership`, `africa_north_america_balance_industry_mobility_command` in `common/scripted_effects/012_africa_world_asia_north_america_effects.txt` | `africa_north_america_convene_continental_bargain` in `common/national_focus/012_africa_world_north_america_focus.txt` | `africa_north_america_negotiate_caribbean_and_central_membership` in `common/decisions/012_africa_decisions.txt` | `africa_world_north_america_founding_problem` in `common/ideas/012_africa_world_order_ideas.txt` | `africa_ai_profile_world_north_america_is_active`; `africa_world_north_america_republics_focus_plan` in Event 012 AI sources | `africa_world_finalize_distinct_package_identity` maps North American route flags to the defined cosmetic identities | `africa_north_america_world_focus_tree` and package idea keys in `localisation/english/012_africa_world_order_l_english.yml` |
| South America | `africa_south_america_apply_resource_and_debt_law_w2`, `africa_south_america_apply_defence_and_corridors_w2` in `common/scripted_effects/012_africa_world_south_america_oceania_effects.txt` | `africa_south_america_convene_three_regions_balance` in `common/national_focus/012_africa_world_south_america_focus.txt` | `africa_south_america_balance_the_three_regions` in `common/decisions/012_africa_decisions.txt` | `africa_world_south_america_founding_problem` in `common/ideas/012_africa_world_order_ideas.txt` | `africa_ai_profile_world_south_america_is_active`; `africa_world_south_america_republics_focus_plan` in Event 012 AI sources | `africa_world_finalize_distinct_package_identity` maps South American route flags to the defined cosmetic identities | `africa_south_america_world_focus_tree` and package idea keys in `localisation/english/012_africa_world_order_l_english.yml` |
| Oceania | `africa_oceania_apply_constitution_and_withdrawal_law_w2`, `africa_oceania_apply_pacific_defence_and_disaster_reserve_w2` in `common/scripted_effects/012_africa_world_south_america_oceania_effects.txt` | `africa_oceania_convene_ocean_network` in `common/national_focus/012_africa_world_oceania_focus.txt` | `africa_oceania_seat_the_island_congress` in `common/decisions/012_africa_decisions.txt` | `africa_world_oceania_founding_problem` in `common/ideas/012_africa_world_order_ideas.txt` | `africa_ai_profile_world_oceania_is_active`; `africa_world_oceania_maritime_federation_focus_plan` in Event 012 AI sources | `africa_world_finalize_distinct_package_identity` maps Oceanian route flags to the defined cosmetic identities | `africa_oceania_world_focus_tree` and package idea keys in `localisation/english/012_africa_world_order_l_english.yml` |

The seven receipt flags are continent-qualified country flags such as `africa_world_candidate_middle_east_route_protocol_receipt` through `africa_world_candidate_middle_east_localisation_receipt`; the trigger and mapper contain the equivalent seven-flag set for each of the other five continents.

## Separate four-role terminal presentation registrar

`africa_world_register_terminal_super_event_runtime_surfaces` maps these exact source-backed role receipts. `africa_world_terminal_super_event_runtime_surfaces_are_registered` evaluates all twenty receipts, and `africa_world_certify_terminal_super_event_runtime_surfaces` is the only readiness writer in this path.

| Role | Slot | Audio id and runtime definitions | Image registration | Localisation/text records | Runtime consumer |
| --- | --- | --- | --- | --- | --- |
| Africa Is One | 101 | `africa_world_super_event.africa_is_one_slot` / `africa_world_super_event.africa_is_one_audio` resolve to id 58; `chaosx_super_event_africa_is_one_track` and `chaosx_super_event_58_sound_*` in `sound/chaosx_sound.asset` | `GFX_super_event_012_africa_africa_is_one` to `gfx/super_events/012_africa/super_event_012_africa_africa_is_one.dds` in `interface/012_africa_event_pictures.gfx` | `chaosx_super_event.101.t/q/a/d` plus the 101 image/title/quote/remark/description selectors in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` | `africa_world_emit_africa_is_one_super_event` |
| Scramble Response | 102 | `africa_world_super_event.scramble_response_slot` / `africa_world_super_event.scramble_response_audio` resolve to id 59; `chaosx_super_event_scramble_response_track` and `chaosx_super_event_59_sound_*` | `GFX_super_event_012_africa_scramble_response` to `gfx/super_events/012_africa/super_event_012_africa_scramble_response.dds` | `chaosx_super_event.102.t/q/a/d` plus the 102 scripted selectors | `africa_world_emit_scramble_response_super_event` |
| Continental Wars | 103 | `africa_world_super_event.continental_wars_slot` / `africa_world_super_event.continental_wars_audio` resolve to id 60; `chaosx_super_event_continental_wars_track` and `chaosx_super_event_60_sound_*` | `GFX_super_event_012_africa_continental_wars` to `gfx/super_events/012_africa/super_event_012_africa_continental_wars.dds` | `chaosx_super_event.103.t/q/a/d` plus the 103 scripted selectors | `africa_world_emit_continental_wars_super_event` |
| The World | 104 | `africa_world_super_event.the_world_slot` / `africa_world_super_event.the_world_audio` resolve to id 61; `chaosx_super_event_the_world_track` and `chaosx_super_event_61_sound_*` | `GFX_super_event_012_africa_the_world` to `gfx/super_events/012_africa/super_event_012_africa_the_world.dds` | `chaosx_super_event.104.t/q/a/d` plus the 104 scripted selectors | `africa_world_emit_the_world_super_event` |

The four role source files, image paths, sound files, sound definitions, localisation keys, and scripted-localisation consumers were present in the static audit. If a role loses any required surface, its mapping must be removed or corrected and the trigger will leave `africa_the_world_super_event_package_ready` unset; no fallback role is provided.

## Validation and evidence

- Static identifier audit resolved every mapped focus, decision, idea, AI trigger/plan, identity helper, localisation key, super-event sprite, sound track, and role consumer.
- File audit found all four Event 012 super-event DDS files and all four WAV files at the exact paths above.
- The source no longer writes the seven unconditional host-wide W5 receipt flags. `africa_world_package_runtime_surfaces_reviewed` and `africa_world_package_runtime_surfaces_certified` remain downstream of the candidate trigger and review/setter sequence.
- The only Scramble-opening writer for `africa_the_world_super_event_package_ready` is now `africa_world_certify_terminal_super_event_runtime_surfaces`, after the separate role registrar and trigger.
- `hoi4.event_inspect` trace for the actual Scramble opening event `chaosx.nr12.309` was rerun after the patch with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9c9e33fc65fdc752d5ab8e8e092db0e216562d7a5c0ea706a1bf64be0d222c5/f1d31f864a87ce26ee5c3fbc1f8cb74f40f8092aa260b7555937d171ca9e9842/event-trace-08357425bddf.json`; the MCP response was partial because inline files were truncated, so the source audit remains decisive for these helper edits.
- `hoi4.probability_inspect` was run against `common/ai_strategy_plans/012_africa_focus_plans.txt` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f31d37def553826e97825e23538425469bed9bbf0a925e7b1b99abba15e745b2/4e56f659977c0f0eba30423fcfa04af2ccab03429183d5311183e06e568d65ce/probability-inspect-812d67ea2457.json`; no weighted value was changed.
- No HOI4 process was launched. Live event, save, and asset playback acceptance remains with the parent/user.

## Limitations and blockers

The Clausewitz trigger language cannot introspect whether a source file, sprite, sound asset, or localisation key exists on disk at runtime. The registrar therefore uses explicit source-owned mappings, with the referenced definitions verified in this handoff and in the repository audit. This is not a generic receipt or fallback; removing a missing role mapping leaves the atomic trigger unsatisfied. No current mapped continent or terminal role has a static source blocker.

The MCP event trace was partial due server inline-file truncation, and no live-save acceptance was attempted. No weighted values were changed, so no probability compare pass was required.
