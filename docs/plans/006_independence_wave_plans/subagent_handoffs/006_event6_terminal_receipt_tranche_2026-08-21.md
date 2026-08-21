# Event 006 terminal receipt tranche

## Scope

This bounded tranche adds source-level observability around the standalone `chaosx.nr6.1` transaction without changing allocation weights, package admission, player-facing entry, or pre-event surfaces.

## Changed files

- `common/scripted_effects/006_independence_wave_execution_effects.txt`
- `.tools/audit_event6_allocator.py`
- `docs/events/006_independence_wave/systems/terminal_receipt.md`

## Implementation

- `independence_wave_clear_standalone_terminal_receipt` clears the previous durable receipt only at the start of a new standalone root transaction.
- `independence_wave_snapshot_standalone_terminal_receipt` copies the current plan id and dates, terminal phase, failure codes, chaos band, target and selected counts, sponsorship and expected-state counts, execution-stage counts, and terminal outcome flags before a later coordinator reset can erase transient plan data.
- The snapshot is called after every standalone terminal branch, including committed, pre-mutation cancellation, post-mutation compensation, finalization failure, and stale-plan failure.
- The public event remains committed-only and no decision, mission, cost, queue, pressure, or pre-event UI surface was added.
- The allocator audit now checks the root fallback contract, committed-only presentation, dormant-shell validation, state transfer, capital finalization, receipt ordering, receipt payload fields, and outcome flags.

## Validation

The following source audits are required after integration:

- `.tools/audit_event6_allocator.py`
- `.tools/audit_event6_flags.py`
- `.tools/audit_event6_country_api.py`
- `.tools/audit_event6_scenario_matrix.py`
- `.tools/audit_event6_form16.py`

The narrow Event MCP lint was attempted twice after the edit, but the server timed out after 180 seconds on both calls. The latest cached Event 006 MCP evidence remains partial with zero selected blocking diagnostics. No live Hearts of Iron IV session was launched.

## Remaining limits

This receipt does not prove a successful live release, complete package admission, typed probability balance, focus or GUI runtime rendering, super-event audio rights, or full spec completion.
