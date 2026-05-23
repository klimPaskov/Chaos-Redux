# Event 005 Soviet Collapse Generated Portrait and Flag Handoff

Bounded pass completed on 2026-05-23. Scope was limited to generated fictional/council portrait replacements and fictional ideology flag variants. No gameplay, `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files were edited.

## Portrait DDS replacements

These paths keep the existing wired DDS filenames, so parent wiring should not need texture path changes unless the parent wants to rename sprites.

| Asset | Final DDS | Proposed sprite name | Suggested `.gfx` file | Use notes |
| --- | --- | --- | --- | --- |
| Khazar Toll Khaganate council | `gfx/leaders/005_soviet_collapse/KZR_leader.dds` | `GFX_portrait_KZR_itil_toll_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Replaces vanilla-hash portrait with generated fictional council portrait. |
| Sogdian City League council | `gfx/leaders/005_soviet_collapse/SOG_leader.dds` | `GFX_portrait_SOG_city_registers_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Replaces vanilla-hash portrait with generated fictional council portrait. |
| Old Great Bulgaria council | `gfx/leaders/005_soviet_collapse/OGB_leader.dds` | `GFX_portrait_OGB_volga_restoration_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Replaces vanilla-hash portrait with generated fictional council portrait. |
| Khwarazmian Oasis Authority council | `gfx/leaders/005_soviet_collapse/KHW_leader.dds` | `GFX_portrait_KHW_oasis_register_authority` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Replaces vanilla-hash portrait with generated fictional council portrait. |
| Alan Pass Principality council | `gfx/leaders/005_soviet_collapse/ALN_leader.dds` | `GFX_portrait_ALN_alan_pass_council` | `interface/005_soviet_collapse_factory_ancient_icons.gfx` | Replaces vanilla-hash portrait with generated fictional council portrait. |

Source PNGs live under `docs/assets/005_soviet_union_collapse/source_png/generated_replacements/`.
Processed previews live under `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/`.
Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/event005_generated_replacement_leaders.png`.

## Flag variants

HOI4 country flags are final TGA gameplay assets, not `.gfx` sprites. This pass created missing fictional ideology variants for the ancient-restoration tags:

- `gfx/flags/{KZR,SOG,KHW,ALN}_{communism,democratic,fascism,neutrality}.tga`
- `gfx/flags/medium/{KZR,SOG,KHW,ALN}_{communism,democratic,fascism,neutrality}.tga`
- `gfx/flags/small/{KZR,SOG,KHW,ALN}_{communism,democratic,fascism,neutrality}.tga`

Processed previews live under `docs/assets/005_soviet_union_collapse/processed_png/generated_replacements/flags/`.
Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/event005_generated_ancient_ideology_flags.png`.

Use notes:

- The ideology variants are fictional generated-asset derivatives from existing generated Event 005 base flags.
- They are not historical flags and do not substitute for a sourced historical-symbol pass if one is later required.
- No `.gfx` edits are needed for country flags.

## Custom successor ideology flag package

Completed on 2026-05-23 during the continuation audit. Scope was limited to fictional/generated ideology flag variants for custom Event 005 successor tags whose existing ideology files were byte-identical to their base flags. No gameplay, `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files were edited.

Source mode: generated-asset derivative. The existing generated base flag TGAs were used as the source artwork, then each ideology route received a distinct fictional color treatment and simple invented route mark. These are alternate-history/generated flags, not historical flags or attested symbols.

Inspected reference folder: `.agents/skills/chaos-redux-event-assets/assets/flags`.

Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/event005_generated_custom_ideology_flags.png`.

Tags completed: `CFR`, `MFR`, `OGB`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, and `NLC`.

Variants completed for every listed tag: `communism`, `democratic`, `fascism`, and `neutrality`; each variant has normal `82x52`, medium `41x26`, and small `10x7` 32-bit TGA outputs.

Source and preview paths:

- source PNG: `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/<TAG>_<ideology>_source.png`
- processed preview PNG: `docs/assets/005_soviet_union_collapse/processed_png/generated_custom_ideology_flags/<TAG>_<ideology>_<normal|medium|small>.png`
- final normal TGA: `gfx/flags/<TAG>_<ideology>.tga`
- final medium TGA: `gfx/flags/medium/<TAG>_<ideology>.tga`
- final small TGA: `gfx/flags/small/<TAG>_<ideology>.tga`

Proposed sprite name and suggested `.gfx` file: not applicable for HOI4 country flags. No `.gfx` edits are needed for country flags.

## Ordinary/internal republic flag package

Completed on 2026-05-23. Scope was limited to fictional/generated base and ideology flags for ordinary/internal Event 005 Soviet-collapse successor tags. No gameplay, `.gfx`, localisation, GUI, event, focus, idea, decision, script, history, country, or spreadsheet files were edited.

Source mode: Codex built-in `$imagegen` generated a fictional 1930s alternate-history flag source sheet, then the sheet was cropped and processed into unique tag-level source PNGs, PNG previews, and final HOI4 TGA files. Generation is appropriate because these are fictional alternate-history successor-state flags.

Inspected reference folder: `.agents/skills/chaos-redux-event-assets/assets/flags`.

Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/event005_generated_ordinary_internal_flags.png`.

HOI4 country flags do not use sprite names or `.gfx` entries. Parent wiring only needs the country tags to resolve these filenames:

- normal: `gfx/flags/<TAG>[_<ideology>].tga`
- medium: `gfx/flags/medium/<TAG>[_<ideology>].tga`
- small: `gfx/flags/small/<TAG>[_<ideology>].tga`

Source and preview paths:

- source PNG: `docs/assets/005_soviet_union_collapse/source_png/generated_ordinary_flags/<TAG>[_<ideology>]_source.png`
- processed preview PNG: `docs/assets/005_soviet_union_collapse/processed_png/generated_ordinary_flags/<TAG>[_<ideology>]_<normal|medium|small>.png`

Tags completed: `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, `TAN`.

Variants completed for every tag: base, `communism`, `democratic`, `fascism`, and `neutrality`; each variant has normal `82x52`, medium `41x26`, and small `10x7` 32-bit RGBA / TrueColorAlpha TGA outputs. Proposed sprite name and suggested `.gfx` file: not applicable for HOI4 country flags. Blockers: none.

## Validation Notes

- Leader portrait replacements were converted to 156x210 DDS using `.tools/convert_to_dds.py`.
- Direct SHA-256 comparison against vanilla leader DDS files found no vanilla hash match for `KZR`, `SOG`, `OGB`, `KHW`, or `ALN` after replacement.
- Normal, medium, and small TGA files exist for all 16 new ideology flag variants. The parent validation pass re-exported them to vanilla-compatible 32-bit RGBA TGA dimensions: normal `82x52`, medium `41x26`, and small `10x7`.
- Normal, medium, and small TGA files exist for all 115 ordinary/internal republic flag outputs. Full ImageMagick validation confirms 8-bit RGBA / TrueColorAlpha dimensions: normal `82x52`, medium `41x26`, and small `10x7`.
- Continuation audit validation confirms `825/825` expected Event 005 scoped flag files present for 32 custom tags and 23 ordinary/internal tags, with correct normal/medium/small dimensions, 32-bit TGA output, zero vanilla flag hash matches, and zero duplicate base-vs-ideology variants per audited tag.
- Continuation audit validation confirms `32/32` custom leader/council DDS portraits present at `156x210`, with zero vanilla leader hash matches and zero duplicate leader portrait hashes inside the Event 005 custom leader set.

## Parent Wiring Still Required

- No country flag `.gfx` wiring is required; HOI4 resolves the TGA filenames directly from country tags and ideology suffixes.
- The current OGB portrait sprite is `GFX_portrait_OGB_volga_restoration_council`, using `gfx/leaders/005_soviet_collapse/OGB_leader.dds`.
- If any older audit or completion report still says the custom ideology flags are identical to base flags, or says `KZR`, `SOG`, `OGB`, `KHW`, or `ALN` use vanilla-hash portraits, update that report to this handoff state.
