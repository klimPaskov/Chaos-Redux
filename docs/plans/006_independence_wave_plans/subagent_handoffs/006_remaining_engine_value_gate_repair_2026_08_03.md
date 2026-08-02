# Event 006 remaining engine-value gate repair — 2026-08-03

## Scope

This narrow repair extends the earlier shared-cost correction to three Event 006 package/formable surfaces that still read engine-backed stability and war support through `check_variable`.

## Changes

- `common/decisions/006_independence_wave_form03_decisions.txt` now uses `has_stability` for the protected-local-services availability gate.
- `common/scripted_triggers/006_independence_wave_form05_triggers.txt` now uses `has_stability` and `has_war_support` for both strategic and proclamation cost helpers.
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` now uses `has_stability` and `has_war_support` for the Pacific-island strategic cost helper.

The existing centralized cost constants, payment effects, decision durations, route gates, and localisation were not changed. No package readiness or attestation flag was opened.

## Evidence and validation

The offline Triggers reference and vanilla trigger documentation identify `has_stability`, `has_war_support`, and `has_army_experience` as the engine-backed country-value triggers. A repository scan now finds no remaining Event 006 `check_variable` stability/war-support cost gates in `common/`.

The focused checks pass after this repair:

- `.tools/audit_event6_allocator.py`
- `.tools/audit_event6_scenario_matrix.py`
- `.tools/audit_event6_gui_matrix.py`
- `.tools/audit_event6_flags.py --strict`
- `.tools/audit_chaosx_country_tags.py --surface-scan`

No live game or save/load evidence is claimed.

## Remaining status

The whole Event 006 goal remains HOLD/PARTIAL. Package research/rights, formable member readiness, 6001 audio, catalog promotion, AI/balance evidence, and runtime proof remain unchanged and fail closed.
