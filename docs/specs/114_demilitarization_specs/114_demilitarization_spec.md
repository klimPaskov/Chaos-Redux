# Demilitarization

A peaceful frontier becomes a place where an army cannot remain. Border posts empty, field plans lose their starting positions, and formations gather farther inland. The first disruption is geographic. Its later consequences are institutional: soldiers begin to question why they are still serving, commanders struggle to keep formations together, and the usable military map contracts toward the capital.

War restores the country's ability to defend its territory. It does not restore soldiers, equipment, unit experience, or formations already lost. Peace brings the territorial restrictions back.

All structural names in this package are working labels, not final localisation. Numbers are authored starting balance targets unless identified as a supplied or inspected system rule.

## The playable promise

Every country at peace participates in the worldwide condition. At baseline, every land-border state under that country's control becomes a demilitarized zone. Interior states remain available under the normal rules of the game.

The player manages the consequences of compulsory withdrawal. They can spend industrial effort on service conditions, concentrate experienced cadres, deliberately consolidate a weakened formation, or impose attendance discipline. These choices become especially important when the Desertion Crisis is active. They preserve an army under restriction, but they cannot purchase a territorial exemption.

The design has three recognisable escalations:

- Deeper Demilitarization adds one inward layer of states.
- Desertion Crisis causes actual losses from peacetime fielded divisions and can culminate in a formation dissolving.
- Total Demilitarization extends the restriction across almost the entire country.

The geography should be immediately legible on the map. The army consequences should be legible through one public value, Army Cohesion, and concrete reports about affected formations.

## First appearance

The shared event dispatcher activates one global regime. It gathers the peaceful countries and applies the current territorial rule to their controlled states. Countries already at war are registered for later peace handling but receive no Event 114 territorial restriction while their war continues.

The opening news describes a simultaneous withdrawal from frontier positions. The country report then describes the actual local result. A large continental country hears about movement into inland garrisons. A thin country hears that almost all domestic space is affected. An island country can receive a short account of the wider development without a false claim that a land border was closed.

There is no player vote on whether the baseline applies. The opening acknowledgement communicates what has already happened and points toward the response category when a response is relevant. It must not imply that the player has voluntarily enacted a treaty.

The first firing deterministically selects the highest enabled, sequentially qualified opening permitted by current Chaos. It waives only the live age requirements, checks valid country and army prerequisites, and commits the chosen form once. There is no additional evolved-opening random draw. The opening report describes the resulting territorial extent and service conditions directly. Three redundant popups should not replay the same withdrawal merely because three evolution records were created.

## What counts as a border

A land-border state is a controlled state with at least one genuine land adjacency to a state controlled by another country. Use the current state controller for applicability. Keep legal ownership as separate provenance.

This distinction matters after occupation, a peace conference, or a civil war. A peaceful legal owner must not impose Event 114 on territory currently controlled by a belligerent country. A peaceful controller also cannot escape the rule by administering land owned by someone else.

| Geographic situation | Intended treatment |
| --- | --- |
| Ordinary international land frontier | Both peaceful sides apply their own restriction to their respective border states. |
| Same faction or military-access partner | The international frontier still counts. Friendly relations do not merge countries. |
| Subject and overlord | Their separate controlled territories still create a frontier where they meet. |
| A coastline with no foreign land adjacency | Coastline alone does not make a border state. |
| An island connected only by a sea route | No border contribution from that route. |
| A scripted strait or special adjacency | Count only when the installed adjacency is genuinely a land connection under the approved geometry rule. Record its type during validation. |
| An enclave or detached possession | Evaluate its own controlled land frontier. Do not borrow depth from the mainland. |
| An impassable frontier | It remains a political land frontier if the installed map represents an actual land adjacency. Pathfinding permission is a separate matter. |
| A state adjoining several countries | Add it once. More neighbours do not multiply the restriction or losses. |
| A border capital | It is a border state and is included. |
| A state whose controller changes | Recompute for the new controller and the affected neighbours. Preserve other sources of demilitarization. |

The final geometry must come from installed state and province adjacency evidence. A state-neighbour iterator is acceptable only after its treatment of sea connections, straits, and impassable links has been established.

### One layer means one layer

Let B be the current country's border-state set. Deeper Demilitarization adds every same-controller state directly land-adjacent to B. The resulting belt is B plus that one additional layer.

Build the additional layer from a fresh snapshot of B. Do not use an already expanded set as the next frontier. Repeated callbacks, repeated firings, and save loading must reproduce the same one-layer result.

### The capital rule

Total Demilitarization adds all controlled non-capital states to the restrictions already imposed by the activated earlier territorial stages. A capital remains usable only when it is outside those earlier belts.

This preserves the brief's universal border rule. It also gives meaning to the word “potentially” in the capital-refuge concept. A deep inland capital may be the sole remaining usable state. A border capital or a capital in the Deeper belt remains restricted.

Moving the capital updates the candidate refuge, but it cannot erase an earlier border obligation, reset a timer, or create two refuges. An uncontrolled legal capital does not create a refuge in an unrelated province. The installed controlled-capital rule must identify the real remaining capital state.

## Armies already in affected territory

The territorial change must preserve actual formations, including their ownership, template, experience, manpower, and equipment. Baseline demilitarization is not a disguised army deletion effect.

Where legal domestic destinations exist, use the native evacuation behaviour if it meets the contract. Otherwise, an explicitly verified transfer can move affected formations to a reachable, legal same-controller state. Prefer the nearest usable interior state in the same connected land component, then a valid controlled capital. Do not promise a teleport across an enemy line or a sea passage merely because both endpoints share a flag.

Foreign formations require their own valid owner and access context. A guest army does not make the host belligerent and does not grant a host-state exemption. Event 114 must not steal, duplicate, or dissolve guest formations while applying a territorial rule.

### Countries with no usable domestic space

A one-state country or a very narrow country can have every state restricted even at baseline. The same can happen under later stages.

The required result is explicit: all mandatory states remain DMZs and the country's existing army survives with its identity and resources intact. On entry into war, that army must be able to resume normal deployment under the ordinary rules. The implementation must demonstrate how the native DMZ system preserves formations in this case.

This is a named engine capability gate. A border-capital exemption, an invented off-map army store, a forced baseline disband, or replacement divisions with reconstructed templates would change the promised event. None is an accepted substitute. The country-specific status must accurately describe the restricted space while the implementation proof remains a development requirement.

## War and peace

A country is at war when it is an actual participant in at least one active war. A war goal, a guarantee, faction membership, a ceasefire narrative, or an ally's war does not suffice.

At war entry, remove that country's Event 114 contribution from its controlled states immediately through the shared DMZ ownership rule. If another source still requires a DMZ, it remains. Suspend Event 114's peacetime cohesion reviews and service penalties. Cancel active response programmes according to their stated settlement rules. Preserve all actual losses, pending personnel returns, earned history, cooldowns, and crisis receipts.

Peace restoration occurs only when the country's last war ends. Recalculate the current frontier and activated territorial stages. Future-enable checkboxes do not roll back a stage that already activated. Do not restore an old geographic snapshot after conquest or a peace settlement.

Cohesion reviews resume with their remaining peacetime interval. A brief war cannot refresh the full interval, erase an endangered formation, or refund response costs. War does not itself satisfy Event 096's allowance or template-unlock conditions.

| Transition | Territorial result | Army and response result |
| --- | --- | --- |
| First entry into war | Release the country's Event 114 claims. | Stop new peacetime desertion. Preserve prior losses and personnel-return receipts. |
| Another war begins while already fighting | No second release transaction. | No extra refund, cohesion gain, or timer reset. |
| One war ends while another continues | Remain suspended. | Continue wartime handling. |
| Last war ends | Rebuild the current territorial footprint. | Resume the remaining review interval and any unresolved formation notice. |
| Same-day war and peace callbacks | Settle from the final valid war state once. | A single transition receipt prevents duplicate effects. |
| Annexation or loss of all controlled states | Retire active territorial claims and obsolete targets. | Settle or transfer outstanding obligations under a verified country-succession rule. |
| Country creation or release | Enrol the actual new country. | Initialise its own legitimate state, without copying another country's rewards. |

Entering a war is an intentional strategic escape from the territorial restriction. The event does not invent a separate test of whether that war was sufficiently serious. Its anti-abuse protection comes from preserving the real costs and history through the transition.

## A persistent, repeatable event

The first firing creates one persistent worldwide regime. A repeat updates that regime. It never starts another controller over the same countries.

Use the shared Minor Repeatable weight and recovery system. A repeat is eligible when it can create a meaningful new result: an unserved territorial application is pending, or Desertion Crisis has an eligible peaceful army whose renewed-pressure cooldown has expired. A fully reconciled baseline with no new consequence is unavailable for an empty repeat.

A renewed-pressure repeat freezes all currently eligible peaceful country targets at preflight. Each country must have an existing eligible fielded army, cohesion of at least 35, and its own 180-calendar-day renewed-pressure guard expired. Revalidate every frozen target before commitment and reduce cohesion by 8 once for each still-valid country. A newly eligible country discovered after preflight waits for a later legitimate repeat. This is one global repeat applied to its valid cohorts, with no additional country-selection roll.

The renewed-pressure consequence does not restart review timing, add an immediate desertion roll, refill a reserve, or undo a response reward. Report the actual affected countries as renewed uncertainty about service and deployment.

An entry that loses its targets before commitment must resolve harmlessly. Selection previews remain read-only. Revalidation and global actor preparation belong before the shared history commitment where the framework permits them.

Repeatability does not grant separate Chaos merely for being selected again. Only the mapped material consequences count.

## Keeping the state coherent

The restriction persists across save and load. Existing obligations are resumed, not replayed. A country has one event-owned lifecycle and one current footprint. State-control changes, country creation, war transitions, and confirmed capital changes mark the relevant actors and neighbours for recalculation.

Use one activation pass for the worldwide launch. Later work is bounded to enrolled actors, due reviews, and dirty state neighbourhoods. A routine whole-world periodic scan is outside the approved maintenance design.

Event 114 releases only its own contributions. The existing Communist Lockdown and Resources Found systems demonstrate why a simple “I set this flag once” snapshot cannot protect later overlapping writers. Their relevant DMZ writes and cleanup must participate in a shared source-aware ownership rule before Event 114 is considered safe.

Disabling future random appearances does not silently remilitarize an already affected world. Evolution controls govern their own future eligibility and activation. Any existing shared administrative reset path must perform source-aware cleanup and retain the campaign's irreversible military outcomes.

## What a completed implementation should feel like

The first appearance changes where an army can stand. Deeper Demilitarization makes geography and supply matter more. Desertion turns long peace into a military management problem with visible losses and meaningful choices. Total Demilitarization makes the capital and the remaining army feel crowded and vulnerable.

The player can understand each result from the map, the actual affected formations, a single cohesion value, and a small set of decisions. The event remains dangerous without forcing identical outcomes on a large inland power, an island state, a recently defeated army, and a country with almost no interior.

