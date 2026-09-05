# Event 012 reconciliation acceptance-window gate

Disposition: implemented.

The host-side `gods_of_africa_accept_reconciliation` target decision now delegates both `target_trigger.FROM` and `available.FROM` to `gods_of_africa_participant_can_reconcile`, while retaining the reparations-paid and reconciliation-offer-pending gates.

This keeps the acceptance row unavailable after the participant's current-generation, non-war, defiance, and reconciliation deadline checks fail, so a timed-out offer cannot remain as a clickable no-op.

Implementation evidence: `common/decisions/012_africa_gods_decisions.txt` under `gods_of_africa_host_category`.

Validation evidence: focused `hoi4_event_inspect` lint for `chaosx.nr12.600` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and `blockers: []` after the source edit on 2026-09-05.

The MCP report remains bounded partial because workspace-wide helper projections are deferred; this does not block the focused Event 012 result.

Remaining boundary: live in-game consumer validation remains with the owner.
