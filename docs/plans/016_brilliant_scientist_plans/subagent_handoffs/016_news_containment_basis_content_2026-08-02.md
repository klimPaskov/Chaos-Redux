# Event 016 containment-coalition news basis handoff

Date: 2026-08-02

## Scope

This bounded continuation adds threat-basis wording to the existing `chaosx.nr16.309` minor news headline. It does not create a new event, alter the shared world-end threshold, activate the world threat, enter Fallout, or produce a model dependency.

## Changed surfaces

- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt`
  - Adds `GetBrilliantScientistNewsContainmentClause`.
  - Reads the global current-host target and selects, in stable order, a prepared or armed Strategic Singularity, a weaponized project portfolio, deployed project formations, or a neutral clause.
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - Adds four public-facing threat-basis clauses.
  - Appends the helper to `chaosx.nr16.309.d`.
- `docs/events/016_brilliant_scientist/systems/news_events.md` and `overview.md`
  - Record the presentation-only state read and the unchanged super-event ownership.
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
  - Indexes this continuation as a bounded news-content tranche.
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`
  - Records the `.309` threat-basis clause alongside the existing `.306` and `.308` selectors.

## Runtime contract

The helper is safe after terminal cleanup because it checks `has_event_target = brilliant_scientist_current_host` before dereferencing the host. It only reads existing country flags and variables. The news event remains a minor, fire-once presentation surface with its original image, option, global guard, and delayed dispatch.

## Validation

- Focused Event Inspector lint for `chaosx.nr16.309` is required after wiring and must report no blocking diagnostics.
- All four new localisation keys must resolve exactly once and the localisation file must retain UTF-8 BOM encoding.
- The frozen Event 016 documentation checksum ledger must retain its existing 55-entry path set with zero mismatches.

## Deferred boundary

No 3D model, entity, unit, provider, world-threat threshold, Fallout effect, achievement, or catalog row is added by this tranche. Broader country-specific flavour, quantitative balance evidence, live consumer acceptance, and the seven Event 016-specific unit-model packages remain deferred.
