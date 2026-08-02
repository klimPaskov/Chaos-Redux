# Event 012 RSA exile-custodian cleanup

Date: 2026-08-02.

Status: Implemented source repair; live-save acceptance remains open.

## Scope

The RSA exile transfer makes one existing African patron the new Event 012 host and copies the suppressed host's surviving member arrays without copying the custodian itself.

The custodian could nevertheless retain its old `africa_relationship_state`, `africa_member_host_generation`, `africa_member_confidence`, `africa_selected_roster_target`, or pending-transition notice on its own country scope.

## Change

`common/scripted_effects/012_africa_rsa_effects.txt` now clears those member and roster markers in the exile-patron initialization block before the successor host receives the copied host state.

The existing selected-country cleanup and array rebuild remain unchanged, and no country tag or fallback host is created.

## Expected behavior

- The accepted patron is the sole current host and has no stale member relationship or roster-selection marker from the suppressed host generation.
- Other copied members retain their relationship states and receive the successor generation as before.
- The no-patron terminal path and original-host preservation flags remain unchanged.

## Validation boundary

Static source inspection confirmed the cleanup runs before the successor arrays are rebuilt and only targets the selected exile patron.

The bounded `hoi4_event_inspect` lint for `chaosx.nr12.1` returned status `ok` with no blocking diagnostics, while its workspace-wide helper analysis remained deferred by the adapter.

No Hearts of Iron IV executable or live save was launched, so patron succession and member-generation equality remain open acceptance work.
