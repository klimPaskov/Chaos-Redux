# Event006 Final Settlement Localisation Audit Handoff

Scope: narrow localisation audit and patch for `independence_wave_certify_final_settlement` and `cr_no_more_flags_needed`. No gameplay, assets, GFX, Event005 files, or unrelated localisation were edited.

## Files Changed

- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_final_settlement_localisation_audit_handoff.md`

## Changed Keys

- `independence_wave_certify_final_settlement_requirements_tt`
  - Before: described an "integrated and recognized compact secretariat", which blurred the integrated compact and recognized secretariat requirements.
  - After: describes "an integrated compact, a recognized secretariat" while preserving the strict gate.
- `cr_no_more_flags_needed_tooltip`
  - Before: used "no patron puppet route", which was less aligned with the final-settlement tranche's in-world anti-puppet clause.
  - After: uses "the anti-puppet clause intact" and keeps the mass-wave, guarantee, peaceful border, no-ultimatum, and no-war requirements.

## Audit Results

- Missing key list: none for the scoped decision and achievement keys.
- Duplicate key list: none found in the two scoped localisation files.
- Scripted localisation issue list: none found in scope; the audited keys are direct localisation keys, not scripted localisation entries.
- Dynamic text opportunities: `independence_wave_certify_final_settlement_cost_tt`, `_blocked`, and `_tooltip` hardcode `25` while gameplay uses `constant:independence_wave_decision.congress_final_settlement_command_power_cost`. A dynamic cost helper could reduce drift, but it would require scripted localisation or helper changes outside this narrow localisation-only scope.
- Cross-surface mismatch notes: patched the achievement tooltip to match the decision/tranche framing around the anti-puppet clause. Docs already describe anti-puppet compact terms and did not need a wording patch.
- File encoding concerns: none. Both scoped localisation files still begin with UTF-8 BOM bytes.
- Recommended fixes: no additional localisation fixes are recommended inside the current scope.

## Cost Text Coverage

- `independence_wave_certify_final_settlement_cost_tt`: present.
- `independence_wave_certify_final_settlement_cost_tt_blocked`: present.
- `independence_wave_certify_final_settlement_cost_tt_tooltip`: present.

## Validation Run

- `file -b --mime-encoding localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_achievements_l_english.yml`
- `xxd -l 3 localisation/english/006_independence_wave_l_english.yml`
- `xxd -l 3 localisation/english/chaosx_achievements_l_english.yml`
- `rg -n ":0\\s*\\\"" localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_achievements_l_english.yml`
- `awk 'BEGIN{FS=":"} /^[A-Za-z0-9_.-]+:/ {print $1}' localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_achievements_l_english.yml | sort | uniq -d`
- Scoped key-presence shell loop for the final-settlement and `cr_no_more_flags_needed` keys.

## Skipped Validation

- No in-game validation was run; this was a localisation-only audit in a dirty shared worktree.
- No broad missing-localisation sweep was run outside the requested Event006 final-settlement tranche.

## Remaining Issues

- No unresolved wording decisions inside the requested scope.
- Broader Event006 completion is not claimed.
