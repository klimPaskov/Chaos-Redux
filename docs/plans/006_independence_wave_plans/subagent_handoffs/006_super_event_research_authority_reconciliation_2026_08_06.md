# Event 006 super-event research authority reconciliation

Date: 2026-08-06.

The text and audio verification notes now use the current ordinary runtime identifiers and package authority without changing the accepted selections.

## Current authority

- The League of New States uses display/audio/Event Log identifiers `23`; its accepted recording remains rights-blocked and absent from runtime.
- Every Border a Casus Belli uses display/audio/Event Log identifiers `24`; its verified recording and source-wired runtime package remain in place.
- Current package authority is 23 content-attested selectable packages across 22 compatible reservation groups, 170 unattested rows out of 193 non-overlay rows, and a 20-package static standalone witness.

## Files changed

- `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_text_verification.md`
- `docs/plans/006_independence_wave_plans/super_event_research/006_super_event_audio_verification.md`

Only dated cross-reference counts and the current-date label changed. The accepted title, quote, audio selection, slot-23 rights block, slot-24 wiring, and no-substitute rule are unchanged.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with the 23/22/170 authority and 20-package witness.
- Active source scan found no Event 006 `6001`/`6002` references outside dated documentation.
- `git diff --check` passed for both research notes.
