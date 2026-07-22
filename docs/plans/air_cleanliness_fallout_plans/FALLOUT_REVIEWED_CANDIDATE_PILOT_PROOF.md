# Fallout Reviewed Candidate Pilot Proof

Status: dormant, statically reconciled, not release-floor credit.

The Fallout scheduler now owns a reviewed ordinary-candidate producer for five
global-survival pilot chains. The producer is deliberately narrower than the
future 660-block release surface. It exists to prove the candidate-array
contract, target-shape contract, and deterministic state selection without
opening either scheduler activation flag.

## Candidate rows

Every current Fallout registry country receives a generation-bound row set when
its candidate registry has not already been built for that transition. The
country row is rebuilt only when the stored candidate generation is absent or
stale. Completion history is preserved while the parallel reviewed-row arrays
are replaced.

The food row is always present and carries no state target. The water row is
added only when the lowest valid owned state has a current Fallout state ledger,
a produced Air Winter water source, and no committed intake registry. The rail
row is added only when the lowest valid owned state also has a native railway,
an Air Winter phase at or above the rail pilot threshold, and no committed rail
registry. The Well Queue row is added only when the lowest valid owned state has
a current Fallout state ledger, a produced Air Winter water source below the
security threshold, an available branch cost, and no committed Well Queue
registry. No infrastructure, supply-node, or invented state substitutes these
native surfaces. The Animal Feed row is added only when the lowest valid owned
state has a produced Air Winter food reserve in the authored feed band and no
committed feed registry. It stores that state as the native feed target and
uses the same generation and ownership proof as the other state rows.

Each row stores both human and hidden-AI event tokens, a unique local
transaction key, a typed branch, phase and cooldown family, visible budget
cost, pressure resource, target shape, route identity, repeatability, actor and
partner absence, and the full required-match provenance fields. Human rows use
the exact 100 relevance control. AI rows use the exact zero relevance control.
The helper appends all 53 reviewed-row arrays together, so a partial row cannot
pass the alignment proof.

## Coordinator route

The existing at-most-once Fallout coordinator calls
`fallout_event_build_pilot_candidate_registries` after the numerical registry
header is current. The producer never sets
`fallout_event_scheduler_activation_approved` or
`fallout_event_scheduler_active`. Human and AI review effects remain behind
those flags, so no popup or hidden result can be issued by this tranche.

After writing the generation and build day, the producer sets
`fallout_event_candidate_registry_reviewed` and immediately re-authenticates
the complete reviewed-row trigger. A malformed row clears the reviewed receipt
and generation markers instead of selecting a fallback.

## Static evidence

- `fallout_event_candidate_registry_arrays_are_aligned` lists 55 arrays. The
  producer appends all 53 mutable row arrays and leaves the two completion
  history arrays intentionally durable.
- The new candidate effect file balances at 229 braces. The edited constants,
  triggers, and scheduler effect files remain balanced.
- The Animal Feed effect file balances at 420 braces, its trigger file at 39,
  and its four dynamic-modifier blocks at 8 braces.
- The candidate pilot constants define five candidate ids, five transaction
  keys, and five route ids in a dedicated Fallout namespace.
- The event tokens resolve to existing dormant Fallout event blocks 100, 101,
  107, 108, 114, 115, and 153 through 174. No zombie event id, file, asset,
  audio, sprite, or path is reused.
- The ordinary candidate eligibility trigger still rejects major-arc and
  relationship rows until their complete atomic reservations are reviewed.
- The Well Queue cost is paid only after its delayed row and ordinary receipt
  both commit, with a cleanup-owned payment flag preventing a second charge.
- The Animal Feed cost is paid only after its delayed row and ordinary receipt
  both commit, with a cleanup-owned payment flag preventing a second charge.
- No HOI4 runtime was launched. Event command issuance, popup display, hidden
  AI resolution, save recovery, multiplayer behavior, and performance remain
  unobserved engine surfaces.

## Remaining blockers

The pilot producer is not a release-floor claim. The activation flags remain
unset because the living-world content caller, full candidate matrix, complete
human and AI result coverage, event log and detail depth, focus integration,
and runtime proof are still incomplete. The exact engine-native all-valid-land-
province sweep blocker for the manual scenario is unchanged.

## Candidate count correction

The producer now carries seven reviewed ordinary rows, adding Triage Wall id
`175` and Seed Vault Custody id `188` after the original food, water, rail, Well
Queue, and Animal Feed rows. The candidate effect appends all 53 mutable row
arrays for the new rows as well. Triage Wall and Seed Vault remain dormant and
uncounted, with the living-world release-floor total at `0 of 660`.
