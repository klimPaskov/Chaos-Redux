# Produce Event 84's complete asset package

Event: 84, The Peace Movement.
Slug: `the_peace_movement`.
Source package: `docs/specs/084_the_peace_movement_specs/`.
Read Part 13, the [asset register](084_the_peace_movement_asset_register.md), the [four 3D model briefs](084_the_peace_movement_3d_model_briefs.md), the achievement matrix, the super-event research, and Part 6 for country identities.
Then read `CLAUDE.md` and the current `chaos-redux-event-assets`, `chaos-redux-3d-model-pipeline`, `chaos-redux-super-events`, and `chaos-redux-subagents` skills.

Route work through `chaos-redux-subagents` with self-contained prompts that carry every path, constraint, allowed write, and acceptance question.
The parent owns non-portrait sprite and gameplay wiring; the portrait creator owns portrait-specific wiring.
An art assignment does not edit events, GUI, localisation, focuses, decisions, history, country files, or the catalog workbook unless explicitly granted.

## Scope

The asset register is the complete list: 16 report scene families, 10 news scenes, four super-event scenes, the static category-picture states, 15 spirit-state icons across three families, 71 focus icons, 35 decision and automatic-mission icons, verified technology and unit-consumer icons, 16 achievements in three states, the country-by-identity flag and portrait matrix, and four unit model, counter, and sound packages.
Inspect the canonical [reference README](../../../.claude/skills/chaos-redux-event-assets/assets/gfx_references/README.md), its catalog and contact sheets, and the actual consumer before each final export.

## Rules that shape this event

- Generate fictional and alternate-history scenes rather than presenting them as archival photographs; source real historical material only with attributed provenance.
- Public queer culture is civic and visible without sexualized bodies.
  Private cases concern adults and stay non-explicit.
- The fictional Lotus order is not a depiction of Hinduism or Buddhism as a whole.
- Every new flag goes through image generation; historical flags first need a cited flat reference.
  Constitutional identities need all three flag sizes and every supported ideology and name consumer.
  Unchanged flags stay unchanged.
- Each asset role gets its own composition; one icon is never resized across focus, idea, decision, achievement, technology, or counter roles.
- Alpha-backed families request native transparency and preserve it through conversion; background removal is fallback only.
- Grounded portraits are sourced placeholders until the user supplies the final HOI4-style version; agents never operate RunPod.
  Fictional adult officials may be generated.
  Never invent a real person's orientation for a case.
- The four firearm units follow the 3D briefs and the owner skill.
  Licensed modern concept references for body and gun generation are the first production gate.
- Audio is licensed and sourced only.
  Unit voices follow country-tag routing.
  Super-event audio belongs to the super-event audio researcher.
- Achievement states come from the canonical template and overlay with their bytes preserved.

## Handoff

Keep event-scoped working evidence under `docs/assets/084_the_peace_movement/` and durable portrait masters under `docs/assets/portraits/084_the_peace_movement/`.
Deliver a manifest mapping each design ID and identity to source mode, license, native dimensions, processing, hash, runtime output, consumer, and status, plus native-size contact sheets, DDS round-trip proof, model and action evidence, sound provenance, and `gfx_handoff.md`.
Blocked portraits, references, country variants, recordings, and animations stay explicitly blocked.
