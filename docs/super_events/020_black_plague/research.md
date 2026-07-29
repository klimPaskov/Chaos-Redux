# Event 020 Black Plague super-event research

This note records the audio package for the Rat King coronation and Rat King world-end super-events. Parent-owned text, image, event, localisation, GFX, sound-definition, and music-registry wiring must be merged here before the full Event 020 super-event package is called complete.

## Roles and audio decisions

| Super-event | Role | Selected audio | Proposed playback ID | Final duration |
| --- | --- | --- | ---: | ---: |
| Rat King coronation | Global transformation: scattered broods become one sentient sovereign | Kevin MacLeod, `Gregorian Chant`, edited chant-style processional | 101 | 110.000000 s |
| Rat King world end | Terminal takeover after the Rat King world-end path | Gregorian chant sequence `Dies irae`, recording by Membeth | 102 | 103.650000 s |

The cues are unique to Event 020 and are not reused from another super-event. Audio ID 101 uses the named Kevin MacLeod recording because the author, source, and CC BY 3.0 terms are explicit. Audio ID 102 uses the public-domain Membeth recording because its worldwide dedication is explicit and the medieval composition is public domain. The source evidence, API metadata, legal-code snapshots, hashes, and conversion ledger are kept in `docs/assets/020_black_plague/source_audio/evidence/` and `docs/assets/020_black_plague/audio_manifest.md`.

## Audio ID 101: Rat King coronation

- Title: `Gregorian Chant` (final in-game cue title: Rat King Coronation - Gregorian Chant Excerpt).
- Composer, creator, and performer: Kevin MacLeod.
- Source: Wikimedia Commons `File:KevinMacLeod - Gregorian Chant.ogg`, imported from the creator's SoundCloud track <https://soundcloud.com/kevin-9-1/gregorian-chant>.
- Source URL: <https://commons.wikimedia.org/wiki/File:KevinMacLeod_-_Gregorian_Chant.ogg>; frozen page revision <https://commons.wikimedia.org/w/index.php?title=File:KevinMacLeod_-_Gregorian_Chant.ogg&oldid=1044292914>.
- Licence: Creative Commons Attribution 3.0 Unported (<https://creativecommons.org/licenses/by/3.0>). Sharing and adaptation are permitted with attribution, licence link, and change notice; no implied endorsement. Composition and recording are both credited to the named contemporary creator.
- Licence confidence: high. The source page names Kevin MacLeod as author, links the originating SoundCloud track, identifies CC BY 3.0, and the preserved file SHA-1 matches the Commons API (`3462dd0732223ee7b7815f8fb04a55415b3bf673`).
- Preserved original: `docs/assets/020_black_plague/source_audio/kevin_macleod_gregorian_chant_commons_original.ogg` (194.000000 s, 44,100 Hz stereo, SHA-256 `d4ec1fe983170ab5f315a54770fdcb0e43992e41166d194a3ae8a1e01041a804`).
- Final sound file: `sound/020_black_plague/super_event_101_rat_king_coronation.wav` (110.000000 s, 44,100 Hz stereo signed 16-bit PCM, SHA-256 `4b717c9744c4a9a3c4ecf5997d55b8a8f1a708226e3d47a3c1fc2f9cd4425722`).
- Editing: source-relative `0.608345-110.608345 s`; initial silence removed; loudness normalized to `-19.9 LUFS` (`5.3 LU LRA`); 1.5-second fade-in; 6-second fade-out; stereo 16-bit PCM render; 44.1 kHz output; Ogg Vorbis quality 6. No generated tone, oscillator, drone, or placeholder was used.
- Attribution: `Kevin MacLeod, “Gregorian Chant”; source via Wikimedia Commons and SoundCloud; CC BY 3.0. Edited, faded, loudness-normalized, resampled, and excerpted by Chaos Redux.`
- Fit: the creator's deliberately unreal chant-style processional reads as an uncanny court ritual, making the public realization of a sentient Rat King feel like a crowned transformation rather than a generic disaster.

## Audio ID 102: Rat King world end

- Title: `Dies irae` (final in-game cue title: Rat King World End - Dies Irae Excerpt).
- Composer or work: traditional medieval Requiem sequence, commonly attributed to Tommaso da Celano; the source page identifies it as Gregorian chant. The sequence's composition is public domain by age.
- Performer and recording source: Membeth, own Gregorian-chant recording dated 12 August 2010.
- Source URL: <https://commons.wikimedia.org/wiki/File:Dies.irae.ogg>; frozen page revision <https://commons.wikimedia.org/w/index.php?title=File:Dies.irae.ogg&oldid=1205385897>.
- Licence: public-domain dedication by the recording author, released worldwide with no conditions (<https://creativecommons.org/publicdomain/zero/1.0/> legal-code snapshot retained locally). Attribution is not required; courtesy credit is recommended.
- Licence confidence: high for the recording and composition. The source page identifies the recording author, states a worldwide public-domain release, and the preserved file SHA-1 matches the Commons API (`d13e914db3016ab43bcb89c695e501ac8fd19605`). Historical authorship of the medieval sequence is not needed to establish its public-domain status.
- Preserved original: `docs/assets/020_black_plague/source_audio/dies_irae_membeth_commons_original.ogg` (434.000952 s, 44,100 Hz stereo, SHA-256 `a94c57586d3215a4ecb67a5eb9701b387be39bef2f53abaa3e3b2214a2e9472e6`).
- Final sound file: `sound/020_black_plague/super_event_102_rat_king_world_end.wav` (103.650000 s, 44,100 Hz stereo signed 16-bit PCM, SHA-256 `7240f9bddc19955fde7c56ef9d15381d87a84ba7ce39f6c5bf3663b67ab0221f`).
- Editing: source-relative `0.905760-104.555760 s`, ending at the first long chant pause; initial silence removed; loudness normalized to `-20.3 LUFS` (`11.7 LU LRA`); 1.5-second fade-in; 6-second fade-out; stereo 16-bit PCM render; 44.1 kHz output; Ogg Vorbis quality 6. No generated tone, oscillator, drone, or placeholder was used.
- Courtesy attribution: `Gregorian chant, “Dies irae”; recording by Membeth; source via Wikimedia Commons; public domain. Edited, faded, loudness-normalized, resampled, and excerpted by Chaos Redux.`
- Fit: the opening sequence's ritual judgment and natural pause give the terminal takeover a final, liturgical weight while remaining short enough for the super-event window.

## Parent wiring handoff

Use `docs/assets/020_black_plague/audio_manifest.md` for the exact six-level registry names, sound wrapper names, paths, volume ladder, and attribution text. Proposed wrappers are `chaosx_super_event_rat_king_coronation_track` and `chaosx_super_event_rat_king_world_end_track`; proposed six-level soundeffect families are `chaosx_super_event_101_sound_*` and `chaosx_super_event_102_sound_*`. Set `global.current_super_event_audio_id` to `101` or `102` through the existing settings-aware helper. Add both final rows to `music/chaosx_music_track_list.html` with the final display-slot IDs. This audio researcher did not edit those shared wiring files.

## Non-selected leads and optional branch

`De profundis.ogg` was not selected because its Commons page leaves the author field blank despite CC BY-SA licensing, so the composition/recording attribution split was not strong enough for a final package. `Rorate Caeli ~ Gregorian Chant.ogg` was not selected because the recording is less directly suited to the coronation role. The optional defeat-aftermath cue is intentionally not prepared until the parent confirms that the long/global-war eligibility gate remains in the accepted implementation.

## Required parent additions

The parent must still add final title/description/remark/quote localisation, generated 457x328 images and GFX mappings, super-event slot flags, settings-aware event wiring, sound definitions, catalogue rows, event docs, and any workbook alignment. No fallback or default audio is authorized for either completed super-event.

## Text research package

This section records the bounded text-research pass for the Rat King coronation and Rat King world-end packages. It does not authorize or perform localisation, scripted-localisation, event, image, GFX, audio, sound-definition, or workbook edits.

### Rat King coronation

Role: global transformation. Scattered broods become one sentient sovereign, with organized movement, captured human spaces, and a public realization that the rats now obey one command.

Selected main quote: “And out of the houses the rats came tumbling.”

- Author: Robert Browning.
- Work: *The Pied Piper of Hamelin*, a narrative poem first published in *Dramatic Lyrics* (1842); the consulted illustrated edition is an 1888 printing.
- Source: [Project Gutenberg text](https://www.gutenberg.org/files/18343/18343-h/18343-h.htm); [Morgan Library publication record](https://www.themorgan.org/printed-books/166062).
- Attribution confidence: high. The line appears in the poem's rat-emergence passage and the Project Gutenberg title page identifies Browning as author.
- Rights: public-domain nineteenth-century poem. Project Gutenberg states that its edition may be copied or reused under its license, and Browning died in 1889.
- Fit: this is the only candidate that names the rats directly and shows them issuing from human dwellings in a coordinated mass. It favors ominous emergence and movement, so the description must supply the sovereign/court dimension rather than making the quote carry kingship alone.

Coronation backup main quote: “Uneasy lies the head that wears a crown.”

- Speaker and source: King Henry IV in William Shakespeare's *Henry IV, Part 2*, Act 3, scene 1, line 31.
- Source: [Folger Shakespeare Library text and citation](https://www.folger.edu/explore/shakespeares-works/henry-iv-part-2/).
- Date and confidence: early-modern play, conventionally dated c. 1598–1600; attribution confidence high because the Folger edition identifies the speaker and exact line.
- Rights: Shakespeare's text is public domain by age.
- Fit: directly announces the burden of the new crown and can support a coronation image dominated by the throne or leader portrait. It is less species-specific and should remain the backup if the package's visual emphasis is on royal legitimacy rather than the broods' emergence.

Selected coronation button remark: “Sic transit gloria mundi.”

- Source and meaning: traditional Latin ritual admonition, “Thus passes the glory of the world,” used during papal coronation/inauguration rites.
- Source: [Vatican Publishing House account of the Petrine inauguration rite](https://www.vatican.va/news_services/liturgy/2006/documents/ns_lit_doc_20061221_ministero-petrino_en.html), which names the former coronation rite “sic transit gloria mundi.”
- Date and confidence: the phrase is traditional and older than the cited 2006 Vatican discussion; attribution confidence high for the cultural reference, but it is not a line by a single author.
- Rights: traditional Latin phrase with no modern copyrighted-work risk.
- Fit: the phrase sounds like a court's ceremonial warning while the world watches a new sovereign rise. It gives the button a cold, fatalistic edge and keeps the coronation from reading as a triumphant generic monarchy.

Coronation button backup: “Uneasy lies the head that wears a crown.” This is the same verified Shakespeare line above and is safe to reuse as the button only if it is not also chosen for the main quote.

Other coronation candidate considered and not selected: “All hope abandon, ye who enter in!” from Dante's *Inferno* is too terminal for a transformation event, while “A plague o’ both houses!” is stronger for the world-end button because its immediate dramatic context is a dying speaker's curse.

### Rat King world end

Role: terminal scenario. The Rat King has completed the world-end path, controls the required territory, and begins the final transfer into a globally organized burrow order.

Selected main quote: “And I looked, and behold a pale horse: and his name that sat on him was Death.”

- Source: Revelation 6:8, King James Version. This is the exact opening sentence of the verse; the complete verse continues with power over a fourth of the earth and killing by sword, hunger, death, and beasts.
- Source: [Bible Gateway Revelation 6:8 KJV](https://www.biblegateway.com/passage/?search=Revelation+6%3A8&version=KJV); [Bible Gateway KJV version-rights page](https://www.biblegateway.com/versions/King-James-Version-KJV-Bible?vm=r).
- Date and confidence: first-century Christian scripture, in the 1611 King James translation; attribution confidence high for the verse and translation.
- Rights: Bible Gateway labels the KJV public domain in the United States. The United Kingdom's Crown-rights treatment of the Authorized Version is a separate jurisdictional caveat, but the cited text is the project's established public-domain candidate.
- Fit: the pale horse and named Death give the terminal takeover a final judgment register without pretending that the Rat King is a biblical figure. The omitted continuation remains visible in the source and is why this short excerpt still carries plague, beasts, and mass mortality associations.

World-end backup main quote: “Therefore hath the curse devoured the earth, and they that dwell therein are desolate.”

- Source: Isaiah 24:6, King James Version.
- Source: [Bible Gateway Isaiah 24:6 KJV](https://www.biblegateway.com/passage/?search=Isaiah+24%3A6&version=KJV).
- Date and confidence: Hebrew prophetic text traditionally associated with Isaiah's eighth-century BCE setting; the English wording is the 1611 KJV. Attribution confidence high for the verse and translation, with the usual historical uncertainty around individual prophetic composition dates.
- Rights: Bible Gateway labels the KJV public domain in the United States, with the same United Kingdom Crown-rights caveat.
- Fit: this candidate is more directly about emptied habitations and a consumed earth than Revelation 6:8. It is the strongest backup if the terminal description foregrounds abandoned human cities and demographic absence over a named rider.

Additional world-end candidate considered: “Nothing beside remains.”

- Author and work: Percy Bysshe Shelley, “Ozymandias,” first published in 1818.
- Sources: [Project Gutenberg's Shelley text](https://www.gutenberg.org/cache/epub/4798/pg4798.html); [Poetry Foundation text and context](https://www.poetryfoundation.org/poems/46565/ozymandias/).
- Attribution confidence: high for the poem and line, though editions vary in capitalization and punctuation elsewhere in the sonnet.
- Rights: Shelley died in 1822; the poem is public domain. The Project Gutenberg edition is a 1914 scholarly text presented as public domain in the United States.
- Fit: the fragment is brutally concise and evokes human monuments reduced to absence. It is less plague-specific than Revelation or Isaiah and can feel like a generic ruin line, so it remains an alternate rather than the selected main quote.

Selected world-end button remark: “A plague o’ both houses!”

- Speaker and source: Mercutio in William Shakespeare's *Romeo and Juliet*, Act 3, scene 1, line 1562.
- Source: [Folger Shakespeare Library full text](https://www.folger.edu/explore/shakespeares-works/romeo-and-juliet/read/).
- Date and confidence: early-modern play, conventionally dated c. 1595; attribution confidence high because the Folger text gives the speaker and line. The immediate continuation later repeats “A plague o’ both your houses!” and invokes “a dog, a rat, a mouse, a cat,” which makes the allusion unusually apt for Event 20 without altering the selected five-word fragment.
- Rights: Shakespeare's text is public domain by age.
- Fit: the button is short, bitter, and unmistakably plague-coded. Its original dramatic context is a dying character cursing feuding houses, so it reads as a final human reproach while the Rat King inherits the emptied cities.

World-end button backup: “All hope abandon, ye who enter in!”

- Source: the inscription on the gate in Dante Alighieri's *Inferno*, Canto III, in Henry Wadsworth Longfellow's nineteenth-century English translation.
- Source: [Project Gutenberg edition of Longfellow's *Divine Comedy, Hell*](https://www.gutenberg.org/cache/epub/1001/pg1001-images.html).
- Date and confidence: Dante's *Inferno* was completed c. 1320; Longfellow's translation is nineteenth century. Attribution confidence high for the line and translation, and the source explicitly identifies both Dante and Longfellow.
- Rights: Dante's original and Longfellow's translation are public domain by age. Project Gutenberg marks the edition as derived from texts not protected by U.S. copyright.
- Fit: this is the cleanest cold terminal-gate remark, but it emphasizes infernal entry rather than plague or rat rule. It is therefore a backup, not a replacement for the selected Shakespearean plague curse.

### Copyright and wording risk

No modern copyrighted song, film, game, or contemporary book line is selected. Every recommended direct reference is public-domain literature/scripture or a traditional liturgical phrase. If a modern cultural allusion is later preferred for a button, keep it to a very short fragment or title-like reference and record the exact source and rights status before localisation.

Do not replace the Dante wording with the common paraphrase “Abandon all hope, ye who enter here” without marking it as a paraphrase. The verified Longfellow text is “All hope abandon, ye who enter in!”

### Parent implementation recommendation

Use the Browning line for the coronation `.q` and the Vatican phrase for the coronation `.a`; use the Revelation excerpt for the world-end `.q` and the Shakespeare plague curse for the world-end `.a`. Preserve quotation punctuation and attribution in the research record, keep author/work references in any quote-attribution localisation separate from player-facing description text, and do not expose hidden thresholds or implementation mechanics in the final descriptions.
