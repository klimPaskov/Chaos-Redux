---
name: chaos-redux-units-divisions
description: Use when creating, changing, or auditing Chaos Redux sub-units, support companies, division templates, package formations, orders of battle, division names, unit-spawning or unit-removal effects, manpower handling, unit counters and texticons, or sub-unit stats and modifiers. Covers the definition files, the loading rules, the runtime effects and triggers, the Event 19 and test-country obligations, and the silent failures.
---

# Chaos Redux Units, Divisions and Orders of Battle

Guidance for land, naval and air units in Chaos Redux.
Characters, unit leaders and their traits belong to `chaos-redux-characters-leaders`.
Equipment types, variants, modules and production belong to `chaos-redux-equipment`; technologies that unlock sub-units belong to `chaos-redux-technology-doctrines`; ideas and modifier definitions belong to `chaos-redux-ideas-modifiers`; wider AI weighting belongs to `chaos-redux-ai-strategies`; state, province and supply data belong to `chaos-redux-map-states`. This skill only covers how a unit consumes equipment and how units are defined, loaded and scripted.
Custom 3D unit models, animations, counters and sounds belong to `chaos-redux-3d-model-pipeline`; counter and flag art belongs to `chaos-redux-event-assets`; frame-sheet animation belongs to `chaos-redux-frame-animation`.
Reference files, read when the task needs them: `references/naval-air-oob.md` (fleets, ships, air wings, carrier wings, aces, ship name lists, DLC splits), `references/runtime-effects-triggers.md` (exact signatures of runtime unit, template, manpower effects and triggers, division scope), `references/names-stats-visuals.md` (division name group skeleton, stat and modifier lists, sprite and counter wiring).

## Contents

- Required reading and vanilla precedents
- Mental model and decision table
- Sub-unit definitions (`common/units`)
- Units versus equipment
- Division templates
- Division placement in an order of battle
- Division names
- Loading orders of battle
- Runtime effects, triggers and scopes (overview)
- Manpower
- Stats and modifiers
- Unit leaders, battle plans and AI
- Visuals and counters (overview)
- Localisation
- Chaos Redux specifics
- Common mistakes and silent failures
- Validation checklist

## Required reading and vanilla precedents

Read the sections that bear on the task before writing script.
With the HOI4 MCP, use `hoi4.reference_search` and `hoi4.reference_read` for the sections below and `hoi4.source_lookup` for vanilla definitions; if a route fails once, retry once, then read the local files directly.

Installed game documentation is more authoritative than the wiki.
Root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

| Topic | Primary source |
| --- | --- |
| Unit effects (`division_template`, `create_unit`, `load_oob`, `set_oob`, `set_naval_oob`, `set_air_oob`, `set_keyed_oob`, `add_units_to_division_template`, `delete_unit`, `delete_units`, `delete_unit_template_and_units`, `set_division_template_lock`, `set_division_template_cap`, `set_division_force_allow_recruiting`, `change_division_template`, `create_colonial_division_template`, `create_ship`, `transfer_units_fraction`, `unlock_subunit`, `add_unit_bonus`, `add_manpower`, `damage_units`) | `documentation/effects_documentation.md` (search `## <effect>`) |
| Unit triggers (`has_template`, `has_template_majority_unit`, `has_template_containing_unit`, `division_has_majority_template`, `division_has_battalion_in_template`, `divisions_in_state`, `num_divisions`, `has_army_size`, `has_army_manpower`, `any_country_division`, `any_state_division`) | `documentation/triggers_documentation.md` |
| Manpower as a readable value (`manpower_k`, `max_manpower_k`, `max_available_manpower_k`, `deployed_army_manpower_k`, `has_manpower`) | `documentation/dynamic_variables_documentation.md` |
| Modifier names and scopes (`army`, `naval`, `air`, `unit_leader` scopes, `training_time_factor`, `conscription_factor`, `weekly_manpower`) | `documentation/modifiers_documentation.md` |
| Localisation objects for units and leaders | `documentation/loc_objects_documentation.md` (UnitLeader, Character) |
| Script constants | `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md` |
| Equipment schema, `type` values, archetypes, modules | `common/units/equipment/_documentation.md`, `common/equipment_groups/_documentation.md` |
| AI division templates and role ratios | `common/ai_templates/_documentation.md`, `common/ai_strategy/_documentation.md` |
| Unit and division defines (grid sizes, experience levels, leader deploy cooldowns) | `common/defines/00_defines.lua` (`NDefines.NMilitary`) |

Offline wiki (`paradox_wiki/`): `Unit modding - Hearts of Iron 4 Wiki.md` (sub-units, categories, groups, stats, icons), `Division modding - Hearts of Iron 4 Wiki.md` (templates, placement, navy and air OOB, unit name lists), `Country creation - Hearts of Iron 4 Wiki.md` (Order of battle, Variants), `Namelist modding - Hearts of Iron 4 Wiki.md` (division, ship and generic name lists), `Technology modding - Hearts of Iron 4 Wiki.md` (`enable_subunits`, sub-unit bonuses), `Equipment modding - Hearts of Iron 4 Wiki.md`, `Entity modding - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md` (division and combatant scopes).

Vanilla precedents to mirror:

- Sub-unit definitions: `common/units/infantry.txt`, `artillery.txt`, `medium_armor.txt`, `recon.txt`, `engineer.txt`, `fire_support.txt` (regimental support), `hq_support.txt` (Army HQ companies), `destroyer.txt` (ship), `air.txt` (air wing).
- Unit categories: `common/unit_tags/00_categories.txt`.
- Per-sub-unit modifier registration: `common/units/unit_modifiers/unit_modifiers.txt`.
- Land OOB with templates, names and `regimental_support`: `history/units/GER_1936_nsb.txt`, `CZE_1936_nsb.txt`; DLC-split OOBs: `GER_1936.txt` versus `GER_1936_nsb.txt`.
- Naval OOB: `history/units/GER_1936_naval_mtg.txt` (Man the Guns) and the matching `*_naval_legacy.txt`.
- Air OOB: `history/units/ENG_1936_air_bba.txt` (By Blood Alone airframes) and `GRE_1936_air_legacy.txt`; aces: `ITA_aquila_magna.txt`.
- OOB registration in country history: `history/countries/GER - Germany.txt` (`set_oob` inside `if`, `set_air_oob`, `set_naval_oob`, `create_equipment_variant`).
- Templates created by effect: `history/general/taog_hq_template.txt` (Army HQ), `common/decisions/AUS.txt` (templates plus `create_unit`), `common/decisions/GER.txt` (`add_units_to_division_template`, `load_oob` after a state transfer).
- Division name groups: `common/units/names_divisions/GER_names_divisions.txt` (the file header documents every key).
- Ship name groups: `common/units/names_ships/*.txt`; generic equipment names: `common/units/names/*.txt`.
- Sprites: `interface/subuniticons.gfx`; entities: `gfx/entities/units_infantry.asset`.
- Unit localisation: `localisation/english/unit_l_english.yml`, `deployment_l_english.yml` (group titles).

## Mental model and decision table

Five layers, each defined in a different place:

1. Sub-unit (battalion or company type): `common/units/*.txt`. Defines stats, which equipment it consumes (`need`), and where it can sit in a template (`group`).
2. Equipment: `common/units/equipment/*.txt`. What sub-units consume. Produced by factories, stockpiled per country, and also fixes the sub-unit speed (`transport`) and many stats.
3. Division template: a country-owned grid of sub-units. Created by `division_template` in an order-of-battle file or as an effect.
4. Division (a unit on the map): created from a template by an OOB `division = { ... }` block, by `create_unit`, by the player's recruiting, or by AI production.
5. Order of battle (OOB): a file in `history/units/` containing templates, divisions, fleets, air wings and an `instant_effect` block. It does nothing until a country loads it.

| I want to... | Use |
| --- | --- |
| Add a new battalion or company type | New `sub_units` entry in `common/units/`, plus unlock, localisation, sprites, optional modifiers registration |
| Change stats of an existing sub-unit | Override the whole entry in a same-named file later in load order, or give a country a modifier; do not edit the vanilla file |
| Give a country a starting army, navy or air force | OOB files registered from country history with `set_oob`, `set_naval_oob`, `set_air_oob` |
| Give an existing country new templates or divisions mid-game | `division_template` effect plus `create_unit`, or `load_oob` on a country that owns at least one state |
| Spawn a division at a place chosen by script | `create_unit` with `prioritize_location` or `country_score` |
| Reshape a template the country already has | `add_units_to_division_template` (adds only), `change_division_template` in division scope, or delete and recreate with `delete_unit_template_and_units` |
| Stop the player editing or over-building a template | `is_locked`, `division_cap`, `force_allow_recruiting` on the template, or the matching effects |
| Remove divisions | `delete_unit` (filters), `delete_units` (template), `delete_unit_template_and_units`, `destroy_unit` in division scope |
| Give or take manpower | `add_manpower`; read through `manpower_k` style variables or `has_manpower` |
| Buff or nerf one sub-unit type | Technology `<sub_unit> = {}` bonus, `add_unit_bonus`, or a registered `modifier_army_sub_unit_<name>_*` modifier |

## Sub-unit definitions (`common/units`)

Files are loaded by folder; every file starts with `sub_units = { ... }` and contains any number of entries keyed by the sub-unit id.
The id is the token used in templates, `need` lookups, technologies (`enable_subunits`), localisation and modifier names.

Land battalion skeleton (fields as used by `common/units/infantry.txt` and `medium_armor.txt`):

```text
sub_units = {
	my_infantry = {
		abbreviation = "MYI"
		sprite = infantry
		map_icon_category = infantry

		priority = 600
		ai_priority = 200
		active = no

		type = { infantry }
		group = infantry

		categories = {
			category_front_line
			category_light_infantry
			category_all_infantry
			category_army
		}

		combat_width = 2

		max_strength = 25
		max_organisation = 60
		default_morale = 0.3
		manpower = 1000
		training_time = 90
		suppression = 1.5
		weight = 0.5
		supply_consumption = 0.06

		need = {
			infantry_equipment = 100
		}

		hills = { attack = 0.1 movement = 0.05 }
	}
}
```

Support company differences (`common/units/artillery.txt`, `recon.txt`, `hq_support.txt`):

```text
		group = support
		type = { infantry support }
		categories = { category_support_battalions category_divisional_support_battalions category_army }
		regimental = no
		affects_speed = no
		combat_width = 0
		same_support_type = recon
```

Field notes, each verified against vanilla files named above and `Unit modding` on the wiki:

- `sprite` is the entity base name. The engine looks up an entity named `<sprite>_entity` (with graphical-culture, country and cosmetic-tag prefixed variants). Wiki: `Unit modding` (Models) and `Entity modding`.
- `map_icon_category`: wiki lists `infantry`, `armored`, `other`, `ship`, `transport`, `uboat`. Vanilla `infantry.txt` header comment lists the same families. You cannot add new map icon categories or new internal `type` values.
- `type = { ... }`: internal types. Wiki list: infantry, support, artillery, anti_tank, anti_air, armor, fighter, cas, naval_bomber, interceptor, suicide, tactical_bomber, strategic_bomber, air_transport, missile, submarine, screen_ship, capital_ship, carrier, motorized, mechanized, flame, amphibious. The `type` values drive built-in rules, so copy the closest vanilla unit instead of inventing combinations.
- `group`: `infantry`, `mobile`, `armor`, `support` in the wiki; vanilla also uses `combat_support`, `mobile_combat_support`, `armor_combat_support` (see `allowed_battalion_groups` in `fire_support.txt`). The group sets the template tab and the row the sub-unit may occupy. A new group name used in `group =` is created automatically; give it `group_<name>_title` localisation and a `GFX_group_<name>_icon` sprite (wiki, `Unit modding` > How to add new Groups; vanilla title keys live in `deployment_l_english.yml`).
- `priority`: which sub-unit's icon and model wins when several are present. Support entries use 0 in vanilla.
- `ai_priority`: AI preference when picking sub-units.
- `active = yes` means usable without unlocking; `active = no` means a technology must unlock it via `enable_subunits = { id }` in a technology (wiki: `Technology modding`). Script can also unlock with `unlock_subunit = id` in country scope (installed effects documentation; vanilla use in `common/doctrines/subdoctrines/special_forces/`).
- `categories`: tags from `common/unit_tags/00_categories.txt`. Technologies and `add_unit_bonus` address categories (for example `category_all_infantry`). A new category is declared in a `sub_unit_categories = { ... }` list like the vanilla file (put it in a new file of the same folder; confirm it loads without a duplicate-definition complaint) and needs a localisation key (vanilla: `category_light_infantry` in `unit_l_english.yml`).
- Flags: `special_forces`, `marines`, `mountaineers`, `rangers`, `cavalry`, `can_be_parachuted`, `can_exfiltrate_from_coast`, `affects_speed`. Vanilla comment in `infantry.txt`: for `can_exfiltrate_from_coast` all non-support sub-units in the division must have it.
- `transport = <equipment>`: the equipment that sets movement speed (motorized and mechanized). Wiki: sets speed via equipment.
- `need`: map of equipment archetype or category to the quantity per battalion. Keys such as `infantry_equipment` are archetypes, not concrete variants such as `infantry_equipment_1`.
- `essential`: list of equipment keys. Vanilla comment in `infantry.txt` for `mechanized`: "needed since we give so much bonus to infantry even with no mech equipment". Treat it as "this sub-unit loses its bonus without these"; verify behaviour in game for a new unit.
- `regimental = no`, `divisional = no`, `allowed_battalion_groups = { ... }`: placement rules. `divisional = no` plus `allowed_battalion_groups` define a regimental support company that may attach only to battalions of the listed groups (`fire_support.txt`). `regimental = no` marks a plain divisional support company.
- `same_support_type = token`: only one sub-unit with a given token per template. Several tokens may be listed (`recon.txt` lists `recon` and `helicopter_recon`).
- `allow_in_army_hq` / `allow_in_non_army_hq`: gate Army HQ templates (`hq_support.txt`).
- `required_dlc = { "..." }`: restricts the entry.
- Terrain blocks (`forest`, `hills`, `mountain`, `jungle`, `marsh`, `urban`, `river`, `amphibious`, `plains`, `desert`, `snow`, `fort`) hold `attack`, `defence`, `movement`.
- Naval and air entries are thin (`destroyer.txt`, `air.txt`): `sprite`, `priority`, `active`, `type`, `need = { ship_hull_light = 1 }` or `need = { small_plane_airframe = 1 }`, `categories`, wing sizes (`land_air_wing_size`, `carrier_air_wing_size`), `critical_parts`, `hit_profile_mult`. Their real stats live on the equipment.

Per-sub-unit modifiers: `modifier_army_sub_unit_<id>_attack_factor`, `_defence_factor`, `_speed_factor`, `_max_org_factor`, `_org_recovery_cap_factor`, and `modifier_army_sub_unit_category_<cat>_*` are available only for names listed in `common/units/unit_modifiers/unit_modifiers.txt`. A new sub-unit that should be targetable by such modifiers must be added there (a new file in that folder, same `sub_unit_modifiers = { ... }` structure). `common/modifier_definitions` contains no entries for these names in vanilla, so the registration is what creates them; localise each in the style of `modifiers_l_english.yml` (`modifier_army_sub_unit_infantry_attack_factor: "Infantry Attack"` plus the `_tt` form). The vanilla file notes that `_speed_factor` and `_max_org_factor` cannot be applied to support battalions.

## Units versus equipment

- A sub-unit asks for equipment (`need`). A division fields the sum of its battalions' needs; deficits lower strength and bonuses, and AI and players fill them from the stockpile.
- Equipment files define `archetype`, `type`, stats, `resources`, `year`, upgrades and modules (`common/units/equipment/_documentation.md`). Infantry weapons: `infantry_equipment` is the archetype, `infantry_equipment_0/1/2/3` are the concrete types (`common/units/equipment/infantry.txt`).
- Unlock chain: technology `enable_equipments` and `enable_subunits` -> equipment becomes buildable and the sub-unit becomes selectable.
- Equipment stats flow into the division (soft attack, defense, breakthrough, armor, speed). A sub-unit's own stats add on top.
- `common/equipment_groups/` groups equipment types for `equipment_bonus` and AI; see `common/equipment_groups/_documentation.md`.
- In OOBs `force_equipment_variants` pins which equipment variant a division uses, and `add_equipment_production` (inside `instant_effect`) starts production lines.
- Naval and air sub-units are driven almost entirely by equipment (`ship_hull_*`, airframes); see `references/naval-air-oob.md`.

## Division templates

Template block (valid in OOB files and as an effect in country scope; skeleton from `history/units/GER_1936_nsb.txt` and the wiki):

```text
division_template = {
	name = "Example Division"
	division_names_group = GER_Inf_01
	role = infantry
	regiments = {
		infantry = { x = 0 y = 0 }
		infantry = { x = 0 y = 1 }
		infantry = { x = 1 y = 0 }
		infantry = { x = 1 y = 1 }
	}
	regimental_support = {
		field_guns = { x = 0 y = 0 }
	}
	support = {
		engineer = { x = 0 y = 0 }
		artillery = { x = 0 y = 1 }
	}
}
```

Optional keys (wiki `Division modding`, `Effects` > `division_template`, and vanilla use): `division_names_group`, `is_locked`, `force_allow_recruiting`, `division_cap` (template must be locked), `priority` (supply priority 0 reserves, 1 default, 2 elite), `template_counter` (icon id; sprites `GFX_div_templ_<n>_large` and `GFX_div_templ_<n>_small` in `interface/subuniticons.gfx`), `ingame_set_template_counter = yes` (vanilla `INS_1936.txt`; makes the counter editable in game), `override_model` (an entity name), `role` (an AI role label seen in vanilla OOBs such as `GER_1936_nsb.txt`; use it only to match `common/ai_templates` roles), `is_army_hq = yes` (Army HQ templates, `history/general/taog_hq_template.txt`).

Grid rules:

- `x` is the column (left to right), `y` the row (top to bottom), both starting at 0.
- Defaults from `NDefines.NMilitary` in `common/defines/00_defines.lua`: regiments 5 by 5 (`MAX_DIVISION_BRIGADE_WIDTH`, `MAX_DIVISION_BRIGADE_HEIGHT`), division support 1 by 5, regimental support 5 by 1, Army HQ templates 1 by 4 with 1 by 4 support and no regimental support. The defines also set a designer minimum regiment height (`MIN_DIVISION_BRIGADE_HEIGHT = 4`).
- Sub-units placed in `support` must have `group = support`; sub-units placed in `regiments` must not. Wiki: the group cannot change within a single column; vanilla keeps one group per `x` column.
- Avoid duplicate coordinates, out-of-range coordinates, sub-units that are not unlocked, and `same_support_type` clashes; the exact engine reaction to each is not documented, so treat them as defects to prevent by review.
- Templates are identified by `name` per country. Two templates with the same name collide: new divisions refer to the template by name.

Runtime template editing:

- `add_units_to_division_template = { template_name = "..." regiments = { infantry = 0 } support = { engineer = 0 } regimental_support = { ... } }` adds battalions to the first free slot of the given column (the number is the column `x`). It adds only; it cannot remove or move. In division scope `template_name` is optional. Vanilla: `common/decisions/GER.txt`.
- To restructure, create a new template and `delete_unit_template_and_units` the old one, or use `change_division_template = "Name"` in division scope to move a division to another template. Vanilla: `common/scripted_effects/NOR_scripted_effects.txt`.
- Locks and caps: `set_division_template_lock = { division_template = "..." is_locked = yes }`, `set_division_template_cap = { division_template = "..." division_cap = 12 }`, `clear_division_template_cap`, `set_division_force_allow_recruiting`, `country_lock_all_division_template`. The country-level lock (`country_lock_all_division_template`) cannot be undone with the per-template effect; unlock it the same way.
- Overlord-owned colonial templates: `create_colonial_division_template = { subject = TAG division_template = { ... } }`.
- Test existence with `has_template`, `has_template_majority_unit`, `has_template_containing_unit` before adding, editing or deleting.

## Division placement in an order of battle

Divisions live in the `units = { ... }` block of an OOB file (wiki: `Division modding` > Division placement; keys frequency-checked against all vanilla `history/units/*.txt`).

```text
units = {
	division = {
		division_name = {
			is_name_ordered = yes
			name_order = 25
		}
		location = 6334
		division_template = "Infanterie-Division"
		start_experience_factor = 0.3
		start_equipment_factor = 0.8
		start_manpower_factor = 0.9
		force_equipment_variants = { infantry_equipment_1 = { owner = "GER" } }
		officer = { name = TAG_officer_loc_key portraits = { army = { large = GFX_x small = GFX_y } } }
	}
	division = {
		name = "1st Example Division"
		location = 9392
		division_template = "Example Division"
	}
}
```

- Exactly one naming method: `name = "literal"` or `division_name = { is_name_ordered = yes name_order = N }` (uses the template's name group; unmatched numbers use the group `fallback_name`).
- `location` is a province id, not a state id. Vanilla places divisions only in provinces of the owning country; assume other placements are unsafe unless a precedent shows otherwise.
- `start_experience_factor` is 0 to 1 (experience levels at 0.1, 0.3, 0.75, 0.9 per `UNIT_EXP_LEVELS`). `start_equipment_factor` defaults to 1 and does not subtract from the stockpile (wiki). `start_manpower_factor` unset means manpower is subtracted from the pool as far as it goes.
- `force_equipment_variants`: key is the concrete equipment type; subkeys `owner`, `creator`, `amount`, `version_name`. Versions are mandatory for variant-based equipment (modern tanks, ships, airframes). The owner or creator must have the technology and the variant must exist in its history.
- `officer = { ... }` defines a division commander character; keep it consistent with `chaos-redux-characters-leaders` (large portrait for the commander, small for the officer corps; the engine falls back to `<large>_small`).

Equipment production lines go in the OOB `instant_effect` block (any effect is valid there):

```text
instant_effect = {
	add_equipment_production = {
		equipment = { type = infantry_equipment_0 creator = "GER" }
		requested_factories = 1
		progress = 0.19
		efficiency = 100
	}
}
```

Ships need `version_name` for hull-based equipment; air wings need airframe names under By Blood Alone. Details in `references/naval-air-oob.md`.

## Division names

Name groups live in `common/units/names_divisions/*.txt` (ordered `%d` or `%s` entries, `fallback_name`, `link_numbering_with`, `for_countries`, `can_use`); templates select one with `division_names_group`, OOB divisions with `division_name = { is_name_ordered = yes name_order = N }`. The full skeleton and rules are in `references/names-stats-visuals.md`.

## Loading orders of battle

An OOB file does nothing until a country loads it.

| Mechanism | Where | Notes |
| --- | --- | --- |
| `oob = "file"` | country history file as an argument | Not an effect, so it cannot sit inside `if` |
| `set_oob = "file"` | country history, effect | Replaces the previous OOB with no key; usable inside `if`; history only |
| `set_naval_oob`, `set_air_oob` | country history, effect | Replace the OOB with key `naval` or `air` |
| `set_keyed_oob = { key = x name = "file" }` | country history, effect | Replaces the OOB registered under the key; history only |
| `load_oob = "file"` | any effect in country scope | Loads immediately and adds to the country's current state |

The filename of the OOB is irrelevant as long as the registering call uses the same string without `.txt` (wiki: Order of battle).

DLC splits: By Blood Alone (air) and Man the Guns (navy) are incompatible with the legacy systems, so vanilla keeps separate files (`*_air_bba` / `*_air_legacy`, `*_naval_mtg` / `*_naval_legacy`), and No Step Back splits land OOBs that mention tank equipment (`GER_1936.txt` / `GER_1936_nsb.txt`). Register them with `if = { limit = { has_dlc = "..." } set_oob = "..." }` and the negated twin. In country history files `else` works only in its nested form (wiki).

`load_oob` caveats:

- Wiki: not recommended in history files because it loads immediately; loading before the needed technologies exist, or a file that contains divisions, can fail or crash.
- Observed in this repository's live testing: `load_oob` on a country that owns no state does nothing silently. Load after the first state has been transferred, or register with `set_oob` in the country's history. Vanilla precedent: `common/decisions/GER.txt` transfers states and gives the new country manpower and technology first, then runs `load_oob = "RK_OOB"`.
- It adds to what the country already has. Reloading the same file duplicates divisions, and templates with the same name collide. Guard with a flag or `has_template`, or use unique template names.
- It also runs the file's `instant_effect` block. Do not put one-time economy effects in an OOB that will be loaded more than once.
- A country with no OOB at game start has broken buildings (wiki: Order of battle). Every playable or scripted-in country needs at least a minimal OOB.

## Runtime effects, triggers and scopes (overview)

Signatures and examples for each are in `references/runtime-effects-triggers.md`. Summary:

- Create: `division_template`, `create_unit`, `create_ship`, `load_oob`, `create_colonial_division_template`.
- Edit templates: `add_units_to_division_template`, `change_division_template`, lock and cap effects.
- Remove or damage: `delete_unit`, `delete_units`, `delete_unit_template_and_units`, `destroy_unit`, `destroy_ships`, `damage_units`.
- Transfer: `transfer_units_fraction`, `transfer_navy`, `transfer_ship`.
- Division scopes: `every_country_division`, `random_country_division`, `every_state_division`, `random_state_division`, and the trigger forms `any_country_division`, `any_state_division`. The scope inside is a division; `owner` returns the country.
- Combatant scope exists only inside combat triggers (traits, abilities, tactics); it is not reachable from ordinary country script.
- Silent behaviours: `create_unit` and `delete_unit` produce no tooltip; wrap with `custom_effect_tooltip` and `hidden_effect`.

## Manpower

- Read manpower through `manpower_k`, `max_manpower_k`, `max_available_manpower_k` (values in thousands), or the `has_manpower` trigger. The plain `manpower`, `max_manpower` and `max_available_manpower` variables are deprecated and overflow at about 2.1 million (`documentation/dynamic_variables_documentation.md`).
- `add_manpower` works in country scope (the pool) and state scope (local manpower). A negative value subtracts.
- Other readable values: `deployed_army_manpower_k`, `deployed_navy_manpower_k`, `deployed_airforce_manpower_k`, `deployed_total_manpower_k`, `amount_manpower_in_deployment_queue`, `foreign_manpower`, `has_army_manpower`, `manpower_per_military_factory`.
- Division creation consumes manpower from the pool unless `start_manpower_factor` limits it; recruiting from the designer is limited by the same pool and `training_time`.
- Never write recomputed manpower numbers into a script as literal magic values; keep them in script constants or variables.

## Stats and modifiers

Sub-unit stats (`max_strength`, `max_organisation`, `manpower`, `supply_consumption`, `combat_width`, terrain blocks), country and army modifiers, `add_unit_bonus`, and the `defense` versus `defence` spelling rule are in `references/names-stats-visuals.md`. Naval and air stats live on the equipment.

## Unit leaders, battle plans and AI

- Unit leaders (corps commanders, field marshals, admirals) are characters; all definition, trait, recruiting and effect guidance is in `chaos-redux-characters-leaders`. A division's own commander appears as `officer = {}` in an OOB or through promotion from the division.
- Battle plans (planned attacks, army group orders) are runtime AI and player state. There is no effect to create, issue or cancel a battle plan. The script surface around them is planning bonuses: `add_planning`, `boost_planning` (character scope), `has_max_planning` and `min_planning` (combatant triggers), `planning_skill_level`, and planning modifiers. Do not promise battle-plan automation from script.
- AI composition: `common/ai_templates/*.txt` target templates by `role`; `ai_strategy` types `role_ratio`, `template_prio` and `unit_ratio` set how many divisions per role (`common/ai_strategy/_documentation.md`). Debug with the console commands `imgui show ai_templates` and `imgui show ai_division_production` (`common/ai_templates/_documentation.md`). Use `ai_has_role_template` and `ai_has_role_division` as triggers.
- New sub-units are unknown to AI templates until a target template lists them and `ai_priority` is non-zero. For wider AI weighting and strategy work use the `chaos-redux-ai-strategies` skill.

## Visuals and counters (overview)

A sub-unit's `sprite` resolves the entity `<sprite>_entity`; counters are `GFX_unit_<id>_icon_medium`, `_medium_white` and `_small` sprites in `interface/subuniticons.gfx`, plus `GFX_group_<name>_icon` for groups and `GFX_div_templ_<n>_large`/`_small` for template counters. Details are in `references/names-stats-visuals.md`. Custom models, animations, sound and counter art belong to `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets` and `chaos-redux-frame-animation`.

## Localisation

- Sub-unit: `<id>: "Name"` and `<id>_desc: "..."` (vanilla `infantry`, `infantry_desc`, `marine`, `marine_desc` in `unit_l_english.yml`). The `abbreviation = "XXX"` field is a literal string, not a key.
- Categories: `category_<name>: "..."`. Group titles: `group_<name>_title: "..."`.
- Templates and divisions use literal names or name-group strings; name-group descriptions may be loc keys.
- Modifier names for new sub-unit modifiers need keys; tooltip text uses `$modifier_...$` references.
- Files: UTF-8 with BOM, `l_english:` header, keys without the `:0` suffix in this repository.

## Chaos Redux specifics
The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here. Loops over divisions use `every_country_division` inside a bounded country scope; world-wide hooks need permission.

**Where Chaos Redux units live**

- `common/units/` has one file per family or owning event: CBRN support (`cbrn_hq_support.txt`, `cbrn_regimental_support.txt`, `livens_projector_support.txt`), `chaos_battalion.txt`, `zombies.txt`, `clone_infantry.txt`, `coal_golems.txt`, and numbered event files (`010_*`, `012_*`, `014_*`, `016_*`, `018_*`, `020_*`, `039_*`). `common/units/unit_modifiers/chaosx_unit_modifiers.txt` holds shared stat modifiers and `common/units/names_divisions/` the division name groups.
- Division templates for AI use are in `common/ai_templates/` per family (`cbrn_hq_support.txt`, `cbrn_regimental_support.txt`, event files); see `chaos-redux-ai-strategies`.
- Counters and texticons: event counter sprites in `interface/*_counters.gfx`, texticons in `interface/*texticons*.gfx` with art in `gfx/texticons/`. A CBRN texticon is a native-alpha `60x12` strip of two `30x12` frames (`noOfFrames = 2`), copied from the vanilla support texticon family (`docs/systems/cbrn_warfare/cbrn_unit_texticon_assets.md`). Entities are `gfx/entities/<owner>.asset` plus `.gfx`; the runtime contract is `docs/systems/3d_model_pipeline/chaosx_3d_runtime_contract.md`.

**Rules that recur**

1. A new Chaos Redux land sub-unit carries three obligations in the same change. (a) Test-country registration through the dynamic extension contract (`docs/testing/chaosx_test_country.md`): a frontline token through `chaosx_test_country_register_frontline_subunit`, or a support token through `chaosx_test_country_register_support_subunit` with a combat anchor that is already processed (a support-only division is never created). Prefer a package-owned grouped formation when several related units arrive together. (b) An Event 19 disposition: a combat unit extends an existing unit-family provider or gets a full provider registration; a support unit is documented as an inseparable provider attachment, a parent-owned support consumer, or a rejected standalone lot with the engine reason. Update `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` and `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`. (c) Counter, texticon, and entity wiring.
2. CBRN formations use `chaos_battalion` as the combat anchor; armored delivery formations use `autonomous_robot` as the armor-group anchor. The shared `same_support_type` exclusion `cbrn_offensive_delivery` stops the armored delivery roles and the Livens variants sharing one roster, so each needs its own formation.
3. A custom 3D model, animation, sound, or counter follows `chaos-redux-3d-model-pipeline`. The worker hands off the bespoke vanilla-green counter requirement; final counter art is `chaosx_icon_artist` under `chaos-redux-event-assets`; the parent wires the runtime. Never ship a unit with a stand-in counter or a static pose passed off as an animation.
4. A unit family is not available merely because its definition exists: package readiness flags (for example the Africa strange-force manifest) gate runtime use until every family model, entity, counter, and audio item is promoted together.
5. Read manpower through `manpower_k`. Population loss that must not create recruitable manpower uses the exact state-loss helpers in `common/scripted_effects/chaosx_dynamic_effects.md` (`chaos-redux-map-states`).
6. Equipment the unit consumes follows `chaos-redux-equipment`, including the `script_enum_equipment_bonus_type` entry.

## Common mistakes and silent failures

- Writing an OOB and never registering it: no error, no units.
- `oob =` inside `if`: it is a history argument, not an effect; use `set_oob`.
- `set_oob` or `set_naval_oob` outside country history (in an event or decision): documented as history-only. Use `load_oob` for runtime.
- `load_oob` on a stateless country: nothing happens (observed).
- Re-running `load_oob`: duplicates divisions and templates.
- A template naming a sub-unit that is not unlocked, or placing it in the wrong grid region or past the grid size: entry dropped or template invalid.
- Referencing a template that does not exist in a `division = { division_template = "..." }` block; the OOB wiki says to use the template defined in the same file. Treat template names as exact strings (case and punctuation).
- Mixing legacy and DLC equipment names in one OOB (tank, ship or air equipment from the other system): fails or produces empty units; split files by DLC.
- Ships and variant-based tanks or planes without `version_name`, or with an owner lacking the technology: not created.
- `location` set to a state id instead of a province id (divisions, fleets, task forces use provinces; air wings use state ids): units spawn elsewhere or not at all.
- Air wings in a state with no air base: the wiki says the state should have an air base set.
- `division_cap` on an unlocked template: ignored (wiki).
- Using `start_equipment_factor` expecting stockpile deduction: it does not subtract.
- Hard-coding manpower from deprecated variables: overflow above about 2.1 million.
- Adding a sub-unit and forgetting `unit_modifiers.txt`, category registration, localisation, or sprites: raw keys in tooltips, random icons, modifiers that cannot target it.
- `same_support_type` clashes make a second recon, engineer or similar support impossible to add to a template that already has one.
- `add_units_to_division_template` adds only "if possible" (wiki): a full or out-of-range column likely adds nothing and gives no tooltip, so re-read the template after changing it in test.
- `create_unit` for an owner that lacks the named template: expect no division; guard with `has_template`.
- `division_names_group` pointing to a missing group, or an `ordered` number repeated in a group: wrong or fallback names.
- Treating the wiki numbers as current: the installed game is newer (Army HQ templates, regimental support, deployable generals). Prefer the installed files.

## Validation checklist

Run the checks that can realistically fail for the change; do not report boilerplate.

1. Read the vanilla precedent for each construct used and mirror its structure.
2. For each new sub-unit: unlock path (`active` or `enable_subunits`), `need` keys exist in `common/units/equipment`, categories exist in `common/unit_tags`, `group` valid for its template region, localisation keys, three sprite names, optional `unit_modifiers` registration, AI priority.
3. For each template: every sub-unit exists and is unlockable, `group` matches region, coordinates are unique and in range, `same_support_type` tokens do not clash, name is unique per country, locked or capped flags are intentional, name group exists.
4. For each OOB: registered by exactly one call per branch (land, naval, air), DLC split files exist for both branches, provinces and states exist and are owned by the country, ship variants and airframes exist for the owner, `instant_effect` runs once.
5. For runtime effects: country scope correct, existence guards (`has_template`, state ownership), idempotence flags, hidden effects wrapped with a visible tooltip, no unbounded world loops.
6. Use `hoi4.script_validate` for effect and trigger bodies under their explicit scope when exposed; its true result covers only the listed checks, and engine behaviour remains unproven until the user tests in game.
7. State clearly in the report which statements are source-verified, which come from the wiki only, and which depend on in-game behaviour.
