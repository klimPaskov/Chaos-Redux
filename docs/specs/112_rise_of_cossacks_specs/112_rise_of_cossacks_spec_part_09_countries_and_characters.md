# Part 09. Country packages, characters, identity, and diplomacy

## A complete playable country

The rising creates a country immediately.
The country must have a valid owned and controlled state, a usable capital, a government led by an ataman, a flag and map color, ordinary diplomacy, a sustainable native army, research, production, laws, a loaded focus tree, and clear recovery actions.
The package cannot rely on the player knowing console commands or receiving a later hidden setup event.

A host is an institution and a military community.
Its nationality, language, religion, service status, and political program can overlap without being identical.
The country package must preserve that distinction.
A local host does not automatically become the government of every nearby Russian, Ukrainian, Belarusian, Caucasian, Kazakh, or Tatar population.

All country and office names in this specification are working labels.
Runtime tags, cosmetic IDs, character IDs, event numbers, and scenario IDs remain subject to the namespace crosswalk.
This file does not allocate them.

## Carrier plan

### Existing Don and Kuban carriers

The current tag registry declares DHC and KHC as existing Don and Kuban carriers, and their country histories identify them with Event 005 Soviet Collapse.
The [DHC history](../../../history/countries/DHC%20-%20Don%20Host%20Emergency%20Circle.txt) assigns capital 218 and three research slots, then creates one of three named leaders from a random list.
The [KHC history](../../../history/countries/KHC%20-%20Kuban%20Host%20Provisional%20Council.txt) assigns capital 234 and three research slots, then creates one of three named leaders from a random list.
The current [tag declarations](../../../common/country_tags/chaosx_countries.txt) are DHC at line 29 and KHC at line 30.
These source facts do not establish current-map eligibility or authorize overwriting either carrier.

The country histories include randomized unsupported named leaders.
The newer grounded identity requirement prevents Event 112 from treating those names as approved historical people.
A coordinated 005/006/112 admission adapter must resolve that shared identity problem.
It should use an authentic institution or a verified available person and preserve the original owner's legitimate content.

An already living DHC or KHC keeps its country, armies, characters, diplomatic history, focus progress, and meaningful tree.
Event 112 can contact it, negotiate a charter, receive volunteers, or accept it as a partner.
The event cannot reinitialize it, replace it with a duplicate tag, or silently transform it into the principal rising.

A dormant correctly admitted DHC or KHC can become the initial host when the selected state and identity match.
The opening must preserve relevant inherited technology and country setup where that is intentional.
Any inherited grants that would duplicate the Event 112 opening are removed or bypassed through the coordinated adapter before activation.
The audit must inspect both entry paths.

### Generic carrier pool

The design needs one principal generic carrier and up to three simultaneous additional release slots for The Hosts Answer when existing legitimate identities cannot supply them.
This is a maximum concurrency requirement, not permission to preallocate four arbitrary tags.
The actual implementation first audits vanilla, project, Workshop, and other active local mod definitions.
It then reuses safe existing identities or reserves genuinely free tags through the shared registry.

A carrier slot is a technical resource.
Its public identity is a specific approved host appropriate to the selected state.
It cannot masquerade as a different living country whose people, history, or flag the slot does not own.

The founding carrier can use the generic New Frontier Host identity when no historical host mapping applies.
That is an explicitly fictional modern rising organized through an authentic ataman and host institution.
It is not a fabricated historical ethnic group.
Its later adopted traditions are earned through contact and political agreement.

A released additional host remains a distinct country unless it later agrees to merger.
A global cap of four simultaneously event-created independent host countries keeps The Hosts Answer bounded.
Existing independently alive host partners do not consume a release slot, but they remain in the bounded participant registry and are subject to opportunity and UI limits.

A dead or annexed carrier is not immediately recycled into a new unrelated community.
Its surviving characters, claims, exile government, commitments, and receipts must first be closed or preserved through an explicit identity transition.
The initial global Fire-Once flag remains spent.

## Country setup matrix

| Surface | New generic principal host | Admitted existing dormant carrier | Already living potential partner |
| --- | --- | --- | --- |
| State and capital | One owned and controlled founding state with a validated deployment and capital province | Same physical rule, with compatible existing identity and capital handling | No forced state transfer or capital change |
| Government | Provisional ataman mandate with an authentic institutional fallback | Grounded identity adapter preserving the shared owner contract | Existing government remains |
| Political membership | Temporary service coalition with all later constitutional choices open | Preserve legitimate existing distribution unless the admission contract explicitly changes it | Existing politics remain until a real treaty or reform |
| Army | Dynamic opening receipt and small native recipes from part 03 | Reconciled dynamic opening without double grants | Existing units remain under their owner |
| Technologies | Bounded conventional prerequisites for the actual starting equipment and templates | Preserve legitimate history technologies and add only missing approved prerequisites | No technology changes merely for contact |
| Research slots | Two | Preserve legitimate existing count, including a documented three-slot carrier | Unchanged |
| Industry | Actual buildings in the transferred state and the one-time workshop route if eligible | Actual inherited state buildings and an audited bridge if needed | No copied buildings |
| Laws | Valid ordinary civilian and military laws with an explicit emergency service basis | Preserve compatible lawful setup or apply the accepted admission transition | Unchanged |
| National spirits | Institutional and Military opening slots, Economic only for a relevant actual crisis | Reconcile existing event-owned ideas without duplicate systems | No removal of another owner's ideas |
| Focus tree | Dedicated host tree with founding-tradition and government filters | Adapter preserves or composes meaningful existing tree content | Existing tree remains with bounded diplomatic integration |
| Flags and color | Approved generic or regional identity with all native ideology bindings | Inspect and preserve approved existing assets where appropriate | No forced flag change |
| Diplomacy | Explicit relationships with legal owner, controller, neighbors, and actual patrons | Same, with prior valid relations preserved | Only signed agreements alter relations |
| Reinforcement | Native recruitment, production, training, purchase, and finite actual transfers | Same with inherited capabilities | Own existing economy |

## Government and starting politics

The initial head is an ataman acting under a provisional host mandate.
The game must represent an immediately functioning office even when no defensible named historical individual is available.
The office can be shown through an authentic institutional representation and a sourced symbol.
It must not invent a face, biography, or identity and call it historical.

The default political distribution for a newly defined generic carrier is a proposed neutral service coalition.
A starting tuning baseline is 50 percent nonaligned, 25 percent democratic, 20 percent communist, and 5 percent fascist.
These are gameplay tuning values, not a historical census or a claim about all Cossacks.
An admitted existing carrier preserves its approved setup unless the transition explicitly establishes a different government.

The opening government uses nonaligned political mechanics where that matches the installed ideology system.
The later civilian, confederal, socialist, professional, sponsor-service, and crown routes change the relevant institutions through actual decisions.
Ideology changes need ordinary political consequences and full flag and party coverage.
A route's descriptive title cannot conceal a government that behaves differently in the engine.

Party names require authentic period institutions or carefully framed descriptive political groupings.
The localisation phase must not invent a named historical party, person, or association to fill a slot.
A descriptive group is clearly a political tendency of the new alternate history state.
It is not presented as an archival organization.

Starting stability and war support should support a precarious but playable state.
The proposed generic baseline is 40 percent stability and 55 percent war support, adjusted only by an explicitly accepted opening variant.
The two host meters are not continuously converted into matching native values.
Specific political events can change both when justified.
That avoids counting the same outcome twice through a hidden conversion.

Normal mobilisation, economy, trade, officer, and occupation laws remain available under their ordinary rules.
The design does not permanently lock the country into a special event-only law set.
Any emergency override has a visible reason, duration, and removal path.

## Grounded character roster

The initial researched candidate roster is deliberately small.
It provides meaningful candidates while preserving an authentic institutional fallback.
A historical person can hold more than one role only where the actual biography supports those roles and the existing game character ownership permits it.
The event does not manufacture extra generals, admirals, scientists, or advisors from a portrait.

| Person or institution | Historical basis | Proposed design role | Availability and duplication gate | Presentation state |
| --- | --- | --- | --- | --- |
| Acting ataman office and host circle | Authentic Cossack command and council institutions | Default functioning head and succession fallback | Must use the correct host institution and a non-person representation where no named candidate is sourced | Institutional source-based representation, no invented face |
| Luka Bych | Kuban civilian political leadership and interwar educational work in Czechoslovakia | Optional civilian constitutional and administrative candidate for Kuban content | Verify period availability, existing country ownership, and return agreement | Named source portrait required |
| Mikhail Getmanov | Kuban military career and documented interwar exile | Optional returning military cadre or commander after an appropriate contact | Verify campaign availability, actual role, current ownership, and return route | Named source portrait required |
| Pavlo Skoropadsky | Former hetman and interwar émigré political activity | Optional invitee for the modern Ukrainian hetmanate settlement | Audit existing Ukrainian and other character definitions, date, survival, and consent | Named source portrait required |
| Pyotr Krasnov | Former Don ataman and émigré political activity | Optional conservative exile contact or candidate under explicitly compatible terms | Verify existing ownership, date, current political circumstances, and the host's decision | Named source portrait required |

The biographical sources are recorded in the research notes.
Luka Bych's civilian expertise does not automatically make him a skilled battlefield general.
Getmanov's military experience does not automatically make him a scientist or industrial magnate.
Skoropadsky does not become the head of every Cossack host.
Krasnov's later collaborationist record must remain part of the historical context and must not be generalized to all Cossack traditions.

The source for Getmanov is the [Hoover archival announcement](https://www.hoover.org/news/hoover-acquires-memoir-general-md-getmanov).
The sources for Bych and Skoropadsky are their [Bych](https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CB%5CY%5CBychLuka.htm) and [Skoropadsky](https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CS%5CK%5CSkoropadskyPavlo) biographical entries.
Krasnov's record is described in the [Holy Trinity Seminary archive biography](https://archive.hts.edu/findingaids/bio/krasnov_bio.html).
These sources establish biographical context.
They do not clear image rights or determine a game trait.

Additional living historical candidates may be researched during the implementation phase if a concrete content gap remains.
No new named character is approved merely because a historical host has an empty portrait box.
If a proposed person cannot be verified, the functioning office remains available and the route continues.

### Availability across campaign dates

A person who died before the scenario starts is not revived as an ordinary historical leader.
A person who is already alive in the campaign follows the game's actual survival and capture state.
The script must not force a historical death date onto a divergent campaign solely to match a biography.
The exact policy must agree with the existing character owner.

The same person may not simultaneously lead two states or arrive as two separately named transliteration variants.
The audit covers given names, initials, patronymics, surnames, aliases, and existing portrait identity.
A successful invitation transfers or activates the actual accepted character once.
A failed invitation never leaves a second hidden copy.

### Succession

The ataman's death, capture, resignation, or removal opens a finite succession event chain.
The existing charter determines who has authority to choose a replacement.
A council holds an election or appoints an interim office.
A professional service state follows its ratified command succession.
A sponsor-service state checks the sponsor's actual appointment rights.
A regency follows the constitution established in its great-project route.

Succession can reduce Cohesion or reopen a specific mandate.
It does not destroy the country, remove trained units, or reset the opening grant.
If no verified named candidate is available, the authentic institutional office carries the government.
The localisation and portrait state must make that representation clear.

## Focus and technology continuity

A fresh generic host loads the dedicated host focus tree immediately.
The tree must expose the survival, charter, economy, and military groups from the start.
Geographic programs remain discoverable and explain missing contact or territory.
The player must not receive an empty tree while waiting for a later evolution.

An admitted DHC or KHC needs an explicit tree composition decision.
The preferred adapter preserves meaningful Event 005 content and attaches the host programs through a coherent shared or branch structure.
A full replacement is acceptable only after the responsible owner has identified what is being replaced and why it is safe for that entry path.
A living partner never loses its meaningful tree because Event 112 considers a shared federation.

Initial technology is a bounded practical package.
It includes the conventional prerequisites needed to use and reinforce the actual starting infantry equipment and native templates.
It may include appropriately basic support and reconnaissance prerequisites when the actual roster uses them.
The host receives neither the source country's entire research tree nor future technologies.

The research and industry development rules in part 06 provide growth.
A technology merge belongs only to a full sovereign merger with an explicit continuity policy.
An ordinary alliance, volunteer detachment, port treaty, or tradition adoption never invokes a generic technology union.

## Diplomatic actors and responses

The opening records both the legal owner and the controller of the selected state.
When they are the same, one country receives the displaced-authority response.
When they differ, the military occupier and legal claimant receive separate relevant choices.
The occupied-state variant must remain disabled until its engine war and ownership behavior is proven.

The displaced authority can negotiate a service relationship, recognize a limited settlement, or pursue a punitive military path.
The host can accept terms, make a counteroffer, or defend its independence.
The actual native war, peace, guarantee, access, or subject action must be validated.
A report option cannot claim a peace while the engine retains an unresolved war.

Neighbors assess a specific proposal.
They can grant access, trade, refuge, equipment, recognition, or a limited defense agreement.
Their response depends on current borders, wars, ideology, rival claims, capacity, and existing commitments.
A distant ideological friend without a route cannot deliver a guaranteed stockpile.

No existing state is treated as an empty historical label.
Ukraine, Russia, the Soviet Union, Turkey, Mongolia, Crimean or Volga polities, Caucasian states, and eastern partners keep their own agency.
The host's claims and restoration ambitions create negotiations and rivalries.
They do not authorize automatic absorption.

## Identity transitions

### Regional identity

A generic founding host can adopt an appropriate regional identity after its actual institutions and geography justify it.
The transition requires a verified mapping and the absence of a conflicting living claimant.
It changes presentation and relevant contextual content.
It does not create a second country, reset the army, or reaward the founding core.

Adopting another military tradition alone does not change the national identity.
The player can learn plastun methods while remaining a Don host.
The public name must reflect government and territorial scope without falsely claiming every related host.

### National identity

Great-project identities are governed by part 05.
The carrier normally remains the same country through an accepted cosmetic and institutional transition.
An actual merger with a living national country uses a separate owner-approved continuity transaction.
That transaction reconciles the two countries rather than selecting whichever tag is easier to script.

A new capital needs a valid owned and controlled state, an actual province, and a workable supply basis.
The old capital remains a meaningful host center or regional seat where appropriate.
Moving the capital grants no automatic infrastructure, buildings, population, or equipment.

### Flags and map color

Part 12 defines twenty possible national identity families with the native ideology bindings and a small number of explicit constitutional alternatives.
Only actual country identity changes use those flags.
A treaty network, diaspora contact, or invited community does not replace the receiving country's national flag.

Historically grounded flags need exact source geometry and symbolism research before production.
An invented alternate history flag must have a clear institutional rationale and be recorded as fictional.
New flag production follows the current ImageGen and deterministic native-size processing route.
Existing approved flags can be reused after consumer and rights inspection.

Map colors must be distinguishable from neighboring and potentially simultaneous hosts.
Suggested generic frontier color is muted blue-green, with regional variants coordinated around the actual map.
Exact RGB values remain part of the collision and visual review.
A decorative flag color does not determine map visibility.

## Defeat, annexation, and return

The global event remains fired after the principal host is defeated.
The country's state, people, equipment, and characters follow actual war and annexation results.
There is no hidden automatic resurrection.

Surviving host institutions can negotiate integration into another host, refuge, or a supported exile state.
Any transferred units and population use the measured receipts.
A defeated unit cannot later appear intact as a volunteer cohort.
A civilian evacuation cannot be repeated because a cosmetic country name changed.

An annexing country receives bounded choices over local service rights, demobilization, and settlement.
A respected agreement can reduce the relevant local dispute and close Event 112's crisis ownership.
A broken agreement can leave an appropriate resistance or political legacy where supported.
The event cannot create a new independent country every time that legacy is checked.

A later restoration is a new political outcome of the surviving community.
It needs an actual return or uprising opportunity under the evolution's finite rules.
It does not reset the root Fire-Once event.
The former original state does not create a second initial reserve.

## Country package acceptance

The package is accepted only when every active host identity has complete history, character, flag, party, law, idea, technology, focus, army, reinforcement, and diplomatic coverage.
The test matrix includes a fresh generic host, dormant DHC, dormant KHC, already living DHC and KHC, an occupied-state candidate, a human switch, an AI host, a missing named candidate, a national transformation, a sovereign partner, a capitulated host, and a restored community.

The exact source map must identify which owner controls every existing carrier and character.
The final implementation must prove that no living country is overwritten and no unsupported historical person is invented.
A country with an incomplete portrait, empty tree, unusable army, or unsustainable reinforcement path is not complete merely because its tag appears on the map.


## Principal-country identities after regional network completion

The optional FL18 Pontic, FL19 Volga-Ural and FL20 Eastern identities use the exact constitutional conversion contract in part 05.
They require the completed full project and first-peace review, 75 Political Power, a 120-day mission, Cohesion and Legitimacy at least 60, actual directly owned and controlled home anchors, a ratified civic mandate and counterpart acknowledgment.
Only the principal's compatible cosmetic identity and current ideology flag change.
No independent partner is absorbed or renamed, and the act creates no tag, core, unit, population, meter increase or repeated formation reward.
Treaty-only completion preserves all existing flags.
The country and flag crosswalk must distinguish these conditional identity consumers from the network agreement itself.
