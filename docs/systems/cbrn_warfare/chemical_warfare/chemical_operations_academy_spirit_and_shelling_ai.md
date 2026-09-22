# Chemical Operations Academy Spirit and Chemical Tactic Weighting

The academy and commander-progression account below follows the 2026-09-20 accepted CBRN amendment and current source. Other older tactic-tuning notes are historical source snapshots until reviewed against the final balance pass.

## Overview
The chemical warfare officer-corps package uses an active Chemical Operations Academy alongside the current Chaos Warfare command structure:

1. `chemical_operations_academy_spirit` is an active army officer-corps spirit.
2. `chemical_division_contamination_command_spirit` receives a preferred-tactic bonus for `tactic_chemical_barrage`.
3. Tactical AI restrictions keep generals from proactively selecting chemical tactics, while `tactic_gas_mask_defense` remains a counter-only response and `tactic_chemical_barrage` remains available through `chaos_warfare`.

## Mechanics
### 1. Chemical Operations Academy
- Spirit key: `chemical_operations_academy_spirit`
- Definition file: `common/ideas/cbw_spirits.txt`
- The spirit is available as an army officer-corps choice and has no doctrine prerequisite.
- The spirit grants +3% army experience gain through `experience_gain_army_factor = @CR_SC_CBRN_ACADEMY_EXPERIENCE_GAIN_ARMY_FACTOR` in `common/ideas/cbw_spirits.txt`.
- The academy has no creation or level-up trait roll. `chemical_operations_commander` is earned through two qualifying completed CBRN Headquarters operations by the named leader under `cbrn_commander_record_completed_hq_operation` and the progression threshold constant.
- Trait service credit is independent of academy selection; no 500-experience manual-acquisition path is promised by the current trait definition.

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
- Updated files: `localisation/english/chaosx_ideas_l_english.yml` and `localisation/english/chaosx_abilities_l_english.yml`
- Added:
  - `chemical_operations_academy_spirit`
  - `chemical_operations_academy_spirit_desc`
  - `chemical_operations_academy_spirit_tt`
- The academy text describes army-experience training, while the commander trait text describes earned Headquarters service.

## Icons Needed
No new sprite is required for this update.

- If custom art is added later:
  - Suggested sprite path: `gfx/interface/ideas/chemical_operations_academy_spirit.dds`
  - Suggested gfx registration file: `interface/chaos_ideas.gfx`
  - Suggested sprite key: `GFX_idea_chemical_operations_academy_spirit`

## Future Plans / Suggestions
1. Show the named leader's qualifying Headquarters service progress when the current UI can expose that exact record.
2. Add AI spirit weighting that also checks whether the country has enough chemical stockpile depth to justify the spirit once condemnation escalation has happened.
3. Add a doctrine-agnostic defensive counter-spirit that improves gas-mask counter quality without reintroducing proactive gas-mask tactic picks.
