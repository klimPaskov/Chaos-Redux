# IW-023 Transylvania post-repair audit

Date: 2026-08-03

Status: source-level PASS for the repaired package contracts; HOLD for runtime content attestation.

## Scope and current authority

This parent-owned follow-up supersedes the planner, roster, focus-carrier, and formable-registration findings in `006_iw023_tra_additive_country_package_audit_2026-08-03.md`. It audits the current repository source after the reviewed TRA package and FORM-08 adapter commits. It does not use the historical pasted flag log as evidence and does not claim live release, save/load, or in-game balance behavior.

## Repaired contracts

- The region-03 planner calls `is_independence_wave_exact_package_iw_023_tag_available`, not the legacy bulk-content predicate. The exact wrapper requires the registered vanilla `TRA` origin, state `84` capital, a unique usable anchor, and a non-TRA owner.
- `chaosx.nr6.350` has an explicit TRA branch. It records `independence_wave_tra_vanilla_roster_checkpoint` only when the preserved vanilla Iuliu Maniu ruling roster is present. Setup then marks the shared command-roster receipt.
- The TRA setup selects family `danubian_confederation`, sets the selected-family flag, loads the family profile, and calls `independence_wave_focus_register_formable_family`. The prepared trigger now requires the family registration and FORM-08 readiness receipt in the intended order.
- FORM-08 readiness is carrier-scoped. `independence_wave_form08_register_readiness` now fails closed unless the active Event 006 country is the reviewed TRA package with anchor state `84` owned and controlled and capital state `84`. The adapter reuses the existing vanilla `HUN_EMPIRE` cosmetic identity and never allocates a new country tag.
- The meaningful vanilla `austro_hungarian_releasable_focus` tree remains the TRA carrier. Its eight Event 006 shared focuses are inert unless the active package owns the additive overlay and lifecycle flags; TRA never calls `load_focus_tree` for the generic tree.
- Shared dispatch still requires both `has_independence_wave_generic_focus_contract` and `independence_wave_generic_ai_profile` during final validation. TRA setup assigns the additive carrier and generic AI profile through the shared focus framework.
- TRA decisions, ideas, force mapping, AI strategies, localisation, host-protection checks, array receipts, and package cleanup remain wired to the package ID. Shared generation cleanup removes formable, focus, decision, relationship, and origin state after the package-specific cleanup runs.

## Remaining blockers

- IW-023 is not in the compile-time content-attestation set. Promotion still requires the independent country-package audit to accept all source-level setup, force, AI, current-map, and cleanup evidence under the current admission policy.
- FORM-08 remains runtime-inadmissible until the frozen minimum three-member/three-consent/three-anchor proof exists. Banat and Macedonia do not receive automatic admission from the TRA carrier, and no fallback identity or tag is authorized.
- Runtime transfer, capital, supply, starting-force, AI survival, save/load, and live balance evidence are intentionally not claimed in this source-only audit.

## Files reviewed or changed

- `common/scripted_effects/006_independence_wave_form08_effects.txt` — added the carrier- and anchor-scoped readiness guard.
- `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt` — current TRA setup, dispatch, validation, and cleanup.
- `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt` — exact availability and prepared-package gates.
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` — exact planner admission.
- `common/national_focus/austro_hungarian_releasable_shared.txt` and `common/scripted_triggers/006_independence_wave_focus_triggers.txt` — reviewed additive carrier.
- `events/006_independence_wave.txt` — TRA roster checkpoint.
- `docs/systems/006_independence_wave_transylvania_package.md` — current package and admission boundary.

## Validation

The current static checks report: allocator ladder `6/8/10/14/20` and World Collapse `20`; all 32 SCN-008 cells and 8 edge cases; `102/102` complete flag families; and zero protected Event 006/Soviet external country-definition or identity-surface collisions. The touched FORM-08 effect has balanced braces and the focused diff has no content errors. No live game or old log evidence was used.
