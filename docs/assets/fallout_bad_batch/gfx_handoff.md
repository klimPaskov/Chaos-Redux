# GFX handoff for Fallout Bad Batch report art

Asset: `report_event_fallout_bad_batch`

Final DDS:

`gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds`

Proposed sprite name:

`GFX_report_event_fallout_bad_batch`

Target size: 210x176

Asset use: global event report card showing fictional altered ecology after fallout

Suggested target GFX file: use the existing event-picture sprite definition file already used by the parent implementation. The exact current filename was not supplied to this asset worker, so the parent should resolve it before wiring.

Ready-to-copy sprite definition shape:

```text
spriteType = {
    name = "GFX_report_event_fallout_bad_batch"
    texturefile = "gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds"
}
```

The texture is already in the event-scoped runtime folder. Do not point the runtime sprite at `docs/assets/`.

The source image is an original imagegen scene. The processed PNG has transparent corners and the standard tilted documentary card treatment. No real person, real flag, readable text, logo, or watermark is present.

Parent wiring tasks:

- confirm the existing event-picture `.gfx` file
- keep the sprite name stable
- bind the sprite to the Fallout Bad Batch global report event
- add or verify the related localisation key in parent scope

Status: handed_off. Final art and DDS conversion are complete. GFX and gameplay edits remain outside this asset worker scope.
