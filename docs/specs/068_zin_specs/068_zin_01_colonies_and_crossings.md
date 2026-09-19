# 068 ZIN: colonies and crossings

## The campaign

A foreign society occupies an Earth state and announces that it now governs that territory. The first incident can become a negotiated frontier, a failed reconquest, a network of settlements, or the opening of a war carried over from another world. A peaceful campaign must remain worth playing. Later arrivals introduce competing societies whose interests cannot be read from their appearance alone.

The catalog identity is **068, ZIN, Major, To Be Reworked, Chaos level 1, Alien Invasions, Severe member**. The runtime entry remains `chaosx.nr68.1`. The first successful entry consumes the Major event once. Subsequent settlements, political crises, reinforcements, and evolutions belong to that persistent event and do not consume another global pacing event.

The player's first report identifies the arriving society and its claimed homeland. It does not announce a single civilization called ZIN. Independent testimony can establish the common origin before the Reckoning. The Reckoning makes that origin public at the latest. The catalog can retain ZIN as its title without placing that knowledge in the opening newspaper.

All new numerical values, timing, institutions, biographies, and route architecture in this package are proposed design. The supplied brief remains authoritative for named characters, the history of the Ainu, the Rush succession, the three powers, Glo, and the Edvoid boundary. Map-derived colony names already proposed in the brief remain working adaptations where their identity was not fixed by the user.

## A settlement has an identity

A colony instance carries a society key, a unique arrival identity, a homeland map key, a founding state, a former owner, a current country carrier, and a political route. These remain separate concepts. Two Noris colonies share a society without sharing a ruler, diplomatic memory, or equipment stockpile. A cosmetic change does not create a new arrival. An annexed country does not become a fresh colony when its carrier is later reused.

There are 44 arrival society packages and four additional Rush dominion packages. The four succession governments are political packages attached to the Rush crisis. Dragons and Volgan's regional detachments are not arrival countries. The country registry lists every package and its earliest ordinary arrival tier.

A common society may establish several colonies. The canonical Rush Kingdom, Afrit, Volgan, Horos, and the Castle of Yeldenne have unique identities. Another Rush settlement cannot receive another Golden King, another founding Lost Cause, or another mandatory assassination sequence. It uses a provincial Rush route and can later support or oppose the canonical kingdom.

### Founding sequence

| Stage | What happens | What the player can do |
| --- | --- | --- |
| Commitment | A valid society and state are selected together with a free, admitted country carrier. | No player chooses the automatic location. The host receives no veto. |
| Arrival | Ownership changes, the founding capital is set, the society's people and forces arrive, and existing Earth residents remain present. | The former owner receives a report with the actual state and society. |
| First contact | The colony starts in a neutral posture and publishes its initial terms. | Establish contact, recognize it, isolate the frontier, or prepare a deliberate attack. |
| Provisioning | The colony has a 120-day homeland supply bridge and must organize a viable local economy. | Complete a domestic settlement mission and choose a resident policy. |
| Consolidation | The country gains its ordinary political and military decisions. | Build a society-specific route, support another colony, or remain a defended enclave. |
| Wider policy | Focus completion and the relevant evolution permit intervention or conquest. | Choose a declared external policy whose risks are visible before commitment. |

There is no hidden option that retrospectively prevents the initial transfer. A report option cannot charge for an effect already applied. Informational reports show the result once and do not execute the transfer again.

## Selecting a society and an Earth state

The automatic first arrival uses the 16 baseline families. The four central baseline families have a proposed family weight of 20 each. The remaining twelve have weight 10 each. These are family-selection weights, not percentages, and they are normalized only over families that currently have a legal state and an admitted carrier. Later ordinary arrivals use the same baseline weights until their pool expands.

A family is selected before its state. This prevents a society with many matching Earth states from becoming common simply because its terrain appears often. State selection then uses the following proposed score among valid candidates.

| State property | Added placement weight |
| --- | ---: |
| Valid candidate | 10 |
| Preferred broad world region | 20 |
| Primary terrain match | 30 |
| Secondary terrain match | 10 |
| Required geographic feature, such as a port for a maritime package | Eligibility requirement |
| A previous same-origin colony within the permitted regional distance | 10 |
| Existing major hostile colony immediately next door | -5 |
| Former-owner capital | -5 |

Clamp a valid candidate to at least 5. Region and terrain bonuses are additive. A state can receive only one primary terrain award and one secondary award. The map geography informs the preference, not a claim that the ZIN homeland physically corresponds to a real Earth country.

Forces do not shrink when the selected former owner is weak. A powerful society may appear beside a small country. The survival of that country depends on diplomacy, geography, help, or military success. Host army size, ideology, and player control do not secretly downgrade the colony package.

### Valid states

The proposed ordinary allocator excludes sea-only or non-playable states, states already reserved by another release transaction, any state currently owned by an active ZIN colony, the Yeldenne state, and states whose transfer would erase the former owner's last owned state. A former-owner capital remains possible when that owner has another legal capital and the transfer coordinator can complete the move safely. This is a stated design choice, not an assertion that the old script already permits capitals.

Landlocked states cannot receive a package whose core playable promise requires a navy. A mountain or forest preference is usually a weight, not a hard exclusion. A port is a hard requirement for the Rush Island Confederacy, Enhesis, Rafby, Pulundur, Sodoloro, Kradlon sea clans, and IHUJ islanders. A coastal state without a functioning port can qualify only when a real port can be built there during setup without replacing another country's building history.

States under disputed wartime control need a coherent transfer transaction. The colony cannot receive a state whose owner and controller are in incompatible active wars unless the allocator has an explicit supported settlement rule. The standard proposal skips those states for initial sovereign arrivals. Volgan's later invasion operations can target wartime territory through their own declared war route.

Player-owned states receive no immunity. The same eligibility rules apply in single-player and multiplayer. A settings-driven exclusion already owned by the shared event system is respected, but this event does not create a separate hidden protected-player list.

### Reservations and failed placement

Reserve the society instance, carrier, and state as one transaction. Commit only after the capital, population receipt, army package, focus entry, and neutral diplomacy can be established. A failed placement returns the reservation and queues another attempt. It does not consume the Major firing, create a history row claiming a colony exists, or transfer half of the package.

The canonical Rush selection also proves that at least one later dominion outpost can be placed. This does not transfer that second state on day one. The reason is specific: the mandatory succession war needs two territorial camps. The later outpost is a real baseline crossing with its own news, people, state loss, army, and Earth response. It is not a silent repair of the map.

## Existing Earth residents

A crossing brings settlers, administrators, and military personnel. It does not remove the state's original population. The arrival record distinguishes new people from Earth residents and from already existing soldiers. Reinforcement credits cannot be created merely by changing a country's name or government.

The founding state receives the colony's core to represent its settled administrative center. The former owner's core remains. This does not authorize all Earth residents to become elves, giants, demons, or ent recruits. Creature reinforcement uses the society's own typed pool. Earth volunteers use separate human templates.

The default civilian arrival groups are proposed at 50,000 for an ordinary human colony, 25,000 for a compact elven or mixed specialist colony, 10,000 for a large-creature society, and 100,000 for the canonical Rush Kingdom. Direct-lord realms use their own packages. These are settlement headcounts, not division strength. A giant formation never counts as thousands of ordinary human bodies because it occupies a division slot.

An external-arrival adapter creates the proven new settlement population once. Movement of existing Earth residents belongs to the shared Migration transfer owner. Migration conserves people between states and records any route deaths as part of the same debit. ZIN must not imitate that transfer by subtracting manpower and adding population elsewhere.

### Resident policies

| Policy | Availability | Immediate choice | Long-term result |
| --- | --- | --- | --- |
| Coexistence | All ordinary baseline societies | Preserve local homes, courts for Earth civilians, and separate military recruitment. | Slow integration, stable trade, and negotiated mixed settlements. |
| Common citizenship | Friendly human states and eligible elven routes | Commit administrators, language schools, and a 180-day integration mission. | Earth volunteers and deeper economic participation, with equal civil protection. |
| Separate administration | Neutral, clan, and isolationist routes | Recognize local civilian communities but keep political and military institutions separate. | Lower foreign recruitment and fewer cultural disputes, with limited shared institutions. |
| Military administration | Authoritarian and hostile routes | Requisition supplies and impose curfews with an explicit legitimacy cost. | Faster military support, resistance incidents, and weaker recognition prospects. |
| Forced removal | Explicitly hostile routes only | Create a real displacement request with a legal destination or trapped-population outcome. | Lost workforce, diplomatic consequences, and responsibility for harm. It cannot erase residents. |

A society cannot oscillate between coercion and integration to harvest both rewards. Policy changes retain their previous conduct and obligations. A rights-restoration route repairs relations over time, but does not erase deaths, forced displacement, or betrayal evidence.

## Settlement missions and the first economy

Every country receives the same three practical tasks, expressed through its own institutions and art: supply the settlement, establish a lawful or coercive administration, and choose a relationship with the former owner. Only one of these is a timed mission at a time. The other two are focus and decision choices.

The first 120-day provisioning mission requires a functioning supply connection to the capital, positive support-equipment reserves, and one completed domestic administration focus. A maritime colony also requires a functioning home port. The mission is not failed merely because the colony is on an island. Actual isolation, port damage, convoy shortages, or an enemy blockade must be present.

Success ends the temporary homeland supply bridge and replaces the founding spirit with the settled version. Failure leaves the country alive, reduces reinforcement throughput by 25 percent, and opens a 90-day repair mission. It does not delete the army or create a free permanent supply exemption. Friendly Earth aid can satisfy the physical shipment requirement and earns a durable diplomatic receipt.

Starting industrial packages are homeland-established workshops and construction capacity, not stolen duplicate factories. The settlement ledger distinguishes inherited buildings from newly introduced capacity. The country profiles specify the intended minimum usable economy. A selected state with more industry keeps that real advantage. A small state is not filled with free factories beyond its supported building slots.

A country that cannot fit its planned permanent industry receives a declared temporary construction-capacity effect within its existing settlement spirit while it completes real construction. It cannot receive the same permanent factories later without removing that temporary substitute. This capacity bridge is a planned mechanical representation of the crossing, not an engine feature claimed to have been tested.

## Neutrality is a posture

Neutral colonies may trade, negotiate, defend themselves, sign non-aggression agreements, receive recognition, and cooperate on civilian projects. They do not automatically enter an ordinary Earth faction or launch offensive wars. A faction such as the early Lost Cause can organize colony defense before Earth governments are eligible for full membership.

A hostile culture can still begin neutral. Dondor must first decide that conquest serves its interests. A demon host can spend its early period securing food, shelter, and command. Its appearance is alarming, but its first arrival is not automatically a declaration of war.

External policy has five qualitative states: neutral, defensive compact, limited intervention, regional expansion, and Reckoning belligerent. These are labels tied to actual route permissions, not another public numerical meter. The focus or decision that changes posture must identify the permitted action and its diplomatic consequences.

A peaceful country has late content: protected settlements, allied reinforcement, refugee protection, mediation, reconstruction, or a defended neutral league. Remaining peaceful does not mean running out of focuses while waiting for a global war.

## Provocation and defensive peace

Provocation is an attack on the colony's sovereignty. Declaring war or committing an explicit expulsion, seizure, or removal operation qualifies. Recognition refusal, border fortification, observation, ordinary intelligence gathering, and declining a trade agreement do not qualify by themselves. Covert sabotage becomes provocation only after a real attributable operation and a route-defined public escalation, not because an AI attitude score is low.

When a defensive war begins, the colony offers peace immediately. The offer demands every state owned by that aggressor which directly borders any state currently owned by the colony. The term uses current ownership, not the colony's cores, founding footprint, occupied territories, or imagined cultural homeland.

For colony-owned state set C and aggressor-owned state set A, the demand is all states in A with a legal land-state adjacency to any member of C. States controlled but not owned by the aggressor are not included. Sea distance, naval-region adjacency, and the aggressor's capital do not create an alternative demand. If the result is empty, the offer is white peace.

The proposal is valid for 10 days. It stores the exact list shown to the recipient. Acceptance revalidates that list and the war relationship. If ownership or the colony border changed, the offer is withdrawn and replaced with a newly displayed offer. It must never accept a smaller displayed demand and silently transfer a larger recalculated set.

An accepted offer transfers the demanded ownership, ends the applicable bilateral conflict through the supported peace helper, and registers the new states for settlement. Third-party occupation is not silently converted into colony control. An ongoing independent war with that occupier keeps its own diplomatic problem. The offer cannot unilaterally end unrelated wars or annex an aggressor's allies.

A refused offer does not repeat every day. The next ordinary offer can appear after 90 days, or after a material border change with at least 30 days since the previous refusal. Recalculate from the new borders. A player cannot open repeated negotiations without a new offer receipt, and repeated acceptance of the same transaction cannot transfer or core a state twice.

Aggressor status belongs to the particular war episode. A country defending against a colony's later offensive war is not punished for that defense. Volgan and Afrit use their route objectives in offensive wars. They do not receive a universal neighboring-state surrender button against every opponent.

## New territory after settlement

The colony can hold a transferred or conquered state without immediately making it a core. A 180-day settlement mission establishes supply, administration, and the selected resident policy. Full integration normally takes another 180 days and requires uninterrupted control, an accepted administration route, and no unresolved displacement crisis.

Coexistence and common-citizenship routes can create integrated states. Separate-administration routes retain an autonomous state relationship. Military administration can extract resources sooner but does not receive instant cores. A claim, occupation, recognition agreement, and core are distinct outcomes.

Hiloron giants can speed actual construction, Kilinti ents can defend forest infrastructure, and goblin engineers can repair captured equipment. None of these creates population or removes the previous state's history. A colony that loses a state loses its state-bound benefit. It retains evidence of former settlement and any surviving people through the appropriate ledgers.

## Repeated arrivals and crossing traffic

The event schedules its own bounded arrival check. The proposed baseline interval target is a 180-day MTTH, reduced by dangerous-crossing progression and current instability. It is not an exact promise that a colony appears every six months. The implementation must use the verified timing adapter and probability audit to evaluate its distribution.

| Active stage | Ordinary arrival MTTH target | Soft active-colony ceiling |
| --- | ---: | ---: |
| Baseline | 180 days | 15 |
| Dangerous Crossings | 150 days | 20 |
| Greater Societies | 120 days | 25 |
| Great Lords | 90 days | 35 |
| Reckoning | 60 days for eligible wartime support | 45 |

The ceiling limits ordinary sovereign arrivals. It does not delete living countries, prevent refugees or unit reinforcements, or block a required unique actor whose explicit story transaction has been admitted. Canonical Rush outposts count toward the ceiling and reserve their capacity early. Unique-lord setup and manual scenarios reserve their complete footprint before consuming common slots.

A province is not a country slot. Available carrier capacity is determined by a current collision and reservation audit. The numbers above are design targets, not a claim that 45 unused tags already exist.

Shared focuses can request another crossing after a 180-day cooldown. The requester chooses a related society family, not an arbitrary Earth state. The allocator retains random weighted placement. An accepted charter can influence whether the new settlement is a subject, ally, or independent partner, but it cannot guarantee political obedience when the society's route rejects it.

Two same-origin colonies can merge only through a real political agreement or conquest. A negotiated merger preserves the people, stockpiles, unit provenance, and obligations of both. No second arrival army is awarded. A federation can retain multiple sovereign members and coordinated decisions without creating another tag for the same population.

## Public values and ordinary resources

Rush Unity and Afrit's Influence are the only new persistent public numerical meters in the event. Other countries use ordinary political power, command power, equipment, manpower, factories, supply, war status, and qualitative route states. A country can see its reinforcement allotment as a practical military capacity, but there is no universal mana currency, portal currency, soul shop, or diplomatic trust meter.

There are at most four spendable cost types in a single ZIN decision surface: political power, command power, a named equipment shipment, and committed civilian construction capacity. A convoy shipment is one equipment cost, not an additional abstract resource. Command-power costs stay at or below 60. Country-specific choices must mostly change institutions, obligations, territory, units, or relationships instead of selling small bonuses.

Each country uses no more than three simultaneous ZIN national spirits. Normally these are one society identity and one political or settlement condition. Glo occupies the third slot when held. New stages replace the relevant spirit instead of accumulating a row of permanent icons.

## What this event does not do

It does not replace the Earth map with the supplied ZIN maps. It does not turn all monsters into one country. It does not create a dragon country, another Edvoid, a second Afrit, or a second Castle of Yeldenne. It does not grant an army every day, bombard all enemies with free nuclear strikes, or take an unrelated capital when the border demand is empty.

The supported campaign remains a collection of countries with histories, choices, armies, costs, and consequences. Their common origin eventually matters, but it does not make their early politics identical.
