# Event 065 Manual Design Review

## Review basis

The full project skill bundle and all 20 supplied subagent definitions were read before the specification was written.

The live project subagents could not be executed because the available custom tool registry returned an MCP tunnel `404`.

This document applies the relevant subagent roles as a manual planning review.

It is not a substitute for the required live audits during implementation.

## Repo explorer review

### Finding 1

The current Event 65 script already has the correct namespace and a hidden world entry point.

### Finding 2

The current root sends a visible event to every country.

The trait is granted inside that visible event's option.

This makes the gameplay result depend on report resolution and should be replaced.

### Finding 3

The current trait list is long, manual, marked incomplete, and contains repeated IDs.

The event needs a generated registry.

### Finding 4

The current repeatable registration and report sprite already exist.

They should be preserved, validated, and not recreated under new IDs.

### Finding 5

The current report DDS requires direct validation because its repository size is unusually small.

## Scripted-system architect review

### Chosen architecture

- one authoritative hidden root
- one global execution pass
- one generated country-leader trait registry
- one stable source-index map
- recipient-level source grant ledger
- weighted sampling without replacement
- one result record per human country
- one global history row
- one direct Chaos milestone path
- one shared root for direct and cluster firings

### Main unresolved engine questions

- whether every final country-leader database entry can be attached natively
- whether the grant ledger should live on character scope or leader-role scope
- which exact generated conditional selection structure gives exact high-saturation probability
- which scripted localisation path best resolves thousands of registry indexes
- which global actor pattern the current Event Log expects

These questions are implementation blockers until inspected.

They do not require broadening the player-facing design.

## Probability auditor review

The user requires exact uniform rolls at Baseline and Evolution I.

The user also requires modest high-Evolution bias.

The accepted model uses:

- ordinary `100`
- featured `125` at Evolution II
- featured `150` at Evolution III
- no stacked featured multipliers

This model is easy to explain and audit.

The final featured class size is unknown until the registry is generated.

The exact ordinary probability mass therefore remains unclaimed.

The probability matrix uses relative mass floors instead of inventing a final percentage.

## Event completion review

A complete Event 65 needs more than an expanded random list.

The pass or fail core is:

- exhaustive generated coverage
- exact unique additions
- correct Evolutions
- host-authoritative execution
- visible local results
- persistent ledgers
- direct Chaos guards
- event log and details
- cluster integration
- asset validity
- workbook alignment
- user test

The 87-row acceptance matrix is the completion checklist.

## Localisation review

The current description is generic and tied to one leader.

The rework is global.

Final text should use concrete observed behavior and show the local player's actual trait names.

The report needs zero, singular, plural, near-saturation, and no-leader states.

Raw registry indexes or source IDs are never player-facing.

Five trait names must render without clipping.

## Event UI review

The normal event report, Event Log, Event Details, and shared cluster views provide enough presentation.

A new interactive mechanic would not give the player a meaningful decision because the mutation is involuntary.

The specification concentrates depth in accurate result reporting and source coverage.

## Asset review

One report image is sufficient.

The image should communicate several incompatible political identities in a fictional period press setting.

A real historical leader collage would create unnecessary sourcing and identity issues.

The accepted direction uses anonymous generated figures and the standard report-event dimensions.

## Spreadsheet and documentation review

The supplied Event 65 row lacks Evolution, cluster, and severity data.

The supplied cluster catalog lacks Randomizations.

The current constants leave ID `9` free in the inspected snapshot.

The preferred workbook update uses ID `9` after a fresh collision check.

The permanent event documentation should include the generated trait manifest and probability summary.

## Improvement-loop review

The event's useful depth comes from technical completeness and visible results.

The following design is sufficient:

- one global mutation
- cumulative traits
- strong Evolution scaling
- complete dynamic source coverage
- bounded high-Evolution weighting
- real interactions from real source traits
- global and local reporting
- cluster and Chaos integration

A larger strategic layer would compete with the event's random and involuntary character.

The manual review recommends closure of the planning design once the current package is complete.

The mandatory live improvement-loop planner must still run near implementation completion.

## Critical challenges retained

### Complete pool claim

The implementation must fail check mode when the registry is stale.

A small fallback pool cannot preserve the complete-pool claim.

### High-saturation fairness

The exact roll method must remain fair when few traits remain.

A fast ordinary-case method cannot use a biased fallback.

### Trait-triggered side effects

The event intentionally uses real source traits.

Implementation testing should fix hard failures without sanitizing strange gameplay interactions.

### Shared role identity

The recipient ledger must follow the same identity as the trait.

Country scope is not automatically correct.

### Cluster ID

ID `9` is a current preference, not an eternal fact.

The workbook and constants need a fresh collision audit.

## Manual review conclusion

The specification is deep enough for the supplied event idea.

It is intentionally compact in player interaction.

The remaining work is implementation, live tool inspection, probability proof, asset validation, localisation rendering, documentation alignment, completion audit, and user testing.
