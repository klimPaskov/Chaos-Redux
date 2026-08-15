# IW-051 Sakha schema and localisation repair — 2026-08-15

## Disposition

This is a package-local syntax and presentation repair for the already committed IW-051 Sakha core. It does not change central adapter, attestation, normal or SCN-008 preflight, deterministic Join, map ownership, history, flags, portraits, identity clearance, or admission authority.

## Changes

- `common/script_constants/006_independence_wave_sakha_constants.txt` now declares explicit `schema` blocks for pressure (`fixed_point`), duration (`int`), cost (`int`), and politics (`fixed_point`) groups, matching the accepted script-constants documentation pattern used by adjacent Event 006 packages.
- `localisation/english/006_independence_wave_sakha_l_english.yml` now begins with exactly one UTF-8 BOM followed by `l_english:`, removing an accidental duplicate BOM marker without changing any player-facing key or wording.

## Validation

The four Sakha constant groups retain their existing values and references, and the localisation file retains its existing key set and wording. The file has one UTF-8 BOM, no duplicate localisation keys, and no 156x210 or portrait/runtime changes.

## Remaining gates

IW-051 remains fail-closed because the identity and rights flag is parent-owned and unset, released-origin and host-remnant evidence is not admitted, flag provenance is unresolved, typed probability fixtures remain incomplete, and central adapter, attestation, preflight, scenario, and Join surfaces intentionally exclude IW-051.
