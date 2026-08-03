# Event 016 launch-error patch handoff

## Files changed

- `common/decisions/016_brilliant_scientist_directorate_foreign.txt`
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
- `common/scripted_effects/chemical_warfare_effects.txt`

## Gameplay surfaces and identifiers

The three foreign-directorate `available` blocks now check `has_event_target = brilliant_scientist_foreign_actor` immediately before entering the actor scope for controlled access, joint laboratory, and host protection.

The malformed helper identifiers `brilliant_scientist_foreign_actor_can_receive_controlled_access`, `brilliant_scientist_foreign_actor_can_host_joint_laboratory`, and `brilliant_scientist_foreign_actor_can_offer_host_protection` were removed because they were only wrappers around the existing actor-scoped triggers and were not registered by the scripted-trigger parser.

The chemical tactic synchronization helper now uses `chem_gas_mask_preferred_tactic_suppression_synced` and `chem_shelling_preferred_tactic_suppression_synced` country flags as idempotence guards, setting each flag immediately after its matching hidden idea is added.

## Behavior before and after

Before the patch, the decision file called unregistered wrapper triggers, and the wrapper block caused parser mismatches around `has_event_target`, `event_target`, and nested scripted triggers.

After the patch, each decision guards the event-target scope inline and then evaluates the existing actor-scoped gate directly.

Before the patch, the chemical synchronization helper repeatedly evaluated the two hidden idea identifiers and produced empty `has_idea` validation errors during repeated startup or research callbacks.

After the patch, each grant is performed once per country through a dedicated country flag, while existing ideas remain the same and old saves gain the flags on the next synchronization call.

## Validation

The three touched script files have balanced braces with no underflow.

No malformed actor-wrapper references remain in the owned decision or scripted-trigger files.

Each of the three actor-scoped `available` blocks contains its own `has_event_target` guard.

No empty `has_idea` assignment remains in `chemical_warfare_effects.txt`.

Both hidden idea identifiers still resolve to definitions in `common/ideas/cbw_ideas.txt`.

The repository-wide game database validator and live Hearts of Iron IV session were not run because the task forbids launching the game and no standalone Clausewitz parser is available in the repository.

## Remaining risks and follow-up

The synchronization flags intentionally persist because the two hidden ideas have no removal call sites in the current repository.

If a later feature removes either hidden idea, its cleanup must also clear the matching synchronization flag before the helper is expected to grant the idea again.

No fallback mechanic or unrelated file change was introduced.
