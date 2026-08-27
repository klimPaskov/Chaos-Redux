# Event20 generated visual-asset handoff

Status: complete for the requested non-icon stills. Main agent owns `.gfx` edits and gameplay wiring; this package does not modify `.gfx`, events, localisation, flags, portraits, ideas, or decisions.

## Runtime assets

| Sprite name | Final DDS | Target `.gfx` | Size | Use |
| --- | --- | --- | --- | --- |
| `GFX_report_event_020_black_plague_unbound` | `gfx/event_pictures/020_black_plague/report_event_020_black_plague_unbound.dds` | `interface/020_black_plague_event_pictures.gfx` | 210x176 | Report-event image for `chaosx.nr020.1` / Black Plague Unbound |
| `GFX_super_event_085_rat_king_coronation` | `gfx/super_events/020_black_plague/super_event_085_rat_king_coronation.dds` | `interface/020_black_plague_super_events.gfx` | 457x328 | Super-event ID 85, Rat King coronation |
| `GFX_super_event_086_rat_king_takeover` | `gfx/super_events/020_black_plague/super_event_086_rat_king_takeover.dds` | `interface/020_black_plague_super_events.gfx` | 457x328 | Super-event ID 86, terminal Rat King takeover |

Ready-to-copy sprite snippets:

```text
spriteType = { name = "GFX_report_event_020_black_plague_unbound" texturefile = "gfx/event_pictures/020_black_plague/report_event_020_black_plague_unbound.dds" }
spriteType = { name = "GFX_super_event_085_rat_king_coronation" texturefile = "gfx/super_events/020_black_plague/super_event_085_rat_king_coronation.dds" }
spriteType = { name = "GFX_super_event_086_rat_king_takeover" texturefile = "gfx/super_events/020_black_plague/super_event_086_rat_king_takeover.dds" }
```

## Evidence and provenance

- Generated source PNGs: `gfx/source/event20/source_png/report_event_020_black_plague_unbound_source.png`, `super_event_085_rat_king_coronation_source.png`, and `super_event_086_rat_king_takeover_source.png`.
- Processed previews: `gfx/source/event20/processed_png/`.
- Contact sheet: `gfx/source/event20/contact_sheets/event20_black_plague_contact_sheet.png`.
- Prompt record and source-mode rationale: `gfx/source/event20/prompts/event20_prompts.md`.
- Full manifest and DDS header evidence: `gfx/source/event20/manifest.md`.

## Remaining gaps

- Custom Event20 flags, Rat King leader/commander/operative portraits, idea or national-spirit icons, focus icons, and decision icons are not part of this non-icon handoff. If gameplay references any of these, route them to the icon artist or source researcher with explicit asset rows.
- Main agent must add the sprites to the correct existing/new `.gfx` files and connect event/super-event consumers. No `.gfx` file was edited here.
