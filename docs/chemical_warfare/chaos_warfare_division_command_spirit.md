# Chaos Warfare Division Command Spirit

## Overview
This mechanic adds a new Chaos Warfare-gated `division_command_spirit`:

- `chemical_division_contamination_command_spirit`

The spirit is selectable after Combat Support mastery two and applies +35% army artillery attack plus +25% reliability to Livens and chemical payload-cylinder equipment.

## How It Works
1. The spirit is defined in `common/ideas/cbw_spirits.txt` under `division_command_spirit`.
2. Shared tuning values are centralized in `common/script_constants/cbrn_doctrine_constants.txt`:
   - `contaminant_fire_coordination.army_artillery_attack_factor = 0.35`
   - `contaminant_fire_coordination.equipment_reliability = 0.25`
3. `common/scripted_effects/chemical_warfare_effects.txt` provides the shared helper:
   - `chem_set_chaos_division_spirit_chemical_modifiers`
4. Combat chemical systems still call that helper for save-compatible profile hooks. Its legacy profile multipliers are neutral; the active spirit's visible combat effect comes from its artillery and equipment modifiers:
   - Livens support profiles: `common/scripted_effects/chemical_livens_support_effects.txt`
   - Chemical tank support profiles: `common/scripted_effects/chemical_tank_shell_effects.txt`
   - Chaos battalion contamination, damage, condemnation: `common/scripted_effects/chemical_infantry_effects.txt`
5. Player-facing name/description/tooltip are in `localisation/english/chaosx_ideas_l_english.yml`.

## Gameplay Impact
- Improves artillery-led chemical divisions and the reliability of their payload equipment.
- Keeps the shared chemical exposure pipeline responsible for dose, duration, contamination, deaths, evidence, attribution, Condemnation, and diplomatic consequences.
- Keeps balancing centralized in one constants table for fast tuning.

## Icons Needed
The active sprite is registered as `GFX_idea_chemical_division_contamination_command_spirit` in `interface/cbrn_doctrine.gfx` and uses the existing officer-corps asset at `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/contaminant_fire_coordination.dds`.

## Future Plans
1. Add AI weighting using cylinder stockpile and active chemical support share for smarter spirit selection.
2. Revisit the neutral compatibility helper only if a later accepted spec gives it a distinct, non-duplicative gameplay owner.
