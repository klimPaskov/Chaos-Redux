# Event 049 Doomsday Super-Event Research and Production Prompt

## Role

Create the complete research and implementation handoff for the two Event 049 super-events using `chaos-redux-super-events`, `chaos-redux-event-assets`, and the relevant narrow research subagents.

Read:

- `specs/049_doomsday_spec_part_1_core.md`
- `specs/049_doomsday_spec_part_8_final_vigil.md`
- `specs/049_doomsday_spec_part_11_presentation_and_assets.md`
- `research/049_doomsday_research_notes.md`
- `research/049_doomsday_bibliography.md`
- `prompts/049_doomsday_asset_prompt.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-super-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents`.

## Required packages

### Package A: Initial Major event reveal

Role:

First global revelation that unrelated prophecies, calculations, dreams, traditions, and movements are converging on one period and one leading date.

The super-event must communicate:

- The prediction is socially real even though its cause is unproven.
- A date two to four years away has become public.
- War, investment, education, recruitment, and long-term planning are already weakening.
- The event concerns mass public behavior and institutions, not one scientist or prophet.

Title direction:

Research a short final title specific to global convergence, the shared date, or the loss of ordinary future planning. The final title can be Event 049’s name if that is strongest after comparison. Do not accept a generic apocalypse title.

Description direction:

Write concise final super-event prose about unrelated systems reaching the same conclusion, immediate public response, and unresolved cause. Do not expose hidden mechanics or claim that Earth will physically end.

Button or cultural remark direction:

Research a short, fitting reaction. It may be restrained, resigned, religious, literary, bitter, or quietly ironic. Modern copyrighted material must remain a very short fragment, title-like reference, or paraphrased allusion.

Quote direction:

Find several reliably sourced candidates about prophecy, time, expectation, judgment, false certainty, or the social consequences of believing an end is near.

Prefer public-domain, historical, religious, philosophical, or literary sources. Do not invent, paraphrase while presenting as direct quotation, or use uncertain internet quote collections as final authority.

Image direction:

Coordinate `doomsday_opening_super_event` with the asset package. The scene should show a broad public gathering, calendars or notices with unreadable print, altered daily life, prayer or civic assembly, and social diversity. Avoid a laboratory, a confirmed comet, a single prophet, modern objects, and physical planetary destruction.

Audio direction:

Research a unique structured musical recording with restraint, expectation, public ritual, or gathering tension. It must have clear rights for mod use. Pure ambience, drones, one-shot sound effects, generated tones, and unlicensed commercial recordings are forbidden.

### Package B: The Final Vigil

Role:

World-end commitment after enough governments and movements transfer political purpose to Doomsday administrations and the Final Assembly.

The super-event must communicate:

- Conventional geopolitics has lost its social foundation.
- Armies demobilize or fragment.
- Long military production and construction stop.
- The Final Assembly organizes food, shelter, peace, records, and public order.
- Earth has not visibly been destroyed.

Title direction:

The accepted route name is **The Final Vigil**. Verify whether it remains the strongest final super-event title after research and UI review. Any alternative must remain aligned with Event Details and the world-end registry.

Description direction:

Write concise final prose about mass political surrender of future ambition, the founding of the Final Assembly, demobilization, and custodial life until the predicted date.

Button or cultural remark direction:

Research a short reaction with finality and human scale. Avoid generic lines about the end beginning or darkness falling.

Quote direction:

Find several reliably sourced candidates about watchfulness, final judgment, peace, the passing of worldly power, time, or the end of ambition.

Image direction:

Coordinate `doomsday_final_vigil_super_event` with the asset package. Show a large human assembly, relief distribution, stored or surrendered weapons, extinguished military activity, shelters, and a shared vigil. Avoid an exploding Earth, supernatural beams, and generic maps.

Audio direction:

Research a unique licensed structured musical recording with public ritual, finality, and human scale. It must be distinct from the opening track unless the user explicitly approves exact reuse.

## Text research requirements

Use `chaosx_super_event_text_researcher` for each package with an isolated, self-contained prompt.

For each super-event, return:

- At least five title candidates where title research is useful.
- At least five main quote candidates.
- At least three button or cultural remark candidates.
- Exact wording and source verification.
- Author or speaker.
- Source work, speech, scripture, poem, or document.
- Date or period where known.
- Source URL.
- Attribution confidence.
- Public-domain or copyright notes.
- Why the candidate fits this exact role.
- A clear recommendation with rejected alternatives.

Do not select a final quote with uncertain attribution when a stronger verified candidate exists.

Respect quotation limits and UI space. Keep direct modern copyrighted wording very short.

## Audio research requirements

Use `chaosx_super_event_audio_researcher` for each package with an isolated, self-contained prompt.

For each super-event, research several candidates and document:

- Title.
- Composer or creator.
- Performer or recording source where relevant.
- Source URL.
- Composition rights.
- Recording rights.
- License and usage terms.
- Duration.
- Attribution requirement.
- Why the track fits the role and pacing.
- Editing and conversion plan.
- Suitability and uncertainty.

Prefer tracks between one and two minutes. A longer source can be edited to a final cue of two minutes or less when the license permits it and the edit is documented.

Reject unclear licensing, unlicensed YouTube uploads, commercial soundtrack recordings without permission, generated music, test tones, drones, and effects-only cues.

Preserve source audio and produce a game-ready WAV only after source and license approval.

## Image coordination

The image producer follows `prompts/049_doomsday_asset_prompt.md`.

The super-event handoff must record:

- Final image basename.
- Final DDS path.
- Sprite name or proposed stable name.
- Source mode.
- Manifest or permanent provenance path.
- Review result against the super-event text and audio role.

Text, image, and audio must describe the same campaign moment.

## Runtime handoff requirements

The parent implementation agent owns final wiring.

Provide:

- Proposed or confirmed super-event slot for each package.
- Final title, description, button, and quote keys.
- Final text after source review.
- Image sprite and path.
- Unique audio ID.
- Base sound definition ID.
- Required settings-volume soundeffect wrapper IDs.
- Final WAV path under `sound/049_doomsday/`.
- The value to use for `global.current_super_event_audio_id`.
- Confirmation that playback uses `play_current_super_event_sound = yes`.
- Required `GetSuperEventImage` and scripted localisation updates.
- Event trigger or effect that calls the super-event.
- Event Details and world-end alignment notes.

## Documentation

Create or update a permanent research note under:

```text
docs/super_events/049_doomsday_super_event_research.md
```

Record source, rights, final text, quote, image, audio, conversion, identifiers, paths, and remaining uncertainty.

Update `music/chaosx_music_track_list.html` with one row per unique final track and the correct super-event ID.

## Completion rules

Do not claim either super-event complete unless:

- Final sourced text exists.
- Quote attribution is verified.
- Button or cultural reference is sourced where applicable.
- Final image exists and is wired.
- Final unique licensed WAV exists.
- Base sound and volume wrappers are wired.
- Settings-aware playback is used.
- Scripted localisation selects the correct image and text.
- Event trigger and world-end state are correct.
- Documentation and music catalog are aligned.
- No placeholder or default asset remains.
