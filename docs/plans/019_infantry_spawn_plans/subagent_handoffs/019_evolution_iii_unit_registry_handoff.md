# Event 019 Evolution III ordinary unit registry handoff

## Scope and ownership

This handoff covers only the Evolution III ordinary unit registry and its
manifest materializer. The implementation is contained in:

- `common/script_constants/019_infantry_spawn_unit_registry_constants.txt`
- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`
- `common/scripted_triggers/019_infantry_spawn_unit_registry_triggers.txt`

No management decision, event, localisation, asset, or claimant file was
edited. The parent implementation owns those call sites and claimant demand
attachment.

## Required references consulted

The implementation was checked against the required offline wiki core pages,
including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes,
On actions, Event modding, Decision modding, Idea modding, AI modding, Division
modding, Technology, and Unit modding. It was also checked against the installed
vanilla documentation for script concepts and constants, effects, triggers,
collections, unit definitions, technologies, doctrines, and special projects.

The dynamic template append path mirrors vanilla's documented
`add_units_to_division_template` effect and the existing Event 19
`Unbidden Muster [TEMPLATE_UID]` template/spawn contract.

## Registry coverage

The aligned registry contains 87 executable rows:

- 45 combat rows, including `irregular_infantry` behind the explicit
  `infantry_spawn_unit_registry_allow_irregular_infantry` country flag.
- 42 support rows.
- `fake_intel_unit` and `bus` remain enumerated for audit continuity but have no
  registry row, token provider, gate provider, or obligation provider.
- Every installed `active = no` row has an exact country-side unlock gate.
  Installed `active = yes` rows remain structurally eligible and can therefore
  produce technology-locked or unresolved-variant outcomes without granting a
  technology.
- All three `same_support_type` columns are preserved. Helicopter pair names in
  the registry are normalized enum labels for the exact installed conflict
  tokens.

Selection scans the complete eligible table each time. It is not capped to a
short candidate sample. Combat layouts remain within five columns by five rows,
with 1–25 combat components and 0–5 support components. Material quality and
coherence are rolled independently, then request mode, request context, muster
control, congestion, and prior request count shape the weights.

## Public draw hooks

### Evolution III opening draw

Call:

```txt
infantry_spawn_unit_registry_draw_evolution_iii_opening_lot = yes
```

The hook sets:

- `infantry_spawn_unit_registry_request_mode` to
  `constant:infantry_spawn_request_mode.unrestricted`
- `infantry_spawn_unit_registry_request_context` to
  `constant:infantry_spawn_unit_registry_request_context.evolution_iii_opening`
- `infantry_spawn_unit_registry_request_command_owner` to
  `constant:infantry_spawn_command_owner.state`

The caller must already be in the generation country scope and must save both:

```txt
save_event_target_as = infantry_spawn_generation_country
# In a selected eligible controlled state scope:
save_event_target_as = infantry_spawn_current_origin_state
```

The draw and materializer must run in the same effect chain because the registry
tables, manifest, result counters, and outcome tags are temporary.

### Requested ordinary draw

Before calling:

```txt
infantry_spawn_unit_registry_draw_requested_lot = yes
```

set these temporary inputs:

```txt
set_temp_variable = {
	var = infantry_spawn_unit_registry_request_mode
	value = constant:infantry_spawn_request_mode.<ordinary_mode>
}
set_temp_variable = {
	var = infantry_spawn_unit_registry_request_context
	value = constant:infantry_spawn_unit_registry_request_context.<context>
}
```

Accepted ordinary modes are `field_reinforcement`, `mobile_reserve`,
`territorial_defense`, `specialist`, `unrestricted`, `numbers`, `discipline`,
`firepower`, `mobility`, and `anything`. `anomalous` is deliberately rejected by
this ordinary registry.

The draw fails closed with an `invalid_origin`, `invalid_request`, or
`manifest_incomplete` outcome tag. It never substitutes another state, unit
family, request mode, or template.

## Draw outputs

A successful draw returns aligned
`infantry_spawn_unit_registry_manifest_*` temporary arrays and these counters:

- `infantry_spawn_unit_registry_result_combat_count`
- `infantry_spawn_unit_registry_result_support_count`
- `infantry_spawn_unit_registry_result_distinct_group_count`
- `infantry_spawn_unit_registry_result_distinct_equipment_profile_count`
- `infantry_spawn_unit_registry_result_compatibility_mismatch_count`
- `infantry_spawn_unit_registry_result_mobility_mismatch_count`
- `infantry_spawn_unit_registry_result_incoherence_score`
- `infantry_spawn_unit_registry_result_heavy_supply_component_count`
- `infantry_spawn_unit_registry_result_extreme_supply_component_count`
- `infantry_spawn_unit_registry_result_max_supply_burden`
- `infantry_spawn_unit_registry_result_finite_risk_component_count`
- `infantry_spawn_unit_registry_result_project_equipment_component_count`
- `infantry_spawn_unit_registry_result_technology_locked_component_count`
- `infantry_spawn_unit_registry_result_unresolved_variant_component_count`

`infantry_spawn_unit_registry_outcome_tag_ids` always contains exactly one of
`coherent`, `strained`, or `incoherent` after a successful draw. It can also
contain `bloated`, `tiny`, `technology_locked`,
`equipment_variant_unresolved`, `heavy_supply`, `project_equipment`, and
`mobility_mismatch`. `draw_complete` is the positive draw contract.

Each new draw clears the previous result arrays, materialized UID outputs, and
`infantry_spawn_unit_registry_materialization_succeeded` country flag.

## Materialization contract

Call:

```txt
infantry_spawn_unit_registry_materialize_drawn_lot = yes
```

The materializer requires:

- a successful unconsumed draw with `draw_complete`
- all 16 non-base manifest arrays aligned to `manifest_token_ids`
- the country-safe origin event targets described above
- `infantry_spawn_current_generation_uid` pointing to an existing generation
  ledger row whose status is `open` or `audited`
- all Event 19 ledgers aligned and no ledger invariant failure
- a context-compatible `infantry_spawn_unit_registry_request_command_owner`

Command-owner compatibility is:

- opening: `state`
- country request: `state` or `local_authority`
- claimant request: `claimant_one`, `claimant_two`, or `claimant_three`
- scripted scenario: any of the preceding non-family owners

The materializer performs this bounded sequence:

1. Loads the existing generation ledger row, reopens its audit status, and
   keeps the country audit flag active.
2. Allocates one lot UID and one template UID.
3. Maps registry quality, coherence, supply burden, and mobility mismatch to the
   existing Event 19 lot fields and readiness factors.
4. Creates `Unbidden Muster [TEMPLATE_UID]` from the first combat row, then
   appends every remaining combat/support row with
   `add_units_to_division_template`.
5. Verifies the engine template, appends every exact component row, and confirms
   the component ledger counts equal the scored manifest.
6. Appends the lot, template, and selected-state rows.
7. Calls the existing transactional
   `infantry_spawn_spawn_current_template_unit` helper for one formation.
8. Appends the exact extended resource obligations, marks technology-locked
   arrays/flags when applicable, and updates the generation totals.
9. Resolves the exact lot row and returns the materialization outputs.

The lot uses the disjoint profile
`constant:infantry_spawn_unit_registry_lot_profile.evolution_iii_random`
(`3190`), so the legacy 300–399 prototype-grant branch is not entered. The
registry never grants technologies or prototype equipment.

Successful outputs are:

- `infantry_spawn_unit_registry_materialized_lot_uid`
- `infantry_spawn_unit_registry_materialized_lot_index`
- `infantry_spawn_unit_registry_materialized_template_uid`
- `infantry_spawn_unit_registry_materialized_unit_uid`
- `constant:infantry_spawn_unit_registry_outcome_tag.materialized` in the
  outcome array
- country flag `infantry_spawn_unit_registry_materialization_succeeded`

Before success, every UID/index output is the registry `missing_index` value.
Invalid generation context returns `invalid_generation_context` plus
`materialization_failed`. Other rejected materializations return
`materialization_failed`. A manifest carrying `materialized` cannot be consumed
again.

### Opening caller setup

Opening generation-row creation is caller-owned. The opening draw does not
allocate or append a generation row. The caller must:

1. Create or select the Event 19 generation and set
   `infantry_spawn_current_generation_uid` to its existing ledger UID.
2. Save `infantry_spawn_generation_country` in the country scope.
3. Select one state that passes `infantry_spawn_state_is_eligible`, is controlled
   by that country, and save it as `infantry_spawn_current_origin_state`.
4. Call `infantry_spawn_unit_registry_draw_evolution_iii_opening_lot`.
5. Check `draw_complete`, then call
   `infantry_spawn_unit_registry_materialize_drawn_lot` in the same chain.
6. Treat the opening as committed only when
   `infantry_spawn_unit_registry_materialization_succeeded` is set.

The exact opening call skeleton is:

```txt
# COUNTRY scope. infantry_spawn_current_generation_uid must already contain
# the UID of an existing open or audited Event 19 generation row.
save_event_target_as = infantry_spawn_generation_country

# Run in the caller-selected eligible, country-controlled STATE scope.
save_event_target_as = infantry_spawn_current_origin_state

# Return to the same COUNTRY scope and remain in this effect chain.
infantry_spawn_unit_registry_draw_evolution_iii_opening_lot = yes
if = {
	limit = {
		is_in_array = {
			array = infantry_spawn_unit_registry_outcome_tag_ids
			value = constant:infantry_spawn_unit_registry_outcome_tag.draw_complete
		}
	}
	infantry_spawn_unit_registry_materialize_drawn_lot = yes
}
if = {
	limit = {
		has_country_flag = infantry_spawn_unit_registry_materialization_succeeded
	}
	# Commit the caller-owned opening follow-up here.
}
```

The two `save_event_target_as` effects, the draw, and materialization must remain
inside one originating effect chain. The opening helper itself sets unrestricted
mode, opening context, and state command ownership. It does not create the
generation row.

### Claimant-request caller setup

For a claimant request, the parent caller must:

1. Create/select an open or audited generation row and set its UID as above.
2. Save the generation country and selected safe origin state event targets.
3. Set the requested ordinary mode.
4. Set request context to
   `constant:infantry_spawn_unit_registry_request_context.claimant_request`.
5. Map the requesting claimant slot to exactly one of
   `constant:infantry_spawn_command_owner.claimant_one`, `claimant_two`, or
   `claimant_three` and store it in
   `infantry_spawn_unit_registry_request_command_owner`.
6. Call `infantry_spawn_unit_registry_draw_requested_lot`, require
   `draw_complete`, then call
   `infantry_spawn_unit_registry_materialize_drawn_lot` in the same chain.
7. Only after the success flag/tag, attach the demand using
   `infantry_spawn_unit_registry_materialized_lot_uid` and the matching
   `infantry_spawn_unit_registry_materialized_lot_index`.

The registry does not attach a claimant UID or mutate claimant demand ledgers;
that remains caller-owned so failed materialization cannot leave a claimant
pointing at a missing lot.

The exact claimant-request call skeleton is:

```txt
# COUNTRY scope. infantry_spawn_current_generation_uid must already contain
# the UID of an existing open or audited Event 19 generation row.
save_event_target_as = infantry_spawn_generation_country

# Run in the caller-selected eligible, country-controlled STATE scope.
save_event_target_as = infantry_spawn_current_origin_state

# Return to the same COUNTRY scope and remain in this effect chain.
set_temp_variable = {
	var = infantry_spawn_unit_registry_request_mode
	value = constant:infantry_spawn_request_mode.<ordinary_mode>
}
set_temp_variable = {
	var = infantry_spawn_unit_registry_request_context
	value = constant:infantry_spawn_unit_registry_request_context.claimant_request
}
set_temp_variable = {
	var = infantry_spawn_unit_registry_request_command_owner
	value = constant:infantry_spawn_command_owner.<claimant_one|claimant_two|claimant_three>
}
infantry_spawn_unit_registry_draw_requested_lot = yes
if = {
	limit = {
		is_in_array = {
			array = infantry_spawn_unit_registry_outcome_tag_ids
			value = constant:infantry_spawn_unit_registry_outcome_tag.draw_complete
		}
	}
	infantry_spawn_unit_registry_materialize_drawn_lot = yes
}
if = {
	limit = {
		has_country_flag = infantry_spawn_unit_registry_materialization_succeeded
	}
	# Attach the caller-owned claimant demand using the returned lot UID/index.
}
```

The angle-bracket tokens are caller substitutions, not literal script tokens.
Each draw clears the success flag first, so
`has_country_flag = infantry_spawn_unit_registry_materialization_succeeded` is
the final commit gate. The `materialized` outcome tag is corroborating output.

## Exact obligation coverage

The existing Event 19 ordinary obligation scanner already supplied 21 exact
manpower/equipment providers. This implementation supplies the other 66 under
the same dynamic provider contract, giving one provider for every registered
row with no duplicate provider identifiers. Shared equipment families feed the
existing accumulators. Thirty equipment types absent from the shared enum use
the registry's disjoint resource-profile IDs 100–129; rocket artillery uses the
existing shared resource profile.

The quantities mirror installed vanilla `manpower` and `need` blocks. Existing
Event 19 providers continue to add their already-modelled fuel liability where
defined; no fuel amount was invented for the newly supplied providers.

Exact need sources under the installed vanilla directory are:

- `common/units/amphibious_armor.txt`: `amphibious_armor`, `amphibious_light_armor`, `amphibious_medium_armor`, `amphibious_heavy_armor`
- `common/units/amphibious_mech.txt`: `amphibious_mechanized`
- `common/units/anti-air.txt`: `anti_air`
- `common/units/anti-air_brigade.txt`: `anti_air_brigade`, `mot_anti_air_brigade`
- `common/units/anti_tank.txt`: `anti_tank`
- `common/units/anti_tank_brigade.txt`: `anti_tank_brigade`, `mot_anti_tank_brigade`
- `common/units/armored_car_battalion.txt`: `armored_car`
- `common/units/artillery.txt`: `artillery`, `rocket_artillery`, `super_heavy_artillery`, `self_propelled_super_heavy_artillery`
- `common/units/artillery_brigade.txt`: `artillery_brigade`, `rocket_artillery_brigade`, `mot_artillery_brigade`, `mot_rocket_artillery_brigade`, `motorized_rocket_brigade`
- `common/units/blackshirt_assault_battalion.txt`: `blackshirt_assault_battalion`
- `common/units/cavalry.txt`: `cavalry`, `camelry`, `elephantry`
- `common/units/engineer.txt`: `engineer`, `pioneer_support`, `jungle_pioneers_support`, `assault_engineer`, `armored_engineer`
- `common/units/field_hospital.txt`: `field_hospital`, `helicopter_field_hospital`
- `common/units/flame_tank.txt`: `light_flame_tank`, `medium_flame_tank`, `heavy_flame_tank`
- `common/units/heavy_armor.txt`: `heavy_armor`
- `common/units/helicopter_brigade.txt`: `helicopter_brigade`
- `common/units/infantry.txt`: `infantry`, `bicycle_battalion`, `marine`, `marine_commando`, `mountaineers`, `ranger_battalion`, `paratrooper`, `penal_battalion`, `irregular_infantry`, `militia`, `motorized`, `mechanized`
- `common/units/land_cruiser.txt`: `land_cruiser`
- `common/units/light_armor.txt`: `light_armor`
- `common/units/logistics.txt`: `logistics_company`, `helicopter_transport`
- `common/units/maintenance.txt`: `maintenance_company`, `armored_maintenance`
- `common/units/medium_armor.txt`: `medium_armor`
- `common/units/military_police.txt`: `military_police`, `motorized_military_police`
- `common/units/modern_armor.txt`: `modern_armor`
- `common/units/recon.txt`: `recon`, `mot_recon`, `armored_car_recon`, `light_tank_recon`, `airborne_light_armor`, `rangers_support`, `northern_territory_recon_support`, `winter_logistics_support`, `long_range_patrol_support`, `helicopter_recon`
- `common/units/signal.txt`: `signal_company`, `armored_signal`
- `common/units/sp_anti-air_brigade.txt`: `light_sp_anti_air_brigade`, `medium_sp_anti_air_brigade`, `heavy_sp_anti_air_brigade`, `modern_sp_anti_air_brigade`, `super_heavy_sp_anti_air_brigade`
- `common/units/sp_artillery_brigade.txt`: `light_sp_artillery_brigade`, `medium_sp_artillery_brigade`, `heavy_sp_artillery_brigade`, `modern_sp_artillery_brigade`, `super_heavy_sp_artillery_brigade`
- `common/units/sturmtruppe_battalion.txt`: `sturmtruppe_battalion`
- `common/units/super_heavy_armor.txt`: `super_heavy_armor`
- `common/units/tank_destroyer_brigade.txt`: `light_tank_destroyer_brigade`, `medium_tank_destroyer_brigade`, `heavy_tank_destroyer_brigade`, `super_heavy_tank_destroyer_brigade`

## Validation evidence

- All 15 source registry arrays contain 87 rows and pass the shared alignment
  trigger.
- Token providers: 87 unique. Gate providers: 87 unique. The union of the 21
  existing and 66 registry obligation providers is exactly the same 87 IDs,
  with no duplicates or gaps.
- The 66 added exact-need constant groups were compared field-for-field with
  the installed unit definitions; every manpower/equipment value matched.
- Installed enumeration comparison found 47 normal combat and 42 support
  definitions. The executable registry intentionally resolves this to 45
  combat plus 42 support by excluding only `fake_intel_unit` and `bus`.
- All 42 support rows were compared with all installed `same_support_type`
  entries, including the normalized helicopter conflict groups.
- Every `active = no` unit row has a nontrivial gate and every `active = yes`
  unit row has an unconditional structural gate. Technology, doctrine, and
  special-project identifiers were resolved against the installed game data.
- All constant references and all scripted effect/trigger calls in the owned
  files resolve. The owned top-level script names have no cross-file
  duplicates.
- The materializer uses the installed documented COUNTRY-scope append effect,
  exact token `GetTokenKey` expansion, the existing Event 19 ledger appenders,
  and the existing transactional single-formation spawn helper.

## Simplifications, omissions, and blockers

No fallback, placeholder unit, shortened registry, technology grant, prototype
grant, hard candidate cap, or obligation approximation was used. There are no
player-facing strings or assets in this internal registry surface, so no
localisation or visual asset was required here. Final management/event call-site
wiring and claimant demand attachment remain with the parent-owned files by
design; the public contract above is complete for that wiring.
