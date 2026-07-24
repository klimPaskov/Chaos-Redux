# Event 016 Kruger portrait and severe-animation parent review

## Review identity

- Date: 2026-07-24
- Mode: parent asset and wiring review
- Scope: Warren Kruger stage progression, route-specific static portraits, advisor crops, Stage IV frame animation, and Directorate static fallback behavior
- Skills applied: `chaos-redux-event-assets` and `chaos-redux-frame-animation`

## Accepted runtime package

The fixed Stage 0 portrait remains the copied `portrait_generic_biowarfare_europe_male_01` identity registered as:

- `GFX_portrait_KRG_doctor_warren_kruger_stage_0`
- `GFX_idea_doctor_warren_kruger_stage_0`

The staged generated package adds:

- Stage I and Stage II leader portraits and advisor crops;
- six Stage III route outputs: clone, machine, temporal, xenobiological, alien-revealed, and synthesis;
- the same six Stage IV static outputs;
- six real Stage IV frame-animation outputs.

The six visual outputs satisfy the five required severe families because the xenobiological-or-alien family has two mutually exclusive evidence-gated conclusions rather than collapsing them into one visual.

There are 15 final `156x210` leader DDS files including Stage 0 and 15 final `65x67` advisor DDS files including Stage 0.

## Animation packages

| Route output | Frames | Runtime sheet | Static fallback |
| --- | ---: | --- | --- |
| Clone | 10 | `gfx/interface/leader_frames/016_brilliant_scientist/doctor_warren_kruger_stage_4_clone_sheet.dds` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_clone.dds` |
| Machine | 10 | `gfx/interface/leader_frames/016_brilliant_scientist/doctor_warren_kruger_stage_4_machine_sheet.dds` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_machine.dds` |
| Temporal | 12 | `gfx/interface/leader_frames/016_brilliant_scientist/doctor_warren_kruger_stage_4_temporal_sheet.dds` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_temporal.dds` |
| Xenobiological | 10 | `gfx/interface/leader_frames/016_brilliant_scientist/doctor_warren_kruger_stage_4_xenobiological_sheet.dds` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_xenobiological.dds` |
| Alien-revealed | 10 | `gfx/interface/leader_frames/016_brilliant_scientist/doctor_warren_kruger_stage_4_alien_revealed_sheet.dds` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_alien_revealed.dds` |
| Synthesis | 12 | `gfx/interface/leader_frames/016_brilliant_scientist/doctor_warren_kruger_stage_4_synthesis_sheet.dds` | `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_synthesis.dds` |

Every animation frame is `156x210`.

Ten-frame sheets are `1560x210` and twelve-frame sheets are `1872x210`.

The package record is `docs/assets/016_brilliant_scientist/package_records/portrait_animation_package.json`.

## Visual review

All six contact sheets were reviewed at original resolution:

- clone frames change the number, position, gesture, and apparent disposition of replicated Krugers;
- machine frames progress through distinct implant, prosthetic, apparatus, and command poses;
- temporal frames use separate clock, map, assistant, chamber, and continuity scenes;
- xenobiological frames use separate specimens, tools, containers, growth states, and handling poses;
- alien-revealed frames change anatomy, instruments, apparatus, and presentation while retaining Warren Kruger’s core identity;
- synthesis frames combine separate clone, biological, mechanical, temporal, and mixed-project scenes.

The loops are not transform-only, filter-only, or derived by moving one still.

Each route has separately created source frames, processed frames, a horizontal DDS sheet, a static fallback, a preview GIF, and a contact sheet.

## Wiring review

`interface/016_brilliant_scientist.gfx` registers all six Stage IV `frameAnimatedSpriteType` sheets with their final frame counts and timing.

`common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` selects the matching animated sprite only when all of these are true:

- the current portrait stage is Stage IV;
- the matching evidence-gated route flag is active;
- the player has not disabled Directorate animations.

The same selector immediately falls through to the matching static Stage IV leader sprite when animations are disabled.

Stage III, Stage II, Stage I, and Stage 0 remain static.

`common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` applies that selector to the custom Directorate portrait and exposes the animation toggle.

`common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` updates the same fixed `KRG_warren_kruger` character portrait for native leader, advisor, and scientist-facing static surfaces.

## Technical evidence

The package-record validation found:

- 20 package records: 14 generated static leaders and six animated routes;
- every recorded processed image, runtime DDS, preview, contact sheet, and static fallback present;
- every DDS dimension equal to its recorded contract;
- every recorded DDS SHA-256 equal to the current runtime file;
- every source-frame and processed-frame count equal to the registered frame count;
- no duplicate source-frame byte hashes within any route;
- all 15 leader DDS files at `156x210`;
- all 15 advisor DDS files at `65x67`.

## Remaining integration boundary

Native advisor and special-project scientist tiles use the static portrait selected on the fixed character because those native surfaces do not consume the custom Directorate frame animation.

This is the required static fallback behavior, not a substitute for the severe animation package: the real frame animation is visible in the event-owned Directorate surface.

The current asset manifest still contains pre-production status prose and must be reconciled after the report, super-event, achievement, focus, and Directorate UI tranches finish so concurrent asset work does not overwrite this review.

No fallback, placeholder, or transform-only animation was accepted in this tranche.
