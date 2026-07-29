# Mengele super-event acceptance criteria

## Scope

These criteria apply to the Angel Directorate reveal super-event and any later world-order super-event that belongs to the live Mengele path.

## Slot and trigger

- The super-event has a verified slot number.
- The event script sets the correct super-event visibility flag.
- The event script sets `global.current_super_event_audio_id` to the correct audio id in the same effect chain or in the established playback helper path.
- Playback uses the existing settings-aware super-event playback helper.
- The reveal fires once and cannot duplicate after save reload, retaking states, repeat coup checks, or repeated focus completion.
- The trigger is a meaningful campaign threshold, not a loose placeholder. Valid thresholds include coup outbreak, Directorate consolidation, emergency laboratory revolt, or final world-order launch depending on repository design.
- The reveal super-event and the world-order super-event use separate identities if both are live.

## Localisation

- Required keys exist for `.t`, `.d`, `.a`, and `.q`.
- Title direction is short, specific, and tied to the Directorate moment.
- Description direction explains public consequence without overexplaining hidden mechanics.
- Button text is final and sourced if it uses a cultural reference.
- Quote is real, sourced, traceable, attributed, and short enough for the UI.
- No invented quote, unsourced quote-site copy, long modern copyrighted line, or hidden-route spoiler is used.
- Wording does not celebrate atrocity, use gore for shock, or frame perpetrators heroically.

## Image

- `GFX_super_event_angel_directorate` points to the final intended DDS.
- `gfx/super_events/003_holy_realm/super_event_angel_directorate.dds` is not default art unless the implementation agent documents that the default was intentionally replaced upstream with final art.
- Image source mode is documented. Use sourced archival material only when it depicts real historical material. Use generated art only for symbolic or fictional presentation that does not claim to depict real victims, real experiments, or a real person's likeness.
- Final art has source PNG or source file, processed preview, final DDS, manifest entry, and GFX handoff.
- Image composition is readable at 457x328.

## Audio

- Final WAV exists at the documented path or at a verified repo path.
- OGG is 44.1 kHz and game-ready.
- Source file is preserved in an asset documentation area.
- Track title, creator, performer or recording source, source URL, license, usage terms, duration, conversion notes, and uncertainty are documented.
- Composition rights and recording rights are considered separately.
- Sound definitions point to the correct final file.
- No placeholder, mismatched, undocumented, or wrong-format audio remains.

## Documentation and spreadsheet

- Event docs describe when the super-event fires, what it means, which image and audio it uses, and where source documentation lives.
- Audio docs list the super-event id and track.
- Asset manifest lists the final image.
- Spreadsheet-facing fields are updated only after the final in-game wording exists.

## Test proof

- Force or play into the super-event trigger and record that it appears.
- Confirm image, text, quote, button, and audio in the super-event UI.
- Trigger the threshold twice and record duplicate prevention.
- Save and reload near the threshold if practical.
- Verify a disabled super-event setting does not play audio or display incorrectly if the setting exists.
