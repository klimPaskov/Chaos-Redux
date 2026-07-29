# System Camp Repression Rework Super-Event Research

## Live implementation disposition, 2026-07-11

All five camp-repression super events are implemented and wired. Final English strings live in `localisation/english/camp_repression_rework_l_english.yml` for slots `74` through `77` and `localisation/english/germany_mengele_l_english.yml` for slot `12`. Scripted-localisation routing lives in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`; playback helpers live in `common/scripted_effects/camp_repression_super_event_effects.txt` and `common/scripted_effects/germany_mengele_effects.txt`; sprite registration lives in `interface/chaosx_super_events.gfx`; music registration lives in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`.

The final art is under `gfx/super_events/system_camp_repression_rework/`. The five unique audio packages, source provenance, and processed runtime files are recorded in `docs/assets/system_camp_repression_rework/audio_manifest.md` and `docs/assets/system_camp_repression_rework/audio_handoff.md`. No placeholder image or shared fallback track remains in these slots.

| Visible slot | Audio id | Role | Live emission helper | Status |
| --- | ---: | --- | --- | --- |
| `74` | `44` | Severe global discovery | `camp_rework_show_global_discovery_super_event` | Final text, art, audio, routing, playback, and cleanup wired. |
| `12` | `45` | Angel of Death Directorate revolt | `germany_mengele_show_angel_coup_super_event` | Final text, art, audio, routing, playback, and cleanup wired. |
| `75` | `46` | Soviet famine catastrophe | `camp_rework_show_soviet_famine_super_event` | Final text, art, audio, routing, playback, and cleanup wired. |
| `76` | `47` | Pingfang exposure | `camp_rework_show_pingfang_exposure_super_event` | Final text, art, audio, routing, playback, and cleanup wired. |
| `77` | `48` | Colonial reckoning | `camp_rework_show_colonial_reckoning_super_event` | Final text, art, audio, routing, playback, and cleanup wired. |

`camp_rework_emit_super_event` owns the shared camp-rework playback path. Slot `12` uses the existing Germany/Mengele super-event bridge because it is emitted by the Directorate revolt rather than a discovery exposure.

### Implemented trigger readback

The accepted candidate labels are useful design shorthand, but several live gates are broader or narrower. The final prose below deliberately describes the implemented behavior.

| Slot | Live trigger | Difference from the earlier candidate wording |
| --- | --- | --- |
| `74` | `genocide_try_discover_state_atrocity` calls `camp_rework_show_global_discovery_super_event` on the first non-Japanese severe discovery. `camp_rework_state_has_severe_discovery_evidence` is true for an extermination site, stored radicalized or contaminated site type, **or** evidence depth at least `55`. | High evidence depth is one sufficient path, not a requirement for a radicalized, contaminated, or extermination site. Japanese biological evidence is routed to slot `76` instead. |
| `12` | Every successful `germany_mengele_start_coup` call shows slot `12`. The effect is reached by the ordinary coup-pressure event, the invader-triggered emergency revolt, or the cloning-project revolt, then starts a civil war with Auschwitz state `88`, biological-warfare facility states, and valid laboratory states. | This is an armed laboratory secession, not a discovery event and not only the ordinary autonomy-threshold coup. |
| `75` | `camp_rework_soviet_update_famine` schedules `soviet_gulag.2` once the Soviet original tag has high paranoia and famine pressure at least `60`; that event immediately emits slot `75`. | The live gate does not separately require war or an active Union Crisis. The text therefore centers high-paranoia administrative famine rather than claiming either condition. |
| `76` | The discovery path emits slot `76` when the responsible country has original tag `JAP` and the discovered state is marked as a Japanese biological atrocity site, the Pingfang anchor, or a biological-evidence site. | The discoverer need not specifically be Allied or Soviet, and the state need not be only the literal Pingfang anchor or a separately counted “major network.” |
| `77` | `camp_rework_expose_first_colonial_evidence` emits slot `77` after it exposes one valid evidence state belonging to an `ENG`, `FRA`/`VIC`, `ITA`, or `BEL` responsibility path. Calls currently arise from such conditions as Raj autonomy or separation, ideological regime change, loss of the Congo pool, and failed review, closure, or reform outcomes. | A major-war end or capital loss is not a universal prerequisite. The live event is the first public colonial evidence handoff produced by the supported country-kit routes. |

Implementation references:

- `common/scripted_triggers/camp_repression_rework_triggers.txt:57`
- `common/scripted_effects/genocide_crisis_effects.txt:946`
- `common/scripted_effects/germany_mengele_effects.txt:1709`
- `common/scripted_effects/camp_repression_major_country_effects.txt:1771`
- `events/soviet_gulag.txt:34`
- `common/scripted_effects/camp_repression_colonial_country_effects.txt:94`
- `common/scripted_effects/camp_repression_colonial_country_effects.txt:1370`
- `common/scripted_effects/camp_repression_super_event_effects.txt:27`

## Superseded text-handoff record

The snippets and source notes below are retained as the research handoff that informed the final writing. They are not an exact copy of the live localisation and include earlier proposed wording and encoding artifacts. The two live localisation files named above are authoritative; do not copy this archived YAML back over them.

### Slot 74 / audio 44 — severe global discovery

```yaml
chaosx_super_event.74.t: "The Evidence Crosses the Wire"
chaosx_super_event.74.q: "\"The things I saw beggar description.\"\n§Y—Dwight D. Eisenhower, letter to George C. Marshall, 15 April 1945§!"
chaosx_super_event.74.a: "I think people ought to know."
chaosx_super_event.74.d: "Advancing troops and investigators have entered a site that official denials can no longer contain. Registers, physical traces, and testimony point beyond the local guards to the government that built and maintained the network. This is no longer another rumor from the front; its purpose and scale are matters of public evidence.\n\nCopies are already crossing borders. The record will not close again."
```

- Quote and remark source: the Eisenhower Presidential Library reproduces the 15 April 1945 letter and the later press-conference remark from which the button takes a short contiguous fragment: <https://www.eisenhowerlibrary.gov/eisenhowers/quotes>.
- Confidence: **high**. The library identifies the letter as *The Papers of Dwight David Eisenhower*, *The War Years IV*, document 2418, and identifies the 18 June 1945 press conference separately.
- Fit: the quote anchors the event in first-hand physical evidence, while the short button remark turns public knowledge into the response. The description remains valid for any live severe path: site class or evidence depth, captured or destroyed evidence.
- Rights note: both direct excerpts are very short and come from the official presidential archive.

### Slot 12 / audio 45 — Angel of Death Directorate revolt

```yaml
chaosx_super_event.12.t: "The Angel of Death Leaves the Camp"
chaosx_super_event.12.q: "\"Spirits raised by me\nVainly would I lay!\"\n§Y—Johann Wolfgang von Goethe, The Pupil in Magic§!"
chaosx_super_event.12.a: "The camp signs its own orders."
chaosx_super_event.12.d: "The Auschwitz laboratory command has broken with Berlin. Josef Mengele's faction has seized the camp, biological-warfare facilities, and the experiment-linked network that answered to it. What grew inside the regime as a separate chain of command now fields its own armies and issues its own orders.\n\nGermany has not lost a department. It has created a rival state."
```

- Quote source: Goethe's *Der Zauberlehrling* in Edgar Alfred Bowring's public-domain English translation, titled *The Pupil in Magic*: <https://www.gutenberg.org/cache/epub/1287/pg1287-images.html>. The scan-backed German source is also available at <https://de.wikisource.org/wiki/Der_Zauberlehrling_(1827)>.
- Confidence: **high**. The proposed quote preserves Bowring's wording and line break.
- Title grounding: the United States Holocaust Memorial Museum documents Mengele's “Angel of Death” nickname and his Auschwitz experiments: <https://encyclopedia.ushmm.org/content/en/article/josef-mengele>.
- Remark grounding: the line is original in-world prose, not a claimed quotation. It reflects both the live `start_civil_war`/laboratory-state transfer and the historical SS pattern that the USHMM describes as a virtual state within a state: <https://encyclopedia.ushmm.org/content/en/article/ss>.
- Fit: Goethe's summoned force that can no longer be subdued describes the trigger more precisely than an inscription over an entrance. The revised description also removes the mechanical and dehumanizing phrase “prisoners to spend” while retaining the actual Auschwitz, facility, laboratory-network, and rival-command outcomes.

#### Existing slot 12 retain/replace assessment

| Element | Recommendation | Evidence and reason |
| --- | --- | --- |
| Title | **Retain** | It is concise, unique to this route, uses Mengele's documented nickname, and accurately describes the laboratory command leaving camp subordination to become a belligerent. |
| Dante quote | **Replace for fit, not authenticity** | The current Longfellow wording is genuine and verifiable in *Inferno* III: <https://www.gutenberg.org/cache/epub/1004/pg1004.html>. It evokes entry into Hell, however, while the live trigger is the regime losing control of an institution it created. Goethe's line maps directly to that reversal. |
| Remark | **Retain** | “The camp signs its own orders” is one of the strongest existing short reactions: it states the exact bureaucratic-to-sovereign transition without exposing variables or repeating the title. |
| Description | **Replace** | The current first sentence broadly matches the state transfer, but the revised text covers all three coup entry routes and removes “prisoners to spend,” which reads as a tuning/resource phrase rather than in-world reporting. |

### Slot 75 / audio 46 — Soviet famine catastrophe

```yaml
chaosx_super_event.75.t: "The Empty Granaries"
chaosx_super_event.75.q: "\"Every Kolchosi [Kolkhoz or collective farm] is starving, it has not got a morsel of bread!\"\n§Y—Jerry Berman, letter of 3 February 1933§!"
chaosx_super_event.75.a: "Give us this day our daily bread."
chaosx_super_event.75.d: "Across the Soviet countryside, grain extraction, forced-labor quotas, political instability, and orders issued under fear have converged into a famine the ministries can no longer classify as a local shortage. Villages are losing people faster than reports can be rewritten, while hunger feeds every grievance already pulling at the Union.\n\nRelief, concealment, or an admission of collapse remain. None can restore the bread already taken."
```

- Quote source: the National Museum of the Holodomor-Genocide's transcription of Jerry Berman's 3 February 1933 letter: <https://holodomormuseum.org.ua/letters/03-02-1933/>. The Museum identifies Berman and the provenance of the donated letters here: <https://holodomormuseum.org.ua/en/jerry-berman-s-letters/>.
- Confidence: **high**. The bracketed explanation of `Kolchosi` is retained from the Museum's transcription rather than silently modernized.
- Remark source: Matthew 6:11 in the public-domain King James Version: <https://www.biblegateway.com/passage/?search=Matthew+6%3A11&version=KJV>.
- Fit: the description names the four live pressure families—grain extraction, forced-labor quotas, low stability, and high paranoia—without claiming the unimplemented war/Union-Crisis gate. The prayer fragment is culturally legible, restrained, and bitterly opposed to the state's extraction logic.

### Slot 76 / audio 47 — Pingfang exposure

```yaml
chaosx_super_event.76.t: "The Pingfang Files"
chaosx_super_event.76.q: "\"There is no doubt that Unit 731 conducted experiments on human subjects that included Chinese, Koreans, and Russians.\"\n§Y—Daqing Yang, Researching Japanese War Crimes§!"
chaosx_super_event.76.a: "Heaven's net lets nothing escape."
chaosx_super_event.76.d: "Investigators have secured records and physical evidence from a Japanese biological-warfare site. Medical files, laboratory inventories, and surviving traces connect experiments in occupied territory to an army program whose evidence is now beyond Tokyo's control.\n\nWhether the trail began at Pingfang or one of its linked facilities, it no longer ends behind a military seal."
```

- Quote source: Daqing Yang's essay in the U.S. National Archives and Records Administration/IWG volume *Researching Japanese War Crimes*, printed page 37: <https://www.archives.gov/files/iwg/japanese-war-crimes/introductory-essays.pdf>.
- Confidence: **high**. The official NARA publication states the conclusion directly and documents the wartime articles, postwar records, and later archival evidence behind it.
- Remark source: a concise paraphrase of Laozi, *Dao De Jing* 73, using James Legge's 1891 public-domain translation as the check text: <https://sacred-texts.com/tao/sbe39/sbe39080.htm>. Because the button is a paraphrase, it is not presented as a verbatim quotation.
- Fit: the wording follows the broad live flag family rather than promising a specific Allied/Soviet discoverer or only the literal Pingfang state. The quote is investigative and documentary; the remark supplies a Chinese cultural frame for evidence escaping concealment.

### Slot 77 / audio 48 — colonial reckoning

```yaml
chaosx_super_event.77.t: "The Empire's Accounts"
chaosx_super_event.77.q: "\"The subjection of peoples to alien subjugation, domination and exploitation constitutes a denial of fundamental human rights.\"\n§Y—United Nations General Assembly Resolution 1514 (XV), 1960§!"
chaosx_super_event.77.a: "Let my people go."
chaosx_super_event.77.d: "A colonial government's own files have passed beyond its control. The first surviving evidence of detention, coerced labor, or local population loss has reached investigators as political pressure, independence, regime change, lost territory, or a failed review breaks the old chain of custody. Former subjects and foreign governments are reading the same account at last.\n\nThe empire kept its books. It can no longer keep the reckoning private."
```

- Quote source: the official United Nations Digital Library record and English text of General Assembly Resolution 1514 (XV): <https://digitallibrary.un.org/record/206145?ln=en>.
- Confidence: **high**. The selected sentence is the resolution's first operative paragraph and directly names colonial domination and exploitation.
- Remark source: `Let my people go` is both the alternate title/refrain recorded for the African American spiritual *Go Down Moses* and the Exodus phrase behind it. The Library of Congress catalogue record is <https://www.loc.gov/item/jukebox-69931/>. This also creates an intentional text-to-audio link with audio id `48`.
- Fit: the description covers the live exposure helper's actual routes—pressure, separation, regime change, territory loss, and failed reform—without claiming that every firing follows a world war or capital loss.

## Source, wording, and rights summary

| Slot | Main quote source type | Attribution confidence | Wording/rights note |
| --- | --- | --- | --- |
| `74` | Official presidential archive reproducing a 1945 letter | High | Two very short excerpts; no alteration beyond normal punctuation and UI attribution. |
| `12` | Public-domain nineteenth-century English translation of Goethe | High | Bowring's line break and wording are preserved. The current Dante line is authentic but not selected. |
| `75` | Primary 1933 letter transcribed by Ukraine's national Holodomor museum | High | The Museum's bracketed gloss is preserved so the unfamiliar source spelling remains intelligible. |
| `76` | Official NARA/IWG historical publication | High | Short, directly supported conclusion from the cited printed page. |
| `77` | Official United Nations resolution | High | Short excerpt from an institutional public document. |

No quotation, attribution, or cultural-reference fallback was used. All five selected quotations have a primary or authoritative source, and all modern or institutionally published excerpts remain well below the direct-excerpt limits.

## Text-handoff uncertainties and implementation decisions

1. The accepted trigger identifiers in the source tracker are stale relative to the live script for slots `74`, `75`, `76`, and `77`. This package follows the live script. If the parent instead narrows those triggers to the earlier candidate definitions, the descriptions should be rechecked in the same change.
2. The dedicated French inherited-evidence helper, `camp_rework_expose_first_french_inherited_evidence`, routes through `camp_rework_expose_first_colonial_evidence`. France and Vichy therefore participate in the same one-shot slot `77` colonial-reckoning threshold as the other fixed colonial kits.
3. Slot `12` keeps its existing `.t` and `.a` verbatim but proposes a new `.q` and `.d`. The change should be applied atomically so the Goethe quote and rival-state description arrive together.
4. This text pass did not assess image completion or change the completed audio selections below. It did not edit the scripted-localisation mappings, which already contain slots `74` through `77`.

## Audio disposition

This note completes the audio-research and audio-production portion of the five accepted camp-repression super-event candidates. It follows the roles in `system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md` and the separate research requirement in `system_camp_repression_rework_super_event_prompt.md`.

Five unique musical recordings were selected, downloaded from their legitimate Wikimedia Commons records, preserved, edited, and converted for Chaos Redux sound registration. The recommended numeric audio IDs continue the live catalogue after audio ID `43`:

| Recommended audio ID | Current visible slot | Super-event role | Selected cue | Final duration |
| --- | --- | --- | --- | --- |
| `44` | `74` | Global Atrocity Evidence Discovery | Erik Satie, *Gnossienne No. 1*, performed by La Pianista | `1:52.000` |
| `45` | `12` | Angel of Death Directorate Revolt | J. S. Bach, *Passacaglia and Fugue in C minor, BWV 582*, performed by Awadagin Pratt | `1:54.000` |
| `46` | `75` | Soviet Famine Catastrophe | *Hey, Plyve Kacha po Tysyni*, performed by the Revutsky Capella | `1:56.000` |
| `47` | `76` | Pingfang Exposure | *Yangguan Sandie (Three Refrains on the Yang Pass Theme)*, performed by Charlie Huang | `1:49.500` OGG / `1:49.404` WAV |
| `48` | `77` | Colonial Reckoning | *Go Down Moses*, performed by Les Petits Chanteurs de Montigny | `1:50.000` |

The small WAV container-duration difference for audio ID `47` is normal Vorbis granule rounding; both derivatives contain the same edited interval and remain below two minutes.

The current implementation constants reserve visible slots `74–77` for the four public camp-rework thresholds and retain the existing Angel of Death slot `12`; those reservations were not edited by the audio worker. Quote, cultural-remark, image, localisation, and gameplay work were outside that audio-only handoff; the text package above now completes the quote and remark research without changing the underlying files. Audio IDs are independent of visible super-event slots.

## Selection standard

- The current approved repository catalogue and every existing final WAV were checked before external research. No selected work or final derivative is already assigned to another Chaos Redux super-event.
- Composition and recording rights were checked separately.
- Every selection is a musical performance. No SFX, drone, stinger, test tone, oscillator cue, synthetic noise bed, or placeholder was used.
- Share-alike sources remain share-alike in their edited derivatives. Attribution text below names the work, composer or tradition, performer, source record, license, and the fact that the file was edited.
- The final derivatives use the current repository wrapper profile: 44.1 kHz stereo PCM signed 16-bit WAV under `sound/`.

## Audio ID 44: Global Atrocity Evidence Discovery

### Selected recording

- Exact title: *Gnossienne No. 1*
- Composer: Erik Satie (1866–1925)
- Performer and recording source: La Pianista; self-recorded performance dated 16 November 2010
- Source record: <https://commons.wikimedia.org/wiki/File:Satie_-_Gnossienne_1.ogg>
- Direct media: <https://upload.wikimedia.org/wikipedia/commons/9/91/Satie_-_Gnossienne_1.ogg>
- Original duration: `217.995646` seconds (`3:37.996`)
- Source SHA-1: `0c33bce5b2f7887939b07dfb21137b82bd7b4d81`, matching the Commons file record
- Source path: `docs/assets/system_camp_repression_rework/source/audio/global_discovery_satie_gnossienne_1_source.ogg`

### Rights and terms

- Composition: public domain. Commons separately marks Satie's composition public domain.
- Performance/recording: Creative Commons Attribution-ShareAlike 3.0 Unported.
- License: <https://creativecommons.org/licenses/by-sa/3.0/>
- License confidence: **high**. The performer uploaded the performance as own work and explicitly licensed it; composition and performance are separated on the file page.
- Usage terms: copying and adaptation are permitted with attribution, a license link, an indication that changes were made, and distribution of the derivative under the same or a compatible share-alike license.
- Derivative status: both final files are distributed under CC BY-SA 3.0.

Recommended attribution:

> *Gnossienne No. 1* by Erik Satie, performed by La Pianista (2010), via Wikimedia Commons, CC BY-SA 3.0. Edited to a 1:52 excerpt, faded, resampled, and loudness-normalized for Chaos Redux. The composition is public domain.

### Edit, paths, and tone fit

- Retained source interval: `00:00.000–01:52.000`
- Processing: `0.25`-second fade-in, `5.00`-second fade-out from `01:47`, two-pass loudness normalization targeting `-18 LUFS` and `-1.5 dBTP`, 44.1 kHz stereo export
- Final WAV: `sound/system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.wav`
- Final WAV: `sound/system_camp_repression_rework/super_event_44_global_atrocity_evidence_discovery.wav`
- Tone fit: the exposed, hesitant piano line keeps the discovery focused on testimony, records, and the weight of recognition. It is sober and unsettled without turning the evidence reveal into generic apocalypse or military triumph.

## Audio ID 45: Angel of Death Directorate Revolt

### Selected recording

- Exact title: *Passacaglia and Fugue in C minor, BWV 582*
- Composer: Johann Sebastian Bach (1685–1750)
- Performer and recording source: pianist Awadagin Pratt at the White House Evening of Classical Music, 4 November 2009
- Source record: <https://commons.wikimedia.org/wiki/File:20091104_Awadagin_Pratt_-_Bach%27s_Passacaglia_and_Fugue_in_C_minor,_BWV_582.ogg>
- Direct media: <https://upload.wikimedia.org/wikipedia/commons/7/7c/20091104_Awadagin_Pratt_-_Bach%27s_Passacaglia_and_Fugue_in_C_minor%2C_BWV_582.ogg>
- Original duration: `719.184000` seconds (`11:59.184`)
- Source SHA-1: `562c2e9b68d02d71370a6ccb70e2f7a583165369`, matching the Commons file record
- Source path: `docs/assets/system_camp_repression_rework/source/audio/directorate_revolt_bach_passacaglia_pratt_source.ogg`

### Rights and terms

- Composition: public domain.
- Performance/recording: Creative Commons Attribution 3.0 Unported; Commons also identifies the source as White House material and applies a U.S. government public-domain marker.
- License: <https://creativecommons.org/licenses/by/3.0/>
- License confidence: **high**. The file page identifies the performer, event, date, original White House source, license, and composition status separately.
- Usage terms: copying and adaptation are permitted with appropriate attribution, a license link, and an indication that changes were made.
- Derivative status: both final files are made available under CC BY 3.0 with the required attribution.

Recommended attribution:

> *Passacaglia and Fugue in C minor, BWV 582* by Johann Sebastian Bach, performed by Awadagin Pratt at the White House (2009), via Wikimedia Commons, CC BY 3.0. Edited to a 1:54 excerpt, faded, resampled, and loudness-normalized for Chaos Redux. The composition is public domain.

### Edit, paths, and tone fit

- Retained source interval: `00:10.169–02:04.169`; the edit removes the opening silence and ends well before the later *Hail to the Chief* quotation documented on the source page.
- Processing: `0.25`-second fade-in, `6.00`-second fade-out from `01:48`, two-pass loudness normalization targeting `-18 LUFS` and `-1.5 dBTP`, resampling from 48 kHz to 44.1 kHz stereo
- Final WAV: `sound/system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.wav`
- Final WAV: `sound/system_camp_repression_rework/super_event_45_angel_of_death_directorate_revolt.wav`
- Tone fit: the repeating bass design and accumulating counterpoint sound controlled, procedural, and inexorable. The cue supplies scientific-horror severity and disciplined momentum without borrowing an existing martial super-event track or becoming a triumphant march.

## Audio ID 46: Soviet Famine Catastrophe

### Selected recording

- Exact title: *Hey, Plyve Kacha po Tysyni* (also known as *Plyve Kacha po Tysyni*)
- Composer/tradition: traditional Ukrainian Lemko folk lament
- Performer and recording source: Revutsky Capella; performance recorded in London in October 2013
- Source record: <https://commons.wikimedia.org/wiki/File:%D0%9A%D0%B0%D0%BF%D0%B5%D0%BB%D0%B0_%D1%96%D0%BC._%D0%A0%D0%B5%D0%B2%D1%83%D1%86%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_-_%D0%93%D0%B5%D0%B9,_%D0%BF%D0%BB%D0%B8%D0%B2%D0%B5_%D0%BA%D0%B0%D1%87%D0%B0_%D0%BF%D0%BE_%D0%A2%D0%B8%D1%81%D0%B8%D0%BD%D1%96.webm>
- Direct media: <https://upload.wikimedia.org/wikipedia/commons/e/ec/%D0%9A%D0%B0%D0%BF%D0%B5%D0%BB%D0%B0_%D1%96%D0%BC._%D0%A0%D0%B5%D0%B2%D1%83%D1%86%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_-_%D0%93%D0%B5%D0%B9%2C_%D0%BF%D0%BB%D0%B8%D0%B2%D0%B5_%D0%BA%D0%B0%D1%87%D0%B0_%D0%BF%D0%BE_%D0%A2%D0%B8%D1%81%D0%B8%D0%BD%D1%96.webm>
- Original duration: `305.988000` seconds (`5:05.988`)
- Source SHA-1: `198f11caa7316deddef91df7d215b1091fb542b0`, matching the Commons file record
- Preserved download: `docs/assets/system_camp_repression_rework/source/audio/soviet_famine_plyve_kacha_revutsky_source.webm`

### Rights and terms

- Composition: traditional folk song; no modern composition claim is attached to the source.
- Performance/recording: Creative Commons Attribution 3.0 Unported. Commons records the Revutsky Capella as author, links the ensemble's source channel, and records the pre-2025 YouTube CC license review.
- License: <https://creativecommons.org/licenses/by/3.0/>
- License confidence: **high**, with the Commons source record, named performing ensemble, source-channel identity, and reviewed irrevocable CC license all aligned.
- Usage terms: copying and adaptation are permitted with attribution, a license link, and an indication that changes were made.
- Derivative status: both final files are made available under CC BY 3.0 with the required attribution.

Recommended attribution:

> *Hey, Plyve Kacha po Tysyni*, a traditional Ukrainian Lemko folk lament, performed by the Revutsky Capella (London, 2013), via Wikimedia Commons, CC BY 3.0. Audio excerpted from the source video, timestamp-repaired, faded, and loudness-normalized for Chaos Redux.

### Edit, paths, and tone fit

- Retained source interval: `00:00.000–01:56.000`
- Processing: audio stream isolated from the preserved WebM; non-monotonic source timestamps repaired with asynchronous resampling; `0.35`-second fade-in; `6.00`-second fade-out from `01:50`; two-pass loudness normalization targeting `-18 LUFS` and `-1.5 dBTP`; 44.1 kHz stereo export
- Final WAV: `sound/system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.wav`
- Final WAV: `sound/system_camp_repression_rework/super_event_46_soviet_famine_catastrophe.wav`
- Tone fit: the unaccompanied lament puts human loss ahead of state spectacle. Its Ukrainian voice gives the famine branch historical and regional gravity while the slow choral contour supports mass hunger, administrative fear, and collapse rather than victory.

## Audio ID 47: Pingfang Exposure

### Selected recording

- Exact title: *Yangguan Sandie (Three Refrains on the Yang Pass Theme)*
- Composer/tradition: traditional Chinese guqin repertory; the performer identifies the score source as *Qinxue Rumen* (1867)
- Performer and recording source: Charlie Huang, also credited as Charles R Tsua; self-recorded on 6 October 2013 at Shaoyun Xuan, Birmingham
- Source record: <https://commons.wikimedia.org/wiki/File:Guqin-Yangguan_Sandie.ogg>
- Direct media: <https://upload.wikimedia.org/wikipedia/commons/6/60/Guqin-Yangguan_Sandie.ogg>
- Original duration: `350.093061` seconds (`5:50.093`)
- Source SHA-1: `1790acd2dfd99a8dcaf7c27a7040f867b89246f2`, matching the Commons file record
- Source path: `docs/assets/system_camp_repression_rework/source/audio/pingfang_exposure_yangguan_sandie_charlie_huang_source.ogg`

### Rights and terms

- Composition/score source: the documented 1867 score source is public domain.
- Performance/recording: Creative Commons Attribution-ShareAlike 3.0 Unported, with GFDL offered as an alternative. This package uses CC BY-SA 3.0.
- License: <https://creativecommons.org/licenses/by-sa/3.0/>
- License confidence: **high**. The performer uploaded the self-recording, names the instrument, score source, date, and recording location, and explicitly licenses the performance.
- Usage terms: copying and adaptation are permitted with attribution, a license link, an indication that changes were made, and distribution of the derivative under the same or a compatible share-alike license.
- Derivative status: both final files are distributed under CC BY-SA 3.0.

Recommended attribution:

> *Yangguan Sandie (Three Refrains on the Yang Pass Theme)*, traditional Chinese guqin repertory from the 1867 *Qinxue Rumen* score source, performed by Charlie Huang / Charles R Tsua (2013), via Wikimedia Commons, CC BY-SA 3.0. Edited to an approximately 1:49.5 excerpt, faded, and loudness-normalized for Chaos Redux.

### Edit, paths, and tone fit

- Retained source interval: `00:01.402–01:50.802`; the edit removes the documented leading silence and ends at the first extended musical pause.
- Processing: `0.25`-second fade-in, `5.00`-second fade-out from `01:44.400`, two-pass loudness normalization targeting `-18 LUFS` and `-1.5 dBTP`, 44.1 kHz stereo export
- Final WAV: `sound/system_camp_repression_rework/super_event_47_pingfang_exposure.wav`
- Final WAV: `sound/system_camp_repression_rework/super_event_47_pingfang_exposure.wav`
- Tone fit: the spare guqin performance is severe without becoming sensational. A Chinese farewell repertory places attention on occupied-territory witnesses and absence, supporting an investigative and tribunal-facing exposure rather than centering the perpetrators.

## Audio ID 48: Colonial Reckoning

### Selected recording

- Exact title: *Go Down Moses*
- Composer/tradition: traditional nineteenth-century African American spiritual
- Performer and recording source: Les Petits Chanteurs de Montigny; Jamendo recording dated 8 February 2005 and preserved on Wikimedia Commons
- Source record: <https://commons.wikimedia.org/wiki/File:01_-_Go_down_Moses_(Negro_Spiritual).ogg>
- Direct media: <https://upload.wikimedia.org/wikipedia/commons/8/8f/01_-_Go_down_Moses_%28Negro_Spiritual%29.ogg>
- Original duration: `182.333333` seconds (`3:02.333`)
- Source SHA-1: `c4fc6d561ef6bfd542e0048715d91a7891ded270`, matching the Commons file record
- Source path: `docs/assets/system_camp_repression_rework/source/audio/colonial_reckoning_go_down_moses_montigny_source.ogg`

### Rights and terms

- Composition: traditional and public domain.
- Performance/recording: Creative Commons Attribution-ShareAlike 2.0 Generic.
- License: <https://creativecommons.org/licenses/by-sa/2.0/>
- License confidence: **high**. The Commons record and embedded source metadata both identify the performer, Jamendo source, track ID, and CC BY-SA 2.0 license.
- Usage terms: copying and adaptation are permitted with attribution, a license link, an indication that changes were made, and distribution of the derivative under the same or a compatible share-alike license.
- Derivative status: both final files are distributed under CC BY-SA 2.0.

Recommended attribution:

> *Go Down Moses*, traditional African American spiritual, performed by Les Petits Chanteurs de Montigny (2005), sourced from Jamendo through Wikimedia Commons, CC BY-SA 2.0. Edited to a 1:50 excerpt, faded, and loudness-normalized for Chaos Redux.

### Edit, paths, and tone fit

- Retained source interval: `00:00.000–01:50.000`
- Processing: `0.25`-second fade-in, `6.00`-second fade-out from `01:44`, two-pass loudness normalization targeting `-18 LUFS` and `-1.5 dBTP`, 44.1 kHz stereo export
- Final WAV: `sound/system_camp_repression_rework/super_event_48_colonial_reckoning.wav`
- Final WAV: `sound/system_camp_repression_rework/super_event_48_colonial_reckoning.wav`
- Tone fit: the Exodus refrain is a direct musical language of captivity and release. The choral treatment is solemn and political, making the cue appropriate for exposed forced labor, survivor testimony, decolonization pressure, and imperial accountability.

## Technical result

| Audio ID | OGG profile | WAV profile | Measured final WAV loudness | Measured final WAV true peak |
| --- | --- | --- | --- | --- |
| `44` | Vorbis, 44.1 kHz, stereo | PCM signed 16-bit, 44.1 kHz, stereo | `-17.96 LUFS` | `-1.31 dBTP` |
| `45` | Vorbis, 44.1 kHz, stereo | PCM signed 16-bit, 44.1 kHz, stereo | `-17.93 LUFS` | `-1.46 dBTP` |
| `46` | Vorbis, 44.1 kHz, stereo | PCM signed 16-bit, 44.1 kHz, stereo | `-18.10 LUFS` | `-1.62 dBTP` |
| `47` | Vorbis, 44.1 kHz, stereo | PCM signed 16-bit, 44.1 kHz, stereo | `-17.98 LUFS` | `-1.17 dBTP` |
| `48` | Vorbis, 44.1 kHz, stereo | PCM signed 16-bit, 44.1 kHz, stereo | `-18.06 LUFS` | `-2.45 dBTP` |

Vorbis encoding can move reconstructed true peak slightly above the processing ceiling; every result remains comfortably below clipping and follows the recent repository package profile.

## Historical catalogue check and rejected directions

At the time of audio selection, the pre-package catalogue ended at audio ID `43`; the implemented package extends it through `48`. Existing assignments excluded from consideration include *A Night on the Bare Mountain*, *Mars, the Bringer of War*, *Coriolan*, *Egmont*, Tchaikovsky's Sixth Symphony finale, *The Hebrides*, and the Beethoven piano works already used by Event 010. Tracks with pending provenance, unknown attribution, or another super-event assignment were not reused.

Also rejected:

- YouTube mirrors without a durable license record;
- public-domain compositions paired with recordings whose neighboring rights were not verified;
- historical recordings whose Commons tags addressed only U.S. publication rights but did not cleanly establish recording reuse for this package;
- generated, synthesized, oscillator, SFX, drone, ambience, and test-tone material.

## Research-pass boundary and current wiring

The original audio research pass did not edit `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, `sound/chaosx_sound.asset`, gameplay, localisation, scripted effects, GUI, GFX, images, achievements, or package specs. That sentence describes the subagent's ownership boundary, not current repository status. Parent-owned integration has since registered ids `44` through `48`, wired settings-aware playback, added final localisation and art, and connected all five live trigger paths. Exact definition and playback handoff is in `docs/assets/system_camp_repression_rework/audio_handoff.md`; file provenance and checksums are in `docs/assets/system_camp_repression_rework/audio_manifest.md`.

There are no audio-production, licensing, placeholder, reuse, text, image, or wiring blockers for these five super events.
