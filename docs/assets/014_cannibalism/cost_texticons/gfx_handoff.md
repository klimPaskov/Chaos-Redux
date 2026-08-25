# Event 014 Cannibalism cost texticon GFX handoff

## Registration

`interface/014_cannibalism_texticons.gfx` is the Event14-owned registration file. It defines five single-frame `spriteType` entries and points them to the five DDS files under `gfx/texticons/014_cannibalism/`. The file uses the repository texticon convention `legacy_lazy_load = no` and does not modify the shared `interface/chaosx_texticons.gfx` registry.

The `GFX_` sprite names are the engine registration identifiers. Localisation consumes the matching short tokens without the `GFX_` prefix, following the existing Famine Deaths pattern where `GFX_fm_deaths_famine` is consumed as `£fm_deaths_famine`.

## Exact semantic handoff

| Cost meaning in Event14 | Use this token | Do not substitute |
| --- | --- | --- |
| Larder Stores | `£cannibalism_larder_texticon` | Do not use `£supply_texticon`, food, or the existing Event14 larder meter art. |
| Consumed state population | `£cannibalism_state_population_texticon` | Do not use generic manpower or the enemy-loss receipt. |
| Victory Receipt earned from distinct enemy capitulation | `£cannibalism_victory_receipt_texticon` | Do not use the enemy-loss or convoy-hunt receipt. |
| Convoy-Hunt Receipt from naval harvest | `£cannibalism_convoy_hunt_receipt_texticon` | Do not use the vanilla convoy resource icon as a receipt ledger. |
| Enemy-Loss Receipt from recorded enemy casualties | `£cannibalism_enemy_loss_receipt_texticon` | Do not use the victory receipt, red-cross, skull, or generic manpower icon. |

## Localisation owner handoff

The parent Event14 owner should add the matching `£` tokens to the literal cost strings in `localisation/english/014_cannibalism_l_english.yml` without changing the ledger names or their numeric values. Larder appears throughout the raise, warlord, unified, and Wendigo decision cost text. Consumed state population appears in the controlled-state, unified consumption, terminal-consumption, and Wendigo population costs. `Victory Receipt` is the battlefield-consumption receipt. `Convoy-Hunt Receipt` is the naval harvest receipt. `Enemy-Loss Receipt` is the Wendigo pack receipt earned from recorded enemy casualties.

This asset package does not edit localisation because the requested scope is Event14-owned visual registration and asset documentation only.

## Visual and technical evidence

- Review sheet: `contact_sheets/cost_texticons_contact.png`.
- Contact-sheet SHA-256: `fcd6897ce307dc45316bfdfda609e7c34e9125eb57e943ec0a677efabb7331c1`.
- Every native source is an RGBA PNG at 1254x1254 with alpha extrema 0–255 and transparent unused canvas; no background-removal fallback was used.
- Every processed preview is RGBA at exactly 18x18 with alpha extrema 0–255.
- Every decoded DDS roundtrip is RGBA at exactly 18x18 with alpha extrema 0–255 and transparent corners preserved.
- Every final DDS is 1424 bytes with 18x18 header dimensions, legacy uncompressed BGRA8 masks, `flags = 65`, and a zero fourCC, matching the installed uncompressed vanilla texticon family.
- The contact sheet shows native source, enlarged exact-size processed preview, and DDS roundtrip side by side for all five assets.

## Files for parent review

- `interface/014_cannibalism_texticons.gfx`.
- `gfx/texticons/014_cannibalism/cannibalism_larder_texticon.dds`.
- `gfx/texticons/014_cannibalism/cannibalism_state_population_texticon.dds`.
- `gfx/texticons/014_cannibalism/cannibalism_victory_receipt_texticon.dds`.
- `gfx/texticons/014_cannibalism/cannibalism_convoy_hunt_receipt_texticon.dds`.
- `gfx/texticons/014_cannibalism/cannibalism_enemy_loss_receipt_texticon.dds`.
- `docs/assets/014_cannibalism/cost_texticons/manifest.md`.
- `docs/assets/014_cannibalism/cost_texticons/prompts/generation_prompts.md`.

Asset production is complete. Localisation token insertion and live in-game visual acceptance remain with the parent Event14 owner by scope.
