# Event 027: Doctrine Research

## Part 1: Core rules

Status markers used in this package: **implemented** means the rule exists in the current source and is described in `docs/events/027_doctrine_research/overview.md`, **pending** means the rule is accepted or proposed but not yet in source, and **live check** means the source exists but depends on engine behaviour that only a live session can confirm.
The README holds the acceptance basis for each status.

## Catalog identity

| Field | Specification |
| --- | --- |
| Event ID | `27` |
| Event name | Doctrine Research |
| Entry event | `chaosx.nr27.1` (console bridge); ordinary dispatch calls the firing transaction directly |
| Type | Minor Repeatable |
| Minimum chaos level | Calm World |
| Cluster | National Breakthroughs (cluster `9`, runtime member row `9001`) |
| Member severity | Medium |
| Main effect | Every valid country receives a doctrine curriculum of one to five choices. |
| Baseline curriculum size | One choice per country. |
| Maximum curriculum size | Five choices per country at Evolution IV. |

## Event promise

Doctrine Research represents a worldwide burst of military learning.
General staffs compare recent campaigns, translate captured manuals, rebuild field exercises, and turn practical lessons into doctrine.
Every country receives a doctrinal choice that sits beside, and never replaces, combat mastery, military experience, faction sharing, focus rewards, or decision rewards.

The player decides how concentrated the breakthrough becomes.
One country finishes a nearly complete armored track, another establishes its first naval doctrine, and a third spreads an evolved curriculum across infantry, operations, air, and naval tracks.
The baseline event is complete on its own, and evolutions only increase the number of choices.

## Terminology

| Term | Meaning |
| --- | --- |
| Doctrine domain | One entry in the Event 027 domain menu: Army, Navy, Air, Special Forces, or Chaos Warfare. A domain maps to one native doctrine folder plus the Grand Doctrines it offers. |
| Grand Doctrine | The high-level doctrine selected inside one native folder. |
| Track | One category inside a Grand Doctrine that holds one selected subdoctrine. |
| Subdoctrine | The selected branch inside a track. |
| Mastery level | One native reward level inside a subdoctrine. |
| Mastery step | Exactly one mastery level granted by one Event 027 choice. |
| Grand Doctrine Milestone | The native reward attached to completing a track. A mastery step is never called a Milestone. |
| Curriculum | The player-facing name for all choices one firing grants to one country. Script and documentation call it a batch. |

Player-facing text uses curriculum, choice, mastery level, and Milestone.
It never uses batch, receipt, adapter, or queue.

## One choice

1. The country selects one valid doctrine domain.
2. If the domain's native folder has no active Grand Doctrine, the country adopts one eligible Grand Doctrine. Adoption spends the choice and grants no mastery step.
3. If the domain has an active Grand Doctrine, the country selects one track that can still advance and gains one mastery step in its subdoctrine.
4. If that track is empty, the country first selects one eligible subdoctrine for it and receives the first mastery step in the same choice.

Rule 2 is the user's explicit brief: adopting the high-level doctrine consumes one choice without mastery.
Domain scoping lets a country with an Army doctrine still adopt a Navy doctrine through a later choice or firing.
All four steps are **implemented**; the empty-track assignment and its banked-mastery readback are a **live check**.

### Army and Chaos Warfare share one native folder

Chaos Warfare is a native Grand Doctrine in the `land` folder, so it is an alternative to the Army Grand Doctrines and never coexists with one.
The domain menu lists Army and Chaos Warfare as separate entries so the player can see the CBRN option, but both offer adoption only while the `land` folder is empty, and only one of them can offer mastery at a time.
Chaos Warfare uses the four Army tracks, and each track holds one Chaos Warfare subdoctrine:

| Track | Chaos Warfare subdoctrine | Compatibility ID |
| --- | --- | --- |
| Infantry | Hazard Assault Formations | `extermination_columns` |
| Armor | Toxic Armored Warfare | `chemical_suppression` |
| Combat Support | Contaminant Fire Support | `contaminant_firebases` |
| Operations | Integrated CBRN Command | `integrated_chemical_operations` |

## Costs and compensation

Event 027 waives the normal experience cost of the doctrine action it performs.
It grants no refund for earlier spending and no experience, research bonus, technology, political power, command power, equipment, unit, spirit, or generic modifier.
Native prerequisites, DLC ownership, mutual exclusions, and owner-system gates still apply.
A country with no valid action receives no substitute reward, because compensation would favour the countries that already finished the most doctrine content.

## Grand Doctrine adoption

Adoption activates the selected Grand Doctrine through the native doctrine system, spends one choice, grants no mastery step, selects no track automatically, and changes no other folder.
The event never replaces an active Grand Doctrine and never changes a selected subdoctrine to a different branch.
Replacement and respecialisation stay with the native doctrine screen.

## Mastery steps

A track can receive a mastery step when it holds a subdoctrine below its maximum level, or when it is empty and at least one subdoctrine can be selected for it.
One successful mastery choice advances exactly one level, whatever the branch's level count or mastery-point thresholds.
Branches with fewer than five levels simply leave the pool earlier, and branches with more levels still receive one level per choice.

The implementation reaches exactly the next level by granting mastery one point at a time and re-reading the level, with a guard scaled to the level's reward cost and the country's mastery gain factors (**implemented**, **live check** for same-effect readback).
The overview owns the exact guard values.

### Banked mastery

Native mastery can be banked on an empty track or a completed branch.
Event 027 never deletes, caps, or hides banked mastery.
When assigning a subdoctrine resolves banked levels, those levels stay native progress and the event then adds one step if a level remains.
When the bank completes the branch on assignment, the assignment stands, no choice is spent, and the player is told that stored mastery finished the branch (**implemented** as page `.13`).
Achievements count only event-attributed steps.

## Choice consumption

A choice is spent only after its doctrine action succeeds.
Navigation, pagination, a target that became invalid, an unsupported domain, and a branch completed by another source while the page was open never spend a choice.
A failed action returns the country to the nearest rebuilt page with its remaining choices intact.

## Stacking and distribution

Every choice is independent.
A country may stack choices on one branch until it completes, divide them among tracks, or spread them across domains.
A Grand Doctrine adopted by one choice is active for the next, so Evolution I is the first stage where a country can establish a doctrine and begin its first track in one curriculum.
The event imposes no diversity quota and no stacking cap.

## Participation

The participant set is fixed when the event fires.
A country participates while it exists as a live country or government in exile, has a doctrine system, and has at least one valid doctrine action (**implemented**).

A country has a doctrine system unless the shared `is_actual_nonhuman_country` classifier marks it, so zombie outbreaks, plague rat states, Death, and similar nonhuman powers receive nothing and no fabricated doctrine.
A Kruger sovereignty keeps its doctrine graph even when its population is no longer human.
A future special country joins only by registering a complete custom adapter (see the registry matrix).

Countries created after a firing receive nothing from it and join the next firing.
A country that disappears loses its unused choices, which never transfer to an annexer, overlord, successor, civil-war opponent, or liberator.
Subject, puppet, ideology, cosmetic tag, faction, leadership, and controller changes never erase a curriculum.
A civil war after the snapshot leaves the original curriculum with the original country, and the new side waits for the next firing.

## Curriculum snapshot and queue

Each curriculum stores its identity, owner, firing date, evolution stage, total and remaining choices, the domains that were empty when it began, and its achievement evidence.
Its size never changes after creation, so an evolution that unlocks mid-curriculum affects only later firings.
Doctrine options are rebuilt before every choice so combat mastery, faction sharing, focuses, DLC state, and owner-system changes are respected.

A country holds one active curriculum and an ordered queue of later ones.
A later firing appends a separate curriculum with its own size and stage, never merging into or overwriting the active one.
When a curriculum closes, the next queued one starts and rechecks the country's doctrine state.
All of this is **implemented**, including compaction of closed rows so ledger scans stay bounded.

## Persistence and control changes

Active and queued curricula survive save and reload.
A one-time transaction receipt prevents a duplicate effect after reload, a double click, or a delayed continuation; a pending receipt is recovered only by its exact identity and otherwise fails closed (**implemented**, **live check** across save and reload).

The current controller resolves remaining choices.
An AI resolves its curriculum silently, a human receives the next page, and a tag switch never redirects one country's choices into another country's doctrine.
Lifecycle callbacks reconcile only countries with pending work (**implemented**).

## Multiplayer

One firing is global.
Every human receives an independent chain, no player can consume or delay another country's choices, and all curriculum state is country-owned.

## Event history and evolution memory

Each firing records one actorless History row whose detail states the curriculum size of that firing.
Choice pages and AI resolution record nothing further.
Evolution promotions record one actorless evolution row each.
Event Details explains the premise and the stage previews without raw variables, queues, or AI scores.

## Connections with other systems

### Native doctrine progress

Combat mastery, training, attachés, faction sharing, focus rewards, and decision rewards stay active.
An Event 027 step can change what native faction sharing later passes on; Event 027 neither duplicates nor suppresses that, and never counts it as its own step.

### Chaos Warfare

Event 027 can establish Chaos Warfare only when the owning establishment gate (`cbrn_chaos_warfare_adoption_capable`) holds, and it advances Chaos Warfare tracks only through native mastery.
Native mastery runs the reward effects in the Chaos Warfare subdoctrine files, so every institutional flag, technology grant, and operation gate the CBRN system reads updates exactly as it would from combat mastery.
Event 027 never grants a downstream CBRN unit, equipment type, policy, operation, idea, or readiness value directly, and a mastery level can be earned while a separate downstream gate stays unmet.

Adopting Chaos Warfare has a real cost beyond the CBRN programme: the Chaos Meter's combat collateral model adds a civilian-death rate for countries with `chaos_warfare` at war, which feeds the Deaths ledger.
Revision R4 in part 2 makes that consequence visible on the adoption choice.

### Event 016 Brilliant Scientist

A successful adoption calls `brilliant_scientist_record_doctrine_research`, which records the decision once in an active Kruger host's policy history (**implemented**).

### National Breakthroughs members

Event 085 grants military experience that countries spend through the native screen; Event 027 never converts itself into experience and never scales Event 085.
Event 089 owns doctrine sharing after its own rework; Event 027 does not absorb that concept or call it.
Events that create countries or unlock custom doctrine families affect only later firings.

## Completion of one firing

A firing is resolved when every participant has spent or closed its curriculum.
The random-event system never waits for human pages, and the event leaves no crisis state behind.
Its campaign memory is the repeatable-event state, History rows, evolution stage, achievement records, and the permanent doctrine progress it created.
