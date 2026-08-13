# CBRN advisor card reprocessing handoff

## Outcome

The twelve existing CBRN historical advisor and theorist cards were regenerated from their existing approved `156x210` scientist DDS sources with the corrected `create_advisor_icon.py` cover-fit behavior. The complete source canvas is uniformly scaled with an aspect-preserved result until it covers the measured rotated opening plus a safe under-frame bleed, centered at the opening center, and masked so it cannot reach the transparent card exterior.

The new cards passed independent native, `4x`, alignment, checker-background, vanilla-scale, no-gap, no-inner-edge-seam, no-exterior-spill, no-stretch, DDS-equality, and composition review for all twelve IDs. The producer did not self-approve.

## Scope and ownership boundary

This pass changed only the evidence package under `docs/assets/chaos_warfare_historical_advisors_v3/`, the twelve runtime DDS files under `gfx/interface/advisors/cbrn/`, and this named handoff.

The parent-owned processor, its focused tests, and skill documentation were consumed in their latest state and were not edited by this portrait pass. Existing character identities, traits, gameplay, localisation, events, focuses, decisions, `.gfx` definitions, and approved large scientist portraits were not changed.

RunPod was not opened, operated, configured, queued, or monitored. No HOI4-style styled-final replacement was supplied in this pass.

## Source and provenance evidence

The twelve grounded historical sources are the existing approved local files `gfx/leaders/scientists/portrait_<ID>.dds`. Each decodes as opaque `156x210`; source paths and SHA-256 hashes are recorded in `docs/assets/chaos_warfare_historical_advisors_v3/manifest.md`, `validation_report.json`, and each card metadata record. No new Internet source or ImageGen output was introduced, and no new rights claim is made; prior approved source attribution and rights status remain unchanged.

## Cover-fit geometry and processing evidence

- Canonical template: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`.
- Template dimensions and hash: `65x67`, `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`.
- Measured opening center: `24.76151027919129, 30.645146882359736`.
- Measured opening fill plane: `30.477406015014285 x 45.09450833210553`.
- Measured and selected rotation: `-4.76` degrees.
- Selected offset: `0,0`.
- Under-frame fill plane: `36.47740601501428 x 51.09450833210553`, adding the centralized `2` px bleed and `1` px resampling guard around the visible opening.
- Complete-source covering content: `37.95592047527839 x 51.09450833210553`.
- Symmetric aspect-ratio excess: horizontal `0.7392572301320541` pixels on each side, with no vertical excess.
- The safe bleed mask contains `1457` pixels and every bleed-ring pixel lies beneath nontransparent frame artwork; the processor fails closed if the bleed reaches a fully transparent exterior pixel.
- Metadata flags for every card: `source_pre_crop=false`, `frame_clip=true`, `frame_clip_pixels=[0.7392572301320541,0.0,0.7392572301320541,0.0]`, `under_frame_bleed_pixels=2`, `resampling_edge_guard_pixels=1`, `stretch=false`, `matte=false`, and `anisotropic_scale=false`.
- The latest processor mechanically rejects anisotropic rendering, so stretching is rejected before output.
- The focused processor suite contains 17 tests; the complete event-asset tool suite contains 25 tests. Both passed against the final processor state.
- The template remains the final composited layer and was not reconstructed or modified.

## Generated files and runtime wiring

Every card directory contains a `65x67` native PNG, `260x268` nearest-neighbour `4x` review PNG, `284x314` placement study, `520x536` `8x` red/green/yellow alignment overlay, and metadata JSON. The package also contains regenerated native, `4x`, alignment, and high-contrast alpha-edge contact sheets plus a `validation_report.json` with per-card dimensions, hashes, visible-opening coverage, translucent-edge coverage, exterior-spill count, DDS-header, pixel-equality, and stable-GFX-path evidence.

The twelve stable runtime DDS files were emitted by `create_advisor_icon.py`; the staged DDS files are byte-identical evidence copies. The processor's DDS round-trip gate confirms exact pixel equality with the native PNG before metadata is written.

The stable GFX sprite names and runtime texture paths remain:

| ID | Sprite | Runtime texture |
|---|---|---|
| `AST_howard_florey` | `GFX_idea_AST_howard_florey` | `gfx/interface/advisors/cbrn/AST_howard_florey.dds` |
| `ENG_alexander_fleming` | `GFX_idea_ENG_alexander_fleming` | `gfx/interface/advisors/cbrn/ENG_alexander_fleming.dds` |
| `ENG_paul_fildes` | `GFX_idea_ENG_paul_fildes` | `gfx/interface/advisors/cbrn/ENG_paul_fildes.dds` |
| `GER_gerhard_schrader` | `GFX_idea_GER_gerhard_schrader` | `gfx/interface/advisors/cbrn/GER_gerhard_schrader.dds` |
| `GER_kurt_blome` | `GFX_idea_GER_kurt_blome` | `gfx/interface/advisors/cbrn/GER_kurt_blome.dds` |
| `JAP_masaji_kitano` | `GFX_idea_JAP_masaji_kitano` | `gfx/interface/advisors/cbrn/JAP_masaji_kitano.dds` |
| `JAP_shiro_ishii` | `GFX_idea_JAP_shiro_ishii` | `gfx/interface/advisors/cbrn/JAP_shiro_ishii.dds` |
| `POL_franciszek_witaszek` | `GFX_idea_POL_franciszek_witaszek` | `gfx/interface/advisors/cbrn/POL_franciszek_witaszek.dds` |
| `SOV_grigory_mairanovsky` | `GFX_idea_SOV_grigory_mairanovsky` | `gfx/interface/advisors/cbrn/SOV_grigory_mairanovsky.dds` |
| `SOV_ivan_mikhailovich_velikanov` | `GFX_idea_SOV_ivan_mikhailovich_velikanov` | `gfx/interface/advisors/cbrn/SOV_ivan_mikhailovich_velikanov.dds` |
| `USA_frank_olson` | `GFX_idea_USA_frank_olson` | `gfx/interface/advisors/cbrn/USA_frank_olson.dds` |
| `USA_ira_baldwin` | `GFX_idea_USA_ira_baldwin` | `gfx/interface/advisors/cbrn/USA_ira_baldwin.dds` |

## Automated checks completed

- All twelve source DDS files decoded as `156x210` with alpha range `255..255`.
- All twelve native candidates are `65x67`; all `4x` reviews are `260x268`; all placement studies are `284x314`; all alignment overlays are `520x536`.
- Every opening-mask pixel has portrait coverage, with `1121` covered pixels and `0` gap pixels per card.
- Every card reports `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, and `exterior_alpha_leak_pixels=0`.
- Every metadata record reports under-frame bleed cover mode, `source_pre_crop=false`, `frame_clip=true`, recorded `frame_clip_pixels`, `under_frame_bleed_pixels=2`, `resampling_edge_guard_pixels=1`, `stretch=false`, `matte=false`, and `anisotropic_scale=false`.
- Every staged and runtime DDS is `65x67`, one-level uncompressed BGRA, exact length `17548` bytes, and pixel-identical to its native PNG.
- Every stable `GFX_idea_<ID>` sprite and `gfx/interface/advisors/cbrn/<ID>.dds` texture path remains present.
- All 17 focused advisor tests and all 25 event-asset tool tests pass with the available processor Python.

## Review state, replacement state, and remaining work

Independent read-only reviewer `chaosx_independent_cbrn_dossier_reviewer_2026-08-13` approved all twelve cards across vanilla-comparable scale, visible-opening and translucent-edge coverage, exterior-corner containment, absence of stretch, face/headwear/shoulder composition, paper overlap, checker-background evidence, DDS equality, and red/green/yellow overlay geometry. No card required another change.

The cards are independently approved sourced placeholders based on the existing approved portraits. No styled-final replacement was requested or supplied, so `replacement_pending` is not asserted and no replacement state remains unresolved.

No blocker, fallback, or simplification remains for this card correction. Live HOI4 consumer validation remains with the user under the repository testing boundary.
