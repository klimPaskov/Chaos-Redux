# Achievement implementation prompt: Event 061

Implement the three Event 61 achievements defined in Part 6.

Use the single Chaos Redux achievement registry and current project achievement conventions.

Read the Event 61 core, evolution, AI, balance, presentation, architecture, asset, and source-of-truth files before editing.

Inspect current vanilla and Chaos Redux achievement syntax and local project rules.

## Achievement 1

Internal key:

`chaosx_achievement_061_arsenal_reborn`

Working label:

`The Arsenal Returns`

Challenge:

A non-major player country is forced into Peacetime Economy and No Army, then restores at least Partial Mobilization and Limited Conscription, reopens every qualifying currently owned Event 61 ledger unit, fields at least 24 ordinary conventional divisions, remains independent, and completes the recovery within the tuned hard period.

Starting time target: 1,095 days.

Disqualify:

- Event 82 providing a qualifying law restoration
- Emergency Rearmament
- Emergency National Defence
- Black Market recovery shortcut
- subject status
- annexed replacement factories used in place of ledger restoration
- unapproved tag change
- debug setup

Track the qualifying cycle, forced-law date, ledger denominator, lost-state reconciliation, law milestones, division count, independence, and disqualifiers.

## Achievement 2

Internal key:

`chaosx_achievement_061_swords_ploughshares_swords`

Working label:

`Swords, Ploughshares, Swords`

Challenge:

The player accepts a meaningful Swords into Ploughshares liquidation, receives and uses a real Reconstruction Materials tier, then before the next Event 61 cycle restores a tuned share of the owned factory ledger, restores one economy law step, reaches Readiness 60, and wins a defensive war against a major.

Starting ledger target: 75 percent.

Disqualify:

- player starts the qualifying war
- Event 82 provides the law step
- Emergency Rearmament
- Emergency National Defence
- Black Market recovery shortcut
- subject status
- unapproved tag change
- debug setup

Track actual equipment value removed, benefit tier and duration, ledger denominator and restoration share, law milestone, Readiness milestone, war initiator, enemy-major status, and victory result.

Use a robust defensive-victory proof. Do not treat a white peace that leaves the player occupied or subject as victory.

## Achievement 3

Internal key:

`chaosx_achievement_061_arsenal_sleeps`

Working label:

`The Arsenal Sleeps`

Challenge:

A continental major with a foreign land border remains independent, outside every faction, under Peacetime Economy and No Army, with zero eligible conventional divisions, Stability at or above the tuned floor, and Chaos at 800 or higher for five continuous years.

Starting Stability floor: 70 percent.

Disqualify or reset for:

- leaving either extreme law
- fielding an eligible conventional division
- faction membership
- becoming a subject
- using Emergency National Defence or Emergency Rearmament
- creating a puppet or subject shield that violates the route
- unapproved tag change
- debug setup

A defensive war does not automatically fail the achievement when every sustained condition remains true.

Define how owner-excluded special units affect eligibility. Do not let hidden special units trivialize or silently block the challenge.

## Shared tracking rules

- player-only completion
- persistent save-safe variables and flags
- no daily whole-world achievement scan
- update through Event 61 actions, law changes, state changes, war outcomes, and bounded player checks
- record a stable qualifying cycle or start date
- preserve approved cosmetic tag continuity only through an explicit mapping
- reset continuous timers correctly
- recheck all final conditions at unlock
- block debug and force-trigger setup according to project policy

## Anti-exploit audit

Test:

- Event 82 shortcut
- emergency decisions
- annexation and state loss
- becoming and leaving subject status
- tag switch and cosmetic tag change
- save and reload at the unlock date
- division template spam
- special-unit classification
- white peace and defensive-victory ambiguity
- Chaos falling below 800 during the five-year timer
- faction entry for one day
- puppet shield creation
- repeated Event 61 cycle before completion

## Assets and localisation

Route the three final icons to `chaosx_icon_artist` using the achievement directions in Part 6 and the asset prompt.

Write final achievement names, descriptions, and requirement tooltips in-world.

Show reasonable disqualifying shortcuts to the player.

Keep internal flags and anti-cheat language out of final descriptions.

## Completion report

For each achievement report:

- final key
- icon path and sprite
- start condition
- persistent state
- completion condition
- time window
- reset behavior
- disqualifiers
- tag continuity
- state ownership handling
- unit classification
- test cases
- live result
- remaining blocker
