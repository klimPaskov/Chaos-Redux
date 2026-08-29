# Famine and Migration Namespace Separation Validation

Date: 2026-08-26.

## Accepted ownership

Famine-owned runtime files, identifiers, flags, variables, constants, triggers, effects, decisions, category, scripted localisation, report carrier, sprites, assets, and localisation use `famine_*`.

Migration-owned runtime files, identifiers, flags, variables, constants, triggers, effects, decisions, category, scripted localisation, report carrier, sprites, assets, and localisation use `migration_*`.

Exact state-to-state population conservation uses the neutral `civilian_transfer_*` namespace. Narrow shared corridor, scheduling, validation, cost-presentation, and achievement infrastructure may use `humanitarian_*` only when it does not own famine or migration state.

There is no compatibility alias or combined runtime namespace.

## Current source result

A literal search for `famine_migration_*` and `fm_*` across `common`, `events`, `interface`, `localisation`, `gfx`, and `history` returned zero matches across 2,188 searched runtime files.

A separate recursive filename audit across the same runtime roots returned `bad_runtime_filenames=0` for names containing `famine_migration` or beginning with `fm_`.

A repository-wide filename audit also returns zero files beginning with `famine_migration` or `fm_`. The last historical handoff carrying the combined prefix was renamed to `mechanic_separation_architecture.md`; its disposition ledger reference was updated in the same change.

The owning decision files are `common/decisions/famine_decisions.txt` and `common/decisions/migration_decisions.txt`. Their categories are `famine_decision_category` and `migration_decision_category`. Their dedicated mapmodes are `famine_state_map_mode` and `migration_state_map_mode`.

The cost-presentation library uses `common/scripted_localisation/humanitarian_cost_scripted_localisation.txt`, `localisation/english/humanitarian_cost_l_english.yml`, `GetHumanitarianCost*`, and `humanitarian_cost_*`. The superseded active `civilian_response_*` / `GetCivilianResponse*` cost namespace was removed atomically; the current library contains 15 selectors and 30 ready/blocked keys consumed by 81 famine/migration cost calls.

The binding specification headings and implementation prompts describe separate famine and migration mechanics connected only through explicit causal adapters and neutral conservation primitives. They do not authorize a single shared mechanic.

The package deliberately has no famine/migration event source, combined decision category, combined mapmode, combined registry, combined stage variable, or combined player-facing meter.

## Historical documentation boundary

Some specifications and superseded handoffs preserve former planning identifiers as historical audit evidence. The current spec notices mark those names superseded, and `handoff_dispositions.md` prevents them from being mistaken for current APIs. Historical quoted names are not runtime aliases and must not be copied back into source.

The umbrella directories `famine_and_migration_system_specs` and `famine_and_migration_system_plans` remain package containers for the two connected mechanics. They are documentation locations, not identifiers, namespaces, categories, registries, mapmodes, or gameplay systems.
