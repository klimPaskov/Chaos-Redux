# Plague Carriers audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `cough_1.ogg` | `74d085545dceef494e95174d07391d102bf7fbcd0d544174e5256f5ddefa8db8` | ezwa / PDSounds | Public domain | https://commons.wikimedia.org/wiki/File:Cough_1.ogg |
| `air_duster.ogg` | `4b6192076f0e06171c405e97b875a69839c8c60bbe04f23a063b4739dc6b5a1a` | stephan / PDSounds | Public domain | https://commons.wikimedia.org/wiki/File:Air_duster.ogg |
| `metal_clanging.ogg` | `b3f1a16f5dda28d20c8b16689050647478812d92ee3c06a66ec4a425a85bb408` | Camshaft64 | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_plague_carriers_select.wav` | `cough_1.ogg` 0.5–2.1 s | `selection/acknowledgement` | one-shot | `6c621c6928de75ed2f10264a73d49c61e5e0b6801935c296940aef5a7cd53927` |
| `chaosx_plague_carriers_idle.wav` | `cough_1.ogg` 5.0–7.2 s | `chaosx_plague_carrier_idle` | frame 1 entry accent; 1–61 action | `7cb97581c44047e47db6e3b4ed40854f9e5e2c48e515b6f1a40eab5abfc70ddd` |
| `chaosx_plague_carriers_move.wav` | `air_duster.ogg` 1.0–2.6 s | `chaosx_plague_carrier_move` | frame 16; 1–31 loop | `7986cdefac49c503aeedc2f10a15188789188ff4e74185ddf8c85e1fc9da327a` |
| `chaosx_plague_carriers_deploy.wav` | `air_duster.ogg` 7.0–9.0 s | `chaosx_plague_carrier_deploy` | frame 24; 1–46 action | `9b7a2d81c74f0900a6a462b2eea4ce653b8e1aa755d4a951eb235d338516500e` |
| `chaosx_plague_carriers_release_containment.wav` | `air_duster.ogg` 14.0–16.2 s | `chaosx_plague_carrier_release_containment` | frame 24; 1–46 action | `0a8679cb4dbd446333567c54c70606d4b2de601272cd8ef7f5f3b47468e76d81` |
| `chaosx_plague_carriers_impact.wav` | `metal_clanging.ogg` 4.0–5.4 s | `chaosx_plague_carrier_release_containment` | frame 16 impact phase | `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` |
| `chaosx_plague_carriers_death.wav` | `cough_1.ogg` 15.0–17.2 s | `chaosx_plague_carrier_death` | frame 24; 1–46 action | `f497fd39b3f34a6ad07b576a9f6e47351cd2cb42140f6af6ed68a11041f3a690` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

