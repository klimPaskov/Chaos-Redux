# Mengele adapter patch handoff

## Changed files

- `common/scripted_effects/germany_mengele_effects.txt`

## Changed identifiers

- `germany_mengele_register_experiment_deaths`
- `germany_mengele_add_requested_biowarfare_facility`

## Behavior

- State `88` experiment deaths now pass `camp_exact_deaths` and `camp_exact_deaths_reason` to `camp_rework_register_exact_state_deaths`.
- The caller only assigns `genocide_responsible_country` when that state variable is absent. It preserves an existing responsible-country pointer.
- Each facility-demand branch registers its actual selected state through `camp_rework_germany_register_requested_laboratory_state` after construction.
- The existing Auschwitz layer marker remains in the successful-demand aftermath, so state `88` can retain its separate experiment-site role when another candidate state receives the facility.

## Validation

- The experiment-death effect has one exact-adapter call, both required inputs, and no direct `chaos_meter_register_deaths` call.
- The facility-demand effect has four construction branches and four branch-local registration calls for states `88`, `89`, `64`, and `60`.
- Both edited effects close at brace depth zero.

## Remaining risks and parent follow-up

- `camp_rework_register_exact_state_deaths` and `camp_rework_germany_register_requested_laboratory_state` must exist with the expected state scope before the full tranche is complete.
- The shared exact-death adapter owns legacy Deaths outputs, state-population reduction, cumulative site deaths, and responsible-country credit. This patch deliberately does not duplicate those operations.
- No event file was edited. The existing `germany_mengele.17` option remains the call site.
