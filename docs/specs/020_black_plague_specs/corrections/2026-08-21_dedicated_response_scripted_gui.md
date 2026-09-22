# Event 020 Dedicated Response Scripted GUI Correction

> **Category boundary:** `black_plague_response_category` is an Event 020 decision category, separate from the accepted CBRN raid categories `chemical_raids` and `biological_raids` in the [2026-09-20 CBRN amendment](../../chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md). Its informational GUI does not add a raid category or payment path.

This correction supersedes the earlier presentation instruction that kept the dedicated Black Plague response category text-only.

`black_plague_response_category` uses one Event 020-owned scripted GUI attachment to present the national response at a glance. The attachment is informational: ordinary decisions remain the only action surface, and the GUI must not duplicate costs, start projects, change disease state, or create a second cure ledger.

The compact display presents no more than three live values:

- Countermeasure Progress from 0 to 100 as the primary meter, with its current programme stage.
- Medical Reserve as current stock against capacity.
- Response Capacity as remaining capacity against total capacity.

Country deaths, worldwide deaths, and international-response status may appear as concise supporting text or tooltips rather than additional dashboard meters. The progress tooltip must explain that countermeasures reduce mortality and spread and enable sustained cleanup, but never remove an active outbreak instantly.

The attachment belongs only to `black_plague_response_category`. It must not alter or replace `chaosx_disease_containment_category`, the shared disease board, the selected-state action surface, the contamination mapmode, or the ownership boundary established by the dedicated-response-category correction.

The final implementation uses `black_plague_response_category_scripted_gui` and `black_plague_response_category_window`. It reuses the registered plague-doctor treatment picture and existing Event 020 variables; it introduces no new gameplay resource, progress producer, category, or asset placeholder.
