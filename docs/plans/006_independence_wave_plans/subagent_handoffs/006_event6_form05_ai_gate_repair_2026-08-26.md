# Event 006 FORM-05 post-formation AI gate repair handoff

## Scope

This narrow source repair restores the existing FORM-05 post-formation AI strategy layer. The previous enable block required `independence_wave_origin_event6`, a country flag with no writer anywhere in the mod, so the policy could never activate.

The target source repair and this handoff were already present in `HEAD` at audit start (`bc83a1e856b601bb16bd6d7226087d065797c520`); this audit made no additional gameplay-file edit.

## Changed path

- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`

## Repair

The FORM-05 policy now requires the canonical `is_independence_wave_active_country` trigger together with the existing `independence_wave_form05_post_formation_active` lifecycle flag. The carrier's war-restraint, convoy, dockyard, and coastal-bunker strategy values are unchanged. The setup effect still writes the lifecycle flag and cleanup still clears it.

## Validation

- A source-only scan confirms zero live `common/` references to the unwritten `independence_wave_origin_event6` token; explanatory mentions remain in this handoff and the source-of-truth/resume notes.
- Source inspection confirms `is_independence_wave_active_country` requires the active-origin flag, Event 006 origin variable, and a non-ended origin.
- Focused FORM-05 source assertions passed for the live gate, lifecycle writer/cleanup, canonical post-formation proof, and unchanged strategy values.
- `python -B .tools/audit_event6_allocator.py`: passed; the 32 attestation and `3/4/5/7/10` ladder remain unchanged.
- `python -B .tools/audit_event6_country_api.py`: passed.
- `python -B .tools/audit_event6_flags.py --strict`: passed.
- `python -B .tools/audit_event6_form16.py`: passed.
- `python -B .tools/audit_event6_gui_matrix.py`: passed.
- `python -B .tools/audit_event6_scenario_matrix.py`: passed.
- `hoi4.probability_inspect` first returned `PROBABILITY_ADAPTERS_LISTED`; the target source with `ai_strategy_factor` then returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, source revision `c5a825408ef8c2aefa03414a11b1d8f585e22d702f3f0b775d9bc90581670a7d`, source hash `414ba72e63b8466406e1bb8c2592f981b511b69be024dad58b4766d9a4123611`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fce7ba13c3d6fc5800c2940ed3fc99b42d669761c2f6e7e89bba424ce37a44a5/ed65803a999b315c91c8ff7d9d25f1fd40e4f5e02f59f0eab467585b5544a31f/probability-inspect-414ba72e63b8.json`.
- Because the adapter exposed no weighted surface, evaluate/sweep/compare were not applicable and no quantitative probability or AI-balance claim is made.

## Boundary

This repair does not promote FORM-05 admission, alter package costs, change formable identity, or claim live AI execution. The whole Event 006 implementation remains **HOLD / PARTIAL**.
