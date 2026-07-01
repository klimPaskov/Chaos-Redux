# Event 015 icon and animation handoff

Suggested `.gfx` target file: `interface/015_utopia_manifesto.gfx`

## Completed static sprites

### Idea sprites

All completed idea icons use the stable sprite pattern `GFX_<idea_id>` and final DDS files under `gfx/interface/ideas/015_utopia_manifesto/`.

- `GFX_idea_utopia_found_manifesto`
- `GFX_idea_utopia_unproven_common_stores`
- `GFX_idea_utopia_common_store_network`
- `GFX_idea_utopia_vocation_confusion`
- `GFX_idea_utopia_vocation_accord`
- `GFX_idea_utopia_compulsory_assignments`
- `GFX_idea_utopia_empty_stores`
- `GFX_idea_utopia_household_councils`
- `GFX_idea_utopia_storekeeper_commission`
- `GFX_idea_utopia_guild_congress`
- `GFX_idea_utopia_civic_wardens`
- `GFX_idea_utopia_marked_bounds_doctrine`
- `GFX_idea_utopia_utopian_league`
- `GFX_idea_utopia_foreign_laughter`
- `GFX_idea_utopia_feared_doctrine`

### Decision sprites

All completed decision icons use `GFX_<decision_id>` and final DDS files under `gfx/interface/decisions/015_utopia_manifesto/`.

- `GFX_decision_utopia_household_census`
- `GFX_decision_utopia_common_storehouse`
- `GFX_decision_utopia_storehouse_audit`
- `GFX_decision_utopia_open_stores`
- `GFX_decision_utopia_collect_petitions`
- `GFX_decision_utopia_fund_apprenticeships`
- `GFX_decision_utopia_urgent_service`
- `GFX_decision_utopia_rural_rotation`
- `GFX_decision_utopia_household_guard`
- `GFX_decision_utopia_guard_shore`

### Proposed focus sprites

These names are proposed because final focus ids were not supplied by the parent handoff. All DDS files live under `gfx/interface/goals/015_utopia_manifesto/`.

- `GFX_goal_utopia_found_manuscript`
- `GFX_goal_utopia_translate_old_hand`
- `GFX_goal_utopia_first_household_census`
- `GFX_goal_utopia_public_reading`
- `GFX_goal_utopia_storehouse_trial`
- `GFX_goal_utopia_useful_arts_register`
- `GFX_goal_utopia_question_of_boundaries`
- `GFX_goal_utopia_country_that_can_be_read`
- `GFX_goal_utopia_readers_assembly`
- `GFX_goal_utopia_storekeeper_opening`

## Completed animated sprite

- Static fallback sprite: `GFX_utopia_ledger_seal`
  - Final DDS path: `gfx/interface/utopia_manifesto/utopia_ledger_seal_static.dds`
- Animated sprite: `GFX_utopia_ledger_seal_animated`
  - Final DDS path: `gfx/interface/utopia_manifesto/utopia_ledger_seal_sheet.dds`
  - Frame count: `8`
  - Frame size: `64x64`
  - Sheet size: `512x64`
  - Animation rate: `8`
  - Looping: `yes`
  - `play_on_show`: `yes`
  - Preview GIF: `docs/assets/015_utopia_manifesto/animations/utopia_ledger_seal/previews/utopia_ledger_seal_preview.gif`
  - Contact sheet: `docs/assets/015_utopia_manifesto/animations/utopia_ledger_seal/previews/utopia_ledger_seal_contact.png`

Suggested `.gfx` snippet:

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_utopia_ledger_seal"
		texturefile = "gfx/interface/utopia_manifesto/utopia_ledger_seal_static.dds"
	}

	frameAnimatedSpriteType = {
		name = "GFX_utopia_ledger_seal_animated"
		texturefile = "gfx/interface/utopia_manifesto/utopia_ledger_seal_sheet.dds"
		noOfFrames = 8
		animation_rate_fps = 8
		looping = yes
		play_on_show = yes
	}
}
```

## Unfinished required deliverables

- Decision category icons are not generated yet.
- The remaining thirteen decision icons from the parent brief are not generated yet.
- The focus pack only covers ten proposed opening icons and is not yet broad enough for the final full tree.
- No achievement icons or their grey and not-eligible DDS triplets exist yet.
- Four requested animated assets are still missing:
  `utopia_overreach_warning`
  `utopia_storehouse_fill`
  `utopia_new_utopia_seal`
  `utopia_marked_bounds_seal`

## Validation

- Completed idea icons were exported at `64x64`.
- Completed decision icons were exported at `32x32`.
- Completed focus icons were exported at `94x86`.
- `utopia_ledger_seal_static.dds` is `64x64`.
- `utopia_ledger_seal_sheet.dds` is `512x64`, matching `8` frames at `64x64`.
