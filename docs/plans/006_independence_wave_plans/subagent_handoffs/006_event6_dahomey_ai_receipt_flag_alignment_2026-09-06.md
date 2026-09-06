# Event 006 Dahomey AI receipt-flag alignment — 2026-09-06

## Disposition

Implemented as a narrow source correction. The change aligns three Dahomey AI enable gates with the canonical package receipts already published by the IW-095 package effects and decisions. It does not alter AI weights, package admission, identity or rights gates, assets, central attestation, or the no-pre-event contract.

## Changed source

`common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3648,3661,3676`

- `independence_wave_iw095_dah_host_ledgers_settled` → `independence_wave_dah_host_ledgers_settled`
- `independence_wave_iw095_dah_compact_stabilized` → `independence_wave_dah_compact_stabilized`
- `independence_wave_iw095_dah_emergency_government` → `independence_wave_dah_emergency_government`

The canonical names are defined and mutated in `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt` and consumed by the IW-095 decisions/triggers. The stale `independence_wave_iw095_dah_*` names no longer occur in the AI registry.

## Validation

- `python .tools/audit_event6_allocator.py --strict` passed with the existing 3/4/5/7/10 ladder and 32/29/40/161 boundary.
- `python .tools/audit_event6_country_api.py` passed with 242 unique tags, 191 carriers, and no missing or duplicate rows.
- `python .tools/audit_event6_flags.py --strict` passed with 102 complete Event 006 flag families.
- `python .tools/audit_event6_form16.py` passed for ARM/GEO/AZR.
- `python .tools/audit_event6_scenario_matrix.py` passed all 32 cells and eight edge cases.
- The required probability baseline for the Dahomey AI source reported `no_weighted_surfaces` with zero candidates and zero required inputs; no numeric balance comparison or weight change is claimed.

## Remaining gates

IW-095 remains package-local and fail-closed. Its 1936 identity/rights receipt, neutral opening flag, approved portrait roster, central adapter/attestation/preflight/Join wiring, typed probability fixtures, and whole-event MCP evidence remain unresolved. No fallback identity or asset was introduced.
