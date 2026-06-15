# Generated Event Art Handoff - Event 010 Death super-event audit

Date: `2026-06-15`
Scope: audit Death super-event image assets and produce missing final art only if a wired slot was missing or placeholder-quality

## Files changed

- `docs/assets/010_death/contact_sheets/death_super_events_contact.png`
- `docs/assets/010_death/generated_art_manifest.md`
- `docs/assets/010_death/generated_art_gfx_handoff.md`
- `docs/assets/010_death/prompts/generated_art_prompts.md`

## Active super-event roles audited

- `super_event_death_reveal`
- `super_event_death_world_end`
- `super_event_death_defeat_aftermath`
- `super_event_death_world_consumed`
- `super_event_death_black_oath`

## Wiring evidence reviewed

- `interface/chaosx_super_events.gfx`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/script_constants/010_death_constants.txt`
- `common/scripted_effects/010_death_effects.txt`
- `docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md`
- `docs/super_events/010_death_super_event_text_research.md`
- `docs/super_events/010_death_super_event_black_oath_research.md`

## Audit result

- Exactly five active Death super-event image slots are currently wired.
- No separate `Dark Methods` super-event image slot is active in the current Death constants or super-event scripted localisation.
- All five active slots already had final-source art, processed PNGs, and DDS exports present.
- Visual review against the project super-event reference folder found no asset that read as a placeholder or mockup, so no regeneration was performed.

## Source mode and prompt record

- Source mode remained `generated` for all five Death super-event images because Death is fictional, supernatural, and alternate-history.
- Prompt record was updated to include the previously missing `super_event_death_black_oath` prompt note in `docs/assets/010_death/prompts/generated_art_prompts.md`.

## Final dimensions and existence checks

- Verified source PNG presence:
  - `docs/assets/010_death/source_png/super_event_death_reveal_source.png`
  - `docs/assets/010_death/source_png/super_event_death_world_end_source.png`
  - `docs/assets/010_death/source_png/super_event_death_defeat_aftermath_source.png`
  - `docs/assets/010_death/source_png/super_event_death_world_consumed_source.png`
  - `docs/assets/010_death/source_png/super_event_death_black_oath_source.png`
- Verified processed PNG presence and target size `457x328`:
  - `docs/assets/010_death/processed_png/super_event_death_reveal.png`
  - `docs/assets/010_death/processed_png/super_event_death_world_end.png`
  - `docs/assets/010_death/processed_png/super_event_death_defeat_aftermath.png`
  - `docs/assets/010_death/processed_png/super_event_death_world_consumed.png`
  - `docs/assets/010_death/processed_png/super_event_death_black_oath.png`
- Verified final DDS presence and target size `457x328`:
  - `gfx/super_events/super_event_death_reveal.dds`
  - `gfx/super_events/super_event_death_world_end.dds`
  - `gfx/super_events/super_event_death_defeat_aftermath.dds`
  - `gfx/super_events/super_event_death_world_consumed.dds`
  - `gfx/super_events/super_event_death_black_oath.dds`

## Validation run

- Used `identify` to confirm all five processed PNGs and all five final DDS files are `457x328`.
- Used visual review of the processed PNGs plus the new `docs/assets/010_death/contact_sheets/death_super_events_contact.png` contact sheet to confirm the active set is coherent and readable at super-event size.

## Remaining blockers or follow-up

- No asset blocker remains for the current five wired Death super-event roles.
- If the parent later wires a distinct `Dark Methods` super-event, that would require a new source PNG, processed PNG, DDS, manifest entry, and handoff update rather than reuse of the existing Black Oath art.
