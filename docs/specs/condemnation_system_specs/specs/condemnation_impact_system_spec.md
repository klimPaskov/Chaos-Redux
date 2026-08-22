# Condemnation Impact System Spec

## Purpose

Condemnation should become a practical diplomatic, economic, and military pressure system. A high condemnation score must change play. It should affect trade, resource access, foreign aid, volunteers, attachés, license production, research sharing, faction trust, and the way neutral countries treat the offender.

The player should understand the bargain clearly. A country can keep using chemical weapons, biological weapons, nuclear strikes, thermonuclear strikes, extermination infrastructure, restricted chemical sites, or discovered atrocity systems, then it must live with the cost. Trade partners leave. Arms supplies close. Fuel becomes harder to import. Neutrals hesitate. Allies may shield the offender only when it costs them something. Black markets and sanction busting become risky ways to keep a condemned war machine moving.

This is a system-level expansion of the Condemnation tab and the surrounding Chaos Meter mechanics. It should stand on its own as the shared consequence layer for unconventional warfare and exposed atrocities.

## Existing foundation

The current mechanics guide already defines condemnation as diplomatic blame for unconventional weapon use. It rises from chemical unit use, chemical and biological attacks, nuclear strikes, and selected decisions. The Condemnation tab already shows country values and updates when condemnation changes.

This spec keeps that foundation and expands it into source buckets, tiered sanctions, real embargo relationships where supported, participant logic, visible UI, AI behavior, compliance options, defiance options, evasion routes, cleanup, decay, and documentation.

## Design rules

1. Condemnation must create practical consequences beyond opinion modifiers.
2. High condemnation must create actual embargo relationships where the HOI4 engine supports them.
3. If embargo scripting is unsupported, incomplete, or behaves differently from the intended design, the implementation must report the blocker. Do not replace it with a cosmetic fallback.
4. Opinion modifiers are support effects. They cannot be the main punishment.
5. Sanctions must be tiered, dynamic, visible, and reversible only through meaningful behavior change or long decay.
6. Source buckets matter. Chemical battlefield use, biological strikes, nuclear devastation, thermonuclear escalation, camp discoveries, restricted chemical sites, and coverups should not feel identical.
7. AI countries must understand when to sanction, abstain, shield, comply, defy, or break sanctions.
8. The player must see the target country, total score, tier, source breakdown, active sanctions, participant count, next threshold, practical penalties, decay state, and available responses.
9. Thresholds, caps, gains, decay, participant scoring, AI weights, duration bands, and penalty scaling must live in script constants or one documented tuning file.
10. Do not add a broad all-country daily, weekly, or monthly on_action pass unless the user explicitly approves it. Use existing approved pulses, targeted refresh calls, weapon-use hooks, discovery hooks, diplomatic action hooks, or decision completion hooks.
11. Every sanction must have cleanup. Dead tags, annexed targets, ended subject relationships, expired flags, invalid embargo pairs, and obsolete modifiers must clear safely.
12. The design must remain readable. Sanctions should not become a debug menu filled with dozens of nearly identical actions.

## Player experience

The Condemnation tab becomes a management and threat screen. At low values it explains why a country is being watched. At middle values it shows who is preparing restrictions. At high values it shows which countries are actively cutting trade, arms, fuel, and military access.

So the condemned country entries should now be clickable and would show the details window. Don't change the ui of the tab. Only make the entries clickable.

For the condemned country, the system should create real choices:

- accept inspections and lower pressure
- destroy stockpiles and lose military options
- pay compensation and bear economic cost
- deny everything and gain internal political support at the cost of foreign pressure
- pursue autarky and suffer transition costs
- rely on black market procurement and risk exposure
- pressure subjects and allies into shielding trade
- keep escalating and accept isolation

For sanction participants, the system should also create choices:

- enforce restrictions despite trade cost
- abstain because the target is useful or too important to trade with
- allow humanitarian carve-outs
- break sanctions quietly for profit
- shield an ally from harsher isolation
- tighten enforcement after exposure or repeated violations

## Data model

### Country values

Each country should track a public total, source buckets, tier memory, decay, and current sanctions state.

| Value | Role |
| --- | --- |
| `condemnation_total` | Public total shown in the Condemnation tab. |
| `condemnation_tier` | Current visible tier. Recalculated from the total and current modifiers. |
| `condemnation_peak_tier` | Highest tier reached. Used for long memory and harsher AI skepticism. |
| `condemnation_chemical` | Chemical support use, chemical abilities, chemical raids, chemical aircraft, contamination, and chemical doomsday release. |
| `condemnation_biological` | Bioweapon strikes, outbreak weapons, deliberate spread, bio-linked experiments, and stockpile release. |
| `condemnation_nuclear` | Nuclear and thermonuclear use, weighted by target population, strike type, fallout, and repetition. |
| `condemnation_atrocity` | Exposed camps, extermination infrastructure, gulags, restricted chemical sites, and discovered mass death systems. |
| `condemnation_coverup` | Evidence destruction, falsified records, hidden sites, blocked inspection, and discovered concealment. |
| `condemnation_repeat_use` | Recent repetition pressure from repeated condemned actions. |
| `condemnation_recent_gain` | Recent spike used for UI highlight and short-term AI reaction. |
| `condemnation_decay_credit` | Recovery progress from non-use, inspections, stockpile destruction, compensation, and settlement. |
| `condemnation_sanction_pressure` | International willingness to punish this target. |
| `condemnation_evasion_pressure` | Current target investment into bypassing restrictions. |
| `condemnation_active_sanctions` | Count or severity value for current active sanction pairs. |
| `condemnation_black_market_exposure` | Risk that evasion becomes public and creates more condemnation. |
| `condemnation_compliance_state` | Current compliance path, such as inspection, stockpile destruction, compensation, or verified non-use. |

### Pair values and flags

Sanctions need pair-level memory because the punishment depends on who sanctions whom.

| Value or flag | Role |
| --- | --- |
| `sanctions_pair_active` | Participant currently applies sanctions against the target. |
| `sanctions_pair_tier` | Highest sanction tier this participant applies to this target. |
| `sanctions_pair_started_date` | Start date for duration, decay, and UI. |
| `sanctions_pair_trade_dependency` | How costly sanctions are for the participant. |
| `sanctions_pair_moral_pressure` | Pressure from ideology, deaths, atrocity source, world tension, and diplomatic position. |
| `sanctions_pair_enforcement_cost` | Cost paid by the participant to maintain enforcement. |
| `sanctions_pair_humanitarian_carveout` | Participant allows limited relief exceptions. |
| `sanctions_pair_quiet_breach` | Participant is violating its own sanctions. |
| `sanctions_pair_evasion_detected` | Breach was detected and can trigger penalties. |
| `sanctions_pair_faction_shield` | Participant or faction leader shields the target from stronger sanctions. |

### Derived values

The system should calculate useful derived values for UI and AI:

- active arms embargo participant count
- active strategic embargo participant count
- active total embargo participant count
- weighted isolation severity
- weighted participant industry share
- weighted participant trade share
- target import vulnerability
- target fuel vulnerability
- target military import vulnerability
- target faction shield strength
- target black market route strength
- compliance credibility
- sanction fatigue among participants

Derived values should be recalculated through helper effects when condemnation changes, sanctions change, diplomatic state changes, or cleanup runs.

## Source buckets and gain logic

Condemnation gain should use one shared helper with source parameters. The helper should update the source bucket, total score, recent gain, repeat-use pressure, tier state, UI refresh data, and participant pressure. It should not scatter separate magic values across chemical, biological, nuclear, camp, and decision files.

Suggested helper shape:

| Input | Purpose |
| --- | --- |
| source type | Chemical, biological, nuclear, atrocity, coverup, or mixed. |
| base gain | Starting value before scaling. |
| target state | Optional state used for population, infrastructure, victory point, capital, and contamination scaling. |
| victim country | Optional country used for war, core, occupation, and diplomacy scaling. |
| visibility | Whether the action is public, suspected, discovered, or hidden. |
| severity | Combat use, city strike, repeated use, mass death, doomsday release, site discovery, or coverup. |
| civilian death value | Deaths tied to the action where available. |
| contamination value | Air cleanliness or state contamination contribution where available. |
| repeat window | Recent repeated use multiplier. |

### Chemical source

Chemical condemnation should rise from real use, not stockpile ownership. It should track battlefield and strike behavior.

Sources:

- chemical support companies fighting
- chemical general abilities
- chemical shelling or projector use
- chemical air bombs
- chemical raids
- large contaminated state areas
- persistent contamination affecting civilians
- chemical doomsday release

Scaling factors:

- number of active chemical combats
- affected state population
- civilian exposure risk
- weather and persistence severity
- repeated use during recent months
- use in foreign territory
- use in occupied territory
- use against non-core populations
- doctrine branches that reduce public visibility or discipline use
- contamination contribution

Doctrine mitigation can reduce gain. It must never erase consequences completely when heavy use is visible.

### Biological source

Biological condemnation should rise from deliberate strikes, outbreaks caused by weapons, deliberate spread, and discovered experiments.

Sources:

- biological attack decision or strike
- outbreak weapon release
- deliberate spread decision
- stockpile leak that becomes public
- bio-linked experiment discovery
- bioweapon doomsday release

Scaling factors:

- outbreak intensity
- spread beyond original target
- affected population density
- civilian deaths
- containment failure
- public visibility
- repeated biological use
- target country status and war context
- whether the user takes visible containment measures

Containment efforts should reduce future growth and improve decay. They should not erase the initial gain.

### Nuclear source

Nuclear condemnation should be heavier than ordinary chemical use. Thermonuclear use should create a severe spike.

Sources:

- normal nuclear strike
- thermonuclear strike
- strike on capital or major population center
- strike on heavily industrial state
- fallout deaths
- repeated nuclear use

Scaling factors:

- target state population
- victory point value
- capital status
- civilian death estimate
- fallout contribution
- contamination contribution
- first use in campaign
- repeated use by same country
- whether target was at war with the user
- whether target was a subject, neutral, ally, or non-belligerent
- chaos tier

### Atrocity source

Atrocity condemnation should be evidence-aware. Secret domestic repression should remain internal until exposed, discovered, leaked, observed, or uncovered through occupation or liberation.

Sources:

- camp discovery
- extermination site discovery
- gulag system exposure
- restricted chemical site discovery
- prisoner experimentation exposure
- liberated mass death infrastructure
- foreign observer reports
- captured records

Scaling factors:

- number of discovered sites
- type of site
- deaths tied to the site
- evidence quality
- state ownership and occupation context
- foreign observer access
- relation between victim and discovering country
- coverup attempts found later
- link to biological or chemical systems

### Coverup source

Coverups should become their own bucket because a country that hides evidence should face a different diplomatic reaction from a country that allows inspection.

Sources:

- destroyed records discovered later
- blocked inspection
- falsified inspection result discovered
- destroyed site found through occupation
- killed witnesses or removed prisoners where exposed
- sanctioned ship or convoy using false papers
- black market route discovered

Scaling factors:

- severity of original act
- evidence quality
- number of affected states or sites
- repeated coverup behavior
- whether the target had promised compliance
- whether the exposure involves a sanction participant

## Condemnation tiers

Threshold values are design anchors. Put final values in constants and tune after testing.

| Tier | Working label | Threshold | Main gameplay result |
| --- | --- | --- | --- |
| 0 | Normal standing | 0 to 24 | No sanctions. The tab records recent sources. |
| 1 | International concern | 25+ | Mild diplomatic penalties, visible monitoring, first sanction participant scoring. |
| 2 | Formal censure | 50+ | Stronger diplomatic penalties, inspection demands, reduced support access, compliance options become important. |
| 3 | Arms embargo | 100+ | Arms embargo pairs begin where supported. Lend-lease, volunteers, attachés, and license production are blocked or sharply reduced by participants. |
| 4 | Strategic embargo | 175+ | Fuel, rubber, chromium, tungsten, military imports, foreign procurement, and market access become restricted. Target receives dynamic shortage pressure. |
| 5 | Total embargo | 300+ | Broad isolation. Trade, research sharing, faction trust, recognition, guarantees, and foreign investment suffer across many participants. |
| 6 | Pariah state | 500+ | Severe diplomatic isolation. Containment pressure, intelligence pressure, resistance support, faction expulsion pressure, and war-preparation pressure become possible where campaign logic supports them. |

Tiers should unlock mechanics. They should not be static modifier labels.

## Tier consequences

### Tier 1: International concern

Purpose: the world begins tracking the offender.

Effects:

- small opinion penalties from likely participants
- small acceptance penalty for military access, non-aggression pacts, lend-lease, attachés, and volunteers
- UI shows next tier and likely reaction sources
- compliance actions become visible if the target wants to reduce future pressure
- AI starts monitoring the target in participant scoring

No embargo applies at this tier.

### Tier 2: Formal censure

Purpose: condemnation becomes a diplomatic problem with early costs.

Effects:

- stronger opinion penalties from high-pressure countries
- foreign military support becomes harder to receive
- attaché acceptance drops
- volunteer acceptance drops
- military access becomes harder to obtain
- lend-lease becomes much less likely from countries with high participant score
- inspection, non-use pledge, compensation, and observer access actions unlock or become more important
- sanction participants can begin preparing arms embargo logic

Censure should matter. It should remain recoverable with early compliance.

### Tier 3: Arms embargo

Purpose: practical military restrictions begin.

Effects:

- participating countries apply actual embargo relationships where the engine supports them
- military lend-lease from participants is blocked through AI and scripted checks
- license production with participants becomes blocked or expensive
- volunteers and attachés from participants become blocked or sharply reduced
- foreign military procurement becomes unavailable through participants
- target receives a visible arms import bottleneck if enough important suppliers participate
- sanction participants appear in the Condemnation tab

Counterplay:

- target can destroy stockpiles, accept inspections, pledge non-use, pay compensation, or attempt covert procurement
- participants can quietly break restrictions, then risk exposure

### Tier 4: Strategic embargo

Purpose: sanctions change production and resource strategy.

Effects:

- active embargo pairs expand among eligible participants
- target receives a dynamic strategic shortage modifier based on participant weight and import vulnerability
- fuel access becomes harder when key fuel suppliers or convoy routes are restricted
- rubber, chromium, tungsten, and other war-critical imports become harder to secure
- foreign procurement actions become blocked or costly
- neutral traders receive stronger pressure to choose a side
- AI trade behavior shifts away from the target when possible
- target can open autarky, forced extraction, subject pressure, and black market routes

Strategic embargo should not use one flat penalty. It should scale by participant count, participant industry, target import reliance, target domestic resources, faction shielding, and black market strength.

### Tier 5: Total embargo

Purpose: isolation affects the whole state and reaches beyond arms access.

Effects:

- broad participant bloc applies trade and diplomatic restrictions
- research sharing and technology group access are damaged
- guarantees and recognition become harder
- foreign investment and aid decisions become blocked or costly
- faction trust drops unless most faction members share or tolerate the same condemnation level
- target economy receives strong dynamic penalties from isolation severity
- black market procurement becomes stronger, riskier, and more expensive
- subject and puppet trade pressure becomes more important
- sanction fatigue appears for participants that pay a high cost for long periods

Total embargo should have visible abstainers, profiteers, and shields. Countries should not all act the same.

### Tier 6: Pariah state

Purpose: extreme condemnation changes the campaign around the target.

Effects:

- faction leaders can pressure the target to comply or leave when the faction would otherwise suffer
- rivals gain stronger intelligence, sabotage, and resistance support options against the target
- justification pressure can become easier only when world tension, ideology, distance, strength, and balance make sense
- neutral countries become more willing to sanction unless trade dependency is severe
- subjects are pressured to follow overlord stance unless autonomy or direct harm changes their behavior
- target propaganda and militarization routes become stronger but costly
- long-term memory remains after score decay

Pariah pressure should be powerful. It should still respect campaign logic and avoid free war spam.

## Embargo implementation contract

The implementation must verify how embargoes work in the installed HOI4 version before scripting final behavior.

Required behavior:

- identify the engine-supported diplomatic embargo mechanism
- prove the exact effect through vanilla documentation, vanilla files, or local syntax references
- apply embargoes as pair-level relations between participant and target where supported
- clear embargoes safely when sanctions expire or scopes become invalid
- keep scripted restrictions aligned with actual embargo pairs
- report any unsupported field, missing effect, missing trigger, or engine limitation

Supported embargo behavior should be used for trade denial. Scripted modifiers can add arms access, market access, license production, research sharing, faction trust, and shortage effects. Scripted modifiers must not pretend to be actual embargoes when the engine supports real ones.

If the engine only supports part of the desired embargo behavior, use the real part and document the remaining restrictions as scripted sanctions. The final report must name the exact supported and unsupported pieces.

## Sanction participant scoring

Every potential participant should receive a dynamic score against the target. The score determines whether it sanctions, abstains, shields, quietly breaks restrictions, or demands compliance.

### Positive pressure

Pressure to sanction increases from:

- target condemnation tier
- recent condemnation spike
- nuclear or thermonuclear source
- biological source with spread
- exposed atrocity source
- coverup after inspection promise
- direct victim status
- rivalry with target
- ideological hostility
- nearby threat
- high world tension
- public moral pressure from deaths or contamination
- faction leader pressure
- guarantee or interest in the victim country

### Negative pressure

Pressure to sanction decreases from:

- same faction with target
- subject or overlord relationship with target
- high trade dependency on target
- reliance on target fuel or strategic resources
- shared ideology or common enemy
- current war where target is useful
- weak participant economy
- participant's own high condemnation
- sanctions already causing high domestic cost
- distance and low strategic interest

### Participant result bands

| Score result | Behavior |
| --- | --- |
| Very low | No sanction and no visible pressure. |
| Low | Abstain, watch, or send weak diplomatic pressure. |
| Medium | Join censure or arms embargo. |
| High | Join strategic or total embargo when tier allows. |
| Very high | Lead enforcement, expose violators, and pressure allies. |
| Negative with profit motive | Quietly break sanctions if target can pay or provide resources. |
| Shielding case | Block harsher isolation for ally, subject, or vital partner while paying a diplomatic cost. |

## Target economic effects

Sanctions should create practical economic pressure through scaling modifiers and access blocks.

### Arms import bottleneck

Triggered mainly by Tier 3 and above.

Possible effects:

- reduced lend-lease acceptance from participants
- blocked or costly military procurement decisions
- license production limits with participants
- increased cost for foreign military aid decisions
- production efficiency strain if the country relied on foreign designs or imported parts
- higher black market equipment cost

### Strategic shortage

Triggered mainly by Tier 4 and above.

Possible effects:

- fuel gain or fuel storage pressure when fuel suppliers participate
- military factory output pressure from resource shortages
- dockyard or convoy pressure when sea routes are restricted
- consumer goods burden from forced substitution
- slower construction for resource projects if sanctions block imports
- route-specific relief if the target controls enough domestic resources

### Isolation economy

Triggered mainly by Tier 5 and above.

Possible effects:

- consumer goods burden
- factory output pressure
- research speed pressure when research sharing collapses
- diplomatic acceptance penalties
- market access denial where applicable
- foreign investment decision blocks
- higher resistance or occupation pressure when local populations react to atrocities

Penalties must scale from isolation severity. Do not apply the same harsh modifier to a minor with two sanction participants and a major facing most of the world.

## Participant costs

Sanctions must have costs for participants. A country should not cut a major trade partner for free.

Possible participant costs:

- temporary consumer goods burden
- lost trade access
- resource shortage risk
- relations damage with target and target faction
- convoy or fuel cost for enforcement
- stability loss if domestic economy suffers
- war support gain when public pressure is high
- legitimacy or diplomatic trust gain with countries that support sanctions
- sanction fatigue after long enforcement

Participant costs should scale with trade dependency, current war state, convoy exposure, distance, and target strength.

## Target counterplay

### Compliance actions

Compliance should reduce future pressure and create decay credit. It should cost something concrete.

Actions:

| Action | Cost direction | Result direction |
| --- | --- | --- |
| Accept inspections | Civilian factory burden, intelligence exposure, temporary compliance timer | Improves decay and lowers coverup suspicion. |
| Destroy chemical stockpiles | Removes or reduces chemical stockpile, equipment, or production access | Reduces chemical pressure and unlocks verified non-use memory. |
| Destroy biological stockpiles | Removes bio stockpile or locks use for a duration | Reduces biological pressure and improves participant willingness to de-escalate. |
| Dismantle restricted sites | Civilian factory burden, loss of site output, possible stability hit | Reduces atrocity and coverup pressure if verified. |
| Pay compensation | Civilian factories, convoys, fuel, equipment, or stability cost | Improves victim relations and adds decay credit. |
| Non-use pledge | Locks or penalizes weapon use for a duration | Lowers future participant pressure. Breaking it adds coverup or repeat-use pressure. |
| Allow observers | Intelligence exposure and political cost | Improves compliance credibility. |
| Remove responsible command | Leader, advisor, commander, or national spirit change where supported | Reduces long-term memory more than ordinary compliance. |

Compliance must never be a cheap button that erases severe condemnation. It should lower pressure gradually.

### Defiance actions

Defiance should help the target survive sanctions while raising risk.

Actions:

- domestic propaganda campaign
- emergency autarky program
- forced resource extraction
- substitute materials program
- military rationing
- subject trade pressure
- controlled shipping program
- hardline internal mobilization
- refusal of inspections

Costs and risks:

- stability pressure
- war support shift
- consumer goods burden
- civilian factory burden
- fuel cost
- resistance pressure
- further condemnation on exposure
- harsher participant scoring

### Evasion actions

Evasion should keep the target alive through illegal or gray-market routes. It must risk exposure.

Actions:

- black market arms procurement
- false-manifest convoy routes
- neutral intermediary contracts
- subject-front import network
- covert fuel shipments
- ship reflagging network
- stolen license production
- smuggled laboratory equipment

Costs:

- convoys
- fuel
- civilian factory burden
- command power only for limited security actions
- intelligence exposure
- relations damage if exposed
- additional coverup condemnation if exposed after a pledge

Evasion should be attractive for a sanctioned player. It should not be safe.

## Participant actions

Participant countries should also have actions and AI decisions.

| Action | Use case | Cost or risk |
| --- | --- | --- |
| Join arms embargo | Target reaches Tier 3 and participant score is high enough | Lost arms trade, relations loss, possible enforcement burden. |
| Join strategic embargo | Target reaches Tier 4 and participant can bear trade cost | Resource shortage risk and consumer goods burden. |
| Join total embargo | Target reaches Tier 5 and broad pressure exists | Larger economic cost and faction tension. |
| Abstain | Trade dependency, ally shield, weak economy, or strategic need | Opinion cost with sanction leaders or victims. |
| Humanitarian carve-out | Relief supplies, medicine, or civilian exceptions | Reduced pressure but less economic damage to target. |
| Quiet breach | Profit motive or resource need | Exposure risk, condemnation gain, relations loss with sanction leaders. |
| Tighten enforcement | Target evasion is exposed | Enforcement cost, lower target evasion strength. |
| Shield ally | Same faction or vital partner | Diplomatic cost and participant hypocrisy pressure. |

## Decay, compliance, and memory

Condemnation should decay slowly and visibly. Recovery should require time, non-use, and credible action.

Decay increases when:

- target has not used condemned methods recently
- inspections remain clean
- stockpiles are destroyed
- restricted sites are dismantled
- compensation is paid
- observers are allowed
- leadership or command responsibility changes
- war ends with settlement terms tied to compliance

Decay slows or stops when:

- target uses condemned methods again
- target refuses inspection
- target hides evidence
- target breaks a non-use pledge
- target is caught using black market routes
- target controls exposed atrocity sites
- target follows a doctrine that normalizes condemned methods

Memory rules:

- peak tier should remain visible in detailed tooltip
- countries that reached Tier 5 or Tier 6 should retain diplomatic skepticism after total score falls
- repeat offenders should climb faster because past use changes participant expectations
- a verified government change can reduce memory, but should not remove it instantly

## UI and player presentation

The Condemnation tab should become the main interface for the system.

### Country list

The sortable country list should show:

- country name and flag
- total condemnation
- current tier
- recent gain
- main source bucket
- active sanction count
- active highest sanction tier
- decay or compliance indicator

### Detail panel

Selecting a country should show:

- total score
- tier name
- next threshold
- peak tier
- source bucket breakdown
- recent source changes
- active sanctions by type
- participant count by type
- likely next participants
- current practical penalties
- compliance state
- decay state
- evasion exposure risk if visible to the player

### Tooltips

Tooltips should explain:

- why the current tier applies
- which source buckets drove the score
- what practical effects are active
- what can lower pressure
- why a decision is blocked
- which participant types are most important
- how long current temporary effects last

Use scripted localisation for dynamic values. Avoid raw trigger spam and long unreadable requirement lists.

### Visual hierarchy

Suggested color identity:

- chemical source in a yellow or sickly green family
- biological source in a green family
- nuclear source in a bright red or orange family
- atrocity source in a dark red or black-red family
- coverup source in gray or purple-gray family
- compliance in blue or green
- evasion in amber

Final colors should match the existing Chaos Redux UI palette.

### Decision category presentation

If sanctions require a decision category, it should remain curated:

- show target responses only to condemned countries
- show participant actions only when a country has a reason to act
- hide obsolete actions after tier changes, peace, annexation, compliance, or expiry
- group actions into compliance, defiance, evasion, enforcement, and carve-outs
- cap active missions where timed compliance or enforcement is used

## Localisation direction

Final player-facing text should be concrete and system-aware. It should explain visible effects and costs without sounding like a raw script dump.

Condemned target text should focus on:

- ports refusing military cargo
- fuel contracts failing
- foreign officers leaving
- factories losing imported parts
- neutral brokers raising prices
- inspectors demanding access
- leaders arguing over compliance or defiance

Participant text should focus on:

- cost of cutting trade
- public pressure after casualties or site discovery
- fear of empowering a rival
- reliance on target resources
- faction discipline
- profit from quiet breach

Do not write final localisation inside this spec. The implementation owns final wording after values and effects are wired.

## AI behavior

AI behavior must use the same visible logic as the player-facing system.

| Actor | Behavior |
| --- | --- |
| Condemned weak target | Seeks compliance, inspections, compensation, and stockpile destruction when sanctions hurt. |
| Condemned strong target | Uses defiance, autarky, subject pressure, and black market routes when it can absorb the cost. |
| Democratic major | Strong sanction preference after civilian deaths, nuclear use, biological spread, or exposed atrocity systems. |
| Fascist major | Sanctions rivals readily, shields aligned offenders, and uses sanctions as strategic pressure. |
| Communist major | Sanctions ideological rivals and weighs resource access, faction discipline, and strategic threat heavily. |
| Neutral trader | Abstains when trade dependency is high. Breaks sanctions for profit if exposure risk is low. |
| Faction leader | Coordinates sanctions, shields members, pressures members to comply, or pushes expulsion only at high tiers. |
| Puppet or subject | Usually follows overlord stance unless autonomy is high or the target directly harmed it. |
| High-condemnation country | Shows hypocrisy penalties and weaker moral pressure unless rivalry, fear, or direct harm overrides it. |

AI must evaluate:

- target tier
- source bucket severity
- recent gain
- deaths and contamination
- ideology
- faction relationship
- subject relationship
- trade dependency
- strategic resource dependency
- current war state
- target strength
- distance
- world tension
- own condemnation
- sanction fatigue
- compliance credibility
- evasion exposure

## Integration with existing Chaos Redux systems

### Chaos Meter

Condemnation should stay connected to the Chaos Meter without double counting source damage. If chemical, biological, nuclear, contamination, death, or atrocity systems already add chaos, condemnation should not add a second large chaos spike for the same act. Sanctions can still affect chaos indirectly through world tension, wars, faction ruptures, resource crises, and instability.

### Air cleanliness

The source breakdown should show when contamination helped drive condemnation. High contamination from chemical, biological, nuclear, or thermonuclear use should increase participant pressure.

### Deaths tracker

Civilian death totals should scale condemnation for chemical, biological, nuclear, thermonuclear, and exposed atrocity sources. The Condemnation tab should make the connection readable.

### Chemical warfare

Chemical systems should call the source-aware helper only when weapons are used or contamination becomes public. Ownership, research, or stockpiling should not create condemnation by itself.

### Biological warfare

Biological systems should call the helper after strikes, deliberate spread, public outbreak links, accident exposure, and doomsday release.

### Camps and genocide mechanics

Discovery, leaks, occupation, liberation, observers, and exposed records should feed atrocity and coverup buckets. Hidden domestic mechanics should remain separate until visible evidence exists.

### Chaos Warfare

Doctrine paths can change gain rates, compliance credibility, evasion options, or defiance strength. They should not remove consequences from heavy visible use.

## Asset and icon needs

This system can mostly reuse existing UI. Add assets only where they make decisions clearer.

Suggested system-owned icons:

- international sanctions category icon
- arms embargo decision icon
- strategic embargo decision icon
- inspection mission icon
- stockpile destruction decision icon
- compensation settlement decision icon
- black market procurement decision icon
- sanction breach exposure icon
- pariah economy idea or dynamic modifier icon

Use shared system folders for final assets because this is not tied to a specific random entry. Use exact repo asset placement rules after inspecting existing structure.

Animation is optional. If a scripted GUI sanctions panel is created, a subtle state-driven seal for high tiers can be considered. Any animated sprite must follow frame-animation rules and include real source frames, a static fallback, a frame sheet, a GIF preview, and a handoff.

## Documentation requirements

Update documentation after implementation:

- `CHAOS_REDUX_MECHANICS.md` condemnation section
- dedicated system doc, suggested path `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md`
- chemical warfare docs where condemnation gain and mitigation are described
- biological warfare docs where bioweapon condemnation is described
- camps and genocide docs where discovery-driven condemnation is described
- Chaos Warfare docs where doctrine changes condemnation behavior
- UI documentation for the Condemnation tab if a doc exists
- asset manifests for new icons
- validation or completion notes describing supported and unsupported embargo behavior

Do not guess player-facing records that mirror in-game localisation. Update such records only after final localisation exists.

## Implementation surfaces

The implementation agent should inspect the repo before choosing exact paths. Likely surfaces:

- `common/script_constants/` for thresholds, AI weights, participant scoring, decay, duration bands, and scaling values
- `common/scripted_effects/` for adding source-aware condemnation, recalculating tiers, scoring participants, applying sanctions, clearing sanctions, handling compliance, handling evasion, and cleanup
- `common/scripted_triggers/` for tier checks, participant eligibility, target eligibility, compliance eligibility, evasion eligibility, and pair validity
- `common/ideas/` or dynamic modifier surfaces for import bottlenecks, strategic shortage, isolation economy, enforcement burden, sanction fatigue, and pariah economy
- `common/decisions/` for target compliance, defiance, evasion, and participant enforcement actions
- AI strategy or `ai_will_do` blocks for target and participant behavior
- opinion modifiers as support effects only
- scripted localisation for breakdowns, thresholds, participant counts, practical penalties, decision costs, and blocked requirements
- Chaos Meter UI or scripted GUI files for the Condemnation tab expansion
- GFX files for any new icons or scripted GUI sprites
- documentation files listed above

## Cleanup rules

Cleanup must handle:

- target no longer exists
- participant no longer exists
- target and participant become the same country through annexation or tag switch
- target becomes a subject of participant
- participant becomes a subject of target
- target joins participant faction
- participant joins target faction
- sanction duration expires
- target tier falls below active sanction threshold
- compliance settlement ends sanctions early
- quiet breach is exposed or expires
- humanitarian carve-out expires
- active modifier outlives its source pair
- UI arrays contain stale participants

Cleanup should use helper effects and pair validity triggers. Avoid repeated cleanup copies across many files.

## Balance guidance

The system should hurt without making every condemned country unplayable.

Balance principles:

- Tier 1 and Tier 2 create pressure and warning signs.
- Tier 3 restricts military support.
- Tier 4 changes resource and import strategy.
- Tier 5 forces a serious economy and diplomacy response.
- Tier 6 makes the target diplomatically dangerous to support.
- A self-sufficient major should suffer less from trade denial, but more from diplomatic and faction pressure.
- A resource-dependent minor should fear strategic embargoes, but should have compliance paths.
- A target with strong faction shielding should survive longer, while the shield pays a cost.
- Sanction participants should hesitate when the target is their main resource supplier.
- Black market routes should help, then become risky if overused.
- Compliance should be slower than damage, because trust takes time to rebuild.

## Validation scenarios

The system is not complete until these scenarios are checked or explicitly blocked.

1. A country uses chemical support in several combats, then stops.
2. A country launches one nuclear strike on a low-population military target.
3. A country launches a thermonuclear strike on a populous capital.
4. A biological strike creates a spreading outbreak.
5. A restricted chemical site is discovered after occupation.
6. A camp system is exposed through discovery or liberation.
7. A country reaches Tier 3 and receives arms embargo pairs from eligible participants.
8. A country reaches Tier 4 and receives a strategic shortage that scales by participant weight.
9. A country reaches Tier 5 with strong faction shielding.
10. A country reaches Tier 5 with no shielding and high trade dependency.
11. A neutral trader abstains because dependency is high.
12. A neutral trader breaks sanctions and is exposed.
13. A condemned country accepts inspections and destroys stockpiles.
14. A condemned country breaks a non-use pledge.
15. A condemned country uses black market procurement repeatedly.
16. A participant stops sanctions after tier decay and cleanup.
17. An annexed or dead target leaves no stale sanction pairs.
18. AI targets choose compliance when weak and defiance when strong.
19. UI shows source breakdown, tier, active sanctions, participant count, and next threshold.
20. Tooltips show dynamic costs and blocked requirements without raw trigger spam.

## Acceptance criteria

The implementation is complete only when all of these are true:

1. High condemnation creates practical sanctions beyond opinion modifiers.
2. Actual embargo relationships are applied where HOI4 supports them.
3. Unsupported embargo behavior is reported clearly with evidence.
4. Arms embargo, strategic embargo, total embargo, and pariah tiers change gameplay in visibly different ways.
5. Chemical, biological, nuclear, thermonuclear, atrocity, restricted site, and coverup sources feed distinct source buckets.
6. The Condemnation tab shows total, tier, source breakdown, active sanctions, participant count, next threshold, decay, and practical penalties.
7. Target countries have compliance, defiance, and evasion choices with concrete costs.
8. Participant countries have enforcement, abstention, carve-out, breach, and shielding logic with real costs or risks.
9. AI can sanction, abstain, shield, comply, defy, or break sanctions for grounded reasons.
10. Sanctions clear safely when scopes, tiers, durations, wars, subject relationships, or diplomatic relationships change.
11. Decay and compliance can lower pressure, while high-tier memory remains.
12. Localisation explains requirements and effects through dynamic text.
13. New icons or UI assets, if added, are final assets and not placeholders.
14. Documentation matches final behavior.
15. No fallback, placeholder, or cosmetic-only substitute is used without explicit user approval.

## Completion report requirements

The implementation report must list:

- files changed
- script constants and tuning values added
- source buckets implemented
- tier thresholds implemented
- sanction tiers implemented
- exact embargo mechanism used
- unsupported embargo pieces if any
- participant scoring behavior
- target compliance, defiance, and evasion behavior
- participant enforcement, abstention, breach, carve-out, and shielding behavior
- AI behavior implemented
- UI and localisation surfaces changed
- icon or asset status
- cleanup helpers and triggers added
- documentation status
- validation scenarios run
- simplifications, blockers, and incomplete pieces

If any acceptance item is incomplete, the goal remains incomplete.
