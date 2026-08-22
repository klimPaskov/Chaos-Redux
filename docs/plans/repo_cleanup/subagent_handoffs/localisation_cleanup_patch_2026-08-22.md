# Shared Event Details Localisation Cleanup, 2026-08-22

## Completed scope

This bounded patch updates only `localisation/english/chaosx_gui_l_english.yml` and this handoff. It rewrites five shared Event Details premise strings and removes one confirmed-dead fallback key.

No gameplay, scripted localisation, sourced quotation, spreadsheet, event-specific Event 21 or later prose, or `interface/*.gui` file changed. No GUI layout, coordinate, or click-region work was performed.

## Changed keys

| Key | Old intent and issue | New intent |
| --- | --- | --- |
| `chaosx.events_log.window.event_details.communism_spread` | Explained exact daily drift, internal state tiers, and intervention coverage | Establishes organizers gaining local control, the escalation toward strongholds and revolt, and the strategic value of early intervention |
| `chaosx.events_log.window.event_details.zombie_outbreak` | Explained division manpower rules, immediate coring, outbreak weighting, and gave direct strategy instructions | Establishes a populous-state outbreak, secondary outbreak risk, evolution pressure, and the available containment responses |
| `chaosx.events_log.window.event_details.fury` | Listed selection-pool exclusions, templates, scaled stockpiles, and internal target rules | Establishes the rogue war state, its Fury columns, conquest pressure, and its later multi-actor and all-border escalation |
| `chaosx.events_log.window.event_details.white_peace` | Described candidate selection, event weighting, and repeated-firing suppression | Establishes peace without conquest or indemnity and preserves the progression from one minor settlement to broader settlements |
| `chaosx.events_log.window.event_details.death` | Enumerated state-transfer operations, building removal, soul-power arithmetic, and a long mechanic checklist | Establishes the island disappearances, wasteland consequence, soul-powered spread, living-country responses, and the victory condition |

Removed `chaosx.events_log.window.event_details.event_011_unavailable`. Its former selector consumer was replaced by the live Secret Alliance detail key in commit `9cfec72b3`, and the current exact-reference scan found no remaining consumer.

## Consumer validation

The current shared selector file `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` references the five retained keys at lines 6091, 6095, 6440, 6449, and 6460. The separate pre-reveal Death key remains unchanged and is selected at line 6456.

An exact repository reference scan found no consumer for the removed Event 11 fallback key outside the prior baseline report. No localisation key names, dynamic tokens, or scripted-localisation calls in the five retained rows were changed.

The edited YAML retains its UTF-8 BOM and `l_english:` header. The changed rows retain valid unversioned localisation syntax.

## Prose before and after

### Vagueness

The replacements name the concrete actors, threat, escalation, and response. None uses implementation-status wording or a generic unavailable message.

### Bloat

Communist Insurgency, Zombie Outbreak, Fury, and White Peace now use two short paragraphs. Death was reduced from five dense mechanic paragraphs to three premise and strategy paragraphs.

### Obvious explanation

The Zombie Outbreak text no longer addresses the reader with a strategy checklist. Each description states the situation and meaningful responses without narrating an obvious interface action.

### Repetition

Repeated lists of internal stages, selection rules, and effects were removed where the event-specific detail and tooltip surfaces already carry them.

### Overcomplication

Exact per-day drift, candidate-pool exclusions, selection-weight behavior, immediate-coring language, stockpile scaling, soul-power conversion arithmetic, and ledger implementation details were removed from the shared premises.

### Style repair

The new prose uses direct subjects and active verbs. It contains no em dashes, semicolons, staged contrast formulas, update-history language, or implementation labels.

## Preserved meaning and boundaries

Communist Insurgency still communicates local escalation and intervention. Zombie Outbreak still communicates population-centered spread, secondary outbreaks, evolution pressure, cure work, prevention, and the Anti-Zombie League. Fury still communicates a minor rogue actor, reinforcements, conquest, multiple actors, and all-border escalation. White Peace still communicates restored borders and the later inclusion of multiple minor wars and rare major-country settlements. Death still communicates island origins, erased population, wastelands, soul-powered spread, ghost hosts, continental footholds, recovery work, the Living Compact, and total territorial reclamation as the victory condition.

No sourced quotation was touched. These five keys contained no dynamic localisation token or formatting code that needed preservation.

## Remaining catalog alignment

The Event Details or equivalent player-facing detail fields for Events 1, 2, 7, 9, and 10 in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` still mirror or summarize the prior wording and need alignment by the spreadsheet owner. The workbook is the only editable catalog source. After it is updated, `.tools/export_event_catalog_csv.py` must regenerate the export-only CSV files.

No spreadsheet was edited in this bounded pass.

## Unresolved and skipped validation

A post-change read-only inspection of `events_log_popup_window` completed with code `GUI_INSPECTED`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/831983422909f80f4651d132f1c312ccd6aa3fb5d79c580bf3ab93436b2ed5dc/75ba2f340fa9b2067a998df37c590185b5ed3b6d00cc994c067cb7a7fbb7b499/gui-inspect.06ba0a616570c830.json`.

The inspection covered the requested window and changed no files. Its global source graph exceeded the fixed diagnostic ceiling and reported truncated, repository-wide GUI and GFX diagnostics, including unrelated symbol collisions and overlap warnings. Those diagnostics are outside this localisation-only ownership and do not identify a failure in the five changed premise keys. The tool did not provide a focused rendered line-wrap comparison for each dynamic Event Details branch, so live branch-specific overflow remains uncertain. This uncertainty does not authorize interface layout changes.

No unresolved wording decision remains inside the five assigned keys. No simplification or fallback was introduced.
