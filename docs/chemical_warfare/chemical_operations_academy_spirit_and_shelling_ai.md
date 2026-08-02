# Chemical Operations Academy Spirit and Chemical Tactic Weighting

## Overview
The chemical warfare officer-corps package uses the active Chaos Warfare command structure and retains the former academy identifier only for save compatibility:

1. The hidden `chemical_operations_academy_spirit` identifier has no availability, AI, or gameplay effect.
2. `chemical_division_contamination_command_spirit` receives a preferred-tactic bonus for `tactic_chemical_barrage`.
3. Tactical AI restrictions keep generals from proactively selecting chemical tactics, while `tactic_gas_mask_defense` remains a counter-only response and `tactic_chemical_barrage` remains available through `chaos_warfare`.

## Mechanics
### 1. Chemical Operations Academy compatibility identifier
- Spirit key: `chemical_operations_academy_spirit`
- Definition file: `common/ideas/cbw_spirits.txt`
- The identifier is hidden and unavailable, and adds no automatic leader-trait roll or operational authority.
- Manual assignment of `chemical_operations_commander` requires only the country's `chaos_warfare` doctrine.

### 2. Division Command Cell preferred tactic boost
- Spirit: `chemical_division_contamination_command_spirit`
- Added modifier:
  - `tactic_chemical_barrage_preferred_weight_factor = constant:chem_chaos_warfare_spirit.division.barrage_preferred_weight_factor`
- Constant value:
  - `chem_chaos_warfare_spirit.division.barrage_preferred_weight_factor = 1.00`
- Gameplay result:
  - When `tactic_chemical_barrage` is a preferred tactic, its preferred selection weight is doubled (`+100%`).
  - AI does not take this spirit, preventing AI countries from deliberately setting a chemical tactic preference.

### 3. Chemical tactic AI restrictions
- Files:
  - `common/combat_tactics.txt`
  - `common/technologies/chaosx_technologies.txt`
- Tactics affected:
  - `tactic_gas_mask_defense`
  - `tactic_chemical_shelling`
  - `tactic_chemical_barrage`

#### Net behavior
1. `tactic_gas_mask_defense` has zero normal pick weight, so it acts as a defensive counter only instead of a proactive tactic.
2. `tactic_chemical_shelling` has zero automatic pick weight, so generals no longer use it as a normal battle tactic.
3. `tactic_chemical_barrage` remains available for `chaos_warfare` countries through its own tactic definition.
4. Offensive chemical condemnation remains tied to explicit delivery systems, not defensive gas-mask counterplay.

## Localisation
- Updated file: `localisation/english/chaosx_ideas_l_english.yml`
- Added:
  - `chemical_operations_academy_spirit`
  - `chemical_operations_academy_spirit_desc`
  - `chemical_operations_academy_spirit_tt`
- Updated:
  - `chemical_division_contamination_command_spirit_tt` (now includes Chemical Barrage preferred-weight effect)

## Icons Needed
No new sprite is required for this update.

- If custom art is added later:
  - Suggested sprite path: `gfx/interface/ideas/chemical_operations_academy_spirit.dds`
  - Suggested gfx registration file: `interface/chaos_ideas.gfx`
  - Suggested sprite key: `GFX_idea_chemical_operations_academy_spirit`

## Future Plans / Suggestions
1. Add separate chance tiers for newly assigned leaders and level-up events if the current single low chance proves too flat.
2. Add AI spirit weighting that also checks whether the country has enough chemical stockpile depth to justify the spirit once condemnation escalation has happened.
3. Add a doctrine-agnostic defensive counter-spirit that improves gas-mask counter quality without reintroducing proactive gas-mask tactic picks.
