# Audio Provenance Handoff — Event 003 Holy Realm

Disposition: neither requested runtime row has confirmed source-to-runtime provenance. The source pages provide usable licensing statements, but ID 9’s original bytes are unavailable under the current network throttle and the downloaded Internet Archive source candidate for ID 28 does not match the listed 120–150 second passage. No runtime WAV, sound definition, event, localisation, or other wiring was changed.

## Requested rows

| ID and cue | Sound definition | Rights and source record | Runtime evidence and status |
| --- | --- | --- | --- |
| 9 — Thermonuclear Final Silence | `chaosx_super_event_final_silence_thermonuclear_track` | “Chanting at Lingyin Temple, Hangzhou,” a Louise Brown field recording of Buddhist monks, is CC BY-SA 3.0 Unported. The source page requires attribution, a license link, a change notice, and share-alike distribution. Commons revision `917959876`; remote original is 755,026 bytes, 63.268957 seconds, SHA-1 `cc4eaa3c0b7a742aa6ab4b3aaa54d601f9fc63df`. | Runtime `sound/003_holy_realm/super_event_9_final_silence_thermonuclear.wav`, 63.188005 seconds, SHA-256 `26baa65e2095bc3a96de73cf7b3b406ac42730ff5e06b9cc52ce7c7222a19dd7`. No local source bytes and no source/runtime comparison. The parent brief says canonical Final Silence delegates to the Fallout-owned terminal modal and this legacy ID 9 cue may not be actively consumed; playback remains unconfirmed. |
| Display slot 51 / audio ID 28 — Mandala of Nations | `chaosx_super_event_mandala_of_nations_track` | Commons describes a 120–150 second excerpt from Ven. Chan Master Hsuan Hua’s recording and states CC BY-SA 3.0; the excerpt contributor Sarah Welch licenses her preparation under the same terms. Commons revision `917959865`; the 30.022676 second OGG metadata is 248,206 bytes, SHA-1 `ae802b04be876693f30c89c65a665d8b27b1f0f1`. The linked Internet Archive item also marks CC BY-SA 3.0. | Runtime `sound/003_holy_realm/super_event_28_mandala_of_nations.wav`, 30.751927 seconds, SHA-256 `e0f519cc9143b3b6c352e032f6e74f3631aac4e2f651f1c04200de843b8cd76e`. The downloaded full IA source is preserved under `docs/assets/003_holy_realm/source_audio/unmatched_candidates/` with its own verified size and hashes, but four waveform comparisons at the stated `00:02:00-00:02:30` point produced a maximum absolute normalized correlation of `0.147552`; this source is not accepted for the current runtime. |

For ID 28, the actual runtime duration is 30.751927 seconds, while the central audio ledger records 30.071 seconds and the Commons excerpt metadata is 30.022676 seconds. This is an evidence discrepancy; I left the ledger row unchanged because source identity is not confirmed.

## Concrete next steps and limits

The first Commons original-file request returned HTTP 429 with a bot-traffic notice before any Commons file was saved; I did not retry or work around the limit. ID 9’s exact source can be restored from Commons revision `917959876` once original-file downloads are available, then compared to its WAV. For ID 28, the exact Commons excerpt revision `917959865` is the concrete licensed source candidate; recover that exact file first and verify its PCM against the runtime. The separate IA MP3 remains a mismatch candidate, not a replacement. If the Commons excerpt is no longer retrievable or does not match, parent acceptance is required before changing the audio source or runtime.

The Commons excerpt and source recording use CC BY-SA 3.0, so any accepted adapted cue must include attribution, a link to the license, a notice of changes, and distribution under the same or a compatible license. A possible parent-reviewed alternative would be to prepare a new cue from the licensed IA recording, but it would differ from the present runtime and would require explicit acceptance; no replacement was made.

The parent brief states that ID 9’s expected Final Silence playback path is Fallout-owned. This handoff makes no claim that its legacy sound definition is active. Final consumer verification and any wiring decision remain parent-owned.

The complete source-page, licensing, hash, duration, and comparison receipts are in `docs/assets/003_holy_realm/source_audio/source_manifest.md`.

## Files changed and force-add list

- `docs/assets/003_holy_realm/source_audio/unmatched_candidates/shurangama_chant_archive_candidate_unmatched.mp3`
- `docs/assets/003_holy_realm/source_audio/source_manifest.md`
- `docs/plans/003_holy_realm_plans/subagent_handoffs/audio_provenance_20261006.md`

No audio ledger rows were changed for Event 003 because provenance was not confirmed. No files were staged or committed.

