# Event 012 D1 action acceptance and disposition handoff

Date: 2026-07-30.

## Scope and boundary

This is a documentation-only acceptance pass over the 102 authoritative action concepts in `docs/specs/012_africa_specs/matrices/012_africa_decision_mission_matrix.csv`.

Only `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` and this handoff were changed.

No decision, event, scripted effect, model, tag, GUI, localisation, asset, or shared runtime file was edited.

## Result

Every former `merged` action row now has one explicit disposition in the acceptance ledger.

| Disposition | Rows | Meaning |
| --- | ---: | --- |
| `implemented` | 5 | The matrix instant contract is live through the common quoted action lifecycle. |
| `queued_with_owner` | 85 | The selector/profile/lifecycle exist, but the matrix timer or objective is not accepted. |
| `blocked_with_gate` | 12 | A deliberately closed review, model, package, or terminal gate prevents a truthful playable action. |
| `rejected_with_reason` | 0 | No matrix action was rejected. |

Implemented rows are 1 `guarantee_sovereignty`, 7 `recognise_provisional_government`, 20 `admit_member_in_emergency`, 27 `guarantee_regional_representation`, and 38 `grant_core_recognition`.

The ledger records the exact action constant, selector ID, profile kernel/target/duration band, live lifecycle evidence, matrix duration, requirements, success, partial-success, failure, cleanup, and remaining owner for every row.

## Static runtime evidence

The live source contains all 102 `africa_select_<key>` selectors, all 102 `africa_action.<key>` constants, and all 102 profile branches keyed by `africa_requested_action_id`.

Every row flows through the same current-target lifecycle: `africa_compute_action_quote`, `africa_validate_action_specific_requirements`, `africa_begin_quoted_action_against_target`, `africa_resolve_action`, `africa_apply_current_action_outcome`, and `africa_cleanup_action` in `common/scripted_effects/012_africa_action_effects.txt`.

The launch path recomputes the quote, revalidates the target, debits only after validation, creates one action-generation record, and either resolves an instant action or activates the corresponding shared mission.

Cleanup removes the precise shared mission, state-project links, target arrays, capacity reservations, natural-disaster reservation, action variables, and applies the target cooldown before allowing a new action.

Selectors are zero-cost quotation selectors with `ai_will_do = { base = 0 }`; the host-only AI dispatcher uses the same profile and final validator rather than a human cursor.

## Critical and high issues

### Action 73 is an explicit reviewed block

Row 73 `weaponise_fictional_pathogen` is `blocked_with_gate`.

The selector and semantic validator both require `africa_fictional_pathogen_review_authorized`, and no runtime setter exists.

The approved Event 013 bridge covers only the Rain and Drought actions; no approved abstract disease API exists for this action.

No authorisation setter, real-world pathogen procedure, weather substitution, or fallback API may be added.

The parent must first accept an abstract fictional contract covering target validity, delivery/access, stockpile consumption, full/partial/failure/backfire outcomes, source registration, cleanup, and diplomatic consequences before a separately approved API or Event 012 implementation tranche begins.

### Actions 74-76 are deliberately model-gated

Rows 74 `awaken_stone_cohort`, 75 `train_gorilla_heavy_infantry`, and 76 `organise_pan_sappers` are `blocked_with_gate`.

Their selectors and validators require the unset `africa_strange_formation_package_ready` gate.

All three keep their matrix long-duration records in the ledger, but no model, entity, template, tag, free-unit fallback, or substitute formation is authorized in this task.

The future owner is the separately approved model-and-formation package, which must prove the model/entity/template consumer before it can set the gate.

### Actions 85-92 are deliberately world-gated

Rows 85-92 are `blocked_with_gate`.

External package installation requires `africa_world_package_implementation_ready`, which must remain unset until all six packages pass their shared W0-W4 proof, and terminal identity additionally requires the unset `africa_the_world_super_event_package_ready` gate.

Rows 85-89 and 91-92 therefore remain blocked on W0-W4 package, sponsorship, union, war, and postwar lifecycle work.

Row 90 `declare_the_world_is_one` also remains blocked on the S1 atomic terminal presentation package.

No external continent fallback or terminal identity substitute is accepted.

## Timer and mission-objective disposition

All 95 non-instant live profiles are explicitly recorded row by row in the ledger.

The live bands are four short (60-day), 21 medium (120-day), 56 long (240-day), and 14 epic (540-day) shared missions.

The full list of each row's matrix duration, action kind, requirements, current profile, fixed live duration, and owner is in its ledger record; the four bands are not treated as acceptance equivalence.

Eight offer-response rows (11-18) can additionally open `chaosx.nr12.210`, but the response event does not create the matrix-required per-action project or objective contract.

The remaining timed records resolve through the common timeout outcome roll without a matrix-specific active objective.

Row 51 `open_voluntary_return_registry` now uses the shared `timed_country/host/medium` profile. Its existing row-specific contract supplies a 90-180-day range with a 135-day default, and the shared medium mission resolves the registry through the normal timeout/outcome path rather than opening it immediately.

The D1 action-duration/objective owner still uses an engine-safe record representation for dynamic duration and binds objectives only where the matrix requires active play. This tranche closes the row-51 instant mismatch without revising the source matrix.

The prior scoped `days_mission_timeout` proposal remains unsafe because no vanilla or approved reference evidence proves a scoped variable is accepted by that targeted decision field.

## Current diaspora evidence

The full-goal delta correctly described missing diaspora writers at its fixed audit commit, but the current shared worktree contains the G1 owner-protocol tranche and must be assessed as newer live evidence.

`common/scripted_effects/012_africa_diaspora_effects.txt` now supplies target-owned consent, refusal, counterterms, withdrawal, emergency activation, capacity, and outcome helpers for rows 52, 53, 55, 56, 57, and 58.

`events/012_africa_diaspora_protocol.txt` calls the target response helpers, and the action start path calls the G1 validation and response hooks.

Those six rows are queued only for D1 timer/objective acceptance, not blocked for absent consent or emergency writers.

This G1 source is uncommitted concurrent work and needs parent integration review before any broader completion claim.

## Decision category lifecycle and mission quality

The Charter Council owns quotation state, selected target/state cursor, action generation, resource reservation, and family paging.

The shared action record prevents two concurrent actions against one target, maintains host-owned active-count and duration arrays, and uses exact target/host generations for resolve or cancellation.

Mission quality is not accepted for the 95 timed profiles because the current four generic timers do not prove the matrix's named corridor, logistics, public, construction, constitutional, war, research, congress, rescue, or terminal objectives.

Duplicate action risk is currently controlled by the active record, per-target active flag, bounded capacity, action generation, and recent-target cooldown; no free-unit, core-spam, equipment-farming, war-goal-spam, or cooldown-bypass path is accepted through the reachable common runtime.

## Cost, requirement, AI, tooltip, and route-lock findings

Profiles use concrete quote inputs across political and command attention, manpower, infantry/support equipment, trucks, trains, convoys, fuel, civilian capacity, intelligence capacity, stability, and war support.

The execution quote, not the zero-cost selector, is the payment surface, so the system is not accepted as a passive political-power store.

Final exact requirements remain primarily in `africa_validate_action_specific_requirements`; the generic post-click preflight event is not an action-specific blocked-tooltip substitute and remains a D1 clarity queue.

AI target evaluation is bounded and calls the same final validator, so it does not rely on a player selection click.

The static audit found no live AI route past the Action 73 review gate, strange-formation model gate, or world readiness gates.

The six decision-list-only families have no recorded accepted Charter-window disposition: Scramble response (77-84), World order (85-92), Constitutional route crises (93-99), Post-unification governance (100), Host opening (101), and Regional restorations (102).

Their precise missing owner is the D1 decision-surface/UI owner; retain the normal decision-list selectors until that owner explicitly accepts list-only presentation or designs matching Charter-window pages with equal costs, tooltips, AI parity, and cleanup.

## Exact remaining queue

1. D1: implement or explicitly revise the matrix-required objective and duration representation for the remaining `queued_with_owner` rows and the 95 live non-instant profile records documented in the ledger.
2. D1/UI: decide the six decision-list-only family presentations without silently treating the current list as accepted GUI coverage.
3. D1 design/API: retain Action 73 blocked until the parent approves an abstract fictional disease contract and, only if needed, an Event 013 disease API.
4. Model/formation package: retain Actions 74-76 blocked until approved models, entities, templates, consumers, caps, and cleanup can set `africa_strange_formation_package_ready` truthfully.
5. W0-W4 plus S1: retain Actions 85-92 blocked until the six external packages, sponsorship/union/war/postwar protocols, and atomic terminal presentation readiness are accepted.
6. Parent review: integrate and verify the concurrent G1 diaspora owner-protocol tranche before using its newer evidence to replace the fixed-commit missing-owner finding.

## Validation and limits

The ledger update parsed exactly 102 matrix rows and exactly 102 action-concept ledger rows, verified matching row order and action keys, and then checked all 102 live selectors and profile branches.

It also verified the six shared lifecycle identifiers and counted exactly 95 non-instant profiles against the live profile table.

No campaign simulation, HOI4 launch, live GUI fidelity review, or new probability run was performed because this task changed documentation only and the underlying gameplay files are concurrently owned.

No models, tags, gameplay changes, fallback claims, or commits were made.
