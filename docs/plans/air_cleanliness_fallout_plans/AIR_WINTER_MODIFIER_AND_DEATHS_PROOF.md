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

Monthly Air Winter civilian losses already call that shared effect. Event
casualties now test the same global flag before calling
`apply_exact_state_civilian_population_loss`. When Deaths is disabled, neither
path removes population or increments `air_winter_population_loss_memory`.
When Deaths is enabled, both paths use reason
`constant:chaos_meter_deaths_reason.air_winter_exposure`.

The shared exact-loss helper can be used by other systems that intentionally
remove population even when Deaths display and logging are disabled. Air
Winter does not use that independent mode. Changing the global setting
contract or the shared helper is outside this tranche and would require a
separate design decision across all callers.

## Runtime observation boundary

Static evidence proves the repair-field categories, every building token, the
Deaths setting gates, and vanilla state usage of controller attrition. Live
controller and enemy attrition deltas remain unobserved because the generated
catalogue and vanilla state precedent do not fully agree. The implementation
retains the stronger live vanilla precedent without reporting a runtime test.
