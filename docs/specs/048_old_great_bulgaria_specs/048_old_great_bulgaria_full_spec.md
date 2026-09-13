# Event 048: Old Great Bulgaria, full specification

# Part 1: Core design

## Event identity

Event 048 turns Bulgaria into an immediate regional aggressor with enough concrete military and economic capacity to act before its new focus tree has had time to mature. The opening is deliberately front-loaded. The country receives the means to fight, while the tree determines how that strength is spent and whether it becomes durable.

The event remains Minor Fire-Once. It can reshape southeastern Europe, but its initial firing does not automatically create a global crisis.

## Immediate surge

The opening package has five material layers.

### Army readiness

Bulgaria receives large stockpiles of infantry equipment, artillery, support equipment, trucks, trains, and a bounded armored package appropriate to the installed technology state. Several fully equipped divisions appear from prepared templates. The package must be strong enough to make immediate Balkan action credible without creating a permanent free-unit loop.

### Manpower and mobilization

Reserve manpower rises sharply. Mobilization friction falls for a limited opening period. The country can sustain rapid reinforcement during its first campaigns, but a prolonged multi-front war still creates a real manpower and equipment problem.

### Industry and logistics

Important Bulgarian states gain factories, infrastructure, rail improvements, airbase capacity, supply expansion, and selected building slots. The opening should visibly alter the map and production screen. A later industry branch turns part of this emergency growth into permanent capacity.

### Political authority

The revival grants enough political leverage to act quickly on claims, government organization, mobilization, and diplomatic pressure. The opening avoids a large stack of disposable national spirits. One event-owned surge idea can carry the time-limited national window while concrete grants deliver most of the power.

### Historic claims

Bulgaria immediately receives claims on the baseline Greater Bulgaria target set. The set centers on the Bulgarian national question around Macedonia, Southern Dobruja, Western Thrace, and selected Serbian border regions. Exact states are bound during map research. Claims are immediate. Cores require integration or an earned formation milestone.

## Public mechanic values

### National Momentum

National Momentum represents the political and military force created by the revival. It rises through victories, successful ultimatums, rapid objectives, mobilization, and visible regional submission. It falls through failed demands, stalled wars, lost Bulgarian core territory, equipment crisis, and repeated diplomatic humiliation.

Momentum controls how aggressively Bulgaria can pressure targets and how much of the opening surge can be converted into lasting institutions.

### Imperial Administration

Imperial Administration represents Bulgaria's ability to govern and integrate expansion. It rises through reconstruction, compliance, administrative missions, transport restoration, local collaboration, negotiated integration, and political consolidation. It falls when Bulgaria expands faster than it can administer, suffers high resistance, loses integrated regions, or chooses especially extractive policies.

Administration governs integration speed, core eligibility, protectorate policy, and the safety of late imperial expansion.

## Design limits

The player should never need to memorize more than these two event-specific persistent values. Target readiness, resistance pressure, diplomatic response, war exhaustion, and state eligibility can be calculated internally and shown through qualitative tooltips or mission status.

The event does not need a bespoke full-screen GUI. Normal focus, decision, map, and formable-state-puzzle surfaces carry the gameplay.

# Part 2: Event flow and evolutions

## Opening sequence

The event fires on the current valid Bulgarian country. If Bulgaria does not exist as an ordinary country, implementation must use the project's country-specific target gate and fail closed rather than inventing a substitute host.

The first popup establishes the revival, then the material surge is applied in one bounded transaction. The replacement or event-owned focus tree becomes available immediately. The first meaningful territorial actions should become reachable after only a few short focuses.

## Baseline progression

Baseline progression has four practical phases.

1. **Awakening** gives the surge, organizes claims, and opens the first pressure actions.
2. **Greater Bulgaria campaign** lets Bulgaria pursue its central Balkan claim groups through demands, border pressure, intervention, or war according to the current owner and diplomatic situation.
3. **Integration** converts controlled claim territory into governable territory through missions, compliance, logistics, stability, and administrative investment.
4. **Greater Bulgaria proclamation** becomes available after the central territorial and administrative proof is complete.

Greater Bulgaria is a full baseline payoff. A campaign without higher evolutions must still have a complete political, military, industrial, diplomatic, and post-formation game.

## Evolution I: The San Stefano Dream

Requirement: 200+ Chaos.

When Event 048 has not fired yet, Evolution I strengthens the initial surge, broadens the immediately visible claim agenda, grants more prepared divisions and material, and shortens the route to the first territorial pressure tools.

When the event is already active, the evolution enters through normal evolution pacing and unlocks a stronger San Stefano pressure layer. Diplomatic demands become harder to resist, limited-war preparation becomes faster, and National Momentum is easier to preserve through a successful Balkan campaign.

The evolution must never invalidate a player who already completed part of the baseline route.

## Evolution II: Tsar of Bulgarians

Requirement: 400+ Chaos.

Evolution II unlocks the medieval imperial identity and the Crown of Simeon route. Greater Bulgaria can become a Bulgarian Empire after a broader territorial and political proof. The route supports annexation, protectorates, client governments, negotiated subordination, and imperial integration according to the chosen political settlement.

If active before Event 048 fires, the opening military and industrial package is significantly stronger and the imperial political branch appears much earlier.

## Evolution III: Kubrat's Legacy

Requirement: 600+ Chaos.

Evolution III unlocks the northern Black Sea and steppe objective. Bulgaria can pursue the Crimean, Azov, Taman, Kuban, lower Don, and bounded southern-steppe groups defined by the geographic research file.

The final formation requires a proven Balkan homeland and a substantial northern Black Sea sphere. It should not be achievable by taking one token state in each region.

If Evolution III is active before the event fires, the event opens at full late-chaos strength with stronger logistics, Black Sea capability, advanced tree visibility, and the final objective visible from the start.

## Evolution pacing

An evolution that is already eligible when Event 048 first fires may modify the initial package immediately. An evolution that becomes eligible after firing should use the shared evolution pacing model and should normally take time to arrive.

Evolution state itself creates no Chaos. Concrete consequences such as wars, annexations, deaths, and other shared sources continue to feed the normal Chaos Meter.

## Campaign-state adaptation

- Already controlled targets move directly toward integration.
- Bulgarian subjects can be kept autonomous, deepened into protectorates, or integrated when route rules permit it.
- If the historical owner no longer exists, pressure targets the current owner.
- Existing regional wars are reused when practical. The event should attach Bulgarian claims and interventions instead of opening redundant parallel wars.
- Dead, annexed, nonhuman, or otherwise invalid targets are skipped or resolved through the current territorial owner.
- A player-controlled target is never protected from the event. It receives the same demand, refusal, negotiation, or war choices as an AI country.

# Part 3: Focus tree architecture

## Tree scale

The implementation blueprint contains 120 authored focus roles. The registry has 108 base-tree roles plus 6 Evolution I roles and 6 Evolution II roles. Evolution III primarily unlocks the already-authored Kubrat and Black Sea late-game branch through visibility and availability gates, so it does not require a separate third set of appended nodes.

The final implementation may adjust exact node count only when MCP focus inspection and rendering prove that a merge or split improves route clarity without deleting accepted content. Any count change must be reported.

## Lane architecture

The normal-zoom tree should read as six large families with clear sublanes:

1. National Awakening and government
2. Army, air, and Black Sea forces
3. Industry, logistics, and reconstruction
4. San Stefano expansion and integration
5. Diplomacy, protectorates, and Balkan order
6. Imperial and Kubrat late game

The opening is compact. Early focuses are commonly 35 days. Emergency handoffs may use shorter durations when they only unlock an immediate action. Mature institutional and integration focuses can use normal 70-day pacing.

## National Awakening

This branch turns the initial surge into a coherent state. It organizes emergency command, mobilization, claims, propaganda, administration, and the first border actions. It also opens the political fork.

## Government of the Greater State

Four political settlements are supported without forcing a simple ideology quota.

### Royal imperial rule

The monarchy becomes the central source of legitimacy. The route favors direct imperial administration, elite command, ceremonial integration, and client monarchies where useful.

### Military-national government

The officer corps dominates the revival. The route maximizes short-term Momentum, faster military pressure, tighter occupation, and rapid mobilization. Its cost is weaker diplomatic acceptance and harder administration in distant territories.

### Centralized Greater Bulgarian state

A civilian-national central government seeks direct incorporation and bureaucratic standardization. It is the strongest route for core integration and domestic administration, but it needs more time and material to absorb distant regions.

### Federation and protectorates

The state accepts a layered Balkan order with protectorates, autonomous clients, and negotiated integration. It has the easiest diplomacy and lowest immediate resistance, but fewer territories become direct cores quickly.

## The Bulgarian Army Reborn

The army family covers mass mobilization, mountain warfare, shock infantry, artillery, armor, logistics, officer reform, veteran integration, captured equipment, reinforcement, and late major-power warfare.

The tree should create or improve concrete templates and production choices. It should not become a line of repeated attack and defense modifiers.

## Arsenal of the Balkans

The industry family permanently changes Bulgarian production and logistics. It places factories, railways, infrastructure, airbases, supply capacity, resources, and building slots in geographically sensible locations. Integrated regions unlock reconstruction and local industrial programs.

The branch has a short-term arsenal route and a long-term integration route. The player can pursue both partially, but the deepest capstones require a clear economic priority.

## The San Stefano Dream

This is the main baseline expansion family. It opens target groups in a readable order, supports diplomatic and military methods, and feeds the integration system after territory is obtained.

The route culminates in Greater Bulgaria. Formation is followed by consolidation content rather than ending immediately.

## Balkan Hegemony

This family decides how Bulgaria handles neighbors and foreign powers. It can build a Bulgarian-led faction, use bilateral protectorates, create client states, seek an outside partner, balance major powers, or insist on strategic independence.

The diplomacy branch changes the options and costs inside the expansion branch.

## Crown of Simeon

Evolution II unlocks the medieval imperial route. It deepens royal or military symbolism, opens broader Balkan ambitions, strengthens subject arrangements, and culminates in the Bulgarian Empire.

The Bulgarian Empire is a major regional order, not a cosmetic rename.

## Kubrat's Legacy

Evolution III reveals the trans-Black-Sea branch. The branch requires Black Sea access and serious logistics. It develops ports, naval or air cover, amphibious and transport capacity, steppe supply, eastern intelligence, and regional administration before the final formation.

The final Old Great Bulgaria formation is the strongest capstone and triggers the event's single dedicated super-event.

## Navigation and filters

Each major family needs Focus Navigation when spatially separate. Search filters must reflect branch ownership. Hidden Evolution II and Evolution III regions must not be revealed by navigation before their evolution gate is active.

## Layout rule

The implementation must use `hoi4.focus_inspect` and `hoi4.focus_render`, then repeat layout review until the six main families, political forks, formation path, and evolution-gated regions are identifiable at normal zoom without tracing long connectors.

# Part 4: Decisions, integration, and formables

## Decision surface

The main category uses a compact status header for National Momentum and Imperial Administration. It exposes only the current phase's most relevant actions. Normal phases should show three to five primary actions and no more than three active missions.

Target-heavy territorial actions use the project's selected-target pattern so the player inspects one foreign target at a time while AI can evaluate all valid targets.

## Territorial pressure families

Bulgaria can use several methods depending on route, target strength, world tension, faction position, and current wars.

- diplomatic demand
- ultimatum backed by mobilization
- border incident
- support for local Bulgarian organizations where historically and politically appropriate
- negotiated border settlement
- protectorate proposal
- direct war preparation
- intervention in an already active regional conflict

These methods have distinct requirements and consequences. They are not cosmetic versions of the same war-goal button.

## Integration loop

A controlled claim does not become a core automatically. Each target group enters one of four administrative states: occupied, pacified, integrating, integrated.

Integration considers control time, compliance, resistance, infrastructure and rail access, garrison or equipment capacity, stability, and Imperial Administration. The exact formula remains hidden. The player sees a short reason when integration is blocked.

Typical actions include restoring local transport, funding municipal administration, recruiting local security, negotiating with local elites, standardizing laws, rebuilding industry, and accepting a slower autonomy settlement.

## Integration missions

Important regions use timed objectives rather than passive stockpile gates. Examples include maintaining supply through a named corridor, keeping resistance under a threshold while holding the state group, restoring a named railway connection, and fielding enough equipped garrison strength in the region.

Failure delays or worsens integration. Success moves the region forward and can improve Imperial Administration.

## Formable 1: Greater Bulgaria

Greater Bulgaria requires the central Greater Bulgaria territorial group to be owned and controlled, with a meaningful share integrated. Subjects do not automatically satisfy direct-core requirements, though the federation route can satisfy designated outer groups through loyal protectorates.

Formation grants a new cosmetic identity and flag, a substantial but bounded power increase, improved integration tools, and new post-formation focuses and decisions.

## Formable 2: Bulgarian Empire

Requires Evolution II, Greater Bulgaria or equivalent territorial proof, broader Balkan dominance, sufficient Imperial Administration, and completion of a valid imperial political settlement.

The formation can tolerate a mix of directly held territory and designated loyal subjects when the political route explicitly supports that order.

## Formable 3: Old Great Bulgaria

Requires Evolution III, a secure Balkan homeland, Black Sea access, the northern Black Sea core group, and enough surrounding steppe or maritime strategic points to prove a real regional sphere.

The formation uses an exact state-puzzle presentation once final state IDs are locked. The puzzle should show required state shapes in their real geographic positions, with clear controlled and missing states.

The final proclamation grants the final cosmetic identity and flag, stronger integration tools for the eastern sphere, a Black Sea military package, and the event's major final power spike.

## Exploit controls

- One-time formation rewards are flagged and cannot be repeated through tag or cosmetic changes.
- Equipment and unit grants are not repeatable decision farms.
- Integration cannot be started on land Bulgaria neither controls nor administers through an accepted subject route.
- Losing a region pauses or reverses integration rather than allowing completion while occupied by an enemy.
- A subject route cannot satisfy every direct-control requirement for free.
- Current-owner targeting prevents dead historical tags from blocking the system.

# Part 5: Politics, diplomacy, regional reactions, and AI

## Political play

The political branch changes the state that emerges from the revival. It controls leader and government direction, law priorities, integration policy, client-state policy, diplomatic tone, and how readily Bulgaria uses force.

The final implementation must inspect installed Bulgarian characters before adding or replacing leaders. Existing vanilla or Chaos Redux characters should be reused when appropriate. Grounded real-person portraits use sourced portrait rules.

## Regional reaction system

Neighboring states react to Bulgarian claims according to their relationship to the current target map, current wars, faction membership, guarantees, army strength, and Bulgaria's escalation level.

Possible reactions include border reinforcement, reciprocal mobilization, guarantees, bilateral defensive talks, a regional containment alignment, foreign requests for support, counterclaims, and negotiated concessions.

Reaction logic should create pressure without guaranteeing an ahistorical dogpile every game.

## Outside powers

Major powers can support, contain, exploit, or bargain with Bulgaria. Their behavior depends on whether Bulgarian expansion helps or threatens their current strategic position. A power already fighting one of Bulgaria's targets can tolerate or coordinate Bulgarian intervention. A power whose faction member is threatened becomes much more resistant.

## Faction and protectorate policy

The Balkan Hegemony family can create a Bulgarian-led faction after enough diplomatic preparation and at least one viable partner exists. The faction should have a clear purpose around regional defense, Bulgarian leadership, and settlement of Balkan disputes.

The protectorate route uses country-specific target handling rather than converting every neighbor into the same generic puppet.

## AI route archetypes

### Opportunist Bulgaria

Prioritizes weak isolated targets, diplomatic demands, and short wars. It preserves Momentum and avoids fighting several stronger factions at once.

### Imperial Bulgaria

Available with Evolution II. It accepts more diplomatic risk, prioritizes the Crown of Simeon route, and prefers direct dominance or hierarchical subjects.

### Administrative Bulgaria

Prioritizes integration, industry, railways, and consolidation before opening another large front. It is more likely when equipment or manpower is strained.

### Federator Bulgaria

Prefers protectorates, faction building, and negotiated arrangements. It accepts slower direct core growth in exchange for lower resistance and broader diplomatic reach.

### Kubrat Bulgaria

Available with Evolution III. It prepares Black Sea access, supply, naval or air support, and logistics before opening eastern targets. It should not suicide across the Black Sea without a viable route.

## AI safety

AI must recalculate target validity when ownership changes. It should avoid declarations against impossible or already allied targets, avoid redundant wars, and stop pressure actions that became obsolete.

Complex AI weights require the project's probability audit workflow before balance is accepted.

# Part 6: Assets, super-event, and achievements

## Asset identity

The event needs a coherent Bulgarian revival visual family across focus icons, idea icons, decisions, formation flags, event art, and the final super-event. Historical symbols must begin from sourced design research. Final flags remain clean flat designs and follow normal HOI4 flag dimensions and naming.

## Event and news art

The opening should use a period-authentic Bulgarian military and national-revival image direction. Greater Bulgaria and Bulgarian Empire milestones can use normal report or news treatment. The final Old Great Bulgaria proclamation receives the strongest unique scene.

## Focus icons

The icon package should cover the six main tree families with distinct visual language. Army icons emphasize infantry, artillery, mountain warfare, armor, logistics, and command. Industry icons emphasize rail, factories, depots, ports, and resources. San Stefano and imperial icons use researched Bulgarian state and royal symbolism. Kubrat icons use Black Sea, steppe, horse, banner, and early-Bulgar imagery only where historically defensible.

## Formation flags

Required flag families:

- Greater Bulgaria
- Bulgarian Empire
- Old Great Bulgaria

Each needs normal, medium, and small runtime variants. Political variants should only be created when the final implementation actually requires distinct ideology or route designs.

## Super-event

The sole planned dedicated super-event marks the successful proclamation of Old Great Bulgaria. Its role is a regional order change and final formable reveal.

The image should present the new Black Sea and steppe identity through a strong period or alternate-history scene, not a map diagram. The exact quote must be researched and verified. The final audio must have its own licensed or public-domain musical recording, unique audio ID, game-ready WAV, settings-aware playback, and documented source.

Greater Bulgaria and the Bulgarian Empire use normal event and news presentation unless later implementation evidence shows that another super-event is justified and the specification is revised.

## Achievement set

The event supports a small achievement family tied to meaningful play rather than automatic firing.

1. Form Greater Bulgaria through the baseline event before reaching Evolution II.
2. Form the Bulgarian Empire while controlling the principal Balkan objective groups directly.
3. Form Old Great Bulgaria and fully integrate at least one northern Black Sea core group.
4. Complete the final form without joining an outside major-power faction.
5. Reach the final form through the federation or protectorate political settlement while keeping designated Balkan partners autonomous.

Achievement implementation requires full trigger, disqualifier, localisation, and icon triplets.

# Part 7: Chaos, cluster behavior, cleanup, and validation

## Event classification

Event 048 remains Minor Fire-Once at Chaos level 1. It belongs to the Formables cluster and should use Medium member severity once the authoritative workbook is aligned.

The current exported event catalog has the event row without cluster and severity values. The package includes a workbook handoff patch row, but the CSV export itself must not be edited directly in the repository.

## Chaos handling

The event does not receive arbitrary Chaos for becoming stronger. Normal shared sources already account for wars, annexations, puppeting, faction changes, deaths, and other world consequences.

Event-owned Chaos changes should be rare and tied to unique outcomes not already counted by shared systems, such as a major forced regional settlement or the final Black Sea imperial proclamation if the implementation decides it represents a distinct world-order shock.

## Formables cluster

The current cluster export identifies Formables as cluster ID 6, Minor Repeatable, unlock tier 3. Event 048 itself has Chaos level 1, so ordinary event eligibility and cluster participation remain separate gates under the shared cluster rules.

The event must remain fully playable when it fires independently before the cluster tier is available.

## Cleanup

Cleanup must remove obsolete territorial target decisions, completed missions, stale target flags, expired opening-surge state, and formation decisions made invalid by a later formation.

Integration state persists only while it remains meaningful. Lost regions retain bounded memory for reconquest and previous administrative work, but the system must not leave active missions against impossible targets.

## Save and campaign robustness

Every formation and route flag must be idempotent. Reopening the decision category, changing owners, capitulating a target, or saving and reloading must not duplicate the opening package, units, buildings, formation rewards, or evolution records.

## Implementation validation

Required production evidence includes:

- event-chain inspection and comparison
- focus inspection, render, and final route coverage audit
- exact-state map inspection for every formation group
- decision and mission audit
- AI probability scenarios and compare pass for weighted logic
- localisation audit
- asset requirement-to-runtime crosswalk
- super-event quote and audio source evidence
- country package audit where political routes change leaders, flags, or government setup
- final event completion audit against all seven spec parts

## No silent simplification

If exact map binding, final assets, AI behavior, an achievement, a political route, a formation, an integration family, or an evolution-gated branch cannot be completed, the implementation remains incomplete and the blocker must be reported.
