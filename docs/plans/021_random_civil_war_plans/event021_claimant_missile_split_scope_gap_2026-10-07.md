# Event 021 claimant-source missile preflight scope gap

Disposition: accepted and queued for cross-system source/receipt repair, not closed by the Event 021 serial metadata bridge.
Acceptance basis: the full goal requires dynamic source allocation and cleanup for active ordinary claimants as well as governments; the accepted active review runs in the canonical government's `.20` callback.

`event021_parent_commit_active_front_row` enters the recorded donor country and calls the ordinary secondary adapter while ROOT remains the reviewing government.
That adapter calls `missiles_preflight_country_split` before the native civil war.
In `common/scripted_effects/032_missiles_operations_effects.txt:6811`, the helper saves the actual source as regular target `missiles_civil_war_parent`.
Its controlled-state loop then writes `missiles_site_civil_war_split_receipt_id` from `ROOT.missiles_civil_war_split_receipt_id` and adds each site's capacity to ROOT's country accumulator.
For a claimant donor under the government callback, those references point at the government rather than the recorded missile source.
The source-owned receipt ID and reserve can therefore disagree with the state receipts and capacity accumulator.

Repair those reads/writes through the recorded source or caller-owned temporary input and inspect `missiles_abort_operation`, `missiles_cleanup_operation`, split-child allocation and callback accounting for the same assumption.
Do not change missile tuning, spend unrelated country reserves, omit missile preflight, or claim native conservation from the Event 021 bridge tests.
Use a government-without-program/claimant-with-program fixture and a two-initialized-programs fixture with distinct receipts, sites, operations and reserves.
Only the recorded claimant's sites, operations, split receipt and counters may change; the government remains untouched except for its intended crisis role.
The Event 032 file is a shared subsystem; the latest narrow status check shows no changes to that path, but its exact owner diff and index state must be rechecked before any scoped edit or commit.
