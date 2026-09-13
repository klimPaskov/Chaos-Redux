# Event 046: The Great Shuffle

## Catalog identity

- Event ID: `46`
- Event name: The Great Shuffle
- Replaces: Seismic Archive
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: `1`
- Cluster: Randomizations
- Member severity: Medium

## Playable promise

The Great Shuffle rewrites large parts of the current campaign without treating any previous arrangement as correct.

A firing can turn a stable government into a political wreck, fill one country with fuel while emptying another, remake the population and industry of the map, alter armies and research, and eventually surrender registered event mechanics and selected structural relationships to the same process.

The result is a new world state, not a temporary modifier package.

The player is asked to understand what changed and adapt to it.

The player does not manage a Shuffle meter, choose a target, purchase protection, or restore a saved world.

## Core invariants

### Every firing is standalone

Each firing begins from a fresh family roll and a fresh set of random result plans.

Earlier Great Shuffles do not create a source pool, preferred distribution, compensation debt, protection state, pity rule, cooldown preference, or target memory for later shuffles.

A family touched in the previous firing can be selected again immediately.

A country that suffered before receives no favorable weighting.

A country that benefited before receives no punitive weighting.

The event system can retain its ordinary repeatable fired count, weight, cap, history, and evolution state.

Those framework facts never affect which value a country or state receives.

### Values are generated, not exchanged

The event does not swap values between countries or states.

It does not redistribute the total equipment, population, factories, fuel, influence, or other material that existed before the firing.

Each valid scope receives a newly generated result from the selected family's current legal range.

World totals may rise, fall, or remain similar by chance.

Conservation is used only where an engine contract requires it for legality.

### Results are permanent

The event stores before values only long enough to validate the transaction and build reports.

There is no restoration timer, return mission, compensation event, hidden equilibrium, or later cleanup that restores the pre-shuffle world.

A value can later change through ordinary play or another Great Shuffle.

Permanent means that Event 46 never reverses its own result merely because time passed.

### There is no proper value

The event never asks whether a country deserves a certain stockpile, whether a state should be populous, or whether an army's experience looks sensible.

The only general tests are legal scope, legal value, compatibility, protected-state safety, and a completed reconciliation contract.

Absurd outcomes are valid when the engine and owning mechanic remain coherent.

### Gameplay state can be shuffled

The event uses an explicit allowlist of gameplay surfaces.

A value is unavailable until its owner proves that Event 46 can identify the correct scope, generate a legal result, apply it without corrupting identity, reconcile dependent state, and report the result.

The event never discovers variables in memory and never assumes that an undocumented number is safe.

### Framework state cannot be shuffled

The event system, Chaos Meter, one-way historical ledgers, stable identities, registries, arrays, indexes, lifecycle proof, settings, and Event 46's own transaction data remain protected.

The protected layer is defined in Part 4 and the classification matrix.

## Global firing scope

One Great Shuffle firing is one global transaction.

The event resolves every selected family against all valid scopes in that family.

Country families operate across valid countries.

State families operate across valid states.

Unit families operate across valid units.

Commander families operate across valid commanders.

Production families operate across valid production objects without changing their stable identity.

Registered mechanic families operate only through their owner adapter.

A human country is never excluded merely because it is controlled by a player.

## Valid country rule

The ordinary country pool includes countries that exist, have a legal country scope, and can use the gameplay system owned by the family.

Normal civilian, population, manpower, party, and law families use the shared civilian classifier or a stricter owner rule.

Special Chaos actors, system actors, actual nonhuman countries, dormant carriers, observer-like scopes, and countries with no meaningful consumer are excluded from ordinary civilian families unless their owner registers an explicit adapter.

Generic resource families can include a special actor only when the value has a real and safe gameplay meaning for that actor.

A special actor is never forced into ordinary human politics because it happens to be a country scope.

## Valid state rule

The ordinary state pool includes existing owned states that accept the selected value and are not protected by a scenario, owner, map, or lifecycle contract.

Impassable states, invalid map carriers, terminal wasteland states, reserved setup states, unowned placeholders, and owner-protected special states can be excluded by the family contract.

Coastal requirements, building capacity, province placement, supply graph validity, and DLC conditions are tested by the family that needs them.

One family can accept a state that another family excludes.

## Valid unit and commander rule

A unit or commander enters the pool only when its identity is stable for the duration of the transaction and the selected numeric surface can be changed without replacing, deleting, or duplicating that identity.

Units in unsupported transport, conversion, deployment, expeditionary, or owner-transfer states are excluded when the engine contract cannot prove safe mutation.

Unit templates, equipment definitions, commander identities, traits, and assignment graphs remain protected unless a later explicit contract proves a narrow safe surface.

## Firing lifecycle

### Selection

The ordinary random-event system selects Event 46 under its Minor Repeatable rules.

The event keeps the standard repeatable weight, recovery, and cap behavior.

One firing contributes one minor pacing event.

A cluster firing that includes Event 46 still counts as one cluster pacing event under the shared cluster contract.

### Transaction opening

The event acquires its global transaction lock and records one immutable firing context.

The context includes the active evolution capability, current Chaos tier, DLC state, valid owner-adapter registry version, and any legal range inputs needed by selected families.

The context does not preserve earlier Great Shuffle results.

### Family and scope planning

The event selects its families from the currently eligible allowlist.

It freezes each selected family's eligible scopes and range inputs.

It determines every result for that family before the family begins commit.

A result plan may store exact values or an immutable seed schedule paired with a stable scope list when that is the safer engine representation.

Either form must make the outcome fully determined before application.

### Validation

Every planned result is checked against its legal range, compatibility group, dependency bundle, protected-state rules, owner vetoes, and required reconciliation path.

A family that cannot prove a complete legal plan is skipped before any value in that family is changed.

The event never replaces an invalid planned family with a weaker substitute.

### Commit

A valid family commits across its full frozen scope list.

Where one family depends on another result, both belong to a declared bundle whose order and combined legality were planned before commit.

The event does not recalculate later scopes from earlier committed results.

### Reconciliation

After a family finishes commit, its declared reconciliation runs.

Reconciliation repairs legal dependencies, refreshes derived systems, and restores symmetric or normalized relationships.

It does not restore the old value or compensate for a bad result.

### Report and close

After all selected families finish or are skipped safely, the event builds one global summary and one personalized report for every human country.

The event records one normal Event 46 history entry and any concrete Chaos change.

It then clears temporary before values, result buffers, report buffers, and the transaction lock.

## Repeatable identity

Event 46 has no active crisis between firings.

Its persistent progression is limited to its five evolution capabilities, ordinary repeatable event state, achievements, and protected audit records.

The world state created by a firing remains ordinary gameplay state after the transaction closes.

AI and player countries react through their existing systems.

A later firing starts from scratch.

## Success and failure states

A successful firing commits at least one selected family, produces one report for each human player, records the event once, and leaves no transaction lock or incomplete result buffer.

A partially available world can still receive a successful firing when some families are ineligible and other families commit fully.

A family-level skip is valid when its full plan failed before commit and the report records the family as unavailable or rejected without exposing debug internals.

A firing that cannot commit any family aborts without changing gameplay state, without consuming an Event 46 repeatable firing, without adding Event 46 Chaos, and without presenting a false success report.

A family that begins commit must finish through its idempotent recovery path before the transaction can close.

## World Collapse reachability

Evolution V requires `1000+` Chaos, while the current mechanics guide also describes an automatic-event freeze at World Collapse.

The implementation must audit the live framework and preserve the fifth evolution's actual reachability.

If ordinary event selection remains active until a terminal `world_end` commits, Event 46 uses the normal picker and needs no exception.

If the live framework freezes automatic events immediately at `1000`, Event 46 receives one bounded pre-freeze eligibility window.

That window activates Evolution V immediately when enabled, respects the event's enabled state, respects the evolution toggle, consumes one normal repeatable firing when it runs, and closes before general event freeze.

It does not reopen other automatic events and does not bypass an already committed terminal state.

The exact source implementation can use the framework's existing pre-freeze hook or an equivalent owner-approved transaction point.

The fifth evolution must not exist only as unreachable Event Details text.
