# Event 011: Secret Alliance, Part 3

Player-facing wording note: every title, option, decision name, focus-style label, achievement title, GUI label, event-detail line, report text, and news text in this package is direction only. Working labels are internal handles for implementation and asset routing. The implementation pass must write final localisation from the directions here, without copying working labels into the game unless a label is explicitly marked as an identifier.

## Counter-pact decision category

The decision category opens during Evolution II or after the player gains enough suspicion through repeated baseline and Evolution I incidents. It should feel like a counterintelligence and diplomatic war room, not a store of political power buttons.

Working category role: Counter Pact Operations. This is an implementation label, not final localisation.

The category should show a compact header using scripted localisation:

| Display value | Meaning |
| --- | --- |
| Suspicion | The target government’s sense that the pattern is coordinated |
| Evidence | Proof that can expose members or pressure foreign governments |
| Preparedness | Defensive readiness against sabotage and later war |
| Known members | Count and list of exposed countries |
| Suspected member estimate | A rough range, not a full hidden list |
| Pact pressure | An estimate derived from readiness, hostility, and recent operations |

Cause and effect must be readable. If a decision raises preparedness, lowers pact secrecy, or risks backlash, final text should say so in world terms and tooltips should describe visible consequences.

## Optional scripted GUI board

A custom board is useful once Evolution II is active. If implementation scope allows it, use a scripted GUI attached to the decision category. If not, the decision category must still show the same values through scripted localisation.

The board should show:

| UI element | Role |
| --- | --- |
| Central pact seal silhouette | Unknown network icon before reveal, revealed pact emblem after reveal |
| Evidence meter | Shows progress toward exposing a member or the whole pact |
| Preparedness meter | Shows war and sabotage readiness |
| Suspect cards | One card per exposed or strongly suspected country, with hidden cards for unknown members |
| Recent operation ledger | Short list of last public incidents, not a raw debug log |
| Border risk strip | Shows whether any exposed or suspected member borders the target |
| Action buttons | Investigate, secure, negotiate, split, mobilize, and confront families |

Animated UI planning:

| Animated asset | State logic | Target surface | Static fallback |
| --- | --- | --- | --- |
| Hidden compact seal | Slow dim pulse when suspicion is high, stronger pulse after Evolution II | Decision category header or GUI panel | Static seal silhouette |
| Evidence meter shimmer | Brief shimmer when evidence increases | GUI meter | Static meter frame |
| Exposed member card glow | Soft glow for a country the player can pressure or confront | Suspect card | Static highlighted frame |
| Crisis border frame | Warning pulse when pact war countdown begins | GUI panel frame | Static red warning frame |

The animation pass must use real source frames through the frame-animation workflow. Do not create final animation by shifting or recoloring one still image.

## Decision family: investigation

Investigation decisions turn suspicion into evidence. They should be cheaper when suspicion is high and stronger when the player has a counter-network, friendly intelligence partners, or recent failed pact operations.

| Working decision | Availability | Cost and requirement direction | Success | Failure or risk | AI use |
| --- | --- | --- | --- | --- | --- |
| Map courier routes | Evolution II or high suspicion | Political attention, trucks or trains if land routes matter, intelligence exposure risk | Adds evidence and may identify a suspect region | Pact secrecy rises if done too often without suspicion | AI uses when evidence is low and stability is safe |
| Compare cipher traffic | Agency exists or enough suspicion | Command power below 60, army XP or air XP depending on signal route, possible civilian factory burden | Finds a member clue or reduces secrecy | False lead risk if target has low stability | AI uses if it has agency or high industry |
| Raid a safehouse | Exposed target state or high suspicion in a region | Supplied divisions or garrison presence in named states, support equipment, stability risk | Strong evidence and can stop an operation | Civilian backlash, member hostility spike | AI uses only when domestic stability is not fragile |
| Interrogate captured couriers | After courier event or failed operation | Command power, legal legitimacy or stability cost, time | Evidence and possible member identity | Heavy-handed use lowers stability and raises hostile propaganda | AI cautious unless authoritarian or at war |
| Trace procurement money | After sabotage or propaganda operation | Civilian factory burden, political attention, market access | Reveals associate or funding path | Money trail can be laundered and pact secrecy rises | AI uses if industrial capacity is safe |

Investigation should never reveal every member from one click. It should create a trail: country clue, member exposure, patron clue, full reveal.

## Decision family: internal security

Internal security decisions reduce sabotage and raise preparedness. They should commit real resources and create opportunity cost.

| Working decision or mission | Type | Availability | Cost and requirement direction | Result |
| --- | --- | --- | --- | --- |
| Guard the rail offices | Timed mission | After rail interference or Evolution II | Place supplied divisions in named rail states, trains or support equipment | Reduces rail sabotage chance and raises preparedness |
| Secure industrial districts | Timed mission | After factory sabotage or high hostility | Garrison or divisions in industrial state group, support equipment, temporary factory burden | Protects industry and may catch a cell |
| Protect officers and ministers | Clickable decision | After killing threat or Evolution II | Command power, infantry equipment, stability or war support tradeoff | Reduces officer attack risk, raises preparedness |
| Audit foreign contracts | Clickable decision | Procurement operation or high suspicion | Civilian factory burden, political attention | Finds funding evidence or reduces future sabotage |
| Harden ports and cable stations | Timed mission | If target has ports, overseas supply, or naval trade | Convoys, naval XP, port control, coastal divisions | Reduces naval-route operations and may expose a member |
| Emergency counter-network | Clickable decision | Evolution II | Political attention, agency capability or civilian burden, intelligence exposure | Unlocks stronger investigation decisions |

Timed missions should last long enough to matter. Easy missions should usually run around three months. Medium missions should run around four to six months. Urgent missions can be shorter only after a clear operation creates immediate risk.

## Decision family: diplomacy and split operations

Diplomatic actions try to isolate members, protect the target’s credibility, and force the pact to reveal too early. They should not always be safer than military preparation.

| Working action | Availability | Cost and requirement direction | Success | Failure or risk |
| --- | --- | --- | --- | --- |
| Private demarche to suspected member | Member exposed or strongly suspected | Political attention, relation path, evidence threshold | Lowers member commitment or pauses operations | If evidence is weak, member warns pact |
| Offer off-ramp guarantees | Exposed minor with low commitment | Political power plus guarantee, trade access, or nonaggression concession | Member defects or becomes associate only | Target may look weak, pact patron may increase hostility |
| Court rival of a member | Member exposed and rival exists | Diplomacy cost, relation work, possible equipment aid | Creates pressure on member and lowers cohesion | Rival can exploit aid without helping |
| Convene neutral conference | Several exposed members or high evidence | Civilian factory or PP burden, friendly neutral support | Can delay reveal war and lower readiness | Public failure raises pact cohesion |
| Leak partial dossier | Evidence threshold | Stability or credibility risk, international reaction | Exposes one or more members and lowers secrecy | If evidence too low, backfires and raises hostility |
| Protect a defector | Defector event active | Convoys or divisions if exile route, political attention, security cost | Large evidence gain and member split | Failure can kill the defector and raise pact readiness |

Diplomatic split logic should depend on member commitment, pact cohesion, target evidence, ideology, relations, fear of patron, and target strength. A country bordering the target may prefer staying in the pact if it fears retaliation. A distant minor may defect if exposed and unsupported.

## Decision family: military readiness

Military readiness should not start the war by itself unless the player chooses a confrontation action later. It prepares the target for sabotage, border incidents, and revealed pact war.

| Working action | Type | Requirement direction | Result |
| --- | --- | --- | --- |
| Draft contingency plan | Clickable | Army XP, command power, known or suspected member count | Preparedness gain, later war-planning bonus |
| Watch the suspected frontier | Timed mission | Exposed or suspected neighboring member, supplied divisions in border states | Lowers border provocation success and unlocks stronger response |
| Secure capital and command lines | Timed mission | Divisions in capital region, trains, support equipment | Reduces shock from reveal and leadership attack |
| Stockpile emergency repairs | Clickable | Civilian factory burden, support equipment, trains | Reduces sabotage repair time |
| Call allied observers | Clickable | Faction member or high relations with a major, diplomatic cost | Raises evidence credibility and lowers pact recruitment |
| Open reserve depots | Clickable | Infantry equipment, trucks, manpower, stability cost | Adds temporary defense readiness without free unit spam |

The target’s preparedness should affect reveal outcomes. High preparedness can reduce surprise, lower member war enthusiasm, protect factories, improve defensive planning, or shorten emergency missions after reveal.

## Decision family: neighbor confrontation

Neighbor-specific actions only appear when a suspected or exposed pact member borders the target or has a direct state connection through a shared sea zone or strategic passage. This avoids irrelevant border decisions against distant countries.

| Working action | Availability | Cost and requirement direction | Outcome |
| --- | --- | --- | --- |
| Controlled border search | Suspected neighbor, not at war | Supplied divisions in border states, command power, support equipment | Evidence gain or provocation risk |
| Close frontier crossings | Suspected or exposed neighbor | Stability or trade cost, border divisions | Reduces sabotage and raises readiness, hurts trade |
| Challenge frontier patrols | Exposed neighbor and high evidence | Army XP, command power, local divisions | Can start a border war or force member exposure |
| Prepare limited border war | Evolution II or III, exposed neighbor | Divisions, supply, army XP, war support threshold | Border war with limited stakes, success weakens member commitment |
| Demand border inspectors | High evidence, neighbor exposed | Diplomatic cost and credibility | Member accepts inspections, refuses and gains exposure, or triggers crisis |

Border wars should be limited and risky. They should weaken the pact if successful, but failure should raise pact cohesion and readiness. AI should avoid them unless the target is strong and border supply is favorable.

## Decision family: public confrontation and war options

These unlock in Evolution III or when evidence and preparedness are high enough. They should give the player initiative but not a free win.

| Working action | Availability | Cost and requirement direction | Result |
| --- | --- | --- | --- |
| Demand pact dissolution | Evolution III or high evidence | Evidence threshold, diplomacy cost, preparedness recommended | Pact can dissolve, stall, reveal, or accelerate war |
| Publish full dossier | High evidence | Credibility risk, stability impact, foreign reaction | Reveals members, lowers secrecy, may split weak members |
| Preemptive strike authorization | Evolution III, exposed members, target not in truce with them | War support, command power, preparedness, border or strategic path | Target starts war on exposed core members and forces pact reveal response |
| Emergency alliance consultation | Target has faction or major friends | Diplomatic cost, evidence, relation checks | Allies improve defense readiness or pressure members |
| Last talks before mobilization | War countdown active | Political attention, evidence, counter-network | Delays war countdown or splits low-commitment member |

Public confrontation should read as a serious state action. The player should be able to start war, but the best route is often to expose and split members first.

## Pact operations and counterplay table

| Pact action | How pact chooses it | Player counter | Success effect | Failure effect |
| --- | --- | --- | --- | --- |
| Invite minor | High recruitment pull, enough secrecy | Diplomatic observation, member pressure | Adds core member or associate | Candidate leaks clue or refuses |
| Fund press network | High secrecy, low target stability | Trace money, public resilience decisions | Stability irritation, ideology drift | Evidence gain against sponsor |
| Sabotage factory | Evolution II, hostility, target industry | Secure industrial districts | Building damage, repair burden | Cell caught, evidence gain |
| Kill or intimidate officer | Evolution II, high hostility | Protect officers and ministers | Temporary command disruption | Backlash, exposure, lowered cohesion |
| Provoke border | Neighbor member, readiness high | Watch frontier, controlled search | Border crisis, target war support strain | Member exposed, pact readiness drop |
| Major patron funding | Major patron active | Procurement audit, ally observers | Cohesion and readiness gain | Patron clue or exposure |
| War council | Evolution III, high cohesion | Full dossier, split operations, mobilization | War countdown begins | Member hesitation or delayed countdown |

## Idea and national spirit plan

Use a small number of staged ideas rather than a pile of one-use modifiers.

| Idea working label | Owner | Stage | Role | Lifecycle |
| --- | --- | --- | --- | --- |
| Unexplained Diplomatic Friction | Target | Baseline or Evolution I | Mild negative or mixed spirit showing recurring pressure | Replaced by Counter-Pact Bureau once E2 opens or removed if pact dissolves early |
| Counter-Pact Bureau | Target | Evolution II | Mixed spirit, improves investigations but costs bureaucracy or consumer goods | Upgraded by decisions, replaced by Wartime Counter-Pact Command if reveal war starts |
| Prepared Security Network | Target | Decision-built | Positive staged spirit from successful security missions | Stronger stages protect industry and lower surprise penalties |
| Compromised Ministries | Target | Failure state | Negative temporary spirit after repeated sabotage or failed public accusation | Removed by cleanup decisions or reveal aftermath |
| Hidden Compact Discipline | Pact members | Hidden stage | Shared hidden modifier for cohesion, operations, and cooperation | Replaced by public faction spirit after reveal |
| Exposed Pact Government | Exposed member | After evidence | Negative diplomatic spirit making defection or pressure more likely | Removed by defection, war reveal, or pact victory path |
| Patron Shield | Major patron | Evolution II or III | Shows major funding, diplomatic cover, and operational reach | Weakens if target exposes patron networks |

Idea effects should be meaningful. Avoid tiny decorative values as the main payoff. Each idea should either alter decisions, reduce or raise sabotage risk, change AI behavior, or affect reveal war readiness.

## Failure and partial success states

The decision system needs partial outcomes.

| Outcome | Meaning | Follow-up |
| --- | --- | --- |
| Clean success | Operation finds evidence or prevents sabotage without collateral damage | Evidence gain, secrecy drop, possible member exposure |
| Heavy-handed success | Operation stops a threat but harms legitimacy or stability | Evidence gain, stability loss, propaganda risk |
| Partial success | Operation blocks immediate damage but loses a trail | Preparedness gain, small evidence gain, pact secrecy remains |
| False lead | Target acts against wrong country or weak evidence | Credibility loss, pact cohesion gain, possible diplomatic penalty |
| Operational failure | Pact action succeeds or target mission misses deadline | Damage, readiness gain for pact, stronger next operation |
| Defector protected | A member or associate provides evidence safely | Major evidence gain, cohesion drop |
| Defector lost | Defection attempt fails | Hostility spike, intimidation event, evidence may still partially survive |

A failed decision should not only be nothing. It should change the living system.
