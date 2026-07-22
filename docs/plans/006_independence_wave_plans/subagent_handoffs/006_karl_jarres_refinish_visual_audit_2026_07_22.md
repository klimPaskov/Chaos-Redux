# Event 006 Karl Jarres refinish visual audit

Date: 2026-07-22  
Reviewer scope: visual/source admission only; no gameplay, GFX, DDS, source
manifest, or existing image files were changed.

## Decision

**`needs_revision` / rejected for runtime admission. Do not convert or wire the
current ImageGen refinish.** The source identity and provenance are defensible,
but the refined portrait does not yet preserve a recognisable Karl Jarres
likeness strongly enough for a grounded real-country leader. It reads as a
generic middle-aged man wearing a Jarres-like hat. This is not approval of a
generated substitute and no fallback is authorised.

## Files and references reviewed

- Primary source: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/RHI/RHI_karl_jarres_bundesarchiv_1925.jpg`
- Identity cross-check: `.../source_masters/RHI/RHI_karl_jarres_loc_undated.jpg`
- Trial source: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/imagegen_sources/RHI/RHI_karl_jarres_hoi4_trial_01.png`
- Refined source: `.../imagegen_sources/RHI/RHI_karl_jarres_hoi4_refined_02.png`
- Native review PNG: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/processed_png/RHI/RHI_karl_jarres_hoi4.png`
- Canonical family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/CATALOG.md` entry and `portraits/leaders/contact_sheet.png`; representative native references reviewed were Stauning, Mannerheim, Björnsson, and Zahir Shah.
- Provenance/processing ledgers: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/manifest.md` and `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/manifest.md`.

## Provenance and source consistency

- The Bundesarchiv 1925 master is the stated primary (Bild 102-01175, CC BY-SA
  3.0 Germany) and the LOC Bain master is correctly retained as a second
  face-reference, not as a replacement identity. Their local paths and source
  hashes match the two ledgers; no source-rights or ownership contradiction was
  found in this visual audit.
- The trial, refined, and processed SHA-256 values match the refinish manifest.
  The processed file is correctly native `156x210` and has an opaque RGB canvas,
  which is suitable for a portrait background.
- Documentation has a dimensional inconsistency that must be corrected before
  final admission: both ImageGen files decode as `1080x1456`, while the
  refinish manifest says `1080x1440`. The stated `1070x1440` centred crop from
  the refined file is plausible, but the actual source dimensions/crop offsets
  are not recorded consistently. This is a provenance note, not a reason to
  substitute another source.

## Visual findings

| Check | Result | Evidence |
| --- | --- | --- |
| Grounded identity | **Fail for admission** | Both generated passes retain the hat and broad costume cues, but the face is too broad, smooth, and symmetrical relative to both Jarres photographs. The long/narrow facial structure, hooded eyes, source asymmetry, and reserved mouth do not survive reliably. The refined face is an interchangeable German-looking man at full resolution and remains so at `156x210`. |
| Trial versus refined | **Refined is an improvement, not a fix** | Refined corrects some eye/age drift and keeps the coat/hat composition, but it does not recover Jarres-specific facial geometry. The trial is more youthful and wide-eyed; neither is safe. |
| Age continuity | **Partial** | The refined subject reads approximately early/mid-50s, compatible with Jarres in 1925/1936. The smoother skin and fuller jaw still de-age and genericise him compared with the archival face. |
| Expression and pose | **Partial / revise** | Frontal neutral gaze is readable, but Jarres's source expression is guarded and slightly downward/side-oriented. Recomposition is allowed only if the face geometry and characteristic expression remain recognisable. |
| Hat continuity | **Revise** | The hat is the strongest source cue, but the generated crown is too tall/peaked and the brim is too wide and curled, drifting toward a generic Western/fedora silhouette. It must match the archival 1925 hat's lower crown, restrained centre crease, and narrower brim. |
| Clothing continuity | **Mostly pass, minor revise** | Dark overcoat, white collar, and tie remain civic/period-appropriate and no invented insignia, flag, text, prop, or second person appears. Lapels are broader and more dramatic than the source; keep them restrained. |
| HOI4 painted finish | **Partial** | It is genuinely painted (not a raw or filtered photograph), with clean silhouette and no photo artefacts. However, the skin/coat brush texture is heavier and more high-contrast than the quiet vanilla leader family. Reduce texture and harsh modelling. |
| Background/value treatment | **Revise** | Native output is a dark olive-green vignette (`processed` corner mean approximately RGB 111/108/95), substantially darker/greener than the canonical leader references' muted warm-grey/cream backgrounds. This weakens family consistency and makes the face read as a generic dramatic portrait. |
| Native composition/readability | **Pass conditionally** | The `156x210` crop has a clean head-and-shoulders silhouette, no clipped hat, and readable eyes/mouth. Hat and shoulders occupy the expected leader canvas. Preserve this framing while correcting likeness; do not crop tighter around the generic face. |
| Invented details | **Fail only where noted** | No forbidden text, symbols, fantasy elements, glasses, facial hair, modern props, or insignia were introduced. The overbuilt hat, widened lapels, and dark olive background are invented visual details that must be pulled back. |

## Required correction before another review

1. Repaint/recompose from the unchanged Bundesarchiv master, using the LOC
   image only to lock the same person's facial structure. Preserve Jarres's
   longer oval/rectangular face, narrower jaw/chin, small hooded eyes, source
   brow/eye asymmetry, nose profile, and restrained mouth; do not solve identity
   with the hat alone.
2. Match the archival hat silhouette (lower crown, restrained crease, narrower
   brim) and reduce the dramatic coat lapels. Keep the civic dark-overcoat,
   white-collar, no-insignia treatment.
3. Use the vanilla leader family's quiet, pale warm-grey/cream painted
   background and controlled value range. Remove the dark olive cast and
   conspicuous diagonal brush texture while retaining a clearly painted finish.
4. Re-export a correctly framed `156x210` review PNG, then repeat an
   independent likeness check at native scale. Do not create a DDS or register
   a sprite until that check passes.
5. Correct the refinish manifest's `1080x1440` claims to the actual `1080x1456`
   ImageGen masters and document the exact crop used. The parent owns that
   manifest correction; this handoff intentionally does not edit it.

## Final handoff state

The sourced Karl Jarres identity remains `source_ready`; only the current
ImageGen repaint is rejected pending revision. Runtime target remains
`GFX_portrait_RHI_independence_wave_provisional_directorate` at
`156x210`. No DDS path is approved, no `.gfx` wiring is approved, and no
fictional, generic, female, advisor, or alternate-person fallback may be used.
