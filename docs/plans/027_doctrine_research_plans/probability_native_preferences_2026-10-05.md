# Event 027 native doctrine preferences, probability evidence, 2026-10-05

Disposition: implemented (decision D16 in `agent_decisions_2026-10-04.md`). The evidence covers the Grand Doctrine `random_list` in `doctrine_research_ai_choose_scored_grand` and the subdoctrine `random_list` in `doctrine_research_ai_choose_scored_subdoctrine` (`common/scripted_effects/027_doctrine_research_ai_effects.txt`). Validation limit: the score vectors are traced from source for qualitative states; they are not native country readings.

Baseline: the before vectors are traced from `027_doctrine_research_ai_effects.txt` at HEAD `c065f4e31`; the after vectors from the D16 source. The scenario files are `probability_round2/grand_combined_scenarios.json` and `probability_round2/subdoctrine_combined_scenarios.json`.

## MCP route

- `hoi4.probability_evaluate` with adapter `random_list`, selector `{ path }`, and the explicit candidate pool of each `random_list` (Grand Doctrine: line 243, entries 2 to 14; subdoctrine: line 2623, entries 2 to 108) completed for both files. Workspace `mod_chaos_redux_ea3b2d67c2c0`, source hash `180d1281d53959bb3db7f63b3946eacec8fbda5b9bd862282b1d7617f9d49521`.
- A subdoctrine run that declared only the non-zero weights ended `PROBABILITY_ANALYZED_PARTIAL` with 99 unresolved items (`probability-d28dc912a1a4b48f09296121`); the complete run declares all 107 weights.
- The retrievable copy of the subdoctrine artifact (1.6 MB) is cut at 1 MB, which keeps the three before scenarios. The after rows below apply the adapter's `proportional_categorical` rule to the same declared weights; the before rows confirm that rule (7 of 56 = 12.5%).
- `hoi4.probability_compare` was not used: both `random_list` blocks are unchanged, and the change lives in the score effects that feed their weight variables, so the comparison is the same scenario IDs evaluated with the before and after vectors.

| File | Analysis ID | Scenario hash | Source revision | Status |
| --- | --- | --- | --- | --- |
| Grand Doctrine | `probability-3073104d02ab0bddedb3a99e` | `cea2d522af13503e3e98099bcebdb32eeebce7f7f3ef85ff3563054a5549acf8` | `6f7d068c0e7209beca3577aaf056cfab4f8291eeaf1e8e2b245090028f2241b7` | complete, 0 unresolved |
| Subdoctrine | `probability-f5be3a5b4624a7ace9ad0003` | `6e13d6cf5223c00131baac2c5a96d03e72cb8519851e2156afa6a5cdde2df053` | `ca37bac71a6526a300cfddf66a59c3dc43b0489c9e91b5ec601ec3d359d311e4` | complete, 0 unresolved |

## Grand Doctrine results

Columns: Mobile Warfare, Superior Firepower, Grand Battleplan, Mass Assault (Army scenarios); Fleet in Being, Convoy Raiding, Base Strike (DR-B04).

| Scenario | Before | After | Native reference |
| --- | --- | --- | --- |
| DR-B01 mobile armoured major | 25.7 / 25.7 / 22.9 / 25.7% | 26.1 / 26.1 / 24.6 / 23.2% | Grand Battleplan base 2; a mobile army no longer counts as infantry mass |
| DR-B02 infantry-heavy minor | 22.6 / 25.8 / 25.8 / 25.8% | 0 / 0 / 51.5 / 48.5% | `is_major = no` factor 0 on Mobile Warfare and Superior Firepower |
| DR-B02-major (same army, major) | 22.6 / 25.8 / 25.8 / 25.8% | 22.2 / 25.4 / 27.0 / 25.4% | factor 0 does not apply to a major |
| DR-B04 minor naval adoption | 31.6 / 36.8 / 31.6% | 7.3 / 85.4 / 7.3% | `is_major = no` factor 10 on Convoy Raiding |

Weights after: DR-B01 `18, 18, 17, 16`; DR-B02 `0, 0, 17, 16`; DR-B02-major `14, 16, 17, 16`; DR-B04 `12, 140, 12`. The analyzer's only design diagnostics are `PROBABILITY_STARVED_OUTCOME` warnings for candidates that are invalid in the scenario domain (weight 0), plus Mobile Warfare and Superior Firepower in the after-state DR-B02, which is the intended native minor zero.

## Subdoctrine results

| Scenario | Before | After |
| --- | --- | --- |
| DR-C07 empty first Special Forces track, generic tag, mountaineer templates, coast and mountains | 12.5% each of the eight tokens | Mountaineers 19.4% each, Marines 13.9% each, Paratroopers 8.3% each, Rangers 8.3% each |
| DR-C07-NOR same state, original tag NOR (minor) | 12.5% each | Mountaineers I 63.4%, Rangers I 27.2%, Mountaineers II 2.5%, Marines 1.8% each, Paratroopers 1.1% each, Rangers II 1.1% |
| DR-C07-N empty Screens track, major, destroyers only | 12.5% each | Convoy Escort, Support Integrated Operations, Hunter Killers, Screen Support Focus, Jeune Ecole, Patrol Boats 14.5% each; Anti-Aircraft Cruisers 11.3%; Torpedo Primacy 1.6% |

Weights after: DR-C07 `7, 7, 5, 5, 3, 3, 3, 3`; DR-C07-NOR `175, 7, 5, 5, 3, 3, 75, 3`; DR-C07-N `9, 9, 9, 1, 7, 9, 9, 9` (Torpedo Primacy has native base 0 and keeps the base weight; Anti-Aircraft Cruisers reads cruisers, which this navy lacks).

## Positive-weight checks

- `doctrine_research_ai_score_selected_subdoctrine_fit` ends every candidate at the base weight or above, so a native factor of 0 or 0.5 never removes a valid subdoctrine. All 107 candidate blocks call it after their shared terms.
- Grand Doctrine scores start at the base weight (Grand Battleplan at its native base) and only add or multiply by 10. The minor zero on Mobile Warfare and Superior Firepower applies only while Grand Battleplan or Mass Assault has a positive weight, so the Army pool never empties.
