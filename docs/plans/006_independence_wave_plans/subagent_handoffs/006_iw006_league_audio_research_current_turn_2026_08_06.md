# Event 006 League audio research, current-turn handoff

Research date: 2026-08-06.

Scope: bounded source, rights, jurisdiction, technical, and tone research for ordinary super-event/audio ID `23`, **The League of New States**. This handoff does not edit event scripts, gameplay, scripted localisation, `.gfx`, sound definitions, the canonical music catalogue, spreadsheets, slot dispatch, or firing logic. It does not replace the accepted cue without parent/user approval.

## Verdict

The accepted Jeremiah Clarke / London Brass Players recording of *A Trumpet Voluntary* remains blocked. The composition is public domain, but the exact 1948 recording first released in 1949 has no verified United States or worldwide redistribution permission in the reviewed evidence. It was not downloaded or processed.

The strongest redistribution-safe replacement candidate found and independently rechecked is **Toujours en Tête** (also described as *Defileermars van het Regiment Infanterie Johan Willem Friso*), composed by Adjudant S.P. van Leeuwen and performed by the Koninklijke Militaire Kapel ‘Johan Willem Friso’. The source is a Netherlands Ministry of Defence publication mirrored on Wikimedia Commons with a confirmed permission-ticket record. The Ministry's current copyright page states that its website material is CC BY-SA 4.0 and may be copied, distributed, and edited with attribution, change indication, and ShareAlike compliance. This supplies an explicit international license for the published composition/recording package rather than relying on age or a jurisdictional public-domain inference.

Candidate status is **rights-complete research candidate; parent/user selection and CC BY-SA integration review required**. It is not an implicit fallback and must not be wired as ordinary audio `23` until the replacement decision, human audition, and attribution/ShareAlike treatment are recorded.

## Event mapping

| Field | Value |
| --- | --- |
| Event | `006`, Independence Wave |
| Super-event role | League formation / irreversible international-institution proclamation |
| Display slot | `23` |
| Ordinary audio ID | `23` |
| Candidate title | *Toujours en Tête* / *Defileermars van het Regiment Infanterie Johan Willem Friso* |
| Composer | Adjudant S.P. van Leeuwen |
| Performer | Koninklijke Militaire Kapel ‘Johan Willem Friso’ |
| Candidate use | One-shot 110-second league-formation cue, subject to audition |
| Future base sound id | `chaosx_super_event_23_track` (parent-owned; not registered here) |
| Reserved eventual WAV | `sound/006_independence_wave/super_event_23_league_of_new_states.wav` |

## Source and license evidence

- Wikimedia Commons file page, stable revision checked: <https://commons.wikimedia.org/w/index.php?title=File:Defileermars_van_het_Regiment_Infanterie_Johan_Willem_Friso.ogg&oldid=1181959059>.
- Direct original download: <https://upload.wikimedia.org/wikipedia/commons/9/93/Defileermars_van_het_Regiment_Infanterie_Johan_Willem_Friso.ogg>.
- Commons raw description: <https://commons.wikimedia.org/w/index.php?title=File:Defileermars_van_het_Regiment_Infanterie_Johan_Willem_Friso.ogg&oldid=1181959059&action=raw>.
- Official source URL recorded by the Commons description: <https://www.defensie.nl/onderwerpen/muziek/downloads/geluidsfragmenten/2014/11/14/toujours-en-tete>. The old path now redirects through the Ministry site migration and currently returns a not-found page; the Commons copy preserves the original source declaration and VRTS permission ticket.
- Ministry copyright terms: <https://english.defensie.nl/service/copyright>.
- CC BY-SA 4.0 deed: <https://creativecommons.org/licenses/by-sa/4.0/>.
- Commons permission template: <https://commons.wikimedia.org/w/index.php?title=Template:Mindef&action=raw>.

The Commons page identifies the composer, band, Dutch Ministry source URL, `{{mindef}}` permission template, hidden `CC-BY-SA-4.0` category, and VRTS ticket `2010120610018876`. The template resolves to CC BY-SA 4.0 for Ministry works. The Ministry copyright page independently says the website is under CC BY-SA 4.0 and permits copy, distribution, and editing, while requiring credit to the Netherlands Ministry of Defence and an indication of alterations. The page also warns that unrelated third-party material is not covered; the source description names the Ministry military band and composer and gives no separate label or commercial-rights notice.

Composition and recording rights are therefore treated separately but covered by the same source-license record: this is **not** a public-domain claim. License confidence is **high** for worldwide redistribution of the identified Ministry-published work, with a practical integration condition that the mod distribution carry attribution, a change statement, a CC BY-SA 4.0 link, and a ShareAlike-compatible notice. If the parent cannot satisfy those obligations, retain this candidate as evidence only and keep audio `23` fail-closed.

Required/courtesy attribution for a 110-second edited derivative:

> Adjudant S.P. van Leeuwen, “Toujours en Tête” (1961); performed by Koninklijke Militaire Kapel “Johan Willem Friso”; source: Netherlands Ministry of Defence / Wikimedia Commons; licensed CC BY-SA 4.0; edited 110-second excerpt by Chaos Redux.

## Source technical record

The source was already preserved unchanged by the preceding candidate pass and was re-read in this pass.

- Local source: `docs/assets/006_independence_wave/super_events/audio/source/Defileermars_Toujours_en_Tete_Johan_Willem_Friso.ogg`.
- Container/codec: Ogg Vorbis, stereo, 44,100 Hz.
- Source duration: `145.946122 s` (Commons structured duration `145.94612244898 s`; page display `2 min 26 s`).
- Source bytes: `1,941,955`.
- Source SHA-256: `99CBD948C3066B7919BF75EB385736EDF81A500486284F857C6B06A1CF885D57`.
- Source SHA-1: `87009AB134CA63522C8BD4CE096387CB26BED5DA`, matching the Commons structured checksum.
- Source tags: no reliable embedded title/artist tags; identity comes from the Commons description and Ministry source record.

## Research derivative and measurements

The following files are evidence/audition derivatives only and have no runtime consumer.

- 110-second WAV candidate: `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_toujours_en_tete_110s_candidate.wav`.
- WAV profile: RIFF/WAV, PCM signed 16-bit little-endian, 44,100 Hz, stereo, exactly `110.000000 s`.
- WAV size: `19,404,332` bytes.
- WAV SHA-256: `7C2B417332309386E6FE1343F34520D9D67A754E6050EDD4E7CEE92D47B16680`.
- WAV SHA-1: `D11D73782F55AD5EFA237623CFFC37BD2536044C`.
- WAV readback: `-18.0 LUFS` integrated, `3.6 LU` LRA, `-5.1 dBFS` true peak; no detected silence interval of at least `0.25 s` below `-50 dBFS`.
- Ogg audition derivative: `docs/assets/006_independence_wave/super_events/audio/candidate/super_event_23_toujours_en_tete_110s_candidate.ogg`.
- Ogg audition profile: Ogg Vorbis, 44,100 Hz, stereo, exactly `110.000000 s`.
- Ogg audition size: `1,984,212` bytes.
- Ogg audition SHA-256: `508DDA83D0623B3DAD1526D7B55A82D7E6C439EB60B0F58B21B8C03796C5E5AF`.
- Ogg audition SHA-1: `FD51D549DBF7F7384FBBDBEBC4BEF135750D40B3`.

## Editing and conversion record

1. The original Ogg was preserved and hashed before derivative work.
2. The first `110.000000 s` were selected as a provisional one-shot excerpt within the preferred 1–2 minute window.
3. A `1.5 s` fade-in was applied at excerpt time `0.000`.
4. A `2.0 s` fade-out was applied from excerpt time `108.000` to `110.000`.
5. Two-pass loudness normalization targeted approximately `-18 LUFS` and `-2 dBTP`, preserving the source's restrained dynamics.
6. The derivative was resampled/encoded as stereo 44.1 kHz PCM S16LE WAV; a separate Vorbis Ogg audition copy was encoded from that WAV.
7. FFprobe readback confirmed duration, codec, sample rate, and stereo channels; FFmpeg decode and loudness readback succeeded.

The excerpt start/end are editorial boundaries, not a certified phrase-safe cadence. Human audition is required before promotion. Do not copy the candidate into the runtime sound folder until the parent explicitly approves the replacement.

## League-tone assessment

The march is a real structured musical recording with a clear ceremonial procession and institutional cadence. It supports a newly ratified league becoming a visible diplomatic order rather than a national victory or an abstract sound bed. The Dutch regimental identity is less U.S.-coded than the Marine Band Sousa candidates, but it still carries armed-ceremony associations. Suitability is **high for structured pacing and rights evidence; medium for the pluralistic League tone pending human audition and parent approval**.

## Comparison with blocked and research-only candidates

| Candidate | Rights/jurisdiction | Tone/pacing | Current disposition |
| --- | --- | --- | --- |
| Jeremiah Clarke, *A Trumpet Voluntary*, London Brass Players (1948/1949) | Composition public domain; exact recording lacks verified U.S./worldwide redistribution permission. | Best match for treaty/brass-and-organ ceremony. | Accepted original selection but **blocked**; do not download, process, or wire. |
| S.P. van Leeuwen, *Toujours en Tête*, Koninklijke Militaire Kapel ‘Johan Willem Friso’ | Explicit Ministry/VRTS CC BY-SA 4.0; worldwide copy/adaptation/distribution allowed with attribution and ShareAlike. | Ceremonial regimental march; 145.946 s source and clean 110 s derivative. | **Strongest rights-complete replacement candidate; user/parent review required.** |
| Carl Faust, *Defilier-Marsch*, Anker-Orchester | Public Domain Project `PD-INT` source determination, but no signed modern waiver; jurisdiction confidence conditional. | Strong structured parade pulse, but German period-march association. | Research-only; weaker rights certainty than the Ministry CC BY-SA candidate. |
| Ivo Muhvić, *Mačekova koračnica*, Croatian Armed Forces Symphonic Wind Orchestra | File-level CC0 recording dedication; composition jurisdiction was not independently established. | Regional title may read as partisan; 113.685 s source. | Research-only; composition-rights gate remains open. |
| John Philip Sousa, *Hands Across the Sea*, U.S. Marine/Navy Band | U.S. federal public-domain recording basis; not a worldwide CC0/public-domain determination. | Excellent league title/ceremonial fit, but strongly American-coded. | Jurisdiction-limited research-only candidate; not globally safe. |
| Jeremiah Clarke, Fehufanga harpsichord recording | Explicit CC BY-SA 3.0, but recording changes the accepted brass/organ character and requires ShareAlike. | Same composition, 108.135 s, but intimate harpsichord rather than public institutional ceremony. | Same-composition research-only fallback; weaker tonal fit. |
| Carl Teike, *Alte Kameraden* and other Anker/PDP transfers | Similar `PD-INT` project determinations without signed modern waivers. | Conventional marches but narrower German military associations. | Research reserve; not preferred. |

## Parent-owned promotion boundary

No runtime sound definition, wrapper, catalogue row, slot-23 firing effect, or playback assignment was created. If the parent/user approves this candidate and the CC BY-SA integration, the parent owns the eventual conversion to `sound/006_independence_wave/super_event_23_league_of_new_states.wav`, base sound/wrapper registration, ordinary audio ID `23`, canonical catalogue attribution, and settings-aware playback wiring. Until then, ordinary audio `23` remains absent and fail-closed as required by the accepted specification.

## Remaining gates and uncertainties

1. Parent/user must explicitly reopen the accepted cue selection; this candidate is not an implicit substitution.
2. Human audition must approve the 110-second opening/fade boundaries and Dutch regimental-march association.
3. The final mod distribution must preserve the CC BY-SA 4.0 attribution, edit statement, license link, and ShareAlike-compatible notice.
4. The old official audio-page URL currently redirects to a migrated not-found page; the Commons VRTS permission record, source description, direct mirror, and current Ministry copyright page remain available evidence.
5. If any new source page reveals third-party rights not covered by the Ministry permission, stop promotion and re-open rights review.

