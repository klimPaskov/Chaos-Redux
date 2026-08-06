# Event 012 strange formation gameplay handoff

Date: 2026-08-06

## Outcome

The assigned gameplay database package now defines eight distinct inactive subunits, sixteen gated equipment definitions, eight hidden bridge technologies, and a shared tuning contract for parent-owned stockpile and formation consumers. The package gate remains untouched and no readiness setter was added.

The package is not runtime-complete until the parent wires the hidden technologies into the action and route effects, registers each `division_template` consumer, installs the model/entity/GFX/counter/icon surfaces, and performs live-consumer validation after the model package is accepted.

## Files changed

- `common/units/012_africa_strange_forces.txt`
- `common/units/equipment/012_africa_strange_force_equipment.txt`
- `common/technologies/012_africa_strange_force_technologies.txt`
- `common/script_constants/012_africa_strange_force_constants.txt`

The constants file contains the eight-unit formation cap, package-gate requirement, parent-owned stockpile targets, and starting equipment/manpower/experience factors. It does not set or clear any flag.

## Stable gameplay identifiers

| Subunit | Role and identity | Width | Strength / organisation | Speed modifier | Supply / manpower | Core combat profile | Equipment archetype and variant | Bridge technology |
|---|---|---:|---:|---:|---:|---|---|---|
| `gorilla_heavy_infantry` | Gorilla Kingdom heavy forest and mountain shock | 4 | 42 / 45 | 0.20 | 0.070 / 720 | Soft 6, hard 4, breakthrough 14, defence 10, armour 24, piercing 20, hardness 0.28 | `africa_gorilla_heavy_infantry_equipment` / `_1` | `africa_gorilla_heavy_infantry_tech` |
| `pan_sappers` | Pan engineering and sabotage support | 0 | 8 / 1 | 0.10 | 0.040 / 480 | Soft 1, hard 1, breakthrough 4, defence 2, entrenchment 4, recon 1 | `africa_pan_sappers_equipment` / `_1` | `africa_pan_sappers_tech` |
| `stone_cohorts` | Stoneborn slow, hard siege and defence | 3 | 48 / 32 | -0.30 | 0.095 / 1100 | Soft 7, hard 8, breakthrough 10, defence 18, armour 72, piercing 48, hardness 0.86 | `africa_stone_cohorts_equipment` / `_1` | `africa_stone_cohorts_tech` |
| `riverborn` | Living Rivers wet-terrain and crossing infantry | 2 | 30 / 38 | 0.35 | 0.052 / 600 | Soft 5, hard 2, breakthrough 12, defence 14, armour 10, piercing 18, hardness 0.18 | `africa_riverborn_equipment` / `_1` | `africa_riverborn_tech` |
| `forest_giants` | The Green heavy ecological company | 5 | 54 / 38 | -0.15 | 0.112 / 1800 | Soft 8, hard 6, breakthrough 18, defence 16, armour 34, piercing 30, hardness 0.45 | `africa_forest_giants_equipment` / `_1` | `africa_forest_giants_tech` |
| `oracle_recon` | Ancient Hosts or Oracle network recon support | 0 | 6 / 1 | 0.25 | 0.025 / 420 | Soft 1, hard 0, breakthrough 2, defence 3, recon 4, initiative 1.10 | `africa_oracle_recon_equipment` / `_1` | `africa_oracle_recon_tech` |
| `disaster_wardens` | Natural-disaster and ecological containment support | 0 | 8 / 1 | 0.05 | 0.040 / 900 | Soft 2, hard 0, breakthrough 1, defence 5, entrenchment 3, suppression 2.50 | `africa_disaster_wardens_equipment` / `_1` | `africa_disaster_wardens_tech` |
| `plague_carriers` | Disease high-chaos pressure formation | 2 | 20 / 24 | 0.10 | 0.050 / 300 | Soft 6, hard 2, breakthrough 8, defence 8, piercing 12, hardness 0.08 | `africa_plague_carriers_equipment` / `_1` | `africa_plague_carriers_tech` |

All eight subunits are `active = no` and consume their own `_1` variant through `need`. Support entries use `type = { infantry support }`, `group = support`, `regimental = no`, zero combat width, and distinct `same_support_type` locks where appropriate. Terrain modifiers are intentionally asymmetric so the units have route identities instead of being interchangeable copies.

The unit-level `maximum_speed` values are equipment-speed bonus multipliers, not absolute kilometre-per-hour values. The `stone_cohorts` value of `-0.30` therefore deliberately produces 70% of its equipment speed and follows the offline Unit Modding wiki formula and vanilla elephantry precedent.

## Parent-owned formation/template consumers

The `division_template` blocks belong in the parent-owned Event 012 action, route, and actor effects. They must be created only after the global package gate and the corresponding hidden bridge technology are available, and they must not silently fall back to generic infantry when the required custom subunit is unavailable.

| Suggested template display name | Required subunit slot | Intended consumer | Current direct action status |
|---|---|---|---|
| `Africa Strange Stone Cohorts` | One or more `stone_cohorts` regimental slots | Stoneborn relic-site formation, Action 74 `awaken_stone_cohort`, and the achievement 40 Stoneborn constitutional route | Direct action 74 is already gate-validated; template creation and technology grant remain parent work. |
| `Africa Strange Gorilla Heavy Infantry` | One or more `gorilla_heavy_infantry` regimental slots | Gorilla Kingdom shock formation and Action 75 `train_gorilla_heavy_infantry` | Direct action 75 is already gate-validated; template creation and technology grant remain parent work. |
| `Africa Strange Pan Sappers` | A `pan_sappers` support slot attached to a Pan formation | Pan engineering and Action 76 `organise_pan_sappers` | Direct action 76 is already gate-validated; template creation and technology grant remain parent work. |
| `Africa Strange Riverborn` | One or more `riverborn` regimental slots | Living Rivers flood-control, crossing, and water-route consumers | No direct action exists; create only from the Living Rivers package consumer. |
| `Africa Strange Forest Giants` | One or more `forest_giants` regimental slots | The Green ecological covenant and forest-rampage consumers | No direct action exists; create only from The Green package consumer. |
| `Africa Strange Oracle Recon` | An `oracle_recon` support slot | Ancient Hosts or Oracle network route | No direct action exists; create only from the Oracle/Ancient Hosts package consumer. |
| `Africa Strange Disaster Wardens` | A `disaster_wardens` support slot | Natural-disaster response and ecological containment | No direct action exists; create only from the approved disaster/covenant consumer. |
| `Africa Strange Plague Carriers` | One or more `plague_carriers` regimental slots | Disease high-chaos route | No direct action exists; create only from the disease route consumer. |

Parent effects should apply the shared `africa_strange_force.formation_equipment_factor`, `formation_manpower_factor`, and `formation_experience_factor` values when creating units. They should enforce the eight-formation cap and record a one-time or cooldown disposition so an action cannot loop free units.

## Gate and model crosswalk

The production and hidden bridge gates use `africa_strange_formation_package_ready`. None of the four assigned files sets that global flag. The gate must remain closed while any model, entity, animation, counter, icon, or rights review is missing.

Reserved subunit sprite tokens are `chaosx_gorilla_heavy_infantry`, `chaosx_pan_sappers`, `chaosx_stone_cohorts`, `riverborn`, `chaosx_forest_giants`, `chaosx_oracle_recon`, `disaster_wardens`, and `plague_carriers`. The gorilla, Pan, stone, forest, and oracle tokens mirror the reserved model handoff consumer/entity bases; the riverborn, disaster, and plague tokens intentionally reserve stable names until their entity packages exist. No vanilla or generic sprite fallback is authorized.

The equipment sprite tokens are `africa_<subunit_id>_equipment` and require parent-owned GFX registration. Unit text icons, technology icons, counter DDS files, entity `.asset` and `.gfx` definitions, sound definitions, and localisation are outside this subagent ownership and remain pending.

## Required parent follow-up

1. Confirm that all sixteen equipment IDs remain present in `common/script_enums.txt` under the appropriate equipment enum before claiming the package is load-ready. The IDs are present in the current shared tree; this subtask did not edit that parent-owned file.
2. Grant each hidden bridge technology from the owning action or route effect after checking the global package gate and the model/entity manifest.
3. Create and consume the eight templates above with `division_template`, including model `override_model` only where the accepted entity handoff provides it.
4. Add the required unit and technology icon/localisation/GFX registrations and preserve the no-fallback policy.
5. Run the parent-owned gameplay, GFX, entity, and live-consumer audits; do not set `africa_strange_formation_package_ready` merely because the database definitions load.

## Validation and limitations

Static validation for this handoff covers identifier cross-references, brace balance, duplicate equipment and technology names, one-entry enum coverage for all sixteen equipment IDs in the current shared `common/script_enums.txt`, gate-setter absence, and unsupported comparison operators in the four assigned script files. The read-only HOI4 MCP technology inspection was also invoked for the workspace and returned `TECH_INSPECTED_PARTIAL`; its large-workspace helper projections were deferred and it returned no source-level diagnostics for these new IDs, so the bounded source audit remains the authoritative evidence until parent runtime wiring is present. No Hearts of Iron IV process was launched and no live-save completion claim is made.

No fallback, generic replacement, or model-gate bypass was used. The remaining omissions are the parent-owned runtime/template/entity/GFX/icon/localisation/enum wiring and the blocked 3D model packages documented in their separate handoffs.

Skills used: `chaos-redux-events` source workflow, `chaos-redux-event-assets` ownership boundary, and the offline HOI4 unit/equipment/technology documentation and vanilla precedents required by `AGENTS.md`.
