# CBRN historical advisor card manifest

## Scope

This package reprocesses twelve existing approved `156x210` historical scientist portrait sources into native `65x67` CBRN advisor and theorist dossier cards. The source identities and approved source DDS files remain unchanged. No source replacement, ImageGen result, RunPod result, repaint, identity substitution, gameplay edit, localisation edit, or `.gfx` edit is part of this pass.

## Source and provenance

The source mode is `grounded_source_existing_approved_dds`. Each source is the existing approved local scientist portrait at `gfx/leaders/scientists/portrait_<ID>.dds`, decoded as an opaque `156x210` DDS. No new Internet source was introduced in this bounded reprocessing pass, so no new attribution or rights claim is made here; the previously approved source attribution and rights status remain unchanged and parent-owned. The source paths, decoded dimensions, SHA-256 hashes, and per-card output hashes are retained in `validation_report.json` and each card metadata record.

| ID | Approved source | Source SHA-256 |
|---|---|---|
| `AST_howard_florey` | `gfx/leaders/scientists/portrait_AST_howard_florey.dds` | `98dc7c95278658a08820e1aab6465283574d694e57de568d6f80d05303a127e2` |
| `ENG_alexander_fleming` | `gfx/leaders/scientists/portrait_ENG_alexander_fleming.dds` | `a4ec2e9656c029dc01843d0d659daa72efe666477d9a88d9f366d679577cdd44` |
| `ENG_paul_fildes` | `gfx/leaders/scientists/portrait_ENG_paul_fildes.dds` | `5baf538b7eb09733e2387424c18885c5c854c9bd926dcce8a020e8b9457af1e5` |
| `GER_gerhard_schrader` | `gfx/leaders/scientists/portrait_GER_gerhard_schrader.dds` | `08e168b09d16f6a8b972f6ee9a873c283aa13356c0e7fc02aa0533107dd95af6` |
| `GER_kurt_blome` | `gfx/leaders/scientists/portrait_GER_kurt_blome.dds` | `02ba623450b7645114e9473ce8490c558d35c10dad802a85f2abf10c5d7fb4e2` |
| `JAP_masaji_kitano` | `gfx/leaders/scientists/portrait_JAP_masaji_kitano.dds` | `ab11d4d4ab13bfd906f76f63b7c68b078a52af1ea4fdf292ec130cb7440a4421` |
| `JAP_shiro_ishii` | `gfx/leaders/scientists/portrait_JAP_shiro_ishii.dds` | `ba806c1ba5c12cfd8c79e5e207f96501b704bc2022f44cbb40296ef74588a985` |
| `POL_franciszek_witaszek` | `gfx/leaders/scientists/portrait_POL_franciszek_witaszek.dds` | `720bc822c3c8ae285573a0267fbcf2aea1b2a19ba5b698635fc9baa7a48a6670` |
| `SOV_grigory_mairanovsky` | `gfx/leaders/scientists/portrait_SOV_grigory_mairanovsky.dds` | `a6b219a9cde2a93ca76030a69a74dc135f606f7a187dab85c47f65e282f28038` |
| `SOV_ivan_mikhailovich_velikanov` | `gfx/leaders/scientists/portrait_SOV_ivan_mikhailovich_velikanov.dds` | `053752e40a48c28ad69780a8f229ea233d6eda05be9c2abcec6df01194315445` |
| `USA_frank_olson` | `gfx/leaders/scientists/portrait_USA_frank_olson.dds` | `898520be5692a36956dc5ebfd8e3638abeded4c3a7b48d9175ab9f95ab426feb` |
| `USA_ira_baldwin` | `gfx/leaders/scientists/portrait_USA_ira_baldwin.dds` | `9ea3896726d4748b4e6fd7b90fdaf876d8281a0036aa6230e0e4cba4ab36edc2` |

## Canonical template and cover-fit workflow

The compositor uses `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` with the unchanged canonical `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`. The template is `65x67` with SHA-256 `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58` and remains the final top layer.

The measured opening center is `24.76151027919129, 30.645146882359736`, the measured opening fill plane is `30.477406015014285 x 45.09450833210553`, and the measured rotation is `-4.76` degrees. Every card uses offset `0,0`, selected rotation `-4.76`, and zero measured angular error.

The complete `156x210` source canvas is loaded without pre-cropping or pre-warping and uniformly scaled with one aspect-preserving factor until it covers the measured opening. The covering content is `33.498777618135534 x 45.09450833210553`; the opening clips only the horizontal excess of `1.5106858015606246` pixels on each side. The portrait is centered under the unchanged frame, with no matte, no padding, no transparent gap, no black gap, and no stretch.

Every metadata record reports `source_pre_crop=false`, `frame_clip=true`, `frame_clip_pixels=[1.5106858015606246,0.0,1.5106858015606246,0.0]`, `stretch=false`, `matte=false`, and `anisotropic_scale=false`. The latest processor mechanically rejects anisotropic rendering, so the no-stretch condition is enforceable rather than visual-only. All 15 focused processor tests pass against the final state.

## Generated evidence and runtime outputs

Each `cards/<ID>/` directory contains the fresh native `65x67` PNG, nearest-neighbour `4x` `260x268` review PNG, `284x314` placement study, `520x536` `8x` alignment overlay, and metadata JSON. The overlay uses red for the measured opening, green for the opening fill plane, and yellow for the complete uniformly fitted portrait bounds.

Each staged DDS under `staged_dds/` is a `65x67` one-level uncompressed 32-bit BGRA output from `create_advisor_icon.py`. Each runtime DDS under `gfx/interface/advisors/cbrn/` was then created from its native PNG with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 65 --height 67`. The staged and runtime DDS pixels are identical to their native PNG, and the header, dimensions, exact length, BGRA masks, and texture caps are recorded in `validation_report.json`.

## Runtime mapping and wiring

| ID | Stable runtime DDS | Stable sprite |
|---|---|---|
| `AST_howard_florey` | `gfx/interface/advisors/cbrn/AST_howard_florey.dds` | `GFX_idea_AST_howard_florey` |
| `ENG_alexander_fleming` | `gfx/interface/advisors/cbrn/ENG_alexander_fleming.dds` | `GFX_idea_ENG_alexander_fleming` |
| `ENG_paul_fildes` | `gfx/interface/advisors/cbrn/ENG_paul_fildes.dds` | `GFX_idea_ENG_paul_fildes` |
| `GER_gerhard_schrader` | `gfx/interface/advisors/cbrn/GER_gerhard_schrader.dds` | `GFX_idea_GER_gerhard_schrader` |
| `GER_kurt_blome` | `gfx/interface/advisors/cbrn/GER_kurt_blome.dds` | `GFX_idea_GER_kurt_blome` |
| `JAP_masaji_kitano` | `gfx/interface/advisors/cbrn/JAP_masaji_kitano.dds` | `GFX_idea_JAP_masaji_kitano` |
| `JAP_shiro_ishii` | `gfx/interface/advisors/cbrn/JAP_shiro_ishii.dds` | `GFX_idea_JAP_shiro_ishii` |
| `POL_franciszek_witaszek` | `gfx/interface/advisors/cbrn/POL_franciszek_witaszek.dds` | `GFX_idea_POL_franciszek_witaszek` |
| `SOV_grigory_mairanovsky` | `gfx/interface/advisors/cbrn/SOV_grigory_mairanovsky.dds` | `GFX_idea_SOV_grigory_mairanovsky` |
| `SOV_ivan_mikhailovich_velikanov` | `gfx/interface/advisors/cbrn/SOV_ivan_mikhailovich_velikanov.dds` | `GFX_idea_SOV_ivan_mikhailovich_velikanov` |
| `USA_frank_olson` | `gfx/interface/advisors/cbrn/USA_frank_olson.dds` | `GFX_idea_USA_frank_olson` |
| `USA_ira_baldwin` | `gfx/interface/advisors/cbrn/USA_ira_baldwin.dds` | `GFX_idea_USA_ira_baldwin` |

Existing `interface/cbrn_historical_advisors.gfx`, `interface/_scientists_portraits.gfx`, character IDs, large scientist portrait paths, and small-slot sprite names remain stable and were read-only checked.

## Review and replacement state

All twelve outputs passed independent native, `4x`, alignment, vanilla-scale, no-gap, no-stretch, and composition review. `independent_visual_review.md` records the per-card approval and `validation_report.json` records the automated evidence.

The runtime state is an independently approved sourced placeholder derived from the existing approved historical source portraits. No user-supplied HOI4-style styled final was requested or supplied, so there is no replacement to install and no `replacement_pending` claim. The user remains the only RunPod operator for any future styled-final branch.

## Review surfaces

- `contact_sheets/cbrn_selected_cards_native_contact_sheet.png`
- `contact_sheets/cbrn_selected_cards_4x_contact_sheet.png`
- `contact_sheets/cbrn_alignment_overlays_contact_sheet.png`
- `validation_report.json`
- `independent_visual_review.md`
