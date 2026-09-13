# Event 54 Achievement Prompt

Implement the two achievements defined in the Event 54 presentation specification. Read the full specification, `AGENTS.md`, the events and event-assets skills, the installed vanilla achievement documentation and precedents, and the current Chaos Redux achievement registry before editing.

Keep event-owned achievement entries grouped inside the single Chaos Redux achievement registry. Use exact final IDs for their root-level DDS triplets. Coordinate final icon production through the Event 54 asset prompt.

## Complete the Chain

Working ID: `chaosx_achievement_054_complete_the_chain`

Eligibility requires a player country that began the campaign with three or fewer research slots.

A qualifying Event 54 firing must grant a conventional technology at least three years ahead of the current date. At grant time, its transitive prerequisite ancestry must contain at least three missing ordinary prerequisite technologies.

Record the recipient, granted technology, exact missing prerequisite set, grant date, and a 730-day deadline. The player must research every stored prerequisite through normal research before the deadline.

Disqualify the tracked attempt when any missing prerequisite is granted by Event 54, another event, an owner callback, setup logic, or a debug route. Also disqualify it if the recipient becomes a subject, is annexed, is replaced, or the tracked graph state becomes invalid.

Researching a node normally removes only that node from the stored set. Unlock when the set becomes empty before the deadline and every stored completion has normal research proof.

If several Event 54 technologies could qualify, use one deterministic bounded selection rule and document it. The rule cannot reroll until it finds an easier chain.

## Borrowed Future

Working ID: `chaosx_achievement_054_borrowed_future`

This hidden achievement requires one independent player country to receive registered Event 54 technologies from two distinct owner providers in the same campaign.

At each grant, the owner must not have delivered its normal primary reward to that country. Store provider identity, candidate identity, grant date, owner reward state, and recipient.

Each owner can expose one bounded public use-milestone callback for the granted technology. A callback records meaningful gameplay use and cannot unlock the achievement by itself. Debug, setup, or grant-time callbacks cannot satisfy use.

After both distinct provider grants and both use milestones, the player must remain independent until global Chaos reaches 800. Becoming a subject, losing the original country, receiving both grants from one provider, or discovering that an owner reward had already been delivered invalidates the run.

Fail closed until at least two implemented providers expose the complete eligibility, grant, lifecycle, and use-milestone contract. Do not invent a second provider or weaken the condition to make the achievement available.

## Shared requirements

- Give each achievement complete visible or hidden state behavior as specified.
- Add final localization written in the project style.
- Implement all tracking flags, variables, arrays, on-action hooks, migration, and cleanup needed for reliable save behavior.
- Keep tracking bounded to active player attempts. Avoid a new broad daily or monthly country scan.
- Prevent tag switching, subject release, event grants, debug setup, and repeated Event 54 firings from bypassing the rules.
- Document every unlock condition, disqualifier, icon path, tracking state, and test case.
- Run source checks and save-reload tests before completion.

Use the exact achievement icon package produced from the asset prompt. A missing final triplet blocks the achievement from completion.
