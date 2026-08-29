# Migration decision phase effects

## `migration_refresh_decision_phase_from_country`

Scope: COUNTRY.

The migration owner retains the aligned live-cohort, current-host, origin, destination, reception-load, and flight/trapped crisis proofs from the registered-country scheduler. It uses those proofs to set `migration_decision_emerging`, restore `migration_decision_active` when an unresolved origin crisis returns, move an active live hosted cohort toward `migration_decision_resolution`, and independently retire a previously observed empty resolution to `migration_decision_dormant`.

Food stage flags and famine lifecycle flags are deliberately absent. The helper never clears or sets famine state, and it does not discover countries or add a recurring world iteration.

The neutral `humanitarian_refresh_decision_phase_from_country` dispatcher lives in `famine_decision_phase_effects.txt` so the existing scheduler call remains source-compatible while the two phase owners stay separate.

No localisation, icon, or scripted-GUI key is owned by this helper.
