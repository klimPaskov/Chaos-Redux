# Event 016 opening report asset handoff

Date: 2026-07-14

Parent integration status: resolved. `interface/016_brilliant_scientist.gfx` registers `GFX_report_event_016_brilliant_scientist_appointment`, and `chaosx.nr16.2` plus `chaosx.nr16.3` use it.

## Scope

This bounded asset tranche completes one static opening report picture for Event 016. It uses only the approved Stage-0 Doctor Warren Kruger identity, applies the repository report-card treatment, produces a runtime BGRA DDS, records the sprite contract, and leaves all source wiring to the parent.

No image generation was run. No Stage I or later portrait source was opened, processed, copied, or created. No `.gfx`, event, localisation, gameplay, GUI, spreadsheet, or Git commit operation was performed.

## Files created or updated

Created:

- `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_appointment.png`
- `docs/assets/016_brilliant_scientist/contact_sheets/report_event_016_brilliant_scientist_appointment_contact_sheet.png`
- `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds`
- `docs/assets/016_brilliant_scientist/gfx_handoff.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_opening_report_asset_handoff.md`

Updated:

- `docs/assets/016_brilliant_scientist/manifest.md`

Verified and preserved without modification:

- `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_appointment_source.png`
- `docs/assets/016_brilliant_scientist/source_png/portraits/portrait_generic_biowarfare_europe_male_01_decoded.png`
- `docs/assets/016_brilliant_scientist/source_png/portraits/generated_static/leader_doctor_warren_kruger_stage_1_source.png`

The Stage I path is listed only to make the non-touch boundary explicit.

## Stable identifier and parent wiring

- Exact proposed sprite: `GFX_report_event_016_brilliant_scientist_appointment`
- Final texture: `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds`
- Target registration file: `interface/016_brilliant_scientist.gfx`
- Target event picture references: `chaosx.nr16.2` and `chaosx.nr16.3`

The two visible opening events currently use the raw Stage-0 portrait sprite. Parent wiring should register the proposed report sprite and replace those two `picture` values. It should not rename or replace the persistent Stage-0 character portrait sprites.

## Before and after

Before this tranche, the recovered source was intact but had no processed report card, runtime DDS, contact sheet, manifest entry, or sprite handoff. The visible events therefore continued to present the raw character portrait.

After this tranche, the parent has a complete `210x176` sepia dossier or report-card asset with subtle tilt, paper edge, grain, soft shadow, transparent corners, exact runtime path, and stable sprite recommendation. The asset is not presented as wired because the parent-owned source references remain unchanged.

## Source-to-output chain

1. Approved Stage-0 reference: `portrait_generic_biowarfare_europe_male_01_decoded.png`, `156x210` RGBA.
2. Recovered report source: `report_event_016_brilliant_scientist_appointment_source.png`, `206x164` RGBA, SHA-256 `33C8ADD65AFB63DD6CD7E995E1C1DF05A2AD264B9D4F2802C8AB77DF8FF29D4D`.
3. Identity check: source pixels `x=25..180`, `y=0..163` are exactly identical to Stage-0 reference pixels `x=0..155`, `y=0..163`. The source adds only symmetric 25-pixel blue-grey margins.
4. Standard report-card processing: `192x153` card on a transparent `210x176` canvas, 2-pixel paper border, 3-degree tilt, soft shadow, sepia monochrome, and deterministic grain seed `1616`.
5. Processed preview: SHA-256 `716CEC05CDD2F66E4FA96D61261857AD9676AAAED115E28D1411C3E3CFFAF03E`.
6. Runtime DDS: SHA-256 `5DFD9CC830A650271D7C66A3501E51F027ED160935151FB0153C8C1FDBB65B5B`.

## Meaningful validation

- The processed PNG and DDS are exactly `210x176`.
- The processed alpha range is `0..255`; all four corner pixels and every pixel on the four outer edges have zero alpha. The non-zero alpha bounding box is `(5, 6, 209, 174)`, so the tilted card and shadow are not hard-clipped.
- The DDS is exactly `147968` bytes, which is the 128-byte legacy header plus `210 * 176 * 4` payload bytes.
- Header inspection confirms `DDS ` magic, header size `124`, pitch `840`, pixel-format size `32`, flags `65`, 32-bit BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`, and `DDSCAPS_TEXTURE` at byte 108.
- The DDS payload is byte-identical to the processed PNG converted to BGRA order. Pillow decodes the DDS successfully and produces RGBA pixels exactly identical to the processed PNG.
- The contact sheet shows the approved source, processed RGBA card over a checker background, and decoded DDS together. It has SHA-256 `B3FB28D7A90738845EA074BB09099EAE6DEC056D8B6D60F67F1C98D2A3FFB9D7`.
- The final presentation was visually inspected at original resolution. Kruger's Stage-0 face remains clear and unchanged, the tilt is subtle, the border reads as paper rather than a thick frame, and the transparent corners remain visible.

The repository-standard `.tools/convert_to_dds.py` selected its built-in FFmpeg raw-BGRA backend because texconv was not present. This is the same standard one-level BGRA writer already used for the Event 016 Stage-0 advisor asset. It produced the skill-mandated header and a pixel-exact round trip; it is a conversion backend, not a substitute visual asset.

## Safety and boundaries

The change is safe and bounded because it adds one event-scoped texture and documentation without altering any live script reference. Existing Stage-0 portrait outputs, Stage I source art, later sprite contracts, gameplay state, and localisation remain untouched.

## Remaining parent work

- Reconcile the opening-report status in any broader Event 016 completion audit after wiring.
- Preserve the existing licensing note: internal Event 016 use is approved, while external redistribution rights for the Stage-0 source remain unresolved.

## Simplifications, omissions, and blockers

No content simplification, placeholder, alternate identity, or fallback art was used. The only incomplete part of this bounded tranche is parent-owned sprite and event wiring, intentionally excluded by the assignment. Broader Event 016 report, news, super-event, icon, flag, UI, Stage I through IV, and animation packages remain outside this tranche and retain their existing manifest status.
