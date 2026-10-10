# Asteroid Incoming, Part 10: Achievements and Acceptance

Status: five achievements implemented with final localisation and icon triplets; acceptance scenarios mostly await native verification by the user.

## Achievements

Achievements reward distinct play patterns, never the event merely firing.
Thresholds and holds are read from `asteroid_incoming_runtime`, and the native `_NAME`, `_DESC` and `_tooltip` text reads the same constants.

| Achievement | Play pattern | Conditions | Disqualifiers |
| --- | --- | --- | --- |
| Preserve the Near Miss (`asteroid_incoming_preserve_the_near_miss`) | Refuse the most dangerous form of the event | Choose the near miss when the opening reached 800 Chaos with both evolutions enabled | Manual or forced opening; an evolution disabled before the choice |
| Government Beyond the Crater (`asteroid_incoming_government_beyond_the_crater`) | Survive the loss of the capital and rebuild | Be the original target whose capital was the locked centre, relocate the government, and complete Reconnect the National Network and Restore the Outer Ring within 1,095 days of the impact while still holding the new capital | Not the original target; no relocation; annexed and recovered by another country |
| Collector of Fallen Stars (`asteroid_incoming_collector_of_fallen_stars`) | Assemble the largest armour advantage | Under Extraordinary Minerals, directly control the main crater and at least three fragment sites for 180 continuous days | Sites held by subjects do not count; any loss resets the hold |
| Piercing the Impossible (`asteroid_incoming_piercing_the_impossible`) | Break the strongest mineral advantage in war | Take the main crater from an enemy that held the main-crater armour bonus, while at war with it, and hold it for 30 days | Peaceful transfer or subject integration; a fragment site instead of the main crater |
| A World Reconnected (`asteroid_incoming_world_reconnected`) | Lead the world through severe dust without being the target | Not the original target; the opening stage was Impact Winter or worse; reach the Hardened tier, join the Observation Network and protect transport reserves while dust lasts; still hold that programme when the dust clears | A protection project that lapsed after the sky cleared |

Tracking rules:

- Progress uses persistent flags and start-day variables that survive save and reload, never a transient event target.
- The intended target stays distinct from the current crater controller, and an annexer never inherits original-target identity.
- Continuous holds reset on lost control or annexation.
- Monthly tracking runs from an `on_monthly` global-host block that is not gated by the Chaos Meter setting, starts only after a recorded strike, and visits only human-controlled countries.
- Recovery achievements depend on real mission success, and the conquest achievement on a hostile control change.

## Acceptance criteria

Each criterion points to the part that defines it; the status column reflects source state, not native observation.

| Area | Criterion | Part | Source status |
| --- | --- | --- | --- |
| Identity | Major, fire-once, Calm World baseline, default queue, `N/A` without a valid board | 1, 8 | Implemented |
| Board | Exactly three distinct pairs plus the near miss; no reroll on cancel or reload | 2 | Implemented |
| Lock | Fixed coordinate for two days; resolves without its chooser | 2 | Implemented |
| Capital | Relocation with fallback tiers and an honest no-relocation outcome | 2 | Implemented |
| Damage | 100/50/25/5 percent rings and 50/25/5 percent fragments, strongest profile once, across borders | 3, 5 | Implemented |
| Buildings | All buildings removed at the main centre | 3 | Blocked for the railway and supply network (README Open question 1) |
| Deaths | Actual losses recorded once under asteroid reasons | 3 | Implemented |
| Units | Location-based damage, no deletion | 3 | Implemented |
| Reports | One consolidated report per affected country | 3 | Implemented |
| Nuclear separation | No nuclear record, condemnation, retaliation, fallout, Chaos entry or Deaths reason | 3, 9 | Implemented in source |
| Dust | Destruction-based load, stages, Air Cleanliness slot, protection, capped mitigation, decay, clean closure | 4 | Implemented |
| Evolutions | Thresholds, toggles, honest fragment count, armour values, transfer without stale copies | 5 | Implemented |
| Decisions | Phase caps, at most four cost types, exact targets, blocked reasons, reserve floors, cleanup | 6 | Implemented |
| AI | Protected targets at zero, strong near-miss preference for ordinary peaceful AI, crater AI without abandoning survival | 7 | Implemented; scenarios partly evaluated |
| Presentation | Finished localisation, no raw keys or working labels, aligned super-event package, every DDS wired | 8, 9 | Implemented |
| Catalog | Row matches Event Details wording; CSVs regenerated | 8 | Implemented |

## Validation scenarios

The user runs native validation; agents never launch the game.
Results recorded so far are in the [named-save observations](../../plans/028_asteroid_incoming_plans/native_save_observations_20261007.md).

1. Baseline strike at low Chaos (one episode observed: population receipts reconciled exactly and ring membership matched the map).
2. Near miss at low Chaos.
3. Fragmentation at 600 to 699 Chaos.
4. Fragmentation plus minerals at 800 to 899 Chaos.
5. Six-fragment plan at 900 or more Chaos with a reduced valid pool.
6. Capital strike, including the no-relocation fallback.
7. Rings crossing into at least three countries.
8. Target annexed during the lock, and chooser annexed before confirmation.
9. Main and fragment ring overlap.
10. Main crater changing controller through war, and a fragment site through peace.
11. Save and reload during the lock, with a pending board, and during severe dust.
12. `N/A` in an invalid late-game world.
13. Nuclear systems unchanged after every visual, and map visuals retiring after 30 days.
14. Achievement holds surviving reload and resetting on lost control.
15. Main-crater railways, supply nodes and queued construction after impact (decides Open question 1).
16. News delivery order and no repeated forecast (L1), after which the temporary delivery counter is removed.

## Completion standard

The event is incomplete while any required path, profile, report, stage, evolution, decision phase, AI behaviour, asset, super-event component, achievement, log surface, document or catalog field is missing.
A smaller fallback must be reported and approved by the user before it can replace accepted design.
Proposed additions in this package are not completion requirements until accepted.
