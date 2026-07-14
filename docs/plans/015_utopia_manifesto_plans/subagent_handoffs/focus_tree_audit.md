# Event 15 Utopia Manifesto focus-tree audit

## Verdict

**FAIL**

The 122-focus source is structurally coherent and fully localised and illustrated, but it is not completion-ready. Two route outcomes are impossible, the decision-phase sequence is disconnected and incomplete, the idea lifecycle exceeds the three-spirit ceiling, the entire tree repeats prohibited fairy-dust Ledger values, and eleven focuses have no mechanically consumed reward beyond those Ledger changes.

Audit basis: `common/national_focus/015_utopia_manifesto_focus_tree.txt` at SHA-256 `C5447DDA420F9FCE41E49125C4B6E0FA2D0940D7D575FF690323D2DE03592931`.

## Ordered blockers

### P1: The Joke Understood route cannot form its commonwealth

`utopia_manifesto_practical_formation_proof_met` requires `utopia_manifesto_broad_recognition_proven` at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:809`. No gameplay file sets that flag. The route opener, eight-focus route, island proof, first Need case, external network, mixed-property proof, false-case resolution, and route capstone can all be completed, but `utopia_manifesto_can_form_current_route` remains false.

Required correction: award the proof through a real recognition milestone that the route can reach, preferably the intended foreign-recognition or league action. Do not put the flag on the route opener or capstone without the external work the proof is meant to represent.

### P1: Closed Island cannot finish the shared post-formation endgame

Paid military growth is capped at six batches by `utopia_manifesto_growth_limits.military_batch_limit = 6` at `common/script_constants/015_utopia_manifesto_constants.txt:453`. `utopia_manifesto_can_pay_military_growth` rejects the seventh batch at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:867`.

Closed Island must consume six focus-owned batches before it can form and enter the post-formation branch:

1. `utopia_manifesto_households_of_service`
2. `utopia_manifesto_perfect_island`
3. `utopia_manifesto_the_citizen_watch`
4. `utopia_manifesto_engineers_before_generals`
5. `utopia_manifesto_a_small_army_well_housed`
6. `utopia_manifesto_commonwealth_defense_compact`

The last defense focus is required because Closed Island formation proof requires `utopia_manifesto_defense_proof_complete`. The post-formation focus `utopia_manifesto_the_commonwealth_at_war` then requires a seventh paid batch at `common/national_focus/015_utopia_manifesto_focus_tree.txt:3341`, so it is permanently unavailable. That also blocks `utopia_manifesto_plenty_in_an_age_of_chaos`.

The same shared counter is incremented by military decisions. Other routes can therefore self-lock the same post-formation chain by buying enough legitimate military growth before reaching it.

Required correction: separate repeatable decision limits from focus progression, reserve a guaranteed paid post-formation batch, or replace the global historical-batch gate with a cost and route-safe cap that cannot invalidate downstream focuses.

### P1: The route opener creates a fourth package spirit

The package initializes Found Manifesto, Unmeasured Country, and Inherited Order together at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:99`. Route commitment then adds one of five route institution spirits at `common/scripted_effects/015_utopia_manifesto_country_effects.txt:178` without retiring any of the three starting lifecycles. The actor therefore holds four focus-package spirits through most of the tree, contrary to the accepted maximum of three.

Clearing the Found Manifesto lifecycle when the route identity is committed is the correct first repair. It matches the accepted lifecycle rule that the book is absorbed into the route institution. A second coordinated repair is required: `utopia_manifesto_two_years_against_hunger` currently swaps Found Manifesto into Common Store Network at `common/national_focus/015_utopia_manifesto_focus_tree.txt:1884`. After the first repair that condition would never run. It should instead replace Unmeasured Country with Common Store Network. `utopia_manifesto_the_island_made_real` already replaces Inherited Order with Garden District Network. The stable mature set can then remain route institution, store network, and garden network.

### P1: Decision phases 7, 8, and 9 are defined correctly, but the progression is not implemented as a usable phase system

The constants are correct and ordered:

- `route = 7`
- `formation = 8`
- `mature = 9`

They are defined at `common/script_constants/015_utopia_manifesto_constants.txt:344`. The setter at `common/scripted_effects/015_utopia_manifesto_effects.txt:713` clamps the input and assigns only when the input is greater than the current value, so the setter itself is monotonic.

The integration fails for three reasons:

- No decision, category, scripted trigger, scripted localisation block, or GUI gameplay condition reads `utopia_manifesto_decision_phase`. Outside its setter, cleanup, and focus writes, it has zero gameplay consumers.
- `districts = 4` is never submitted to the setter.
- `route = 7` is submitted only by the optional crisis convergence focus `utopia_manifesto_a_settled_interim_charter` at `common/national_focus/015_utopia_manifesto_focus_tree.txt:3153`. A normal campaign advances from Necessary Ground 5 or League 6 directly to Formation 8, skipping Route 7.

Formation 8 is submitted by `utopia_manifesto_proof_of_the_commonwealth` and Mature 9 by `utopia_manifesto_the_second_generation`. Those calls are monotonic but do not repair the missing stages or the absent consumers.

Required correction: make phase thresholds the source of truth for category and family visibility, submit Districts from the district milestone, submit Route from every valid route commitment or a shared guaranteed convergence milestone, and retain the 8 and 9 calls.

### P1: Repeated fairy-dust Ledger rewards fail the focus-tree balance standard

Every one of the 122 focuses applies a prepared Ledger delta. The focus file contains 347 nonzero delta assignments using the following authored magnitudes:

- `tiny = 2`, used 76 times
- `negative_tiny = -2`, used 80 times
- `small = 4`, used 84 times
- `negative_small = -4`, used 45 times
- `medium = 7`, used 45 times
- `negative_medium = -7`, used 17 times

The magnitudes are defined at `common/script_constants/015_utopia_manifesto_narrative_constants.txt:15`. This is the exact repeated `2`, `4`, and `7` pattern that the focus-tree skill treats as completion-blocking fairy dust. The standard focus cost is also an authored `7` at `common/national_focus/015_utopia_manifesto_focus_tree.txt:12`, producing a nonstandard 49-day band without a documented technical reason.

Required correction: retune focus-owned changes to meaningful round increments, combine weak movements, and let mechanically substantial unlocks carry focuses whose Ledger movement should be secondary. Preserve route tradeoffs and formation-threshold reachability when recalculating totals.

### P1: Eleven focuses are true orphan-flag plus Ledger rewards

Thirty-eight rewards contain only `set_country_flag`, four Ledger inputs, and `utopia_manifesto_apply_prepared_ledger_delta`. Twenty-seven of those set at least one flag consumed by another gameplay file. The following eleven set no flag referenced anywhere outside the focus source, so their only gameplay result is the fairy-dust Ledger movement:

| Focus | Source line | Unconsumed flag or flags |
| --- | ---: | --- |
| `utopia_manifesto_transparent_store_accounts` | 347 | `utopia_manifesto_transparent_store_accounts` |
| `utopia_manifesto_council_autonomy` | 682 | `utopia_manifesto_council_autonomy` |
| `utopia_manifesto_emergency_central_plan` | 712 | `utopia_manifesto_emergency_central_plan` |
| `utopia_manifesto_shortage_forecasting` | 895 | `utopia_manifesto_shortage_forecasting` |
| `utopia_manifesto_useful_freedom` | 946 | `utopia_manifesto_useful_freedom`, `utopia_manifesto_planner_appeals_protected` |
| `utopia_manifesto_sunset_clauses` | 1443 | `utopia_manifesto_sunset_clauses` |
| `utopia_manifesto_rotate_old_stores` | 1827 | `utopia_manifesto_store_rotation_protocol` |
| `utopia_manifesto_no_glory_in_the_field` | 2240 | `utopia_manifesto_defensive_war_doctrine`, `utopia_manifesto_strict_war_authorization` |
| `utopia_manifesto_necessary_victory` | 2303 | `utopia_manifesto_necessary_victory_doctrine` |
| `utopia_manifesto_offer_the_first_surplus` | 2414 | `utopia_manifesto_first_surplus_offered` |
| `utopia_manifesto_a_rule_for_need` | 3283 | `utopia_manifesto_mature_need_law`, `utopia_manifesto_case_expiry_permanent` |

The two defense-doctrine alternatives and the mature Need-law focus are especially serious because they present strategic policy choices and late-game lawmaking without implementing either policy.

Required correction: give each focus a mechanically consumed decision, mission, trigger, idea stage, diplomatic rule, military rule, map action, or durable modifier. Remove flags that remain redundant after the real hook is added.

### P2: Paid-growth affordability uses a stale state-scaled cache

Growth costs are calculated from `num_of_controlled_states` by `utopia_manifesto_refresh_dynamic_costs` at `common/scripted_effects/015_utopia_manifesto_effects.txt:1765`. The cache is initialized at event acceptance and refreshed only by later growth helpers and a few decisions. Focus `available` blocks call `utopia_manifesto_can_pay_institutional_growth` or `utopia_manifesto_can_pay_military_growth` without refreshing that cache.

If controlled-state count changes, a focus can be hidden by an obsolete high cost, or it can start under an obsolete low cost and complete after the helper recalculates and rejects payment. The latter consumes the focus while withholding its advertised paid growth.

Required correction: base the availability trigger on current state-scaled values, refresh through bounded state-change integration, or redesign the cost check so the visible and completion checks use the same live calculation.

## Structural and coverage results

The static graph is sound:

- 122 focus blocks and 122 unique IDs
- one root, `utopia_manifesto_recover_the_manuscript`
- zero unresolved prerequisite references
- zero unresolved mutual-exclusion references
- zero statically unreachable focuses
- zero asymmetric mutual exclusions
- zero duplicate resolved coordinates
- zero prerequisite parent-order violations
- all 122 focuses have a completion reward, icon, cost, and `ai_will_do`
- 18 short, 71 standard, and 33 long focuses
- 26 paid institutional-growth calls and 8 paid military-growth calls
- no direct free unit, equipment, factory, core, claim, war-goal, or annexation reward in the focus source

Paid military units are created only after the dynamic manpower, infantry equipment, support equipment, and army experience deductions in `utopia_manifesto_apply_paid_military_growth`. They are not free divisions.

### Route coverage

| Required route | Implemented route | Status | Evidence and blocker |
| --- | --- | --- | --- |
| Consent of Households | 10-focus route | Partial | Reachable with symmetric opener exclusion, paid growth, decision hooks, final idea, and valid formation proof sources. Shared phase, idea-cap, dust, and reward-depth defects remain. |
| Common Table | 10-focus route | Partial | Reachable with a real internal fork, decision hooks, paid growth, final idea, and valid formation proof sources. `Council Autonomy` and `Emergency Central Plan` are mechanically empty choices. |
| Guardians of Measure | 10-focus route | Partial | Reachable with a real freedom versus obedience fork, district integration, paid growth, final idea, and valid formation proof sources. `Shortage Forecasting` and `Useful Freedom` lack their advertised mechanical policy. |
| Closed Island | 9-focus route | Fail | Route and formation proof are reachable, but the mandatory sixth military batch makes the post-formation war focus and final tree capstone impossible. |
| The Joke Understood | 8-focus hidden route | Fail | Reveal trigger correctly requires Choice, Concord, debate, education, criticism, and noncoercion. Formation is impossible because broad-recognition proof has no producer. |

### Shared branch coverage

| Surface | Status | Notes |
| --- | --- | --- |
| Opening trunk | Pass with balance defect | Eight-focus AND structure reaches the congress and country question. Three starting ideas are established, but route commitment creates a fourth. |
| Callings and education | Partial | Seven focuses, education proof, decision hooks, and paid growth exist. Phase 4 is skipped and phase values are unused. |
| Common stores | Partial | Seven focuses, reserve gating, paid growth, and a staged store idea exist. `Rotate Old Stores` has no consumed protocol effect. |
| Garden districts and island variants | Pass | Nine focuses, three symmetric island variants, geography helpers, paid growth, proof refresh, and staged Garden District idea are connected. |
| Defense without waste | Fail | Eight focuses and paid unit growth exist. Both doctrine choices are mechanically empty, and the shared batch cap breaks Closed Island post-formation progression. |
| Foreign Commonwealth | Partial | Seven focuses, league unlocks, external network, and paid growth are connected. `Offer the First Surplus` has no consumed effect. |
| Necessary Ground | Pass with balance defect | Eight focuses, a peaceful versus coercive fork, case decisions, expiry and stewardship hooks, first-associate proof, and formation integration are connected. Deltas still use fairy-dust values. |
| Stewardship and status | Pass with balance defect | Six focuses connect to real decision-owned obligations, emergency provision, charter period, status review, and proof refresh. |
| Crisis correction | Pass with phase defect | One crisis entry, five symmetric route corrections, and a shared convergence focus are reachable under crisis state. Route phase 7 is incorrectly exclusive to this optional path. |
| Formation and post-formation | Fail | Decision-owned proof and formation are substantial. Joke formation and Closed Island terminal post-formation play are impossible, and `A Rule for Need` is mechanically empty. |

## Localisation, icon, AI, and integration evidence

- Focus localisation has 122 of 122 titles and 122 of 122 descriptions. There are no duplicate or empty focus strings.
- The tree assigns 122 icons from 72 unique sprites. All 72 base sprites and all 72 shine sprites resolve to existing DDS files at 94 by 86 pixels.
- The Event 15 focus contact sheet was reviewed. The icon set has distinct subjects and branch accents while retaining a coherent frame language.
- All 122 focuses have AI weights. The source has 76 high, 28 normal, 10 urgent, 6 low, and 2 hidden base weights, with 21 conditional modifier blocks.
- Five route-specific country AI strategies, foundation restraint, crisis response, Ledger recovery strategies, Closed Island escalation handling, and mature-commonwealth behavior are present in `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt`.
- All 17 idea identifiers referenced directly by the focus source resolve to Event 15 idea definitions.
- Focus unlock helpers resolve to calling, reserve, district, Necessary Ground, stewardship, league, and formation decision families.
- Formation remains decision-owned. The proof trigger combines route capstone, island completion, first resolved external case, external network, Ledger thresholds, no constitutional crisis, no failed stewardship, and route-specific evidence.

## Machine-readable audit summary

```yaml
verdict: FAIL
focus_total: 122
focus_unique_ids: 122
branch_group_counts:
  opening: 8
  consent: 10
  common_table: 10
  guardians: 10
  closed_island: 9
  joke_understood: 8
  callings: 7
  stores: 7
  garden_island: 9
  defense: 8
  foreign_commonwealth: 7
  necessary_ground: 8
  stewardship: 6
  crisis: 7
  formation_mature: 8
cost_counts:
  short_35_days: 18
  standard_49_days: 71
  long_70_days: 33
graph:
  roots: 1
  unresolved_prerequisites: 0
  unresolved_mutex_refs: 0
  static_unreachable: 0
  asymmetric_mutex_pairs: 0
  coordinate_collisions: 0
  parent_order_violations: 0
coverage:
  missing_icons: 0
  missing_ai_blocks: 0
  missing_rewards: 0
  missing_focus_titles: 0
  missing_focus_descriptions: 0
  unique_focus_icons: 72
  unresolved_focus_icon_sprites: 0
rewards:
  ledger_helper_calls: 122
  nonzero_fairy_dust_assignments: 347
  pure_flag_plus_ledger_focuses: 38
  mechanically_consumed_flag_plus_ledger_focuses: 27
  orphan_flag_plus_ledger_focuses: 11
  paid_institutional_growth_calls: 26
  paid_military_growth_calls: 8
  direct_free_unit_or_equipment_rewards: 0
ideas:
  maximum_package_spirits_before_postformation: 4
  allowed_maximum: 3
phases:
  route_constant: 7
  formation_constant: 8
  mature_constant: 9
  setter_monotonic: true
  gameplay_phase_consumers: 0
  districts_phase_calls: 0
  normal_route_phase_calls: 0
route_blockers:
  impossible_formation_routes: 1
  impossible_terminal_postformation_routes: 1
```

## Completion decision

The focus-tree audit must be rerun after the six P1 findings are fixed. At minimum, rerun route reachability with live proof producers, calculate the maximum compatible paid-growth batches for every route, trace the three-spirit lifecycle through crisis switching and post-formation, verify all phase thresholds are consumed, and reclassify the eleven orphan rewards after their mechanics are wired.

No gameplay, localisation, asset, specification, workbook, or shared documentation file was changed by this audit.
