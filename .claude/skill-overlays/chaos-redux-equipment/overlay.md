---
description: Use when creating, changing, scripting, or auditing Chaos Redux equipment: archetypes and variants, CBRN chemical and biological payload lots, modular tank, ship, and aircraft designs, stockpile, reservation, and production effects, equipment bonuses and military industrial organizations, script_enum_equipment_bonus_type, or test-country equipment registration. Also use when an equipment type, module, or bonus silently does nothing.
---

### In Modules, the designer, graphics, and AI designs of references/modular-equipment-and-designer.md

`GAME` is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. (Chaos Redux wording differs from the kit)

### In Production, stockpile, licences, and equipment script catalogue of references/production-and-stockpile.md

`GAME` is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`. (Chaos Redux wording differs from the kit)

### In Chaos Redux Equipment

In this skill `GAME` means `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV` and `WIKI` means the repository folder `paradox_wiki`. (Chaos Redux wording differs from the kit)

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here.

**Where Chaos Redux equipment lives**

- `common/units/equipment/` holds one file per family, named by owning event number or system: `cbrn_payload_equipment.txt` (strategic agent lots, filled shell lots, class-specific air payload lots), `cylinders.txt`, `livens_projectors.txt` (modular chassis with a mandatory `projectile_slot`), `chemical_airframes.txt`, `chemical_special_bombs.txt`, `bioweapons.txt`, `zombie_special_bombs.txt`, `cbrn_protective_equipment.txt`, `clone_equipment.txt`, `coal_golems.txt`, and the event files (`012_*`, `016_*`, `039_*`). Module definitions are in `common/units/equipment/modules/`. Per-file tuning uses file-scoped `@` constants with the file overview at the top.
- A `zz_` prefix makes a file load after the vanilla file that defines the archetype it extends (`zz_cbrn_project_armored_vehicle.txt` extends the vanilla `armored_support_vehicle`, which has no module slots, with a separate producible decontamination type).
- Sprites are registered in `interface/chaosx_equipment.gfx`, `interface/cbrn_project_equipment.gfx`, and `interface/042_equipment_from_heavens.gfx`; MIO badges follow `GFX_military_industrial_organization_<archetype>` in `interface/cbrn_mio_industry.gfx`. Equipment art follows `chaos-redux-event-assets`; 3D equipment models follow `chaos-redux-3d-model-pipeline`.

**Rules that recur**

1. Payload lots are exact. Every strategic agent has its own archetype so a native raid can reserve that agent without drawing another agent's stock. Never substitute a generic payload or another agent. Native raids carry their own equipment payment (`chaos-redux-native-raids`); scripted operations reserve exact lots through `cbrn_reserve_action_payload` (`docs/systems/cbrn_warfare/chemical_payload_reservations.md`) and must not add a second debit.
2. Measure real debits. Stockpile removal can differ from the request, so compare before and after, or use the helpers in `common/scripted_effects/chaosx_dynamic_effects.md` (`stockpile_debit_helpers`, `cbrn_debit_motorized_stockpile_oldest_first`, input `equipment_stockpile_removal_amount`).
3. `script_enum_equipment_bonus_type` in `common/script_enums.txt` lists category names plus both archetype and numbered type ids (`chemical_chlorine_payload_cylinder` and `chemical_chlorine_payload_cylinder_1`). Add every new id in the same change, in the owning group. The file is a full copy of the vanilla enum, so re-merge new vanilla entries after a game update; the startup log error is the reminder. (Chaos Redux wording differs from the kit)
4. A military industrial organization filter cannot require a particular aircraft module, so an airframe bonus would also boost conventional designs. The CBRN delivery organization therefore grants exact module access through hidden grant-only technologies (`docs/systems/cbrn_warfare/cbrn_designers.md`). Organizations live in `common/military_industrial_organization/organizations/cbrn_*.txt`.
5. Chemical carrier variants use the No Step Back flame-tank chassis types (`light_tank_flame_chassis_3` and its medium and heavy equivalents). Create the named domestic variant before stockpile grants and unit creation, and name both the concrete type and the variant in stockpile calls.
6. Test-country registration: a new concrete equipment type registers through `chaosx_test_country_register_equipment` from the package setup effect (`docs/testing/chaosx_test_country.md`, "Dynamic extension contract"). The test country grants 1,000,000 of each type only from the **Refill Equipment Stockpile** decision and initial setup, never periodically. (Chaos Redux wording differs from the kit)
7. A new land sub-unit that consumes the equipment also needs the unit obligations in `chaos-redux-units-divisions` (test-country formation, Event 19 disposition, counters).
8. Document the mechanic in `docs/` with its icons and the `.gfx` file that references them. (Chaos Redux wording differs from the kit)

### In New equipment line checklist

9. Docs and tests: the mechanic document, the repository test-country registration, and the Chaos Redux dynamic-effects documentation if a helper was added. (Chaos Redux wording differs from the kit)
