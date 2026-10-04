# Event 033 Acid Rain Audio Audition Gate Revalidation

Date: 2026-10-03.

Disposition: unresolved; the prompt's full-recording and excerpt-listening requirement has not been demonstrated in this revalidation.

Scope: source-recovery follow-up within the Event 033 audio package. The original source OGG was restored after its published size, SHA-1, and SHA-256 matched. This gate note records that recovery. No excerpt, runtime audio asset, catalogue, event, sound definition, or wiring file was changed, and no commit was made.

## Gate result

The Event 033 prompt requires listening to the complete source recording, selecting an excerpt no longer than two minutes, and confirming that the selected interval fits the formation scene. This revalidation did not hear either the complete recording or the selected excerpt, so it cannot accept the auditory-fit portion of the audio package.

Listening method: none. The attached audio item was supplied with the notice “audio content omitted because you do not support audio input.” The original source path recorded in the handoff, `docs/assets/033_acid_rain/source_audio/Carl_Maria_von_Weber_-_Der_Freischuetz_Overture.ogg`, was missing during the initial read-only check and has since been restored with exact-byte verification. The source and installed WAV now exist as files, but this runtime exposes no audio-listening input for either.

Audible content heard: none. No claim is made about the source's mood, instrumentation, speech, applause, musical development, or the sound at either edit boundary.

Entry and exit fit: unverified. The reported excerpt is 61.500-141.500 seconds, with an 80.000-second final duration. Whether its opening enters naturally, its ending releases coherently, or either boundary conflicts with the formation reveal cannot be judged here.

Uncertainty: the prior handoff describes a dark opening, rising threat, central surge, and controlled release. Its listed evidence consists of waveform and spectrogram images plus signal measurements. Those can document signal shape and technical properties, but they do not prove auditory perception. This report does not infer that a previous researcher did or did not listen; it records that the evidence reviewed here does not establish the required listening gate.

## Prior acceptance versus the required gate

`docs/assets/033_acid_rain/audio_manifest.json` currently marks the package `ACCEPTED` / `accepted_replacement`, and its decision basis includes “audition.” `docs/assets/033_acid_rain/audio_research_handoff.md` likewise calls the Weber replacement accepted and describes audition evidence, but the evidence it enumerates is visual signal analysis rather than proof of listening.

Those prior status fields record metadata and technical acceptance claims. They do not resolve the prompt-level auditory requirement in this revalidation. For this gate, source and recording rights remain supported, runtime-file integrity and exact-binary uniqueness were rechecked, while musical suitability and edit-boundary fit remain unresolved.

## Source and rights recheck

The exact Wikimedia Commons file page identifies *Der Freischütz*, J. 277, Overture, as performed by the Skidmore College Orchestra, and identifies Musopen as the source. It states that Musopen released the recording into the public domain worldwide, records Wikimedia VRT ticket 2008012110017088, and gives the courtesy request to credit Musopen and not sell the recording by itself. The page also reports the source file's SHA-1 as `5bba4a3a3b14620a44f9d66e5ec4a5d53a3fa273`, size as 13,152,669 bytes, and duration as 617.64 seconds. [Exact Commons file page](https://commons.wikimedia.org/wiki/File:Carl_Maria_von_Weber_-_der_freischutz,_j._277_-_overture.ogg).

This current page review supports the handoff's recording-rights and performer claims, with high confidence for the stated public-domain reuse terms and courtesy attribution. A request to the [Commons original-file URL](https://upload.wikimedia.org/wikipedia/commons/5/5d/Carl_Maria_von_Weber_-_der_freischutz%2C_j._277_-_overture.ogg) first returned HTTP 429. The [same file's Commons redirect](https://commons.wikimedia.org/wiki/Special:Redirect/file/Carl_Maria_von_Weber_-_der_freischutz,_j._277_-_overture.ogg) then returned the source bytes, now preserved at the recorded local path. The recovered file is 13,152,669 bytes, has SHA-1 `5BBA4A3A3B14620A44F9D66E5EC4A5D53A3FA273`, and has SHA-256 `27108788AF4CA24176D09BA49062EEDEA077C5C6C8F053D6451584FF9255D56D`, matching all published integrity values. This closes the local source-byte identity gap; it does not satisfy the listening gate.

## Current work-level uniqueness and runtime file

The current canonical catalogue has one matching Weber / *Der Freischütz* row, at `music/chaosx_music_track_list.html` lines 795-800. It records playback ID 117 as exclusive to Event 033. The exact-title and composer search found no second matching catalogue entry. The catalogue statement is recorded as current catalogue evidence; runtime wiring was not re-audited here, consistent with the parent's confirmation that wiring is unchanged.

A fresh SHA-256 inventory of all 311 `.wav` and `.ogg` files under `sound/` found exactly one match for each accepted runtime digest, and each match is the Event 033 file itself. The installed WAV exists at `sound/033_acid_rain/super_event_033_acid_rain_formation.wav`, is 14,112,404 bytes, and hashes to `C0BD481F23AECD058BBCC49F54570353CA2974FF5EED9E497B6980721AABB033`. The companion OGG's recorded digest, `7951F486E425CB059C34C093190EBBE040DB10F3570FE3BC4309E89F6C1A4951`, also matched exactly once at its Event 033 path. This establishes current exact-binary uniqueness in the installed sound folder; it says nothing about subjective musical fit.

## Handoff

Keep the existing Weber files and rights documentation unchanged during this bounded pass; no replacement or fallback was authorized. The auditory acceptance status remains unresolved until the complete 617.640-second source and the 61.500-141.500-second excerpt are actually played and heard, with the listening method, audible content, and entry and exit fit recorded by an audio-capable reviewer.

No game start/stop, settings-volume, disabled-setting, missing-audio, or multiplayer behavior was tested here; those engine and runtime checks remain with the orchestrator.
