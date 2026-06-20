# Event 012 Africa Goal And Idea Icon Alpha Audit Handoff

- Date: `2026-06-20`
- Scope: live Event 012 Africa `goal_*` focus icons and live Event 012 Africa `idea_*` idea or national-spirit icons
- Requested correction applied: audit for opaque white backgrounds, white halos, fake checkerboard, opaque unused canvas, and focus-to-idea asset reuse

## Files changed

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_goal_idea_alpha_audit_handoff.md`

## Live files audited

### Focus or goal icons

- `gfx/interface/goals/012_africa/goal_africa_archive_old_seats.dds`
- `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds`
- `gfx/interface/goals/012_africa/goal_africa_charter_league_diplomacy.dds`
- `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds`
- `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds`
- `gfx/interface/goals/012_africa/goal_africa_industry_logistics.dds`
- `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds`
- `gfx/interface/goals/012_africa/goal_africa_military_forces.dds`
- `gfx/interface/goals/012_africa/goal_africa_political_congress.dds`
- `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds`
- `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds`
- `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds`
- `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds`

### Idea or national-spirit icons

- `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds`
- `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds`
- `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds`
- `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds`
- `gfx/interface/ideas/012_africa/idea_africa_is_one.dds`
- `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds`
- `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds`
- `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds`
- `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds`

## Supporting files reviewed

- `interface/012_africa.gfx`
- `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v4_2026_06_19/manifest.md`
- `docs/assets/012_africa/icon_regen_goal_icons_no_white_bg_v4_2026_06_19/gfx_handoff.md`
- `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v4_2026_06_19/manifest.md`
- `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v4_2026_06_19/gfx_handoff.md`
- `.agents/skills/chaos-redux-event-assets/assets/focuses/focus_reference_contact.png`
- `.agents/skills/chaos-redux-event-assets/assets/ideas/`

## Validation method

- Decoded every live `.dds` file to RGBA and checked:
  - exact dimensions
  - alpha presence
  - transparent corner pixels
  - non-transparent bounding box
  - bright semi-transparent fringe pixels
  - bright opaque border pixels
- Visually reviewed the live goal and idea contact sheets over checker backgrounds.
- Compared live idea icons against the live goal set for composition reuse risk.

## Validation results

### Focus or goal icons

- All 13 live goal icons decode to `94x86`.
- All 13 have transparent corners: `(0, 0, 0, 0)` in all four corners.
- All 13 have non-full-canvas alpha bounds, so none contain an opaque square background.
- Bright semi-transparent fringe hits: `0` on all 13 files.
- Bright opaque border hits: `0` on all 13 files.
- Result: no live Event 012 goal icon currently fails the white-background or white-halo check.

### Idea or national-spirit icons

- All 9 live idea icons decode to `64x64`.
- All 9 have transparent corners: `(0, 0, 0, 0)` in all four corners.
- All 9 have non-full-canvas alpha bounds, so none contain an opaque square background.
- Bright semi-transparent fringe hits: `0` on all 9 files.
- Bright opaque border hits: `0` on all 9 files.
- Result: no live Event 012 idea or national-spirit icon currently fails the white-background or white-halo check.

### Idea distinctness from goals

- The live idea set reads as separate 64x64 spirit art rather than reduced focus art.
- Thematic pairs use different framing and different symbol treatment.
- A rough full-set similarity sweep did not produce any close goal-match result that would indicate simple resizing or cropping.
- Result: the live idea icons pass the distinct-asset requirement.

## Regeneration or reprocessing outcome

No live Event 012 Africa focus or idea icon required regeneration or reprocessing in this pass.

I did not replace any live DDS, source PNG, processed PNG, manifest entry, or `gfx_handoff.md` mapping because the currently wired assets already satisfy the requested alpha and distinctness constraints.

## Sprite and path status

- No filename changes required.
- No sprite-name changes required.
- No `.gfx` updates required.
- `interface/012_africa.gfx` already points to the correct live DDS paths for all audited `goal_*` and `idea_*` assets.

## Minor review note

- `goal_africa_sponsor_paths.dds` contains one bright opaque highlight pixel inside the painted subject, not on the border and not in unused canvas. This is not a white-background failure and did not justify replacement.

## Remaining risks

- None for the specific user correction about opaque white backgrounds and focus-to-idea reuse.
- Older historical asset-package folders under `docs/assets/012_africa/` may still contain superseded intermediate files, but the live wired DDS set in `gfx/interface/goals/012_africa/` and `gfx/interface/ideas/012_africa/` is clean.

## Blocked assets

None
