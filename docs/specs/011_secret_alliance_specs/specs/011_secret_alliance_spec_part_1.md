# Event 011 Secret Alliance Specification

This specification treats **Secret Alliance** as a hidden diplomatic crisis aimed at the current player country. Three countries begin a covert compact against the player. The compact grows through quiet meetings, intelligence work, diplomatic pressure, sabotage, provocations, and later public military coordination. The player should first feel that foreign behavior has become strange rather than see a complete enemy list.

The design keeps the first phase subtle, then gives the player a counter-conspiracy layer once the pattern becomes too strong to ignore. The hidden pact becomes public only through exposure, a public escalation milestone, or a war involving a pact member and the player.

## Core playable promise

The event should make the player feel hunted by a diplomatic pattern that was already moving before it became visible. It should not open with three countries instantly declaring war. The interesting play is the period between the first oddities and the public compact.

The player experience has four linked pressures.

| Pressure | What it means in play | How it should feel |
| --- | --- | --- |
| Shadow reach | How many countries and assets the compact can use | Foreign behavior repeats with a pattern before the pattern has a name |
| Secrecy | How hard it is to identify members and prove coordination | Early incidents do not name the full network |
| Aggression | How often the compact damages or provokes the player | Sabotage changes from nuisance to strategic pressure |
| Player preparedness | How ready the player is for exposure, diplomacy, border incidents, and war | Counterplay becomes stronger if the player acted before open conflict |

The compact should have its own internal values, not only flags. Those values should change through meetings, recruitment, player countermeasures, leaks, failed operations, war state, chaos tier, member strength, and the presence of major powers.

## Initial target and founder selection

The event fires for the current player country and stores that country as the target. The first firing chooses one convenor and two other founding members.

### Hard eligibility

A country can be a founding member only if it exists, is independent enough to make foreign policy, is not the target, and is not at war with the target. It should not be a special non-human or terminal chaos country. It should not be capitulated. A subject can only qualify if its autonomy level and diplomatic situation allow plausible independent plotting. Same-faction countries with the target should normally be excluded because the surprise would be hard to present cleanly.

The event should prefer minors that are outside factions. This preference should be strong enough that most calm openings create three small countries acting in the dark. A country already in a faction can be a low-weight candidate only when it has a strong grievance and the pact has no clean factionless candidate pool.

### Weighted preference model

Candidate scoring should be dynamic. The selection helper should compute a hidden `secret_alliance_candidate_score` from factors like these.

| Factor | Weight direction | Design reason |
| --- | --- | --- |
| Minor status | Strong positive for baseline and Evolution I | The premise starts as minor states conspiring |
| Factionless | Strong positive | The player should not instantly read the compact from existing blocs |
| Poor relations with target | Positive | Grievance should feel grounded |
| Different ideology family | Positive | Ideological fear gives recruitment a voice |
| Claims, cores, border rivalry, or contested region near the target | Positive | Makes border incidents and military preparation plausible |
| Recent target expansion or world tension caused by target | Positive | Makes the pact feel like a reaction to player conduct |
| Has a shared border with target | Moderate positive for one member, not all | Neighbor members enable border wars but distant members keep mystery wider |
| Same continent as target | Moderate positive | Local concern should matter |
| Far away naval or colonial reach | Situational positive | Allows one distant member to fund spy and propaganda work |
| Being in the target faction | Strong negative or exclusion | Prevents unreadable betrayal in ordinary openings |
| Being a player country in multiplayer | Exclusion unless that player is the target | Prevents hidden hostile control of another player |
| Being already at war with the target | Exclusion | The user requirement forbids this |

### Founder roles

The compact should assign roles to the first three members. These roles can later change, but early role identity gives the AI useful behavior.

| Role | Preferred candidate | Hidden behavior |
| --- | --- | --- |
| Convenor | Factionless minor with high grievance and decent stability | Hosts first meetings, invites members, tracks compact cohesion |
| Purse holder | Country with civilian industry or money-flavored political stability | Funds propaganda, bribes officials, builds foreign press reach |
| Knife hand | Neighbor or militarized country | Runs border incidents, courier routes, sabotage, and military probes |

If a country is selected for a role, it receives a hidden role flag and a hidden role value. A later major can become patron without replacing the convenor unless the major forces a leadership contest.

## Compact values and state

The implementation should keep the compact as a hidden system before it becomes a normal faction.

| Value | Scope | Opens with | Changes through play | Visible to player |
| --- | --- | ---: | --- | --- |
| Pact secrecy | Global or target-scoped | High | Leaks, failed operations, counterintelligence, major entry, public incidents lower it | Shown as uncertainty only after the dossier opens |
| Pact cohesion | Global or pact leader scope | Medium | Successful meetings, shared enemies, major patronage, player exposure attempts, bribery, rival ideologies | Hidden until reveal, then shown as public unity |
| Pact aggression | Global or pact leader scope | Low baseline | Evolutions, sabotage success, target weakness, major entry, border tension | Felt through incident frequency |
| Pact war readiness | Pact leader scope | Low | Military meetings, arms pooling, member count, major entry, failed diplomacy | Shown when the public faction appears |
| Player suspicion | Target country | Very low | Repeated incidents, evidence decisions, intercepted couriers, failed pact action | Visible once the dossier category opens |
| Player preparedness | Target country | Low | Dossier decisions, counterintelligence missions, border guard objectives, war cabinet preparation | Visible in dossier and war tooltips |
| Evidence quality | Target country | None | Investigations, leaks, defector deals, captured agents | Visible in exposure decisions |
| Identified members | Target country flags on each member | None | Intelligence actions and public incidents | Visible as named targets in the dossier |

The player should never see an exact list of secret members from the first popup. The list is earned through evidence, leaked incidents, or public reveal.

## Baseline phase

The baseline starts after the first compact meeting. The player receives a small report that does not prove coordination. The report direction should focus on repeated behavior, informal diplomatic gatherings, travel by junior attachés, embassy staff movement, newspaper habits, trade delegates, and odd local rumors.

Baseline incidents are slow. They should rarely apply severe damage. Their purpose is to create a pattern and seed hidden compact values.

### Baseline incident families

| Family | Actor | Player-facing information | Mechanical direction |
| --- | --- | --- | --- |
| Closed-door meetings | Convenor or random founder | Diplomats from several small states meet outside normal channels | Raises cohesion and secrecy unless a player spy network is strong |
| Press whispers | Purse holder | Foreign papers begin printing similar language about the target | Small relation damage and target suspicion gain |
| Embassy couriers | Any founder | Couriers move between consulates and military attaché offices | Creates evidence chance if the player has intelligence tools |
| Procurement irregularities | Purse holder | Commercial orders look too similar across countries | Raises pact war readiness slowly |
| Port and rail curiosity | Knife hand or neighbor | Foreign travelers take interest in depots, ports, rail junctions, and border roads | Seeds later sabotage or border incident targets |
| Diplomatic cold shoulder | Any founder | A minor diplomatic meeting fails in a strange way | Small opinion and trade friction |

### Baseline player options

The player should get ordinary event options only. The options should not name the pact or offer direct retaliation. The option tone should vary between calm caution, irritated dismissal, and quiet intelligence interest. Final localisation should avoid explaining that the event is a warning.

Baseline options should nudge hidden values.

| Option role | Narrative meaning | Effect direction |
| --- | --- | --- |
| Ignore odd behavior | The government treats the reports as diplomatic noise | Slightly preserves pact secrecy, no direct cost |
| Ask legations for clarification | The government sends polite inquiries | Small suspicion gain, small relation risk with potential members |
| Quietly file the pattern | Intelligence staff begins a low-priority file | Small evidence chance, tiny political or intelligence cost |

## Evolution I, wider minor compact

Evolution I begins once the compact has enough cohesion, enough time has passed, or world chaos makes quiet organizing easier. It can also be the first public intensity if Event 011 fires after the relevant chaos threshold and the event has not fired before.

The change from baseline is scale. More minor countries can join. The compact becomes noticeable through repeated actions, but direct war remains locked unless a member is pulled into war with the player by another route.

### Evolution I new behavior

| New behavior | Design |
| --- | --- |
| Minor invitations | The convenor and purse holder can invite additional factionless minors. Refusal can leak evidence. |
| Shared talking points | Several countries repeat similar diplomatic phrases in newspapers, votes, guarantees, and trade talks. |
| Soft isolation | The target receives more relation pressure, attaché refusals, trade friction, and lowered invite acceptance. |
| Low-grade sabotage | Industrial mishaps begin, usually as timed state modifiers or one damaged building rather than heavy destruction. |
| False committees | Diplomatic conferences appear to discuss peace, neutrality, transit, or trade but quietly score potential recruits. |

### Evolution I containment through ordinary systems

The player still does not receive the full dossier category. Counterplay should come through ordinary intelligence strength, diplomacy, and event options. If the player has high intel networks, strong counterespionage laws, or high stability, incidents should produce more clues and less damage.

## Evolution II, active sabotage and the dossier

Evolution II is the point where the player knows a pattern exists. A major power can join here. If Event 011 first fires at this stage, a major power can be the founder or patron, then it extends the compact to minors. If the compact is already active, the major joins as patron, arsenal, guarantor, or shadow chair.

The dossier decision category appears here. The player does not get one automatic war button yet. The player gets tools to investigate, harden the country, split members, expose the compact, and prepare for a future conflict.

### Major member logic

A major can join at Evolution II only if it is not at war with the target and can plausibly oppose the target. The major should prefer joining if it has rival ideology, low opinion, competing claims, strategic fear of the target, or a nearby sphere interest. A major should avoid joining if it is dependent on the target, in the same faction, near capitulation, already overloaded by wars, or has strong positive relations.

Major entry changes the compact.

| Major role | Behavior |
| --- | --- |
| Patron | Increases funding, evidence risk, and diplomatic reach |
| Arsenal | Adds war readiness and shared equipment support |
| Shield | Makes minor members braver and harder to split |
| Rival chair | Can contest the convenor and reduce cohesion if ideologies clash |

### Evolution II incident families

| Family | Player-facing information | Mechanical direction |
| --- | --- | --- |
| Factory sabotage | Explosions, delays, contaminated contracts, and missing tools in a key industrial state | Damages factories or applies a timed production penalty, with scale based on secrecy and preparedness |
| Targeted intimidation | Activists, officers, diplomats, or engineers connected to the target disappear or are attacked abroad | Stability, war support, advisor availability, or command power pressure |
| Border provocation | Neighbor members create patrol incidents, shots, local seizures, and suspicious mobilization | Opens border missions and possible border war decisions |
| Trade squeeze | Members quietly cancel contracts or coordinate embargo-like behavior | Consumer goods burden, resource import cost, or trade opinion penalties |
| Courier capture | The player can intercept real evidence | Raises evidence quality and can identify one member |
| Threatening notes | Public statements use increasingly shared language | Raises suspicion and reduces pact secrecy |

### Dossier category role

The dossier should feel like a compact intelligence board rather than a store. It should show suspicion, evidence quality, preparedness, guessed membership count, identified member list, and current danger stage. The player should choose between investigation, defense, diplomacy, public exposure, and border preparation.

The category should not show every possible target at once. Use a selected-target pattern for human players. The list should present known or suspected countries, allow selecting one target, then show actions for that target.

## Evolution III, public compact and war horizon

Evolution III makes the compact visible. The hidden compact becomes a public faction named dynamically as an Anti-[target country] Pact. More members can join, and a second major can join if prior decisions, high aggression, and campaign state allow it.

The player receives a war option and public faction tools. War should not start immediately just because Evolution III unlocked. It should become likely through a war-readiness mission, escalating incidents, failed talks, player preemption, or a member entering war with the player.

### Public reveal paths

The compact is revealed through one of these paths.

| Reveal path | What happens |
| --- | --- |
| Evolution III public announcement | A public bloc forms and appears on the map. War pressure starts. |
| Member enters war with target | The compact is revealed instantly. The faction forms and all members join war against the target. |
| Player exposes enough evidence | The compact is forced into public view early. Cohesion can fall and some members may deny involvement. |
| Pact operation fails badly | A sabotage or assassination incident leaves public evidence. The compact can reveal with lower cohesion. |
| Player attacks a confirmed member | The compact reveals unless the player isolated that member through prior decisions. |

### Evolution III actions

| Public compact action | Design |
| --- | --- |
| War council mission | A visible timer tracks the compact's march toward war. Strong player preparedness can extend it. |
| Final recruitment | Remaining eligible countries can be invited publicly, with higher refusal chance if evidence damaged the pact. |
| Military pooling | Members gain shared military planning bonuses, equipment transfers, or coordinated mobilization. |
| Ultimatum chain | The pact can demand demobilization, reparations, diplomatic retreat, or territorial concessions where relevant. |
| Open war option | The player can strike first, demand dissolution, or force a border settlement depending on evidence and preparedness. |
| Splitter diplomacy | Identified weak members can be pressured to leave before the war timer expires. |

## War conversion rule

When any compact member goes to war with the target, the hidden compact must reveal and convert to the public faction immediately. All compact members that are still valid join the faction and enter the war against the target. This applies if another event, focus, decision, guarantee, or scripted war pulls a member into conflict.

The implementation should call a single helper for this rule. That helper should sanitize the member list, create the faction if it does not exist, set the dynamic faction name, add valid members, start the war, apply war ideas, record the event log, and clean up hidden-only state.

If a member has been isolated by a completed player decision chain, that member can be exempt from the immediate war join. This exemption must be rare, visible in tooltips before the war, and tracked with a clear flag.

## Member lifecycle

Countries can join, leave, defect, deny involvement, or be expelled.

| Lifecycle state | Trigger | Result |
| --- | --- | --- |
| Suspected | Clues point to the country but no proof exists | The player can investigate it but not take hard public action |
| Hidden member | Country is in the compact but unidentified | It can act through hidden incidents |
| Identified member | Evidence confirms membership | The player can target it with diplomacy, sanctions, border missions, or exposure |
| Public member | Pact is revealed and country is in the faction | Normal faction and war rules apply |
| Defector | Player turns a member or the member breaks under exposure | It can provide evidence, immunity, or a temporary intelligence bonus |
| Isolated member | Player prevents the full war guarantee from applying to that member | It can be attacked or coerced without automatic full pact war if the isolation tooltip says so |
| Expelled member | Pact removes a weak or compromised country | It loses pact ideas and cannot rejoin without a major event |

Leaving the compact should be possible but not cheap. A member leaves because it is exposed, bribed, threatened, defeated in a border incident, abandoned by a major patron, or harmed by player intelligence work.

## Player response routes

The player has five response routes. They are compatible, but time and cost force priorities.

| Route | Primary value | Best against | Risk |
| --- | --- | --- | --- |
| Counterintelligence | Evidence quality and member identification | Hidden members and sabotage | Costs support equipment, command attention, and stability if heavy-handed |
| National hardening | Preparedness and sabotage defense | Factory damage, assassinations, border panic | Consumes equipment, trains, factories, and manpower |
| Public exposure | Secrecy damage and cohesion loss | Major patron entry and public legitimacy | Fails badly if evidence quality is weak |
| Splitter diplomacy | Member exits and isolation flags | Minor members and ideologically mixed pacts | Creates concessions, foreign influence debt, and relation costs |
| War preparation | War readiness, border missions, and strike option | Evolution III and instant reveal war | Can raise pact aggression and domestic war anxiety |

The design should avoid a single optimal route. A player who spends everything on exposure may enter war unprepared. A player who only prepares for war may let the pact grow. A player who bribes members may weaken domestic legitimacy.

## Incident escalation pacing

The compact should not use daily whole-world polling. Use event pulses, timed flags, scheduled events, and target-scored decision actions. Evolution MTTH can use a base around ninety days, modified by chaos tier, compact values, and player state.

Suggested pacing direction:

| Stage | Ordinary time between compact incidents | Notes |
| --- | ---: | --- |
| Baseline | 60 to 120 days | Most incidents are flavor plus small hidden value changes |
| Evolution I | 45 to 90 days | More member invitations and visible patterns |
| Evolution II | 30 to 75 days | Dossier opens and sabotage can matter |
| Evolution III | 20 to 60 days | Public pressure, ultimata, and war readiness dominate |

Durations should be dynamic constants, not hardcoded scattered values.

## Outcomes

### Hidden collapse

The player can collapse the compact before it becomes public by identifying enough members, turning one founder, blocking invitations, and forcing failed operations. This should feel like a quiet intelligence victory. It should leave a small diplomatic aftermath and a hidden event log entry that records the compact's collapse.

### Forced public scandal

The player can expose the compact early. The public reveal happens, but cohesion is lower, some members may deny involvement, and the future war timer is delayed or weakened. If a major patron exists, the major may either double down or abandon the compact depending on evidence and strategic strength.

### Public cold war

At Evolution III, the faction can appear without immediate war. The player can still negotiate, split members, or prepare. The public compact applies diplomatic and mobilization pressure. War starts if readiness, aggression, ultimatum failure, or direct conflict crosses the threshold.

### Open war

If war begins, all valid public members join. The pact should receive a temporary opening coordination bonus that decays unless cohesion remains high. The player receives bonuses or missions based on preparedness. Defeating the pact should remove the public compact, clear hidden state, and unlock postwar cleanup decisions.

### Pact victory

If the target capitulates to the pact or accepts a severe ultimatum, the pact imposes a humiliation package. This can include demilitarization ideas, forced reparations, loss of guarantees, temporary faction restrictions, and diplomatic vulnerability. Territorial transfers should only happen when a member has a real claim or the war path created a specific demand.

## Design constraints for implementation

The event should be fire-once. Its hidden systems can continue for years, but the root event should not create a second independent compact. If the target tag changes through player switching or tag transformation, the implementation should keep the pact target clear or cleanly migrate the target if the project has a standard helper for that situation.

The compact should stay outside existing event cluster mechanics unless the implementation agent receives a later accepted design that changes that. Do not register it as a member of a random cluster during this rework.

The event must keep baseline stages separate from evolution log entries. Normal dossier progress, incident counts, and war-readiness timers are baseline progression. Only the three named escalation stages are event evolutions.
