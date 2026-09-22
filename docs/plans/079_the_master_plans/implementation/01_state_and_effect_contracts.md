# Event 79 state and effect contracts

Status: implementation design. Proposed names are not claims of existing Clausewitz functions. The parent implementation owner must verify the installed engine and current project helpers before writing syntax.

## Authoritative records

Use a bounded registry of active races and target-owned or registry-indexed participant rows. Every lookup requires a target country identity and a race generation. Country identity by itself is insufficient because a released country may enter a later race.

| Record | Required fields |
| --- | --- |
| Race | Slot, generation, target identity, opening date, activated stage, lifecycle state, winner identity, closure reason, shared firing receipt, evolution-log receipts |
| Participant | Race key, sponsor identity, initial human/major status, registration date, seed components, current score, activity date, suspension reason, withdrawal state |
| Positive-action history | Race key, sponsor, family, completion date, actual gain, actual paid receipt, pledged ideology, delivered-output receipt |
| Interference history | Race key, victim, attacker, completion date, actual loss, loss-budget period, evidence receipt |
| Action | Stable action ID, race key, payer, recipient, selected rival where relevant, family, scale, pledged ideology, political recipient, start date, due date, delivery state, payment transaction ID |
| Project | Project ID, target state identity, output token and level, original contracted factory count, funded installments, remaining work, sponsor reservation, paused date, post-race owner |
| Institution | Race key, institution kind, aligned sponsor, recipient identity, creation date, expiry date, creating action receipt |
| Completion archive | Race key, target identity, winner or external overlord, dates, stage, outcome, paid-rival participation, achievement qualification facts |
| UI selection | Local player's selected active race key, selected rival, expanded state, pin preference |

The logical records above may be implemented as documented parallel arrays with numeric IDs and supported country references. Do not invent token-keyed maps or dynamic variable names unless the installed engine explicitly supports them. Verify numeric bounds before choosing the generation counter's range.

## State machine

The race proceeds through reserved, active, committing, and won. An external change can move reserved or active to invalidated. Administrative shutdown can move it to cancelled. An unexpected failed takeover postcondition moves committing to commit_failed and freezes further writes to that race until a validated repair resolves it.

An action proceeds through quoted, paid, running, delivered, and settled. It may instead become cancelled with a component-level refund disposition. Quoted is not paid. Delivered is not refundable physical stock. Settled receipts remain as proof against duplicate completion or refund.

Only the parent race owner can change the winner or close the race. UI code can select a view and request an action. A news event can report a result. Neither can mutate another race's identity or decide the winner.

## Opening sequence

First verify capacity and choose a target. Reserve the target and generation before notifying participants or updating a successful-firing log. Build the participant roster once and calculate each seed from a single snapshot. Initialize all aligned arrays before exposing decisions. Record the accepted root firing once. Only then make the race visible and send opening reports.

If selection fails before reservation, return unavailable to the shared selector. If initialization fails after a reservation but before public activation, remove only that reservation and do not consume a false successful-firing receipt.

## Starting an action

Resolve the action's race key and confirm active status. Resolve the payer, recipient, selected political target, and any rival. Check slots, cooldown, political conditions, actual state placement, and every resource component. Quote all eligible costs using the shared framework. Recheck affordability immediately before the first debit.

Debits across unrelated native effects are not a database transaction. Perform complete preflight first, debit only verified supported components, and record actual paid amounts as each succeeds. If a later component unexpectedly fails, use explicit receipt-based compensation for components actually paid. Do not claim the engine has atomic rollback.

Once paid, persist immutable action identity and exact future obligations. UI selection changes must not affect those fields. Reserve factory capacity or escrow material through the proven owner adapter.

## Completion sequence

Resolve the saved action key and reject a stale generation. Verify that the race is active and that the political or material recipient still qualifies. Reconcile physical delivery or the native political result. Calculate saturation from completed family history before adding this completion. Apply the ordered political state changes, calculate gain, and update the score once.

If the score reaches 100, mark the race committing before any delayed notification. Snapshot the intended post-campaign politics and execute the verified relationship transition. Check the actual puppet-of-winner postcondition. On success archive award facts, settle all affected actions, release future reservations, close the race, and queue reports. On failure retain a single diagnostic commit receipt and grant no completion award. Do not rerun a delivered action automatically.

For a nonwinning completion, record the completed family and delivery history, free the action slot, and notify the relevant player. Rebuild live rank views from current scores.

## Ranking and decay

Compute rankings from current participant rows. Never append historical scores to a global maximum array. A score reduction must immediately change ranking order. Tied rows are presentation ties until a genuine threshold-crossing action is processed.

A bounded periodic receiver handles active-race expiry work, five-day display milestones, 30-day inactivity checks, and institution expiration. Active factory commitments need daily capacity accounting or an equivalent verified capacity-change ledger. This is a bounded active-project update, not a whole-world scan. The registry contains at most the designed number of active targets. Use target or participant lifecycle hooks where documented to reduce polling. Do not create a daily whole-world scan merely to discover new majors or players. Join reconciliation can run on race opening, relevant controller/major-status hooks, and the bounded attention check.

## Save and load

Persist identities, paid receipts, funded progress, generations, stage, and authoritative scores. Rebuild transient ranking and UI caches after load. A loaded paid action must not debit again. A loaded delivered action must not deliver again. A loaded closed race must not re-register as active.

Use tombstones or deferred compaction while scheduled callbacks still reference a row. If arrays are compacted, every reference must use a stable key and resolve the new row. Reusing a slot requires incrementing its generation before activation.

## Logging and diagnostics

Event-owned diagnostics should record race key, action ID, payer, target, variant, quoted amount, actual paid amount, delivered amount, score before and after, and closure reason. Keep verbose traces behind test flags. Player-facing tooltips must use translated descriptions, not raw IDs.
