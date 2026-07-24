# Event 016 achievement icon manifest

## Contract

Event 016 owns exactly seventeen achievement identities and fifty-one final DDS files. Each identity requires a distinct 64x64 completed icon, a matching grey icon, and a matching not-eligible icon. Source masters must remain editable PNGs at no less than 512x512. The completed image establishes the composition; the grey and not-eligible variants must be derived from that same approved master so silhouettes remain identical.

Final DDS directory: `gfx/achievements/`

Sprite registry: `interface/chaosx_achievements.gfx`

Required contact sheet: `docs/assets/016_brilliant_scientist/contact_sheets/016_brilliant_scientist_achievement_icons_contact_sheet.png`

Kruger's portrait is not an acceptable default motif. At 64x64, every icon must remain distinguishable by its central silhouette and not by tiny text.

## Identity directions

| Achievement ID | Completed-icon direction |
| --- | --- |
| `016_brilliant_scientist_borrowed_century` | A period calendar overtaken by a vacuum tube, rocket arc, atom orbit, gear, and medical lens. |
| `016_brilliant_scientist_every_door` | Six visibly different laboratory doors opening around one impossible central light. |
| `016_brilliant_scientist_public_method` | An open technical folio and precision instrument supported by several different hands. |
| `016_brilliant_scientist_the_one_who_left` | A lone scientist silhouette crossing a hard border between two laboratory skylines. |
| `016_brilliant_scientist_clean_break` | A laboratory key resting beside an intact national academy under calm daylight. |
| `016_brilliant_scientist_approve_everything` | A government fountain pen signing beneath a dangerous stack of incompatible project diagrams. |
| `016_brilliant_scientist_the_former_host` | Conventional soldiers entering a reclaimed laboratory past clone, machine, and beast silhouettes. |
| `016_brilliant_scientist_combined_arms_redefined` | Three unmistakably different project formations advancing beneath one precise command emblem. |
| `016_brilliant_scientist_clever_girl` | A predatory dinosaur silhouette entering a monumental period capital skyline. |
| `016_brilliant_scientist_the_machine_continues` | Kruger's empty chair before a live branching command network. |
| `016_brilliant_scientist_population_one` | Repeated human profiles that begin identical and resolve into distinct individual faces. |
| `016_brilliant_scientist_yesterday_sent_help` | Two versions of one defensive line joined by a broken clock and phase ring. |
| `016_brilliant_scientist_not_from_here` | A human laboratory silhouette split by unfamiliar anatomy and a distant stellar vector. |
| `016_brilliant_scientist_no_second_sun` | A dark singularity core safely opened beneath an unbroken ordinary sky. |
| `016_brilliant_scientist_the_last_calculation` | A calculation grid collapsing inward toward a destructive global core; severe, not celebratory. |
| `016_brilliant_scientist_the_world_is_the_laboratory` | A globe converted into a precise network of laboratory nodes without map text. |
| `016_brilliant_scientist_ordinary_people_won` | Human, clone, and machine hands rebuilding one damaged laboratory together. |

## Exact output triplets

For every ID above, create:

- `<achievement_id>.dds`
- `<achievement_id>_grey.dds`
- `<achievement_id>_not_eligible.dds`

The not-eligible variant must preserve the underlying composition and add the established Chaos Redux ineligibility treatment; it must not be an unrelated replacement image. All 51 texture paths are already registered under `GFX_achievement_<achievement_id>`, `GFX_achievement_<achievement_id>_grey`, and `GFX_achievement_<achievement_id>_not_eligible`.

## Current status

- Gameplay registry: wired, seventeen entries.
- Sprite declarations: wired, fifty-one entries.
- Source masters: complete; seventeen built-in ImageGen masters are retained under `docs/assets/016_brilliant_scientist/source_png/` at 1254x1254 RGB.
- Alpha masters: complete; chroma-key removal outputs are retained under `docs/assets/016_brilliant_scientist/alpha_png/` at 1254x1254 RGBA with transparent corners.
- Processed PNG previews: complete; fifty-one exact 64x64 RGBA files are retained under `docs/assets/016_brilliant_scientist/processed_png/`.
- Final DDS files: complete; fifty-one one-level uncompressed 64x64 BGRA DDS files are in `gfx/achievements/`.
- Contact sheet: complete at `docs/assets/016_brilliant_scientist/contact_sheets/016_brilliant_scientist_achievement_icons_contact_sheet.png`.
- Prompt record: `docs/assets/016_brilliant_scientist/prompts/achievement_icon_generation_record.md`.
- Dimension and SHA-256 evidence: `docs/assets/016_brilliant_scientist/package_records/achievement_icon_hashes.json`.
- No substitute, reused achievement art, or portrait fallback is approved.

## Completed package evidence

Every row below has one generated source master, one alpha extraction, one completed PNG, one grayscale PNG, one overlay-composited not-eligible PNG, and the matching three root-level DDS files. Runtime achievement ids remain unchanged.

| Achievement id | Completed DDS | Grey DDS | Not-eligible DDS |
| --- | --- | --- | --- |
| `016_brilliant_scientist_borrowed_century` | `gfx/achievements/016_brilliant_scientist_borrowed_century.dds` | `gfx/achievements/016_brilliant_scientist_borrowed_century_grey.dds` | `gfx/achievements/016_brilliant_scientist_borrowed_century_not_eligible.dds` |
| `016_brilliant_scientist_every_door` | `gfx/achievements/016_brilliant_scientist_every_door.dds` | `gfx/achievements/016_brilliant_scientist_every_door_grey.dds` | `gfx/achievements/016_brilliant_scientist_every_door_not_eligible.dds` |
| `016_brilliant_scientist_public_method` | `gfx/achievements/016_brilliant_scientist_public_method.dds` | `gfx/achievements/016_brilliant_scientist_public_method_grey.dds` | `gfx/achievements/016_brilliant_scientist_public_method_not_eligible.dds` |
| `016_brilliant_scientist_the_one_who_left` | `gfx/achievements/016_brilliant_scientist_the_one_who_left.dds` | `gfx/achievements/016_brilliant_scientist_the_one_who_left_grey.dds` | `gfx/achievements/016_brilliant_scientist_the_one_who_left_not_eligible.dds` |
| `016_brilliant_scientist_clean_break` | `gfx/achievements/016_brilliant_scientist_clean_break.dds` | `gfx/achievements/016_brilliant_scientist_clean_break_grey.dds` | `gfx/achievements/016_brilliant_scientist_clean_break_not_eligible.dds` |
| `016_brilliant_scientist_approve_everything` | `gfx/achievements/016_brilliant_scientist_approve_everything.dds` | `gfx/achievements/016_brilliant_scientist_approve_everything_grey.dds` | `gfx/achievements/016_brilliant_scientist_approve_everything_not_eligible.dds` |
| `016_brilliant_scientist_the_former_host` | `gfx/achievements/016_brilliant_scientist_the_former_host.dds` | `gfx/achievements/016_brilliant_scientist_the_former_host_grey.dds` | `gfx/achievements/016_brilliant_scientist_the_former_host_not_eligible.dds` |
| `016_brilliant_scientist_combined_arms_redefined` | `gfx/achievements/016_brilliant_scientist_combined_arms_redefined.dds` | `gfx/achievements/016_brilliant_scientist_combined_arms_redefined_grey.dds` | `gfx/achievements/016_brilliant_scientist_combined_arms_redefined_not_eligible.dds` |
| `016_brilliant_scientist_clever_girl` | `gfx/achievements/016_brilliant_scientist_clever_girl.dds` | `gfx/achievements/016_brilliant_scientist_clever_girl_grey.dds` | `gfx/achievements/016_brilliant_scientist_clever_girl_not_eligible.dds` |
| `016_brilliant_scientist_the_machine_continues` | `gfx/achievements/016_brilliant_scientist_the_machine_continues.dds` | `gfx/achievements/016_brilliant_scientist_the_machine_continues_grey.dds` | `gfx/achievements/016_brilliant_scientist_the_machine_continues_not_eligible.dds` |
| `016_brilliant_scientist_population_one` | `gfx/achievements/016_brilliant_scientist_population_one.dds` | `gfx/achievements/016_brilliant_scientist_population_one_grey.dds` | `gfx/achievements/016_brilliant_scientist_population_one_not_eligible.dds` |
| `016_brilliant_scientist_yesterday_sent_help` | `gfx/achievements/016_brilliant_scientist_yesterday_sent_help.dds` | `gfx/achievements/016_brilliant_scientist_yesterday_sent_help_grey.dds` | `gfx/achievements/016_brilliant_scientist_yesterday_sent_help_not_eligible.dds` |
| `016_brilliant_scientist_not_from_here` | `gfx/achievements/016_brilliant_scientist_not_from_here.dds` | `gfx/achievements/016_brilliant_scientist_not_from_here_grey.dds` | `gfx/achievements/016_brilliant_scientist_not_from_here_not_eligible.dds` |
| `016_brilliant_scientist_no_second_sun` | `gfx/achievements/016_brilliant_scientist_no_second_sun.dds` | `gfx/achievements/016_brilliant_scientist_no_second_sun_grey.dds` | `gfx/achievements/016_brilliant_scientist_no_second_sun_not_eligible.dds` |
| `016_brilliant_scientist_the_last_calculation` | `gfx/achievements/016_brilliant_scientist_the_last_calculation.dds` | `gfx/achievements/016_brilliant_scientist_the_last_calculation_grey.dds` | `gfx/achievements/016_brilliant_scientist_the_last_calculation_not_eligible.dds` |
| `016_brilliant_scientist_the_world_is_the_laboratory` | `gfx/achievements/016_brilliant_scientist_the_world_is_the_laboratory.dds` | `gfx/achievements/016_brilliant_scientist_the_world_is_the_laboratory_grey.dds` | `gfx/achievements/016_brilliant_scientist_the_world_is_the_laboratory_not_eligible.dds` |
| `016_brilliant_scientist_ordinary_people_won` | `gfx/achievements/016_brilliant_scientist_ordinary_people_won.dds` | `gfx/achievements/016_brilliant_scientist_ordinary_people_won_grey.dds` | `gfx/achievements/016_brilliant_scientist_ordinary_people_won_not_eligible.dds` |
