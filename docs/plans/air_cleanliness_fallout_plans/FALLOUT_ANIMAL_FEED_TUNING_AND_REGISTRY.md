# Fallout Animal Feed Tuning and Registry

## Status

Animal Feed Debate is a dormant global-survival pilot. Its candidate row is
owned by the Fallout scheduler, but no activation flag or gameplay caller is
present. It contributes zero blocks to the 660-block release floor until
activation, event-log review, manual content review, and audit gates pass.

## Candidate identity and native source

The generation-bound candidate uses id `164`, transaction key `710005`, route
`7105`, and the food-security cooldown family. It selects the lowest valid
owned state that has a current Fallout identity row, a durable survival
resource row, and a produced Air Winter pre-transition food reserve between
the authored feed minimum and pressure bands. The snapshot generation, source
kind, owner country, and absence of the state registry flag are all required.
The country must also be able to pay at least one authored branch cost. A
missing state, stale generation, unproved source, or ownership mismatch omits
the row rather than inventing a target.

## Human and hidden-AI chain

Event `chaosx.fallout.164` offers three manually authored policies. Event `165`
is the hidden-AI opening and uses the same eligibility and reservation path.

| Branch | Cost | Deterministic condition | Main effect |
| --- | ---: | --- | --- |
| Feed the kitchens first | 4 Food Security | food ledger and feed reserve | conversion memory and kitchen supply |
| Protect breeding stock | 6 Food Security | feed reserve and adaptation | breeding reserve and second-season capacity |
| Divide the reserve by region | 5 Food Security | food ledger and reclamation | regional depot memory and reclamation capacity |

Events `166` through `168` are human delayed result popups. Events `169` through
`171` are their hidden-AI counterparts. They use one outcome calculator, three
outcome bands, one exact Deaths-backed failure path, and one state-owned feed
ledger. The selected branch cost is paid only after the delayed result row and
ordinary receipt both commit. A persistent payment flag prevents a second
charge until cleanup.

Events `172` and `173` are the human and hidden-AI first-harvest callbacks.
They arrive thirty days after the result and apply branch-neutral success,
partial, or failure changes to food, recognition, cohesion, stability, state
memory, and grievance. Event `174` is the only cleanup event. It releases the
callback row before the result row, clears the state registry flag and feed
reserve, and then clears the country receipts. The shared delayed reconciler
defers this cleanup while the callback flag and cleanup token are present.

## Event-log and asset reuse

History id `9109` has branch-specific opening and first-harvest payloads. The
event-log detail router is `GetFalloutEvent164EventLogDetail`, and the history
name is `fallout.event_log.animal_feed.name`. The chain reuses the dedicated
Fallout food report art `GFX_report_event_fallout_last_inventory`, so no zombie
asset, audio, sprite, or path is introduced.

## Engine-sensitive boundary

Static inspection covers typed constants, aligned candidate arrays, exact
ordinary and delayed receipts, branch cost ordering, Deaths effect inputs,
state-scope registry checks, callback deferral, event ids, localisation, and
dedicated Fallout asset reuse. The chain remains dormant because HOI4 was not
launched. The read-only event inspector was attempted for event `164`, but its
fixed projection ceiling returned `EVENT_NODE_LIMIT` before producing an
artifact. Popup timing, hidden-AI command issuance, save recovery, state
variable scope at runtime, multiplayer ordering, and dynamic-modifier display
remain unobserved engine surfaces.

## Deferred expansion

This pilot does not add a bilateral partner, successor-specific branch, focus
integration, or a scheduler activation caller. Those surfaces require separate
source-spec work and manual review. No generic fallback is used.
