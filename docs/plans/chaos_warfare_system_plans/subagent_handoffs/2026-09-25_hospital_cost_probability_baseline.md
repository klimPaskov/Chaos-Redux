# Hospital Protection Probability Baseline

Date: 2026-09-25. Status: pre-patch, read-only weighted audit. No gameplay, AI, or localisation files were changed. Parent owns the cost-row patch and the post-patch probability comparison.

## Audited surface and sources

Weighted surface: `decision_ai_will_do` for `cbrn_protect_hospitals_and_utilities` in `common\decisions\cbrn_protection_decisions.txt:338-358`.

The AI block uses `constant:cbrn_protection_ai.base_response` with three multiplicative modifiers: `alert_factor` when target `FROM` has the active chemical raid alert, `capital_factor` when `FROM` is a capital, and `high_population_factor` when `FROM.state_population_k` exceeds `high_population_k`.

The decision has native `cost = constant:cbrn_protection_decision_cost.protect_hospitals_pp` (10 Political Power), an availability/target gate through `cbrn_state_can_protect_hospitals_and_utilities`, and a hidden effect that applies protection and debits the two equipment charges. Its current completion tooltip names both variable charges but does not display them as an iconized payment row (`localisation\english\cbrn_protection_l_english.yml:59-61`).

Source revisions and local SHA-256 values at inspection:

| Source | Role | Local SHA-256 |
|---|---|---|
| `common\decisions\cbrn_protection_decisions.txt` | AI weight, target, availability, PP cost | `D849CE9FBD2BFDF866525A8F2C522911D9B50E90087B4761215571D8814DE0CF` |
| `common\script_constants\cbrn_system_constants.txt` | AI factors, population threshold, equipment cost ratios and clamps, durations | `4EA5BC73CE0D689CB126A37A56F5A55DFF34F945F92119778C519DE4BE1C8E4F` |
| `common\scripted_triggers\cbrn_protection_triggers.txt` | Exact-state and equipment affordability gates | `0A1D43DAAAAB35292BE092E6D080F10D7921FFECC644542A79F6E9633FCFF18C` |
| `common\scripted_effects\cbrn_protection_decision_effects.txt` | Dynamic quantity calculation, debit, protection application | `159FB58CF64FCFF1CF72F44749445458CFC107F2C67EBCF2CBD29F83A7C390CB` |
| `common\scripted_effects\cbrn_protection_effects.txt` | Respirator stock refresh and oldest-first model debit | `021F5F19DE0BA4BCB615411531ECE7A9BCE2A3E6D3346B46D218F553D7B2BD15` |
| `localisation\english\cbrn_protection_l_english.yml` | Current player-facing effect text | `5D261A32FBD8E9E30E7969BEE6F92CD71E4587BE3B8D68B018B2A45343408B43` |

I consulted `AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, the required offline wiki core pages including Decision modding and AI modding, and the installed HOI4 markdown documentation. Relevant references were the offline `Decision modding`, `AI modding`, `Triggers`, `Effects`, `Modifiers`, `Data structures`, `Scopes`, and `Localisation` pages; installed `triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`. Vanilla's `common\decisions\AUS.txt` around its `custom_cost_trigger` / `custom_cost_text` use was consulted as a payment-row precedent.

## MCP evidence and scenario

The required first weighted pass was `hoi4.probability_inspect` on adapter `decision_ai_will_do`, source `{ "path": "common/decisions/cbrn_protection_decisions.txt" }`, with candidate pool `["cbrn_protect_hospitals_and_utilities"]`. It succeeded with `poolComplete=true`, `candidates=1`, `availableCandidates=0`, `requiredInputs=1`, and `unresolved=0`. MCP `sourceRevision` is `7941450868f30a5995782a8c169915b4fb63b8cfd399d06f5518158b4fdc0530`; MCP `sourceHash` is `0d1e3655f3627c914f0de84d93daf057c1db7ce5a2ef56026a79d74bdb0651d6`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/febcbcade5d2c6215ce654743d08ca59d2f422882414c0092520f8560c52d442/57718c6c35a8233d8434ddf54e5a3ec2cbbf935a884c27d8402856fe1705a00c/probability-inspect-0d1e3655f362.json`.

The exact typed `scenarioSet` request submitted to `hoi4.probability_evaluate` is saved at `docs\plans\chaos_warfare_system_plans\subagent_handoffs\2026-09-25_hospital_cost_probability_fixture.json`. Scenario ids are `hospital_capital_high_population_raid_alert` and `hospital_noncapital_below_population_threshold_raid_alert`; the single candidate is the decision above. The request followed the installed contract `{ id, scenarios: [{ id, actor, state, flags, scopes }] }` and added no fixture or variable-declaration fields.

Evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, `analysisId=probability-8be1f89ad12404e8315d77c7`, `scenarioHash=772dd922cf5c479579c053b0b86324fded3de4fce76a15cb60097c584159b279`, `sourceRevision=7941450868f30a5995782a8c169915b4fb63b8cfd399d06f5518158b4fdc0530`, and `sourceHash=0d1e3655f3627c914f0de84d93daf057c1db7ce5a2ef56026a79d74bdb0651d6`. It analyzed two scenario/candidate pairs and returned four unresolved items. Diagnostic `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` says the decision was never eligible in the supplied scenarios; `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` says the alert modifier was inactive in both. These are fixture-binding results and do not establish that the decision is unavailable in normal play.

The evaluator's source-linked JSON, waterfall, and unresolved views were rendered with the same scenario hash. Rendered resources:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73ba482631043e7a7ef8b555cc0e523f9ab24d86e8f4de3e6e04d6cd9ae66d1a/42a693d7b2c7fc0f70f38a5087cae1f9c4a896a4fcd39de874757375aa45c314/probability-8be1f89ad12404e8315d77c7.json`
- Waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0757da58067fb41a779ffd617277de9d90fb28dfd216d94bab979724fb1dabbe/e237ec20956088081c5b41c066a5f54a929f68e7cd742ae3553f78a862856c93/probability-probability-8be1f89ad12404e8315d77c7-waterfall.svg`
- Waterfall HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b900ddf7a376a4429031d3f5b0dd251751e3e7c8dfc433149b51f23b895ca016/8daae8b690068535e09336d3daf5aca469b1634ee59ca53f86d300823f140dfa/probability-probability-8be1f89ad12404e8315d77c7-waterfall.html`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/854b7b4558699310324288b1138400d4561bd654e4768d709911cd062cff4d71/e0743958f32159a7b4694cbebbe0943e56420e855a35d1cb15fa8c20351a9cdb/probability-probability-8be1f89ad12404e8315d77c7-unresolved.svg`
- Unresolved HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b45d2af33411f4d4ffc661e43de611e1472e3d0843b44dfee414609aee2d9ae/c4ae96f2fbcee4db0066832fe57d1495c94cb30d3738ae6c72b4445e21759047/probability-probability-8be1f89ad12404e8315d77c7-unresolved.html`

The decision score's candidate pool is complete for this one named surface according to inspect. The adapter did not prove a complete family-wide decision selection race, and no normalized probability or click probability is claimed. External factors are incomplete: the supplied alert flag did not bind to target scope `FROM`; target ownership/control, the `cbrn_response_hospital_mask_cost` and `cbrn_response_hospital_support_cost` Clausewitz state variables, and equipment inventories are not represented by the accepted primitive scenario fields. The current evaluation therefore proves no effective score or runtime affordability result.

## Baseline values and source path

| Component | Source-defined value or condition | MCP trace/classification |
|---|---|---|
| Base AI score | `base_response = 8` | Source fact only; no effective score returned |
| Raid alert modifier | Factor `5` when target `FROM` has `cbrn_chemical_raid_alert_active` | MCP says unsatisfied in both declared scenarios; unresolved fixture binding |
| Capital modifier | Factor `3` when target `FROM` is capital | No usable modifier trace returned |
| Population modifier | Factor `2` when target population exceeds `high_population_k = 2500` | No usable modifier trace returned |
| Combined AI score | Multiplicative `ai_will_do` score | Unresolved; do not interpret as a probability |

`cbrn_state_can_protect_hospitals_and_utilities` requires the target state to be controlled by the decision actor, to have the exact active chemical raid alert, not to have `cbrn_hospitals_utilities_secured`, and to have sufficient controller stock. Alert registration calculates respirator cost as target population × `0.03`, clamps to `10..400`, and rounds; Support Equipment cost is population × `0.01`, clamps to `20..300`, and rounds. The state stores those values. The trigger checks both equipment requirements against the controller's inventory. The hidden effect debits respirator stock oldest-first across models and then Support Equipment; protection is applied only if both completed debits meet their stored requests. Native PP cost is 10.

The score is a willingness score, not a click probability. MCP returned no ranking, effective score, timing distribution, or rank reversal because the sole candidate was ineligible in both scenarios. No dominance, starvation, or normalized-selection conclusion is supported by this result.

## Validity, repetition, and patch recommendations

Source-level target and resource gates are aligned with the two equipment debits for the same state and controller; the MCP scenario could not verify live stock, so this is source evidence only. The AI has no separate stock factor: scarce or insufficient equipment blocks availability, while an eligible target receives the target-state AI factors. Do not tune or compare these factors as if they were probabilities.

The decision re-enable delay and the secured-state protection duration are both 14 days. The raid alert can remain active for up to 30 days. A target may therefore become eligible for a second paid activation at day 14 if the alert continues. This may be an intended protection refresh; no sequence or exploit test was run, so repeat frequency and the intended refresh behavior remain unresolved.

Recommended bounded patch: display the existing state-specific respirator and Support Equipment quantities beside the native 10 PP cost using the same stored values as the availability check and debit, and keep visible affordability tied to the same controller stock requirements. Preserve the existing base and three AI modifiers unless the parent explicitly chooses a balance change. If the patch changes availability or target eligibility, run `hoi4.probability_compare` using these exact named scenarios and record that the current fixture does not bind the target alert or Clausewitz cost variables; do not treat a repeat of this partial scenario as balance proof.

## Skipped analysis and blockers

`hoi4.probability_sweep` was not run at the parent's direction; this is a one-candidate pre-patch baseline with unresolved eligibility binding, so no threshold or sensitivity conclusion is made. `hoi4.probability_simulate` was not used because no uncertain-input distribution was declared. `hoi4.probability_sequence` does not apply because this is not a declared dynamic weighted pool. `hoi4.probability_compare` is reserved for the parent-owned post-patch pass. No HOI4 launch or live-game test was performed.

Availability and stock evaluation remain unresolved under the connected scenario contract because it cannot bind the required target-scoped alert and dynamic Clausewitz cost/inventory values in this request. The parent should preserve this limitation with the fixture and compare handoff.
