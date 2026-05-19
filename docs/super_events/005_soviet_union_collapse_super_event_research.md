# Soviet Union Collapse Super-Event Research

## Package

- Event id: `5`
- Event slug: `soviet_union_collapse`
- Super-event slot: `14`
- Super-event role: major escalation, not a world-end scenario
- Title: `The Union Unmade`
- Localisation keys: `super_event.14.t`, `super_event.14.d`, `super_event.14.a`, `super_event.14.q`
- Trigger effect: `soviet_collapse_show_union_unmade_super_event`
- Trigger direction: fires once from `soviet_collapse_setup_breakaway_country` when the Soviet crisis has more than `constant:soviet_collapse_super_event.min_breakaways_for_union_unmade` breakaway republics, currently three or more
- Image asset manifest: `docs/assets/005_soviet_union_collapse/manifest.md`

## Latest Continuation State

The republic focus and influence super-event prompt is present at `tmp/005_soviet_union_collapse_republic_focus_and_influence_super_event_prompt.md`, and the base super-event prompt named by the active objective is present at `tmp/005_soviet_union_collapse_super_event_prompt.md`. The package has been checked against the active objective inputs.

The sourced super-event image package contains `10` documented rows: slot `14` and slots `19` through `27`. Each sourced image has a source path, processed PNG, final DDS, sprite wiring, and manifest entry. The tracking sheets remain informational evidence for source provenance and art-pass history.

Generated high-chaos branch images for slots `15` through `18` are fictional symbolic scenes and are not part of the sourced-image review queue.

Latest direct package recount confirms super-event slots `14` through `27` are `14/14` for sprite definitions, DDS files, title/description/button/quote localisation, image selectors, show helpers, script constant IDs, and documented audio slots.

## Text

### Title

`The Union Unmade`

The title is the primary title from the super-event prompt and matches the moment when foreign observers stop treating the crisis as a few local refusals.

### Description

The description presents a broad loss of union authority across ministries, military districts, railway authorities, and emergency governments. It does not describe the crisis as a world-end state.

### Button Text

`No orders return.`

This is original button text, not a direct cultural quotation. It is short enough for the super-event button and fits the prompt's telegram/order/silence direction.

## Quote

### Selected Quote

`The state is a relation of men dominating men.`

- Author: Max Weber
- Source: `Politics as a Vocation`
- Source context: lecture delivered in 1919, commonly translated in the Gerth and Mills collection
- Source URL: `https://archive.org/download/weber_max_1864_1920_politics_as_a_vocation/weber_max_1864_1920_politics_as_a_vocation.pdf`
- Additional search evidence: DuckDuckGo result for the Archive.org PDF and university-hosted copies returned the longer passage containing this sentence
- Attribution confidence: medium-high; the wording is widely reproduced from the standard English translation, but the exact English translation is not a primary German text
- Rights note: Weber's original 1919 lecture is public domain in the United States; this English sentence is short and used as a sourced excerpt
- Why it fits: the Soviet crisis is about the center losing the obedience relation that makes command effective
- User review status: not required for the short historical quote, but attribution wording can be adjusted if a preferred translation is chosen later

Rejected quote direction:

- Unsourced Lenin-attributed "decades/weeks" wording was avoided because attribution is disputed.

## Image

- Asset: `super_event_union_unmade`
- Sprite: `GFX_super_event_union_unmade`
- Final DDS: `gfx/super_events/super_event_union_unmade.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:August_1991_coup_-_awaiting_the_counterattack_outside_the_White_House_Moscow_-_panoramio.jpg`
- Author: David Broad
- License: Creative Commons Attribution 3.0 Unported
- License confidence: high; Wikimedia Commons page lists CC BY 3.0 and Panoramio bot review
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_union_unmade_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_union_unmade_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_union_unmade.png`
- Target size: 457x328
- Processing notes: cropped to super-event aspect ratio, resized to 457x328, converted to black and white, lightly increased contrast, exported to uncompressed 32-bit DDS
- Review status: `wired, documented`
- Why it fits: civilians and barricades outside the Moscow White House during the 1991 coup attempt visually communicate the loss of assumed Soviet central command

## Audio

- Selected track: Overture in C minor, Op. 62, "Coriolan"
- Composer: Ludwig van Beethoven
- Performer/source recording: Fulda Symphonic Orchestra, conducted by Simon Schindler
- Source URL: `https://commons.wikimedia.org/wiki/File:Ludwig_van_Beethoven_-_Overt%C3%BCre_c-moll,_op._62.ogg`
- License: EFF Open Audio License v1
- License confidence: high; already documented in `docs/super_events/super_event_audio_packages.md` and embedded Vorbis metadata
- Source path: `docs/audio_sources/super_events/beethoven-coriolan-overture.ogg`
- Final `.ogg` path: `music/super_event_union_unmade.ogg`
- Sound-channel derivative path: `sound/chaosx_super_event_union_unmade.wav`
- Sound definition id: `chaosx_super_event_union_unmade_track`
- Music definitions: `chaosx_super_event_14_0_5`, `chaosx_super_event_14_1_0`, `chaosx_super_event_14_1_5`, `chaosx_super_event_14_2_0`, `chaosx_super_event_14_2_5`, `chaosx_super_event_14_3_0`
- Soundeffect definitions: `chaosx_super_event_14_sound_0_5`, `chaosx_super_event_14_sound_1_0`, `chaosx_super_event_14_sound_1_5`, `chaosx_super_event_14_sound_2_0`, `chaosx_super_event_14_sound_2_5`, `chaosx_super_event_14_sound_3_0`
- Duration: final `1:59.50`
- Editing notes: first `119.5` seconds, fade out over the last `5` seconds, encoded to Ogg Vorbis and converted to WAV for the sound-channel wrapper
- Why it fits: the overture has political tragedy and restrained martial pressure without becoming triumphal
- Uncertainties: the same source recording is also used for the Fallout super-event; this package uses a separate final file, separate slot, and separate audio id

## Research Notes

- The configured DuckDuckGo MCP search was used for quote, image, and audio/source research.
- Repository audio sources were inspected before searching for new audio. The existing Beethoven Coriolan source had clear license documentation and fit the event tone better than adding an uncertain external track.
- The super-event image is wired, documented, and tracked through the sourced-image manifest.

## Optional Branch Super-Events

The custom extreme paths and republic transformation routes have thirteen rare branch super-event slots. Implemented focus routes call the wired helpers listed below; presentation-ready helpers remain available for later splinter route work where no implemented route exists yet.

| Slot | Title | Trigger |
| --- | --- | --- |
| `15` | The Black Banner Returns | Ukraine completes `ukr_soviet_collapse_black_banner_takes_the_villages` |
| `16` | The Northern Signals Break | Helper present; no implemented death-state route currently calls it |
| `17` | The Workshops Choose Their Councils | `MFR_state_as_one_arms_order` |
| `18` | Every Port a Council | Helper present; no implemented naval council route currently calls it |
| `19` | A Map Larger than the Union | Ukraine completes `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map` |
| `20` | The Steppe Beyond History | `kaz_soviet_collapse_the_southern_republics_do_not_kneel` |
| `21` | The Corridors Decide | Belarus completes `blr_soviet_collapse_the_corridor_state` or `blr_soviet_collapse_the_leagues_spine` |
| `22` | The Bread State | Ukraine completes `ukr_soviet_collapse_last_harvest_plan` |
| `23` | The League of Equal Republics | Ukraine completes `ukr_soviet_collapse_league_of_equals` |
| `24` | The Steppe Federation | Kazakhstan completes `kaz_soviet_collapse_steppe_federation_charter` |
| `25` | The Baltic League | The Baltic regional tree completes `baltic_soviet_collapse_baltic_defense_compact` |
| `26` | The Caucasus League | The Caucasus regional tree completes `caucasus_soviet_collapse_caucasus_defense_compact` |
| `27` | The Eastern Buffer Coalition | Moldova completes `moldova_soviet_collapse_alliance_not_union` |

Image coordination:

- Source sheet: `docs/assets/005_soviet_union_collapse/source_png/optional_super_event_sheet_source.png`
- Processed PNGs: `docs/assets/005_soviet_union_collapse/processed_png/optional_super_events/`
- Final DDS files: `gfx/super_events/super_event_black_banner_returns.dds`, `super_event_northern_signals_break.dds`, `super_event_workshops_choose_councils.dds`, `super_event_every_port_a_council.dds`
- Sprite definitions: `interface/chaosx_super_events.gfx`
- Source mode: generated with Codex built-in `image_gen` because these scenes are fictional high-chaos branch reveals rather than documentary reporting.

Quote notes:

- Slot `15` uses a short Proudhon excerpt. DuckDuckGo returned Wikiquote and quote collections for source checking; the final text keeps the excerpt short.
- Slot `16` uses Ecclesiastes 9:5, a public-domain biblical source in common English use.
- Slot `17` uses a short Karl Marx excerpt from *Capital* about machinery and labour; DuckDuckGo returned public web copies of Chapter 15.
- Slot `18` uses the Kronstadt slogan "All power to the soviets and not to parties"; DuckDuckGo returned Kronstadt rebellion reference pages and anarchist-history references for source checking.
- Slot `19` uses Mackinder's Heartland formula from *Democratic Ideals and Reality*. DuckDuckGo returned the Archive.org scan text for the 1919 Henry Holt edition, and the fetched text directly contains the formula in Chapter VI, `The Freedom of Nations`.
- Slot `20` uses a short line from Herodotus, *The Histories*, Book IV, about mobile steppe peoples being "invincible and impossible to approach"; Project Gutenberg's public-domain Macaulay translation was checked directly.
- Slot `21` uses a short Carl von Clausewitz line from *On War*; Project Gutenberg's public-domain J. J. Graham translation was checked directly.
- Slot `22` uses Deuteronomy 8:3 from the King James Version; Project Gutenberg ebook `10` was checked directly.
- Slot `23` uses Article II from the Articles of Confederation; the National Archives transcript was checked directly.
- Slot `24` uses a short Federalist No. 5 phrase from Project Gutenberg ebook `1404`.
- Slot `25` uses Proverbs 22:28 from the King James Version; Project Gutenberg ebook `10` was checked directly.
- Slot `26` uses Psalm 125:2 from the King James Version; Project Gutenberg ebook `10` was checked directly.
- Slot `27` uses a short Federalist No. 8 line from Project Gutenberg ebook `1404`.

Audio notes:

- Slots `15` and `18` reuse the already documented Beethoven Coriolan super-event track package.
- Slot `16` reuses the already documented Final Silence/Requiem track package.
- Slot `17` reuses the already documented Angelic World Order track package.
- Slot `19` reuses the already documented Beethoven Coriolan super-event track package because its cold political pressure fits the Ukraine great-power transformation without changing the wider Soviet-collapse audio identity.
- Slot `20` reuses the already documented Beethoven Coriolan super-event track package because its sparse political pressure fits the Steppe route's distance, statecraft, and railway-power tone.
- Slot `21` reuses the already documented Beethoven Coriolan super-event track package because its controlled political pressure fits Belarusian corridor sovereignty.
- Slot `22` reuses the already documented Final Silence/Requiem track package because its sparse, heavy tone fits ration power and hunger politics better than a martial reveal.
- Slot `23` reuses the already documented Beethoven Coriolan super-event track package because its restrained constitutional-crisis tone fits an equal-republics league without presenting the route as military triumph.
- Slot `24` reuses the already documented Beethoven Coriolan super-event track package because its restrained political pressure fits a federation formed from distance, railways, and contested patron access.
- Slot `25` reuses the already documented Beethoven Coriolan super-event track package because its restrained crisis tone fits Baltic restoration politics and defensive pact formation.
- Slot `26` reuses the already documented Beethoven Coriolan super-event track package because its restrained crisis tone fits mountain compact politics, defended passes, oil-road bargaining, and patron pressure around the southern collapse frontier.
- Slot `27` reuses the already documented Beethoven Coriolan super-event track package because its restrained political pressure fits a defensive western line built from border desks, rail junctions, foreign missions, and anti-reconquest pressure.
- These are wired as separate audio ids `15` through `27` in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset` so settings-aware playback works per slot.

## Package Audit Matrix

This matrix maps the implemented Event 005 super-events to their current artifact evidence. Localisation keys are in `localisation/english/005_soviet_collapse_l_english.yml`; image sprites are in `interface/chaosx_super_events.gfx`; audio variants are in `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset`; show helpers live in `common/scripted_effects/005_soviet_collapse_effects.txt`, with implemented route calls in `common/national_focus/005_soviet_collapse_republics.txt` and `common/national_focus/005_soviet_collapse_factory_successors.txt`.

| Slot | Title | Text keys | Quote/source status | Image status | Audio status | Trigger status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | The Union Unmade | `super_event.14.t/d/a/q` | Weber quote documented with Archive.org source note | sourced DDS wired | unique audio id wired from Coriolan package | fires from `soviet_collapse_setup_breakaway_country` through `soviet_collapse_maybe_show_union_unmade_super_event` | sourced image wired |
| `15` | The Black Banner Returns | `super_event.15.t/d/a/q` | Proudhon quote note documented; attribution remains reviewable | generated DDS wired | slot audio id wired from Coriolan package | fires from the Ukraine black-banner route and the `FTH` / `BBH` endgame helpers | none for generated image |
| `17` | The Workshops Choose Their Councils | `super_event.17.t/d/a/q` | local production quote note documented | generated DDS wired | slot audio id wired from the industrial package | `MFR_state_as_one_arms_order` calls `soviet_collapse_show_workshops_choose_councils_super_event` through the Military Factory package | none for generated image |
| `18` | Every Port a Council | `super_event.18.t/d/a/q` | Kronstadt slogan note documented | generated DDS wired | slot audio id wired from Coriolan package | fires from implemented port-council capstones for `KRS` and `ARD` routes | none for generated image |
| `19` | A Map Larger than the Union | `super_event.19.t/d/a/q` | Mackinder quote documented against Archive.org scan text of the 1919 Henry Holt edition | sourced DDS wired | slot audio id wired from Coriolan package | fires from `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map` | sourced image wired |
| `20` | The Steppe Beyond History | `super_event.20.t/d/a/q` | Herodotus quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Coriolan package | `kaz_soviet_collapse_the_southern_republics_do_not_kneel` calls `soviet_collapse_show_steppe_beyond_history_super_event` | sourced image wired |
| `21` | The Corridors Decide | `super_event.21.t/d/a/q` | Clausewitz quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Coriolan package | fires from `blr_soviet_collapse_the_corridor_state` or `blr_soviet_collapse_the_leagues_spine` | sourced image wired |
| `22` | The Bread State | `super_event.22.t/d/a/q` | Deuteronomy quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Final Silence package | fires from `ukr_soviet_collapse_last_harvest_plan` | sourced image wired |
| `23` | The League of Equal Republics | `super_event.23.t/d/a/q` | Articles of Confederation quote documented with National Archives source | sourced DDS wired | slot audio id wired from Coriolan package | fires from `ukr_soviet_collapse_league_of_equals` | sourced image wired |
| `24` | The Steppe Federation | `super_event.24.t/d/a/q` | Federalist No. 5 quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Coriolan package | fires from `kaz_soviet_collapse_steppe_federation_charter` and the `BSC`, `TNC`, and `ALA` Central Asian endgame helpers | sourced image wired |
| `25` | The Baltic League | `super_event.25.t/d/a/q` | Proverbs quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Coriolan package | fires from `baltic_soviet_collapse_baltic_defense_compact` | sourced image wired |
| `26` | The Caucasus League | `super_event.26.t/d/a/q` | Psalm quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Coriolan package | fires from `caucasus_soviet_collapse_caucasus_defense_compact` | sourced image wired |
| `27` | The Eastern Buffer Coalition | `super_event.27.t/d/a/q` | Federalist No. 8 quote documented with Project Gutenberg source | sourced DDS wired | slot audio id wired from Coriolan package | fires from `moldova_soviet_collapse_alliance_not_union` | sourced image wired |

## A Map Larger than the Union

- Super-event slot: `19`
- Localisation keys: `super_event.19.t`, `super_event.19.d`, `super_event.19.a`, `super_event.19.q`
- Trigger effect: `soviet_collapse_show_map_larger_than_union_super_event`
- Trigger direction: fires once from the Ukraine focus `ukr_soviet_collapse_endgame_a_ukraine_outside_the_old_map`.
- Role: great-power transformation, not a world-end scenario by default.
- Button text: `The borders answer.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `Who rules East Europe commands the Heartland;`
- Quote author: Halford J. Mackinder
- Quote source: *Democratic Ideals and Reality: A Study in the Politics of Reconstruction*, Henry Holt and Company, 1919, Chapter VI, `The Freedom of Nations`
- Verification source: DuckDuckGo result for the Archive.org 1919 scan plus fetched Archive.org OCR text. The fetched text directly contains Mackinder's formula in the paragraph beginning with the warning that statesmen should hear "this saying" during talks with the defeated enemy.
- Source URL: `https://archive.org/download/democraticideals00mack/democraticideals00mack_djvu.txt`
- Attribution confidence: high for the 1919 Henry Holt edition OCR and work attribution; if exact pagination is needed later, use the page-image PDF at `https://archive.org/download/democraticideals00mack/democraticideals00mack.pdf`.
- Rights note: the 1919 work is public-domain in the United States; the in-game excerpt is short.
- Why it fits: the Ukraine route is about Eastern Europe, map power, and the moment a breakaway republic starts thinking in regional corridors rather than inherited borders.

Image package:

- Asset: `super_event_map_larger_than_union`
- Sprite: `GFX_super_event_map_larger_than_union`
- Final DDS: `gfx/super_events/super_event_map_larger_than_union.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:Kiev_Cabinet_of_Ministers.jpg`
- Author: Daniel Haussmann
- License: Creative Commons Attribution-Share Alike 3.0 Unported, with other compatible historical licensing listed on the Commons file page
- License confidence: high; Wikimedia Commons file metadata lists the author, source, and license options
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_map_larger_than_union_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_map_larger_than_union_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_map_larger_than_union.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the Kyiv Cabinet of Ministers building gives the expansion route a state-building image rather than a battlefield image, matching the prompt's cold political-ascent tone.

## The Steppe Beyond History

- Super-event slot: `20`
- Localisation keys: `super_event.20.t`, `super_event.20.d`, `super_event.20.a`, `super_event.20.q`
- Trigger effect: `soviet_collapse_show_steppe_beyond_history_super_event`
- Trigger direction: fires once from the Kazakhstan focus `kaz_soviet_collapse_the_southern_republics_do_not_kneel`.
- Role: high-chaos regional transformation, not a world-end scenario by default.
- Button text: `The horizon answers.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `These assuredly are invincible and impossible to approach.`
- Quote author: Herodotus
- Quote source: *The Histories*, Book IV, section 46, G. C. Macaulay translation
- Verification source: Project Gutenberg ebook `2707`, public-domain Macaulay translation
- Source URL: `https://www.gutenberg.org/files/2707/2707-h/2707-h.htm`
- Attribution confidence: high for the translation/source; the line describes Scythian mobility, used here for the Steppe route's thematic emphasis on distance and mobile authority.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Kazakhstan high-chaos route turns distance, mobile command, railways, resources, and steppe memory into state power.

Image package:

- Asset: `super_event_steppe_beyond_history`
- Sprite: `GFX_super_event_steppe_beyond_history`
- Final DDS: `gfx/super_events/super_event_steppe_beyond_history.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:Turk-Sib_railway.jpg`
- Author: Petar Milosevic
- License: Creative Commons Attribution-Share Alike 3.0
- License confidence: high; Wikimedia Commons file metadata lists the author, source mode, and license.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_steppe_beyond_history_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_beyond_history_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_beyond_history.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the Turkestan-Siberia railway in the southern Kazakhstan steppe gives the route a concrete image of rail power crossing open distance.

## The Corridors Decide

- Super-event slot: `21`
- Localisation keys: `super_event.21.t`, `super_event.21.d`, `super_event.21.a`, `super_event.21.q`
- Trigger effect: `soviet_collapse_show_corridors_decide_super_event`
- Trigger direction: fires once from the Belarus focus `blr_soviet_collapse_the_corridor_state` or `blr_soviet_collapse_the_leagues_spine`.
- Role: corridor-sovereignty declaration, not a world-end scenario by default.
- Button text: `The timetable is authority.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `War is a mere continuation of policy by other means.`
- Quote author: Carl von Clausewitz
- Quote source: *On War*, J. J. Graham translation
- Verification source: Project Gutenberg ebook `1946`, public-domain Graham translation
- Source URL: `https://www.gutenberg.org/cache/epub/1946/pg1946.txt`
- Attribution confidence: high for the translation/source; the line is used here because Belarus's corridor route turns movement access, supply passage, and border administration into policy power.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Belarus corridor route makes logistics and passage rights the decisive political instrument between Moscow, western patrons, and the League.

Image package:

- Asset: `super_event_corridors_decide`
- Sprite: `GFX_super_event_corridors_decide`
- Final DDS: `gfx/super_events/super_event_corridors_decide.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:Refugees_on_train_roof.jpg`
- Author or archive: unknown photographer / The Ukrainian Museum Archives
- License: public domain in Ukraine and the United States per Commons `PD-Ukraine` tag
- License confidence: medium-high; Wikimedia Commons metadata identifies the 1933 image as a Ukrainian SSR work published before 1956, with unknown author and PD-Ukraine status.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_corridors_decide_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_corridors_decide_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_corridors_decide.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: a 1933 Ukrainian SSR refugee train gives the route a period image of rail corridors as survival infrastructure, crowd control, and contested passage rather than modern transit.

## The Bread State

- Super-event slot: `22`
- Localisation keys: `super_event.22.t`, `super_event.22.d`, `super_event.22.a`, `super_event.22.q`
- Trigger effect: `soviet_collapse_show_bread_state_super_event`
- Trigger direction: fires once from the Ukraine focus `ukr_soviet_collapse_last_harvest_plan`.
- Role: dark ration-state transformation, not a world-end scenario by default.
- Button text: `The card decides.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `Man shall not live by bread alone.`
- Quote author: Deuteronomy 8:3
- Quote source: King James Version
- Verification source: Project Gutenberg ebook `10`, public-domain King James Version text
- Source URL: `https://www.gutenberg.org/cache/epub/10/pg10.txt`
- Attribution confidence: high for the source; the line is used here as a moral counterpoint to a state that makes bread into an instrument of rule.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Ukraine bread-state route turns grain ledgers, ration cards, silo guards, port elevators, and rail convoys into coercive state power.

Image package:

- Asset: `super_event_bread_state`
- Sprite: `GFX_super_event_bread_state`
- Final DDS: `gfx/super_events/super_event_bread_state.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:%D0%A1%D0%B5%D0%BB%D1%8F%D0%BD%D0%B8_%D0%B7%D0%B4%D0%B0%D1%8E%D1%82%D1%8C_%D1%85%D0%BB%D1%96%D0%B1.jpg`
- Author or archive: unknown photographer / Central State Audiovisual and Electronic Archive of Ukraine
- License: public domain in Ukraine and the United States per Commons `PD-Ukraine` tag
- License confidence: medium-high; Wikimedia Commons metadata dates the image to 1930, identifies a Ukrainian archive source, and lists PD-Ukraine status.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_bread_state_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_bread_state_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_bread_state.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the 1930 Kyiv-region grain handover scene directly shows bread becoming a state-administered obligation, which matches the route's ration cards, guarded stores, and coercive grain ledgers.

## The League of Equal Republics

- Super-event slot: `23`
- Localisation keys: `super_event.23.t`, `super_event.23.d`, `super_event.23.a`, `super_event.23.q`
- Trigger effect: `soviet_collapse_show_league_equal_republics_super_event`
- Trigger direction: fires once from the Ukraine focus `ukr_soviet_collapse_league_of_equals`.
- Role: constitutional league transformation, not a world-end scenario by default.
- Button text: `No capital above the others.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `Each state retains its sovereignty, freedom and independence.`
- Quote author: Articles of Confederation, Article II
- Quote source: Articles of Confederation transcript
- Verification source: National Archives Milestone Documents transcript
- Source URL: `https://www.archives.gov/milestone-documents/articles-of-confederation`
- Attribution confidence: high for the source; the line is used here because the Ukraine League route turns breakaway survival into a formal order of equal republics.
- Rights note: United States federal source transcript of an eighteenth-century public-domain document; the in-game excerpt is short.
- Why it fits: the League route is about a republic-led order where Ukraine coordinates without claiming imperial succession.

Image package:

- Asset: `super_event_league_equal_republics`
- Sprite: `GFX_super_event_league_equal_republics`
- Final DDS: `gfx/super_events/super_event_league_equal_republics.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:1989_08_23_Baltijoskelias17e.jpg`
- Author: Rimantas Lazdynas
- License: Creative Commons Attribution-Share Alike 3.0 or GFDL
- License confidence: high; Wikimedia Commons file metadata lists the author and license options, and the same source original is already used by the Free Republics' League news image.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/news_free_republics_league_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_league_equal_republics_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_league_equal_republics.png`
- Target size: 457x328
- Processing notes: reused the League source original, cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the Baltic Way image emphasizes voluntary republican coordination and mass civic legitimacy rather than a single capital replacing Moscow.

## The Steppe Federation

- Super-event slot: `24`
- Localisation keys: `super_event.24.t`, `super_event.24.d`, `super_event.24.a`, `super_event.24.q`
- Trigger effect: `soviet_collapse_show_steppe_federation_super_event`
- Trigger direction: fires once from the Kazakhstan focus `kaz_soviet_collapse_steppe_federation_charter`.
- Role: regional faction formation, not a world-end scenario by default.
- Button text: `The rails count the votes.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `that combination and union of wills of arms and of resources,`
- Quote author: John Jay
- Quote source: *The Federalist No. 5*
- Verification source: Project Gutenberg ebook `1404`, *The Federalist Papers*
- Source URL: `https://www.gutenberg.org/cache/epub/1404/pg1404.txt`
- Attribution confidence: high for the public-domain text; the phrase is used here because the Steppe Federation is explicitly about combining political will, armed security, and logistical resources across distance.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Steppe Federation route turns distant republics, rail authorities, oasis councils, and garrisons into one bargaining structure without erasing local sovereignty.

Image package:

- Asset: `super_event_steppe_federation`
- Sprite: `GFX_super_event_steppe_federation`
- Final DDS: `gfx/super_events/super_event_steppe_federation.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:Turk-Sib_railway.jpg`
- Author: Petar Milosevic
- License: Creative Commons Attribution-Share Alike 3.0
- License confidence: high; Wikimedia Commons file metadata lists the author, source mode, and license, and the same source original is already used by The Steppe Beyond History.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_steppe_beyond_history_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_steppe_federation_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_steppe_federation.png`
- Target size: 457x328
- Processing notes: reused the Steppe Beyond History source original, cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the Turkestan-Siberia railway image gives the federation formation a concrete visual language of rail linkage, distance, and continental bargaining power.

## The Baltic League

- Super-event slot: `25`
- Localisation keys: `super_event.25.t`, `super_event.25.d`, `super_event.25.a`, `super_event.25.q`
- Trigger effect: `soviet_collapse_show_baltic_restoration_pact_super_event`
- Trigger direction: fires once from the Baltic regional focus `baltic_soviet_collapse_baltic_defense_compact`.
- Role: regional faction formation, not a world-end scenario by default.
- Button text: `The line is restored.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `Remove not the ancient landmark, which thy fathers have set.`
- Quote author: Proverbs 22:28
- Quote source: King James Version
- Verification source: Project Gutenberg ebook `10`, public-domain King James Version text
- Source URL: `https://www.gutenberg.org/cache/epub/10/pg10.txt`
- Attribution confidence: high for the source; the line is used here because the Baltic route frames restoration as refusal to accept an erased legal boundary.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Baltic League is about legal continuity, restored state borders, coast-watch coordination, and defensive guarantees rather than conquest.

Image package:

- Asset: `super_event_baltic_restoration_pact`
- Sprite: `GFX_super_event_baltic_restoration_pact`
- Final DDS: `gfx/super_events/super_event_baltic_restoration_pact.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:Lithuanian_Army_in_the_surroundings_of_Vilnius_Region,_1939.jpg`
- Author or archive: Unknown photographer / Marija and Jurgis Slapeliai House-Museum via Europeana
- License: CC0 / public-domain dedication on Commons
- License confidence: high; Wikimedia Commons metadata dates the image to 1939-10-28 and lists CC0.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_baltic_restoration_pact_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_baltic_restoration_pact_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_baltic_restoration_pact.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: Lithuanian soldiers near the Vilnius region in 1939 give the pact a period restoration image built around legal continuity, state return, road control, and defensive mobilization rather than a late-Cold-War protest.

## The Caucasus League

- Super-event slot: `26`
- Localisation keys: `super_event.26.t`, `super_event.26.d`, `super_event.26.a`, `super_event.26.q`
- Trigger effect: `soviet_collapse_show_caucasus_defense_compact_super_event`
- Trigger direction: fires once from the Caucasus regional focus `caucasus_soviet_collapse_caucasus_defense_compact`.
- Role: regional faction formation, not a world-end scenario by default.
- Button text: `The passes close ranks.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `As the mountains are round about Jerusalem, so the LORD is round about his people.`
- Quote author: Psalm 125:2
- Quote source: King James Version
- Verification source: Project Gutenberg ebook `10`, public-domain King James Version text
- Source URL: `https://www.gutenberg.org/cache/epub/10/pg10.txt`
- Attribution confidence: high for the source; the line is used here because the route frames collective mountain defense and encircled protection.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Caucasus League is about mountain passes, border roads, oil routes, and small republics using terrain and coordination to avoid being conquered separately.

Image package:

- Asset: `super_event_caucasus_defense_compact`
- Sprite: `GFX_super_event_caucasus_defense_compact`
- Final DDS: `gfx/super_events/super_event_caucasus_defense_compact.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:CAUCASUS_MOUNTAINS.jpg`
- Author or archive: NASA / Visible Earth
- License: public domain in the United States as a NASA work
- License confidence: high; Wikimedia Commons metadata lists the image as PD-USGov/NASA and identifies NASA as author.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_caucasus_defense_compact_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_caucasus_defense_compact_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_caucasus_defense_compact.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the satellite view makes the compact's terrain logic immediately visible: a defensive pact of ridgelines, passes, oil routes, and hard-to-subdue republics.

## The Eastern Buffer Coalition

- Super-event slot: `27`
- Localisation keys: `super_event.27.t`, `super_event.27.d`, `super_event.27.a`, `super_event.27.q`
- Trigger effect: `soviet_collapse_show_eastern_buffer_coalition_super_event`
- Trigger direction: fires once from the Moldova regional focus `moldova_soviet_collapse_alliance_not_union`.
- Role: regional faction formation, not a world-end scenario by default.
- Button text: `The line holds if the desks hold.`
- Button source: original remark, not a direct cultural quotation.
- Quote: `Safety from external danger is the most powerful director of national conduct.`
- Quote author: Alexander Hamilton, The Federalist No. 8
- Quote source: Project Gutenberg ebook `1404`, The Federalist Papers
- Source URL: `https://www.gutenberg.org/files/1404/1404-h/1404-h.htm`
- Attribution confidence: high; Project Gutenberg text has the line in Federalist No. 8.
- Rights note: public-domain source text; the in-game excerpt is short.
- Why it fits: the Eastern Buffer Coalition turns fear of reconquest and foreign pressure into a shared defensive line, while preserving unease about what emergency security does to republican politics.

Image package:

- Asset: `super_event_eastern_buffer_coalition`
- Sprite: `GFX_super_event_eastern_buffer_coalition`
- Final DDS: `gfx/super_events/super_event_eastern_buffer_coalition.dds`
- Source mode: internet source image
- Source URL: `https://commons.wikimedia.org/wiki/File:Soviet_invasion_on_Poland_1939.jpg`
- Author or archive: Unknown photographer / unknown source, hosted on Wikimedia Commons
- License: public domain in Russia and the United States per Commons `PD-Russia-1996` tags
- License confidence: medium; Wikimedia Commons metadata dates the image to 1939 and records the public-domain basis, but the original photographer and source are unknown.
- Source path: `docs/assets/005_soviet_union_collapse/source_original/super_event_eastern_buffer_coalition_source.jpg`
- Source PNG path: `docs/assets/005_soviet_union_collapse/source_png/super_event_eastern_buffer_coalition_source.png`
- Processed PNG path: `docs/assets/005_soviet_union_collapse/processed_png/super_event_eastern_buffer_coalition.png`
- Target size: 457x328
- Processing notes: cropped to the super-event aspect ratio, resized to 457x328, converted to black and white, and contrast-adjusted before DDS conversion.
- Review status: `wired, documented`
- Why it fits: the 1939 Soviet column in Poland turns the coalition into a period frontier-security scene: buffer troops, contested borders, road control, and improvised defensive administration under pressure from larger powers.
