# Event 006 small localisation continuation merge — 2026-08-25

## Scope

This source-layout pass removes three small localisation fragments whose keys already belong to an existing Event 006 receiver: IW-043/IW-058 category strings join the package country-core file, Transcaucasus blocked-cost companions join the package localisation, and super-event/history strings join the shared Event 006 localisation.

No executable source changed. The merge does not alter event reachability, decision costs, category registration, scripted-localisation names, package admission, or super-event dispatch.

## Preservation evidence

The receiver files retain all 21 parsed IW-043/IW-058 category key/value pairs, all 30 parsed Transcaucasus cost companion key/value pairs, and all 25 parsed super-event/history key/value pairs from the removed fragments. The only omitted line from each source is its `l_english:` root, because each receiver already has exactly one root.

Each receiver retains the UTF-8 BOM (`EF BB BF`) and exactly one `l_english:` root. A duplicate-key scan found no duplicate localisation keys in the three receivers, and a source-to-receiver comparison found no missing or changed key/value entries.

## Changed paths

- `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`
- `localisation/english/006_independence_wave_transcaucasus_l_english.yml`
- `localisation/english/006_independence_wave_l_english.yml`
- removed `localisation/english/006_independence_wave_iw043_iw058_categories_l_english.yml`
- removed `localisation/english/006_independence_wave_transcaucasus_costs_l_english.yml`
- removed `localisation/english/006_independence_wave_super_event_l_english.yml`

## Validation boundary

This is a static source-layout consolidation only. It does not claim live game localisation rendering, event-log presentation, scripted-GUI acceptance, or save/load evidence.
