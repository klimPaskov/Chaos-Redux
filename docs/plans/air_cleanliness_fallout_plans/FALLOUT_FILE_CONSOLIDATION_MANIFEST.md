# Fallout runtime file consolidation manifest

This manifest records the mechanical consolidation of Fallout and Air Cleanliness runtime sources.
Each loader directory has one consolidated file with source blocks retained in lexical filename order.
Identifiers, event ids, localisation keys, asset paths, and namespaces were not renamed.

| Loader surface | Destination | Sources | Source bytes | Output bytes |
| --- | --- | ---: | ---: | ---: |
| `common/ai_strategy_plans` | `fallout_consolidated_ai.txt` | 2 | 7,832 | 8,644 |
| `common/characters` | `fallout_consolidated_characters.txt` | 1 | 511 | 1,093 |
| `common/countries` | `fallout_consolidated_countries.txt` | 1 | 647 | 1,226 |
| `common/country_leader` | `fallout_consolidated_leader_traits.txt` | 1 | 2,283 | 2,868 |
| `common/decisions` | `fallout_consolidated_decisions.txt` | 5 | 120,335 | 121,859 |
| `common/decisions/categories` | `fallout_consolidated_categories.txt` | 3 | 1,662 | 2,750 |
| `common/dynamic_modifiers` | `fallout_consolidated_dynamic_modifiers.txt` | 106 | 261,517 | 289,848 |
| `common/ideas` | `fallout_consolidated_ideas.txt` | 2 | 9,765 | 10,562 |
| `common/national_focus` | `fallout_consolidated_focus.txt` | 2 | 37,187 | 38,002 |
| `common/on_actions` | `fallout_consolidated_on_actions.txt` | 3 | 5,695 | 6,753 |
| `common/opinion_modifiers` | `fallout_consolidated_opinion_modifiers.txt` | 27 | 23,131 | 30,370 |
| `common/script_constants` | `fallout_consolidated_constants.txt` | 99 | 1,280,751 | 1,306,306 |
| `common/scripted_effects` | `fallout_consolidated_effects.txt` | 123 | 10,553,738 | 10,585,679 |
| `common/scripted_guis` | `fallout_consolidated_scripted_gui.txt` | 2 | 1,712 | 2,554 |
| `common/scripted_localisation` | `fallout_consolidated_scripted_localisation.txt` | 106 | 506,708 | 536,932 |
| `common/scripted_triggers` | `fallout_consolidated_triggers.txt` | 114 | 2,007,965 | 2,037,891 |
| `interface` | `fallout_consolidated.gfx` | 4 | 41,413 | 42,634 |
| `interface` | `fallout_consolidated.gui` | 2 | 1,209 | 1,990 |
| `localisation/english` | `fallout_consolidated_l_english.yml` | 113 | 1,314,723 | 1,341,719 |
| `events` | `fallout_world_end_events.txt` | 2 | 1,402,058 | 1,402,801 |

The source files are intentionally not retained as compatibility stubs because Clausewitz loads every file in these directories and the consolidated files preserve the same top-level blocks.
The event catalog workbook and exports contain no Fallout event rows after this pass. Fallout remains internal consequence content rather than an event catalog registration.
The following remain separate by design: event pictures and their manifests, source art, documentation, shared non-Fallout routing files, and the existing normal-map and blackout assets.
The direct Fallout event-picture root remains `gfx/event_pictures/fallout`.
