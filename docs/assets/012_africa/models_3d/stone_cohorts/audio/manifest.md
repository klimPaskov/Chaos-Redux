# Stone Cohorts audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `quern_stones.ogg` | `2b281cec5a193a20e7c969d7cd79b990cd920822a2685087cd2ce18bf20557d7` | Work With Sounds; recordist Monika Widzicka | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:WWS_Quern-stones.ogg |
| `metal_clanging.ogg` | `b3f1a16f5dda28d20c8b16689050647478812d92ee3c06a66ec4a425a85bb408` | Camshaft64 | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_stone_cohorts_select.wav` | `quern_stones.ogg` 1.0–2.4 s | `selection/acknowledgement` | one-shot | `9e57db53e3f6b73f099d72c54f2d461207765941ccfc76b840d85668023251eb` |
| `chaosx_stone_cohorts_idle.wav` | `quern_stones.ogg` 10.0–12.2 s | `chaosx_stone_idle` | frame 1 entry accent; 1–61 action | `729f14dede6b178678544bbd880a5c71498393f034c1c6684ef3c778cb5d4e49` |
| `chaosx_stone_cohorts_move.wav` | `quern_stones.ogg` 20.0–21.6 s | `chaosx_stone_move` | frame 16; 1–31 loop | `9ecc737021ea144c452786879909f98ab422d62d6312468a8c8ab7401b810743` |
| `chaosx_stone_cohorts_attack.wav` | `metal_clanging.ogg` 4.0–5.4 s | `chaosx_stone_attack` | frame 21; 1–41 action | `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` |
| `chaosx_stone_cohorts_collapse_recovery.wav` | `metal_clanging.ogg` 8.0–9.5 s | `chaosx_stone_collapse_recovery` | frame 16; 1–31 action | `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a` |
| `chaosx_stone_cohorts_death.wav` | `quern_stones.ogg` 45.0–47.2 s | `chaosx_stone_death` | frame 24; 1–46 action | `7ffbe2820f00621a1db3743edc6518b7f71f65da8b2e19906ea5e7f504c1d842` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

