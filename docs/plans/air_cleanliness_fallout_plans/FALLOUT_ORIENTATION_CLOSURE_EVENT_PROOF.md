# Fallout Orientation Closure Event Proof

Date: 2026-07-18

Status: dormant events `82` through `84` implemented and uncounted

## Scope

This tranche defines the human closure, hidden AI closure, and authenticated cleanup at `chaosx.fallout.82` through `chaosx.fallout.84`. It does not add an orientation caller, approve a missing implementation surface, or activate the living-world scheduler.

## Durable identity restoration

Every component result preserves five durable identity values before clearing its transient payload:

- transition generation
- live region
- government archetype
- country memory
- cause memory

The earlier closure starter created a new pending transaction after those transient fields had been cleared, but did not restore the four frozen identity fields required by `fallout_orientation_transaction_is_current`. A closure therefore could not pass the current-transaction gate.

`fallout_orientation_begin_closure` now copies region, archetype, country memory, and cause memory from the authenticated durable identity row before it sets the pending flag and issues an event. `fallout_orientation_closure_is_eligible` independently compares every durable identity value with the current transition, country registry, and global cause receipt. A stale or mismatched identity cannot enter closure.

## Human closure envelope

Event `82` requires all of the following:

- dormant orientation activation
- a current closure transaction
- a closure-stage issued envelope from the current generation
- exact component, mode, and branch equality between the transaction and issued envelope
- the human closure event token
- all five orientation component receipts
- no existing closure receipt

Its single option copies the issued token into a temporary request token and calls the cleanup scheduler. The scheduler repeats the full closure-entry gate and requires that request token to match the issued token before it replaces the closure envelope with the cleanup envelope. The visible description uses an exact twelve-row country-memory closure text, the current region and government archetype, and current Food, Clean water, Filters, Shelter capacity, Recognition, and Cohesion values. It does not claim that ordinary Fallout incidents are active.

## Hidden AI closure envelope

Event `83` uses the same closure-entry trigger and requires the hidden AI mode plus the exact AI closure token. Its immediate effect copies the issued token into a temporary request token and follows the same cleanup path as the human event. It has no reduced costs, automatic success mutation, alternate memory, or separate cleanup rule.

## Cleanup authentication

Event `84` must authenticate its stored envelope before its immediate effect runs. Its entry trigger requires:

- dormant orientation activation
- a current cleanup transaction
- a cleanup-stage issued envelope from the current generation
- exact component, mode, and branch equality
- the exact cleanup event token
- all five orientation component receipts
- no existing closure receipt

After entry, the event copies the issued cleanup token into a temporary request token. `fallout_orientation_cleanup_event84` then re-authenticates that request token against the stored envelope before clearing transient transaction data.

Only authenticated event `84` writes `fallout_orientation_closure_complete`, `fallout_orientation_closure_generation`, and `fallout_orientation_closure_day`. Events `82` and `83` cannot write the closure receipt. Cleanup preserves durable component receipts, orientation memories, and identity values because those fields are not part of the transient payload clearer.

## Dormancy and release count

No caller for `fallout_orientation_begin_closure` was added. No setter for `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active` was added. The missing regional, archetype, country-memory, capital-repair, government-row, and candidate-install approval surfaces remain blocked.

Events `82` through `84` have no event-log rows or event-detail rows. After the later immediate-resource and government pilots, the orientation tranche still lacks eight reserved component blocks, all callers, final runtime row producers, installable candidate packages, and final audits. These three events do not increase the Fallout release-floor count. The count remains 0 of 660.

## Asset disposition

The visible closure uses the existing dedicated Fallout sprite `GFX_report_event_fallout_orientation_closure`, backed by `gfx/event_pictures/fallout_world_end/report_event_fallout_orientation_closure.dds`. The hidden AI closure and cleanup have no picture. No zombie file, id, asset, sprite, audio, or path is referenced.

## Validation boundary

Static inspection confirmed one definition each for events `82`, `83`, and `84`, twelve exact country-memory closure rows, matching localisation coverage, preserved localisation encoding, balanced script blocks, no orientation caller, and no scheduler activation setter in this tranche.

The read-only HOI4 event inspector was asked to lint `chaosx.fallout.82` with helper expansion disabled and bounded traversal. It returned `EVENT_HELPER_PROJECTION_LIMIT` before producing an artifact. The event therefore has no successful MCP lint artifact. This is recorded as a tooling inspection blocker and is not treated as proof of runtime behavior.

Hearts of Iron IV was not run. Runtime delivery, save recovery, and multiplayer behavior remain unproven until a separately authorized test pass.
