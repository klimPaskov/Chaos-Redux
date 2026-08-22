# Chaos Warfare Officer Corps Spirits

## Overview
The active officer-corps package uses a Chemical Operations Academy, three mutually exclusive army-command postures, and three mutually exclusive division-command postures. The former air identifier remains a hidden compatibility record:

1. Army: `chemical_command_reagent_optimization_spirit`, `cbrn_theater_contamination_doctrine_spirit`, and `cbrn_terminal_hazard_doctrine_spirit`.
2. Division command: `cbrn_mask_discipline_spirit`, `cbrn_hazard_assault_cadres_spirit`, and `chemical_division_contamination_command_spirit`.
3. Academy route: `chemical_operations_academy_spirit`.
4. Compatibility-only identifier: `chemical_air_deep_strike_spirit`.

## Implemented Spirits
### 1. Army command postures
- Key: `chemical_command_reagent_optimization_spirit`
- Category: `army_spirit`
- Availability: Chaos Warfare plus the Protective Foundation milestone.
- Effects: +20% army organisation, +30 maximum Command Power, and 15% lower military mask/filter consumption.

- Key: `cbrn_theater_contamination_doctrine_spirit`
- Availability: Theater Exploitation milestone.
- Effects: +30% planning speed, -20% attrition, and +20% supply consumption, with the larger CBRN delivery, biological-lifecycle, preparation, and cleanup effects documented in `docs/systems/cbrn_warfare/chaos_warfare_doctrine.md`.

- Key: `cbrn_terminal_hazard_doctrine_spirit`
- Availability: Terminal CBRN Command milestone plus Unrestricted Chaos Warfare policy.
- Effects: +35% army attack, +25% coordination, +25% supply consumption, and the Terminal Hazard chemical/biological lethality, contamination, medical-pressure, camp-network, and reduced-Condemnation multipliers.

### 2. Division command postures
- Key: `cbrn_mask_discipline_spirit`
- Availability: Hazard Assault Formations Mastery 1.
- Effects: +20% army organisation and -20% organisation loss when moving; the shared mask ledger applies its separate military consumption multiplier.

- Key: `cbrn_hazard_assault_cadres_spirit`
- Availability: Hazard Assault Formations Mastery 3 plus `chaos_battalion_tech`.
- Effects: +10% special-forces capacity, +25% army experience gain, and +30% attack and defence for Hazard Pioneers and Chaos Assault Battalions.

- Key: `chemical_division_contamination_command_spirit`
- Category: `division_command_spirit`
- Availability: Contaminant Fire Support Mastery 2.
- Effects: +35% army artillery attack and +25% reliability for Livens projectors and chemical payload-cylinder equipment.

### 3. Chemical Operations Academy
- Key: `chemical_operations_academy_spirit`
- Category: `academy_spirit`
- Availability: active army officer-corps choice with no doctrine prerequisite.
- Effects: army leaders have a 50 percent chance to gain `chemical_operations_commander` when created or when they level up, provided they do not already have the trait.
- The commander trait is also manually assignable through its normal experience cost without a doctrine prerequisite.

### 4. Compatibility identifier
- Key: `chemical_air_deep_strike_spirit`
- Category: `air_force_command_spirit`
- Availability: hidden and unavailable.
- Effects: none. Existing chemical raids and air operations use their current route-specific multipliers and the shared exposure pipeline.

## Script Integration
### Tuning and script integration
- Active officer-corps modifiers use the file-local constants at the top of `common/ideas/cbw_spirits.txt`.
- CBRN delivery, protection, cleanup, evidence, casualty, and Condemnation multipliers use the shared tables in `common/script_constants/cbrn_doctrine_constants.txt` and `common/script_constants/chemical_warfare_constants.txt`.
- `common/script_constants/chemical_spirit_constants.txt` centralizes the academy's leader-trait acquisition chance and the retained chemical spirit tuning.

### Idea definitions
- File: `common/ideas/cbw_spirits.txt`

### Hook points
- Doctrine availability and milestone effects: `common/ideas/cbw_spirits.txt`, `common/doctrines/`, and `common/scripted_effects/cbrn_doctrine_effects.txt`.
- Delivery, protection, cleanup, consequence, and route-specific effects: `common/scripted_effects/cbrn_*.txt` and `common/scripted_effects/chemical_*.txt`.
- Trait assignment and academy acquisition: `common/unit_leader/chaosx_traits.txt`, `common/on_actions/chaosx_on_actions_chemical_warfare.txt`, and `common/scripted_effects/chemical_warfare_effects.txt`.

### Localisation
- File: `localisation/english/chaosx_ideas_l_english.yml`

## Icons and Runtime Wiring
The active spirits use the generated Chaos Warfare officer-corps art package. The six spirit sprites are registered in `interface/cbrn_doctrine.gfx` under the `stage_5_chaos_warfare` officer-corps folder, while the grand doctrine and mastery icons use the dedicated doctrine-style paths documented in `docs/assets/chaos_warfare_system/stage_5_doctrine_officer_corps/manifest.md`.

- Army spirits: `GFX_idea_chemical_command_reagent_optimization_spirit`, `GFX_idea_cbrn_theater_contamination_doctrine_spirit`, and `GFX_idea_cbrn_terminal_hazard_doctrine_spirit`.
- Division spirits: `GFX_idea_cbrn_mask_discipline_spirit`, `GFX_idea_cbrn_hazard_assault_cadres_spirit`, and `GFX_idea_chemical_division_contamination_command_spirit`.
- The original grand doctrine icon remains `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds`; the four subdoctrines use the generated `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/` files.

## Future Plans / Suggestions
1. Add spirit-specific UI previews that show exact Command Power, mask, filter, and payload consequences when the officer-corps interface exposes those dynamic values.
2. Add AI preference weights based on reserve depth, military mask condition, and active route readiness.
3. Keep the generated doctrine-style and officer-corps assets under the stage 5 asset manifest so future art revisions cannot silently replace the preserved grand-doctrine icon or the legacy raid icon family.
