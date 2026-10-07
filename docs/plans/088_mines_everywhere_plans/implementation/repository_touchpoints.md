# Repository reconnaissance and intended edit boundaries

Connected repository: `klimPaskov/Chaos-Redux`.
Inspected revision: `33b6946dd923b9fc90fbf29bc5798dce3c76a76f`.
This is bounded reconnaissance. The full repository and all current shared implementations were not read.

## Actually observed

| Surface | Evidence and limitation | Required disposition |
| --- | --- | --- |
| `events/088_mines.txt` | Full connected file read. Namespace `chaosx.nr88`, entry `.1`, generic minelaying picture. Option chooses one random sea and loops countries through a meta-effect `add_mines` call | Preserve public entry compatibility where safe, replace one-region option mutation with the global committed incident |
| `localisation/english/088_mines_l_english.yml` | Connected search excerpt contains the title, one-random-region description and acknowledgment | Rewrite from Part 4 after mechanics are implemented. Do not copy the old description |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | Connected search confirms `get_random_sea_region` has a curated random list. Full helper registry text was supplied and read | Remove Event 088's dependency on random selection. Delete or alter the shared helper only after a complete caller audit |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | Search excerpt describes `add_mines` as adding mines for the current country | Consult full relevant current docs and installed vanilla before treating the call as verified |
| `docs/systems/event_system/event_clusters.md` | Connected excerpt has Sudden Abundance with Event 032 included, unlike supplied cluster export | Preserve unrelated membership. Reconcile through runtime and XLSX authority |
| Supplied event CSV, row 88 | Description is unrelated technology sharing and cluster cell is blank | Correct only through the actual workbook after runtime wording exists |

An older Event 029 plan refers to a `meta_add_mines` implementation. The fully read current Event 088 file uses an inline `meta_effect` containing `add_mines`. The direct file is the stronger evidence. Do not treat an old audit's shorthand as an existing helper API.

## Skill-identified integration surfaces, not fully inspected here

| Surface | Responsibility |
| --- | --- |
| `common/scripted_effects/chaosx_logic_effects.txt` | Category registration, event type, timer and fired-event accounting |
| `common/scripted_effects/chaosx_settings_effects.txt` | Generic firing and settings-owned dispatch paths |
| `common/scripted_effects/chaosx_events_log_effects.txt` | Shared history, event details, actor mapping and display records |
| `common/script_constants/event_cluster_constants.txt` | Existing cluster and member attribute constants |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | Cluster definitions, membership, aligned arrays, availability, shared state |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | Shared event and cluster detail selectors |
| `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` | Debug event name mapping |
| `localisation/english/chaosx_event_names_l_english.yml` | Shared event names |
| `localisation/english/chaosx_events_l_english.yml` | Shared event text as appropriate to current ownership |
| `localisation/english/chaosx_gui_l_english.yml` | Shared interface and cluster text |
| `common/achievements/chaos_redux_achievements.txt` | Single root achievement registry, Event 088 group |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Sole editable catalog authority |
| `.tools/export_event_catalog_csv.py` | Export-only mirror refresh |

Inspect exact current functions before choosing edits. Do not create a competing log, copy shared arrays into the event, or move unrelated GUI behavior into the event's worker scope.

## Proposed event-owned additions

Event-local effects, triggers and constants may use the `088_mines_everywhere` file stem where the repository conventions allow it. Their exact identifiers remain pending a collision and current-pattern inspection. Keep temporary inputs, scope, side effects, and lifetime documented.

A reusable complete-map provider, if actually feasible, should be neutral and documented in the shared helper registry only if it is genuinely a shared capability. Event-only bookkeeping should remain event-owned. Do not generalize the existing random helper by changing its semantics for all callers.

Final report art may live under `gfx/event_pictures/088_mines_everywhere/`, pending the actual consumer inspection. Achievement DDS files belong in the existing root `gfx/achievements/` namespace with the verified registry key and variant suffixes. Source artwork and QA evidence do not belong in runtime paths.

## Scope discipline

This planning task changed none of the above files. The provided package is new Markdown, JSON and a model test harness. No connected writes were performed. The future implementation must retain unrelated work and inspect the live checkout rather than overwriting it from this snapshot.
