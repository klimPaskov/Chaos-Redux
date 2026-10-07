# Event 006 Signature Catalog Review — 2026-10-07

Disposition: Catalog parity review is complete; Event 006 remains incomplete.

## Catalog parity

The authoritative workbook row is `Events!A7:M7`, keyed by ID `6` (`Independence Wave`). `B7` matches `chaosx.event_name.6` in `localisation/english/chaosx_event_names_l_english.yml:8`.

`C7` matches the current Event Details text at `chaosx.events_log.window.event_details.independence_wave` in `localisation/english/chaosx_gui_l_english.yml:1117`. The shared Event Log detail dispatcher selects that key for Event 006 at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6762-6763`.

`D7:H7` match `independence_wave.evolution.1.body` through `.5.body` in `localisation/english/006_independence_wave_evolution_l_english.yml:12,14,16,18,20`; the shared dispatcher resolves these evolution bodies at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9492-9508`.

`I7` remains blank, `L7` remains `2, 16`, and `M7` remains `Needs Testing`. The existing Events row has no Notes or Implementation Detail column, and no player-facing mirror cell needs correction. No workbook cell was changed.

The workbook SHA-256 was `C945A81B16454DE68468F73D43348612828DF76EAE463973626990AF06A91A29` at review start and remained the same at the pre-handoff check. It was already locally modified relative to the tracked Git LFS pointer before this review; this task preserved that version.

Because the workbook was not saved, `python .tools/export_event_catalog_csv.py` was not run and the three export-only CSV snapshots were not touched.

## Source facts carried forward

`docs/events/006_independence_wave/signature_modules.md:10-11` records 31 imported signature focuses, three signature achievements, and open imported-focus layout, campaign AI, and native lifecycle gates. The same document identifies Oyo/IW-097, Aceh/IW-150, and Mon/IW-161 signature packages.

The source lists eight paid signature projects at `signature_modules.md:80-87`. Mon river services take 120 days and apply +15 Capacity, +5 Legitimacy, and −5 Instability; the River Service Administration also gives 5% political-power gain and 10% infrastructure construction speed (`signature_modules.md:47-48,87`). PUSA is dated from 5 May 1939 and its paid organization grants one named 50% industry research bonus (`signature_modules.md:29-30,81`). The three achievement predicates are named at `signature_modules.md:113`.

`docs/plans/006_independence_wave_plans/subagent_handoffs/ready_formable_contracts_20261006.md:9,13,19-22,34-36` records FORM-17, FORM-32, FORM-36, and FORM-37 as cosmetic-carrier formations with two paid 180-day integration stages. Member countries retain sovereignty; annexation, subject creation, blanket cores, and origin-ending shortcuts are excluded.

Admission remains 109 as specified in the parent task. Imported layout, AI, GUI, and portrait gates remain open. No status promotion or whole-event completion claim is made.

## Handoff result

Workbook delta: none. Sheets, rows, columns, and Event IDs changed: none. Export paths: none; exporter not run. Scoped mirror cells have no blocked or needs_user_review wording gaps.