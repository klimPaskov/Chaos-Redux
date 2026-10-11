# Alien Infantry audio attribution

The complete existing-source cue repairs below identify the current installed derivatives.
The following laser-tail record is historical and is superseded by the layered laser entry.

## Superseded laser-tail derivative

`alien_infantry_laser_fire.wav` retains the existing “Space Laser” identity by bart, CC0 1.0, https://opengameart.org/content/space-laser.
The unchanged original archive is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/space_laser.wav`, SHA-256 `3a26ecab8f36dca14a91519657e60351566a268d28a2ec4f933b0f9718a7258d`.
The existing source-bound 1.200-second derivative has SHA-256 `f91951502a2693d3806ef2fa5b20bb5fc54d5d552c3b2ea8fbe37b82637f110d` and is preserved in the takeover preimage evidence.
Mechanical processing keeps the onset and first 0.900 seconds, applies a 60 ms tail fade, then uses the shared shot mastering route for mono PCM16 at 44.1 kHz.
Historical derivative SHA-256: `5146acdd307b095484994514703d568041b2c06d2bd515b56dbd87ec9213ed76`.
No new tone, recording, layer, synthesis, or download was introduced.
The source production method remains undocumented; this repair makes no claim that the source is a recording or that the broad noise burst became a tonal zap.
Parent acceptance covers source, format, and nonoverlapping timing only.

## Complete existing-source cue repairs

`alien_infantry_move.wav` uses “Footsteps: 01” by GboxMikeFozzy (CC0 1.0, https://opengameart.org/content/footsteps-0).
Verified immutable source SHA-256: `33c9bef5e8aeb1069455699a34a0c5e1ef1787fd3f61594b0859d7e6bb9f9dec`.
Mechanical source trimming where applicable, entry/release fades, level mastering and mono PCM16 at 44.1 kHz preserve the declared sound identity.
Installed derivative SHA-256: `00b592be8b23ce43f50491474610d8c983e94d8bec1ac11ae1d221f9bd1c2b20`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`alien_infantry_laser_fire.wav` uses “Space Laser” by bart (CC0 1.0, https://opengameart.org/content/space-laser) + “Sci-Fi Sounds: laserSmall_000” by Kenney (CC0 1.0, https://kenney.nl/assets/sci-fi-sounds).
Verified immutable source SHA-256: `3a26ecab8f36dca14a91519657e60351566a268d28a2ec4f933b0f9718a7258d`, `72b589eadd41781257ac859e4f4d030222e623390e4a1a83f6d05329a6e026f1`.
The existing 0.900-second Space Laser derivative is mixed with the exact archived Kenney laserSmall_000 member, with source-only fades/gain and mastering; no new tone or noise is generated.
Installed derivative SHA-256: `83395802e3c1c9ce118e3719493216d1bf568d9ce89580968a1567687fe33b9a`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`alien_infantry_impact.wav` uses “Sci-Fi Sounds: impactMetal_000” by Kenney (CC0 1.0, https://kenney.nl/assets/sci-fi-sounds).
Verified immutable source SHA-256: `956c6612a256aa1a67a2327fffe2454f6b1d82e4c1c2be28fd66916335d5b1d6`.
Mechanical source trimming where applicable, entry/release fades, level mastering and mono PCM16 at 44.1 kHz preserve the declared sound identity.
Installed derivative SHA-256: `0bae4e766a4c6b729d7e9462e6d101180a6c7fdfb314eeb3621f01b62d10be99`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

Portal Raider step 01 and Alien Infantry movement intentionally share the same archived GboxMikeFozzy boot-footfall member and derivative pool (SHA-256 `00b592be8b23ce43f50491474610d8c983e94d8bec1ac11ae1d221f9bd1c2b20`); they are not separate recorded takes.
Alien Infantry's movement pool also references the existing `portal_raider_step_02` through `_06` sound sources without copying or modifying their WAVs.
Together these form one declared six-take CC0 boot-footfall family with immediate repetition prevented.
Their per-file source and derivative hashes, transformations and license are retained in [Portal Raider attribution](../../portal_raider/WP4_ATTRIBUTION.md).
At the minimum configured playback rate of 0.94, the longest take lasts 0.354273 seconds, below the 0.533333-second minimum movement interval and 0.6-second retreat interval, including loop boundaries.
No audio was downloaded, synthesized or recorded by the agent; no auditory, spoken-word or live playback acceptance is asserted.

## Distinct licensed laser library variants

Both variants layer Kenney's “Sci-Fi Sounds” members (CC0 1.0, https://kenney.nl/assets/sci-fi-sounds) over the accepted 0.900-second “Space Laser” core by bart (CC0 1.0, https://opengameart.org/content/space-laser).
The immutable Kenney members are archived in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0/Audio/`.
The immutable bart original is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/space_laser.wav`, SHA-256 `3a26ecab8f36dca14a91519657e60351566a268d28a2ec4f933b0f9718a7258d`; the accepted core has SHA-256 `5146acdd307b095484994514703d568041b2c06d2bd515b56dbd87ec9213ed76`.

`alien_infantry_laser_fire_02.wav` uses `laserSmall_001.ogg`, source SHA-256 `ab87913aba9790a0c5fa173d086267ba521ad522fcad2252271db49988313cf5`, retaining its 0.244444444-second decoded duration.
Installed derivative SHA-256: `94ad23258f3686a4e4470dfda8240e959b73fb7dfd948a391ec56e9f4eaa10c1`.
Its bounded mastering recovery applies at most 1.500001 dB of gain reduction; exact commands remain in the shot master report.

`alien_infantry_laser_fire_03.wav` uses `laserSmall_002.ogg`, source SHA-256 `e70139466c3e801358c9041ee17db7ff82c0e9a9cdf44647ad0ea6b9f8458f63`, retaining its 0.344263039-second decoded duration.
Installed derivative SHA-256: `3cc9e350bc51e255fd10a370b3d96f182f0b7421be5c4c44ed007b0ac3f7211d`.

Each library member has 5 ms entry and 40 ms release fades and is mixed at -3 dB over the core at -9 dB.
Shared mastering uses a 30 Hz high-pass filter, 8 ms entry and 50 ms terminal fades, a -3 dBFS peak and the unchanged level, spectral and clipping gates; output is mono PCM16 at 44.1 kHz.
Both 0.900-second clips last 0.927835052 seconds at the configured minimum rate of 0.97, below the 1.066666-second support-event spacing.

These are distinct licensed library members sharing one bart core, not separate acoustic recordings or new synthesized sounds.
Exact source/member/core hashes, recipe, decoded waveform and unchanged gates are retained in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/wp4_audio_takeover/library_variants/review_packet.json`, `shot_master_report.json` and `laser_install/integration_receipt.json`.
The original laser take, six-take shared movement family, all entity timings and existing sound properties remain unchanged; immediate repetition is prevented.
No auditory or live playback acceptance is claimed.

## Distinct licensed impact library variants

Both variants use Kenney’s “Sci-Fi Sounds” impact members (CC0 1.0, https://kenney.nl/assets/sci-fi-sounds), preserved in the existing archived library.

`alien_infantry_impact_02.wav` uses `Audio/impactMetal_003.ogg`, source SHA-256 `ef29c3943ee701616f65e3d596c13eb3ff6b11ca5b3ac01e7bc923366a5c6f76`.
The immutable source is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0/Audio/impactMetal_003.ogg`; its complete 0.776780045-second decoded duration is retained.
Mechanical processing applies 5 ms entry and 40 ms release fades, the same 30 Hz high-pass filter and -1.228436674 dB peak-normalization gain to reach -6 dBFS, then delivers mono PCM16 at 44.1 kHz.
Installed derivative SHA-256: `55f7c8e7fb2c62f5e3a6dd8bca1e5ef77a559ebea4d8962250ae7bcaa83a9925`.
At the configured minimum playback rate of 0.96, its duration is 0.809145881 seconds.

`alien_infantry_impact_03.wav` uses `Audio/impactMetal_004.ogg`, source SHA-256 `0032710d1fc88c217946cd54492f275eb4363bb8025a4bc1b7ce08df7b3c60de`.
The immutable source is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0/Audio/impactMetal_004.ogg`; its complete 0.389523810-second decoded duration is retained.
Mechanical processing applies 5 ms entry and 40 ms release fades, the same 30 Hz high-pass filter and 0.352408939 dB peak-normalization gain to reach -6 dBFS, then delivers mono PCM16 at 44.1 kHz.
Installed derivative SHA-256: `3cf35f3da295051f4945164a3530171e1a4d0039ca03d93307b210469dd1746b`.
At the configured minimum playback rate of 0.96, its duration is 0.405753968 seconds.

The source-frequency gate passes without a subsonic exception or stronger filtering; the two earlier low-frequency members remain rejected evidence.
The impact remains one event at 1.4 seconds in the nonlooping death state.
The installed death animation `gfx/models/units/alien_infantry/alien_infantry_death.anim` has SHA-256 `d836be94902af5608b3fcc98be8005b5a8eada59e947b58930f43d8d66a2d7eb` and the parent-verified 61 samples at 30 FPS span 2.0 seconds.
The longest impact at the minimum rate of 0.96 ends at 2.209145881 seconds after state start, retaining a one-shot tail 0.209145881 seconds beyond the final pose.
This is source timing arithmetic, not repeated-cue overlap or observed state-exit playback; no full decay was trimmed to fit the pose duration.
These are distinct licensed library members, not a claim of separate acoustic recordings.
Exact member/source/candidate hashes, recipes, decoded waveform comparisons and unchanged checks are retained in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/wp4_audio_takeover/library_variants/review_packet.json`, `impact_member003_004_numeric.json` and `impact_install/integration_receipt.json`.
The original impact, accepted laser pool, six-step movement pool, all entity events, playback rates, volumes, categories and repetition flags remain intact.
No audio was downloaded, synthesized or newly recorded; no auditory or live playback acceptance is claimed.
