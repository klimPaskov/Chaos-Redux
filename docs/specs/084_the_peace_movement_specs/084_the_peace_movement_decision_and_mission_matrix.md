# 84 · Decision and mission matrix

## Reading the matrix

The matrix holds 33 actions and 17 mission types.
IDs are stable design IDs, not engine IDs or final localisation.
The complete scope of an action includes its corresponding part of the specification.
PP means Political Power.
CP means Command Power.
CIV means a temporary commitment of usable civilian factories, not a permanent building deletion.
Capacity bands are small below 10 usable civilian factories, medium at 10 through 29, and large at 30 or more.
Ordinary project CIV commitments are 1/3/5.
Support-equipment commitments are 50/150/300.
Transport commitments use 5/15/30 motorized equipment or 5/10/20 convoys for a genuinely maritime route, never both by default.

Freeze the selected cost band and target when the project is accepted.
Do not raise a contracted cost because the country's economy grows during the mission.
No action has more than four spend types.
CP costs never exceed 50 in this package.
An unaffordable project is unavailable, or offers an explicitly reduced-scope result before acceptance.
It never creates negative stockpiles or free capacity.

## Visible pages

At most one Event 84 page is active for a country at a time.
Use native decision-category visibility conditions, not a new custom window.
Page navigation has no political, Chaos, reward, or resource effect.

| Page | Six primary slots, maximum | Mission display priority |
|---|---|---|
| Initial response | Tolerate, negotiate, co-opt, suppress, eradicate, current local dispute | One local emergency if present |
| Public organizing | Current mandate, civic project, character case, foreign contact, political settlement, emergency response | Emergency, current agreement, one funded civic or foreign project |
| Movement government | Constitutional objective, economic project, service program, foreign commitment, character case, return/emergency | Emergency, constitution, one material project |
| Traditionalist government | Constitutional objective, national service, civic/family support, external security, character case, return/emergency | Emergency, constitution, one material project |
| Civil war | Command objective, training allocation, supply/relief, foreign aid, negotiate settlement, return | Survival/command, supply, mediation or aid |
| International | Congress or mandate, refuge/passage, aid, funding/security case, mediation/ultimatum, return | Urgent defense, one treaty mission, one aid mission |
| World order | Current final objective, accession, defense integration, civilian protection, rival settlement, return | Urgent defense, ratification, one integration or accession project |
| Target selection | Up to four valid named target choices, previous page, next/return page | No additional mission is created by browsing |

On pages where an emergency occupies the last slot, return navigation occupies a nonurgent slot or is provided by the resolved event's normal close behavior.
Never accidentally show seven buttons.
Multiple eligible cases use a bounded queue and the case slot, not one permanent button per person.
The active-mission ceiling is three across all Event 84 categories combined.

## Choices that are not decisions

Seven earlier design IDs are retired as decisions because a button would only repeat a choice another surface already owns.
Their IDs are not reused.

| Retired ID | Where the choice lives now |
|---|---|
| DEC07–DEC10 | Civilian service, assembly and expression, equal legal standing, and partial demobilization are package options in the event opened by DEC02 (Part 3). The chosen package's delivery objective runs inside MISS01 |
| DEC13 | The population policy is chosen in the family-policy congress event (Parts 2 and 4) |
| DEC18 | MISS15 starts automatically when an agreement or postwar convention is delivered |
| DEC38 | MISS17 starts automatically when Part 10's conditions and focus W07 are met |

## Government and civic actions

| ID | Working action direction | Availability and cost | Objective and resolution | Reuse |
|---|---|---|---|---|
| DEC01 | Tolerate public organizing | Active movement, 25 PP | Adopt open posture and its defined monthly contributions | Posture minimum 60 days, no repeated adoption award |
| DEC02 | Open negotiations | Willing authorities, 50 PP plus 1/3/5 CIV | Start one 90-day local reform negotiation, select one package | One national agreement at a time, completed terms cannot be bought again |
| DEC03 | Bring organizers into government | An actual available institution, 25 PP plus 1/3/5 CIV | A 120-day co-optation project must give real authority or deliver a project | Same organization locked 180 days after outcome |
| DEC04 | Restrict an identified organization | Actual local organization and accountable command, 50 PP plus support equipment and 1/3/5 CIV | A 90-day suppression mission with visible, underground, and failure outcomes | Same target requires a new surviving organization or distinct new cause |
| DEC05 | Dismantle the movement network | Capital and loyal command, no ongoing domestic civil war, 100 PP, 50 CP, support equipment, 1/3/5 CIV | A 180-day eradication campaign, with success, partial survival, or institutional rupture | Same-cause 360-day lock, no purge-reward farming |
| DEC06 | Resolve a local gathering dispute | Actual festival, retreat, or assembly case, 25 PP | Agree public-order terms, investigate a concrete incident, or impose the chosen restriction | One resolution per gathering |
| DEC11 | Fund a communal welfare charter | A real civilian venue or local authority, 25 PP plus 1/3/5 CIV | Deliver a 120-day housing, kitchen, or cooperative project | One active project per anchor, delivered buildings are not repeatedly granted |
| DEC12 | Fund inclusive family support | Governing authority and actual capacity, 50 PP plus 1/3/5 CIV | A 180-day childcare and housing project can remove an explicit policy growth penalty | Policy minimum 180 days, no retroactive population refund |
| DEC14 | Support a public cultural exchange | Valid sponsor and venue, 25 PP plus 1/3/5 CIV | Complete a 90-day exchange and create one bounded contact contribution | Same pair 180-day cooldown, no duplicate festival contribution |
| DEC15 | Investigate a public case | An actual pending adult character case, 25 PP or 25 CP for a command case, not both | Resolve evidence and choose the permitted protection, inquiry, dismissal, or public-response branch | One active case per character, outcome persistent |
| DEC16 | Establish a lawful transition | Valid takeover or caretaker route, 50 PP plus 1/3/5 CIV | Start the 120-day national convention | Revisions must be real political changes, no repeated constitution award |
| DEC17 | Mediate the service-and-authority crisis | A concrete command rupture, 50 PP plus 25 CP | Complete the 30-day command mission or face its actual failure outcome | One mission per rupture |

## Military and international actions

| ID | Working action direction | Availability and cost | Objective and resolution | Reuse |
|---|---|---|---|---|
| DEC19 | Allocate a Rainbow cohort | Armed Peace, valid mandate, Influence at least 40, actual unit requirements from Part 8 | Train and deploy the reserved cohort once | Capacity and training gates, no simultaneous duplicate reservation |
| DEC20 | Charter a territorial Guard | Armed Peace, eligible anchor and mandate, actual Guard requirements | Train one local cohort tied to a real defended area | Anchor and ceiling limited |
| DEC21 | Admit a Lotus cohort | Armed Peace and resolved order relationship, actual Lotus requirements | Train one limited 120-day cohort | Only one active national cohort, capacity ceiling |
| DEC22 | Professionalize a Brigade | Armed Peace, officer agreement, logistics, actual Brigade requirements | Convert a real formation or train a new one, with conserved material | Each formation can be converted once per valid retraining cycle |
| DEC23 | Repair military supply | Real depot or transport need, 25 PP, support equipment, chosen transport, 1/3/5 CIV | Deliver a 120-day supply project | Actual damaged or insufficient capacity needed |
| DEC24 | Integrate the armed order | Independent order and consenting authority, 50 PP plus 25 CP | A 120-day command integration mission removes independent-armed-group pressure after compliance | A refused or splintered order cannot instantly be reintegrated for another reward |
| DEC25 | Demobilize an emergency formation | War or emergency ended, actual surviving unit | Return supported survivors and recoverable equipment through verified native rules | One outcome per actual unit, losses remain lost |
| DEC26 | Offer asylum or safe passage | Valid threatened organization or person, 50 PP, 1/3/5 CIV, transport only if required | A 120-day reception mission with actual capacity and sovereign consent | One project per case, uses one foreign contact slot |
| DEC27 | Sponsor legal or cultural work abroad | Eligible partner, 25 PP plus 1/3/5 CIV | Complete a 90-day recipient project and one bounded foreign contribution | Same recipient/project 180-day lock |
| DEC28 | Send a declared equipment shipment | Actual owned equipment and a valid route, shipment plus transport if needed | Deliver equipment to a real training, relief, or defense objective | Deduct once, no duplicate lend-lease plus event shipment |
| DEC29 | Commit volunteer assistance | Valid war and supported native volunteer conditions | Commit actual units or supported volunteer capacity | Follow native return and casualty ownership |
| DEC30 | Convene an international congress | Three qualified consenting governments, 100 PP plus 1/3/5 CIV | A 180-day congress establishes a charter or a lesser compact | One founding process per bloc, no refounding reward |
| DEC31 | Coordinate a security or funding case | An actual channel and supported institutions, 50 PP, 25 CP when command resources are genuinely needed | A 120-day treaty or investigation objective | One case per channel and incident, no universal private-identity exposure |
| DEC32 | Negotiate a frontier settlement | Willing opposing authorities, 100 PP plus 1/3/5 CIV | A 180-day mediation mission with ceasefire, authority, and protection terms | Same rejected unchanged terms 180-day lock |
| DEC33 | Present an authorized ultimatum | Charter authority and a real strategic dispute, 100 PP plus 25 CP | One 30- to 90-day crisis according to the established scenario, then terms, compromise, or valid war | No resetting the deadline by repeated presentation |
| DEC34 | Hold a leadership or obligation vote | A valid dispute or ended mandate, 50 PP | Resolve the congress, obligations, or leadership without a cohesion meter | Ordinary mandate minimum 180 days, actual emergency exception |
| DEC35 | Begin final accession negotiations | Active terminal scenario and eligible authority, 100 PP plus 1/3/5 CIV | A 180-day accession mission, with enforceable legal and security terms | One active accession target per member, actual authority required |
| DEC36 | Integrate international defense | Active terminal scenario and consenting material contributions, 100 PP, 25 CP, declared support-equipment shipment, 1/3/5 CIV | A 180-day program opens terminal recruitment ceilings and replacement modifiers | Once per completed coalition program, not per rotating leader |
| DEC37 | Protect the civilian rear | Active terminal threat and a real relief or reconstruction need, 50 PP, support equipment, selected transport, 1/3/5 CIV | A 120-day funded protection project | One active project per anchor |
| DEC39 | Negotiate civil-war peace | Valid belligerents and settlement authority, 50 PP plus 25 CP | Open the relevant ceasefire, reunification, independence, or surrender outcome | Each agreed settlement has persistent terms and the relapse rules |
| DEC40 | Implement traditionalist readiness | Chosen traditionalist route and real institutions, 50 PP, support equipment, 1/3/5 CIV | Constitutional service agreement or 180-day discipline program, with that route's distinct consequences | No stacking route recoveries or reacquiring them through cosmetic changes |

## Mission result matrix

A mission completes as soon as all required objectives are met, unless it explicitly requires a period of maintained compliance.
The player does not need to find a second claim-reward button.
A maintained settlement waits for its stated duration.
Cancellation releases only undelivered ongoing commitments, preserves delivered material and spent PP, and creates no reward.

| ID | Mission and normal duration | Full success | Partial success | Failure or cancellation |
|---|---|---|---|---|
| MISS01 | Local reform negotiation, 90 days | Implement chosen terms, −15 Reaction and −5 confrontational Influence, then maintenance | −5 Reaction and one 60-day extension | Broken agreement +10 Influence/+10 Reaction. Unrelated territorial loss cancels without alleging bad faith |
| MISS02 | Co-optation delivery, 120 days | Real institutional inclusion, −10 Influence and +5 Stability for 180 days | Delivered local benefit remains, no national confrontation reduction | Exposed sham +15 Influence/+10 Reaction, possible official defection |
| MISS03 | Suppression, 90 days | −15 visible Influence and actual network containment | −5 Influence and a surviving underground node | Abusive failure +15 Influence/+15 Reaction and a repression case |
| MISS04 | Eradication, 180 days | −30 Influence and closure of identified anchors with a 180-day aftermath | −10 Influence and an exile or underground successor | +20 Influence/+20 Reaction and a concrete rupture, with civil war only if viable |
| MISS05 | Command crisis, 30 days | A lawful command and transfer or negotiated refusal | Caretaker authority or limited neutral command | Valid split, capital crisis, or failed uprising, according to actual geography |
| MISS06 | National constitution, 120 days | Establish the chosen lawful authority and route | A caretaker cabinet with one unresolved institutional term | Coalition collapse or a new explicit authority crisis, not an automatic army gift |
| MISS07 | Commonwealth supply charter, 150 days | Real civilian coordination and the route's production adjustment | Local cooperatives remain, national reward withheld | Supply and autonomy dispute, with actual losses handled by their owners |
| MISS08 | Family-support program, 180 days | Delivered childcare/housing and removal of a selected policy penalty | Completed local capacity remains, no national demographic-policy removal | No population refund, ongoing undelivered commitment released |
| MISS09 | Order integration, 120 days | Civilian command and removal of independent-armed-group pressure | Limited local charter, no full integration benefit | Schism, refusal, or negotiated departure of real surviving personnel |
| MISS10 | Supply or civilian protection project, 120 days | Deliver the actual stated logistical or relief improvement | Keep delivered material, reduce the promised scope | No synthetic casualty award, unresolved real need remains |
| MISS11 | Asylum and passage, 120 days | Actual safe reception and a valid protected organization or person | Partial route or reception success, with survivors recorded correctly | A diplomatic case or canceled route, no population or character duplication |
| MISS12 | International founding congress, 180 days | Qualified charter and valid bloc | A limited compact with fewer powers | Congress dissolves and spent resources remain spent |
| MISS13 | International mediation or accession, 180 days | Actual signed and implemented authority/security settlement | A ceasefire or partial treaty, no full victory credit | Terms lapse or crisis returns, with no automatic unrelated war |
| MISS14 | Traditionalist discipline program, 180 days | Deliver command and production objectives, apply bounded route recovery and its costs | Recover only the fulfilled institutional part | Underground growth, service dispute, or command crisis |
| MISS15 | Domestic or postwar maintenance, 180 days, starts automatically | Durable settlement and removal of temporary crisis penalties | One outstanding issue remains without repeating earlier rewards | A specific institution fails and its own consequence follows |
| MISS16 | Terminal defense integration, 180 days | Real contributions and expanded military capacity limits | Delivered equipment remains, unsupported ceiling increase withheld | No free units, the coalition must resolve its funding or command dispute |
| MISS17 | Final world ratification, 180 days, starts automatically | All maintained requirements and final victory | Military settlement survives but the celebratory social-order ending waits | Suspension or terminal reversal according to actual lost conditions |

MISS01 is the 90-day local reform process.
MISS06 is the separate 120-day national constitutional convention.
MISS07 is the 150-day national economic charter.
Their different durations are deliberate, not inconsistent labels for the same mission.
A parent negotiation and its selected reform do not occupy two mission slots.
