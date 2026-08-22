# US Special Chemical Projects

## Purpose and current status

The United States has two country-gated incapacitating-agent special projects:

1. `sp_cw_malodor_bomb_program`
2. `sp_cw_aphrodisiac_bomb_program`

The second stable identifier remains for compatibility, while final player-facing text calls it the Behavioral-Agent Aerosol Program. Both projects unlock production, aircraft-module, designer, and selected-state raid content. Their payloads emphasize disruption rather than conventional lethality, but they are not consequence-free: release attempts can create evidence, accepted releases use the shared Chemical exposure pipeline, and confirmed use records Condemnation. Chaos Warfare doctrine can reduce only the Condemnation impact.

## Unlock and logistics flow

1. Lewisite permits the Malodor Bomb Program.
2. Tabun and the completed Malodor project permit the Behavioral-Agent Aerosol Program.
3. Malodor completion unlocks `chem_air_bomb_malodor`, `malodor_agent_lot_1`, and the retained compatibility model `malodor_bomb_1`.
4. Behavioral-Agent completion unlocks `chem_air_bomb_behavioral`, `behavioral_agent_lot_1`, and the retained compatibility model `aphrodisiac_bomb_1`.
5. The supported conversion route turns the matching strategic-agent lot into `incapacitating_chemical_air_payload` only after the required air profile and line-change gates pass.
6. The matching rack can be fitted only to eligible CAS and tactical-bomber designs.
7. Each raid reserves 120 units of native incapacitating Chemical air payload as essential equipment and requires the exact matching rack, Chemical Air Interdiction, readiness, use policy, an eligible target state, and the shared Chemical raid preparation gates.

The compatibility project, equipment, and sprite identifiers remain stable so existing script consumers do not break. No approximate stock migration or duplicate free payload route is used.

## Active selected-state raids

The native raid definitions are active in `common/raids/cbrn_chemical_air_raids.txt`:

- `chemical_malodor_strike`
- `chemical_aphrodisiac_strike`

Both target an exact selected state. They use the same aircraft, intelligence, air-superiority, interception, anti-air, radar, reliability, and experience success model as the other Chemical air raids. Their four native result levels call dedicated thin wrappers:

- `cbrn_resolve_chemical_air_raid_malodor_outcome`
- `cbrn_resolve_chemical_air_raid_behavioral_outcome`

Those wrappers set only the agent identity and enter `cbrn_resolve_chemical_air_raid_outcome`. The shared adapter resolves the native payload reservation, verifies whether a release occurred, records the exact actor and target state, resolves protection, applies doctrine only to the Condemnation multiplier, prepares the common Chemical action record, and dispatches the common exposure consequences. Failed or aborted attempts use the shared attempted-use evidence and Condemnation record without fabricating target exposure.

## Outcome identity

Malodor emphasizes evacuation pressure, cohesion loss, entrenchment disruption, movement disruption, occupation-control strain, and sortie preparation. Behavioral Agent emphasizes uncertain command breakdown, coordination loss, reinforcement disorder, planning loss, and resilience penalties. Their accepted releases can create contamination and the full shared record when the common calculation produces those outputs. Neither profile suppresses evidence, attribution, use history, deaths, contamination, medical saturation, or public-harm floors.

No-release outcomes create no target deaths, contamination, medical saturation, mask loss, treaty-use record, confirmed-use history, or Chemical-use achievement. They can still record attempted-use evidence and Condemnation according to the shared failed-attempt table.

## Engine boundaries

The native raid scope proves target state, actor, victim, aircraft and module eligibility, interception, air defence, intelligence, air superiority, and essential-equipment reservation. The implementation derives release efficiency from the native result. It supplies no weather, terrain, forecast, or friendly-risk receipt because the current engine does not expose one to this outcome effect.

The ordinary continuous-air-mission surface still exposes no verified eligible-activity hook. Chemical-capable aircraft therefore produce no passive regional contamination, and idle aircraft can never contaminate a region.

Direct forced retreat and cancellation of an already-running attack are not exposed as reliable raid effects. No substitute is retained for those behaviors.

## Files and identifiers

- Projects: `common/special_projects/projects/chemical_special_projects.txt`
- Exact aircraft modules: `common/units/equipment/modules/chemical_air_bomb_modules.txt`
- Strategic-agent lots and native air payload: `common/units/equipment/cbrn_payload_equipment.txt`
- Raid definitions: `common/raids/cbrn_chemical_air_raids.txt`
- Raid gates: `common/scripted_triggers/cbrn_chemical_raid_triggers.txt`
- Shared reservation, failed-attempt, and release accounting: `common/scripted_effects/cbrn_chemical_raid_effects.txt`
- Shared Chemical exposure record: `common/scripted_effects/cbrn_exposure_effects.txt`
- State disruption: `common/dynamic_modifiers/chemical_special_raid_modifiers.txt`
- Special-project GFX: `interface/special_projects/biowarfare.gfx`
- Equipment GFX: `interface/chaosx_equipment.gfx`
- State-modifier GFX: `interface/chaosx_ideas.gfx`
- Localisation: `localisation/english/chaosx_special_projects_l_english.yml`, `localisation/english/chaosx_equipment_l_english.yml`, and `localisation/english/chaosx_raids_l_english.yml`

## Assets

The Malodor and Behavioral-Agent aircraft racks have independent type-correct module icons with source PNGs, processed PNGs, runtime DDS files, contact sheets, manifests, and GFX wiring under `docs/assets/chaos_warfare_system/stage_6_chemical_air_modules/`.

The project pictures, standalone payload technology art, and state-modifier icons use a separate six-asset workflow under `docs/assets/chaos_warfare_system/stage_6_incapacitating_agent_visible_assets/`. Each consumer type has an independent source and processed output; no special-project picture, technology image, or state-modifier icon is a resized cross-type substitute. Stable sprite identifiers remain unchanged while their final DDS files live in dedicated CBRN runtime folders.

## Validation still owned by the user

Live aircraft-designer module display, native raid eligibility, target selection, essential-equipment reservation, and visual outcome validation remain user-owned in-game checks. Source-level package validation does not claim those live observations.
