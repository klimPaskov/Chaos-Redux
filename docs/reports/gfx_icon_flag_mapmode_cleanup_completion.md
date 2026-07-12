# GFX, Icon, Flag, Map Mode, and Division Symbol Cleanup Completion Report

## Completed surfaces

### Biological operations and related actions

- Replaced the byte-identical vanilla sabotage placeholders used by all three biological outbreak operations.
- Added a dedicated `85x85` main operation icon and separately composed `48x48` map icon.
- Replaced all six reused vanilla phase sprites with three dedicated `210x176` phase scenes and three `59x58` small phase icons.
- Wired existing dedicated map icons to anthrax, plague, tularemia, smallpox, and zombie-cure raids through `custom_map_icon`.
- Added dedicated `32x32` icons for smallpox vaccination, biological stockpile release, and biological stockpile destruction.
- Corrected both special-project specializations to use vanilla's valid `GFX_sp_blueprint_bg_straight` sprite.

### Event 002 zombie categories

- Added dedicated `52x40` category icons for outbreak prevention, weaponized-zombie operations, the Anti-Zombie League, and all seven creator profiles.
- Retained the existing custom cure identity for the two cure categories.
- Replaced the nonexistent `GFX_decision_generic_democracy` reference with a dedicated migration-restriction decision icon.

### Japan chemical campaign

- Confirmed and updated the existing exact category ID `japan_chemical_campaign_category`.
- Added and wired `GFX_decision_category_japan_chemical_campaign` without inventing a replacement category.

### Scripted map modes

- Added the four official per-mode sprite names expected by the scripted-map-mode engine.
- Reused the existing death-skull and contamination-mask artwork from shared strip frames `18` and `19`.
- Created dedicated selected and deselected `20x18` DDS files for both map modes.
- Kept the shared strip at its correct `19` frames of `20` pixels each.

### Division-template picker

- Added biowarfare at safe custom picker index `44`.
- Added chemical warfare at safe custom picker index `45`.
- Added the required `76x42` large and `30x12` small sprites for both indices.

### Flags

- Repaired the real `KHW` TGA triplets by removing the full-height left-edge seam.
- Repaired the real `KHW_neutrality` TGA triplets by removing the full-height right-edge seam.
- Normalized 31 legacy custom flag identities across normal, medium, and small folders from 24-bit to required 32-bit TGA.
- Preserved the `82x52`, `41x26`, and `10x7` dimensions, bottom origin, filenames, and orientation for all 365 triplets.

### Broader GFX audit

- Added the missing acid-rain ending news sprite for its existing DDS.
- Corrected the Soviet-nukes event picture token's case to match the registered sprite.
- Recorded every remaining static sprite and loose texture gap in `docs/assets/shared_gfx_cleanup/missing_gfx_audit.md`.

## Primary files changed

### Wiring and gameplay references

- `interface/chaosx_gfx_cleanup.gfx`
- `interface/chaosx_operations.gfx`
- `interface/mapmodes_interface.gfx`
- `common/decisions/categories/002_zombie_outbreak_categories.txt`
- `common/decisions/categories/japan_chemical_campaign_categories.txt`
- `common/decisions/002_zombie_outbreak_decisions.txt`
- `common/decisions/biowarfare_disease_containment_decisions.txt`
- `common/decisions/chemical_warfare_decisions.txt`
- `common/decisions/condemnation_sanctions_decisions.txt`
- `common/operation_phases/chaosx_bioweapon_operation_phases.txt`
- `common/raids/biological_raids.txt`
- `common/special_projects/specialization/chaosx_specializations.txt`
- `events/023_soviet_nukes.txt`

### Final assets

- `gfx/interface/operations/chaosx_bioweapon/`
- `gfx/interface/decisions/002_zombie_outbreak/categories/`
- `gfx/interface/decisions/002_zombie_outbreak/decision_zombie_lift_migration_restrictions.dds`
- `gfx/interface/decisions/biowarfare/`
- `gfx/interface/decisions/japan_chemical_campaign/`
- `gfx/interface/counters/division_templates_large/custom_template_044.dds`
- `gfx/interface/counters/division_templates_large/custom_template_045.dds`
- `gfx/interface/counters/division_templates_small/custom_template_044.dds`
- `gfx/interface/counters/division_templates_small/custom_template_045.dds`
- `gfx/interface/mapmode/custom/`
- repaired TGA files under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`

### Documentation and source packages

- `docs/assets/002_zombie_outbreak/`
- `docs/assets/shared_gfx_cleanup/`
- `docs/systems/gfx_icon_flag_mapmode_cleanup.md`
- `docs/systems/state_map_modes.md`
- `docs/biological_warfare/bioweapon_operative_outbreak_operation.md`
- `docs/chemical_warfare/japan_chemical_campaign_decisions.md`
- `docs/events/002_zombie_outbreak.md`

## Visual acceptance

The deleted skill reference library was restored to 93 example PNGs under `.agents/skills/chaos-redux-event-assets/assets/`. Final generated assets were reviewed against those examples and the corresponding vanilla asset families. Earlier ornate variants were rejected. The approved assets use:

- restrained painterly silhouettes for decisions and categories
- sepia, grainy, brush-masked operation phases
- vanilla-compatible square and circular operation framing
- simple sage-green relief for division-template symbols

Every new icon has a generated source PNG, exact-size processed PNG, final DDS, manifest entry, GFX handoff, and contact-sheet review.

## Meaningful validation

- Verified 31 requested sprite definitions against exact existing texture paths, dimensions, and nontrivial alpha ranges.
- Confirmed the biological main/map DDS files no longer hash-identically to vanilla sabotage placeholders.
- Confirmed no Event 002 category retains a generic category sprite.
- Confirmed all five biological raid definitions request their dedicated existing map icon.
- Confirmed all 365 custom flag filename sets match across the three size folders, all files are 32-bit bottom-origin TGA, and the repaired KHW edge pixels match their adjacent artwork columns.
- Confirmed all 93 restored skill reference examples are present.

## Remaining missing GFX

The exhaustive remaining list contains 91 static sprite references and five inherited loose texture paths. They belong to unrelated Event 003 scripted-GUI states, Event 005 decisions/report art, Event 049 portrait art, Event 079 report art, and inherited technology-interface files. Each token, reference line, and expected path is listed in `docs/assets/shared_gfx_cleanup/missing_gfx_audit.md`.

These entries are not fallbacks for the requested cleanup and are not silently treated as complete; they remain explicit follow-up work for their owning event or interface packages.

## Routing and scope notes

- `chaosx_icon_artist` produced the full Event 002 category package.
- The shared systems icon subagent reached the image-generation safety boundary; the parent used the same official image-generation workflow with nonprocedural symbolic prompts and completed the full source/processed/DDS package.
- `chaosx_localisation_auditor` was not required because no visible localisation text or key changed.
- `chaosx_improvement_loop_planner` was not used because the work remained bounded GFX cleanup rather than a mechanic design expansion.

## Simplifications, omissions, and blockers

No requested asset, wiring surface, documentation item, or validation item was simplified or omitted. There are no blockers in the requested scope.
