# Event 012 Gods AI strategy activation repair — 2026-09-26

Disposition: **implemented with quantitative validation blocked**. This handoff records a source repair to five existing Gods of Africa AI strategy profiles. It does not approve new profile values or settle the broader Event 012 Part 8 focus-route scope.

## Design basis and scope

The strategy file already defines doctrine-specific host profiles and participant compliance/defiance profiles. The repair preserves each profile's existing effects and values; it changes only eligibility so runtime state can activate the profiles. The host active flag is committed by `gods_of_africa_activate_system` after consolidation, participant enrollment writes its flag during runtime initialization, and defiance is also written during play. The offline Paradox Wiki AI Modding page and vanilla `common/ai_strategy/_documentation.md` state that an AI strategy's `allowed` trigger is checked only before game start, while `enable` is checked continuously and `abort_when_not_enabled = yes` removes the strategy when its enable condition stops matching.

## Source change

In `common/ai_strategy/012_africa_gods_ai_strategy.txt`, removed the three host and two participant `allowed` blocks that depended on runtime flags. The five existing `enable` predicates and `abort_when_not_enabled` behavior remain. The file now documents why runtime activation belongs in `enable`.

| Profile | Existing strategy values retained |
| --- | --- |
| `africa_gods_host_reciprocal_ai` | `pp_spend_priority = 20`; `force_build_armies = 150` |
| `africa_gods_host_exaction_ai` | `pp_spend_priority = 35`; `force_build_armies = 250` |
| `africa_gods_host_ambiguity_ai` | `pp_spend_priority = 25`; `force_build_armies = 200` |
| `africa_gods_participant_compliance_ai` | `pp_spend_priority = 10` |
| `africa_gods_participant_defiance_ai` | `pp_spend_priority = -10`; `force_build_armies = 200` |

These are engine strategy modifiers, not selection probabilities. No numeric value was tuned. The current mechanic description is in `docs/events/012_africa/gods_of_africa.md`.

## Probability adapter evidence and limit

The required `hoi4.probability_inspect` baseline used adapter `ai_strategy_factor` on `common/ai_strategy/012_africa_gods_ai_strategy.txt`. It returned `status = ok`, `code = PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`, zero candidates, zero available candidates, and zero unresolved inputs. Source revision: `1131727e54d1d4c677a331f5a8d710c38ad56a06d23a03dc3b7aded7a6eacf59`; source hash: `3f37e05e6d555fe3e483b49d62f619ecd28905e73c12f5267e4286626a7957b9`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee33d1d4785d2d4fddbd69f99e0e635c554759b0f03ca3238250013e363f4db3/0fdd6db2335d34b803932e00df0a044d17bbe8d85f6e0212804be1c6f0a203bf/probability-inspect-3f37e05e6d55.json`.

The refreshed post-change inspect returned the same discovery status and zero candidates, available candidates, and unresolved inputs. Source revision: `f2fcc263aa6ad25c1504b889414b2f303dd2cf1688a3039f413d775b1a8a4a69`; source hash: `763acf72df105a6ac8708867519b41f92aff481e9b1fd800dfd515e473d540ca`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd4a260a8c891d7879b4eab2031494902e93ca8b3d7e7a1b5fbed6c83381163c/89f31ecd44984296e9ac3102d609099585fe02b6f3d706495919057d66feb0c2/probability-inspect-763acf72df10.json`.

`chaosx_ai_probability_auditor` confirmed that neither inspect provides a weighted candidate pool or supported scenario inputs, so it could not assemble a valid same-scenario `hoi4.probability_compare` call. No comparison was run, no strategy ranking or balance result is claimed, and no unsupported fixture was invented. This leaves quantitative acceptance of the profile effects blocked by the installed adapter.

## Remaining scope and validation limits

The source fix addresses the startup-only eligibility defect; it does not prove the game activates each profile or establish the effect of the retained strategy values. User-owned live-game validation remains outstanding. The accepted 24-node overlay, the protection cost split, AAT market access, enemy intelligence, and report-art mapping remain as documented in their accepted handoffs. The user's answer is still needed on whether the older Part 8 focus-route promises should return to active scope.

No numeric tuning, new strategy profile, focus-route expansion, fallback, or other gameplay change was made in this tranche.
