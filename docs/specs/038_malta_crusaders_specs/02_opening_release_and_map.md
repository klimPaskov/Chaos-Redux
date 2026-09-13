# Opening release and map design

## Release purpose

Event 38 must begin with a coherent military problem. Malta needs enough land, supply, and armed force to survive. It must also remain small enough that the first day is a regional crisis rather than a settled empire.

The opening map is therefore divided into four roles:

1. **Sovereign heartland** gives the country a secure political core.
2. **Holy Land command** creates the central crusade objective and immediate conflict.
3. **Maritime bridge** lets Malta reinforce the eastern theater.
4. **Conditional expeditionary footholds** vary the opening without producing broken enclaves or too many simultaneous wars.

The implementation must select from curated state groups. It must never select an arbitrary coastal state from the whole Mediterranean.

## Provisional state anchors

The table below records current public-wiki anchors for planning. These values are not implementation proof. The coding agent must inspect the installed vanilla state files and use `hoi4.map_inspect` before freezing the registry.

| Strategic role | State | Provisional ID | Status |
| --- | --- | ---: | --- |
| Sovereign heartland | Malta | `116` | Provisional, locally verify |
| Holy Land command | Palestine | `454` | Provisional, locally verify |
| Holy Land corridor | Jordan | `455` | Provisional, locally verify |
| Maritime bridge | Cyprus | `183` | Provisional, locally verify |
| Aegean island option | Dodecanese | `164` | Provisional, locally verify |
| Aegean island option | Aegean Islands | `187` | Provisional, locally verify |
| Aegean reserve | Crete | `182` | Provisional, locally verify |
| Greek mainland option | Attica | `47` | Provisional, locally verify |
| Greek mainland option | Peloponnese | `186` | Provisional, locally verify |
| Greek mainland option | Epirus | `185` | Provisional, locally verify |
| Greek mainland option | Central Macedonia | `731` | Provisional, locally verify |
| Greek mainland option | Thrace | `184` | Provisional, locally verify |
| Southern Anatolian option | Antalya | `342` | Provisional, locally verify |
| Cilician option | Adana | `344` | Provisional, locally verify |
| Cilician option | Mersin | `345` | Provisional, locally verify |
| Cilician option | Hatay | `799` | Provisional, locally verify |
| North African option | Tripolitania | `661` | Provisional, locally verify |
| North African option | Cyrenaica | `663` | Provisional, locally verify |

The exact local state list can contain newer subdivisions. When local files differ, the local installed game is authoritative.

## Authoritative state collections

Implementation should create event-owned state collections with stable semantic names. Suggested collections are:

```text
malta_crusaders_heartland_states
malta_crusaders_holy_land_core_states
malta_crusaders_holy_land_corridor_states
malta_crusaders_aegean_bridge_candidates
malta_crusaders_greek_foothold_candidates
malta_crusaders_anatolian_foothold_candidates
malta_crusaders_north_african_foothold_candidates
malta_crusaders_principality_jerusalem_states
malta_crusaders_principality_antioch_states
malta_crusaders_principality_tripoli_states
malta_crusaders_principality_cyprus_states
malta_crusaders_principality_aegean_states
malta_crusaders_principality_anatolian_states
malta_crusaders_principality_north_african_states
malta_crusaders_holy_world_continent_<continent>_states
malta_crusaders_atlantean_roman_program_states
malta_crusaders_atlantean_atlantic_program_states
```

A state appears once per semantic role. Overlap between different semantic collections is allowed when documented. The scripted architecture must never duplicate a state inside the same collection.

## Opening packages

### Baseline package

The baseline opening contains:

- Malta as the sovereign capital and core
- Palestine as the primary Holy Land command
- Jordan as the inland corridor when the local map and ownership transfer remain coherent
- Cyprus as the normal maritime bridge
- one conditional island or coastal foothold from a curated pool
- no more than four distinct displaced owners in the opening war set

The conditional foothold is selected by a deterministic priority score:

1. an island with a port and valid supply path
2. a state whose owner is already displaced by another selected state
3. a state adjacent by sea or land to another selected state
4. a state that does not isolate a landlocked pocket
5. a state that does not force a new major power into the opening unless the package explicitly allows it
6. a state with enough infrastructure or port capacity to function after bounded setup support

Dodecanese is the preferred historical-symbolic island candidate because of the Order's earlier rule in Rhodes and the direct eastern Mediterranean bridge. It must still pass owner and war-count checks.

### Evolution I pre-fire package

Evolution I does not normally add another sovereign state. It strengthens the human and military package:

- larger knight cadres
- additional mounted and ranged formations
- one more order headquarters
- more convoy and train support
- larger equipment reserves
- one additional commander group
- better port and depot preparation

This keeps the opening regional and avoids using territorial grants as the only difficulty scaler.

### Evolution II pre-fire package

Evolution II includes all lower packages and can add one established dependent state:

- a Jerusalem commandery or Kingdom of Jerusalem if the Holy Land package is valid
- a Cyprus order-state if Jerusalem cannot form coherently
- an Aegean order-state only when its territory is contiguous within the selected island group

The dependent actor receives its own minimal viable country package, forces, equipment, supply, and shared-tree overlay. It cannot appear as a name-only puppet.

Evolution II can add one extra expeditionary foothold when doing so connects two selected areas or gives a stable port. It cannot add a random mainland state merely to make the opening larger.

### Evolution III pre-fire package

Evolution III includes all lower packages and adds:

- immediate foreign religious support receipts
- at least one valid allied participant or volunteer sponsor
- one relic or equivalent legitimacy advantage
- Blessed formation access
- stronger air and naval transport support
- a higher opening Crusade Authority floor
- a larger but still bounded force package

The opening remains regional. Evolution III must not divide every country into believers and nonbelievers. That division belongs only to the Holy World route or its manual scenario.

## State eligibility

A state is eligible for the opening only when all required checks pass:

- the state exists in the loaded map
- it has a valid owner
- it is not wasteland or otherwise unusable for normal country control
- it can support ordinary civilian systems
- it is not already owned by Malta
- it is not part of an active terminal actor's protected territory
- the transfer does not violate an event-owned exclusion
- the selected set has a usable capital and at least one port
- every non-island land pocket has adjacency to another selected Malta or subject state
- the resulting owner war set remains within the package cap
- the state can receive the required population, building, supply, and ownership transactions safely

A state may remain occupied instead of owned when permanent transfer would create a broken setup. The design supports occupied expeditionary commands, but these commands must have clear integration, restoration, or principality routes.

## Freeze, validate, commit

The release transaction uses a three-step contract.

### Freeze

The selector writes the proposed country actor, state set, displaced owners, dependent actors, capital, and evolution package to a private frozen ledger. No ownership changes occur during this step.

### Validate

The validator checks:

- all scopes still exist
- every state is unique in the frozen opening set
- all country tags are collision-safe
- no selected owner has become invalid
- the capital state belongs to the frozen set
- supply and port minimums can be satisfied
- the war list is bounded
- the release will not annex or erase a protected actor unexpectedly
- the transaction can roll back if a later creation step fails

### Commit

The commit effect changes ownership, creates the country and subjects, installs history, creates wars, spawns forces, registers provider families, and opens the player-facing event. The commit writes a success proof only after every required surface exists.

If commit cannot complete, the transaction restores previous ownership and clears every temporary actor and state ledger. The event must not leave half-created principalities or transferred states after rejection.

## Existing Malta handling

The implementation must audit the local vanilla Malta identity before choosing a strategy.

Preferred order:

1. Reuse the vanilla Malta tag and preserve meaningful vanilla history when Malta exists as a releaseable or current country.
2. Transform an existing Malta into the crusader state when it is alive and valid.
3. Release Malta from the current controller when it does not exist.
4. Use an approved protected carrier only when the installed game has no safe Malta identity. A new tag requires a complete collision scan against vanilla, Chaos Redux, installed Workshop mods, and sibling local mods.

When a human player controls existing Malta, the event must not silently replace the player's country with an AI copy. The event can transform the player's Malta and offer the opening route through the player's actor.

## War creation

The opening declares wars only against countries that lost selected territory and remain valid. War creation follows these rules:

- consolidate claims against the same displaced owner into one war
- do not create duplicate wars when the countries are already at war
- do not force a new faction war when a limited regional war can represent the seizure
- handle faction escalation through normal guarantees, faction rules, and regional reaction events
- avoid one global declaration block
- save the original displaced owners for settlement and restoration decisions
- preserve ownership history so postwar decisions can distinguish conquest from later occupation

War goals should support control of the seized region and adjacent crusade claims. They should not grant free conquest of an entire major power.

## Capital and sacred centers

### Malta

Malta remains the initial political capital. Fort St Angelo and the Grand Harbour provide the symbolic and logistical center of the early campaign.

### Jerusalem

Jerusalem is the central sacred and military objective. It can become the crusader state's primary sacred center, but it does not replace Malta as political capital at event start.

### Rome

Rome becomes the primary holy capital only after the Papal route establishes the Holy See or Kingdom of God. The state must be validly controlled and the Pope must be installed through the accepted route.

### Dual-center behavior

The Holy See and Kingdom of God can use Rome as political and holy capital while Jerusalem remains a secondary sacred and military center. The UI and localisation should present this as a two-center system, not as two simultaneous engine capitals.

## Initial construction and supply

The release transaction may repair or add a bounded setup package:

- one viable naval base in Malta and each required bridge theater
- enough infrastructure to prevent immediate zero-supply collapse
- one supply hub or depot only where local topology and balance justify it
- rail links between the Holy Land command and its corridor
- coastal forts in Malta rather than a large inland factory grant
- modest dockyard and military workshop capacity distributed across Malta and captured ports
- airfield access appropriate to the package

The event must not place an implausible metropolitan industry block on Malta. Long-term growth comes from ports, captured workshops, sponsor aid, principalities, naval logistics, and focus-driven development.

## Initial ownership consequences

Transferred population remains real and continues to use famine, migration, occupation, resistance, and casualty systems. The opening seizure can produce:

- trapped civilian movement
- refugee requests
- resistance and local collaboration
- supply strain
- port congestion
- hostile government claims
- religious and interchurch disputes
- condemnation only when the crusader government commits qualifying actions

The transfer itself is not a population deletion and must not create hidden demographic changes.

## Map acceptance tests

The exact map registry is not accepted until all of these scenarios pass:

1. Standard 1936 owners
2. Malta already independent
3. Italy does not exist
4. Britain does not exist
5. France does not exist
6. Turkey is partitioned
7. Palestine and Jordan have different owners
8. Cyprus has changed hands
9. Greece controls the Dodecanese
10. a world-end actor owns one candidate state
11. several candidate states are puppets or subjects
12. Event 40 has active Arabian clients
13. Holy Realm territory overlaps an intended hidden-route area
14. a selected state has no valid port after a map update
15. local vanilla adds or renames states in the target region

Every scenario must return a coherent package, a documented smaller package, or a clean unavailable result. It may not select arbitrary substitutes outside the curated region.
