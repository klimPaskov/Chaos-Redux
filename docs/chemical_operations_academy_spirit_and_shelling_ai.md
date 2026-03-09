# Chemical Operations Academy Spirit and Chemical Tactic Weighting

## Overview
This update extends the chemical warfare officer corps package with three connected changes:

1. A new `academy_spirit` (`chemical_operations_academy_spirit`) that works without `chaos_warfare`.
2. A preferred-tactic bonus for `chemical_division_contamination_command_spirit` to reinforce `tactic_chemical_barrage` for player use.
3. Tactical AI restrictions so generals do not proactively use chemical tactics, while `tactic_gas_mask_defense` remains a counter-only response and `tactic_chemical_barrage` remains available through `chaos_warfare`.

## Mechanics
### 1. Chemical Operations Academy spirit
- Spirit key: `chemical_operations_academy_spirit`
- Category: `academy_spirit`
- Definition file: `common/ideas/cbw_spirits.txt`
- Shared tuning constant:
  - `chem_chaos_warfare_spirit.academy.chemical_operations_trait_gain_chance = 50`
  - File: `common/script_constants/chemical_spirit_constants.txt`

#### Trait gain behavior
- Trigger points:
  - `on_unit_leader_created`
  - `on_unit_leader_level_up`
  - File: `common/on_actions/chaosx_on_actions_chemical_warfare.txt`
- Shared scripted effect:
  - `chem_try_grant_chemical_operations_trait_from_academy_spirit`
  - File: `common/scripted_effects/chemical_warfare_effects.txt`
- Rules:
  1. Country must have `chemical_operations_academy_spirit`.
  2. Leader must be an army leader.
  3. Leader must not already have `chemical_operations_commander`.
  4. Roll `50%` chance and grant `chemical_operations_commander` on success.

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
1. Add separate chance tiers for newly assigned leaders and level-up events (for finer balancing).
2. Add AI spirit weighting that scales with cylinder stockpile depth and active chemical battalion share for non-preferred-tactic chemical support tools.
3. Add a doctrine-agnostic defensive counter-spirit that improves gas-mask counter quality without reintroducing proactive gas-mask tactic picks.
