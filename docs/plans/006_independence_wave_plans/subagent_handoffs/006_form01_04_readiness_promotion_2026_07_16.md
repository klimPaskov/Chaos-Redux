# Event 006 FORM-01 through FORM-04 readiness promotion

Date: 2026-07-16

## Outcome

The parent restored the exact audited readiness bundles for FORM-01 Celtic
Congress, FORM-02 North Atlantic Union, FORM-03 Confederation of the Low
Countries, and FORM-04 Rhenish League. FORM-05 through FORM-48 remain
fail-closed.

The promotion follows these independent reports:

- `006_form01_04_operational_reaudit_2026_07_16.md`;
- `006_form03_promotion_reaudit_2026_07_16.md`.

## Exact runtime change

Each registration helper first calls
`independence_wave_formable_clear_selected_family_readiness`, sets
`independence_wave_formable_readiness_family` to the selected exact family, and
then sets the six shared adapter flags:

- `independence_wave_formable_territory_adapter_ready`;
- `independence_wave_formable_x_tag_reserved`;
- `independence_wave_formable_flag_package_ready`;
- `independence_wave_formable_identity_adapter_ready`;
- `independence_wave_formable_integration_adapter_ready`;
- `independence_wave_formable_member_policy_audited`.

FORM-01, FORM-02, and FORM-04 set only their matching family attestation.
FORM-03 sets both `independence_wave_form03_readiness_attested` and
`independence_wave_form03_progression_attested`.

Changed runtime files:

- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`;
- `common/scripted_effects/006_independence_wave_form03_effects.txt`.

## Promotion checks

A post-edit extraction proved all four helpers clear first, bind the expected
family constant, and contain the exact ordered flag set. The FORM-03 English
file retains its UTF-8 BOM and contains no player-facing raw state 34 or state
36 label. Every entry in the FORM-03 report-scene checksum ledger resolves; the
reconciled submanifest hash is
`e1bf4c0ab711cb38df83e94a4776578528837bbb7080351c1e9b91c27a8015bb`.

This is static promotion evidence, not a claim that HOI4 runtime scenarios have
already been executed. Individual automatic and SCN-008 country-package gates
remain separate from formable-family readiness.

## Simplifications and blockers

No fallback or readiness simplification was used. The four families received
only the bundles authorized by their audit. Remaining formable families are
still blocked on their own researched identity, assets, territory contract,
integration policy, package content, and audit evidence.
