# AI behavior, pacing, and balance

The AI must choose a plan that its country can carry out.
High Intervention Pressure or Boxer Strength can change urgency, but neither removes the requirements for equipment, supply, access, political authority, and compatible diplomatic relationships.
The human and AI use the same action validity and payment contracts.

The values below are starting design anchors.
No HOI4 probability tool, focus evaluator, event-chain analyzer, or live game test was executed for this package.
Expected rankings are design targets that require later evidence.

## Chinese government plans

A government capable of protecting threatened sites and containing the armed networks should normally prefer a controlled suppression or negotiated disarmament plan.
It should not choose toleration merely because toleration is the cheapest immediate button.
Its plan needs enough resources to fulfill the guarantee it offers.

A government under serious foreign attack can prefer limited Boxer support when societies can operate against the occupier and the government can control the terms of the compact.
It must still protect civilians and avoid treating an invited ally as a hostile occupier.
It should not support a movement whose likely territorial ambitions would destroy its only viable supply route.

A weak government that cannot immediately suppress the movement can choose toleration as a temporary policy.
It should use that period to negotiate, improve protection, or build a credible security force.
The AI must not remain indefinitely in passive toleration while every relevant site deteriorates and it has affordable alternatives.

A Chinese subject considers autonomy and the patron's actual role.
It can protect civilians or seek a limited local accommodation within its authority.
Openly supporting an uprising against its overlord requires a supported political break and a feasible survival plan.

## Boxer plans

The movement prioritizes survival, supply, and an achievable political position.
A small enclave should defend its founding route, regularize a sustainable core, and negotiate useful agreements before attempting a distant offensive.
A powerful movement with several supplied centers can pursue broader command and political authority.

The AI should accept a favorable auxiliary compact when independence would be militarily unsustainable and the compact preserves meaningful local institutions.
It can reject a compact that would leave its forces disarmed under an authority that has repeatedly broken agreements.
The decision follows actual history and capacity, not a fixed refusal weight.

The Boxer country chooses its political route from its existing institutions.
A broad coalition of regional societies favors the federal route.
A strong, supplied central army under immediate military pressure favors military government.
A movement whose established authority rests on religious councils and schools can favor the religious route.
None of those tendencies overrides an invalid route.

## Foreign plans

A power first identifies the value of its actual interest and the cheapest credible way to protect it.
Evacuation can be a successful plan.
The AI should not treat withdrawal as a failure that must always be avoided by starting a wider war.

An existing regional occupier may favor suppression to protect its transport and holdings.
A distant power with threatened civilians but few territorial interests may favor evacuation and a limited guarantee.
A capable power seeking expanded privileges can pursue a stronger mandate, but must account for Chinese resistance, coalition disagreement, and its other wars.

A country without a deployment route cannot choose an expedition merely because Pressure is high.
A country already fighting a major war elsewhere should protect the capacity needed for that war before accepting a new large commitment.
It can still offer a limited contribution that fits its means.

## Coalition behavior

The coalition evaluates mandates and contributions separately.
A participant that has completed an evacuation can withdraw even when another participant's suppression campaign continues.
A leader cannot spend the other members' resources or accept a new territorial demand on their behalf.

Leadership preference follows practical theater capacity and accepted coordination responsibility.
It does not depend on which actor clicked the first conference button.
An extinct or departed leader is replaced through the surviving agreement, with an interim pause on new collective commitments when needed.
Existing individual missions continue under their owners.

Enemy foreign powers require a valid deconfliction arrangement before a common operation.
If that is impossible, the AI pursues separate operations or refuses the proposed joint task.
It must not repeatedly propose the same impossible coalition every update.

## Scoring and probability semantics

Apply hard validity first.
Then evaluate capacity, urgency, expected benefit, political compatibility, existing commitments, and recorded trust or breach.
Keep factors bounded so one diplomatic opinion value cannot outweigh a nonexistent deployment route.
Use shared MTTH-backed score helpers when appropriate to avoid inconsistent copies of the same logic.

Relative design score anchors of 25, 50, 100, and 150 can represent weak, plausible, preferred, and urgent choices after validity.
They are not probabilities.
The final complete event-option or random-list pool must be supplied to the probability auditor when normalization applies.

Decision `ai_will_do` represents willingness under its actual engine semantics.
Do not report its weight as the probability that a decision will be clicked.
Focus selection must be evaluated with the installed focus-selection model.
Do not convert every focus weight into a simple weight divided by total probability.

An MTTH parameter near 90 days is a tuning anchor, not a proof of a particular cumulative chance by day 90.
Timing claims require the verified game-version adapter and scheduled changes in the relevant state.
The probability auditor must distinguish exact, bounded, sampled, score-only, and unresolved results.

## Strength and Pressure changes

Changes should follow an attributable event or a sustained condition.
The event keeps one receipt per relevant milestone and target.
A single development cannot be counted again through a news event, a mission completion, and a periodic update.

| Development | Boxer Strength target | Intervention Pressure target | Limitation |
| --- | ---: | ---: | --- |
| First viable network established in a new region | +5 | 0 | Once per region and crisis generation |
| First successful funded recruitment program in a region | +5 | 0 | Once per regional program, later recruitment provides forces rather than repeated political rewards |
| Sustained connected command and supply | +5 | 0 | At most once per 30 days, and only while below the institutional ceiling |
| A significant stronghold defense succeeds | +10 | +5 when it materially threatens an accepted foreign objective | Once per meaningful operation, with a 90-day repeat restriction at the same site |
| A key stronghold is dismantled | -15 | -10 when the relevant threat is removed | Once for that stronghold's defeat, no reward for repeatedly toggling control |
| A funded government compact is honored | +10 to the affiliated organization | -10 when it fulfills a foreign protection demand | Once per compact's completed verification, not on signature alone |
| A government openly endorses the movement | +5 when it brings actual political support | +15 for materially exposed foreign interests | Once per government's first public commitment, with an aggregate opening limit |
| A registered site becomes besieged | +5 only if it reflects a genuine gain in local control | +10 | Once per incident, no duplicate site records |
| An unresolved serious siege continues | 0 | +5 per theater update | Within the normal aggregate update limit and only while the threat remains credible |
| Safe evacuation or a verified local guarantee | 0 | -15 for the resolved incident | Only the actual resolved population or site counts |
| Negotiated disarmament is completed | -10 for the armed network | -10 | Legal peaceful societies can remain without being counted as an armed threat |
| Sponsorship collapses or its supply is cut | -10 | Depends on the unresolved foreign threat | No automatic Pressure reduction while civilians remain at risk |
| Harsh occupation sustains a real recruitment grievance | +5 when a surviving network can exploit it | Depends on actual foreign disputes | At most once per 30 days for that cause, with no free unit grant |

A network without armed or territorial institutions normally cannot grow beyond roughly 50 Strength through passive coordination alone.
A local stronghold network without broad sustainable administration normally cannot pass roughly 70 through the same passive process.
Higher Strength requires actual successes and institutions.
These ceilings apply to passive growth, not to a fabricated territorial percentage.

The normal 10-day update aggregates no more than 10 Strength and 15 Pressure in either direction before separately identified major incidents.
The final implementation must specify which developments are periodic and which are discrete so it cannot apply the same cause through both routes.
All public values clamp to 0 through 100.

## Resource and force balance

A militia formation pays its real template bill.
A captured depot transfers only its recorded remaining allocation.
A donor shipment is debited before it can be delivered.
A country-creation process reconciles all those allocations before its army is activated.
Those constraints are more important than a decorative global recruitment cap.

Use the action scale and physical capacity limits from Part 5.
Large countries can support larger operations, but they also have more territory and interests to protect.
A small country must retain at least one credible protection, negotiation, or withdrawal response when an event-owned emergency is assigned to it.
An operation that it cannot afford should not be its only route to avoiding an unavoidable failure.

The shared crisis budget remains authoritative.
Event 069 does not silently raise the project's country crisis limit.
Natural targeting should avoid adding a forced emergency to a country whose applicable crisis budget is already full.
Invitations and news do not count as active commitments until the existing shared policy says they do.

## Named balance and AI scenarios

These are required future fixtures, not executed test results.

| Fixture | Setup | Expected ordering or invariant |
| --- | --- | --- |
| AI01 Capable unified government | Moderate Strength, threatened foreign district, adequate security | Protection and negotiated suppression outrank passive toleration |
| AI02 Government under invasion | Invader occupies an active region, allies are invited | Limited anti-occupation support can outrank broad suppression, while allied sites remain protected |
| AI03 Weak fragmented government | Low supply and several rival societies | Negotiation and a feasible local compact outrank an unaffordable general offensive |
| AI04 Chinese subject | Patron owns the diplomatic authority | No unrestricted anti-overlord war choice without a valid break mechanism |
| AI05 Distant rescue power | One threatened civilian group, little territorial interest | Evacuation and a local guarantee outrank expanded territorial demands |
| AI06 Regional occupier | A real supply corridor is threatened | A supplied local operation outranks an unrelated distant conquest |
| AI07 Foreign power in another major war | Limited spare transport and troops | A bounded contribution or refusal outranks an unsustainable expedition |
| AI08 Landlocked distant minor | High Pressure, no route | Expedition remains invalid regardless of its score |
| AI09 Rival foreign factions | Interested powers are at war with each other | No automatic common command, faction merge, or global peace |
| AI10 Completed rescue | Nationals safe and mandate complete | Orderly withdrawal outranks indefinite mission expansion |
| AI11 Small Boxer enclave | Low stocks and a threatened founding route | Supply and defense outrank more unsupported recruitment |
| AI12 Supplied Boxer regional network | Several societies, functioning routes | Regional council and regularization become attractive |
| AI13 Religious route without anomalies | Evolution II disabled or unconfirmed | Conventional military and education routes remain useful |
| AI14 Failed ritual claim | Operational evidence contradicts a school | Regulation or command reform outranks repeated unsupported use |
| AI15 Coalition mandate dispute | Leader seeks new privileges after rescue | Limited members can refuse, narrow the mandate, or leave |
| AI16 Cooperative Chinese rival | Negotiated contribution is viable | A limited pact can outrank a simultaneous internal offensive |
| AI17 Unified China at Evolution III | One Chinese government with regional institutions | National coordination works without creating fake rival countries |
| AI18 Treaty capacity collapse | Signatory loses industry but remains compliant elsewhere | Moratorium or amendment outranks an impossible payment loop |
| AI19 Empty foreign-interest pool | Stable isolated theater | No invented coalition or foreign institution in a natural opening |
| AI20 Former site owner extinct | Site survives under a successor | No payment, troop transfer, or mandate points to a dead actor |
| AI21 High Strength without arms | Strength is 85, required equipment is absent | No free militia or unsupported independent country activation |
| AI22 Mixed treaty result | One member withdraws and another continues a wider war | Event closure for one objective does not terminate the unrelated war |
| AI23 Full mission capacity | Three accepted objectives already active | No hidden fourth deadline is assigned |
| AI24 Manual evolved setup | Scenario forces an initial state below normal Chaos gates | Setup succeeds where structurally possible, then normal future gates resume |

## Evidence required during implementation

The probability auditor first inspects the real sources and complete candidate pools.
It then evaluates the named scenarios, sweeps relevant thresholds, compares matched before-and-after sources, and records unresolved engine inputs.
Only declare a sequence analysis when its manifest includes cadence, recovery, caps, cooldowns, removals, resets, timer changes, and terminal states.

Balance review must include actual stockpile accounting, force ownership, treaty capacity, mission deadlines, route exits, and the ability to close a crisis without universal capitulation.
A syntactically valid script or a successful source render cannot by itself prove those behaviors.
