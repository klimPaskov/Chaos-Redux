# Event 011 Secret Alliance Member Country Effects and Integration

Secret Alliance uses existing countries as temporary event-managed actors. It should not replace a country's national focus tree or country identity by default. It should add hidden roles, AI behavior, temporary ideas, decisions, and public faction effects that clean up after the compact ends.

## Hidden member package

| Surface | Requirement |
| --- | --- |
| Hidden role flags | Every member has one or more role flags. Founders keep founder flag for achievements and targeting. |
| Hidden idea or dynamic modifier | Use only if it is needed for AI and incident hooks. It should not show to the player before reveal unless the member is controlled by a human who should know its own role. |
| AI strategy | Members gain target-focused diplomatic and military behavior without suicidal war starts. |
| Incident cooldowns | Each member needs cooldowns for meetings, sabotage, invitations, and border actions. |
| Cleanup | All hidden member state clears when the member leaves, defects, dies, or the compact ends. |

## Public member package

| Surface | Requirement |
| --- | --- |
| Faction membership | Valid members join the public Anti-[target] Pact through the reveal helper. |
| Public idea | A temporary coordination idea can apply to public members. It should decay or be removed after war or dissolution. |
| War plan AI | Public members evaluate fronts, allies, target strength, and war readiness. |
| Diplomatic identity | Public members can receive opinion changes with target, observers, defectors, and other members. |
| Exit logic | Weak members can leave before war if cohesion is low and player actions succeeded. |

## Temporary idea lifecycle

| Idea working label | Who gets it | Start | Upgrade or change | Removal |
| --- | --- | --- | --- | --- |
| shadow_compact_member | Hidden members | On joining hidden compact | Role flags change behavior rather than stacking many ideas | Member exits or public reveal converts it |
| pact_coordination | Public members | Public reveal | Stronger if cohesion high, weaker if exposure damaged compact | Pact defeated, dissolved, or member exits |
| exposed_conspirator | Member caught by evidence | Exposure success | Can become defector or isolated member | After aftermath or settlement |
| defector_protection | Defector | Defection accepted | Can provide evidence and immunity | After compact ends or defector betrays target |
| target_under_shadow_pressure | Target | Root or later incident | Worsens with aggression, mitigated by preparedness | Compact collapse, public transition, or aftermath |
| counterintelligence_desk | Target | Dossier opens | Improves through missions | After aftermath if no longer needed |
| prepared_state | Target | War preparation success | Gives opening defense in war | After war or compact dissolution |

Use few ideas with staged upgrades. Do not create one idea for every incident.

## Focus tree interaction

Existing countries should keep their focus trees. If a member country uses a generic tree and the repository already has a safe additive focus hook pattern, the implementation can add optional crisis hooks that improve AI role behavior. The main design does not require a new focus tree for random pact members.

If additive focus hooks are added, they should be narrow:

| Hook | Use |
| --- | --- |
| Shadow conference focus hook | AI or generic-tree member can strengthen cohesion once |
| Public pact mobilization hook | Public member can support war readiness after reveal |
| Defector alignment hook | Defector can receive a small diplomatic payoff and remove member state |

Do not overwrite a meaningful national focus tree for a country selected by this event.

## Country package audit expectations

The country package auditor should verify:

- selected tags remain valid and alive
- public faction creation does not break existing factions in unsafe ways
- subjects and same-faction target countries cannot become invalid hidden enemies
- public member ideas and AI strategies clear after exit
- defector and isolated member states do not leave stale war-call exemptions
- localization exists for member ideas and dynamic country references
- assets for public pact identity exist before the reveal super-event is called

## Diplomacy integration

The compact changes relations through targeted opinion modifiers rather than permanent country identity changes.

| Relationship | Direction |
| --- | --- |
| Member to target | Worsens as commitment rises |
| Target to identified member | Worsens after proof or public reveal |
| Defector to target | Improves while protected |
| Member to defector | Worsens sharply |
| Observer to target | Can improve if evidence is strong |
| Observer to member | Can worsen after public exposure |
| Major patron to weak member | Improves if patron shields member, worsens if member defects |

## Military integration

Do not spawn large free armies for members simply because they joined the compact. Public members can receive planning, mobilization, or equipment support based on war readiness. Any unit or equipment grant should be dynamic, capped, and justified by the public compact phase.

Possible military effects:

- planning speed or coordination bonus at war opening
- limited infantry equipment transfer from major patron to weak members
- temporary defense on pact cores if target strikes first
- border state militia only if member is weak and neighbor to target
- no repeated free unit loops

## Defector integration

A defector is a country that exits the compact and provides evidence or public testimony. It should gain short-lived protection and diplomatic vulnerability.

Defector state should:

- remove hidden member behavior
- block automatic war conversion unless the defector later rejoins through a special failure
- give target evidence or member list progress
- create a retaliation chance from hardline pact members
- apply a temporary idea or opinion changes
- count toward achievements if the player used the evidence before public reveal or war
