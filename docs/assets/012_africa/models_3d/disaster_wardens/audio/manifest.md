# Disaster Wardens audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `rain_thunder.ogg` | `cbfd7b7504bc4e53d6e56ac8d933ba56f97cc28f15a46800c74c2d8eccb3fa89` | Caesar | Public domain | https://commons.wikimedia.org/wiki/File:Rain_and_thunder.ogg |
| `signal_bell.ogg` | `bc2247f3ac132b631d821b03c94bbbce436d9090369b06276577404bbfc16f92` | Work With Sounds; Konrad Gutkowski / Julian Blaschke | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:WWS_Signalbell.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_disaster_wardens_select.wav` | `signal_bell.ogg` 0.2–2.0 s | `selection/acknowledgement` | one-shot | `0098173064ed59b18474f93993aa44e662a996e172fbfaae2fc0d92857601c8c` |
| `chaosx_disaster_wardens_idle.wav` | `rain_thunder.ogg` 1.0–3.5 s | `chaosx_disaster_warden_idle` | frame 1 entry accent; 1–61 action | `e365f91a3ea5c02194ed72194ef14398f5b7d3803319c39384991eed64c62e58` |
| `chaosx_disaster_wardens_move.wav` | `signal_bell.ogg` 3.0–4.5 s | `chaosx_disaster_warden_move` | frame 16; 1–31 loop | `faec254dd67c679edc41b6a21877a655080d779a0d90794bf8f2950aca3a3b6e` |
| `chaosx_disaster_wardens_rescue.wav` | `signal_bell.ogg` 7.0–8.8 s | `chaosx_disaster_warden_rescue` | frame 16; 1–31 action | `4c407ad9e8f5abf9d3a6754e6633568acf18c5a36b6e168b1e21768a12a16595` |
| `chaosx_disaster_wardens_containment.wav` | `rain_thunder.ogg` 8.0–10.0 s | `chaosx_disaster_warden_containment` | frame 24; 1–46 action | `fadcbdaeaeefc8dcc27690bcaefe046317435cccd91e7a69c40d2d5d4fac8084` |
| `chaosx_disaster_wardens_death.wav` | `rain_thunder.ogg` 14.0–16.2 s | `chaosx_disaster_warden_death` | frame 24; 1–46 action | `cb77ea77f081022c39205826966d3e0008f38f685c2d2aff0942bd14cd904d23` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

