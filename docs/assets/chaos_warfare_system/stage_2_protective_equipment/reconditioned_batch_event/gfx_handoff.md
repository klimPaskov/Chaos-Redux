# GFX handoff — cbrn_protection.2 defective reconditioned batch

- Event id: `cbrn_protection.2`
- Asset type: report-event picture
- Final DDS: `gfx/event_pictures/cbrn/report_event_cbrn_defective_reconditioned_batch.dds`
- Intended sprite id: `GFX_report_event_cbrn_defective_reconditioned_batch`
- Registered target `.gfx`: `interface/cbrn_protection.gfx`
- Texture path for the sprite: `gfx/event_pictures/cbrn/report_event_cbrn_defective_reconditioned_batch.dds`
- Dimensions: `210x176`
- Format: uncompressed 32-bit RGBA/BGRA-style DDS, alpha pixels retained, `8` mip levels
- Visual notes: true report-event card, not an icon; the source is a grounded fictional 1936–1945 documentary inspection photograph. The local report processor supplies the slight positive tilt, sepia tone, paper edge, transparent corners, grain, and soft shadow.
- Readability notes: the foreground cracked seal and degraded filter are the focal defects; respirator rows and crates establish the defective batch without readable labels or national insignia.

Registered sprite declaration:

```text
spriteType = {
	name = "GFX_report_event_cbrn_defective_reconditioned_batch"
	texturefile = "gfx/event_pictures/cbrn/report_event_cbrn_defective_reconditioned_batch.dds"
}
```

The asset worker changed no localisation, GUI, event, gameplay, or `.gfx` files. The main implementation has completed sprite registration and event wiring; no blocker or fallback remains for this asset.
