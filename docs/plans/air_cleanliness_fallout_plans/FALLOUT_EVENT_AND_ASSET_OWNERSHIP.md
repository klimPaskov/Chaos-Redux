# Fallout Event and Asset Ownership

## Canonical ownership

Fallout is an independent world-end system. It owns its event namespace, event file, scripted effects, scripted triggers, constants, GUI, GFX definitions, visual assets, audio assets, documentation, and manual-scenario sequencing.

Fallout does not borrow an event namespace, numbered event identity, event file, sprite path, portrait folder, icon folder, report image, sound wrapper, music track, or scripted localisation slot from another Chaos Redux feature.

## Event file

All internal Fallout orchestration events and post-consequence survivor story events belong in:

`events/fallout_world_end_events.txt`

The file uses:

`add_namespace = chaosx.fallout`

All Fallout sequencing events use `chaosx.fallout.*` identifiers. The exact numeric suffixes must be allocated inside this namespace after checking the completed file for duplicates. They are local event slots and are unrelated to the manual scenario registry id.

The dedicated file owns only the internal event callbacks and survivor-facing story chains needed by the consequence system:

- automatic contamination-collapse entry
- direct scripted terminal entry
- manual scenario launch handoff
- seven-day manual scenario completion event
- blackout phase advancement
- bounded state grading and rewrite continuation events
- successor assignment continuation events
- player continuation events
- post-transition orientation and regional aftermath events
- transition recovery events that belong to the Fallout system

The Fallout consequence itself is not an event. It has no public Event Details row, evolution entry, ordinary consequence Event Log entry, or ordinary super-event slot. The internal callbacks in this file are transport and presentation surfaces for the consequence, while survivor-country stories may write their own Fallout memory history after the transition.

## Event ownership boundaries

`events/chemical_warfare_events.txt` keeps chemical warfare and Air Contamination milestone events only. Remove the old Fallout event block from that file. Air Contamination requests the Fallout consequence through a dedicated scripted effect or an internal `chaosx.fallout.*` callback defined in the Fallout file.

`events/chaosx_triggerable_scenarios.txt` keeps generic scenario framework events only. A manual Fallout launch, when its native sweep gate is proven, may call the Fallout-owned handoff, but the consequence is never inserted into the public event, evolution, or Event Details catalogs.

No compatibility event remains in an older event namespace. Remove stale event definitions and migrate callers directly to the Fallout request helper. Save compatibility, if required, is handled by a versioned Fallout migration effect. It must not fire an event from another feature namespace.

## Script ownership

Use these dedicated system files unless local repository precedent proves a narrower layout:

- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_triggers/fallout_world_end_triggers.txt`
- `common/script_constants/fallout_world_end_constants.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/on_actions/fallout_world_end_on_actions.txt` only for narrowly scoped Fallout lifecycle hooks
- `common/scripted_guis/fallout_world_end_scripted_gui.txt`
- `common/scripted_localisation/fallout_world_end_scripted_localisation.txt`

Shared helpers may be called from existing global systems when they are genuinely shared. Fallout-owned state machines, cursors, migration, rewrite logic, and presentation remain in the Fallout files.

## GUI and GFX ownership

Use:

- `interface/fallout_world_end.gui`
- `interface/fallout_world_end.gfx`
- `gfx/interface/fallout_world_end/`

The blackout background, transition textures, processing indicators, successor-selection UI, warning states, and any animated transition elements use dedicated Fallout sprites and textures.

Fallout is not a normal super-event. It must not use a super-event image slot, super-event image path, super-event quote slot, super-event reaction slot, or super-event audio id. The blackout display text and transition sound are private presentation surfaces for the consequence and do not register a super-event.

## Visual asset ownership

Use dedicated system folders:

- `docs/assets/fallout_world_end/`
- `gfx/event_pictures/fallout_world_end/`
- `gfx/interface/fallout_world_end/`
- `gfx/interface/goals/fallout_world_end/`
- `gfx/interface/ideas/fallout_world_end/`
- `gfx/interface/decisions/fallout_world_end/`
- `gfx/leaders/fallout_world_end/`

Flags remain in the engine-required `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` roots. Their filenames must use the Fallout successor or cosmetic-tag identities. They must be newly sourced, newly generated, or deliberately reused from the same country's normal identity. They must not be copied from an unrelated feature package.

Report images, portraits, flags, icons, faction emblems, GUI panels, animated frames, and static fallbacks require Fallout-owned manifest entries and Fallout-owned final paths.

## Audio ownership

The blackout may use silence or a dedicated transition sound design. Any audio that is accepted belongs under:

- `sound/fallout_world_end/`
- `music/fallout_world_end/` only when actual music is approved for a non-super-event presentation role

Do not assign a normal super-event audio id. Do not reuse another feature's sound wrapper or final audio file.

## Manual scenario boundary

The manual scenario receives the next free scenario registry id found in the writable live repository. That registry id is independent from `chaosx.fallout.*` event suffixes.

The generic scenario launcher calls a Fallout-owned launch handoff only after the exact native sweep gate is proven. Every strike, countdown, blackout, rewrite, and post-transition callback after that call remains inside the Fallout namespace and file, without creating a public Fallout event row.

## Required cleanup

Before Fallout implementation begins:

1. Delete the old Fallout event definition from any non-Fallout event file.
2. Replace every caller with `fallout_request_aftermath` or the correct `chaosx.fallout.*` entry event.
3. Remove stale sprite definitions and asset paths that place Fallout art inside another feature folder.
4. Remove stale super-event image, text, quote, reaction, and audio wiring for Fallout.
5. Update documentation and catalogs to point to the dedicated Fallout file and asset package.
6. Confirm no Fallout event is defined outside `events/fallout_world_end_events.txt`.

## Validation gate

The ownership gate passes only when:

- every `chaosx.fallout.*` event definition is in `events/fallout_world_end_events.txt`
- no Fallout event block remains in chemical warfare, generic scenario, or other feature event files
- no Fallout caller uses an event id from another namespace
- the consequence itself has no public Event Details, evolution, or ordinary Event Log registration
- no Fallout sprite or texture points into another feature asset folder
- no Fallout presentation uses the normal super-event system
- the asset manifest lists only dedicated Fallout paths or engine-required flag roots
- the manual scenario registry id was allocated from the live registry and is not confused with event suffix numbering
