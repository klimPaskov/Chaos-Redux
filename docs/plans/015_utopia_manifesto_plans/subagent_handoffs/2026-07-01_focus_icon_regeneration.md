# Event 015 Focus Icon Regeneration Handoff

Date: 2026-07-01

Scope: Event 015 focus icons only. Idea, decision, decision-category, achievement, `.gfx`, localisation, GUI, event, focus, decision, idea, script, spreadsheet, and audio files were left out of scope.

## What Changed

Regenerated the full existing Event 015 `goal_utopia_*` focus icon package from actual imagegen source art.

Changed focus asset outputs:

- `docs/assets/015_utopia_manifesto/source_png/goal_utopia_*_source.png`
- `docs/assets/015_utopia_manifesto/source_png/focus_atlas_*_imagegen_atlas.png`
- `docs/assets/015_utopia_manifesto/processed_png/goal_utopia_*.png`
- `docs/assets/015_utopia_manifesto/dds/goal_utopia_*.dds`
- `gfx/interface/goals/015_utopia_manifesto/goal_utopia_*.dds`
- `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_*.png`
- `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_validation.txt`
- `docs/assets/015_utopia_manifesto/manifest.md`

## Source Mode

All regenerated focus icons are imagegen atlas crops. Seven imagegen-generated source atlases were used:

- opening and ledger icons
- common store and surplus logistics icons
- guild, useful arts, learning, and vocation icons
- Living Humanism, diplomacy, mercy, and League icons
- Island Discipline, coastal defense, convoy, and just-war icons
- Needful Land, arbitration, survey, and Marked Bounds icons
- adaptive and late-outcome icons

Local processing only removed the chroma-key background, cropped atlas cells, fit each icon to 94x86, exported PNG previews, wrote DDS files, and produced contact sheets. No primitive-shape or local-script-only art was used as final focus source art.

## Validation

- Regenerated focus icons: 109.
- Runtime focus DDS coverage: 109 `goal_utopia_*` files under `gfx/interface/goals/015_utopia_manifesto/`.
- DDS dimensions: all regenerated focus DDS files verified at 94x86.
- Transparency: final DDS files have transparent unused corners and no white square matte.
- Visual review: inspected `focus_regenerated_imagegen_contact_01.png` through `focus_regenerated_imagegen_contact_04.png` after a second matte pass removed visible chroma-key edge artifacts.

## Blockers And Review

Blocked focus icons: none.

Needs parent review: none flagged by this pass.
