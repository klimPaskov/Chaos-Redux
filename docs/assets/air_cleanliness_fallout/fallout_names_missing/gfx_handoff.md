# GFX handoff — Names for the Missing

- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds`
- Proposed sprite name: `GFX_report_event_fallout_names_missing`
- Target `.gfx`: the existing Chaos Redux report-event sprite registry; the parent request did not name a registry filename, so the main agent should confirm the established file before wiring.
- Target size: `210x176`
- Use: fictional report-event picture for the dormant global-survival “Names for the Missing” chain (suffixes `269`–`281`), with no Zombie ids or assets.
- Source mode: generated fictional/symbolic scene; no real identifiable person or historical archive item is depicted.
- Visual read: cold concrete shelter, wall ledger of intentionally illegible family marks, one non-identifiable volunteer archivist under low electric light, frost and paper bundles, sepia documentary print treatment.
- Text safety: no readable names, letters, numbers, captions, logos, signs, watermarks, or UI artifacts.
- Runtime QA: DDS is 210×176, one-level uncompressed BGRA, 128-byte header, exact length 147,968 bytes, alpha range 0–255, transparent corners.
- SHA-256: source `c3e201ef51fc063a2a9eb0c1ea67218d057ab23269e1f05bccc898d8dd08d0b2`; processed `197aa312dda055835cf8682c3fa5d9a5b677fde8f7fc9e24e045342d673e7355`; DDS `f723b1ecbad5537085381ac97fcf47453137888e1743fd6592475d0ab9a1c2f5`.

Suggested sprite snippet for the main agent to adapt to the established report-event `.gfx` file:

```text
spriteType = {
	name = "GFX_report_event_fallout_names_missing"
	texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_names_missing.dds"
}
```
