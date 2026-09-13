# Event 53: Mysterious Man

This package is the source specification for Chaos Redux Event 53.

## Catalog identity

| Field | Accepted value |
| --- | --- |
| Event ID | `53` |
| Event name | Mysterious Man |
| Event type | Minor Fire-Once |
| Chaos level | `1` |
| Cluster | None |
| Member severity | Not applicable |
| Current catalog status | To Be Reworked |

The parent event fires once and selects one valid player-controlled country. Every later visit is a follow-up event attached to that country. Later visits do not count as new Event 53 firings.

## Design promise

An ordinary-looking man appears inside places that should be inaccessible. He makes one demand and waits for an answer. Paying settles the current visit. Refusing, or being unable to pay, causes one substantial harmful consequence selected uniformly from every currently valid Event 53 consequence package. He leaves after either answer and returns later.

The event never explains who he is, how he enters secure places, why he chooses the country, how he causes consequences, or where he goes. No mechanic can arrest, expose, deter, kill, trap, investigate, delay, or permanently satisfy him.

## Package map

The `specs` folder defines the complete design, lifecycle, demand engine, consequence system, evolutions, system connections, presentation, multiplayer rules, balance targets, and implementation architecture.

The `quality` folder contains the registry manifest, adapter contracts, probability scenarios, validation scenarios, design-scope closure review, and source-reading record.

The `catalog` folder records the required Event 53 catalog correction without editing the export-only CSV.

The `prompts` folder contains a compact goal prompt, a full implementation prompt, an asset-production prompt, and context-complete prompts for the relevant project subagents.

## Authoritative rules

The following rules outrank optional tuning suggestions elsewhere in this pack:

1. The original selected player country remains the target for the chain.
2. The man cannot be countered or prevented.
3. Every refusal selects exactly one registered package.
4. Every valid registered package appears exactly once in the active pool.
5. Every entry in the active pool has exactly equal probability.
6. Severity variants, target variants, and flavour variants never receive extra ballots.
7. Borrowed systems keep ownership of their gameplay package and cleanup.
8. Borrowed source events do not count as having fired.
9. Event 53 owns selection, attribution, recurrence, and lifecycle state.
10. The event uses recurring country-scoped follow-ups and no whole-world daily or monthly scan.
11. An unrelated `world_end` flag does not cancel the chain while the selected target remains valid.

## Working labels

Names for packages, helpers, events, files, sprites, and engineering states in this specification are working implementation labels. They are not final localisation. Final player-facing text must be written during implementation under the event writing rules and then reviewed by the localisation auditor.
