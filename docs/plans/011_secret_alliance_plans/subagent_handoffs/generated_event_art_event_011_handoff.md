# Generated Event Art Handoff: Event 011 Secret Alliance

Subagent: `chaosx_generated_event_art`
Event id: `011`
Event slug: `secret_alliance`
Scope: generated non-icon visual assets only
Source method: official built-in `image_gen` for all source artwork, then local crop/style processing and `.tools/convert_to_dds.py` DDS conversion

No `.gfx`, gameplay, localisation, GUI, focus, idea, decision, event, script, history, country, or spreadsheet files were edited.

## Package Files

- Manifest: `docs/assets/011_secret_alliance/manifest.md`
- GFX handoff: `docs/assets/011_secret_alliance/gfx_handoff.md`
- Prompt record: `docs/assets/011_secret_alliance/prompts/secret_alliance_generated_non_icon_prompts.md`
- Contact sheet: `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_generated_non_icon_contact_sheet.png`
- Source PNG folder: `docs/assets/011_secret_alliance/source_png/`
- Processed PNG folder: `docs/assets/011_secret_alliance/processed_png/`
- Package DDS copy folder: `docs/assets/011_secret_alliance/dds/`

## Missing or Inferred Inputs

- At asset-generation time, the worker did not find the short relative path `matrices/011_secret_alliance_asset_matrix.md`. The source matrix exists in the accepted spec package at `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_asset_matrix.md`.
- Dossier Board background size inferred as `520x236` from the Event 010 Black Atlas background.
- Pact emblem size inferred as `128x128` transparent UI seal.

Current disposition as of the final documentation pass:
- The missing-matrix note is historical path evidence, not a current blocker.
- The generated package, current Event 011 documentation, and asset handoffs keep stable sprite names and runtime DDS paths for the dossier background and pact emblem.

## Created Assets

| Sprite name | Asset | Dimensions | Source PNG | Processed PNG | Runtime DDS | Status |
|---|---|---:|---|---|---|---|
| `GFX_super_event_secret_alliance_reveal` | reveal super-event image | `457x328` | `docs/assets/011_secret_alliance/source_png/super_event_secret_alliance_reveal_source.png` | `docs/assets/011_secret_alliance/processed_png/super_event_secret_alliance_reveal.png` | `gfx/super_events/011_secret_alliance/super_event_secret_alliance_reveal.dds` | complete |
| `GFX_report_event_secret_alliance_meeting` | suspicious meeting report image | `210x176` | `docs/assets/011_secret_alliance/source_png/report_event_secret_alliance_meeting_source.png` | `docs/assets/011_secret_alliance/processed_png/report_event_secret_alliance_meeting.png` | `gfx/event_pictures/011_secret_alliance/report_event_secret_alliance_meeting.dds` | complete |
| `GFX_report_event_secret_alliance_sabotage` | sabotage aftermath report image | `210x176` | `docs/assets/011_secret_alliance/source_png/report_event_secret_alliance_sabotage_source.png` | `docs/assets/011_secret_alliance/processed_png/report_event_secret_alliance_sabotage.png` | `gfx/event_pictures/011_secret_alliance/report_event_secret_alliance_sabotage.dds` | complete |
| `GFX_report_event_secret_alliance_protocol` | exposed protocol report image | `210x176` | `docs/assets/011_secret_alliance/source_png/report_event_secret_alliance_protocol_source.png` | `docs/assets/011_secret_alliance/processed_png/report_event_secret_alliance_protocol.png` | `gfx/event_pictures/011_secret_alliance/report_event_secret_alliance_protocol.dds` | complete |
| `GFX_secret_alliance_dossier_bg` | Dossier Board background | `520x236` | `docs/assets/011_secret_alliance/source_png/secret_alliance_dossier_bg_source.png` | `docs/assets/011_secret_alliance/processed_png/secret_alliance_dossier_bg.png` | `gfx/interface/secret_alliance/secret_alliance_dossier_bg.dds` | complete, size inferred |
| `GFX_secret_alliance_pact_emblem` | faction/UI pact emblem | `128x128` | `docs/assets/011_secret_alliance/source_png/secret_alliance_pact_emblem_source.png` | `docs/assets/011_secret_alliance/processed_png/secret_alliance_pact_emblem.png` | `gfx/interface/secret_alliance/secret_alliance_pact_emblem.dds` | complete, size inferred |

## Suggested Wiring

Suggested target `.gfx` file: `interface/011_secret_alliance.gfx`, matching the event-scoped pattern used by `interface/014_cannibalism.gfx`. If the main implementation already has a central super-event sprite file, keep `GFX_super_event_secret_alliance_reveal` stable and move only that definition to the central file.

Ready-to-copy sprite definitions are in `docs/assets/011_secret_alliance/gfx_handoff.md`.

## Validation

- Runtime DDS files exist and open at the expected dimensions.
- Package DDS copies exist under `docs/assets/011_secret_alliance/dds/`.
- Report processed PNGs are `210x176` RGBA with transparent corner alpha.
- Pact emblem processed PNG is `128x128` RGBA with transparent corner alpha.
- Visual contact sheet reviewed for composition and generated-text risk.

## Remaining Risks

- Historical size-inference risk: the two UI sizes were inferred before final dossier GUI wiring. Current documentation keeps those sprite names and runtime paths stable; no remaining documentation blocker is attached to this note.
- No `.gfx` wiring was performed in this sidecar scope.
