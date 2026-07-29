# Event 006 DM-57 Sponsorship Transaction Handoff

Date: 2026-07-15

## Scope and result

This handoff covers only the Event 006 DM-57 `Sponsor Another Breakaway`
transaction. The implementation turns the decision into a durable, bounded
queue contract that biases package selection, freezes exact sponsor metadata in
the shared plan, applies the promised opening package to the released country,
and consumes the queue record only after the shared Event 005/006 coordinator
has actually entered `committed`.

The implementation does not touch Events 014, 015, or 019, does not add a
periodic on action, and does not scan the world. Queue reconciliation is bounded
to `global.independence_wave_sponsored_breakaway_states`.

## Transaction contract

| Phase | DM-57 sponsorship behavior |
| --- | --- |
| Decision publication | The target state receives the active marker, exact sponsor scope, sponsor generation, opening strength `15`, and radical-sovereignty route enum `6`; the state is added to the bounded queue once. |
| Planning | Structurally valid queued anchors receive one full base-weight band (`+100`) in the candidate allocator. Current package eligibility is not part of queue validity. |
| Reservation | A successful selected reservation freezes the country row, state, sponsor, sponsor generation, opening strength, and route in a dedicated aligned sponsorship sub-ledger and mirrors the record into the reserved country pending metadata. |
| Pre-mutation validation | The executor proves the sub-ledger alignment and exact country row, anchor, pending record, source state record, sponsor, generation, strength, and route before ownership changes. |
| Country preparation | After generation reset and before package setup, the pending record is copied into durable country generation state and grants the `15` opening-force budget plus the radical-route AI preference. The source queue is not consumed. |
| Shared commit | Standalone Event 006 and joint Event 005/006 call the consumer only after `liberation_release_commit_plan` and only when `global.liberation_plan_phase` equals `committed`. |
| Consumption | The consumer re-proves the frozen source/country record, clears the exact source-state queue record, clears the country commit-pending marker, and increments the successful-sponsored-release counter exactly once. |
| Abort or rollback | Pending country metadata and the sponsorship sub-ledger are cleared with the plan contribution. The durable source queue record remains available for a later wave. |
| Stale cleanup | Only structurally broken records, ended/dead sponsors, or sponsor-generation mismatches are removed. Unselected and temporarily invalid candidates remain queued. |

## Key identifiers

### Scripted trigger

- `has_valid_independence_wave_breakaway_sponsorship_record`

### Scripted effects

- `independence_wave_clear_breakaway_sponsorship_record`
- `independence_wave_clear_pending_breakaway_sponsorship_metadata`
- `independence_wave_reconcile_breakaway_sponsorship_queue`
- `independence_wave_apply_pending_breakaway_sponsorship`
- `independence_wave_consume_committed_breakaway_sponsorships`

### Planner and durable state

- `global.independence_wave_plan_sponsorship_count`
- `global.independence_wave_plan_sponsorship_country_rows`
- `global.independence_wave_plan_sponsorship_states`
- `global.independence_wave_plan_sponsorship_sponsors`
- `global.independence_wave_plan_sponsorship_generations`
- `global.independence_wave_plan_sponsorship_opening_strengths`
- `global.independence_wave_plan_sponsorship_routes`
- `independence_wave_pending_breakaway_sponsorship`
- `independence_wave_sponsored_release`
- `independence_wave_sponsorship_commit_pending`
- `global.independence_wave_successful_sponsored_releases`

### Tuning constants

- `constant:independence_wave_allocation_weight.sponsored_candidate = 100`
- `constant:independence_wave_decision_gate.sponsorship_opening_strength = 15`
- `constant:independence_wave_government_route.radical_sovereignty = 6`
- `constant:independence_wave_league.danger_sponsored_releases = 3`

## Files changed for this transaction

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/script_constants/006_independence_wave_mechanics_constants.txt`
- `common/scripted_effects/005_006_liberations_collision_effects.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_execution_effects.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `docs/events/006_independence_wave/overview.md`

Several of these files already contained concurrent Event 006 balance,
formable, or documentation edits in the shared worktree. This task used
identifier-anchored edits and did not revert or rewrite those unrelated changes.

## Validation evidence

### Standalone Event 006 commit path

`common/scripted_effects/006_independence_wave_execution_effects.txt` contains
the only standalone consumer call. The order is:

1. validate and commit all frozen country origins;
2. call `liberation_release_commit_plan`;
3. require `global.liberation_plan_phase = committed`;
4. call `independence_wave_consume_committed_breakaway_sponsorships`.

The failure branch marks finalization failed and never invokes the consumer.

### Joint Event 005/006 commit path

`common/scripted_effects/005_006_liberations_collision_effects.txt` follows the
same order inside the exact joint-commit branch. The consumer runs before the
joint presentation flags are published, and the invalid-phase branch does not
invoke it.

An exact repository search found only these two call sites for
`independence_wave_consume_committed_breakaway_sponsorships`.

### Abort, rejection, and rollback preservation

- Candidate rejection never calls the source-record clearer.
- `independence_wave_clear_pending_package_metadata` clears only country-local
  pending sponsorship metadata.
- `independence_wave_clear_plan_contribution` clears the sponsorship sub-ledger
  and pending rows but does not call
  `independence_wave_clear_breakaway_sponsorship_record`.
- Verified shared rollback calls the Event 006 contribution cleanup before
  clearing the shared arrays, so the pending rows are still reachable.
- The source-record clearer has only two operational callers: bounded stale
  reconciliation and the post-commit consumer.

### Idempotence and successful-release counting

The consumer requires both the live source record and
`independence_wave_sponsorship_commit_pending`. A successful row clears both,
so a repeated consumer call cannot increment
`global.independence_wave_successful_sponsored_releases` again. The dangerous
cascade reads that committed counter, not queue size, while retaining the
existing durable radical-league, membership, common-cause, and reserve gates.

### Focus and source checks

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` with validation passed and no
  blocking diagnostics for the Event 006 focus source. The change affects only
  the radical-root `ai_will_do` preference and does not change layout.
- The sponsorship plan metadata trigger proves all six sub-ledger arrays equal
  the sponsorship count and constrains that count to the selected package count.
- The touched script blocks are brace-balanced and the targeted diff has no
  whitespace errors. The worktree reports only its existing line-ending
  normalization warnings.
- A bounded `hoi4.event_inspect` impact request for the consumer helper was
  attempted after source refresh. The server returned
  `ARTIFACT_STORAGE_LIMIT` because its retained artifact store was full; it did
  not return a source diagnostic. Exact call-site and state-flow evidence above
  was therefore verified directly from the source.

## Assets and localisation

No new player-facing object, icon, sprite, or localisation key is required.
The existing DM-57 decision text already promises support for the next
breakaway. The Event 006 system documentation and dynamic-helper contract were
updated to describe the concrete transaction.

## Simplifications, omissions, and blockers

No gameplay simplification, fallback, placeholder, or omitted requested route
was used. There is no implementation blocker. The event-chain MCP artifact
retention ceiling noted above is a tooling limitation only and does not alter
the transaction behavior.

No commit was created.
