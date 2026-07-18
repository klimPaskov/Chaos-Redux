# IW-043 / IW-058 visual GFX handoff

Parent-owned `.gfx` files were not edited. Use the following stable runtime paths and identifiers.

## Portraits

Suggested registration file: `interface/006_independence_wave_iw043_iw058_portraits.gfx`.

```text
GFX_portrait_CHU_independence_wave_middle_volga_congress -> gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_middle_volga_congress.dds
GFX_portrait_CHU_independence_wave_federal_presidium -> gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds
GFX_portrait_CHU_independence_wave_bolgar_civic_presidium -> gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.dds
GFX_portrait_CHU_independence_wave_river_security_directorate -> gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds
GFX_portrait_ASY_independence_wave_provisional_national_council -> gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_provisional_national_council.dds
GFX_portrait_ASY_independence_wave_concordat_council -> gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds
GFX_portrait_ASY_independence_wave_civic_national_assembly -> gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_civic_national_assembly.dds
GFX_portrait_ASY_independence_wave_levies_guardianship -> gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.dds
```

All eight are large 156x210 collective leader portraits. They require institutional names, not personal random-name pools. No small, commander, or advisor sprite is supplied.

## Reports

Suggested registration file: `interface/006_independence_wave_event_pictures.gfx`.

```text
GFX_report_event_independence_wave_iw043 -> gfx/event_pictures/006_independence_wave/report_event_006_iw043_middle_volga_congress.dds
GFX_report_event_independence_wave_iw058 -> gfx/event_pictures/006_independence_wave/report_event_006_iw058_assyrian_national_council.dds
```

Both are 210x176 report cards with transparent corners. They are not news or super-event images.

## Flags

Flags are engine-convention TGAs and do not need custom `.gfx` sprites. Keep the exact cosmetic/formable filenames in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` as listed in [`manifest.md`](manifest.md). The ladder contact sheet and machine validation are in `contacts/flags/`.

## Provenance and review

Prompts are retained in `prompts/portraits_prompts.md`, `prompts/flags_prompts.md`, and `prompts/reports_prompts.md`. Source/processed/runtime hashes and processor metadata are in `manifests/asset_manifest.json` and `manifests/hashes.sha256`. The source-research caveats are preserved from `docs/assets/006_independence_wave/iw043_iw058_source_research_2026_07_18/`. Protected BAY/RHI hashes were rechecked after conversion.
