# Weaponized Zombie Creator Overview Decision Category

## Overview

When a country successfully completes `Weaponize the Zombies`, it now gets a dedicated creator-only decision category named `Weaponized Zombie Outbreak`.

The category is read-only and appears from the completed creator country itself, using the existing `weaponized_zombies_completed` flag plus the resolved `weaponized_zombie_type_*` flag. It does not depend on a live deployed outbreak country, so the creator can inspect the final profile immediately after project completion and before launching any zombie payload raid.

## Flow

1. The special project resolves the zombie profile through `resolve_weaponized_zombie_profile`.
2. Successful completion applies `apply_weaponized_zombie_completed_bonuses`, which sets `weaponized_zombies_completed`.
3. Exactly one creator overview category becomes visible because the creator also has exactly one final `weaponized_zombie_type_*` flag.
4. The category localisation reads the creator's final profile variables and scripted localisation:
	- `GetWeaponizedZombieTypeName`
	- `GetWeaponizedZombieNatureSummary`
	- `GetWeaponizedZombieLifeStateSummary`
	- `GetWeaponizedZombieArchetypeSummary`
5. The category picture is selected by the internal category that matches the final type.

## Category Files

- Category definitions: `common/decisions/categories/chaosx_weaponized_zombie_creator_overview_categories.txt`
- Localisation: `localisation/english/chaosx_decisions_l_english.yml`

The implementation uses one internal category per final zombie type because HOI4 decision-category `picture` fields are static sprite references. The player still sees one category name and one overview at a time.

## Icons And Portraits

No new art is required. The category uses the existing weaponized zombie portrait sprites already wired in `interface/chaosx_characters.gfx`:

- `GFX_portrait_ZZZ_weaponized_infected`
- `GFX_portrait_ZZZ_weaponized_rabid`
- `GFX_portrait_ZZZ_weaponized_parasitic`
- `GFX_portrait_ZZZ_weaponized_mutant`
- `GFX_portrait_ZZZ_weaponized_undead`
- `GFX_portrait_ZZZ_weaponized_necrotic`
- `GFX_portrait_ZZZ_weaponized_demonic`

The source files live in:

- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_infected.dds`
- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_rabid.dds`
- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_parasitic.dds`
- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_mutant.dds`
- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_undead.dds`
- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_necrotic.dds`
- `gfx/leaders/ZZZ/portrait_ZZZ_weaponized_demonic.dds`

## Future Plans

- Add a small creator-side decision that reopens a report event if a longer narrative summary is needed later.
- Add profile-specific warning lines for creator betrayal, human-friendly targeting, and canonical convergence so the category can double as a deployment briefing.
