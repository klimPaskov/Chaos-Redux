# Event 013 Natural Disasters, super-event research handoff matrix

This matrix is a research handoff for `chaos-redux-super-events` and the narrow super-event research subagents. It does not provide final titles, final quotes, final button text, slogans, lyric fragments, cultural remarks, or audio choices. Every source-dependent text and every track remains blocked until researched, verified, licensed, and documented.

## Research roles

| Role | Subagent or skill | Output expected |
| --- | --- | --- |
| Main quote research | `chaosx_super_event_text_researcher` | Several sourced quote candidates, selected quote, attribution confidence, source URL, copyright note. |
| Cultural remark research | `chaosx_super_event_text_researcher` | Short remark or allusion candidates, source notes, copyright risk, selected recommendation. |
| Audio research | `chaosx_super_event_audio_researcher` | Legal track candidate, source file, final WAV, license note, duration, sound ID direction. |
| Image production | `chaosx_generated_event_art` or `chaosx_asset_source_researcher` | Super-event image source, processed preview, DDS, manifest, gfx handoff. |
| Main implementation | parent coding agent | Slot wiring, scripted localisation, settings-aware playback, image sprite, docs, spreadsheet alignment. |

## Super-event candidate matrix

| Working role label | Trigger moment | Quote theme direction | Cultural remark theme direction | Audio mood constraints | Image prompt direction | Blockers before implementation |
| --- | --- | --- | --- | --- | --- | --- |
| `se_013_first_abnormal_skyfall` | First major meteor shower or meteor impact causes severe multi-state deaths or damage. | Public domain or historical writing about falling stars, omens, sky terror, human smallness, or sudden ruin. Avoid unsourced quote-site astronomy lines. | Short allusion to watching the sky, night lights, or a culturally known omen. Keep modern references brief and source checked. | Real music only, tense and sparse at first, then heavy percussion or choir acceptable. No drones, beeps, oscillator cues, or unlicensed film music. | Generated period-documentary night scene with civilians, soldiers, or rail workers under multiple fire trails in the sky, no readable text. | Verified quote, verified remark if used, licensed audio, generated image, unique slot, no raw final title from this matrix. |
| `se_013_whole_earth_rupture` | Whole-earth rupture wave begins and hits several regions or schedules global aftershocks. | Religious, philosophical, or historical text about the earth shaking, foundations, judgment, or fragile cities. Public domain preferred. | Grim understatement from a traceable literary, religious, or period source. Avoid direct apocalypse clichés. | Large orchestral, choral, or organ mood with weight and low motion. Must be licensed and final length documented. | Generated global seismic crisis composition with broken rail, cracked city streets, and distant coast disturbance, period plausibility, no modern rescue branding. | Event 046 placeholder documented separately, quote source verified, audio license verified, no reuse of old Earth Earthquake logic. |
| `se_013_massive_eruption_crisis` | Massive eruption crisis devastates a volcanic region and starts ashfall, lahar, or food-chain pressure. | Source themes around volcanoes, ash, buried cities, fire mountains, nature overwhelming human plans. Classical, scripture, and public domain travel writing can be candidates. | Cultural remark direction can draw from old volcano myths, classical references, or period disaster journalism. Must be sourced. | Dark ritual-like orchestral or choral piece, or solemn classical movement. Avoid pure ambience. | Generated volcanic super-event scene with ash plume, port or rail workers, darkened fields, and evacuation columns, strong central plume. | Need image distinct from normal eruption report, licensed audio, no final myth reference without verification. |
| `se_013_ocean_impact_tsunami_train` | Ocean meteor impact, volcanic collapse, or rupture schedules a large delayed tsunami chain across several coasts. | Quotes about the sea, waves, flood, or coast destruction from public domain literature, scripture, maritime writing, or historical disaster accounts. | Short maritime allusion, prayer, or proverb direction. Avoid modern song lyric unless extremely brief and legally safe. | Slow swell, choral or maritime lament, rising dread. Must not be a storm sound effect bed. | Generated coast scene showing withdrawn harbor, stranded boats, civilians climbing roads, and distant wave shape, no text. | Need arrival-order UI verified, quote and remark source checked, audio rights checked. |
| `se_013_storm_corridor` | Moving storm or tornado corridor crosses multiple states and the abnormal map becomes active globally or regionally. | Quotes about wind, storm, fate, or houses and foundations from public domain sources. Avoid generic disaster lines. | Cultural remark can draw from storm folklore, old weather sayings, or period local phrase direction after source review. | Fast but structured music with motion, strings or percussion, not a looping wind sound. | Generated map-adjacent period scene with rail corridor, damaged towns, and a visible storm wall moving behind them. | Needs animated path assets or accepted static fallback, verified text sources, unique audio. |
| `se_013_disaster_barrage_maximum` | Manual Disaster Barrage Maximum intensity starts several abnormal families in one season. | Quote themes about human helplessness before many calamities, old catastrophe literature, or judgment without using final apocalypse wording. | Brief allusion to a catalogue of plagues, trials, or impossible weather, source checked. | Large, intense, but not terminal. Music should feel like a challenge launch, not campaign ending. | Generated composite scene with multiple disaster signs in one period landscape, readable at super-event size and not a flat collage. | Manual scenario context must be clear, no world-end framing, all audio and text sources verified. |
| `se_013_global_recovery_aftershock` | Optional rare aftermath super-event only if an abnormal season causes enormous losses and many countries still have active aftermath cards after a long recovery period. | Quotes about rebuilding, memory, responsibility, and endurance from public domain or historical sources. | Cultural remark direction should be restrained, reflective, and source checked. | Reflective orchestral, hymn, or solemn march. Avoid triumphant victory tone. | Generated reconstruction scene with rail crews, shelters, damaged port, and ruined factories under clearing sky, no readable text. | Use only if implementation proves the campaign moment deserves it. Do not create this as default bloat. |

## Quote research constraints

- Do not invent quotes.
- Prefer public domain, religious, classical, philosophical, historical, or literary sources for main quotes.
- Use several candidates before selecting one.
- Record exact wording, source, translator if relevant, year or period, source URL, confidence, and copyright note.
- If attribution is uncertain, either mark it uncertain or choose another quote.

## Cultural remark constraints

- Remarks can be short and sharper than the main quote, but they still need source checks when they allude to a song, film, book, poem, proverb, scripture, speech, or slogan.
- Modern copyrighted material must stay very short and should usually be an allusion, not a long direct line.
- Do not convert a working role label into button text.

## Audio constraints

- Every final super-event needs a unique final track and unique audio id unless the user explicitly approves reuse.
- Final music must be real licensed or public domain music, not generated test tones, primitive waveforms, abstract drones, or placeholder ambience.
- Final WAV must be documented with title, creator or composer, performer or recording source if known, source URL, license, duration, edit steps, final path, and sound ID direction.

## Image constraints

- Generated images are preferred for abnormal fictional disaster scenes.
- Sourced images are only preferred when the super-event must depict a real historical photograph or specific real object.
- Super-event images need strong central composition, period-appropriate visual direction, no readable generated text, no modern rescue branding, no modern vehicles unless the mod context intentionally allows it.
