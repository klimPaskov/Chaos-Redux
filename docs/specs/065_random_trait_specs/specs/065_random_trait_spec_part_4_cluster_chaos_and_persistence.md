# Event 065 Random Trait

## Part 4: Cluster, Chaos, Persistence, and Interactions

## Randomizations cluster membership

Event 65 belongs to the `Randomizations` cluster.

The cluster is a repeatable minor-event cluster at Chaos level `1`.

Event 65 has Medium member danger.

Its runtime role is optional.

The planned participation value is `60` percent.

The value should use a named cluster participation constant so it can be tuned without changing member logic.

The preferred constant name is:

`event_cluster_member_participation.random_trait`

The member should become eligible whenever Event 65 passes its own event-level rules and the Randomizations cluster passes its shared unlock rules.

The cluster must not add a stricter hidden gate than the supplied Chaos level.

## Cluster ID

The current cluster constant registry assigns IDs `1` through `8`.

The supplied cluster CSV also uses ID `10` for Intelligence and leaves ID `9` open.

The preferred new assignment is:

`event_cluster_id.randomizations = 9`

This assignment is conditional on a fresh collision audit at implementation time.

The authoritative XLSX and current source constants are the final authority.

If ID `9` has been assigned by then, the implementation agent must choose one unused ID and update every registry, selector, log mapping, setting, detail view, documentation page, and export together.

## Cluster execution

When Event 65 participates in a cluster firing:

1. The cluster member loader selects Event 65 once.
2. Member availability confirms that a valid registry exists and the world has at least one active country-leader role.
3. The member applies its optional participation roll.
4. A successful member invokes `chaosx.nr65.1` or the accepted shared executor effect once.
5. The Event 65 root performs the global mutation.
6. The cluster records one member outcome.
7. The shared event system records one global pacing event.

The cluster must not invoke Event 65 once per country.

The cluster must not add a second set of rolls after the direct Event 65 root has executed.

## Cluster ordering

Random Trait observes the world state that exists when its ordered member slot begins.

When an earlier member in the same Randomizations firing changes country leaders, Event 65 affects the new active leaders.

When a later member changes leaders, those new leaders wait for the next Event 65 firing.

This order dependence is intentional and should be documented in the cluster implementation.

The Event 65 member does not need to reserve states, countries, targets, or resources.

Its shared availability context is the registry validity and the existence of at least one eligible leader.

## Forced cluster behavior

The shared manual cluster debug path may force member execution according to the cluster framework.

A forced Event 65 member still requires a valid generated registry and at least one active leader.

The forced path bypasses the ordinary participation roll only when the shared cluster rules say a forced member should execute.

It uses the same trait logic and counters as the ordinary path.

## Direct Chaos map

Random Trait causes an abnormal global leadership mutation.

It therefore creates a direct Chaos source when a new intensity first succeeds.

The source is global and event-owned.

It does not scale per leader because doing so would create very large and farmable gains.

### One-time manifestation milestones

| Successful form first manifested | Direct Chaos gain |
| --- | ---: |
| Baseline | `+2` |
| Evolution I | `+3` |
| Evolution II | `+5` |
| Evolution III | `+8` |

A milestone requires at least one accepted trait addition.

A zero-result firing does not claim it.

Each milestone can be awarded once per campaign.

When the event first manifests at a higher form, it grants only that form's milestone.

Lower unmanifested milestones are marked bypassed so a later setting change or Chaos decline cannot award them retroactively.

When the campaign naturally experiences each form in order, the maximum Event 65 direct Chaos total is `18`.

## Chaos exclusions

Event 65 does not add Chaos for:

- reaching an Evolution threshold
- enabling an Evolution setting
- recording an Evolution
- opening or closing a report
- each leader processed
- each trait rolled
- a rejected collision
- a cluster participation skip
- a zero-result firing

Normal shared Chaos sources remain independent.

If a randomly granted trait later contributes to a war, annexation, deaths, nuclear use, contamination, or another already tracked consequence, the shared system owns that later Chaos.

Event 65 does not duplicate it.

## Persistence

The following state persists through save and load:

- highest manifested enabled Event 65 Evolution
- Evolution history
- Event 65 direct Chaos milestone flags
- bypassed lower milestone flags
- recipient-level source-trait grant ledger
- generated registry version expected by the save
- latest report data until overwritten
- cluster membership and cluster history through shared systems
- repeatable event weight and cap through shared systems

Temporary loop variables, candidate arrays, and debug scopes do not persist after their execution purpose ends.

## Leader lifecycle

A leader keeps Event 65 traits when the same recipient object:

- remains in office
- leaves office
- returns to office
- changes ideology role while preserving the same underlying role or character state
- moves to another country through a supported game route
- becomes an exile or returns from exile

The final behavior depends on engine role storage.

The implementation must verify that the Event 65 ledger follows the same recipient identity as the traits.

A new leader has a new ledger and receives no retroactive grants.

A copied or cloned character is a separate recipient unless the engine exposes it as the same role object.

## Removal by other systems

Event 65 never removes one of its grants.

Other game content may explicitly remove, replace, upgrade, or invalidate a source trait.

Event 65 does not run a maintenance loop to restore it.

The Event 65 ledger still remembers the source ID.

A future Random Trait firing therefore selects a different source trait for that recipient.

This preserves cumulative source variety without fighting the owning system.

## Country lifecycle

A country created after Event 65 fires waits for the next Event 65 firing.

A country annexed before the executor begins is not eligible.

A government in exile remains eligible when it still exists as a country and has an active leader.

A civil-war participant is eligible as its own country.

A subject is eligible.

A special Chaos Redux country is eligible when it has a valid active political leader.

A country that changes tag or cosmetic identity without changing the underlying country-leader role keeps the result normally.

## Content-profile changes

The generated registry is versioned.

When a game update or Chaos Redux update adds source traits, those traits become eligible after the registry is regenerated.

Old grants remain.

When a source trait is removed from the new build, the Event 65 ledger must preserve the old registry identity long enough to migrate or mark it as legacy.

The implementation must not reuse a retired numeric registry index for a different source trait.

Stable indexes are append-only inside a major registry version.

A deliberate compacting migration requires an explicit old-to-new map.

## DLC behavior

The registry records verified content conditions.

The implementation must test:

- no DLC
- each directly relevant DLC profile where trait definitions differ
- the full supported DLC set

When a trait definition remains loaded without its owning DLC, it stays eligible.

When the definition is absent or rejected without that DLC, its registry entry is gated out for that profile.

The event must not fail because a player lacks a DLC.

The report's pool count must reflect the active eligible registry, not a fixed full-DLC count.

## Interaction with leader changes

A trait grant can affect country modifiers or script checks immediately.

That may influence AI strategy, focus availability, decisions, advisors, or other content that checks the source trait.

The event does not suppress those interactions.

The implementation team should inspect high-risk route-specific traits for hard script defects.

A surprising route interaction is not automatically a defect.

A broken scope, infinite event loop, crash, save corruption, or deterministic desynchronization is a defect.

## Interaction with trait upgrade chains

Separate source IDs in an upgrade chain remain separate outcomes.

A leader can receive several versions when the source database permits them.

The event does not collapse them into one family.

The event does not choose the strongest version.

The event does not remove the weaker version.

This can create redundant or contradictory stacks and is intentional.

## Interaction with country leader replacement scripts

Some national content removes or replaces traits when a leader is upgraded.

That content remains authoritative for its own action.

Event 65 should not patch unrelated focus or event scripts merely to preserve every visible grant.

The grant ledger prevents repeated Event 65 selection of the same source identity.

## Balance role

Random Trait is a high-variance global event.

It can help or harm any country.

It should not attempt to equalize outcomes between the player and AI.

Every eligible leader uses the same pool and stage weights.

The player receives better visibility, not a better distribution.

The high-Evolution featured weighting raises the frequency of unusual results while keeping the maximum individual ratio bounded.

## Exploit controls

The player cannot select a trait, reroll a result, pay to remove a result, delay the world pass, or choose which countries are affected.

Debug forcing must be recorded and excluded from production validation.

Manual save reloading can alter random outcomes under normal game behavior.

Event 65 does not add a bespoke anti-reload system.

## Status lifecycle

The event remains disabled for normal campaigns while the rework is incomplete.

After source implementation, generated-registry validation, probability audit, asset validation, localisation audit, documentation alignment, automated checks, and completion audit pass, the catalog status can move to `Needs Testing`.

Only user-led in-game acceptance should move it to `Available`.

The implementation must not mark it available based only on source inspection.

## Workbook and export alignment

The authoritative workbook must receive:

- Event 65 baseline direction
- Evolution I direction
- Evolution II direction
- Evolution III direction
- Minor Repeatable type
- Chaos level `1`
- Randomizations cluster ID
- Medium member severity
- status transition supported by evidence

The Randomizations cluster row must receive:

- final numeric ID
- cluster name
- global randomization premise
- Event 65 membership
- repeatable minor type
- Chaos level `1`
- implementation status

The three CSV files are export snapshots.

They must be regenerated from the authoritative XLSX.

They must not be edited as the source of truth.
