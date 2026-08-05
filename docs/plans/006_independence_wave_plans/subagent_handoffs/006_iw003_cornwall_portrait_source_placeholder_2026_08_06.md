# IW-003 Cornwall grounded leader portrait source-placeholder handoff

Date: 2026-08-06.

Scope: bounded portrait-source tranche for the dormant ACX Cornwall civic/provisional-leader surface. No gameplay, country, map, character, localisation, AI, focus, decision, or `.gfx` file was edited. The package remains unadmitted and this handoff is not a country-package completion claim.

## Source and identity

The selected grounded source is Sir Arthur Thomas Quiller-Couch (1863-1944), a Cornish writer and civic figure who remained alive in the 1936 scenario year. The source is face-visible and preserves a formal civilian head-and-shoulders view. It is a civic identity candidate for the existing `portrait_ACX_cornish_port_and_mines_committee` leader surface, not proof that Quiller-Couch held a named 1936 Cornwall provisional-office title. The parent package owner must accept that role adaptation before admission.

- Commons object page: https://commons.wikimedia.org/wiki/File%3APicture_of_Arthur_Quiller-Couch.jpg
- Direct original: https://upload.wikimedia.org/wikipedia/commons/1/19/Picture_of_Arthur_Quiller-Couch.jpg
- Archive/credit: scan from *Current Literature*, no later than 1906; author not stated on the Commons record.
- Rights basis: Commons records a public-domain basis for a pre-1929 United States publication/anonymous historical print. Territorial release status remains a parent-review caveat.
- Durable unchanged source: [portrait_ACX_cornish_port_and_mines_committee_source.jpg](../../../assets/portraits/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee_source.jpg)
- Source dimensions/mode/size: RGB `493x643`, 108,652 bytes.
- Source SHA-256: `b5c7629250c4d497985f574876dca6dd0318873f4389da5199dd8ba32744740a`.

The source was copied byte-for-byte from the prior source-ready ACX ledger at `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/source_masters/ACX/ACX_arthur_quiller_couch.jpg`. The durable archive is one flat folder and the source file is not a generated portrait.

## Crop and processing evidence

The immutable crop was created with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` and its exact decoded-pixel equality metadata. Crop rectangle is Pillow half-open `(left=50, top=20, right=450, bottom=560)`, yielding `400x540` RGB and keeping the full head, collar, shoulders, and upper jacket while removing excess border and lower torso.

- Crop PNG: `docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/crop/portrait_ACX_cornish_port_and_mines_committee_source_crop.png`
- Crop PNG SHA-256: `0e9ac8caf17803671994f52c75bc3ca5fda8e49c9fab4f8e78d3eb45cd8e16ef`
- Crop metadata: `docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/metadata/portrait_ACX_cornish_port_and_mines_committee_source_crop.json`
- Crop metadata SHA-256: `ec8dc3c5100a21a0c2d44ac913fb9fc17e63e1eae236a01c41f49ffc9c05103`
- Equality result: `exact_source_crop_verified`; decoded master rectangle and crop PNG are RGBA-pixel identical with comparison hash `cb1a0f0f4b507147a69201434f700f8bc487aeb06cfce700f0d84a7c6a02996c`.

The deterministic source-placeholder candidate uses Pillow `11.1.0` and `Image.Resampling.LANCZOS` to resize the RGB crop directly to `156x210`. No repaint, recolour, retouch, contrast change, padding, transparency, face substitution, or HOI4-style filter was applied.

- Processed PNG: `docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/processed_png/portrait_ACX_cornish_port_and_mines_committee.png`
- Processed PNG dimensions/mode/size: RGB `156x210`, 57,616 bytes.
- Processed PNG SHA-256: `bae86e8974e6d9e6bbb8ab3581e3d6eb06054d5a0387745ee5abd950944d7ab8`.
- Processing record: `docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/metadata/processed_png.md`.

## DDS and current path

The processed PNG was converted with the required repository converter:

```text
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/processed_png/portrait_ACX_cornish_port_and_mines_committee.png --output docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/final_dds/portrait_ACX_cornish_port_and_mines_committee.dds --width 156 --height 210
```

The source-placeholder DDS is `156x210`, one-level uncompressed BGRA, exact length `131168` bytes, pixel-format block `(size=32, flags=65, fourCC=0, bitcount=32, BGRA masks 0x00FF0000/0x0000FF00/0x000000FF/0xFF000000)`, texture caps `0x1000`, and alpha range `255..255`. Decoded BGRA pixels match the processed RGB PNG exactly after channel conversion.

- Evidence DDS: `docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/final_dds/portrait_ACX_cornish_port_and_mines_committee.dds`
- Evidence DDS SHA-256: `2b3b98f4621bc43f0f517a28f984337755bf193746d0dadcedffeb4f2cd9a0b8`.
- Stable current candidate path: `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds`.
- Stable candidate SHA-256: `2b3b98f4621bc43f0f517a28f984337755bf193746d0dadcedffeb4f2cd9a0b8`.

The pre-existing generated readiness-pool DDS was preserved at `docs/assets/006_independence_wave/iw003_cornwall_portrait_source_2026_08_06/superseded_generated/portrait_ACX_cornish_port_and_mines_committee_generated.dds` with SHA-256 `7e17cde267d9306495d7d879a0d623b118c70eca5fd66ddcd1c27092d2ad96ba`. The stable `gfx/leaders` file now contains the sourced `source_placeholder` bytes, not the generated readiness-pool bytes.

## Wiring and review

No ACX sprite definition or character portrait consumer exists in the current repository. The stable DDS path is therefore an unregistered readiness candidate. If IW-003 is later admitted, the parent should add a portrait-specific sprite (proposed name `GFX_portrait_ACX_cornish_port_and_mines_committee`) in the Event 006 leader portrait `.gfx` family and bind the existing character key to the stable DDS path. No advisor, commander-small, or dossier derivative was created.

The unchanged source, explicit crop, and `156x210` candidate were inspected against the canonical vanilla leader family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` and the native `156x210` references. Producer visual review (portrait subagent, 2026-08-06): face remains attributable, asymmetry and period civilian dress are unchanged, and the tighter crop reads as head-and-shoulders at native size. Independent parent review remains pending. The source is low-resolution and early (no later than 1906), so it is a source placeholder rather than a styled final.

## State and blockers

- Portrait state: `source_placeholder` candidate available; no provider-backed styled final was requested or supplied.
- Replacement state: sourced bytes replace the old generated readiness-pool DDS at the stable path; no `.gfx` or character wiring was added because the ACX package has no live consumer.
- Package state: **HOLD / fail-closed**. The current IW-003 audit still blocks ACX on the installed-map state-ID/collision contract and absent package adapter/content attestation. The Quiller-Couch role adaptation is also not a historical proof of a named 1936 provisional office and requires package-owner acceptance.
- Skipped checks: no HOI4 MCP runtime/event/focus/map validation (portrait-only tranche; ACX has no live consumer), no RunPod/provider operation, no advisor/small-pair processing, no gameplay or localisation review.
- No fallback or generated person was used.
