# CBRN advisor card reprocessing handoff

## Outcome

The twelve existing CBRN historical advisor and theorist cards were regenerated from their existing approved `156x210` scientist DDS sources with the latest `create_advisor_icon.py` cover-fit behavior. The complete source canvas is uniformly scaled with an aspect-preserved result until it covers the measured rotated opening, centered at the opening center, and clipped only by the unchanged dossier frame.

The new cards passed independent native, `4x`, alignment, vanilla-scale, no-gap, no-stretch, and composition review for all twelve IDs. The producer did not self-approve.

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
- Complete-source covering content: `33.498777618135534 x 45.09450833210553`.
- Frame clip: horizontal `1.5106858015606246` pixels on each side, with no vertical clip.
- Metadata flags for every card: `source_pre_crop=false`, `frame_clip=true`, `frame_clip_pixels=[1.5106858015606246,0.0,1.5106858015606246,0.0]`, `stretch=false`, `matte=false`, and `anisotropic_scale=false`.
- The latest processor mechanically rejects anisotropic rendering, so stretching is rejected before output.
- The focused processor suite contains 15 tests; the parent reran all 15 successfully against the final processor state.
- The template remains the final composited layer and was not reconstructed or modified.

## Generated files and runtime wiring

Every card directory contains a `65x67` native PNG, `260x268` nearest-neighbour `4x` review PNG, `284x314` placement study, `520x536` `8x` red/green/yellow alignment overlay, and metadata JSON. The package also contains regenerated native, `4x`, and alignment contact sheets plus a `validation_report.json` with per-card dimensions, hashes, opening coverage, DDS-header, pixel-equality, and stable-GFX-path evidence.

The twelve staged DDS files were emitted by `create_advisor_icon.py`. The twelve stable runtime DDS files were generated from the native PNGs with:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <native.png> --output <runtime.dds> --width 65 --height 67
```

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
- Every metadata record reports cover mode, `source_pre_crop=false`, `frame_clip=true`, recorded `frame_clip_pixels`, `stretch=false`, `matte=false`, and `anisotropic_scale=false`.
- Every staged and runtime DDS is `65x67`, one-level uncompressed BGRA, exact length `17548` bytes, and pixel-identical to its native PNG.
- Every stable `GFX_idea_<ID>` sprite and `gfx/interface/advisors/cbrn/<ID>.dds` texture path remains present.
- The latest focused processor test suite was not changed; its direct `pytest` invocation remains environment-blocked because the available `pytest` interpreter lacks Pillow while the processor Python lacks pytest.

## Review state, replacement state, and remaining work

Independent read-only reviewer `019ffa95-8460-7861-9d23-ad097dca1883` approved all twelve cards across vanilla-comparable scale, opening-edge coverage, absence of stretch, face/headwear/shoulder composition, paper overlap, and red/green/yellow overlay geometry. No card required another change.

The cards are independently approved sourced placeholders based on the existing approved portraits. No styled-final replacement was requested or supplied, so `replacement_pending` is not asserted and no replacement state remains unresolved.

No blocker, fallback, or simplification remains for this card correction. Live HOI4 consumer validation remains with the user under the repository testing boundary.
