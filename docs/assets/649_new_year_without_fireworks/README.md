# 649 The New Year Without Fireworks asset package

This temporary package contains the generated source and processed evidence for the static Fallout report image used by the East Asia year-turning report, “The New Year Without Fireworks.” The scene is fictional and non-identifying: a cold ash-darkened East Asian community with covered lamps, a ration table, memorial ribbons, civilians, and unmarked guards beneath an empty sky.

The runtime DDS is [report_event_fallout_new_year_without_fireworks.dds](../../../gfx/event_pictures/fallout_world_end/report_event_fallout_new_year_without_fireworks.dds) and the proposed sprite is `GFX_report_event_fallout_new_year_without_fireworks`. The main agent owns `.gfx` wiring and should use the handoff in [gfx_handoff.md](gfx_handoff.md).

Source mode is `$imagegen` because this is a fictional alternate-history report scene with no real person, place, archive item, or historical event to source. The generated source is retained in `source_png/`. Deterministic HOI4 report-card processing is retained in `processed_png/`. The report-card processor supplies the required sepia, grain, tilt, border, shadow, and transparent corners.

Only one final alternative was generated, so a contact sheet is not required for this single-asset package. No animation, audio, readable text, flags, religious markers, modern branding, zombie imagery, or real identities are present.

This is active evidence while the event remains in implementation. Before final event completion, copy durable provenance and wiring facts into permanent event documentation and remove this temporary `docs/assets/649_new_year_without_fireworks/` workspace as required by the event-assets skill.
