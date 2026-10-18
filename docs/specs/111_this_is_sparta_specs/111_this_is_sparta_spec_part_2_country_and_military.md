# Part 2: Country creation and military growth

This is design specification for Event 111, `This is SPARTA!!!`, formerly catalog entry 116. Every new label and semantic identifier in this document is an authoring reference, not finished localisation or an installed game identifier. `SPARTA_TAG` remains a role placeholder until the complete installed-content identity audit assigns a legal tag. The five user-supplied campaign names remain unchanged.

Read with [the focus architecture](111_this_is_sparta_spec_part_3_focus_routes.md), [decisions and settlements](111_this_is_sparta_spec_part_4_decisions_and_settlements.md) and [presentation and assets](111_this_is_sparta_spec_part_7_presentation_and_assets.md). The opening and Age of Heroes contracts govern their respective transactions. This part specifies the country that those transactions must leave behind.

## 1. An independent country on the first successful day

Sparta owns and controls a valid Laconian home state immediately after the founding transaction. Creating its government, transferring its land, setting a capital, providing supply and deploying its returned army are one successful entry operation. A focus may strengthen an existing Sparta. It may not postpone the actual country creation.

The map requires a build-time Laconia state split. The pinned repository geography pass found a Peloponnese state and no indexed Laconia state. That observation does not establish a current installed state or province ID. Implementation must inspect the installed map, define the exact Laconian province subset, allocate a collision-free state ID and reconcile the remaining Peloponnese. Transferring the whole Peloponnese or temporarily assigning province control would change the premise and is excluded.

The split must conserve the original population, resources, buildings and applicable state modifiers across its two results unless a separately documented Event 111 reward changes them. Audit capital and victory-point placement, a deployable land province, coast and port availability, supply hubs, railway links, terrain, building slots and both supported bookmarks. Every state list, map puzzle and compatibility crosswalk must use the new geography. The event remains ineligible until the installed map package can provide these postconditions.

| Country surface | Required result |
|---|---|
| Identity | Independent `SPARTA_TAG`, marked with Event 111 creation provenance and the shared special-country classification. Returned humans remain human for species checks. |
| Starting territory | The new Laconia state. No additional Greek territory is transferred by this country package. |
| Core and dispute | Sparta receives its Laconian home core. Existing Greek claims or cores remain meaningful unless an explicit negotiated settlement later changes them. Other routes award claims or administration rights through their own gates. |
| Capital | A verified province in the real Laconian location. The country must have a legal capital and supply before unit creation. A pre-audited owned Peloponnesian backup is used only if the primary capital is subsequently lost. |
| Government | Joint Spartan royal government with ephors, represented as an institution under `111_identity_joint_royal_ephors`. |
| Country leader | One institutional leader identity representing the joint royal and ephor system. No invented personal biography, invented ancient photograph or generated historical likeness. |
| Politics | A neutral or nonaligned founding alignment, mapped to the installed ideology system. Starting party support describes a contested modern polity and does not create four equal ideology branches. |
| Diplomacy | Relations with the actual former owner, surviving Greece, relevant neighbours and existing foreign powers. No inherited faction, guarantee or diplomatic immunity merely because a new country has appeared. |
| Existing actors | Greece, Macedonia, Persia and other countries retain their tags, leaders, packages and human agency. A later ordinary conquest can change their sovereignty. This event does not overwrite their identities at birth. |
| Player control | The opening offers control according to the shared event contract. The country package is identical in its material guarantees whether AI or human controlled. |

The institution has a complete flag, map colour, adjective and party-name direction, portrait source plan, capital plan, historical naming brief and diplomatic identity. Final strings and images belong to the localisation and asset handoffs. If a later political settlement changes institutions, it replaces the leader identity and any specifically authored matching flag variant through a documented country identity state. An earned route identity owns the national flag. A political change cannot restore an obsolete unformed-Sparta flag, and the design does not require every possible institution and route combination to receive a separate flag. It does not create a second Spartan tag.

## 2. A viable opening that reflects the campaign

Opening strength uses four anchors and bounded interpolation. A regional threat evaluation considers actual hostile or imminently hostile forces that can reach Laconia, their modern equipment and air support, the former owner's war position, available supply and the current campaign date. Chaos and date can influence the band. Neither alone grants a powerful late army in a quiet region.

| Anchor | Returned brigades | Contemporary local brigades | Civic Settlement | Military Adaptation | Effective starting stability | War support |
|---|---:|---:|---:|---:|---:|---:|
| Weak regional opposition | 2 | 1 | 25 | 10 | 45% | 35% |
| Normal opening | 3 | 2 | 25 | 15 | 40% | 45% |
| Severe immediate opposition | 5 | 3 | 20 | 20 | 35% | 55% |
| Late modern opposition | 6 | 4 | 20 | 25 | 35% | 60% |

Each returned brigade represents 2,000 people. Each contemporary brigade has a ceiling of 3,000 people. The contemporary local brigades are ordinary native infantry, not the custom modern Spartan cadre family. They receive no returned-origin exemption. These are manpower requirements, not assumptions about native battalion manpower. The implementation audit chooses legal templates with those totals or records a minimal necessary adjustment. Formation counts and manpower conservation are explicit exceptions to the preference for round modifier tuning.

The returned host therefore contains 4,000, 6,000, 10,000 or 12,000 people at the anchors. They are added once as the actual supernatural arrival of ancient humans. Local brigades draw from the recruitable modern population under the chosen law. They can begin as understrength ordinary infantry formations when the population or equipment cannot support their ceiling. A stronger opening never silently creates additional contemporary Greeks.

Interpolation may change a formation's starting strength or choose between neighbouring anchors. It cannot exceed six returned and four local brigades. If supply cannot support an anchor, place a smaller deployable force and retain only the explicitly recorded undeployed part of the same returned cohort for a one-time deployment at a valid local supply point. Do not repeatedly grant supply, equipment or replacement soldiers. A country with no valid initial deployment and supply cannot pass the founding transaction.

The late anchor requires a materially modern regional threat as well as a late campaign. Its ancient soldiers still arrive with ancient equipment. Higher Military Adaptation represents contemporary liaison and faster access to available knowledge. It does not mean the returned host already possesses tanks, automatic rifles or aircraft.

### Native laws and opening resources

The law names below are design selections whose exact installed identifiers and legal triggers must be audited. Effective stability and war support in the table already include the opening spirit effects, so setup must avoid subtracting the same crisis twice.

| Surface | Weak and normal | Severe and late |
|---|---|---|
| Conscription | Limited Conscription, with actual local recruitable manpower conserved | Limited Conscription by default. Extensive Conscription only if its native wartime conditions are met and the emergency cabinet accepts the cost. |
| Economic law | Civilian Economy | Early Mobilization when legally available. Partial Mobilization is a later decision or focus reward, not an unconditional birth law. |
| Trade law | Export Focus | Export Focus, with later strategic controls available through state-capacity policy |
| Political power | 75 | 100 for severe and 125 for late |
| Command power | 20 | 20 |
| Starting experience | 10 army experience, zero naval and air experience | 10 army experience, zero naval and air experience |
| Fuel | No free strategic reserve. Any transferred local fuel is recorded and conserved. | Same rule. A more dangerous war does not create oil. |

Transferred factories, infrastructure and resources come from the Laconia split. If the resulting state has no civilian factory, founding supplies one bounded civilian workshop as an explicit event-created resource. It is recorded once and cannot be farmed through release or reconquest. There is no unconditional military factory, dockyard, refinery, airfield or railway grant. Early development supplies tools to build the missing facilities.

Modern rifles come from a documented local transfer, a negotiated delivery or a bounded opening allotment. The new allotment ceilings are 500, 1,000, 1,500 and 2,000 basic rifles for the four anchors. Existing equipment transferred from another country is debited from its real stock or formations using an audited transfer method. Existing Greek divisions are not copied. Infantry-equipment targeting can rise to 1,500, 3,000, 5,000 and 6,000 rifles when actual transfers and deliveries permit it, but these are readiness goals rather than additional free grants. All shortages remain visible in normal logistics.

The returned host begins with its own finite equipment allowance of spears, shields and associated field gear. Replacing worn equipment through an artisan production line is allowed. Producing that equipment does not produce more returned people. Initial artillery, trucks, armour, aircraft and combat ships are zero unless an actual transfer or captured asset with a recorded origin exists. Convoys are received only through a real transfer, purchase or the first coastal logistics program. The opening does not spawn a fleet into a state with no functioning port.

## 3. Research, production and technical catch-up

Sparta begins with exactly two research slots. The institution already contains contemporary technicians and civilians, which supports a narrow modern knowledge base. Returned martial experience does not grant industrial or scientific mastery.

| Research stage | Slots after completion | Material and institutional gate | Result beyond the slot |
|---|---:|---|---|
| Birth | 2 | Successful founding package | Basic modern administration can sustain a small research effort. |
| Technical education | 3 | A working civilian workshop, adult training program and Military Adaptation at least 25 | Opens technical instructors, an engineering support program and a bounded research bonus for basic industrial or infantry technology. |
| Research network | 4 | At least three functioning civilian factories across owned core states, a funded domestic laboratory or real foreign research agreement, Civic Settlement at least 50 and Military Adaptation at least 50 | Opens coordinated industrial research and equipment licensing. A revoked agreement suspends its cooperation benefits without removing an earned slot. |
| Late imperial institutions | 5 | At least eight functioning civilian factories, two completed regional administration projects, Civic Settlement at least 65, Military Adaptation at least 70 and a selected route's late institutional group | Supports the final production and logistics programs. No early conquest shortcut grants the fifth slot. |

The weak opening has a complete route to the first adaptation gate. Modern liaison grants 10 Military Adaptation, and a once-only basic firearms familiarization program grants 5. Familiarization is available below 25 and uses a safe site, instructors from the founding contemporary liaison cadre and at least 100 existing modern rifles. It trains existing personnel rather than creating a new intake. The weak opening can therefore advance from 10 to 25 before technical education, cadre intake or conversion is available.

The starting technology basket is explicit by role. Grant the installed basic infantry-equipment technology, the corresponding earliest support equipment, the earliest industrial tooling and construction technologies necessary for local production, and the transport knowledge needed for ordinary land supply. A valid coast and an existing convoy acquisition program permit basic transport hull knowledge. Do not grant doctrine progress, modern combat ship designs, armour, advanced aircraft, special-force technologies or research sharing by default.

For a later opening, compare the local former owner's actually researched infantry and industrial technologies with the current date. The country may receive at most one additional completed tier in each of three baskets: infantry weapons, industrial tooling and construction. A basket must exist locally and be no later than the campaign date. Airframes, tank chassis, naval hulls, electronics and doctrine remain outside this inheritance. Record the selected technologies in the founding receipt. A late world with an impoverished former owner remains technologically difficult.

Missing prerequisites follow the installed technology chain and count against that basket's allowance. If a technology tree replacement makes the role ambiguous, the implementation gate requires a mapping rather than granting the entire former owner's technology set. Equipment stock uses only technologies already granted or a legal captured/licensed equipment route. The player can field foreign equipment without receiving an unsupported national design.

Production starts with returned arms maintenance and any supported native basic rifle line. If no military factory exists, the first arsenal program converts workshop effort into one real local military factory after a 70-day focus and a paid construction decision. It cannot produce rifles before its building is complete. Later choices support domestic standardization or foreign licensing. Standardization reduces long-run production friction after an initial conversion period. Licensing delivers equipment access sooner but depends on the supplier and consumes industrial capacity. Both paths retain a domestic basic-rifle fallback.

## 4. Three spirit slots with complete lifecycles

Every starting and focus-developed national spirit belongs to one of three slots. A stage change replaces the previous stage in that slot. Timed country modifiers also count if they are effectively an additional tree-owned spirit. Rewards should usually change access, units, equipment, institutions or state projects instead of adding another country-wide modifier.

| Slot | Opening stage | Ordinary middle stages | Ordinary mature stage | Failure and recovery |
|---|---|---|---|---|
| Polity | Contested royal and ephor order, with restricted administrative cooperation and a modest stability burden | Renewed dyarchy, representative civic settlement or military supremacy, each with a real constitutional choice | A settled version of the selected institution, replacing its initial penalties with a narrow policy advantage | A broken compact replaces the same slot with a contested stage. Mediation, legal revision or successful institutional reform can recover it. Repression alone does not award civic legitimacy. |
| Military institution | Returned discipline with obsolete command and support practices | Adult Agoge and modern liaison, followed by integrated staff work | A trained modern cadre institution that supports a larger contemporary army | Excessive casualties or failed conversion replace the military stage with an instructor shortage. Equipment restoration and a fresh adult intake recover it. The ancient dead do not return. |
| State capacity | Isolated administration, damaged fiscal coordination and dependence on a small workshop base | Repaired local administration, then a functioning industrial and logistics network | Route-appropriate administrative capacity with a limited production or supply advantage | Overextension replaces the stage with strained administration. Completing regional settlements and restoring supply can recover it without abandoning the selected route. |

The initial tuning envelope is a combined industrial-output burden of about 15%, research burden of about 10% and supply-consumption burden of about 10%, distributed transparently between the applicable slots. Avoid duplicating the same penalties through the public values. A mature slot normally carries one narrow advantage of about 5% to 10% plus its institutional unlocks. There is no permanent nationwide attack modifier added at every military focus. Exact modifier support and final balance belong to installed implementation review.

Civic Settlement and Military Adaptation are bounded from zero to 100. Their gains come from completed material or institutional outcomes. A focus that changes a constitution need not instantly satisfy the settlement it promises. Mythic Strain appears only when Age of Heroes activates. That evolution transforms the appropriate existing slot and adds bounded mythic actors or units. It does not create a fourth spirit.

## 5. Political development

The founding arrangement provides immediate leadership while creating a question about who can govern a modern population. Three directions answer that question. They do not map mechanically to an ideology quota, and none requires a named invented historical person.

**Renewed dyarchy** preserves joint royal leadership and ephor oversight under `111_identity_reformed_dyarchy`. Its internal choice concerns restrained institutional continuity or a stronger royal campaign mandate. The first exchanges slower emergency decisions for reliable civilian cooperation and less disruptive succession. The second permits faster campaign preparation and greater command authority at the cost of more difficult constitutional bargaining. Both must define modern legal status and tax obligations. Retaining hereditary prestige does not provide an unlimited recruitable population.

**Wider citizenship and civic reform** creates `111_identity_civic_assembly`. Its internal choice is between a representative settlement that gives new citizens a durable voice and a service-based settlement that accelerates admission through adult military or civilian contribution. The representative option takes longer to ratify and offers better integration and diplomatic acceptance. The service option supplies trained recruits earlier but faces a later dispute if long-serving residents remain excluded. Military service is not the only route to civic standing. Technical, medical, construction and commercial service must remain meaningful alternatives.

**Military supremacy** creates `111_identity_military_directorate`. It transfers operational authority to an institutional staff while retaining a defined relationship to the returned royal tradition. The internal choice is temporary emergency command with a scheduled civilian settlement or a durable command state. Emergency command has an actual end and a recovery path if the promised settlement is missed. Permanent supremacy sustains stronger mobilization and faster operational preparation, but recruitment coercion and weak civilian institutions constrain Civic Settlement and foreign trust. It does not receive free stability for occupying more territory.

These institutions may support any of the five conquest routes. Their costs and diplomatic effects differ. A league negotiated under a military directorate is harder to sell but remains possible if terms provide real sovereignty. Broad citizenship can accompany an aggressive empire, but its integration promises create obligations in conquered regions. A political reform after route commitment changes domestic institutions without unlocking a second route's claim package.

## 6. Human unit families and personnel conservation

| Family | Mechanical purpose | Equipment and personnel | Growth boundary | Required presentation |
|---|---|---|---|---|
| `111_unit_returned_host` | Cohesive ancient human infantry with formidable discipline and close-terrain value, badly exposed to modern firepower | Finite returned people, dedicated returned arms and field gear | The original arrival cohort only, including any recorded undeployed portion. No normal recruitment queue can create this family. | Original counter, emblem, ancient body and armour, separately generated held spear and shield, assembled movement/combat/death actions and a sourced human voice plan. |
| `111_unit_modern_cadre` | Modern Spartan infantry that carries the training institution into the modern army | Native modern infantry and support equipment, surviving converted returnees or qualified contemporary adult graduates | Academy capacity, instructors, equipment and actual recruitable population. This family is deliberately renewable through modern society. | Distinct counter and emblem, modern uniform and loadout, separately generated weapon props, complete assembled actions and sourced human voice plan. |

The ancient family's initial balance envelope is about 25% higher organization than the audited comparable infantry family, with a small terrain-specific defensive advantage and much lower ranged attack. Start testing around 50% lower soft attack and negligible hard attack, armour and anti-air capability. Their success should depend on terrain, preparation and the opponent's weaknesses. They cannot ignore tanks, artillery, air attack or supply. This is a proposed comparison target, not a claim about tested combat outcomes.

Modern cadres begin near normal modern infantry effectiveness. Their mature distinction should be approximately 10% higher organization and a narrow 5% terrain or planning benefit, paid for with greater training time and support-equipment requirements. They are capped by the Agoge institution and cannot replace the entire army with costless elite battalions. Ordinary infantry, mountain formations, marines, motorized units, armour and artillery remain essential.

The personnel invariant is strict. No transaction may turn one surviving returned soldier into both a modern cadre and additional free national manpower. Conversion removes or changes the original formation, conserves its surviving manpower, transfers a bounded share of experience and accounts for every equipment return. Ordinary casualties reduce the finite cohort. Replacement through the native manpower system must be prevented for the ancient family using an audited supported method. This is an implementation gate, not permission to assume an unverified engine attribute.

Modern cadre admission and every contemporary refill obey the quota in Part 4. Let `O` be actual Spartan-owned deployed ordinary-native land manpower, excluding returned-host and modern-cadre personnel, mythical bodies and their liaison staff, foreign-owned expeditionaries, garrisons, queues and the unassigned pool. Let the academy tier `p` be 0.10, 0.20 or 0.25. The renewable allowance is `Q = max(2000, floor(p*O/(1-p)))`, preserving the intended share of ordinary and non-exempt cadre manpower outside the explicit one-brigade floor.

With `M` actual modern-cadre manpower, `E` certified surviving returned attribution currently within those cadres and `P` all committed contemporary intake or replacement manpower not yet included in `M`, a proposed admission or refill must leave `M - E + P <= Q`. Contemporary recruits and replacements always consume this renewable quota. They never refill an inherited exemption. Conversion moves already certified original survivors into `E` without raising the total original-person allowance.

Gross casualty evidence reduces original attribution. Where mixed casualties cannot identify who was lost, consume original attribution first using `E_i_after = max(0, E_i_before - L_i)`, capped by actual remaining strength. This is conservative eligibility accounting, not an invented identification of individual casualties. Replenishment never raises `E`. Gross loss receipts must be deduplicated, and net strength polling is insufficient when casualties and replacement can cancel each other.

If ordinary losses reduce `Q` below existing non-exempt cadre strength, retain living formations, freeze further admission and refill, and reconcile unused pending commitments through their paid receipts. Never delete troops to force the equation. Supported native control of every automatic reinforcement path and safe attribution or prevention of unobserved refill are explicit enablement gates. No assumed casualty-identity or reinforcement API satisfies them.

If a unit is encircled, disbanded, transferred, captured, merged or unavailable when conversion is confirmed, the decision recalculates or cancels its quote. Converted formations can thereafter receive qualified contemporary replacements only within the renewable quota. Transfers and reorganizations move certified attribution once and cannot recreate a used exemption. The story and military institution survive without pretending that every later soldier is one of the original returnees.

The modern Agoge recruits adults from modern Greece first. Later citizenship and regional settlement programs admit wider populations. Its curriculum includes weapons, fieldcraft, logistics, medicine, engineering and unit leadership. Recruitment is limited by actual manpower, equipment, training time and instructor capacity. A society that loses its modern population cannot replenish itself simply by invoking ancient prestige.

## 7. Army modernization, air power and the navy

Land modernization moves through three practical groups. The first teaches modern firearms, field medicine, communications and support integration. The second adds artillery coordination, engineers, reconnaissance and reliable supply. The third offers mobile combined arms or a mountain and amphibious specialist emphasis. These late emphases share ordinary support technology, but the first spends industry and fuel on motorization and armour while the second spends training and specialized equipment on difficult terrain and landings. Neither grants unsupported equipment designs.

The army must possess the modern tools before a focus's doctrinal benefit can be fully used. Military Adaptation gates access to complex programs and rises when exercises, equipped formations and operational projects demonstrate that knowledge. A player cannot buy 100 adaptation through repeating the cheapest decision. Failed exercises retain a limited amount of experience but do not complete the whole institutional milestone.

Air development begins with an actual airfield or an access agreement, technical staff and an aircraft source. Initial combat aircraft are zero by default. A training and observation group precedes an interceptor and reconnaissance group. The late choice emphasizes close air support for continental campaigning or naval reconnaissance and strike support for Mediterranean operations. Transports and airborne ambitions require their own aircraft, training and researched capability. The air branch is useful to every route, including homeland defence, and never ends after a token research bonus.

Naval development begins with a verified functioning port. Until one exists, the relevant focus prepares coastal works and opens a paid port project. Convoys, escorts, repair capacity and fuel storage precede cruisers or amphibious ambition. The middle naval groups choose a concentrated eastern Mediterranean fleet or distributed patrol and escort forces. Both protect supply. The late groups offer convoy warfare and sea denial, sustained amphibious operations, or an expensive surface fleet where the actual industrial base supports it.

Ships arrive through domestic construction, a legal purchase, a consensual transfer or a real capture. The same hull cannot remain with the donor and appear in Sparta. Naval exercises consume fuel and risk normal wear. A captured foreign port does not instantly repair all ships or open every strait. Port capacity, route access, naval range and hostile sea zones are actual campaign constraints.

The colonial route turns this support branch into a core strategy through depot chains, repair bases, convoys, escort coverage, negotiated access and distant local administration. Other routes can pursue a navy without inheriting colonial formable rewards. An eastern empire still needs coastal supply, and an Italian campaign needs a credible crossing or an existing land approach. Naval depth therefore supports the whole tree while remaining indispensable for the maritime route.

### DLC-independent outcomes

| Optional system | Available content path | Required fallback |
|---|---|---|
| Tank, aircraft or ship designers | Use audited chassis, hull, module and variant mechanics | Use complete native equipment models and ordinary production. The strategic equipment and training gate remains the same. |
| International equipment market | Purchase through its supported workflow when suitable | Event-owned bilateral contract with a real seller, consent, exact equipment debit, civilian industrial commitment and delivery receipt. No anonymous infinite vendor. |
| Specialized industrial organizations | Integrate the available organization into the production program | Use researched equipment, ordinary designers where available and bounded state production effects. No inaccessible organization blocks the route. |
| Specialized force progression | Use supported mountain, marine or airborne progression | Use researched native special-force units, legal caps, army experience and training decisions. |
| Advanced naval access or subject features | Use supported access, transfer and subject terms | Offer ordinary military access, docking rights where supported, existing legal subject relationships or direct ownership. An unavailable lease mechanic cannot count as territorial sovereignty. |
| Research cooperation | Use a supported sharing group or licensing system | A finite bilateral research bonus with a real partner and a paid technical mission. Earned slots remain domestic institutions. |

All fallbacks preserve the material problem and its payoff. They must not convert an unavailable designer or diplomacy feature into an automatic free technology, fleet or territorial transfer.

## 8. Evolution interfaces and country-package acceptance

Age of Heroes adds the actual manifested Castor and Polydeuces as mythic characters, the earthborn Spartoi as a land family, unique Talos as a heavy land entity and short-range Stymphalian birds as an aerial family. These are the entire approved mythic roster. Their source traditions, access, capabilities, caps, costs and defeat behavior belong to the evolution specification. No extra sea monster or invented Spartan hero is implied by this file.

The baseline army remains human after the evolution. Human tournament eligibility and mythic Open Division eligibility use actual actors and units. Sacred dyarchy makes Castor the single visible country leader representing the joint kingship. Polydeuces receives a real senior office with his own adviser portrait and, if retained, a separate commander consumer. Their portraits never become a composite face. Castor cannot remain a free field commander while sovereign. Mortal custodianship and a mortal government's divine mandate retain the appropriate human institutional leadership. None creates a sixth conquest route or makes a normal route's final formable require mythology.

Country-package acceptance requires a legal independent country, audited capital and state split, correct identity and leadership, complete flags and portrait direction, balanced laws, conserved local manpower, exact starting slots, recorded technology and equipment baskets, viable supply, bounded force creation, renewable modern recruitment and all required visual and sound consumers. It also requires AI and human behavior in weak, normal, severe and late scenarios, with and without optional systems. The implementation and validation handoffs own those checks. This specification does not claim that they have run.
