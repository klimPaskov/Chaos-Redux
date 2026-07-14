# Event 016 GFX handoff

Date: 2026-07-14

## Opening appointment report card

- Final DDS: `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds`
- Exact proposed sprite: `GFX_report_event_016_brilliant_scientist_appointment`
- Target GFX file: `interface/016_brilliant_scientist.gfx`
- Target events: `chaosx.nr16.2` and `chaosx.nr16.3`
- Target size: `210x176`
- Asset status: `handed_off`
- Naming or placement uncertainty: none

Ready-to-copy sprite definition:

```text
spriteType = {
	name = "GFX_report_event_016_brilliant_scientist_appointment"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_appointment.dds"
}
```

After registering the sprite, use this event-picture reference in both visible opening appointment events:

```text
picture = GFX_report_event_016_brilliant_scientist_appointment
```

Both events currently point directly at `GFX_portrait_KRG_doctor_warren_kruger_stage_0`. Replacing those two picture references with the report sprite gives the opening a dedicated sepia dossier or report-card presentation while preserving the approved Stage-0 identity. The persistent character portrait sprites remain unchanged.

## Review evidence

- Source: `docs/assets/016_brilliant_scientist/source_png/report_events/report_event_016_brilliant_scientist_appointment_source.png`
- Processed preview: `docs/assets/016_brilliant_scientist/processed_png/report_events/report_event_016_brilliant_scientist_appointment.png`
- Contact sheet: `docs/assets/016_brilliant_scientist/contact_sheets/report_event_016_brilliant_scientist_appointment_contact_sheet.png`
- The processed PNG and decoded DDS are pixel-identical.
- The DDS is a one-level legacy uncompressed `210x176` BGRA texture with real `0..255` alpha and fully transparent corners and outer edges.

No `.gfx`, event, localisation, gameplay, GUI, spreadsheet, or later-stage art file was edited in this asset tranche.
