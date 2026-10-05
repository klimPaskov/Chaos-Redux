# Fallout survivor achievements

Baseline spec 06 lists ten achievement hooks for Fallout route mastery. Seven are implemented (agent decision A21); three wait for routes that do not exist yet. The New Zealand Lifeboat State has its own three achievements, documented in `docs/specs/air_cleanliness_fallout_specs/fallout_nzl_lifeboat_state_achievement_handoff.md`.

## How they work

Each achievement is registered in `common/achievements/chaos_redux_achievements.txt` in the Fallout section after the New Zealand achievements. Its `possible` block is always true, because a Fallout identity is created long after campaign start. Its `happened` block calls one completion trigger in `common/scripted_triggers/fallout_consolidated_triggers.txt`. Every completion trigger first calls `fallout_achievement_survivor_is_current`: a human, independent, uncapitulated country that is a current Fallout registry survivor with a loaded survival account, while Fallout is active and no transition is running. Thresholds live in `fallout_achievement` in `common/script_constants/fallout_consolidated_constants.txt`; the three collection counts are mirrored as file-scoped values next to the triggers because collection values reject script-constant tokens.

| Achievement | Route | Completion |
| --- | --- | --- |
| `chaosx_fallout_keep_the_lights_on` (Keep the Lights On) | Technate | Technate archetype, `fallout_generic_reopen_power_grid` completed, the grid engineer office made an institution (`fallout_institution_engineer_civic` or `_command`), Power at least 60, and no owned state with a failed reactor memory from the Air Winter (`air_winter_memory_reactor_scram_failed`, `_reduced_output_failed`, `_plant_council_failed`). |
| `chaosx_fallout_bread_for_the_black_sky` (Bread for the Black Sky) | Food Compact | Food Compact archetype, leader of an active Frontier Pact with at least 3 members carrying `fallout_generic_joined_frontier_pact` (the leader counts), Food at least 70, and Cohesion at least 70. |
| `chaosx_fallout_the_old_flag_still_flies` (The Old Flag Still Flies) | Continuity | Continuity Government archetype, the survival charter published or the USA Lakes Charter ratified, the Year Ten Order reached or the USA Federal Reconstruction Drive finished, and the capital is the country's own pre-Fallout capital (`fallout_pretransition_capital` with `fallout_pretransition_capital_country` equal to the country), owned and controlled. |
| `chaosx_fallout_crown_of_ruins` (Crown of Ruins) | Warlord | Warlord Command archetype, `fallout_generic_reclaim_the_heartland` completed and the heartland held (or the Year Ten Order reached), and at least 3 owned and controlled states graded Dead City or worse. |
| `chaosx_fallout_no_more_ground_zero` (No More Ground Zero) | Any | At least 4 owned and controlled states graded Dead City or worse in which the country restored a corridor or integrated the reclaimed state through the survivor mandate decisions. |
| `chaosx_fallout_last_seed` (The Last Seed) | Any | The flourishing seed-vault memory or the treaty seed archive memory applied at the survivor start, an owned and controlled seed vault or greenhouse refuge, Food at least 75, and Cohesion at least 50. |
| `chaosx_fallout_after_final_silence` (After the Final Silence) | Final Silence cause | The Fallout came from the Final Silence (`global.fallout_cause_memory_source` or `global.fallout_pretransition_request_source`), the government is neither a religious refuge nor a mutant polity, the tenth year since map return has begun, and Cohesion is at least 50. |

## Not implemented

- `fallout_no_empty_bunks` (Bunker): needs a shelter riot mechanic and a population growth measure in the Fallout; neither exists.
- `fallout_new_species_order` (Mutant polity): needs the mutant late-game route and a recognition mechanic from human states.
- `fallout_the_sea_roads_open` (Maritime): needs a port compact that can span three regions; the Frontier Pact invitation only reaches neighbours in the same region.

## Icons

Each achievement has three 64x64 DDS states in `gfx/achievements/`: `<id>.dds`, `<id>_grey.dds`, and `<id>_not_eligible.dds`. They are registered as `GFX_achievement_<id>`, `GFX_achievement_<id>_grey`, and `GFX_achievement_<id>_not_eligible` in `interface/fallout_consolidated.gfx`. Each icon comes from one native-transparency ImageGen medallion subject, built into the three states and composited onto the skill achievement templates with `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`, which audited every triplet. Prompts, sources, layers, and review sheets are in `docs/assets/air_cleanliness_fallout/achievements/` while the Fallout asset work is active. The icons still need parent or user visual review.

Provenance (the workspace under `docs/assets/` is local and not tracked):

- Source mode: native ImageGen through the `gptimage` MCP route, one new generation per achievement, no edits, native transparent background (zero-alpha corners verified, no background removal).
- Prompt frame: a Hearts of Iron IV achievement subject inside an aged bronze laurel medallion (dark iron for Crown of Ruins, silver-grey for After the Final Silence) filling about 90 percent of a transparent canvas, gritty 1940s painterly texture, readable at 64x64, with no text, square backing, frame plate, or red cross.
- Subjects: a power pylon with one lit bulb over a ruined skyline; a bread loaf, wheat sheaf, and four ration bowls under a black sky; a plain tattered flag without emblem over a ruined domed government building; an iron crown shaped from broken skyscrapers on rubble; a green sapling in a scorched crater beside a repaired road; a sealed seed jar with one sprout in a stone vault; a gloved hand holding a lantern before a black eclipsed sun over a silent city with a fallen bell.
- Layers: alpha bounding box resized with Lanczos into a centred 60x60 footprint on 64x64; grey state by luma conversion with alpha kept; not-eligible state by compositing the unchanged skill overlay over the grey state.
- Known readability note: at 64x64 the eclipse and the fallen bell in After the Final Silence read as two dark circles beside the lantern.

## Localisation

`localisation/english/fallout_consolidated_l_english.yml` holds `<id>_NAME`, `<id>_DESC`, `<id>_tooltip`, and the shared `chaosx_fallout_achievement_eligible_tooltip`.

## Future plans

1. Add the three missing routes and their achievements: a shelter riot and population growth layer for bunker authorities, the mutant late-game route, and a cross-region maritime port compact.
2. Let Crown of Ruins require that one of the dead cities was another government's pre-Fallout capital once the heartland targets favour fallen capitals.
3. Give After the Final Silence a reading of the Holy Realm memory so successors that kept the faith but rejected the cult can still qualify.
