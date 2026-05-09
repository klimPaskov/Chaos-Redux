# Mengele Clone World Order Asset Manifest

## Package

This package supports the Angelic Directorate clone world-end path documented in `docs/events/germany_mengele_clone_world_order_spec.md`.

Source and processed PNG previews live under:

- `docs/assets/mengele_clone_world_order/source_png/`
- `docs/assets/mengele_clone_world_order/processed_png/`

## Final Assets

| Asset | Type | Final path | Sprite or tag | Size |
| --- | --- | --- | --- | --- |
| Angelic Directorate flag | flag | `gfx/flags/germany_mengele_angelic_directorate.tga` | `germany_mengele_angelic_directorate` | 82x52 |
| Angelic Directorate flag | flag | `gfx/flags/medium/germany_mengele_angelic_directorate.tga` | `germany_mengele_angelic_directorate` | 42x26 |
| Angelic Directorate flag | flag | `gfx/flags/small/germany_mengele_angelic_directorate.tga` | `germany_mengele_angelic_directorate` | 10x7 |
| Clone Client flag | flag | `gfx/flags/mengele_clone_client_regime.tga` | `mengele_clone_client_regime` | 82x52 |
| Clone Client flag | flag | `gfx/flags/medium/mengele_clone_client_regime.tga` | `mengele_clone_client_regime` | 42x26 |
| Clone Client flag | flag | `gfx/flags/small/mengele_clone_client_regime.tga` | `mengele_clone_client_regime` | 10x7 |
| Centralized Replication Command | idea icon | `gfx/interface/ideas/idea_mengele_clone_world_order.dds` | `GFX_idea_mengele_clone_world_order` | 64x64 |
| Clone Client Regime | idea icon | `gfx/interface/ideas/idea_mengele_clone_client_state.dds` | `GFX_idea_mengele_clone_client_state` | 64x64 |
| Hidden Clone Network | decision icon | `gfx/interface/decisions/decision_mengele_hidden_clone_network.dds` | `GFX_decision_mengele_hidden_clone_network` | 32x32 |
| The Numbered World | focus icon | `gfx/interface/goals/focus_mengele_numbered_world.dds` | `GFX_focus_mengele_numbered_world` | 94x86 |
| Angelic World Order | super-event art | `gfx/super_events/super_event_angelic_world_order.dds` | `GFX_super_event_angelic_world_order` | 457x328 |

Ideology-suffixed flag copies are included for the Angelic Directorate and clone client cosmetic tags in all three flag folders so cosmetic lookup cannot fall through to a missing ideology flag.

## Wiring

- `interface/germany_mengele_world_order.gfx` registers the idea, decision, and focus sprites.
- `interface/chaosx_super_events.gfx` registers `GFX_super_event_angelic_world_order`.
- `common/countries/cosmetic.txt` assigns cosmetic colors for the Angelic Directorate and clone client regimes.
- `localisation/english/germany_mengele_l_english.yml` contains the matching names, descriptions, and super-event localisation.

## Source Notes

The source visuals are custom-generated symbolic Chaos Redux assets produced for this package. They use the requested red, black, and white authoritarian research-state palette.

The current Angelic World Order super-event art is generated symbolic artwork with no real-world extremist insignia. It shows a hidden biomedical command cathedral, rows of clone soldiers, laboratory tanks, and a winged medical-industrial statue to match the clone world-end activation.

## Super-Event Art Record

- Asset name: Angelic World Order
- Related event id: `super_event.13.*`
- Related event slug: `mengele_clone_world_order`
- Asset type: super-event image
- Intended in-game use: world-end super-event image for `GFX_super_event_angelic_world_order`
- Source mode: `image_gen`
- Image generation prompt: `Create a single HOI4 super-event image in a dark alternate-history documentary style, intended to be cropped to 457x328. Subject: "Angelic World Order" as a terrifying hidden clone-state activation. Scene: a vast underground biomedical command cathedral, rows of identical uniformed clone soldiers seen from behind, cold laboratory tanks and medical-industrial machinery lining the sides, a central winged statue or angelic medical emblem looming above a command dais, sterile lamps, black steel, pale stone, deep shadows, severe composition, high contrast, ominous ceremonial atmosphere. Visual language: cinematic black-and-white with restrained dark red accents, grainy wartime archival texture, realistic painted-photographic finish, strong central composition readable at small size. Avoid: text, captions, UI elements, watermarks, swastikas, real-world extremist insignia, real people, gore, cluttered tiny details.`
- Source PNG path: `docs/assets/mengele_clone_world_order/source_png/super_event_angelic_world_order_source.png`
- Processed PNG path: `docs/assets/mengele_clone_world_order/processed_png/super_event_angelic_world_order.png`
- Final DDS path: `gfx/super_events/super_event_angelic_world_order.dds`
- Target size: 457x328
- Sprite name: `GFX_super_event_angelic_world_order`
- `.gfx` file: `interface/chaosx_super_events.gfx`
- Related super-event: `13`
- Review status: `needs_user_review`
- Notes: cropped and resized to 457x328, converted to uncompressed ARGB8888 DDS, replacing the previous symbolic DDS under the same stable filename and sprite name.
- Asset status: `wired`
