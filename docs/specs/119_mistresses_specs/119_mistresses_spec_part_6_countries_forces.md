# Part 6. Alien countries, armed forces and territorial survival

## The country the alien player inherits

A playable brood should feel like a social network suddenly forced to become an army and a government. It knows the households, offices, railway yards and command posts through which it spread. It does not automatically know how to keep a continent supplied. Its opening advantage is local preparation, surprise and the bodies of adult aliens already present. Its opening danger is that the surviving human state still has aircraft, ships, armored formations and allies.

The first campaign is therefore about assembling a defensible country from an uprising. Secure a supply source, connect scattered territorial pockets, protect the finite adult recruitment pool and decide which captured systems to preserve. A successful brood then chooses how to fight a larger war. It can concentrate command and heavy organisms around an industrial center, or retain a more distributed command with mobile cadres and resilient peripheral garrisons. It can preserve machinery and conventional transport, or commit scarce military factories to organic equipment. These are choices about operational method, authority and survival. Every route remains an alien belligerent on the same side as other broods.

The human counterplay is legible. Hold railway junctions, deny ports, exploit exposed reserves, destroy isolated heavy formations and prevent separate revolts from joining. A small brood is a dangerous local insurgent country. A continental brood is a difficult land opponent. Neither gains a navy by being alien. The Mother of Mothers can transform the strategic scale only through the sustained territorial success specified in part 8. Unveiling begins a war that can be won, lost or contained.

All new country, unit, leader, route and institution labels in this chapter are working design labels. They are not proposed final localisation. All numerical tuning is a launch proposal, subject to the controlled balance cases in part 12. Native game capacity counts, derived arithmetic and the agreed combat-equivalent weights need not be multiples of five.

## Country identity and geographical expressions

Use one coherent species identity with several territorial expressions, rather than several unrelated alien ideologies. Create at most one initial brood per pre-revelation host, as specified in part 5. Its package selects an expression from its frozen origin and actual viable territory. Overseas holdings can belong to that same country without being connected. The expression informs opening choices, AI and art. It does not permanently prohibit a player from developing another capability.

| Expression | Starting fantasy and strategic advantage | Persistent problem | Useful opening direction |
| --- | --- | --- | --- |
| Metropolitan brood | Prepared networks seize an urban and industrial center. Captured workshops can sustain equipment and infrastructure repair. | Urban territory can be fragmented, fuel dependent and exposed to bombing. A seized capital does not guarantee a connected hinterland. | Preserve machinery, secure the nearest supply corridor, protect industry and contest human counterattacks. |
| Continental brood | Numerous inland networks produce connected territory and a comparatively broad adult recruitment base. | Long fronts, poor infrastructure and thin military industry make equipment replacement difficult. | Line formations, railway repair, distributed reserves and limited offensives toward industrial nodes. |
| Littoral brood | Port households and colonial networks create a coastal or island foothold with access to transport infrastructure. | Convoy losses, naval superiority and separated islands constrain expansion. A hostile fleet can isolate an otherwise strong land army. | Port defense, conventional transport preservation, coastal air protection and cooperation with other broods. |

Expression is selected from qualitative map facts, not a third public number. A mixed country can expose the opening associated with its capital while retaining other branches when their geographical conditions become true. Relocating a capital does not erase its original-host provenance or reroll opening rewards.

The displayed map identity should combine an alien emblem with a recognizable geographic anchor. Avoid a bureaucratic placeholder as the final country name. The exact tag is symbolic here as `BROOD_CARRIER_n`. Reservation requires a collision audit against the installed game, Chaos Redux, every enabled Workshop mod and local mod. A free-looking three-character string in the supplied files is not sufficient evidence.

Every carrier has a complete dormant definition, color, name pools, flag sizes, capital-resolution policy, history, technology access, characters, ideas, equipment graphics, focus access and AI. Dormant carriers own no accidental land, field no armies and do not run active-country behavior. Creation records an immutable brood generation ID separately from its reusable country tag.

## Territory, ownership and the capital

Part 5 owns the worldwide snapshot and influence-dependent state allocation. This chapter consumes its committed result. No country is created early enough to influence another participant's snapshot. Every eligible uprising uses the same pre-Unveiling information, and every host-war declaration belongs to the same committed transition.

The allocation should favor prepared, connected clusters around valid supply and administrative sites. Part 5 fixes the candidate thresholds, hidden readiness, population-weighted seizure caps and one-state exception. A one-state host becomes a full territorial brood only at readiness at least 75, cell presence at least 75, institutional access at least 60, the normal candidate adult minimum, a funded viable formation and verified human continuation. Otherwise it receives Part 5's finite nonterritorial insurrection. Influence determines both viable territory and the finite adults and stores available there. It does not justify claiming every host state or every colony. A state considered for transfer retains original owner, controller, original host, population ledger and occupation provenance. Where owner and controller differ, the transaction resolves both interests explicitly. An occupying army cannot be silently converted into alien forces, and a displaced legitimate government cannot lose its restoration claim without a specified settlement.

At creation, the country layer accepts only committed transferred states that the brood actually owns and controls. Later conquest can establish valid merger contact through a continuous controlled, passable land route linking each country's usable territorial component, even while legal ownership remains human. An isolated stranded occupation without that connection does not qualify. Sea adjacency, a shared sea zone, convoy access and nominal ownership through enemy control do not trigger absorption. Part 8's separate durable-holding rule governs Mother qualification.

Select a capital from the brood's committed territory in this order:

1. The prepared administrative center, if owned, controlled and usable as a native supply origin.
2. Another owned and controlled state with a valid supply source and a suitable victory point, favoring the strongest surviving prepared cluster.
3. A legal port-centered fallback if the country is maritime and the native supply rules permit it.
4. A remaining legal owned and controlled state, selected deterministically by the shared state identifier tie break.

This is a priority contract, not a claim that a scripted capital effect creates supply capacity. Verify actual supply-source behavior before promotion. If no legal state exists, do not create a nominal country with a fabricated capital. Keep the incident in its supported enclave or insurgent resolution until the common transaction has a legal territorial result. If the host loses its capital, its own native capital or exile behavior is evaluated before the transition completes.

State-scale transfer must not erase a surviving human enclave. Record the people and the unresolved locality through the occupation and evacuation adapter. A tiny human enclave can lack its own state on the game map while remaining a visible, consequential objective. The same rule protects a tiny alien foothold from receiving the whole population, industry and recruitable pool of a large state merely because the engine transfers ownership at state scale.

Capital loss after creation changes the supply and command problem. It does not restart Unveiling, restore spent equipment or create a new leader. A valid replacement capital is selected through the same priority. If all land is lost, the package enters defeat or a supported landless continuation. A surviving navy is not proof of sovereign land ownership.

## The complete opening package

The following values establish a playable starting country without turning creation into a free major-power package.

| Surface | Proposed opening contract | Development and failure rule |
| --- | --- | --- |
| Politics | A fictional alien authority, elections disabled, no ordinary human party competition. Use the installed compatible ideology carrier after inspection. | Centralized or distributed authority changes characters, command effects and focus access. It never changes the common alien war side. |
| Stability and war support | Stability 45 and war support 70 before inherited local crises. | High network preparation can improve the opening through part 5's bounded result. It cannot guarantee permanent maximum values. |
| Political and command resources | Political power 75, command power 25, army experience 15. | One creation receipt. Merger, reload and capital relocation never repeat these grants. |
| Research | Two base research slots and a narrowly defined operational technology package. | Three slots after an industrial or research-center anchor, four through sustained institutional development, five only after a substantial late-game payoff. Slots are entitlement maxima on merger. |
| Civilian economy | Existing usable factories, infrastructure, construction and damage from committed territory. No unconditional starting factory grant. | Repair and conversion compete with military equipment and consumer requirements. |
| Military economy | Existing usable military factories and finite captured stores. | No production output from enemy-controlled or damaged capacity beyond native rules. |
| Conscription | A dedicated zero-human-recruitment law or verified equivalent with native recruitable population fixed at zero. | Only explicitly accounted surviving adult aliens and qualified adult growth enter native manpower. Human residents remain civilians. |
| Trade and economy laws | A defensive wartime economy and a resource policy appropriate to a country excluded from normal human trade. | Later machinery and maritime branches can reopen permitted trade. No hidden resource creation substitutes for denied imports. |
| Fuel | Measured captured fuel only, bounded by the transfer receipt and native capacity. | Organic infantry does not consume fuel merely to create an artificial weakness. Trucks, aircraft and ships retain ordinary fuel requirements. |
| Air and navy | Only genuinely captured or transferred eligible assets with an inspected ownership path. Otherwise none. | No free carrier fleet, trained pilots, naval invasion transport or instant air superiority. |
| Starting ideas | Command disruption and infrastructure discontinuity occupy two focus-owned spirit slots. | The third slot remains available for the strategic settlement. Mother command replaces slot one. Part 7 defines replacements and the cap. |
| Unit access | Cadre and Line operational access. Siege is conditional on the actual funded heavy package and its production prerequisites. | Live role gates control recruitment after technology has been granted. Defeat does not pretend to unlearn a permanent technology. |

These resources are not compensation for every difficulty in the uprising. An island with no military factory starts with a finite force and a difficult supply problem. It receives a concrete survival route, rather than five factories and a fleet appearing from nowhere. A major-country revolt can inherit substantial industry, but it also inherits bombing exposure, damaged railways and a long front.

## Adult manpower and deployment

Use part 2's measured population accounts and part 5's frozen result. For each originating state, let `C` be the surviving adult alien cohort, `Hc` the measured absorbed registered adult civilian partners and `Hs` the measured absorbed registered adult service partners. The country's recruitment entitlement is the sum of:

`B = surviving C + floor(0.50 × (measured absorbed Hc + measured absorbed Hs))`.

This is a biological conversion budget, not a claim that all residents have become aliens. Civilian and service losses are measured before territory moves. The same person cannot appear in both categories. If the installed engine cannot measure the service-partner subtraction from existing formations, the shared service adapter is a release requirement. Subtracting those people from civilian population a second time is not an acceptable substitute.

Partition `B` once into committed field manpower and reserve. Proposed opening deployment shares are 30% for an isolated or unsupplied cluster, 45% for an ordinary viable cluster, and 60% only for a strongly prepared cluster with a controlled usable capital and depot connection. These are snapshot classifications under part 5, not a public readiness meter. Every adult not committed stays in the accounted reserve or the explicit nondeployable remainder. The sum must equal the measured entitlement. Creation also measures and neutralizes any automatic native recruitable credit caused by state ownership through the verified shared adapter. A zero-conscription law alone is not proof that an earlier automatic credit was removed.

Allocate committed manpower initially at 35% Cadre, 60% Line and 5% Siege. If the heavy prerequisites are absent, move the Siege allocation to Line. A heavy opening requires at least 10,000 adults in total entitlement, five usable controlled military factories and a supplied legal deployment site. Arithmetic results need not be multiples of five. Do not round up a formation, battalion or equipment bill to make a small country look impressive.

These allocation weights are planning preferences. If splitting a tiny committed share would prevent every legal formation, consolidate that same finite share into one Emergency Cadre. This redistribution creates no extra adults. Its funded full-equipment bill is proportional to its actual funded adults, rounded down to whole equipment, before the opening readiness factor is applied. For example, 50 actual adults authorize ten Cadre equipment at full issue, then six, seven or nine at 60%, 75% or 90% readiness after integer rounding. The implementation must verify separately that native manpower and equipment fill can express those real quantities.

A brood with 100 deployable adults may receive a one-battalion Cadre at its verified supported understrength level. Territorial creation requires at least 50 actual deployable adults and their finite equipment, representing at least 20% of that battalion. It does not receive a full 250 adults. If exact understrength creation is unsupported and a complete legal formation cannot be funded from the committed share, Part 5's nonterritorial local-insurrection outcome replaces territorial creation. Reserve people are not a second fielded army. Empty templates are not armies and must not create merger strength.

Subsequent reinforcement consumes that country's native alien manpower and actual equipment. New adult recruitment uses the shared age and cohort rules. Births, children, captured unregistered human civilians and combat kills do not create immediate recruitable soldiers. No focus converts a percentage of all state residents into manpower. Preservation and restraint may improve occupation outcomes, but they do not turn the surviving human population into an ordinary alien conscription base.

## Equipment, templates and initial forces

Each family has its own concrete organic equipment and readable production line. The equipment represents replaceable protective structures, metabolic stores and specialized organs. Manpower still represents adult alien combatants. Factories can produce equipment without manufacturing unaccounted adults.

Proposed basic bills are 50 Cadre equipment per 250-adult battalion, 100 Line equipment per 500-adult battalion and 25 Siege equipment per 250-adult battalion. The low count of Siege equipment is compensated by much greater industrial cost per item. Initial cost targets are five IC per Cadre item, five per Line item and 25 per Siege item. These are provisional industrial balancing values, not measured vanilla equivalence. Later tests compare cost, frontage, manpower, supply and replacement time together.

Initial organic equipment is a finite one-time entitlement attached to the frozen deployment plan. Assign the funded template bill at 60%, 75% or 90% readiness for the isolated, ordinary or strongly prepared opening respectively. Reserve replacement equipment is at most 25% of the issued organic bill. Both portions consume the same state-origin manifestation receipt. The underlying organic mass authorization is the fixed bill of those funded adults and their equipment, not a renewable currency. Equipment from a different host or a later merger cannot recalculate this authorization.

Separate captured human stores from newly manifested organic stores. Captured conventional equipment keeps its actual type, variant and provenance. Trains, trucks, infantry weapons, support equipment, convoys, aircraft and ships are available only where the transfer transaction truly delivers them. A captured airplane type does not imply an unlimited domestic production license. If equipment that cannot legally be operated or replaced remains in the inventory, its limitation must be visible.

The practical opening OOB uses the following proposed formations. Battalion composition is concrete, while exact native grid placement and width compatibility require the installed-unit review.

| Formation working label | Proposed combat composition | Full adult manpower | Full organic equipment bill | Opening use |
| --- | --- | ---: | --- | --- |
| Emergency Cadre | One Cadre battalion | 250 | 50 Cadre | The smallest legal country defense, below full strength when the measured budget requires it. |
| Cadre group | Five Cadre battalions | 1,250 | 250 Cadre | Mobile screening and urban or forest operations. |
| Line formation | Five Line battalions | 2,500 | 500 Line | Main front and corridor defense. |
| Breach formation | Three Line battalions and one Siege battalion | 1,750 | 300 Line and 25 Siege | A funded, supplied heavy opening or later paid recruitment. |

Formation counts are calculated from the committed adult allocation, not fixed per country. Fit complete formations first, then the supported understrength result, and keep unfunded or undeployable adults in the same reserve ledger. A mixed formation must satisfy both family budgets simultaneously. Adding a support company also pays its actual adults and equipment, so the combat-only totals above cannot be reused as all-inclusive totals. Do not create a separate near-identical template for every regional expression. Use homogeneous showcase templates in CXT separately from practical mixed fighting formations.

Supply and transport support initially use compatible vanilla engineers, logistics and reconnaissance where the operating country has the technology, equipment and adults to sustain them. Support companies consume manpower from the same alien pool. Do not add human service crews without accounting for who they are. No unique organic support subunit is necessary for launch merely to increase the roster.

Initialization order is ownership and control, legal capital, characters and politics, laws and live role gates, researched operational dependencies, templates, paid stores, and finally units. The spawning layer must account for the documented fact that an OOB `start_equipment_factor` does not debit stockpiles. A fully equipped spawn plus an undebited stockpile grant would duplicate the same stores. Either the reviewed creation path consumes its issue allocation correctly, or the receipt explicitly subtracts the issued quantity once. A repeated `load_oob` is forbidden as a refresh mechanism. Province IDs are used for land and naval deployment, while air-wing location uses state IDs. These are distinct native scopes. [U][E]

## Three organic combat families

The event justifies three new land combat types because its battlefield identity requires light remnants, durable transformed line troops and genuinely large breach organisms. Existing ordinary alien infantry cannot communicate all three transformations, counters or tactical weaknesses. Three families also provide a manageable asset and balance surface. They do not justify separate aircraft, ships, artillery species and a complete replacement equipment tree at launch.

### Cadre

Cadres are adult infiltrators retaining enough human scale and trained behavior to use buildings, narrow routes and captured transport. Their alien silhouette becomes evident in movement and close contact. Their battlefield role is reconnaissance in force, screening, raids against weak positions and emergency defense of disconnected territory.

The proposed battalion is 250 adults, 50 equipment, movement speed five km/h, organization 55 and a 60-day training requirement. Combat width and native categories must use an inspected compatible definition. Relative to equal-manpower contemporary infantry, target 75% sustained soft attack, 75% open-terrain defense and 125% reconnaissance utility where that utility is actually represented by a supported modifier. Avoid representing this last target as a fictional combat stat. A supported terrain or recon implementation is selected during unit authoring.

Cadres should be effective in urban areas and forests, with a proposed 15% local movement or combat advantage confined to the appropriate supported modifiers. They have little armor, weak hard attack and poor staying power against prepared artillery. Their speed does not allow teleportation, travel through blocked straits or automatic infiltration behind a front. Training, casualty replacement and transport still matter.

Recruitment is available to active broods with the operational package and to an explicit CXT test fixture. Event 19 can supply them only through the registered family provider and its actual paid obligations. Their merger combat-equivalent weight is 1.00 per surviving adult, applied once.

### Line

Line organisms are the transformed mass of the revolt. Their protection and organization let a brood hold land, but their dense bodies and metabolic requirements make supply central. They should look unlike both ordinary infantry and the large Siege silhouette.

The proposed battalion is 500 adults, 100 equipment, movement speed four km/h, organization 60 and a 90-day training requirement. At equal manpower and broadly comparable industrial cost, target 110% soft defense, 110% soft attack and 75% hard attack. Low piercing preserves the value of human armor. Their protection is primarily durability and defensive staying power, rather than armor that early human weapons can never penetrate.

Supply consumption should be 25% above an equal-manpower infantry reference before national modifiers. Fighting efficiently from a stocked rail corridor is their strength. Prolonged attacks through deserts, mountains and destroyed infrastructure are their weakness. No broad national supply immunity removes this identity. The machinery route can support them with trucks and logistics, while the organic route improves replacement efficiency at the cost of industrial flexibility.

Recruitment requires active brood identity, the proper organic equipment technology and an ordinary paid training queue. Advanced versions improve one clear property at a time, such as durability or industrial efficiency. Their merger combat-equivalent weight is 1.50 per surviving adult, applied once.

### Siege

Siege organisms are large adult-derived breach forms with a distinct gait, attack and death profile. They are a concentrated investment for breaking fortified infantry positions. They are neither main battle tanks nor a universally superior Line upgrade.

The proposed battalion is 250 adults, 25 heavy organic equipment, movement speed three km/h, organization 30 and a 120-day training requirement. At equal manpower, target 150% soft attack and 150% breakthrough against the intended infantry role, balanced by the much greater equipment cost. A proposed 25% fort attack benefit is the specialty. Piercing remains limited, armor is tested against the contemporary human anti-tank tier, and no unpierceable value is assumed.

Supply demand should be at least 150% of the equal-manpower Line reference. River crossing and difficult-terrain penalties remain substantial. Concentrated air attack, anti-tank fire, encirclement and exhausted equipment stocks are human answers. Siege equipment is slow to replace and should be a poor garrison choice. A country that cannot keep Line formations equipped should rarely add more Siege battalions.

The first access requires the heavy industrial and supply anchor. Advanced access requires the appropriate technology and a completed production commitment. A tiny country can eventually earn and fund one, but the template never bypasses actual adults, equipment and site constraints. Their merger combat-equivalent weight is 3.00 per surviving adult, applied once.

### Shared balance discipline

These targets describe intended relative behavior. They are not a completed native stat file. The implementation worker must compare equal manpower, equal frontage and equal industrial cost separately. None of those comparisons substitutes for the others. Stack limits must include unit stats, equipment, technologies, doctrine, commanders, spirits and terrain. A 15% family improvement cannot be balanced as if three other 15% layers were absent.

The launch roster uses compatible native categories and map-icon categories selected after inspection. Inventing a new engine `type` or `map_icon_category` is not permitted. A custom category or group needs its proper definition and all consumers. Native division caps require compatible locked-template behavior and do not arise from a displayed description. [U]

## Research, production and conventional capabilities

The operational technology package unlocks only what the country needs to exist and field its funded opening. It should be a grant-only package on the supported technology surface, not a free completion of the host's entire research tree. It contains Cadre and Line foundations, the associated equipment and verified basic support and transport prerequisites. The selected native technology IDs must be resolved against the installed game.

Captured research is a specific provenance transfer. The brood can acquire demonstrated industrial, electronics and equipment knowledge from its actual host network or retained research facilities. It does not receive every nation's latest tank, nuclear, naval and air design merely because worldwide Unveiling occurred. Advanced conventional equipment requires the appropriate research, usable production capacity, resources and, where applicable, an imported valid variant definition.

Organic research has a small set of consequential families. Adaptation improves a selected combat property. Sustainment improves equipment replacement or attrition tolerance. Heavy morphology enables Siege production. Coordination improves command or support compatibility. Each competes with industry, logistics, anti-air and ordinary transport research. Avoid dozens of technologies that each add an invisible two-percent modifier.

The retained-machinery route values existing civilian and military factories, conventional supports and transport. The dedicated-organic route increases organic equipment efficiency but leaves conventional aircraft, ships and motorization harder to sustain. Neither route creates a second economy outside the native production system. Resource requirements are chosen from installed resources and justified by the actual equipment bill. Unsupported fictional resources are not silently added.

The opening doctrine contract gives each brood a valid installed land-doctrine selection suited to its initial Line-centered army, with no free completion of the host's doctrine mastery. Centralized and distributed routes can supply bounded experience and supported mastery investments in that same doctrine framework. Any custom Chaos Warfare interaction must respect the current grand-doctrine and subdoctrine architecture and the cumulative unit budget. Do not create an obsolete parallel doctrine technology tree or inherit mutually exclusive mastery from both sides of a merger. [T]

No DLC is required for the core army, production, research, decisions, coalition or Mother war. Intelligence agencies, military industrial organizations, special projects, designer variants and native faction systems can enrich the package when present, with a complete base-game path for the same strategic function. A player must not need an optional project facility to unlock the only working organic equipment line.

Granted technologies can be effectively permanent. Cleanup disables inappropriate production, recruitment, provider access and country-role behavior through live gates. It does not promise that setting a technology to zero reverses unlocks. Research union on merger uses the supplied compatible-technology helper and the exclusive-branch policy in part 10. Technology provenance, completed research and legal capability access are different records. [T]

### Adult replenishment during a long war

After an industrial maturation anchor, a brood can grow new adult alien replacements through paid, finite incubation. This is a distinct post-Unveiling biological production process. It does not reuse human childbirth, absorb surviving residents or claim that a combat kill yields another soldier. The process is available to both economy routes, with organic specialization reducing its equipment burden.

The launch batch reserves 50 existing uncommitted adult aliens as living noncombat staff, consumes 250 Line organic equipment and 50 support equipment, and takes 90 days at a legal owned, controlled, supplied industrial site. It produces 100 mature adult aliens. Fielded soldiers, assigned escorts and staff already reserved elsewhere cannot simultaneously meet this requirement. The staff remain alive but unavailable for deployment until released, and are returned once if the site survives. Payment and output have separate durable receipts. A site supports one batch, with at most five simultaneous batches in a country. Factories must genuinely produce the consumed equipment. Possessing five military factories is not a substitute for paying the bill.

The country-wide monthly release ceiling is the smaller of 500 adults and 5% of the living adult-alien population recorded at that month's opening, rounded down. Completed adults beyond the month's remaining allowance wait in the same physical maturation record. They are not separately counted as recruitable reserves. On merger, release already consumed by all components counts against the unified allowance, and the larger valid pre-merge allowance can be honored without summing duplicated entitlements. New allowances use the combined actual population at the next monthly boundary. Tag reuse and capital relocation cannot refresh a ceiling.

Already paid batches from merging donors are grandfathered even if their combined number temporarily exceeds five. Keep each physical site, staff reservation, elapsed time and payment receipt intact. Admit no new batch until fewer than five remain active, and subject every completion to the one unified monthly release allowance. Do not cancel paid commitments, restart their clocks or create one replacement output per donor tag.

A destroyed or captured site stops its batch and resolves its actual staff, pending adults and consumed stores once through the shared population and capture adapter. An early voluntary cancellation returns only verified unconsumed inputs. A blockade can stop production before payment, while occupation can destroy progress after payment. Neither produces an automatic full refund. Machinery specialization pays the full bill. The organic route can reduce the Line-equipment input to 200 after a substantial commitment, while preserving the same adult-output cap and maturation period.

All processing visits the registered active batches. There is no daily worldwide population search. Native medical recovery can remain available where the installed support rules permit it, but no additional scripted percentage of all battlefield deaths is resurrected. This controlled, costly replenishment supports a long campaign without eliminating the human strategy of destroying alien armies faster than they can recover.

## Leaders, government and national spirits

Each playable brood starts with a readable governing personality or institution and a small useful officer cadre. A centralized command has an adult alien sovereign and subordinate specialists. A distributed command has a council or coordinating institution, represented with institutional naming and people-free institutional art. It must not receive a random human personal name simply because the native leader slot expects a character.

The opening authority is selected before politics are finalized. Characters and any runtime generation templates are registered through the verified history path. An unregistered midgame recruitment call is not presumed to work. Each character has a durable identity, role eligibility, portrait set, death or retirement rule and merge disposition. Country leaders with advisor roles need both leader and advisor portrait sizes. Female human guise identities use female metadata and appropriate female name pools. Wholly alien forms receive their own fictional visual identity. [C]

Initial commanders should include a competent line commander and a mobile-operations specialist. Their skill distribution should leave room for experience. A third heavy specialist can arrive through the actual Siege commitment. Do not set every alien commander to maximum skill or distribute mutually stacking all-purpose traits. Low native skill integers are structural values, not an exception intended to evade the five-multiple tuning convention.

Use three focus-owned spirit slots across the entire brood tree:

| Slot | Initial state | Development | Crisis and endgame handling |
| --- | --- | --- | --- |
| Command | Command disruption, proposed organization recovery −20% and planning speed −15%. | Replaced by centralized or distributed command and later upgraded within that same identity. | Capital disruption temporarily replaces the command form. Mother command and the later severed-command aftermath also replace this slot. Restoration returns the attained tier without granting it twice. |
| Economy | Infrastructure discontinuity, proposed production-efficiency growth −25% and supply use +15%. | Repair and economy commitments replace this with machinery or organic sustainment effects. | Encirclement or transport crisis replaces the relevant tier only when necessary. Do not add a fourth spirit. |
| Strategic settlement | Empty at creation. | A later occupation and war policy can occupy it with a real tradeoff. | Occupation policy remains in this slot during Mother command and aftermath. Any later settlement replaces its previous tier. |

Native laws, leader traits and territorial modifiers still need a cumulative balance review. They must not be used to hide a pile of focus rewards outside the cap. A brief mission-specific modifier can express a temporary operation, but repeated timed ideas are not an acceptable way to simulate ten permanent spirits.

## War, faction and peace

Every committed brood is immediately at war with its actual host and joins the same alien side. The war adapter also resolves any occupied territory and existing faction war so that a brood cannot accidentally fight another brood through inherited diplomatic relationships. A revolt in occupied land is hostile to both the relevant human host and the actual human occupier, as part 5 requires. Do not copy the human host's alliances, guarantees or faction obligations wholesale. A fictional alien faction is the common relationship container where the native system permits it. War-side consistency is the binding rule even when a particular faction mechanic is unavailable.

There is no independent alien diplomacy path that starts a civil war against other broods. Centralized and distributed authority remain compatible members of the same side. Trade or negotiation with humans is limited to explicit supported arrangements. Part 8's temporary civilian evacuation agreement is not permission to sell the alien alliance into a separate human faction. A general negotiated peace leaving a sovereign armed brood contained is outside the launch design.

Initial war goals and territorial claims follow origin and actual uprising territory. They do not make the entire world a core. Captured human land retains occupation consequences. Alien military manpower remains separate from those residents, and reconstruction requires administration. A focus can reduce a particular occupation burden through a funded policy, but it cannot cure all resistance globally.

Human coalitions form through the reaction pathway associated with Tin foil hat and the existing diplomatic framework. The initial human response need not erase every preexisting war. It should make anti-alien cooperation possible and increasingly attractive as the threat becomes visible. Requests for access, coordinated pressure and expeditionary support use supported native diplomacy. Ordinary effects cannot draw or execute player battleplans, and AI strategies can only influence legal native operations. [D][A]

Peace has several concrete states. A local brood can be destroyed. A defeated nonterritorial cohort can be contained through Part 5's actual isolation rules. An armed territorial remnant remains a belligerent until a genuine military outcome. A human host can reconquer and restore territory, with occupation and displaced-government rules respected. An alien victory can create a continuing occupied order with reconstruction and military rivalry against surviving human powers. Mother defeat ends supreme command rather than deleting all alien countries. No early peace automatically gives the alien player control of all original-host territory or cancels the human endgame objectives.

Peace-conference and scripted settlement handling must be tested with existing human wars, subjects, colonies and faction leaders. A scripted territorial restoration is a specific transaction, not a blanket annex command. State provenance survives every merge so the proper human claimant can be considered later.

## Absorption and player continuity

The merger interface is `MERGE_COMPONENT(snapshot_id, member_generation_ids)`, a design contract owned by part 10. It is not a claimed native effect. Freeze the valid controlled-land graph, determine its connected components and select one recipient per component before any assets move.

Rank members by surviving adult alien combat-equivalent strength, then usable military industry that is both owned and controlled, then the lower immutable brood registration ID. Combat-equivalent strength weights Cadre 1.00, Line 1.50 and Siege 3.00. Count actual surviving adults once. If the native measurement already reflects losses, do not multiply the current strength fraction a second time. Prior committed merger survivors count under their current owner. Same-batch incoming assets, pending spawns, human civilians, captured ordinary human formations, allied expeditionaries and duplicate references do not inflate the rank.

The recipient preserves the full surviving force and asset union required by the user. This includes the exact native capability questions for land, naval and air units, equipment, characters, commanders, experience, research and production. A documented land-division annex effect is not evidence that every carrier, wing, assigned commander and variant will survive. If the installed ownership path cannot conserve a class, its adapter or supported engine extension is a release requirement before destructive transfer. Do not replace an irreplaceable veteran army with a numerically similar fresh OOB and call it preservation.

The recipient's political route and incompatible economic or doctrinal commitment persist. Donor permanent territorial rewards, legal capabilities and compatible research transfer once with provenance. Research-slot entitlement is the maximum attained entitlement, never the sum of all donors. Donor focus receipts prevent repeating a completed factory, research, manpower or stockpile grant. In-progress focuses and incompatible research require an explicit continuation or compensation rule based on verified native support, with no repeated completion payoff.

A human player does not veto compulsory absorption. The player does receive a supported continuation in the recipient. Where both merging countries have human controllers, verified co-op control or an explicit supported observer handoff must preserve both sessions. Silent AI replacement, forced disconnection and an unannounced game-over screen are unacceptable. This is an engine capability gate, not a request for extra consent to the merger. Player handoff occurs only after the recipient package and ownership result are valid.

A host player is offered the event's supported choice to remain with the human state or continue with the generated alien country. The choice does not change the frozen allocation, secretly improve the alien army or grant knowledge to every human opponent. If the human state becomes an exile, its continuation follows the installed game's actual support. If no viable player-owned country remains, the supported observer or recipient route is made explicit.

## Mother war and aftermath

The Mother is never obtained merely by finishing the last focus. Part 8 owns the strict Chaos greater-than-1000 requirement, sustained multi-region success, frozen population and industry denominators, continuous qualification period and shared world-end arbitration. The country package supplies valid ownership, control, origin-capital and force records to that predicate.

The actual Mother leader character exists only in the selected host polity. Other broods retain regional governors under her supreme command. Noncontiguous countries remain separate until the normal land-contact merger rule applies. If her host merges, her unique character and lair record transfer once. At accession, central command creates a playable operational problem. The alien side has a powerful supreme authority and concrete command dependencies. Human countries receive the discoverable weaknesses and lair objectives specified in part 8. Existing alien units remain funded finite units. There is no automatic global manpower replenishment, universal organization immunity or invisible instant reconquest.

On Mother defeat, replace the command spirit in slot one with the 60-day severed-command aftermath specified in part 8. Retain territory, surviving forces, research and valid leaders. Each surviving brood can stabilize, retreat to a defensible perimeter, support Part 8's limited civilian evacuation agreement or continue the war. Such an agreement does not end its belligerent status. Distributed institutions retain useful continuity tools, while centralized institutions can retain a stronger concentrated army. Both experience the shared 60-day command shock, with their route distinction expressed through available recovery operations rather than shortening the mandatory shock. Neither route changes the historical fact that the Mother was defeated.

The fixed relay set, finite guardian, one connected-land relocation, final mission and no-respawn outcome remain exactly those of part 8. Route rewards cannot bypass relay isolation or grant a replacement guardian after genuine defeat. Human reconquest resolves population, displacement and surviving-enclave records. It does not respawn everyone absorbed or erase wrongful purges. Alien success likewise requires occupation and production after victory. The campaign continues through actual countries rather than a final screen that discards the war.

## Shared unit integration and independent testing

Cadre, Line and Siege each have a distinct shared unit-family entry under one Event 119 provider. Their availability depends on actual brood identity or an explicitly supported test or derivative context, paid adult-alien and equipment commitments, and the final family capability. Generic human rewards must not create an unbounded alien breeding army or activate the parent invasion. The provider has real payment, cleanup and parent-isolation obligations.

The CXT test package groups the three families and practical formations at valid retained family sites. It must test the units without starting Mistresses or manufacturing civilian history. Registration, templates and actual deployed units have separate proof obligations. Daily fallback registration cannot become daily resource or army grants.

The complete native metadata, callback, CXT and source-evidence contracts are preserved in [Country execution notes](119_mistresses_country_execution_notes.md). Those notes are implementation evidence and handoff details, while this chapter defines the country and force design.

## Visual and audio package

The full production contract is in part 11. This chapter requests a coherent alien family identity with three distinct battlefield silhouettes. Cadre remains adult and human-scale in disguise but moves with a recognizable alien articulation. Line is broader, armored and clearly organized into a formation. Siege has a much larger silhouette, different gait and a visible attack cycle. Sharing the exact same model with a color change would fail the intended combat readability.

Each family needs its own 3D binding, equipment illustration, native counter and tested animation set covering idle, movement, attack and death. Any scale reference must be selected from the installed assets by the future worker. No named vanilla asset, measured model height or inspected palette is claimed here. Counters use the required vanilla-green treatment sampled from the actual source and preserve legibility at ordinary map zoom.

Country flags require normal 82×52, medium 41×26 and small 10×7 runtime sizes. Regional expression can vary the composition within a common species emblem system. Mother authority changes the command symbol rather than pretending all regional cultures and flags never existed. Fictional emblems must remain readable at the smallest size. Alien leaders and human guise portraits have separate briefs and cannot be assembled from unlicensed identifiable portraits without provenance.

Unit audio must be supplied from licensed existing files, with source and license recorded. No recording, synthesis, generated sound or hand-authored imitation is requested. Specify footsteps or locomotion, attack, impact and death variants, attenuation and animation synchronization. Disable accidental inherited ordinary infantry speech where it contradicts the creature. Audio coverage, model coverage and counter coverage are promoted together, not deferred behind a working stat definition.

## Country evaluation cases

| Case | Required observable result | Design failure to reject |
| --- | --- | --- |
| Tiny island | A funded viable understrength Cadre and legal capital, or Part 5's nonterritorial host response. Port blockade has real consequences and no navy is invented. | Free full army, empty country, free industry, overlapping CXT family sites or automatic overseas land connection. |
| Major industrial host | A substantial influence-dependent revolt, mixed fronts, useful captured industry, human armor and air counterplay. | Whole-country annexation from a modest network or unrestricted inheritance of every host technology. |
| Colonial host | Distinct territorial components, original-host and local-owner provenance, feasible transport limits. | A colony teleports forces to the metropole or receives all metropolitan stores twice. |
| Occupied territory | Owner and controller remain distinguishable, armies and civilian losses accounted, restoration claims retained. | Occupier units turn into aliens, or the legitimate owner silently disappears from settlement. |
| Host exile | Valid human continuation or explicit supported alternative, capital and war membership reconciled. | A second empty tag created as a substitute for working exile support. |
| Human player in weaker brood | Recipient route, army, equipment and character continuity after compulsory absorption. | Silent AI replacement or destruction of veteran units followed by a fresh equivalent OOB. |
| Two human broods merge | Verified co-op or supported observer handoff, both sessions preserved, same deterministic recipient. | Rank changed to avoid the requirement or an unverified player-transfer promise. |
| Naval and air isolation | Ordinary fuel, ports, convoys, range and superiority still constrain operations. | Scripted invasion plans, free carriers or aircraft appearing outside the transfer ledger. |
| Mother defeated | Supreme command ends, local broods persist, forces remain finite, human victory can be completed. | Every brood is deleted, or the Mother immediately reappears through a focus receipt. |
| Reload or repeated callback | No repeated creation, stockpile, technology, manpower, focus or CXT grant. | A retry silently doubles an OOB or reopens a spent population entitlement. |

## Source basis

The source anchors used above and their complete pinned repository receipts are preserved in [Country execution notes](119_mistresses_country_execution_notes.md). They support the design without claiming native runtime validation.
