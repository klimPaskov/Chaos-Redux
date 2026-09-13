# Event 046 owner-adapter contract

## Purpose

An owner adapter lets another mechanic surrender a mutable current value to The Great Shuffle without transferring ownership of the mechanic.

The adapter is a narrow declaration.

It is not a copy of the owner's internal implementation.

## Owner prerequisites

Before registration, the owner must identify:

- the current value that can be rewritten
- the scope that owns it
- the value's legal range or candidate set
- the lifecycle state in which rewriting is safe
- the history and identity that remain protected
- the dependent stage, modifier, AI, and UI state that must be refreshed
- the cleanup path
- the save and load path

A value with uncertain meaning or incomplete lifecycle proof remains unregistered.

## Registration phase

The owner registers one stable family ID and contract version.

Registration is idempotent.

The owner can register several distinct values as several families.

A group of values that must remain coordinated registers one dependency bundle.

The owner does not register raw variable names for Event 46 to mutate directly.

It provides owner-controlled read, plan-range, set, reconcile, and cleanup behavior.

## Eligibility phase

For one transaction, the owner returns the stable active instances that can participate.

It excludes missing targets, incomplete setup, transitional cleanup, terminal state, inactive values with no meaning, and any instance whose protected ledger is incomplete.

A failure to prove eligibility excludes the instance.

It does not produce a default scope.

## Snapshot phase

The owner supplies the current public value for reporting and any frozen facts needed to calculate a legal range.

The old value cannot influence the preferred direction or center of the new result.

The owner can supply a legal cap, stage-specific candidate set, or scope category.

The owner cannot supply a compensation preference based on earlier Shuffle harm.

## Planning phase

Event 46 chooses the distribution profile and produces the planned result under the owner range.

For categorical systems, the owner provides the candidate set and compatibility proof.

For share systems, the owner provides the normalization rule.

For pair systems, the owner provides stable pair identity and symmetry rules.

The owner can reject the complete family before commit when one planned result would invalidate the mechanic.

It cannot reroll only the inconvenient instance.

## Commit phase

Event 46 calls the owner setter with the immutable planned result.

The owner changes the current value once.

It does not update history to claim that an ordinary decision, war, election, death, discovery, or player action caused the new value.

It records only the minimal source proof needed to identify Event 46 as the change owner.

## Reconciliation phase

The owner recalculates derived stages, modifiers, available actions, AI strategy, display state, and bounded processing registration.

Reconciliation restores legality.

It cannot restore the old value, award compensation, or silently clamp the result to a preferred range that was not part of planning.

When a clamp is legally necessary, the legal clamp must have been included in the result plan and report.

## Report phase

A public adapter supplies a concise player-facing name, value formatter, threshold crossing score, and optional scope name.

A hidden internal value is omitted from the report or summarized through the public value it supports.

The owner does not expose raw variable names or private stage IDs.

## Chaos phase

The owner proposes a low, medium, or high disruption class.

Event 46 approves the class and compresses it into the one transaction gain.

The owner suppresses any generic Chaos source created only by the setter when Event 46 owns the result.

A later real consequence remains ordinary owner or shared Chaos.

## AI phase

The owner confirms whether ordinary AI observes the changed value automatically.

When it does not, the owner supplies a bounded refresh.

The refresh changes evaluation and action choice.

It does not improve a bad random result.

## Recovery phase

The owner records enough progress to make commit and reconciliation idempotent.

On load, it resumes the exact planned value.

It does not reroll, restore the old value, or create a second report.

## Cleanup phase

The owner clears transaction-local scope markers, planned values, temporary targets, source suppression, and report candidates.

Stable current gameplay state remains.

Historical ledgers and identity remain unchanged.

## Owner veto reasons

Valid veto reasons include:

- lifecycle setup is incomplete
- current target proof is missing
- value has no meaning in the current state
- setter or cap is unavailable
- dependent stage cannot be reconciled
- object identity can change during commit
- history would become false
- save recovery is not idempotent
- performance is unsafe for the current instance count

The owner must not veto merely because the planned result is unfavorable.

## Adapter acceptance evidence

Every adapter needs:

- source documentation
- registered family and owner identity
- no-write proof for protected ledgers
- valid and invalid scope cases
- minimum and maximum result cases
- threshold crossing cases
- save and load resume case
- AI refresh case when relevant
- report formatting case
- source-overlap case
- cleanup case
- probability inclusion and starvation case
