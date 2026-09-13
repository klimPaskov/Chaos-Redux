# Event 067 Generalissimo Super-Event Prompt

Research and complete the two Event `067` super-event packages. Follow the source specification and do not write or wire unsourced final material.

## Required sources

Read:

- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_6_scenario_and_world_end.md`
- `docs/specs/067_generalissimo_specs/specs/067_generalissimo_spec_part_8_presentation_assets_localisation.md`
- `docs/specs/067_generalissimo_specs/prompts/067_generalissimo_asset_prompt.md`
- `AGENTS.md`
- `chaos-redux-super-events`
- `chaos-redux-event-assets`
- `chaos-redux-events`
- `chaos-redux-subagents`

Use `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher` with complete context-free prompts. Use `chaosx_generated_event_art` for the two fictional super-event images through the asset package.

## Super-event 1: Generalissimo becomes ruler

### Role

A major political transformation after either:

- peaceful submission to the final ultimatum
- junta victory and national reunification

The civil-war start does not use this super-event.

### Final text direction

Research or write a short specific title about military command becoming state authority. It must fit both peaceful submission and civil-war victory.

The description should show:

- ministries and armed forces answering to one command
- the Generalissimo becoming head of state
- the host country dynamically
- the survival or subordination of old institutions
- public and officer reaction

Do not list traits, modifiers, focus routes, or hidden variables.

### Quote research

Find several sourced candidates concerning:

- armies and political power
- command and obedience
- rule by soldiers
- civil authority under military pressure
- personal command

Prefer public-domain, historical, political, philosophical, military, or literary sources. Verify wording, author, work, date where known, and attribution confidence.

Do not invent a quote. Do not use a long modern copyrighted line.

### Button or cultural remark research

Find a short sourced or defensibly paraphrased reaction with one of these directions:

- cold staff language
- old military idiom
- restrained literary allusion
- severe understatement

Document the source and whether the wording is a quote, fragment, title reference, or paraphrase.

### Image

Use `generalissimo_super_event_rule` from the asset package.

The image must be host-neutral, period-authentic, fictional, and centered on command becoming government.

### Audio

Find one unique licensed musical recording.

Tone:

- military
- processional
- severe
- structured with clear musical structure

Requirements:

- composition and recording rights checked separately
- legitimate source
- creator or composer
- performer or recording source where relevant
- license and usage terms
- source URL
- duration
- attribution
- final edited duration between one and two minutes unless a documented exception is approved
- preserved original source file during active work
- final game-ready WAV

Reject drones, sound effects, beeps, generated tones, noise beds, placeholder tracks, undocumented repository audio, and another super-event's track.

## Super-event 2: The Generalissimos' World

### Role

Public Event 067 world-end launch at 1000 or higher Chaos.

### Title

The accepted scenario name, The Generalissimos' World, is the primary title candidate. Confirm that it fits the final super-event slot and localisation layout. Do not replace it casually.

### Description direction

Show:

- military establishments replacing or subordinating governments
- peaceful coups and split-command wars
- aligned juntas
- rival generalissimos
- civilian defiance and resistance
- the original Generalissimo as a major center

Do not claim that he already controls the whole world.

### Quote research

Find several sourced candidates concerning:

- military rule
- civil authority
- armies and politics
- men on horseback
- command by force
- fear of military government

Verify exact wording and attribution. Prefer a source that fits a world divided among competing military orders.

### Button or cultural remark research

Find a short sourced allusion about soldiers governing, command, or civil authority. Keep modern copyrighted material very short.

### Image

Use `generalissimo_super_event_world` from the asset package.

The composition should show several regions and competing military centers. Maps can appear only as secondary material.

### Audio

Find a second unique licensed musical recording.

Tone:

- international scale
- military or choral structure
- broad conflict
- final world-order shift

It cannot reuse the first track or another super-event track without explicit user approval.

## Wiring requirements

For each super-event:

- select an intentional slot
- add image sprite wiring
- add title, description, button, and quote localisation
- add scripted localisation getters
- add a unique base sound definition
- add every settings-volume wrapper required by the current helper
- set the unique audio ID
- set `global.current_super_event_audio_id`
- call `play_current_super_event_sound = yes`
- wire the exact event trigger
- prevent repeated playback
- update Event 067 documentation
- update `music/chaosx_music_track_list.html`
- align the authoritative workbook where relevant

## Research note

Create or update a permanent Event 067 super-event research note with:

- role
- final title
- final description direction and approved text
- button or cultural remark and source
- quote candidates
- selected quote
- exact source and confidence
- image runtime path and source manifest replacement note
- audio candidates
- selected track
- title, creator, performer, source, license, terms, duration, attribution, original path, final WAV path, sound IDs, volume wrappers, edit steps, and uncertainties

## Completion blockers

Treat these as blockers:

- no defensible quote
- uncertain attribution
- no licensed musical recording
- unclear recording rights
- missing image
- reused default audio
- wrong slot
- missing volume wrappers
- missing music catalog row
- mismatch between text, image, audio, and trigger

Do not ship temporary or guessed final text, quote, remark, image, or audio.
