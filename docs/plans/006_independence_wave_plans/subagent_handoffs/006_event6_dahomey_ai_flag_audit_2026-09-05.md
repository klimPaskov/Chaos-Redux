# Event 006 Dahomey AI strategy flag audit

Date: 2026-09-05.

Scope: inspect the IW-095 Dahomey host-restraint AI strategy and its package/decision flag writers after the current completion audit identified a spelling mismatch. This is a read-only weighted-logic audit; no AI strategy, package, decision, effect, localisation, or asset source was changed.

## Finding

`common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3648` checks `independence_wave_iw095_dah_host_ledgers_settled`, but the package effects and decision use `independence_wave_dah_host_ledgers_settled` at `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt:292,301,338,450` and `common/decisions/006_independence_wave_decisions.txt:4117`. The AI strategy therefore cannot observe the settlement receipt written by the package. This is a concrete source mismatch, but correcting it changes when a weighted AI strategy activates.

## Probability baseline

The required first HOI4 MCP call used `adapter = ai_strategy_factor`, `source.path = common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, `candidatePool = [independence_wave_iw095_dahomey_host_restraint]`, `refresh = yes`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `PROBABILITY_SOURCE_DISCOVERED` with source revision `1e219ffc21b3c5d0aa1f9384088be2edc986918f5639e127e762662d08d0e351`, source hash `9fa2ceabcceb79e6d2240ceac219e1c3304c6c4ca2ae42003958452ecad10ae7`, zero parser diagnostics, zero candidates, zero available candidates, zero required inputs, and `discoveryReason = no_weighted_surfaces`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5db6e9c8111dcdc6b422bb481bf4a8a2c59847a588978d39d660e49f479a4ee2/8c021a78672ac4867c608238b3af9f25ddfb7dac91d80cb95ed547c550123bcc/probability-inspect-9fa2ceabcceb.json`.

## Disposition

No source patch is applied. The installed adapter exposes no weighted surface or complete typed fixture for this strategy, so a same-scenario `hoi4.probability_compare` cannot establish the activation change safely. The mismatch remains an explicit unresolved AI audit item; no numeric weight or admission boundary is changed, and no live/runtime claim follows.

## Validation and next owner

The source references were cross-checked with `rg`, and the probability response reported `validation.passed = true` with no diagnostics. A future owner with a complete AI-strategy fixture must compare the corrected flag against this exact candidate/scenario declaration before promoting the repair.
