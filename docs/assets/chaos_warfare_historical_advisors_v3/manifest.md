# CBRN historical advisor card manifest

## Scope

This package reprocesses twelve existing approved `156x210` historical scientist portraits into native `65x67` advisor, theorist, and high-command dossier cards. It preserves every approved identity and source portrait; no source research replacement, ImageGen result, RunPod result, crop, or identity substitution is part of this package.

## Workflow

The cards use `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` and the untouched canonical `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`, whose SHA-256 is `8f594ef62afba6fdec58de66a80609350dcfe884320b11e6cb6220f1a0e19f58`.

The compositor measures opening center `24.76151027919129, 30.645146882359736`, opening size `30.477406015014285 x 45.09450833210553`, and rotation `-4.76` degrees from the template. Every canonical card uses offset `0,0` and has zero measured angular error. The full source portrait is uniformly contained at `30.477406015014285 x 41.027277327903846`, preserving the original `156:210` aspect ratio without cropping or stretching. A source-derived upper-corner matte fills the residual `4.06723100420168`-pixel top strip, and the contained portrait is bottom-aligned before the unchanged dossier template is composited.

Each `cards/<id>/` directory contains a native PNG, nearest-neighbour `4x` PNG, placement study, `8x` alignment overlay, and JSON metadata. Each metadata file records source and template hashes, measured geometry, crop and stretch booleans, contained content size, source-derived padding, selected placement, alignment error, and staged DDS hash.

## Runtime mapping

| ID | Approved source | Runtime DDS |
|---|---|---|
| `AST_howard_florey` | `gfx/leaders/scientists/portrait_AST_howard_florey.dds` | `gfx/interface/advisors/cbrn/AST_howard_florey.dds` |
| `ENG_alexander_fleming` | `gfx/leaders/scientists/portrait_ENG_alexander_fleming.dds` | `gfx/interface/advisors/cbrn/ENG_alexander_fleming.dds` |
| `ENG_paul_fildes` | `gfx/leaders/scientists/portrait_ENG_paul_fildes.dds` | `gfx/interface/advisors/cbrn/ENG_paul_fildes.dds` |
| `GER_gerhard_schrader` | `gfx/leaders/scientists/portrait_GER_gerhard_schrader.dds` | `gfx/interface/advisors/cbrn/GER_gerhard_schrader.dds` |
| `GER_kurt_blome` | `gfx/leaders/scientists/portrait_GER_kurt_blome.dds` | `gfx/interface/advisors/cbrn/GER_kurt_blome.dds` |
| `JAP_masaji_kitano` | `gfx/leaders/scientists/portrait_JAP_masaji_kitano.dds` | `gfx/interface/advisors/cbrn/JAP_masaji_kitano.dds` |
| `JAP_shiro_ishii` | `gfx/leaders/scientists/portrait_JAP_shiro_ishii.dds` | `gfx/interface/advisors/cbrn/JAP_shiro_ishii.dds` |
| `POL_franciszek_witaszek` | `gfx/leaders/scientists/portrait_POL_franciszek_witaszek.dds` | `gfx/interface/advisors/cbrn/POL_franciszek_witaszek.dds` |
| `SOV_grigory_mairanovsky` | `gfx/leaders/scientists/portrait_SOV_grigory_mairanovsky.dds` | `gfx/interface/advisors/cbrn/SOV_grigory_mairanovsky.dds` |
| `SOV_ivan_mikhailovich_velikanov` | `gfx/leaders/scientists/portrait_SOV_ivan_mikhailovich_velikanov.dds` | `gfx/interface/advisors/cbrn/SOV_ivan_mikhailovich_velikanov.dds` |
| `USA_frank_olson` | `gfx/leaders/scientists/portrait_USA_frank_olson.dds` | `gfx/interface/advisors/cbrn/USA_frank_olson.dds` |
| `USA_ira_baldwin` | `gfx/leaders/scientists/portrait_USA_ira_baldwin.dds` | `gfx/interface/advisors/cbrn/USA_ira_baldwin.dds` |

## Review surfaces

- `contact_sheets/cbrn_selected_cards_native_contact_sheet.png`
- `contact_sheets/cbrn_selected_cards_4x_contact_sheet.png`
- `contact_sheets/cbrn_alignment_overlays_contact_sheet.png`
- `independent_visual_review.md`
