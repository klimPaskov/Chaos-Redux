# GFX handoff — Work for Rations report image

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_work_for_rations.dds`
- Exact sprite name: `GFX_report_event_fallout_work_for_rations`
- Target size: `210x176`
- Suggested target `.gfx` file: the existing event-picture sprite registry selected by the main agent; the parent request did not identify a registry filename
- Suggested sprite definition:

```text
spriteType = {
	name = "GFX_report_event_fallout_work_for_rations"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_work_for_rations.dds"
}
```

- Runtime owner: candidate 670, Work for Rations report-event picture
- Localisation key: not supplied by the parent asset request
- Wiring note: add the sprite to the existing event-picture `.gfx` registry and reference it from the candidate 670 event implementation; this package intentionally does not edit `.gfx`, events, localisation, GUI, or gameplay files.
- Visual notes: report-card processing follows the canonical report family with a sepia documentary tone, transparent corners, slight tilt, grain, and shadow. The source scene is a fictional Food Compact harvest crew in an ash-dark winter field with concrete agricultural infrastructure, sheltered machinery, ration ledger, and tokens.
- Review: `docs/assets/670_work_for_rations/contact_sheets/report_event_fallout_work_for_rations_decoded_review.png`
- Status: handed off; `.gfx` registration remains parent-owned.

