# Chaos Warfare: Extermination Columns and Chaos Assault Battalions

## Overview

Extermination Columns is the Chaos Warfare infantry track that grants the doctrine-only Chaos Assault Battalion. The battalion is a protected special-forces line formation for deliberate assaults through fortified, urban, forest, jungle, and marsh terrain. It is not an autonomous chemical or biological release system.

Numbered spec 08 governs the doctrine boundary: Extermination Columns does not unlock camp or genocide infrastructure. Doctrine may reduce the Condemnation impact of an otherwise valid chemical action, but it does not erase evidence, attribution, deaths, contamination, medical saturation, or confirmed-use history.

## Current formation contract

The stable public subunit identifier is `chaos_battalion`. Its definition lives in `common/units/cbrn_regimental_support.txt`; `common/units/chaos_battalion.txt` is retained only as a compatibility pointer.

The fully equipped formation has:

- 2 combat width, 25 strength, 28 organization, and 1,050 manpower;
- special-forces classification and a 180-day training requirement;
- 0.32 supply use and an asymmetric assault profile;
- positive attack in forest, jungle, marsh, urban, and fort terrain;
- penalties in plains, desert, mountains, river crossings, and amphibious assaults.

Each battalion requires 170 infantry equipment, 70 support equipment, 100 gas-mask crates, 60 decontamination sets, 15 CBRN instruments, and 30 trucks. All six archetypes are `essential`, so missing equipment reduces the formation's native contribution through the engine's reinforcement and shortage system.

The battalion deliberately has no standing chemical cylinder, shell lot, nerve-agent store, or biological bomb requirement. Its presence in a division never creates contamination, casualties, outbreaks, evidence, or Condemnation. Any later operation involving the formation must reserve and consume a selected payload before calling the shared exposure pipeline.

## Technology and doctrine ownership

- `chaos_battalion_tech` is the hidden doctrine-only base unlock.
- `chaos_battalion_1939` remains a hidden no-bonus compatibility alias.
- `chaos_battalion_1942` is the doctrine-only improvement and grants only the matrix-mapped organization and breakthrough bonuses.
- Stage 5 owns final Extermination Columns mastery pacing, prerequisites, doctrine balance, and Condemnation mitigation.

The old passive daily/combat release hooks are disconnected in `common/on_actions/chaosx_on_actions_chemical_warfare.txt`. Legacy helper identifiers remain resolvable until the Stage 6 route migration proves that no external caller depends on them.

## AI use

The baseline `cbrn_chemical_assault` role in `common/ai_templates/cbrn_regimental_support.txt` may include Chaos Assault Battalions only after the doctrine unlock, use-policy gate, protective-equipment bill, and real chemical-payload stock signal are all satisfied. Stage 10 owns country-specific route preferences and target-aware force ratios.

## Assets

Final registered assets are:

- `gfx/interface/counters/divisions_large/unit_chaos_battalion_icon.dds`
- `gfx/interface/counters/divisions_small/onmap_unit_chaos_battalion_icon.dds`
- `gfx/interface/technologies/chaos_battalion.dds`
- `gfx/interface/technologies/chaos_battalion3.dds`

The counter sprites are registered in `interface/chaosx_subuniticons.gfx`; the technology sprites are registered in `interface/chaosx_techtree.gfx`. Source masters, processed files, contact sheets, and the asset manifest belong to `docs/assets/chaos_warfare_system/stage_3_regimental_support/`.

## Future integration

- Stage 5 completes the doctrine track and officer-corps integration without broad permanent-stat stacking.
- Stage 6 migrates every chemical delivery route to exact payload reservation, consumption, and shared exposure.
- Stage 9 removes the remaining doctrine/genocide cross-links and implements targeted nerve-agent suppression as an independent consequence-heavy operation.
- Stage 10 validates differentiated AI force use and production against representative country profiles.
