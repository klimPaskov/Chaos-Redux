# Event 012 Africa Bestiary Actor Assets Handoff

Date: `2026-06-17`
Scope: static asset production only for fictional/nonhuman Bestiary actor tags `CTL`, `OKP`, `TRM`, `HGD`, and `GHC`. No gameplay, localisation, `.gfx`, or script edits.

## Source method

- All ten source images were created with `$imagegen`.
- Portraits are fictional/nonhuman institutional leader portraits, not real people and not human caricatures.
- Flags are original symbolic fictional flag designs created for HOI4 reduction, then resized into the required TGA triplets.

## Validation

- Verified all portrait DDS files exist and are exactly `156x210`.
- Verified all flag TGAs exist in normal, medium, and small sizes: `82x52`, `41x26`, `10x7`.
- Verified all TGAs report as `Targa image data - RGBA ...` and do not include a `- top` orientation suffix in `file` output.
- Reviewed portrait and flag contact sheets for basic readability.

## Asset package

| Tag | Asset | Source method | Source file | Processed file | Final file(s) | Dimensions | Notes / risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CTL` | leader portrait | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/leader_012_africa_ctl_chimpanzee_telegraph_league_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/leader_012_africa_ctl_chimpanzee_telegraph_league_processed.png` | `gfx/leaders/012_africa/leader_012_africa_ctl_chimpanzee_telegraph_league.dds` | source `1071x1469`; final `156x210` | Institutional nonhuman signal-marshal portrait. Uses explicit telegraph key and handprint motif. |
| `CTL` | flag family | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/CTL_flag_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/CTL_flag_processed.png` | `gfx/flags/CTL.tga`; `gfx/flags/medium/CTL.tga`; `gfx/flags/small/CTL.tga` | source `1573x1000`; finals `82x52`, `41x26`, `10x7` | Handprint and wire-key emblem reads well at normal/medium size. The side wire branches simplify heavily at `10x7`, which is expected. |
| `OKP` | leader portrait | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/leader_012_africa_okp_okapi_court_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/leader_012_africa_okp_okapi_court_processed.png` | `gfx/leaders/012_africa/leader_012_africa_okp_okapi_court.dds` | source `1081x1455`; final `156x210` | Institutional nonhuman court-herald portrait with courier satchel and restrained seal/court styling. |
| `OKP` | flag family | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/OKP_flag_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/OKP_flag_processed.png` | `gfx/flags/OKP.tga`; `gfx/flags/medium/OKP.tga`; `gfx/flags/small/OKP.tga` | source `1577x997`; finals `82x52`, `41x26`, `10x7` | Stripe band and seal remain recognizable at small size. The fine inner okapi-line detail compresses on `10x7`. |
| `TRM` | leader portrait | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/leader_012_africa_trm_termite_citadel_engineers_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/leader_012_africa_trm_termite_citadel_engineers_processed.png` | `gfx/leaders/012_africa/leader_012_africa_trm_termite_citadel_engineers.dds` | source `1081x1455`; final `156x210` | Institutional nonhuman engineer portrait with surveying tools and termite-citadel backdrop. |
| `TRM` | flag family | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/TRM_flag_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/TRM_flag_processed.png` | `gfx/flags/TRM.tga`; `gfx/flags/medium/TRM.tga`; `gfx/flags/small/TRM.tga` | source `1575x999`; finals `82x52`, `41x26`, `10x7` | Mound silhouette and survey-ring motif stay readable across all sizes. |
| `HGD` | leader portrait | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/leader_012_africa_hgd_honeyguide_commons_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/leader_012_africa_hgd_honeyguide_commons_processed.png` | `gfx/leaders/012_africa/leader_012_africa_hgd_honeyguide_commons.dds` | source `1083x1452`; final `156x210` | Institutional nonhuman courier-envoy portrait with honeycomb route markers. |
| `HGD` | flag family | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/HGD_flag_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/HGD_flag_processed.png` | `gfx/flags/HGD.tga`; `gfx/flags/medium/HGD.tga`; `gfx/flags/small/HGD.tga` | source `1574x999`; finals `82x52`, `41x26`, `10x7` | Bird and honeycomb route mark remain clear at normal/medium size. Honeycomb cells blur together somewhat at `10x7`. |
| `GHC` | leader portrait | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/leader_012_africa_ghc_great_herds_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/leader_012_africa_ghc_great_herds_processed.png` | `gfx/leaders/012_africa/leader_012_africa_ghc_great_herds.dds` | source `1080x1456`; final `156x210` | Institutional nonhuman Great Herds portrait with migration medallions and corridor markers. |
| `GHC` | flag family | `$imagegen` | `docs/assets/012_africa/bestiary_actor_assets/source_png/GHC_flag_source.png` | `docs/assets/012_africa/bestiary_actor_assets/processed_png/GHC_flag_processed.png` | `gfx/flags/GHC.tga`; `gfx/flags/medium/GHC.tga`; `gfx/flags/small/GHC.tga` | source `1573x1000`; finals `82x52`, `41x26`, `10x7` | Track-band composition stays legible. The tiny hoof-track border marks become mostly texture at `10x7`. |

## Review aids

- `docs/assets/012_africa/bestiary_actor_assets/contact_sheets/012_africa_bestiary_portraits_sheet.png`
- `docs/assets/012_africa/bestiary_actor_assets/contact_sheets/012_africa_bestiary_flags_sheet.png`

## Parent handoff notes

- The requested final portrait DDS filenames were used exactly.
- No sprite ids were provided for these portraits, so no `.gfx` proposal is included in this pass.
- All five portraits should be treated as institutional/nonhuman leaders rather than personal human officeholders.
