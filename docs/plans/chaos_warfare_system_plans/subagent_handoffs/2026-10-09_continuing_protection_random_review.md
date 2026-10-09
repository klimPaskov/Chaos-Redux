# Continuing-protection random-value and probability review

Status: read-only review complete. The connected probability analyzer did not classify the native random-value effects as weighted surfaces, so no exact campaign probability is claimed and no additional analyzer retry remains.

## Scope and MCP result

This review covers the native RNG calls reached by `cbrn_delivery.4`: the percentage-death helper `chaos_meter_register_state_civilian_deaths_percent` at `common/scripted_effects/chaos_meter_effects.txt:3575-3707`. The two draw effects are at lines 3641 and 3665.

The primary continuing-protection handoff reports an earlier generic native-random probability inspection returned `no_weighted_surfaces` despite these visible commands. Its raw receipt could not be located in `docs/testing/2026-10-09_continuing_protection/` or elsewhere under `docs/testing/`; the primary handoff is the retained record at lines 154-157.

The connected live probability schema exposes adapter `direct_random` and has no `native_random` adapter. Within the shared one-initial-plus-one-corrected attempt budget, one narrower read-only `hoi4.probability_inspect` call targeted canonical source `common/scripted_effects/chaos_meter_effects.txt`. It returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates and zero unresolved items. The adapter artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d850a7c1b8113b7cd4bf7be6a287716062bf319f9a4b08c5f34d90fca53457ce/4e65860b0465b92f26c5bf2c4ae2532b298fe2eee3a4d316d9e749302347bf5b/probability-inspect-d7afa38dece3.json`; its source hash is `d7afa38dece30ac357eb230fe873062a5a20e74fb53d0e58e83546f1d6137f84`, source revision `b6d778e5506e33962854d88aebadd1c509e363525de31fb902d922892b1ffc98`. The exact raw request, response and artifact envelope are retained in the testing folder.

No `probability_evaluate`, `sweep`, `compare`, or `render` followed because there is no candidate pool to normalize or evaluate. No simulation was run because no defensible campaign distribution is declared. No sequence analysis applies to these two native draws, which are not a custom pool with declared transitions and cadence.

Candidate-pool completeness is not applicable because the corrected inspection discovered zero weighted candidates. External-factor completeness is also unresolved as a probability model: population, class/stage, current terminal doctrine, paid overlap, environment and cap inputs determine each execution, but no campaign-state distribution was declared for them.

## Native RNG contract

The installed `effects_documentation.md` entry for `set_temp_variable_to_random` says the effect works in any scope, defaults to `[0,1)`, and defaults to decimal output (`integer = no`). The offline wiki's `set_variable_to_random` entries say the lower bound is inclusive and the upper bound exclusive. Neither source specifies the draw distribution, independence of successive draws, or how this effect's random stream is seeded. The source uses the shortened no-argument form twice, so only the default range and decimal mode are documented for these call sites.

The exact source operations are `set_temp_variable_to_random = { var = chaos_state_deaths_roll }` and `set_temp_variable_to_random = { var = chaos_state_deaths_cap_roll }`. The first roll is transformed by the caller-provided outbreak constants `1.25 + 1.65 × roll`, giving the documented-value bound `[1.25, 2.90)`. The cap roll uses the generic constants `0.75 + 0.85 × roll`, giving `[0.75, 1.60)`. These are deterministic interval bounds derived from the documented range and current constant values; they are not selection probabilities or distribution claims.

## Deterministic protection and death arithmetic

The changed `cbrn_delivery.4` path still sets `chaos_state_deaths_random_min` and `chaos_state_deaths_random_span` from the same outbreak constants, sets the same cap factor and percent divisor, and invokes the same `chaos_meter_register_state_civilian_deaths_percent` helper. The new `cbrn_apply_continuing_civilian_protection` changes the deterministic casualty multiplier using current mask and medical data, exact paid-hospital overlap, and the existing Burn Treatment factor. It clamps the combined multiplier no lower than same-mask result `M × 0.50`.

The terminal doctrine's 1.10 multiplier moved from the stored continuing class rate to caller-owned `chaos_state_deaths_percent` inside that new helper, after protection and before population/divisor arithmetic. It is still applied once at the same fixed-point quantization stage. The class rate remains raw in state storage; the current controller's terminal idea is checked at the due tick.

The generic helper first computes population × death percent × people-per-k, divides by the caller's fixed-point divisor when present, then multiplies by the deterministic casualty multiplier and the first native draw's random multiplier, rounds to an integer, and clamps against a population-derived cap. The cap is itself rounded from population × cap factor × the second draw's multiplier, then clamped between the configured cap floor and hard maximum.

The `M × 0.50` floor is a bound on the deterministic multiplier before native draws, rounding and cap application. It is not a promise that realized integer deaths remain at least half of a separate unprotected integer count. Rounding thresholds, the separately drawn cap, and saturation can move that ratio in either direction.

## Preservation and source-harness evidence

The continuing-protection source manifest lists six changed gameplay files and does not list `common/scripted_effects/chaos_meter_effects.txt`. The current file's raw SHA-256 is `f2e4a3a6dbdd30bee11b5ceea021213cff23d772bc9ad05317988e15962ac257`; the testing folder contains no exact before copy for this shared helper, so this review cannot claim a raw before/after hash match for it.

The preserved event diff shows the same caller random-min/span, cap-factor, divisor, and generic registration-effect lines around the newly inserted deterministic protection calculation. The chemical-state diff removes terminal hazard from stored class-rate construction, while the new helper applies it once to the caller-owned percentage. No AI weights, `ai_chance`, `random_list` weights, or custom pool definitions were added or changed by this tranche.

The parent handoff reports a 125-case source harness and 32 matched unprotected cases across all four agent classes, four stages and both terminal states. Its test VM substitutes exactly `0.5` for each `set_temp_variable_to_random` call and counts both draws; those fixtures show before/after source outcomes agree under the same declared draws. This is deterministic source-fixture preservation evidence, not sampling of the game RNG or proof of its distribution. Protected outcomes are intentionally different because the deterministic mask/hospital and terminal inputs change.

## Remaining probability limits and disposition

No empirical campaign odds are established. The available docs provide the native draw range but not a distribution law, stream independence or seeding contract, and the MCP adapter does not model these numeric effects. The current scenario/campaign state distribution is also undeclared. The source harness covers representative fixed draws only.

AI score validity, candidate dominance, starvation and rank reversal are not applicable to this reviewed surface; no AI willingness score, `ai_chance`, weighted pool or random-list selection is present in the continuing-protection change.

No balance or gameplay fix is recommended from the probability evidence. Keep the native RNG calls, outbreak random-min/span, cap inputs and same-mask multiplier floor as authored unless a separate accepted design supplies a native-distribution target. Do not replace the calls with a normalized weighted pool. If precise odds become a design requirement, first obtain an authoritative native distribution contract or a validated analyzer adapter for numeric random-value effects; any future campaign claim must still account for state inputs, deterministic percent/multiplier, rounding and cap.

The initial adapter receipt is missing from its requested folder; the primary handoff's narrative is the only retained record of that first failure. The single corrected direct-random inspection is preserved. A source-lookup request initially exceeded the live `maxLines=80` limit, was corrected once, and returned the definition start through line 3623; the remaining helper body was read from the local source at lines 3624-3707. No helper expansion, job, native task, game launch or log action was used.

The parent-reported service status is HOI4 MCP 3.10.0 over stdio; the status resource does not expose client task negotiation. No async delivery route was used.

Skills used: `.agents/skills/chaos-redux-subagents/SKILL.md` guidance was applied from the existing session context. No skill was created or changed.
