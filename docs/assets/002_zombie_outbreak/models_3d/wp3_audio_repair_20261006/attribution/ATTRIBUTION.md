# WP3 zombie audio attribution evidence

Zombie source recordings and the cross-package evidence cited below were already present in the repository. No download or recording was made for this repair.

## Idle moan source set

Source: “Zombie noises and moans” by ianzazz, labeled CC0 on the archived OpenGameArt source page: <https://opengameart.org/content/zombie-noises-and-moans>. Archived direct pack URL: <https://opengameart.org/sites/default/files/zombienoises.zip>. The unchanged source archive is `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_downloads/idle_moan/zombienoises.zip`, SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.

| Archived archive member | Extracted source file | Source SHA-256 | Prior runtime match | Match evidence |
| --- | --- | --- | --- | --- |
| `zombienoise1.ogg` | `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_downloads/idle_moan/extracted/zombienoise1.ogg` | `E3105F5259AD8B17BD1134C5A5CEE79FC7F2F3662466D348BC05944CB92F16AE` | `sound/002_zombie_outbreak/zombies/zombie_idle_moan_01.wav` | Decoded mono 44.1 kHz full-duration comparison: 93,353 samples each; Pearson correlation 0.999999436; least-squares gain 0.70711100 (-3.010 dB); residual RMS 0.00000881715. |
| `zombienoise2.ogg` | `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_downloads/idle_moan/extracted/zombienoise2.ogg` | `F9E23D6545F64798D29F2B7AC767DA6208C1DC43B6D0928DC037FAE4BCA13B13` | `sound/002_zombie_outbreak/zombies/zombie_idle_moan_02.wav` | The source/member is in the recorded three-file CC0 family. The prior installed conversion was shortened; exact alignment and current preimage were not accepted for replacement in this repair. |
| `zombienoise3.ogg` | `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_downloads/idle_moan/extracted/zombienoise3.ogg` | `968B48B14A83A17B387E7373C83D3B9553BF21D2B0E03A67909EAD4FC21F38B1` | `sound/002_zombie_outbreak/zombies/zombie_idle_moan_03.wav` | Decoded mono 44.1 kHz full-duration comparison: 29,582 samples each; Pearson correlation 0.999995753; least-squares gain 0.70708251 (-3.011 dB); residual RMS 0.00000878193. |

The extracted OGG SHA values are the source-member hashes; archive SHA and the archived license statement are separately retained above. The correlations bind the prior runtime recordings to those specific members despite lossy Vorbis decoding and prior downmix/gain processing. This is not an audible semantic or quality review.

## Other archived recording families reviewed

- `ZombiePackSFX 2` by Colodical, CC BY 3.0, <https://opengameart.org/content/zombiepacksfx-2>, is a distinct, labeled set of seven recordings (brains, idle, sniffing, attack, lunge, defeated, eating). Exact original SHA-256 values and license text are in `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_acquisition_20260926.md`. The existing package already has derivatives for attack, lunge, defeated, and eating; the archive provides one take per labeled role and does not establish a multi-take pool. No role was changed or wired here.
- The artisticdude zombie CC0 archive contains 24 numbered clips that already have listening-reviewed assignments in `docs/assets/002_zombie_outbreak/models_3d/zombie_variant_sound_spec.json` and `zombie_variant_sound_receipts.json`. Preserve those assignments; do not infer additional roles from filenames or archive order. Its existing mapping has demonic attack (14, 13) and scream (9); mutant attack (4, 7) and roar (12); parasitic gurgle (18, 21) and feed (19); rabid attack (5, 6, 8); undead grunt (1?3), pain (22, 24), and moan (16). These assigned takes do not supply the requested additional specialized pools.
- The archived footsteps and punch sources are identified in `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_acquisition_20260925.md`; the punch source does not establish cloth/flesh or wet-contact semantics by filename alone. No cough/retch/spit, wet lash/suction, dedicated rabid shriek/death-gasp, demonic low-growl, or mutant heavy-voice pool is evidenced by the currently available zombie source files.

## Level contract

The WP3 source brief says shared zombie moans should be targeted at -20 LUFS as loops. The cross-cutting audio pipeline in `unit_fix_plan.md` section 3.5 also requires -20 LUFS with true peak at most -1 dBTP and uses the same role-specific master tool. WP3 section 3 separately mentions a -3 dBFS target for shared steps/voices. These are distinct role instructions; this repair uses the `loop` preset and records any target conflict from the gate instead of changing accepted shared levels silently. The existing global master pass left moan01 and moan03 `needs_review`, while moan02 was previously staged and is already the accepted installed output. This repair installed a new moan01 candidate; moan03 remains unchanged because the shared gate cannot produce a loop-valid file.

## Previously documented monster source gap

A historic paleogenetic handoff records Ogrebane?s *Monster Sound Effects 2* as CC0 from <https://opengameart.org/content/monster-sound-effects-2>, archive SHA-256 `8D9831E5596446EBAFB8E6A958E757F07CBD385F9E417B4D9704D63A05A2CD63`, with 17 sequential WAV members. The archive and extracted files are absent from the current `docs/assets` tree; the current WP5 audio-needs plan says the originals/archive need reacquisition. This is a prior source reference, not an archive available to stage from this task.

An existing cross-package candidate for a wet eating/biting texture is `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/audio/derived/black_plague_rat_bite_wet_01.wav`, SHA-256 `24FFCA89AFC65AD59335BB846F044AC0CB0324D95C3E48017F3395351C26AE10`. Its receipt traces it to public-domain `cat_eating_noisily.ogg`, source SHA-256 `B96EE393ADAB3A45832B0BE54C3CB0726F7317EC52F203ED18AE2B1B30D4B955`, <https://commons.wikimedia.org/wiki/File:Cat_eating_noisily.ogg>. The original recording is absent from this workspace, but the derived 1.2 s candidate and source receipt are present. The rat package labels it a review-gated cat wet-bite candidate; it may be considered for parasitic feed only after listening review. It does not establish a lash, suction, spit, or multi-take pool.

## Additional explicit idle-role candidate

Source: “ZombiePackSFX 2” by Colodical, labeled CC BY 3.0. Source page: <https://opengameart.org/content/zombiepacksfx-2>. The archived original is `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_downloads/zombiepacksfx2_20260926/zombieidlesfx.wav`, SHA-256 `76820CFEC561EADD6EF39F2F0F31BA444CD11E3D2CAE2CE3AD7D4270CF6F812B`. The archived source page labels this recording “idle.” This is a distinct recording from the ianzazz source members. It is staged only as a possible additional zombie idle/moan take for human listening; no demonic growl, undead-exclusive voice, final quality, or runtime acceptance is claimed.
## Shared step source records

The six movement recordings are from “Footsteps” by GboxMikeFozzy, labeled CC0 on the archived OpenGameArt source page <https://opengameart.org/content/footsteps-0>. Direct source links in the archived acquisition record point to `01-footstep_0.ogg` through `06-footstep.ogg`. Their exact extraction paths, SHA-256 values, and per-take decoded comparison with the currently installed runtime files are captured in `evidence/step_source_comparison.json`; no file was downloaded in this repair.

| Source member | Direct source URL | SHA-256 | License |
| --- | --- | --- | --- |
| `01-footstep_0.ogg` | `https://opengameart.org/sites/default/files/01-footstep_0.ogg` | `33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC` | CC0 |
| `02-footstep.ogg` | `https://opengameart.org/sites/default/files/02-footstep.ogg` | `F05396C807EB8EAECFFB2A1EAD611EC971C5A7914D1D081C91D7796E852692A2` | CC0 |
| `03-footstep.ogg` | `https://opengameart.org/sites/default/files/03-footstep.ogg` | `9817CC93897ED1DE5DA87675B26BE4196BFDA3DAA6F1DE9DC4398A68D250CDB9` | CC0 |
| `04-footstep.ogg` | `https://opengameart.org/sites/default/files/04-footstep.ogg` | `B373FF981E44D6F7BA2291225A4803078771029615ED81606136FDB9599906D5` | CC0 |
| `05-footstep.ogg` | `https://opengameart.org/sites/default/files/05-footstep.ogg` | `F1B4893DD3CEBE23438567A0DCAF047848A52B594E7EB03E5C212D99E83D2298` | CC0 |
| `06-footstep.ogg` | `https://opengameart.org/sites/default/files/06-footstep.ogg` | `39147CC1B98ABB4B5378AD07B15D50D18F2AA0F0FD2F5514F078C1E574D14773` | CC0 |

## Sample windows for isolated step-master candidates

`candidates/step_excerpt_input/zombie_move_step_03_excerpt.wav` is the 0.100 s sample window from `03-footstep.ogg` at source offset 0.110 s; archived OGG SHA-256 `9817CC93897ED1DE5DA87675B26BE4196BFDA3DAA6F1DE9DC4398A68D250CDB9`, excerpt input SHA-256 `4876C27ABD80E79F40B9A100DE472E2A558B936C81D3AEAB09105177E3CA5460`.

`candidates/step_excerpt_input/zombie_move_step_04_excerpt.wav` is the 0.100 s sample window from `04-footstep.ogg` at source offset 0.090 s; archived OGG SHA-256 `B373FF981E44D6F7BA2291225A4803078771029615ED81606136FDB9599906D5`, excerpt input SHA-256 `978E52BFBB088BA9266503E9DBCADD036BF997C5E2BC168B94D9D058A248900F`.

Both source recordings are from “Footsteps” by GboxMikeFozzy, CC0, <https://opengameart.org/content/footsteps-0>. The offsets select one measured peak window with recorded pre-roll and release; this is waveform-window evidence, not an auditory classification.

## Demonic pitch-derived candidates

All inputs are listening-classified takes from the existing `Zombies Sound Pack` archive by artisticdude, labeled CC0 1.0 on <https://opengameart.org/content/zombies-sound-pack>. Source-to-role assignments are in `docs/assets/002_zombie_outbreak/models_3d/zombie_variant_sound_spec.json`; exact source/derivative SHA links are in `zombie_variant_sound_receipts.json`.

| Candidate role | Original source member | Original SHA-256 | Source role | Recorded trim (s) | Pitch operation | Pitch-stage SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |
| demonic scream, low variant | `zombie-9.wav` | `938C9A75828CDA0EC78482E7A969CEBC8F989968DCDE15326E8C5A2F437FD468` | listening-classified demonic scream | 0.049–0.874989 | rubberband pitch ratio 0.8408964153 (-3 semitones), tempo 1, formants preserved | `A1AB510E605CC201DDF8A0B38EED08EFA26B5520F9E62F7D5260E274FA9780D1` |
| demonic scream, high variant | `zombie-9.wav` | `938C9A75828CDA0EC78482E7A969CEBC8F989968DCDE15326E8C5A2F437FD468` | listening-classified demonic scream | 0.049–0.874989 | rubberband pitch ratio 1.1224620483 (+2 semitones), tempo 1, formants preserved | `A740602362D89813FA5122184E5B5935FD3F2A8BDD83EA9D03A74132A57D1E34` |
| demonic attack, low variant | `zombie-13.wav` | `B8A64C3A557D7CE0B69492717BC1A88706B69C499A2714F02527D822A8462545` | listening-classified demonic attack growl | 0.0379–0.562517 | rubberband pitch ratio 0.7937005260 (-4 semitones), tempo 1, formants preserved | `96B2546DF23AABDDABA90861BDB43EC20C772C4BC3476FE69DE77F8749474154` |
| low-growl loop candidate, take 13 | `zombie-13.wav` | `B8A64C3A557D7CE0B69492717BC1A88706B69C499A2714F02527D822A8462545` | listening-classified demonic attack growl | 0.0379–0.562517 | same recorded pitch stage as the attack variant; separate loop master gate, never wired as an attack-effect alias | `96B2546DF23AABDDABA90861BDB43EC20C772C4BC3476FE69DE77F8749474154` |
| low-growl loop candidate, take 14 | `zombie-14.wav` | `B1FFFBF93FD9CF353A9DD0D519B6CD6E739BD3FB28853A580E018AC73EFDDA4B` | listening-classified demonic attack growl | 0.0259–0.666667 | rubberband pitch ratio 0.7937005260 (-4 semitones), tempo 1, formants preserved | `8D983BE44F6B4E094DFEEF80F8D8C9C4994134B68A426D05ED5A7D64D913C79E` |

Pitch derivatives are correlated variants of the named CC0 recordings, not new recordings or independent takes. Their pitch processing preserves the trimmed source duration. Final one-shot levels and the proposed loop seam pass remain controlled by `.tools/3d_pipeline/audio/master.py`; a loop candidate is not promoted if it fails the shared loop boundary or -20 LUFS/-1 dBTP gate.
