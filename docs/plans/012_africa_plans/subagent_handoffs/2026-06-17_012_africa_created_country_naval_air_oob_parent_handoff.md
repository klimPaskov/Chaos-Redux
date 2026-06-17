# Event 012 Created-Country Naval And Air OOB Parent Handoff

Date: 2026-06-17

## Scope

Added small static naval and air OOB surfaces for Event 012 created actors whose current seat states have matching vanilla infrastructure. This extends the earlier static land OOB pass; it does not replace the dynamic force helpers or create full bespoke naval/air branches.

## Files Changed

Country histories:

- `history/countries/MAG - Maghreb Coast.txt`
- `history/countries/EAC - East African Railway Congress.txt`
- `history/countries/IOC - Indian Ocean Congress.txt`
- `history/countries/TDM - Tidemark Dominion.txt`
- `history/countries/CRR - Crocodile Rivers.txt`
- `history/countries/WAC - West African Congress.txt`
- `history/countries/CBC - Congo Basin Charter.txt`
- `history/countries/ANW - Ananse Web.txt`
- `history/countries/OVN - Orisha Vodun Nature Courts.txt`
- `history/countries/NHR - Nile-Horn League.txt`
- `history/countries/SLC - South African Liberation Congress.txt`

New OOB files:

- `history/units/MAG_1936_naval_mtg.txt`, `history/units/MAG_1936_naval_legacy.txt`, `history/units/MAG_1936_air_bba.txt`, `history/units/MAG_1936_air_legacy.txt`
- `history/units/EAC_1936_naval_mtg.txt`, `history/units/EAC_1936_naval_legacy.txt`
- `history/units/IOC_1936_naval_mtg.txt`, `history/units/IOC_1936_naval_legacy.txt`, `history/units/IOC_1936_air_bba.txt`, `history/units/IOC_1936_air_legacy.txt`
- `history/units/TDM_1936_naval_mtg.txt`, `history/units/TDM_1936_naval_legacy.txt`
- `history/units/CRR_1936_naval_mtg.txt`, `history/units/CRR_1936_naval_legacy.txt`
- `history/units/WAC_1936_naval_mtg.txt`, `history/units/WAC_1936_naval_legacy.txt`
- `history/units/CBC_1936_naval_mtg.txt`, `history/units/CBC_1936_naval_legacy.txt`
- `history/units/ANW_1936_naval_mtg.txt`, `history/units/ANW_1936_naval_legacy.txt`
- `history/units/OVN_1936_naval_mtg.txt`, `history/units/OVN_1936_naval_legacy.txt`, `history/units/OVN_1936_air_bba.txt`, `history/units/OVN_1936_air_legacy.txt`
- `history/units/NHR_1936_air_bba.txt`, `history/units/NHR_1936_air_legacy.txt`
- `history/units/SLC_1936_air_bba.txt`, `history/units/SLC_1936_air_legacy.txt`

Documentation updated:

- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_static_oob_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_production_parent_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_country_package_audit_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_completion_audit_handoff.md`

## Coverage

Naval static OOBs:

- `MAG`: Algiers/Oran harbor watch at vanilla naval base province `7132`.
- `EAC`: Dar es Salaam rail coast patrol at `2196`.
- `IOC`: Toamasina monsoon passage watch at `5222`.
- `TDM`: Mombasa Tidemark watch at `5210`.
- `CRR`: Loango toll watch at `12975`.
- `WAC`: Lagos Congress watch at `2050`.
- `CBC`: Congo river gate watch at `10968`.
- `ANW`: Abidjan ledger watch at `10803`.
- `OVN`: Duala grove watch at `6039`.

Air static OOBs:

- `MAG`: `24` interwar fighters in state `459`.
- `IOC`: `12` interwar fighters in state `543`.
- `OVN`: `12` interwar fighters in state `773`.
- `NHR`: `18` interwar fighters in state `271`.
- `SLC`: `20` interwar fighters in state `275`.

## Implementation Notes

- Naval histories use `set_naval_oob` with MTG and legacy branches. MTG OOBs use one created `ship_hull_light_1` cutter-class variant per tag; legacy OOBs use `destroyer_1`.
- Air histories use `set_air_oob` with BBA and legacy branches. BBA OOBs follow vanilla's interwar pattern using `small_plane_airframe_0`, `creator = "ENG"`, and `version_name = "Hawker Fury"`; legacy OOBs use `fighter_equipment_0`.
- Added only the minimum tech and convoy setup required for these small patrol/liaison starts.

## Parent Validation

- Verified all `set_naval_oob` and `set_air_oob` registrations resolve to existing files.
- Verified all new OOB files brace-balance.
- Verified each naval `naval_base` and task-force `location` province is a vanilla province with `naval_base`.
- Verified each air OOB state has a vanilla `air_base`.
- Verified each MTG OOB `version_name` matches a country-history `create_equipment_variant`.
- Verified referenced technology, equipment, and module tokens exist in vanilla files.
- Checked touched country and OOB files for unsupported comparison-operator tokens.
- After the country-package subagent patch, rechecked all `set_technology` tokens across all 21 Event 012 created-country histories against vanilla and mod technology definitions: `created_country_tech_audit=passed`.

## Subagent Audit

`chaosx_country_package_auditor` wrote `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_naval_air_oob_audit_handoff.md`.

The audit found one adjacent technology issue and patched it:

- `history/countries/NHR - Nile-Horn League.txt`: replaced invalid `mountain_infantry = 1` with vanilla `tech_mountaineers = 1`.

The audit otherwise found no scoped OOB issues: registrations resolve, MTG variants match, naval bases and airbases are valid, and the added patrol/liaison packages are small enough for created minor actors.

## Remaining Risks

- These are deliberately small patrol and liaison packages. They do not provide full country-specific naval focus branches, air doctrine branches, admirals, aces, ship name lists, or production histories.
- Landlocked actors remain land-only unless their future package receives a new controlled state with relevant infrastructure.
- No live game scenario validation was run for the new static OOB loading.
