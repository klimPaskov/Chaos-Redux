# Event 028 caller-owned helper outputs

Disposition: bounded caller-storage correction implemented; native helper-return execution remains an acceptance gate.
Acceptance basis: the full package requires the prepared three-pair board to reach dispatch/history and an accepted two-day lock to schedule its preparedness/resolver chain.
The completion audit's F01 identified newly created temporary helper outputs that were consumed after return without storage in their caller frame.

## Exact boundaries

The Event 028 prefire branch in `chaosx_settings_effects.txt` initializes `asteroid_incoming_prefire_ready`, `events_log_history_payload_override` and `events_log_history_payload_override_active` to the existing zero constant before `asteroid_incoming_prepare_random_event_fire`.
The accepted-target caller in `028_asteroid_incoming_runtime_effects.txt` initializes `asteroid_incoming_lock_result` before `asteroid_incoming_lock_candidate_pair` and its subsequent result check.
These are the actual consumers, not an initializer hidden inside the returning helper.
No dispatch, option weight, target, nonce, outcome, cost or elapsed-day tuning is changed.
The impact processor, physical receipts, delayed-news country count and dust destruction contributions remain separate unfinished source tranches and are excluded from this commit.

## References and checks

Fresh MCP `reference_read` covered offline `Data structures:435–443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Line 440 explicitly distinguishes helper-created temporary lifetime from caller-preinitialized storage; the installed assignment command alone does not prove that behavior.
The relevant installed `set_temp_variable` section is effects documentation lines 7820–7827, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, retained in the [skill handoff](subagent_handoffs/skill_maintenance_20261003.md).
The shared events skill's conservative lifetime contract and recursive gated-dispatcher review are used; that reusable maintenance change is commit `0d9f7a4cd9436bd0c35862ad2d6849e7a91ec7a5`.

The actual parsed caller ASTs assert initialization of all four consumed outputs before their respective helper calls.
The same validation run retains 19 explicit availability cases, the matching five-option return board and the recursive authorization/dispatch/accounting ordering check.
It models the availability triggers and checks source ordering, not complete native dispatch or call-frame lifetime.
Unknown evaluated trigger commands fail instead of being silently accepted.
No basic syntax pass or unchanged weight number is presented as equivalent engine evidence.

The fresh event route is responsive but focused inspection defers helper lifecycle, and the required artifact-backed comparison cannot retrieve its provenance manifest.
`hoi4.script_validate` is not exposed, and connected version/task negotiation was not established, so unsupported helper-expansion/job routes are not invented.
These exact native/source evidence limits remain open; the caller-storage correction does not complete F01's separate physical helper work or the full Event 028 package.
