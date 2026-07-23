# Fallout Reviewed Candidate Pilot Proof

Status: dormant, statically reconciled, not release-floor credit.

The Fallout scheduler now owns a reviewed ordinary-candidate producer for seventeen
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
- The candidate effect file balances at 508 braces. The edited constants,
  triggers, and scheduler effect files remain balanced.
- The Animal Feed effect file balances at 420 braces, its trigger file at 39,
  and its four dynamic-modifier blocks at 8 braces.
- The candidate pilot constants define seventeen candidate ids, seventeen transaction
  keys, and seventeen route ids in a dedicated Fallout namespace.
- The event tokens resolve to existing dormant Fallout event blocks 100 through
  126, 153 through 200, 204 through 309, and the hidden companion ranges
  `1009` through `1018`. No zombie event id, file, asset, audio, sprite, or
  path is reused.
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

## Bad Batch correction

The producer now carries eight reviewed ordinary rows. Bad Batch adds state
candidate id `204`, transaction key `710008`, route `7108`, and event tokens
`204` through `216`. Its target is the lowest valid owned state with a
generation-bound seed or greenhouse provenance receipt, produced Air Winter
snapshot, reclamation and adaptation thresholds, and an affordable branch.
The row is tagged to `first_winter_year`, remains dormant, and contributes no
release-floor credit. The greenhouse receipt is copied during pretransition
capture so the candidate does not depend on the Air Winter teardown flag.

## Filters Fail correction

The producer now carries nine reviewed ordinary rows. Filters Fail adds state
candidate id `217`, transaction key `710009`, route `7109`, and event tokens
`217` through `229`. Its state gate requires shelter capacity, current Filters
pressure, a produced Air Winter snapshot, and an affordable branch. The chain
remains dormant and contributes no release-floor credit.

## Door List correction

The producer now carries ten reviewed ordinary rows. Door List adds state
candidate id `230`, transaction key `710010`, route `7110`, and event tokens
`230` through `242`. It selects a deterministic source and shelter-qualified
destination state, then remains dormant behind scheduler activation.

## Last Transformer correction

The producer now carries eleven reviewed ordinary rows. Last Transformer adds
state candidate id `243`, transaction key `710011`, route `7111`, and event
tokens `243` through `255`. It requires a produced Air Winter state snapshot,
durable Supply Access, repairable infrastructure, and a live factory. Its
state and partner selections use stable id tie breaks.

## Fever Dormitory correction

The producer now carries twelve reviewed ordinary rows. Fever Dormitory adds
state candidate id `256`, transaction key `710012`, route `7112`, and event
tokens `256` through `268`. The state gate binds disease and shelter to the
current Air Winter receipt and requires low Medicine with an affordable policy.
The chain has four human and hidden-AI policy lanes, delayed results, callback,
Deaths-backed failure, fifteen Event Log payloads, dedicated art, and cleanup.
It remains dormant and uncounted. No HOI4 runtime was launched.

## First Safe Birth correction

The producer now carries the fourteenth reviewed ordinary row. First Safe Birth
uses country candidate id `282`, transaction key `710014`, route `7114`, and
event tokens `282` through `288`. Its gate requires the current country row,
campaign day `120` through `420`, Cohesion at least `45`, Medicine at least
`35`, Shelter at least `50`, and one affordable generation-change branch. Its
severity is the clamped Deaths score and its mechanic-pressure field is zero.
The country Cohesion ledger supplies the state value. The chain freezes Deaths,
Cohesion, Medicine, Shelter, Recognition, and exposure, then schedules a
21-day result and 180-day callback with hidden-AI parity. History `9119`, six
dedicated modifiers, fifteen payloads, cleanup, and dedicated report art are
statically wired. It remains dormant and uncounted.

## School in the Vent Room correction

The producer now carries the fifteenth reviewed ordinary row. School in the
Vent Room uses country candidate id `289`, transaction key `710015`, route
`7115`, and event tokens `289` through `295`. Its gate requires the durable
First Safe Birth memory, one generation change, campaign day `360` through
`899`, Cohesion at least `35`, Food at least `25`, Shelter at least `35`, and
one affordable curriculum. Its severity is the clamped generation-count score
and its mechanic-pressure field is zero. Food supplies the state value. The
chain freezes Cohesion, Food, Shelter, Recognition, generation count,
education, and exposure, then schedules a 28-day result and a 210-day cohort
callback with hidden-AI parity. History `9120`, six dedicated modifiers,
fifteen payloads, cleanup, and dedicated report art are statically wired. It
remains dormant and uncounted.

## Empty Ward correction

The producer now carries the sixteenth reviewed ordinary row. The Empty Ward
uses country candidate id `296`, transaction key `710016`, route `7116`, and
event tokens `296` through `302`. Its gate requires the closed School memory,
one Fever Dormitory outcome memory, campaign day `500` through `1199`, Cohesion
at least `30`, Medicine at least `15`, Shelter at least `30`, and one affordable
policy. Its severity is the clamped recorded-Deaths score and its
mechanic-pressure field is zero. Medicine supplies the state value. The chain
freezes Medicine, Shelter, Cohesion, Recognition, generation count, ward
capacity, research, and trust, then schedules a 35-day result and a 240-day
institution callback with hidden-AI parity. History `9121`, six dedicated
modifiers, fifteen payloads, cleanup, and dedicated report art are statically
wired. It remains dormant and uncounted.

## Names for the Missing correction

The producer now carries thirteen reviewed ordinary rows. Names for the
Missing adds country candidate id `269`, transaction key `710013`, route
`7113`, and event tokens `269` through `281`. Its gate requires a current
country row, high recorded civilian deaths, incomplete Recognition, and an
affordable census branch. The chain freezes country ledgers, uses the bounded
severity formula `clamp(Deaths * 0.001, 0, 100)` with zero survival-resource
mechanic pressure, reserves a three-unit human opening envelope, and uses zero
visible budget for hidden-AI delayed rows. It writes history `9118`, routes
result failure at 0.4 percent and callback failure at 0.2 percent through
Deaths, and remains dormant behind scheduler activation.

## Shelter Marriage Law correction

The producer now carries the seventeenth reviewed ordinary row. Shelter
Marriage Law uses country candidate id `303`, transaction key `710017`, route
`7117`, and event tokens `303` through `309`. Its gate requires the closed Empty
Ward memory, generation count at least two, campaign day `720` through `1500`,
Cohesion at least `35`, Food at least `20`, Shelter at least `35`, Recognition
at least `20`, and one affordable family-law policy. Its severity is the
clamped recorded-Deaths score and its mechanic-pressure field is zero. Cohesion
supplies the state value and Food supplies the required resource. The chain
freezes family ledgers, schedules a 42-day result and a 300-day household
callback with hidden-AI parity, records history `9122`, and remains dormant and
uncounted.

## Black Start correction

Black Start is the eighteenth reviewed ordinary candidate row. Candidate `310`
uses transaction key `710018`, route `7118`, and history `9123`. It requires
the closed Shelter Marriage Law memory, a second-generation country with
Power, Scrap, Cohesion, Recognition, Reclamation, and an affordable grid policy.
Events `310` through `316` provide four authored policies, deterministic result
grading, a 270-day maintenance callback, hidden-AI parity, Deaths-backed
failure, durable grid ledgers, fifteen Event Log payloads, dedicated report art,
and authenticated cleanup. It remains dormant and contributes zero blocks to
the `0 of 660` release-floor total. The event inspector request returned
`Transport closed`, so engine-sensitive reachability and host or save behavior
remain unproven.

## First Streetlight correction

The producer now carries the nineteenth reviewed ordinary row. First
Streetlight uses country candidate id `317`, transaction key `710019`, route
`7119`, and event tokens `317` through `323`. Its gate requires the closed
Black Start memory, second-generation timing, Power, grid capacity,
governance, Cohesion, Reclamation, and one affordable urban policy. Its
severity is the clamped recorded-Deaths score and its mechanic-pressure field
is the Black Start capacity ledger. The chain freezes urban and grid ledgers,
uses a 35-day first-light result and a 240-day public maintenance callback
with hidden-AI parity, records history `9124`, and remains dormant and
uncounted. The dedicated report art and the event-inspector `Transport closed`
proof are recorded in `FALLOUT_FIRST_STREETLIGHT_CHAIN_PROOF.md`.
