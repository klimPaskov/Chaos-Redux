# Base zombie audio source and design evidence, 2026-09-19

## Current base-zombie sound state, 2026-09-20

Status: **installed with offline frame synchronization; sonic listening and live HOI4 playback remain unverified**. The current base entity uses 33 declared signed-16 PCM, 44.1 kHz mono runtime WAVs, including nine base-only levelled derivatives documented with source and output hashes in `base_zombie_mix_20260920.json`. Its exported skeletal actions and the exact state event times were audited against 24 fps action lengths in `../../validation/exact_selected_runtime_audit_20260920.json`. No audio was synthesized or recorded; the nine new files are bounded-gain mixes of the preserved CC0 sources. No agent playback claim is made.

| State | Current sound event times in seconds | Reviewed visible phase |
| --- | --- | --- |
| Idle | One ambient groan on entry; tag-scoped `ZZZ_infantry_idle` selects a levelled groan | Low, uneven stance and breathing loop |
| Move | Steps at 0.08 and 1.05 | First and opposite-foot contacts in the 2.0 s stride |
| Retreat | Steps at 0.08 and 0.88 | Two contacts in the 1.67 s retreat loop |
| Attack | Vocal at 1.65; flesh contact at 3.60 | Wind-up and forward hand strike in the 4.79 s action |
| Defend | Hurt at 0.65; contact at 1.10 | Guard rises during a short recoil step |
| Support attack | Vocal at 0.95; contact at 2.45 | Reach, lunge, and recovery in the 3.5 s action |
| Training | Vocal at 0.95; one-shot action returns to idle | Practice lunge and return |
| Death | Vocal at 0.50; body impact at 2.55 | Collapse onto the floor before settled pose |

The `ZZZ_infantry_idle` selection route is tag scoped, matching the inspected vanilla country/class voice pattern. No verified subunit-specific selection selector has been found; one is not claimed. Sonic suitability, the mix in the actual game, and live cue timing remain for the user's live session. The five older shared attack/death files with incomplete source crosswalks belong to specialized zombie-family wrappers and are not consumed by this base entity. The source research and earlier timing table below are historical evidence from the preceding package.

For the nine later mechanically converted vocal, impact, and hurt files, `runtime_derivations_20260919.json` records each extracted source path and SHA-256, conversion command, runtime path and SHA-256, and format probe; all nine installed files matched the recorded runtime hashes on 2026-09-19. The other fifteen files were the earlier shared zombie package before the nine base-only mixes. The three earlier idle/selection files, six movement files, and `zombie_attack_01.wav` have exact source-to-runtime crosswalks; the remaining five older attack/death files still need an equally durable per-file source-to-runtime crosswalk before their provenance can be treated as independently verified.

## Source pages and immutable downloads

The source pages and their direct file links were inspected on 2026-09-19 before the new impact archive was downloaded. Earlier downloaded originals were rehashed on disk. All source archives and extracted files are non-shipping evidence. Each page declares CC0; the archival creator attribution is retained even though CC0 does not require it.

| Page, title and creator | Direct original and SHA-256 | Purpose |
| --- | --- | --- |
| [Zombies Sound Pack](https://opengameart.org/content/zombies-sound-pack), artisticdude, 24 WAV files, CC0 | [zombies.zip](https://opengameart.org/sites/default/files/zombies.zip) → `original/zombies.zip`, `8096CEEB4DAC35D9EEF9BFE0CC6649778D1EEBF141B208D394AC338B9E5BE314` | General zombie vocal/hit candidates; individual content unconfirmed |
| [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans), ianzazz, CC0; author says free for any use | [zombienoises.zip](https://opengameart.org/sites/default/files/zombienoises.zip) → `original/zombienoises.zip`, `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6` | Groans and hurt candidates |
| [Zombie / Skeleton / Monster Voice Effects](https://opengameart.org/content/zombie-skeleton-monster-voice-effects), ArcadeParty, CC0 | [voice archive](https://opengameart.org/sites/default/files/Voice%20Effects%20Zombie-Skeleton-Monster%20Human%20Male.zip) → `original/Voice_Effects_Zombie_Skeleton_Monster_Human_Male.zip`, `041EF356EFC5D947DB903530D68EB55B7E6FBFB77B96FDD092AB81EB8BE59D57` | Attack and death voice candidates; mixed pack requires clip review |
| [Footsteps](https://opengameart.org/content/footsteps-0), GboxMikeFozzy, CC0, recorded subway steps | [01-footstep.ogg](https://opengameart.org/sites/default/files/01-footstep_0.ogg) → `original/01-footstep.ogg`, `33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC`; five more direct links in `source_ledger.md` | Move and retreat contacts; surface fit unconfirmed |
| [Impact](https://opengameart.org/content/impact), Iwan “qubodup” Gabovitch, CC0; page says impacts based on two earlier qubodup Freesound recordings | [qubodupImpact.7z](https://opengameart.org/sites/default/files/qubodupImpact.7z) → `original/qubodupImpact.7z`, `98D72B55D6F78A32072439ED4D052FC43FDD80B8B409D18A9BB3150FC2CCD97B` | Explicit meat impact candidates for attack, defend and support attack |

The impact archive extracted successfully with locked source bytes preserved. `extracted/qubodupImpact/qubodupImpact/qubodupImpactMeat01.ogg` SHA-256 `1A3EF408F784204053BC1606C39BCAD9DACCE4BFB30F30980D0BA51EF1CA1379` and `...Meat02.ogg` SHA-256 `44FB337B317E95C32531BE17173B5A533E1513A80D5F889B477770A65FBC6B5E` each probe at 0.5 seconds. These are candidates, not accepted sonic matches. The OGA impact page declares CC0 for the derivative; underlying Freesound pages were not independently audited, so preserve that uncertainty in a final source choice.

Other examined file hashes and durations: `extracted/zombienoises/zombienoise1.ogg` `E3105F5259AD8B17BD1134C5A5CEE79FC7F2F3662466D348BC05944CB92F16AE` (2.116848 s); `extracted/zombienoises/fastzombie1.ogg` `21B7FB4BD7C588AD67FAFCB1D72BDD65312FF22AE60660D552E7477C569111FE` (0.336689 s); `extracted/voice_effects/Voice Effects Zombie-Skeleton-Monster Human Male/zombieYell1.wav` `8C7A107AB2696B9905BFDAEADAD6CC255F091676538B35BC12B0A85ADE69E8DE` (0.384580 s); `.../zombieDeath1.wav` `F32B96086C4E23E568508BD0542BFDADB34EF0D5DC1FEF9094B82DC18AA1C623` (0.644354 s); `extracted/zombies/zombies/zombie-1.wav` `DAD8280256985CADC5745F407C53EBDCF428D55E6369A70847E5B83D60E98C17` (0.854172 s). File names and waveform metadata do not establish audible suitability.

Five review-only Opus previews under `previews_20260919/` were mechanically converted from those originals with ffmpeg (`-ac 1 -ar 16000 -c:a libopus -b:a 16k`, maximum four seconds), without sound design or synthesis. They are not game-ready assets: `idle_groan.ogg` `89989D1A7E7BB4712B3FB12202D451E9FF136AF324309AB737A97077C8F993B7`; `attack_vocal.ogg` `E2531B5285786DD52832E57B6C9CB28A3CF61B0201E8DE3C84F07B7BAE350DF4`; `death_vocal.ogg` `4386B077187302B58A0A7B5109F27F37BC5A17AF38778AD4362260F99DEFB084`; `footstep_1.ogg` `FBBEE633DD6E740C2D1A558BBF4ABD311B1AF6DB314ED47825EEBBD2B3451EAE`; `zombie_pack_1.ogg` `0508FD2A1FEF455EBDCD3F8C6FF8F83464E2603C328EB51572AA1634E9067478`. The tool could not return audible preview to this agent, so no clip has passed listening review.

## Historical intended roles and synchronization handoff

| Role | Candidate source | Intended action phase | Status |
| --- | --- | --- | --- |
| Idle groan and ambient vocal | `zombienoise1.ogg`, then compare 24-sound pack | Idle breath/groan accent, sparse loop | needs_user_review |
| Move and retreat footsteps | Six installed `zombie_move_step_*.wav` files; preserved originals `01-footstep.ogg` through `06-footstep.ogg` | Entity events at 0.3333 and 1.0000 in each looping move/retreat state | source-to-runtime hashes verified; contact alignment still needs user review |
| Attack vocal | Three installed `zombie_attack_vocal_*.wav` files from `zombieYell1.wav` through `zombieYell3.wav` | Attack and support attack event at 0.3333 (frame 8 at 24 fps) | needs_user_review for sonic fit and playback alignment |
| Attack impact | Two installed `zombie_attack_impact_*.wav` files from `qubodupImpactMeat01.ogg` and `Meat02.ogg` | Attack event at 0.6667 (frame 16 at 24 fps) | needs_user_review for sonic fit and contact alignment; underlying Freesound provenance unresolved |
| Defend and support contact | Same installed meat-impact files through distinct wrappers | Defend event at 0.5000 (frame 12); support attack at 0.6667 (frame 16) | needs_user_review for sonic fit and contact alignment |
| Hurt/injured | Installed `zombie_hurt_01.wav` from `zombienoise2.ogg` | Wrapper exists, but no entity event invokes it | blocked: live consumer absent; sonic fit needs review |
| Death | Three installed `zombie_death_vocal_*.wav` files from `zombieDeath1.wav` through `zombieDeath3.wav`; later sourced meat-impact derivatives for the base impact event | Vocal event at 0.5000 (frame 12), sourced impact event at 1.5000 in controlled death v9 | needs_user_review for sonic fit and action alignment; five legacy specialized-wrapper mappings remain unresolved |
| Selection and acknowledgement | Zombie pack/noise alternatives | UI voice consumer depends on original tag | blocked: tag-scoped selection has no verified subunit-specific route |

Vanilla `gfx/entities/units_infantry.asset#infantry_rifle_entity` triggers `infantry_move_animation`, defined in `sound/soundeffects.asset` with per-variant `sound.asset` entries. Vanilla `integrated_dlc/dlc018_together_for_victory/sound/vo.asset` names selection voice lines by country and infantry class, such as `GER_infantry_idle`; a zombie-only selection voice cannot be promised through that consumer without a verified subunit route. The current mod binds distinct final v1 attack, defend, support attack, move, and retreat actions plus controlled death v9, and `gfx/entities/chaosx_zombies.asset` now invokes `chaosx_zombie_attack_vocal`, `chaosx_zombie_attack_impact`, `chaosx_zombie_defend_contact`, `chaosx_zombie_support_attack_contact`, `chaosx_zombie_death_vocal`, and `chaosx_zombie_death_impact` at the numeric times above. `chaosx_zombie_hurt` is defined without a verified consumer; `chaosx_zombie_retreat_step` remains a proposal because retreat uses `chaosx_zombie_move`. The source timing values are implemented, but no listening or live-game review has established exact contact synchronization.

## Movement source-to-runtime crosswalk, 2026-09-20

The earlier movement provenance note is superseded by `older_move_runtime_crosswalk_20260920.json`. All six installed movement WAVs have a preserved original, direct source URL, original SHA-256, deterministic conversion command, runtime SHA-256, and byte-for-byte reproduction receipt. Re-running the documented FFmpeg command reproduces every installed movement file exactly, and all six runtime files meet the signed-16 PCM, 44.1 kHz, mono contract.

This closes the six-file movement provenance gap. `older_attack_death_partial_crosswalk_20260920.json` additionally closes `zombie_attack_01.wav`. The base entity's death impact now uses the later sourced meat-impact derivatives; the other five older attack/death WAVs remain specialized-wrapper assets and still need their own source-to-runtime crosswalk. Sonic suitability, exact contact timing, the hurt consumer, acknowledgement selection, and live playback remain open review items.
