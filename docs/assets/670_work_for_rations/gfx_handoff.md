# GFX handoff: Work for Rations report image

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_work_for_rations.dds`
- Exact sprite name: `GFX_report_event_fallout_work_for_rations`
- Target size: `210x176`
- Target `.gfx` file: `interface/fallout_world_end.gfx`
- Suggested sprite definition:

```text
spriteType = {
	name = "GFX_report_event_fallout_work_for_rations"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_work_for_rations.dds"
}
```

- Runtime owner: candidate 670, Work for Rations report-event picture
- Localisation key: not supplied by the parent asset request
- Wiring note: the parent implementation adds the sprite to `interface/fallout_world_end.gfx` and references it from candidate 670, while this package remains asset-owned.
- Visual notes: report-card processing follows the canonical report family with a sepia documentary tone, transparent corners, slight tilt, grain, and shadow. The source scene is a fictional Food Compact harvest crew in an ash-dark winter field with concrete agricultural infrastructure, sheltered machinery, ration ledger, and tokens.
- Review: `docs/assets/670_work_for_rations/contact_sheets/report_event_fallout_work_for_rations_decoded_review.png`
- Status: static `.gfx` registration and event reference complete. Live consumer rendering remains unproven because HOI4 is not run in this task.
