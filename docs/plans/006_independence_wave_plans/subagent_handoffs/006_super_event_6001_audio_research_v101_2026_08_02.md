# Event 006 super-event 6001 audio research v101

> Superseded identifier note (2026-08-06): live Event 006 uses ordinary super-event ID 23 for League of New States. The legacy 6001 label is retained only for historical audit traceability.

> **Superseded audio research candidate (2026-08-03):** v109 replaces this Marine Band 2018 candidate as the strongest current research record and preserves v101 as historical evidence. No candidate is approved or wired. Use `006_super_event_6001_audio_research_v109_2026_08_02.md` for current rights, provenance, jurisdiction, and tonal-fit routing.

Research date: 2026-08-02.

Scope: bounded audio-rights research for Event 006 super-event `6001`, The League of New States. The accepted Jeremiah Clarke/London Brass Players recording remains blocked. This pass checked the existing 6001 research and package, found a separate rights-clear candidate, downloaded only the immutable source into the temporary event-scoped evidence folder, and performed no runtime, sound-definition, event, localisation, `.gfx`, GUI, spreadsheet, or catalogue edit.

## Decision

The strongest newly found candidate is John Philip Sousa's *Hands Across the Sea*, performed by the United States Marine Band in 2018 and conducted by Lieutenant Colonel Jason K. Fettig. The title and ceremonial march structure fit the league-formation role: the event announces that newly independent states have become a public international institution rather than isolated releases. The candidate is a different composition and recording from the accepted Jeremiah Clarke cue, not a disguised reuse of it.

This is a pending replacement candidate, not an approved final track. The accepted Event 006 specification requires explicit parent/user approval before reopening the selected 6001 recording. No derivative, final `.wav`, final `.ogg`, sound definition, wrapper, audio id assignment, or runtime wiring was created.

## Candidate record

- Track title: *Hands Across the Sea*.
- Composer: John Philip Sousa (1854-1932); the Commons file description records the 1899 composition date and identifies Sousa as composer.
- Performer and recording source: United States Marine Band, 2018; Lieutenant Colonel Jason K. Fettig is listed as conductor in the Commons file description.
- Commons source page: <https://commons.wikimedia.org/wiki/File:Sousa%27s_%22Hands_Across_The_Sea%22_-_United_States_Marine_Band_(2018).ogg>.
- Stable page evidence: <https://commons.wikimedia.org/w/index.php?title=File:Sousa%27s_%22Hands_Across_The_Sea%22_-_United_States_Marine_Band_(2018).ogg&oldid=910888599>.
- Commons raw description used for provenance: <https://commons.wikimedia.org/w/index.php?title=File:Sousa%27s_%22Hands_Across_The_Sea%22_-_United_States_Marine_Band_(2018).ogg&action=raw>.
- Direct original URL: <https://upload.wikimedia.org/wikipedia/commons/f/ff/Sousa%27s_%22Hands_Across_The_Sea%22_-_United_States_Marine_Band_%282018%29.ogg>.
- Official source credited by Commons: <https://www.marineband.marines.mil/Audio-Resources/The-Complete-Marches-of-John-Philip-Sousa/>.
- Source page description: track 56 from the Marine Band's 2018 album *The Complete Marches of John Philip Sousa: Vol. 4 (1899-1916)*.

## Rights and licensing evidence

Composition rights and recording rights are separate and both have a documented basis.

- Composition: the Commons file applies `PD-old-auto-expired` to Sousa's 1899 composition. Sousa died in 1932, so the composition is public domain under the source page's stated basis.
- Performance/recording: the Commons file applies `PD-USGov-Military-Marines`. The English template text states that the file is a work of a United States Marine or employee made as part of official duties and, as a work of the U.S. federal government, is public domain. The file's structured data also records public-domain status applying to the United States with the determination method “work of the federal government of the United States.”
- Commons license metadata reports `Public domain`, `UsageTerms=Public domain`, `Copyrighted=False`, and the hidden category `PD US Marines`.
- Attribution: no attribution is required by the stated public-domain basis. Recommended provenance credit, if retained in the catalogue, is `John Philip Sousa, Hands Across the Sea (1899); United States Marine Band (2018), conducted by Lt. Col. Jason K. Fettig; U.S. Marine Band / Wikimedia Commons, U.S. federal public domain.`
- License confidence: high for United States redistribution because the source page provides both the composition and U.S. federal performance/recording tags; medium for worldwide redistribution because a U.S. federal public-domain status is not a blanket worldwide copyright opinion.
- The official Marine Band URL linked by Commons returned HTTP 403 to this automated research client. The Commons raw description, file metadata, and license templates remain available as the primary evidence captured in this handoff. A parent-side manual source-page check is still prudent before final release.

## Preserved source and technical profile

- Local source path: `docs/assets/006_independence_wave/super_events/audio/source/Sousa_Hands_Across_The_Sea_United_States_Marine_Band_2018.ogg`.
- Source preservation: downloaded from the Commons `Special:Redirect/file/` endpoint, which resolves to the direct original URL above. The file was not edited.
- Source bytes: `7,302,316`.
- SHA-256: `5C5B4C3ADAB6E3D4A6BFB1496C0A02780B7B9F98697DC05B12369D93F7C955B6`.
- SHA-1: `36171615CA8F41512F4CF0B8336F1A0F4AA370EB` (matches Commons imageinfo metadata).
- Decoded format: Ogg container with Vorbis audio, 48 kHz, 2-channel stereo.
- Decoded duration: `167.185167` seconds.
- The source contains an embedded PNG stream in addition to the Vorbis audio stream. Any later conversion must map the audio stream explicitly and exclude the PNG (`-map 0:a:0`, `-vn`).
- A `-50 dBFS`/`0.25 s` silence scan found only the trailing source pause from approximately `165.495187` to `167.185167` seconds (`1.689979 s`). The first 110 seconds contain no detected silence of that threshold and duration.
- Whole-source loudness probe: approximately `-19.26 LUFS` integrated, `-0.19 dBTP` true peak, and `12.60 LU` LRA. A probe of the proposed first-110-second excerpt measured approximately `-20.42 LUFS`, `-1.55 dBTP`, and `12.30 LU` LRA before any final treatment.

## Super-event fit

- Suggested use: `6001`, league formation / faction formation / international institutional reveal.
- Fit rationale: the title directly evokes cooperation across borders, while the period brass-band march supplies the public proclamation and treaty-ratification energy expected from a HOI4-style super-event. It gives the league a distinct identity instead of reusing the blocked Clarke recording or another Event 006 cue.
- Suitability rating: medium-high for role and pacing, high for United States rights evidence, medium for worldwide rights certainty.
- Tone risk: this is a confident Sousa march with a strong American military-band idiom. It may read as more triumphant or U.S.-centered than the accepted legalist, covenant-oriented Clarke selection. Parent/user approval must explicitly accept that tonal and compositional change.
- Existing-catalogue check: `Hands Across the Sea`, Sousa, and the Marine Band recording are absent from `music/chaosx_music_track_list.html`; no existing Event 006 or super-event track was reused.

## Treatment constraints if replacement is approved

Do not perform these edits until the parent/user approves reopening 6001 selection.

1. Keep the immutable source file and its hashes above.
2. Trim the final in-game cue to no more than 110 seconds, matching the accepted package's maximum. A provisional edit window is `00:00.000-01:50.000` because it preserves the opening proclamation and avoids the known trailing pause; a human listening pass must confirm that the endpoint is musically phrase-safe before production.
3. If the first-110-second window cuts a phrase, compare a closing-window alternative such as `00:57.000-02:47.000` and select only after human review. Do not silently repeat or loop a march section.
4. Apply the accepted treatment target of a `1.5 s` fade-in and `2.0 s` fade-out, with the fade-out start adjusted to the approved excerpt length.
5. Normalize conservatively around `-18 LUFS` and no higher than `-2 dBTP`, preserving the march's dynamics rather than flattening it.
6. Deliver a 44.1 kHz stereo PCM WAV for the HOI4 runtime path. If a quality-preserving Ogg derivative is also requested by the parent workflow, derive it from the approved WAV and document both files separately.
7. Remove the embedded PNG stream during conversion and verify decoded duration, sample rate, channels, loudness, true peak, and final hash.

## Reserved implementation handoff (not wired)

These identifiers remain reserved by the accepted Event 006 package but were not written or assigned in this pass.

- Super-event: `6001`.
- Display slot: `23`.
- Reserved future runtime path: `sound/006_independence_wave/super_event_006_01_league_of_new_states.wav`.
- Suggested base sound name: `chaosx_super_event_6001_track`.
- Suggested settings wrappers: `chaosx_super_event_6001_sound_0_5`, `chaosx_super_event_6001_sound_1_0`, `chaosx_super_event_6001_sound_1_5`, `chaosx_super_event_6001_sound_2_0`, `chaosx_super_event_6001_sound_2_5`, and `chaosx_super_event_6001_sound_3_0`.
- After approval, the main agent must perform the existing collision check, register the final sound and wrappers, add the track to `music/chaosx_music_track_list.html`, and wire `global.current_super_event_audio_id = 6001` through `play_current_super_event_sound = yes`.

## Exact remaining gates

1. Obtain explicit parent/user approval to reopen the accepted 6001 recording selection; the Event 006 specification forbids silent substitution.
2. Confirm that the parent accepts the different Sousa composition, Marine Band instrumentation, and stronger march-nationalism risk for the pluralistic League of New States reveal.
3. Confirm the intended redistribution jurisdiction. The evidence is strong for U.S. redistribution, but the federal public-domain basis does not by itself guarantee worldwide copyright status.
4. Perform a human listening review of the proposed 110-second window and choose a phrase-safe start/end, with no looping or repeated section unless separately approved.
5. Only after gates 1-4, convert the preserved source to the final runtime WAV (and any requested Ogg derivative), record final hashes and measurements, and complete the main-agent sound-definition, settings-wrapper, catalogue, and super-event wiring.
6. Keep this source under the temporary event-scoped workspace while the replacement decision is pending. If 6001 is accepted and the event is later declared complete, promote durable provenance into permanent documentation before the event-scoped workspace is cleaned up; if the candidate is rejected, retain the handoff as rejection evidence and do not wire it.

## Status and blockers

The candidate is legally usable on the documented U.S. federal public-domain basis and is materially closer to the requested ceremonial super-event role than the prior same-composition organ/harpsichord alternatives. It is not final because selection reopening, tonal acceptance, jurisdiction review, phrase-boundary review, and all runtime production gates remain open. The accepted London Brass Players recording remains blocked, and no fallback, placeholder, derivative, or runtime audio was created.
