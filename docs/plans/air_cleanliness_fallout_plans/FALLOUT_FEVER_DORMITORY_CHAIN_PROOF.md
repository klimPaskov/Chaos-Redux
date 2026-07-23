# Fallout Fever Dormitory chain proof

Status: implemented as a dormant reviewed pilot. It is not release-floor
credit because the Fallout scheduler has no activation setter or live caller.

## Contract identity

The chain is owned by the Fallout namespace `chaosx.fallout`. Its candidate is
`256`, transaction key `710012`, route `7112`, and Event Log history `9117`.
Event suffixes `256` through `268` are allocated as follows:

| Suffixes | Surface | Visibility |
| --- | --- | --- |
| `256` | human opening | visible |
| `257` | hidden AI opening | hidden |
| `258` through `261` | four delayed branch results | visible |
| `262` through `265` | four delayed branch results | hidden AI |
| `266` | callback | visible |
| `267` | callback | hidden AI |
| `268` | authenticated cleanup | hidden |

The four authored policies are quarantine the dormitory, disperse the bunks,
treat in public, and conceal the fever. Every policy has distinct costs,
thresholds, state deltas, resource deltas, memory, delayed results, callback
text, hidden-AI parity, and cleanup.

## Candidate and state proof

`fallout_event_pilot_fever_dormitory_state_is_current` requires the current
Fallout state identity row, durable state resource row, a current produced Air
Winter snapshot, shelter at or above the minimum, disease pressure at or above
the crisis threshold, population above the reviewed minimum, baseline Filters
and Food, low country Medicine, and one affordable branch. The producer chooses the lowest valid
owned state id. A committed state flag rejects a second reservation until
cleanup releases it.

The opening freezes shelter, exposure, adaptation, reclamation, and disease
from the produced Air Winter state receipt. It also freezes food, Medicine,
Filters, and Recognition from the country survival ledger. Viability is a
weighted deterministic score using shelter, adaptation, Filters, Medicine, and
disease relief. Each branch converts that score and its policy resource into
success, partial success, or failure. No random effect or variable-only
fallback is used.

## Consequence and receipt proof

Human and hidden-AI openings use the same delayed-result scheduler receipt.
Costs are paid only after the delayed result and ordinary receipt both commit.
Results update the Air Winter disease, shelter, exposure, adaptation, and
reclamation values through the live disease modifier path. They also update
food, Medicine, Filters, Recognition, Cohesion, Stability, and typed memory.
Failure requests population loss through `apply_exact_state_civilian_population_loss`
with the shared Fallout aftermath reason and a bounded minimum remainder.

The result is scheduled at exactly 14 days. Its callback is scheduled at
exactly 120 days after result resolution. The cleanup event releases the
callback receipt, then the result receipt, and clears the state flag, country
variables, history guards, and payment flag. A failed receipt path records an
owned schedule error and does not charge a branch twice.

## Event Log and asset proof

History `9117` has fifteen explicit payloads. The shared Event Log routes map
that history to `fallout.event_log.fever_dormitory.name` and
`fallout.event_log.fever_dormitory.detail`, while
`GetFalloutEvent256EventLogDetail` maps every branch and outcome payload to
concrete localisation. The dedicated report sprite is
`GFX_report_event_fallout_fever_dormitory`, backed by
`gfx/event_pictures/fallout_world_end/report_event_fallout_fever_dormitory.dds`.
Source, processed, contact-sheet, prompt, manifest, and GFX handoff evidence
are under `docs/assets/air_cleanliness_fallout/fallout_fever_dormitory/`.
No Zombie id, file, asset, audio, sprite, or path is reused.

## Engine-sensitive proof boundary

The following surfaces are statically reconciled against the existing Fallout
receipt and dormant-chain precedents:

- namespace, event ids, candidate id, transaction key, route, and history id
- balanced Clausewitz blocks and unique event-definition ids
- delayed-result scheduling, ordinary receipt consumption, callback receipt,
  and cleanup effect names
- Deaths-backed failure request shape
- Air Winter state variables and disease-modifier call
- shared Event Log name and detail selectors
- dedicated sprite registration and runtime DDS path

The following engine surfaces remain unobserved because the user directed that
HOI4 need not be launched:

- scheduler activation and the live ordinary candidate caller
- host-authoritative request handling and multiplayer ownership
- save recovery after an interrupted result or callback
- `var:` state-target scope across delayed event delivery
- popup blocking, hidden-AI issue timing, and Event Log rendering in a live save

These are proof boundaries, not claims that the unobserved engine behavior is
passing. Both scheduler activation flags remain unset, the chain is dormant,
and the Fallout living-world release-floor count remains `0 of 660`.
