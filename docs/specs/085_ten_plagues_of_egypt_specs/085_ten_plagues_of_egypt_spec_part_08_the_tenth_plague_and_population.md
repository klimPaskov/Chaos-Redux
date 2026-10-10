# 8. Death of the Firstborn

## X. One night across the world

The tenth plague resolves once, for every state at the same deadline, at the end of Darkness.
It strikes firstborn people of all ages; it is never framed as killing only children.

In an unprepared first cycle it is the sequence's largest single mortality spike.
A well-protected country may lose fewer people that night than it lost to the storm, and that success stands.

The result removes real population from states, writes shared Deaths records, starts mourning and can kill eligible named characters.
No organization, manpower or description effect substitutes for the population loss.

## The firstborn share

Each state carries one hidden value: its **remaining firstborn share**.
It starts at 25% of the state's population when the state first faces a tenth plague in the campaign.
This is a game-balance abstraction, not a historical estimate of birth order.

- Other causes of death reduce population proportionally and leave the share unchanged.
- Migration does not move the share: arrivals take the destination state's share, and the origin keeps its own.
- After a tenth plague, the state's share falls by the fraction of its firstborn who died, so a later night in the same state finds fewer firstborn.
- The share persists after the episode, through controller changes and into any later legitimate episode; it is never reset except by a debug action, which invalidates survival achievements.

A younger sibling does not become firstborn when an older one dies, and no cycle regenerates the share.

## The formula

For a country with Divine Wrath `W`, the unprotected hazard is:

`h(W) = 0.10 + 0.85 × (W / 100)²`

The tenth-plague intensity is 1.00 at baseline, 1.10 under Evolution I and 1.25 under Evolutions II and III; scenario and recurrence multipliers (Parts 9 and 12) also apply.
The combined hazard is capped at 0.95 before protection.

For each state:

`deaths = population × remaining firstborn share × min(0.95, h(W) × intensity × recurrence) × Passover factor × network factor`

| Factor | Value |
| --- | ---: |
| Passover factor: Prepared | 0.05 |
| Passover factor: Partly prepared | 0.50 |
| Passover factor: Unprepared | 1.00 |
| Network factor: state with a completed earlier objective in a country with a working response network (Part 7) | 0.90 |
| Network factor: otherwise | 1.00 |

Low Wrath is valuable even without Passover, and Passover is decisive.
Extreme Wrath with no preparation kills a devastating share of the population.

### Example

A state of 1,000,000 people in its first cycle has a remaining share of 25%, so 250,000 firstborn.
At Wrath 50, `h = 0.3125`.
Unprepared, 78,125 die.
Prepared, 3,906 die; with the network factor, 3,516.
The same state at Wrath 90 unprepared loses about 197,000 (`h = 0.7885`).

## One transaction per state

At the deadline the coordinator freezes Wrath, intensity, Passover status and population for every state, then settles each state once with `apply_exact_state_civilian_population_loss`, which applies the protected population floor and logs the actual loss to Deaths under the Ten Plagues reason (Part 13).
Processing may run in batches, but the result is as if every state resolved at the same moment, and later choices cannot change it.
The state's firstborn share falls by the **applied** deaths, not the requested amount; any shortfall from the floor is discarded, never carried forward.
A state cannot be settled twice by save/load, a controller change or a repeated call.

Reports show applied deaths only, from the shared Deaths records.

## Named characters

Political leaders, heirs, generals, admirals, ministers and other supported characters can die if they are alive, hold a valid role and are established as firstborn.
For a real person that needs a reliable biographical source; for a fictional character it needs explicit metadata.
Unknown birth order is never guessed, and this package has established no eligible historical character.

A character's chance follows the Passover status of their country's capital state and the same hazard formula.
The character owner handles removal, vacancies and succession.
Killing a general does not delete their divisions, and killing a leader does not annex the country or start a civil war.
Named deaths are part of the demographic loss, not an extra civilian debit.

## Repeated cycles

Each later night finds a smaller firstborn share where earlier nights killed many.
Higher Wrath and intensity raise the hazard for the survivors but cannot kill people already dead, so later tenth-plague totals can fall even as the world-end grows harder to survive.
Storms, disease, hunger and lost services threaten the wider population between nights; the world-end needs no eleventh plague or replenished share.

Physical networks persist where intact, but each cycle's Darkness requires a new Passover; Passover status resets to Unprepared at each new Blood onset.

## A footprint that remains

Smaller populations, reduced firstborn shares, succession changes and shared casualty history remain after settlement.
No mourning decision or cleanup restores population.
