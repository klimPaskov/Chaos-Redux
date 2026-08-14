# IW-153 POK dormant anchor hardening — 2026-08-14

## Scope

This bounded source repair strengthens the dormant IW-153 POK compatibility contract without admitting the package or changing any central dispatcher, attestation, preflight, scenario, or Join list.

## Source change

`common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt` now requires the Event 006 country to both own and control state 334 in `has_independence_wave_iw_153_pok_compatibility_contract`, alongside the existing capital-scope, core, releasable, character, origin, and package-identity witnesses.

This matches the anchor witness pattern used by the adjacent dormant compatibility adapters and prevents a capital-only predicate from being treated as a current-map preservation proof.

## Boundary

IW-153 remains dormant and fail-closed. No POK state transfer, core mutation, leader recruitment, flag or portrait installation, central adapter/attestation widening, preflight change, scenario admission, or Join change was made.

## Validation

The edited trigger block is balanced and `git diff --check` reports no whitespace errors. The existing POK preservation audit remains the source of truth for identity, vanilla-origin, map, and admission blockers.
