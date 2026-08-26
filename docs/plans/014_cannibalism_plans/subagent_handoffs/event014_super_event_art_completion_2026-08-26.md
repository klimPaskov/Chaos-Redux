# Event 014 super-event art completion handoff

Status: complete for the four requested Event 014 super-event image assets.

Scope was limited to the super-event art refresh package, its temporary manifest/handoff, the four final DDS files, and verification of the existing shared super-event registry. No gameplay, localization, GUI, focus, decision, portrait, 3D, audio, or spreadsheet files were changed.

## Completed assets

| Super-event | Sprite | Final DDS | Source master | Processed preview |
| --- | --- | --- | --- | --- |
| Cannibalism public reveal | `GFX_super_event_cannibalism_reveal` | `gfx/super_events/014_cannibalism/super_event_cannibalism_reveal.dds` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/source_png/current/super_event_cannibalism_reveal.png` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/processed_png/super_event_cannibalism_reveal.png` |
| Ordinary cannibal world end | `GFX_super_event_cannibalism_world_end_ordinary` | `gfx/super_events/014_cannibalism/super_event_cannibalism_world_end_ordinary.dds` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/source_png/current/super_event_cannibalism_world_end_ordinary.png` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/processed_png/super_event_cannibalism_world_end_ordinary.png` |
| Wendigo world end | `GFX_super_event_cannibalism_world_end_wendigo` | `gfx/super_events/014_cannibalism/super_event_cannibalism_world_end_wendigo.dds` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/source_png/current/super_event_cannibalism_world_end_wendigo.png` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/processed_png/super_event_cannibalism_world_end_wendigo.png` |
| Cannibalism global defeat | `GFX_super_event_cannibalism_global_defeat` | `gfx/super_events/014_cannibalism/super_event_cannibalism_global_defeat.dds` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/source_png/current/super_event_cannibalism_global_defeat.png` | `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/processed_png/super_event_cannibalism_global_defeat.png` |

The four source masters are independent native ImageGen outputs, each `1536x1024` RGB. They are visually distinct and action-led: civic-square pursuit, rail-bridge exodus, alpine Wendigo chase, and harbor evacuation/counterassault. They contain no readable text, watermarks, UI elements, portraits, default imagery, or reused prior stills. The old duplicate two-file source cache at `source_png/` root was removed; the unrelated report/news source masters in `source_png/current/` were left untouched.

## Generation and processing evidence

Native ImageGen run records:

- Reveal: `C:\Users\klimp\.codex\generated_images\01a03d29-2f8c-7133-ad6c-4629b1ab333a\exec-131f6bfc-215b-4bca-881a-3315ff460d5e.png`.
- Ordinary world end: `C:\Users\klimp\.codex\generated_images\01a03d29-2f8c-7133-ad6c-4629b1ab333a\exec-16570f4a-f88b-4dc7-9b47-c83b9f2a0f99.png`.
- Wendigo world end: `C:\Users\klimp\.codex\generated_images\01a03d29-2f8c-7133-ad6c-4629b1ab333a\exec-7980cd39-9bc2-4c58-aaa0-f6f9f172dcdc.png`.
- Global defeat: `C:\Users\klimp\.codex\generated_images\01a03d29-2f8c-7133-ad6c-4629b1ab333a\exec-9cee5a59-4f6d-4e3a-8582-d43a64c8342b.png`.

Processing was mechanical only: center crop the `1536x1024` masters to the `457x328` consumer aspect, then LANCZOS resize to `457x328` RGBA PNG. All four are opaque (`alpha_min=255`, `alpha_max=255`) because the inspected super-event family is full-canvas scene art.

| Asset | Source SHA-256 | Processed SHA-256 | DDS SHA-256 |
| --- | --- | --- | --- |
| `super_event_cannibalism_reveal` | `1A5C80E88044BF9C0A5AAF83D324DC6CA70C1700418CD13007E6F595B236EFAB` | `A62759BC0796C6A8F3864ADDD525B3FC9D79C756161700524A335B2084250C1F` | `50B4F7A95818845BEDE3892A6545FC428277C9482349A80E1F7D37C6AB606E38` |
| `super_event_cannibalism_world_end_ordinary` | `A2A8C1A326F2C7248559578E6CDD62205DD8B6C112DB32EF2D8A3354D9DF2EC4` | `1A56CC3AC33E47FF8DDF7DCA79F0DEB41765058D383459618FBE0D4269472FE9` | `CF5173A65873CFDD548E6B5C3334C1013572C5C3BC725EE81EDFD481E5551CA8` |
| `super_event_cannibalism_world_end_wendigo` | `BE75143BE413787EBF5E4D12D86FF00DF00FDAB7CB6606840261E94F6DC0759D` | `3B1F73096380A8B388A2EF49F23DDF4A4E7E8CDB48AA1C38A0ADF03A2B315E36` | `597C31EF0E1726402FC157A27E89F6D202341B9FB7B6583FEB7FFC8E62170FE1` |
| `super_event_cannibalism_global_defeat` | `C5D77F159CDE5438BA40873AA565D8E12D9D6887B82BCE7CE37959E010AA7C34` | `13CD38BE3CB22D75503770C685189E9FC6610976D324B243E49921D72B447C65` | `CF57406A51693FFC07363027337B65B331FF403876BD5CA3A5A336B05796571E` |

## Runtime registration and validation

`interface/chaosx_super_events.gfx` already contains the four stable sprite definitions and points to the four final DDS paths above. No registry mutation was needed.

Every DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and passed strict header and round-trip checks: `DDS ` magic; `DDS_HEADER` size `124`; declared `457x328`; `DDS_PIXELFORMAT` size `32`, flags `65`, fourCC `0`, bit count `32`; BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`; texture caps `0x1000`; exact one-level length `599712` bytes; alpha bytes `255..255`; and byte-exact BGRA-to-RGBA round-trip against each processed PNG.

Review sheet: `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/contact_sheets/super_events_contact_sheet.png`.

Package manifest and sprite handoff: `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/manifest.md` and `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/gfx_handoff.md`.

## Blockers and remaining review

No asset is blocked or `needs_user_review`. The parent agent should force-add the ignored `docs/assets/014_cannibalism/event_art_refresh_2026-08-25/` manifest, source, preview, and contact-sheet evidence if those temporary files are to remain in Git; `docs/assets/` is ignored by repository policy. The four final DDS files are tracked runtime changes. Event 014 report/news art was outside this specific four-super-event refresh and remains untouched.
