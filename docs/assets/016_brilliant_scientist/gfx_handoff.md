# Event 016 GFX handoff

Date: 2026-07-14

## Opening appointment report card

- Final DDS: `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds`
- Exact proposed sprite: `GFX_report_event_016_brilliant_scientist_appointment`
- Target GFX file: `interface/016_brilliant_scientist.gfx`
- Target events: `chaosx.nr16.2` and `chaosx.nr16.3`
- Target size: `210x176`
- Asset status: `wired`
- Naming or placement uncertainty: none

Ready-to-copy sprite definition:

```text
spriteType = {
	name = "GFX_report_event_016_brilliant_scientist_appointment"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds"
}
```

The registered event-picture reference used by both visible opening appointment events is:

```text
picture = GFX_report_event_016_brilliant_scientist_appointment
```

Both events use the dedicated sepia dossier or report-card presentation while preserving the approved Stage-0 identity. The persistent character portrait sprites remain unchanged.

## Review evidence

- Source: `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_appointment_source.png`
- Processed preview: `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_appointment.png`
- Contact sheet: `docs/assets/016_brilliant_scientist/contact_sheets/report_event_016_brilliant_scientist_appointment_contact_sheet.png`
- The processed PNG and decoded DDS are pixel-identical.
- The DDS is a one-level legacy uncompressed `210x176` BGRA texture with real `0..255` alpha and fully transparent corners and outer edges.

No `.gfx`, event, localisation, gameplay, GUI, spreadsheet, or later-stage art file was edited in this asset tranche.

## Kruger State focus icons 041-060

Date: 2026-07-24

- Final DDS folder: `gfx/interface/goals/016_brilliant_scientist/`.
- Sprite naming: `GFX_goal_<exact focus id>` for normal sprites; each registered `_shine` sprite reuses the same DDS through `GFX_focustree_goal_effect`.
- Runtime size and encoding: exact `94x86`, one-level uncompressed BGRA DDS, with transparent corners.
- Source masters: `docs/assets/016_brilliant_scientist/source_png/focus_icons/goal_KRG_*_source.png` for rows 041-060.
- Alpha evidence: `docs/assets/016_brilliant_scientist/alpha_png/focus_icons/goal_KRG_*_alpha.png` for rows 041-060.
- Processed previews: `docs/assets/016_brilliant_scientist/processed_png/focus_icons/goal_KRG_*.png` for rows 041-060.
- Prompt/provenance ledger: `docs/assets/016_brilliant_scientist/package_records/focus_icon_generation_041_060_provenance.json`.
- Validation: `docs/assets/016_brilliant_scientist/validation/focus_icon_validation_041_060.tsv`; all 20 rows decode pixel-identically from DDS and report zero visible key-color pixels.
- Review sheets: `docs/assets/016_brilliant_scientist/contact_sheets/focus_icon_sources_041_060_contact_sheet.png`, `focus_icon_processed_041_060_contact_sheet.png`, and `focus_icon_dds_decoded_041_060_contact_sheet.png`.

No `.gfx`, focus, localisation, gameplay, GUI, event, spreadsheet, or unrelated asset file was edited for this focus-icon tranche.

## Kruger State focus icons 061-080

Date: 2026-07-24

- Final DDS folder: `gfx/interface/goals/016_brilliant_scientist/`.
- Sprite naming: `GFX_goal_<exact focus id>` for normal sprites; each registered `_shine` sprite reuses the same DDS through `GFX_focustree_goal_effect`.
- Runtime size and encoding: exact `94x86`, one-level uncompressed BGRA DDS, with transparent corners.
- Source masters: `docs/assets/016_brilliant_scientist/source_png/focus_icons/goal_KRG_*_source.png` for rows 061-080.
- Alpha evidence: `docs/assets/016_brilliant_scientist/alpha_png/focus_icons/goal_KRG_*_alpha.png` for rows 061-080.
- Processed previews: `docs/assets/016_brilliant_scientist/processed_png/focus_icons/goal_KRG_*.png` for rows 061-080.
- Prompt/provenance ledger: `docs/assets/016_brilliant_scientist/package_records/focus_icon_generation_061_080_provenance.json`.
- Validation: `docs/assets/016_brilliant_scientist/validation/focus_icon_validation_061_080.tsv`; all 20 rows decode pixel-identically from DDS and report zero visible key-color pixels.
- Review sheets: `docs/assets/016_brilliant_scientist/contact_sheets/focus_icon_sources_061_080_contact_sheet.png`, `focus_icon_processed_061_080_contact_sheet.png`, and `focus_icon_dds_decoded_061_080_contact_sheet.png`.

No `.gfx`, focus, localisation, gameplay, GUI, event, spreadsheet, or unrelated asset file was edited for this focus-icon tranche.

## Achievement icon triplets

Date: 2026-07-24

- Final DDS folder: `gfx/achievements/` (achievement root exception).
- Runtime size and encoding: exact `64x64`, one-level uncompressed BGRA DDS with real alpha.
- Sprite registry: `interface/chaosx_achievements.gfx`, using the already-registered `GFX_achievement_<achievement_id>`, `_grey`, and `_not_eligible` names.
- Source masters: `docs/assets/016_brilliant_scientist/source_png/016_brilliant_scientist_*.png` (17 generated 1254x1254 RGB masters).
- Alpha evidence: `docs/assets/016_brilliant_scientist/alpha_png/016_brilliant_scientist_*.png` (17 1254x1254 RGBA chroma-key extractions).
- Processed previews: `docs/assets/016_brilliant_scientist/processed_png/` (51 exact 64x64 RGBA PNGs).
- Prompt/provenance record: `docs/assets/016_brilliant_scientist/prompts/achievement_icon_generation_record.md` and the identity prompts in `achievement_icon_prompts.md`.
- Dimension and SHA-256 ledger: `docs/assets/016_brilliant_scientist/package_records/achievement_icon_hashes.json`.
- Review sheet: `docs/assets/016_brilliant_scientist/contact_sheets/016_brilliant_scientist_achievement_icons_contact_sheet.png`.
- Ineligibility treatment: each `_not_eligible` PNG and DDS is an alpha composite of its mechanically grayscale-derived sibling with `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`; silhouettes and composition remain identical.

All seventeen identities have complete completed, grey, and not-eligible triplets. No `.gfx`, achievement, localisation, gameplay, GUI, event, focus, idea, decision, or spreadsheet file was edited in this icon-production tranche.

## Kruger State decision and decision-category icon package

Date: 2026-07-24

Parent wiring target: `interface/016_brilliant_scientist.gfx`. Runtime decisions are in `gfx/interface/decisions/016_brilliant_scientist/decisions/`; runtime categories are in `gfx/interface/decisions/016_brilliant_scientist/categories/`. Decisions are exact `32x32`; categories are exact `50x40`. Ready-to-copy exact sprite blocks for all 40 decisions and 10 categories are retained in `docs/assets/016_brilliant_scientist/package_records/decision_category_sprite_blocks.txt`.

Representative exact blocks (the package-record file contains the remaining unchanged rows):

```text
spriteType = { name = "GFX_decision_brilliant_scientist_krg_foundation_repair" texturefile = "gfx/interface/decisions/016_brilliant_scientist/decisions/decision_foundation_repair.dds" }
spriteType = { name = "GFX_decision_brilliant_scientist_krg_singularity_arming" texturefile = "gfx/interface/decisions/016_brilliant_scientist/decisions/decision_singularity_arming.dds" }
spriteType = { name = "GFX_decision_category_brilliant_scientist_krg_foundation_administration" texturefile = "gfx/interface/decisions/016_brilliant_scientist/categories/decision_category_foundation_administration.dds" }
spriteType = { name = "GFX_decision_category_brilliant_scientist_krg_terminal_program" texturefile = "gfx/interface/decisions/016_brilliant_scientist/categories/decision_category_terminal_program.dds" }
```

The 130-row semantic decision assignment ledger is `docs/assets/016_brilliant_scientist/package_records/decision_assignment_ledger.tsv`; the 10-row category ledger is `docs/assets/016_brilliant_scientist/package_records/decision_category_assignment_ledger.tsv`. Do not edit gameplay or `.gfx` in this asset tranche; parent wiring should copy the blocks unchanged. No `.gfx`, decision, category, localisation, GUI, gameplay, focus, or spreadsheet file was edited here.
