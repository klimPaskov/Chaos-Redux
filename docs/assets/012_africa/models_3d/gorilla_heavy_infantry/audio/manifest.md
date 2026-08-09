# Gorilla Heavy Infantry audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `pant_hoot.ogg` | `14bb11683f3180dafcda15c8b1e73af5e6e6f2b54578e9a01f9edfa236fa07b5` | Pawel Fedurek et al. | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:Pant-hoot_call_made_by_a_male_chimpanzee.ogg |
| `metal_clanging.ogg` | `b3f1a16f5dda28d20c8b16689050647478812d92ee3c06a66ec4a425a85bb408` | Camshaft64 | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_gorilla_heavy_infantry_select.wav` | `pant_hoot.ogg` 0.2–2.0 s | `selection/acknowledgement` | one-shot | `856487537e180a54ca56edc01a39b7e00fa90bbdee5cc3624cbb8ef31c513e59` |
| `chaosx_gorilla_heavy_infantry_idle.wav` | `pant_hoot.ogg` 3.0–5.0 s | `chaosx_gorilla_idle` | frame 1 entry accent; 1–61 action | `f9aa4e4680fe4e2329529a769f04565a0a7565ed33d5fb12a54fe9936fadd0a8` |
| `chaosx_gorilla_heavy_infantry_move.wav` | `metal_clanging.ogg` 0.3–1.5 s | `chaosx_gorilla_move` | frame 16; 1–31 loop | `4a4f7fe38ef2bf21d1aa480bc7a5682834b780054b42c5acb9be50c940148e8d` |
| `chaosx_gorilla_heavy_infantry_attack.wav` | `metal_clanging.ogg` 4.0–5.4 s | `chaosx_gorilla_attack` | frame 21; 1–41 action | `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` |
| `chaosx_gorilla_heavy_infantry_recovery.wav` | `metal_clanging.ogg` 8.0–9.5 s | `chaosx_gorilla_recovery` | frame 16; 1–31 action | `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a` |
| `chaosx_gorilla_heavy_infantry_death.wav` | `pant_hoot.ogg` 9.0–11.2 s | `chaosx_gorilla_death` | frame 24; 1–46 action | `597a20c7d4f676cd788931eb5ec2d0ea70956895cd8af6bb448395c764da5c98` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

