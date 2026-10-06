# Resources Found small advisor-portrait manifest

Updated 2026-10-06 for the three small DHO advisor portraits used by army advisors.

The existing runtime sprite names, texture paths, and character references remain unchanged in `interface/chaosx_characters.gfx` and `common/characters/018_resources_found_cave_characters.txt`.

| Sprite | Source master DDS | Master SHA-256 | Candidate PNG | Runtime DDS | Runtime SHA-256 |
|---|---|---|---|---|---|
| `GFX_portrait_DHO_thessik_small` | `gfx/leaders/018_resources_found/portrait_DHO_thessik.dds` | `a424a94fd4e2d4e4715310ea339e2df998b5db1704fbe911d07a400e1f7d0f89` | `DHO_thessik_small/portrait_DHO_thessik_small_candidate_65x67.png` (`3864161d4988ff5a3c63c966147749320653046fcadf807fd11d313ce10064ef`) | `gfx/leaders/018_resources_found/portrait_DHO_thessik_small.dds` | `66e332dfb1c04af183fe964b95d985b0e64c0a55349c2593fe58da6935bed8db` |
| `GFX_portrait_DHO_orrukesh_small` | `gfx/leaders/018_resources_found/portrait_DHO_orrukesh.dds` | `0042064daec1931a5247dcea5a0975835167cf5495aaae0e1ab632e513fd6688` | `DHO_orrukesh_small/portrait_DHO_orrukesh_small_candidate_65x67.png` (`53926845e8f0f855cddfc2243d7e59a5bf0c53bb297cb1bdf409bb9159547fd6`) | `gfx/leaders/018_resources_found/portrait_DHO_orrukesh_small.dds` | `318d473ebe1ae2dc1c79f99f2ddd5526be2f45f27ee7833b7903c834484b0156` |
| `GFX_portrait_DHO_khalvek_small` | `gfx/leaders/018_resources_found/portrait_DHO_khalvek.dds` | `3c8ed895017ec8c3cbff7b542a6d712370d8dff67315cce3c5f19b967b9445ac` | `DHO_khalvek_small/portrait_DHO_khalvek_small_candidate_65x67.png` (`678ce11c9d604063c899856a7c2c94262d6c670164c57779363b4780e09b2060`) | `gfx/leaders/018_resources_found/portrait_DHO_khalvek_small.dds` | `f850e72de6aed7561dee87cf9b12e907331b34ae543e24dfe570f9d1f26100c6` |

All new DDS files are native 65×67 outputs produced by `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; each is 17,548 bytes and decoded pixel-identical to its candidate PNG.

Each original 50×67 runtime DDS is preserved at its package's `legacy_unverified_dds/*_pre_fix.dds` path with hashes recorded in `docs/plans/gfx_fix_2026-10/shared_chaosx_characters_report.md`.

The measured vanilla advisor frame uses a 65×67 portrait opening centered at `(24.7615102792, 30.6451468824)` with size `(30.4774060150, 45.0945083321)` and `-4.76°` rotation; output alignment, internal edge fill, and transparency were checked against that template.

The parent independently reviewed the native candidate sheet `review/portrait_DHO_small_candidates_native.png` (SHA-256 `30fe00caccb94abc7b4500cb364d9c42507bafb161cb2cef9f2905217e0a6b6f`) and 4× checker sheet `review/portrait_DHO_small_candidates_4x_checker.png` (SHA-256 `71ef3697cbc65fab22da8b330da61c1e0cf9580c434e468311d33161e5c45673`) and approved identity, framing, style, and transparency.

The existing full portrait masters are fictional game characters; no new character likeness or altered master was created.

Their original native ImageGen prompt/source receipts were not recovered, and this crop-only approval does not repair that inherited lineage gap.
