# Fallout Well Queue Tuning and Registry

## Status

The Well Queue is a dormant global-survival pilot. Its candidate row is owned by the Fallout scheduler, but no activation flag or gameplay caller is present. The chain contributes zero blocks to the 660-block release floor until the scheduler activation, event-log review, manual content review, and audit gates are complete.

## Candidate identity

The generation-bound candidate row uses candidate id `153`, transaction key `710004`, route `7104`, and the existing water-security cooldown family. The row is created only for the lowest valid owned state that has a current Fallout identity row, durable state resource row, produced Air Winter water-source receipt, and water security below the success band. The state must remain owned by the same country and cannot already carry the Well Queue registry flag. The country must have at least one of the three authored branch costs available.

The candidate stores a state subject, first-season phase, public-queue opening branch, and the state id as its state-value source. The country and state registry rows carry the current transition generation. The row is rejected if any identity, source, ownership, generation, or state registry proof is absent.

## Human and hidden-AI chain

The human opening is event `chaosx.fallout.153`. It offers three concrete responses:

| Branch | Cost | Main condition | Resolution | Follow-up memory |
| --- | ---: | --- | --- | --- |
| Publish one water queue | 3 Clean Water Security | country water resource | four-day result and five-day callback | shared cistern or water exclusion |
| Issue ration cards for filtered water | 5 Filter Stock | filter resource | four-day result and five-day callback | shared cistern or water exclusion |
| Put the well under guard | 10 Command Power | command power | four-day result and five-day callback | shared cistern or water exclusion |

Event `154` is the hidden-AI opening. Its branch choice follows the same costs and result reservation as human play. It favors filtered water when filters are strained, chooses guarded intake only when the country has the required Command Power and a forceful government or active war, and otherwise uses the public queue. The candidate gate guarantees at least one affordable branch before either lane can enter.

Events `155` through `157` are the human branch results. Events `158` through `160` are their hidden-AI companions. All six use the same deterministic outcome calculation and effect path. Result terminalization authenticates the issued delayed receipt before any branch effect runs. A stale, foreign, or malformed receipt mutates nothing. The selected branch cost is paid only after the delayed reservation and ordinary-receipt consumption both succeed, then an idempotent country flag prevents a second payment until cleanup.

Event `161` is the visible callback and event `162` is its hidden-AI companion. Both resolve the issued callback before applying follow-up effects. Event `163` is the only cleanup event. It authenticates each cleanup token, releases the callback row before releasing the result row, clears the state registry flag and registry owner values, and then clears the country chain receipts. The shared delayed reconciler defers the resolved result row while the Well Queue callback flag and cleanup token are present, so generic cleanup cannot erase the state proof before the five-day callback.

## Deterministic outcomes and effects

The outcome bands are authored from the country resource or state water security values at result delivery. A success requires the branch resource and state water threshold of 45. A partial result uses the authored intermediate thresholds. The guarded branch also recognizes a fascist or non-aligned government or a country at war. Failure applies 0.8 percent of the state population through the exact Deaths-backed civilian loss effect, with at least 100 people remaining when the state is nonempty.

Success and partial results alter country water security, recognition, cohesion, stability, and the exact state water-security variable. Guarded outcomes also alter War Support. The branch applies one Fallout-owned dynamic modifier for public flow, ration tokens, guard watch, or grievance. The callback changes the same ledgers again and records either a shared-cistern memory flag or a water-exclusion memory flag on the state. Every result clamps the state water ledger and refreshes the Air Winter state view.

## Event-log and asset wiring

History id `9108` has branch-specific success, partial, and failure payloads for the three opening branches plus callback outcomes. `GetFalloutEvent153EventLogDetail` routes those payloads to the dedicated Well Queue detail strings, and the history-name router exposes `fallout.event_log.well_queue.name`. The report art is `GFX_report_event_fallout_well_queue`, registered in `interface/fallout_consolidated.gfx` and backed by the dedicated DDS and provenance manifest at `docs/assets/fallout_well_queue/`.

## Engine-sensitive boundary

The chain uses the existing Fallout delayed-result scheduler, state variables, state flags, exact Deaths effect, and `meta_effect` dispatch path. Static inspection proves event id uniqueness, typed constants, aligned candidate-row writes, no duplicate branch token, no stale zombie asset path, and shared callback deferral. The read-only event inspector was attempted for event `153`, but its fixed projection ceiling returned `EVENT_NODE_LIMIT` before producing an artifact. Runtime popup timing, save recovery, state-scope variable resolution, dynamic-modifier display, and multiplayer ordering remain unobserved because HOI4 was not launched. The chain stays dormant until those surfaces receive an authorized runtime pass.

## Deferred expansion

The pilot deliberately does not add a bilateral water partner, successor-specific content, focus integration, or a scheduler caller. Those are separate source-spec work items and cannot be represented by this one state chain. No generic fallback is used.
