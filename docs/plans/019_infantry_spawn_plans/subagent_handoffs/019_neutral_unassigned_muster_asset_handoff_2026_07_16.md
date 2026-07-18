# Event 019 Identity-Neutral Muster Asset Handoff

Date: 2026-07-16

Status: complete

The first bounded asset subagent attempt stopped before producing files because the Codex subagent usage limit was reached. The parent completed the same approved built-in ImageGen workflow directly. No substitute, reused claimant scene, or external fallback was used.

## Runtime contract

- Sprite: `GFX_portrait_infantry_spawn_unassigned_muster`
- Texture: `gfx/leaders/019_infantry_spawn/portrait_019_unassigned_muster.dds`
- Consumers: the two claimant scripted-localisation fallthroughs, the Muster Board initial sprite, and the SCN-013 generic or unknown-provider army-scene fallthrough
- Semantics: display-only technical default. It never assigns claimant profile 01, a family row, a region, a leader identity, or any gameplay state.

## Generation prompt

The built-in ImageGen request used `event_019_claimant_processed_contact_sheet.png` only as a style reference and required an entirely original vertical scene:

> Generate one identity-neutral 1936–1945 massed army muster for a Hearts of Iron IV portrait-shaped UI slot. The formation, not a leader, is the subject. Show an anonymous assembly ground at dawn with deep infantry blocks, period field guns, unmarked supply lorries, and canvas depots in radial-and-column geometry. Use an elevated documentary viewpoint, restrained painterly HOI4 finish, and muted charcoal, khaki, steel, and dusty amber. No individual focal person, visible face, officer, commander, podium, national uniform, flag, emblem, readable text, number, landmark, region-specific terrain, modern equipment, fantasy element, collage, reuse, recolour, or transformed prior scene.

Retained built-in output: `exec-b8e36c0c-d7c1-47f9-8c39-d4892af7ba58.png`.

## Asset chain

| Stage | Path | Dimensions / bytes | SHA-256 |
| --- | --- | ---: | --- |
| Source | `docs/assets/019_infantry_spawn/source_png/portraits/technical/portrait_019_unassigned_muster_source.png` | 1085x1450 / 2901239 | `03dfba747c7b0d22e6af87bbc08eb34b65670cf42a8bdd680359f5697c7d4ae6` |
| Processed | `docs/assets/019_infantry_spawn/processed_png/portraits/technical/portrait_019_unassigned_muster.png` | 156x210 / 63962 | `2534bd36ca5cf6a01e93b2b8d573edd948f524b6a6240a6bd7d22af6d617546c` |
| Runtime | `gfx/leaders/019_infantry_spawn/portrait_019_unassigned_muster.dds` | 156x210 / 131168 | `17327542dd0669469a20b2e41d64d78e3885fb358d58edc23351d031ca33d3fe` |

Review sheets:

- `docs/assets/019_infantry_spawn/contact_sheets/event_019_unassigned_muster_source_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_unassigned_muster_processed_contact_sheet.png`

## Visual review

Source-size and 156x210 review show a massed radial army assembly with no focal human, readable insignia, flag, emblem, national architecture, or regional landmark. The scene remains readable as an army at runtime size and is visually distinct from all twenty claimant and six derivative source images.

## Validation

`process_event_019_generated_art.py` completed successfully after adding the technical scene to its source, processing, conversion, contact-sheet, uniqueness, and decoded-pixel-parity checks. Its final portrait result was:

`validated 20 claimant army scenes, 6 derivative host scenes, and 1 identity-neutral muster scene`

The DDS is legacy uncompressed 32-bit BGRA, has the required 131168-byte length, and is decoded-pixel-equal to the processed PNG.

## Simplifications, omissions, and blockers

None. The technical scene is a separately generated original, not a gameplay fallback or identity substitution.
