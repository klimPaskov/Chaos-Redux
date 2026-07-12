# RF-018-01 Cave Starting Strength Recalibration Handoff

Date: 2026-07-11  
Owner: `chaosx_scripted_system_architect`  
Status: core formula and duration helpers implemented; lifecycle call-site wiring completed by the concurrent event-chain owner and verified here.

## Scope

This handoff implements only improvement-loop item RF-018-01. It changes the centralized cave-strength constants and `resources_found_calculate_cave_starting_strength`, adds exact maximum-extraction duration helpers, and records deterministic regression profiles. It does not change decisions, focuses, assets, localisation, spreadsheets, events, or the achievement threshold.

## Implemented Formula

The cave score is clamped to `0..120`. Starting divisions are:

`6 + floor(score / 5)`, hard-capped at `30`.

The positive score is:

`max(total_resources - 720, 0) / 100 * 0.50`

`+ distinct_resources * 0.25`

`+ max(discoveries - 1, 0) * 2.50`

`+ maximum_yield * 0.25`

`+ maximum_depth * 0.25`

`+ min(maximum_extraction_months, 18) * 1.25`

`+ field_deaths / 10000 * 2.00`

`+ 12 if a full seal failed`

`+ 14 if military exploitation occurred`

`+ 5 if an unsealed nest remained`

The reductions are:

`max(workforce_safety - 40, 0) * 0.20`

`+ 8 for a successful evacuation`

`+ 7 for sealing the access network`

`+ min(total_suspension_days / 90, 3) * 4.00`

`+ min(successful_hunts, 4) * 2.50`

Completed and currently active suspension time both count. Maximum-extraction duration is recorded as exact accumulated days; finalization adds any live interval, converts days to 30-day scoring months, and caps the scored duration at 18 months.

## Band Mapping

| Score interval | Starting divisions | Intended profile |
|---|---:|---|
| `0 <= score < 25` | 6-10 | Minimal qualifying breach |
| `25 <= score < 65` | 11-18 | Developed or dangerous field |
| `65 <= score < 95` | 19-24 | Heavily exploited field |
| `95 <= score < 120` | 25-29 | Extreme, repeated, or military exploitation |
| `score = 120` after clamp | 30 | Capped extreme; preserves Thirty From Below |

## Deterministic Regression Profiles

All profiles use six distinct resources because Evolution III guarantees that diversity floor. `Flags / mitigation` lists only non-numeric inputs; suspension is shown in days and hunts as a count.

| Profile | Total | Discoveries | Peak yield / depth | Max extraction months | Deaths | Safety | Flags / mitigation | Suspension / hunts | Score | Divisions |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| Minimal direct Evolution III package, low roll | 720 | 1 | 10 / 40 | 0 | 0 | 60 | none | 0 / 0 | 10.00 | 8 |
| Minimal direct Evolution III package, high roll | 1200 | 1 | 10 / 40 | 0 | 0 | 60 | none | 0 / 0 | 12.40 | 8 |
| Protected qualifying breach | 900 | 1 | 15 / 45 | 0 | 0 | 85 | evacuation, sealed network | 180 / 1 | 0.00 | 6 |
| Developed | 1600 | 3 | 45 / 70 | 6 | 5000 | 45 | none | 0 / 0 | 47.15 | 15 |
| Dangerous developed | 1800 | 3 | 55 / 75 | 8 | 10000 | 40 | unsealed nest | 0 / 0 | 61.40 | 18 |
| Heavy exploitation | 2000 | 4 | 70 / 80 | 9 | 10000 | 35 | unsealed nest | 0 / 0 | 71.15 | 20 |
| Rich unmitigated history | 2200 | 4 | 75 / 85 | 10 | 10000 | 30 | unsealed nest | 0 / 0 | 75.90 | 21 |
| Heavy plus failed seal | 2200 | 4 | 75 / 85 | 10 | 10000 | 30 | unsealed nest, failed full seal | 0 / 0 | 87.90 | 23 |
| Mitigated heavy history | 2200 | 4 | 75 / 85 | 10 | 10000 | 85 | unsealed nest, evacuation, sealed network | 180 / 2 | 38.90 | 13 |
| Extreme military exploitation | 2500 | 5 | 85 / 90 | 14 | 20000 | 30 | unsealed nest, military exploitation | 0 / 0 | 104.65 | 26 |
| Extreme repeated exploitation | 3000 | 6 | 100 / 100 | 18 | 40000 | 20 | unsealed nest | 0 / 0 | 110.90 | 28 |
| Capped extreme | 3000 | 6 | 100 / 100 | 18 | 40000 | 20 | unsealed nest, military exploitation, failed full seal | 0 / 0 | 120.00 | 30 |

The mandatory all-six package's tonnage-and-diversity floors contribute only `1.50..3.90` score across its `720..1200` resource range: `1.50` from diversity and at most `2.40` from package tonnage. Those unavoidable resource inputs therefore cannot grant even one full bonus division on their own. With the opening's actual peak yield, depth, safety, and first free discovery included, the complete direct Evolution III opening produces 10.00-12.40 score and eight divisions.

The mitigation comparison is intentional: the same rich `2200 / 75 / 85 / 10-month` history falls from 21 divisions in the unmitigated heavy profile to 13 after high safety, evacuation, access sealing, 180 suspended days, and two hunts. These inputs therefore affect the outcome without weakening the six-division breach floor.

## One-Input Boundary Behaviour

Five score points always equal one division. Continuous inputs cross boundaries in stable increments:

| One-input change | Score change | Division-scale meaning |
|---|---:|---|
| +1000 resources above the package floor | +5 | +1 division |
| +2 repeat discoveries after the first | +5 | +1 division |
| +20 maximum yield | +5 | +1 division |
| +20 maximum depth | +5 | +1 division |
| +120 maximum-extraction days before the 18-month cap | +5 | +1 division |
| +25000 field deaths | +5 | +1 division |
| +25 safety above the 40-point floor | -5 | -1 division |
| +2 successful hunts before the four-hunt cap | -5 | -1 division |
| +90 suspension days before the three-period cap | -4 | usually -1 division; continuous partial periods avoid a 90-day cliff |

An unsealed nest is exactly +5 score. Failed sealing (+12) and military exploitation (+14) are deliberately larger categorical consequences, normally adding two or three divisions depending on the existing five-point remainder.

## Lifecycle Wiring

The core helpers are present. The concurrent event-chain worker owns the call-site edits and has wired them as follows:

1. The `maximum_shifts` completion block calls the following immediately after `set_state_flag = resources_found_maximum_shifts_active`:

   `resources_found_start_maximum_extraction_tracking = yes`

2. End paths call:

   `resources_found_stop_maximum_extraction_tracking = yes`

   Verified end paths are regulated output before clearing `resources_found_maximum_shifts_active`, strategic-reserve suspension, emergency suspension, partial closure, and full sealing.

The cave-strength calculation independently finalizes a still-live interval, so an emergence during active maximum extraction remains deterministic.

## Achievement Compatibility

No achievement file change is required. `resources_found_record_cave_emergence_achievement_state` still records the calculated starting divisions, and `resources_found_achievement.maximum_starting_divisions` remains exactly 30. The score clamp of 120 and five-points-per-division conversion make 30 reachable only from a genuine upper-band history.

## Checks and Evidence

- Replayed all deterministic profiles against the implemented constants; every target profile lands in its requested band.
- Verified the package-floor proof separately: six-resource diversity plus the package's own 720-1200 tonnage yields only 1.50-3.90 score.
- Verified the cap algebra: `6 + floor(120 / 5) = 30`, with both score and division loop capped.
- Verified duration accounting covers completed intervals and a live interval without double counting; start is idempotent, stop clears the active start date, and finalization does not mutate interval state.
- Compared the variable math and clamp structure with official effect documentation and vanilla score-building precedents in `operation_strat_effects.txt`, `SWE_scripted_effects.txt`, and `USA_scripted_effects.txt`.

## Risks and Follow-up

- The field-death term is intentionally uncapped before the global 120-point clamp. Catastrophic losses can therefore finish the climb to 30, but can never exceed the hard cap.
- The 18-month extraction and four-hunt caps are scoring caps, not gameplay-state caps; full exact duration/count state remains available for other systems.

## Spec Promotion Rules

Promote the following into the Event 018 tuning/balance specification after parent review:

- the `0/25/65/95/120` score boundaries and `6 + floor(score / 5)` conversion;
- normalization of the unavoidable 720-resource all-six minimum package;
- the principle that yield, depth, extraction duration, deaths, failed sealing, and military exploitation own upper-band movement;
- the exact mitigation inputs and their scoring caps;
- the deterministic profile table as the regression fixture for future balance changes.

Do not promote the handoff status text or concurrent-ownership notes. Once audited, fold the accepted rules into the source-of-truth spec and mark RF-018-01 resolved in the improvement addendum rather than leaving this plan handoff as design authority.

## Files Changed by This Subtask

- `common/script_constants/018_resources_found_constants.txt`
- `common/scripted_effects/018_resources_found_effects.txt`
- `docs/plans/018_resources_found_plans/subagent_handoffs/rf_018_01_cave_strength_recalibration_handoff.md`

No fallback, placeholder, achievement weakening, or unrequested subsystem change was used.
