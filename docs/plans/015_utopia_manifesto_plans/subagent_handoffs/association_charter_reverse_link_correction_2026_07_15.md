# Event 015 association-charter reverse-link correction

Date: `2026-07-15`

Scope: completed association-charter ownership, annexation, withdrawal, teardown, and multiplayer cleanup

## Problem closed

Association duties previously cleared their temporary mission state on completion while leaving the visible state charter modifier and flag. The partner relationship was indexed, but the charter state itself was not persistently reverse-indexed. Later partner annexation or ownership transfer could therefore leave a charter marker on a successor-owned state, and founder cleanup lacked an exact state relationship to remove.

## Implemented data model

The charter now records exact reverse links on all three participating scopes.

| Scope | Array or flag | Purpose |
| --- | --- | --- |
| Charter state | `utopia_manifesto_association_charter_founders` | every exact Event 15 founder whose charter remains valid on the state |
| Charter state | `utopia_manifesto_association_charter_hosts` | recorded host countries for current charter relationships |
| Founder | `utopia_manifesto_association_charter_state_targets` | exact charter states owned by this founder's relationship |
| Host | `utopia_manifesto_association_chartered_states` | exact states hosted under association charters |
| Host | `utopia_manifesto_association_charter_host` | host-side relationship marker |
| Founder | `utopia_manifesto_association_charter_lost` | durable evidence that a completed charter was lost |

New reusable helpers register and unregister exact founder links, clear state packages only after the final founder leaves, clear all founder-owned charter links, clean links for an annexed partner, and reconcile changed charter-state ownership.

## Lifecycle behavior

- Association-duty start registers its live partner in the League reverse-link system.
- If the active duty target is annexed, the duty fails, its mission and temporary state clear, and the exact partner link is removed.
- Completion converts the temporary duty state into durable founder, host, and state reverse indexes.
- If a completed partner is annexed, only that founder's exact charter-state relationship is removed. The bridge reads the founder's durable state index and filters it by the recorded annexed host, so partner-side terminal array cleanup cannot erase the cleanup input before the bridge runs.
- If a charter state's owner changes away from its recorded host, bridge `.165` removes only the affected founder link. Another founder's valid charter on the same state remains.
- The final founder-link removal clears the state modifier and flag so no charter survives on an unrelated successor-owned state.
- Voluntary withdrawal clears the withdrawing founder's complete charter set.
- Founder teardown and terminal external-network cleanup clear all exact founder, host, and state links.
- Charter loss records Ledger Need and Concord consequences, refreshes recognized external partners, and refreshes formation proof.
- Recognized compacts and surviving associates are re-adopted during network refresh so loss of one charter does not erase another live external compact.

## Narrow callbacks

`on_state_control_changed` snapshots both Necessary Ground case-state founders and association-charter founders, deduplicates them, and dispatches hidden founder-rooted event `.165` after one hour. The existing delay still allows full-annexation bridge `.163` to settle country disposition first.

`on_annex` snapshots case and League founder relationships before terminal target cleanup. Annexed association partners and completed charter hosts are reconciled through their exact reverse indexes. No daily, weekly, monthly, or world-iterating scan was added.

### Follow-up, 2026-07-16

The current package also reconciles charter ownership through the bounded self-scheduling Event 15 actor pulse and the peace-conference callback. This covers owner-only changes that do not invoke `on_state_control_changed`. Bridge `.165` now snapshots settlement, long-supply, and island-lease founders alongside case and charter founders and calls the shared external-term integrity reconciler. The actor pulse remains limited to active Event 15 actors; no global country iteration was introduced.

## Files changed

- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `events/015_utopia_manifesto.txt`
- Event 15 canonical documentation, proof matrix, and resume packet

## Direct validation

- The four changed Clausewitz sources have balanced block depth.
- Each new helper is defined once.
- The Event 15 event inventory remains 99 definitions, including 8 documented hidden definitions and zero `hide_window` uses.
- Event `.165` invokes both selected-case-state and association-charter-state reconciliation.
- The state, founder, and host arrays have explicit registration and exact cleanup consumers.
- No recurring global maintenance hook was introduced.

The optional Event Chain Viewer inspection was attempted, but the shared artifact store rejected retention with `ARTIFACT_STORAGE_LIMIT`. This does not replace or invalidate the direct source checks, but the optional graph artifact remains unavailable.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Recurring scan substitute: none.
- Remaining package gate: a fresh country-package and decision-and-mission specialist snapshot is still required because this correction postdates the earlier passing audit reports.
