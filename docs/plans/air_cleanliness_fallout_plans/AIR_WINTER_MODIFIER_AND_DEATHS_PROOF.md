# Air Winter Modifier and Deaths Proof

## Installed engine baseline

The inspected installed build is Hearts of Iron IV 1.19.2.0. This proof uses
the generated official modifier catalogue, live vanilla dynamic modifiers,
the Chaos Redux Deaths implementation, and the player-facing Deaths setting
contract.

## State repair modifiers

The official `documentation/modifiers_documentation.md` entry for
`state_repair_speed_<Building>_factor` defines it as a state category modifier
and lists all building types damaged by Air Winter. The six phase modifiers
therefore apply their shared repair value through these exact fields:

- `state_repair_speed_infrastructure_factor`
- `state_repair_speed_rail_way_factor`
- `state_repair_speed_industrial_complex_factor`
- `state_repair_speed_arms_factory_factor`
- `state_repair_speed_air_base_factor`
- `state_repair_speed_dockyard_factor`
- `state_repair_speed_supply_node_factor`

The earlier `industry_repair_factor` and `industry_free_repair_factor` fields
were removed. The official catalogue restricts both to country and war
production categories, so they do not prove a state modifier effect. There is
no documented state equivalent for free repair and none is simulated.

Vanilla `common/dynamic_modifiers/mun_dynamic_modifiers.txt` provides a live
state modifier precedent for the infrastructure and supply-node forms. The
official modified-type list proves the other five generated building forms.

## Operational attrition

The official catalogue marks `enemy_attrition` as valid for state and army
categories. It does not list a state category for `attrition_for_controller`.
Vanilla nevertheless applies `attrition_for_controller` in state-owned dynamic
modifiers. The strongest precedents are:

- `FIN_motti_tactics_modifier` in
  `common/dynamic_modifiers/aat_dynamic_modifiers.txt`, applied to a target
  state by `common/decisions/FIN.txt`.
- `skirmishes_against_imro` in
  `common/dynamic_modifiers/0_dynamic_modifiers.txt`, applied directly to
  numbered states and controlled-state iterators by
  `common/decisions/BUL.txt`.
- The resistance state modifier in
  `common/resistance_compliance_modifiers/resistance_modifiers.txt`.

This vanilla evidence supports retaining the controller-side field. The
generated category list still disagrees with live vanilla usage. A future
runtime comparison can observe a controlled state with and without one Air
Winter phase modifier while identical friendly units remain in the state. The
controller and enemy attrition deltas are not claimed as observed here.

## Deaths setting contract

The player-facing setting states that disabling the Deaths system also disables
state-population losses from its mechanics. `chaos_meter_register_deaths`
enforces that contract by gating its ledger work and state-population effect
behind the absence of `settings_chaos_deaths_disabled`.

Monthly and event Air Winter casualties test that global flag before calling
`apply_exact_state_civilian_population_loss`. When Deaths is disabled, neither
path removes population or increments `air_winter_population_loss_memory`.
When Deaths is enabled, both paths use reason
`constant:chaos_meter_deaths_reason.air_winter_exposure` and derive winter
memory from the helper's returned applied amount. Monthly pressure preserves
its existing zero protected floor. Incident casualties preserve their 1,000
person protected floor.

The shared exact-loss helper can be used by other systems that intentionally
remove population even when Deaths display and logging are disabled. Air
Winter does not use that independent mode. Changing the global setting
contract or the shared helper is outside this tranche and would require a
separate design decision across all callers.

## Exact state population route

The official `documentation/effects_documentation.md` entry for
`add_manpower` permits state scope and says that it changes local state
manpower. The offline Effects reference is more explicit. A positive value
adds state population, while a negative value reduces state population and
also credits recruitable manpower. The official trigger catalogue documents
`state_population_k` as state population in thousands. The offline data
structures reference documents `manpower_k` as country manpower in thousands.

`apply_exact_state_civilian_population_loss` clamps the requested people to
the current `state_population_k` above the caller's protected floor and then
uses one shared state mutation. Its internal
`apply_state_population_loss_without_recruitable_manpower_gain` transaction:

1. snapshots the legal owner's `manpower_k`
2. snapshots a distinct controller's `manpower_k` when the state is occupied
3. issues one negative state-scope `add_manpower` using the rounded people loss
4. measures positive manpower changes in both country scopes
5. removes only the observed credit, bounded by the original loss

This handles either owner or controller credit without guessing which country
the engine selects for an occupied state. Monthly and incident Air Winter code
contains no direct `add_manpower` effect. Both routes use the shared helper,
pre-seed its temporary outputs, and add only
`state_civilian_population_loss_applied` to winter memory.

## Runtime observation boundary

Static evidence proves the repair-field categories, every building token, the
Deaths setting gates, the documented state population mutation route, the
recruitable-credit reconciliation contract, and vanilla state usage of
controller attrition. The exact live state-population delta and the controller
and enemy attrition deltas remain unobserved. The implementation retains the
documented population route and stronger live vanilla attrition precedent
without reporting a runtime test.
