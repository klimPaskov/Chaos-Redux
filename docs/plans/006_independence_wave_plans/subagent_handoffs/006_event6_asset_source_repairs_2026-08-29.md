# Event 006 non-portrait asset source repair and scope quarantine handoff

Date: 2026-08-29.

Scope: ASSET-004 news-image grayscale repair, active Event 006 asset-package receiver reconciliation, and evidence-only disposition of the AEX/NWE alias, BWX, and chunk-3 flag surfaces.

This handoff does not touch portraits, gameplay, decisions, localisation, spreadsheets, super-event audio, or any .gfx file.

## ASSET-004 repair

| Field | Evidence |
| --- | --- |
| Asset and runtime basename | ASSET-004, news_event_006_asset_004_league_congress, sprite GFX_news_event_006_asset_004_league_congress |
| Source PNG | docs/assets/006_independence_wave/source_png/event_pictures/news_event_006_asset_004_league_congress_source.png |
| Source SHA-256 | 7f11bae7083ba0044ace8ac3de8214c2cdc031f63313f68a380fe44e37364781 |
| Source provenance | Generated fictional/alternate-history documentary scene from docs/assets/006_independence_wave/prompts/generated_event_scenes.md, ASSET-004 prompt. |
| Source licence record | No third-party source pixels are used; the package does not record a separate provider licence or generation date, so those fields remain not separately recorded rather than assumed. |
| Era fit | Prompted as a 1930s press photograph with period civic chamber, clothing, microphones, and ballot cards; no real person, real flag, readable text, or modern equipment is intended. |
| Existing derived input | docs/assets/006_independence_wave/notes/asset_004_grayscale_repair/asset_004_processed_before_grayscale_repair.png |
| Existing derived SHA-256 | 981f45f949887f14b6ebf6bc319f36e8c9596a41a72e677e652f7756ac36fb03 |
| Repaired processed PNG | docs/assets/006_independence_wave/processed_png/event_pictures/news_event_006_asset_004_league_congress.png |
| Repaired processed SHA-256 | c1bbca9b8083731faafaab384e341be27b8fb990a035405ff443ddd4d56b7e9c7 |
| Final DDS | gfx/event_pictures/006_independence_wave/news_event_006_asset_004_league_congress.dds |
| Final DDS SHA-256 | 4ad0366dc87d54599d77aa2735cc832adca657dd212c3585b7948a91d5e57cef |
| DDS-decoded review PNG | docs/assets/006_independence_wave/dds_decoded_png/event_pictures/news_event_006_asset_004_league_congress.png |
| DDS-decoded SHA-256 | c1bbca9b8083731faafaab384e341be27b8fb990a035405ff443ddd4d56b7e9c7 |
| Review contact sheet | docs/assets/006_independence_wave/notes/asset_004_grayscale_repair/asset_004_grayscale_repair_contact_sheet.png |
| Contact-sheet SHA-256 | f42bb6f44bf56305039db62deb7c54b5055ca4b097b2010204aad556d9957196 |
| Runtime receiver | interface/006_independence_wave_small_assets.gfx, already registered for chaosx.nr6.35. |
| Status | Complete for the requested mechanical grayscale repair. |

The source PNG and its source hash are unchanged.

The existing 397x153 derived PNG was converted to RGBA luminosity grayscale with Pillow while preserving the crop, contrast, period press grain, and opaque alpha, then written back to the same processed path.

The repaired processed PNG has zero pixels with unequal RGB channels, and its decoded DDS review copy is pixel-identical to it.

The final DDS was regenerated with the repository converter .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py using the input processed PNG, output runtime basename, and explicit 397x153 dimensions.

The DDS is 397x153, one-level, legacy uncompressed 32-bit BGRA with a 128-byte header and a 243092-byte total length.

## Receiver reconciliation

The active Event 006 package manifests and handoffs now identify interface/006_independence_wave_small_assets.gfx as the current receiver for the consolidated sprite sets.

The old interface/006_independence_wave_event_pictures.gfx, interface/006_independence_wave_mediterranean_assets.gfx, and interface/006_independence_wave_form05.gfx paths do not exist as runtime files.

The following active package records resolve to the small-assets registry: generated_event_scenes_manifest.md, generated_event_scenes_gfx_handoff.md, the FORM-03 report-scene submanifest, its metadata and runtime handoff, the Mediterranean manifest and handoff, the FORM-05 manifest, and the IW-043/IW-058 JSON manifest and handoff.

References to the former files that remain in dated build or checksum records are historical provenance markers, not current receiver claims.

No .gfx file was edited in this tranche.

## AEX and NWE alias quarantine

AEX is owned by the separate Event 005 Basmachi Confederation surface through common/country_tags/chaosx_countries.txt, not by Event 006 NWE.

The NWE source and processed trees remain AEX-free, while the global runtime roots currently contain fifteen existing AEX TGAs: the unsuffixed file and four ideology aliases at each normal, medium, and small level.

The retained AEX base hashes are gfx/flags/AEX.tga 49d1205a64d792e2ea7bdd04049da5c89e88bf024f1418f7b50da27508fa4f5e, gfx/flags/medium/AEX.tga ac656b8f8f86eeed03c7acdc545980da31ddc63b87e131de3ba725e129d699b8, and gfx/flags/small/AEX.tga 32059e03d495b36142c3cd2a67a1ce366e31cc947c5607d5620fc9f35d270a01.

Those AEX files are retained unchanged as cross-event assets and are not standalone Event 006 NWE outputs.

The global runtime roots also contain forty-eight byte-identical suffix aliases for ACX, AFX, AGX, and AJX, comprising _democratic, _communism, _fascism, and _neutrality at all three ladder sizes.

The NWE aliases are quarantined as cross-event compatibility evidence only, are not counted as package-owned generated outputs, and receive no new route meaning.

No AEX or NWE alias file was deleted, renamed, or promoted.

## BWX and chunk-3 rights quarantine

BWX remains blocked for a historically sourced neutral 1936 flag.

Its existing source master, processed ladder, and runtime normal/medium/small TGAs remain intact as evidence-only assets because the current package records no provider date or licence and no primary or official source attests a neutral Erzya-Moksha federal flag in 1936.

The 1934 Mordovian ASSR flag is retained as a dated Soviet historical reference only and is not treated as the BWX neutral identity source.

The chunk-3 ladders for GMX, GZX, HAX, HDX, HEX, IBX, GIX, GRX, HFX, HGX, HKX, HPX, HSX, and HUX remain needs_user_review and evidence-only.

Their source masters and exact ladders exist, but alternate-history symbol ownership, community or institutional review, and a defensible 1936 flag-rights record remain unresolved.

GTX, GYX, and HCX retain their existing handed_off status.

No BWX or chunk-3 asset was deleted, replaced, relabelled, or promoted, and no generic or fallback flag was introduced.

## Files changed or produced

- gfx/event_pictures/006_independence_wave/news_event_006_asset_004_league_congress.dds was regenerated.
- docs/assets/006_independence_wave/processed_png/event_pictures/news_event_006_asset_004_league_congress.png was repaired in place as an ignored package artifact.
- docs/assets/006_independence_wave/dds_decoded_png/event_pictures/news_event_006_asset_004_league_congress.png was refreshed as the DDS review copy.
- docs/assets/006_independence_wave/notes/asset_004_grayscale_repair/asset_004_processed_before_grayscale_repair.png preserves the pre-repair derived input.
- docs/assets/006_independence_wave/notes/asset_004_grayscale_repair/asset_004_grayscale_repair_contact_sheet.png provides pre-repair, repaired, and DDS-round-trip comparison evidence.
- docs/assets/006_independence_wave/generated_event_scenes_manifest.md records the repaired hashes and strict grayscale validation.
- docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md records the Event 005 AEX boundary and NWE alias quarantine.
- docs/assets/006_independence_wave/006_nwe_historical_flag_comparison.md clarifies package-local AEX absence versus retained Event 005 runtime files.
- docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md marks BWX as source/rights/era blocked.
- docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk3/manifest.md records the fourteen needs-user-review chunk-3 ladders.
- docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_asset_source_repairs_2026-08-29.md is this source and scope handoff.

The package documentation under docs/assets/ is ignored by the repository-wide .gitignore; the runtime DDS and this handoff are the tracked commit surfaces for this tranche.

## Validation and boundaries

The repaired image was visually reviewed in the comparison contact sheet.

The processed and decoded images reopen at 397x153 and have opaque alpha.

The processed and decoded images have identical SHA-256 values and zero unequal RGB triplets.

The runtime DDS header has the expected legacy BGRA masks, dimensions, pitch, texture caps, and exact byte length.

No portrait, gameplay, decision, localisation, spreadsheet, super-event audio, or .gfx file was touched.

No fallback asset or unapproved sourced or generated replacement was used.
