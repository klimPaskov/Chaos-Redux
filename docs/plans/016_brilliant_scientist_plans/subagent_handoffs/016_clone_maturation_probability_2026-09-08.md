# Event 016 clone maturation probability baseline — 2026-09-08

Status: `baseline_frozen_reviewable`. This is a read-only audit of the current live decision. No gameplay source, AI weight, helper, runtime, or architect file was edited, and no commit was created.

## Scope and source boundary

The audited surface is `brilliant_scientist_krg_run_bounded_clone_growth_cycle` in `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt:63-97`.

The helper boundary is `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`, and `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`.

The exact local before-source SHA-256 values and the complete named fixture are in [016_clone_maturation_probability_baseline_2026-09-08.json](../testing/016_clone_maturation_probability_baseline_2026-09-08.json).

The frozen live decision hash is `FEA4A7E178D945E15991B93543AF728B5F75FA84404B82664BFB6E4B4D488F7D`. The MCP canonical source hash is `a0ced8e1012917d90d1273cf075d52b4794322822af038517eb5365532a1240f`.

The unused architect files `common/script_constants/016_clone_maturation_constants.txt`, `common/scripted_effects/016_clone_maturation_effects.txt`, and `common/scripted_triggers/016_clone_maturation_triggers.txt` are explicitly excluded from this baseline, even though their local hashes are recorded in the fixture.

## MCP evidence

The required first call was `hoi4.probability_inspect`. The matching adapter is `mission_ai_will_do`, not `decision_ai_will_do`, because the source uses `days_remove` and is indexed as a mission-style AI surface.

The inspect result was `PROBABILITY_SOURCE_INSPECTED`, with one complete candidate at the source boundary, nine required inputs, zero unresolved inspector constructs, raw-score support, and no normalized probability or timing support.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be678c8cfb700339399f07d8637c629cfee6e2faca7b2e689f2d292f0794b834/3c9674502d99a6680b2dd916beedf5b34d319f2bd7d96bed3343f1087e598ca9/probability-inspect-a0ced8e10129.json`.

The source-only discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5ce95eefa1400e2f61a13c4f47cfbd021984002fd4cf84e5e7f69b7a22c8299/eb9f37e870548290e15ad999ad6aba8aff271ba51ea7e30f5af000a90dfca4a5/probability-inspect-a0ced8e10129.json`. The initial `decision_ai_will_do` request correctly returned the adapter mismatch and suggested `mission_ai_will_do`; that artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c67fa64b885583ef1a1aeb0840611eb8f8b03eec95b02b2ba541b8ce83d5e09b/94f2bcbf3e3b2a3acc7798d0457175349d99e3d2a2f4466ec6140f778151d55e/probability-inspect-a0ced8e10129.json`.

The full named evaluation used `E016_CLONE_MATURATION_2026_09_08`, 18 scenarios, one candidate per scenario, horizon one day, and the `raw_value` metric. It returned `PROBABILITY_ANALYZED`, analysis ID `probability-314acd3fccffec94341672b0`, source revision `7bab0d710f6c472f95622e01a5756d595643bd23cf922aa1b7b3d724d97801bf`, scenario hash `51307c304c7f2224d2cedee2be8d2faa4de4987b12144e5f4c3a0e458e97db86`, zero diagnostics, and zero unresolved items in the override fixture.

Evaluation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a526490f413b2472f91e855432b4d19653beb2e5f35296e6e32abdb65b40de0b/d44f1b8642e938de47984bf470c0c65fefc17dbfc08c2b7b65e5217430db8d5e/probability-314acd3fccffec94341672b0.json`.

The evaluate call emitted deterministic ranking, matrix, waterfall, and unresolved resources. The JSON fixture records the ranking and matrix URIs. A separate `hoi4.probability_render` retry for both the evaluation and sweep analysis IDs returned the exact blocker `PROBABILITY_ANALYSIS_NOT_CACHED` because render requires an analysis ID produced by the same server process. No separate render artifact is claimed.

The bounded sweep used the same 18 rows under `E016_CLONE_MATURATION_2026_09_08_SWEEP`, path `cycles`, explicit values `0`, `7`, `8`, and `9`, four steps, pairwise sensitivity, and rank-reversal detection. It returned `PROBABILITY_ANALYZED`, analysis ID `probability-19e1742f80c333f13cabf1d8`, source revision `f1aa1a7889b0a6a0dc75a2b329a049d9a8538fe6e0e29a34d8b3fd36eca956df`, scenario hash `5e65ac59308d9226e13d3a7f1effc25d219cc99f68d507e8030500b16b4275da`, 18 sweep points, zero unresolved items, and zero diagnostics.

Sweep JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc37697659b7a88f83d97217c6a47ab160682305cc90ed9729d34bb7fc6a9ad4/14fa5636b4e819ec4f611726a34b5884c03ecf8def89f0a3c1686d1df354cc18/probability-19e1742f80c333f13cabf1d8.json`.

Sweep sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51f7f515f314cd449504645d76f87652c25f5267c444cfaa587e16304d847bd5/e254b7de5bb205db6e42922018873a47d1b22a55b6b9e5db1793d57e288261aa/probability-probability-19e1742f80c333f13cabf1d8-sensitivity.svg`.

Sweep threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/6239cd2900d432c65ea5f9035c69c801d2bc6b8a720baf53667ea6bc809e3594/probability-probability-19e1742f80c333f13cabf1d8-threshold.svg`.

No `probability_compare` was run because no owner-applied patch exists. No `probability_simulate` was justified because no uncertain input distribution or seed was declared. No `probability_sequence` was justified because this is a native decision/mission score, not a complete custom weighted pool with declared cadence and terminal-state transitions.

## Scenario results

The candidate pool is complete only at the adapter’s source boundary and contains exactly one candidate. Since `mission_ai_will_do` is score-only, every result below is a willingness score and eligibility classification, never a click probability.

The exact owner/tech/valid-site/exact-affordability rows at cycles 0 and 7 score `1` and rank first because the sole candidate has base `constant:brilliant_scientist_krg_ai.medium = 1`.

The current hard cap makes cycles 8 and 9 ineligible. This is a source fact for the current baseline and conflicts with the accepted correction’s requirement to retain history threshold 8 without a lifetime paid-cycle cap.

The lost-site, no-tech, no-owner, short support, short motorized, short fuel, short manpower, short civilian-capacity, short military-capacity, and active/pending fixtures score `0` under their explicit candidate overrides.

The `E016_CLONE_MATURATION_CURRENT_RAID_BYPASS_NO_SITE_C0_PEACE` fixture scores `1`. This records the current `available` OR path through `brilliant_scientist_kruger_raid_ai_is_active`, which can bypass the growth-site flag. It is an exploit-risk fixture, not an endorsement of that route.

## Actual eligibility uncertainty

An unoverridden positive probe returned `PROBABILITY_ANALYZED_PARTIAL` with diagnostic `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` and 14 unresolved runtime/helper inputs. The adapter could not type the compound cloning-operational arrays, host/character/original-tag chain, equipment and fuel stockpiles, manpower variable, factory counts, and cycle variable from the flat scenario. This means actual campaign eligibility remains unresolved; the result does not prove the live decision is unavailable.

The unoverridden probe artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/520fdf9807d7f5023b636fdfd02a52744481071d0ac03eb315e3d883034e0a57/0c8276edd1edcb519021fadf5f22cb2acd41b4f3b38031db60111287771fe4c3/probability-411d1b001dffd0fa3cbd26b2.json`.

A second probe that added flat typed character, stockpile, factory, cycle, and array fields returned the same `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostic with 14 unresolved inputs. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae5fc641ec52b8c9620eb51ce0cdf825c66185618a54aa8650a16a2c8decadf6/2070bee673763f231e6ab41e41f9218ae9ba2ef137d306ca289a35a3fc464f45/probability-8453a198d20bce244e033221.json`.

The override matrix is therefore exact for the declared score fixtures but bounded for live eligibility. No exact selection probability is claimed, even though the one-candidate pool is complete, because the adapter does not model a mission click-selection denominator.

## Current source findings

The current completion effect produces 400 `infantry_equipment_0` and 40 `support_equipment_1`, increments the cycle variable, and sets clone-growth burden state. It does not produce the accepted `clone_equipment_1` receipt.

The current payment effect removes 150 support equipment, 50 motorized equipment, 1000 fuel, and 1000 manpower. The current trigger gates these old axes plus military factories and four available civilian factories. The accepted correction instead specifies 65 PP, 150 support, 1000 fuel, four native CIC, and one exact 100-clone-equipment receipt.

The current `available` block accepts either the cloning-operational trigger or the raid-AI-active bypass, and it checks a country flag rather than a typed owned-and-controlled growth site. The current `cancel_trigger` does not independently revalidate site ownership/control, so a lost-site or pending receipt can remain a source-level risk until the owner adds those guards.

The current `< clone_growth_cycle_maximum` gate hard-stops paid cycles at eight. The accepted correction retains history threshold 8 but removes a lifetime paid-cycle cap, so the post-patch compare must explicitly cover cycles 8 and 9 with an otherwise-valid receipt state.

The current AI base is `constant:brilliant_scientist_krg_ai.medium = 1`. This audit reports the source score and does not choose a replacement balance target.

## Recommended owner follow-up, not applied

1. Wire the accepted 100 `clone_equipment_1` receipt and the 65 PP, 150 support, 1000 fuel, four native CIC, 90-day duration, and 30-day cooldown contract through the owner’s implementation files.
2. Require an owned and controlled growth site at payment, completion, and pending/cancel boundaries. Remove or deliberately re-scope the raid-AI bypass so it cannot authorize a paid maturation without that site.
3. Keep history threshold 8 as history/pressure state while removing the lifetime paid-cycle cap. Preserve ordinary production and training behavior.
4. Add one exact receipt and an active/pending guard so one payment cannot produce duplicate completion.
5. After the owner patch, rerun `hoi4.probability_inspect`, `hoi4.probability_evaluate`, the same 18 scenario IDs, `hoi4.probability_sweep`, and `hoi4.probability_compare` with the before hash `FEA4A7E178D945E15991B93543AF728B5F75FA84404B82664BFB6E4B4D488F7D`. Keep all score-only and unresolved classifications.

## Skipped structural routes and remaining uncertainty

`hoi4.event_inspect` and `hoi4.event_render` were not run because this bounded surface is a decision/mission score audit, not an event-chain surface. The event route would not replace the required probability evidence.

The source adapter cannot certify live compound trigger state, site ownership/control, native production completion, cooldown/pending state, or the broader mission candidate pool beyond the indexed one-candidate surface. These remain unresolved until the owner supplies typed runtime fixtures or the adapter supports those constructs.

Parent wiring status: the baseline is frozen and reviewable; use the JSON fixture’s before hash and named scenario set as the preservation/compare contract. No gameplay files were changed by this handoff.
