---
name: chaos-redux-super-events
description: Use when designing, researching, wiring, or documenting Chaos Redux super-events.
---

# Chaos Redux Super Events

Use this skill when a Chaos Redux task creates, updates, researches, or wires a super-event.

This skill covers super-event presentation, localisation, quote selection, audio research, image handoff, implementation wiring, and documentation.

General event implementation belongs to `chaos-redux-events`.

Visual asset sourcing and processing belongs to `chaos-redux-event-assets`.

## 1. Core purpose

A Chaos Redux super-event is a major presentation moment.

It should mark a major event, major escalation, defeat aftermath, or world-end scenario that deserves stronger treatment than a normal popup.

A super-event package must keep these parts aligned:

- super-event slot
- title localisation
- description localisation
- button text localisation
- quote localisation
- image
- audio id
- final sound file
- audio documentation
- event trigger or effect wiring
- settings-aware sound playback
- event docs
- spreadsheet entry if relevant

Do not wire only one part of a super-event. The image, text, quote, audio, event effect, docs, and spreadsheet must agree.

## 2. When to use this skill

Use this skill for:

- major-event super-events
- evolved minor events that become major enough for super-event treatment
- world-end scenario super-events
- defeat aftermath super-events
- major faction or world-order announcements
- global threat escalation
- large event chain milestones
- super-event quote research
- super-event audio research
- super-event audio documentation
- super-event localisation updates
- super-event image handoff to `chaos-redux-event-assets`

Do not use a super-event for every dramatic event. Use it when the campaign moment should feel larger than a normal popup.

## 3. Relationship with other skills

### `chaos-redux-events`

Use `chaos-redux-events` for the full implementation contract:

- event script
- event registration
- event log
- evolutions
- world-end logic
- docs
- spreadsheet updates
- full event system wiring

### `chaos-redux-event-assets`

Use `chaos-redux-event-assets` for:

- super-event image sourcing or generation
- image processing
- PNG previews
- DDS conversion
- sprite handoff notes for main-agent `.gfx` wiring
- asset manifests

Super-event images may be sourced or generated. Prefer generated images for fictional, alternate-history, symbolic, supernatural, high-chaos, or emotionally specific moments. use sourced images when the visual must depict real historical material.

### This skill

This skill owns:

- super-event presentation design
- localisation structure
- quote selection and verification
- audio research and licensing checks
- audio documentation
- super-event package checklist

### Custom research subagent split

For actual research work, use the narrow project subagents instead of making one agent research everything at once.

| Need | Spawn |
| --- | --- |
| Main quote candidates, wording verification, attribution, source confidence, and quote recommendation | `chaosx_super_event_quote_researcher` |
| Button text, cultural remark, short allusion, slogan, title-like reference, and copyright-risk notes | `chaosx_super_event_cultural_remark_researcher` |
| Audio candidates, license verification, legitimate download, conversion to a game-ready `.wav`, and audio research notes | `chaosx_super_event_audio_researcher` |
| Real historical, archival, or real-world super-event image that must depict real material | `chaosx_asset_source_researcher` |
| Fictional, alternate-history, symbolic, supernatural, high-chaos, or emotionally specific generated super-event image | `chaosx_generated_event_art` |

The main agent owns final localisation, scripted localisation, slot wiring, settings-aware sound playback wiring, audio id wiring, sound definition wiring, `.gfx` image wiring, event trigger wiring, docs alignment, and spreadsheet alignment. When spreadsheet alignment is needed, edit only the authoritative XLSX and then run `python .tools/export_event_catalog_csv.py`; never edit the three CSV exports directly.

The quote, remark, audio, and image subagents produce research notes, final files where applicable, and handoff notes. They do not edit event files, localisation files, `.gfx` files, GUI files, sound definition files, or spreadsheet rows unless the parent prompt explicitly expands their scope.


## 4. Super-event design role

Before wiring a super-event, decide what role it plays.

Common roles:

- first reveal
- escalation
- global response
- faction formation
- world-end scenario
- defeat aftermath
- irreversible political shift
- campaign-ending signal
- rare hidden branch
- ideological victory or collapse

The role should determine the tone, title, image, quote, and audio.

Do not choose a quote, image, or track because it sounds dramatic in isolation. It must fit the exact super-event role.

## 5. Localisation format

Super-event localisation must follow the existing Chaos Redux format.

Example:

```yaml
chaosx_super_event.1.t: "Undead?"
chaosx_super_event.1.d: "The dead have risen, spreading terror and chaos.\n\nWitnesses describe scenes of horror as reanimated corpses or \"zombies\" began to terrorize cities and rural areas alike. The outbreak's cause appears to be unknown.\n\nAuthorities are urging the public to remain vigilant and avoid contact with anyone exhibiting unusual behavior."
chaosx_super_event.1.a: "Do you like to take a yo-yo for a ride?" # Ironic remark
chaosx_super_event.1.q: "This, then, is how you should pray: 'Our Father in heaven, hallowed be your name.' \n §Y-Matthew 6:9-§!" # An actual quote that fits the situation
```

Required keys:

- `.t` for title
- `.d` for description
- `.a` for button text
- `.q` for quote

Keep the key numbering aligned with the actual super-event slot.

Do not invent a different localisation pattern unless the existing repo pattern has changed.

## 6. Title rules

A good super-event title should be short, memorable, and specific.

It can be:

- direct
- ironic
- ominous
- religious
- political
- military
- bureaucratic
- poetic
- understated

Avoid generic titles such as:

- The End Begins
- World in Flames
- The Final Crisis
- Humanity Falls
- Darkness Rises

Use titles that fit the event's actual identity.

## 7. Description rules

The description should explain the event clearly without turning into a normal event wall of text.

It should:

- give the player enough context
- fit the tone of the event
- avoid overexplaining mechanics
- avoid direct spoilers if the event is meant to remain uncertain
- describe visible consequences or public understanding
- keep uncertainty where the event has not fully revealed itself

For secret or uncertain events, use partial information:

- observers are unsure
- reports conflict
- foreign diplomats avoid clear statements
- intelligence agencies disagree
- governments deny involvement
- regional witnesses give different accounts
- the full meaning is not yet clear

Do not reveal a hidden world-ending branch too early.

## 8. Button text and remark rules

The button text (`.a`) should feel like a reaction to the moment.

It may be:

- ironic
- grim
- understated
- religious
- ideological
- military
- sarcastic
- resigned
- coldly bureaucratic
- a meaningful cultural reference

Button text can use a short cultural reference when it fits the super-event.

Possible sources include:

- songs
- films
- books
- poems
- games
- political slogans
- religious texts
- historical remarks
- internet-era phrases only when the event intentionally fits that tone

Examples of the kind of source that may be considered include Steely Dan lyrics, a line from *The Lord of the Rings*, a film line, or a book line, but only if the reference genuinely fits the event.

Use the repository web research workflow from `AGENTS.md` to verify the exact wording and source of any referenced line.

For modern copyrighted songs, films, books, or games, keep the line very short. Prefer a short fragment, a title-like reference, or a paraphrased allusion when a direct quote would be too long.

Avoid generic button text such as:

- OK
- We must act
- This is terrible
- The world will never be the same

The button text should be short enough to fit well in-game.

Document the cultural source in the super-event research note when the button text is a reference.

## 9. Quote rules

The quote (`.q`) should deepen the super-event.

Do not invent quotes.

Do not misattribute quotes.

Do not use a quote unless it fits the specific event.

Use the repository web research workflow from `AGENTS.md` to find and verify real quotes.

Prefer quotes that can be checked against a reliable source. Primary sources are best. If a primary source is not available, use reputable quote collections, archives, books, speeches, scripture references, or other traceable sources.

Good quote sources can include:

- public domain literature
- religious texts
- historical speeches
- philosophical works
- political writings
- military memoirs
- legal documents
- poetry
- mythology
- propaganda slogans
- period documents

For the main quote, prefer public domain, historical, religious, literary, philosophical, or political sources when possible.

Avoid:

- invented quotes
- misattributed quotes
- unsourced internet quotes
- quotes that only sound dramatic but do not fit the event
- quotes with uncertain attribution unless clearly marked
- long copyrighted song lyrics, film dialogue, book dialogue, or game dialogue

Modern songs, films, books, and games are better suited for the button text or remark (`.a`) than the main quote (`.q`).

If a modern cultural line is used as the main quote anyway, it must be very short, and clearly sourced

If attribution is uncertain, mark it uncertain or choose another quote.

## 10. Quote research workflow

Use the repository web research workflow from `AGENTS.md` for quote research.

Search for quotes by combining the event's core themes with terms such as:

- quote
- speech
- poem
- scripture
- proverb
- historical quote
- public domain quote
- literature quote
- military quote
- political quote
- philosophical quote

Do not stop at the first quote that sounds good. Find several candidates, compare them, and select the one that best fits the exact super-event role.

For every proposed quote, document:

- quote text
- speaker or author
- source work, speech, book, scripture, or document
- year or approximate period if known
- source link
- why it fits the super-event
- attribution confidence
- notes about uncertainty
- whether the quote is public domain, copyrighted, or unclear when this can be determined

Use direct quotes sparingly and keep them short enough for the super-event UI.

If the quote is too long, use a shorter excerpt.

Do not alter a quote in a way that changes its meaning.

If a translation is used, state that it is a translation when relevant.

If no strong quote is found, continue searching instead of inventing one.

## 10.1 Cultural remark research workflow

The button text (`.a`) can be a meaningful remark or cultural reference.

This is separate from the main quote (`.q`).

Use the repository web research workflow from `AGENTS.md` to find and verify cultural references.

Good cultural remark sources can include:

- song lines or titles
- film lines
- book lines
- play lines
- game lines
- well-known slogans
- religious or mythological phrases
- political or military catchphrases

The remark should fit the super-event's tone. It can be ironic, grim, darkly funny, understated, reverent, fatalistic, or bitter.

For modern copyrighted works, keep the direct quote very short. Prefer brief fragments, paraphrased allusions, or title-like references when possible.

For every cultural remark candidate, document:

- remark text
- source work or artist
- author, songwriter, filmmaker, or writer if relevant
- year if known
- source link
- why it fits the super-event
- whether it is a direct quote, short fragment, title reference, or paraphrase

Do not invent a cultural reference.

Do not misquote a line if presenting it as a direct reference.

Do not use a reference that breaks the tone of the event unless the contrast is intentional.

## 11. Quote style by super-event type

### First reveal

Use quotes about discovery, doubt, fear, false peace, hidden rot, or the first sign of collapse.

### Escalation

Use quotes about loss of control, failed containment, pride, punishment, betrayal, war, disease, or mass panic.

### World-end scenario

Use quotes about final judgment, collapse, extinction, fate, prophecy, silence, ruin, or the end of order.

### Defeat aftermath

Use quotes about memory, cost, survival, rebuilding, responsibility, or vigilance.

### Ideological victory or transformation

Use quotes about faith, revolution, obedience, sacrifice, destiny, legitimacy, power, or rebirth.

### Scientific or experimental disaster

Use quotes about knowledge, arrogance, forbidden inquiry, unintended consequences, or the limits of control.

## 12. Audio research purpose

Super-event audio should make the moment feel distinct.

Super-event audio runtime uses sound output only. Register the final cue as sound and play it through the settings-aware sound helper.

Core rule: a super-event task is not complete unless its audio is selected, verified, converted to a game-ready WAV, registered, wired, and documented.

Every super-event implementation must include complete sound wiring. Do not leave a completed super-event on default, placeholder, mismatched, wrong-format, or undocumented audio.

Every super-event must have its own unique final track, unique audio id, and unique sound registration unless the user explicitly approves a specific reuse before implementation. Do not reuse another super-event's track just because the moments are related.

The final cue should be an intentional musical recording by default, such as a chant, hymn, orchestral excerpt, song, march, or other track with musical structure. Do not use pure sound effects, drones, pulses, room tone, one-shot stingers, abstract ambience, or texture beds for a super-event unless the user explicitly asks for non-musical audio and the exception is documented.

Never create or accept a super-event track from generated test tones, primitive waveforms, signal-generator output, metronome clicks, generated beeps, simple oscillator layers, noise beds, or quick local synthesis. This includes sine, square, triangle, sawtooth, and similar waveforms, even when mixed with noise or effects. If no real licensed track is available, stop and report the blocker instead of manufacturing a cue.

Never describe a final cue with placeholder provenance such as "restored legacy", "legacy audio package", "repository history", or similar implementation-history wording in player-facing or attribution documentation. The canonical audio catalogue at `music/chaosx_music_track_list.html` and the audio docs must name the actual source title, creator or composer, performer or recording source when known, source URL, license, and duration. Use attribution status `verified` only after the title and creator/composer are identified and the source/license have been checked.

The final cue should be chosen intentionally.

## 13. Audio research rules

Before looking outside the repository, check whether an approved suitable track already exists in the repo. Inspect:

- existing `sound/*.wav`
- `sound/chaosx_sound.asset`
- `music/chaosx_music_track_list.html`
- existing docs or manifests that identify source and license

Use an existing track only when its source, license, duration, and intended use are already documented well enough to trust, and when its tone fits the specific super-event role and pacing.

If no approved suitable track exists, search the internet using the repository web research workflow from `AGENTS.md`. Do not use unapproved web browsing tools for this repo.

Find audio that fits the exact super-event tone, role, and pacing. Prefer tracks between 1 and 2 minutes long. If a better track falls outside that range, document the exception before use and trim the final in-game file to 2 minutes or less unless the user explicitly approves a longer final track.

Prefer:

- public domain audio
- Creative Commons audio
- government or institutional recordings with clear use terms
- official archive recordings with clear rights
- user-provided audio with explicit permission
- otherwise clearly licensed audio that permits the intended mod use

Reject:

- generated test-tone or oscillator audio, including sine, square, triangle, sawtooth, beep, pulse, and noise-bed cues
- tracks that are primarily sound effects, drones, stingers, loops, abstract ambience, or texture beds when the request is for a structured musical cue
- tracks with unclear licensing
- YouTube uploads with no license information
- vague "royalty free" claims without usage terms
- modern commercial recordings with unclear rights
- copyrighted film, game, trailer, or album recordings without clear permission
- tracks where the composition is public domain but the recording is not usable

For each candidate and final selected track, verify and document:

- title
- creator or composer
- performer or recording source if relevant
- source URL
- license
- license confidence
- duration
- usage terms
- attribution text if required
- source link
- why it fits the super-event
- suggested in-game use
- editing notes
- suitability rating
- uncertainty notes

Check composition rights and recording rights separately.

A public domain composition does not automatically make a recording public domain.

If the license is unclear, mark it unsuitable and find another option. Do not wire uncertain audio into a completed super-event.

Do not claim a track is public domain without checking.

## 14. Audio implementation workflow

For every super-event audio package:

1. Select the track after repository and internet-source checks.
2. Verify the track title, creator or composer, source, license, duration, and usage terms.
3. Download the selected audio from its legitimate source.
4. Preserve the downloaded source file under the temporary event-scoped `docs/assets/<event_id>_<event_slug>/` source-audio path when practical. Before the event goal is fully complete, promote durable source, license, attribution, and conversion facts into the permanent audio documentation, verify that no runtime reference points into `docs/assets/`, and delete the event-scoped workspace. Keep it for blocked or incomplete work.
5. Convert the final cue to a game-ready `.wav`.
6. Place the final `.wav` in the event-scoped sound folder: `sound/<event_id>_<event_slug>/super_event_<super_event_id>_<super_event_name>.wav`.
7. Add or update the base `sound` definition in `sound/chaosx_sound.asset` so it points to the final WAV and has a unique sound definition id.
8. Add or update the required settings-volume `soundeffect` wrappers in `sound/chaosx_sound.asset`. Each wrapper must point to the base sound, follow the existing `max_audible` and `max_audible_behaviour` pattern, and use the helper naming contract `chaosx_super_event_<super_event_id>_sound_<volume_suffix>`.
9. Set `global.current_super_event_audio_id` to the correct unique audio id and call `play_current_super_event_sound = yes`, the settings-aware sound helper.
10. Update the relevant event/system documentation and `music/chaosx_music_track_list.html`, the canonical audio catalogue. Every final cue must have a row that lists the super-event id using the track and the source/rights details. If a user-approved reuse exists, document every id in the row and explain the approval in the audio docs.
11. Verify the final file paths, sound definitions, volume wrappers, ids, helper call, and docs before calling the super-event complete.

Use the existing Chaos Redux settings-aware sound helper. Do not bypass it.

## 15. Audio editing notes

For every suitable track, propose practical editing notes.

Possible notes:

- trim start
- trim ending
- fade in
- fade out
- loop segment
- lower volume
- raise intro volume
- remove silence
- use only first 30 seconds
- use quiet opening only
- avoid loud ending
- match super-event duration

Do not perform destructive edits without preserving the original source file.

Document any edited derivative file.

## 16. Audio implementation expectations

When implementing audio, follow the existing Chaos Redux audio pattern.

The implementation should keep these aligned:

- final sound file
- base sound definition
- required volume-wrapper soundeffects
- audio id
- `global.current_super_event_audio_id`
- settings-aware sound helper
- super-event slot
- localisation
- documentation

Every super-event must have a specific audio id and a unique final track. Shared audio ids or shared tracks are allowed only when the user explicitly approved the exact reuse.

Use `play_current_super_event_sound = yes` rather than bypassing the settings-aware sound helper.

Fallbacks are not allowed without discussing them with the user. If final audio is unavailable, stop and explain the blocker instead of silently leaving default or placeholder audio.

## 17. Audio documentation

Always update `music/chaosx_music_track_list.html`, the canonical audio catalogue, for every super-event track. Every final super-event track must have a row in that table, and the row must show the super-event ID using the track. User-approved reuse must list every affected ID and the audio docs must explain why reuse was approved.

Update any additional audio documentation used by the repo.

For each super-event audio package, document:

- title
- creator or composer
- performer or recording source if relevant
- source URL
- license
- license confidence
- usage terms
- duration
- attribution text if required
- downloaded source path
- final `.wav` path
- base sound definition id
- required volume-wrapper soundeffect ids
- super-event id or key using the track
- `music/chaosx_music_track_list.html` row with the final track and super-event ID or IDs
- editing or conversion steps
- uncertainties, if any
- why the track fits the super-event tone, role, and pacing

If metadata cannot identify the author, title, source, license, or duration, and the user did not provide it, reject the track or ask the user for the missing information instead of guessing.

## 18. Audio validation checklist

Before finishing any super-event task, confirm:

- the final `.wav` exists
- the final `.wav` is game-ready for the HOI4 sound pipeline
- the file is in the correct event-scoped sound folder
- the selected track is between 1 and 2 minutes long, or the exception is documented
- the base sound definition in `sound/chaosx_sound.asset` points to the correct `.wav`
- the required settings-volume soundeffect wrappers point to the base sound and use the helper naming contract
- the super-event points to the correct audio id and calls `play_current_super_event_sound = yes`
- `music/chaosx_music_track_list.html` documents every super-event track and shows the super-event ID or IDs using it
- documentation records the source, license, and duration
- documentation records the downloaded source path, final `.wav` path, sound definition id, volume-wrapper ids, and super-event use
- no generated test-tone, oscillator, beep, primitive waveform, or noise-bed cue remains in any completed super-event track
- every completed super-event has a unique final track unless exact reuse was explicitly approved by the user and documented
- no placeholder, default, mismatched, or wrong-format audio remains for completed super-events

## 19. Super-event image handoff

Super-event images are handled through `chaos-redux-event-assets`.

Default rule:

- use generated super-event images when the moment is fictional, alternate-history, symbolic, supernatural, high-chaos, or needs a unique emotional composition
- use internet-sourced images when the super-event must depict a real historical person, real photographed event, or real archival artifact
- follow `chaos-redux-event-assets` and the official `$imagegen` workflow for generated images

The super-event skill should define the image direction:

- subject
- tone
- composition need
- symbolism
- source mode: generated, sourced, or user-provided
- source-image search direction or image-generation prompt direction
- what to avoid
- why the image fits the super-event

The asset skill handles:

- source search
- source documentation
- image processing
- PNG preview
- DDS conversion
- main-agent `.gfx` wiring
- manifest

Treat project-root `docs/assets/<event_id>_<event_slug>/` as temporary evidence for super-event image and audio work. Retain source files, previews, contact sheets, manifests, provenance, research notes, and handoffs while work is active, blocked, awaiting review, or undergoing acceptance scenarios. Before declaring the event goal fully complete, move or copy durable evidence into `docs/events/`, `docs/plans/`, `docs/specs/`, `docs/super_events/`, or another permanent documentation surface, then delete only that event-scoped workspace. Never delete skill-local reusable assets under `.agents/skills/.../assets/` or unrelated workspaces. Do not require the deleted workspace to exist for a completion claim.

## 20. Super-event slot wiring

When wiring a super-event, choose the slot intentionally.

Make sure the implementation:

1. sets the correct visibility flag
2. sets `global.current_super_event_audio_id`
3. uses the settings-aware playback helper
4. updates scripted localisation, including `GetSuperEventImage` for the slot's sprite and the title/description/quote/remark getters
5. updates player-facing localisation
6. updates image wiring in the correct `.gfx` file
7. updates audio wiring
8. updates docs
9. updates spreadsheet or event catalog if relevant

Do not reuse a slot accidentally.

Do not let two unrelated super-events point to the same current image, text, or audio unless the reuse is intentional and documented.

## 21. World-end super-events

World-end super-events need stricter alignment.

When a super-event represents a world-end scenario:

- guard the branch with the world-end rules from `chaos-redux-events`
- make the terminal state clear
- set the scenario-specific global flag
- set the matching super-event visibility
- stop or gate incompatible future systems and branches
- make the docs and spreadsheet agree
- choose quote and audio with finality in mind

A world-end super-event should feel like an end-state, not a normal escalation.

## 22. Defeat aftermath super-events

Use defeat aftermath super-events only when the defeated threat was global or near-global, long enough, and costly enough to reshape the campaign.

The super-event should communicate:

- what was defeated
- what the world lost
- what remains unstable
- what new order or memory follows
- why the campaign does not simply return to normal

Quotes and audio should usually feel reflective, not triumphant without cost.

## 23. Documentation requirements

The event documentation should explain:

- which super-event exists
- when it fires
- what branch or evolution triggers it
- what slot it uses
- what image it uses
- what audio id it uses
- what quote it uses
- what source the quote came from
- what audio source is used
- whether any image is placeholder
- confirmation that audio is final and not placeholder/default

Do not leave the docs saying only "super-event added."

## 24. Manifest or research note

For every super-event research package, create or update a markdown note.

Recommended path:

```text
docs/super_events/<event_id>_<event_slug>_super_event_research.md
```

The note should include:

- event id
- event slug
- super-event role
- title
- description
- button text
- button text source or cultural reference if applicable
- button text source link if applicable
- quote candidates
- selected quote
- quote source and confidence
- image direction
- image asset manifest path or permanent asset-provenance/crosswalk note. If the temporary `docs/assets/` manifest was deleted after completion, record the permanent note that replaced its durable facts instead of leaving a broken path.
- audio candidates
- selected audio
- track title
- creator or composer
- performer or recording source if relevant
- source URL
- license
- license confidence
- duration
- attribution text if required
- downloaded source path
- final `.wav` path
- base sound definition id
- required volume-wrapper soundeffect ids
- super-event id or key using the track
- `music/chaosx_music_track_list.html` row with the final track and super-event ID or IDs
- editing or conversion steps
- uncertainties, if any
- implementation notes
- open questions

## 25. Improvement-loop super-event depth

Improvement addenda can propose new super-events, but a super-event should still mark a real campaign threshold. Do not add one just because a route has a strong image. Use one when a formable changes regional order, a hidden route becomes public, a scripted GUI mechanic reaches a global milestone, a league or world threat emerges, or a defeat aftermath reshapes the campaign.

For formables, the super-event should reflect the formation method. A negotiated federation, violent restoration, occult revival, imperial proclamation, anti-colonial congress, and puppet-backed union should not share the same tone. The title, quote, image, audio, remark, and trigger should reveal the route identity.

Animated portraits or animated scripted GUI assets can support a super-event-adjacent moment, but they are not replacements for the super-event package. The super-event still needs aligned text, quote, image, audio, trigger, docs, etc.

## 26. Final checklist

Before closing a super-event task, confirm:

1. The super-event role is clear.
2. The slot is chosen intentionally.
3. Title, description, button text, and quote exist.
4. The repository web research workflow from `AGENTS.md` was used to find and verify real quote candidates.
5. The quote is sourced and not invented.
6. Quote attribution is documented.
7. Button text cultural references are sourced when applicable.
8. Modern copyrighted lyrics, film lines, book lines, or game lines are kept very short.
9. The image direction has been handed to `chaos-redux-event-assets`.
10. The super-event image is sourced or generated according to the asset rules.
11. An approved existing track was checked first.
12. If no approved track existed, the repository web research workflow from `AGENTS.md` was used.
13. Audio candidates were researched against the event tone, role, and pacing.
14. Composition rights and recording rights were considered separately.
15. Tracks with unclear licensing were rejected.
16. License or public domain status is documented.
17. Selected audio has title, creator or composer, source, license, duration, usage terms, and suitability notes.
18. The final `.wav` exists in the correct event-scoped sound folder.
19. The selected track is between 1 and 2 minutes long, or the exception is documented.
20. The base sound definition in `sound/chaosx_sound.asset` points to the correct `.wav`.
21. Required settings-volume soundeffect wrappers point to the base sound and follow the helper naming contract.
22. `music/chaosx_music_track_list.html` records the final track, source/rights details, and super-event ID or IDs.
23. The audio id is specific to the super-event or intentionally shared and documented.
24. `global.current_super_event_audio_id` is set correctly.
25. `play_current_super_event_sound = yes` uses the settings-aware sound helper.
26. Scripted localisation is updated, including `GetSuperEventImage`. otherwise the slot can show default art while the text/audio work.
27. Player-facing localisation is updated.
28. Image wiring is updated.
29. Audio wiring is updated.
30. Audio documentation is updated with source, license, duration, paths, sound definition id, volume-wrapper ids, super-event use, and conversion steps.
31. No placeholder, default, mismatched, or wrong-format audio remains for completed super-events.
32. Event docs are updated.
33. Spreadsheet or event catalog is updated if relevant.
