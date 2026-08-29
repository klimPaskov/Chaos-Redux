# Event 35 Evolution III super-event research and implementation prompt

## Goal

Create the complete super-event package for Event 35 Evolution III, The Second Great Depression. The super-event marks the first worldwide activation of the global economic crisis. It should feel larger than a national report because it changes output, construction, trade, exposure, and recovery conditions across most ordinary countries.

Follow `AGENTS.md`, `chaos-redux-super-events`, `chaos-redux-event-assets`, the accepted Event 35 specification, and the current super-event framework. This prompt does not approve a second super-event for ordinary national openings, contagion conversions, or routine Social Collapse incidents.

## Super-event role

- Role: Global escalation.
- Trigger: First valid activation of Event 35 Evolution III.
- Owner event: Event 35.
- Origin: The country whose crisis caused the worldwide activation, including an Event 34 Evolution III collapse when applicable.
- Frequency: Once per worldwide Event 35 lifecycle.
- Chaos rule: Evolution state itself gives zero Chaos. The worldwide activation is a concrete global consequence and may create the bounded Event 35 Chaos milestone defined by the specification.

## Required source reading

Read:

- Event 35 specification part 7.
- Presentation and asset part 10.
- Cross-event and Chaos part 8.
- Research notes.
- Current super-event slots, localisation, scripted localisation, image registry, sound definitions, and music catalogue.
- Current Event 34 super-event plans when any slot or audio relationship exists.

Inspect current slot availability and preserve unrelated super-events.

## Title direction

The established evolution identity, `The Second Great Depression`, is the default title direction. Another title is acceptable only when it is shorter, period appropriate, and more specific to the implemented global threshold.

Avoid generic titles such as:

- World in Ruin.
- The Final Crisis.
- Darkness Falls.
- The Global Collapse.

The title should identify an economic world event, not a military apocalypse.

## Description direction

The description should show observable worldwide conditions:

- Factories reducing shifts or closing.
- Freight and ports losing traffic.
- Construction stopping.
- Orders and payments failing across borders.
- Governments choosing aid, control, withdrawal, or public works.
- Unemployment and political pressure increasing.

Dynamic references may include:

- Origin country.
- A failed Industrial Boom when it caused activation.
- Several affected regions or major economies when the current script can prove them.
- Current global stage only when the stage is visible and useful.

Do not expose:

- Hidden global pressure.
- Candidate pools.
- Conversion weights.
- Future coup or civil-war gates.
- Achievement conditions.
- Implementation history.

The prose should remain concise enough for the super-event window.

## Button or cultural remark direction

Use `chaosx_super_event_text_researcher` to find several candidates.

Suitable tones:

- Bitter official understatement.
- Period newspaper or political phrase.
- Short line about work, hunger, debt, idle industry, or world trade.
- Grim administrative acceptance.

Candidate sources can include:

- Public-domain literature.
- Historical speeches.
- Period labor or economic writing.
- Political slogans with clear source.
- A very short modern cultural allusion only when it fits and copyright limits are respected.

Do not invent a remark or copy a long song, book, film, or game line.

The research note must record exact wording, source, creator, year when known, link, confidence, copyright status, and why it fits.

## Quote direction

Use `chaosx_super_event_text_researcher` to find and compare verified candidates.

Themes:

- Work and unemployment.
- Economic interdependence.
- Failed prosperity.
- Poverty amid industrial capacity.
- Fear and political instability.
- Recovery and responsibility only when the selected quote fits the first global collapse, not the later recovery.

Preferred sources:

- Public-domain literature.
- Historical speeches and writings.
- Religious or philosophical texts when directly relevant.
- Interwar economic or labor writing.
- Government or international documents.

Reject:

- Unsourced quote websites.
- Misattributed lines.
- Invented dramatic prose.
- Long copyrighted lyrics or dialogue.
- A quote about military defeat that has no economic connection.

For every candidate, record:

- Exact text.
- Author or speaker.
- Source work or speech.
- Date.
- Reliable link.
- Attribution confidence.
- Public-domain or copyright note.
- Fit analysis.

Select one only after comparison. If no defensible candidate exists, report the blocker and do not invent one.

## Image direction

Route image production to `chaosx_generated_event_art` unless the final concept requires a specific real archival scene.

### Preferred generated scene

A period-authentic documentary scene of a major industrial and transport system at a standstill:

- Idle port cranes and freight tracks.
- Closed factory gates and dark machine halls.
- Workers or families waiting outside industrial sites.
- Halted construction and unfinished expansion.
- Several national settings suggested through architecture and people without becoming a collage.

The image should communicate worldwide scale through the breadth of industrial shutdown. It should not use a world map, stock chart, currency symbols, arrows, flags covering the canvas, or readable generated headlines.

Visual period:

- 1930s to 1940s photographic technology or press illustration.
- Period clothing, vehicles, cranes, locomotives, factory buildings, and streets.
- No modern containers, digital signs, high-visibility clothing, contemporary cars, glass office towers, or electronic market boards.

Mood:

- Severe and human.
- Broad economic stillness.
- No fantasy apocalypse, flames, skulls, or military battlefield unless the actual activation occurred during war and the final composition remains economic.

The asset package requires source art, prompt, processed PNG, final DDS, sprite handoff, checksums, contact or comparison review, and permanent provenance record.

## Audio research direction

Route audio research to `chaosx_super_event_audio_researcher`.

The final cue must:

- Be unique to this super-event unless the user explicitly approves exact reuse.
- Be a real musical recording with structure.
- Have clear composition and recording rights.
- Fit a worldwide economic collapse.
- Be approximately one to two minutes after final editing, unless an exception is documented.
- Use a legitimate source.
- Preserve the original download and licence evidence.
- Be converted to a game-ready WAV.

Suitable directions:

- Period orchestral lament.
- Public-domain classical work with a usable recording.
- Historical labor or religious music with clear rights and serious fit.
- Restrained march, dirge, or hymn where the musical meaning fits industrial and social collapse.

Reject:

- Generated tones.
- Drone or noise bed.
- Beep, pulse, or oscillator cue.
- Unlicensed commercial recording.
- Film, game, or album track without clear permission.
- YouTube upload without defensible rights.
- A triumphant military march unless the contrast is explicitly justified.

The audio research note must record:

- Title.
- Composer or creator.
- Performer or recording source.
- Source URL.
- Composition status.
- Recording licence.
- Duration.
- Usage terms.
- Attribution.
- Downloaded source path.
- Editing and conversion steps.
- Final WAV path.
- Sound definition ID.
- Required volume-wrapper IDs.
- Final super-event audio ID.
- Music-catalog row.

## Runtime wiring

The parent implementation agent owns final wiring.

Required surfaces:

- Stable super-event slot.
- One worldwide-activation visibility flag.
- Event 35 Evolution III trigger effect.
- Title, description, button, and quote localisation.
- Scripted localisation selectors.
- `GetSuperEventImage` or current image selector.
- Event-owned sprite and DDS.
- Unique audio ID.
- Base sound definition.
- Volume wrappers.
- `global.current_super_event_audio_id`.
- `play_current_super_event_sound = yes`.
- Super-event research note.
- Event documentation.
- `music/chaosx_music_track_list.html`.
- Authoritative workbook alignment when the catalog exposes the evolution.

The trigger must fire once when the global Evolution III lifecycle begins. A later national conversion or secondary origin must not replay it.

## Settings and conflict behavior

- Respect the existing super-event visibility and sound settings.
- Do not reuse a slot already owned by unrelated content.
- Do not overwrite another event's current image or audio selector.
- If another super-event is already visible, follow the framework's queue or conflict rule.
- The worldwide state must still activate when presentation is disabled.

## Documentation note

Create or update:

`docs/super_events/035_great_depression_super_event_research.md`

The final note should contain:

- Role and trigger.
- Slot.
- Final title and description.
- Button source.
- Quote and attribution.
- Image source mode, prompt, final path, and sprite.
- Audio title, creator, performer, source, licence, duration, and paths.
- Sound IDs and helper use.
- Implementation references.
- Remaining uncertainty.

## Validation

Verify:

- Super-event appears once on first worldwide activation.
- Correct origin and text are shown.
- Image, title, description, button, quote, and audio describe the same event.
- No raw key or wrong slot appears.
- Audio uses settings-aware playback and correct volume wrappers.
- Final WAV exists and is documented.
- Image aspect and crop fit the window.
- Quote and button fit without clipping.
- Disabling the presentation does not block the worldwide mechanic.
- Save and reload does not replay an already completed initial reveal.

## Handoff

Return:

- Candidate comparison tables.
- Selected quote and button source.
- Selected audio and rights evidence.
- Image prompt or archival provenance.
- Final file paths and checksums.
- Slot and identifier map.
- Files that the parent must wire.
- Task-specific validation.
- Any blocker or unresolved rights issue.

Do not claim the super-event complete while the quote is unsourced, audio is unlicensed or placeholder, image is unwired, slot is uncertain, documentation is missing, or the trigger can repeat.
