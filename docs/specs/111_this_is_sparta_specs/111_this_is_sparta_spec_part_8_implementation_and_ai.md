# Event 111: implementation, state ownership and AI

This part defines the implementation contract for This is SPARTA!!!, current Event 111 and original catalog identity 116. It is a specification for future work. No engine script, map patch, registered tag, final balance, generated asset, native test or HOI4 MCP result is claimed here.

The opening, five campaign routes, Age of Heroes, achievements and presentation remain governed by their respective specification parts. This part supplies the technical dependencies and common behavior needed to preserve them. Semantic identifiers below are proposed event-owned names. Numeric state, province, provider, scenario and super-event identifiers remain unallocated until the installed-content audit.

## 1. Identity migration is a prerequisite

The observed repository snapshot still has legacy row 111 Resistance and legacy row 116 This is SPARTA!!!. Both are marked Unavailable. The complete event-category initializer inspected at that revision registers neither 111 nor 116. Targeted root searches and the event directory inventory found no Sparta root. These observations support a new implementation under the user's current identity, with an explicit catalog migration. They do not authorize silently deleting the existing legacy row. [R1]

Use one event identity, one fire-once receipt and one canonical entry, chaosx.nr111.1. The old number 116 is provenance. It must not remain a second random-event registration, a second fired counter, a duplicate evolution identity or an alias that can grant the founding package again.

Before registration, the parent records an identity crosswalk covering the current ID, former ID, affected catalog rows, script roots, localisation selectors, debug names, Event Log mappings, existing saved arrays, docs, tests and assets. Reconcile the current event 111 row without guessing a new destination for Resistance or applying a blanket offset to unrelated events. The explicit user mappings for IMRO 110 and Wrestling Tournament 108 are separate known corrections. Unresolved legacy identities retain their own records until the complete migration resolves them.

An old save row with only the integer 111 cannot prove whether its author intended Resistance or Sparta. Do not reinterpret it as a Spartan achievement, birth or evolution. A supported migration needs additional identifying evidence and a versioned, idempotent conversion. Otherwise declare the new map and event package as requiring a new campaign. A quiet partial migration is unacceptable.

The event is Minor Fire-Once, Chaos 1 and unclustered. Keep it outside an arbitrary Formables cluster assignment. Register the event, default enablement, manual dispatch, names, actor mapping and history only when the package is ready for that surface. Catalog status reflects actual implementation and the user's approval, with no automatic Playable assignment.

## 2. Mandatory Laconia state split

### 2.1 Evidence and decision

The committed state registry identifies state 186 as Peloponnese with provinces 1173, 4078, 4178, 4193, 7096, 7211 and 11965. No Laconia or Sparta source/name match appears in its 1,081 indexed records. The actual installed map is unavailable in this planning environment. These values describe a stored source snapshot and do not identify the final Laconian province subset. [R2]

The accepted implementation includes a build-time Laconia state split. Sparta must own territory at the real Laconian location in the successful entry transaction. The entire Peloponnese is not the opening substitute. Province control is not a substitute for state ownership. The offline effect reference describes whole-state transfer and warns that province-only control may reset at peace or a peace conference. [R3]

Use STATE_LACONIA, PROVINCE_SPARTAN_CAPITAL and PROVINCE_SPARTAN_DEPLOYMENT as planning roles. They do not reserve native IDs.

### 2.2 Required map package

The map owner must inspect the installed game and every active map-changing overlay in actual load order. Establish the exact state and province definitions, map bitmap, province terrain, strategic-region membership, adjacency, coastline, ports, supply and railway files. Resolve source hashes and collisions before assigning the new state ID. Do not derive an allocation from the old snapshot's maximum of 1081.

Determine the Laconian boundary from documented geography and the available native province geometry. Keep every province in exactly one state. Avoid disconnected fragments unless the geography and native movement behavior justify them. The parent must review the selected capital and a valid deployment location inside the new state's controlled territory.

Before the event fires, the split preserves the starting territorial and economic situation. For every supported bookmark and dated state-history change, reconcile:

| Surface | Required treatment |
| --- | --- |
| Population | Split the former total once using a documented allocation and exact residual handling |
| Resources | Allocate existing deposits without multiplying or deleting them |
| State buildings and slots | Reconcile current levels, category, shared capacity and any justified capacity adjustment |
| Province buildings | Keep each actual port, fort, airfield-related consumer and other province placement attached to its province |
| Victory points | Reassign by province and review capital selection, surrender weight and visible city naming |
| Supply | Review local supply, hub placement, port supply, rail connections and links across the new border |
| Starting units | Keep valid deployment and ownership for both base bookmarks after the boundary moves |
| Ownership and cores | Preserve the intended pre-event owners, controllers, cores and claims for both resulting states |
| Country setup | Preserve Greece's live capital, focus tree, history and diplomatic identity |
| State references | Reconcile every semantic whole-Peloponnese requirement, location-specific check and hardcoded consumer |
| Compatibility | Record the combined map revision and supported overlay order, with an explicit new-campaign or save-migration policy |

These are conservation and compatibility requirements. They do not add free factories, population or resources to the campaign. Any separate Spartan opening grant belongs to the event transaction and its budget, so its source remains visible to accounting.

A whole-Peloponnese formation condition may need both resulting states. A Laconian condition needs only the Laconian state. Do not mechanically replace every literal 186 with the new ID. Walk each consumer's meaning, including vanilla/formable overrides, missions, Event 006 identities, victory conditions, claims, cores, map displays and historical rules.

### 2.3 Registry and compiler dependency

The source registry documents an archived geometry producer, registry builder and consumer compiler. They are provenance, not routine supported tools. New geometry and a new consumer therefore require deliberate restoration and review of that chain or an accepted replacement. The active runtime generator cannot reconstruct missing province geometry by itself. [R4]

The map dependency remains open until the rebuilt geometry registry, state index, universal triggers, affected consumer manifests, exact state textures and category attachments all refer to the same combined map revision. Preserve every other complete consumer while adding the Spartan one. Review the split itself and representative affected old consumers. Do not report a new panel as complete while its source-state hashes still describe the unsplit map.

The gameplay package must not become normally selectable with an unresolved map dependency. The visible unavailable reason belongs to the ordinary event-system presentation. It must not start a campaign incident and then ask the player to manufacture Laconia through months of decisions.

## 3. Shared state model

Only Civic Settlement, Military Adaptation and, after activation, Mythic Strain are public custom values. Each is bounded from 0 to 100. The other data below is private identity, accounting or lifecycle storage. It creates no additional public currency or general progress meter.

Use one owner for each field. A target or receipt may be mirrored only to prove identity, with the matching nonce checked before mutation. All saved rows require stable IDs. Array indexes are implementation positions, not durable identities.

| Owner | Persistent data | Meaning and lifetime |
| --- | --- | --- |
| Global event system | Event 111 registration and successful fire-once state | Shared selection and history authority |
| Global event owner | Founding episode ID, actor pointer, birth receipt and package version | One successful founding, with versioned repair state |
| Global Event 111 military owner | Family allowance, paid reservations, actual surviving beings and custody lineage across every authorized country | One shared allowance per family, with no new cap on transfer or derivative creation |
| Spartan country | Civic Settlement and Military Adaptation | Public baseline development |
| Spartan country | Political settlement and route commitment | Mutually exclusive qualitative identity and route flags |
| Spartan country | Research and institution stages | One-time unlocks and exactly three named spirit-slot lifecycles, with at most three active spirits |
| Spartan country | Founding cohort records | Original units, exact issued people/equipment, proven survivors and consumed conversion receipts |
| Spartan military owner | Ordinary deployed manpower, cadre manpower, certified original attribution and pending contemporary admission | One native-backed quota and conservation predicate for every intake and reinforcement path |
| Spartan country | Active operation rows | Actor, target, territory-set revision, due date, quote, paid components and outcome |
| Spartan country | Age of Heroes activation receipt and Mythic Strain | Orthogonal evolution state, initialized only once |
| Spartan country or exact manifestation owner | Manifestation identity, instance ID, location, due date and cleanup receipt | Unique or bounded mythic consumers |
| Event 111 mythic owner | Warning episode, exposed service/site, material cause, original due date, dormant status and continuous recovery interval | One durable warning and targeted outcome, without reset through service or ownership changes |
| State | Laconian anchor identity and event-owned local projects | Stable location markers with provenance |
| State | Any actual civilian movement/cohort records | Physical people, reception burden and one transfer owner |
| Shared cost owner | Recorded transaction components and refund state | Exact paid and refunded amounts |
| Shared Event Log | History and evolution rows | Published event history, never private copied arrays |

Recommended event-owned flag families distinguish prepared, committed, failed, interrupted, completed and cleaned states. Do not collapse all of them into a single active flag. A failed operation is not a completed one. A refunded operation is not free to pay out again. A copied leader or unit does not confer the parent country's identity.

No regular daily, weekly or monthly world scan should maintain this package. Existing event-owned country callbacks, state-controller hooks and one-time deliveries are bounded to registered active actors and records. Each timed record stores an absolute due date and survives duplicate callbacks or controller changes without gaining time.

## 4. Founding transaction and actor setup

### 4.1 Preflight

Before irreversible mutation, freeze the selected founding episode, SPARTA_TAG role, exact Laconian state and provinces, prior owner and controller, source-state identity, expected package revision, initial cohort plan and any manual requester. Validate the map package, a valid deployable location, country reservation, source authority, no prior birth receipt and no conflicting active setup.

The default opening requires a settled state whose owner also controls it. An occupied-state handover remains disabled until its separate native path is validated. The former owner must retain territory and a valid remaining capital, and every existing formation needs a legal disposition that neither steals nor deletes it. A one-state owner cannot be silently removed to satisfy the founding. These gates follow Part 1's common opening contract.

SPARTA_TAG is locked only after the installed country-tag audit. The observed repository has no established Sparta package, but the source pass did not prove any proposed tag is unused across all installations. Reuse or reserve a carrier only through the current country collection and collision contract. [R5]

Preserve a living Greece or other holder as a country. The territorial event can remove the specific Laconian state under the accepted premise without replacing that holder's focus tree, leader or unrelated country package. Record any forced territorial change as such. Do not apply the ordinary peaceful diplomatic-consent rule to erase the event's immediate founding premise.

The native release effect can transfer every qualifying core and may remove the former owner's core on transferred states. Its exact behavior must be considered when selecting the activation method. Preserve prior cores and claims as the design requires and restore only proven side effects. Never use broad release as a shortcut around the frozen territorial request. [R3]

### 4.2 Commit and verification

The successful entry transaction must leave a real independent country with owned and controlled Laconian territory, a valid capital, the institutional royal government, a loaded event-owned tree, viable starting units, basic equipment and manpower handling, research capability and the starting institution stages.

Create the country and territory before capital-dependent helper work. When a helper requires the recipient as ROOT, send the recipient a hidden triggered-only country event with frozen context. Merely entering another country's scope does not rebind ROOT. For any optional transfer of the player's control, schedule required recipient delivery first and make the native player transfer the last relevant effect.

The actual Event 019 precedent creates units in a proven state target, with an explicit owner, one-line division payload, registered template and unique deletion identity. Its helper compares before and after divisions and checks ledger structure. Use this as a state-scope precedent, then verify the installed native schema. Do not paste a country-scope create_unit expression from a conflicting prose summary. [R6]

Prove the required country, territory, capital, initial unit set and institution package before marking the founding receipt committed. Count only the units this transaction created. A pre-existing division or an unrelated helper-created unit cannot satisfy a missing founding formation.

The shared random-event pipeline records history before the target's immediate block. Resolve actor preparation and the success boundary in that pipeline so the first history row points to the intended Spartan actor. Do not create an extra fired row or leave a successful history row for an impossible founding. The parent owns shared logger changes and must preserve unrelated events.

Failure after partial mutation enters deterministic reconciliation from the frozen receipt. Return or remove only effects whose ownership is proven. If the native rollback cannot safely restore the exact original context, retain an explicit blocked repair record and suppress repeat grants. Never refire a fresh random opening to hide the partial state. Every repair must distinguish a real uncommitted operation from an already successful founding.

## 5. People, military consumers and the finite host

### 5.1 Opening population and cohort accounting

The returned ancient host is a finite supernatural arrival, distinct from the modern local civilian population. Its initial people and equipment are recorded once. Modern Greeks and later admitted citizens supply the normal country's manpower and recruits under the ordinary demographic rules.

The map split conserves existing civilian population. The arrival adds only the approved founding cohort. Do not both add that cohort to local population and also grant the same people as free recruitable manpower and fully filled units without an explicit conservation model.

Returned survivors can become modern cadres once. The conversion receipt references exact source cohorts, the amount actually available, actual paid modernization equipment, destination package and a consumed marker. Native casualties or damaged strength may reduce the result. An original nominal cohort size is not proof of surviving soldiers.

Use a verified same-country unit or template conversion when it preserves the intended people and equipment. If the engine requires a replacement transaction, prove exact source absence and destination creation without refreshing casualties or duplicating equipment. The existing Event 019 recreate-and-delete workaround explicitly has native fidelity limits. It cannot be presented as lossless conversion. [R7]

Modern recruitment is not a second ancient-host generator. Agoge development changes present-day training, organization, admission and equipment. It does not produce minors or renew dead ancient warriors.

#### Renewable cadre quota and inherited survivors

[Part 4, section 5](111_this_is_sparta_spec_part_4_decisions_and_settlements.md) owns the exact cadre invariant. The founding 3,000-person contemporary local brigades use ordinary native infantry. They do not start as custom cadres and have no original-returnee attribution.

| Quantity | Required definition |
| --- | --- |
| O | Actual human manpower in Spartan-owned deployed ordinary-native land formations. Exclude returned-host and cadre personnel, mythic bodies and their liaison staff, foreign-owned expeditionaries, garrisons, queues and the unassigned pool. Spartan-owned expeditionaries remain counted when an ally commands them |
| p | Academy quota tier of 0.10, 0.20 or 0.25 |
| Q | Renewable allowance, `max(2000, floor(p*O/(1-p)))`. The 2,000-person floor is the explicit small-army exception |
| M | Actual human manpower in Spartan-owned custom modern-cadre consumers |
| E | Conservatively certified surviving original-returnee attribution currently included in M |
| P | All committed contemporary intake and replacement people not yet in M, including queues and reserved transfers |

Every proposed admission or refill must leave `M - E + P <= Q` after commitment. Move a person from P into M once. Every contemporary recruit or replacement consumes renewable capacity and never raises E. The founding host, converted survivors, foreign-owned troops and undeployed people cannot enlarge O. These quantities are private accounting, with no additional public value.

Only a proven conversion or permitted physical transfer can move existing original attribution into or between cadre consumers. It consumes the source receipt once and never grows the total original-person allowance. Deduplicated gross casualties reduce the affected attribution. Where mixed casualties cannot identify original and contemporary people, apply `E_i_after = max(0, E_i_before - L_i)`, capped by actual remaining strength. L_i is supported gross human loss. This conservative rule consumes original attribution first without inventing individual casualty identities.

Native admission and reinforcement control is an enablement gate. Prove gross-loss and admission evidence with safe control of every automatic refill path, or prevent automatic refill and prove a conserved, quota-checked admission path. Net strength polling cannot prove the invariant when casualties and replacement cancel between observations. No assumed casualty-identity API or reinforcement command satisfies the gate.

If ordinary losses reduce Q below existing non-exempt cadre strength, retain living troops and freeze further contemporary admission and refill. Reconcile unused P through its actual paid receipts while preserving trained people and consumed materials. Do not delete troops or refund deployed people to force the equation. A loss of certified original attribution likewise cannot be refilled as an inherited exemption. Ordinary contemporary training remains useful when the elite quota is full.

### 5.2 Consumer dispositions

The parent has accepted these boundaries:

| Military consumer | Disposition | Required integration |
| --- | --- | --- |
| Returned ancient host | Parent-owned finite cohort | Event-owned spawn, finite survivor and conversion receipts, CXT package, exact unit/equipment/model consumers |
| Modern Spartan cadre | Owner-registered land provider | Complete Event 019 provider contract for eligible documented consumers, normal training and sustainment, CXT package |
| Earthborn Spartoi | Owner-registered land provider | Complete gated land-provider contract, one Event 111 allowance across all owners, manifestation costs, custody lineage and exact cleanup, CXT package |
| Talos | Parent-owned unique heavy land entity | One active instance identity, creation/recovery/defeat receipts, no repeatable Event 019 draw, CXT package |
| Stymphalian birds | Air package | Native air-family definitions and explicit bounded manifestation lifecycle, outside the land-battalion consumer |

Every new concrete land sub-unit and equipment type receives a full inventory disposition. Support-only entries remain attached to their provider or explicitly parent-owned. They do not become fabricated standalone divisions.

Provider IDs are assigned only after inspecting the live registry. Do not reuse a current family ID or invent a proposed numeric value in this specification. Modern cadre and Spartoi providers register idempotently from their own startup surface and supply all thirteen callbacks required by contract v4. Eligibility and native-host eligibility are separate receipts. Provider registration does not authorize a general foreign draw or add a broad export route.

The Spartoi allowance belongs to Event 111 once, across every authorized country. Count active consumers, pending paid reservations and surviving beings held as equipment for redeployment or recovery under one owner ledger. Interim custody allows four companies, mortal custodianship three and sacred dyarchy four. Coercive mandate permits six only when its additional supplied site and trained liaison institution also exist. The actual usable allowance remains the lower of the constitutional limit, supported site capacity and trained liaison capacity. Stored survivors occupy capacity. A template disappearing does not release their count.

Verified destruction removes only the actual lost beings from the live count. Their replacements still require an individually paid manifestation, valid site custody, support personnel and free allowance. A verified transfer moves the existing identity and count. Disbanding, capture, licensing, lend-lease, annexation or template copying cannot grant another allowance. A constitution that lowers the cap cannot complete until its disclosed safe release has removed the excess, including stored surviving beings. Talos and the birds follow the same event-wide ownership principle with their own accepted family limits.

General foreign Event 019 draws are ineligible for Spartan mythic families. An intentionally authorized derivative requires an explicitly authored transfer, preserved Event 111 origin, real recipient custody or access to the registered site, trained human support, its actual paid manifestation receipt and the same global count. It receives no Spartan polity, route progress, royal government, heroes, focus or constitution access, Age of Heroes eligibility, divine sovereignty or achievement progression. Receiving a unit cannot call the country-creation or evolution helpers.

Missing lineage, unsupported transfer accounting or unavailable exact native cleanup rejects the transfer and blocks the affected consumer's registration. Do not replace that gate with a generic family fallback, a broad scan that deletes unrelated foreign forces or an asserted engine capability. A modern-cadre consumer must likewise be explicitly eligible under its own documented contract and preserve parent identity isolation.

### 5.3 Spirits, research and equipment

There are exactly three named focus-tree spirit slots: polity, military institution and state capacity. At most three tree-owned spirits are active, with at most one current stage in each slot. Starting, reformed, stressed and evolved stages replace that slot's prior stage. A timed country modifier counts toward this limit if it functions as an additional tree-owned spirit. A mythic upgrade does not add a fourth spirit under a different category name.

Research begins with the agreed two slots and advances through technical education, a working research network and late imperial institutions to the agreed maximum of five. Each stage uses a one-time receipt. Repeated focus loading, tag changes or re-entered decisions must not add slots again.

Conventional artillery, trucks, armor, ships and aircraft use audited installed families. Custom model names are not proof that a new equipment archetype is needed. Add concrete equipment and enum registration only for an actual package consumer.

CXT registration is parallel coverage, not a campaign grant loop. Add the idempotent setup and matching modifier-free hidden carrier. Bounded startup registers it. The daily CXT path registers or marks pending only. Explicit user-triggered debug decisions apply grants, repair and replenishment. CXT-created proof actors cannot contribute to campaign achievements, finite-cohort history or evolution outcomes.

## 6. Decisions, missions, diplomacy and territorial proof

Each operation owns one immutable request receipt with actor, target, target type, route, semantic territory-set revision, original authority, setup result, creation and expiry dates, ordinary quote, final quote, actual component debits and outcome. The selection cursor is not a receipt.

Part 4 owns a limit of three concurrent accepted work undertakings per acting country across ordinary and mythic categories. At most two consume territorial or industrial capacity and at most one consumes intake or conversion capacity. AI uses the same limits. An outsider's EX01–EX03 work uses that outsider's equivalent budget, so Sparta's queue cannot block enemy containment.

MY01, MY03 and MY14 consume one general slot. MY04, MY06, MY07, MY11 and MY12 consume one slot and one territorial/industrial allowance. MY05 and MY08 consume one slot and the shared intake/conversion allowance also used by ordinary Agoge work. EX01–EX03 consume a slot and territorial/industrial allowance for their actual acting outsider while material work is underway. MY02 service terms, MY09 effect durations and cooldowns, MY10 safe-removal records, completed MY13 aftercare, unavoidable warnings and pure 90-day or 180-day holding periods remain durable records outside the accepted-work limit. They cannot conceal an additional training, construction or binding project.

MY10 remains free and available with all work slots occupied, subject to real safe withdrawal. MY12 may require an explicit pause or cancellation of another undertaking with exact treatment of consumed work, released reservations and refundable paid resources. A full queue is not permission to discard a paid project silently.

All click, tooltip, AI and scripted-effect gates use one authoritative requirement helper. Revalidate the current actor, target, authority, prerequisites and quote immediately before payment. A stale selection, a newly independent client or changed controller may invalidate the operation. An ordinary alliance, access treaty or docking right never counts as political subordination by itself.

Use the shared universal cost API for supported resources and exact owner adapters where needed. Quotes are recomputed before payment. A quote neither reserves resources nor proves payment. Refunds credit actual paid components once, preserving tombstones and any owner-adapter acknowledgement. Effects execute only after the complete payment and setup receipt. [R8]

Every operation lists which resources are spent, reserved or merely required. A capacity reservation is not a population debit. A construction commitment is not a free factory. A convoy requirement is not an invented special colonial currency.

Respect the agreed action presentation limits, four spendable types maximum, command power no higher than 60, and three inline cost values maximum. Put complete material detail in the tooltip. Hide obsolete or irrelevant actions and contextualize secondary choices.

Mission completion is checked before timeout consequences at the same due date. Setup failure, loss of authority, voluntary cancellation and ordinary deadline failure have distinct outcomes. A refund cannot undo a valid prior completion or reward. If a target moves, decide from the operation's contract whether the objective follows the actor, stays with the physical state or cancels. Do not silently switch to a different country.

The selected-route puzzle, its summary, the formation decision, the focus payoff, the AI condition and any achievement all call the same semantic territory predicate. Predeclared candidates may change relevance, but a missing visual piece cannot change the actual requirement. The Laconian anchor remains required and visibly unresolved when lost.

Direct ownership, direct control, qualified subject ownership and qualified subject control are separate predicates. A client state must meet the specific relation and route rules. Territorial qualification at the final click is authoritative, regardless of an earlier green display.

## 7. Lifecycle, defeat and connections

The baseline route state and Age of Heroes are orthogonal. Every ordinary route can reach its normal completion with the evolution disabled. An eligible high-Chaos opening and an active-run activation share one evolution receipt, so rewards, manifestations and hero recruitment cannot duplicate.

Mythic Strain is initialized only when Age of Heroes actually activates. Enabling a toggle or becoming eligible grants no Chaos. Log evolution through the shared context. Actor, track, stage and enabled-state handling must match each shared view. Actual mythic outcomes can contribute Chaos only through the defined consequence hooks and without duplicating generic war, death or annexation sources.

The twins Castor and Polydeuces are separate mythic characters. Character identity, command roles and tournament appearances require real per-person records. Only the sacred dyarchy outcome changes leadership to the actual twins. Mortal custodianship and aggressive divine mandate retain the mortal institutional government. No combined portrait or unit receipt becomes proof that two characters exist.

Talos uniqueness is global to the owning event episode, with one exact active instance and one destruction or retirement receipt. Capture, controller change, reload, tag change and callback retry cannot create another Talos. A future repair restores only the defined damaged instance when allowed by the mythic design, rather than awarding a replacement on every pulse.

The Part 5 warning contract is persistent state. Entering Strain 75–89 with a real exposed service records one site, material cause, start date and original due date 90 days later. Ownership changes, a brief fall below 75, service toggles and save/load preserve that target and deadline. MY11 shows its actual scaled completion date beside the fixed warning date. Payment and project acceptance do not postpone the warning, and a repair that cannot finish in time must disclose that fact beside the feasible MY10 mitigation.

MY10 neutralizes exposure only after the actual service ends and the beings reach lawful supplied custody or valid permanent release. A withdrawal request during battle is insufficient. A broken treaty, abandoned dangerous binding or enemy-held entity remains exposed until its actual obligation is resolved. A completed repair that resolves the named obligation and brings Strain below 75 can also neutralize exposure. The warning then becomes dormant with its original date and history. Passing that date while safely dormant creates no rupture.

The affected service cannot reactivate while its dormant warning remains unsettled. Closing and rearming require repair or lawful release of the material breach, a valid disposition for every related entity and Strain below 50 for 30 continuous days. A new warning needs a new material exposure after recovery. At the original due date, unresolved real exposure raises Strain to at least 90 and causes one targeted native rupture. A direct rise to 90 or more applies the same exposed-site priority without waiting. No exposed service means blocked resumption and safe recovery, with no invented incident or Chaos award. The actual local consequence precedes eligibility for C111_RUPTURE.

On defeat, clear active event-owned operations, permissions and unearned claims according to their receipts, while preserving historical achievements and completed rows. A defeated country can retain meaningful conquered or successor history without leaving active AI, free reinforcement or invisible hostile missions behind. Do not clear shared world threat while another source remains active.

The Persia connection checks an actual living restored actor. The current source calls PER and sets PER_UNIFIED plus form_persian_empire_flag when accepted. It creates no separate new Persia tag. Existing Iran by itself is not sufficient restoration evidence, and the flag by itself is not proof that the same living actor still owns the relevant territory. [R9]

Event 019 connections use its public provider or history contracts. IMRO 110 is a living Macedonian diplomatic actor. Wrestling Tournament 108 receives ordinary human Spartans as ordinary human competitors and only actually manifested supernatural beings under its applicable open category. Malta 038 and Heroic Crusade retain their actual current actors and religious or strategic motives. Do not invent the latter's unresolved new numeric ID from its legacy 126.

EX03, ACH20 and the conditional international-defeat presentation share Part 1's qualifying-opponent predicate. Require a prior C111_TRANSREGIONAL or C111_ROUTE_ORDER receipt and actual C111_DIVINE_SOVEREIGNTY or C111_COERCIVE_MANDATE. Authenticated removal, accepted settlement authority and the paid EX03 commitment begin one fixed 180-day episode. Its industrial reservation, durable removal, containment receipt and applicable achievement/presentation use that same episode. Technical scaling cannot shorten it and completion does not start a second automatic 180-day wait. A material breach invalidates the episode with exact payment and site treatment. A new valid attempt cannot count failed time.

EX03 occupies one accepted-work slot and one territorial/industrial allowance for its acting outsider while its industrial reservation or other material work remains. The shared durability record adds no second slot. It does not make the paid undertaking slot-free.

C111_MAJOR_CONTAINMENT uses −15 with a route receipt and −10 otherwise, paying only the difference if a lesser dissolution reduction already applied. Sacred sovereignty does not need an additional coercive-mandate history to qualify. ACH20 additionally retains its own actual war and individual-contribution requirements, so coalition membership alone cannot supply outsider credit.

## 8. AI policy and audit contract

### 8.1 Decision ownership

AI uses ordinary focuses, decisions and effect helpers. It never presses the informational puzzle or gets a cheaper hidden payment path. It receives the same geographic, resource, authority, unique-instance and evolution gates as the player.

Separate four probability surfaces:

| Surface | Interpretation |
| --- | --- |
| Route-choice event options | Conditional normalized shares only over the complete eligible option pool |
| Focus priorities | Native willingness and selection/race semantics, not automatically a probability distribution |
| Decisions and missions | Willingness or action-score semantics with native cadence and affordability |
| Evolution and incident pacing | MTTH or explicitly defined scheduled chance, separate from conditional option selection |

Give the probability auditor complete source selectors, candidates and context for each surface. A probability for a route conditional on an event firing does not include the chance of the event firing.

### 8.2 Route preferences

At commitment, eligible route scores combine the common baseline with political direction, territorial opportunity, available military capabilities, expected foreign resistance, current war burden and strategic access. Use named tuning constants and documented factors rather than hidden arbitrary offsets. Unavailable routes are removed by the actual route predicate.

| Route | Positive reasons for AI preference | Reasons to delay commitment or shift within its permitted support branches |
| --- | --- | --- |
| Spartan Hegemony | Strong local position, receptive Greek actors, credible land force and manageable nearby obligations | Unstable citizenship settlement, stronger protected Greek opposition or an unresolved Laconian defense |
| Legacy of Alexander | Developed logistics and research, secured Macedonian position, viable eastward route and broad military capacity | Distant targets without access, multiple hostile fronts, no administrative capacity for new conquests |
| Thermopylae Avenged | A real restored Persian opponent provides an additional motive, alongside a reachable Aegean/Anatolian front and sufficient endurance | Unresolved current territorial targets, inaccessible route or inability to sustain an eastern campaign |
| The Western Campaign | Southern Italian or Sicilian opening, fleet and convoy support, viable staging and limited opposing coalition | No practical crossing, severe convoy losses, insufficient supply or a dominant hostile navy |
| Hellenic Colonies Reborn | Working ports, protected shipping, willing clients and viable connected coastal objectives | Landlocked expansion bait, clients outside authority, isolated ports or an unaffordable escort burden |

After commitment the AI pursues that route's current useful objective rather than rerolling the route whenever a target changes. It can repair supply, improve institutions, negotiate, defend or recover from a setback through shared and route support content. It does not unlock an exclusive rival conquest route to escape a temporary difficulty.

Named restoration interactions are optional connections. A route's ordinary geographic continuation cannot require another random event to fire. If a restored Persian or Macedonian actor is absent, use the selected route's defined treatment of actual current territorial owners and internal alternatives. Do not make the whole route ineligible merely because its special diplomatic counterpart is absent.

Target selection uses the exact live target set and a documented stable tie-break. A deterministic maximum-score selector must accept its first valid candidate even if all scores are negative. A numerical sentinel cannot make a valid pool empty.

### 8.3 Resource and crisis behavior

The AI preserves enough actual resources and force to defend Laconia and meet its active commitments. It delays optional expansion when its supply route, equipment fill or existing war obligations fail the decision's real conditions. It prioritizes completing an already paid feasible mission over opening several conflicting projects.

Civil reform and military adaptation remain useful under every route. AI should remove or upgrade its starting liabilities through the same institution stages as the player. It must not get stuck permanently accumulating a pile of opening spirits.

When Age of Heroes is active, AI balances the concrete manifestation opportunity with Mythic Strain, the approved outcome path, current threat and the actual costs. It does not treat evolution activation as free strength or choose a unique manifestation whose active instance already exists. Sacred dyarchy requires the real twins and its full political conditions.

Foreign AI evaluates the actual proposal, current sovereignty, strength, war, alliances, subject relations and territorial stake. A state does not accept subordination merely because a route is selected. Human actors retain their direct decision where the design calls for one.

### 8.4 Accepted action and counterpart policy ledger

The following dispositions promote the completed improvement review's full AI ledger into the implementation specification. Each row is an accepted behavior requirement. It is not a claimed native weight, measured probability or implemented helper. The actual action retains every player-facing gate, cost, target rule, timer and lifecycle in Parts 1, 4 and 5.

For every row, the implementation handoff records the actual owner source and helper, complete target/candidate pool, hard eligibility gates, committed-resource and defense reserve policy, positive and negative preference factors, unavailable fallback, counterpart response where applicable and a named audit scenario. The AI probability auditor validates those actual surfaces without inventing the parent's numeric targets. A score-only surface remains score-only. Unsupported native context remains an explicit blocker.

#### Ordinary action families

| Action | Accepted AI disposition |
| --- | --- |
| `111_action_emergency_supply` | Prioritize a real capital or home bottleneck and the smallest feasible repair. Preserve already committed materials. Where native supply inspection cannot prove the wider outcome, use the disclosed infrastructure objective and its actual scope |
| `111_action_civic_compact` | Prioritize early viability and broken civic promises that can actually be repaired. Respect the selected political institution. Use the mature compact only after its real eligibility and restore losses only against a recorded, materially repaired breach |
| `111_action_agoge_intake` | Require eligible adults, equipment, quota headroom and reserves for deployed forces. Choose ordinary training when elite capacity is full. Never grow original-returnee attribution through recruitment |
| `111_action_convert_returnees` | Select an actual surviving formation at a supplied safe site with the required kit. Preserve enough legal defenders while it withdraws. Apply the quota and origin contract, and cancel a vanished or already consumed source |
| `111_action_industrial_project` | Prioritize supply, a working workshop, arsenal or institution that enables a feasible next step. Require a real site and capacity. Do not reserve the same industrial capacity for conflicting projects |
| `111_action_armament_contract` | Select a willing stocked supplier and a viable delivery path. Compare real compensation and dependency terms. Defer or use local production when delivery is infeasible. Never copy equipment or infer granted technology |
| `111_action_select_objective` | Evaluate the complete eligible target pool and choose a reachable incomplete required objective with a stable tie-break. Accept the first valid candidate even when every score is negative. With no valid target, recover or wait |
| `111_action_diplomatic_offer` | Offer only legal selected-route terms to a useful attainable counterpart. Preserve refusal history. Reoffer only after a material change in terms or circumstances under the declared cooldown. A human retains the response |
| `111_action_campaign_preparation` | Require the route's actual staging, transport, passage and logistics. Prefer completing a feasible paid operation and defer another front while existing commitments fail. Do not impose an invented perfect-strength gate |
| `111_action_postwar_settlement`, including charter repair | Prioritize a missing required contribution or an existing conquered region before optional conquest. Recheck owner, controller, charter and observation periods. Preserve genuinely completed reconstruction through failure |
| `111_action_regional_integration` | Apply actual citizenship and settlement policy. Greek cores use the stricter approved rule. Extra-Greek integration uses supported administration or recruitment. Defer during a resource or domestic crisis |
| `111_action_proclaim_route` | Commit once when affordable and the complete exact-set helper, administrations, thresholds and required 90-day persistence all pass. Painted map cells alone never prove completion |

#### Automatic ordinary mission dispositions

These eight mission consumers do not introduce a second reward-choice AI. Every one automatically completes success before timeout, cancels mandatory authority loss and preserves the exact sunk-cost, reservation and refund rules. Voluntary cancellation is reserved for infeasible or strategically untenable work.

| Mission | Accepted continuation or cancellation disposition |
| --- | --- |
| `111_mission_home_supply` | Continue the feasible paid bottleneck repair or disclosed infrastructure objective, then evaluate its actual completion and observation condition |
| `111_mission_civic_settlement` | Continue the paid institutional or repaired-promise work while its political and territorial authority remains valid |
| `111_mission_agoge_training` | Continue valid adult training within the quota and real manpower/equipment contract. Preserve already trained people and consumed work if the remaining commitment becomes invalid |
| `111_mission_returnee_conversion` | Continue the selected surviving cohort's safe conversion. A destroyed or unavailable source cannot complete or refund nonexistent people |
| `111_mission_industrial_delivery` | Continue feasible construction or authenticated delivery, preserving completed infrastructure and actual delivered or lost materials |
| `111_mission_campaign_preparation` | Continue the paid selected-route operation while its actual staging and logistical objective remains feasible |
| `111_mission_regional_settlement` | Continue the required region or basin's material settlement under the correct current owner/control/charter predicate |
| `111_mission_charter_repair` | Continue repair of the recorded contribution or civic breach, restoring only the qualified benefit after its real observation period |

#### Mythic and outsider actions

| Action | Accepted AI disposition |
| --- | --- |
| `MY01` | Investigate when ordinary defense and institutions are viable and actual materials plus a work slot exist. Otherwise use the existing 180-day deferral. Do not activate for an assumed free force or create another returned host |
| `MY02` | Accept or renew one useful authenticated hero service when its term is affordable. Choose command for a real suitable army or training for actual curriculum need. Reject overlapping commander, office, recovery or tournament duties |
| `MY03` | Negotiate needed custody with the site's current legal counterpart. Prefer a treaty when it supplies the capability without unnecessary war. Respect refusal and existing promises. No invented actor or automatic seizure |
| `MY04` | Prepare the Theban site only with actual lawful supplied custody, trained support and a feasible paid undertaking. Defer when modern defense or prior commitments require the same reserves |
| `MY05` | Raise or replace one authorized company only with authentic origin, real liaison personnel, equipment, payment and room under the one event-wide allowance. Defer optional growth when Strain or commitments make it unsustainable |
| `MY06` | Restore the same unique Talos only with valid body/state, Cretan custody, technical capacity, transport and maintenance. Prefer the agreed defensive use first. A duplicated, permanently destroyed or retired body is ineligible |
| `MY07` | Recover the recoverable unique body or relocate it through the legal verified paid path. Prioritize safe recovery over another expedition. Without a valid location or transport, preserve the real lost or unavailable state |
| `MY08` | Create or replenish a legal wing only with Arcadian custody, airfield, handlers, paid materials and cap headroom. Prefer effective local reconnaissance/support. It is not a substitute for an unattainable conventional air campaign |
| `MY09` | Select only a proved scoped benefit for a currently assigned family with an attainable military purpose. Evaluate post-transaction Strain, shared cooldown and warning dates. Decline overdrive when it would make custody unmanageable |
| `MY10` | Prioritize free safe stand-down when exposure is dangerous or MY11 cannot finish before the original warning deadline. Request early enough for actual withdrawal. A click alone does not mitigate exposure. Keep the service unavailable until its genuine return gate passes |
| `MY11` | Select the actual warned breach and compare the repriced scaled completion date with the fixed warning window. Repair when feasible. If too late, secure lawful safe MY10 withdrawal or release before slower repair. Payment does not clear an unrepaired treaty |
| `MY12` | Prioritize one real rupture. Choose paid stricter rebinding only when sustainable, otherwise lawful permanent release or the documented lost capability. Resolve or cancel another undertaking honestly if a work slot is required |
| `MY13` | Choose permanent release when military manifestations are untenable or accepted mortal policy favors it. Require actual safe custody, release each consumer once and conserve human staff. Respect permanent closure and the fixed 180-day aftercare |
| `MY14` | Choose exactly one constitution only through the full shared gate. Mortal custodianship favors stable voluntary cooperation. Sacred dyarchy requires the authentic twin offices and sustainable civic/Strain duties. Mandate requires its viable higher-cap institutions and acceptance of its counterplay. Otherwise postpone without a fallback constitution. Safely release excess beings before a lower cap completes |
| `EX01` | The actual hostile controller secures a real exposed site when feasible and strategically useful. Preserve local supply and legal authority. Do not transfer a free creature or seize an ally's territory |
| `EX02` | An actual qualifying war participant dismantles a real defeated or withdrawn hostile binding at its controlled site when irreversible closure is intended and feasible. Recheck survivor and entity disposition. Do not duplicate another actor's operation |
| `EX03` | An accepted settlement participant or recognized custodian acts only under the shared qualifying-threat, authenticated-removal and material-authority predicates. Complete the one fixed 180-day episode. Individual outsider credit requires actual authenticated contribution |

#### Counterpart response dispositions

| Counterpart surface | Accepted response policy |
| --- | --- |
| Former owner and Greece at founding | Evaluate survival, remaining capital and army, sovereignty, current war, strength, guarantees and offered border terms. Acceptance, negotiation and contest preparation remain distinct. Human stay/switch keeps the safe default. A response cannot retroactively undo the successful founding |
| Union, league, regional client and port-charter counterparts | Weigh sovereignty surrendered, retained rights, material benefit and obligation, security, strength, alliances and trust. Independent co-sponsorship qualifies only through its explicit route charter. Generic alliance or access does not qualify |
| Arms suppliers and delivery counterparts | Accept only a real surplus and a supported compensation/delivery workflow. War needs, route danger or stock deficits can yield refusal, a smaller batch or revised terms. Preserve actual delivered and intercepted material |
| Mythic site custodians | Evaluate real custody, allowed defensive/offensive use, maintenance, recall, religion or policy, current war and coercion history. Permit refusal and contractual revocation. Government succession needs actual renewed consent or owner-supported continued consent |
| Actual IMRO Macedonia | Evaluate co-sponsorship, regional client, border-only settlement and rivalry against its real holdings and government. Refuse contradictory or excessive demands. Preserve its sourced identity and any human player's authority |
| Actual restored Persia | Evaluate defense, allies and bounded peace against the real war and territory. No Tehran-only surrender, restored-tag shortcut or forced global peace. Civil-war successors require owner-supported provenance |
| Wrestling Tournament owner | Validate the actual episode, entrant identity, division and unique availability. Use the owner's real entry/combat rules and authenticated result. Polydeuces neither automatically wins nor enters as an ordinary human |
| Malta, Heroic Crusade and other ancient revival actors | React to actual religious policy, overlapping claims, sea lanes, sacred sovereignty or coercion and their own plans. Evaluate access, cooperation, rivalry and refusal with legal state rights. An absent or unresolved actor cannot block an ordinary route |
| Hero service and office return responses | Verify the same unique character and conflicting duties before renewal, rotation, tournament return or office restoration. Expiry uses safe native removal. Service or constitutional changes cannot create a duplicate |
| Containment and peace participants | Evaluate the actual hostile qualifying power, contributed authority, feasible terms and enforceability. Humans answer their own terms. A non-hostile ally or copied coalition flag cannot invent individual credit |

### 8.5 Required audit scenarios

The following cases define evidence requests for the future probability and lifecycle auditors. They are not test results.

| Fixture | Required observation |
| --- | --- |
| Peaceful low-Chaos opening with strong Greece | Complete viable route pool and defensive priorities |
| Laconia held by a foreign occupier at birth | Default opening is unavailable until the separately validated occupied-state handover exists, with no replacement of the wrong country package |
| Missing or incompatible map build | Event unavailable with no founding, no debit and no history success |
| Post-commit duplicate entry or reload | No extra country grant, research slot, cohort, model or history row |
| Weak economy with insufficient transport | Naval routes delay practical actions rather than obtain free ships or convoys |
| Strong navy and receptive clients | Colonies route scores and actual valid port/client conditions agree |
| Restored Persia alive, absent or changed by civil war | Distinct correct eligibility with no invented opponent |
| Macedonia controlled by human IMRO or another actor | Actual actor diplomacy and contested territorial proof |
| Existing wars on two fronts | Support and defense remain attractive, no compulsory suicidal expansion |
| Exactly affordable payment | Inclusive price gate and exact debit agree |
| A discount begins or ends between opening and confirmation | Fresh quote, clear actual payment and exact later refund |
| Target/controller changes during a mission | Correct cancellation or continued objective from the frozen contract |
| Success and timeout on the same date | One completion result and no second failure effect |
| Negative target scores with valid candidates | First-valid handling and stable tie-break work |
| No eligible route candidate | Visible recoverable state, no arbitrary invalid fallback |
| Evolution disabled throughout a campaign | Every normal route retains a complete path |
| High-Chaos opening followed by later activation callback | One evolution receipt and no doubled hero or manifestation grant |
| Mythic Strain at floor, threshold and cap | Bounded values, intended policy change and no overflow |
| Talos already active, captured, destroyed or repaired | One identity and no repeat draw |
| General foreign Event 019 mythic draw | Ineligible with no paid debit, unit or Spartan progression grant |
| Intentionally authorized Spartoi derivative | Real custody/site access, trained support, paid origin receipt and unchanged event-wide allowance across both owners |
| Spartoi transfer, capture, disband, storage, casualty replacement and constitutional cap reduction | Active, reserved and surviving recoverable beings share one global count, with paid replacements and safe release of excess before a lower cap completes |
| Missing derivative lineage or exact cleanup capability | Transfer and affected consumer registration fail closed without touching unrelated foreign forces |
| Returned host conversion after casualties | No restoration of dead soldiers and no equipment duplication |
| Cadre admission at the 2,000-person floor and every academy tier | The same post-commit `M - E + P <= Q` gate includes all pending contemporary admissions and replacements |
| Converted cadre suffers gross casualties and immediate refill | Deduplicated gross loss consumes original attribution first, modern refill never raises it, and a net unchanged strength snapshot is insufficient proof |
| Ordinary army losses lower Q below existing cadre use | Living troops remain, further contemporary admission/refill freezes and unused pending commitments follow exact receipts |
| Cadre reorganization, transfer, ally command and ownership loop | Original attribution moves once, Spartan-owned expeditionaries remain in the applicable ownership count and no new inherited allowance appears |
| Native gross-loss or reinforcement control is unavailable | Affected admission and reinforcement consumer stays blocked rather than relying on assumed APIs |
| Three occupied work slots and an endangered service | MY10 remains available, while MY11 and MY12 respect the accepted-work budget and actual cancellation treatment |
| MY11 completion falls after the original warning due date | Both dates are visible, payment does not extend the warning and real timely mitigation is identified |
| Warning expiry with unresolved exposure | Strain rises to at least 90 and one actual targeted consequence occurs before one eligible rupture receipt |
| MY10 requested during battle or with unlawful/unsupplied custody | Warning clock continues until safe removal and valid actual custody or release are proved |
| Neutralized dormant warning through reload, brief recovery and service toggles | No reset or reactivation until breach disposition is complete and 30 continuous days below 50 are proved |
| High Strain without an exposed service | Resumption stays blocked and safe recovery proceeds without a fabricated incident or Chaos award |
| Sacred or coercive qualifying power contained | EX03, ACH20 and defeat presentation use the same prior reach, actual institution and 180-day predicate |
| EX03 commitment, removal, breach and a new valid attempt | One fixed 180-day episode serves all consumers, with no accelerated duration, serial second wait or reused failed time |
| Each action and counterpart ledger row | Exact helper and complete candidate pool, shared hard gates, reserve policy, preference factors, feasible fallback and authenticated response match its accepted disposition |
| CXT debug package active | Campaign tracking and unique-instance proofs remain isolated |
| Annexation, actor death or tag change during cleanup | Exact owned teardown, no clearing of another actor's records |

For each weighted surface, inspect the current source first, preserve an immutable baseline before any change, then evaluate or compare the same complete scenarios. Record exact, bounded, sampled, score-only and unresolved results separately. Simulations need seeds, run counts, uncertainty and the declared schedule. A full sequence is appropriate only when its cooldowns, resets, removals, caps and terminal states are complete.

Do not use source-only reasoning as a claimed replacement for an unavailable mandated probability route. Report the exact tool or unsupported-context blocker and retain the implementation item as unvalidated.

## 9. Delivery gates and evidence levels

The parent integrates in dependency order: identity and map resolution, conserved state and country bootstrap, military consumers and institutions, routes and operations, Age of Heroes, shared connections and history, then presentation and final audits. Assets and gameplay can proceed in bounded parallel packages once their identities are stable. Registration must not make incomplete paths normally selectable.

The completion review needs evidence for the following gates:

1. Identity 111 is unique in runtime and correctly migrated from legacy 116 without deleting another catalog identity.
2. The Laconia map split, both bookmarks and all affected registry consumers agree on one combined-map provenance.
3. Country creation is immediate on success and produces a playable capital, forces, equipment, research and reinforcement path.
4. Every physical transfer, finite cohort, unique entity, paid operation and cleanup has an exact owner and one-time receipt. Cadre admission and all reinforcement preserve the authoritative renewable quota and conservative original-survivor attribution through proven native controls.
5. The five routes are substantial and preserve locks, support paths, setbacks, recovery and ordinary completion with evolution disabled.
6. Only the three public custom values and exactly three named tree-spirit slots exist, with at most three active spirits and one stage per slot.
7. Both land providers have complete owner contracts. Finite and unique consumers remain bounded, Spartoi shares one allowance across all owners, and general foreign mythic draws remain ineligible. Authorized derivatives preserve custody, origin, payment, global count and exact cleanup or remain blocked.
8. AI and player paths share legality, cost and authority predicates. Every row in section 8.4 has an actual implementation disposition and evidence path, with no unclassified action or counterpart response and unresolved probability evidence clearly marked.
9. The compact puzzle uses real geometry, the common territorial predicate and every required category attachment.
10. Required models, sounds, icons, flags, portraits and super-event packages have their separate provenance and native consumer receipts.
11. Shared Event Log, evolution views, country classifiers, CXT, cost and Chaos accounting remain coherent.
12. The actual improvement-loop and completion audits receive the complete accepted specification and disposition every material finding.

Static source checks prove source properties. GitHub snapshots prove what was committed at that revision. MCP analysis proves only its declared coverage. Model reimport proves an exported asset round trip. Native playback and campaign behavior need their own evidence. A document that mentions a previous successful tool run is not a fresh result for Event 111.

## Source references

The targeted read register and limitations are recorded separately in the source evidence appendix. The following references support the repository observations in this part. All refer to commit a3ef485c5da7e2337122eca04ac65c175050f251.

- R1: docs/spreadsheets/chaos_redux_events_catalog.csv, lines 228–242, and common/scripted_effects/chaosx_logic_effects.txt, lines 220–345.
- R2: docs/formables/state_registry/state_registry_index.json, metadata lines 1–46 and Peloponnese record lines 8205–8246.
- R3: paradox_wiki/State modding - Hearts of Iron 4 Wiki.md, lines 1–150, and paradox_wiki/Effects - Hearts of Iron 4 Wiki.md, lines 1033–1077 and 1225–1250.
- R4: docs/formables/state_registry/README.md, lines 1–67, and docs/formables/formable_state_puzzle_system.md, lines 1–136.
- R5: common/country_tags/chaosx_countries.txt, lines 1–44, and common/country_tags/006_independence_wave_countries.txt, lines 1–118.
- R6: events/019_infantry_spawn.txt, lines 1–180, and common/scripted_effects/019_infantry_spawn_generation_effects.txt, lines 2235–2355.
- R7: docs/systems/cbrn_warfare/chaos_unit_family_registry.md, lines 1–148.
- R8: docs/systems/universal_cost_modifier.md, lines 1–139.
- R9: events/071_persian_empire.txt, lines 1–161.

The current user brief, full Project Source Protocol, current AGENTS, event, state-ledger, AI/MTTH, GUI and subagent skills remain the primary supplied implementation rules. Parent acceptance of the mandatory map split and roster dispositions is recorded in the shared design contract and source handoff.

