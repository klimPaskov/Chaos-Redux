# Event 012 Africa Prompt Idea Icons Audit And Regeneration

- Event id: `012`
- Event slug: `africa`
- Package path: `docs/assets/012_africa/icon_regen_prompt_idea_icons_2026_06_21/`
- Asset type: idea and national-spirit icons
- Target size: `64x64`
- Reference folders inspected before generation:
  - `.agents/skills/chaos-redux-event-assets/assets/ideas`
  - `.agents/skills/chaos-redux-event-assets/assets/focuses`
- Source mode for newly generated assets: built-in `$imagegen`, then local chroma-key removal and DDS conversion
- Scope note: this package audits the 12 prompt-listed idea ids, generates the 10 missing exact live DDS assets, and leaves the already-complete `idea_africa_charter_league` and `idea_africa_world_is_one_ambition` packages in place.
- Conversion note: `.tools/convert_to_dds.py` hit its known ffmpeg header-pack bug on this checkout, so the processed PNGs were written to DDS via Pillow for this package instead of patching repo tooling outside the allowed asset scope.
- Distinction rule note: every newly generated icon is its own idea-specific source artwork. None of these ten icons is a resized, cropped, recolored, or lightly edited goal icon.

## Audit Summary

Before this pass, prompt-listed live DDS coverage was:

- Present with adequate asset package and manifest:
  - `idea_africa_charter_league`
  - `idea_africa_world_is_one_ambition`
- Missing exact live DDS path:
  - `idea_africa_paper_cores`
  - `idea_africa_proclamation_without_machinery`
  - `idea_africa_regional_trust`
  - `idea_africa_colonial_alarm`
  - `idea_africa_liberation_momentum`
  - `idea_africa_congress_legitimacy`
  - `idea_africa_continental_general_staff`
  - `idea_africa_green_covenant`
  - `idea_africa_diaspora_return_cadres`
  - `idea_africa_scramble_pressure`

After this pass, all 12 prompt-listed idea ids have live DDS files under `gfx/interface/ideas/012_africa/`.

## Prompt-Listed Asset Audit

| Asset id | Live DDS before audit | Adequate manifest before audit | Live DDS after audit | Asset package used | Status |
| --- | --- | --- | --- | --- | --- |
| `idea_africa_paper_cores` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_proclamation_without_machinery` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_charter_league` | yes | yes | yes | `icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20` | `complete_existing` |
| `idea_africa_regional_trust` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_colonial_alarm` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_liberation_momentum` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_congress_legitimacy` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_continental_general_staff` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_green_covenant` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_diaspora_return_cadres` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_scramble_pressure` | no | no | yes | `icon_regen_prompt_idea_icons_2026_06_21` | `complete` |
| `idea_africa_world_is_one_ambition` | yes | yes | yes | `idea_world_is_one_ambition_2026_06_21` | `complete_existing` |

## Generated Assets In This Package

| Asset id | Source PNG | Processed PNG | Package DDS | Live DDS | Sprite name | Related prompt item | Distinction note | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `idea_africa_paper_cores` | `source_png/idea_africa_paper_cores_source.png` | `processed_png/idea_africa_paper_cores.png` | `dds/idea_africa_paper_cores.dds` | `gfx/interface/ideas/012_africa/idea_africa_paper_cores.dds` | `GFX_idea_africa_paper_cores` | `idea_africa_paper_cores` | paper-core charter bundle with pinned Africa seal; no direct goal counterpart | `complete` |
| `idea_africa_proclamation_without_machinery` | `source_png/idea_africa_proclamation_without_machinery_source.png` | `processed_png/idea_africa_proclamation_without_machinery.png` | `dds/idea_africa_proclamation_without_machinery.dds` | `gfx/interface/ideas/012_africa/idea_africa_proclamation_without_machinery.dds` | `GFX_idea_africa_proclamation_without_machinery` | `idea_africa_proclamation_without_machinery` | proclamation scroll over broken machinery; no direct goal counterpart | `complete` |
| `idea_africa_regional_trust` | `source_png/idea_africa_regional_trust_source.png` | `processed_png/idea_africa_regional_trust.png` | `dds/idea_africa_regional_trust.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_trust.dds` | `GFX_idea_africa_regional_trust` | `idea_africa_regional_trust` | clasped hands and hanging regional seals, not the map-chain `goal_africa_regional_integration` treatment | `complete` |
| `idea_africa_colonial_alarm` | `source_png/idea_africa_colonial_alarm_source.png` | `processed_png/idea_africa_colonial_alarm.png` | `dds/idea_africa_colonial_alarm.dds` | `gfx/interface/ideas/012_africa/idea_africa_colonial_alarm.dds` | `GFX_idea_africa_colonial_alarm` | `idea_africa_colonial_alarm` | alarm bell and warning beacon, not the larger scramble route map icon | `complete` |
| `idea_africa_liberation_momentum` | `source_png/idea_africa_liberation_momentum_source.png` | `processed_png/idea_africa_liberation_momentum.png` | `dds/idea_africa_liberation_momentum.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_momentum.dds` | `GFX_idea_africa_liberation_momentum` | `idea_africa_liberation_momentum` | rushing banner and broken chain, distinct from the war-office wreath/crest goal icon | `complete` |
| `idea_africa_congress_legitimacy` | `source_png/idea_africa_congress_legitimacy_source.png` | `processed_png/idea_africa_congress_legitimacy.png` | `dds/idea_africa_congress_legitimacy.dds` | `gfx/interface/ideas/012_africa/idea_africa_congress_legitimacy.dds` | `GFX_idea_africa_congress_legitimacy` | `idea_africa_congress_legitimacy` | gavel and ballot charter, not the large medallion congress-goal seal | `complete` |
| `idea_africa_continental_general_staff` | `source_png/idea_africa_continental_general_staff_source.png` | `processed_png/idea_africa_continental_general_staff.png` | `dds/idea_africa_continental_general_staff.dds` | `gfx/interface/ideas/012_africa/idea_africa_continental_general_staff.dds` | `GFX_idea_africa_continental_general_staff` | `idea_africa_continental_general_staff` | compact staff shield with baton and rail ruler, not the broad military-forces combat crest | `complete` |
| `idea_africa_green_covenant` | `source_png/idea_africa_green_covenant_source.png` | `processed_png/idea_africa_green_covenant.png` | `dds/idea_africa_green_covenant.dds` | `gfx/interface/ideas/012_africa/idea_africa_green_covenant.dds` | `GFX_idea_africa_green_covenant` | `idea_africa_green_covenant` | sacred baobab and river spiral spirit icon; no direct goal counterpart | `complete` |
| `idea_africa_diaspora_return_cadres` | `source_png/idea_africa_diaspora_return_cadres_source.png` | `processed_png/idea_africa_diaspora_return_cadres.png` | `dds/idea_africa_diaspora_return_cadres.dds` | `gfx/interface/ideas/012_africa/idea_africa_diaspora_return_cadres.dds` | `GFX_idea_africa_diaspora_return_cadres` | `idea_africa_diaspora_return_cadres` | return-pass parcel, officer cap, book, and ship badge; no direct goal counterpart | `complete` |
| `idea_africa_scramble_pressure` | `source_png/idea_africa_scramble_pressure_source.png` | `processed_png/idea_africa_scramble_pressure.png` | `dds/idea_africa_scramble_pressure.dds` | `gfx/interface/ideas/012_africa/idea_africa_scramble_pressure.dds` | `GFX_idea_africa_scramble_pressure` | `idea_africa_scramble_pressure` | clamped Africa seal under pressure, distinct from `goal_africa_scramble_for_africa` route art | `complete` |

## Existing Prompt-Listed Assets Intentionally Not Regenerated

### `idea_africa_charter_league`

- Live DDS: `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds`
- Existing package: `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v7_2026_06_20/`
- Existing supporting files confirmed:
  - `manifest.md`
  - `gfx_handoff.md`
  - `prompts/generated_prompts.md`
  - checker contacts and validation under `contact_sheets/` and `validation/`
- Decision: not regenerated in this package because the exact prompt-listed id already had a live DDS and an adequate asset package.

### `idea_africa_world_is_one_ambition`

- Live DDS: `gfx/interface/ideas/012_africa/idea_africa_world_is_one_ambition.dds`
- Existing package: `docs/assets/012_africa/idea_world_is_one_ambition_2026_06_21/`
- Existing supporting files confirmed:
  - `manifest.md`
  - `gfx_handoff.md`
  - `prompts/idea_africa_world_is_one_ambition_prompt.txt`
  - checker/contact sheet and validation notes
- Decision: not regenerated in this package because the exact prompt-listed id already had a live DDS and an adequate asset package.

## Validation Artifacts

- Source sheet: `contact_sheets/source_labeled_sheet.png`
- Processed checker sheet: `contact_sheets/processed_checker_contact.png`
- Processed dark sheet: `contact_sheets/processed_dark_contact.png`
- Live DDS checker sheet for all 12 prompt-listed icons: `contact_sheets/live_dds_checker_contact_all_12.png`
- Idea-versus-goal distinction sheet: `contact_sheets/idea_vs_goal_distinctness_pairs.png`
- Validation summary: `validation/validation_summary.md`
- Validation metrics: `validation/validation_metrics.json`

## Blockers

- None. Image generation, alpha cleanup, and live DDS output all completed inside the allowed asset scope.
