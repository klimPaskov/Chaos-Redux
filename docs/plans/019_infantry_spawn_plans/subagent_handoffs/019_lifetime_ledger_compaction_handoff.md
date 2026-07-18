# Event 019 lifetime-ledger compaction handoff

## Result

Event 019 has a country-scoped, bounded maintenance state machine at the tail of
its existing `.900` pulse. It removes only fully detached terminal lot graphs
after their generation has completed closeout, then prunes detached generation
summaries outside the twelve rows retained by the Muster Board. Stable UIDs and
all gameplay, evolution, claimant, incident, management, and achievement
aggregates remain monotonic and unchanged.

No daily or world-iterating on-action was added. No new Event 019 code file and
no filename or implementation surface containing `registry` was created.

## Scheduling and work bounds

- A maintenance cycle is checked from stored row counts and the existing
  country pulse. An idle cycle is due no more often than every 30 days; changes
  to the core row counts mark the country dirty so a backlog can continue on
  the next country pulse.
- Candidate discovery and every referential scan retain a country variable
  cursor and inspect at most 24 source rows per pulse.
- One lot commit removes at most 64 logical rows, including the lot row,
  optional private template row, aligned child rows, and auxiliary evidence.
- One cycle commits at most four lots and four generation summaries.
- Candidate indexes are gathered during forward scans and removed only in
  descending source-index order. No iterated source array is mutated in place.
- A multi-pulse proof captures all main-ledger and auxiliary-array sizes plus
  `infantry_spawn_scenario_launch_serial`. Any drift restarts the proof from the
  same stable candidate instead of committing against stale indexes.

All thresholds, phases, and work budgets are in the existing
`infantry_spawn_ledger_compaction` script-constant category.

## Terminal lot certificate

A lot graph is removable only when all of the following are proved:

1. its exact generation row exists once, is `resolved` or `archived`, and has
   therefore already passed synchronous closed-generation achievement
   evaluation;
2. the lot is `demobilized`, `destroyed`, or `unaccounted_settled`, with exact
   zero live-unit count, equipment debt, manpower liability, and claimant UID;
3. it is not the currently selected lot;
4. every child unit has the same lot, generation, and template identity, is in
   the corresponding terminal state, and has exact zero claimant UID;
5. every obligation referring to the lot belongs to one of those exact child
   unit UIDs and the same generation, is `settled` or `forfeited`, and has exact
   zero outstanding amount and debt value;
6. every selected-state row referring to the lot uses the same generation;
7. any removable template exists exactly once, belongs only to that lot, is
   retired, and uses the non-recruitable `locked_pending` or `spawn_only` mode;
   shared, integrated, reusable, or otherwise referenced templates are retained;
8. every component and auxiliary UID row tied to a removed unit or removable
   template is identified within the same bounded proof.

Immediately before deletion, the complete capped candidate batch is
revalidated by stable UID, source index, terminal status, zero balances,
generation identity, and template identity. Exact expected post-commit sizes
are calculated before any mutation. A post-commit mismatch marks the existing
ledger invariant failure and stops maintenance.

## Auxiliary evidence and historical identity

The compactor removes matching entries from:

- locked-template and spawn-only-template UID arrays;
- technology-locked template and unit UID arrays;
- transfer-eligible unit UID arrays;
- pretechnology template and unit UID arrays;
- the aligned achievement pretechnology unit-UID/gate pair;
- achievement composition-disqualification unit UIDs; and
- supervised-demobilization lot UIDs, after exact generation closeout has
  consumed them.

Achievement pretechnology pair alignment is checked before and after each
commit. Integrated-random lot UID entries are retained as monotonic achievement
progress tombstones; their UIDs are never reused, and the append surface in
`common/scripted_effects/019_infantry_spawn_achievement_effects.txt` stops at the
exact Order from Noise distinct-lot threshold. Supervised-demobilization lot UID
evidence is removed only after closed-generation exact proof has completed.

Transferred units and transferred obligations are conservatively retained.
Their cross-country derivative and transfer identity is not treated as a
detached local graph. Claimant rows are likewise retained as historical actor
identity; compaction requires exact zero claimant references on every removed
lot and unit.

## Generation summary pruning

After lot maintenance, the same state machine considers generation rows older
than the newest twelve Muster Board history entries. A summary must be
`resolved` or `archived` and have no remaining lot, unit, obligation, or
selected-state generation reference. It is also retained when referenced by
the country's last-closed-generation identity, derivative origin, or scenario
claimant origin. A generation commit removes all nine aligned summary fields at
one source index and repairs the open Muster Board history source indexes.

## Transaction isolation

Maintenance requires `infantry_spawn_scenario_transaction_is_idle = yes` and
pauses for invariant failure, scenario setup, same-tag or dynamic rollback,
derivative creation, generation audit, active achievement rail proof, and every
lot-targeted management mission. Open incident, prefire-opening, claimant-demand,
rail, demobilization, and division-template-lock transactions also pause it. It
also pauses while any deferred Event 019 action remains queued. The pulse
replays deferred actions before maintenance,
so an undrained deferred lot, claimant, incident, opening, rail, or cooldown
record cannot lose its identity to compaction.

The post-freeze replay integration centralizes the twelve authoritative pending
flags in `infantry_spawn_has_deferred_event19_action`. The management/event
setters, replay clearers, shared trigger, and compaction gate all cover the same
twelve records: nine management completions plus incident, prefire-opening, and
claimant-demand choices. `infantry_spawn_ledger_compaction_may_advance` consumes
that shared trigger through one negative gate instead of maintaining a duplicate
flag list. Valid records that cannot yet execute remain queued and block
compaction; structurally invalid records are cleared through quarantine and mark
the ledger invariant failure.

Deferred-action pulse continuation additionally requires the invariant failure
to be absent. If quarantine raises the invariant during an active maintenance
cycle, `infantry_spawn_run_lifetime_ledger_compaction` immediately enters its
fail-closed path, clears active and dirty maintenance state, and returns to the
idle phase. An inactive cycle cannot start under the invariant. A quarantined
record therefore cannot combine with another queued record or a maintenance
backlog to create a self-rescheduling pulse loop.

When ordinary country-pulse eligibility ends while compaction still has a
backlog, the existing `.900` event is rescheduled with the existing audit-pulse
delay. It is never rescheduled while a scenario transaction is locked; the
transaction release owns that wake-up.

## Muster Board behavior

Lot compaction decrements `infantry_spawn_selected_lot_index` only when a row
before the selected lot is removed; the selected row itself is ineligible. An
open Muster Board is repaired incrementally after a commit: at most 40 cached
lot rows and 12 cached history rows are checked, a removed UID is discarded if
present, and later source indexes are decremented. Terminal lot/unit removal
does not change the live-only family cache. A closed board reconstructs every
cache on its next open.

## Files changed

- `common/script_constants/019_infantry_spawn_constants.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
  (shared deferred-action and pulse-continuation gates)
- `common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_ledger_effects.txt`
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
  (coordinated exact replay and quarantine integration)
- `common/scripted_effects/019_infantry_spawn_pulse_effects.txt`
- `common/scripted_effects/019_infantry_spawn_achievement_effects.txt`
  (parent-owned coordinated cap for retained integrated-random proof UIDs)
- `events/019_infantry_spawn.txt`
  (coordinated deferred event-choice capture)
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_lifetime_ledger_compaction_handoff.md`

## Assets and localisation

No player-facing action or text was added. No icon, sprite, `.gfx`, `.gui`, DDS,
or localisation change is required.

## Validation scenarios

- A settled terminal lot with detached units, obligations, selected-state rows,
  private retired template data, and auxiliary evidence compacts as one aligned
  reverse-index commit.
- An open or audited generation, active/claimant/transfer-staged unit,
  outstanding or transferred obligation, claimant-owned lot, selected lot,
  reusable template, or lot with more than the commit budget remains intact.
- A concurrent append, scenario launch-serial change, or auxiliary-size change
  invalidates the snapshot and restarts proof without deletion.
- A same-tag/dynamic scenario lock or undrained deferred action pauses both
  maintenance and maintenance-only rescheduling.
- A generation with any remaining child reference, one of the protected scalar
  identities, or a position inside the newest twelve history rows remains.
- An older detached resolved generation removes all nine aligned summary
  fields, after which an open Muster Board repairs its cached history source
  indexes.

## Independent audit and remediation

The independent compaction audit reviewed the frozen first-pass gameplay files
before this handoff was finalized. It found no P0 issue and identified two P1
corrections:

1. fail-closed maintenance could be marked dirty by its own partial size change
   and re-enter maintenance-only scheduling despite the invariant failure; and
2. supervised-demobilization lot UID closeout evidence was neither snapshotted
   nor retired.

The final implementation clears active/dirty maintenance state on failure,
refuses to start while the invariant flag exists, and treats an active invariant
as an immediate quiescing failure. It also gives supervised-demobilization
evidence its own 24-row scan phase, snapshot boundary, capped candidate rows,
pre-commit UID revalidation, descending removal, and exact post-size proof.

The fresh-hash audit then found one remaining P1: the open-board refresh helper
performed full lifetime lot and nested family-ledger scans on a successful
commit. The final path replaces that helper with the bounded 40-row lot-cache
and 12-row history-cache repair described above; no compaction commit calls the
full Muster Board rebuild.

Parent review additionally caught the missing last-closed-generation scalar
exclusion and the deferred-action gates before release. Both are present in the
final triggers.

The final pre-integration fresh-hash re-audit was clean at P0/P1. It confirmed
that no compaction path calls a full Muster Board refresh or rebuild, cache
repair is capped at 40
lot rows and 12 generation rows, cached removal is descending with later source
indexes decremented, terminal rows remain outside live-family aggregation, and
no P0/P1 regression remained.

The post-freeze deferred-replay integration re-audit is also **clean at P0/P1**.
It matched the shared trigger against all pending-flag setters and clearers: each
surface contains exactly the same twelve authoritative flags. The ledger gate
contains only the shared trigger call, replay runs before compaction, queued
valid records continue to block compaction, and structural replay failure both
quarantines its record and raises the existing ledger invariant. The revised
deferred-only continuation gate suppresses further scheduling under that
invariant, while an already-active compaction cycle fail-closes and clears its
continuation state. The bounded effects, cache repair, exact commit checks, and
achievement evidence handling retain their previously audited hashes. No
gameplay file was changed by this re-audit; this handoff update is documentation
only and remains the durable audit record for the tranche.

Gameplay hashes reviewed by the final audit:

- ledger effects: `D8F7FC86C59283C560C4813A06CA977D662E19D0233EE990822A685D06D3CE84`
- shared Event 019 triggers: `17B27E02B21710FFA7AFC477E90FD12BD4736F5F188B556E95C586BB22CF1B4A`
- ledger triggers: `30ABC883BD65DCB0DB76CB7ED860DC8A6364E4D4A2B15A3077C2C304B59BF806`
- script constants: `17F0758174404C4FF81F747D0D72923DF8EBC3B8AF3472897B6B7E72BF4674B3`
- deferred management replay: `424109D8C473C1F4E4B21BD49C416A35F9DC3A741D299BA6E562451752E00B7F`
- deferred event-choice integration: `F0D88177A1C0B348D2485EF44B1EB6E685DEC99381F971551A22AF3CF2611D46`
- pulse integration: `96771A3DD33803F6057C17C5061D631F423C9C8FA5A07D32E01C421726B4E54A`
- coordinated achievement cap: `DDC1388609BE209EAF90331500291FE666474BC668F96240C4BBF537150822AE`

## Future extension suggestions

- If terminal claimant history is normalized into a dedicated immutable archive
  schema, add claimant-row compaction as a separately audited tranche.
- If cross-country transfer records gain an exact consumption/archive marker,
  extend terminal eligibility to `transferred_out` units and transferred
  obligations without weakening the current local-reference proof.
- Profiling can raise the conservative 24/64/4 budgets through the existing
  constants without changing the transaction or eligibility contract.

## Simplifications, omissions, and blockers

No fallback or substitute route was used. Claimant and transferred-object rows
are intentional preservation boundaries because their external historical
identity is not locally provable as detached; they are not silently erased.
There are no asset, localisation, wiring, or implementation blockers in this
bounded compaction tranche.
