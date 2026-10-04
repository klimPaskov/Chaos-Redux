# Event 021 Reused Event 006 Portrait Provenance Audit

Audit date: 2026-09-26. The requested handoff filename retains the supplied 2026-09-25 date.

## Result and scope

The current Event 021 adapter registry names 32 complete Event 006 package IDs, but selection and eligibility remain runtime-dynamic. This is the adapter’s current source registry, not a fixed gameplay roster or proof that every package is eligible in a particular save. I did not infer any fixed-tag fallback or claim coverage of all 193 Event 006 packages.

Those package/tag mappings are `iw_001/SCO`, `iw_002/WLS`, `iw_004/BRI`, `iw_006/AFX`, `iw_007/AGX`, `iw_008/RHI`, `iw_009/BAY`, `iw_010/AJX`, `iw_012/ICE`, `iw_014/CAT`, `iw_017/COR`, `iw_018/ARX`, `iw_019/ASX`, `iw_023/TRA`, `iw_024/AXX`, `iw_026/MAC`, `iw_027/BAX`, `iw_028/BBX`, `iw_029/BOS`, `iw_030/MNT`, `iw_031/KOS`, `iw_033/KAR`, `iw_038/RUT`, `iw_040/KUB`, `iw_041/CRI`, `iw_044/TAT`, `iw_045/BSK`, `iw_070/ARM`, `iw_071/GEO`, `iw_072/AZR`, `iw_173/HAW`, and `iw_184/HBX`.

The adapter’s package-ID registry is in `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt`; the state/control/population/infrastructure and dormant-country checks are in `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt`. Event 021 gates candidates through `event021_parent_event6_dormant_candidate` and package setup proof in `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`. These selectors make the admitted set context-dependent.

I traced the package portrait consumers through `common/characters/006_independence_wave_characters_registry.txt`, Event 006 scripted character preparation, the active mod `.gfx` registrations, and vanilla character/history/GFX registrations. The detailed consumer crosswalk, exact character tokens, sprite IDs, GFX source paths, runtime paths, provenance references, per-file dimensions, byte lengths, and SHA-256 values are in the existing read-only audit matrix: `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_event006_portrait_asset_audit_2026-09-25.json` (with its companion `event021_event006_portrait_asset_audit_2026-09-25.md`). I rechecked the current runtime hashes against that matrix; all extant files still match it.

## Coverage and image inspection

The crosswalk contains 65 portrait-consumer rows: 46 Event 006 mod portrait sprites and 19 vanilla portrait consumers. They resolve to 60 unique runtime path strings: 46 mod DDS files, 13 distinct existing vanilla DDS files, and one missing vanilla path. The 18 resolvable vanilla consumer rows share those 13 vanilla textures; the remaining row is the missing KUB leader texture.

All 59 extant unique runtime portrait files were visually re-opened at 156×210 and at nearest-neighbour enlargement for framing review. The visual pass is therefore complete for extant unique files; the absent KUB file cannot be visually reviewed. All 59 files have DDS headers. The 46 Event 006 files and eight named vanilla portraits are uncompressed 32-bit RGB/alpha DDS (`DDS ` header, 32-bit pixels); the five vanilla generic textures are 16-bit RGB DDS. Each present file’s exact relative path, dimensions, byte count, and SHA-256 are in the JSON crosswalk. No project PNG or DDS output was created, and no portrait was generated, processed, converted, or rewired in this audit.

The missing path is `dlc/dlc034_no_step_back/gfx/leaders/KUB/portrait_KUB_ivanis_vasily_nikolaevich.dds`, consumed as `GFX_portrait_KUB_ivanis_vasily_nikolaevich` for `KUB_ivanis_vasily_nikolaevich` in package `iw_040/KUB`. Its vanilla sprite declaration exists, but the large DDS is absent, so it has no dimensions, format, or file hash to report. No substitute was inspected or proposed.

The five installed generic textures are `gfx/leaders/Europe/Portrait_Europe_Generic_1.dds`, `gfx/leaders/Europe/Portrait_Europe_Generic_2.dds`, `gfx/leaders/Europe/Portrait_Europe_Generic_land_1.dds`, `gfx/leaders/Europe/Portrait_Europe_Generic_land_5.dds`, and `gfx/leaders/SOV/Portrait_Soviet_Generic_3.dds`. They are legible vanilla art, but not likenesses of the named consumers: respectively Pēteris Irklis, Ilyas Tarkhan, Aleksandr Alemasov, and Grigor Harutyunyan; Hovhannes Kajaznuni and Mammad Amin Rasulzade; Mir Jafar Baghirov; Iuliu Maniu and Drastamat Kanayan; and Gara Garabeyov. These 10 consumer rows need an owner decision on generic-art acceptability. The installed game files are proprietary Paradox assets; this audit does not assert mod redistribution clearance.

The eight vanilla named-portrait consumers resolve to subject-named ICE, CAT, GEO, and KAR textures. Their exact file paths and hashes are listed per consumer in the JSON crosswalk. Their installed-game provenance is clear, but that does not grant redistribution rights.

## Provenance findings

The current crosswalk classifies 15 Event 006 mod portraits as legacy generated, identity-unverified faces. Their ImageGen prompt/manifest records exist under `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/`; those records document generated assets, not attributed source portraits for a named real person. The current DDS files are not admitted as verified real-person portraits by this audit.

The crosswalk marks 25 mod portrait rows as awaiting a user-supplied HOI4-style final and records source/crop evidence for named people. This is a pending state, not approval or rights clearance. The cited `docs/assets` evidence paths exist, but a dossier’s presence does not prove that the current DDS is an unchanged source placeholder or that its license permits redistribution. The crosswalk’s exact per-row source/master, crop, processing, attribution, and rights-record paths should be followed for any later replacement review.

One material contradiction was found in the current crosswalk: `iw_002/WLS`, sprite `GFX_portrait_WLS_independence_wave_national_council`, character token `WLS_independence_wave_national_council`, runtime `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` (current SHA-256 `e11254da91774c9f0495c60943835a8ba26263934b8bc4e2d6e3016c01e4334d`) is labeled there as a J. H. Thomas source-placeholder identity, but its listed “source” paths point to unrelated RUT source-placeholder images. The live localization currently names this WLS token “J. H. Thomas” (`localisation/english/006_independence_wave_scotland_wales_l_english.yml`), while the live package effect dynamically creates that token and assigns the sprite (`common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt`). The WLS runtime is not an exact decoded-pixel match to an archived 156×210 source PNG in the crosswalk. The actual WLS runtime-art record at `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/institutional_metadata/WLS_independence_wave_national_council.json` calls the generated input fictional/role-only and points to ImageGen output, not J. H. Thomas source material. Other WLS source/repaint trials name Saunders Lewis or David Rhys Grenfell and are not approved runtime replacements. Therefore this row is not established as a sourced placeholder; identity/source mapping and replacement status must be reconciled before it can be counted among verified sourced placeholders.

Other source and rights caveats recorded in the existing dossiers include:

- `iw_045/BSK`, Yakov Bykin: the archived source record states CC BY-SA 4.0; attribution and share-alike obligations apply.
- `iw_173/HAW`, Samuel Wilder King: current runtime pixels match an archived ImageGen repaint, not the source crop. The Hawaiʻi State Archives dossier records a public-use caveat; no independent rights clearance is asserted.
- `iw_184/HBX`, William D. Stephens: current runtime pixels match an archived ImageGen repaint, not the source crop. The Library of Congress “no known restrictions on publication” note is not a license grant or public-domain determination.
- `iw_018/ARX`, Luigi Mella Sant’Elia: the selected image record is post-1936 and records CC BY-SA; the date/rights gate remains unresolved.
- `iw_018/ARX`, Vittorio Vernè: the source dossier names Vernè but the live portrait consumer token is `ARX_gavino_piras`; this is an explicit identity/consumer mismatch.

The other specifically flagged visual/provenance rows are `ASX_vincenzo_di_benedetto` (low-contrast grayscale), `KOS_independence_wave_shaban_polluzha` (very grainy/high-contrast source image), and the WLS/AFX/SCO generated faces noted in the crosswalk for tight profile framing. The two current ImageGen repaint rows (HAW and HBX) are not accepted user-supplied finals or source placeholders. Generic vanilla rows are subject-mismatched by definition. Other reviewed portraits were generally legible at native size; stylistic resemblance to the canonical vanilla leader family does not establish subject identity or rights.

## Exact remaining gaps and limits

1. Reconcile the WLS identity, source record, and current DDS before describing it as a source placeholder. The existing crosswalk’s RUT evidence links are unrelated to WLS, and its J. H. Thomas label conflicts with the role-only ImageGen provenance record.
2. The KUB large texture is missing. Its vanilla GFX reference cannot be visually validated against an installed portrait file.
3. The 15 legacy generated identity-unverified rows still lack verified subject/source provenance. Their current images remain wired, but no source attribution or license establishes a real depicted identity.
4. The 25-row pending-final count in the prior crosswalk is not a count of cleared or approved assets; the WLS contradiction means that count must not be reported as 25 verified sourced placeholders. The other dossiers also need per-identity final review and applicable rights/attribution review before any replacement is treated as cleared.
5. HAW and HBX have source dossiers but currently wired ImageGen repaints; source-rights notes are caveats, not grants. Mella’s rights/date gate, Vernè’s identity mismatch, Di Benedetto’s image quality, and Polluzha’s grain/contrast remain open.
6. Ten consumer rows use five proprietary vanilla generic portraits rather than subject-specific likenesses. An owner decision and any required asset-rights decision remain outstanding.
7. The current static adapter crosswalk covers the 32 listed package IDs only. Runtime state ownership/control, population, infrastructure, country existence, human-player, safety, and prepared-package checks remain dynamic and were not executed against a live save. This audit makes no claim of live eligibility or 193-package coverage.

## Handoff boundary

Only this handoff report was added. No portrait, PNG, DDS, country, character, GFX, or runtime wiring file was changed. No RunPod session was opened or operated; native ImageGen and DDS conversion were not used. Existing workspace edits were preserved. No in-game or save-level eligibility validation was performed.
