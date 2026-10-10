# International Chaos Weapons Program

## Program promise

The program lets convention members open special projects that are normally reachable only through separate Chaos events.

It is shared research and investment, not an event bypass, a free weapon, or a substitute source event.
It opens only after Evolution III and the program Charter entering force.

## What a grant is

A grant opens access to the provider's native special project for one country.
The country must still research the project, pay its resources, and use the provider's own payload, delivery, accident, evidence, and Condemnation systems.

The repository already has the pattern: Event 016's Mengele clone directorate opens event-gated projects through country flags such as `directorate_special_project_weaponized_zombies_available` and `directorate_special_project_black_plague_available`, read by the `weaponize_the_zombies` visibility trigger and by `black_plague_weaponization_directorate_has_access`.
An Event 036 grant adds one provider-owned access flag read in the same place, so the source event never runs.

## Known candidates

The original concept named a Zombie Weapon and a Black Plague Weapon.
Current source shows two matching providers, which still need owner registration:

| Candidate | Special project | Source owner | Access trigger to extend | Global normal-route proof |
| --- | --- | --- | --- | --- |
| Black Plague Weapon | `black_plague_weaponization_program` | Event 020 weaponization | `black_plague_weaponization_directorate_has_access` | Event 020 has fired and released plague samples |
| Zombie Weapon | `weaponize_the_zombies` | Zombie outbreak and weaponized-zombie projects | `weaponize_the_zombies` `visible` block | `has_global_flag = has_zombie_outbreak` |

Implementation enumerates every other event-gated weapon project from source and registers only those whose owners supply the full contract.
Names, localisation, comments, unused assets, and planned documents never create a candidate.

## Provider contract

Each provider row, owned by the source system and read by Event 036, supplies:

| Field | Contract | If missing |
| --- | --- | --- |
| Project id | Stable script constant | Block registration |
| Display key | Owner localisation for the project name | Block selection |
| Source owner | Exact event or system | Block registration |
| Access flag | The country flag the grant sets and the project's access trigger reads | Block registration |
| Global normal-route proof | Read-only trigger that is true once the source route has opened the project to the world | Block registration |
| Participant trigger | Country-scope proof the country can use the project, including family limits such as no biological project for Chemical Accession | Skip that recipient |
| Contribution profile | Allowed families and any resource substitution | Use the defaults below |
| Target factor | `0.75` to `1.50` in a script constant | Use `1.00` |
| Cancellation call | One call to the Event 036 cancellation effect inside the transaction that makes the global proof true | Block registration |
| Condemnation mapping | The family relief that applies to the project's use contexts, or none | No relief |

A provider whose grant would fire, advance, or record its source event, or create its crises, countries, evolutions, world threats, super-events, terminal states, or narrative stages, is blocked.
The grant is narrower than the source event's reward.

Per-country routes that are not the global source route, such as the Mengele directorate or Event 016's Kruger program, do not cancel the program.
A recipient that already has access through them is skipped at completion.

## Equal selection

The candidate array is rebuilt from every registered provider that passes all of these:

- the Charter is in force
- the provider row is complete
- the global normal-route proof is false
- the project was not completed or cancelled by Event 036 before
- at least one current member passes the participant trigger

Each unique project id appears once, and selection is a uniform random index over the array.
No weight comes from AI strategy, ideology, war, technology, contribution capacity, project power, age, or earlier selection.
With one candidate it is selected, and with none the program becomes Dormant.

The selection records the candidate count, selected id, date, target, and project sequence number for debug evidence, never for player text.

## Lifecycle

The program is in one of four states:

| State | Meaning |
| --- | --- |
| Inactive | The Charter is not in force |
| Active | One project is selected and accepts contributions |
| Paused | The Charter's ratifiers fell below the Arsenal quorum, with or without a selected project |
| Dormant | No candidate is eligible |

Completion and cancellation are transactions that write a permanent history row, then return the program to selection after a 7 to 30 day interval.

## Progress

One global progress value runs against a target of `1000` internal units times the provider factor.

The player sees the percentage and a stage name: Organization, Experimental Work, Prototype Access, or Final Validation, at 0, 25, 50, and 75 percent.
Each stage change sends a short report to participants and adds no Chaos.

## Contributions

Only members passing the participant trigger can contribute, and public opponents never can.
Each country runs one contribution mission at a time, and each family has a 60-day country cooldown after its mission ends.

| Family | Mission | Default cost | Applied progress |
| --- | --- | --- | --- |
| Dedicate Industrial Capacity | 90 days | One to three civilian factories by economy size | `25` to `55` |
| Assign Research Teams | 90 days | Political power and a temporary research-speed penalty | `20` to `55` |
| Provide Specialist Equipment | Paid at start | One or two equipment types from the provider profile, debited through existing stockpile helpers | `20` to `50` |
| Host a Testing Facility | 120 days | Civilian factories and manpower, in a state with a native special-project facility | `35` to `60` |

Bounds keep the program shared:

- every paid contribution applies at least `20` units
- one contribution applies at most `60` units
- one country applies at most `12%` of the target per 90 days

Each mission writes one receipt with the project sequence, family, costs paid, and progress applied.
A receipt applies once across save and reload, and progress never exceeds the target.
Costs are never refunded by a later cancellation.

The country's share of the active project is internal, except that the header says whether the country has contributed and the Small State achievement reads the share.

## Completion

When progress reaches the target, one transaction:

1. hides contribution decisions
2. rechecks the global normal-route proof and runs cancellation instead if it is true
3. grants the access flag to every current member that contributed to this project and passes the participant trigger, skipping countries that already have access
4. records the completion, its recipients, and the Chaos outcome from [12](12_chaos_impact_and_cross_event_connections.md#event-owned-chaos)
5. clears active progress, participants, and decisions, and schedules the next selection

## Cancellation

The provider's normal-route transaction calls the Event 036 cancellation effect.
If that provider's project is active or paused, it freezes contributions, discards progress, keeps receipts as history, grants nothing, and schedules the next selection.
A provider becoming normally available while not selected is simply never selected.

A 30-day coordinator recheck of the selected provider's proof is a fail-safe for a missing call and reports the provider defect in debug evidence.

Cancellation adds no Chaos.

## Dormancy and wake-up

A Dormant program rechecks its candidates every 90 days through the coordinator and wakes at once when a provider registration or a membership change calls the wake-up effect.

## Quorum pause

While the Charter's ratifiers are below the Arsenal quorum, the program is Paused, contributions are hidden, and progress is kept.
It resumes when the quorum returns.
If the program stays Paused for 365 days, the Charter lapses, the project is cancelled with its progress discarded, and the program returns to Inactive until a later Charter agenda passes.

## Player-facing text

Selection text names the project and the work it needs without claiming its source incident occurred.
Completion text says participants can begin the project.
Cancellation text says the weapon appeared through another route and the shared work was abandoned.
Dormancy text says no unclaimed weapon program is within reach.
