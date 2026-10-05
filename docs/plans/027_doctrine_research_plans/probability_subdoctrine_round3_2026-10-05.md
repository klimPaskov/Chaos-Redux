# Event 027 subdoctrine candidate scoring, probability evidence, 2026-10-05

Disposition: implemented (decision D25 in `agent_decisions_2026-10-04.md`). The evidence covers the subdoctrine `random_list` in `doctrine_research_ai_choose_scored_subdoctrine` (`common/scripted_effects/027_doctrine_research_ai_effects.txt`, line 2639 before and line 1879 after, entries 2 to 108). Validation limit: the score vectors are traced from source for the qualitative scenario states below; they are not native country readings.

Baseline: the before vectors are traced from the subdoctrine chooser at HEAD `f38b4702a` (the D16 scorer: shared base, factory, dockyard, war, coast, faction, track force, owner readiness, level-1 investment, and level-4 completion terms on every candidate, then the own-fit term and the native factor). The after vectors are traced from the D25 source. The scenario file is `probability_subdoctrine_round3/subdoctrine_scenarios.json`; DR-C07, DR-C07-NOR, and DR-C07-N keep the states of `probability_native_preferences_2026-10-05.md`, and DR-C07-A2 and DR-C07-A4 are new.

## MCP route

`hoi4.probability_evaluate`, adapter `random_list`, selector `{ path }`, the complete 107-entry candidate pool, every weight declared, workspace `mod_chaos_redux_ea3b2d67c2c0`. Both runs returned `PROBABILITY_ANALYZED`, analysis status complete, 0 unresolved. The only design diagnostics are `PROBABILITY_STARVED_OUTCOME` warnings: 495 before and 499 after, almost all for candidates of other tracks that are invalid in each scenario (weight 0); the four added warnings are valid candidates left at the base weight after the change, which is the intended bounded randomness.

| Run | Analysis ID | Scenario hash | Source hash | Source revision |
| --- | --- | --- | --- | --- |
| Before, 5 scenarios | `probability-10e903b7e362b7b839f4ae0b` | `848cbf66671df9def3fdc17712f877dd653031558f1096f43d1b39a9c17d73fa` | `bb2c5cd19436d889cd00d848f1ac1a8590f8da756e53af6f99ba482228c5e690` | `ea214007a89f5c4d0e6882ef2d200d4f69bdb16853c9b49466d16adb1b97d12f` |
| After, 5 scenarios | `probability-361eeb470944becef1cf8d56` | `0ed3133d388e61ee4ca72f4ff9dff1ea67559d31e1e67ba26bbd8fb3f25f16ce` | `8e7439436b69c290aedc2f229bc0ef5f0c217ec35892ea2b4fa0a78058567737` | `38ca436a9b691d7953189c545f1ec351c5e62b7f49c3388f9fefd4069580a963` |

The analysis artifacts are 1.39 MB each, above the 1 MB retrievable limit, so the percentages below apply the adapter's `proportional_categorical` rule to the declared weights, as in the earlier rounds.

Route notes:

- `hoi4.probability_inspect` (adapter `random_list`, selector `{ path }`) returned `INTERNAL_ERROR` with no artifact, as in the earlier rounds.
- A run with a partial candidate pool (only the eight Special Forces entries, `probability-90a7e5df0125d7ea263b2f28`) returned `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` and withheld normalised probabilities, so both recorded runs declare the full pool.
- `hoi4.probability_compare` rejected both selector forms tried for the frozen before snapshot (`{ path, snapshotPath, expectedSourceHash }` and `{ snapshotPath, expectedSourceHash }`, the snapshot held in the session scratchpad) with "Invalid tool arguments" before any analysis ran. It is also structurally limited here: the `random_list` block and its entry-to-subdoctrine mapping are unchanged, and the change lives in the score effects that feed the declared weight variables, so identical scenarios would yield identical results. The comparison is therefore the same scenario IDs evaluated against the before and after sources with their own traced vectors.

## Score model traced

Before: base 1, plus military factories 2, dockyards 2 (Navy), war 2, coast 2, faction 2, the track's shared force term 2 (Army) or Chaos Warfare programme term 2, owner readiness 3 (Special Forces adoption available, Chaos Warfare requirements met), level 1 reached 2, level 4 reached 3, continuity 2; then the own-fit term of `doctrine_research_ai_score_selected_subdoctrine_fit`, the native factor, and the base-weight floor. A typical at-war land-power candidate started at 11 shared points.

After (D25): base 1, plus investment 1 for every mastery level the subdoctrine has earned or banked, completion 3 when it is one level below its maximum, continuity 2, and the own-fit term (forces 2 for its own ship, plane, or battalion type; geography 2 for Marines on a coast and Mountaineers in mountains). The sum is squared, multiplied by the native factor, and raised to the base weight when below it.

## Results

| Scenario | State | Before | After | Weights after |
| --- | --- | --- | --- | --- |
| DR-C07 | Empty first Special Forces track, generic tag, mountaineer templates only, coast and mountains, at peace | Mountaineers 19.4% each, Marines 13.9% each, Paratroopers and Rangers 8.3% each | Mountaineers **34.7%** each, Marines 12.5% each, Paratroopers and Rangers 1.4% each | 25, 25, 9, 9, 1, 1, 1, 1 |
| DR-C07-NOR | DR-C07 for original tag NOR (minor) | Mountaineers I 63.4%, Rangers I 27.2%, Mountaineers II 2.5%, Marines 1.8% each, Paratroopers 1.1% each, Rangers II 1.1% | Mountaineers I **89.8%**, Mountaineers II 3.6%, Rangers I 3.6%, Marines 1.3% each, Paratroopers and Rangers II 0.1% each | 625, 25, 9, 9, 1, 1, 25, 1 |
| DR-C07-N | Empty Screens track, major, destroyers only, dockyards, coastal, at peace | the six destroyer subdoctrines 14.5% each, Anti-Aircraft Cruisers 11.3%, Torpedo Primacy 1.6% | the six destroyer subdoctrines **16.1%** each, Anti-Aircraft Cruisers 1.8%, Torpedo Primacy 1.8% | 9, 9, 9, 1, 1, 9, 9, 9 |
| DR-C07-A2 | Empty Army Infantry track, generic major at war in a faction, coastal, infantry templates without militia or irregulars, not communist, Defensive Postures banked at level 2 | Defensive Postures 20.2%, Mobile Infantry, Large Unit Tactics, Assault Infantry, and Great War Infantry 17.1% each, Mounted Infantry 8.5%, Commandos and Irregulars 1.6% each | Defensive Postures **56.2%**, every other valid candidate 6.2% | 1, 9, 1, 1, 1, 1, 1, 1 (People's War invalid, 0) |
| DR-C07-A4 | DR-C07-A2 with Defensive Postures banked at level 4 | Defensive Postures 23.7%, the four neutral candidates 16.3% each, Mounted Infantry 8.1%, Commandos and Irregulars 1.5% each | Defensive Postures **90.1%**, every other valid candidate 1.4% | 1, 64, 1, 1, 1, 1, 1, 1 |

Reading:

- The fitting or banked subdoctrine leads clearly in every scenario. Before the change, a banked Defensive Postures led its neutral rivals by 20.2% to 17.1%; it now leads by 56.2% to 6.2%, and a branch one step from completion is finished in nine choices of ten.
- Native-zero candidates (Torpedo Primacy, Commandos, Irregulars without militia or irregular templates) and Mounted Infantry with its 0.5 major factor keep exactly the base weight 1, so every valid choice stays possible.
- Anti-Aircraft Cruisers now sit at the base weight in a navy without cruisers, instead of 11.3% from the shared dockyard, factory, and coast terms.
- NOR's native Rangers I preference without ranger battalions now weighs the same as one fitting neutral candidate squared (25), so country identity still counts but no longer outweighs a candidate the country fields.

## Positive-weight checks

- All 107 candidate blocks keep their validity `limit` unchanged; an invalid candidate keeps weight 0.
- Every valid candidate starts at the base weight 1 before squaring, so its square is at least 1, and `doctrine_research_ai_score_selected_subdoctrine_fit` raises any product below the base weight to the base weight.
- Chaos Warfare tracks hold one subdoctrine each, so their single-candidate pools are unaffected by the removed terms.
