# Event 064 Border Fortifications

## Part 1: Core event and baseline wave

## Accepted identity

| Field | Accepted value |
| --- | --- |
| Event ID | `064` |
| Event name | Border Fortifications |
| Type | Minor Repeatable |
| Status during planning | To Be Reworked |
| Chaos level | `1` |
| Primary cluster | Sudden Abundance |
| Primary member severity | Medium |
| Additional cluster | Military Preparation |
| Additional member severity | Medium |
| Canonical entry event | `chaosx.nr64.1` |

## Playable promise

A complete line of defensive works appears along the world's current land frontiers during one synchronized incident. Countries receive concrete positions they did not budget, schedule, or build. The map changes at once, but the strategic result differs by geography. A compact state gains a short fortified belt. A large continental power gains many disconnected sectors. An occupied front can harden in place. An island government sees foreign coastlines and invasion plans change even when no local frontier exists.

The first wave should be useful without deciding every future war. Repeated waves should make the world increasingly difficult to attack, while still leaving gaps, supply problems, weak sectors, and countermeasures. Higher evolutions reserve the strongest packages for selected positions.

The event gives the player three immediate questions:

1. Which parts of the new line matter most?
2. Can the country supply and man the positions it received?
3. How will the army cross equally strong foreign lines?

These questions create the event's replay value. The automatic construction is global and simple. The strategic use of that construction is local and depends on each country's wars, borders, economy, terrain, and plans.

## Global incident model

The canonical entry event is a hidden global root. It owns the incident sequence, builds the firing-time snapshot, applies every automatic building change, records the world result, and sends local reports after the transaction is complete.

The construction must not be attached to a player-facing option. Forts should exist at the same game moment for human and AI countries. A player who leaves a report open must not delay their own line while the rest of the world receives one. This also prevents multiplayer desynchronization and prevents the same global wave from running once for every human player.

The root creates one incident token. Every country, state, province role, report, direct Chaos source, cluster context, and cleanup action belongs to that token. Any duplicate dispatch that reaches Event 064 while the token is active must reuse the active incident or reject the duplicate. A second world pass cannot start.

### Transaction order

1. Confirm that this is a new valid incident and create the global wave token.
2. Save automatic, manual, debug, and cluster context before any country processing begins.
3. Snapshot the countries that currently control valid map territory.
4. Process each country once and build its current foreign land-frontier set.
5. Apply the baseline fort level to every qualifying direct frontier province.
6. Apply each enabled and matured evolution package in ascending order.
7. Save per-country and global result counts.
8. Record the event history row and any first concrete evolution rows.
9. Apply mapped event-owned Chaos changes after confirming the actual footprint.
10. Send each human-controlled country its local report.
11. Establish the response window and AI posture choices.
12. Clear temporary arrays, saved scopes, scores, deduplication flags, and incident context.

The complete construction pass should finish before any report option is selected.

## Valid countries

The physical wave applies to any country that currently controls at least one valid land province and can receive normal map buildings. A country does not need to be independent, recognized, at peace, human controlled, or part of the ordinary civilian system.

The event should include the following when they have valid territory:

- majors and minors
- player-controlled countries
- AI countries
- subjects and overlords
- faction leaders and faction members
- countries in civil wars
- temporary countries and released countries
- normal event-created countries
- special Chaos countries whose owner package permits ordinary map buildings

A country is skipped only when its current state makes the map transaction invalid, such as having no controlled land territory, using a nonstandard owner contract that forbids normal buildings, being a dead scope, or existing only as an off-map carrier.

Special Chaos classification alone is not an exclusion. Forts appear independently of ordinary government capacity. The separate response decisions can be withheld from actors that do not use normal civilian, stockpile, command, or decision systems.

## Foreign land-frontier definition

A direct frontier province is a controlled land province with at least one passable direct land adjacency to a land province controlled by another country at the moment of the snapshot.

The definition includes:

- peaceful borders
- hostile fronts
- allied borders
- faction-internal borders
- subject and overlord borders
- civil-war frontiers
- boundaries inside occupied territory when different countries control the neighboring provinces
- river edges that still count as ordinary land adjacency
- enclaves and disconnected land pockets

The definition excludes:

- sea adjacency
- strait-only adjacency
- canal-only adjacency that is not an ordinary land edge
- lake edges
- impassable connections
- off-map provinces
- provinces without a valid land-fort building slot
- neighboring provinces controlled by the same country

Diplomatic relations do not filter the result. The anomaly fortifies the physical boundary that exists, including boundaries between close allies. This is important to the event's Sudden Abundance identity. Geography determines the distribution. Strategic intent does not filter the result.

### Current control defines the frontier

The snapshot follows current control so an active occupation front can harden where armies actually meet. The resulting structures are physical province buildings. They remain after occupation changes, peace settlements, annexations, releases, transfers, and later wars.

The event does not return to an old owner to rebuild a historical boundary. It also does not move forts when a front advances. A later Event 064 wave evaluates the new map from scratch.

### Province deduplication

A province can border several countries, belong to a selected Fortress State, guard a major city, and form part of a capital approach. It still receives the baseline level once. Role overlap is resolved before construction.

The ordinary per-wave land-fort increase is one level. A strategic anchor can receive one additional level from an evolved package in the same incident. No province may receive more than two Event 064 land-fort levels during one wave.

State buildings such as anti-air and radar use separate state-level caps and do not count as duplicate land-fort grants.

## Firing-time snapshot

All automatic targets are determined from one coherent world state at the start of the incident. The event should not build a line, alter the map, then let later country passes use the changed buildings as a new strategic cause.

The snapshot needs enough information to keep the transaction stable:

- valid country scopes
- each country's controlled states
- direct frontier provinces or the closest safe bounded representation supported by the current engine
- border states
- foreign neighboring countries
- strategic candidate roles needed by enabled evolutions
- existing relevant building levels
- current war and threat context
- cluster context
- evolution enablement and maturity

Ownership or control changes caused by unrelated same-day effects after the snapshot do not reopen the candidate set. The next wave handles the new frontier.

## Baseline construction

Every qualifying direct frontier province receives one land-fort level during the wave, up to the baseline total-level cap.

### Starting balance anchors

- Ordinary per-wave increase: `+1` land fort.
- Baseline ordinary frontier cap: level `3` total.
- Existing provinces already at or above the active cap: unchanged.
- Existing provinces below the cap: raised by one, never set to a fixed replacement value.
- Province with several foreign adjacencies: still raised once.
- Province that becomes an evolved strategic anchor: can receive one further level from that package, subject to the anchor cap and the two-level per-wave ceiling.

The cap applies to the resulting total building level. The event does not need to claim ownership over individual pre-existing fort levels. A province with a level five historical fort is preserved even during a baseline wave whose cap is level three.

The one-level wave is deliberate. Global coverage already creates a large strategic change. A two-level grant to every frontier on every repeat can turn early wars into a general siege before countries have engineers, air power, doctrine, or supply capacity to respond.

## What the baseline does not grant

The baseline wave does not automatically add anti-air, radar, infrastructure, railways, supply hubs, coastal forts, inland redoubts, national modifiers, or free divisions. Those belong to evolved packages or the local response system.

This separation keeps the first firing clear. Every country sees the same simple world rule, while later Chaos levels change how deeply the event reaches into each state's defense network.

## Existing fortifications

Existing defenses are part of the strategic landscape and must be respected.

- The event never deletes or lowers an existing fort.
- Historical and mod-added forts above the current Event 064 cap remain intact.
- Damaged fort levels remain damaged unless the engine's building-level effect inherently restores them. The implementation must verify this behavior and avoid an unintended global repair.
- A province at one level below the active cap receives one level.
- A province several levels below the cap still receives only the normal one-level wave, plus a possible anchor bonus.
- A province at the cap receives no land-fort change but can still contribute to result counts as an existing fortified frontier when needed for reports and achievements.

The local report should distinguish provinces improved this wave from frontier provinces already at or above the cap. This makes a repeat firing understandable even when a mature country receives fewer new levels.

## Border states

A border state is a controlled state that contains at least one qualifying direct frontier province in the firing snapshot.

Border-state identity is used for:

- local report summaries
- strategic scoring
- response decision targets
- Evolution II Fortress State packages
- achievement challenge ledgers
- AI posture and project choices

A state that only touches another country across a strait is not a border state for Event 064. A coastal border state must satisfy the land-frontier definition and also have a valid coast or port role.

## Countries with no direct land frontier

A country with no qualifying direct frontier receives no baseline land-fort grant. Human-controlled countries still receive a concise local version of the global report because foreign fort lines affect their diplomacy and war plans.

At low tiers, such a country can select offensive study if it expects to attack fortified land powers. Defensive and logistics responses remain unavailable when there is no local line to use.

Evolution III can create internal redoubts for an island or isolated country when it has a valid capital, major victory point, supply hub, or other accepted strategic position. The local report then treats those redoubts as the country's Event 064 result.

A country with no valid local construction and no meaningful response target should receive no persistent decision category after it closes the report.

## Tiny countries, enclaves, and fragmented territory

The system should not judge value only by raw province count.

- A one-state land country can receive a complete short line.
- A country with one direct frontier province receives the ordinary level and can qualify that province as an evolved anchor.
- An enclave is processed like any other controlled territory.
- Disconnected frontiers should receive geographic spread before a second evolved target is selected in the same state or region.
- A long colonial frontier does not justify filling every interior position with high-tier works.
- A country split across continents uses one country quota with a minimum spread rule so the home region does not always consume every evolved target.

When exact connected-front segmentation is too expensive or unsupported, use border-state and strategic-region diversity as the bounded approximation. Do not replace the distribution rule with uniform random province selection.

## Demilitarized and restricted areas

The event is an abnormal physical manifestation, so ordinary political construction policy is not a design exclusion. A demilitarized or treaty-restricted state can receive a line if the engine permits the building.

The implementation must not force an invalid engine placement. If a hard map or building rule blocks construction, record the province as skipped and continue the transaction. The report can mention that some surveyed positions remained unchanged without exposing internal error language.

The event itself does not create automatic war goals or claims over treaty breaches. Existing diplomacy, tension, and cluster systems can react through their normal rules.

## Report and player choice timing

Every human-controlled valid country receives a local report after the global construction transaction.

The report communicates:

- that the same phenomenon occurred worldwide
- how many local direct frontier provinces were improved
- how many local frontier provinces were already at the active cap
- which evolved packages produced local positions
- whether the country has a valid response window
- the broad posture choices now available

The report should not list raw hidden scores, candidate arrays, cluster rolls, or future evolution conditions.

Countries with local works choose one of three response postures in the report. These postures are developed in Part 3. Countries without a local line receive only choices that remain meaningful for them.

AI countries make the same posture selection through weighted option logic after their construction result is known. Their option has no control over whether the forts exist.

## Multiplayer behavior

The world transaction runs once from the canonical root. Every human player receives a local report based on their own country result.

The event must preserve these properties:

- all players see the same global construction state
- one player cannot delay the fort grant by leaving a popup open
- one player cannot trigger the global pass again by choosing an option
- local counts and posture options use the correct country scope
- a country controlled by several human participants receives the normal game-supported report behavior without duplicating the world effect
- the event history records one global incident, not one event firing per player

## Repeatable lifecycle

A later natural or cluster firing creates a new wave token and reevaluates the current map.

Repeated waves can:

- strengthen old frontier provinces toward the active cap
- fortify borders created by wars, releases, annexations, and occupations since the last wave
- choose different strategic anchors and evolved state packages
- open a new response window
- replace the old posture with a new choice
- produce a small repeat Chaos premium only when the wave has a meaningful footprint and its direct-source cooldown has expired

Repeated waves cannot:

- exceed role caps
- process one province more than twice in one incident
- stack several copies of the same posture
- preserve stale target markers from an earlier map
- pay direct Chaos for a no-op or tiny cleanup wave
- rebuild every newly changed border through a recurring background scan

### Natural availability and duplicate protection

The ordinary repeatable-event weight system remains the main frequency control. Add a bounded Event 064 recent-wave availability or effect guard if repository inspection shows the generic system can otherwise dispatch global waves too close together.

Starting design anchor:

- natural Event 064 wave cooldown: about `365` days
- exact same-incident or queued duplicate guard: at least `30` days, with the active token taking priority
- manual debug firing: can bypass the natural cooldown but must still create one unique token and must suppress achievements
- cluster firing: follows cluster rules and cannot duplicate a wave already created by the same cluster incident

The implementation should tune the natural cooldown against the current random-event timer, weight recovery, and cluster cadence. The purpose is to prevent rapid global map scans and immediate cap saturation, not to make the event effectively fire once.

## Persistence

Land forts, coastal forts, state anti-air, radar, infrastructure improvements, and other completed buildings are normal map state after construction. They survive save and reload and transfer with the province or state.

Event-specific temporary state includes:

- current wave token
- country result counts
- active response posture
- response-window expiry
- active targeted project
- project target
- evolution first-materialization guards
- direct Chaos cooldown guards
- achievement challenge ledgers

Temporary candidate arrays and scoring variables must be cleared when the transaction ends. Persistent state must use stable country, state, province, or global ownership appropriate to its purpose.

## Event history and Event Details

The event needs one global History row for each completed wave. The row should be actorless unless the shared event-log surface requires another verified global presentation. It must not imply that one country built the world's defenses.

The History detail should expose useful visible results:

- date
- natural, cluster, or manual context where public
- global countries processed
- global direct frontier provinces improved
- current highest concrete evolution package applied
- local country result when opened from a player context if the log supports it

Event Details should describe the premise and accepted evolution identities. It should not list exact fort caps, Chaos gains, hidden scoring, achievement conditions, or future candidate logic.

The event-detail evolution catalog remains distinct from logged evolution history. It previews Defense in Depth, Fortress States, and Fortress World without fake dates or fake sequence numbers.

## Baseline completion standard

The baseline is complete only when:

- `chaosx.nr64.1` resolves one global transaction
- every valid direct foreign land-frontier province is processed once
- the one-level grant respects the baseline cap and existing higher forts
- non-land adjacency is excluded
- country and province deduplication is proven
- no player option owns the automatic grant
- human reports use saved local results
- AI receives the same physical outcome
- save and reload preserve buildings and response state
- repeat waves use a new snapshot and new token
- stale temporary data is removed
- History, Event Details, debug names, and catalog identity agree
- task-specific large-world validation shows no recurring scan and no duplicate global application
