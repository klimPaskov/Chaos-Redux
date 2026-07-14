# US Special Chemical Projects

## Purpose and current status

The United States has two country-gated chemical special projects:

1. `sp_cw_malodor_bomb_program`
2. `sp_cw_aphrodisiac_bomb_program`

The second stable identifier is retained for compatibility, but final player text identifies its payload as an experimental Behavioral Agent. Both concepts belong to the incapacitating-agent family. They are disruption weapons, not zero-consequence alternatives to lethal agents: every attempted operation can create evidence, and every confirmed release enters the shared Chemical Condemnation pipeline. Integrated CBRN Command may reduce only the Condemnation impact.

The production and aircraft-design foundation is implemented. The selected-state release routes are not active yet. Their direct legacy raid definitions are fail-closed until they can consume exact native payload reservations and use the shared exposure record without a weather or terrain fallback.

## Unlock and logistics flow

1. `Lewisite` permits the Malodor Bomb Program.
2. `Tabun (GA)` and the completed Malodor project permit the Behavioral-Agent project.
3. Malodor completion unlocks `chem_air_bomb_malodor`, `malodor_agent_lot_1`, and the retained compatibility model `malodor_bomb_1`.
4. Behavioral-Agent completion unlocks `chem_air_bomb_behavioral`, `behavioral_agent_lot_1`, and the retained compatibility model `aphrodisiac_bomb_1`.
5. The exact strategic-agent lot can be converted into the incapacitating air-payload class only when the selected air profile and line-change gates permit it.
6. The matching rack may be fitted only to CAS and tactical-bomber designs. Strategic bombers are not eligible.
7. A future active raid must prove the exact matching module, profile, 120-unit native payload reservation, policy, readiness, selected state, and accepted condition inputs before release.

The two compatibility bomb models remain enabled only because old consumers have not all been retired. The idempotent payload-stock migration must not run until those references are gone.

## Stable raid identifiers

- `chemical_malodor_strike`
- `chemical_aphrodisiac_strike`

Both IDs remain parse-safe but currently have `always = no` in `visible`, `available`, and `launchable`. Their legacy direct outcomes bypass the shared exposure record and therefore cannot be launched. Final replacements must preserve these IDs or provide explicit compatibility wrappers.

## Accepted outcome identity

Malodor emphasizes evacuation pressure, cohesion loss, entrenchment disruption, movement disruption, occupation-control strain, and sortie preparation. Behavioral Agent emphasizes uncertain command breakdown, coordination loss, reinforcement disorder, planning loss, and resilience penalties. Neither profile is permitted to claim immunity from evidence or Condemnation.

For either route:

- Aborted attempts consume 10–25 percent of the reserved payload and leave a small latent evidence trace.
- Failed attempts consume 40–80 percent, create no target exposure, and establish at least the aircraft-wreckage evidence floor.
- Partial, successful, and catastrophic outcomes must pass through the shared exposure calculator and exact-state consequence dispatcher.
- No-release outcomes create no deaths, contamination, medical saturation, mask loss, treaty-use record, confirmed-use history, or chemical-use achievement.

## Engine boundaries

The current raid scope proves target state, actor, victim, aircraft/module eligibility, interception, air defence, intelligence, air superiority, and native essential-equipment reservation. It does not expose a verified live target-state weather or terrain trigger. The active release route therefore remains fail-closed pending an explicit user decision on a disclosed forecast model or a verified engine hook. No neutral multiplier, deployed-aircraft estimator, continuous-mission approximation, or idle-aircraft contamination path is retained.

Direct forced retreat and cancellation of an already-running attack are also not exposed as reliable raid effects. No substitute has been retained for those behaviors.

## Files and identifiers

- Projects: `common/special_projects/projects/chemical_special_projects.txt`
- Exact modules: `common/units/equipment/modules/chemical_air_bomb_modules.txt`
- Strategic and air payload equipment: `common/units/equipment/cbrn_payload_equipment.txt`
- Native reservation and failed-attempt accounting: `common/scripted_effects/cbrn_chemical_raid_effects.txt`
- Legacy fail-closed raids: `common/raids/chemical_special_raids.txt`
- Equipment GFX: `interface/chaosx_equipment.gfx`
- Localisation: `localisation/english/chaosx_special_projects_l_english.yml`, `localisation/english/chaosx_equipment_l_english.yml`, and `localisation/english/chaosx_raids_l_english.yml`

## Assets and unresolved visual work

The Malodor and Behavioral-Agent aircraft racks have independent type-correct module icons with source PNG, processed PNG, runtime DDS, archive DDS, contact sheet, manifest, and GFX wiring under `docs/assets/chaos_warfare_system/stage_6_chemical_air_modules/`. Their runtime sprites are `GFX_EMI_chem_air_bomb_malodor` and `GFX_EMI_chem_air_bomb_behavioral`; neither reuses a generic bomb-lock or another agent's concept.

The older project pictures, standalone bomb-equipment icons, and state-modifier icons still include legacy placeholder or prototype assets. They are unresolved and cannot be counted as final package art. The special-project reward definitions also still reference `GFX_PLACEHOLDER_sp_project_picture`. All of those surfaces require dedicated final assets before completion.

## Remaining implementation

1. Replace the fail-closed raid bodies with exact selected-state shared-pipeline routes after the condition-input decision is resolved.
2. Retire the compatibility bomb consumers, run exact stock migration, and remove duplicate active equipment families.
3. Rebuild the Malodor and Behavioral state effects through shared calculated outputs rather than legacy direct formulas.
4. Run live aircraft-designer and exact-module raid-eligibility scenarios.
5. Add route-aware US AI, final project/reward/raid/state art, final sounds where mapped, localisation audit, decision/raid audit, balance scenarios, and completion audit.
