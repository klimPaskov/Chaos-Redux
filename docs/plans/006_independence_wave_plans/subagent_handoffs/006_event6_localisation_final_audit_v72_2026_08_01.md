# Event 006 final localisation audit v72

Date: 2026-08-01

Scope: read-only localisation audit of the currently implemented Independence Wave package, including event titles and descriptions, decisions and cost text, focuses and ideas, country package names, event-log evolution surfaces, scenario 008 UI, super-event strings, scripted localisation, and the spreadsheet/catalog mirror.

Disposition: the implemented Event 006 localisation source is PASS for key coverage, duplicate-key hygiene, encoding, scripted-localisation references, dynamic-value coverage, and catalog wording alignment. Full runtime/UI completion remains PARTIAL because live game rendering and event-log interaction were not run by this subagent, and the intentionally inert reserved tags are not meant to receive country-package names.

## Audited surfaces

- The Event 006 English package contains 45 `localisation/english/006_*_l_english.yml` files and 6,353 parsed entries.
- The Event 006 package has 6,353 unique keys with no duplicate groups; the combined scan with `localisation/english/chaosx_gui_l_english.yml` and `localisation/english/chaosx_event_names_l_english.yml` found 7,358 entries and no duplicate groups.
- All 45 Event 006 localisation files begin with the required UTF-8 BOM bytes `EF BB BF`.
- Working-label detection found no player-facing `TODO`, `FIXME`, `placeholder`, `WIP`, `TBD`, `debug`, prompt, test, or replacement labels; hits for words such as 'process' describe in-world statehood or charter processes.
- Direct event localisation references in the 10 `events/006_*.txt` files resolved completely: 435 references, 435 unique keys, and 0 missing keys.
- Direct decision and scripted-button localisation references in `common/decisions/**/006_*.txt` resolved completely: 1,564 references, 1,266 unique keys, and 0 missing keys after restricting the check to player-facing name, description, tooltip, cost, and custom-cost fields.
- Focus custom-effect tooltip references resolved completely: 318 references, 318 unique keys, and 0 missing keys.
- Event 006 scripted-localisation `localization_key` references resolved completely: 111 references, 105 unique keys, and 0 missing keys.
- Event 006 custom-effect tooltip references resolved completely: 949 references, 882 unique keys, and 0 missing keys.
- The 236 Event 006 idea identifiers all have matching `_desc` localisation; no idea name/description pair is missing.
- The 319 Event 006 focus identifiers have matching focus names; the only absent description is the intentional root focus-tree description `independence_wave_focus_tree_desc` at `common/national_focus/006_independence_wave_focus.txt:25`.
- The 85 active Event 006 country packages have complete expected name, definition-name, adjective, and ideology-variant localisation pairs; 0 active package-name pairs are missing.
- The 17 unresolved reservations `DJX`, `DMX`, `DNX`, `ENX`, `EXX`, `EYX`, `FPX`, `GDX`, `GGX`, `GHX`, `GLX`, `HHX`, `HMX`, `HQX`, `HTX`, `HWX`, and `HXX` remain intentionally inert and fail closed without package names.
- The CAT overlay package uses the existing vanilla CAT tag and has its route-specific strings installed; no CAT localisation blocker was found.
- Evolution titles, bodies, type, and summary keys in `localisation/english/006_independence_wave_evolutions_l_english.yml` resolve through the event-log scripted localisation helpers.
- Evolution incident events `chaosx.nr6.360` through `chaosx.nr6.364` have complete title, description, and option localisation in `localisation/english/006_independence_wave_evolution_incidents_l_english.yml`.
- The Event 006 event-log helpers map all five evolution stages through `independence_wave.evolution.{1..5}.title` and `independence_wave.evolution.{1..5}.body`; the type and summary helpers are also present and use the configured evolution constants.
- Scenario 008 strings in `localisation/english/006_independence_wave_scenario_l_english.yml` cover the name, description, eight mode names, four intensity impacts, launch-state text, triggerable scenario event 80, ledger category/navigation, package identifier, and rejection reasons.
- The super-event strings in `localisation/english/006_independence_wave_super_event_l_english.yml` are present for the wired Event 006 super-event surface.

## Required issue lists

### Missing key list

No missing player-facing Event 006 localisation keys were found in the implemented event, decision, focus-tooltip, scripted-localisation, evolution, incident, scenario, or super-event surfaces.

`independence_wave_focus_tree_desc` is the sole absent focus-tree description key, and it is an intentional root focus-tree description omission rather than a missing focus name or runtime tooltip.

The 17 reserved tags listed above are intentionally inert reservations and are not missing active country package names.

### Duplicate key list

No duplicate localisation keys were found in the 45 Event 006 localisation files.

No duplicate groups were found in the combined Event 006 plus shared GUI/event-name scan.

### Scripted localisation issue list

No unresolved `localization_key` references, custom-effect tooltip references, or event-log evolution title/body references were found.

No raw implementation constants or phase numbers were found in the audited event-details, event-log, GUI, or scenario strings where the existing dynamic getters already provide player-facing values.

### Dynamic text opportunities

- Existing dynamic coverage is appropriate for the major surfaces: event report counts and rival/host/network getters, GUI phase and ledger getters, scenario outcome/type/intensity/territory/force values, and constant-backed costs use formatted dynamic values.
- The CAT route effect summaries in `localisation/english/006_independence_wave_catalonia_l_english.yml` remain static summaries in keys such as `independence_wave_cat_project_failure_effect_tt`, `independence_wave_cat_depots_effect_tt`, `independence_wave_cat_guards_effect_tt`, `independence_wave_cat_assembly_effect_tt`, `independence_wave_cat_host_ledgers_effect_tt`, `independence_wave_cat_route_effect_tt`, `independence_wave_cat_patron_route_effect_tt`, `independence_wave_cat_sovereignty_effect_tt`, and `independence_wave_cat_network_effect_tt`.
- Those CAT summaries could optionally expose the relevant constant-backed magnitudes if the owning gameplay pass wants more numerical feedback; this is a UX enhancement, not a coverage defect, and no patch was made in this audit.

### Cross-surface mismatch notes

- The shared Event Details key `chaosx.events_log.window.event_details.independence_wave` is premise-only and exactly matches the Event 006 catalog Details field, including the two dynamic rival-bloc getters.
- Each catalog evolution title/body exactly matches the corresponding localisation key `independence_wave.evolution.{1..5}.title/body`.
- The workbook Events row for Event ID 6 exactly matches the exported CSV and the Event Details/evolution localisation values.
- Scenario SCN-008 name, description, mode names, and impact bodies exactly match the corresponding scenario localisation; the CSV intensity labels are presentation prefixes only and the body text matches after stripping those labels.
- The current punctuation in `localisation/english/006_independence_wave_decisions_l_english.yml:236` is a sentence period in `independence_wave_cost_pre_wave_crisis_tooltip`; the previously reported semicolon-style tooltip issue is not present in the current source.
- Evolution incidents are represented as subevents under the evolution track rather than separate catalog event rows; this is consistent with the current event-log/evolution design and is not a localisation omission.

### File encoding concerns

No encoding concern was found in the audited Event 006 files; all 45 `006_*_l_english.yml` files are UTF-8 with BOM.

The shared GUI and event-name files used for the duplicate scan did not introduce duplicate keys in the combined scan.

### Recommended fixes

No required localisation fix is recommended for the current implemented scope.

If the CAT gameplay surface is expanded, consider adding dynamic magnitude fragments to the CAT effect-tooltip keys listed in the Dynamic text opportunities section while keeping the existing route wording and constants authoritative.

Keep the intentional root focus-tree description omission and inert reserved-tag omission documented as design boundaries rather than adding speculative keys.

## Patch record and validation

No gameplay, localisation, focus, decision, event, or workbook source was patched by this audit.

The only changed file is this handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_localisation_final_audit_v72_2026_08_01.md`.

Meaningful validation consisted of parsing the current English localisation files, checking BOM bytes, scanning direct event/decision/focus/scripted-localisation references, resolving idea and active-country package name pairs, resolving evolution/event-log keys, and comparing Event ID 6, cluster 2, and SCN-008 values between localisation, exported CSVs, and the workbook.

Live Hearts of Iron IV launch, GUI rendering, event-log interaction, scenario trigger execution, and in-game font/overflow inspection were skipped because agents must not launch the game; these remain parent/user runtime checks.

## Unresolved wording decisions and blockers

No unresolved wording decision blocks the current localisation package.

The only remaining confidence limit is runtime presentation evidence for the GUI, event log, and scenario surfaces; source-level coverage and catalog mirror checks are complete.

No plan handoff was required because the optional CAT dynamic-value opportunity does not reveal a missing mechanic and does not change gameplay meaning.

Simplifications or omissions: none in the audited implemented localisation scope; the intentional root focus-tree description omission and 17 inert reservations are recorded above as design boundaries.
