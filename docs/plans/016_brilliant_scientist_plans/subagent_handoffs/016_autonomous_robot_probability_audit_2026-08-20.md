# Autonomous Robot probability audit

Date: 2026-08-20

## Scope and ownership

This is a read-only probability audit of the reusable Autonomous Robot technology family and Event 019 provider 505. No gameplay weights, eligibility conditions, outcomes, or AI behavior were changed.

The dedicated `chaosx_ai_probability_auditor` run did not return usable evidence and was interrupted after a bounded wait. The parent therefore completed the mandatory HOI4 MCP inspection and scenario evaluation directly. This handoff does not treat hand arithmetic as a substitute for MCP evidence.

## Reusable custom-technology pool

The audited selector is `chaosx_grant_random_custom_operational_technology` in `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`. It has seven base families: Portal Warfare, Clone Formations, Autonomous Robots, Paleogenetics, Xenobiology, Exotic Arms, and Temporal Guard. Each unowned family receives `constant:chaosx_custom_technology_tuning.random_candidate_weight`, whose current value is 1; an already-owned family receives zero weight.

Fresh `hoi4.probability_inspect` with the `random_list` adapter returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, seven candidates, seven required inputs, and zero unresolved inputs. Source hash: `c6523f553c75404f013d67dd9659b7bd7cc1adf775eed6672d814b797e1b465f`. Source revision: `f7640688dafc72fbf8ba0db3454b1a6d190185571a981e745e80b30d6bf1582e`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00893de0152c7cc6fbd3d4cafc4e280b2322c3243e47e796511bfa030acf43f1/669c7df25995a10ee5e4a8003acfaade90ca3b7cb2a0d2047964249c970d2b39/probability-inspect-c6523f553c75.json`.

The exact scenario set `E16_ROBOT_POOL_CONSTANT_EXACT_2026_08_20` returned `PROBABILITY_ANALYZED`, analysis `probability-c25bfe2ca9629aa57f8f1f69`, scenario hash `eba87f6ef9270320e3561a1d1c527b6d14376127fa2818c58a063c91074556e2`, 28 candidate-state projections, and zero unresolved inputs.

| Scenario | Autonomous Robot probability | Interpretation |
| --- | ---: | --- |
| `ROBOT_POOL_ALL_UNOWNED` | 1/7, or 14.285714% | All seven equal-weight operational families are candidates. |
| `ROBOT_POOL_ONLY_ROBOT_UNOWNED` | 1 | Robot Formations is the only remaining operational family. |
| `ROBOT_POOL_ROBOT_ALREADY_OWNED` | 0 | Duplicate robot grants are excluded; each of the other six families is 1/6. |
| `ROBOT_POOL_ZERO_ELIGIBLE` | undefined conditional probability | Every weight is zero. The adapter reports `PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO`; engine fallback behavior is not proved by this projection. |

Analysis JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25d663483880d67f82cbd416bf3bc639761882b35dd411d369111bcac7bf69a6/60c6e2a6f8c836e77b8c1d1b9ec2a7c2dfc2120e880e73515fc71c85221b02fe/probability-c25bfe2ca9629aa57f8f1f69.json`.

Ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a685294825714f30541d99ed557d4fb1d905adf219f8f16e5789312cc09c5834/f059195420fc4c60539dd4b9c7b403920da294344c42f266d1c3971e5574b3f0/probability-probability-c25bfe2ca9629aa57f8f1f69-ranking.svg`.

Scenario matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e28e907cd08272b1c4db3e8ced01e1e325c918e2a364d7efb36b4cb40c89947/ad70462fd58420a9e03441a99fc9df2c4733d85b88a9d72c28ae2bf7e5f3be44/probability-probability-c25bfe2ca9629aa57f8f1f69-matrix.svg`.

The zero-weight case is intentionally reported as unresolved engine behavior. The source comment states that the selector safely does nothing when all seven families are owned, but the probability adapter does not prove that final runtime fallback.

## Event 019 provider 505

Provider 505 registers the generic Autonomous Robot family with `constant:chaos_unit_family_event16_autonomous_robot.spawn_weight`, whose current value is 14. Eligibility is evaluated through `chaos_unit_family_provider_505_event19_evaluate_eligibility`; selection is performed by `infantry_spawn_select_native_registered_family` in `common/scripted_effects/019_infantry_spawn_core_effects.txt`.

That selector is not a native `random_list`. It iterates aligned global registry arrays, sums the eligible rows' dynamic weights, draws a temporary random value, and subtracts each eligible row's weight until a provider is selected.

Fresh `hoi4.probability_inspect` with `custom_weighted_pool` returned `PROBABILITY_SOURCE_INSPECTED`, source hash `44e72ead2c6f82f34a691948b2e036a4fe2e7db65060e496df6bcd22cf9fc9c0`, zero candidates, and `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5033da68a93c0eeb647f66dfa8c976a87c2f771f82b36508b4ed8527925d736d/22a81d99947ba8a821d57686ea83bcdddb4c03ef77db60ba7ccf587d7d7ca1ca/probability-inspect-44e72ead2c6f.json`.

The same source inspected with `direct_random` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and no usable pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a494ce90f91f437aa42841c00259a4df9f7cbed2e56b3eef5eafb75b1f25c44/4581da77b4fe9b81b983b1c66221d2f894b65981a449b24911a45b296dc925b9/probability-inspect-44e72ead2c6f.json`.

The intended scenarios `EVENT19_PROVIDER_ALL_ELIGIBLE`, `EVENT19_PROVIDER_505_ONLY_ELIGIBLE`, `EVENT19_PROVIDER_505_INELIGIBLE`, and a competing-provider weight sweep cannot be evaluated truthfully by the installed adapter because the manual array selector is not exposed as a declared custom weighted pool. No candidate manifest exists in the repository for this surface. Creating one only for an audit would duplicate the runtime registry and risk stale evidence, so no parallel probability ledger was introduced.

The only safe static statement is conditional: when provider 505 is eligible, its one-draw share is its weight 14 divided by the sum of all eligible registered provider weights at that moment. No whole-pool numerical probability is claimed because registry membership and eligibility are dynamic.

## Findings

- The reusable random-technology API gives Autonomous Robots the same base opportunity as every other unowned custom family and prevents duplicate robot grants.
- The scenario-bound zero and one probabilities are expected behavior, not starvation or dominance defects.
- Provider 505's configured spawn weight is 14, but the current MCP adapter cannot normalize or sweep the dynamic Event 019 registry selector.
- No balance target or probability-bearing source was changed in this tranche, so there is no before/after `probability_compare` claim.
