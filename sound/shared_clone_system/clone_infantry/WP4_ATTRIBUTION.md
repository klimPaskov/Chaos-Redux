# Clone rifle recording attribution

`clone_infantry_rifle_01.wav` uses the recorded Lee-Enfield .303 report by kyles, https://freesound.org/people/kyles/sounds/450851/, CC0 1.0.
The archived original `lee_enfield_450851_hq.mp3` has SHA-256 `3df56b0fd86d87dc2203eea587b2108fa6d4df63ffcda9507a2d1ef68ffba256`.
Changes: a 0.45 second report cut after the 0.17 second source lead, 120 ms tail fade, DC removal, mastering and mono PCM16/44.1 kHz conversion.
Installed derivative SHA-256: `42f23c496111944c41489a0d295750808777a216f3aa9dc48ae1170962746bfd`.
The inherited simulated rifle cue is retained only as an archived preimage and is not the installed report.

Source identity, mastering measurements and installed-byte proofs are retained in `docs/plans/unit_fix_2026-10/wp4_audio_evidence/provenance_index.md`, `reports/clone_rifle_final_inspect.json`, and `install/accepted_tranche3.json`.
This rifle cue is consumed by attack, defend and support attack through the existing `clone_infantry_rifle_attack` wrapper and their measured muzzle events.
