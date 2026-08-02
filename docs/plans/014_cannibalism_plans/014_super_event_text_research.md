# Event 014 Cannibalism super-event text research

## Status and scope

This handoff supplies the final proposed English text and verified quotation research for four Event 014 super-events:

- `49`: Hannibal Lecter reveal
- `50`: ordinary Hannibal worldwide victory and world-end
- `52`: eligible global defeat aftermath
- `53`: transformed Hannibal Lecter worldwide victory and world-end

The research was completed on 2026-07-11 after reading the complete Event 014 spec package, the super-event and subagent skills, the offline HOI4 references required by `AGENTS.md`, the live super-event GUI, the live scripted-localisation getters, and the Event 014 audio handoff.

This file is the only file changed by the text researcher. No gameplay, localisation, scripted localisation, GUI, GFX, audio, spreadsheet, or catalog file was edited.

Hannibal Lecter is the revealed Event 014 leader. Text and art use the package's alternate-history interpretation without copying a specific screen actor.

## Interface interpretation

The live super-event window has four text getters:

- `GetSuperEventTitle` reads `.t`
- `GetSuperEventDesc` reads `.d`
- `GetSuperEventQuote` reads `.q`
- `GetSuperEventRemark` reads `.a`

There is no separate subtitle getter or `.s` key. In this handoff, the requested subtitle surface is the quotation block `.q`, which appears beneath the UI label `Quote of the Day`. Do not invent a fifth localisation key without an intentional GUI change.

The recommended normal-localisation target is `localisation/english/014_cannibalism_l_english.yml`, encoded as UTF-8 with BOM. Keys must have no `:0` suffix and no leading space.

## Final recommendation

| Slot | Role | Final title | Selected quotation source | Audio ID |
| ---: | --- | --- | --- | ---: |
| `49` | Hannibal Lecter reveal | `Hannibal Lecter Commands` | Thomas Hobbes, *Leviathan* | `49` |
| `50` | Ordinary worldwide victory | `The World Is the Larder` | William Shakespeare, *King Lear* | `50` |
| `52` | Eligible global defeat aftermath | `The Burial Detail` | Walt Whitman, *Specimen Days* | `52` |
| `53` | Wendigo worldwide victory | `No Thaw Will Come` | Lord Byron, *Darkness* | `53` |

All titles, descriptions, and option remarks are original Chaos Redux copy. The option remarks are not borrowed cultural references and need no external attribution.

## Slot 49: Hannibal Lecter reveal

### Final localisation proposal

```yaml
chaosx_super_event.49.t: "Hannibal Lecter Commands"
chaosx_super_event.49.q: "\"A Multitude of men, are made One Person, when they are by one man, or one Person, Represented\"\n §Y-Thomas Hobbes, Leviathan-§!"
chaosx_super_event.49.a: "The scattered knives have found a hand."
chaosx_super_event.49.d: "The identical maps, rank tables, prisoner ledgers, and synchronized attacks have acquired a public author. Hannibal Lecter has taken command of the strongest Host and summoned the warlords to his standard.\n\nNo government can determine how much of the network Hannibal designed before claiming it as his own. The warlords have accepted his command, and their armies, islands, and feeding territories now move together."
```

### Ranked quotation candidates

1. Selected quotation in `.49.q`

   - Author and work: Thomas Hobbes, *Leviathan*, chapter XVI, 1651.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/cache/epub/3207/pg3207-images.html).
   - Fit: The line describes a multitude becoming one represented person. It mirrors the warlords and cells becoming one military state under a visible commander.
   - Attribution confidence: High. The wording is verified in the cited text.
   - Rights: Public domain. Hobbes died in 1679 and the work was published in 1651. Project Gutenberg distributes the cited edition as a public-domain text in the United States.
   - Text note: Capitalisation and commas vary in modern editions. Preserve the cited early-modern wording if it is presented as an exact quotation.

2. `Awake, arise, or be for ever fallen!`

   - Author and work: John Milton, *Paradise Lost*, Book I, 1667.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/files/26/26-h/26-h.htm).
   - Fit: A defeated host rises at its commander's call. It gives the reveal a martial and infernal rallying tone.
   - Attribution confidence: High.
   - Rights: Public domain. Milton died in 1674 and the work was first published in 1667.
   - Ranking note: Strong, but more theatrical and less specifically about unification than the Hobbes line.

3. `Th' abuse of Greatnesse, is, when it dis-ioynes Remorse from Power`

   - Author and work: William Shakespeare, *Julius Caesar*, Act II, scene 1, first performed around 1599. The cited wording follows the First Folio text of 1623.
   - Exact source: [Project Gutenberg First Folio transcription](https://www.gutenberg.org/ebooks/1120.txt.utf-8), with [public-domain metadata](https://www.gutenberg.org/ebooks/1120).
   - Fit: It frames the reveal as power stripped of restraint.
   - Attribution confidence: High for the cited First Folio transcription.
   - Rights: Public domain. Shakespeare died in 1616 and Project Gutenberg marks this edition public domain in the United States.
   - Ranking note: The original spelling is visually distracting in the compact quote box. Modernising it would create an adaptation rather than an exact quotation.

### Spoiler review

- This text is safe only after the Evolution III reveal flag is set in the same effect chain.
- The title and body name Hannibal and therefore must never be used as a default scripted-localisation branch.
- The body preserves the required uncertainty about Hannibal's origin and how much of the earlier network he personally designed.
- No quotation redirects the reveal toward a different historical subject.
- The famous feared-versus-loved passage from *The Prince* was rejected because its surrounding context distracts from Hannibal Lecter's own reveal.

### Audio alignment

- Audio ID: `49`.
- Final cue: Saint-Saëns, *Danse macabre, Op. 40*, Philadelphia Symphony Orchestra under Leopold Stokowski, 1925.
- Final file: `sound/014_cannibalism/super_event_49_hannibal_reveal.wav`.
- Duration: `114.000 s` with a `0.25 s` fade-in.
- Sync note: The first sentence reveals the name and command immediately, matching the cue's immediate macabre motion. Set slot `49` and audio ID `49` before calling `play_current_super_event_audio`. No delayed text change or timed voice line is needed.

## Slot 50: ordinary Hannibal worldwide victory

### Final localisation proposal

```yaml
chaosx_super_event.50.t: "The World Is the Larder"
chaosx_super_event.50.q: "\"Humanity must perforce prey on itself,\nLike monsters of the deep.\"\n §Y-William Shakespeare, King Lear-§!"
chaosx_super_event.50.a: "Nothing will be left uncounted."
chaosx_super_event.50.d: "The last limits on Hannibal Lecter's command have been struck from its ledgers. Warlord armies, prison routes, silent ports, and feeding states answer a single timetable, carrying each conquest into the next.\n\nEvery country outside the Host has been named as prey. Its armies march in the certainty that each ruined city will furnish the next advance and each defeated population will be counted as supply."
```

### Ranked quotation candidates

1. Selected quotation in `.50.q`

   - Author and work: William Shakespeare, *King Lear*, Act IV, scene 2, written around 1605 to 1606 and first printed in 1608.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/files/1532/1532-h/1532-h.htm).
   - Fit: The line directly turns humanity into its own predator and matches the ordinary route's human-origin world consumption.
   - Attribution confidence: High. The work date is approximate, but the wording and attribution are secure.
   - Rights: Public domain. Shakespeare died in 1616 and the play has been public domain for centuries.

2. `who enlargeth his desire as Sheol, and he is as death, and cannot be satisfied`

   - Author and work: The Book of Habakkuk 2:5, American Standard Version, 1901. The prophetic book is traditionally attributed to Habakkuk.
   - Exact source: [eBible ASV text](https://ebible.org/eng-asv/HAB02.htm).
   - Rights record: [eBible ASV edition page](https://ebible.org/find/show.php?id=eng-asv).
   - Fit: It combines endless appetite, death, and the gathering of nations in the surrounding verse.
   - Attribution confidence: High for the translation and verse reference. Traditional authorship remains a religious attribution rather than a modern biographical certainty.
   - Rights: Public domain. eBible explicitly marks the 1901 ASV public domain and permits free copying.

3. `Famine seems to be the last, the most dreadful resource of nature.`

   - Author and work: Thomas Robert Malthus, *An Essay on the Principle of Population*, first edition, 1798.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/cache/epub/4239/pg4239-images.html).
   - Fit: It gives the terminal route human, material finality without introducing supernatural language.
   - Attribution confidence: High.
   - Rights: Public domain. Malthus died in 1834 and the work was published in 1798.
   - Ranking note: It fits famine better than organized predation, so it ranks behind the first two.

### Spoiler review

- This package is post-reveal and may name Hannibal.
- It must be gated to the ordinary world-end branch after chaos exceeds 1000 and the terminal route completes.
- It contains no Wendigo, winter, transformation, or nonhuman language.
- The title describes the public world state and avoids generic apocalypse wording.
- The body presents irreversible mobilization through armies, routes, cities, and population loss rather than implementation terms.

### Audio alignment

- Audio ID: `50`.
- Final cue: Wagner, *Siegfried's Funeral March and Finale*, United States Marine Band under John R. Bourgeois, 1981.
- Final file: `sound/014_cannibalism/super_event_50_hannibal_world_end.wav`.
- Duration: `120.000 s` with a `0.25 s` fade-in. The retained excerpt begins after a musical pause.
- Sync note: Show the title and body before playback is dispatched. The opening should land as an immediate procession rather than a delayed reveal. The phrase `single timetable` suits the cue's massed military structure. No victory fanfare wording should be added.

## Slot 52: eligible global defeat aftermath

### Final localisation proposal

```yaml
chaosx_super_event.52.t: "The Burial Detail"
chaosx_super_event.52.q: "\"Future years will never know the seething hell\"\n §Y-Walt Whitman, Specimen Days-§!"
chaosx_super_event.52.a: "Begin with the names."
chaosx_super_event.52.d: "The last army under Hannibal Lecter's command has been broken, and the roads into the feeding capitals are open. Recovery teams are finding prisoners, ledgers, unmarked pits, and names erased from military rolls across several countries.\n\nThe coalition has won the war, and whole districts remain emptied. Every surviving government has inherited the work of identification, burial, trial, and relief. The destroyed network leaves incomplete family lists wherever its routes once ran."
```

### Ranked quotation candidates

1. Selected quotation in `.52.q`

   - Author and work: Walt Whitman, *Specimen Days*, section `The Real War Will Never Get in the Books`, 1882.
   - Exact source: [Project Gutenberg full text](https://gutenberg.org/cache/epub/8813/pg8813-images.html).
   - Fit: The excerpt rejects a clean official memory and centers the suffering that records cannot fully hold.
   - Attribution confidence: High. The selected words are a contiguous excerpt from the section's opening paragraph.
   - Rights: Public domain. Whitman died in 1892 and *Specimen Days* was published in 1882.

2. `This is the hour of lead / Remembered if outlived`

   - Author and work: Emily Dickinson, `After great pain a formal feeling comes`, composed around 1862 and first published in the cited edition in 1929.
   - Exact source: [Academy of American Poets text](https://poets.org/poem/after-great-pain-formal-feeling-comes-175).
   - Fit: It presents survival as heavy, formal, and remembered rather than triumphant.
   - Attribution confidence: High for the cited 1929 text.
   - Rights: Public domain. The source explicitly labels this poem public domain. Dickinson died in 1886 and the cited edition appeared in 1929.
   - Text note: Dickinson manuscript and editorial punctuation varies by edition. Preserve the cited wording if this candidate replaces the selected line.

3. `For heroes have the whole earth for their tomb`

   - Author and work: Thucydides, *History of the Peloponnesian War*, Book II, in Richard Crawley's 1874 translation.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/files/7142/7142-h/7142-h.htm).
   - Fit: It gives a global burial image appropriate to a war that crossed many countries.
   - Attribution confidence: High for Crawley's translation. As with all Thucydidean speeches, the historian presents the speech in his own reported form.
   - Rights: Public domain. The ancient work is public domain and Crawley died in 1893.
   - Ranking note: The word `heroes` makes it more triumphal than the selected Whitman line.

### Spoiler review

- Fire this package only when Hannibal was publicly revealed and the duration, territory, population-loss, and coalition thresholds justify a global aftermath.
- The body names Hannibal because the reveal has already occurred.
- Small local or regional containment must not use this slot.
- The text does not imply that dead population returns or that the world has returned to normal.
- Identification, burial, trials, relief, emptied districts, and incomplete records align with the required reconstruction system.

### Audio alignment

- Audio ID: `52`.
- Final cue: Fauré, *Élégie, Op. 24*, Hans Goldstein on cello and Eli Kalman on piano, 2006.
- Final file: `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav`.
- Duration: `116.100 s` with opening silence removed and a `0.25 s` fade-in.
- Sync note: The short option remark lets the elegy continue without turning the close button into a victory slogan. The first paragraph should remain visible from the cue's first cello phrase. Do not add a military stinger or reuse another victory cue.
- Rights note: The final audio derivative is CC BY-SA 2.0 and requires the attribution, license link, change notice, and share-alike treatment recorded in `docs/super_events/014_cannibalism/audio_research.md`.

## Slot 53: transformed Hannibal Lecter worldwide victory

### Final localisation proposal

```yaml
chaosx_super_event.53.t: "No Thaw Will Come"
chaosx_super_event.53.q: "\"The World was void\"\n §Y-Lord Byron, Darkness-§!"
chaosx_super_event.53.a: "The snow keeps no graves."
chaosx_super_event.53.d: "Every transformation anchor has sealed beneath frost and butchered stone. The transformed Hannibal Lecter no longer depends on roads, seasons, or the living institutions that once confined his armies.\n\nCannibal Hosts and winter packs move together from the frozen capitals, drawing fresh strength from every population they overrun. The cold ahead of them carries no terms, accepts no surrender, and leaves no season in which the hunted can recover."
```

### Ranked quotation candidates

1. Selected quotation in `.53.q`

   - Author and work: Lord Byron, *Darkness*, 1816.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/cache/epub/20158/pg20158-images.html).
   - Fit: Four words communicate total extinction without borrowing an Indigenous saying or explaining the Wendigo through outside cultural claims.
   - Attribution confidence: High. The capitalisation follows the cited edition.
   - Rights: Public domain. Byron died in 1824 and the poem was first published in 1816.

2. `The ice was here, the ice was there, / The ice was all around:`

   - Author and work: Samuel Taylor Coleridge, *The Rime of the Ancient Mariner*, first published in 1798. The cited wording follows the later revised text collected by Project Gutenberg.
   - Exact source: [Project Gutenberg full text](https://www.gutenberg.org/files/29091/29091-h/29091-h.htm).
   - Fit: It gives the route a simple, encircling image of inescapable ice.
   - Attribution confidence: High for the cited text.
   - Rights: Public domain. Coleridge died in 1834.
   - Ranking note: The wording is vivid but less terminal than Byron's void world.

3. `Thereby Cocytus wholly was congealed.`

   - Author and work: Dante Alighieri, *Inferno*, canto XXXIV, translated by Henry Wadsworth Longfellow, 1867.
   - Exact source: [Project Gutenberg Longfellow translation](https://www.gutenberg.org/cache/epub/1004/pg1004.html).
   - Fit: The frozen deepest circle supports the route's image of a world locked beneath supernatural cold.
   - Attribution confidence: High for the Longfellow translation.
   - Rights: Public domain. Dante died in 1321, Longfellow died in 1882, and the translation was published in 1867.
   - Ranking note: `Cocytus` is obscure and imports Christian infernal imagery. It is safe from the Indigenous-tradition concern, but it is less direct for the player.

### Spoiler and cultural review

- Fire this package only after the Wendigo merge is public and the transformation countdown has reached terminal lock above chaos 1000.
- The title, body, and option must never be exposed through scenario labels, event previews, achievement names, or scripted-localisation defaults.
- The body reuses the existing Chaos Redux terms `Wendigo` and `Wendigo Pack` without claiming authenticity, origin, or meaning for a living Indigenous tradition.
- No Indigenous quotation, chant, sacred figure, regalia, language, or invented tradition appears.
- The quotation candidates are European public-domain literary sources chosen for winter and extinction only.

### Audio alignment

- Audio ID: `53`.
- Final cue: Grieg, *Peer Gynt Suite No. 1, Op. 46 - II. The Death of Åse*, Musopen Symphony, 2012.
- Final file: `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav`.
- Duration: `118.000 s` with source silence removed and a `0.25 s` fade-in.
- Sync note: The title's finality and Byron's brief void image suit the quiet opening. The body should remain static while the lament develops. Do not add an ambience-only pre-roll, a generated cold drone, or a borrowed ceremonial vocal element.

## Exact localisation and getter map

| Slot | Title key | Quote or subtitle key | Option key | Body key |
| ---: | --- | --- | --- | --- |
| `49` | `chaosx_super_event.49.t` | `chaosx_super_event.49.q` | `chaosx_super_event.49.a` | `chaosx_super_event.49.d` |
| `50` | `chaosx_super_event.50.t` | `chaosx_super_event.50.q` | `chaosx_super_event.50.a` | `chaosx_super_event.50.d` |
| `52` | `chaosx_super_event.52.t` | `chaosx_super_event.52.q` | `chaosx_super_event.52.a` | `chaosx_super_event.52.d` |
| `53` | `chaosx_super_event.53.t` | `chaosx_super_event.53.q` | `chaosx_super_event.53.a` | `chaosx_super_event.53.d` |

For every slot, `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` needs a matching guarded entry in:

- `GetSuperEventTitle`
- `GetSuperEventQuote`
- `GetSuperEventRemark`
- `GetSuperEventDesc`

The guard must use the matching numeric value in `has_global_flag = { flag = super_event_visible value = <slot> }`. The localisation key suffix must match the getter. No Event 014 key may be used as an unguarded or fallback text.

`GetSuperEventImage` also needs a guarded sprite mapping for each slot. The text researcher does not assign those sprite IDs. Use the accepted asset handoff and do not let any Event 014 slot fall through to another super-event's default image.

As of this research pass, slots `49`, `50`, `52`, and `53` have no live mappings in the shared scripted-localisation file. Slot `51` is occupied by the Holy Realm's `Mandala of Nations` and must remain untouched.

## Audio dispatch map and ordering

The accepted audio handoff currently mirrors visible slot IDs with audio IDs:

| Slot | `global.current_super_event_audio_id` | Stable track ID | Final WAV |
| ---: | ---: | --- | --- |
| `49` | `49` | `chaosx_super_event_cannibalism_hannibal_reveal_track` | `sound/014_cannibalism/super_event_49_hannibal_reveal.wav` |
| `50` | `50` | `chaosx_super_event_cannibalism_hannibal_world_end_track` | `sound/014_cannibalism/super_event_50_hannibal_world_end.wav` |
| `52` | `52` | `chaosx_super_event_cannibalism_global_defeat_aftermath_track` | `sound/014_cannibalism/super_event_52_global_defeat_aftermath.wav` |
| `53` | `53` | `chaosx_super_event_cannibalism_wendigo_world_end_track` | `sound/014_cannibalism/super_event_53_wendigo_hannibal_world_end.wav` |

Use this order inside each emit effect:

1. Set the guarded Event 014 route and reveal state.
2. Set `super_event_visible` to the selected slot for the intended visible duration.
3. Set `global.current_super_event_audio_id` to the matching audio ID or its verified script constant.
4. In each player-country scope, call `play_current_super_event_audio = yes`.

The shared helper does nothing when either the visible flag or audio variable is absent. It dynamically resolves `chaosx_super_event_<audio_id>_sound_<volume_suffix>`. The close button clears both the visible flag and the current audio variable.

The audio files are one-shot musical cues. The GUI text is static and requires no line-by-line timing. Keep the visible slot and audio selection aligned in the same effect chain, then let the track play without replacing title, body, quotation, or option during the cue.

Re-scan all shared registries immediately before integration. The audio and visible numbers were collision-free when researched, but this repository is being edited concurrently.

## Rights conclusion

All twelve quotation candidates are short excerpts from public-domain works or explicitly public-domain editions. No modern song lyric, film line, game line, copyrighted novel line, unsourced quotation, or living Indigenous tradition claim was used.

Project Gutenberg's standard notice requires users outside the United States to check local law. In this candidate set, the authors and relevant translators died long enough ago for the texts to be public domain in ordinary life-plus-70 and life-plus-100 jurisdictions. The ASV source explicitly states `Public Domain. Copy freely.` The Academy of American Poets explicitly marks the cited 1929 Dickinson text public domain.

## Uncertainty and parent decisions

- The final Event 014 gameplay implementation did not yet exist as a complete wired system during this research. Trigger names and emit-effect names therefore remain parent-owned.
- Numeric slots and audio IDs must be rechecked at integration time because shared registries are changing concurrently.
- Early-modern spelling and punctuation varies between editions. The handoff identifies the exact edition used for every affected candidate.
- The *King Lear* composition date is approximate. This does not affect attribution or rights.
- The cited Coleridge wording is from the later revised form of a poem first published in 1798.
- The Dante candidate is Longfellow's English translation, not Dante's original Italian. Any use must credit the translator.
- If the implemented merged country receives a different revealed public name, replace `the transformed Hannibal Lecter` in `.53.d` with that established post-reveal name only. Do not add an explanation of living cultural traditions.
- The ID `50` recording has the U.S. federal-work jurisdiction note recorded by the audio researcher. The text package does not change that audio-rights disposition.
- The ID `52` audio derivative must retain CC BY-SA 2.0 attribution and share-alike treatment.

## Simplifications, omissions, and blockers

No quotation or text blocker remains. Three ranked quotation candidates, final title, quotation block, body, option remark, spoiler review, precise keys, and audio alignment notes are present for every requested route.

No fallback, placeholder, modern copyrighted quotation, invented attribution, copied screen-actor identity, or Indigenous sacred motif was used. Final gameplay, localisation, scripted-localisation, image, audio-definition, and spreadsheet wiring remain intentionally outside this subagent's scope.
