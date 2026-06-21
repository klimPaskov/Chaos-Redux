# 012 Africa Asset QA Handoff

Date: 2026-06-21
Scope: achievement DDS triplets listed in the attachment, 8 Death focus icons, listed Soviet Collapse focus icons, and 7 Africa regional leader portraits.
Changed files: this handoff only.

## Reference inspection used

- `/.agents/skills/chaos-redux-event-assets/assets/achievements`
- `/.agents/skills/chaos-redux-event-assets/assets/focuses`

## Death focus icons

Status: `pending fresh-package audit`

Per updated instruction, I did not treat the current live Death icons or `docs/assets/010_death/focus_icon_regen_white_artifact_2026_06_21/` as satisfying the request.

Current QA stance:

- Do not pass the live 8 Death focus icons yet.
- Do not use the excluded white-artifact regen package as completion evidence.
- No new fresh package was present under `docs/assets/010_death/` during this audit beyond the older/excluded regeneration folders, so there was nothing new to approve.

## Achievement DDS triplets

Status: `pass`

Checked set size:

- 46 achievement families
- 138 DDS files total

Results:

- Every scoped achievement file exists.
- Every scoped achievement variant is exactly `64x64`.
- Every scoped achievement family has a complete `base + grey + not_eligible` triplet.
- The current regenerated set broadly matches HOI4 achievement presentation better than the old non-style-compliant direction: framed medal/seal compositions, readable central subjects, and correct grey/not-eligible treatment.

No concrete localized DDS defect in the scoped achievement set was clear enough to patch safely without design ambiguity, so no art files were modified.

## Soviet Collapse focus icons

Status: `fail`

Checked set size:

- 43 scoped focus icons

Results:

- Every scoped Soviet Collapse focus icon exists.
- Every scoped Soviet Collapse focus icon is exactly `94x86`.
- The family is closer to HOI4 focus-icon composition than the earlier broken batch, but several live DDS files still contain visible mint crop/guide marks near the edges. Those marks are visible in rendered previews and should be treated as blocking defects.

Blocking files with visible guide-mark artifacts:

- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_common_steppe_passports.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_kyrgyz_mountain_liaisons.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_league_cavalry_school.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_deputies_seats.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_republics_do_not_kneel.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_republics_write_together.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_southern_shield.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_steppe_defense_council.dds`
- `gfx/interface/goals/soviet_collapse/kaz_soviet_collapse_tajik_pass_agreements.dds`

Those files should be regenerated or reprocessed from clean source art. I did not patch them because the issue is part of the source/export treatment across multiple icons, not a single unambiguous one-pixel fix.

## Africa regional leader portraits

Status: `pass`

Checked set size:

- 7 scoped portraits

Results:

- Every scoped portrait exists.
- Every scoped portrait is exactly `156x210`.
- All 7 current portraits read as male-presenting in the rendered DDS output.

Scoped portraits checked:

- `gfx/leaders/012_africa/leader_012_africa_cbc_congo_basin_charter.dds`
- `gfx/leaders/012_africa/leader_012_africa_glk_great_lakes_council.dds`
- `gfx/leaders/012_africa/leader_012_africa_ioc_indian_ocean_congress.dds`
- `gfx/leaders/012_africa/leader_012_africa_mag_maghreb_coast.dds`
- `gfx/leaders/012_africa/leader_012_africa_sah_sahel_caravan.dds`
- `gfx/leaders/012_africa/leader_012_africa_slc_south_african_liberation_congress.dds`
- `gfx/leaders/012_africa/leader_012_africa_zsc_zambezi_stone_cities.dds`

## Remaining risks

- The Death focus icon request remains unresolved until a fresh package appears under `docs/assets/010_death/` and the live DDS replacements are updated from that package.
- The 9 Soviet Collapse icons listed above should not be treated as QA-complete while the mint guide marks remain in the final DDS output.
