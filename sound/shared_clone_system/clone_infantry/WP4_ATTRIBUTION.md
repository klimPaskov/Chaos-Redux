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
