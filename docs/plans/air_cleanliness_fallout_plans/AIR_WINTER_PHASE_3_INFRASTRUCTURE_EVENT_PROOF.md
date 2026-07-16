# Air Winter Phase 3 Infrastructure Event Proof

## Implemented surface

The Phase 3 infrastructure tranche adds six manually authored event blocks to `events/fallout_world_end_events.txt`:

- `chaosx.fallout.22` and `.25` for Dam Ice Crisis
- `chaosx.fallout.26` and `.27` for Black Refinery Snow
- `chaosx.fallout.28` and `.29` for Cooling Pond Emergency

The opening ids are typed scheduler candidates. The result ids are direct delayed calls. Every opening has three choices, exact click-time validation, government-aware AI, ledger-aware AI, branch memory, a bound original owner, and a deterministic result. Every result exposes only the option matching its stored branch and outcome.

The tranche raises the Air Winter pilot from 35 to 41 blocks. It contains 119 options, of which 118 have effects. The remaining option is the existing effect-free stale-order acknowledgement.

## State-local routing

The inline Phase 3 block inside `air_winter_event_select_unseen_phase_route` checks the selected state in this order:

1. reactor
2. hydroelectric
3. oil or refinery
4. transport
5. clinic and heat

This order does not override country candidate scoring. The bounded scheduler still compares family priority, origin cycle, phase and pressure score, then state id. A transport state with a higher score can defeat a reactor state elsewhere in the country. The shared Phase 3 seen flag allows one ordinary Phase 3 chain per country.

## Building and resource predicates

The infrastructure identities run in state scope and require an operational building where damage can disable the route:

- hydroelectric uses `non_damaged_building_level` for `dam`, `dam_mountain`, and `cataract_dam_mountain`
- oil or refinery uses positive state oil or an operational `synthetic_refinery`
- reactor uses `non_damaged_building_level` for `nuclear_reactor`, `nuclear_reactor_heavy_water`, and `commercial_nuclear_reactor`

`fuel_silo` is not an eligibility identity. It is storage and can only be a fire-damage target. `nuclear_facility` is not eligible because it is a research facility rather than a reactor.

Installed engine references:

- `documentation/triggers_documentation.md`, `building_count_trigger`, documents state and country building counts and lists the three dam and reactor families
- `documentation/triggers_documentation.md`, `has_resources_amount`, documents the state resource predicate
- `documentation/triggers_documentation.md`, `non_damaged_building_level`, documents operational building checks
- vanilla `common/resistance_activity/resistance_activity.txt` checks and damages operational synthetic refineries and all three reactor families
- vanilla `common/raids/air_raids.txt` uses state oil predicates for oilfield targets

## Oil output and repairable damage

The Chaos-owned `air_winter_refinery_output_disruption_state` modifier uses the documented state field `state_resources_oil_factor`. It applies a 25 percent natural-oil penalty for the 21-day branch. A synthetic-only state would not respond to that resource modifier, so the opening also deals 0.25 repairable damage to an installed synthetic refinery.

Fire failure uses `damage_building` for an installed synthetic refinery, fuel silo, and infrastructure. This represents the accepted repairable incident rather than permanent removal.

Installed engine references:

- `documentation/modifiers_documentation.md`, `state_resources_<Resource>_factor`, documents state resource output factors and oil support
- vanilla `common/dynamic_modifiers/wuw_dynamic_modifiers.txt` defines oilfield damage tiers with `state_resources_oil_factor`
- vanilla `common/raids/air_raids.txt` applies those modifiers to oil states
- vanilla `common/resistance_activity/resistance_activity.txt` uses repairable `damage_building` against synthetic refineries and fuel silos

## Reactor energy and fallout

Emergency pumping applies the Chaos-owned `air_winter_reactor_emergency_power_demand_state` modifier. It raises `local_factory_energy_consumption` by 10 percent for no more than 31 days. The delayed success trigger also requires the country-scoped `energy_ratio` to remain above 50 percent. Manpower and support equipment pay for the plant crews, so country fuel is not used as a substitute for electricity.

A failed route damages one installed reactor family in a fixed order and local infrastructure. It then calls the existing clamped state fallout helper, raising intensity by up to 0.50 and ensuring Fallout remains for at least 180 days. That fallout enters the existing nuclear and Air Cleanliness ledgers. The event adds no Fallout grade coefficient and changes no global Air Contamination coefficient.

Installed engine references:

- `documentation/modifiers_documentation.md`, `local_factory_energy_consumption`, documents the state energy demand field
- `documentation/triggers_documentation.md`, `energy_ratio`, documents country energy fulfilment
- `documentation/effects_documentation.md`, `add_dynamic_modifier`, supports state scope
- vanilla `common/dynamic_modifiers/mun_dynamic_modifiers.txt` applies `local_factory_energy_consumption` in a state modifier
- vanilla `common/resistance_activity/resistance_activity.txt` provides reactor damage precedents

## Delayed ownership and Fallout isolation

Each opening writes its branch before `air_winter_event_refresh_state` binds the regular country target as `air_winter_pending_event_owner`. `air_winter_event_targets_are_valid` conditionally requires the stored owner whenever the generic pending flag exists. Every delayed result therefore fails closed if the country target, state target, ownership, owner variable, or branch is stale.

The same target trigger rejects `fallout_transition_active` and `fallout_active`. A click from an older popup can still cancel its matching branch, but the stale-order notice is suppressed during Fallout. During the existing `fallout_take_world_snapshot` state pass, all Air Winter values are frozen before `air_winter_event_cancel_pending_chain` clears branch flags and temporary refinery or reactor modifiers. This adds no state or country iterator. A result that arrives after the snapshot cannot mutate the frozen row.

Installed engine references:

- `documentation/effects_documentation.md`, `save_event_target_as`, documents regular event targets
- `documentation/triggers_documentation.md`, `has_event_target`, documents target presence checks
- the offline Data structures page documents regular target propagation into events fired by the same effect chain
- `documentation/effects_documentation.md`, `every_state`, documents the existing snapshot iterator used for cleanup

## Deterministic AI boundaries

Pre-choice AI thresholds include the exact opening ledger changes before testing the delayed result:

- dam crews require pre-choice Water Security 32 and Reclamation 21
- full-head operation requires pre-choice Adaptation 28 and Building Damage Pressure no more than 45
- military refinery output requires pre-choice Adaptation 31 and Building Damage Pressure no more than 35
- reactor scram requires pre-choice Water Security 48 and national Energy Fulfilment above 60 percent
- reduced reactor output requires pre-choice Adaptation 41 and Building Damage Pressure no more than 40
- the plant council requires pre-choice Adaptation 44 and Water Security 40

The state-ledger values are derived from the disclosed result thresholds and exact opening deltas. The reactor's 60 percent AI energy floor is a conservative buffer above the 50 percent result threshold. It accounts for the route's own 10 percent local demand increase and later live grid movement. Government and war modifiers remain separate, so ideology does not erase mechanical feasibility. Unaffordable options are absent and their exact costs are repeated in the click guard.

## Assets and text

All six blocks use `GFX_report_event_air_winter_phase_3`. The sprite is registered in `interface/air_cleanliness_winter.gfx` and its DDS is present under the dedicated Fallout and Air Winter path. The asset manifest maps `chaosx.fallout.20` through `.29` to the shared Phase 3 image.

All titles, descriptions, choices, result descriptions, and tooltips are present in the Fallout event localisation file. The text names the affected state, varies authority language through Air Winter scripted localisation, and describes actual resource, building, energy, casualty, and ledger consequences.

## Runtime boundary

Static source review proves the wiring, typed ids, building predicates, modifier categories, option guards, pending-owner transaction, snapshot cleanup order, and asset registration. It does not prove popup presentation, delayed regular-target retention, AI behavior, modifier behavior, or save recovery in a live session. Hearts of Iron IV was not launched, and no runtime claim is made.

An optional narrow `hoi4.event_inspect` lint request for `chaosx.fallout.22` returned `ARTIFACT_STORAGE_LIMIT` with zero artifacts. It produced no source diagnostic and is not used as evidence.
