# Event006 Reduced Core Recovery Decision

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched `common/script_constants/006_independence_wave_constants.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `common/decisions/006_independence_wave_decisions.txt`, `localisation/english/006_independence_wave_l_english.yml`, and `docs/events/006_independence_wave.md`.

- Added `independence_wave_recover_surveyed_core`, a generic Border Commission state-targeted decision for reduced-territory Event006 releases.
- Added `can_independence_wave_recover_surveyed_core` so the decision only targets unowned non-capital cores that pass existing Border Commission host-survival checks.
- Added a matching scripted effect that transfers the state, records a peaceful border resolution, applies cooldown, raises legitimacy, and lowers claim ambition.
- Added costs and effects through `independence_wave_decision` script constants.
- Added localisation and event documentation for the reduced-start territory recovery route.

## Reason

Reduced one-state releases need a direct way to grow after the wave without waiting for route-specific focus flags. The spec allows one-state releases only when they can grow later through focuses, decisions, claims, settlement talks, or border wars. This patch makes that path immediately visible through the Border Commission while preserving the host-survival rule.

## Validation

Passed parent validation:

- Scoped brace-balance checks returned zero for touched Event006 script, decision, event, docs, and handoff files.
- Unsupported less-equal/greater-equal operator scan returned clean for touched files.
- Trailing-whitespace, CRLF, and `git diff --check` checks returned clean.
- Localisation file retained UTF-8 BOM.
- New localisation keys each resolve once and duplicate-key scan returned clean.
- Reference scan found the new recovery decision wired through constants, trigger, effect, decision, localisation, docs, and this handoff.
- No fresh HOI4 `error.log` is present under `tmp/hoi4-error-logs`; only the old May 29 `watchdog.log` remains.

## Remaining Scope

This closes the generic reduced-start territory recovery gap. It does not complete the full Event006 source-spec pack, remaining package depth, final asset checks, spreadsheet alignment, or final completion audit.
