# Event 013 Natural Disasters, Part 7, AI, balance, acceptance criteria, and documentation

## AI response model

AI countries must use the disaster system. They should not ignore warnings, preparation decisions, or recovery missions.

AI should consider:

- whether the affected state is a capital, major city, port, supply hub, rail corridor, airfield, resource state, or high-population state
- war state and current fronts
- stability, war support, and manpower
- equipment, trucks, trains, convoys, fuel, and support equipment
- current supply and infrastructure
- disaster severity and family
- chain risk and time remaining
- foreign aid availability
- whether the country is player-adjacent or faction leader

AI priorities:

| Situation | AI behavior |
| --- | --- |
| Dense capital hit | Prioritize search, medical, shelter, and transport recovery. |
| Port or dockyard hit | Close or repair port based on family and warning state. |
| Rail or supply hit during war | Prioritize rail clearance and supply hub repair over cosmetic reconstruction. |
| Heat, drought, cold, or blizzard | Prioritize water, fuel, food, and medical relief. |
| Flood or tsunami | Prioritize evacuation, clean water, medical corridor, and port checks. |
| Volcanic ash | Prioritize airfield closure, ash cleanup, crop protection, and respiratory response. |
| Meteor or rupture | Prioritize triage, capital survival, transport repair, and follow-up warning. |
| Weak country with low resources | Choose cheapest useful relief, accept foreign aid when safe, and avoid impossible reconstruction. |
| Strong country | Use preparation to reduce death spike and clear aftermath faster. |

AI should avoid clicking expensive preparation actions when the warning window is already expired or the target no longer exists. It should not take actions for invalid states, dead countries, inactive disaster cards, or closed aftermaths.

## Balance principles

Natural Disasters should be punishing but not random nonsense. The player should be able to reduce losses through preparation and recovery, while still respecting that some disasters cannot be erased.

Important balance rules:

- Baseline disasters are strong enough to matter.
- Warnings reduce losses but do not nullify severe disasters.
- Preparation has real opportunity cost.
- Recovery actions are meaningful, family-specific, and staged.
- Deaths scale with vulnerability and population, not flat numbers.
- Building damage targets relevant systems, not random tiny damage.
- Evolution II chains are dangerous if ignored.
- Evolution III abnormal disasters can be absurdly destructive when earned by chaos state.
- News throttling prevents late-game spam.
- One Event 013 firing creates one log row even when several disaster subevents happen.
- Disaster Barrage is a manual challenge and can be much harsher than ordinary pacing.

## Exploit and abuse checks

Implementation should guard against:

- repeated free reconstruction rewards
- farming foreign aid for equipment
- using evacuation to delete or move population in exploitable ways
- repeatedly triggering low-cost disaster calls against enemies without cooldown or cost from external callers
- world-spanning abnormal disasters repeating too often
- heat effects stacking with Event 051
- Event 046 or Event 099 old logic firing separately
- report spam from every small Evolution II disaster
- recovery decisions staying visible after the disaster is cleared
- stale target references after state owner changes or annexation
- AI spending scarce resources on invalid or low-value recovery

External callers that weaponize disasters need their own costs, cooldowns, and target rules. The Event 013 engine should support the call but should not make divine or hostile disaster spam free.

## Documentation requirements

The event documentation should explain:

- what Event 013 is
- how one firing becomes a delayed disaster season
- how the reusable call system works at a design level
- how deaths and building damage scale
- how warnings, reports, and aftermath cards work
- how family-specific recovery works
- how evolutions change the system
- how Disaster Barrage uses the same controller
- how Event 046 and Event 099 are treated
- how heat stacking with Event 051 is prevented
- how news throttling works
- what assets and super-events are planned
- what limitations remain

The spreadsheet should later be updated from final in-game Event Details wording after implementation. This planning package does not directly edit the workbook.

## Acceptance criteria

A future implementation should not be marked complete until these criteria are true.

| Surface | Acceptance criteria |
| --- | --- |
| Event controller | Event 013 can start a season with delayed impacts, target validation, news policy, report policy, aftermath policy, and cleanup. |
| Reusable calls | Other events can request family, target, severity, news, report, aftermath, chain, and scaling behavior without copying logic. |
| Family playbooks | Every implemented family has unique target scoring, warning behavior, damage pattern, death drivers, recovery tasks, and report direction. |
| Deaths system | Disaster deaths reduce real local population and feed the shared Deaths system with visible records. |
| Damage | Building and state damage is strong enough to matter and family-specific. |
| Reports | Affected countries reliably receive delayed reports 1 to 2 days after serious impact. |
| Aftermath UI | Serious impacts reliably open or refresh the aftermath category notification and active disaster card. |
| News | Early news is specific and varied. Later news is throttled to serious or unusual disasters. |
| Evolutions | Evolution I, II, and III are logged as evolutions and change behavior without logging ordinary stages. |
| Abnormal GUI | Evolution III moving disasters have dynamic map presentation and static fallback assets. |
| Super-events | Major abnormal moments have complete researched super-event packages before being called complete. |
| Scenario | Disaster Barrage uses the same controller with type and intensity controls. |
| Old events | Event 046 is inactive placeholder. Event 099 does not keep separate sandstorm logic. Heat stacking with Event 051 is blocked. |
| AI | AI uses preparation and recovery decisions with route-safe and resource-aware weights. |
| Docs and catalog | Event docs, event details, scenario docs, cluster docs, and spreadsheet text are aligned after implementation. |
| Audits | Localisation, decisions, scripted system helpers, assets, super-events, and completion are audited before completion claims. |

## Meaningful validation expected after implementation

The implementation agent should perform task-specific checks such as:

- trigger Event 013 baseline and verify delayed impacts are not same-day
- call a specific disaster family from an external test effect and verify reports and aftermath open
- run a Disaster Barrage Low and Maximum scenario and verify intensity changes sequence size
- hit a dense state and a sparse state with the same severity and verify absolute deaths scale with population
- trigger Evolution II regional system and verify neighboring state damage and chain risks
- trigger Evolution III storm corridor and verify GUI path updates
- verify Event 046 does not fire old logic
- verify Event 099 either stays placeholder or calls Event 013 dust family only
- verify Event 051 heat stacking is blocked when active
- verify no small repeated Evolution II impacts spam global news
- verify recovery decisions disappear after cleanup
- verify AI can take at least one preparation and recovery path without human-only GUI dependence

These checks should be reported with evidence. Generic syntax hygiene should be run internally but does not need a bloated final report unless it finds a problem.
