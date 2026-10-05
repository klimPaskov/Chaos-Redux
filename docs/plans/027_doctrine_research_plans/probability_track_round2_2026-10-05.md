# Event 027 track and Grand Doctrine fit, probability evidence, 2026-10-05

Disposition: implemented (decision D19 in `agent_decisions_2026-10-04.md`). The evidence covers the track `random_list` in `doctrine_research_ai_choose_scored_track` (`common/scripted_effects/027_doctrine_research_ai_effects.txt:448`, entries 2 to 19) and the Grand Doctrine `random_list` in `doctrine_research_ai_choose_scored_grand` (line 249, entries 2 to 14). Validation limit: the score vectors are traced from source for the qualitative scenario states below; they are not native country readings.

Baseline: the before vectors are traced from the scorers at HEAD `4e2ea76b8` (D16 state); the after vectors from the D19 source. Both `random_list` blocks are unchanged by D19, so the comparison is the same scenario IDs evaluated with the before and after vectors; `hoi4.probability_compare` is not applicable for the reason recorded in `probability_native_preferences_2026-10-05.md`. The scenario files are `probability_track_round2/track_scenarios.json` and `probability_track_round2/grand_scenarios.json`.

## MCP route

`hoi4.probability_evaluate`, adapter `random_list`, selector `{ path }`, explicit candidate pools `...:448.entry.2` to `entry.19` and `...:249.entry.2` to `entry.14`, workspace `mod_chaos_redux_ea3b2d67c2c0`, source hash `9f01e630856516b526d0ef4ee12aeb2ac74681de4850591d4fdb3cc624446c1b`. Every run returned `PROBABILITY_ANALYZED`, complete pool, 0 unresolved. The only diagnostics are `PROBABILITY_STARVED_OUTCOME` warnings for candidates of other domains, which are invalid in each scenario (weight 0).

| Run | Analysis ID | Scenario hash | Source revision |
| --- | --- | --- | --- |
| Track, 28 scenarios | `probability-0d64502a80a1ed77cf016732` | `5036c19ee4b27c0a6e7709e573885274916623b1d62e7f283d56997a0b8a355c` | `952933a3ac85334931e5c1add1b398f9f6a07b77f6fe0d747fe692ecc9fdb759` |
| Track, last 6 after-scenarios | `probability-118a2fd43d7ac254d6dc67d2` | `0a9a15f024905ddb8228f9d3313dfd85bd673aabf76612d6b6a65e1537486718` | `39148d300e150f63175e623f3a24dd2892d0018983a5ffb314c8f3afa131f681` |
| Grand Doctrine, 8 scenarios | `probability-3188942c7063a03d8b239fc2` | `22f36389e50d20300e79bf8080b72c490db17f3c3a796c8c195e277e3f459de6` | `c2ba06134f771f9c79291a00c65a2bcf6e522515f722e8ae05b79ccc353acad0` |

The retrievable copy of the 28-scenario artifact (1.26 MB) is cut at 1 MB and keeps the first 22 scenarios, so the last six after-scenarios were evaluated again in their own run with identical states.

## Score model traced

Before (HEAD): every track scored base 1 plus divisions 2, military factories 2, dockyards 2, war 2, coast 2, faction 2, and domain strategy 2 (13 for the at-war major used below, 11 at peace), plus Chaos Warfare readiness 3, plus continuity 2, completion 3, and one force-fit term 2. Every Chaos Warfare track shared one force term (`cbrn_chaos_warfare_ai_has_viable_program`).

After (D19): base 1, force fit 3, investment 1 per level earned, empty-track fit 2, completion 3 (only with force fit), continuity 2, and the sum squared.

## Track results

Columns: Infantry / Combat Support / Armor / Operations (Army), or Hazard Assault / Contaminant Fire Support / Toxic Armored Warfare / Integrated CBRN Command (Chaos Warfare).

| Scenario | State | Before | After | Weights after | Target |
| --- | --- | --- | --- | --- | --- |
| DR-C01 | Armour major at war; Armor level 4 with tanks; the other three tracks level 2 with fit | 23.8 / 23.8 / 28.6 / 23.8 | 15.7 / 15.7 / **52.8** / 15.7 | 36, 36, 121, 36 | Armor at or above 45%: met |
| DR-C02T | Armor level 4 without any armour templates; the other three level 2 with fit | 24.6 / 24.6 / **26.2** / 24.6 | 27.1 / 27.1 / 18.8 / 27.1 | 36, 36, 25, 36 | Irrelevant near-complete track no longer leads |
| DR-C03 | Land war; Operations empty; Infantry and Armor level 2, Combat Support level 1, all with fit | 25 each | 27.1 / 18.8 / 27.1 / **27.1** | 36, 25, 36, 36 | Empty Operations competes at the top |
| DR-C04 | Four tracks level 2 with fit, first choice | 25 each | 25 each | 36 each | Each between 20% and 30%: met |
| DR-C04.second | Same, after the first choice advanced Armor to level 3 | 24.2 / 24.2 / 27.4 / 24.2 | 19.0 / 19.0 / 42.9 / 19.0 | 36, 36, 81, 36 | Some stacking, frequent spread |
| DR-C05 | At war; Armor level 4 with tanks; Infantry level 1 with fit; Combat Support level 1 without artillery; Operations level 1 | 24.6 / 21.3 / 29.5 / 24.6 | 14.3 / 2.3 / **69.1** / 14.3 | 25, 4, 121, 25 | Dominant at or above 50%: met |
| DR-D03 | Chaos Warfare just established, all tracks empty, protection detachments fielded only | 25 each | **92.3** / 2.6 / 2.6 / 2.6 | 36, 1, 1, 1 | Hazard Assault highest: met |
| DR-D03-HQ | DR-D03 with an HQ operations section | 25 each | 48.6 / 1.4 / 1.4 / 48.6 | 36, 1, 1, 36 | Integrated CBRN Command competes |
| DR-D04 | Integrated CBRN Command level 2 with HQ section; Hazard Assault level 1 with protection detachments; the other two empty without battalions | 25 each | 39.7 / 1.6 / 1.6 / **57.1** | 25, 1, 1, 36 | Integrated CBRN Command highest: met |

### DR-E04 sequence

Evolution IV batch at peace: Armor empty with tank templates, Infantry level 2 with fit, Combat Support and Operations level 1 without fit. Each row is the Armor share at that choice when every earlier choice went to Armor.

| Choice | Armor state | Before | After |
| --- | --- | --- | --- |
| 1 | empty | 27.1 | 45.0 |
| 2 | level 1, continuity | 30.0 | 52.7 |
| 3 | level 2, continuity | 30.0 | 59.3 |
| 4 | level 3, continuity | 30.0 | 64.8 |
| 5 | level 4, continuity, completion | 34.0 | 79.3 |
| All five in Armor (product) | | 0.25% | 7.2% |

This is a close-score case, because Infantry also fits; the spec asks that completion be possible, not guaranteed. Without an Infantry template the same sequence completes the branch in about 30% of batches (36 against 9, 4, 4 at the first choice).

## Grand Doctrine results

Columns: Mobile Warfare / Superior Firepower / Grand Battleplan / Mass Assault (Army); Fleet in Being / Convoy Raiding / Base Strike (DR-B04).

| Scenario | Before | After | Weights after | Target |
| --- | --- | --- | --- | --- |
| DR-B01 mobile armoured major | 26.1 / 26.1 / 24.6 / 23.2 | **45.5** / 27.3 / 18.2 / 9.1 | 5, 3, 2, 1 | Mobile or armour Grand Doctrine highest: met |
| DR-B02 infantry-heavy minor | 0 / 0 / 51.5 / 48.5 | 0 / 0 / 57.1 / 42.9 | 0, 0, 4, 3 | Ordering unchanged: met |
| DR-B02-major | 22.2 / 25.4 / 27.0 / 25.4 | 9.1 / 27.3 / 36.4 / 27.3 | 1, 3, 4, 3 | Ordering unchanged: met |
| DR-B04 minor naval adoption | 7.3 / 85.4 / 7.3 | 3.1 / 93.8 / 3.1 | 1, 30, 1 | Ordering unchanged: met |

## Positive-weight checks

- Every valid track starts at the base weight 1 and only adds non-negative terms before squaring, so its weight is at least 1. Invalid tracks keep weight 0 because the chooser scores only tracks with a valid action.
- Grand Doctrine scores start at the base weight (Grand Battleplan at its native base) and only add or multiply by the native factor 10; the minor zero for Mobile Warfare and Superior Firepower is unchanged from D16.
