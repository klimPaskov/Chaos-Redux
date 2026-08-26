# Event 006 FORM-05 post-formation AI gate repair handoff

## Scope

This narrow source repair restores the existing FORM-05 post-formation AI strategy layer. The previous enable block required `independence_wave_origin_event6`, a country flag with no writer anywhere in the mod, so the policy could never activate.

## Changed path

- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`

## Repair

The FORM-05 policy now requires the canonical `is_independence_wave_active_country` trigger together with the existing `independence_wave_form05_post_formation_active` lifecycle flag. The carrier's war-restraint, convoy, dockyard, and coastal-bunker strategy values are unchanged. The setup effect still writes the lifecycle flag and cleanup still clears it.

## Validation

- `rg` confirms zero remaining references to the unwritten `independence_wave_origin_event6` token.
- Source inspection confirms `is_independence_wave_active_country` requires the active-origin flag, Event 006 origin variable, and a non-ended origin.
- `python -B .tools/audit_event6_allocator.py`: passed; the 32 attestation and `3/4/5/7/10` ladder remain unchanged.
- `python -B .tools/audit_event6_country_api.py`: passed.
- `python -B .tools/audit_event6_flags.py --strict`: passed.
- `python -B .tools/audit_event6_form16.py`: passed.
- `python -B .tools/audit_event6_gui_matrix.py`: passed.
- `python -B .tools/audit_event6_scenario_matrix.py`: passed.
- The installed probability adapter reports no `ai_strategy_factor` surface, so no numeric probability comparison is claimed.

## Boundary

This repair does not promote FORM-05 admission, alter package costs, change formable identity, or claim live AI execution. The whole Event 006 implementation remains **HOLD / PARTIAL**.
