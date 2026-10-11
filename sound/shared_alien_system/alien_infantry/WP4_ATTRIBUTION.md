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
