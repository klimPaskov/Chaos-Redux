# Event 063: Subjects Break Free

## Part 1: Core event design

## Event identity

- Event ID: `63`
- Event name: Subjects Break Free
- Type: Minor Repeatable
- Chaos level: 1
- Primary cluster: Liberations
- Primary cluster role: Medium member
- Secondary cluster classification: Domestic Unrest
- Secondary cluster role: Medium member

## Premise

Several countries that currently exist as subjects cease to answer to their overlords. Ministries assume full control of foreign policy, armed forces receive national orders, and dependent diplomatic arrangements are either converted into ordinary agreements or terminated. The countries remain the same campaign entities. Their territory, armed forces, stockpiles, government, leaders, laws, research, production, national spirits, focus progress, intelligence state, claims, and cores remain intact unless a later settlement outcome directly changes one of those relationships.

The event is a recurring liberation shock. It should make the current subject map less stable without turning every firing into a worldwide colonial war. A calm firing may produce a few orderly separations. A later firing can release a coordinated group from one overlord, open a combined independence war, or strengthen an international network of previously liberated states.

## Core player experience

The event should create three linked questions.

1. Which subjects become independent in this firing?
2. How does each former overlord answer the separation?
3. Do the newly independent countries remain isolated, cooperate informally, or enter the Liberation Pact?

The first question is resolved by a bounded weighted selection from a frozen pool. The second question uses a settlement matrix with human choices and AI evaluation. The third question persists after the event and connects Event 063 with Independence Wave and compatible Soviet Collapse successors.

## Existing-country preservation rule

A selected subject becomes independent in place. The event must never destroy the subject and create a substitute country to represent the same government.

The following country state is preserved:

- owned and controlled states
- cores and claims
- capital and map identity
- current government, ruling party, ideology, party popularity, and elections
- country leader, commanders, operatives, advisors, and character state
- armed forces, templates, deployed units, fleets, wings, equipment, and manpower
- production lines, construction, trade, resources, fuel, convoys, trains, and stockpiles
- research slots, technologies, active research, doctrine progress, and special projects
- laws, national spirits, dynamic modifiers, balance of power, and country variables
- focus tree, completed focuses, available branches, and current focus
- intelligence agency, networks, cryptology state, and operations
- cosmetic name, flag state, and other identity already active for that country
- war participation against third countries unless the settlement creates a direct conflict that requires a safe topology change

The release changes subject status and the diplomatic arrangements that depended on it. It does not grant a generic replacement army, reset the economy, replace the leader, or erase country-specific content.

## Frozen release transaction

Every firing uses one release transaction. The transaction is built before any selected country becomes independent.

### Transaction sequence

1. Build the complete valid subject pool from the current campaign state.
2. Snapshot the facts needed for selection, settlement, rollback, and reporting.
3. Determine the target release count from the frozen pool size and active evolution state.
4. Select countries without replacement.
5. Reserve every selected country and the relevant former-overlord relationship through the shared Liberation Release Coordinator.
6. Prepare fallback candidates from the same frozen pool.
7. Release the valid reserved countries in place.
8. Resolve human and AI settlement postures.
9. Register successful liberations in the shared liberation-origin contract.
10. Publish one global summary, direct notices for affected human countries, and the required history and evolution entries.
11. Clear all transaction reservations and temporary context.

The first release must not alter the candidate pool used for later picks in the same firing. A subject becoming independent can change faction membership, war participation, relative strength, autonomy totals, and overlord eligibility. Freezing the pool prevents those changes from biasing or corrupting the remaining selections.

### Reservation authority

The Liberation Release Coordinator is the collision authority whenever Event 063, Independence Wave, Soviet Collapse, or another approved country-release system could act on the same country or territory during the same execution window.

Event 063 reserves an existing subject relationship. It does not reserve or redraw states because it is not creating a new country. A state reservation is needed only when another release system has already reserved states belonging to the selected subject or is in the middle of replacing its country package. Such a candidate is normally excluded before selection.

A reservation must identify:

- transaction owner
- selected subject
- current overlord
- transaction generation
- selection order
- settlement status
- whether the release completed
- whether the shared origin record was written
- whether cleanup completed

A failed reservation is replaced by a frozen fallback before the first country is released. Once the first release has occurred, the transaction does not rebuild the pool. A later invalid candidate is skipped and the firing continues with its other valid selections.

## Candidate validity

A valid candidate must meet all of these conditions when the pool is frozen:

- the country exists
- the country is currently a subject of another country
- the country owns at least one state
- the country controls at least one valid state
- the subject relationship can safely be removed without recreating the country
- the country is not already reserved by another release, split, civil-war, annexation, or country-replacement transaction
- the country is not a special Chaos actor whose diplomatic and civilian systems cannot support ordinary independence
- the country is not an actual nonhuman country
- neither side is in a terminal state that makes the release transaction meaningless
- the current relation is not a transient civil-war or scripted relation whose removal would corrupt its owner system
- the country is outside its Event 063 target cooldown following a recent re-subjugation and re-release

Subject type alone should not decide validity. Integrated puppets, collaboration governments, dominions, satellites, reichskommissariats, supervised states, and modded autonomy types can participate when their relation can be removed safely. Their autonomy and political circumstances affect selection weight and settlement, not the basic principle that a valid existing subject can break free.

If an unusual subject type has an owner system that would be damaged by ordinary independence, it must be blocked by an owner-provided compatibility trigger. Event 063 should not maintain a hardcoded list of every present and future autonomy type.

## Candidate snapshot

The frozen snapshot should retain the facts that matter after independence changes the live state.

### Identity and relation

- subject country
- former overlord
- autonomy type and autonomy progress
- subject start date when available
- origin of the subject relation when known
- faction leader and faction membership
- guarantees, non-aggression pacts, military access, docking rights, licenses, and active aid
- expeditionary forces and foreign-controlled units

### Political and diplomatic condition

- mutual opinion
- ideology and ideological distance
- ruling-party relationship
- active claims and cores between the two countries
- guarantees from third countries
- relations with previously liberated states
- liberation-origin and network status
- whether either side has recently supported or suppressed another breakaway

### Military and strategic condition

- relative army, air, and naval strength
- available manpower and equipment condition
- state count and industrial strength
- shared border and capital distance
- supply connection and access dependence
- active wars and whether both countries fight on the same side
- surrender progress, casualties, war load, and front exposure
- strategic resources, ports, bases, or routes that make the subject unusually important to the overlord

### Event ownership state

- Event 063 cooldowns
- Event 006 provenance and active package state
- Soviet Collapse successor provenance
- reservations held by other release systems
- unresolved prior settlement or independence war
- current Liberation Pact membership or partner status

The snapshot is evidence for the firing. Later live changes should determine ongoing diplomacy, but they must not rewrite why the country was selected or how the opening settlement was classified.

## Release count scaling

The release count scales with the number of valid candidates in the frozen pool. The event remains a medium-severity repeatable incident, so the batch is bounded even when the world contains many subjects.

| Valid candidates | Baseline release range | Normal center |
| ---: | ---: | ---: |
| 1 | 1 | 1 |
| 2 to 4 | 2 | 2 |
| 5 to 9 | 2 to 3 | 3 |
| 10 to 16 | 3 to 4 | 4 |
| 17 to 25 | 4 to 5 | 5 |
| 26 or more | 5 to 6 | 6 |

The exact count within a range should use a weighted roll. Larger pools should favor the upper end. Very small pools should not lose half their remaining candidates to a low roll. Evolution I increases the range and raises the hard cap to eight.

The selected count can be lower than the target only when reservations or late validity checks fail and no frozen fallback remains. The global report must state the completed number, not the intended number.

## Selection model

Selection uses weighted sampling without replacement. The weight represents the chance that a subject becomes part of this firing. It does not determine the settlement outcome by itself.

### Strong positive factors

- high autonomy or near-complete autonomy progress
- military or industrial strength relative to the overlord
- an overlord with low stability, high surrender progress, heavy casualties, many wars, or exposed fronts
- strong hostility toward the overlord
- major unresolved claims or cores between subject and overlord
- recent successful breakaways from the same overlord
- recognition, guarantees, or aid from the liberation network
- support from the Liberation Pact
- a previous Independence Wave or Soviet Collapse origin that gives the country a remembered independent identity

### Moderate positive factors

- a land border that makes independent administration practical
- distance from the overlord's capital
- ideological incompatibility
- a subject government with a strong domestic mandate or military establishment
- an overlord already managing several subjects
- pressure created by Event 127 Warlords or Event 128 Autonomy

### Negative factors

- recent voluntary acceptance of subject status
- very low autonomy with no independent military or administration
- high mutual opinion and close ideological alignment
- a stable overlord with overwhelming strength and no war pressure
- active dependence on the overlord for access or survival
- a recent Event 063 release and re-subjugation cycle
- unresolved owner-system state that makes another immediate status change unsafe

Every valid candidate keeps a small nonzero selection floor. Loyal and integrated subjects should be uncommon at low Chaos, but they should not become permanently immune to a chaos event.

### Diversity and cohort rules

At baseline, the selection should spread releases across different overlords when enough valid overlords exist. It can select two subjects of one overlord, but it should not consume the entire batch from one empire merely because that empire has many subjects.

Evolution I deliberately creates one same-overlord cohort. The event first selects an eligible cohort host, then selects two to five of that overlord's subjects as a coordinated group. Remaining release slots return to the global pool.

Only one coordinated cohort is created in one firing, and it belongs to one former overlord. This keeps the event readable and prevents a single medium event from opening many separate group crises.

## Repeatability and cooldowns

The event remains eligible while at least one valid subject exists. Event weight is shown as `N/A` when no valid candidate exists.

Two cooldown families control repetition:

- A country that was freed by Event 063 and later becomes a subject again should normally be protected from another Event 063 release for about two years. The exact duration may use dynamic factors based on how the new subject relation formed.
- A former overlord affected by an Event 063 firing should normally receive about one year of reduced selection pressure. The penalty can be shortened when the overlord still has many subjects, suffers severe war collapse, or faces an active coordinated breakaway movement.

Cooldowns reduce weight or temporarily block a target. They do not make the event globally unavailable when other candidates exist.

A repeat firing can affect a country that was originally created by Independence Wave or Soviet Collapse, later became a subject, and is now valid again. Its first origin remains preserved in the shared registry.

## Failure handling

### Failure before the first release

If no selected candidate can be reserved, the event does not partially fire. It reports no valid target to the event system, clears temporary data, and leaves the event weight available for a later valid draw.

### Failure after one or more releases

Completed releases remain valid. The failed candidate is skipped, the transaction continues with its other reserved candidates, and the global report records a smaller batch. The event must not reverse countries that were already released simply to restore the original target count.

### Overlord disappears during the transaction

The affected subject remains independent. Its settlement becomes recognized by default because no former government remains able to contest it. Claims and subject-derived agreements tied only to the vanished overlord are cleaned up.

### Subject disappears during the transaction

Its reservation and pending settlement are removed. It is not replaced after the first release. The remaining batch continues.

### Save and reload during a pending human settlement

Successful independence remains in force. Pending reaction choices, their expiry date, and safe default must persist. Reloading must not repeat the release, duplicate origin records, or reopen already resolved notices.

## Baseline completion state

A firing is complete when:

- every completed subject is independent
- the preserved country state remains intact
- subject-derived diplomatic arrangements have been retained, converted, or removed according to the settlement
- any human-human pending settlement has resolved or has a stored bounded deadline
- successful countries have shared origin records
- the network has evaluated recognition and support opportunities
- one global report has been published
- affected human countries have received their direct notices
- history has recorded the firing once
- all reservations and temporary arrays have been cleared

The event should leave behind countries, relations, and possible conflicts that continue to matter. It should not leave a permanent maintenance burden when no settlement, war, network action, or Pact activity remains.
