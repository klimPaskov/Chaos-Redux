# Specification packages

Specifications are accepted design sources. They remain separate from event implementation overviews and working plans.

## Package convention

- Event packages use `docs/specs/<event_id>_<slug>_specs/`.
- System packages use a descriptive `<slug>_specs/` directory.
- Each package should provide a root `README.md` that identifies its accepted source, status, aliases, and superseded material.
- New packages should use `specs/`, `research/`, `matrices/`, `prompts/`, `validation/`, and `handoffs/` only when those surfaces exist.
- Existing historical filenames are preserved until their references and authority are reconciled.

## Known structural exceptions

- Event 003 has both `003_holy_realm_specs/` and `003_holy_realm_buddhahood_specs/`. Their relationship requires an explicit design disposition and neither package is silently discarded.
- `air_cleanliness_fallout_specs/` is a large cross-event system package with baseline and reviewed-event material.
- `chaos_redux_3d_model_workflow_planning_package/` is a workflow package rather than an event specification.
- `dynamic_major_event_weights_specs/dynamic_major_event_weights_spec.md` is a deliberate forwarder to the nested source.

