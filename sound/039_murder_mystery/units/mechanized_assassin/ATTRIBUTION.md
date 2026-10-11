# Mechanized Assassin destruction sound

`destroyed.wav` derives from “Mechanical Explosion” by Spring Spring, [OpenGameArt source](https://opengameart.org/content/mechanical-explosion), CC0 1.0.
The original archive is `docs/assets/039_murder_mystery/audio/source/mechanical_explosion.wav`, SHA-256 `13e9f713bd0d5921b223b01d29d68bb7625a1a1fbf1894af35ebfd5ef72c8632`.
Mechanical processing preserves the complete 1.360-second source decay with pre-attenuation, mastering, fades, and mono PCM16 at 44.1 kHz.
The selected installation receipt is `docs/plans/unit_fix_2026-10/wp4_audio_evidence/install/accepted_tranche4.json`, with runtime SHA-256 `667c84dea448d1009ea2b4f243251c5cdabc2626fec717e37c7fa7996c240317`.
No additional audio was generated or downloaded.

The MG soundeffects reference installed vanilla `mechanized_units_mg_fire_01` through `_05`, with `_02` through `_05` used for defend.
Those engine-owned files are referenced in place and are not redistributed by this package.

`destroyed_02.wav` derives from Kenney Sci-Fi Sounds `explosionCrunch_000` (CC0 1.0, https://kenney.nl/assets/sci-fi-sounds).
Archived source `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0/Audio/explosionCrunch_000.ogg`, SHA-256 `4b597d658d0ae101f0a030fbeea5fc3a4292ab85f017470a8254a8e7959cbd69`, decoded duration 0.777460s.
Mechanical processing uses a 30 Hz high-pass, 8 ms entry and 50 ms release fades, and -0.931701 dB gain to the -3 dBFS one-shot target; delivery is PCM16 mono at 44.1 kHz.
Installed duration 0.777460s; peak -2.999988 dBFS; RMS -16.478367 dBFS; derivative SHA-256 `ab3f2ac92bdbb0c6a58f2d2e87be311291f8d620b80370f7b4629dca23df315b`.

`destroyed_03.wav` derives from Kenney Sci-Fi Sounds `explosionCrunch_001` (CC0 1.0, https://kenney.nl/assets/sci-fi-sounds).
Archived source `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0/Audio/explosionCrunch_001.ogg`, SHA-256 `fdd04d6f0032d4d57c134ad37f3587d2d00e58c9572715275bd8cf4f43593576`, decoded duration 1.356780s.
Mechanical processing uses a 30 Hz high-pass, 8 ms entry and 50 ms release fades, and -2.043747 dB gain to the -3 dBFS one-shot target; delivery is PCM16 mono at 44.1 kHz.
Installed duration 1.356780s; peak -2.999988 dBFS; RMS -15.925567 dBFS; derivative SHA-256 `e5a36319a972e44be951e96a6b69c87e60ee150693308388b2915bf44924cdd8`.

The existing 1.360-second `destroyed.wav` remains in the selection.
All three source-distinct licensed library choices form one destruction pool with immediate repetition prevented; the two Kenney members are library-designed effects, not a claim of separate acoustic recordings.
The entity still fires `chaosx_mechanized_assassin_destroyed` once at 0.1 seconds; soundeffect volume, concurrency limit, and nonlooping behavior remain unchanged.
No sound was downloaded, generated, or newly recorded. No auditory or live playback acceptance is claimed.
Exact sources, allowlist, mastering report, source checks and installed hashes are in the owning model job `evidence/wp4_audio_takeover/destruction_variants/`.
Kenney distributed these as designed sound-effect library members; their original production method is undocumented, so these are distinct licensed library choices rather than a claim of separate acoustic recordings.
