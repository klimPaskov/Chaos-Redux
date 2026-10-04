# Migration decision phase effects

## `migration_project_reception_preparation_cost_quote`

Scope: COUNTRY.
Inputs: none; the shared `migration_reception_preparation_cost` constants provide all three amounts.
Outputs: normal display-only `migration_reception_preparation_quote_political_power`, `migration_reception_preparation_quote_support_equipment`, and `migration_reception_preparation_quote_fuel`.
Side effects: assigns those three text projections only, without payment, resource grants, policy changes, services, capacity, category reveal, or scheduling.
The existing active-country registration calls this projection before a newly eligible action can render, and the existing phase refresh updates it thereafter.
Neither affordability nor payment reads these cached display amounts.

Usage inside the actual COUNTRY scope:

```text
migration_project_reception_preparation_cost_quote = yes
```

## `migration_refresh_decision_phase_from_country`

Scope: COUNTRY.

The migration owner retains the aligned live-cohort, current-host, origin, destination, reception-load, and flight/trapped crisis proofs from the registered-country scheduler. It uses those proofs to set `migration_decision_emerging`, restore `migration_decision_active` when an unresolved origin crisis returns, move an active live hosted cohort toward `migration_decision_resolution`, and independently retire a previously observed empty resolution to `migration_decision_dormant`.

Food stage flags and famine lifecycle flags are deliberately absent. The helper never clears or sets famine state, and it does not discover countries or add a recurring world iteration.

At the same existing country refresh boundary, it calls the shared cost projection from the centralized reception preparation cost table.
These are display-only cost amounts, not new mechanic values, stockpiles, or authority for availability or payment.
The preparation owner and cost color selectors read fresh constants instead.

The neutral `humanitarian_refresh_decision_phase_from_country` dispatcher lives in `humanitarian_runtime_effects.txt` so the existing scheduler call remains source-compatible while the two phase owners stay separate.

The country phase and active-country registration also call `humanitarian_project_legacy_cost_quote` for the 15 legacy fee display amounts, separately from the three Open Reception quotes.
Those normal text values never govern cost readiness, payment, refund or paid-action matching and create no registry, periodic world scan, category reveal or additional mechanic value.

The quote consumer is `common/scripted_localisation/migration_reception_preparation_cost_scripted_localisation.txt`, which resolves six ready/blocked keys in `localisation/english/migration_l_english.yml`.
Its existing political-power, support-equipment, and fuel texticons remain unchanged; no new asset or scripted-GUI layout is introduced.
