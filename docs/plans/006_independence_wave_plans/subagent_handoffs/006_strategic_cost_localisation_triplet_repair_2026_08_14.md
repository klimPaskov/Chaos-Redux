# Event 006 strategic cost localisation triplet repair

Date: 2026-08-14

## Scope

This narrow localisation repair covers the package-local administrative and strategic custom-cost keys for KOM, KUB, TAT, KOS, and RUT.

The KUB and TAT strategic project cost lines now show the convoy/train commitment already required by their `can_pay_*_strategic_cost` triggers and `independence_wave_decision_pay_diplomatic_standard` completion effects.

Each of the five package-local cost families now has base, blocked, and tooltip siblings for its custom cost keys.

## Files changed

- `localisation/english/006_independence_wave_komi_l_english.yml`
- `localisation/english/006_independence_wave_kuban_l_english.yml`
- `localisation/english/006_independence_wave_tatarstan_l_english.yml`
- `localisation/english/006_independence_wave_kosovo_l_english.yml`
- `localisation/english/006_independence_wave_ruthenia_l_english.yml`

No decision, trigger, effect, AI, central adapter, attestation, preflight, scenario, or Join file changed.

## Evidence and limits

The mandatory pre-change probability inspections for KUB and TAT mission sources returned `PROBABILITY_SOURCE_INSPECTED` with 11 candidates, zero available candidates, 15 required inputs, and `poolComplete=false`; this localisation-only repair does not support a quantitative balance claim or require a before/after probability comparison.

The KUB inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/665bb652ff4e346a9b8f8b7deaad341eb713ea55b5f645a1cacc444128e17436/1793c70a7ee527dc7a08caac1120438ffcc111bea9099a28b9ce2e4c0952c53d/probability-inspect-de8e919c4eae.json`.

The TAT inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cafad4869e778b5093b6420b722227520cb22614ca819f56f5fcb2687d4257b0/c78bea7cba6ce569d9ebeb1a9cacb393671080043e3d3ab3f00d9b0c18e52138/probability-inspect-fc2e09b238bd.json`.

The current Event 006 authority remains 40 runtime adapters, 32 content-attested packages, 29 compatible reservation groups, and 161 unattested selectable rows.

The whole event remains HOLD / PARTIAL because adapter-only packages, portrait and flag provenance, typed probability fixtures, GUI/runtime validation, and super-event 23 audio/firing approval remain open.
