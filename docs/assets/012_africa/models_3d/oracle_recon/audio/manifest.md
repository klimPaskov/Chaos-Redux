# Oracle Recon audio manifest

Package date: 2026-08-06.

All originals are preserved under `audio/source/`. Detailed source-page and direct-download evidence is in `audio/evidence/source_research.md`.

## Source ledger

| Original | SHA-256 | Creator / attribution | License | Source page |
|---|---|---|---|---|
| `signal_horn.ogg` | `126e34bacc49fd7b12b3c54fafe0db8d4a1b85c74f836858168c085ac2405a79` | Work With Sounds; Konrad Gutkowski / Jonathan Nicolai | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:WWS_Signalhorn.ogg |
| `gong_short.ogg` | `f57283d08a0ecb052425af1ac1457f827fa27f423d49158963b3370c89fc942d` | Ocaasi / PDSounds | CC0 1.0 | https://commons.wikimedia.org/wiki/File:Gong_or_bell_vibrant_(short).ogg |

## Derived ledger

Every WAV is mono 44,100 Hz PCM 32-bit float. Each derivative was mechanically trimmed from the stated source interval, normalized with FFmpeg `loudnorm=I=-20:TP=-2:LRA=7`, given a 0.03-second entry fade and 0.10-second exit fade, resampled, and channel-converted. No synthesis, generation, pitch alteration, layering, or invented audio was used.

| Role / file | Source excerpt | Semantic consumer | Synchronization | SHA-256 |
|---|---|---|---|---|
| `chaosx_oracle_recon_select.wav` | `signal_horn.ogg` 0.2–2.0 s | `selection/acknowledgement` | one-shot | `c72d9378d85733091fb48478e99b68fbb7cf1cb2b064f1e6749e6bdcab41d229` |
| `chaosx_oracle_recon_idle.wav` | `gong_short.ogg` 0.2–2.4 s | `chaosx_oracle_idle` | frame 1 entry accent; 1–61 action | `3146df216da596c84fc09781f6e2153e0b83f04a7c2d5df532776ca1d3b82cfe` |
| `chaosx_oracle_recon_move.wav` | `signal_horn.ogg` 3.0–4.5 s | `chaosx_oracle_move` | frame 16; 1–31 loop | `4303c5996978f64bee3f1c8c281756308a61a0f8c21632ffb970d22fc9ba7e04` |
| `chaosx_oracle_recon_recon.wav` | `signal_horn.ogg` 6.0–7.8 s | `chaosx_oracle_recon` | frame 21; 1–41 action | `c236fff9d51ade19f6918604344a96cd0dca2d8ba08c9a1e13138b78d0df01af` |
| `chaosx_oracle_recon_observation.wav` | `gong_short.ogg` 2.5–4.3 s | `chaosx_oracle_observation` | frame 24; 1–46 action | `73e91a619f21b9e7449705a504410b6b4f6c58625c6a8538e2a7848c710737e8` |
| `chaosx_oracle_recon_death.wav` | `gong_short.ogg` 3.2–5.4 s | `chaosx_oracle_death` | frame 24; 1–46 action | `184cb87973ec4933bdb6e4341b13a4f9823c8193c8a08bb32a904692537e2256` |

The source-to-runtime hashes above were recomputed after all source copies and conversions; every selected source copy matches its recorded source hash and every derived file matches its final recorded hash.

