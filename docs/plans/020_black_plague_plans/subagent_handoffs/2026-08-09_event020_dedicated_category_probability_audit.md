# Event 020 dedicated Black Plague category probability audit

Audit date: 2026-08-09. This is a read-only weighted-logic audit of the category-ownership correction in `common/decisions/020_black_plague_response_decisions.txt` and `common/decisions/020_black_plague_shared_response_decisions.txt`. No gameplay, AI, decision, mission, category, trigger, effect, localisation, or runtime file was changed.

## Scope and evidence boundary

The moved surfaces are the national Black Plague actions in `black_plague_response_category`. The source moves do not intentionally change their `ai_will_do` constants. The complete requested action roster is:

- `black_plague_produce_medical_reserve` (medical reserve)
- `black_plague_establish_countermeasure_program`
- `black_plague_shared_emergency_countermeasure_drive`
- `black_plague_shared_publish_findings`
- `black_plague_shared_restricted_alliance_exchange`
- `black_plague_shared_hoard_protocol`
- `black_plague_shared_steal_foreign_progress`
- `black_plague_shared_international_medical_mission`
- `black_plague_shared_reconstruction_vigilance`
- `black_plague_shared_international_inspection_compact`
- `black_plague_shared_condemn_future_weaponization`
- `black_plague_shared_population_recovery_program`
- `black_plague_shared_memorial_biosecurity_charter`

The first four are ordinary decisions. `black_plague_shared_emergency_countermeasure_drive` is a selectable mission and must use the `mission_ai_will_do` adapter. These are not one mixed normalized probability pool. A decision willingness score is not a click probability.

## MCP provenance and exact blockers

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The required canonical-source reads were attempted with `hoi4.probability_inspect` and `refresh = true`.

| Surface | Adapter and candidate pool | Result | Artifact/evidence |
| --- | --- | --- | --- |
| `common/decisions/020_black_plague_shared_response_decisions.txt` | `decision_ai_will_do`; the ten ordinary dedicated actions from `black_plague_shared_publish_findings` through `black_plague_shared_memorial_biosecurity_charter` | `PROBABILITY_SURFACE_EMPTY`; blocker `No weighted blocks matched this request`; `artifactCount = 0`; `filesScanned = []` | No MCP artifact. The no-candidate-pool retry returned the same exact result. |
| `common/decisions/020_black_plague_shared_response_decisions.txt` | `mission_ai_will_do`; `black_plague_shared_emergency_countermeasure_drive` | `INTERNAL_ERROR`; blocker `Unexpected internal error`; `artifactCount = 0`; `filesScanned = []` | No MCP artifact. The no-candidate-pool retry returned the same exact result. |

These are adapter results, not claims that the source blocks are absent or that the game will not load them. The current canonical files contain repeated root `black_plague_response_category` blocks because the correction separates moved groups around the remaining `chaosx_disease_containment_category` blocks. The installed probability index does not provide a reliable canonical result for this representation.

For parser diagnosis only, I extracted the current eleven shared AI blocks into a temporary non-runtime probe and supplied all eleven IDs, including the selectable mission, to `decision_ai_will_do`. That supplemental call returned `PROBABILITY_SOURCE_INSPECTED` with `candidates = 11`, `requiredInputs = 0`, `unresolved = 0`, and `poolComplete = true`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01b16c8c55170936497ee2bb6129b51bd71736d99957e006f78e69089c3cecf1/ccc268998bfe29adb0e791ffdfbab0bc1e641cf2ee95a64cf33345ba1dc85a09/probability-inspect-baac4937fe4e.json`; source revision `25d5551da5c62cd0e3c1d1a99a8b243901c600c10e8ac66df2f6ed9e79f69c29`; source hash `baac4937fe4e1b5e44af21e308598ba9c2d1ae55e4b8624ad4121048716b20b1`. This probe is not canonical engine evidence because it omitted the real decision fields and target/cost gates. It only confirms that the flat shared score blocks can be indexed when the adapter receives a complete minimal pool.

## Source-level score evidence

The following values are source-attested score inputs only. They are not normalized probabilities and were not evaluated by the canonical MCP route.

| Decision or mission | Base | Source modifiers |
| --- | ---: | --- |
| `black_plague_produce_medical_reserve` | `constant:black_plague_response_ai.strong` (4) | `countermeasure_priority` (5) while the reserve variable is below the batch target; `war_pressure_factor` (0.60) while at war. |
| `black_plague_establish_countermeasure_program` | `preferred` (2) | `countermeasure_priority` (5) in a severe state; `high_burden_factor` (0.35) when response capacity four is unavailable. |
| `black_plague_shared_emergency_countermeasure_drive` | `critical` (12) | No `ai_will_do` modifier. Activation and cost gates remain separate. |
| `black_plague_shared_publish_findings` | `strong` (4) | No `ai_will_do` modifier. |
| `black_plague_shared_restricted_alliance_exchange` | `preferred` (2) | No `ai_will_do` modifier. |
| `black_plague_shared_hoard_protocol` | `cautious` (0.50) | No `ai_will_do` modifier. |
| `black_plague_shared_steal_foreign_progress` | `emergency` (8) | No `ai_will_do` modifier. |
| `black_plague_shared_international_medical_mission` | `strong` (4) | No `ai_will_do` modifier. |
| `black_plague_shared_reconstruction_vigilance` | `preferred` (2) | No `ai_will_do` modifier. |
| `black_plague_shared_international_inspection_compact` | `strong` (4) | No `ai_will_do` modifier. |
| `black_plague_shared_condemn_future_weaponization` | `preferred` (2) | No `ai_will_do` modifier. |
| `black_plague_shared_population_recovery_program` | `preferred` (2) | No `ai_will_do` modifier. |
| `black_plague_shared_memorial_biosecurity_charter` | `preferred` (2) | No `ai_will_do` modifier. |

The constants resolve in source to `cautious = 0.50`, `preferred = 2`, `strong = 4`, `emergency = 8`, and `critical = 12`. Those literal resolutions are exact as source constants, but their runtime selection behavior is unresolved.

## Candidate-pool and external-factor completeness

The intended ordinary-decision pool is the four decision IDs in the response source plus the ten ordinary shared country-level IDs. The intended mission pool is the one selectable mission ID. The canonical adapter did not return a discovered pool for either source, so every requested scenario has `poolComplete = unknown` rather than `true` or `false`.


## Named scenarios

The requested scenario IDs are declared here for the next valid MCP run. Because canonical inspection failed, all rows are unresolved and no ranking or probability is asserted.

| Scenario ID | Declared state | Candidate pool | Classification and result |
| --- | --- | --- | --- |
| `E020_DEDICATED_PREPARED_HUMAN_AFTER_SYSTEM_START` | Prepared human country immediately after system start, strategic category visible, no severe crisis asserted | Four ordinary response decisions plus ten ordinary shared dedicated decisions; mission evaluated separately | **Unresolved**. No canonical inspect artifact, so no eligibility, score race, dominance, or click-probability result. |
| `E020_DEDICATED_PREPARED_AI_AFTER_SYSTEM_START` | Prepared AI country immediately after system start with the same category and resource assumptions | Same ordinary pool, mission separate | **Unresolved** for the same adapter blocker. Human and AI ownership must be typed separately in a rerun. |
| `E020_DEDICATED_SEVERE_LOW_COUNTERMEASURE_PROGRESS` | Strategic category visible, at least one active severe state, low countermeasure progress, no invalidation flag | Four ordinary response decisions, ten ordinary shared actions, and emergency mission separately | **Unresolved**. The source expresses severe urgency, but MCP did not prove which targets, costs, or active locks are eligible. |
| `E020_DEDICATED_COUNTERMEASURE_RECOVERY_COMPLETE` | Countermeasure/recovery complete state with completion flags and high progress | Same pools | **Unresolved**. No MCP timing, cleanup, starvation, or post-completion visibility result. |
| `E020_SHARED_OTHER_DISEASE_BOARD_BLACK_ACTIVE` | Another disease selected on the shared board while Black Plague's strategic category remains active | Shared ordinary actions and emergency mission separately, with Black Plague category visibility asserted | **Unresolved**. The adapter did not evaluate cross-board selection, target validity, or category filtering. |

These are declared scenario contracts, not executed probability results. `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, and `hoi4.probability_render` were not run after the canonical inspect blockers. There is no exact, bounded, sampled, or normalized scenario result to report.

## Baseline and comparison

The earlier Event 020 probability handoff, `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-06_event020_ai_probability_audit_handoff.md`, records that the response, shared-response, and weaponization decision sources returned `PROBABILITY_SURFACE_EMPTY` with no artifact. It is a textual blocker record, not a cached baseline artifact accepted by `hoi4.probability_compare`.

No valid before/after `hoi4.probability_compare` receipt exists for this category correction. The compare pass is therefore unresolved because no artifact-backed pre-correction source was available and the current canonical inspect did not produce a source revision or candidate pool. A same-source or synthetic-probe comparison would not prove the category correction and was not used as one.

## Findings and recommendations

- No positive-weight impossible target, dead choice, rank reversal, dominance, starvation, repetition, cooldown, or exploit conclusion is proven. The required availability, cost, target, and hidden-state inputs were not engine-resolved.
- Do not convert `4`, `2`, `0.50`, `8`, or `12` into click percentages. Even with a complete pool, `ai_will_do` is a willingness score race, not a direct player-click chance.
- Obtain a probability adapter route that can index repeated category blocks and target-gated decisions in the canonical files, or provide an engine-supported source fixture that preserves all decision and mission fields.
- Re-run `hoi4.probability_inspect` with the complete four-entry ordinary response pool, complete ten-entry ordinary shared pool, and one-entry mission pool. Then evaluate the five named scenario IDs with typed category, target, resource, flag, and human/AI state.
- Add declared numeric ranges for countermeasure progress, severe-state pressure, war pressure, and response-capacity modifiers before using `hoi4.probability_sweep` with `findRankReversals = true`.
- Run `hoi4.probability_compare` only after an owner-applied source change and a real pre-correction baseline are available, using identical scenario IDs and candidate pools.

## Skipped analyses and blockers

- Canonical ordinary decision inspection: exact `INTERNAL_ERROR` blocker, no artifact.
- Canonical shared decision inspection: exact `PROBABILITY_SURFACE_EMPTY` blocker, no artifact.
- Canonical mission inspection: exact `INTERNAL_ERROR` blocker, no artifact.
- `hoi4.probability_evaluate`, `sweep`, `simulate`, `sequence`, and `render`: skipped because no canonical inspect result supplied an adapter-backed source surface and no complete typed scenario fixture was available.
- `hoi4.probability_compare`: skipped because the prior Event 020 handoff has no accepted baseline artifact and current canonical inspection produced no source revision. No before/after claim is made.
- Structural event inspection/render: not run because this bounded task audits decision and mission AI weights, not an event chain. The parent event and decision auditors retain structural review.
- No gameplay or runtime validation was attempted. The user owns live Hearts of Iron IV validation.

## Files changed

Only this handoff was added:

`docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_dedicated_category_probability_audit.md`

