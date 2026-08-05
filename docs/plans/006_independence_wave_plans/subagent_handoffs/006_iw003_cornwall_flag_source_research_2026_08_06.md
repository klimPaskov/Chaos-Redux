# IW-003 / ACX Cornwall flag source and design handoff

Research date: 2026-08-06. Scope: sourced regional symbol research for the accepted IW-003 Cornwall package, tag `ACX`, compact anchor state `123`, registry row `RG-123`, and source packet `REG-EUR-NW`.

## Verdict

**READY for a period civic-motif baseline; HOLD for any claim that this is a proven sovereign Cornish state flag in 1936, and HOLD for package admission.** The St Piran's Cross design is defensible as a flat reconstruction of a nineteenth-century/traditional Cornish community flag. The evidence does not establish a pre-1838 or sovereign-state flag, so runtime prose and asset manifests must call it a `generated_period_civic_baseline` or `historical_motif_reconstruction`, never an authenticated 1936 national flag or an ancient flag.

The existing ACX normal, medium, and small triplets are already flag-art complete and match this bounded design decision. This handoff makes no runtime-art or gameplay change and does not reopen the separate ACX map/state-ownership admission blocker documented in `006_iw003_acx_admission_audit_current_2026_08_03.md`.

## Historical evidence and rights boundary

| Source | Evidence used | Rights and allowed use |
|---|---|---|
| [Davies Gilbert, *The parochial history of Cornwall* (1838), Internet Archive item](https://archive.org/details/parochialhistory03gilb) and [printed page 332](https://archive.org/details/parochialhistory03gilb/page/332/mode/2up) | The 1838 printed source contains the first known written attestation identified in the specialist literature: “A white cross on a black ground was formerly the banner of St. Perran, and the standard of Cornwall.” It associates the black and white with tin ore and metal, but does not prove earlier surviving use. | The 1838 publication is public domain by age. Internet Archive scan terms are not stated in the item metadata, so use the citation and short factual quotation only; do not redistribute the scan pages as an asset. |
| [Flag Institute UK Flag Registry: Cornwall](https://www.flaginstitute.org/wp/flags/cornwall-flag/) | Official registry metadata identifies the design as St Piran's Cross, a plain white cross on a black field; `Flag Type: County Flag`, `Flag Date: C19th`, `Flag Designer: Traditional`, `Adoption Route: Traditional`, UK Design Code `UNKG7400`, aspect ratio `3:5`, and black/white colours. Its note describes a Cornish community flag and the tin-mining symbolism. The page's structured publication date is 2012-11-10 and its last modification is 2023-10-25. | The page is an authoritative history/proportion reference, but it gives no explicit redistribution licence for the official PNG. The official preview (`UNKG7400.png`, 1030x620 RGBA) was inspected only; do not copy or ship it. |
| [Phil Rendle, “Cornwall – The Mysteries of St Piran”, Flag Institute proceedings PDF](https://www.flaginstitute.org/pdfs/Phil%20Rendle.pdf) | Specialist research confirms the first known reference is Davies Gilbert's 1835/1838 material and warns that medieval-origin stories and claims of continuous pre-1838 use are uncertain or misattributed. This is the reason the design is accepted only as a period civic motif, not as a verified ancient or sovereign flag. | The PDF's copyright/redistribution terms are not explicit. Cite the research and its uncertainty warning; do not extract or redistribute PDF artwork. |
| [Wikimedia Commons: `File:Flag of Cornwall.svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Cornwall.svg) | Current vector geometry is 500x300 (5:3), a plain black field with one centered upright white cross. Commons credits Jon Harald Søby and marks the vector public domain. This is a modern rights-cleared geometry reference that mirrors the attested motif, not a 1936 artifact. | Public-domain dedication permits the flat geometry to be retained and reconstructed. Do not use its current upload/revision date as historical evidence or backdate the vector itself. |

## Design and reconstruction handoff

The allowed design is one centered upright white cross on an otherwise solid black field, with no text, seal, crown, pole, fabric folds, perspective, shadow, or additional charge. The retained source SVG is 500x300 and uses a 60-pixel cross stroke; the retained 1920x1152 raster is a 5:3 grayscale flat master with pure black `#000000` and pure white `#FFFFFF`. In that raster the vertical arm occupies x=845–1074 and the horizontal arm occupies y=461–690, which is a geometric proportion check rather than a claim about a historical surviving flag.

The final HOI4 ladder follows the repository contract: normal 82x52, medium 41x26, and small 10x7. The installed TGA files are uncompressed 32-bit BGRA with bottom-left origin. Keep the unsuffixed ACX family only; there are no ideology or cosmetic variants. The canonical presentation references are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/arm.png`, `medium/arm.png`, and `small/arm.png`; they are layout references, not source history.

## Existing source, processed, and runtime files

These files already exist in the asset package and were not changed for this research handoff.

| Role | Path | Dimensions/mode | SHA-256 |
|---|---|---|---|
| Rights-cleared vector source retained by the package | `docs/assets/006_independence_wave/source_svg/country_symbols/acx_st_pirans_cross_source.svg` | 500x300 SVG | `3d257c4f792664b3215e7e46c8ac625cb9949dd53e932cfea0f2517f1d036a3c` |
| Flat source raster | `docs/assets/006_independence_wave/source_png/country_symbols/acx_st_pirans_cross_source.png` | 1920x1152, grayscale `L` | `72c2db524f5b7c30e1aa71e0b034bd28c29c1d52469c9404ebbbe97636a7bf7d` |
| Retained raw ImageGen inspection output | `docs/assets/006_independence_wave/source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_raw.png` | 1536x1024 RGB | `2b1564faad74671bf717756fdb923ff60cf84d30ecdeaad71beefaab2816c94c` |
| Flat ImageGen master | `docs/assets/006_independence_wave/source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_flat_master.png` | 1536x1024 RGBA | `c4b5b11e8d77c5595d21ac0db8e75a3111530ee5e9a36b8c8205126e4d0c1008` |
| Processed normal preview | `docs/assets/006_independence_wave/processed_png/generated_nwe/flags/normal/ACX.png` | 82x52 | `726e91c832ce4644a20bc3a7b36c701f38b6372f13ee89e3c63691702ca44d65` |
| Processed medium preview | `docs/assets/006_independence_wave/processed_png/generated_nwe/flags/medium/ACX.png` | 41x26 | `4a7119cb141557b9df1ba83452befaf6b7744652d576c94ff48ba3bf342b44f1` |
| Processed small preview | `docs/assets/006_independence_wave/processed_png/generated_nwe/flags/small/ACX.png` | 10x7 | `dcb5a8f6de252a857950db90ecc9d2559813020df3a804c69346e0d2ba5bb524` |
| Runtime normal flag | `gfx/flags/ACX.tga` | 82x52, 32-bit BGRA | `e44993e121278c5d5dd72d51cd78d47c66f34f256e12e3c80e4fc11af70cfaad` |
| Runtime medium flag | `gfx/flags/medium/ACX.tga` | 41x26, 32-bit BGRA | `38aa26dad200038e0bb3db84d651227312ea9941e31505f49541cb100b2fe1fb` |
| Runtime small flag | `gfx/flags/small/ACX.tga` | 10x7, 32-bit BGRA | `c47d991628fe98cc8b7c6c669521530319cc4b8f35b06c5aff23a93dd0bfa718` |

The existing package manifests remain the operational asset records: `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md`, `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md`, and `docs/assets/006_independence_wave/006_nwe_historical_flag_comparison.md`. They correctly identify ACX as St Piran's Cross and separately record that the flag is not evidence of a sovereign 1936 Cornish state.

## Admission boundary and remaining uncertainty

- The source decision is ready only for the civic-motif interpretation accepted by `006_package_research_resolution.csv`; it does not authorize a historical-state claim.
- No defensible primary evidence was found for a sovereign Cornish flag in 1936, for continuous medieval use, or for an official pre-1838 national adoption. Those claims must remain absent from localisation, event prose, and manifests.
- The modern Commons vector is public-domain geometry, not a period artifact. The historical date/function come from the 1838 print and Flag Institute's C19th/traditional registry classification.
- Flag-art completion does not clear ACX admission. Keep the current package-level HOLD for exact Cornwall geography/state ownership, dormant country shell, and any remaining country-package gates.

No gameplay, GFX, localisation, country, portrait, advisor-icon, or other runtime files were edited. No new binary asset was generated, staged, or committed by this handoff.
