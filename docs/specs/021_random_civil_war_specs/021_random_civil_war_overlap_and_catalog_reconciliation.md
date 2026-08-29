# Event 021 Overlap and Catalog Reconciliation

## Current catalog snapshot

The supplied event CSV lists Event 021 as:

- `Random civil war`
- `A random country fractures into rival governments and armed camps.`
- `Minor Repeatable`
- no cluster
- no member severity
- `Unavailable`

The supplied cluster CSV lists Wars as:

- Cluster ID `1`
- members `4, 7`
- type `Minor Repeatable`
- chaos level `1`
- `Partially Available`

This specification assigns Event 021 to Cluster `1` with `Medium` severity. The authoritative workbook should be updated only after implementation and final player-facing wording.

## Event ownership matrix

| Event | Existing premise | Event 021 relationship |
| --- | --- | --- |
| 004 Random War | External war between eligible countries | Cluster partner, can overlap at higher chaos |
| 005 Soviet Union Collapse | Soviet collapse waves and successor coalition | Separate owner, Event 021 can later target human successors |
| 006 Independence Wave | Multi-country release system and full country packages | Package provider and identity source, Event 021 does not consume Event 006 firing |
| 007 Fury | Expansionist human war actors and Fury escalation | Cluster partner, newly created Fury actor normally reserved |
| 019 Soldiers from Nowhere | Generated formations, claimants, and immediate formation revolt scenario | Separate formation owner, no Event 019 progression through Event 021 |
| 095 Occupation Revolt | Exile or occupation-based uprising | Takes priority when occupation is the premise |
| 117 Five-Way Civil War | Bespoke five-camp major or player crisis | Separate owner, may reuse helpers later |
| 127 Warlords | Named warlord political system | Separate owner, Event 021 command schism stays institutional |
| 131 Widespread Mutiny | Low-war-support mutiny | Separate owner, can provide documented command pressure |
| 134 Duchies | Separate specialized event premise | Event 021 can use only accepted package identities |
| 142 Partisans | Partisan divisions tied to ideology support | Separate owner, explicit integration required |
| 144 Freedom or Death | Simultaneous global subject liberation and faction | Separate owner, Event 021 can fracture one subject only |

## Scenario separation

| Scenario | Owner | Main setup | Difference from Event 021 scenario |
| --- | --- | --- | --- |
| SCN-008 Every Banner Rises | Event 006 | Every viable independence package considered | Event 021 scenario mixes ordinary civil-war actors and does not need to release every package |
| SCN-013 The Unbidden Muster | Event 019 | Immediate formation revolts and generated military lots | Event 021 scenario uses political, legal, command, regional, and Event 006 actors through the civil-war framework |
| The Fracture Cascade | Event 021 | Chosen share of normal human countries enter civil wars | No Event 019 unit-generation identity and no automatic Event 006 event state |

## Specialized event precedence

When two premises fit one country:

1. terminal or owner-specific safety gate
2. specialized event already active
3. specialized event whose defining premise is present
4. Event 021 generic route
5. another target or no event

Examples:

- foreign occupation and exile claimant favors Event 095
- globally generated army revolt favors Event 019
- named five-way design favors Event 117
- ordinary domestic ideology split favors Event 021
- complete regional independence actor can use Event 021 plus Event 006 package
- global subject uprising favors Event 144

## Shared-helper boundary

Reusable Event 021 helpers may later support specialized events for:

- connected region planning
- parent remnant protection
- force allocation
- front registry
- selected-front decisions
- independent front settlement
- cleanup
- lineage tracking

The specialized event retains:

- event ID
- trigger
- actor identity
- evolution
- presentation
- scenario
- super-event
- achievements
- documentation
- catalog wording

## Catalog fields after implementation

Suggested player-facing direction:

### Event details

A country can fracture into rival governments, military commands, regional movements, or independence actors. The scale follows its stability, war state, administration, territory, political access, and command loyalty. Later escalation can create several fronts, neighboring political pressure, and global domestic risk.

### Evolution I

Internal divisions become separate armed projects. Large and major countries can split into several governments, commands, and independence fronts.

### Evolution II

Civil wars attract sponsors, spread organized political and military networks across borders, strengthen surviving sides, and produce rare unexplained practices.

### Evolution III

Every normal human country must manage its own fracture risk. Newly independent states and successor governments remain vulnerable.

### Cluster

Wars should list members `4, 7, 21` after implementation.

### Scenario

Add the verified Event 021 scenario ID, final name, four types, four intensities, and status.

Final spreadsheet wording must mirror final in-game Event Details and scenario localisation.
