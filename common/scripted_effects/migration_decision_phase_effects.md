# Migration decision phase effects

## `migration_project_reception_preparation_cost_quote`

Scope: COUNTRY.
Inputs: the central `migration_transport_cost` constants.
Outputs: six display-only normal fuel quantities in k through `migration_transport_project_cost_quotes`.
Side effects: retires the three obsolete reception display caches, without payment, resource grants, policy changes, services, capacity, reveal or scheduling.
The existing active-country registration calls this projection before the eligible action can render, and the existing phase refresh updates it thereafter.
Neither affordability nor payment reads cached display quantities.
The selected-state getters read FROM geography and the same central constants, so states in different landmasses can show different fees within the same country.
See [migration_transport_cost_effects.md](migration_transport_cost_effects.md) for the complete contract and source cases.

```text
migration_project_reception_preparation_cost_quote = yes
```

## `migration_refresh_decision_phase_from_country`

Scope: COUNTRY.

The migration owner retains the aligned live-cohort, current-host, origin, destination, reception-load, and flight/trapped crisis proofs from the registered-country scheduler. It uses those proofs to set `migration_decision_emerging`, restore `migration_decision_active` when an unresolved origin crisis returns, move an active live hosted cohort toward `migration_decision_resolution`, and independently retire a previously observed empty resolution to `migration_decision_dormant`.

Food stage flags and famine lifecycle flags are deliberately absent. The helper never clears or sets famine state, and it does not discover countries or add a recurring world iteration.

At the same existing country refresh boundary, it calls the shared physical transport display projection from the centralized transport cost table.
These are display-only cost amounts, not new mechanic values, stockpiles, or authority for availability or payment.
The preparation owner and cost color selectors read fresh constants instead.

`migration_process_registered_country` calls it directly; famine refreshes its own phase from its own country registry.
The phase flags are presentation: they choose the category header text and mission visibility, but no ordinary migration decision is locked or unlocked by them. Each decision is offered by its own state, cohort, load and policy conditions.

The country phase and active-country registration also call `humanitarian_project_legacy_cost_quote` for the 15 legacy fee display amounts, separately from the physical transport projection.
Those normal text values never govern cost readiness, payment, refund or paid-action matching and create no registry, periodic world scan, category reveal or additional mechanic value.

The transport quote consumer is `common/scripted_localisation/migration_transport_cost_scripted_localisation.txt`, whose ready/blocked fuel labels use lowercase k and whose selected FROM state controls the conditional convoy fee.
Reception medical supplies use `migration_reception_preparation_cost_scripted_localisation.txt` and the existing support-equipment texticon.
No asset or scripted-GUI layout is introduced.
