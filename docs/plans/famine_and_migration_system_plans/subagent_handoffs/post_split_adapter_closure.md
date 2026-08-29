# Post-split adapter closure handoff

## Scope

This bounded pass closes the famine/migration adapter seams requested after the split. It does not add recurring world scans, alter decisions beyond exact adapter ownership checks, or create a combined famine/migration lifecycle.

## Changed files and identifiers

- `common/scripted_effects/famine_core_effects.txt`: `famine_submit_survivor_flight_request` now owns only famine stage/request bookkeeping and submits the people amount, resource-shortage source, actor proof, and stage generation through `migration_apply_flight_request`. Direct migration initialization, pressure, incident, active-registration, decision-refresh, and accepted-request writes were removed from the famine caller. Temporary famine calculation names are `famine_flight_*`.
- `common/scripted_effects/migration_core_effects.txt`: `migration_apply_flight_request` remains the migration owner for pressure, state flight population, incident creation, active registration, decision refresh, and optional `migration_flight_request_generation` / `migration_flight_request_accepted_total` writes. The optional positive `migration_pressure_request_generation` input is cleared with the other request fields.
- `common/scripted_effects/fallout_consolidated_effects.txt`: Air Winter supplies state, phase, shelter, adaptation, cycle, loss-memory, actor-target, cause, and date proof before `famine_adapt_air_winter_state`.
- `common/scripted_effects/camp_repression_rework_effects.txt`: Camp supplies site, pool, reach, coercive-control, responsible-actor target, death reason, date, and loss proof before `famine_adapt_camp_state`; the custody caller re-resolves its staged migration row and supplies current-host route, projection-generation, revision, transaction-date, and request-date proof before `migration_record_current_state_cohort_custody_exact`; the obsolete consumer now checks `migration_current_state_custody_result`.
- `common/scripted_effects/cbrn_occupation_effects.txt`: accepted nerve-suppression callback supplies operation route, severity/contamination fallback, attribution, action date, civilian-loss, and actor-target proof before `famine_adapt_chemical_state`.
- `common/scripted_effects/020_black_plague_effects.txt`: non-rat plague pulse supplies outbreak ledgers, route/phase fallback, containment/phase fallback, provenance/phase fallback, pulse/date, exact loss, and actor-target proof before `famine_adapt_black_plague_state`.
- `common/scripted_effects/013_natural_disasters_effects.txt`: Event 013 supplies sequence, family, severity, driver fallback, loss, cause, actor-target, and date proof before `famine_adapt_natural_disaster_state`.
- `common/scripted_effects/migration_forced_movement_effects.txt`: valid positive forced-transfer transaction supplies origin-state target, cohort, exact origin debit, route, actor, cause, transaction generation, revision, and request identity before `migration_condemn_deportation`.
- `common/scripted_effects/famine_adapter_effects.md` and `common/scripted_effects/migration_adapter_effects.md`: documented caller proof status, custody result rename, and the migration-owned optional flight-generation contract.

## Removed/renamed references

Focused source searches show no remaining `humanitarian_condemn_*` or `humanitarian_current_state_custody_result` references in `common/`. The split wrappers are `famine_condemn_*` and `migration_condemn_*`; no famine decision currently invokes a condemnation wrapper without a proof bundle, and the split migration decision file contains no stale removed condemnation call.

## Validation evidence

- `rg` confirmed the old condemnation and custody identifiers are absent from `common/`.
- `rg` confirmed famine flight calculations use `famine_flight_*` temporary/persistent names; remaining `migration_flight_*` reads in famine are migration-owned ledgers, and famine writes only the explicit `migration_pressure_request_*` contract fields.
- `rg` confirmed all five named hazard adapters have adjacent source-owned proof assignments and actor targets.
- No game launch was performed. No additional HOI4 MCP call was made in this closure pass because the scoped changes are scripted adapters/effects without a linked focus, event, GUI, map, or weighted surface, and the parent requested no additional long MCP calls.

## Blockers and uncertainty

- Camp custody now consumes the migration-owned result name and re-resolves the staged row before the adapter. The caller supplies a current-host/whole-row route proof, action-date transaction/request identity, migration projection generation, and staged whole-row revision. A missing runtime generation or invalid current host still fails closed; no synthetic proof is added.
- `famine_condemn_*`, `migration_condemn_forced_return`, and `migration_condemn_violent_pushback` remain available fail-closed wrappers. The current split famine/migration decision surfaces do not provide complete independent condemnation proof bundles, so they do not call the wrappers. The forced-transfer path is the only repaired condemnation caller in this bounded pass.
- Source fallback proof values (Air Winter phase, CBRN severity, plague phase, and natural-disaster severity) are only used when a corresponding source ledger is zero/missing; if the source owner cannot provide a positive identity fact, the validator rejects the receipt. This preserves fail-closed behavior but still needs focused live-save confirmation by the parent.
- Engine/runtime validation was not available in this pass; parent review should confirm that every source callback executes in a state scope with a valid `OWNER` and that the chosen source ledgers are positive in the intended edge cases.
