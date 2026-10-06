# `shared_chaosx_characters` portrait repair report

Date: 2026-10-06. The source-of-truth finding set is `shared_chaosx_characters` in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` and the matching entries in `gfx_issues.json`.

The group contained seven findings: zero severity 1, five severity 2, and two severity 3. Exactly four runtime DDS files changed in this group: three DHO advisor small portraits were corrected, and Chigi's incorrect painting reference was replaced with an authentic source placeholder. The current approved ZZZ and THR packages supersede the other two rows. The group is not fully closed because the 001 collective source placeholder and CRU source placeholder still await user-supplied painted finals.

## Findings, in severity order

| Severity | Sprite | Original finding | Disposition and evidence |
|---:|---|---|---|
| 2 | `GFX_portrait_communist_rebels` | Raw monochrome committee photograph was visible among painted portraits. | Left untouched per parent direction; accepted 1918 Moscow Soviet group source placeholder remains at runtime with HOI4-style final pending the user. Runtime SHA-256 is `059b20336d625906b5debf1545db445e7c361f90745c239b01d7ce704da9d021`. The package handoff confirms pending user art, while the canonical contract says `styled_final: not_requested` and `replacement_pending: false`; this documentation mismatch is reported without editing the 001-owned package. |
| 2 | `GFX_portrait_CRU_crusader` | Low-contrast museum photo of a 16th-century Knight of Malta painting did not identify the 1936 Grand Master or match the painted portrait family. | Replaced by an authentic, attributed photo of Ludovico Chigi, the actual Grand Master from 1931 to 1951. Parent approved identity, provenance, and framing on 2026-10-06; age/date fit is limited because the photo is from 1910–15. The installed art is an archival source placeholder and the user-supplied HOI4-style final remains pending, so the style part of the finding remains open. |
| 2 | `GFX_portrait_DHO_thessik_small` | 50×67 small portrait left a 15 px gap in the vanilla 65×67 advisor slot. | Fixed with parent-approved 65×67 dossier card derived from the unchanged 156×210 fictional master. Identity, framing, style, and transparency passed parent review. |
| 2 | `GFX_portrait_DHO_orrukesh_small` | Same 50×67 advisor-slot gap. | Fixed with parent-approved 65×67 dossier card derived from the unchanged 156×210 fictional master; identity, framing, style, and transparency passed parent review. |
| 2 | `GFX_portrait_DHO_khalvek_small` | Same 50×67 advisor-slot gap. | Fixed with parent-approved 65×67 dossier card derived from the unchanged 156×210 fictional master; identity, framing, style, and transparency passed parent review. |
| 3 | `GFX_portrait_ZZZ_weaponized_rabid` | Existing glossy, saturated portrait contrasted with the muted painted zombie set. | Superseded by the existing parent-approved fictional native ImageGen v2 source and installed runtime DDS; portrait and GFX bytes were left untouched in this tranche. Runtime SHA-256 is `8656707116a9bf12670a29dbe0f7a9c3667f045e2485337c413fb2480ae15b76`. |
| 3 | `GFX_portrait_THR_godly_figure` | Existing flat lavender thangka-style figure contrasted with the painted progression set. | Superseded by the existing fictional ImageGen package-level parent-approved runtime. Portrait and GFX bytes were left untouched. Runtime SHA-256 is `6c7adb3aa157ccc3cbefca6ea66c1bed7bfd954f4add4633137e8ff07e407be1`. The 003 release manifest still has per-row “awaiting review” claims that contradict package-level “approved and installed”; this conflict remains visible in `docs/assets/portraits/003_holy_realm/release_20261006/manifest.md`. |

## Changed runtime and evidence files

| Runtime path | Dimensions / bytes | SHA-256 | Output / review evidence |
|---|---:|---|---|
| `gfx/leaders/018_resources_found/portrait_DHO_thessik_small.dds` | 65×67 / 17,548 | `66e332dfb1c04af183fe964b95d985b0e64c0a55349c2593fe58da6935bed8db` | `docs/assets/portraits/018_resources_found/DHO_thessik_small/portrait_DHO_thessik_small_candidate_65x67.png`. |
| `gfx/leaders/018_resources_found/portrait_DHO_orrukesh_small.dds` | 65×67 / 17,548 | `318d473ebe1ae2dc1c79f99f2ddd5526be2f45f27ee7833b7903c834484b0156` | `docs/assets/portraits/018_resources_found/DHO_orrukesh_small/portrait_DHO_orrukesh_small_candidate_65x67.png`. |
| `gfx/leaders/018_resources_found/portrait_DHO_khalvek_small.dds` | 65×67 / 17,548 | `f850e72de6aed7561dee87cf9b12e907331b34ae543e24dfe570f9d1f26100c6` | `docs/assets/portraits/018_resources_found/DHO_khalvek_small/portrait_DHO_khalvek_small_candidate_65x67.png`. |
| `gfx/leaders/038_malta_crusaders/portrait_CRU_crusader.dds` | 156×210 / 131,168 | `878a3e6d9ad6e18b41c683277d863128b6d63eeba405a2e54714d379302b0edf` | `docs/assets/portraits/038_malta_crusaders/grand_master_ludovico_chigi/portrait_CRU_crusader_156x210.png`, SHA-256 `6d2ce3b730a3f8a94a0c04749561223052cdf50e4a9a81b729366ea5de126fb3`. |

The DHO native candidate sheet `docs/assets/portraits/018_resources_found/review/portrait_DHO_small_candidates_native.png` has SHA-256 `30fe00caccb94abc7b4500cb364d9c42507bafb161cb2cef9f2905217e0a6b6f`; the 4× checker sheet `portrait_DHO_small_candidates_4x_checker.png` has SHA-256 `71ef3697cbc65fab22da8b330da61c1e0cf9580c434e468311d33161e5c45673`. Parent independently passed identity, framing, style, and transparency on 2026-10-06.

The previous small DDS files are preserved under `docs/assets/portraits/018_resources_found/DHO_*_small/legacy_unverified_dds/`: Thessik SHA-256 `7755c4afb814501d4be9c4d5e0a8fa7b3412878c23a83e5f18402b3cb9262527`, Orrukesh `5e4cbd1f70607831ad92ae74dff3d7eca4606749cb7db8d1cf0ae79c6cc1a73e`, and Khalvek `6dc4861ab127bba3dcc303f3386b5956c06894f19a6dc3385201c1b90cb201fb`.

The Chigi source archive, contract, crop JSON, parent review sheet, and pre-fix DDS are in `docs/assets/portraits/038_malta_crusaders/grand_master_ludovico_chigi/`; the source-crop review sheet SHA-256 is `485cb8b408fdb6a023c91a540af1e8db8ce80a2637d8fdf2d0e32d744975e980`, and the previous runtime SHA-256 is `5536ea97df2271b7c9230c6fb6eec9686acc4c25f7995e6724ad74f2f5dd72cd`.

`docs/assets/portraits/shared_chaosx_characters/manifest.md`, `docs/assets/portraits/018_resources_found/manifest.md`, and `docs/assets/portraits/038_malta_crusaders/manifest.md` provide the exact owned runtime paths, source lineage, and replacement states.

## Source, generation, and portrait review

The Chigi image is Bain News Service's photo of Ludovico Chigi, archived by the Library of Congress under [LCCN 2014692087](https://www.loc.gov/pictures/item/2014692087/) and [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Prince_Chigi_LCCN2014692087.jpg), where the source is marked public domain.

Its 4135×5779 original JPEG is SHA-256 `1cacb2129bf2da39e25ed51d432a851a038561ea294f1a77714630064ab251a0`; the manual source crop `[600,600,2800,3562]` is 2200×2962 and SHA-256 `bef72c818e63a718db5d44a08f9fc0fc2189316f573313ce0f420640bd7cdcda`.

The prior painting's identity mismatch is corrected, but this 1910–15 image predates Chigi's 1931 Grand Master appointment and shows him younger than the 1936 campaign; parent accepted only a pending source placeholder.

The DHO small cards reuse unchanged fictional portrait masters whose ImageGen receipts were not recovered; their exact master source paths and hashes are in the shared character manifest, and the crop review does not claim to resolve that inherited provenance gap.

The rabid v2 source image is `docs/assets/portraits/002_zombie_outbreak/release_20261006/source_imagegen/portrait_ZZZ_weaponized_rabid_v2.png` (1082×1454, SHA-256 `618258e7481b32f2b8d4bae76275fc003534fbbc6e541659b3fd30469b3ca319`); its processed 156×210 PNG hash is `46fcdad1d4a48449a4f7fd1fe12c66a89e8a08128ed9fbc8b788b1d669a91928`. The current release manifest marks its fictional native ImageGen v2 as approved and installed.

The Godly Figure source is `docs/assets/portraits/003_holy_realm/release_20261006/source_png/static/portrait_THR_godly_figure_v1.png` (156×210, SHA-256 `6279944a7c21ec9b5c416ef2d1668a1089254ab25d1b82f6705e50d44e67a3bd`); processed PNG SHA-256 is `aebdf2f7d1003e16ba83656e966088de87dc331e812faee4473b46ecf6b2185c`.

## Processing, wiring, and validation limits

The native advisor reference `.agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/advisors/advisor_template.png` was inspected; the small slot is 65×67 and the measured dossier opening is centered at `(24.7615102792, 30.6451468824)`, sized `(30.4774060150, 45.0945083321)`, and tilted `-4.76°`.

All four changed DDS assets were produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; DHO DDS roundtrips match the 65×67 PNGs and Chigi matches its 156×210 processed PNG pixel-for-pixel. Runtime hashes, sizes, and unchanged sprite mappings were checked from the worktree.

`GFX_portrait_*` texture paths in `interface/chaosx_characters.gfx` and small-portrait references in `common/characters/018_resources_found_cave_characters.txt` were checked and left unchanged. The Chigi stable `GFX_portrait_CRU_crusader` mapping also remains unchanged.

No dedicated portrait inspection route was found. GUI/source inspection routes exist, but no successful engine-context portrait preview was obtained. No game or desktop window was opened.

The filtered current group sheets were generated with `python .tools/gfx/gfx.py sheet --groups _scientists_portraits shared_chaosx_characters --out docs/plans/gfx_fix_2026-10/portrait_group_sheets_20261006 --label after`. The before snapshot copied the current two portrait registry files and referenced textures into a temporary root, then replaced the six changed portrait textures with their exact preserved pre-fix DDS backups; the temporary root is recorded in the scientist report.

The shared-character group sheets are:

| Snapshot | File | SHA-256 |
|---|---|---|
| Before | `portrait_group_sheets_20261006/shared_chaosx_characters_before_snapshot_1.png` | `8a874db18d2980834fd18e63f07cd23c10f272dcf202f6d9a13dde8b21230740` |
| Before | `portrait_group_sheets_20261006/shared_chaosx_characters_before_snapshot_2.png` | `cf0810e33babfa3faa6bb830cebf13af569ad5b4dd8aae590e466767930b3722` |
| After | `portrait_group_sheets_20261006/shared_chaosx_characters_after_1.png` | `03bd83343eb90b7dd971dbc99f3209b96fcec12dcf00958cc43dc65aedcf983e` |
| After | `portrait_group_sheets_20261006/shared_chaosx_characters_after_2.png` | `9cb94e9d7043bbb87499381a77e6a3135737c7b08286a961b015898cc87f6877` |

Visual comparison confirms the three small DHO cards changed from 50×67 crops to 65×67 dossiers and the CRU slot changed from a 16th-century painting to the Chigi source placeholder; the 001, ZZZ, and THR portrait textures remained unchanged.

An earlier attempted command `python C:\Users\klimp\Videos\chaos_redux_trailer\tools\gfx_sheets.py --help` on 2026-10-06 at 10:12:47 Europe/Kyiv had no CLI parser and produced no captured output; its exact Python process (PID 12272) was stopped. At final audit the external shared-character sheet timestamp still read 08:55:03 local, before the runtime promotion tranche. Per parent direction, external originals are treated as unreliable and were neither restored nor used as the before baseline; the documented in-repository snapshot sheets are the comparison evidence.

## Replacement state, omissions, and blockers

The three DHO small-crop findings are fixed and their portrait-card replacements are parent-approved.

The CRU identity/source issue is corrected with an explicitly pending archival source placeholder; the user-styled final remains outstanding.

The 001 collective portrait remains an explicitly pending source placeholder awaiting user-painted art; its canonical contract's `replacement_pending:false` conflicts with its own `user_hoi4_style_final: pending user creation and supply` entry and the accepted 001 handoff, and it was not changed here.

The ZZZ rabid and THR Godly Figure findings are superseded by current approved portrait sources and were not reinstalled or edited by this task.

No historical likeness was invented, repainted, genericized, or replaced by an unrelated person. No agent operated RunPod.

No successful MCP GUI portrait preview or live-game check was obtained; live consumer validation remains user-owned. No `.gfx`, character, gameplay, or localization files changed.

## Parent current-family review

The parent independently reviewed the current Rabid v2 and Godly Figure runtime portraits at native156x210, alongside the complete Holy Realm progression family.
Their painted finish, framing, and family consistency pass this task review; the Holy Realm family uses a quiet temple interior for the human seed and ornate interiors for later stages.
This current direct acceptance within the user-authorized graphics review is separate from the contradictory earlier release-manifest status labels, which are left for their owner to reconcile.
