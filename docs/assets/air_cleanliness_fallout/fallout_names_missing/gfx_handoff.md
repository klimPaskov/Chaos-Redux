# GFX handoff - Names for the Missing

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds`
- Proposed sprite name: `GFX_report_event_fallout_names_missing`
- Target `.gfx`: `interface/fallout_world_end.gfx`. The sprite is wired as `GFX_report_event_fallout_names_missing`.
- Target size: `210x176`
- Use: fictional report-event picture for the dormant global-survival "Names for the Missing" chain (suffixes `269` to `281`), with no Zombie ids or assets.
- Source mode: generated fictional or symbolic scene. No real identifiable person or historical archive item is depicted.
- Visual read: cold concrete shelter, wall ledger of intentionally illegible family marks, one non-identifiable volunteer archivist under low electric light, frost and paper bundles, sepia documentary print treatment.
- Text safety: no readable names, letters, numbers, captions, logos, signs, watermarks, or UI artifacts.
- Runtime QA: DDS is 210x176, one-level uncompressed BGRA, 128-byte header, exact length 147,968 bytes, alpha range 0 to 255, transparent corners.
- SHA-256 source: `c3e201ef51fc063a2a9eb0c1ea67218d057ab23269e1f05bccc898d8dd08d0b2`. Processed: `d277dc7d831c10e73ab18f3274d03b577c04a2e9a50f42668a520993be9dfd2d`. DDS: `baeec9bd25a6c582b5094b949bdd87eb095c4869a9b6558c6e4d242f825a4bc0`.

Runtime sprite registration:

```text
spriteType = {
	name = "GFX_report_event_fallout_names_missing"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds"
}
```

- Runtime consumers: visible opening event `chaosx.fallout.269`, visible result events `chaosx.fallout.271` through `chaosx.fallout.274`, and visible callback `chaosx.fallout.279`. Hidden AI results, the hidden AI callback, and cleanup intentionally use no picture.
