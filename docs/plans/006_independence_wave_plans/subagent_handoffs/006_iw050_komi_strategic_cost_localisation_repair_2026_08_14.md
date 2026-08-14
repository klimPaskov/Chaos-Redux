# IW-050 Komi strategic-cost localisation repair — 2026-08-14

## Scope

This narrow package-local repair updates the visible `independence_wave_komi_cost_strategic` line in `localisation/english/006_independence_wave_komi_l_english.yml`.

The Komi strategic trigger and completion effect already require and pay the shared diplomatic-standard command-power plus convoy-or-train commitment, while the trigger also checks Stability, War Support, and the one-factory project burden.

The old Komi cost line displayed Stability, War Support, Command Power, and the factory burden but omitted the convoy-or-train commitment.

The updated line now exposes all of those live requirements and preserves the Komi-specific one-factory value from `constant:independence_wave_komi_cost.civilian_factory_use`.

## Boundaries

No decision trigger, payment effect, AI score, central dispatcher, content attestation, scenario preflight, Join sequence, flag, portrait, formable, or Event 005 origin surface changed.

IW-050 remains package-local and fail-closed at the current Event 006 authority boundary of 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows.

## Evidence

The live source pairing is `common/decisions/006_independence_wave_komi_decisions.txt:124-129,261-269`, `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:51-57`, and `common/scripted_effects/006_independence_wave_decision_effects.txt:180-199`.

The mandatory pre-change probability inspection completed with `PROBABILITY_SOURCE_INSPECTED` for `mission_ai_will_do`, source revision `da4449ebf33e1a528d39acbc907d31879aa5c78802ad1f0dd458636171a8e4e4`, source hash `a247b55afe8f3c28d38584f13083eb3d6d8f3454e854198c115f145110769886`, 11 candidates, 0 available candidates, 15 required inputs, and `poolComplete=false`.

The inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b994317dc989486449b27a80bbe6645b9a6b4588f3cbe8b6c54ed9bb9fabe612/bef831173b0da3b5c6c3b361cc22e346e2bfff2634d1a8c20c096b1d2f00e768/probability-inspect-a247b55afe8f.json`.

The localisation remains UTF-8 with BOM, and the owned strategic-cost key occurs exactly once.

This repair does not justify a normalized probability, timing, dominance, starvation, or balance claim because the mission adapter still reports an incomplete pool with no available candidates.
