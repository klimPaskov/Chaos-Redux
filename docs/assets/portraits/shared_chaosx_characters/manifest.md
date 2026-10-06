# Shared character portrait runtime manifest

Updated 2026-10-06 as the exact runtime-path ledger for the seven portrait findings assigned to `shared_chaosx_characters`.

The current stable sprite mapping is in `interface/chaosx_characters.gfx`; this tranche left that file and all character references unchanged.

| Sprite | Runtime DDS | SHA-256 | Dimensions / bytes | Disposition |
|---|---|---|---|---|
| `GFX_portrait_communist_rebels` | `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds` | `059b20336d625906b5debf1545db445e7c361f90745c239b01d7ce704da9d021` | 156×210 / 131,168 | Existing accepted archival source placeholder remains installed; HOI4-style final is pending from the user. This other-group output was left untouched. |
| `GFX_portrait_CRU_crusader` | `gfx/leaders/038_malta_crusaders/portrait_CRU_crusader.dds` | `878a3e6d9ad6e18b41c683277d863128b6d63eeba405a2e54714d379302b0edf` | 156×210 / 131,168 | Parent-approved authentic Ludovico Chigi source placeholder installed; date/age fit limited and user HOI4-style final pending. |
| `GFX_portrait_DHO_thessik_small` | `gfx/leaders/018_resources_found/portrait_DHO_thessik_small.dds` | `66e332dfb1c04af183fe964b95d985b0e64c0a55349c2593fe58da6935bed8db` | 65×67 / 17,548 | Parent-approved final dossier card; replaces prior 50×67 slot crop. |
| `GFX_portrait_DHO_orrukesh_small` | `gfx/leaders/018_resources_found/portrait_DHO_orrukesh_small.dds` | `318d473ebe1ae2dc1c79f99f2ddd5526be2f45f27ee7833b7903c834484b0156` | 65×67 / 17,548 | Parent-approved final dossier card; replaces prior 50×67 slot crop. |
| `GFX_portrait_DHO_khalvek_small` | `gfx/leaders/018_resources_found/portrait_DHO_khalvek_small.dds` | `f850e72de6aed7561dee87cf9b12e907331b34ae543e24dfe570f9d1f26100c6` | 65×67 / 17,548 | Parent-approved final dossier card; replaces prior 50×67 slot crop. |
| `GFX_portrait_ZZZ_weaponized_rabid` | `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_rabid.dds` | `8656707116a9bf12670a29dbe0f7a9c3667f045e2485337c413fb2480ae15b76` | 156×210 / 131,168 | Existing parent-approved fictional ImageGen v2 package supersedes the glossy-source finding; portrait bytes were left untouched in this tranche. |
| `GFX_portrait_THR_godly_figure` | `gfx/leaders/003_holy_realm/portrait_THR_godly_figure.dds` | `6c7adb3aa157ccc3cbefca6ea66c1bed7bfd954f4add4633137e8ff07e407be1` | 156×210 / 131,168 | Existing fictional ImageGen package supersedes the flat-thangka finding; portrait bytes were left untouched in this tranche. Its release manifest contains stale per-row review states despite its package-level parent-approved/installed claims; see `003_holy_realm/release_20261006/manifest.md`, and do not treat that contradiction as portrait acceptance evidence. |

## DHO small-card evidence

The three 65×67 outputs are derived from the unchanged fictional 156×210 masters `gfx/leaders/018_resources_found/portrait_DHO_thessik.dds` (SHA-256 `a424a94fd4e2d4e4715310ea339e2df998b5db1704fbe911d07a400e1f7d0f89`), `portrait_DHO_orrukesh.dds` (`0042064daec1931a5247dcea5a0975835167cf5495aaae0e1ab632e513fd6688`), and `portrait_DHO_khalvek.dds` (`3c8ed895017ec8c3cbff7b542a6d712370d8dff67315cce3c5f19b967b9445ac`).

The workflow followed the inspected vanilla advisor dossier frame at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/portraits/advisors/advisor_template.png` (SHA-256 `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`), including its measured `65×67` output, zero placement offset, and `-4.76°` frame tilt.

Parent independently approved `docs/assets/portraits/018_resources_found/review/portrait_DHO_small_candidates_native.png` (SHA-256 `30fe00caccb94abc7b4500cb364d9c42507bafb161cb2cef9f2905217e0a6b6f`) and `portrait_DHO_small_candidates_4x_checker.png` (SHA-256 `71ef3697cbc65fab22da8b330da61c1e0cf9580c434e468311d33161e5c45673`) for unchanged identity, framing, dossier style, and transparency.

Per-card placement measurements, source master hashes, candidate PNG hashes, and alpha-coverage tests are in the three `docs/assets/portraits/018_resources_found/DHO_*_small/*_placement_metadata.json` files.

The three prior DDS files remain preserved under each package's `legacy_unverified_dds/` directory; their SHA-256 values are recorded in the `_scientists_portraits` group report.

The full masters were inherited fictional assets without recovered generation prompts or source receipts; using their existing appearance as crop inputs does not resolve that lineage gap.

## Chigi source placeholder

The source is Bain News Service's photograph of Ludovico Chigi, archived from the [Library of Congress record LCCN 2014692087](https://www.loc.gov/pictures/item/2014692087/) and its [Commons file](https://commons.wikimedia.org/wiki/File:Prince_Chigi_LCCN2014692087.jpg); the archive marks it public domain.

The source original is `docs/assets/portraits/038_malta_crusaders/grand_master_ludovico_chigi/portrait_CRU_crusader_original.jpg` (4135×5779, SHA-256 `1cacb2129bf2da39e25ed51d432a851a038561ea294f1a77714630064ab251a0`), and the exact crop is `portrait_CRU_crusader_source_crop.png` (2200×2962, SHA-256 `bef72c818e63a718db5d44a08f9fc0fc2189316f573313ce0f420640bd7cdcda`).

The processed source placeholder is `portrait_CRU_crusader_156x210.png` (SHA-256 `6d2ce3b730a3f8a94a0c04749561223052cdf50e4a9a81b729366ea5de126fb3`), converted to the runtime DDS shown in the table with exact decoded-pixel equality.

The parent-reviewed source-crop sheet `grand_master_ludovico_chigi/review/portrait_CRU_crusader_source_crop_review.png` has SHA-256 `485cb8b408fdb6a023c91a540af1e8db8ce80a2637d8fdf2d0e32d744975e980`. Review passed identity, provenance, and framing; fit is limited because the 1910–15 photo depicts a younger Chigi before his 1931–51 Grand Master tenure.

The HOI4-style final remains pending the user; no agent used RunPod.

## Unchanged superseding packages

The anonymous communist rebels runtime source placeholder and all its attribution, crop, and pending-final evidence remain owned by the 001 package at `docs/assets/portraits/001_communism_spread/`.

The rabid zombie v2 ImageGen master is `docs/assets/portraits/002_zombie_outbreak/release_20261006/source_imagegen/portrait_ZZZ_weaponized_rabid_v2.png` (SHA-256 `618258e7481b32f2b8d4bae76275fc003534fbbc6e541659b3fd30469b3ca319`); its processed PNG is `processed_png/portrait_ZZZ_weaponized_rabid_v2.png` (SHA-256 `46fcdad1d4a48449a4f7fd1fe12c66a89e8a08128ed9fbc8b788b1d669a91928`). The current release manifest lists it as approved and installed.

The Godly Figure source is `docs/assets/portraits/003_holy_realm/release_20261006/source_png/static/portrait_THR_godly_figure_v1.png` (SHA-256 `6279944a7c21ec9b5c416ef2d1668a1089254ab25d1b82f6705e50d44e67a3bd`); processed PNG hash is `aebdf2f7d1003e16ba83656e966088de87dc331e812faee4473b46ecf6b2185c`. Its package-level disposition says parent approved and installed, while individual manifest rows still say awaiting review; the contradiction remains explicitly open.
