# Event 006 super-event 23 audio re-verification v117

Research date: 2026-08-22.

Scope: fresh bounded rights, provenance, integrity, alternative-search, and tone-fit verification for Event 006, **The League of New States**, using ordinary display/audio identifier `23`.

This note does not edit event scripts, gameplay, scripted localisation, `.gfx`, sound definitions, the canonical music catalogue, spreadsheets, slot dispatch, or firing logic.

## Decision

The accepted Jeremiah Clarke / London Brass Players recording of *A Trumpet Voluntary* remains blocked because its 1948 recording released in 1949 has no verified United States or worldwide redistribution permission.

The existing *Toujours en Tête* / *Defileermars van het Regiment Infanterie Johan Willem Friso* candidate remains the strongest currently documented replacement for rights and musical structure, but it is not promoted or runtime-wired.

On the stated source record, CC BY-SA 4.0 permits worldwide sharing, adaptation, and commercial redistribution of the recording and the 110-second derivative, provided the distributed mod carries attribution, a license link, a change notice, and ShareAlike treatment without adding restrictions to the audio.

The candidate still requires explicit parent/user selection, a parent-owned ShareAlike integration decision, and human audition of the excerpt before audio ID `23` can leave its fail-closed state.

No stronger candidate was found that combines equally clear composition-and-recording rights, complete identity/provenance, a structured 1–3 minute cue, and a better fit for a pluralistic league proclamation.

## Current source verification

| Field | Verified value | Evidence and confidence |
| --- | --- | --- |
| Track title | *Toujours en Tête*, also described as *Defileermars van het Regiment Infanterie Johan Willem Friso* | Current [Wikimedia Commons file record](https://commons.wikimedia.org/w/index.php?title=File:Defileermars_van_het_Regiment_Infanterie_Johan_Willem_Friso.ogg&oldid=1181959059), revision `1181959059` checked on 2026-08-22 |
| Composer | Adjudant S.P. van Leeuwen; Commons description says the march was composed for the regiment in 1961 | Current Commons file description; composition is not treated as public domain |
| Performer | Koninklijke Militaire Kapel ‘Johan Willem Friso’ | Current Commons file description and `Artist` metadata |
| Recording date | Not stated; Commons `Date` is 2020-02-09 and is treated as source publication/upload metadata, not a recording date | Current Commons file record |
| Official source | [Netherlands Ministry of Defence music page](https://www.defensie.nl/onderwerpen/muziek/downloads/geluidsfragmenten/2014/11/14/toujours-en-tete) | The URL is still recorded by Commons but returned HTTP 404 on 2026-08-22, so the Commons/VRT record is the durable source evidence |
| Preserved direct source | [Wikimedia Commons original Ogg](https://upload.wikimedia.org/wikipedia/commons/9/93/Defileermars_van_het_Regiment_Infanterie_Johan_Willem_Friso.ogg) | Local SHA-1 exactly matches the current Commons file record |
| License | Creative Commons Attribution-ShareAlike 4.0 International | Current Commons file record, [Commons `Mindef` permission template](https://commons.wikimedia.org/wiki/Template:Mindef), and [current Ministry copyright page](https://english.defensie.nl/service/copyright) agree on CC BY-SA 4.0 |
| License confidence | High for the published recording permission; medium-high overall because the original Ministry music URL is now unavailable and the recording date is not stated | Commons records a VRT-confirmed Ministry permission ticket `2010120610018876`; the current Ministry copyright page confirms website copy/distribution/editing under CC BY-SA 4.0 |
| Source duration | `145.946122 s` (`2:25.946`) | Local FFprobe readback; Commons page rounds to 2 min 26 s |

## Composition and recording rights

### Composition

The composition is identified as a 1961 work by Adjudant S.P. van Leeuwen and is not assumed to be public domain.

The rights basis is the Netherlands Ministry of Defence permission record represented by the Commons `Mindef` template, rather than an expired composition term.

### Recording

The recording is identified as the Koninklijke Militaire Kapel ‘Johan Willem Friso’ performance published from the Netherlands Ministry of Defence music source.

The Commons file records a VRT-confirmed Ministry permission and explicitly applies CC BY-SA 4.0, so the recording may be shared, adapted, and redistributed worldwide under that license.

The [CC BY-SA 4.0 deed](https://creativecommons.org/licenses/by-sa/4.0/) requires appropriate credit, a license link, an indication of changes, and distribution of the adapted recording under the same or a compatible license.

For a distributed mod, the parent must keep the edited audio derivative under CC BY-SA 4.0 or a compatible license, include the attribution and license URL in permanent audio documentation/credits, state the 110-second trim, fades, loudness normalization, and format conversion, and avoid archive or platform terms that impose additional restrictions on the audio itself.

Suggested attribution text:

> Adjudant S.P. van Leeuwen, “Toujours en Tête” (1961); performed by Koninklijke Militaire Kapel “Johan Willem Friso”; source: Netherlands Ministry of Defence / Wikimedia Commons; licensed CC BY-SA 4.0; edited 110-second excerpt by Chaos Redux.

This is a rights-complete candidate on the recorded evidence, not legal advice or a CC0/public-domain claim.

## Preserved source and derivative integrity

The original source remains unchanged at `docs/assets/006_independence_wave/super_events/audio/source/Defileermars_Toujours_en_Tete_Johan_Willem_Friso.ogg`.

| File | Bytes | Codec/profile | Duration | SHA-1 | SHA-256 |
| --- | ---: | --- | ---: | --- | --- |
| `docs/assets/006_independence_wave/super_events/audio/source/Defileermars_Toujours_en_Tete_Johan_Willem_Friso.ogg` | `1,941,955` | Ogg Vorbis, stereo, 44.1 kHz | `145.946122 s` | `87009AB134CA63522C8BD4CE096387CB26BED5DA` | `99CBD948C3066B7919BF75EB385736EDF81A500486284F857C6B06A1CF885D57` |
| `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_toujours_en_tete_110s_candidate.wav` | `19,404,332` | RIFF PCM S16LE, stereo, 44.1 kHz | `110.000000 s` | `D11D73782F55AD5EFA237623CFFC37BD2536044C` | `7C2B417332309386E6FE1343F34520D9D67A754E6050EDD4E7CEE92D47B16680` |
| `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_toujours_en_tete_110s_candidate.ogg` | `1,984,212` | Ogg Vorbis, stereo, 44.1 kHz audition derivative | `110.000000 s` | `FD51D549DBF7F7384FBBDBEBC4BEF135750D40B3` | `508DDA83D0623B3DAD1526D7B55A82D7E6C439EB60B0F58B21B8C03796C5E5AF` |

The local source SHA-1 matches the current Commons file record `87009ab134ca63522c8bd4ce096387cb26bed5da`.

## Editing and conversion record

The source was downloaded from the Commons original URL before derivative work and has not been overwritten.

The provisional excerpt uses the first `110.000000 s` of the `145.946122 s` source, with a `1.5 s` fade-in and a `2.0 s` fade-out beginning at excerpt time `108.000 s`.

The derivative was normalized to approximately `-18.0 LUFS` and `-2 dBTP`, rendered as stereo 44.1 kHz PCM S16LE WAV, and encoded separately as a Vorbis Ogg audition file.

The WAV and Ogg are research/audition derivatives only; no runtime sound file, sound definition, wrapper, catalogue row, or firing assignment was created.

No human audition was performed in this verification pass, so phrase-safe start/end points, the perceived ending, and the military-regimental versus egalitarian balance remain open.

## Super-event mapping and proposed future wiring

| Field | Value |
| --- | --- |
| Event | `006`, Independence Wave |
| Super-event | **The League of New States** |
| Role | League formation / irreversible international-institution proclamation |
| Display slot | `23` |
| Ordinary audio ID | `23` |
| Suggested base sound ID | `chaosx_super_event_23_track` |
| Suggested settings wrappers | `chaosx_super_event_23_sound_0_5`, `_1_0`, `_1_5`, `_2_0`, `_2_5`, `_3_0` |
| Reserved eventual runtime WAV | `sound/006_independence_wave/super_event_23_league_of_new_states.wav` |

The march has a clear ceremonial procession and institutional cadence, which supports a public ratification or league proclamation better than an abstract ambient cue.

Its regimental military identity can also read as hierarchy or state ceremony rather than sovereign equality, so tone suitability is **medium pending human audition**, not an unconditional fit.

## Alternative search and verdicts

The following clear-license structured candidates were checked against the current Commons records and rejected without download or runtime use.

| Candidate | Current evidence | Verdict |
| --- | --- | --- |
| [Trænregimentets March](https://commons.wikimedia.org/wiki/File:Tr%C3%A6nregimentets_March.ogg) | CC BY-SA 4.0 with VRT-confirmed permission ticket `2017061610010514`, 186.362676 s, performer Prinsens Musikkorps; page lists only `Source=Compact Disc` and does not identify the composer or composition-right basis | Not stronger: recording permission is clear, but composition rights and source provenance are incomplete; also another Danish regimental march with the same hierarchical-tone risk |
| [The Enola Foam March](https://commons.wikimedia.org/wiki/File:The_Enola_Foam_March.flac) | Explicit CC BY-SA 4.0 self-publication by `Peeeeet`, original 2012 composition, 176 s, described as a WWII-style orchestral march with slight Klezmer influence | Legally plausible, but no separate performer/recording identity or independent provenance; the WWII-style and Klezmer framing is less institutionally neutral for this league moment |
| [First May March in 4 languages](https://commons.wikimedia.org/wiki/File:First_May_March_in_4_languages_(Turkish-Kurdish-Armenian-Lazuri).ogg) | Commons marks CC BY 4.0 and credits Can Karakulak, but the 357.262222 s recording is sourced to a YouTube upload whose current page exposes no CC license metadata, and no composer/performer split is supplied | The multilingual egalitarian theme is attractive, but recording/composition rights cannot be verified without relying on the Commons uploader’s assertion; rejected as unclear rather than adopted |
| [Lully, *Marche pour la Cérémonie des Turcs*](https://commons.wikimedia.org/wiki/File:Lully_Le_Bourgeois_Gentilhomme_-_11._Marche_pour_la_Ceremonie_des_Turcs.ogg) | CC BY-SA 2.0, 130 s, Advent Chamber Orchestra; Commons license chain relies on the legacy EFF Open Audio License/ibiblio record | Structured and ceremonial, but the older license chain and source availability are weaker than the Ministry/VRT CC BY-SA 4.0 record |
| [Oft in the Stilly Night](https://commons.wikimedia.org/wiki/File:Oft_in_the_Stilly_Night.ogg) | CC0 self-publication, 82.6855 s, uploader Endersslay; page does not identify a composer or separate performer and describes it as a slow march associated with the 2nd Battalion Ulster Defence Regiment | Worldwide-clear license, but incomplete musical identity, short duration, and politically specific military association make it unsuitable for this role |

No alternative found in this pass is simultaneously clearer in rights, more complete in provenance, and a better tonal match than *Toujours en Tête*.

## Exact remaining gates

1. The parent/user must explicitly approve replacing the blocked Clarke recording with *Toujours en Tête*.
2. The parent must approve the CC BY-SA integration treatment and preserve attribution, license URL, change notice, and ShareAlike status in permanent audio documentation and distribution materials.
3. A human must audition the 110-second excerpt and approve its start/end, fade endpoint, ending cadence, loudness, and regimental-military association.
4. The parent must accept the unavailable official Ministry music URL as a provenance caveat or obtain an archived/current official source confirmation.
5. Until gates 1–4 are recorded, keep audio ID `23`, its wrappers, runtime file, catalogue row, dispatch, and firing/playback assignment absent.

## Parent handoff

Candidate verdict: **retain as the strongest rights-complete replacement candidate; do not promote yet**.

Evidence links: [current Commons record](https://commons.wikimedia.org/w/index.php?title=File:Defileermars_van_het_Regiment_Infanterie_Johan_Willem_Friso.ogg&oldid=1181959059), [Commons `Mindef` permission](https://commons.wikimedia.org/wiki/Template:Mindef), [Netherlands Ministry copyright page](https://english.defensie.nl/service/copyright), [CC BY-SA 4.0 deed](https://creativecommons.org/licenses/by-sa/4.0/), and [official music URL currently returning 404](https://www.defensie.nl/onderwerpen/muziek/downloads/geluidsfragmenten/2014/11/14/toujours-en-tete).

Files changed: this handoff note only.

Runtime wiring: none.

Simplifications or blockers: accepted Clarke recording remains blocked; Dutch candidate has a source-URL availability caveat, ShareAlike integration gate, and human-audition gate; no fallback was silently selected.
