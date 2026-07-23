# Stage 7 Biological Doomsday Release Validation

Date: 2026-07-23

Status: implemented source tranche; Stage 7 and the overall Chaos Warfare goal remain incomplete.

## Accepted requirement coverage

| Requirement | Evidence | Result |
| --- | --- | --- |
| Existing exceptional decision remains | Stable `bio_unleash_stockpiled_pathogens` identifier and legacy wrapper | implemented |
| Explicit route or extreme policy | `bio_doomsday_actor_has_explicit_route_or_extreme_policy` | implemented |
| Near capitulation or world-end | Centralized 0.80 surrender threshold and verified world-end/Chaos Meter gate | implemented |
| Existing real stockpile | Four exact ordinary-agent equipment checks | implemented |
| Domestic warning list | Temporary domestic state array and per-state tooltip loop | implemented |
| Controlled territory and nearby fronts | Deduplicated controlled-state plus enemy-controlled wartime-border array | implemented |
| Complete arsenal consumption | Four aggregate stock snapshots and four producer-agnostic negative stockpile effects | implemented |
| Distinct agents and severity | Catastrophic Anthrax, Plague, and Smallpox; severe Tularemia | implemented |
| Shared biological lifecycle | Every successful state-agent allocation calls `bio_lifecycle_dispatch_seed` | implemented |
| Maximum evidence and confirmed attribution | Doomsday route profile, force-detection record, public state flags, and one batch consequence | implemented |
| Severe deaths, contamination, medical load, and spread | Route profile plus agent profile plus doctrine snapshot in the ordinary lifecycle | implemented |
| Extreme Condemnation | One 300-point public source, doctrine-adjusted only for Condemnation and clamped to 200–500 | implemented |
| Self and allied risk | Direct domestic targeting plus 0.85 connected friendly-spread risk | implemented |
| Route-aware AI | Unrestricted-route zero gate, doctrine/stock/safety/risk modifiers, centralized constants | implemented |
| No fallback or broad pulse | No alternate target, proxy, estimator, continuous-air hook, or periodic country scan | implemented |
| Existing assets preserved | Legacy decision icon reused and biological military-raid icons untouched | implemented |

## Contract scenarios

| Scenario | Expected source behavior | Source evidence |
| --- | --- | --- |
| Ordinary or defensive route | AI score is zero and the category remains hidden without an accepted extreme policy. | Route gate and zero AI factor. |
| Player with unrestricted policy at 0.81 surrender progress | Decision is visible and available when arsenal and target conditions are also true. | Category, availability, and resolver share the same trigger family. |
| Explicit unrestricted AI route at 0.81 surrender progress | AI may use the decision and evaluates doctrine, arsenal, safety, outbreak, sanctions, and treaty factors. | `ai_will_do` matrix and installed decision analyzer. |
| World-end condition below the surrender threshold | The last-resort gate succeeds without inventing a surrender value. | `bio_doomsday_actor_is_in_world_end_condition`. |
| Four-agent arsenal | Every agent is consumed and dispatched separately through one state array. | `bio_doomsday_capture_and_consume_arsenal` and four calls to `bio_doomsday_dispatch_current_agent`. |
| Tularemia-only arsenal | The last national result is severe and every accepted Tularemia seed validates as severe. | Severe lifecycle result token and doomsday validator branch. |
| Anthrax, Plague, or Smallpox present | The national result is catastrophic and each accepted non-Tularemia seed validates as catastrophic. | Catastrophic branch in dispatcher and national history calculation. |
| Agent stock smaller than state count | One unit reaches each state in array order until the stock reaches zero. | Allocation minimum and remaining-stock clamp. |
| One enemy state adjacent to several controlled states | The enemy state appears once and cannot receive duplicate array entries from adjacency alone. | `NOT = { is_in_array = ... }` before every front-state insertion. |
| Controlled and enemy-held border states | Controlled states are marked domestic; non-domestic targets are marked front release. | Exact controller check in `bio_doomsday_mark_current_seed`. |
| Allied territory | No allied state is directly inserted, but subsequent connected spread may cross into it. | Target trigger requires enemy controller at war; route friendly-spread risk remains 0.85. |
| Wasteland, zombie, invalid controller, or otherwise ineligible state | The state does not enter the target array. | Shared ordinary-pathogen target validator. |
| Dispatch rejection after arsenal debit | Material stays consumed, no alternate state is used, and exact partial or failure history is recorded. | Fail-closed resolver status branches. |
| At least one successful state and later rejection | News and one public political batch occur once; full-resolution history remains false. | Seeded-payload gate and exact equality test. |
| Terminal Hazard doctrine | Physical potency rises through the lifecycle and only Condemnation may fall. | Doctrine snapshot and isolated batch Condemnation multiplication. |
| Repeated state-agent allocations | State payload totals rise, but the national deliberate-use, route, treaty, Condemnation, and domestic-penalty records occur once. | Separate per-state/per-agent history and one batch registrar. |
| Already-active undetected state-agent episode | Forced detection still produces maximum evidence and confirmed attribution, while validated batch suppression prevents the lifecycle from releasing a second political consequence. | `bio_seed_batch_condemnation_proof` is required by the doomsday validator and applied before immediate detection. |
| Idle chemical-capable or biological-capable aircraft | No contamination or outbreak can occur. | No aircraft or continuous-air hook exists in the decision, helper, lifecycle caller, or on-action surface. |

## AI score audit

The installed Operation Postern 1.19.2 decision analyzer discovered the decision and all nine `ai_will_do` modifiers with no unsupported weighted construct.

An isolated exact matrix for the analyzer-supported conditions produced raw scores of 0 without an unrestricted AI route, 0.35 for an unrestricted unsafe baseline, 1.05 for Terminal Hazard plus a large stockpile, and 0.021 after an active domestic outbreak and treaty membership.

The decision adapter correctly reports scores only and does not invent a click probability.

The analyzer currently leaves the two script-constant operands inside `bio_doomsday_ai_is_sanction_vulnerable` unresolved.

The source-defined factor is 0.10 when both threshold checks pass, so the final exposed scenario has a source score of 0.0021.

This tool limitation is recorded as unavailable automated evidence for that helper, not as unsupported game behavior and not as a gameplay approximation.

## Source and engine review

The target collector follows the installed vanilla `any_neighbor_state` and `CONTROLLER = { has_war_with = ROOT }` pattern.

Official effect documentation and the offline Data Structures reference verify temporary arrays, `array^num`, `is_in_array`, and `for_each_scope_loop`.

The installed scripting surface exposes no exact active-front state predicate.

The implementation therefore defines nearby fronts as exact enemy-controlled wartime border adjacency and does not retain an estimator.

## Asset audit

`GFX_decision_bio_unleash_stockpiled_pathogens` remains registered in `interface/chaosx_gfx_cleanup.gfx`.

Its original 4,224-byte DDS remains at `gfx/interface/decisions/biowarfare/decision_bio_unleash_stockpiled_pathogens.dds` with SHA-256 `4F711064D2A7E0E70631C79538387E9C78A8DF8731D524FCC0AB90D64A1BC1FF`.

No file under `gfx/interface/military_raids/` was edited or replaced by this tranche.

## Remaining Stage 7 work

Historically specific Japan–China biological campaign actions, the complete surveillance, containment, countermeasure, and treatment package, remaining biological designers, differentiated AI closure, remaining assets and final localisation, cross-route package scenarios, improvement-loop review, and mapped specialist audits remain open.

This validation does not claim Stage 7 or overall goal completion.
