# Event 011 asset validation

## Current package result

The current validation evidence is `docs/assets/011_secret_alliance/validation_icons_ui_animation.txt` plus the raster checks recorded below. Final gameplay and balance freeze `1c87d923` preserves the validated sprite paths, eight-frame confrontation-emblem animation plus still fallback, six achievement triplets, and slot `73` reveal image wiring.

- Runtime DDS targets: `57`
- DDS encoding: one-mip 32-bit BGRA/B8G8R8A8-style masks on every target
- Runtime DDS dimensions: `32x32`, `64x64`, `128x96`, `256x24`, `720x360`, `736x96`, and `1024x96`
- Transparent runtime assets checked: `38`
- Visible alpha pixels checked for chroma fringe: `143172`
- Visible bright chroma-green pixels: `0`
- Decision source artworks: `17` unique
- Idea source artworks: `7` unique
- Animation source frames: `8` unique
- Animation processed frames: `8` unique
- Animation sheet: `1024x96` with eight exact `128x96` columns
- Suspect-card sheet: `736x96` with four exact `184x96` columns
- Achievement triplets: six exact normal, grey, and recovered-overlay composites

## Event, news, and super-event rasters

The nine large rasters remain separately verified against their processed PNGs.

- Seven report cards are `210x176` with transparent corners.
- `news_event_public_coalition` is `397x153` and true grayscale before DDS conversion.
- `super_event_public_reveal` is `457x328` and was reviewed through the verified super-event aperture.
- All nine source rasters have distinct SHA-256 hashes.
- DDS decoding matches the processed PNG pixels.

The political-attack report art is intentionally shared by `chaosx.nr11.4`, `chaosx.nr11.10`, and the Evolution II rare assassination attempt `chaosx.nr11.21`. This is one event-family scene reuse, not a missing asset. The 14-day reveal slot and day-15 presentation cleanup change scripted presentation lifetime only; they do not alter the validated super-event DDS or sprite registration.

## Historical processor record

The original raster pass used the byte-verified project processor `process_report_event_image.py` with SHA-256 `5B51613F391934960A8310268041C66B00FDD31BC12DA2393EB02C8F3DC87BD9`. The full source-restoration record remains in `docs/assets/011_secret_alliance/manifest.md`. The old worktree path is retained there as production chronology and is not the current validation authority.
