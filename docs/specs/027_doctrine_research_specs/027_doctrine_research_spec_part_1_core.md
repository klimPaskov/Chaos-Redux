# Event 027: Doctrine Research

## Catalog identity

| Field | Accepted specification |
| --- | --- |
| Event ID | `27` |
| Event name | Doctrine Research |
| Type | Minor Repeatable |
| Status during specification | To Be Reworked |
| Recommended minimum chaos level | Calm World |
| Cluster | National Breakthroughs |
| Recommended member severity | Medium |
| Main effect | Every valid country receives a doctrine-development batch. |
| Baseline batch size | One choice per country. |
| Maximum evolved batch size | Five choices per country at Evolution IV. |

## Event promise

Doctrine Research represents a worldwide burst of military learning. General staffs compare recent campaigns, translate captured manuals, rebuild field exercises, test new formations, and turn practical lessons into doctrine. The event gives every country a meaningful doctrinal choice without replacing normal combat mastery, military experience, faction sharing, focus rewards, or decision rewards.

The player decides how concentrated the breakthrough becomes. One country may finish a nearly complete armored track. Another may begin naval doctrine. A third may divide an evolved batch across infantry, operations, air, and naval tracks. The event remains understandable at baseline and gains depth through the number of choices. Unrelated crisis mechanics are outside its design.

The full ordinary event is complete at baseline. Evolutions increase the batch size. They do not replace the normal choice flow and do not create a separate doctrine system.

## Doctrine terminology

The current doctrine model distinguishes Grand Doctrines, tracks, subdoctrines, mastery levels, and Grand Doctrine Milestones.

For Event 027, the following terms are authoritative:

| Term | Meaning in this specification |
| --- | --- |
| Doctrine domain | One military doctrine family, such as Army, Navy, Air, an eligible Special Forces family, or Chaos Warfare. |
| Grand Doctrine | The high-level doctrine selected inside one domain. |
| Track | One category inside a Grand Doctrine. A track contains the subdoctrine choice for that category. |
| Subdoctrine | The selected branch inside a track. |
| Mastery level | One reward level inside the selected subdoctrine. |
| Event mastery step | Exactly one mastery-level advancement granted by one Event 027 choice. |
| Grand Doctrine Milestone | The native reward attached to completing a track. Event text must not call an ordinary mastery step a Milestone. |
| Batch | All choices granted to one country by one firing of Event 027. |

The rough input uses `mastery milestone` for the repeated reward. The implementation and player-facing text should use `mastery level` or `mastery step` so the reward does not collide with the doctrine interface's separate Milestone concept.

## Domain-scoped interpretation

Each country can have doctrine state in several military domains. A country may have an Army Grand Doctrine while lacking a Navy Grand Doctrine. The event therefore evaluates doctrine adoption inside the domain selected for the current choice.

A single choice follows this rule:

1. The country selects one valid doctrine domain.
2. If that domain has no active Grand Doctrine, the country selects and adopts one eligible Grand Doctrine in that domain.
3. Grand Doctrine adoption consumes the choice and grants no event mastery step.
4. If that domain already has an active Grand Doctrine, the country selects one eligible track and advances its selected subdoctrine by one mastery level.
5. If the chosen track has no selected subdoctrine, the country selects one eligible subdoctrine for that track and receives the first event mastery step in the same choice.

This interpretation preserves the user's explicit rule that adopting the high-level doctrine consumes one choice without mastery. It also lets a country develop several military services over repeated firings instead of treating the first Grand Doctrine selected anywhere as the only doctrine it can ever adopt through the event.

## Baseline firing

At baseline, one random-event firing grants one choice to every valid country in the firing snapshot.

For a country with at least one active Grand Doctrine and one eligible subdoctrine track, that choice can advance exactly one mastery level.

For a country that selects a domain with no Grand Doctrine, that choice can adopt one eligible Grand Doctrine in that domain. It receives no event mastery step from that choice.

For a country with several valid domains, the country chooses the domain. The event does not force Army doctrine merely because Army is the most common military domain.

For a country with no valid doctrine options in any registered domain, the batch resolves without a substitute reward. A human country receives a concise closure report that explains that no eligible curriculum remains. An AI country closes the batch silently.

## Country participation snapshot

The participant set is fixed when Event 027 fires.

A country belongs to the participant set when all of the following are true at the snapshot:

- the country exists as a live country scope
- the country is not an observer, placeholder carrier, or invalid system scope
- at least one registered doctrine domain can produce a valid adoption or mastery option for that country
- the country's doctrine state can be read and changed safely through the verified domain adapter

Countries created after the snapshot receive no retroactive batch. They become eligible at the next normal firing.

A country that disappears before resolving its batch loses the unresolved batch. Unused choices do not transfer to its annexer, overlord, civil-war opponent, successor, or liberator.

A government that still exists in exile remains eligible if its doctrine state and event scope remain valid. A cosmetic tag, ideology change, puppet status change, faction change, or leadership change does not erase the batch.

A civil war that begins after the snapshot does not duplicate the original batch. The country that owned the batch retains it when that scope remains valid. The newly created side waits for a later Event 027 firing.

## Valid country families

Ordinary countries, subjects, governments in exile, event-created human countries, and special Chaos countries may participate when they have a valid doctrine adapter.

Special and nonhuman countries are not excluded by identity alone. Their participation depends on whether the owning event or system gives them a coherent doctrine domain and a safe mastery contract. A plague state with no normal doctrine system receives no fabricated Army doctrine. A Kruger sovereignty with a valid normal or custom doctrine graph may participate through that graph.

The event must never invent a generic human doctrine package for a special country merely to satisfy global coverage.

## Choice costs

Event 027 represents the breakthrough itself. Grand Doctrine adoption and subdoctrine adoption performed through the event do not charge the normal military-experience purchase cost.

The choice also does not provide a refund. A country that previously spent experience on doctrine receives no compensation.

The event grants no Army, Navy, or Air experience. It grants no research bonus, technology, political power, command power, equipment, unit, spirit, or generic modifier alongside the doctrine result.

Normal doctrine prerequisites, DLC ownership, branch eligibility, mutual exclusions, domain availability, and custom system gates continue to apply. The event waives the purchase cost for the selected valid doctrine action. It does not waive the existence and validity of that action.

## Grand Doctrine adoption

When the selected domain lacks a Grand Doctrine, the country chooses among the Grand Doctrines that are currently eligible in that domain.

Adoption has these consequences:

- the selected Grand Doctrine becomes active through the native doctrine system
- the current Event 027 choice is consumed
- no event mastery step is granted
- no track or subdoctrine is selected automatically
- no other domain is changed
- no existing doctrine progress in another domain is removed
- normal immediate bonuses from Grand Doctrine adoption apply through the native system

The event never replaces an existing Grand Doctrine. A domain with an active Grand Doctrine proceeds to track development. Doctrine replacement, refund, reset, or late-game respecialization remains owned by the native doctrine system and other explicit content.

## Subdoctrine and mastery development

When the selected domain already has a Grand Doctrine, the country sees every track that can produce a valid event mastery step.

A track is valid when one of these states applies:

- it has a selected subdoctrine below its maximum mastery level
- it has no selected subdoctrine and at least one eligible subdoctrine can be selected

A selected subdoctrine at maximum mastery is not a valid target. A track with no eligible subdoctrine is not a valid target.

If a track has an active subdoctrine, one successful choice advances that branch by exactly one event mastery step.

If a track is empty, the country first chooses one eligible subdoctrine for that track. The event then grants the first event mastery step to that branch as part of the same choice. The normal subdoctrine purchase cost is waived.

The event never changes a selected subdoctrine to a different branch. A country that wants to replace a branch uses the native replacement rules outside Event 027.

## Banked mastery

Native doctrine mastery can be banked before a subdoctrine is selected or after a branch is completed. Event 027 preserves that banked mastery.

The event must resolve the country's current native state at the moment the final choice is confirmed. If selecting a subdoctrine causes banked mastery to unlock one or more native levels, those levels remain valid native progress. The event then applies one additional event mastery step when another level remains.

If banked mastery or another effect completes the selected branch before the event grant is applied, the choice returns to the valid-target selection without consuming a choice.

The event must not delete, cap, convert, or temporarily hide banked mastery to force the visible result to look like a one-level increase. Achievement tracking distinguishes event-attributed choices from native banked progress.

## Exact advancement rule

One successful choice consumes one choice and produces one of two event-attributed results:

- one Grand Doctrine adoption with zero event mastery steps
- one event mastery step in one valid subdoctrine branch

The event must not use a flat mastery-point amount that can cross an unknown number of thresholds. The implementation needs a verified doctrine operation that targets the next mastery level or calculates the exact amount required for one level without spilling into another event-attributed level.

Branches may have a different number of levels. Five choices do not imply that every modded branch has five levels. A branch with fewer remaining levels becomes invalid when complete, and the country redirects later choices. A branch with more than five levels receives at most one level per choice.

## Choice consumption

A choice is consumed only after a valid doctrine action succeeds.

The following actions never consume a choice:

- opening a domain page
- opening a track page
- returning to a prior page
- selecting an option that became invalid before resolution
- reaching an unsupported doctrine adapter
- encountering a missing DLC gate
- finding that another effect completed the branch while the event was open
- closing a batch because the country has no valid options

A failed doctrine action returns the country to the nearest valid selection page and preserves the remaining choice count.

## Stacking and distribution

Every choice in an evolved batch is independent.

A country may spend all choices on one branch until that branch is complete. It may divide choices among tracks in one Grand Doctrine. It may divide choices among Army, Navy, Air, supported Special Forces content, Chaos Warfare, and future registered domains.

Grand Doctrine adoption can be followed by mastery in the same domain when the batch has another choice. Evolution I therefore enables a country with no doctrine in the selected domain to adopt a Grand Doctrine with its first choice and begin one subdoctrine with its second.

The event does not impose a diversity quota or stacking cap on the player.

## Batch snapshot

Each country batch stores the following design facts when Event 027 fires:

- the batch identity
- the evolution stage used for the batch
- the total number of choices
- the remaining number of choices
- the country that owns the batch
- the firing date
- achievement tracking for choices made inside that batch

Doctrine options are not snapshotted. They are rebuilt before each choice so combat mastery, DLC state, focus rewards, custom-system changes, branch completion, and other doctrine effects are respected.

The batch size is snapshotted. An evolution that unlocks while a country is resolving a batch does not add choices to that batch.

## Repeat firing and queue behavior

Event 027 is repeatable and uses the shared repeatable-event weight system. Later firings may occur while one or more countries still hold unresolved choices, especially in multiplayer or after control changes.

Each country can have one active batch and an ordered queue of later batches.

When Event 027 fires for a country that already has an active batch:

- the new batch is appended after the active batch
- its own size and evolution stage are preserved
- the active batch is not overwritten
- the batches are not merged
- achievement tracking remains separate per batch
- the queued batch begins when the prior batch closes

A batch that reaches zero remaining choices closes immediately. A batch that has no valid doctrine options also closes. The next queued batch then begins and rechecks the country's current doctrine state.

Repeatable weight recovery and cap reduction remain shared Event 027 behavior. The batch queue does not alter event weight, timer acceleration, major-event gain, or cluster pacing.

## Save, reload, and control changes

Active and queued batches must survive save and reload.

A change between human and AI control does not erase doctrine choices. The current controller resolves the remaining choices. When a country becomes AI-controlled, the AI uses the same valid pool and finishes the active batch through a bounded continuation path. When a country becomes human-controlled, the next unresolved choice opens for that player.

Tag switching must not redirect one country's choices into another country's doctrine state. The country owns the batch, and the current player tag only determines which human sees its next page.

## Multiplayer behavior

One Event 027 firing is global. Every human country in the participant snapshot receives its own independent chain, and every AI country resolves its own batch.

One player cannot consume, delay, redirect, or overwrite another player's choices. A player who resolves quickly does not advance another player's chain.

The random-event history records one Event 027 firing for the world. It does not record one random event per human player.

The event must avoid a shared global `remaining_choices` value. Every country's active batch and queue are country-owned.

## Event history and evolution memory

The canonical Event 027 entry event creates one global History row with no country actor. The row describes a worldwide doctrine-development wave.

Country selection pages and AI resolution events do not create extra History rows.

Evolution unlocks create global evolution records with no country actor. The evolution record identifies the Event 027 stage and its increased batch size. Ordinary choices inside a batch are not evolution records.

Event Details should explain the event premise and current evolution stage without listing raw variables, internal queues, or hidden AI scores.

## Connection with native doctrine sharing

Native faction doctrine sharing, mastery from combat, training, attachés, focus rewards, decision rewards, and other doctrine sources remain active.

An Event 027 choice can make a country newly eligible to share or receive doctrine progress through native faction systems. Those native consequences are allowed. Event 027 must not duplicate the sharing reward, suppress it, or claim the secondary progress as another Event 027 choice.

## Connection with Chaos Warfare

Chaos Warfare is a conditional custom Grand Doctrine with four visible mastery tracks:

- Hazard Assault Formations
- Toxic Armored Warfare
- Contaminant Fire Support
- Integrated CBRN Command

Event 027 may advance these tracks only through the verified Chaos Warfare adapter. Grand Doctrine establishment requirements, fielded formation requirements, technology gates, equipment gates, use-policy gates, readiness caps, operation gates, and doctrine visibility rules remain owned by Chaos Warfare.

The event cannot activate Chaos Warfare for a country that fails its Grand Doctrine eligibility. It cannot grant a blocked custom unit, equipment type, operation, or policy by directly setting a downstream mastery reward.

One mastery step must use the same route that the Chaos Warfare system recognizes for its institutional state, ideas, operation eligibility, AI, documentation, and any Condemnation multiplier.

## Connection with other events

Event 027 remains distinct from other National Breakthroughs members.

Event 085 may grant military experience that countries later spend through normal doctrine actions. Event 027 grants direct event choices and does not convert itself into experience.

Event 089 concerns doctrine or technology sharing and requires its own rework. Event 027 does not absorb that event's concept, spread a fixed doctrine to every country, or assume Event 089 is implemented.

Events that create countries, transform countries, or unlock custom doctrine families affect future Event 027 firings through the normal participant snapshot and adapter registry. They do not receive retroactive batches from a firing that occurred before the country or adapter existed.

## Baseline completion condition

The baseline event is complete when every country in the participant snapshot has resolved or closed its one-choice batch.

The global random-event system does not wait for every human popup before scheduling the next event. Country batches persist independently through the queue contract.

The event has no persistent crisis state after all batches close. Its campaign memory consists of repeatable-event state, fired history, evolution stage, achievement records, and the permanent doctrine progress created through the native and custom doctrine systems.
