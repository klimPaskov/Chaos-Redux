# Event 016 news formation-origin content handoff

Date: 2026-08-02

## Scope

Add one presentation-only route selector to the delayed Kruger State formation headline `chaosx.nr16.307`. The selector reads the formation flag already persisted on the active Kruger State carrier and rebound to `brilliant_scientist_current_host` after the sovereignty transaction.

## Changed files

- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt`
- `localisation/english/016_brilliant_scientist_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/news_events.md`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`

## Runtime contract

`GetBrilliantScientistNewsFormationClause` is guarded by `has_event_target = brilliant_scientist_current_host` and uses stable precedence for `brilliant_scientist_formation_charter`, `brilliant_scientist_formation_rebellion`, `brilliant_scientist_formation_enclave`, and `brilliant_scientist_formation_takeover`. A neutral clause is returned after terminal cleanup or for an unusual pre-existing save. The `.307` effect block, receipt, delay, picture, formation super-event, territory transfer, cores, government, and all unit/model contracts are unchanged.

## Validation

- Focused Event Inspector lint for `chaosx.nr16.307` returned `status: ok`, zero blockers, and zero blocking diagnostics.
- The five new localisation keys occur exactly once and the `.307.d` helper call occurs exactly once.
- The localisation file retains UTF-8 BOM encoding.
- The frozen Event 016 checksum ledger was recomputed after the documentation edits and must remain at 55 entries with zero mismatches before commit.

## Deferred boundary

Broader country-specific flavour, quantitative balance evidence, user-owned live acceptance, and all seven Event 016-specific 3D packages remain deferred. This handoff does not create or reference a model, entity, provider, unit, reward, or new fire path.
