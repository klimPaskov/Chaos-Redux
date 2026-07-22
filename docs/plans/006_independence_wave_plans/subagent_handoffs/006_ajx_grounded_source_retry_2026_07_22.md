# Event 006 AJX grounded source retry handoff

Date: 2026-07-22
Owner: sourced visual asset subagent
Scope: source/research and source-ready portrait package only

## Result

The AJX retry now has two independently sourced, face-visible archival
portrait packages under
`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/`.

- **Leader candidate - Johannes Hoffmann (1890-1967):** complete source
  master, explicit 156x210 head-and-shoulders crop, DDS, and provenance. The
  Nationaal Archief/Anefo original is CC0 and the Saar civic/constitutional
  identity is strong. Status remains `needs_user_review` because the image is
  dated 7 September 1955, after the 1936 scenario; the parent must explicitly
  accept the age/era gap before wiring.
- **Commander candidate - Willy Schmelcher (1894-1974):** complete source
  master, explicit 156x210 head-and-shoulders crop, DDS, and provenance. The
  1938 public-domain archival book portrait and Schmelcher's exact
  Saarbruecken Polizeipraesident role make this `source_ready`. His SS/police
  context must remain explicit in the parent implementation and final review.

No character, event, localisation, GFX, history, interface, runtime `gfx/`,
advisor icon, or `_small` file was edited. No generated face or external-mod
art/source was used.

## Owned files

Asset package:

- [README.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/README.md)
- [manifest.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/manifest.md)
- [gfx_handoff.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/gfx_handoff.md)
- [ownership and candidate log](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/search_notes/ownership_and_candidate_log.md)
- [contact sheet](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/contact_sheets/ajx_grounded_sources_and_crops.png)
- [source hash inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/source_hashes.sha256)
- `source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg`
- `source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg`
- `processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png`
- `processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png`
- `final_dds/AJX/AJX_johannes_hoffmann.dds`
- `final_dds/AJX/AJX_willy_schmelcher.dds`

## Handoff details

1. Hoffmann direct original: Nationaal Archief/Anefo, photographer Joop van
   Bilsen, archive component 907-3171, 7 Sep 1955, [Commons record](https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg),
   [durable archive handle](http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84),
   [direct original](https://upload.wikimedia.org/wikipedia/commons/f/f9/Stemming_Saarstatuut_Minister_President_Hoffmann%2C_Bestanddeelnr_907-3171.jpg?download=1).
2. Schmelcher direct original: 1938 *Der Grossdeutsche Reichstag* portrait,
   image credit A. Gerspach, [Commons record](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg),
   [direct original](https://upload.wikimedia.org/wikipedia/commons/6/69/Willy_Schmelcher.jpg),
   Commons public-domain / `PD-Germany-Section-134` record.
3. Both crops were direct geometry and resize only; no retouching, face
   reconstruction, recolouring, background replacement, or uniform invention.
   DDS files were made with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`
   at 156x210 legacy uncompressed BGRA 32-bit.
4. Exact/variant ownership search found no current Chaos Redux, vanilla,
   Kaiserreich `1521695605`, or approved `2265420196` real-person owner. The
   approved `1458561226` Saarland history contains a Johannes Hoffmann
   historical-person overlap at lines 163-164, but the parent clarified that
   cross-mod reuse is non-blocking; no art/source was copied from that mod.

## Parent actions required

- Decide whether the 1955 Hoffmann image is acceptable for the 1936 grounded
  leader. If not, keep the leader surface `needs_user_review`; do not invent or
  generic-fill it.
- Decide whether to preserve current fictional role-key sprites or perform a
  guarded identity transfer to grounded names. Suggested paths and sprite
  structures are documentation-only in `gfx_handoff.md`.
- Review Schmelcher's Nazi SS/police context and the Commons public-domain
  basis before copying the package DDS to a runtime `gfx/` path.

## Validation evidence

- Source masters were downloaded from the direct Wikimedia upload URLs and
  are hash-recorded unchanged.
- PNG dimensions are exactly 156x210; DDS headers report width 156 and height
  210, and the package hash inventory matches all binary outputs.
- Contact sheet visually compares each unchanged master with its crop.
- No files outside the new asset package and this dated handoff were changed
  by this subagent.

## Focused commit

Focused commit: `06b5008f6` (will be amended once to record this hash in the
handoff itself).
