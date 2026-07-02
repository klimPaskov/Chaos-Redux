# Source review manifest for Event 17 planning

This manifest records the project files available in `/mnt/data` that were read before writing the Event 17 planning package. The package was created from the uploaded project source files, the uploaded CSV catalog rows, the uploaded subagent TOML files, and the required spreadsheet skill instructions. No gameplay repository checkout, offline Paradox wiki snapshot, vanilla HOI4 folder, or actual Codex subagent runtime was available in this chat environment.

| File | Kind | Bytes | Lines | Words | SHA-256 prefix |
| --- | --- | ---: | ---: | ---: | --- |
| `AGENTS.md` | text | 33825 | 400 | 4811 | `07c0a22711699c6e` |
| `CHAOS_REDUX_MECHANICS.md` | text | 44359 | 973 | 6190 | `fb4ed4ab5894c5c9` |
| `chaos-redux-event-assets.md` | text | 54245 | 1038 | 7864 | `059ba78e37912742` |
| `chaos-redux-event-planning.md` | text | 131350 | 1771 | 19185 | `fa145bb0d3c9a97f` |
| `chaos-redux-events.md` | text | 53008 | 696 | 7144 | `3544341fa09d7a80` |
| `chaos-redux-frame-animation.md` | text | 23669 | 483 | 3609 | `6a4e68dc4e5a89f0` |
| `chaos-redux-improvement-loop.md` | text | 24080 | 275 | 3576 | `7e137b6135c335e4` |
| `chaos-redux-subagents.md` | text | 19124 | 288 | 2607 | `1d155c650f16f6c4` |
| `chaos-redux-super-events.md` | text | 30134 | 790 | 4538 | `1fabb5d93da37703` |
| `chaos_redux_clusters_catalog.csv` | text | 1721 | 15 | 192 | `6d21ad63a942c17e` |
| `chaos_redux_events_catalog.csv` | text | 56282 | 1035 | 6926 | `8c669b51f762ec29` |
| `chaos_redux_scenarios_catalog.csv` | text | 3660 | 20 | 455 | `e972443ca43849b3` |
| `chaosx_asset_source_researcher.toml` | text | 3847 | 56 | 539 | `421793129a5a846c` |
| `chaosx_country_package_auditor.toml` | text | 6614 | 82 | 916 | `78b510c8425f0883` |
| `chaosx_decision_mission_auditor.toml` | text | 4608 | 79 | 665 | `48fa04a9100b85f1` |
| `chaosx_documentation_curator.toml` | text | 8395 | 120 | 1171 | `86145139edca0e58` |
| `chaosx_event_completion_auditor.toml` | text | 2956 | 50 | 410 | `57668b3c57069268` |
| `chaosx_focus_tree_auditor.toml` | text | 3646 | 76 | 530 | `36afd9e6d67b98be` |
| `chaosx_generated_event_art.toml` | text | 5856 | 66 | 818 | `61bdcfac345f3bb7` |
| `chaosx_icon_artist.toml` | text | 7170 | 88 | 981 | `b75b6f1e18e8469c` |
| `chaosx_improvement_loop_planner.toml` | text | 6345 | 58 | 893 | `f438da1473185ad8` |
| `chaosx_localisation_auditor.toml` | text | 4163 | 74 | 581 | `79ffbeddb6683c83` |
| `chaosx_repo_explorer.toml` | text | 11817 | 231 | 1806 | `9bde006e5add9c9f` |
| `chaosx_scripted_system_architect.toml` | text | 4565 | 71 | 636 | `62406e456ed972e9` |
| `chaosx_skill_maintainer.toml` | text | 3236 | 44 | 478 | `13d693a536b5225c` |
| `chaosx_spreadsheet_doc_worker.toml` | text | 3947 | 55 | 541 | `712d05bf76de9b49` |
| `chaosx_super_event_audio_researcher.toml` | text | 3314 | 65 | 500 | `ea374f776aabaa3e` |
| `chaosx_super_event_text_researcher.toml` | text | 3902 | 62 | 569 | `5d466a4d0e7a217c` |
| `hoi4-decisions-missions.md` | text | 40087 | 864 | 5903 | `369db0c2785ec2f0` |
| `hoi4-focus-trees.md` | text | 38682 | 837 | 5688 | `6b8dfb504b3eec14` |

## Direct catalog baseline used

The uploaded event catalog row for ID `17` identifies the old name as `Choose faction`, the old detail as `Random minor not in a faction will join the Axis or the Comintern.`, the type as `Minor Repeatable`, and the status as `To Be Reworked`.

The user-provided task renames the event to `Random faction` and expands the premise so that an eligible minor, including the player when selected, must choose or be assigned a faction from the factions that actually exist in the world.
