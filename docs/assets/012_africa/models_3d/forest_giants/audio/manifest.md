# Forest Giants audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `forest_ambience.ogg` | `43848c3eda5f42829f1033112c2a91ba3e5c91b79a0532fda264c9f59856d431` | nille / PDSounds | Public domain | https://commons.wikimedia.org/wiki/File:20090610_0_ambience.ogg |
| `quern_stones.ogg` | `2b281cec5a193a20e7c969d7cd79b990cd920822a2685087cd2ce18bf20557d7` | Work With Sounds; recordist Monika Widzicka | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_forest_giants_select.wav` | `forest_ambience.ogg` 5.0–6.8 s | `selection/acknowledgement` | one-shot | `daa9f35516e12068535e5cee18233c62b1ca7d7e307402ef27ab7a504cefc1a0` |
| `chaosx_forest_giants_idle.wav` | `forest_ambience.ogg` 20.0–22.5 s | `chaosx_forest_giant_idle` | frame 1 entry accent; 1–61 action | `3675dea66dbaf458450282d317e9213d1b15bc92c341d550ce83bc6fc0d6db0b` |
| `chaosx_forest_giants_move.wav` | `quern_stones.ogg` 10.0–11.6 s | `chaosx_forest_giant_move` | frame 16; 1–31 loop | `aa4d8efa831bc61316ac327fa13b1fdb23a1da7883fad60dc962fa65101ed2d0` |
| `chaosx_forest_giants_attack.wav` | `quern_stones.ogg` 30.0–31.5 s | `chaosx_forest_giant_attack` | frame 21; 1–41 action | `c1bf32450c72f8dc2b51688b1ae63bfd6e949f476e0f8ec6dc33e4e994906836` |
| `chaosx_forest_giants_concealment_emergence.wav` | `forest_ambience.ogg` 60.0–62.0 s | `chaosx_forest_giant_concealment_emergence` | frame 24; 1–46 action | `07a65609e710d7fc55749959b777e2838a5d1131099cf65810acf45beb138c1b` |
| `chaosx_forest_giants_death.wav` | `quern_stones.ogg` 45.0–47.2 s | `chaosx_forest_giant_death` | frame 24; 1–46 action | `7ffbe2820f00621a1db3743edc6518b7f71f65da8b2e19906ea5e7f504c1d842` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

