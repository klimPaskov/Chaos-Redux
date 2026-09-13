# Event 043 legacy replacement map

| Surface | Legacy role | Required disposition | Guard |
| --- | --- | --- | --- |
| events/043_massive_flood.txt | Old Event 43 event chain | Replace with Event 043 Monsters from the Deep chain. Preserve namespace `chaosx.nr43.*` where possible. | Old broad every-state and every-country loops must not survive. |
| localisation/english/043_massive_flood_l_english.yml | Old flood popup text | Replace or rename with Event 043 localisation file and complete key set. | Write as if the monster event always existed. |
| localisation/english/chaosx_event_names_l_english.yml | Event 43 name mapping | Change Massive Flood to Monsters from the Deep. | Keep ID 43 stable. |
| common/scripted_effects/chaosx_logic_effects.txt | Event classification | Remove Event 43 from repeatable registry and add to Major registry. | Major weight and timer reset rules must apply. |
| events/070_africa_gods.txt | Direct calls to `chaosx.nr43.1` under Massive Flood meaning | Remove or replace with Event 013 flood gateway or another accepted Event 70 consequence. | Do not start the global invasion through an unrelated random list. |
| docs/specs/013_natural_disasters_specs | Notes that reserve Event 43 as separate flood | Update cross-reference after Event 43 replacement. | Event 013 remains ordinary flood owner. |
| Event catalog workbook | Old Massive Flood row | Replace with intended Event 43 row and add SCN-015 after implementation. | Export CSVs through tool. |
| Event Details and log mappings | Old type, name, details, or default state | Register Major, Chaos 3, evolutions, and one world-end row. | No cluster registration. |
| Event default-enable allowlist | Unreworked Event 43 may be disabled | Add only when implementation is ready for normal selection. | Planning alone does not enable it. |

## Repository-wide search terms

Implementation must search for:

- `chaosx.nr43`
- `043_massive_flood`
- `Massive Flood`
- `Massive flood`
- event ID `43` in category arrays
- event ID `43` in cluster definitions
- event ID `43` in scenario and world-end registries
- old flood image sprites
- old flood decision or idea keys
- documentation links to the old event

Every match receives a documented disposition.

## Namespace rule

The entry remains `chaosx.nr43.1`. Sub-event IDs can be reorganised inside the namespace. Save-facing or externally called IDs need an adapter or migration note when changed.
