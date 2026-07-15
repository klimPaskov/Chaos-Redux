# Event 006 character portrait regeneration manifest

## Scope and source mode

- Source mode: 18 independent official ImageGen calls using the canonical
  vanilla leader or commander PNGs in
  `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/`
  as style-only references.
- Identity mode: every depicted person in this package is fictional and was
  designed for the exact Event 006 regional office or named commander token.
- Historical exceptions: the existing Rupprecht of Bavaria and Josef Friedrich
  Matthes portraits are user-approved real-person assets and are not generated,
  processed, or overwritten by this package.
- Final leader and commander size: `156x210` legacy uncompressed BGRA DDS.
- Final commander thumbnail size: `50x67` legacy uncompressed BGRA DDS derived
  from the approved full commander portrait; there is no fabricated small
  source portrait.

## Asset inventory

| Runtime stem | Subject | Full portrait | Commander thumbnail | Runtime state |
| --- | --- | --- | --- | --- |
| `portrait_ACX_cornish_port_and_mines_committee` | fictional Cornish committee chair | replaced | — | readiness-pool asset; not currently sprite-registered |
| `portrait_ACX_cornish_coastal_commander` | Thomas Trevorrow | replaced | replaced | readiness-pool asset; not currently sprite-registered |
| `portrait_AEX_flemish_civil_industrial_board` | fictional Flemish board chair | replaced | — | vanilla-overlay readiness-pool asset; not currently sprite-registered |
| `portrait_AEX_flemish_industrial_security_commander` | Hendrik Vermeulen | replaced | replaced | vanilla-overlay readiness-pool asset; not currently sprite-registered |
| `portrait_AFX_walloon_provisional_assembly` | fictional Walloon assembly chair | replaced | — | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_AFX_walloon_reserve_commander` | Marcel Delcourt | replaced | replaced | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_AGX_friesland_coastal_council` | fictional Frisian council magistrate | replaced | — | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_AGX_friesland_coastal_commander` | Sjoerd Hoekstra | replaced | replaced | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_AJX_saar_municipal_neutral_commission` | fictional Saar commission chair | replaced | — | readiness-pool asset; not currently sprite-registered |
| `portrait_AJX_saar_industrial_security_commissioner` | Karl Becker | replaced | replaced | readiness-pool asset; not currently sprite-registered |
| `portrait_RHI_independence_wave_provisional_directorate` | fictional Rhenish director | replaced | — | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_RHI_independence_wave_river_commandant` | fictional Rhenish commandant | replaced | replaced | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_BAY_independence_wave_state_council` | fictional Bavarian councillor | replaced | — | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_BAY_independence_wave_mountain_commandant` | fictional Bavarian commandant | replaced | replaced | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_SCO_independence_wave_civic_convention` | fictional Scottish convenor | replaced | — | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_SCO_independence_wave_territorial_commandant` | fictional Scottish commandant | replaced | replaced | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_WLS_independence_wave_national_council` | fictional Welsh council secretary | replaced | — | wired through `interface/006_independence_wave_region_01_portraits.gfx` |
| `portrait_WLS_independence_wave_mountain_commandant` | fictional Welsh commandant | replaced | replaced | wired through `interface/006_independence_wave_region_01_portraits.gfx` |

The approved historical files remain outside this generated inventory:

- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`

Their accepted SHA-256 values are embedded as a write guard in
`build_portrait_package.py` and are also included in
`portrait_package_hashes.sha256`.

## Production and review artifacts

- ImageGen masters: `source_png/`
- deterministic `156x210` candidates: `processed_png/`
- deterministic `50x67` commander derivatives: `processed_small_png/`
- actual runtime DDS decodes: `dds_decoded_png/` and
  `dds_decoded_small_png/`
- vanilla comparison sheets: `review_sheets/`
- processing metadata: `metadata/`
- generation directions: `prompts.md`
- visual acceptance record: `visual_review.md`
- reproducible builder and guard: `build_portrait_package.py`
- exact file hashes: `portrait_package_hashes.sha256`

The builder invokes `.tools/process_hoi4_portrait.py` for the restrained HOI4
finish and `.tools/convert_to_dds.py` for runtime export. It decodes every
installed DDS and requires exact processed-PNG pixel equality before success.

## Wiring boundary

Existing sprite names and texture paths were retained, so the six currently
playable package pairs did not need `.gfx` or character-script renaming. The
ACX, AEX, and AJX pairs remain art-ready pool entries only; this manifest does
not claim that their country packages or overlays are ready to release.
