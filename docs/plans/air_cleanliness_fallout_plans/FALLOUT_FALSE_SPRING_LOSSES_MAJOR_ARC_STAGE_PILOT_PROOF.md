# Fallout False Spring Losses major-arc stage pilot proof

Status: dormant, statically reconciled, not release-floor credit.

## Scope

The existing False Spring Losses chain is the fourth authored consumer for a reserved major-arc row. The shared reconciler selects its identity and calls `fallout_event_schedule_false_spring_losses_arc_opening_dispatch` only after the production gate and current candidate proof pass. It reuses event tokens `478` through `484`, transaction key `710042`, route `7142`, history `9147`, and the existing report asset. No event id, transaction key, route, history, asset, audio, sprite, or path is added.

## Authenticated opening

`fallout_event_dispatch_source.major_arc_stage` is a distinct dispatch source. The scheduler writes it only for the False Spring Losses identity after both activation flags, the generation-current registry, the current candidate state, and the existing production gate pass. Human mode maps to token `478`. Hidden AI mode maps to token `479`. The dispatch matcher requires the exact arc ticket, generation, opening stage, False Spring Losses identity, mode-specific token, state target, and current candidate state id.

The False Spring Losses opening triggers accept either the exact major-stage envelope or the pre-existing ordinary receipt envelope. The major-stage consumer clears only its envelope without creating an ordinary receipt. The ordinary receipt path remains available for legacy authored callers.

## Stage and cleanup contract

The consumer freezes the existing Food, Medicine, Cohesion, Recognition, Adaptation, Reclamation, frost-memory, and seed-reserve ledgers, links result and callback delayed rows to the major ticket, advances the major row through `conflict`, `choice`, `delayed_result`, `consequence`, `callback`, and `cleanup`, and releases the same arc identity after delayed cleanup. Failed delayed reservation, callback reservation, or stage proof cancels and releases the major row through the existing cancellation and release APIs.

## Engine-sensitive boundary

Static proof covers the separate dispatch source, dynamic event-token command, human and hidden-AI token mapping, exact ticket matching, current-state target gate, parent-arc linkage, stage transitions, and cleanup ownership. Runtime event delivery, save recovery, multiplayer host authority, scheduler activation, Event Log delivery, and live consumer presentation remain unobserved because the user instructed that HOI4 must not be run. The activation flags remain unset. The reviewed total remains 460 defined blocks and 0 of 660 countable blocks.
