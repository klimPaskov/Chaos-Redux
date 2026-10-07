# State ownership and dispatch contract

This document is a proposed architecture contract. State labels and record fields below are conceptual names, not asserted HOI4 variables or supported syntax. The implementation must bind them to verified repository conventions.

## Minimal event-owned state

| Concept | Lifetime | Owner and meaning |
| --- | --- | --- |
| Global lifecycle status | Campaign | Unfired, preparing, applying, committed, legacy-consumed, or incomplete. It prevents another worldwide deposition |
| Material manifestation awarded | Campaign | A once-only guard for the authored +20 award after a complete pass with a real increase |
| Firing identity and date | Campaign history | One stable historical incident, shared across human viewers and independent timer initiators |
| Region coverage receipt | Firing and durable evidence | Effective-map identity, unique valid region count, and proof of complete coverage |
| Recipient coverage receipt | Firing and durable evidence | Existing legal owners, excluded identities with verified reasons, and pair count |
| Preparation workspace | One invocation | Snapshot C, snapshot R, native capability checks, and temporary effect inputs |
| Achievement provenance | Campaign, bounded participants | Only the owner/region facts required for material-increase and qualifying clearance evidence |
| Report-delivery state | Presentation | Prevent redundant personal display where required. Never controls whether mines are applied |

Avoid storing a permanent C × R matrix merely to mirror engine state. Retain what the actual verification and achievements need. The persistent event record is historical, not a second live mine simulation.

## Transaction boundary

1. An ordinary picker, cluster member call, or authorized direct test call requests Event 088.
2. Check the global consumed, applying, and incomplete state before any mine write or successful history entry.
3. Verify eligibility, map completeness, native capability and configuration support. C and R must be nonempty. Build unique, deterministic snapshots.
4. Reserve the single global application before entering the write loop, using the established synchronous dispatcher model. No report option controls this reservation.
5. Apply the requested addition once to every snapshot pair with the correct owner scope. Do not advance game time between batches to make the task easier.
6. Verify the completion condition supported by the actual engine and retain an honest coverage receipt. Only a complete pass can become committed.
7. Record the event's consumed state, one successful history identity, and the +20 manifestation award only if at least one field materially increased. A no-change but complete pass consumes the event and records the no-change result with zero Chaos.
8. Deliver the report through the established presentation route. Acknowledgment is mechanically inert.
9. Release temporary selection data without removing native fields or persistent consumed/provenance records.

When the incident is a cluster member outcome, use the existing cluster history record and its member data rather than adding a second top-level ordinary-event entry. The actual shared dispatcher must be inspected before implementing this order. Some generic paths can log a fired event before the event body runs. Adding an early return inside the event after that log is not sufficient. Eligibility and capability preflight must be integrated before the irreversible shared firing path. If success logging must be deferred until commit, make the narrow explicit shared-contract change and audit other callers. Do not add a second Event 088 history entry to compensate for the first.

## Failure handling

Preflight failure is not a successful fire. It must not clear mines, consume the once-only incident, award Chaos, or create an ordinary success record. The existing unavailable-event presentation should communicate ineligibility rather than representing it as a zero-probability event where the framework distinguishes those states.

There is no claimed engine transaction rollback. If an unexpected partial application occurs, preserve existing mines and retain an explicit incomplete state and pair-level evidence where available. Block automatic reentry. A blind retry can add another 1,000 under a raised cap and destroy the once-only semantics. Never attempt rollback by deleting all affected fields, because they include preexisting mines.

A repair procedure needs actual exact progress and a verified remaining-pair resume route. If the engine cannot support that evidence, the partial result is a release failure, not a recoverable success by assertion. The implementation's normal supported path must be validated so that an ordinary campaign does not encounter this state.

## Timers, cluster accounting and multiplayer

Event 088 is one global incident in both shared and independent timer modes. The initiating picker consumes its normal logical outcome. Do not reset every recipient's timer or increment major weights once per mine-owning country. Propagate fire-once availability so a later country's independent picker cannot deposit again.

For Sudden Abundance, inspect all parallel member arrays together. Event ID, required/optional participation role, optional chance, minimum tier and severity are separate entries. Preserve the cluster's other members and shared cooldown. Repeated cluster selection must omit consumed Event 088 while allowing other valid members under the actual cluster rules.

The player's client, report recipient, and mine owner are separate roles. Every client's notification must observe the same committed world state. Country switching and report acknowledgment do not authorize new mutation. Do not introduce client-dependent random choices or game-time delays inside the pass.

## Save and legacy migration

Fresh unfired saves may use the reworked event once after all supported configuration checks pass. Saves with proven legacy consumption preserve that consumption and their existing minefields. They do not receive an automatic new global incident.

Do not fabricate new coverage receipts or achievement provenance for the old one-region firing. The historical detail can distinguish legacy behavior where the framework supports it. A save with ambiguous partial or debug history needs an explicit migration classification, not an assumption that absence of the new flag means the old event never fired.

Mid-application save semantics must be verified rather than assumed. If normal effect execution does not permit such a save, test the available reentry paths. If saves can preserve incomplete state, the guard must survive loading. Clearing transient data on load must not clear the consumed guard.

## Complexity and performance

The intended placement count is |C| × |R|. Deduplicate both sets before application. Coverage tests must include large supported mod maps and many current dynamic countries. Check engine loop limits, meta-effect expansion size, temporary-variable handling and worst-case synchronous execution cost.

Do not reduce the number of owners or regions to meet a performance target. Do not spread the placement over days, because that changes the simultaneous global incident and exposes ordering advantages. A capacity failure belongs in the supported-configuration gate until an equivalent implementation is demonstrated.

The event adds no recurring global placement hook. Achievement observation, if supported, uses bounded active participants through an existing framework or native event observations. An event-only setup pass must not become an accidental whole-world daily scan.
