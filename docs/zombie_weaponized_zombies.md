# Weaponize the Zombies

## Overview

`Weaponize the Zombies` is the long-form offensive branch of the zombie special-project system.
It sits in the biowarfare facility once the outbreak is active and turns the zombie outbreak into a configurable strike weapon instead of a passive world threat.

The project does not produce one fixed result.
It builds a hidden zombie profile from repeated prototype rewards, then resolves that profile into a final outbreak archetype on completion.

Disease identity and behavior are not the same thing.
The actual spawned battalion/template family now comes from the disease classification and life-state choices, while obedience, target selection, and betrayal remain behavior layers applied through outbreak ideas and flags.

## Research flow

1. `Initial Acquisition` starts the profile and marks the country as having entered the program.
2. `Nature of the Disease` determines the broad scientific or extra-scientific explanation for the zombie.
3. `Life State` determines whether the infected are dead, alive, fragmented, or transformed.
4. `Human Experimentation` consumes `1000` manpower and escalates the program into live testing.
5. `Resource Allocation` trades safety for program scale and accident risk.
6. The six tuning passes shape:
   - strength
   - infectiousness
   - speed
   - durability
   - cure resistance
   - friendliness / obedience
7. `Field Testing` may test on enemy territory, zombie territory, or domestically depending on the final profile and local war state.
8. `Forbidden Branches` can push the zombie toward more extreme outcomes.
9. On completion, a conclusions event summarizes the resulting archetype and unlocks production plus raids.

The project no longer pulls generic prototype rewards.
Its key choices now follow a mandatory ordered chain so the player establishes subjects first, then determines zombie nature and life state, and only after that gets the detailed stat-tuning prompts.
Each step now writes its own completion flag and unlocks the next step, so the project cannot skip ahead to later zombie tuning choices.

Current project pacing:

- startup cost: `1` biowarfare breakthrough
- prototype progress per iteration: `8`
- containment accident MTTH: intentionally very rare, and inactive until `Nature of the Disease` has been chosen

## Disease types

Weaponized outbreaks now resolve into one of these battalion/template families:

- `Infected Horde`
- `Rabid Horde`
- `Parasitic Horde`
- `Mutant Horde`
- `Undead Horde`
- `Necrotic Horde`
- `Demonic Zombie Horde`

These unit families determine:

- manpower per battalion
- speed
- baseline attack and breakthrough
- baseline staying power
- baseline armor / hardness where relevant

The project strength sliders do not create separate battalion classes for mild, medium, or extreme variants.
Those broader performance swings still come from the outbreak's ideas and stage/tier setup.

## World pressure and late-evolution drift

The final visible horde type is no longer a pure one-to-one lookup from the research choices.
The project still records the chosen disease nature and life-state, but completion now also reads the wider apocalypse state:

- the current global `chaos_tier`
- the main `ZZZ` horde's `zombie_current_tier`
- whether forbidden branches were used
- whether the profile became transformed or mutation-heavy

Low-chaos worlds still mostly stay on the ordinary family implied by the research path.
As the chaos meter rises and the zombie evolution reaches tier `2` or `3`, transformed and extreme zombies gain a growing chance to drift upward into `Mutant Horde` or `Demonic Zombie Horde`.
That keeps extreme but still usable weapon outputs rare early while making them meaningfully more common once the world is already deteriorating.

`Wendigo Pack` is not a normal successful project result.
It is reserved for a catastrophic completion-stage failure.

## Behavior outcomes

The zombie resolves into one of several behavior profiles:

- `Rabid Horde`
- `Necrotic Siege`
- `Parasitic Directed Strain`
- `Controlled Loyalty Strain`
- `Purifier Strain`
- `Semi-Sapient Strain`
- `Controlled Loyalty Conditioning`
- `Canonical Convergence`
- `Wendigo Convergence`

These outcomes change outbreak behavior, the creator-side temporary cure advantage, bomb production cost, and whether spawned outbreak countries merge back into the main `ZZZ` horde.
They do not define the battalion family on their own.
One selective-control branch can later fail in the field, but that instability is no longer labeled as its own visible zombie type.

## Runtime behavior

- Completion gives the country `zombie_disease_bomb_delivery_systems` and an initial payload stockpile.
- The unlocked raid tier depends on the final infectiousness score.
- Weaponized outbreaks copy the creator's disease nature and life-state flags before spawning, then load either `history/units/ZZZ_weaponized_1936.txt` or `history/units/ZZZ_weaponized_hardened_1936.txt` and unlock only the matching template.
- The visible outbreak family is resolved into explicit type flags before spawning, so leaders, templates, and created divisions all read the same final disease-type result instead of re-deriving it separately.
- Armor is no longer granted purely by disease family for the ordinary outbreak families. It only appears on the hardened outbreak path when both strength and durability resolve high enough.
- `Wendigo Pack` sits outside the normal successful outbreak ladder: it is always armored, always hostile, and only appears when the project catastrophically fails at completion.
- Zombies marked `zombies-only` can only target zombie-controlled states and can earn the `Fight Fire With Fire` achievement.
- Independent weaponized outbreaks are excluded from the base zombie auto-merge rules in `common/on_actions/chaosx_on_actions.txt`.
- Creator-friendly zombies store their protected creator in outbreak-local diplomacy state and can later lose that protection through an unannounced field-control failure event.
- Weaponized outbreak leader names are now type-based (`Undead Horde`, `Necrotic Horde`, `Demonic Zombie Horde`, etc.) rather than behavior-profile titles.

## Wendigo world-end branch

If a `Wendigo Pack` survives into `chaos_tier = 5`, it can now force its own world-end scenario.

The Wendigo itself now comes from a completion failure, not from a normal successful result.
When that happens, the incident spawns in a controlled state with a `biowarfare_facility`, uses the dedicated armored Wendigo battalion, and scales its initial division count upward by `+5` for each current chaos tier.

The later world-end check is dynamic and continent-based:

- the zombie must be a weaponized Wendigo outbreak country
- the global chaos meter must already be in the world-end tier
- the Wendigo must control at least `85%` of one continent and be missing no more than `3` states there

Once that threshold is met, the outbreak gains the `Wendigo Ascendancy` idea, fires the Wendigo super event, and sets the campaign end-state to `world_end_wendigo`.
This is separate from the ordinary `Zombie Apocalypse` branch and reflects a project-ending catastrophe becoming the dominant terminal threat on the map.

## Event chain

The system now uses `events/zombie_weaponized_special_projects.txt` for:

- completion conclusions
- completion-stage Wendigo incident failure
- enemy field-test results
- domestic safe test results
- domestic outbreak results
- MTTH lab containment failure during research
- hidden creator-betrayer resolution
- creator-side betrayal notification

## Files touched by the system

- `common/special_projects/projects/zombie_weaponized_projects.txt`
- `common/script_constants/zombie_special_project_constants.txt`
- `common/scripted_effects/zombie_special_project_effects.txt`
- `common/scripted_triggers/002_zombie_outbreak_triggers.txt`
- `common/raids/zombie_weaponized_raids.txt`
- `common/ideas/zombie_weaponized_ideas.txt`
- `common/technologies/zombie_special_project_technologies.txt`
- `events/zombie_weaponized_special_projects.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `common/scripted_localisation/zombie_weaponized_scripted_localisation.txt`
- `common/units/zombies.txt`
- `history/units/ZZZ_weaponized_1936.txt`
- `history/units/ZZZ_weaponized_hardened_1936.txt`
- `interface/chaosx_subuniticons.gfx`
- `interface/chaosx_texticons.gfx`
- `localisation/english/chaosx_events_l_english.yml`
- `localisation/english/chaosx_units_l_english.yml`
- `localisation/english/chaosx_characters_l_english.yml`

## Icon wiring

Project icon:
- File: `gfx/interface/special_project/project_icons/sp_weaponize_the_zombies.dds`
- GFX definition: `interface/special_projects/biowarfare.gfx`
- Token: `GFX_sp_weaponize_the_zombies`

Payload equipment icon:
- File: `gfx/interface/technologies/zombie_disease_bomb_equipment.dds`
- GFX definition: `interface/chaosx_equipment.gfx`
- Token: `GFX_zombie_disease_bomb_equipment_medium`

Technology icon:
- File: `gfx/interface/technologies/zombie_disease_bomb_equipment.dds`
- GFX definition: `interface/chaosx_techtree.gfx`
- Token: `GFX_zombie_disease_bomb_delivery_systems_medium`

Super-event art:
- File: `gfx/super_events/super_event_wendigo.dds`
- GFX definition: `interface/chaosx_super_events.gfx`
- Token: `GFX_super_event_wendigo`

Weaponized zombie battalion icons:
- Large counter files:
  - `gfx/interface/counters/divisions_large/unit_infected_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_rabid_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_parasitic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_mutant_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_undead_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_necrotic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_demonic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_wendigo_zombies_icon.dds`
- Small on-map files:
  - `gfx/interface/counters/divisions_small/onmap_unit_infected_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_rabid_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_parasitic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_mutant_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_undead_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_necrotic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_demonic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_wendigo_zombies_icon.dds`
- Text icon files:
  - `gfx/texticons/unit_infected_zombies_icon_small.dds`
  - `gfx/texticons/unit_rabid_zombies_icon_small.dds`
  - `gfx/texticons/unit_parasitic_zombies_icon_small.dds`
  - `gfx/texticons/unit_mutant_zombies_icon_small.dds`
  - `gfx/texticons/unit_undead_zombies_icon_small.dds`
  - `gfx/texticons/unit_necrotic_zombies_icon_small.dds`
  - `gfx/texticons/unit_demonic_zombies_icon_small.dds`
- `gfx/texticons/unit_wendigo_zombies_icon_small.dds`
  - `gfx/interface/counters/divisions_large/unit_armored_undead_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_armored_necrotic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_large/unit_armored_demonic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_armored_undead_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_armored_necrotic_zombies_icon.dds`
  - `gfx/interface/counters/divisions_small/onmap_unit_armored_demonic_zombies_icon.dds`
  - `gfx/texticons/unit_armored_undead_zombies_icon_small.dds`
  - `gfx/texticons/unit_armored_necrotic_zombies_icon_small.dds`
  - `gfx/texticons/unit_armored_demonic_zombies_icon_small.dds`
- GFX definitions:
  - `interface/chaosx_subuniticons.gfx`
  - `interface/chaosx_texticons.gfx`
- Tokens:
  - `GFX_unit_infected_zombies_icon_medium`
  - `GFX_unit_rabid_zombies_icon_medium`
  - `GFX_unit_parasitic_zombies_icon_medium`
  - `GFX_unit_mutant_zombies_icon_medium`
  - `GFX_unit_undead_zombies_icon_medium`
  - `GFX_unit_necrotic_zombies_icon_medium`
  - `GFX_unit_demonic_zombies_icon_medium`
  - `GFX_unit_wendigo_zombies_icon_medium`
  - `GFX_unit_armored_undead_zombies_icon_medium`
  - `GFX_unit_armored_necrotic_zombies_icon_medium`
  - `GFX_unit_armored_demonic_zombies_icon_medium`
  - `GFX_unit_infected_zombies_icon_small`
  - `GFX_unit_rabid_zombies_icon_small`
  - `GFX_unit_parasitic_zombies_icon_small`
  - `GFX_unit_mutant_zombies_icon_small`
  - `GFX_unit_undead_zombies_icon_small`
  - `GFX_unit_necrotic_zombies_icon_small`
  - `GFX_unit_demonic_zombies_icon_small`
  - `GFX_unit_wendigo_zombies_icon_small`
  - `GFX_unit_armored_undead_zombies_icon_small`
  - `GFX_unit_armored_necrotic_zombies_icon_small`
  - `GFX_unit_armored_demonic_zombies_icon_small`

## Future ideas

- Give creator-friendly zombies more explicit diplomacy behavior beyond war-target filtering, such as temporary access or cooperation effects.
- Add more visible strike aftermath on target states so each archetype leaves clearer strategic fingerprints.
- Add continent-specific flavour text or event-log details for which region first falls to Wendigo dominance.
