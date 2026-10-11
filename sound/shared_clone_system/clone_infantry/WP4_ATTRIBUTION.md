# Clone rifle recording attribution

`clone_infantry_rifle_01.wav` uses the recorded Lee-Enfield .303 report by kyles, https://freesound.org/people/kyles/sounds/450851/, CC0 1.0.
The archived original `lee_enfield_450851_hq.mp3` has SHA-256 `3df56b0fd86d87dc2203eea587b2108fa6d4df63ffcda9507a2d1ef68ffba256`.
Changes: a 0.45 second report cut after the 0.17 second source lead, 120 ms tail fade, DC removal, mastering and mono PCM16/44.1 kHz conversion.
Installed derivative SHA-256: `42f23c496111944c41489a0d295750808777a216f3aa9dc48ae1170962746bfd`.
The inherited simulated rifle cue is retained only as an archived preimage and is not the installed report.

Source identity, mastering measurements and installed-byte proofs are retained in `docs/plans/unit_fix_2026-10/wp4_audio_evidence/provenance_index.md`, `reports/clone_rifle_final_inspect.json`, and `install/accepted_tranche3.json`.
This rifle cue is consumed by attack, defend and support attack through the existing `clone_infantry_rifle_attack` wrapper and their measured muzzle events.

## Complete existing-source cue repairs

`clone_infantry_body_impact_01.wav` uses “BODY FALL - V HVY - DIRT” by leonelmail (CC0 1.0, https://freesound.org/people/leonelmail/sounds/504626/).
Verified immutable source SHA-256: `336a44d95279173764073a9b2d4d7e12f4167cfb0c1ad5c58e316895e129c6bb`.
Mechanical processing trims the recorded body/feet landing from 0.400 to 1.300 seconds, adds fades and masters the 0.900-second cue.
Its 1.500-second entity event follows the authored frame-37 marker in the exact selected/current death action SHA-256 `2f3f44819868da8c03585d23361ce478876c196082701bd28127bb3ede8b7057`; this is source timing acceptance, not new anatomical contact proof.
Installed derivative SHA-256: `e54259450101ad5ad71ab73fdd2e68f75c3f734a965996ede9477f37f07ce931`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`clone_infantry_attack_voice_01.wav` uses “Soldier Voice Acting: battlecries” by kurt (CC BY 3.0, https://opengameart.org/content/soldier-voice-acting).
Verified immutable source SHA-256: `26fbe5af927786b854389e5ba6d2e04d0283f95e47aa16214a1d82943ba9db74`.
Mechanical source trimming where applicable, entry/release fades, level mastering and mono PCM16 at 44.1 kHz preserve the declared sound identity.
Installed derivative SHA-256: `ae2abfa552bafd8737894f118bd9c6138ff0fcb01f08991acd845294ca5e1a82`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`clone_infantry_wounded_01.wav` uses “Soldier Voice Acting: wounded” by kurt (CC BY 3.0, https://opengameart.org/content/soldier-voice-acting).
Verified immutable source SHA-256: `eeb48bd1abee14052941df29fe93b660df4a811998146616f5d6eaa138484ee6`.
Mechanical processing preserves the captured vocal peak level while applying 10 ms entry and 20 ms release fades, original-source trimming and mono PCM16 at 44.1 kHz.
Installed derivative SHA-256: `d48417342af00dc5e5e94100658c5c011b83abf9011399b458116851513ef4ff`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

`clone_infantry_death_01.wav` uses “Grunts: male death and pain” by thebardofblasphemy (CC0 1.0, https://opengameart.org/content/grunts-male-death-and-pain).
Verified immutable source SHA-256: `3f00fba827f20ff9ccea1bc07d2c21ab8d3a36e81b48a6005cf8459f02779586`.
Mechanical processing preserves the captured vocal peak level while applying 10 ms entry and 20 ms release fades, original-source trimming and mono PCM16 at 44.1 kHz.
Installed derivative SHA-256: `79e6d5a4ea4fdb68cea6ce907071561860167ce955b85ac5a3359b5cfc64440d`.
Original sources, selected candidates, exact transformations and measured receipts are retained in `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/wp4_audio_takeover/receipt.json` while the model repair remains active.

No audio was downloaded, synthesized or recorded by the agent; no auditory, spoken-word or live playback acceptance is asserted.
CC BY 3.0 sources retain attribution and adaptation notices: https://creativecommons.org/licenses/by/3.0/.

## Distinct recorded voice takes

The attack pool retains its original take and adds one recorded battlecry; the wounded pool retains its original and adds two recorded wounded vocal events.
All three additions use Soldier Voice Acting by kurt, CC BY 3.0, https://opengameart.org/content/soldier-voice-acting, https://creativecommons.org/licenses/by/3.0/.

`clone_infantry_attack_voice_02.wav` uses `docs/assets/shared_clone_system/models_3d/clone_infantry/clone_preserved_acceptance_audio/battlecries.ogg`, source SHA-256 `26fbe5af927786b854389e5ba6d2e04d0283f95e47aa16214a1d82943ba9db74`, source window 0.934000000-1.234000000 seconds.
Mechanical processing applies 10 ms entry and 30 ms release fades, 30 Hz high-pass filtering, -1.626085434 dB gain and mono PCM16/44.1 kHz conversion.
Derivative SHA-256 `6f551f3e4e0df06558c8804751d6fdde869272e1257526134b6d194d54d4ecd3`; duration 0.300000 seconds, peak -2.999988 dBFS, leading silence 19.954649 ms.

`clone_infantry_wounded_02.wav` uses `docs/assets/shared_clone_system/models_3d/clone_infantry/clone_preserved_acceptance_audio/wounded.ogg`, source SHA-256 `eeb48bd1abee14052941df29fe93b660df4a811998146616f5d6eaa138484ee6`, source window 1.727000000-2.130000000 seconds.
Mechanical processing applies 10 ms entry and 20 ms release fades, 30 Hz high-pass filtering, 3.776421109 dB gain and mono PCM16/44.1 kHz conversion.
Derivative SHA-256 `673e86f516c4ae911d78ce6f48fca17c4a22e1e014ba86cd21da52e8451136cf`; duration 0.407370 seconds, peak -6.677271 dBFS, leading silence 19.954649 ms.

`clone_infantry_wounded_03.wav` uses `docs/assets/shared_clone_system/models_3d/clone_infantry/clone_preserved_acceptance_audio/wounded.ogg`, source SHA-256 `eeb48bd1abee14052941df29fe93b660df4a811998146616f5d6eaa138484ee6`, source window 3.333000000-4.109818594 seconds.
Mechanical processing applies 10 ms entry and 20 ms release fades, 30 Hz high-pass filtering, 4.616138215 dB gain and mono PCM16/44.1 kHz conversion.
Derivative SHA-256 `5971c359aa56b322fdacb60c515a1742c6ef74052a1010cf1f43d49478273c53`; duration 0.776825 seconds, peak -6.677271 dBFS, leading silence 14.965986 ms.

Wounded peaks retain the accepted -6.677271 dBFS level; the added battlecry peaks at -3 dBFS.
The rejected additional battlecry remains unused because preserving its early vocal onset did not meet the unchanged 20 ms leading-silence gate.
The selected attack pool has two takes and the wounded pool has three, both preventing immediate repetition.
Original takes, entity events, cue volumes and playback-rate ranges are unchanged.
Source/context waveforms, exact recipes and candidate checks are in the Clone job `evidence/wp4_audio_takeover/voice_variants/review_packet.json`; installed binding checks are in `integration_receipt.json` there.
No sound was downloaded, synthesized or recorded by the agent; no auditory, spoken-content or live playback acceptance is claimed.

`clone_infantry_death_02.wav` uses the distinct recorded death/pain event from the original CC0 source by thebardofblasphemy.
Source `docs/assets/shared_clone_system/models_3d/clone_infantry/audio/evidence/originals/death_pain_grunts.wav`, SHA-256 `3f00fba827f20ff9ccea1bc07d2c21ab8d3a36e81b48a6005cf8459f02779586`, source window 20.318004535-22.500000000s.
Processing preserves the complete documented envelope with 10 ms entry and 20 ms release fades, 30 Hz high-pass, level matched to -7.667008 dBFS, mono PCM16/44.1kHz.
Installed duration 2.181995s; lead 19.954649ms; candidate SHA-256 `0526962a0c247dd6a65a9a8792bfb161ccb35c1470e2a3179b19bbeed567ddf3`.

`clone_infantry_death_03.wav` uses the distinct recorded death/pain event from the original CC0 source by thebardofblasphemy.
Source `docs/assets/shared_clone_system/models_3d/clone_infantry/audio/evidence/originals/death_pain_grunts.wav`, SHA-256 `3f00fba827f20ff9ccea1bc07d2c21ab8d3a36e81b48a6005cf8459f02779586`, source window 23.844988662-25.950000000s.
Processing preserves the complete documented envelope with 10 ms entry and 20 ms release fades, 30 Hz high-pass, level matched to -7.667008 dBFS, mono PCM16/44.1kHz.
Installed duration 2.105011s; lead 14.965986ms; candidate SHA-256 `c3e02ca7220df6f99263ee7feaccfffdc2d79d2e23c512fd2650f57a866eaa74`.

The death cue has three distinct source-event choices from the existing CC0 voice recording, with the captured -7.667 dBFS role level, existing single one-shot death event and immediate-repetition prevention preserved.
The chosen excerpts are disjoint from the installed 0.506-1.893s event and from each other. An initially selected pair with 29.932ms leading silence remains rejected evidence; the retained pair passes the unchanged 20ms gate.
Exact source windows, recipes, levels and waveform/context evidence are in the Clone job `evidence/wp4_audio_takeover/death_variants/`.
No audio was downloaded, synthesized or recorded; no auditory, spoken-content or live playback acceptance is claimed.
