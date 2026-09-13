# Event 065 Design Resolution Ledger

## Purpose

This ledger separates user-provided rules from planning decisions and implementation questions.

It should be reviewed before source work begins.

## User-provided rules

| Topic | Accepted rule |
| --- | --- |
| Event identity | Event `65`, `Random Trait` |
| Type | Minor Repeatable |
| Initial status | To Be Reworked |
| Chaos level | `1` |
| Cluster | Randomizations |
| Member severity | Medium |
| Baseline | Every existing country leader gains one completely random trait |
| Pool | Every applicable Hearts of Iron IV and Chaos Redux trait |
| Filtering | No thematic, ideological, country, personality, or situation filter |
| Result range | Useful, useless, harmful, contradictory, strange, and inappropriate traits are valid |
| Existing traits | Kept |
| Repeat behavior | Later firings stack more traits |
| Evolution I | At raw Chaos `200+`, two random traits |
| Evolution II | At raw Chaos `400+`, three traits and modest bias toward powerful, unusual, rare, and Chaos Redux traits |
| Evolution III | At raw Chaos `600+`, five traits and a further modest bias toward powerful, bizarre, extreme, and rare traits |
| New leaders | Unaffected until a future firing |

## Planning resolutions

### Trait universe

**Resolution**

Use every final loaded trait accepted by the country-leader trait database and `add_country_leader_trait`.

**Reason**

The receiving object is a country leader.

This matches the current implementation's source family and preserves the user's complete-pool intent without importing unrelated engine databases.

### Duplicate proposals

**Resolution**

Reject a source ID already owned, previously granted by Event 65, or selected earlier in the same firing.

**Reason**

A duplicate effect usually cannot add a second visible copy.

Counting it would break the promise of two, three, or five added traits.

### Sampling model

**Resolution**

Use weighted sampling without replacement from the recipient's remaining eligible source IDs.

**Reason**

Every slot begins from the same stage distribution, while accepted earlier results leave the remaining pool.

This preserves randomness and exact additions.

### Event 65 ledger

**Resolution**

Track source IDs previously granted to each recipient.

**Reason**

Another system can later remove a visible trait.

Without a ledger, Event 65 could grant the same source again and fail to expand the recipient's cumulative random history.

### Trait side effects

**Resolution**

Use the real source trait and accept normal downstream checks.

**Reason**

The user explicitly allows inappropriate and contradictory results.

Route-specific or country-specific side effects are part of the event unless they create a hard technical failure.

### Evolution persistence

**Resolution**

The highest manifested enabled Evolution persists.

A raw Chaos decline does not de-evolve the event.

**Reason**

Chaos Redux Evolutions are lasting event-state changes.

Event 65 has no active phase, so each new form manifests on a firing.

### Direct Chaos

**Resolution**

Grant one-time successful manifestation gains of `+2`, `+3`, `+5`, and `+8`.

**Reason**

The event creates an abnormal global mutation.

Per-country or per-trait scaling would be too large and farmable.

### Higher-form jump

**Resolution**

A first firing at Evolution III grants only the Evolution III manifestation Chaos and marks lower missed milestones bypassed.

**Reason**

The campaign did not experience the lower manifestations.

Awarding all four amounts at once would create a delayed stack.

### Cluster runtime role

**Resolution**

Use optional membership with a 60 percent participation value and Medium danger.

**Reason**

The user supplied Medium severity.

An optional role prevents a world-scale leader mutation from becoming mandatory in every Randomizations cluster firing.

### Cluster ID

**Resolution**

Prefer ID `9` after a fresh collision check.

**Reason**

The inspected source assigns IDs `1` through `8`, and the supplied CSV uses `10` for Intelligence.

### Player reporting

**Resolution**

Apply effects in the hidden root and report results to human countries afterward.

**Reason**

Trait outcomes must not depend on popup timing.

### Report detail

**Resolution**

Show the local player's leader and trait names, plus global counts and pool size.

**Reason**

The player should know the immediate result without searching the leader interface.

A full world assignment list would be too large.

### Asset scope

**Resolution**

Use one opaque `210x176` generated report-event image.

**Reason**

The event has one visible report surface.

A focused documentary image is sufficient.

## Implementation questions requiring evidence

| Question | Required evidence |
| --- | --- |
| Exact vanilla trait roots | Offline documentation, source inspection, generator discovery report |
| Whether every database entry accepts direct application | `hoi4.event_inspect`, targeted test event, error log |
| Whether trait ownership is character-local or role-local | Character and leader-role inspection across leave and return cases |
| Best ledger scope | Save and load test, leader replacement test, shared-character test |
| Exact conditional random-list support | Offline effect documentation and `hoi4.probability_inspect` |
| Exact generated selector method for trait names | Scripted localisation inspection and rendered report |
| DLC definition availability | No-DLC and full-DLC registry builds |
| Randomizations cluster ID at implementation time | Authoritative XLSX and current constants collision audit |
| Current event-log actor fallback for global events | Existing global event history patterns |
| Existing DDS validity | Image metadata inspection and in-game render |
| High-tag performance | Profiler or reproducible execution comparison |
| Multiplayer determinism | Two-client synchronized firing and error-log review |

## Decisions that must not be changed silently

The implementation agent must request a design revision before:

- adding thematic trait filters
- allowing duplicate source IDs to consume slots
- reducing the complete pool to a curated list
- moving gameplay mutation back into the report option
- giving the player a veto or reroll
- increasing the maximum featured ratio above `1.50`
- adding per-country or per-trait Chaos
- using a random country as the false global actor
- declaring Event 65 available without user testing
