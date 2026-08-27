# Event 006 decision and mission audit: FER strategic cost clarity

Date: 2026-08-27

Scope: bounded audit of the Event 006 decision and mission surface against `docs/specs/006_independence_wave_specs/` and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.

## Disposition

One safe package-local defect was patched. `independence_wave_fer_codify_durable_sovereignty` displayed War Support as though it were consumed and displayed convoy and train icons together, while its affordability trigger treated War Support as a gate and its payment effect consumed stability, command power, and one transport alternative. The patch keeps the existing gameplay and lifecycle unchanged while making the player-facing requirement and cost accurate.

## Issue list by severity

1. Resolved, high clarity: `independence_wave_fer_cost_strategic` included `war_support_minor` even though `can_pay_independence_wave_fer_strategic_cost` only gates on that value and `independence_wave_decision_pay_strategic` does not debit it. The same string implied both convoy and train were paid even though `independence_wave_decision_pay_diplomatic_standard` consumes either convoy or train. The corrected string uses `GetIndependenceWaveDiplomaticStandardTransportCostText`, and the decision now exposes the War Support threshold through `independence_wave_fer_strategic_war_support_requirement_tt`.

2. Open, medium: analogous package-specific strategic cost strings remain queued for Bashkiria/Mari, Kurdistan, Buryatia, Khakassia, and Sakha. Their source ownership and the distinction between gate-only War Support and consumed resources should be reconciled package by package; this handoff deliberately does not widen the patch.

3. Open, medium: the required read-only GUI evidence remains blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` for both `independence_wave_status_window` and `chaosx_independence_wave_formable_state_puzzle_window` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The fresh `hoi4.gui_inspect` and `hoi4.gui_render` calls produced no new artifacts because the artifact provenance manifest did not match its immutable address.

4. Open, medium: the source-of-truth map still queues dynamic preactivation disclosure for DM-01, package cost prose reconciliation, typed probability evidence, and GUI fidelity review. No category redesign or retired pre-event surface was introduced here.

## Changed files and identifiers

- `common/decisions/006_independence_wave_far_eastern_decisions.txt:497-518` — decision `independence_wave_fer_codify_durable_sovereignty` now includes a custom trigger tooltip whose hidden trigger exactly mirrors the existing `NOT = { has_war_support < constant:independence_wave_decision_cost.war_support_minor }` gate.
- `localisation/english/006_independence_wave_far_eastern_l_english.yml:82-83` — `independence_wave_fer_cost_strategic` now lists stability, command power, and the dynamic convoy-or-train transport cost; `independence_wave_fer_strategic_war_support_requirement_tt` explains the separate War Support threshold.

No shared source-of-truth map, specification, category, scripted GUI, payment effect, AI weight, mission helper, or unrelated dirty file was edited.

## Before and after behavior

Before, the FER strategic codification row showed stability, War Support, command power, and both transport icons as one apparent cost string, while the source effect paid no War Support and paid only one transport alternative. War Support was therefore an invisible/ambiguous requirement and transport choice was misleading.

After, the visible cost shows only the three spendable groups with the existing icon-first dynamic transport helper, and the availability tooltip separately tells the player to maintain the War Support threshold before beginning the settlement. The existing `available`, `custom_cost_trigger`, `days_remove`, `complete_effect`, `remove_effect`, `cancel_trigger`, `cancel_effect`, and AI block remain intact.

## Category and lifecycle notes

The current Event 006 map records no reintroduced pre-event pressure category or history surface. The implementation receipt records 80 accepted decision rows, including 18 timed mission blocks with availability, timeout/cancel, and terminal lifecycle coverage. The FER decision remains owned by its railway compact package category, uses the existing strategic duration constant, and refuses duplicate package work through `NOT = { has_independence_wave_fer_active_package_project = yes }`.

The phase-0 visibility receipt reports at most three simultaneously startable primary actions and three retained active objectives in the audited Event 006 phase, so this narrow cost patch does not alter category density or objective capacity.

## Cognitive-load notes

The source audit found no proven category-density violation in the current matrix: visible primary action counts remain within the accepted cap. The status scripted GUI presents five named ledger values plus host, patron, network, phase, and mission text, but fresh visual fidelity cannot be claimed while the GUI artifact manifest is invalid. The FER row is now easier to scan because its cost line no longer presents a gate-only value as spendable and no longer presents both mutually exclusive transport types as jointly paid.

The existing status values have named significance in the source and localisation, while the queued DM-01 preactivation disclosure and GUI evidence remain parent-owned follow-up items.

## Mission quality notes

No mission was added or re-timed. The accepted matrix receipt identifies Event 006 as the owner of 18 timed mission blocks and records availability, timeout, cancellation, title, description, cost, AI, and terminal-effect coverage. Their package categories and region or target gates remain unchanged. The FER strategic codification is a timed decision rather than a new mission block; its package owner, capital-control requirement, project-readiness requirement, success completion effect, cancellation path, and duplicate-project guard remain intact. No duplicate objective risk was introduced.

## Cost and requirement clarity

The corrected FER cost has three spendable groups: stability, command power, and one transport alternative resolved dynamically to convoy or train. Every displayed spendable value uses the existing texticon or scripted transport-localisation path. War Support is now a separately described threshold, not a fourth debit. The payment proof is `common/scripted_effects/006_independence_wave_decision_effects.txt:350-353` plus `:199-214`; the gate proof is `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:70-74`.

The remaining package-specific strategic strings are still an accepted queue and should not be mass-edited without confirming each package's actual effect and factory or transport behavior.

## AI validity and route locks

The FER AI weight remains `constant:independence_wave_decision_ai.standard`; no weighted logic or target selection was changed. Existing package readiness, capital ownership, compact, crisis, and active-project gates remain in force. A probability-auditor run was not required for this non-AI patch, and no AI balance claim is made. Any future AI or probability-bearing change still requires the baseline and same-scenario compare route through `chaosx_ai_probability_auditor`.

## Localisation and tooltip gaps

The new key has one source reference and one English definition, and the touched localisation file retains its UTF-8 BOM. The package continues to use the established base custom-cost key convention without adding blocked or tooltip sibling keys; whether those siblings are needed should be decided with engine evidence rather than inferred from this narrow repair.

## Cleanup and exploit-risk notes

No effect, cancellation, cleanup, cooldown, AI, target, or payment code changed. Removing a falsely displayed War Support debit does not create a free-resource exploit because the existing War Support gate remains in `available` and `custom_cost_trigger`, and the shared payment effect was already the authoritative debit path. No new loop, objective, route, or target was introduced.

## Validation

- Scoped `git diff` confirmed only the two listed source/localisation changes plus the required handoff file.
- Static reference checks found exactly one definition and one source reference for `independence_wave_fer_strategic_war_support_requirement_tt`.
- Source review rechecked the FER affordability trigger, shared strategic payment effect, dynamic standard transport helper, and decision lifecycle around the edited block.
- The touched localisation file begins with the required UTF-8 BOM.
- Mandatory `hoi4.gui_inspect` and `hoi4.gui_render` attempts for the status and formable windows were made before this handoff; both were blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED`, so no visual pass or `hoi4.gui_rewrite` was performed.
- Live HOI4 execution and in-game validation were not performed, per repository instructions.

Historical GUI artifact references retained by the source-of-truth map are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28ddca8151debd0c47d39c1780314d35b3d3f1d8ed91dc38b9ddae54e674528d/5313dbce3175a3e93eca27b6bdfa1147c7130bdda47a42a50280ba995be3f0e3/gui-inspect.4938ff384cd68acc.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/31dfbfe904ad10540b2e9acc8639fc25ec36ee2c40b65be55b5da2f108eb4568/independence_wave_status_window-full.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0d6628e50f989b4c7b7264b970286e228543cf35b7af4a53887d4ae62f51/eab86477ad9ff486f14c856c3682b40f8f67394dfd37423a56e6b2bc534a79da/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

Remaining issues are the package-family cost reconciliation, DM-01 disclosure, GUI artifact-manifest repair and re-render, typed probability evidence, and any parent decision on broader category or mission presentation.

No separate plan handoff was written because this was a narrow source/localisation repair.
