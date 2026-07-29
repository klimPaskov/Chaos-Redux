# Event 011 Secret Alliance improvement addendum

Status: promoted historical planning addendum.

The accepted five-part source specification under `docs/specs/011_secret_alliance_specs/specs/` supersedes this file as design authority. The prohibition on a manual triggerable scenario in this early plan was rejected by the accepted source specification; SCN-009 Coalition Unmasked is part of the approved Event 011 scope. Retain this file only as the improvement-loop design history.

Working labels in this file are implementation handles only. They are not final localisation, final super-event text, final quote text, final button text, or final cultural references.

## Design problem

The core idea promises a hidden anti-player conspiracy, but a shallow implementation could easily become one popup, a hidden list of countries, and a sudden faction join. That would miss the playable tension. The player should notice odd incidents, make choices with incomplete information, and decide whether to expose, bargain, prepare, or provoke before the compact becomes a public war bloc.

The stronger design is a secret-pact system with three layers:

- a hidden pact roster and organizer logic
- visible symptoms that create player counterplay without revealing the full roster too early
- a reveal threshold that turns the hidden pact into a visible anti-player faction, calls the reveal super-event, and commits members to the war against the player

This event should stay focused. It does not need focus trees, new country tags, formables, or a broad scripted GUI country package. It needs a tight event, decision, sabotage, reveal, super-event, asset, and AI package.

No prior Event 011 addendum or source spec was found in `docs/plans/011_secret_alliance_plans/` or `docs/specs/011_secret_alliance_specs/`, so this plan is not stacking on an unresolved Secret Alliance pass.

## Research anchors

Use these as design inspiration, not as final localisation:

- Interwar small-state security pacts: the Little Entente was described in a 1937 U.S. diplomatic document as a defensive alliance against Hungarian revisionist aims. This supports pacts that claim they are defensive while outsiders suspect a specific target.
- Balkan Entente structure: the 1934 Balkan Pact guaranteed Balkan frontiers, required consultation before obligations to other Balkan states, and created a council structure. This supports a secret compact with consultation, vetoes, and later member invitation rules.
- Anti-Comintern model: the Anti-Comintern Pact began as an ideological anti-Communist agreement between Germany and Japan in 1936, with Italy joining in 1937. This supports ideology-framed pact variants where the public justification differs from the actual anti-player target.
- Covert influence model: Polish Prometheism mixed political, military, intelligence, and cultural work, including emigre networks and influence efforts. This supports non-war pact actions such as press networks, exile contacts, advisers, and sabotage preparation.
- SOE and secret-war model: wartime special operations mixed resistance support, sabotage, wireless work, and supply. This supports active pact operations that cost real resources and create specific incidents instead of abstract penalties.
- Manufactured provocation model: Operation Himmler and Gleiwitz show how false-flag incidents can be used to justify war. Use this carefully as a mechanical inspiration for provocations and evidence manipulation, not as a cheap joke or final cultural reference.

Sources consulted:

- U.S. Office of the Historian, FRUS 1937 document on the Little Entente: `https://history.state.gov/historicaldocuments/frus1937v01/d48`
- AVIM analysis with League of Nations Treaty Series discussion of the Balkan Entente: `https://avim.org.tr/en/Analiz/1934-PACT-OF-BALKAN-ENTENTE-THE-PRECursor-OF-BALKAN-SOUTHEAST-EUROPE-COOPERATION`
- United Nations Treaty Collection, League of Nations Treaty Series overview: `https://treaties.un.org/pages/Content.aspx?path=DB%2FLoNOnline%2FpageIntro_en.xml`
- U.S. Holocaust Memorial Museum, Axis alliance and Anti-Comintern Pact summary: `https://encyclopedia.ushmm.org/content/en/article/axis-powers-in-world-war-ii`
- Foreign Policy Research Institute, Prometheism overview: `https://www.fpri.org/article/2025/05/prometheism-a-polish-covert-action-program/`
- Imperial War Museums, SOE and secret-war overview: `https://www.iwm.org.uk/history/second-world-war/intelligence/soe-the-secret-british-organisation`
- National WWII Museum, invasion of Poland and Operation Himmler summary: `https://www.nationalww2museum.org/war/articles/invasion-poland-september-1939`

Historical uncertainty notes:

- Regional pacts and covert programs varied widely. Do not imply that every inspiration used the same methods.
- Prometheism is useful as a covert-influence model, but its exact operational details should be treated as a research-gated inspiration if final text names it.
- False-flag and assassination inspirations are sensitive. Use them to structure mechanics and serious report tone, not spectacle.

## Core playable loop

### Hidden setup

When Event 011 fires, it should pick the current player country as the target and build a secret pact roster.

The baseline roster should contain three pact members:

- independent countries
- not at war with the player
- not in the player's faction
- not subjects
- not capitulated
- not special chaos countries or nonhuman countries
- not under a terminal or special isolation system
- preferably not in any faction
- plausibly hostile, afraid, rival-aligned, ideologically opposed, threatened by the player, or strategically exposed to the player

The system should not silently accept bad candidates. If three valid countries cannot be found, the event should stay unavailable or delay its setup through the normal event availability system. Do not create dummy members.

Faction preference:

- First pass should prefer countries outside factions.
- If fewer than three factionless candidates exist in a dense faction world, allow a fallback candidate class only if the country is not a faction leader, not in the player's faction, not at war with the player, and can safely leave or defect on reveal.
- The implementation should record whether each member was factionless at selection. This lets reveal logic avoid accidental faction destruction or invalid `leave_faction` behavior.

The pact should have one organizer:

- Baseline: pick one of the three members as organizer, preferably the strongest industry or army among them.
- Evolution II pre-fire: a major can be organizer from the start, with three or more minors as the network.
- Evolution III pre-fire: use the Evolution II opener first, then schedule Evolution III intensification soon after. Do not skip the organizer logic.

### Hidden values

The pact should be governed by dynamic values. These should live in event-specific script constants, with MTTH entries for repeated chance and AI pressure calculations where that keeps `ai_will_do` and pacing readable.

Recommended values:

| Value | Owner | Meaning | Visible to player |
| --- | --- | --- | --- |
| `secret_alliance_pact_cohesion` | global or organizer | how committed members are to acting together | not directly before reveal, summarized as suspicious coordination |
| `secret_alliance_exposure` | player | how much evidence the player has gathered | yes, in decision category header |
| `secret_alliance_threat_pressure` | player | how intense pact activity against the player has become | yes, as public incidents and risk band |
| `secret_alliance_member_commitment` | each member | how likely a member is to invite, sabotage, or join reveal war | hidden or hinted through reports |
| `secret_alliance_provocation_heat` | player or member | how close incidents are to public crisis | yes, after Evolution II |
| `secret_alliance_player_readiness` | player | preparation against pact reveal war | yes, in decision category header |
| `secret_alliance_negotiation_leverage` | player | ability to split or delay the pact | yes, in decision effects |
| `secret_alliance_roster_size` | global | number of live pact members | hidden before reveal, public after reveal |

Cause and effect must be readable. The player should see exposure and readiness move because of decisions, missions, reports, border incidents, and sabotage. They should not see the full country list until reveal or successful exposure.

### Baseline phase

The opening event should tell the player that foreign incidents are becoming patterned without naming every conspirator. The tone should be investigative, uneasy, and political. Do not frame it as a generic diplomatic cable or staff-room briefing.

Baseline behavior:

- three hidden pact members are selected
- organizer receives hidden coordinator flag
- members receive hidden commitment values
- player receives only suspicion/report state, while the full countermeasure category stays locked until Evolution II unless a later accepted spec adds an early-discovery route
- one low-grade suspicious report family starts appearing over time
- pact can invite a small number of additional minor members through hidden MTTH or decision-equivalent AI actions
- no visible faction exists yet
- no automatic war starts at baseline

Baseline incidents should be subtle:

- trade obstruction
- suspicious press campaigns
- embassy leaks
- border rumor reports
- minor industrial accidents with uncertain attribution
- foreign advisors appearing near a player frontier
- anti-player rhetoric in states that already had local reasons to fear the player

Use report events sparingly. The event should not spam the player with every hidden pulse.

## Pact reveal rule

If any live pact member goes to war with the player, the pact reveals.

Reveal should immediately:

1. select or confirm a visible faction leader, usually the organizer unless invalid
2. create a visible anti-player faction using an event-specific faction name or faction template
3. move live pact members into that faction if they are valid and not already in a blocking war state
4. call all live members into the war against the player
5. show the reveal super-event
6. replace secret incidents with open aggression decisions and missions
7. record the event log and evolution context
8. clear or convert secret-only flags and missions

Do not reveal only because exposure reaches a normal investigation threshold. High exposure should let the player split, delay, expose, sanction, or preempt parts of the pact. The full public faction reveal is reserved for war entry, failed brinkmanship, or a player decision that deliberately forces exposure.

If the player attacks a suspected member and the target was in the pact, that also reveals the pact. If the player attacks a suspected country that is not in the pact, the pact should gain cohesion or propaganda leverage instead of revealing.

If a member becomes invalid before reveal:

- annexed, subject, capitulated, transformed, or special-chaos converted members should be pruned
- the organizer should be reassigned if possible
- if fewer than two live members remain, the pact should enter a collapse cleanup path instead of becoming a one-country secret faction

## Evolution entry paths

The event has baseline progression and three true evolutions. The evolutions should not merely be ordinary stages. Each one changes who can join, how openly the pact acts, and how much agency the player has.

### Evolution I: Wider cell network

Design role:

Evolution I turns the initial three-member compact into a minor-state network. It adds more minor members, more visible incidents, and more player pressure without making a major power the organizer.

Unlock direction:

- baseline pact has survived long enough
- pact cohesion is above a threshold
- player exposure remains low while threat pressure rises
- at least one neighboring or same-region minor is eligible
- chaos tier or diplomatic panic state makes expansion plausible

Active-event evolution:

- existing pact invites one to three additional minors over time
- invite chance depends on ideology, fear of player, border proximity, rival claims, past wars, and factionlessness
- player receives stronger suspicious reports and may gain passive evidence for the later countermeasure category
- pact incidents become more noticeable
- some new members join as low-commitment associates that can be peeled away

Pre-fire evolved opening:

- initial setup may start with four or five minors instead of three
- organizer is still a minor unless Evolution II is also available at first fire
- player starts with more suspicion and less time before Evolution II countermeasures become available

Player experience:

- the player sees enough pattern to suspect a wider network
- they can infer likely regions and prepare informally through ordinary play
- the full spend-resources counterplay starts when Evolution II unlocks the category
- later, they can identify likely members, prepare borders or industry, and attempt to split low-commitment members

### Evolution II: Major organizer or violent methods

Design role:

Evolution II makes the pact dangerous. A major can organize or sponsor it, and the pact can use active sabotage, provocations, assassinations, and industrial damage.

Unlock direction:

- Evolution I exists or equivalent network size exists
- player is a major, a regional hegemon, or a high-threat country
- a major rival is eligible and not at war with the player
- pact exposure or threat pressure is high
- world tension, chaos tier, or active wars create plausible clandestine escalation

Active-event evolution:

- if no major is in the pact, try to add one major sponsor or organizer
- if a major cannot join, upgrade the strongest member into a hardened organizer and raise sabotage intensity
- sabotage incidents can damage factories, infrastructure, railways, air bases, ports, or supply nodes using existing reusable building-damage helper patterns
- assassination or killing incidents should be rare and should create severe stability, command, or advisor consequences only when a safe target surface exists
- provocations can start border-war missions only against neighboring pact members

Pre-fire evolved opening:

- start with one major organizer and three minor members where possible
- if no eligible major exists, start with a stronger minor organizer, four minors, and high sabotage readiness
- initial player event should communicate that several incidents already predate the public discovery

Player experience:

- counterplay becomes urgent
- the player can choose between public exposure, covert infiltration, negotiation, counter-sabotage, and war preparation
- bad choices can increase provocation heat and make reveal more likely

### Evolution III: Public shadow bloc

Design role:

Evolution III makes the pact's existence difficult to deny. It does not have to start immediate war, but the faction's outlines appear on the map and aggression becomes hard to contain.

Unlock direction:

- Evolution II has fired or pre-fire Evolution II opener exists
- pact has at least five live members or a major organizer plus three live minors
- player failed or declined major exposure and split-pact actions
- provocation heat or threat pressure is high
- at least one pact country borders the player or controls a strategic route near the player

Active-event evolution:

- the pact may reveal as a visible faction without immediate war if no member is currently at war with the player
- visible faction has a war-preparation mission or crisis timer rather than instant declaration
- members receive open anti-player decisions
- player gets emergency diplomacy and border-war decisions
- a second major can join if player choices increased pact cohesion or if the player is much stronger than the pact

Pre-fire evolved opening:

- start from Evolution II setup first
- schedule Evolution III intensification with MTTH or short delayed event after the pact has initialized
- do not start directly with a fully visible faction unless there is already a direct war condition

Player experience:

- the player sees a public anti-player bloc forming
- war is likely, but still shaped by decisions, border preparation, and negotiation
- a prepared player can split members, delay the declaration, or choose a limited border conflict before general war

## Candidate selection and member roles

### Candidate scoring

Member selection should use weighted logic, not uniform random picks. Strong factors:

| Factor | Effect |
| --- | --- |
| not in faction | strong increase |
| borders player | strong increase |
| has lost land to player or has claims against player | strong increase |
| player has high generated threat or world tension contribution | moderate increase |
| ideological hostility to player | moderate increase |
| historical or regional rivalry with player | moderate increase |
| recently harmed by player actions or wars | strong increase |
| same continent or nearby sea-region to player | moderate increase |
| far overseas without route or interest | strong decrease |
| weak, isolated, or near capitulation | decrease unless backed by major organizer |
| already in a major faction | strong decrease |
| in player's faction or war with player | reject |

The player country should never be selected as a pact member. The player is always the target.

### Roles

Each pact member should receive one role. Roles can change on evolution.

| Role | Typical holder | What it does |
| --- | --- | --- |
| Organizer | strongest member or major sponsor | invites members, keeps cohesion, leads reveal faction |
| Financier | industry-heavy minor or major | funds sabotage and press networks |
| Border arm | neighbor of player | creates frontier missions, border war candidates, provocations |
| Intelligence node | country with agency bonuses or high stability | increases exposure race, leaks, counter-intelligence conflicts |
| Agitator | ideological enemy | press campaigns and party pressure |
| Reluctant member | low-commitment minor | can be split, bribed, or neutralized by player |
| Major sponsor | Evolution II or III major | raises cohesion, sabotage intensity, and diplomatic shield |

Roles should matter mechanically. For example, border arms are the only members that can generate border-war decisions, financiers reduce sabotage costs, and reluctant members are the best negotiation targets.

## Player decision category

Working category label: `secret_alliance_response_category`.

The full category should appear for the player at Evolution II, when the pact's actions become concrete enough for countermeasures. Before Evolution II, the player should learn through the opening event and suspicious reports, not through a broad response menu. If implementation later accepts an early-discovery variant, it should expose only a compact watchlist or single investigation action and should not reveal the full decision suite.

The category should disappear only when the pact collapses, reveals into normal war handling, or is fully neutralized.

Category header should show:

- exposure level
- threat pressure level
- player readiness level
- provocation heat once Evolution II is active
- latest known suspect type, not necessarily a country name
- whether the pact is hidden, partially exposed, or public

Use normal decisions first. A custom scripted GUI can be queued only if the decision category becomes too crowded during implementation. If a GUI is added, it should be a compact intelligence board with suspect cards, exposure meter, readiness meter, and pact pressure band. It must reuse the same decision effects and AI equivalents.

### Decision family: investigate the network

Purpose: raise exposure and identify likely members.

Actions:

- Open Embassy Files: costs political power and civilian factory burden, raises exposure, low risk.
- Trace Arms Shipments: costs convoys, command power, or navy XP depending on route access, can identify financier or border arm.
- Break Courier Lines: costs infantry equipment and support equipment, can reduce member commitment, raises provocation heat if failed.
- Offer Amnesty to Envoys: costs stability or political power, can reveal a reluctant member or lower cohesion.

Missions:

- Secure Capital Archives: timed mission requiring capital control, stability above a low threshold, and no severe sabotage state. Success gives exposure and readiness. Failure raises threat pressure.
- Follow the Border Couriers: timed mission requiring supplied divisions in likely border states or capital if no border exists. Success can reveal a border arm.

AI behavior:

- Human player owns this category in normal play, but if the player country is AI in automated tests, AI should prioritize exposure when threat pressure is high and stability is not collapsing.

### Decision family: prepare the country

Purpose: make reveal war survivable without instantly starting it.

Actions:

- Harden Rail Junctions: costs trains, support equipment, and civilian factory burden, reduces sabotage damage and raises readiness.
- Guard Armories: costs infantry equipment and command power, lowers killing and arsenal-sabotage chance.
- Quiet Mobilization: costs command power, manpower, and war support strain, raises readiness but increases provocation heat.
- Emergency Airfield Watch: costs fuel or air XP, protects air bases and radar from sabotage.
- Port Screen: costs convoys or navy XP, protects ports and naval bases.

Missions:

- Hold the Suspect Frontier: timed objective for neighboring member or suspected member borders. Requires supplied divisions in named border states. Success raises readiness and can deter a border arm. Failure raises provocation heat.
- Secure the Supply Spine: timed objective around rail hubs, capital, and supply node states. Success reduces future damage. Failure increases next sabotage damage.

Costs should scale with player size. Large players should pay larger equipment, train, convoy, and factory burdens. Small players should pay smaller costs but get less broad protection.

### Decision family: expose or negotiate

Purpose: give the player non-war tools that are neither free nor guaranteed.

Actions:

- Leak a Partial Dossier: requires exposure threshold, lowers pact cohesion, may identify one member, but can drive the organizer to accelerate.
- Demand Public Clarification: targets a suspected member. If correct, reduces its commitment or forces partial reveal. If wrong, increases pact propaganda leverage.
- Quiet Settlement: targets a low-commitment suspected member. Costs political power, civilian factories, or equipment. Can remove that country from the pact if negotiation leverage is high.
- Split the Pact Council: requires high exposure and at least one reluctant member. Can remove one member, lower cohesion, or delay reveal.
- Force the Names Into the Open: high exposure decision. Publicly reveals identified members and can trigger the faction reveal if the pact decides to stand together.

Failure and partial success:

- Negotiation can lower threat pressure while raising exposure.
- Public exposure can reduce cohesion but increase provocation heat.
- Wrong accusations should not reveal hidden mechanics. They should create visible diplomatic and stability costs.

AI behavior:

- Pact AI should resist negotiation based on commitment, ideology hostility, player strength, and organizer cohesion.
- Reluctant members should accept more often if low stability, no border with player, low ideology hostility, and no major sponsor.

### Decision family: counter-sabotage

Purpose: respond to Evolution II incidents with concrete resource tradeoffs.

Actions:

- Sweep Railway Crews: costs support equipment and trains, lowers rail sabotage.
- Watch Factory Gates: costs command power and military factory output burden, lowers factory sabotage.
- Raid Safehouses: costs infantry equipment and stability, can remove a member operation but raises provocation heat.
- Double the Agents: requires exposure and intelligence readiness. Can reduce pact cohesion or discover organizer role.

Use the existing reusable `damage_buildings_in_random_states` pattern for sabotage implementation where possible. Damage should target controlled states and should respect player preparation.

### Decision family: border wars and limited provocations

Purpose: give neighboring players a limited military response before general war.

Available only when:

- a live pact member borders the player
- the pact member is not already at war with the player
- both sides own and control adjacent states
- neither side already has a border war with the other
- Evolution II or III is active, or provocation heat is high
- the player has enough readiness or has completed a frontier mission

Actions:

- Challenge the Frontier Cell: starts a non-transfer border war against a neighboring pact member.
- Seize the Provocation Site: shorter, riskier border war if the member triggered a recent provocation.
- Stand Down the Frontier: reduces provocation heat and threat pressure but lowers readiness or costs political capital.

Border wars should use `change_state_after_war = no`. They are about disrupting the pact and creating leverage, not free state transfer.

Outcomes:

- player win: raises readiness, lowers member commitment, may reveal that member
- player loss: raises pact cohesion, threat pressure, and chance of full reveal
- cancel: moderate provocation heat and temporary cooldown

Do not let the player farm repeated border wars. Use per-pair and global cooldowns, and remove or hide decisions when the member is invalid, capitulated, annexed, subject-converted, or already in a full war.

## Pact AI behavior

AI is central because all pact members are AI countries against the player.

### Member AI

Member actions should be weighted by role and situation:

| Situation | AI direction |
| --- | --- |
| borders player and has enough divisions | prefer frontier pressure and border incidents |
| much weaker than player | prefer secrecy, sabotage, and major sponsor requests |
| same ideology as organizer | higher commitment |
| high stability and no direct grievance | lower commitment, more likely to accept negotiation |
| in faction before secret pact | avoid reveal unless safe to leave or faction rules permit |
| already in another war | reduce sabotage and invitation activity, unless player is an enemy or opportunity target |
| player is overextended in major war | higher chance of provocation and reveal preparation |
| player has high exposure | reduce risky operations or accelerate reveal depending on organizer personality |

### Organizer AI

Organizer should:

- maintain cohesion
- invite candidates when roster is below target
- avoid inviting countries that would make reveal invalid
- choose sabotage only when threat pressure has room to rise
- push reveal if a pact member is attacked by the player or a full war becomes advantageous
- delay reveal if exposure is high but pact readiness is low
- seek a major sponsor at Evolution II when not already a major

Use MTTH entries for invite, sabotage, provocation, and reveal pressure calculations. This keeps AI behavior readable and tunable.

### Major sponsor AI

Major sponsor should not behave like a free win button.

It should:

- join only if it is not at war with the player
- consider player strength, distance, war state, ideology, threat, and faction obligations
- prefer proxy sabotage and pressure before reveal
- become more likely if player is dominant, isolated, or already fighting several wars
- become less likely if it would be pulled into a suicidal war immediately

### Revealed faction AI

After reveal:

- faction leader prioritizes calling members, defending member capitals, and opening fronts against the player
- border members prioritize local defense and limited attacks
- remote members prioritize expeditionary support, naval pressure, or lend-lease style aid if a direct front is impossible
- reluctant members can get lower offensive AI but still join the war if reveal conditions require it

## Rare variants

Rare variants should be low-frequency and clearly gated. They should add replay value without bloating the event.

### Exile Committee variant

Condition:

- player has annexed or occupied several countries
- exiled or released states exist nearby
- at least one eligible member has claims or cores lost to the player

Behavior:

- pact uses exile networks, claims, and restoration language
- more likely to invite countries harmed by player expansion
- negotiation can split members by offering autonomy or settlement
- sabotage focuses on logistics and propaganda rather than random killings

Asset direction:

- report art should show clandestine committee or printing-room mood, not a generic conference table

### Ideological Counterweight variant

Condition:

- player ideology is extreme or globally threatening
- several eligible candidates are ideologically opposed

Behavior:

- pact justification uses ideology rather than border fear
- Anti-Comintern style inspiration is useful if the target is communist or if the member group is anti-revolutionary
- other ideological pairings should use period political rhetoric research before final text
- decisions should include propaganda exposure and party-pressure countermeasures

### Border Memory variant

Condition:

- player borders several pact candidates
- player has recently taken states, generated threat, or fought regional wars

Behavior:

- border arms dominate roster roles
- border-war decisions unlock earlier
- sabotage targets rails, supply hubs, and forts
- pact reveal can create a dangerous but geographically coherent front

### Merchant Channels variant

Condition:

- island player, overseas empire, or pact members connected by sea rather than land

Behavior:

- fewer border wars
- more port, convoy, naval-base, and trade-route incidents
- Port Screen and Trace Arms Shipments decisions become more important
- reveal faction can still be dangerous through naval access, convoys, and expeditionary support

### Double-Cross variant

Condition:

- player achieves high exposure and high negotiation leverage before reveal
- at least one reluctant member exists

Behavior:

- one member can secretly become an informant
- informant provides exposure boosts or reduces sabotage damage
- if mishandled, organizer discovers the leak and accelerates reveal
- the informant should not automatically become a player ally or puppet

## Event and report family

The chain should use a small set of event families rather than dozens of generic popups.

### Opening event

Role:

- establishes the pattern
- starts player suspicion state and later enables Evolution II countermeasure unlocks
- does not reveal all members
- records Event 011 as fired

Text direction:

- player viewpoint
- unease from repeated incidents
- mention foreign meetings, unusual couriers, economic pressure, or border rumors
- avoid final quotes, staff-table framing, and direct "this is a warning" labels

Option direction:

- one practical option that accepts the response category
- optional route-specific reaction direction based on ideology or player threat status, but final wording must be written later

### Suspicious incident reports

Roles:

- low-grade baseline reports
- stronger Evolution I reports
- sabotage reports at Evolution II
- public bloc reports at Evolution III

Report types:

- press campaign
- embassy channel
- border drill
- arms shipment
- rail accident
- factory fire
- advisor disappearance
- provocation site
- leaked meeting place

Each report should either move a value, unlock a target, or update a mission. Do not add flavour-only reports unless they are part of pacing and explicitly have no mechanical consequence.

### Member invitation report

Role:

- shows that the pact is widening without full reveal
- may identify region, role, or suspect type
- should not list all members unless exposure is high

### Negotiation result events

Role:

- split, fail, or partially expose a member
- show consequences of player diplomacy
- keep uncertainty when the target was not actually a member

### Reveal event

Role:

- normal event wrapper that applies reveal effects and triggers the super-event
- should be aligned with event log and history
- after reveal, normal reports can handle war escalation and member reactions

## Super-event direction

The reveal deserves a super-event because it converts a hidden anti-player compact into a public war faction and forces all live members into the conflict.

Super-event role:

- first public reveal of the anti-player pact
- faction formation
- war commitment threshold

Trigger:

- any live pact member enters war with the player
- or player deliberately forces public exposure and the pact chooses collective war
- or Evolution III visible bloc reaches a war-preparation crisis threshold and chooses declaration

Text research gate:

- Do not implement final title, button text, quote, or cultural remark from this addendum.
- Use `chaos-redux-super-events` and the super-event text researcher for final quote and remark selection.
- Good quote themes: secret compacts, false peace, betrayal, encirclement, open names after hidden plotting, small states acting together, fear of hegemony.
- Avoid final cultural references until sourced and checked.

Image direction:

- generated period-authentic documentary-style image is preferred because the pact is fictional and campaign-dynamic
- subject should be a clandestine council becoming public, sealed documents and radio cables, or a line of flags emerging from shadow
- avoid map-only art, modern intelligence walls, readable generated text, and generic conference tables
- if a real historical pact inspiration is directly named in final text, image sourcing must avoid misrepresenting a real meeting as the fictional pact

Audio direction:

- use a researched public-domain or clearly licensed musical track
- tone should be restrained, conspiratorial, and martial, not supernatural or triumphant
- do not reuse another super-event track without explicit approval and documentation

Suggested file planning:

- research note: `docs/super_events/011_secret_alliance/research.md`
- image assets: `docs/assets/011_secret_alliance/` and final `gfx/super_events/011_secret_alliance/`
- audio assets: `music/011_secret_alliance/` and `sound/011_secret_alliance/` per super-event skill if implemented

## Asset and animation needs

Static asset families:

| Asset | Use | Source mode |
| --- | --- | --- |
| report event image, secret meetings | opening and baseline reports | generated documentary-style |
| report event image, sabotage aftermath | Evolution II sabotage reports | generated documentary-style |
| report event image, public compact | Evolution III public bloc reports | generated documentary-style |
| super-event image | reveal | generated unless final research demands sourced material |
| decision category icon | response category | generated icon |
| decision icons | investigate, prepare, expose, negotiate, counter-sabotage, border war | generated icons |
| idea icons | public suspicion, anti-pact preparations, sabotage damage, pact pressure | generated icons |
| faction emblem | visible anti-player pact | generated emblem or faction template art if supported |
| achievement icons | if achievements are later added | generated icons |

Animated assets:

| Asset | Surface | State logic | Static fallback |
| --- | --- | --- | --- |
| sealed dossier pulse | decision category or optional GUI header | exposure above first threshold | static sealed dossier |
| cipher-line warning | category header or suspect card | threat pressure high or sabotage pending | static cipher line |
| red frontier frame | border-war decision or optional GUI card | neighboring pact member and high provocation heat | static warning frame |
| reveal seal break | super-event adjacent GUI or report art variant | reveal has fired | static broken seal |

Animation rules:

- use `chaos-redux-frame-animation`
- final animations need real source frames, frame sheets, static fallbacks, manifests, and `.gfx` handoff notes
- do not create transform-only glow, opacity pulse, or GIF-only assets
- animation should clarify state, not decorate every button

If implementation chooses normal decisions with no custom GUI, keep animation to the category icon/header and border-war warning asset. Do not build a large scripted GUI only to showcase animation.

## Idea and modifier lifecycle

Use a small number of meaningful ideas or timed modifiers.

Player-side ideas:

- Public Suspicion: mixed stability or political cost while exposure is low and threat pressure rises. Removed when pact reveals or collapses.
- Emergency Counter-Intelligence: preparation idea upgraded by prepare decisions. Removed or converted after reveal.
- Sabotaged Logistics: temporary damage pressure after serious sabotage. Removed by repair/counter-sabotage actions or timeout.
- War Preparedness Against the Pact: readiness payoff after strong preparation. Converts into wartime defensive bonus after reveal.

Pact-side ideas:

- Secret Compact Discipline: organizer or member hidden/visible effect representing cohesion. Removed or converted after reveal.
- Foreign Safehouses: intelligence node role support. Removed by successful raids or exposure.
- Reluctant Signature: low-commitment member vulnerability. Removed by negotiation, reveal, or organizer crackdown.
- Sponsor Shield: major sponsor support. Removed if sponsor exits, is exposed, or joins open faction.

Avoid idea stacks. Upgrade, replace, or remove ideas through decisions and reveal/collapse paths.

## Implementation surfaces affected

If accepted, promote the design into `docs/specs/011_secret_alliance_specs/` and implement through these likely surfaces:

- `events/011_secret_alliance.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/mtth/011_secret_alliance_mtth.txt` or append event-specific entries to the existing MTTH file if repo pattern prefers one file
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/ideas/011_secret_alliance_ideas.txt`
- `common/on_actions/011_secret_alliance_on_actions.txt` only for narrow cleanup hooks, not broad daily or weekly iteration
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- event log and event-name mappings required by `chaos-redux-events`
- super-event localisation, sprite, audio, and docs surfaces if the reveal super-event is accepted
- `docs/events/011_secret_alliance/overview.md`
- asset manifests and super-event research notes

On actions:

- Use targeted hooks such as war start, faction leave, capitulation, annexation, puppet, release, government change, and subject changes where available and appropriate.
- Do not add broad daily, weekly, or monthly world iteration. If implementation thinks a world pulse is unavoidable, the main agent must ask the user first.

## Cleanup and invalidation

Cleanup must handle:

- member annexed
- member capitulated
- member becomes subject
- member joins player faction
- member enters war with player and reveal fires
- organizer invalid and replacement needed
- player tag transformed by another event
- pact roster below minimum
- faction leader dies after reveal
- border-war target invalidated
- global event targets used for persistent suspect/member pointers
- active decisions and missions after reveal or collapse

Use arrays for live roster and suspect lists where useful, with refresh helpers. Avoid stale global event targets. If global event targets are used for organizer or selected suspect, clear them on collapse/reveal cleanup.

## Balance and exploit checks

The implementation should explicitly check these:

- pact cannot select the player, player faction members, direct enemies, invalid countries, or special chaos countries
- event does not fire when three valid members cannot be found
- member invite logic does not grow without caps
- sabotage cannot repeatedly damage the same player beyond planned cooldowns
- player cannot farm exposure or readiness from cheap repeat decisions
- negotiation cannot remove all members without commitment, exposure, and cost
- border-war decisions cannot be repeated against the same pair without cooldown
- false accusation cannot reveal the hidden roster
- reveal faction does not break existing factions through unsafe forced membership moves
- full war reveal cannot call invalid or dead members
- AI does not use border incidents when it has no adjacent controlled states
- no broad on-action iteration is introduced without explicit approval

## Acceptance criteria

The implemented Secret Alliance system should satisfy all of the following:

- Event 011 can initialize a hidden anti-player pact with three valid countries and an organizer.
- Initial members are not at war with the player, are not in the player's faction, and strongly prefer factionless candidates.
- The pact has dynamic cohesion, exposure, threat pressure, member commitment, provocation heat, and player readiness values.
- The player receives a decision category with visible exposure, threat, readiness, and current phase summaries.
- Player decisions include investigation, preparation, exposure/negotiation, counter-sabotage, and border-war families with concrete costs beyond political power.
- Decisions and missions use dynamic costs, custom requirement text, meaningful success/failure effects, and cleanup.
- Pact members can invite others with caps, role logic, candidate validity, and AI behavior.
- Evolution I adds more minors and stronger visible incidents.
- Evolution II supports a major organizer or sponsor, active sabotage, provocations, rare killings, and industry/logistics damage.
- Evolution III can make the pact public and intensify aggression without forcing immediate war unless reveal conditions are met.
- If any pact member enters war with the player, the pact reveals, forms a visible faction, triggers the reveal super-event, and live members join the war against the player.
- Reveal, collapse, negotiation success, member invalidation, and world-state changes clean stale roster, mission, target, and decision state.
- AI behavior exists for member roles, organizer actions, major sponsor behavior, invite logic, sabotage, negotiation resistance, border incidents, and revealed faction war priorities.
- Required visual assets are planned, produced, processed, wired, and documented before completion claims.
- Animated assets, if implemented, use real source frames, frame sheets, and static fallbacks.
- The reveal super-event receives sourced quote, title direction, button direction, image, audio, docs, and spreadsheet alignment through the proper super-event workflow.
- Event docs and Event Log surfaces describe the premise and evolutions without exposing hidden future surprises.

## What should not be added

- Do not add a world-end branch.
- Do not add a manual triggerable scenario.
- Do not add a cluster entry unless the parent later changes the event classification plan.
- Do not add focus trees or country packages for pact members.
- Do not add formables.
- Do not turn the pact into a generic world threat framework source unless later design makes it existential. This is a dangerous anti-player bloc, not a global supernatural threat.
- Do not let every incident become a popup. Use reports only when they move values, unlock choices, or mark a meaningful threshold.
- Do not make the player-facing text reveal hidden variables, future reveal conditions, or the full roster before exposure mechanics justify it.
- Do not use final quotes, slogans, cultural remarks, or historical references without source checks.

## Promotion guidance

Keep this file in `docs/plans/011_secret_alliance_plans/` until the parent accepts or rejects it.

If accepted, fold the design into a source spec pack under `docs/specs/011_secret_alliance_specs/`. Recommended split:

- `specs/011_secret_alliance_spec_part_1_core_pact.md`
- `specs/011_secret_alliance_spec_part_2_decisions_and_sabotage.md`
- `specs/011_secret_alliance_spec_part_3_evolutions_ai_balance.md`
- `specs/011_secret_alliance_spec_part_4_assets_super_event_acceptance.md`
- `research/011_secret_alliance_research_notes.md`
- `prompts/011_secret_alliance_super_event_prompt.md`
- `prompts/011_secret_alliance_asset_prompt.md`
- `prompts/011_secret_alliance_coding_prompt.md`

If rejected, record the rejection reason in this plans folder so a later improvement-loop pass does not repeat the same design.
