# Fallout Event Release Audit Contract

## Purpose

The Fallout living-world scheduler remains dormant until a reviewed release receipt proves the content floor and the engine-sensitive presentation surfaces.

This contract keeps the activation flags fail-closed without inventing a runtime result that has not been observed.

The current reviewed pilot contains 558 defined Fallout blocks through Battalion's List. Historical receipts may retain lower counts from earlier tranches, but they do not authorize activation.

The countable release floor is 660 manually reviewed blocks, so the current count is 0 of 660 for release purposes.

## Receipt layers

The release floor receipt stores a reviewed block count, transition generation, review date, and review day.

The count must be at least 660.

The receipt is generation-bound and cannot be carried into a later Fallout transition.

Five separate engine-sensitive flags cover the exact all-valid-province thermonuclear sweep, the full-screen blackout, host authority, save recovery, and multiplayer input delivery.

The exact engine-native sweep is not proven in the current handoff, so the manual-sweep flag remains unset.

The world barrier also requires current map return postconditions, the current timeline receipt, successor allocation, the survival transition barrier, player continuation commit, assignment uniqueness, the scheduler registry, every current orientation row, and every current reviewed candidate registry.

## Authoring contract

`fallout_event_record_release_floor_review` is an audit-only effect.

Its caller supplies temporary values for the reviewed block count and the five engine-sensitive review receipts.

It accepts only the Fallout transition coordinator after map return and before scheduler activation.

It records evidence and never sets either scheduler activation flag.

The audit effect never sets `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

When the receipt is valid it records an accepted audit status and leaves the activation decision to a separate final review.

When any gate is missing it records a rejection reason and leaves event production dormant.

No periodic on_action invokes either effect.

## Rejection reasons

The rejection ledger distinguishes the reviewed floor, manual sweep, blackout, host authority, save recovery, multiplayer, transition, scheduler error, and world barrier failures.

This makes an unproven engine surface visible in the handoff instead of allowing a silent activation shortcut.

## Review handoff

The release audit effect may record the five engine-sensitive inputs only after the corresponding static and runtime evidence is attached to the release report.

The current no-launch constraint means runtime delivery, save recovery, host authority, multiplayer input blocking, and the exact native sweep remain unobserved unless separate evidence is supplied.

The audit receipt therefore remains an implementation surface rather than a claim that Fallout is ready for a human campaign.

The accepted scheduler numerical contract does not authorize an activation setter.

The two scheduler activation flags remain unset until a separate final review authorizes an activation surface.
