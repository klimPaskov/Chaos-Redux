# Chaos Warfare: Extermination Columns Implementation

## Overview
This mechanic adds a Chaos Warfare infantry-track subdoctrine (`extermination_columns`) that grants broad infantry combat buffs, unlocks a new special sub-unit (`chaos_battalion`) at mastery level 3, and escalates frontline contamination pressure while that unit is actively fighting.

## What Was Implemented
1. Added a new infantry subdoctrine definition:
- File: `common/doctrines/subdoctrines/land/chaos_warfare_infantry_subdoctrines.txt`
- Track: `infantry`
- Subdoctrine: `extermination_columns`
- Mastery/reward values are implemented from `docs/spreadsheets/doctrines.xlsx`.

2. Added a new special sub-unit:
- File: `common/units/chaos_battalion.txt`
- Sub-unit key: `chaos_battalion`
- Unlock state: `active = no` by default, enabled by researching `chaos_battalion_tech`.
- Role: extreme soft attack and breakthrough, with very low survivability and reliability.
- Terrain profile: asymmetric chemical-assault profile.
  - Strong: `fort`, `urban`, `forest`, `jungle`, `marsh`.
  - Weak (explicit debuffs): `plains`, `desert`, `hills`, `mountain`, `river`, `amphibious`.
- Equipment burden:
  - `infantry_equipment`
  - `support_equipment`
  - `motorized_equipment`
  - `light_tank_flame_chassis`
  - Chemical cylinders: chlorine/phosgene/mustard/lewisite/sarin/soman (tabun remains a tech gateway, not direct equipment)
  - Bioweapon bombs: anthrax/plague/tularemia

3. Added doctrine-unlocked tech chain for chaos battalion progression:
- File: `common/technologies/chaosx_technologies.txt`
- Base tech: `chaos_battalion_tech` (visible in tree, non-researchable, granted directly by mastery 3)
- Upgrade techs: `chaos_battalion_1939`, `chaos_battalion_1942`
- Purpose: once mastery grants the base unlock, later upgrades improve the `chaos_battalion` sub-unit directly.

4. Added combat contamination/casualty behavior:
- File: `common/scripted_effects/chemical_infantry_effects.txt`
- Core effect: `chaos_battalion_apply_state_dispersal`
- While in combat, leaders with chaos battalions apply strong state contamination through the existing chemical contamination pipeline.
- Combat-state damage scales with chaos battalion density (more chaos battalions per engaged division increases damage pressure).
- The same contamination burst now explicitly damages enemy units and also causes friendly-fire collateral to non-enemy units in the affected state.
- Low-probability biowarfare outbreak trigger was added to the same combat-confirmed state loop:
  - Runs only on contested states where chaos battalion combat contribution is already confirmed.
  - Uses existing disease effects (`apply_tularemia_contamination`, `apply_anthrax_contamination`, `apply_plague_contamination`).
  - Skips states already marked as `bioweapon_contaminated` to avoid repeat outbreak stacking.
- Mastery 5 integration:
  - Reward sets `chaos_battalion_terminal_contagion_unlocked`.
  - Effect multiplies contamination severity, casualty damage, and condemnation pressure for terminal mode.

5. Hooked the behavior into existing chemical combat on_actions:
- File: `common/on_actions/chaosx_on_actions_chemical_warfare.txt`
- Trigger paths: `on_army_leader_daily`, `on_army_leader_won_combat`, `on_army_leader_lost_combat`
- Conditions include:
  - `num_units_in_combat > 0`
  - owner has chemical weapon tech
  - owner has Chaos Warfare selected and `chaos_battalion_unlocked`
  - active leader has chaos battalions
- Won/lost combat now registers additional chaos-specific condemnation scaled by offensive chaos battalion participation.

6. Added required localisation and doctrine icon registration:
- `localisation/english/chaosx_doctrines_l_english.yml`
- `localisation/english/chaosx_units_l_english.yml`
- `localisation/english/chaosx_technologies_l_english.yml`
- `interface/chaosx_doctrines.gfx`
- `interface/chaosx_subuniticons.gfx`

## System Interaction Notes
- Uses the existing chemical contamination variable/modifier stack (`chem_apply_state_contamination`) so contamination stacking/expiry behavior remains consistent with current chemical systems.
- Uses existing `on_army_leader_daily` flow already used by Livens and chemical tank-shell systems.
- Does not add new `on_weekly`/global sweep loops.

## Icons Needed
Registering is complete. Replace placeholder textures with final art files at:

1. Chaos battalion large counter icon:
- Path: `gfx/interface/counters/divisions_large/unit_chaos_battalion_icon.dds`
- GFX key: `GFX_unit_chaos_battalion_icon_medium`
- GFX file: `interface/chaosx_subuniticons.gfx`

2. Chaos battalion on-map small counter icon:
- Path: `gfx/interface/counters/divisions_small/onmap_unit_chaos_battalion_icon.dds`
- GFX key: `GFX_unit_chaos_battalion_icon_medium_white`
- GFX file: `interface/chaosx_subuniticons.gfx`

3. Extermination Columns doctrine icon (optional dedicated art; currently reuses Chaos Warfare art):
- Path: `gfx/interface/doctrines/icons/doctrine_extermination_columns.dds` (planned)
- GFX key: `GFX_doctrine_extermination_columns_medium`
- GFX file: `interface/chaosx_doctrines.gfx`

4. Chaos battalion base tech icon:
- Path: `gfx/interface/technologies/chaos_battalion.dds`
- GFX key: `GFX_chaos_battalion_tech_medium`
- GFX file: `interface/chaosx_techtree.gfx`

5. Chaos battalion 1939 tech icon:
- Path: `gfx/interface/technologies/chaos_battalion2.dds`
- GFX key: `GFX_chaos_battalion_1939_medium`
- GFX file: `interface/chaosx_techtree.gfx`

6. Chaos battalion 1942 tech icon:
- Path: `gfx/interface/technologies/chaos_battalion3.dds`
- GFX key: `GFX_chaos_battalion_1942_medium`
- GFX file: `interface/chaosx_techtree.gfx`

## Future Plans / Suggestions
1. Add explicit doctrine tooltips for contamination dose/duration scaling by mastery level to improve player readability.
2. Add AI template weighting so countries with Chaos Warfare actively field `chaos_battalion` when stockpiles support it.
3. Add an optional risk event chain for chaos battalion mishandling (friendly contamination incidents) to reinforce high-risk doctrine identity.
