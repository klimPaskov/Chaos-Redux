# Boxer Rebellion

A revived Boxer movement challenges the people who govern China and the foreign powers that exercise authority within it.
Its first strongholds are local societies with different leaders, grievances, and relationships with nearby governments.
Some defend their districts against occupation, some attack civilians and foreign institutions, and some attempt to replace Chinese officials.
The player must decide which of those forces to confront, negotiate with, or support while a wider diplomatic crisis develops.

The movement can be defeated without an international war.
It can also become an auxiliary of a Chinese government, establish an independent government, provoke a multinational intervention, or help several Chinese rivals coordinate a successful withdrawal of foreign forces.
Those outcomes emerge from the campaign's actual governments, territory, military position, and decisions.

## Catalog identity

| Field | Value |
| --- | --- |
| Event ID | `069` in filenames and specification references |
| Existing runtime entry | `chaosx.nr69.1`, retained unless a separately reviewed migration proves necessary |
| Event name | Boxer Rebellion |
| Type | Minor Fire-Once |
| Current catalog status | To Be Reworked |
| Chaos level | 1 |
| Primary cluster | Domestic Unrest |
| Primary member severity | Severe |
| Additional cluster | Diplomacy |
| Additional member severity | Medium |

A large war does not reclassify the event into a second random major event.
The original firing remains one catalog occurrence and one timer beat.
The continuing crisis, its evolutions, and its aftermath belong to that occurrence.

## The player's main problem

A Chinese government must preserve authority without making the Boxers' claim of foreign dependence self-fulfilling.
Supporting the movement provides local fighters and political support, but also creates armed institutions that may refuse later orders.
Suppressing it can protect civilians and prevent intervention, but requires an actual security effort and a settlement with communities that supported the uprising.
Toleration buys time while making control less reliable.

A foreign government must decide which interests justify a commitment it can supply.
Rescuing nationals, protecting a concession, restoring a railway, defeating the movement, and imposing a punitive treaty are separate objectives.
A power can achieve its limited objective and leave while another member continues the conflict.

A playable Boxer government must turn local mobilization into a state that can feed its population, equip an army, and negotiate or fight for its independence.
It cannot solve those problems through an unlimited reserve of newly created militia.

## Two visible values

**Boxer Strength**, from 0 to 100, represents the movement's ability to coordinate, recruit, sustain strongholds, and challenge government authority across the active theater.
It does not represent the percentage of China controlled by the Boxers and does not directly multiply combat statistics.
Territorial control, equipment, manpower, and supply remain real requirements.

**Intervention Pressure**, from 0 to 100, represents the accumulated international crisis around the movement.
It measures political urgency, not a guaranteed probability of war.
Every foreign actor still evaluates its own exposure, objectives, capacity, existing wars, and diplomatic constraints.

There are no additional public event-specific meters.
Local organization, popular cooperation, ritual practice, government discipline, coalition disputes, and treaty compliance appear as qualitative statuses or specific objectives.
Ordinary game resources and existing shared crisis values remain visible in their own established interfaces.

| Value band | Boxer Strength meaning | Intervention Pressure meaning |
| --- | --- | --- |
| 0 to below 25 | Isolated circles or a defeated organization | Routine diplomatic concern |
| 25 to below 45 | Coordinated unrest and recruitment | Formal demands and evacuation planning |
| 45 to below 65 | Sustained armed organization | Ultimatums and serious intervention preparation |
| 65 to below 85 | A major movement with durable regional institutions | Competing intervention plans and a possible coalition |
| 85 to 100 | Strong coordination across the active movement | An acute crisis in which restraint requires a concrete settlement |

These are presentation bands, not automatic state-transfer or war-declaration triggers.
An active siege can justify a rescue at lower Pressure.
A distant power with no viable deployment route can refuse intervention at 100 Pressure.
A movement at 90 Strength can remain geographically small if China has successfully contained it.

## A crisis with distinct phases

| Phase | What is happening | Main choices | Exit conditions |
| --- | --- | --- | --- |
| Local emergence | Several districts report organized Boxer activity | Investigate, protect threatened people, choose a government stance | Containment, negotiated dispersal, or sustained mobilization |
| Armed mobilization | Societies acquire arms, coordinate actions, and challenge local authorities | Disarm networks, establish auxiliaries, protect routes, organize local defense | Territorial strongholds, a stable accommodation, or organizational defeat |
| Foreign crisis | Actual foreign interests are threatened and governments issue demands | Evacuate, negotiate, reinforce, authorize an expedition | A negotiated guarantee, withdrawal, or an intervention commitment |
| Intervention campaign | One or more powers pursue declared objectives | Defend corridors, relieve sites, counterattack, limit the mandate | Objective completion, operational failure, exhaustion, or settlement |
| Political settlement | Armed actors bargain over authority and foreign privileges | Demobilize, integrate, impose terms, refuse terms, or continue a limited dispute | A signed and executable agreement or a continuing war |
| Aftermath | Institutions and obligations survive the fighting | Reconstruct, enforce or revise terms, integrate societies, prevent renewed unrest | Expired obligations and stable institutions, or a bounded resurgence |

Phases can overlap between regions.
The global presentation follows the most important unresolved campaign question, while a selected region shows its own situation.
A ceasefire in one district does not erase an ongoing siege elsewhere.

## Natural opening

The source event needs a usable Chinese theater, at least two valid candidate states, and a credible grievance or institutional opening.
Foreign occupation, contested privileges, a foreign-backed government, recent defeat, or severe instability can supply that opening.
A stable, isolated China with no meaningful foreign relationship is normally a poor candidate.
The event must not manufacture a foreign mission, concession, or occupation simply to justify a random firing.

The opening chooses a small group of connected or regionally related centers, normally two to five states.
A larger map provides a larger candidate pool, not an immediate uprising in every state.
The selected centers determine the initial governments, foreign interests, and civilian protection problems.

The opening creates one major news event and a response event for each directly affected Chinese government.
Foreign governments receive a personal response only when they have a verified interest at risk.
Other countries receive news without a redundant decision popup.

The initial policy choice is free.
Later policy reversals have costs and a commitment period because they alter relationships already created by earlier actions.
The opening does not instantly remove millions of manpower, assign the movement a fixed ideology, or split a fixed share of every army.

## Proposed tuning anchors

All numbers in this package are authored starting targets for balance work, not tested results.
The implementation must centralize them and preserve their relationships when tuning.

A normal opening starts near 25 Boxer Strength and 15 Intervention Pressure.
Weak local authority, an active occupation, recent military defeat, and an existing supportive government can raise the opening, with a normal upper bound of 55 Strength and 40 Pressure.
An enabled evolved opening may have stronger institutions, but its army still requires the same material accounting.

A bounded theater update evaluates accumulated developments every 10 days.
It normally changes Strength by no more than 10 and Pressure by no more than 15 in either direction before discrete major incidents are applied.
Repeated reports of the same battle, siege, or government commitment must be coalesced into one development.
The update is an event-owned scheduled process over registered participants and states, not a new whole-world daily or weekly scan.

A security or diplomacy action normally changes a relevant public value by 5, 10, or 15 when it actually resolves a problem.
Clicking a preparatory button alone does not provide the full completion reward.
Important increases and reductions have a named cause, a target, and a receipt that prevents repeated collection.

## What counts as success

Containment requires the movement to lose the ability to sustain armed action and a local settlement to hold.
A low Strength value alone is insufficient while an armed stronghold remains active.

Boxer success requires a concrete achievement, such as continued lawful autonomy, removal of a foreign garrison, restoration of a concession, survival of an intervention, or establishment of a durable government.
High Strength alone is insufficient.

Foreign success is measured against the participant's declared mandate.
A rescued population or reopened evacuation route can satisfy a limited mandate without granting control over China.

A government may accept a mixed settlement.
It can suppress attacks on civilians, incorporate selected societies, and negotiate removal of a foreign privilege in the same outcome.
Those are compatible actions when the parties accept the terms and the military situation supports them.
