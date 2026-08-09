# Pan Sappers audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `vervet_monkey.ogg` | `94673ca955cb54e81ac0c7ad0fa38ad5d95af4f871cb87799d6133aeb63c5e2d` | British Library; recordist Roland McVicker | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:Vervet_Monkey_(Chlorocebus_pygerythrus)_(W_CERCOPITHECUS_AETHIOPS_R2_C2).ogg |
| `metal_clanging.ogg` | `b3f1a16f5dda28d20c8b16689050647478812d92ee3c06a66ec4a425a85bb408` | Camshaft64 | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_pan_sappers_select.wav` | `vervet_monkey.ogg` 1.0–2.5 s | `selection/acknowledgement` | one-shot | `ff66173a723b36b8e6e80550c040f4841bef491d8e49662c597485f0ccac1a19` |
| `chaosx_pan_sappers_idle.wav` | `vervet_monkey.ogg` 8.0–10.0 s | `chaosx_pan_idle` | frame 1 entry accent; 1–61 action | `78deabbc26b553fcc9b5d15ec0a61427908bafd3a5bed9c02edd3b831cbfd697` |
| `chaosx_pan_sappers_move.wav` | `metal_clanging.ogg` 0.3–1.5 s | `chaosx_pan_move` | frame 16; 1–31 loop | `4a4f7fe38ef2bf21d1aa480bc7a5682834b780054b42c5acb9be50c940148e8d` |
| `chaosx_pan_sappers_sabotage.wav` | `metal_clanging.ogg` 4.0–5.4 s | `chaosx_pan_sabotage` | frame 21; 1–41 action | `fa3dbe874bbccf33999071d479697eab4ceb8997562af230a8633f750c5cec2b` |
| `chaosx_pan_sappers_construction.wav` | `metal_clanging.ogg` 8.0–9.5 s | `chaosx_pan_construction` | frame 24; 1–46 action | `f44a0121d14af7a6ef28cc3caa538fd12c93e3518ea699ad3c78e35671c53b8a` |
| `chaosx_pan_sappers_death.wav` | `vervet_monkey.ogg` 28.0–30.2 s | `chaosx_pan_death` | frame 24; 1–46 action | `511cbb615ccb75c0180b4d9f859f6c157748bd5f3e83b767b9ff2dade9e04ad2` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

