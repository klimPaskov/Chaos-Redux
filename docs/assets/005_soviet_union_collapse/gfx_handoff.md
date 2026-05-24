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

HOI4 country flags are final TGA gameplay assets, not `.gfx` sprites. The 2026-05-23 generated ideology pass created missing variants for the ancient-restoration tags:

- `gfx/flags/{KZR,SOG,KHW,ALN}_{communism,democratic,fascism,neutrality}.tga`
- `gfx/flags/medium/{KZR,SOG,KHW,ALN}_{communism,democratic,fascism,neutrality}.tga`
- `gfx/flags/small/{KZR,SOG,KHW,ALN}_{communism,democratic,fascism,neutrality}.tga`

That pass is superseded for `KZR`, `SOG`, `KHW`, and `ALN` by the 2026-05-24 historical-restoration correction:

- Source PNGs: `docs/assets/005_soviet_union_collapse/source_png/historical_flags/<TAG>[_<ideology>]_source.png`
- Processed previews: `docs/assets/005_soviet_union_collapse/processed_png/historical_flags/<TAG>[_<ideology>]_<normal|medium|small>.png`
- Contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/event005_historical_restoration_flags.png`

Use notes:

- The ancient/restoration states do not have reliably attested medieval state flags suitable for direct reproduction, so the current assets use historically grounded motifs and textile/banner language rather than invented route marks.
- `OGB` uses the previously preferred repository flag set restored from the earlier asset state; the correction records PNG previews for it but does not replace the gameplay TGAs with a new design.
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

## Historical restoration flag pass

Completed on 2026-05-24 for custom historical-restoration tags `KZR`, `SOG`, `KHW`, `ALN`, and `OGB`.

Scope: replace generated/simple historical-restoration flag artwork with historically grounded symbols and region-appropriate palettes. These are custom Chaos Redux countries, not vanilla-supported tags, so they keep country-tag flag files. Because no reliable direct medieval flag originals are available for these restored polities, the source art uses historical motifs rather than claiming direct reproduction.

Final outputs exist for base, `communism`, `democratic`, `fascism`, and `neutrality` in all three HOI4 flag sizes:

- normal: `gfx/flags/<TAG>[_<ideology>].tga`
- medium: `gfx/flags/medium/<TAG>[_<ideology>].tga`
- small: `gfx/flags/small/<TAG>[_<ideology>].tga`

Source and preview paths:

- source PNG: `docs/assets/005_soviet_union_collapse/source_png/historical_flags/<TAG>_<variant>_source.png`
- processed preview PNG: `docs/assets/005_soviet_union_collapse/processed_png/historical_flags/<TAG>_<variant>_<normal|medium|small>.png`
- contact sheet: `docs/assets/005_soviet_union_collapse/contact_sheets/event005_historical_restoration_flags.png`

## Existing-tag route flag rule

The generated ordinary/internal republic flag package has been removed. Vanilla-supported tags `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN` must use their existing game flags by default.

Existing-country flag changes are allowed only as explicit route changes, usually through focus or event effects that apply a cosmetic tag. The current implemented example is Ukraine's Black Banner route:

- cosmetic tag: `UKR_BLACK_BANNER`
- focus effect: `ukr_soviet_collapse_black_banner_compact` applies `set_cosmetic_tag = UKR_BLACK_BANNER`
- final normal TGA: `gfx/flags/UKR_BLACK_BANNER.tga`
- final medium TGA: `gfx/flags/medium/UKR_BLACK_BANNER.tga`
- final small TGA: `gfx/flags/small/UKR_BLACK_BANNER.tga`
- ideology variants: base, `communism`, `democratic`, `fascism`, and `neutrality`

Do not add default `gfx/flags/<existing_TAG>*.tga` overrides for these tags unless the design explicitly moves that country to a new cosmetic tag and wires the route effect.

## Validation Notes

- Leader portrait replacements were converted to 156x210 DDS using `.tools/convert_to_dds.py`.
- Direct SHA-256 comparison against vanilla leader DDS files found no vanilla hash match for `KZR`, `SOG`, `OGB`, `KHW`, or `ALN` after replacement.
- The 2026-05-24 follow-up reused unused generated Event 005 council portrait DDS files as active council portraits for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`; all five are 156x210 and have distinct SHA-256 hashes.
- Normal, medium, and small TGA files exist for all 16 new ideology flag variants. The parent validation pass re-exported them to vanilla-compatible 32-bit RGBA TGA dimensions: normal `82x52`, medium `41x26`, and small `10x7`.
- No mod-side default flag overrides remain for the 23 vanilla-supported ordinary/internal tags listed above; direct path audit finds only the explicit `UKR_BLACK_BANNER` cosmetic files among those tag prefixes.
- All checked Event 005 flag TGA files use normal `82x52`, medium `41x26`, and small `10x7` dimensions and bottom-left TGA origin. The orientation pass found zero top-origin TGA descriptors after correction.
- Continuation audit validation confirms `32/32` custom leader/council DDS portraits present at `156x210`, with zero vanilla leader hash matches and zero duplicate leader portrait hashes inside the Event 005 custom leader set.

## Parent Wiring Still Required

- No country flag `.gfx` wiring is required; HOI4 resolves the TGA filenames directly from country tags and ideology suffixes.
- The current OGB portrait sprite is `GFX_portrait_OGB_volga_restoration_council`, using `gfx/leaders/005_soviet_collapse/OGB_leader.dds`.
- Vanilla-supported release council portrait sprites for `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` are wired in `interface/005_soviet_collapse_custom_icons.gfx` and created by `soviet_collapse_apply_event_created_republic_council_leader`.
- If any older audit or completion report still says the custom ideology flags are identical to base flags, or says `KZR`, `SOG`, `OGB`, `KHW`, or `ALN` use vanilla-hash portraits, update that report to this handoff state.
