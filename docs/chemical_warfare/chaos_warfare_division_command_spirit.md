# Chaos Warfare Division Command Spirit

## Overview
This mechanic adds a new Chaos Warfare-gated `division_command_spirit`:

- `chemical_division_contamination_command_spirit`

The spirit is selectable only when `has_doctrine = chaos_warfare` and applies a unified `+20%` effectiveness multiplier to chemical frontline subunit effect pipelines.

## How It Works
1. The spirit is defined in `common/ideas/cbw_spirits.txt` under `division_command_spirit`.
2. Shared tuning values are centralized in `common/script_constants/chemical_spirit_constants.txt`:
   - `chem_chaos_warfare_spirit.division.support_profile_mult = 1.20`
   - `chem_chaos_warfare_spirit.division.chaos_state_effect_mult = 1.20`
   - `chem_chaos_warfare_spirit.division.chaos_damage_mult = 1.20`
   - `chem_chaos_warfare_spirit.division.chaos_condemnation_mult = 1.20`
3. `common/scripted_effects/chemical_warfare_effects.txt` provides the shared helper:
   - `chem_set_chaos_division_spirit_chemical_modifiers`
4. Combat chemical systems call that helper and apply the multiplier:
   - Livens support profiles: `common/scripted_effects/chemical_livens_support_effects.txt`
   - Chemical tank support profiles: `common/scripted_effects/chemical_tank_shell_effects.txt`
   - Chaos battalion contamination, damage, condemnation: `common/scripted_effects/chemical_infantry_effects.txt`
5. Player-facing name/description/tooltip are in `localisation/english/chaosx_ideas_l_english.yml`.

## Gameplay Impact
- Buffs all chemical combat subunits, including chaos battalion.
- Increases contamination pressure and related combat output rather than adding flat stat modifiers.
- Keeps balancing centralized in one constants table for fast tuning.

## Icons Needed
No new sprite is required for this spirit right now.

- If custom art is later desired:
  - Suggested file path: `gfx/interface/ideas/chemical_division_contamination_command_spirit.dds`
  - Suggested registration file: `interface/chaos_ideas.gfx`
  - Suggested sprite key: `GFX_idea_chemical_division_contamination_command_spirit`

## Future Plans
1. Split single `20%` bonus into separate doctrine-tiered values (early, mid, late chaos warfare).
2. Add a small tradeoff (for example modest planning decay) if this spirit is outperforming alternatives.
3. Add AI weighting using cylinder stockpile and active chemical support share for smarter spirit selection.
