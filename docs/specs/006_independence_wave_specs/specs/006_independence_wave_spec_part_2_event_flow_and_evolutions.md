# Independence Wave, Part 2: Event flow, escalation, and evolutions

All names in this file are working labels, not final localisation.

## Baseline event flow

Independence Wave uses one repeatable event identity with a persistent network of released countries. Ordinary wave growth is baseline progression. Evolutions are separate mutation tracks that change how future and existing Independence Wave countries behave.

### Phase 1: Pressure before the wave

The event is eligible when the world contains enough valid candidate packages to meet the current wave count without deleting a host.

Selection weight should rise when:

- several countries hold large non-core regions
- colonial empires retain extensive territory
- federal or imperial hosts have low stability
- recent wars, capitulations, occupations, or peace settlements have weakened host authority
- prior liberation events have made secession appear possible
- several candidate regions contain unrecognized movements or old claims
- chaos is high
- the Liberations cluster is eligible

Selection weight should fall when:

- too few viable hosts exist
- most candidates already live
- the previous wave fired recently
- the same host or region dominated the last wave
- protected-state reservations leave too little valid territory
- a terminal campaign state has disabled ordinary random events

The event does not require a historical petition, autonomy flag, or active resistance movement for every candidate. Those factors improve eligibility and influence opening legitimacy. The supernatural premise is that a wave can suddenly make dormant claims politically real.

### Pre-event surface decision

The Independence Wave has no pre-event pressure system. No country-facing pressure category, mission, cost, queue, history row, or other decision surface may appear before the public Event 006 report fires.

Pressure, resistance, instability, or occupation conditions do not imply that the wave has begun and do not create an early request. The synchronized allocator is entered only by the public Event 006 firing path or by explicitly post-event systems such as Join, with the normal host-survival, reservation, origin, and collision contracts unchanged.

The former crisis source is retained only as inert compatibility code for stale scripted references. It is not part of the player-facing design and must remain hard-disabled in runtime triggers; new implementation work must not restore or reference its category, mission, cost, queue, or pre-event history.

## Scoped conversion: Join the Independence Wave (accepted current addition, 2026-08-09)

Join the Independence Wave is a voluntary conversion offer for a living, independent country that has lost at least half of its former owned-state footprint and at least two states, while retaining only states covered by one prepared Event 006 homeland package.

The offer is discovered only from bounded callbacks for the affected country scopes, including war-entry observation and state-control, peace-conference, capitulation, and release changes; the addition does not introduce a daily, weekly, monthly, or on-game-start world scan.

On `on_state_control_changed`, the old controller and current owner are re-evaluated without manufacturing an owned-state loss because controller changes do not prove ownership changes.

War entry records the exact pre-loss owned-state baseline for both belligerents, and core-count reconstruction runs only when no prior peak baseline exists.

When the shared Liberations coordinator is busy, the source schedules the hidden country-scoped retry event `chaosx.nr6.40` only after the eligible, threshold, and busy-coordinator recheck; the pending marker is `independence_wave_join_retry_pending` and the centralized retry interval is `independence_wave_join.retry_days = 7`.

The retry marker clears on offer, success, decline, failure, or ineligibility, so a qualifying country receives a later bounded opportunity without holding a second release transaction or requiring a world iteration.

The conversion still reserves one exact package, proves complete remaining-territory coverage, uses the ordinary frozen release transaction, and changes a human source tag only after setup, validation, and commit succeed.

Decline and timeout retain the existing country and apply the scoped refusal cooldown, while failure records the normal failure receipt and uses the shared compensating rollback when safe.

### Phase 2: Wave planning

The event builds and locks the release plan described in Part 1.

The plan records:

- wave number
- chaos band
- target count
- selected candidate package IDs
- selected hosts
- anchor, compact, and extended states
- protected host states
- origin assignment
- starting package severity
- government archetype pool
- military archetype
- regional overlay
- host response profile
- patron interest profile
- league eligibility
- rare variant eligibility

### Phase 3: Synchronized release

All countries appear in the same incident. The exact script can execute sequentially, but the design treats the moment as simultaneous and prevents earlier releases from invalidating later ones.

The player-facing summary should communicate:

- how many countries appeared
- which broad regions were affected
- whether the wave was concentrated or global
- whether one host suffered several releases
- whether any released state began with an army, foreign backing, or radical government
- whether a previous Independence Wave network reacted

The summary should not list raw modifiers, package IDs, or future secret routes.

### Phase 4: The first seventy-two hours

Every released country receives immediate setup.

- provisional government or public leadership body
- provisional capital
- starting laws and ruling coalition
- basic diplomatic status
- starting national spirits
- mechanic values
- emergency forces
- first category of survival decisions
- temporary protection against instant AI self-destruction
- former host relation state
- opening focus or overlay access
- AI route seed

Every distinct former host receives one consolidated crisis response for all of its losses in the committed Event 006 wave, as specified in the accepted host-response defaults below.

Nearby majors and regional powers receive interest scores rather than one popup per country. High-interest states can receive targeted recognition, intervention, or patron events.

### Phase 5: The first one hundred and eighty days

Every new state enters a founding mission sequence.

The first mission asks the country to establish minimum statehood across four public pillars:

1. population and administration
2. defensible territory
3. functioning government
4. external relations

These pillars are inspired by period statehood practice, but the in-game system uses plain player-facing terms. The four pillars feed Government Capacity, Recognition, Legitimacy, and Security.

The country chooses an early priority:

- constitutional order
- mass mobilization
- traditional authority
- military emergency rule
- foreign sponsorship
- league cooperation

The priority shapes short-term decisions and route weights. It does not permanently lock the political tree until the country reaches a formal constitutional settlement.

### Phase 6: Recognition and host settlement

The country seeks bilateral recognition, guarantees, trade access, diplomatic missions, and eventual admission to wider international institutions.

The former host can:

- accept independence
- offer autonomy or reunion
- demand demobilization
- negotiate borders
- sponsor a friendly cabinet
- impose a blockade
- seek arbitration
- prepare reconquest

A settlement can be peaceful, coercive, delayed, or impossible. Countries that survive without recognition can continue, but they face trade, diplomacy, and legitimacy pressure.

### Phase 7: Network formation

Once several Independence Wave countries exist, they can form bilateral cooperation links and regional councils.

Shared actions include:

- mutual recognition
- emergency arms transfers
- refugee and civil service exchanges
- officer missions
- joint border arbitration
- common guarantees
- league congress preparation

The global league does not appear automatically. It requires enough living members, political preparation, and a charter route.

### Phase 8: Regional ambition

Stable countries can pursue larger identities through decisions. These ambitions use the regional formable registry and package-specific claim families.

The route can be diplomatic, federal, dynastic, revolutionary, military, religious, or high-chaos. Each method changes integration costs, member consent, diplomatic backlash, and post-formation content.

### Phase 9: Long-term memory

A country remains part of the Independence Wave network until it is annexed, voluntarily merged, or loses its origin through an explicit transformation.

The network remembers:

- recognition history
- former host settlement
- patron influence
- league votes
- wars among released countries
- rescue or abandonment of members
- formable progress
- route extremity
- survival time
- whether the country later sponsored another wave

## Baseline incidents

The event needs recurring incidents that make the survival system feel active.

### Founding incidents

- capital administration breaks down or stabilizes
- provisional currency crisis
- civil servants refuse or accept transfer
- police and garrison allegiance dispute
- port, railway, or telegraph control dispute
- first flag and seal controversy
- leader legitimacy challenge
- emergency census or registration drive
- refugee movement from the former host
- former host property claims

### Recognition incidents

- first bilateral recognition
- foreign mission arrival
- denied diplomatic credentials
- recognition conditional on arms limits
- trade office accepted without full recognition
- rival patron offers competing guarantees
- major power demands basing access
- recognition vote fails narrowly
- league members coordinate a recognition campaign

### Security incidents

- militia refuses central command
- border guards defect from the host
- depot seizure
- officer shortage
- foreign volunteers arrive
- army faction enters politics
- former host probes the border
- disputed town declares allegiance
- demobilization talks
- emergency conscription backlash

### Government incidents

- constituent assembly dispute
- royal or traditional claimant returns
- military council extends emergency rule
- labor council demands executive power
- clergy contests secular law
- provincial leaders resist the capital
- patron-backed ministers enter cabinet
- corruption scandal damages the provisional government

### League incidents

- member asks for arms
- member asks for arbitration
- host attacks one member
- patron tries to capture the secretariat
- radical member proposes collective war
- democratic member demands a rights charter
- regional caucus blocks a global vote
- expelled member forms a rival bloc

### Formable incidents

- congress convenes
- member state refuses integration
- capital dispute
- flag and constitutional identity conflict
- border plebiscite
- old dynasty or movement claims leadership
- foreign powers threaten non-recognition
- army demands immediate centralization
- integration mission fails in one region

## Wave variants

The same release count can produce different narratives.

### Distributed wave

Candidates come from several continents. This is the default high-variety pattern.

Gameplay result:

- several separate hosts
- cross-regional patron competition
- early opportunity for a global league
- fewer immediate border wars among new states

### Imperial fracture

Several countries come from one large host.

Gameplay result:

- consolidated host crisis
- connected borders
- regional congress and formable opportunities
- higher risk of coordinated reconquest
- stronger local league play

### Colonial chain reaction

Several colonies or mandate regions become independent.

Gameplay result:

- recognition and trade access dominate
- former colonial power chooses between negotiated retreat and punitive intervention
- outside powers compete through investment, arms, and guarantees
- local elites and mass movements have different legitimacy profiles

### Federal unravelling

Several republics, autonomous areas, or federal regions break away.

Gameplay result:

- shared institutions and army assets must be divided
- host cores and legal claims remain contested
- border, railway, and debt settlement decisions matter
- Event 5 overlap must be checked carefully in Soviet regions

### Restoration wave

Several historical polities appear in different regions.

Gameplay result:

- traditional authority and historical symbolism have stronger opening legitimacy
- government capacity is often weaker than symbolic legitimacy
- formable and restoration routes appear earlier
- foreign recognition may demand constitutional guarantees

### Indigenous sovereignty wave

Several indigenous or local nations emerge.

Gameplay result:

- land, language, community governance, and external guarantees become central
- package research must distinguish internal territorial identities
- route design avoids a single generic tribal government
- borders may remain deliberately limited while wider cultural claims become diplomatic objectives

### Armed wave

Countries begin with defecting units, seized depots, or foreign volunteers.

Gameplay result:

- higher Security
- higher former-host hostility
- military route temptation
- faster border wars
- stronger danger milestone eligibility

### Patron wave

Several releases begin with outside backing.

Gameplay result:

- recognition rises faster
- dependency pressure starts high
- rival patron incidents begin immediately
- league formation may be delayed by sponsor blocs

## Evolution structure

Independence Wave has five evolution stages. Each chaos tier can unlock one stage. These are genuine mutations that add new behavior. The baseline wave count remains separate.

Each evolution applies only after the public Event 006 report has fired:

- active-event evolution, which changes countries already released by Event 6
- post-report opening package, which changes the first package created by a later wave

The final evolution names require implementation localisation work. The labels below are structural.

## Evolution 1: Replicable Independence

Earliest band: Gathering Storm

### Design meaning

The first wave proves that sudden independence can be copied. Political movements, exile circles, local elites, veterans, labor groups, clerics, and traditional authorities begin preparing for the next rupture.

### Active-event evolution

Existing Independence Wave countries gain:

- diplomatic missions to endorse future candidates in their region
- a limited ability to sponsor recognition for a later wave
- civil service exchange decisions
- an early network of bilateral recognition
- first regional conference events

### Post-report opening package

Countries released after the public report may start with:

- one prepared institution, such as a civil service, militia committee, traditional court, trade office, or exile cabinet
- slightly higher opening Legitimacy or Government Capacity
- a chance to have prior contact with an earlier released country
- a lower chance of a completely improvised leader

### New incidents

- copied declarations
- borrowed constitutional drafts
- volunteer civil servants
- shared flag and seal workshops
- former hosts coordinate anti-secession policy

### Failure and containment

The evolution weakens when earlier released countries are rapidly annexed, become puppets, or collapse. The system can still remain unlocked, but later countries start with caution and lower confidence.

## Evolution 2: Dormant Nations

Earliest band: Rising Chaos

### Design meaning

The candidate pool expands beyond obvious releasables. Historical states, local polities, indigenous nations, city-centered identities, island states, and old confederacies become viable.

### Active-event evolution

Existing countries gain:

- regional history and identity branches
- expanded formable discovery
- historical institution decisions
- new naming and cosmetic identity routes
- regional patron and rival events

### Post-report opening package

After the public report, the next wave can draw from Layers C and D. New countries receive stronger regional overlays and more distinctive leaders, institutions, units, and claims.

### New incidents

- old seals or charters become political symbols
- dynastic or traditional claimants return
- language and education disputes shape legitimacy
- competing local identities contest one proposed state
- foreign scholars, missionaries, exiles, or archaeologists influence public claims

### Failure and containment

A sensitive or uncertain package is skipped when required research or assets are not ready. The event uses another candidate rather than filling the slot with a generic invented identity.

## Evolution 3: Armed Birth

Earliest band: Chaos Tier

### Design meaning

New states no longer appear only as vulnerable republics. Some begin with defecting regiments, seized depots, frontier commands, militant movements, or foreign volunteers.

### Active-event evolution

Existing countries gain:

- stronger military professionalization routes
- emergency mutual-defense decisions
- border mobilization missions
- league reserve contributions
- aggressive reclamation branches for suitable routes

### Post-report opening package

Countries released after the public report can begin with:

- more experienced units
- captured support equipment, artillery, trains, or aircraft when the host package supports it
- a named military faction
- an immediate border mission
- a former-host ultimatum or ceasefire

### Dynamic strength factors

- host military weakness
- local population
- local depots and railways
- current war state
- chaos value
- regional military tradition
- sponsor involvement
- prior liberation success nearby

### Failure and containment

Armed countries start with higher instability, military political influence, and host hostility. Their early strength can produce a coup, faction split, or equipment crisis if civilian institutions remain weak.

## Evolution 4: Sovereign Congress

Earliest band: Totalen Chaos

### Design meaning

Released countries stop acting only as isolated survivors. They begin treating sudden independence as a shared international principle and prepare a common league.

### Active-event evolution

Existing countries gain:

- charter drafting
- league congress missions
- shared recognition campaigns
- member rescue decisions
- collective border arbitration
- joint reserve and aid systems
- leadership contests

### Post-report opening package

Countries released after the public report can start with:

- mutual recognition from existing Event 6 countries
- a delegate already assigned to the congress
- a league-oriented focus route
- shared defense expectations
- a choice between joining, observing, or rejecting the project

### New incidents

- charter rights dispute
- secretariat location vote
- common defense clause debate
- patron influence scandal
- expulsion threat
- rival regional caucus
- collective response to host reconquest

### Failure and containment

The congress can fail, split into regional leagues, become patron-controlled, or form a weak consultative body. Failure does not erase bilateral cooperation. It changes later league routes and super-event eligibility.

## Evolution 5: Open Sovereignty

Earliest band: World Collapse

### Design meaning

The principle of sudden state creation becomes a weapon. High-chaos governments use it to redraw regions, launch coordinated revisionism, revive unusual formables, and challenge the existing state system.

### Active-event evolution

Eligible existing countries gain, subject to their accepted package route matrix:

- radical government routes
- hidden regional formables
- coordinated reclamation doctrine
- bloc-wide intervention decisions
- state sponsorship of further independence movements
- high-risk transformation paths

### Post-report opening package

After the public report, the next wave can include the rarest candidate packages and begins with maximum package variety. Some countries start unusually strong, unstable, ideological, or ambitious.

### New incidents

- synchronized territorial demands
- rival leagues
- anti-host coalition war planning
- radical constitutional experiments
- external powers establish containment blocs
- one successful local formable inspires several others

### Failure and containment

The evolution can create wars among released states, league fracture, patron intervention, or aggressive blocs that alarm the world. It is powerful by design and should not become the ordinary route of every country.

## Evolution logging direction

Each evolution records:

- Event 6 as source event
- evolution type and stage
- chaos tier
- date
- actor when a specific released country first embodies the evolution
- enabled state

The evolution title direction should describe the public change in the independence system. It should not expose package IDs, hidden rarity weights, or implementation language.

## Country opening event family

Every country receives a tailored opening assembled from package data.

The event direction should mention:

- the government or movement that took control
- the capital or anchor territory
- the source of its first security forces
- the condition of the former host
- the most urgent public problem
- regional identity without turning the description into a history lecture

The player option should establish an early governing posture. The exact text may be serious, proud, anxious, traditional, revolutionary, military, religious, or darkly ironic depending on the package. Final wording belongs to implementation.

### Accepted country opening implementation map (2026-09-27)

Acceptance basis: the user authorized implementation of every accepted Part 2 requirement, including a tailored opening for each country in a committed Event 006 wave. This mapping completes the existing family requirement without adding a country, historical officeholder, tag, or alternate route.

The visible opening follows acknowledgement of the committed public report `chaosx.nr6.2`. Event `chaosx.nr6.41` presents the human posture choice and hidden event `chaosx.nr6.42` resolves it for AI countries. The queue is captured from the committed Event 006-owned country rows and dispatched by the single report option, once for each live Event 006 country. It never includes an Event 005 row, a Join conversion, a failed plan, or a rolled-back release. Per-generation identity checks prevent delayed content from reaching a later use of the same country tag. The report recipient holds a global pending receipt until its sole option dispatches; plan reset and a second report are held while that receipt is live. The actor router is scheduled one day after the report option so each opener follows the public acknowledgement.

Assemble the opening from the released country's retained data. Its text names the country and region, the government or movement that took power, the capital or anchor, the source of its first security forces, the former host and its current condition, and the most urgent public problem selected from the country's live statehood values and host pressure. Use the package's actual ruling party, anchor state, force profile, former-host pointer, host outcome, region, and five country values. Describe the force's recruitment origin separately from its brigade template, using the profile's local, industrial, inherited, frontier, coastal, mobile, riverine, or volunteer source. Missing required data fails closed rather than displaying a generic replacement.

The posture choice presents civilian administration and frontier security as distinct early priorities. Civilian administration raises legitimacy, recognition, and capacity, improves network standing, reduces founding instability, and accepts limited exposure in security. Gains ease for values already in established bands; war, severe host threat, and a fragile starting force increase the security tradeoff, while strained instability receives stronger relief. Where the former host survives, this posture moderates bilateral claims, hostility, obligations, domestic pressure, and reconquest fear while advancing border settlement.

Frontier security strengthens security according to the current Security band, starting force level, and force profile. It costs legitimacy, Capacity, and network standing; it increases Instability only during war or under a severe threat from a surviving former host. Against a living former host, it increases bilateral hostility and domestic pressure while reducing fear of reconquest. AI countries choose deterministically from active war, host threat, security strength, and the starting force profile, then receive the same posture effects as human countries. Both postures use the shared country, host, and network delta helpers and existing delta constants and grant no territory, claims, forces, paid receipts, or automatic government route. They update the public statehood values and host/network ledgers that later focuses, decisions, missions, and AI already read.

The existing IW-043 and IW-058 package introductions follow the shared posture choice by one day. Package setup does not interrupt the public report or country opening.

Use a single new shared report image for the country-opening family, registered within ASSET-048. It depicts a provisional local authority taking its first decisions alongside the source of its security forces, without a real leader, a national flag, generated writing, or invented heraldry. Register the stable sprite and 210×176 runtime DDS in the existing Event 006 report-image family before production.

## Post-event host response family

After the public Event 006 report, the host-response event should differ according to the share of territory lost.

### Accepted host response defaults (2026-09-27)

Acceptance basis: on 2026-09-27 the user accepted Event 006-only loss measurement, host aggregation, post-opening dispatch, and deterministic AI, then explicitly selected the recommended thresholds: limited below 50 percent, severe at 50 percent or more, and capital remnant if only the protected state remains or the original capital is lost while no more than two states remain.

Measure each former host's loss as the number of distinct states transferred by the committed Event 006 release divided by that host's pre-release state count. Exclude Event 005, Join conversions, and every other origin from the numerator. Aggregate all Event 006 losses to one response for each distinct former host in the wave.

Dispatch the host responses after the public report is acknowledged and the released countries have received their opening choices. A host qualifies for the capital-remnant response when only its protected state remains, or when the host no longer owns its original capital and has no more than two states remaining. This remnant condition overrides the loss-share tiers. Otherwise, classify a loss below 50 percent as limited secession and a loss of 50 percent or more as severe partition.

AI hosts select deterministically from the classified tier and their live host-relation ledgers. The three tiers retain the response content below; this accepted mapping defines classification, aggregation, and dispatch order. Current implementation evidence and limits are recorded in the Event 006 source map and dated host-response handoff.

### Limited secession

The host loses a peripheral area and can choose negotiation, pressure, or reconquest.

### Severe partition

The host loses several regions and must choose which claims to prioritize. It receives a temporary command, refugee, debt, and army-division crisis.

### Capital remnant

The host keeps only its protected state or a very small remnant. It receives a successor-state survival route, emergency government, outside guarantee opportunities, and a decision between legal continuity and acceptance of a new identity.

The host should remain playable and should not be punished with an unrecoverable empty state.

## Foreign reaction tiers

The [accepted foreign-reaction and remnant-petition contract](006_foreign_reactions_and_remnant_petitions_contract.md) records the user-selected score and the recommended caps, timing, actor reach, and generation-safe delivery accepted under the 2026-10-03 continuation instruction.
It is accepted design queued for implementation and does not establish runtime completion.

Foreign countries react through interest scores.

### Local neighbor

Interest comes from borders, claims, ideology, trade routes, minorities, and immediate security.

### Regional power

Interest comes from strategic access, patron competition, a threatened balance, and league leadership.

### Great power

Interest comes from bases, resources, containment, ideology, colonial precedent, and global recognition politics.

### Existing Independence Wave country

Interest comes from solidarity, rivalry, league goals, rescue obligations, and shared regional ambitions.

Only high-interest actors receive detailed targeted events. Others receive summary news or decisions when they choose to engage.

## Rare milestone events

Rare milestones are not evolutions unless they mutate the event system.

Examples:

- first released country receives broad recognition
- first peaceful treaty with a former host
- first Event 6 country annexed by its former host
- first regional formable completed
- first league congress convened
- first member rescued by collective action
- first cross-regional league formed
- first radical bloc adopts coordinated revisionism
- ten surviving Event 6 countries exist at once
- twenty-five surviving Event 6 countries exist at once
- a one-state country becomes a major power

These milestones feed achievements, event log details, super-event thresholds, AI strategy, and world reactions.
