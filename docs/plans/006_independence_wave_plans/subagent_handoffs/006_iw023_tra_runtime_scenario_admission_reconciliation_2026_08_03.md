# IW-023 Transylvania runtime and scenario admission reconciliation — 2026-08-03

## Scope

This handoff reconciles the current independent IW-023 Transylvania (`TRA`) source/package audit with the central Event 006 dispatch gates. It uses the repository and current handoff files only. The obsolete pasted flag-log is not evidence for this admission.

## Admission decision

IW-023 is admitted to the exact Event 006 runtime and SCN-008 package dispatch sets. The package uses the existing vanilla `TRA` identity and does not create a duplicate tag, history identity, or leader surface. Its package-specific setup, force mapping, AI, decisions, cleanup, host-survival, current-map anchor, and additive focus carrier are documented in `006_iw023_tra_independent_source_admission_audit_2026_08_03.md` and the Transylvania package source files.

FORM-08 remains a separate fail-closed formable gate. TRA admission does not imply Vojvodina/Slavonia member readiness, consent, or anchor proof.

## Source changes

- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` now includes `iw_023` in the runtime content-attestation whitelist.
- The normal runtime preflight now requires `original_tag = TRA` for IW-023, matching the vanilla carrier and the package's runtime-ready contract.
- SCN-008 preflight now has an exact IW-023 branch guarded by `is_independence_wave_exact_package_iw_023_tag_available`.
- `.tools/audit_event6_allocator.py` now expects the accepted fifteen-package closure, fourteen compatible reservation groups, and fifteen unique anchors.

## Current static receipt

The allocator and constrained static suite pass after the admission patch: 15 exact attested packages, 14 compatible reservation groups, 15 unique anchors, automatic ladder `6/8/10/14/20`, SCN-008 32-cell matrix plus eight edge cases, strict Event 006 flag families, and scoped Event 006/Soviet tag collision checks. This is source/static evidence; live game execution, save/load, and player-owned scenario observation are not claimed.

## Remaining boundaries

The whole Event 006 goal remains **HOLD / PARTIAL**. The admitted pool remains below the 14- and 20-country bands, the wider 193-row package registry is not a blanket readiness grant, and FORM-08, assets, package AI/balance coverage, and `6001` rights/runtime wiring remain open. No fallback package or shallow generic replacement was used.
