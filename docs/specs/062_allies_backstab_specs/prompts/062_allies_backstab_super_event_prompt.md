# Event 062 conditional super-event prompt

Create and implement the one-time Evolution III super-event for Chaos Redux Event 62, Allies Backstab.

Read:

- `docs/specs/062_allies_backstab_specs/specs/062_allies_backstab_spec_part_5_evolutions.md`
- `docs/specs/062_allies_backstab_specs/specs/062_allies_backstab_spec_part_7_ai_achievements_presentation.md`
- `docs/specs/062_allies_backstab_specs/quality/062_allies_backstab_chaos_impact_map.md`
- `docs/specs/062_allies_backstab_specs/quality/062_allies_backstab_acceptance_scenarios.md`
- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-super-events`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

## Role

The super-event marks a proven world-order fracture caused by simultaneous collapse of several major alliances. It is an escalation and world-order announcement. It is not a world-end scenario.

It must not fire for a normal Event 62 purge or one internal faction war.

## Trigger proof

Evolution III must be enabled. The super-event is fire-once per campaign. Fire it when one accepted proof is met:

- three factions with at least eight political units each suffer full internal bloc wars and at least twelve political units change side or withdraw
- two major-led factions split and at least eight countries enter new Event 62 linked wars
- one faction with at least twenty political units breaks into three viable camps and at least ten units leave the original leader

Store the proof before showing the super-event. A save and reload cannot fire it twice.

## Text research

Spawn `chaosx_super_event_text_researcher` with no inherited context.

Research several verified quote candidates about betrayal, broken oaths, divided alliances, civil conflict, or political trust. Prefer public-domain literature, historical speeches, political writing, scripture, or another traceable source.

The researcher must provide:

- exact quote
- author or speaker
- source work or speech
- date when known
- reliable source link
- attribution confidence
- public-domain or copyright note
- why it fits this exact super-event

Do not invent or misattribute a quote.

Research a short reaction or cultural remark separately. Keep modern copyrighted material very short and sourced. Final wording must fit the current super-event UI.

## Writing direction

Title direction: short, specific, and about the collapse of alliance order. Avoid generic titles about the end, flames, darkness, or the world changing forever.

Description direction: describe several alliance headquarters closing, members changing sides, military commands splitting, and existing fronts becoming uncertain. Name the scope of the collapse without exposing numeric trigger conditions.

Reaction direction: controlled disbelief, bitter recognition of political betrayal, or a verified short allusion. Avoid a plain `OK` response.

The final text must follow Chaos Redux event writing rules. Do not use em dashes, semicolons, staccato fragments, contrast templates, or process wording.

## Image

Use the generated super-event image from the Event 62 asset handoff.

Expected direction:

- `457x328` after exact consumer inspection
- period-authentic documentary or alternate-history press scene
- several delegations or military groups separating into armed camps
- visible institutional collapse
- no modern equipment
- no readable generated text
- no map as the main subject

## Audio research

Spawn `chaosx_super_event_audio_researcher` with no inherited context.

Select one unique musical recording with clear rights. Prefer a structured chant, hymn, orchestral work, march, or other music that fits division and political collapse. Do not use a drone, test tone, sound effect, oscillator, noise bed, placeholder, or another super-event's track.

The audio handoff must include:

- title
- composer or creator
- performer or recording source
- source URL
- composition rights
- recording rights
- license and confidence
- duration
- original download path and checksum
- edit and conversion steps
- final game-ready WAV
- attribution text

Target final duration is one to two minutes unless a documented exception is approved.

## Wiring

The parent implementation agent owns:

- intentional super-event slot
- visibility flag
- image sprite and scripted localisation
- title, description, reaction, and quote localisation
- unique audio ID
- base sound definition
- settings-volume wrappers
- `global.current_super_event_audio_id`
- `play_current_super_event_sound = yes`
- trigger proof and one-time receipt
- Event 62 documentation
- music catalog row
- event catalog alignment

The super-event may apply the distinct one-time `+5` Chaos source only after the shared-source overlap audit approves it.

## Validation

Verify:

- near-miss generations do not show the super-event
- qualifying generation shows it once
- save and reload does not repeat it
- image, text, quote, and audio use the same slot
- settings-aware volume works
- no raw localisation key or clipping appears
- music catalog identifies the actual source and Event 62 use
- no placeholder asset or audio remains
