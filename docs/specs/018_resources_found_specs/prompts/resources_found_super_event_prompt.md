# Super-Event Research and Implementation Prompt for Event 018 Resources Found

Create the complete super-event research packages for Chaos Redux Event 018, Resources Found. Use `chaos-redux-super-events` and the narrow research subagents with `fork_context=false`.

Use:

- `chaosx_super_event_text_researcher` for title direction resolution, main quotes, button remarks, attribution, and copyright notes
- `chaosx_super_event_audio_researcher` for final licensed music, source verification, download, editing, conversion, and audio documentation
- `chaosx_generated_event_art` for the fictional super-event images described in the asset prompt

The main implementation agent owns final localisation, scripted localisation, slot selection, image GFX wiring, audio definitions, settings-aware playback, event triggers, docs, and spreadsheet alignment.

No title, button line, quote, cultural remark, slogan, lyric fragment, or audio track in this prompt is final. Every source-dependent wording and every track is blocked until researched and documented.

## Required source inputs

Read:

- Event 018 source specs, especially Parts 4, 5, 7, and 8
- `prompts/resources_found_asset_prompt.md`
- `chaos-redux-super-events`
- relevant existing super-event slot, music, image, and documentation patterns
- existing track list and audio manifests to prevent accidental reuse

Every super-event must have its own final image, final track, audio ID, sound wrapper, text package, and research note. Reuse requires explicit user approval and is not assumed.

## Research-note path

Create or update:

```text
docs/super_events/018_resources_found/overview.md
```

The note must include considered candidates, selected sources, confidence, licensing, final file paths, implementation IDs, and open blockers.

## Super-event A: Cave-country emergence

### Role

First public reveal of an organized nonhuman country emerging from the overexploited field.

### Trigger

Evolution IV completes. The cave country receives the field state, its 6 to 30 division starting army is created, and war begins against every land neighbor.

### Player emotion

Recognition that the underground attacks were the edge of an organized polity and army. The moment should feel heavy, physical, and politically transformative rather than supernatural spectacle without rules.

### World understanding

The field state has fallen. Mineral-armored nonhuman formations are using the excavation system as a capital and are attacking neighboring borders. Observers do not yet know the full resource-capacity rule or world-end condition.

### Title direction

Research required. Find a short specific title about organized emergence, birth of a state below the field, or the land opening into an army. Avoid generic apocalypse titles, generic darkness wording, and comedy cave puns.

### Description direction

Write final localisation during implementation. The description should mention the ruined extraction zone, organized formations, the loss of state control, and immediate border attacks. It should not list modifiers, division counts, capacity formulas, or future continent conditions.

### Main quote direction

Research several real candidates about digging too deeply, awakening hidden powers, the earth producing armies, buried danger, or human greed opening destruction. Prefer public-domain literature, scripture, historical writing, myth, political writing, or traceable philosophical sources.

Do not use the famous Tolkien line about delving too greedily and too deep as an automatic choice. It is modern copyrighted text and overly obvious. It may be considered only as a very short cultural remark or title-like allusion if copyright and fit are documented, and a stronger public-domain main quote is still preferred.

For each candidate record:

- exact wording
- author or speaker
- source work or document
- date or period
- reliable source URL
- attribution confidence
- public-domain or copyright note
- why it fits emergence rather than world end

### Button or cultural remark direction

Research required. The button should be short and react to the first organized emergence. Suitable tones include grim industrial irony, a short mining proverb direction, fatalistic understatement, or a compact cultural allusion. Modern copyrighted lines must remain very short.

### Image direction

Use the final generated image from:

```text
gfx/super_events/018_resources_found/super_event_018_cave_emergence.dds
```

Proposed sprite:

```text
GFX_super_event_018_cave_emergence
```

The image shows organized mineral-armored broods leaving a colossal industrial breach. Human defenders withdraw at the edges. The focus is the creation of a nonhuman state.

### Audio mood

Research unique real music with clear licensing. Desired pacing:

- low, weighty opening
- deliberate rise
- organized martial or processional structure
- no pure drone
- no generated tone
- no primitive waveform or noise bed
- roughly 1 to 2 minutes in final game form

Possible source directions include public-domain compositions with clearly usable recordings, archive recordings, Creative Commons orchestral or choral works, or institutional collections. Check composition and recording rights separately.

### Proposed implementation handles

Final IDs must be checked against the repository.

```text
super_event role: 018_cave_emergence
image sprite: GFX_super_event_018_cave_emergence
audio id direction: super_event_audio_018_cave_emergence
music path direction: sound/018_resources_found/super_event_<slot>_cave_emergence.wav
sound path direction: sound/018_resources_found/super_event_<slot>_cave_emergence.wav
```

The final audio ID, slot, and filenames must match actual wiring.

## Super-event B: Cave world-end scenario

### Role

Terminal world-end revelation after the cave country consumes its origin continent, global chaos exceeds 1000, and stronger ruptures begin on other continents.

### Trigger

All eligible origin-continent states are owned and controlled by the cave country for the verification period. Chaos is above 1000. No world end is active. The first valid cross-continent footholds are created.

### Player emotion

Finality, global scale, and the realization that the first continent became a connected template for expansion.

### World understanding

Resource centers on distant continents rupture. The armies are stronger and organized by knowledge gained during the first continental war. The campaign has entered a terminal state.

### Title direction

Research required. Find a short, specific title about the world opening below, a continent becoming a seed, or simultaneous ruptures. Avoid generic titles such as The End Begins, World in Flames, Darkness Rises, or Humanity Falls.

### Description direction

The description should show simultaneous physical ruptures, collapsing industrial or resource centers, organized nonhuman armies, and the loss of ordinary geographic containment. Do not list chaos value, state counts, or spawn formulas.

### Main quote direction

Research several real candidates about judgment from below, the earth opening, buried nations, the end of order, insatiable hunger, or a world consumed by what it extracted.

Prefer public-domain or historical sources. Scripture, classical literature, myth, public-domain poetry, historical philosophy, and traceable political writing are suitable. Verify exact wording and translation.

The world-end quote must feel final. Do not reuse the emergence quote or merely select a more dramatic line from the same source without comparison.

### Button or cultural remark direction

Research required. Suitable tones include fatalistic understatement, a short title-like allusion to mining or descent, religious dread, or bitter commentary on extraction. Keep modern references extremely short and document copyright risk.

### Image direction

Use:

```text
gfx/super_events/018_resources_found/super_event_018_world_end.dds
GFX_super_event_018_world_end
```

The generated image shows a mature organized cave host emerging through a shattered resource center on another continent, with signs of simultaneous distant ruptures. A map is not the central subject.

### Audio mood

Research a unique final track, different from emergence. Desired shape:

- immediate sense of global scale
- strong musical structure
- solemn or catastrophic weight
- progression from deep low register into overwhelming ensemble or choral force where licensing permits
- 1 to 2 minutes after trim
- no drone, generated tone, pulse, ambience-only bed, or placeholder

### Proposed implementation handles

```text
super_event role: 018_cave_world_end
image sprite: GFX_super_event_018_world_end
audio id direction: super_event_audio_018_cave_world_end
music path direction: sound/018_resources_found/super_event_<slot>_cave_world_end.wav
sound path direction: sound/018_resources_found/super_event_<slot>_cave_world_end.wav
```

## Super-event C: Global cave defeat aftermath

### Use gate

Produce and wire this package only if the implemented cave crisis became global or near-global, lasted long enough, and caused enough loss to justify a major defeat aftermath. A short regional containment does not use this super-event.

### Role

Reflective defeat aftermath after every cave state and cross-continent foothold is eliminated.

### Trigger

- no cave country territory remains
- no active cave foothold remains
- the cave world threat is cleared
- the campaign met the global-severity and duration requirements
- no incompatible world-end resolution blocks the aftermath

### Player emotion

Relief mixed with exhaustion, reconstruction, and awareness that resource sites and underground infrastructure can no longer be treated as ordinary.

### Title direction

Research required. Find a short title about sealing the last depth, the ground becoming quiet, or survival after a buried war. Avoid uncomplicated victory language.

### Description direction

Describe the final sealed strongholds, damaged resource regions, surviving armies, reconstruction teams, and the political memory of the crisis. Do not say the world returned to normal.

### Main quote direction

Research public-domain or historical candidates about survival, vigilance, memory, rebuilding, or the cost of victory. The quote should be reflective rather than triumphant.

### Button or cultural remark direction

Research required. A quiet practical phrase, restrained religious line, miners’ return motif, or short cultural reference can fit. Avoid jokes about holes, digging, or exterminating creatures.

### Image direction

Use only if produced:

```text
gfx/super_events/018_resources_found/super_event_018_global_defeat.dds
GFX_super_event_018_global_defeat
```

The image shows a final sealed chasm, damaged industrial ruins, multinational engineers, abandoned anti-armor weapons, and survivors.

### Audio mood

Unique licensed final music. Desired shape:

- reflective opening
- restrained relief
- audible cost and aftermath
- not a victory march
- 1 to 2 minutes
- no reuse of emergence or world-end tracks

## Audio research workflow

For each super-event:

1. Check existing approved repository tracks and documentation for suitability and uniqueness.
2. Reject any track without verified title, creator or composer, source, license, and duration.
3. Search legitimate public-domain, Creative Commons, archive, government, institutional, or clearly licensed sources.
4. Verify composition and recording rights separately.
5. Compare several candidates.
6. Select one final track that fits the exact role.
7. Preserve the original downloaded source under the Event 018 docs asset package.
8. Trim, remove silence, normalize carefully, and fade where useful.
9. Convert final WAV to 44.1 kHz.
10. Prepare matching sound file if the current super-event system requires it.
11. Document exact editing and conversion steps.
12. Propose final unique audio ID and sound wrapper.

No fallback audio is allowed. If no legally usable track is found, mark the super-event audio blocked.

## Quote and remark research workflow

For each super-event:

1. Find at least several main quote candidates.
2. Find several button or cultural remark candidates.
3. Verify exact wording and attribution through reliable sources.
4. Record source work, date, translation where relevant, confidence, and copyright status.
5. Reject unsourced quote-site wording and invented lines.
6. Prefer public-domain main quotes.
7. Keep modern copyrighted direct references very short.
8. Select one complete package and at least one backup.
9. Explain why the selected main quote fits this role and not the other Event 018 super-events.

## Research note required fields

For each package record:

- role
- final trigger
- selected title
- description direction and final implementation text status
- selected button or remark
- source and copyright note for the remark
- considered main quotes
- selected quote
- author or speaker
- source work or document
- year or period
- source URL
- attribution confidence
- public-domain or copyright note
- image path and sprite
- audio candidates
- selected track title
- composer or creator
- performer or recording source
- source URL
- license and confidence
- duration
- attribution text
- original source path
- final WAV path
- final WAV path if used
- audio ID
- super-event slot
- editing steps
- implementation notes
- uncertainty or blocker

## Final implementation requirements

The main implementation agent must:

- choose and reserve unique super-event slots
- write final localisation keys in existing format
- wire scripted localisation for image, title, description, button, and quote
- wire image sprites in the correct GFX file
- define unique audio IDs and volume variants
- add representative entries to the super-event music station
- add sound wrappers where required
- set `global.current_super_event_audio_id`
- use the settings-aware playback helper
- trigger the correct event effects
- update the Event 018 doc
- update `music/chaosx_music_track_list.html` with every track and super-event ID
- update the catalog workbook where relevant
- validate final paths, sample rate, IDs, slots, and text alignment

## Completion standard

No Event 018 super-event is complete until its title, description, button, quote, image, audio, unique IDs, playback, trigger, docs, music table, and catalog alignment are final and verified. Research directions and working labels are blockers, not pasteable localisation. Default audio, reused audio without approval, generated tones, unclear licenses, placeholder images, invented quotes, and unsourced remarks are forbidden.
