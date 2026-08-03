# Event 012 Africa super-event audio roles 1 and 4 re-audit

Superseded on 2026-08-03 by `012_africa_super_event_audio_cc0_roles_1_4_2026-08-03.md`. The original-commission-only blockers recorded below remain historical research, not the current Event 012 runtime disposition.

Prepared: 2026-07-30

Scope: narrow audio research and acceptance audit for role 1, **Africa is one**, and role 4, **The World**. This note does not edit sound definitions, event files, localisation, GFX, GUI, catalogue rows, or gameplay wiring. It supersedes neither the canonical Event 012 audio research handoff nor the 2026-07-30 four-role audit; it records the current acceptance boundary after a fresh source-folder, runtime, registry, and identifier check.

## Disposition

Neither missing role reached the production gate. No final `.wav` or `.ogg` was created for audio IDs `58` or `61`, no source was promoted to runtime, and no identifier was reserved.

| Role | Slot / audio ID | Current disposition | Why it cannot be accepted |
| --- | --- | --- | --- |
| Africa is one | `101 / 58` | **Blocked** | The approved brief requires a separately commissioned, through-composed `110.000 s` master with identified composer, performers, producer, stems or a lossless multitrack archive, and a signed worldwide perpetual editable redistribution/synchronization/sublicensing grant. No such commission or rights chain exists. |
| The World | `104 / 61` | **Blocked** | The approved brief requires a separately composed and separately credited `116.000 s` master under the same complete composition, performance, recording-master, contributor-release, and worldwide redistribution contract. No such commission or rights chain exists. |

The canonical role briefs intentionally reject an anthem, a generic “African” cue, a generic “world” library cue, or a reuse/derivative of the other role. No fallback is approved.

## Role 1 candidate retained for review only

- Title: *Enough of the Past*.
- Creator/artist: Pamela Yuen; no separate performer is identified by the source record.
- Source page: <https://freemusicarchive.org/music/pamela-yuen/cinematic-orchestral-hybrid/enough-of-the-past/>.
- Direct source URL: <https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/6ADeaAUClg6KShMzeR3N295pCDEAfGK2PR4Llztk.bin>.
- Rights page: <https://pamelayuen.blogspot.com/p/cc-by-4.html>.
- License: CC BY 4.0, with attribution and change notice; the artist permits game/commercial use and adaptation but prohibits isolated music resale and music-service redistribution.
- License confidence: medium-high for synchronized review use, below the Event 012 acceptance threshold because there is no signed contributor/producer release or master-level sublicensing agreement.
- Preserved source: `docs/super_events/source_audio/012_africa/candidates/pamela_yuen/pamela_yuen_enough_of_the_past_source.bin`.
- Source properties: `115.500 s`, stereo MP3 in an FMA `.bin` container, 44,100 Hz, `11,931,287` bytes.
- Source SHA-256: `b0c7f2dd52dc0c2b6a5cca5e858a34a01701b3d30415d30066036c1053f0d723`.
- Review derivative (not runtime): `docs/super_events/processed_audio/012_africa/candidates/role_01_enough_of_the_past_candidate_110s.wav`, `110.000 s`, 24-bit stereo 44.1 kHz, SHA-256 `42449b584fa25e42ff8afb41c856ce2907b0a3d74fb51b58a0025461ae0dacc1`.
- Edit record: first `110.000 s`, fixed gain `-8.6 dB`, `0.100 s` fade-in, `3.000 s` fade-out from `107.000 s`, no loop/time-stretch/pitch change/compression/limiter.
- Candidate evidence: `docs/super_events/source_audio/012_africa/candidates/pamela_yuen/evidence/fma_enough_of_the_past.html`, `pamela_yuen_cc_by_terms.html`, and `cc_by_4_0_deed.html`.
- Fit: structured instrumental cinematic arc, no language dependency, and no anthem identity. It is not proof of the requested independent counterline, culturally accountable commissioned production, lossless master, stems, or signed rights chain. The source is lossy MP3, so the 24-bit WAV is only an up-converted review derivative.
- Decision: **needs user/design approval and a stronger rights/source package; do not promote or wire**.
- If a later explicit design amendment approves it, the provisional mapping remains audio ID `58`, raw sound `chaosx_super_event_africa_is_one_track`, slot `101`, and wrappers `chaosx_super_event_58_sound_0_5` through `_sound_3_0`. None are registered.

## Role 4 candidate retained for review only

- Title: *Fiery Word*.
- Creator/artist: Pamela Yuen; no separate performer is identified by the source record.
- Source page: <https://freemusicarchive.org/music/pamela-yuen/cinematic-orchestral-hybrid/fiery-word/>.
- Direct source URL: <https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/EppvZxw3yjfzo3HN55vQcJ28WCC7mKD7XOemh4YD.mp3>.
- Rights page: <https://pamelayuen.blogspot.com/p/cc-by-4.html>.
- License: CC BY 4.0 with attribution and change notice under the same artist terms as role 1.
- License confidence: medium-high for synchronized review use, below the Event 012 acceptance threshold because no signed contributor/producer release, lossless master, stems, or master-level sublicensing agreement is available.
- Preserved source: `docs/super_events/source_audio/012_africa/candidates/pamela_yuen/pamela_yuen_fiery_word_source.mp3`.
- Source properties: `134.400 s`, stereo MP3, 44,100 Hz, `5,471,429` bytes.
- Source SHA-256: `0bfd7c5d67ac485119166f37e28d5d14f06a3d1a6f3d021ed35ab5e368d16cf4`.
- Review derivative (not runtime): `docs/super_events/processed_audio/012_africa/candidates/role_04_fiery_word_candidate_116s.wav`, `116.000 s`, 24-bit stereo 44.1 kHz, SHA-256 `1c4b37df7f025166be5978e3f5727d65f35dc2e6e3963544282b64081652578a`.
- Edit record: first `116.000 s`, fixed gain `-8.9 dB`, `0.100 s` fade-in, `3.000 s` fade-out from `113.000 s`, no loop/time-stretch/pitch change/compression/limiter.
- Candidate evidence: `docs/super_events/source_audio/012_africa/candidates/pamela_yuen/evidence/fma_fiery_word.html`, `pamela_yuen_cc_by_terms.html`, and `cc_by_4_0_deed.html`.
- Fit: structured orchestral/cinematic arc with no vocal or language dependency. The title and large peaks can imply fiery victory/escalation rather than the approved exhausted, irreversible terminal identity, and the source is lossy MP3 with no stems or signed master grant.
- Decision: **needs user/design approval and a stronger rights/source package; do not promote or wire**.
- If a later explicit design amendment approves it, the provisional mapping remains audio ID `61`, raw sound `chaosx_super_event_the_world_track`, slot `104`, and wrappers `chaosx_super_event_61_sound_0_5` through `_sound_3_0`. None are registered.

## Current runtime and identifier check

- `sound/012_africa/` contains only `super_event_59_scramble_response.wav` and `super_event_60_continental_wars.wav`; no role 1 or role 4 runtime file exists.
- `sound/chaosx_sound.asset` contains role 2/3 registrations and wrappers only. There is no `chaosx_super_event_africa_is_one_track`, `chaosx_super_event_the_world_track`, `super_event_58`, or `super_event_61` registration.
- `music/chaosx_music_track_list.html` contains role 2/3 rows but no final row for audio ID `58` or `61`.
- A narrow scan of the current sound and music registries found no live use of IDs `58` or `61`; repeat the full collision scan immediately before any future atomic registration.

## Acceptance requirements and blocker

To clear either role, obtain the commissioned original master matching the exact duration/brief, frozen composer/arranger/performer/producer credits, signed contributor releases, lossless 24-bit source and stems or equivalent multitrack archive, sample clearances, worldwide perpetual irrevocable royalty-free editable synchronization/distribution/mirroring/sublicensing rights, final 44.1 kHz runtime derivative, and decoded-audio uniqueness evidence. Until then, preserve the candidate source/evidence and review WAVs but do not create runtime files, sound definitions, catalogue rows, or gameplay references.

No unrelated Event 006 files were touched. No commit was created by this re-audit.
