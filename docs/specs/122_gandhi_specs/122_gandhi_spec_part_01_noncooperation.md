# 122 Gandhi, Part 1: A worldwide refusal to cooperate

Gandhi calls on occupied communities to stop sustaining the governments that rule them. Work continues for local survival, but the occupying power loses the benefit of that work. Administrations encounter empty recruitment lists, unusable production, withheld resources and a movement that insists on actual independence. The refusal is peaceful and finite. It can win a negotiated settlement, exhaust itself, or help create an international political organization that outlives the original campaign.

The player can release territory, negotiate a complete settlement, absorb a temporary economic and military crisis, or exploit the movement's failure under a fascist government. Later choices determine whether the Peace League remains voluntary, accepts national nuclear deterrence, or follows Gandhi into compulsory world peace. The peaceful route has its own useful institutions, achievements and durable outcomes.

## Event identity

| Field | Design value |
| --- | --- |
| Proposed event identity | 122 Gandhi |
| Original catalog identity | 133 |
| Proposed event type | Minor Fire-Once |
| Proposed Chaos threshold | 1 |
| Proposed cluster and severity | Liberations, High |
| Historical brief status | To Be Reworked |
| Current catalog status | Unavailable |
| Chaos level | 1 |
| Cluster | Liberations |
| Cluster severity | High |
| Mechanical centre | Worldwide independence demands and finite noncooperation |
| Personal centre | One Gandhi, whose life, location and authority remain consequential |

All newly introduced action, branch and institution labels throughout this package are working labels for implementation discussion. They are not finished localisation. Gandhi, Peace League, Nuclear Pacifism, Loss of Morale and The Ultimate Society of Peace and Nukes are names supplied in the brief. Player-facing wording remains governed by Part 11.

The event has one global firing receipt. A report, acknowledgement, reload or multiplayer client cannot create another incident. Its later decisions and institutions are the aftermath of that firing, with their own bounded lifecycles.

### Natural selection and an empty world

Natural selection requires the event to be enabled and unfired, no already resolved shared world ending, and at least one valid non-core holding. It uses the current shared event cadence and ordinary eligible-event weight, with the requested High membership in Liberations. The current source baseline is weight 1000 and a normal 45 to 60 day global event interval. These are shared-system settings, not a new Gandhi recurrence timer. The event does not require a human holder, a major, an Indian state or a particular starting date.

The selector may choose a report actor, but that actor does not become the only affected country. A direct manual request with no valid holdings returns a truthful unavailable reason before creating the incident or consuming its fire-once receipt. A state list becoming empty during final preflight aborts without invented targets. A later valid request can still fire it once.

The absence of a consenting host for Gandhi does not excuse existing holders from the worldwide demand. Local noncooperation can run while his hosting remains unresolved. League founding and personal late routes still require his actual lawful location and freedom.

## The opening

The incident identifies every living country holding non-core land. Human players, AI minors, majors, subjects, unusual governments and countries on remote continents receive the same eligibility examination. A country whose entire territory is core land can respond as an observer, mediator or potential supporter. It receives no fabricated occupied state.

The opening has three simultaneous layers.

1. A worldwide report establishes the movement and its demand for sovereignty.
2. Each affected holder receives its own exact territorial case and a fourteen-day response window.
3. Gandhi seeks a lawful place to organize, using the character and hosting rules in Part 6.

Acknowledging the worldwide report changes no ownership and grants no nuclear, diplomatic or military power. The holder's case distinguishes owned territory that it can release from foreign-owned land that it controls during a war. The latter requires an actual settlement with the people who can lawfully deliver sovereignty.

The initial choices are a commitment to independence and a refusal. A commitment immediately executes ready, uncontested releases. Where a war or claim dispute prevents execution, it opens one thirty-day settlement mandate with its required participants and exact outstanding obligations. A promise has no success value. Unfulfilled portions become refusals when the mandate expires. The player can settle individual bundles later, but the initial offer cannot conceal an indefinite occupation behind a negotiation flag.

## What counts as holding non-core territory

The substantive target is foreign land for which the current holder lacks a core. The selection cannot rely only on `owner != controller`, because annexed occupations often have the same owner and controller. It cannot require resistance already above zero. High compliance, a tiny population, a strong garrison or an unusual country tag does not exempt a valid non-core holding.

| Situation | Treatment |
| --- | --- |
| Owned and controlled non-core state | Demand addressed to its owner and controller as one holder |
| Foreign-owned non-core state under wartime control | Controller receives the local campaign. Owner and claimant join the settlement case |
| Subject owning or occupying non-core land | Subject receives its own local case. An overlord is included only where its consent or authority is actually required |
| A beneficiary already exists | Negotiate return or accession of the affected territory to that living sovereign country |
| Dormant homeland with a valid release identity | Offer a genuine independent release through Part 2 |
| Competing homeland claims | Demand remains active while an exact accepted allocation is negotiated |
| No attested national identity | Examine a coherent territorial civil council package. Do not invent an ethnic nation or silently exempt the state |
| Controller's genuine core | Outside this campaign, even if another country also claims it |
| No living controller | Keep an unresolved ownership case where relevant. Apply no modifier to a nonexistent country |
| State with no native resistance system | Preserve the same independence and output-denial intent through an attested state adapter. Do not create fake resistance values |
| Mixed province control | Use the installed engine's authoritative state relationship and verify output effects. Do not multiply the incident by province |
| Newly acquired non-core territory during the campaign | Enters through a scoped control or ownership callback and inherits the remaining campaign window |

A new core removes a state only when the core is a genuine result of another accepted mechanic. An event-local cosmetic core used solely to evade the demand is prohibited. Legitimate integrations from other systems still occur and are recorded with their own cause.

## Non-fascist refusal

For each active non-fascist occupation, both current resistance and current compliance become zero. They remain zero for the local campaign. This represents organized noncooperation outside the native violent resistance abstraction. It does not mean the territory has become content or productive.

The occupier receives no useful factory output, resources or recruitable manpower from those states. This is an independent requirement. Setting compliance to zero is not accepted as proof of full denial. Occupation laws, collaboration bonuses, export calculations and other modifiers must not restore useful output while the campaign is active.

Local civilian production is described as serving local survival. The mechanic does not repeatedly kill the population, delete buildings, destroy the country's existing stockpile or remove soldiers already recruited before the refusal. It stops new benefits attributable to affected land. Factories, resources and manpower belonging to unrelated core states remain usable.

Part 13 requires installed-game evidence for the exact output adapter. If the current scripting surface cannot prove all three denial channels, implementation remains incomplete. A guessed compliance modifier or a national penalty that damages unrelated states is not an equivalent delivery.

### Loss of Morale

The host also receives one temporary Loss of Morale variant. Its severity follows the share of the country's usable economy denied by active occupations, the breadth of the dispute, and whether it is fighting a demanding war. It does not stack once per state.

The central tuning anchor is a temporary reduction of fifteen percentage points in war support and ten percent in division attack and organization recovery. The intended bounds are ten to twenty-five war-support points and five to fifteen percent for each military effect. A country with one economically marginal occupation is near the lower bound. An empire losing a large fraction of usable output while fighting a major war approaches the upper bound.

These are authored balance anchors, not measured engine results. The implementation must verify how the installed modifier expresses war-support points and remove only this event's contribution on expiry. Do not repeatedly subtract permanent war support or restore a stale snapshot that overwrites later political changes.

Releasing some territory reduces the current burden. Releasing every active bundle ends the spirit immediately. A country that keeps refusing can outlast the movement. Its existing army remains capable of fighting, though the loss of occupation benefits and morale can make a long war much harder.

### Interaction with resistance

Event 106 Resistance must treat an active noncooperation state as protected from its write. The wave can report that protection, but it neither adds resistance nor stores an unpaid addition for later. An uprising event cannot use a suppressed wave as evidence of violent mobilization in that state. Separate, already active uprisings retain their own ownership and lifecycle.

When local noncooperation ends, normal resistance and compliance rules resume from the then-current state. Old compliance is not restored as a windfall. Old resistance is not replayed. A later genuine Event 106 firing affects the state normally if it remains eligible. Gandhi has no permanent resistance immunity.

## The fascist exception

The brief deliberately gives fascist governments a different result. Their refusal does not trigger economic denial or Loss of Morale. The noncooperation campaign fails locally and can consolidate the occupation.

Each affected state receives a one-time reduction of twenty resistance points and an increase of ten compliance points, clamped to native limits. A finite control-reinforcement variant then helps retain that improvement using supported native occupation modifiers. Its duration cannot exceed the remaining campaign window. The intended ongoing anchor is twenty percent faster compliance gain and twenty resistance-target points of relief, subject to installed-unit verification.

The one-time state receipt belongs to the global Gandhi incident. Changing ideology, transferring the state among allies or returning to a previous controller cannot collect the same benefit again. The continuing treatment follows the current recognized government ideology. A transition into fascism removes non-fascist denial immediately and applies only benefits that remain legitimately unclaimed. A transition out reinstates active noncooperation for the remaining original term. Neither transition creates a fresh deadline.

A fascist country can still grant independence, participate in diplomacy, apply for League membership or face international opposition. Membership requires actual charter conduct. The exception does not automatically make its promises credible or its nuclear policy acceptable.

This is an authored gameplay asymmetry. The historical research explicitly separates it from Gandhi's stated doctrine. No fabricated quotation should justify it.

## Finite endurance and ordinary stages

Ordinary stages change the strength and endurance of the initial worldwide campaign. They are separate from the two institutional evolutions and the world-end route.

| Chaos when the incident is frozen | Opening Momentum | Base local endurance after refusal |
| --- | ---: | ---: |
| 0 to 199 | 40 | 150 days |
| 200 to 399 | 45 | 180 days |
| 400 to 599 | 50 | 210 days |
| 600 to 799 | 55 | 240 days |
| 800 to 999 | 60 | 270 days |
| 1000 and above | 65 | 270 days |

At local activation, Movement Momentum can vary endurance by up to thirty days around the anchor. Local endurance is clamped to ninety through three hundred days. Every state also has an absolute incident ceiling of the firing date plus 314 days, including the fourteen-day opening response. Use the earlier deadline. A new occupation late in the campaign receives only the remaining time.

The incident freezes its ordinary stage before any consequences change Chaos. Later Chaos increases do not lengthen existing refusal terms. A later evolution does not restart noncooperation. The League can undertake fresh negotiated work after the initial campaign has faded, but it cannot quietly renew worldwide zero-output occupations forever.

Campaign closure clears only Gandhi-owned state denial, suppression flags, morale or reinforcement contributions, pending opening cases and temporary presentation queues. It keeps historical outcomes, achievement evidence, character history and legitimate independent countries. League institutions use their own lifecycle after that closure.

## Two public values

The whole event uses two persistent custom numerical values.

| Value | Purpose | What it cannot do |
| --- | --- | --- |
| Movement Momentum, 0 to 100 | Measures the movement's ability to organize, persuade and sustain commitments | Purchase equipment, invent countries, provide nuclear devices, replace real success receipts |
| League Cohesion, 0 to 100 | Measures cooperation among actual members after a League exists | Override national consent, give foreign nuclear command, settle a war by itself |

Cohesion is absent before the League is founded. Native research, factories, manpower and nuclear inventory remain ordinary national facts. Finite response timers and counts of completed historical cases are not new currencies. Qualitative statuses explain whether a country has consented, fulfilled an obligation or lost access.

Momentum rises through concrete independence, peace and constructive-work outcomes. It falls when the movement exhausts itself, lies are exposed, member promises fail or its leadership turns to coercion. Cohesion changes through consultation, equitable burdens, fulfilled aid, security disagreements and departures. Part 3 supplies the event table. Values are bounded and changes use one outcome receipt, so repeating a report cannot farm them.

Three Gandhi spirit families are sufficient. The occupation-response family holds Loss of Morale or fascist consolidation. The civic-institution family replaces its earlier variant as the country's role changes. The temporary-obligation family represents a paid material or reconstruction burden. There is no new spirit for every focus, release or peace conference.

## The life behind the movement

Gandhi begins as a civilian organizer and convenor. Hosting him does not remove a country's ruler, change its ideology or replace its focus tree. His location, legal access and personal safety affect which meetings and missions are possible.

If a living Gandhi character already exists, use that identity. If the campaign has passed his historical death and the game records him as dead, this event permits one explicitly fictional Chaos return. It is recorded as such. The event does not create multiple Gandhis or silently rewrite history as ordinary survival.

After this appearance, capture, rescue, removal and death matter. An institutional League may survive his death. The personal supreme-leader route cannot. A second death is not followed by another free resurrection.

## Evolution entry and player settings

At 400 or 800 Chaos, institutional evolution becomes eligible only when its real political and material conditions are met. A threshold alone does not create members, successes, reactors or warheads.

During an active incident, completing the required durable outcomes opens the relevant proposal. Before a first firing at high Chaos, the event evaluates any already available, explicitly attributable cross-event receipts and current capabilities. It may offer a founding or nuclear congress promptly if every condition is genuinely proved. It does not backfill Gandhi participation in unrelated earlier liberations or invent sixty days of observation. In the usual fresh high-Chaos opening, the campaign starts at the appropriate ordinary stage while earned institutions still need to be built.

An evolution grant is recorded once. Falling Chaos does not retroactively erase a lawful treaty or a real arsenal. Disabled evolution settings prevent new grants and route-specific actions. They do not confiscate independent states, delete countries or reverse completed native research. Existing obligations receive a safe exit or completion path. Re-enabling a previously granted stage restores only actions whose current actor, consent and capability gates still pass.

The world-end route always rechecks Chaos strictly above 1000 at its mandate vote and at the start of its coercive campaign. Exactly 1000 is insufficient. Once a real campaign has begun, a later Chaos fall creates political pressure and an opportunity to de-escalate, rather than deleting ongoing wars or disguising a completed victory.

## Campaign outcomes worth reaching

The early movement can leave a world of independent countries without creating a League. A League can become a useful mediator without seeking nuclear arms. A nuclear-capable League can accept reciprocal disarmament. Former members can defeat a coercive Gandhi and preserve a reformed peaceful organization. These are complete outcomes with meaningful aftermath, not failures to reach the largest spectacle.

The remaining parts define the exact sovereignty transactions, League institutions, nuclear constraints, final conflict, country content, decisions, AI, accounting and validation needed to make those outcomes playable.
