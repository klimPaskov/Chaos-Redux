# Event 006 Banat project-failure tooltip clarity — 2026-09-20

Disposition: implemented / bounded localisation-only repair.

The source-backed effect `independence_wave_axx_apply_project_failure` in `common/scripted_effects/006_independence_wave_balkan_package_effects.txt:100-110` applies standard losses to legitimacy, capacity, and security, a minor recognition loss, a major instability increase, and standard losses to the Banat civic and mountain-defence ledgers.

The former `independence_wave_axx_project_failure_effect_tt` only described the two ledger losses and did not disclose the visible national-value changes. The current localisation at `localisation/english/006_independence_wave_balkan_l_english.yml` now states that the failure costs legitimacy, recognition, capacity, and security, raises instability, and lowers civic mandate and mountain-defence readiness.

No effect, trigger, decision availability, AI score, cost, route, variable, flag, asset, workbook, or package-admission gate changed. The five route-specific Banat outcome tooltips were inspected and left unchanged because they already describe their distinct government and ledger outcomes.

Validation required: run `.tools/audit_localisation_static.py`, confirm the edited file retains its UTF-8 BOM and English header, and confirm the key remains the sole definition and the decision consumer remains `common/decisions/006_independence_wave_balkan_decisions.txt:57-59`.

Remaining limitation: this is source/localisation evidence only; no live decision-row or in-game tooltip render is claimed.
