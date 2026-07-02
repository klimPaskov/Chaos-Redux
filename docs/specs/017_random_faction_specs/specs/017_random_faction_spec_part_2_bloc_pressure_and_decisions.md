# Event 17: Random faction, bloc pressure and decision systems

## The living system: bloc pressure

The event should create a small persistent memory system called bloc pressure. This is not a custom GUI-first mechanic. It is a decision and event-layer system that records where neutrality is weakening and which factions are gaining local credibility.

Bloc pressure should have four visible or semi-visible concepts:

| Concept | Meaning | Main surface |
| --- | --- | --- |
| Regional bloc pressure | a region is seeing repeated faction moves | decision category header or event detail |
| Neutrality resilience | a neutral country is still able to resist pressure | national spirit tooltip and decisions |
| Faction pull | a specific faction is becoming attractive in a region | scripted localisation where useful |
| Rival reaction | other factions respond to a new member | follow-up events and faction-leader decisions |

The values should be dynamic. They should not be a few hidden flat numbers that only the event reads. Firing Event 17 should increase regional pressure. Neighbor decisions can reduce or redirect pressure. A rival faction reaction can increase competing pull. A failure to answer pressure can leave a neutral country easier to select in later firings.

## Country memory

The implementation should use flags and variables to avoid repeat abuse and stale targets.

### Selected country memory

- recent Event 17 alignment flag with a timed duration
- stored chosen faction leader or chosen faction id where the engine can support it
- local political shock variable if the country receives a temporary spirit
- optional war entry risk flag if the chosen faction is already at war

### Neighbor memory

- under bloc pressure flag
- pressure source faction id or source faction leader target where possible
- pressure region id or scope marker
- neutrality resilience value
- delayed follow-up flag if Evolution I or later schedules a response event

### Faction leader memory

- recently gained Event 17 member count
- region where member was gained
- rival reaction cooldown
- faction cohesion strain value if repeated small-state entries are overloading a faction

## Decision category: Bloc pressure

A decision category should appear only when a country has visible work to do. It should not be a permanent global debug menu. The category can be called by a working label such as `bloc_pressure_category`, but final localisation should be written from the country viewpoint.

### Category visibility

The category appears for:

- a country that joined a faction through Event 17 and still has its alignment shock spirit
- an eligible neutral neighbor under active pressure
- a faction leader that recently gained or lost a regional influence contest
- a faction leader with active reaction decisions toward a pressured region

The category disappears when the relevant flags and missions are cleared.

### Category header

The header should summarize the current state in one or two dynamic lines:

- for selected minors, show the faction joined and remaining alignment shock duration
- for pressured neutrals, show pressure source and neutrality resilience state
- for faction leaders, show the active region and whether a rival faction is competing there

Do not expose raw trigger text. Use scripted localisation and custom tooltips.

## Decision families for selected minors

### Stabilize the New Alignment

A one-time or cooldown decision for a minor that just joined a faction.

Narrative role: the government tries to reconcile cabinet, command, and public organizations after the sudden alignment.

Costs and requirements should scale with country size and state of war. Use a mix of political power, stability strain, command power, infantry equipment, and support equipment. If the country joined a faction at war, the decision can also require a small manpower commitment or border garrison presence.

Result direction:

- reduces the alignment shock duration or penalty
- improves faction leader relations
- slightly increases faction cohesion if that mechanic is implemented
- can raise domestic polarization if overused or taken under low stability

AI use:

- high priority if the country is newly aligned and not collapsing
- low priority if equipment is scarce and the country is already fighting for survival

### Request Liaison Mission

A targetable decision aimed at the faction leader.

Narrative role: the new member asks for staff officers, signals coordination, and basic training support.

Costs and requirements:

- selected minor spends command power or army XP if it has enough
- faction leader may pay support equipment, trucks, convoys, or command power through a paired effect
- requires the leader to exist and not be at war with the selected country

Result direction:

- improves military coordination for a limited time
- can increase faction leader influence over the minor
- can lower neutrality resilience of nearby minors because the alignment looks real

### Quiet the Opposition

This is a risky internal decision, not a free stability button.

Narrative role: the government pressures parties, newspapers, and local assemblies that opposed the faction choice.

Costs and risks:

- stability and political power
- possible war support shift if faction is at war
- risk of ideology polarization
- larger risk under Evolution II and Evolution III

Result direction:

- reduces short-term shock
- increases a hidden polarization value
- can create a later backlash event if repeated under poor stability

## Decision families for pressured neutral neighbors

### Convene the Neutrality Council

A cooldown decision for eligible neutral countries under pressure.

Narrative role: parties, army officers, business groups, and local officials argue over whether neutrality still protects the country.

Costs and requirements:

- political power, but not only political power
- stability threshold or cost
- small army XP or command power to represent military consultation
- if at war or threatened, require divisions in the capital or border states

Result direction:

- raises neutrality resilience
- delays a forced alignment follow-up
- can reduce regional bloc pressure slightly
- may make future Event 17 selection less likely for this country

AI use:

- democratic or neutral AI with high stability prefers it
- fascist, communist, or desperate wartime AI is less likely to resist pressure

### Reinforce the Border Posts

A timed mission that auto-completes when the country has divisions in relevant border or capital states.

Narrative role: neutrality has to be defended physically, not only declared.

Requirements:

- place supplied divisions in named border states or the capital region
- enough infantry equipment to maintain reserves
- not already in a faction

Success direction:

- raises neutrality resilience
- lowers the weight of joining hostile or remote factions
- can slightly improve war support without making the country aggressive

Failure direction:

- lowers neutrality resilience
- raises chance of a later copycat or rival-alignment event
- can make the country more attractive to nearby factions

### Invite Observers from a Faction

A risky decision where a neutral country invites one faction to inspect exercises or send advisers without formally joining.

Costs:

- relations with the faction leader
- political power or command power
- possible support equipment or convoy requirement if overseas
- hidden independence debt toward that faction

Result direction:

- makes that faction more likely in a later forced alignment
- can deter rival factions temporarily
- can anger a neighboring rival faction member

This decision should be visible only when the country is pressured and the faction leader is a valid target.

### Publish a Neutrality Declaration

A public stance decision that temporarily resists all faction pull but increases attention.

Costs:

- stability if the country is polarized
- political power
- possible war support reduction if the country is threatened

Result direction:

- improves neutrality resilience for a limited time
- increases regional attention, so another nearby neutral may become more likely to be targeted later
- should not be spammable

## Decision families for faction leaders

### Offer Staff Mission

A faction leader can invest in a pressured or newly aligned minor.

Costs:

- support equipment
- command power
- trucks or convoys if the target is distant or overseas
- diplomatic exposure or temporary relation risk with rival factions

Result direction:

- increases pull toward the leader's faction
- helps a new member stabilize
- can reduce the chance that the new member leaves through another system

### Sponsor Radio and Press Networks

A soft-power pressure decision.

Costs:

- political power
- civilian factory burden or consumer goods burden for a short duration
- intelligence exposure if La Resistance systems are available or if Chaos Redux has a compatible proxy value

Result direction:

- increases faction pull in one region
- raises ideological polarization in pressured minors
- can trigger rival propaganda follow-ups under Evolution I and higher

### Guarantee the Corridor

A faction leader attempts to make a new member or pressured neutral feel protected.

Costs and requirements:

- convoys or trains when supply routes matter
- enough army strength relative to local rivals
- not invalid because of direct war with target

Result direction:

- raises faction pull
- can create a defensive guarantee or scripted guarantee-like relation if appropriate
- under Evolution II, can increase war danger if the target borders a faction enemy

### Demand a Public Commitment

A harsher Evolution II and III decision for faction leaders.

Narrative role: the faction leader pushes a neutral country to stop balancing and publicly choose.

Costs and risks:

- political power and command power
- relation damage with the target if it refuses
- world tension or chaos pressure if used aggressively

Result direction:

- can force a follow-up event for the target
- can push the target toward a rival if the target refuses
- AI should only use it when aggressive, threatened, or high chaos

## Temporary national spirits and idea lifecycle

This event does not need a full country focus tree, but it does need a small set of reusable spirits.

| Working idea label | Holder | Role | Lifecycle |
| --- | --- | --- | --- |
| Alignment shock | selected minor | short-term strain after sudden faction entry | expires or is shortened through stabilization |
| Border pressure | neutral neighbor | visible tension and readiness burden | removed by successful neutrality decisions or joining a faction |
| Bloc polarization | pressured country | harsher Evolution II political split | upgraded, removed, or converted after choice |
| Neutrality exhaustion | regional late-stage country | Evolution III pressure that makes remaining outside factions harder | removed by joining, resisting through objectives, or region cooldown |
| Liaison mission | selected minor or faction leader | temporary military coordination | expires or upgrades through successful support decisions |

Effects should be meaningful but not huge. The spirit should change behavior enough that the player reacts, but the event should not become a permanent buff farm.

## Scripted GUI and animated presentation

A full custom window is not required for the baseline. A compact scripted GUI or category header becomes useful at Evolution II and Evolution III when several countries and factions are under pressure.

Recommended UI direction:

- a small decision category header seal showing crossed diplomatic cables and faction banners
- a pressure status line with the active region and pressure state
- a warning state when neutrality resilience is low
- a selected faction card or target row only if the repository already has a good selected-target decision pattern

Animated presentation is useful for the category seal and warning state. The animation should be subtle and state-driven:

| Animated asset | Surface | State logic | Static fallback |
| --- | --- | --- | --- |
| bloc pressure seal | decision category header or scripted GUI header | active when a country has pressure missions | static crossed banners seal |
| warning border | scripted GUI header or status card | visible when neutrality resilience is critically low | static red-tinted warning frame |
| faction pull node | optional target card | visible when a faction leader is actively pressuring a country | static faction marker |

The final animation must use real source frames, a frame sheet, and a static fallback. Do not implement a transform-only glow or GIF-as-asset.

## Cleanup rules

The system must clean up pressure flags and decisions when:

- the country joins a faction
- the country becomes a subject
- the country stops existing
- the faction leader stops existing
- the region pressure expires
- the country becomes a special chaos country
- the country is annexed, released, or transformed by another event
- a world-end terminal state exists

Cleanup should remove active decisions, stale target flags, temporary variables, and temporary event targets where used. Avoid global event targets unless persistence is truly needed.
