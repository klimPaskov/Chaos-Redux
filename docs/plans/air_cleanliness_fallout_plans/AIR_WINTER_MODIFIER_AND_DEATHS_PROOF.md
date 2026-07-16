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

## Country air operations

### Supported modifier scope

The generated official modifier catalogue places `air_accidents_factor` at
line 1497, `air_detection` at line 1557, `air_mission_efficiency` at line 1627,
and `air_weather_penalty` at line 1702. All four belong to the air category. It
does not list any of them as state-category modifiers. The offline Modifiers
reference at lines 5911 through 5930 limits strategic-region air modifiers to
static weather. The official `add_dynamic_modifier` effect at lines 1153
through 1169 supports country, state, character, and special-project scopes.
It does not support a strategic-region scope.

The country dynamic modifier is therefore the narrowest documented runtime
surface for these general air fields. Vanilla supplies variable-backed country
dynamic modifier precedents in:

- `common/dynamic_modifiers/aat_dynamic_modifiers.txt` for
  `air_mission_efficiency`, `air_accidents_factor`, and `air_weather_penalty`
- `common/dynamic_modifiers/bba_dynamic_modifiers.txt` for
  `air_accidents_factor`
- `common/dynamic_modifiers/mun_dynamic_modifiers.txt` for
  `air_weather_penalty`

Vanilla static weather also establishes the intended signs. Rain, snow, and
blizzard use negative `air_mission_efficiency` and `air_detection` values.
Country air-force defects use positive `air_accidents_factor` and
`air_weather_penalty` values. The Air Winter full-burden values follow those
signs.

### Working-airfield input

The official `non_damaged_building_level` trigger at lines 6554 through 6567
supports state scope and tests available building levels after damage. The
official dynamic-variable catalogue at lines 1139 through 1140 also exposes
`non_damaged_building_level@air_base`. Fallout already freezes that exact
dynamic variable in its pretransition state snapshot.

Air Winter copies each valid state's final phase and undamaged air-base level
before entering `CONTROLLER`. Temporary variables are deliberately unscoped,
so the controller contribution reads the copied phase without an invalid
scoped temporary-variable reference. A state contributes only when its
undamaged air-base level is above zero. Fully damaged winter closures therefore
leave the state out of the aggregate until the airfield becomes operational again.

Each contributing state adds one to the country count and adds its phase to the
phase sum. Addition is commutative, so state traversal order cannot alter the
result. The finalizer divides the sum by the count, then divides that mean by
the maximum phase. The burden is clamped from zero through one before it scales
the four shared constants.

The scaled values are:

| Modifier | Mean phase 1 | Mean phase 3 | Mean phase 6 |
| --- | ---: | ---: | ---: |
| Air mission efficiency | -5 percent | -15 percent | -30 percent |
| Air detection base value | -0.0417 | -0.125 | -0.25 |
| Air accidents factor | +3.33 percent | +10 percent | +20 percent |
| Air weather penalty | +2.5 percent | +7.5 percent | +15 percent |

`air_detection` is a flat base-detection modifier, not a multiplicative
factor. Its table row uses the fixed-point values written by the dynamic
modifier. The phase 1 values are ideal arithmetic before engine display
rounding.

### Bounded ownership and receipts

The existing monthly state pass registers both owners and controllers in
`global.air_winter_registered_countries`. Registration is deduplicated. No new
state or country world iterator is introduced.

`air_winter_air_operations_cycle_id` lazily resets the count and phase sum on
the first contribution of a new monthly cycle. The bounded finalizer calls the
same preparation helper for every registered country. This resets a stale row
when a country lost its final controlled airfield or received no state
contribution during the current cycle. The country modifier is removed when
there is no contribution, the mean phase is zero, or Air Cleanliness is
disabled.

`air_winter_air_operations_last_finalize_cycle_id` makes repeated country
finalization in the same cycle inert. The global monthly finalizer already has
its own date and cycle receipt. A changed variable-backed modifier is followed
by the official `force_update_dynamic_modifier` effect. Administrative reset
removes the modifier and clears every aggregate and receipt variable.

Fallout stops the ordinary Air Winter begin, state, and finalize calls while
its transition flag is active. The standard request path first builds and
validates the complete prelock snapshot. Only a lock-ready request sets
`fallout_transition_active`, clears the country modifier through the bounded
Air-owned registry, and schedules blackout. A failed prelock snapshot leaves
the modifier intact. `air_winter_begin_fallout_snapshot_production` repeats the
same narrow cleanup only when a transition is already active, which covers
snapshot recovery without clearing the state ledger needed by that snapshot.

### Static scenario audit

| Scenario | Required result | Script evidence |
| --- | --- | --- |
| A second finalize on the same date | No country value changes twice | The global cycle receipt blocks the second loop. The country cycle receipt independently blocks a repeated row. |
| A state changes controller between monthly passes | The current controller receives the state. The former controller loses stale burden. | State aggregation enters current `CONTROLLER`. The former controller remains in the persistent registry and receives a zeroed current-cycle row at finalize. |
| A country loses its final airfield state | Its modifier is removed | The finalizer prepares every registered country even when it received no contribution. |
| A winter closure damages all air-base levels | The state does not contribute | Aggregation reads `non_damaged_building_level@air_base` and requires a value above zero. |
| Every contributing airfield state is phase 0 | The modifier is removed | The mean and burden are zero even when the airfield count is positive. |
| Air Cleanliness is disabled | The modifier is removed | The country finalizer requires `air_winter_system_enabled`. |
| A Fallout request passes the complete prelock snapshot gate | Every registered country loses the modifier before blackout scheduling and before the monthly pass pauses | The request lock sets the transition flag, calls bounded Air-owned cleanup, then schedules the blackout phase. |
| A Fallout prelock snapshot fails | The Air Winter modifier remains active | Cleanup occurs only after the request is lock-ready or while recovering an already active transition. |
| State traversal order changes | The final burden is unchanged | Count and phase sum use only commutative addition before one final division. |

### Granularity boundary

The country modifier affects all air operations owned by that country. It is a
national burden derived from the complete set of working controlled airfields,
not a claim that the engine confines the four fields to their originating
strategic regions. No supported runtime dynamic modifier for that exact local
result was found.

## Combat and strategic-bombing pressure boundary

The official trigger catalogue at lines 2515 through 2523 documents
`days_since_last_strategic_bombing` in state scope. Vanilla uses it in
`events/MTG_Britain.txt` lines 8278 through 8281. Chaos Redux already uses the
same state fact for its separate strategic-bombing Deaths tick.

No documented state trigger reports an active ordinary land battle. Combat
weather and attacker facts require combatant scope. The official on-action list
has only `on_state_control_changed` under states at lines 68 through 69 and
post-combat leader callbacks at lines 75 through 80. Vanilla comments at
`common/on_actions/00_on_actions.txt` lines 5573 through 5595 expose the owner
country for those leader callbacks, not the fought state. There is no state
combat-start or combat-end callback that exposes that state. War status,
occupation, controller mismatch, and border-war predicates are not exact
substitutes.

Direct Air Winter pressure or mortality from active combat remains blocked by
that missing state surface. A second strategic-bombing multiplier is absent
because it would compound the existing bombing casualty tick and change the
accepted balance through pressure, building loss, and winter mortality at once.

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

A successful mountain-capital tunnel-school result writes
`air_winter_memory_tunnel_school_protection`. The monthly route applies its
constant-backed 0.90 multiplier after the ordinary exposure, food, shelter,
infrastructure, occupation, and adaptation result. The same exact-loss helper,
setting gate, reason, and returned applied amount remain in force. Failure and
cancelled branches do not receive the protection memory.

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
Deaths setting gates, the tunnel-school protection multiplier, the documented
state population mutation route, the
recruitable-credit reconciliation contract, and vanilla state usage of
controller attrition. It also proves country scope for the four air fields,
country dynamic-modifier application, working-airfield input, bounded
aggregation, duplicate-finalize protection, and transition cleanup. The exact
live state-population delta, controller and enemy attrition deltas, and country
air-operation modifier effects remain unobserved. The documented routes and
vanilla precedents are retained without a runtime claim.
