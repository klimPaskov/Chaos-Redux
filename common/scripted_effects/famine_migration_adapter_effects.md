# Famine and migration owner adapters

This file documents the owner-local bridges in `famine_migration_adapter_effects.txt`. The bridges register consequences in the shared famine and migration system after an owner has already proven the exact state and, where available, the responsible actor. They do not apply a second civilian population loss, create a route, start pacing, or scan states.

## Helper map

| Helper | Scope and inputs | Output and side effects | Owner call site |
| --- | --- | --- | --- |
| `famine_migration_adapt_air_winter_state` | State scope; `state_civilian_population_loss_applied` from Air Winter and a valid civilian state. | Registers the exact applied amount as Air Cleanliness food pressure, or Fallout pressure when `nuclear_fallout_state` is present. | `common/scripted_effects/fallout_consolidated_effects.txt`, `air_winter_apply_state_population_loss`. |
| `famine_migration_adapt_camp_state` | State scope; `camp_site_last_month_deaths`, `camp_state_site_type`, and `genocide_responsible_country`. | Registers the exact owner Deaths amount as camp, gulag, or forced-labor pressure. It never calls a Deaths effect. | `common/scripted_effects/camp_repression_rework_effects.txt`, `camp_rework_record_latest_state_deaths`. |
| `famine_migration_adapt_chemical_state` | State scope; accepted nerve-suppression operation, `cbrn_occupation_last_civilian_deaths`, and `cbrn_occupation_responsible_country`. | Registers chemical-aftermath pressure from the exact applied civilian loss. | `common/scripted_effects/cbrn_occupation_effects.txt`, `cbrn_occupation_apply_accepted_operation_state`. |
| `famine_migration_adapt_black_plague_state` | State scope; established Black Plague state and `state_civilian_population_loss_applied`. | Registers outbreak pressure from the exact applied loss; normal-civilian validation excludes nonhuman states. | `common/scripted_effects/020_black_plague_effects.txt`, `black_plague_apply_current_state_mortality_once`. |
| `famine_migration_adapt_natural_disaster_state` | State scope; Event 013 `natural_disaster_last_deaths` after impact resolution. | Registers the exact owner Deaths amount as natural-disaster food pressure. | `common/scripted_effects/013_natural_disasters_effects.txt`, `natural_disaster_apply_population_loss`. |
| `famine_migration_apply_related_state_deaths_exact` and reason aliases | State scope; explicit proven request, positive amount, owner target, and one of the accepted occupation/repression/forced-labor/forced-displacement reasons. | Calls the existing exact population-loss API and returns the applied amount. This remains API-only until an owner supplies a call site. | Public owner adapter API; no new owner call site is fabricated. |

All pressure calls set request proof, a positive amount, and actor proof before invoking the source-specific shared wrapper. The shared wrapper clears those temporary request fields after validation.

## Constants

`famine_migration_adapter_pressure.nuclear_strike_population_fraction` is the only adapter ratio. The nuclear callback proves the strike state and launching country but does not expose an applied civilian-loss amount, so it uses this centralized fraction and rounds the resulting people count. Air, Fallout, camp, CBRN, Black Plague, and Event 013 callbacks pass their exact owner-applied amount instead of estimating it.

## Cleanup and ownership

No adapter adds a persistent flag, event target, registry, or recurring action. Shared request fields are temporary and are cleared by `famine_migration_apply_pressure_request`. Owner Deaths ledgers, contamination ledgers, camp ledgers, plague phases, disaster history, and nuclear state flags remain owned by their existing systems.

## Unsupported owner seams

The handoff under `docs/plans/famine_and_migration_system_plans/subagent_handoffs/adapter_wiring_closure.md` records every integration-matrix row. The unresolved rows lack one or more of an exact state, responsible actor, causal event context, or stable owner callback. They are deliberately left API-only or unavailable-source; no generic pressure call, world scan, replacement event, or duplicate death path is used.
