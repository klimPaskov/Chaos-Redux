# 020 Black Plague super-event prompt

Use `chaos-redux-super-events`. Use `chaosx_super_event_text_researcher` for quotes, title research, button remarks, cultural references, source confidence, and copyright notes. Use `chaosx_super_event_audio_researcher` for licensed or public domain music. Use `chaosx_generated_event_art` for fictional super-event images unless the implementation explicitly needs a sourced historical image.

Do not use unresearched final titles, button text, quotes, slogans, song fragments, allusions, or final audio choices. Treat them as blockers until researched and documented.

All package labels below are working labels only.

## Required package A: King reveal

Role: transformation and global escalation.

Trigger direction:

- Evolution IV creates the King of Rats as a separate country
- rat nations are transferred, absorbed, or unified under the King according to implementation
- King focus tree and world-threat behavior become active
- human countries can observe that scattered warren states now follow one command

Tone direction:

- organized nonhuman sovereignty
- fear should come from visible coordination, plague states answering the crown, empty towns, broken cordons, and disciplined swarm movement
- do not reveal the hidden world-end path in public text
- avoid generic apocalypse language

Title direction:

- short and specific to rat sovereignty, coronation, or organized warren rule
- research required before final localisation

Description direction:

- describe a public threshold in the campaign
- focus on what observers can see, such as coordinated attacks, marked ruins, plague routes moving together, and a new ruler or court below the surface
- avoid mechanics summary

Quote direction:

- compare several real, traceable quotes about pestilence, beasts, hunger, sovereignty, ruins, judgement, or the fall of human dominion
- prefer public domain literature, scripture, medieval or early modern writing, folklore scholarship, political writing, or historical sources
- avoid unsourced quote-site material

Button remark direction:

- grim, bitter, or restrained
- a short folklore, literary, religious, or historical allusion may fit if sourced
- modern copyrighted references must be very short and copyright-safe

Image direction:

- generated fictional super-event image
- 457x328
- strong central composition of the rat sovereign, rat court, or organized warren force
- period-compatible HOI4 super-event tone
- no readable generated text
- avoid generic map tables, abstract skull icons, and modern horror poster styling

Audio direction:

- unique real licensed or public domain music
- oppressive, ritual, choral, court-like, funeral, or low martial tone
- no generated tones, oscillator cues, drones, sound-effect beds, or placeholder tracks

## Required package B: rat world-end

Role: terminal world-end scenario.

Trigger direction:

- the King completes the world-end focus path
- required continent, state-set, or accepted equivalent is controlled
- death pressure, rat-held territory pressure, or plague-state pressure meets the spec threshold
- normal world-end rules are satisfied

Tone direction:

- final campaign state
- human order has collapsed into rat sovereignty and Black Death ecology
- the description should make the end-state clear without a long mechanics explanation
- avoid generic final-crisis wording

Title direction:

- short terminal title tied to rat world, inheritance, crown, or end of human dominion
- research required before final localisation

Description direction:

- visible world-end state: rat-held roads, plague-darkened cities, ruined human symbols, organized warrens, and a world no longer governed by humans
- no hidden formula dump

Quote direction:

- compare real sourced quotes about ruin, judgement, beasts inheriting human spaces, plague, extinction, fallen kingdoms, or the end of pride
- public domain or religious texts may be strongest if they fit
- verify exact wording and translation status

Button remark direction:

- short, grim, and final
- researched allusion allowed if it fits and passes copyright rules

Image direction:

- generated fictional super-event image
- 457x328
- vast rat-held capital or world under rat dominion
- black fog, ruined human symbols, crown or warren geometry
- no readable text

Audio direction:

- unique real track distinct from King reveal
- final, choral, processional, funeral, or dark orchestral direction
- source, license, duration, and conversion notes required

## Optional package C: continental rat threat escalation

Use only if the implementation accepts a middle threshold between King reveal and world-end.

Trigger direction:

- King controls a major share of a continent or event-defined continent group
- world-end path is not complete
- human powers still have a meaningful chance to stop the King

Role direction:

- regional order collapse and emergency cooperation
- opens or amplifies anti-rat coalition behavior if implemented
- should not duplicate the rat world-end package

Presentation acceptance:

- use a super-event only if the threshold is campaign-defining
- otherwise use a major news event, event log, and disease board escalation

Research gates:

- title, quote, button remark, image, and audio remain blocked until a super-event pass accepts this package

## Optional package D: rat defeat aftermath

Use only if the King was a global or near-global threat.

Trigger direction:

- King is defeated after controlling a large region, causing massive deaths, or nearing world-end path completion
- major warren remnants are cleaned or contained enough to declare the war ended
- this must not fire for a small base warren defeated early

Role direction:

- costly survival and long cleanup
- reflective aftermath, not triumphant celebration
- the world remembers the missing population, ruined infrastructure, and ongoing vigilance

Quote direction:

- real sourced quotes about survival, memory, recovery, vigilance, ruins, or the cost of victory

Image direction:

- likely generated period-documentary aftermath scene
- cleanup lines, medical crews, soldiers, black fog residue, ruined districts
- 457x328 if super-event, news or report size if implemented as smaller presentation

Audio direction:

- reflective music, not victory fanfare

## Research note requirements

For every implemented super-event, produce a research note under a stable `docs/super_events/` or event-scoped research path.

The note must include:

- package role
- trigger direction
- considered title candidates if researched
- considered quote candidates
- selected quote
- speaker or author
- source work, speech, scripture, document, archive, or collection
- year or approximate period if known
- source URL
- attribution confidence
- copyright or public domain note
- considered button remark or cultural allusion candidates
- selected button direction or final remark after research
- audio candidates
- selected track title
- creator or composer
- performer or recording source if relevant
- source URL
- license and use terms
- duration
- source audio path
- final in-game audio path
- suggested sound definition id
- image direction and asset handoff path
- uncertainties

## Implementation handoff requirements

The main implementation agent owns final wiring:

- super-event slot and visibility flag
- `global.current_super_event_audio_id`
- settings-aware playback helper
- scripted localisation
- player-facing localisation after research
- image `.gfx` wiring
- audio definitions
- docs and spreadsheet alignment

Do not wire a completed super-event with missing audio, placeholder image, unverified quote, or unresearched title. If a package is blocked, report it plainly.
