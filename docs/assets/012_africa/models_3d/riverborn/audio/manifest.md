# Riverborn audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `flowing_water.ogg` | `6cab6c85a0b9159aa9e98f30bef16e5f8976a3154d8cec4e00925aac21289f0b` | Fg2 | Public domain | https://commons.wikimedia.org/wiki/File:Flowing-water-100019.ogg |
| `ducks_landing_water.ogg` | `c95c1641721cb80645d58fb05ceed871dcb74d1a62ad14e5d26f3b73f7bfa816` | U.S. Fish and Wildlife Service | Public domain U.S. federal work | https://commons.wikimedia.org/wiki/File:Ducks_landing_in_water.ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_riverborn_select.wav` | `flowing_water.ogg` 0.5–2.3 s | `selection/acknowledgement` | one-shot | `5e923a7c38e2dee453f1f174301109e70d65d17df23f48b0fed63b295ee42b6a` |
| `chaosx_riverborn_idle.wav` | `flowing_water.ogg` 4.0–6.5 s | `chaosx_riverborn_idle` | frame 1 entry accent; 1–61 action | `8ecdf4c1e95588304f4070ae07c5f8481a95c75891f6f199cd1ecf0b2a9d2474` |
| `chaosx_riverborn_move.wav` | `flowing_water.ogg` 8.0–9.6 s | `chaosx_riverborn_move` | frame 16; 1–31 loop | `146de88d1393c83c9b92b9de29ad29c2e4e8f23613c3e4eed778211b25fec75f` |
| `chaosx_riverborn_attack.wav` | `ducks_landing_water.ogg` 0.5–2.0 s | `chaosx_riverborn_attack` | frame 21; 1–41 action | `26ffe43934ac355da6df6887968b061ad54bef41a80bbe7d2bc69f506351d994` |
| `chaosx_riverborn_water_transition.wav` | `ducks_landing_water.ogg` 3.0–5.0 s | `chaosx_riverborn_water_transition` | frame 24; 1–46 action | `739e9720bc812c573aed579f7db5687b9d92496175cbfe67e70b64a7274878fa` |
| `chaosx_riverborn_death.wav` | `ducks_landing_water.ogg` 6.5–8.7 s | `chaosx_riverborn_death` | frame 24; 1–46 action | `ebc3839c560129e25fd2bfe8a763ed5bf0e4a2de53ecd4a09ec10b4230b6af33` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

