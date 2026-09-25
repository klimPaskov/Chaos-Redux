# Hospital Protection AI Cost Post-Edit Comparison

Date: 2026-09-25. Status: read-only post-edit weighted audit. The parent owns the gameplay change; this audit wrote only this handoff.

## Audited surface and source

Weighted surface: `decision_ai_will_do` for `cbrn_protect_hospitals_and_utilities` in `common/decisions/cbrn_protection_decisions.txt`.

The parent committed the payment-row change as `687e158b6`. The decision now uses zero native political-power cost, keeps `ai_hint_pp_cost = @CR_SC_CBRN_PROTECTION_DECISION_COST_PROTECT_HOSPITALS_PP_AI_HINT` (the file-scoped constant is 10), and gates `available` and `custom_cost_trigger` through `FROM.cbrn_state_hospital_payment_ready`. `custom_cost_text` is `cbrn_protect_hospitals_and_utilities_cost`. The `ai_will_do` block and its factors are unchanged.

Source-defined willingness operands remain base `cbrn_protection_ai.base_response = 8`, alert factor `cbrn_protection_ai.alert_factor = 5`, capital factor `cbrn_protection_ai.capital_factor = 3`, and high-population factor `cbrn_protection_ai.high_population_factor = 2` when target population exceeds `high_population_k = 2500`. These are exact source operands, not an effective score trace.

The current payment-ready trigger also requires the existing hospital-protection state and raid-alert gates, enough respirator and support-equipment stock, and actor political power at least `cbrn_protection_decision_cost.protect_hospitals_pp` (10). The completion effect rechecks readiness, debits the equipment, and removes the same 10 PP after successful equipment debits. These gates and costs are source evidence; the scenario adapter did not resolve them.

The relevant source paths are `common/decisions/cbrn_protection_decisions.txt`, `common/scripted_triggers/cbrn_protection_triggers.txt`, `common/scripted_effects/cbrn_protection_decision_effects.txt`, and `common/script_constants/cbrn_system_constants.txt`. Current local raw SHA-256 for the decision file at the compare call was `9adc49508ba698db8379a0501d014f9f7da504c9f8a6489e14c46f45fedec586`.

The baseline handoff records the required wiki and vanilla review: offline `Decision modding`, `AI modding`, `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, and `Idea modding`; installed `triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`; and vanilla `common/decisions/AUS.txt` custom-cost precedent. This follow-up also reviewed `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, the decision AI guidance in `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, the named fixture, and the baseline handoff.

## Scenario and pool

The exact saved scenario set is `cbrn_hospital_cost_baseline_2026_09_25` from `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_hospital_cost_probability_fixture.json`. Its scenario ids are `hospital_capital_high_population_raid_alert` and `hospital_noncapital_below_population_threshold_raid_alert`. Both use actor `CXT`, a top-level `cbrn_chemical_raid_alert_active` flag, and target `FROM` primitives for capital status, population, and actor control.

The supplied candidate pool is the single named decision. Post-edit inspect reported `poolComplete=true`, one candidate, zero statically available candidates, two required inputs, and zero inspect-time unresolved items. This means the named one-candidate source pool was accepted; it does not establish a complete category-wide in-game decision race. The adapter provides willingness scores and does not normalize them into click probabilities.

External factors are incomplete. The fixture cannot bind the top-level alert flag to `FROM.has_state_flag`, the target's scripted readiness triggers, the stored respirator and support-equipment cost variables, controller equipment inventories, or actor political power. No exact eligibility or payment result is supported.

## MCP evidence

The required first post-edit `hoi4.probability_inspect` used adapter `decision_ai_will_do`, source `{ path: "common/decisions/cbrn_protection_decisions.txt" }`, and the one-candidate pool. It returned `PROBABILITY_SOURCE_INSPECTED`, `sourceRevision=f86591e0f8fa5b1a472eeb045d191c1b5e4c90ac7ad63ccdb752110e0d576c1c`, and `sourceHash=fff03a92fdd48fa73adc2921471aec5eb8127b5c33c7a10e22da6914d304ee36`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c69fbb4e07fbb4134ddf69cb027eb24ea431ac91a4d9b011b5012c65d8a287d5/853df27bfce4a5db1f6eb86320da3f0bc4c399955138b6a2ce6a9523b290eade/probability-inspect-fff03a92fdd4.json`.

Post-edit `hoi4.probability_evaluate` used the exact saved scenario set, the same source path, and the same single-candidate pool. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-5623eba262854453ec7b4a97`, the baseline scenario hash `772dd922cf5c479579c053b0b86324fded3de4fce76a15cb60097c584159b279`, the post-edit source revision and hash above, two scenario/candidate rows, and two unresolved items. Its only diagnostic says `cbrn_protect_hospitals_and_utilities`'s alert factor is inactive in both supplied scenarios (`PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS`, decision source line 358). No effective score or actionable rank was returned.

Evaluation artifacts:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8af9026bfa911185e18c03fdf5e592ed6b9056064de2749a49e355dac499611d/897066b3e37c273b5819023eef958cb2ecfe2806609718e69ac49742a6fe8feb/probability-5623eba262854453ec7b4a97.json`
- Waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ba75360c56e551991ec95309b6ef2d2b31fc21e0b790f7089cacb3db712fa25/4a2798156c9b100887d532eb8230037bfc4f85477be763810e88b9b12d62f0f6/probability-probability-5623eba262854453ec7b4a97-waterfall.svg`
- Waterfall PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3930716dc4ae98fe5378420bc90a842cc51ae361ba8eeb5a691fae0f2f0b29ac/d5d72444b7558e0c1fa7dfa906aab361158261e6093b761fc59ced894dfd8d41/probability-probability-5623eba262854453ec7b4a97-waterfall.png`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e4f93435aa6ecf9b66edb85c0b6f1c9dce3c0ced78a30c31a0070b430e3214b/da56688b5d2c51a1773dbc71c6a454c6f4d1500f1866a28efde3742f64351db1/probability-probability-5623eba262854453ec7b4a97-unresolved.svg`
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3b2fca8b3c6a6a6bccb629d2893cbee45e69d16e11ea49ebae60663a3b9b18e/a8e62a04e52f695ba7d39d1e8533d9138e53a302b950cec80c816ff481b20918/probability-probability-5623eba262854453ec7b4a97-unresolved.png`

The single same-scenario `hoi4.probability_compare` call used the pre-edit `HEAD` file body as `before.inlineClausewitz`, the current decision path with expected raw source hash `9adc49508ba698db8379a0501d014f9f7da504c9f8a6489e14c46f45fedec586` as `after`, and the exact same candidate and scenario set. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-a569e2e7eee5c33e006bc13c`, `sourceRevision=818815074215ba9383f7deefe7d7e2b09d8184a4bd9ff0ff1fe0a95f6e755c5c`, post-edit `sourceHash=fff03a92fdd48fa73adc2921471aec5eb8127b5c33c7a10e22da6914d304ee36`, the same scenario hash, two reported comparison changes, four unresolved items, and one diagnostic for the inactive alert modifier. Its status was partial and it had no tool blockers.

The pre-edit source identity is not proven to match the saved baseline. The baseline path inspection recorded revision `7941450868f30a5995782a8c169915b4fb63b8cfd399d06f5518158b4fdc0530` and source hash `0d1e3655f3627c914f0de84d93daf057c1db7ce5a2ef56026a79d74bdb0651d6`. A separate inspect of the `HEAD` inline body supplied as the compare's before source returned revision `e86550e5a53c62445b3bbacbe5438395953879fea15ed83d0bda4063763fb3a4` and synthetic inline source hash `913c964f848acaef350e6adb0cc7b43dbccb67428573462d33bbdd3d45a5e460`, which differs from the baseline path hash. The baseline handoff's pre-edit local raw SHA-256 was `D849CE9FBD2BFDF866525A8F2C522911D9B50E90087B4761215571D8814DE0CF`; raw `HEAD` bytes were `83a2be18e19d86a2a92e9c2fb000dcd50704ded11b6ce04c9a26295624905814`. The before-source mismatch may reflect source snapshot or line-ending differences, but the evidence does not resolve that. Do not attribute the two compare changes to the parent's patch as a proven before/after delta.

The comparison's JSON, ranking, comparison, and unresolved artifacts were returned directly by `probability_compare`:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/507668890f63a912c29034776a96d8debb435ae1ad12ac4d604b3541d57a3f14/e8be980286e07a5274f1a50405b2a1f79b02119af9fe51253f0ae622f49584fe/probability-a569e2e7eee5c33e006bc13c.json`
- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8916411045dfb2d0d7c8d9f03fe022c170bb477e82888d52e122c8cd0c5962bd/8e91b1ba121366ee4eadf58cf41cfe8bd5ed7d487772c964f90b871ae6ea2dab/probability-probability-a569e2e7eee5c33e006bc13c-ranking.svg`
- Comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6f31542f9d8d245bb900186fb8f851194c64f6915d657b47ba860b9424fa136/c9948980d3f909e6afd5c5d82cdb13fc7fc54760b88f9530c9da12d3c7f7a09e/probability-probability-a569e2e7eee5c33e006bc13c-comparison.svg`
- Comparison PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab37e234b5bb21225f81c8ca2d398cfb209bb33083cb87d61b1bf03fcec84fb7/95032c36fd2a1bce71938f82f42741f72ca0f18bf3d877b8a9d267937aee1400/probability-probability-a569e2e7eee5c33e006bc13c-comparison.png`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc821319eedd467807c7ba822c85e65e31548714fdc49d0fb37857b3ca8b591f/d0dbcefc1c64008361ff878cb18fd594ee1d430dc4b7014d4a26ad5990bbceb5/probability-probability-a569e2e7eee5c33e006bc13c-unresolved.svg`
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec0679e605fe566fccd35107debd23f8ab672aac881c2a7398feb23d8974f0ac/e0606bb9f587c7d12bb06650ffcb46552a5e1bdcc3086512f86ae0e27bcca1e8/probability-probability-a569e2e7eee5c33e006bc13c-unresolved.png`

A separate `hoi4.probability_render` request for the comparison analysis was attempted with the exact analysis id and scenario hash. It failed with `PROBABILITY_ANALYSIS_NOT_CACHED` and blocker message `Render requires an analysis ID produced by this server process`; no retry was made. The comparison call itself had already returned the rendered views listed above.

## Result classification and findings

- **Exact source operands:** base 8, alert factor 5, capital factor 3, and high-population factor 2 above 2500 target population. No post-edit effective score or score modifier waterfall values are established by the returned summaries.
- **Score-only:** `decision_ai_will_do` is willingness scoring. The one-candidate supplied pool cannot establish category-wide rank, selection probability, or click probability.
- **Unresolved eligibility:** neither the pre-edit baseline nor the post-edit scenario proves alert binding, stock affordability, the new payment-ready gate, or PP affordability. Post-edit inspect reports zero statically available candidates, and evaluation says the alert factor was inactive in both fixtures.
- **Dominance, starvation, rank reversal, repetition, and exploit risk:** unresolved. No complete in-game candidate pool or eligible score race was analyzed. The compare's two reported changes are not attributable because the before-source hash does not match the saved baseline source hash.
- **AI validity:** source review shows the original readiness predicate remains nested in `cbrn_state_hospital_payment_ready`; the parent added equipment and PP readiness checks to `available` and `custom_cost_trigger`, while retaining the AI factors and 10-PP hint. Runtime validity remains unproved by MCP because the target-scoped alert and live inventories are not represented by this fixture.

## Recommendations and skipped analysis

Do not retune the four AI willingness operands from this result. Keep the factors as source-defined until an adapter scenario can bind the target-scoped raid alert, stored hospital costs, controller stockpiles, and actor PP. If that adapter support becomes available, rerun the saved named scenarios with a verified before-source snapshot and the same candidate pool before making an AI balance claim.

`probability_sweep` was skipped because the parent changed cost and eligibility fields, not an AI threshold or weight, and the saved fixture cannot evaluate the new gate. No uncertain-input distribution was declared, so `probability_simulate` was not applicable. This is not a manifest-declared dynamic pool, so `probability_sequence` was not applicable. No live-game validation was performed.

## Files owned and remaining blockers

Only this comparison handoff was written by the auditor. The exact unresolved limitation is the mismatch between the baseline path hash and the available pre-edit inline source hash; the exact MCP render blocker is `PROBABILITY_ANALYSIS_NOT_CACHED`. No source patch or AI balance claim was made.
