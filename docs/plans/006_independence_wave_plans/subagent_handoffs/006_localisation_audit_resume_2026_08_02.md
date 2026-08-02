# Event 006 localisation audit handoff

Date: 2026-08-02

Scope: Event 006 localisation, scripted localisation, dynamic scenario text, event details, Event Log/evolution mappings, and catalog-facing SCN-008 wording were compared with the current source and the Event 006 scenario documentation.

## Audit results

- Missing key list: none in the 45 Event 006 English localisation files; the audit found 6,420 unique non-root keys.
- Duplicate key list: none inside Event 006 files, and no Event 006 key conflicts with another English localisation file.
- Scripted localisation issue list: none; the audited Event 006 scripted-localisation files contain 50 unique `defined_text` names and 348 `localization_key` references, all resolving to existing English keys.
- Scripted call audit: no undefined `[Get...]` call was found in Event 006 localisation or source files.
- Event Log/evolution audit: 57 Event 006-specific Event Log localisation references resolve, including danger milestone, crisis cause/outcome, event details, five evolution stages, and the evolution summary.
- File encoding concerns: none; all 45 Event 006 English localisation files are UTF-8 with BOM, and the touched scenario file still begins with BOM bytes `239,187,191`.

## Patch

Changed file: `localisation/english/006_independence_wave_scenario_l_english.yml`.

- `chaosx.scenarios.launch_status.independence_wave.transaction_busy`: before, "Unavailable: another Liberation release plan owns the transaction barrier." After, "Unavailable: a Liberation release plan currently owns the transaction barrier." The launch-status trigger also fires for Event 006's own queued or active plan, so "another" was inaccurate.
- `chaosx.triggerable_scenarios.80.d`: before, "Movements turned away". After, "Bound movements turned away". The source freezes `global.independence_wave_scenario_bound_blocked_count` before appending the 55 `unbound_current_map` rows, while the next line separately reports `disabled_unbound_count`; the label now names the exact counter.

## Dynamic text and cross-surface notes

- Existing dynamic localisation already covers scenario outcome/failure reason, type and Universal Belligerence rule, intensity, territory, force tier, package IDs, country names/tags, and rival-bloc route/member details; no additional safe dynamic patch was identified.
- The SCN-008 result event has two intentionally distinct paths: standard transaction failures freeze blocked rows and expose the ledger option, while the delayed pre-allocation barrier failure resets without rows and exposes "The plan did not commit." This is consistent with `events/006_independence_wave_scenario.txt:21-45` and does not require a localisation change.
- Event 006 Event Details, crisis history/outcome text, evolution titles/bodies, and scenario chooser strings use the same current names and route vocabulary; no contradiction was found in the inspected catalog-facing SCN-008 wording.
- The existing "Liberation" capitalization is a proper cross-system cluster name and was retained.

## Validation

- Re-ran duplicate and global-key-conflict parsing across all English localisation files: zero Event 006 duplicates and zero conflicts.
- Re-ran scripted-localisation reference parsing: zero missing keys and zero duplicate `defined_text` names.
- Re-ran Event 006 `[Get...]` call parsing: zero undefined scripted-localisation calls.
- Re-ran Event Log localisation-reference parsing: 57 Event 006 references, zero missing keys.
- Confirmed BOM preservation on the patched YAML and reviewed the focused `git diff`.

Skipped meaningful validation: no Hearts of Iron IV launch or live GUI rendering was performed, per repository policy; no workbook edit/export was needed because no catalog source string required a change.

Unresolved wording decisions: none requiring parent action. Existing Event Details and evolution prose were left unchanged because source evidence did not show a defect.

No additional plan handoff was written; this file is the complete localisation handoff for the audit.
