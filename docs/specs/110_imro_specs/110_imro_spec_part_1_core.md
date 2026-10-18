# IMRO

IMRO begins as a clandestine Macedonian independence movement. Its cells need people, weapons, safe routes and a political reason for civilians to trust them. A successful revolt creates a country with difficult choices about citizenship, neighbouring claims, foreign patrons and the future of revolutionary power. That country can become the centre of a Balkan network, then inspire a worldwide revolt against subject rule. At extreme Chaos, a faction within the movement can corrupt its founding slogan into a doctrine that demands the death of every human being, including its own adherents.

The playable promise is a progression from a vulnerable local organisation to a country whose choices can change the world. Each scale has a complete outcome. A contained uprising is a resolved event. An independent, peaceful Macedonia is a successful campaign. A Balkan federation and a decentralised worldwide liberation coalition are substantial late games. Human extinction is the exceptional terminal route, with an active campaign that other countries can stop.

## Identity and reading order

| Field | Design requirement |
| --- | --- |
| Event identity | Event 110 IMRO, original catalog identity 115 |
| Catalog class | Minor Fire-Once, To Be Reworked, opening Chaos level 1 |
| Cluster | Liberations, Severe member |
| Main player roles | Controller of affected territory, IMRO-led Macedonia, foreign sponsor, liberated subject, former master, independent supporter, surviving opponent of the terminal regime |
| Starting geography | A verified installed-map Macedonian territorial set under foreign control |
| Fire-once meaning | One originating movement transaction and one worldwide Freedom or Death declaration cohort. Persistent play, defeat, negotiated settlement and internal leadership changes belong to those transactions |
| Public custom values | Organisation, Mandate and, after the global Front appears, Front Authority |
| Named evolutions | Balkan Revolutionary Network, Freedom or Death, Freedom AND Death |
| Terminal rule | Chaos strictly above 1000 plus the specified surviving-country, prior-liberation, power and commitment conditions |

All route names, anchor-group labels, action labels, achievement labels and asset descriptions in this package are **working design labels, not final localisation**. IMRO, National Liberation Front, Freedom or Death and Freedom AND Death retain the names supplied in the brief. Final prose must be written during implementation from the directions here. The specification supplies no pasteable event descriptions, quotations, button jokes, song selections or finished localisation.

Read the underground and country parts first, then the focus architecture. The Balkan and global parts explain how the event grows. The two slogan parts define different systems and must be read together. The actions part owns common numerical tuning and AI policy. Presentation and achievements define the complete visible result. The integration and research handoffs record implementation contracts, evidence and limitations separately from the design.

## The campaign at each scale

| Scale | Main question | Player decisions | Distinct endings |
| --- | --- | --- | --- |
| Underground | Can the movement survive discovery and acquire real support? | Quiet organisation, arms procurement, civic outreach, sponsor terms, timing of the revolt | Dismantled cells, enforceable autonomy, premature rising, prepared rising |
| Uprising | Can armed independence survive a stronger controller? | Defend a viable homeland, protect civilians, negotiate recognition, trade secrecy for outside aid | Defeat, negotiated independence, independent military victory, externally dependent settlement |
| Country building | What replaces clandestine command? | Constitution, civil administration, communes, federal institutions, professional forces, production and territorial policy | Stable plural republic, anarchist confederation, socialist federation, sovereign revolutionary state, patron-aligned government |
| Balkan network | Can solidarity survive conflicting local goals and patrons? | Support distinct movements, mediate overlapping claims, expose foreign interference, accept or refuse joint operations | Resilient regional association, negotiated federal compact, fractured network, sponsor capture |
| Worldwide liberation | Can every former subject defend its new independence? | Master acceptance or restoration war, mutual aid, regional settlements, coalition charter and command mandates | Different local victories, defeats and settlements within one world movement |
| Radical evolution | Can IMRO's revolutionary authority be captured and turned against its own purpose? | Resist the takeover, accept radical rule, secure or reject central command, complete conquest focuses | Defeated radicals, isolated dictatorship, pre-lock world conquest campaign, qualified terminal commitment |
| Terminal campaign | Can humanity stop an exterminating human regime? | Territorial resistance, protection and evacuation, defections, attacks on the regime's command and administration | Regime destroyed and campaign stopped, or verified extinction including IMRO's own population |

## The three values

**Organisation, 0 to 100**, represents the movement's capacity to organise and sustain operations. It comes from functioning cells, actual arms deliveries, retained cadres, secure administration and reliable logistics. It falls when cells are exposed, forces are exhausted, depots are lost or commands are severed. It does not represent a second manpower or equipment pool. After independence it measures the institutions connecting local organisation to the state and, later, to the network.

**Mandate, 0 to 100**, represents consent for IMRO's political leadership. Civil protection, credible reforms, respected settlements and successful self-government improve it. Collective punishment, broken guarantees, predatory requisitions and interference in another people's independence reduce it. High resistance against a controller can aid mobilisation without automatically granting high Mandate to IMRO. These are separate relationships.

**Front Authority, 0 to 100**, appears only after the worldwide Front exists. It measures IMRO's actual capacity to direct that coalition. It requires member consent or coercive command commitments and real contributions and reach. Nominal membership, a cosmetic faction title and surviving as the last member do not create world leadership. The authority calculation and terminal safeguards are defined in the slogan parts.

These values are state, not currency. Decisions cannot buy units by spending Organisation or pay for civic reform by spending Mandate. Costs use real resources and the effects change the values. Sponsor relationships, exposure, constitutional crises, command delegation and radical capture use specific qualitative conditions and receipts. They do not introduce a fourth or fifth hidden public meter. Native Chaos, resistance, compliance, population, manpower, equipment, political power and mission time retain their existing meanings.

## Ordinary progress and evolutions

The underground, revolt, peace negotiation, independence and constitutional settlement are ordinary event progress. They do not consume evolution slots. Independence never requires reaching a later Chaos tier.

| Evolution | Proposed unlock tier | Active-event condition | Evolved opening when IMRO has not fired | What changes |
| --- | --- | --- | --- | --- |
| Balkan Revolutionary Network | Chaos 200 or higher | Surviving organisation and a viable foreign contact, normally after 180 days of independent survival or a sustained underground exile network | Initial sponsors and contacts may already be linked to a regional network. The Macedonian opening still needs an eligible territory and a real uprising or settlement | Distinct regional partner play, joint aid and patron conflict |
| Freedom or Death | Chaos 400 or higher | Independent IMRO-led Macedonia has survived 180 days, Mandate at least 55, a credible outward liberation policy, and at least one existing subject in the frozen cohort | A more internationally connected movement begins locally. It cannot release the world before establishing and sustaining an independent Macedonia | One simultaneous worldwide subject breakaway, global Front, master responses and settlements |
| Freedom AND Death | Chaos 800 or higher | Independent IMRO-led Macedonia survives and the worldwide Freedom or Death transaction completed. A radical political contest becomes available | The opening may contain radical doctrine and a warning of its appeal, but cannot skip independence, the global uprising or the contest | Takeover route, changed institutions, coalition rejection and world-conquest focus groups |

The 200 and 400 thresholds are proposed balance constants introduced by this design. The brief fixes 800 for the radical evolution and strictly above 1000 for the possible world-end lock. There is no invented 600-tier evolution and no automatic world-end activation at 800 or 1000. An evolution remains a historical unlock if Chaos later falls, while ongoing strength calculations use current conditions. The terminal commitment rechecks current Chaos above 1000 immediately before it commits.

Evolution activation, focus availability and a changed title grant no Chaos. Actual uprisings, failed containment, expanded destabilisation and exceptional power gains use the guarded impact map. A movement cannot manufacture its own terminal eligibility by repeatedly opening its decision category.

## Outcome promises

The controller has a credible containment game before the rising. Autonomy must create obligations and relief that the player can inspect, and it must be possible to honour it. Suppression can work through intelligence and targeted arrests without forced mass atrocities. Indiscriminate repression is a costly alternative with civilian consequences and political backlash, not the only controller action.

Macedonia has several serious constitutional paths. Anarchism changes command, production, political consent and foreign relations. Federalism creates negotiated relationships among sovereign partners. National revolution can remain independent of sponsors. Patron alignment buys immediate help at the price of dependency. None is a disguised obligation to become the terminal regime.

Every country that is a subject at the worldwide declaration snapshot becomes independent, including a human-controlled country, an unusual ideology, a subject of another subject, and an eligible country already fighting its master. Existing independence is never removed to create a more dramatic opening. All members enter the National Liberation Front organisation, which remains coherent even where existing game factions or nested master relationships make a single game faction impossible.

Each former master chooses whether to recognise the independence of all of its snapshot subjects and exit the corresponding restoration conflicts, or continue fighting. A subject that was also a master makes that choice for its own former subjects. Regional peace does not end the Front elsewhere. The peace implementation must preserve unrelated wars.

Freedom AND Death is a fictional corruption. The regime remains human and its civilian population remains part of the existing population and Deaths systems. Its campaign consumes resources, territory, institutions and time. Other countries can stop it. Its final victory requires that every surviving human representation, including the regime's own, be exhausted through truthful accounting. An empty manpower pool, total capitulation or a world conquest flag is insufficient.

## Connections that change play

| Connection | Incoming effect on IMRO | Outgoing effect and duplicate guard |
| --- | --- | --- |
| 095 Occupation Revolt | Qualifying resistance and a real revolt can reveal contacts, experienced cadres and a weakened controller | One territory and movement receipt decides whether IMRO adopts, reinforces or coexists with that revolt. It never spawns a second duplicate army from the same mobilisation |
| 106 Resistance | Current resistance and recorded repression affect recruitment, warning time and discovery | IMRO actions update the shared resistance system through its owner. They do not create an independent copy of the resistance score |
| 006 Independence Wave | An already released Macedonia is a living country with existing route content. Other released nations are possible voluntary supporters | Preserve existing sovereignty, characters, divisions, flags and tree progress. Reuse compatible Macedonian institutions and add IMRO content through guarded integration |
| 063 End Subject Status | A country already freed before the snapshot remains outside the compulsory breakaway cohort | It may join or support the Front voluntarily. A subject released during the transaction is reconciled by identity receipt without a second release or declaration |

Connection identifiers follow the user's current catalog brief. The historical catalog and pinned repository do not agree with all of them. The integration handoff owns migration and exact runtime hook discovery so this design cannot accidentally attach IMRO to an unrelated event.
