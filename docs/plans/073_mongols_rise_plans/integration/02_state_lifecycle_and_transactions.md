# Lifecycle and transaction contracts

## State ownership

The accepted restoration owns one central actor record, one opening entitlement, the current Evolution entitlement record, a bounded campaign collection, and active imperial relationships. Each khanate owns its own country, armies, economy, and regional state. Each agreement owns its payer, recipient, terms, delivery record, and status.

Public values are Momentum and Authority. Internal records for dates, entitlement, relationships, and held objectives are necessary state, not additional public mechanics.

## Lifecycle

| Phase | Entry | Required behavior | Exit |
|---|---|---|---|
| Eligible | Valid Mongolia and no equivalent empire | No private ticking grant | Selected by existing engine |
| Offered | Root routes to the actor | Human acceptance or refusal | Refused or accepted |
| Muster | Acceptance committed | One tier grant and safe reception | Active restoration |
| Active | Army and country valid | Campaigns, institutions, obligations | Succession or strain can interrupt |
| Succession | Valid office vacancy | Caretaker and kurultai | Accepted successor or contested order |
| Strained | Concrete severe unresolved condition | Warning and targeted response | Recovery, defiance, or fragmentation |
| Fragmented | Actual political separation | Viable successors and obligation cleanup | Regional survival or reunification |
| Recovered | New viable settlement | Continuing campaign without entry grant | Normal active or successor play |
| Ended | Center no longer valid and no central continuation | Stop center-owned callbacks | Successor systems continue where valid |

The active phase can contain a succession without recreating the entire country. Terminal cleanup must distinguish ending the central actor from ending every successor country.

## Muster accounting

For each cumulative tier, store entitlement received and entitlement consumed for deployment. The deployed army's present strength is not the entitlement counter. An upgrade compares the new total with the total already awarded. Casualties do not increase the difference.

An arrival has a valid owner, capital arrangement, controlled reception state, technology, template, equipment, and manpower source before deployment. Waiting entitlement remains visible. A destroyed unit never returns its initial grant entitlement.

## Transfers

A transfer resolves and rechecks payer and receiver, calculates a feasible amount, debits the payer, credits the receiver by the same amount, and records completion once. A retry sees the completion record. An invalid recipient or insufficient donor amount produces no partial duplicate credit.

Use existing stockpile helpers only after inspecting their sign contract. The provided dynamic-effects reference describes helpers whose positive input is converted into a negative debit. Reinitialize each call's input. Never pass a previously negated value back as a new debit.

A manpower transfer, troop contingent, or resource arrangement must use a verified supported mechanism. Unsupported transfer types remain blocked. Do not manufacture a parallel resource stockpile solely to make the design appear implemented.

## Settlement

Recheck the chosen required-state manifest, owner, controller, peace rights, target identity, capital, and relationship immediately before a release or transfer. Occupation alone may support a temporary military milestone but not an unauthorized permanent country release.

The settlement record owns its one-time reward allocation. A later change from direct rule to autonomy cannot pay conquest rewards again. A renamed existing country is not a newly created country eligible for another opening grant.

## Bounded updates

Recurring work uses the existing scheduler and the finite set of active actors, agreements, and campaigns. No new daily scan of every state, every division, or every country is authorized by this plan. Recheck only the state needed for a current commitment at the appropriate existing cadence or event boundary.

Use dirty or event-driven refresh where the project supports it. Exact hooks and costs require local profiling and source inspection.

## Save and cleanup

Persist one-time claims, outstanding entitlement, current agreements, active objectives, and phase. Reconstruct presentation from that state after reload. Do not infer a fresh opening from a missing cosmetic flag.

When a relationship ends, clear its future payment, access, subject effects, and invalid AI assumptions together. When the center disappears, stop center-owned processing while leaving valid successor content alive. Expired campaign records can be archived or reduced through the established project pattern without removing anti-farming history.
