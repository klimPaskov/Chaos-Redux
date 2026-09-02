# Event 016 conventional technology API effects

This file owns the neutral country-scoped package grant and runtime reconciliation for the six existing conventional Event 016 project families.

The API uses existing `brilliant_scientist_project_family` IDs for Computation, Electronics, Materials, Rocketry, High Energy, and Biomedical, and existing `brilliant_scientist_project_stage` IDs for Deployment and Weaponization.

It adds no hidden technology, project family, project stage, facility, Directorate history, achievement, GUI, or random candidate.

## Public effects

### `chaosx_grant_conventional_technology_package`

Scope: Country.

Inputs:

- `chaosx_conventional_technology_family` must be one of `constant:brilliant_scientist_project_family.computation`, `electronics`, `materials`, `rocketry`, `high_energy`, or `biomedical`.
- `chaosx_conventional_technology_tier` must be `constant:brilliant_scientist_project_stage.deployment` or `weaponization`.
- `chaosx_custom_technology_source` is optional and uses the existing source validator.

Behavior:

- Invalid or missing family/tier input is a no-op.
- Deployment sets only `conventional_technology_<family>_operational`.
- Weaponization sets the operational flag first, then `conventional_technology_<family>_weaponized`.
- The matching full-strength existing theory, prototype, deployment, and optional weaponization dynamic modifiers are reconciled immediately.
- Computation reconciles one shared research slot through the neutral owner marker.
- Valid public source input is recorded after the grant in a separate operational or weaponization provenance array.
- Repeated valid calls are idempotent.

Output:

`chaosx_conventional_technology_grant_applied` is a temporary value of `1` for a valid request and `0` otherwise.

The effect does not charge resources, start a timer, occupy factories, execute a strategic directive, or change target scope.

### `chaosx_reconcile_conventional_technology_runtime`

Scope: Country.

Inputs: None.

Behavior:

- Reads only the six durable neutral operational and weaponization flags.
- Reapplies the existing matching Event 016 dynamic modifiers without creating weaker duplicate modifiers.
- Does not change `chaosx_conventional_technology_family`, `chaosx_conventional_technology_tier`, or `chaosx_custom_technology_source`.
- Adopts `brilliant_scientist_computation_research_slot_active` into `conventional_technology_computation_research_slot_active` without adding another slot when a native slot already exists.
- Adds one `constant:brilliant_scientist_project_technology.research_slot_gain` slot only when the neutral computation package is operational and neither owner marker exists.
- Never removes a learned slot and never creates the old native marker.

Output:

`chaosx_conventional_technology_runtime_reconciled` is a temporary value of `1` after the bounded reconciliation pass.

## Private effects

### `chaosx_grant_conventional_technology_package_core`

Scope: Country.

This is the shared validated core for public neutral callers and native completion wrappers.

It validates the exact family and tier, writes neutral package flags, calls runtime reconciliation, and returns `chaosx_conventional_technology_grant_applied = 1` for a valid request.

It never records provenance, so a native caller cannot consume an unrelated public `chaosx_custom_technology_source` variable.

### Provenance writers

`chaosx_record_conventional_technology_operational_provenance` and `chaosx_record_conventional_technology_weaponization_provenance` are country-scope private writers used only after the public core returns success.

Each writer uses the existing `chaosx_custom_technology_source_is_valid` query and encodes `chaosx_conventional_technology_family * constant:chaosx_custom_technology_tuning.provenance_stride + chaosx_custom_technology_source`.

The writers append to separate `conventional_technology_operational_provenance` and `conventional_technology_weaponization_provenance` arrays only when the encoded receipt is absent.

Invalid or missing source input does not invalidate a valid package grant and creates no receipt.

## Query contract

The matching trigger file provides these country-scope queries:

- `chaosx_conventional_technology_request_is_valid` validates the exact six-family and two-tier request.
- `chaosx_requested_conventional_technology_is_owned` checks the requested family’s operational or weaponized durable flag according to the requested tier.
- `chaosx_has_conventional_operational_technology` checks whether any of the six operational flags is present.
- `chaosx_has_conventional_weaponized_technology` checks whether any of the six weaponized flags is present.

Queries are read-only and fail closed for missing or invalid selectors.

## Caller contract

Public callers set the two selectors, optionally provide `chaosx_custom_technology_source`, and invoke `chaosx_grant_conventional_technology_package = yes` in country scope.

Native completion callers set the selectors and invoke `chaosx_grant_conventional_technology_package_core = yes` so public provenance state is not inherited accidentally.

Runtime reset, transfer, provider cleanup, and neutral category owners invoke `chaosx_reconcile_conventional_technology_runtime = yes` only in country scope.

The caller remains responsible for any explicit native-source provenance it owns.

## Existing consumer boundaries

The six existing `brilliant_scientist_<family>_{theory,prototype,deployment,weaponization}` dynamic modifiers are reused directly.

Their enable and removal conditions recognize the corresponding neutral flags as well as the native host state.

Native stage completion and valid native history reconstruction call `brilliant_scientist_record_conventional_stage_knowledge`, which invokes the private core and records the known Event 016 source without reading the public optional-source input.
Inheritance records that knowledge before the physical-project health gate, so a completed but suspended, damaged, or dismantled project still transfers its learned package without repairing the project or repeating stage rewards.
Project disable removes project-bound modifiers and then reapplies durable learned packages through the neutral reconciliation effect.
The existing public `chaosx_reconcile_custom_technology_runtime` boundary also invokes this reconciliation without granting missing conventional families.
Kruger State initialization and same-country takeover call `brilliant_scientist_apply_formation_research_floor`, which keeps the ordinary starting floor separate from an active native or neutral Computation slot and never reduces a larger research establishment.

The eight strategic actions use one ordinary `conventional_technology_operations` category and read the accepted weaponized package flags, not native project completion or Kruger ownership.
Their native timers, payment, refund, target, and cooldown consumers remain distinct from the knowledge grant.
The existing Event 016 CXT carrier grants the six weaponized packages through the private core, without claiming an event-source discovery, and reapplies their runtime consumers idempotently.

## Example

```text
set_variable = { chaosx_conventional_technology_family = constant:brilliant_scientist_project_family.computation }
set_variable = { chaosx_conventional_technology_tier = constant:brilliant_scientist_project_stage.weaponization }
set_variable = { chaosx_custom_technology_source = 25 }
chaosx_grant_conventional_technology_package = yes
```

The example grants the cumulative Computation operational package, the Computation weaponization output, one shared research slot, and idempotent receipts for the valid source `25`.

The existing seven-family random technology helper is not a caller of this package effect and remains unchanged.
