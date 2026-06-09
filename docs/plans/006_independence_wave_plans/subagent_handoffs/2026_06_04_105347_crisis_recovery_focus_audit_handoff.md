# Event 006 Crisis Recovery Focus Audit Handoff

## Scope

Bounded audit of the Event 006 Independence Wave crisis recovery focus tranche:

- `independence_wave_summon_emergency_session`
- `independence_wave_form_street_defense_committees`
- `independence_wave_reopen_cabinet_authority`
- `independence_wave_send_permanent_delegation` reconnection
- `independence_wave_crisis_recovery_posture`

Consulted required references before patching: offline Paradox wiki national focus, triggers, effect, localisation, and data structures pages; vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and `common/script_constants/documentation.md`; repo skills `hoi4-focus-trees`, `chaos-redux-events`, and `xlsx`.

## Files Changed

- `common/ai_strategy/006_independence_wave.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_105347_crisis_recovery_focus_audit_handoff.md`

No Event 005 files were edited. No flags or assets were edited.

## Patch Summary

The focus branch gate correctly allowed crisis entry from war, low stability, compact failure, regional compact integration failure, release-side cabinet-seat demands, or dangerous patron leverage.

One narrow AI mismatch was patched: `independence_wave_crisis_recovery_posture` did not enable from `has_war = yes` or `has_independence_wave_dangerous_patron_leverage = yes`, even though both are valid crisis-entry signals for `independence_wave_summon_emergency_session`. The AI posture OR now includes both signals, keeping the AI defense/restraint overlay aligned with the focus availability gate.

## Audit Findings

- Reachability: pass. The branch opens from `independence_wave_recognition_desk` but is gated by crisis conditions, so it is reachable without becoming a normal stable-country route.
- Prerequisites: pass. The three crisis focuses form a linear branch from emergency session to street defense to cabinet authority.
- Reconnection: pass. `independence_wave_reopen_cabinet_authority` is included in the single prerequisite block for `independence_wave_send_permanent_delegation`, which gives OR semantics alongside the other route endpoints.
- Rewards: pass. The three focuses set route/progress flags and adjust stability, legitimacy, pressure, militia, equipment, cohesion, and patron leverage through constants or existing helper logic.
- Constants and dynamic values: pass. New tranche tuning uses `constant:independence_wave_focus.*` values rather than hardcoded reward and gate numbers.
- Icons: pass. The three focus icons resolve through existing Event 006 focus sprites in `interface/006_independence_wave_icons.gfx`.
- Localisation: pass. Name and description keys exist for all three new focuses.

## Validation Run

- Counted actual `focus = {}` blocks in `common/national_focus/006_independence_wave_focus.txt`: 93.
- Checked focus localisation coverage for every focus block in `localisation/english/006_independence_wave_l_english.yml`: 0 missing name/description pairs.
- Verified Event 006 catalog workbook row mentions the shared 93-focus Liberation Provisional tree by reading workbook XML.
- Brace balance checked for:
  - `common/national_focus/006_independence_wave_focus.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/ai_strategy/006_independence_wave.txt`
  - `localisation/english/006_independence_wave_l_english.yml`
  - `docs/events/006_independence_wave.md`
- Unsupported operator scan on touched tranche files: no `<=` or `>=` found.
- Localisation encoding check: UTF-8 BOM present.
- Localisation key style check: no `:0` entries found in `localisation/english/006_independence_wave_l_english.yml`.

## Skipped Validation

- No full HOI4 parser or live-game validation was run.
- No full Event 006 completion audit was attempted; this was limited to the crisis recovery focus tranche.
- `openpyxl` was not installed, so the workbook check was read-only XML inspection rather than a library-level workbook load.

## Remaining Gaps

No remaining gaps were found inside this bounded crisis recovery focus tranche.
