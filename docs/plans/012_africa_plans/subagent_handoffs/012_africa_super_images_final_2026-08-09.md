# Event 012 Africa final super-event image handoff

Status: complete for the exact four requested super-event images, with parent visual review still required before permanent promotion or temporary-workspace cleanup.

Date: 2026-08-09.

Scope: generated non-icon alternate-history super-event art only. The package contains Africa Is One, Scramble Response, Continental Wars, and The World. No extra super-event role, host grid, route grid, portrait, icon, news image, animation, GFX edit, gameplay edit, localisation edit, GUI edit, sound edit, focus edit, country edit, or spreadsheet edit was made.

## Runtime handoff

| Role | Slot | Sprite | Final DDS | Consumer |
| --- | --- | --- | --- | --- |
| Africa Is One | 101 | `GFX_super_event_012_africa_africa_is_one` | `gfx/super_events/012_africa/super_event_012_africa_africa_is_one.dds` | `interface/012_africa_event_pictures.gfx` |
| Scramble Response | 102 | `GFX_super_event_012_africa_scramble_response` | `gfx/super_events/012_africa/super_event_012_africa_scramble_response.dds` | `interface/012_africa_event_pictures.gfx` |
| Continental Wars | 103 | `GFX_super_event_012_africa_continental_wars` | `gfx/super_events/012_africa/super_event_012_africa_continental_wars.dds` | `interface/012_africa_event_pictures.gfx` |
| The World | 104 | `GFX_super_event_012_africa_the_world` | `gfx/super_events/012_africa/super_event_012_africa_the_world.dds` | `interface/012_africa_event_pictures.gfx` |

All four final DDS files are exactly `457x328`, uncompressed 32-bit BGRA, one level, and decode successfully to opaque RGBA images. The DDS round-trip comparison and native-size visual review are retained in `docs/assets/012_africa/super_events/images_final/contact/super_event_012_africa_images_contact_sheet.png`.

## Visual direction and acceptance

Africa Is One uses a central continental congress table and seal with delegates framed by a rail station and harbor, making political completion the subject rather than a map.

Scramble Response uses a fortified African harbor, signal apparatus, treaty folder, organized dock response, and distant foreign battleships to reverse the colonial gaze.

Continental Wars uses a shattered railway bridge, armored trains, period aircraft, and two rival continental armies to communicate a campaign-defining war without science-fiction technology or a globe diagram.

The World uses a diverse global council, an empty final seat, a six-part continental seal, lowered standards, and a damaged industrial horizon to communicate exhausted finality without a planet explosion.

The canonical reference family inspected was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event/`, especially the 457x328 contact sheet and League Formation institutional composition. Generation used the built-in `$imagegen` workflow, with full prompts and output ids in `docs/assets/012_africa/super_events/images_final/prompts/generation_prompts.md`.

## Package contents

- Four generated source PNG masters under `docs/assets/012_africa/super_events/images_final/sources/`.
- Four processed `457x328` RGBA PNG previews under `docs/assets/012_africa/super_events/images_final/processed/`.
- Four final runtime DDS files under `gfx/super_events/012_africa/`.
- Four decoded DDS round-trip PNGs under `docs/assets/012_africa/super_events/images_final/roundtrip/`.
- The 3-column, 4-role contact sheet under `docs/assets/012_africa/super_events/images_final/contact/super_event_012_africa_images_contact_sheet.png`.
- Generation prompts and source-mode rationale under `docs/assets/012_africa/super_events/images_final/prompts/generation_prompts.md`.
- Manifest, hashes, source-mode evidence, and requirement-to-runtime mapping under `docs/assets/012_africa/super_events/images_final/manifest.md`.
- Exact sprite and `.gfx` handoff under `docs/assets/012_africa/super_events/images_final/gfx_handoff.md`.

## Ignored material for the parent

- `docs/assets/012_africa/super_events/current_runtime_previews/` is inspection-only output derived from the superseded DDS files and is not part of the final package.
- The first generated The World candidate `exec-31479ca9-8254-4fa3-9edf-4da620a4a581.png` was rejected because the council read as Western-only. It was not copied into the final source folder.
- No other generated candidate was promoted, and no fifth image was created.

## Parent action

Review the contact sheet and the final DDS textures, then retain the stable sprite names and existing texture path contracts during runtime wiring. The image package is complete within this bounded asset scope; final in-game presentation and consumer validation remain parent-owned.


Repository note: the existing .gitignore marks docs/assets/012_africa/ ignored, so source masters, processed previews, prompts, manifest, contact sheet, round-trips, and GFX handoff remain workspace evidence unless the parent intentionally force-adds them or promotes their durable facts elsewhere.
