# Zombie model and audio repair — 18 October 2026

Status: scoped combat-animation and audio repair installed and reviewed from runtime bytes.
Eight replacement combat actions are installed across base, infected, necrotic, rabid, undead and demonic zombies; the other combat actions were individually qualified and retained.
All seven added semantic soundeffects are wired.
The separate demon job still owns its mesh/weight/gait defects; this report does not claim that job is complete.
No in-game validation is claimed.
This job owns base zombies and the seven named variants' attack, defend and support-attack work, plus the scoped zombie audio package.
The demonic job remains active; its handoff was reread before the final combat copy.
This job changed only its support-attack animation and combat/idle sound bindings, preserving the sibling?s move/retreat edits and leaving its mesh and weights untouched.

## Current work

The shipped base combat motions pull or lift the hands without a readable strike/contact/recovery sequence.
Three separate archived presets were ingested through the locked adapter, with their existing source hashes and task receipts verified: Punch Forward with Both Fists for attack, Block2 for defend, and Punch Combo for support attack.
The original installed mesh, skin weights and runtime textures are preserved.
Manual live Blender work gives attack a forward step, grab, pull and overhand claw strike; defend braces and makes a one-arm counter-shove; support attack makes alternating forward claw swipes.
An independent source-pose review rejected the earlier bite gesture as weak and face-guard-like, then accepted the corrected grab/club sequence with commitment before contact and recovery afterwards.
For the attack's live IK controls, existing limb tails were lengthened to their measured child-joint heads without adding bones or changing weights; maximum rest-matrix rounding delta was about 0.0000052.
The original runtime skeleton remains in the unchanged mesh, and actual-byte reimport proves the resulting animation against it.
The overly fast opening shuffle was removed from attack, and each combat action received deliberately authored root-height corrections from measured contacts.
Live-authored torso controls were baked with Blender's native visual-keying operator to preserve facing through the source hip turns; no procedural motion, automatic rig or automatic weights were generated.

Base candidate sources under `docs/assets/002_zombie_outbreak/models_3d/zombies/`:

- Attack: `models_1018/attack_club_delivery.blend`, 106 frames at 30 FPS; selected export `export/models_1018_v13/chaosx_zombies_attack.anim`, SHA-256 `DECB3A36F0D1D88A1EC782A13CC2351F9BB4DA7A3E054EB399127C81FC981022`, with proof `blender/checkpoints/reimport_models1018_base_club_attack.blend`.
- Defend: `models_1018/defend_candidate.blend`, 49 frames at 30 FPS; `export/models_1018_v4/chaosx_zombies_defend.anim` passes the exported delivery gate and has native proof `blender/checkpoints/reimport_models1018_base_defend.blend`.
- Support attack: `models_1018/support_60fps_final.blend`, 149 exported samples at 60 FPS; selected export `export/models_1018_v9/chaosx_zombies_support_attack.anim`, SHA-256 `1206DB6E2067A87BB323A2194747274596130D64BAF37D6376FC9C6F1E4C51DE`, with proof `blender/checkpoints/reimport_models1018_base_support_final.blend`.

Earlier exports remain diagnostic candidates and must not be installed by filename similarity.
The selected attack v13 supersedes v7 and every earlier attack candidate.
`runtime/models_1018_base_install.json` records selected source/destination hashes, prior runtime hashes, preimages, proofs and the superseded copy history.
Defend's installed SHA-256 is `0B1D13307C6B9B2A680D4E5B2E2054F5C1E3FFBD4B5522C4D66022BB76206E94`.
All three selected animations pass the actual-byte motion/root/seam gates; the final attack does not need quaternion-sign repair.
The parent reviewed every exported integer frame from front/side/map views and sampled all half frames geometrically.
Native minimum-Z ranges are attack 0.00190–0.00795, defend 0.00129–0.00939, and support 0.00166–0.01059 source units.
Support uses 60 FPS to retain contact corrections between the original 30 FPS samples; the retimed source was corrected and rechecked before selection.
The attack's physical duration was extended to 3.5 seconds between endpoint samples so its overhand wind-up and return meet the motion limits while keeping every authored phase.
Base entity sounds follow grab at native frame 26.5, pull at 34, overhand strike at 70, and the measured sole contacts around 21 and 97.

## Variant progress

Infected attack is installed from `infected_zombies/export/models_1018_pelvis/chaosx_infected_zombies_attack.anim`, SHA-256 `A0FBE7D8C88081A3CCCADE9FFE7BC25350F998B46A093C2F287AFFE0B55C9774`.
It uses the verified Punch Combo archive with a forward plant, grab/pull and cross-body claw; the original 103-degree pelvis turn at the grab opposed the planted legs and forward torso, causing a coat corkscrew.
Manual pelvis rotation cleanup removed that defect without editing mesh or weights, and an independent focused visual recheck accepted it.
All 75 exported frames were reviewed from front/side/map, with half-frame minimum-Z 0.00698?0.00734.
Its copy authority is `infected_zombies/runtime/models_1018_install.json`, and source is `models_1018/attack_pelvis_baked.blend` in that job root.
The five unchanged noncombat actions were rendered and reviewed at five phases; the inherited limp was preserved rather than represented as a repaired symmetric gait.
Infected support retains its retch/expulsion motion, with reviewed frames 75?95 and cough/spit cues; training uses the separate cough pool.
Rabid and mutant death states use their dedicated four-take vocals while retaining body-fall timing.

Necrotic attack candidate `necrotic_zombies/models_1018/attack_baked.blend` uses a separately ingested Punch Combo source and deliberate live forward plant/grab/pull/diagonal-rake poses.
Its exported 75-frame bytes pass delivery checks and were reimported and rendered in every frame; the current candidate hash is `B8AFFB8868998309BA4B4CD2F14DD41D142456DDB625033B65C73B7BB10F3979`.
Independent source-pose review accepted the catch-and-rake sequence, and the selected bytes are installed with contact cues at frames 22 and 54.
Its source/destination copy authority is `necrotic_zombies/runtime/models_1018_install.json`; actual-byte half-frame minimum-Z is 0.00472?0.00863.
Five unchanged noncombat necrotic actions were rendered/reviewed, and its defensive recoil remains distinct from the attack.

Rabid support attack is installed from `rabid_zombies/export/models_1018_stable/chaosx_rabid_zombies_support_attack.anim`, SHA-256 `80FB63717572B4FEEDE1126F29B5E68C5B71DD0617E037DFDA3665521EE1B00A`.
It uses the separate Double Fist preset, with plant 22, catch 36, pull 48 and a head/torso biting lunge at 58, followed by release and recovery.
The source-pose reviewer accepted that sequence; native review covers all 105 frames and half-frame minimum-Z 0.00728?0.00804.
An interpolation defect was caught before installation: provider arm-roll keys were competing with live IK controls, causing rapid elbow flips.
The final cleanup uses explicitly placed elbow controls and retains the chosen starting arm bend beneath them; the rejected exports are not installed.
Selected source: `models_1018/support_stable_baked.blend`; copy receipt: `runtime/models_1018_install.json` in the rabid job root.
The biting motion is conveyed through head/torso movement, not an independently animated jaw.

Undead support attack is installed from `undead_zombies/export/models_1018_slow/chaosx_undead_zombies_support_attack.anim`, SHA-256 `4704E044DA8987C6461E7D05B412482C5918B3194FBB808C036DF7CBFF17E63D`.
Its separately ingested Punch Combo cleanup replaces the prone ground-feeding gesture with a planted low catch, right-arm windup, low cross-body rake and rise.
The action was physically slowed by 1.5 times to remove an excessive forearm transition while preserving the authored poses; it is 112 samples at 30 FPS.
Native review covers every frame and half-frame minimum-Z 0.00818?0.00886.
Selected source: `models_1018/support_delivery.blend`; copy receipt: `runtime/models_1018_install.json` in the undead job root.

Demonic support attack is installed from `demonic_zombies/export/models_1018_combat_final/chaosx_demonic_zombies_support_attack.anim`, SHA-256 `5658C671514806AC7426B976EB3FFA0DAB8F0052682E6FDCD82697ED7C124933`.
Its distinct Double Fist preset cleanup gives a forward plant at 20, paired overhead preparation at 40, double-claw downward slam at 60 and follow-through at 69, with recovery by 105.
The wings follow the existing spine hierarchy; this job added no wing bones or weights.
A heel vertex with equal leg/foot influence dipped during the high preparation pose, so its ankle-contact keys were corrected locally rather than changing the sibling-owned skin weights.
The exporter?s four q/-q sign changes were normalized without altering orientations, timing or translations; the final actual-byte gate passes.
All 105 exported frames were reviewed against mesh SHA-256 `1F22772883C2E1B16BA4ED6C64752602B59048BF19D6592CF3DD87A24386EACC`; native half-frame minimum-Z is 0.00803?0.00869.
Selected source: `models_1018_combat/support_final_baked.blend`; copy receipt: `runtime/models_1018_combat_install.json` in the demonic job root.
The sibling?s currently installed 120-FPS move/retreat files were rendered read-only and are not this job?s changes or acceptance claim.

### Retained combat qualification

| Unit | Attack | Defend | Support attack |
|---|---|---|---|
| Base | Replaced: grab/pull/overhand claw | Replaced: brace/counter-shove | Replaced: alternating claw swipes |
| Infected | Replaced: planted catch/cross-rake | Retained hit recoil | Retained retch/forward spit, with cough/spit vocals |
| Rabid | Retained broad clawing flurry | Retained hit recoil | Replaced: catch/pull/biting lunge |
| Parasitic | Retained directed crown lashes | Retained host/crown recoil | Retained loaded forward crown thrust |
| Undead | Retained directed claw/downward sweep and recovery | Retained compact guard/recoil | Replaced: low catch/rake |
| Necrotic | Replaced: catch/pull/diagonal rake | Retained evasive recoil | Retained raised-arm curse/sweep role |
| Mutant | Retained broad claw sweep | Retained guard/recoil | Retained crouch/pounce/hand slam |
| Demonic | Retained alternating claw slashes | Retained wing-wrapped dodge | Replaced: paired downward slam |

Qualification used the actual installed animations, nine combat phases where retained, and additional contact neighborhoods when broad sampling was ambiguous.
An independent reviewer checked base and replacement variant source poses and the parasite/mutant/undead/necrotic qualifications; the parent reviewed the installed-byte renders and actual fixes.
The mutant facing suspicion did not establish a quarter-turn error: measured head-forward vectors still point toward the enemy, with about 20?23 degrees of yaw within its recoiling stance.
No blanket facing rotation was applied.

## Evidence and routes

The owned hidden Blender Lab process was PID 31832 on port 9885, Blender 5.2.2 LTS.
It was closed after final review, with PID, executable name and port argument verified before stopping it; no other Blender process was stopped.
The live bridge returned that exact PID before source work.
Adapter 1.11.0 health passed; `.tmp/models_1018/zombies/current_dependency_preflight.json` records no locked-dependency findings.
The initial attack reimport request failed because the candidate folder had no adjacent DDS maps; one corrected retry with copies of the actual runtime DDS bytes succeeded.
The exporter's equivalent-quaternion sign flips are corrected only with the existing `anim_signs.py` operation, followed by actual-byte delivery analysis; rejected motion findings were repaired in the source, not waived.

Review renders and contact sheets are under `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/current_review/`.
They include the preset candidates, authored strike phases, interpolation corrections, native attack/defend frames and floor scans.
`runtime_geometry.json` records current runtime mesh hashes and passing closed-surface/winding checks for all eight named zombie meshes.
The base eight-action overview is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/final_base_actions_contact_sheet.png`.
Full final combat frames use prefixes `club_attack_native`, `native_defend`, and `approved_support`; their numbered contact sheets were visually reviewed.
The final replacement-action sheet is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/final_reimported_actions_contact_sheet.png`.
Eight separate `evidence/final_*actions_contact_sheet.png` overviews cover every unit?s eight installed actions; all source frames in them were reviewed individually at front, side and map views.
`evidence/final_integration_checks.json` confirms eight selected copies match source hashes and all 64 states resolve their soundeffect references with timed cues inside their actual animation durations.
These are Blender reviews, with the runtime diffuse decoded for display, rather than engine material or in-game observations.

Offline reference: `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md`, State, lines 124–138, revision `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`, read through MCP.
Installed documentation: `documentation/effects_documentation.md`, `set_entity_animation`, lines 6826–6838, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, read through MCP; this documents script animation selection and does not establish asset timing semantics.
Installed entity precedents were also read from `gfx/entities/units_infantry.asset`.
Installed `GER_infantry.mesh` and attack/move/idle/death actions were imported and reviewed from front/side/map views; their hashes, frames and FPS are in `current_review/vanilla_reference.json`.
The installed standing rifle attack is 79 frames at 30 FPS; the zombie's 106-frame main attack gives its step/grab/overhand sequence a longer deliberate cycle, while defend is 49 frames and support is 149 samples at 60 FPS.
Both compared combat families stay in place and return to their initial posture; the reference weapon attachments were not part of this body-motion comparison.

## Provider and audio status

No Meshy call or credit expenditure occurred in this run.
Reused historical preset task IDs are `01a0d901-df3b-75f3-9f5a-94c16fcf3a28`, `01a0d901-ce9a-7161-aa19-aba0cefbd0b2`, and `01a0d901-d24e-7637-b96e-7b9d75da6c34`.
The exact ingestion receipts are in `models_1018/preset_receipts/` in the base job root.

The audio delivery comprises 84 installed/replaced source-bound WAVs and seven verified retained moans, with 29 pools updated across 34 soundeffects.
The 126 WAV paths referenced by the three owned sound definitions were checked as PCM16, 44.1 kHz, mono; every vocal/contact pool has four to six source-distinct recordings, while the explicitly retained shared/mutant footstep pools have six/two takes.
The [current source/copy receipt][audio-current] is authoritative for the 84 selected derivatives; each row records the original path and `original_sha256`, creator, licence, source/direct-download URLs, prepared-input hash, mastering receipt/result index, selected-copy hash and installed runtime hash.
The seven retained EmoPreben/AntumDeluge moans have their [original/archive/member/master hash recheck][audio-retained-check] and [source-to-runtime copy rows][audio-retained-copies].
These durable source details and the wiring table below replace reliance on the scratch handoff.

### Recording sources and original-hash evidence

Licences are [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) or [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) unless an explicitly unselected legacy source is noted below.
Original recordings, downloaded archives, source-page snapshots and preimages are retained as non-shipping evidence; original and derivative bytes are kept separate.

| Source and creator | Licence | Use and original-hash evidence |
|---|---|---|
| [16 Monster Growls](https://opengameart.org/content/16-monster-growls), StarNinjas | CC0 1.0 | Mouth-performed growls/grunts; [current original/derivative rows][audio-current] and [archive/member acquisition hashes][audio-earlier-downloads]. |
| [Zombie / Skeleton / Monster Voice Effects](https://opengameart.org/content/zombie-skeleton-monster-voice-effects), ArcadeParty | CC0 1.0 | Zombie death/yell recordings; [current original/derivative rows][audio-current] and [source/attribution rows][audio-earlier-attribution]. |
| [80 CC0 creature SFX](https://opengameart.org/content/80-cc0-creature-sfx), rubberduck | CC0 1.0 | Eating, cough, spit, burble, grunt, hurt and roar source members; [current original/derivative rows][audio-current] and [archive/member hashes][audio-earlier-downloads]. |
| [80 CC0 creture SFX #2](https://opengameart.org/content/80-cc0-creture-sfx-2), rubberduck | CC0 1.0 | Attack, death and additional roar source members; [current original/derivative rows][audio-current] and [archive/member hashes][audio-earlier-downloads]. |
| [Pain sounds by EmoPreben](https://opengameart.org/content/pain-sounds-by-emopreben), EmoPreben | CC0 1.0 | Separate recorded pain takes; [current original/derivative rows][audio-current] and [archive/member hashes][audio-earlier-downloads]. |
| [Zombie Moans 01](https://opengameart.org/content/zombie-moans-01-by-emopreben), EmoPreben | CC0 1.0 | Three retained moans; [original/archive/member/master recheck][audio-retained-check] and [copy/source/URL rows][audio-retained-copies]. |
| [Undead Moans](https://opengameart.org/content/undead-moans), AntumDeluge | CC0 1.0 | Four retained self-performed undead moans; [original/archive/member/master recheck][audio-retained-check] and [copy/source/URL rows][audio-retained-copies]. |
| [Zombie moans](https://opengameart.org/content/zombie-moans), Darsycho | CC0 1.0 | One immutable multi-call original, with five non-overlapping performance windows; [original download hash][audio-downloads], [segment/rate recipes][audio-preparation] and [current derivative rows][audio-current]. |
| [Zomby sfx pack](https://opengameart.org/content/zomby-sfx-pack), saturn91 | CC0 1.0 | Six separately supplied microphone/voice calls; [original file/download hashes][audio-downloads] and [current derivative rows][audio-current]. |
| [Action sounds](https://opengameart.org/content/action-sounds), pauliuw | CC0 1.0 | Recorded cough/spit foley; [archive/member hashes][audio-foley-downloads] and [current duration/mastering chains][audio-current]. |
| [8 wet squish, slurp impacts](https://opengameart.org/content/8-wet-squish-slurp-impacts), Independent.nu, submitted by qubodup | CC0 1.0 | Separate wet contact/slurp source files; [archive/member hashes][audio-foley-downloads] and [current derivative rows][audio-current]. |
| [Body Hitting Ground](https://opengameart.org/content/body-hitting-ground), dklon | CC BY 3.0 | Recorded thick-book/towel floor impacts; [original download hash][audio-body-download], [five non-overlapping impact windows][audio-body-preparation] and [current derivative rows][audio-current]. |
| [40 wet towel club/pound/hit/attack sounds](https://opengameart.org/content/40-wet-towel-clubpoundhitattack-sounds), qubodup | CC0 1.0 | Recorded wet towel applied to a human back; the source-page CC0 grant explicitly supersedes contrary archive TXT; [archive/member hashes][audio-contact-download] and [five final contact source/copy chains][audio-contact-final]. |
| [Zombies Sound Pack](https://opengameart.org/content/zombies-sound-pack), artisticdude | CC0 1.0 | Retained classified variant recordings and the separately lowered mutant roar source; [original 24-file source hashes][audio-artisticdude] and [current new derivative chain][audio-current]. |
| [ZombiePackSFX 2](https://opengameart.org/content/zombiepacksfx-2), Colodical | CC BY 3.0 | Retained base attack, lunge, eating and defeated mouth voices; [original-member hashes and trims][audio-base-originals], [source/terms acquisition record][audio-base-acquisition] and [shipped base attribution][audio-base-attribution]. |
| [Footsteps](https://opengameart.org/content/footsteps-0), GboxMikeFozzy | CC0 1.0 | Six retained shared footfalls and two EQ-treated mutant footfalls; [original source-member SHA-256 mappings][audio-steps] and [mutant original-to-EQ chains][audio-mutant-steps]. |

The primary current receipt links the full mastering commands and measurements through each row's `master_receipt` and `master_result_index`; source-file hashes must not be confused with archive, selected-derivative or runtime hashes.
Rate changes, quiet-margin/contact crops, channel/sample-rate conversion, gain, bounded limiting and short fades modify recorded samples only; no synthetic, generated, newly recorded or placeholder sound was used.
Darsycho's four lower demonic performances use non-overlapping windows at 0.75 source rate, and the four mutant roar files each retain a different underlying performance; pitch variants of one performance are not counted as extra takes.
The [final duration/contact correction receipts][audio-duration-final] preserve previous selected copies and exact crop/rate operations; their five historical CGEffex rows are superseded by the final qubodup contact receipt.
The [shipped attribution][audio-attribution] identifies selected authors, licences and permitted modifications.

The earlier CGEffex/congusbongus [Punch, slap, n' kick](https://opengameart.org/content/punch-slap-n-kick) chain was rejected after review of its [upstream Freesound page](https://freesound.org/people/CGEffex/sounds/98341/) left remix/recording rights unresolved.
The [rights disposition][audio-rights] distinguishes that unresolved chain from a proven infringement claim, and all five current contacts use qubodup recordings instead.
The downloaded [7 Eating Crunches](https://opengameart.org/content/7-eating-crunches), by Tito with StarNinjas, are CC0 but unselected; their original archive/member hashes remain in the acquisition receipt.
The historical base attribution additionally records remaxim's [Falling body](https://opengameart.org/content/falling-body), CC BY-SA 3.0, and Delta12 Studio's [RPG Sound Effect Pack](https://opengameart.org/content/rpg-sound-effect-pack), CC0; those older individual samples are not selected by the current owned body-fall/contact pools, and their original source hashes remain in the base receipts.

### Current entity cue wiring

| Entity/state | Current soundeffect and event time seconds | Wiring status |
|---|---|---|
| Rabid / death | `chaosx_rabid_zombie_death` at 0.0667 | Installed by scoped audio-worker exception; body-fall stays at 1.4667. |
| Mutant / death | `chaosx_mutant_zombie_death` at 0.0667 | Installed by scoped audio-worker exception; body-fall stays at 0.6333. |
| Infected / training | `chaosx_infected_zombie_cough` at 1.2000 and 3.9667 | Both existing coughing events were rebound without retiming. |
| Infected / support attack | `chaosx_infected_zombie_cough` at 0.3000 and 1.5000; `chaosx_infected_zombie_spit` at 2.7333 | Parent-installed bindings, verified in current entity source. |
| Rabid / support attack | `chaosx_rabid_zombie_shriek` at 0.2000; `chaosx_base_zombie_eating` at 1.8000 | Parent-installed bindings, verified in current entity source. |
| Demonic / idle-defend | `chaosx_demonic_zombie_idle`, `trigger_once = yes` on state entry | Parent-installed one-shot bindings; no recurring timed trigger was added. |
| Parasitic / attack lash contacts | `chaosx_parasitic_zombie_lash` at 0.5500 and 2.4500 | Parent-installed bindings, verified in current entity source. |

All seven added semantic soundeffects have the bindings listed above.
Acquisition, mastering and initial phase receipts retain historical delivery statuses; the current entity wiring table here supersedes their earlier pending-binding labels.
The audio worker's entity patch changed exactly four soundeffect references across `gfx/entities/chaosx_rabid_zombies.asset`, `gfx/entities/chaosx_mutant_zombies.asset` and `gfx/entities/chaosx_infected_zombies.asset`, preserving event times, body-fall/particle events and every other state at that patch snapshot.
The parent's subsequent combat/support changes remain parent-owned.
`ZZZ_infantry_idle` is the `Voices` category country/original-tag selection route for all infantry under ZZZ, including variant Hordes and Wendigo Pack; no per-subunit selection or selection for other original tags is claimed.

### Audio checks and integration boundary

The [installed WAV/ffprobe measurements][audio-wav-audit] and [actual pool audit][audio-pool-audit] record formats, runtime hashes, timing and the absence of missing-file/undersized-pool or within-pool waveform-correlation findings above 0.8.
The [phase handoff][audio-phases] supplies measured waveform onset and peak offsets; these are signal measurements, not automatic visual-contact approval.
Final grab contacts are 0.342-0.350 seconds with peaks 11.9-26.5 ms after cue start; parasitic lash takes are 0.550 seconds with peaks approximately 11-15 ms after cue start.
Coughs are 0.530-1.080 seconds, spit takes 0.550-0.652 seconds, and mutant roars 1.017-1.453 seconds.
The 3.320-7.067 second demonic idle takes are one-shots bound with `trigger_once = yes`; their playback is not scheduled again at each short defend-loop phase.
Audio input is unavailable in the worker's model, so provenance and decoded waveform/spectrum inspection are not subjective listening or in-game approval.
The parent completed the state/phase bindings and reviewed all three sound definitions; no audio role was omitted or replaced with a synthetic fallback.

The current [audio and scoped-entity SHA-256 inventory][audio-inventory] covers the prior 97 audio/definition/JSON paths plus the three entity files containing the narrow cue changes.
Full entity-file hashes are current snapshots that also include parent-owned combat content; the inventory does not attribute that content to the audio worker.
Its durable handoff pointer identifies this section and its section hash, so the scratch handoff is no longer required to understand source rights, original hashes, selected recordings or wiring status.

[audio-current]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/runtime_install_receipts.json
[audio-retained-check]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/prior_twelve_source_recheck.json
[audio-retained-copies]: ../../assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/runtime_copy_receipts.json
[audio-earlier-downloads]: ../../assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/download_receipts.json
[audio-earlier-attribution]: ../../assets/002_zombie_outbreak/models_3d/zombies/evidence/audio/ATTRIBUTION.md
[audio-downloads]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/additional_download_receipts.json
[audio-preparation]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/preparation_receipts.json
[audio-foley-downloads]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/foley_download_receipts.json
[audio-body-download]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/body_fall_download_receipt.json
[audio-body-preparation]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/body_fall_preparation_receipts.json
[audio-contact-download]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/contact_replacement_download_receipt.json
[audio-contact-final]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/runtime_contact_replacement_receipts.json
[audio-artisticdude]: ../../assets/002_zombie_outbreak/models_3d/zombie_variant_sound_receipts.json
[audio-base-originals]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio_sources/runtime_base_receipts_20260927.json
[audio-base-acquisition]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio_sources/source_acquisition_20260926.md
[audio-base-attribution]: ../../../sound/002_zombie_outbreak/zombies/base/ATTRIBUTION.txt
[audio-steps]: ../../assets/002_zombie_outbreak/models_3d/wp3_audio_repair_20261006/evidence/step_source_comparison.json
[audio-mutant-steps]: ../../assets/002_zombie_outbreak/models_3d/wp3_audio_repair_20261006/evidence/wp3_mutant_short_footfall_receipts_20261006.json
[audio-attribution]: ../../../sound/002_zombie_outbreak/zombies/ATTRIBUTION.txt
[audio-duration-final]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/runtime_duration_refinement_receipts.json
[audio-rights]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/upstream_contact_rights_review.json
[audio-wav-audit]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/installed_wav_ffprobe_and_signal.json
[audio-pool-audit]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/final_sound_pool_audit.json
[audio-phases]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/parent_phase_handoff.json
[audio-inventory]: ../../assets/002_zombie_outbreak/models_3d/zombies/audio/changed_file_sha256.json

## Changed files and limitations

The complete current runtime/definition/source/evidence SHA-256 inventory is `docs/assets/002_zombie_outbreak/models_3d/zombies/evidence/final_changed_file_sha256.json`.
It includes every task-owned shipping path, selected authoring/export/proof files, runtime-copy receipts and the produced review evidence; source and destination hashes are separately recorded in each copy receipt.
The demonic entity hash includes sibling-owned move/retreat text, which this job preserved rather than claiming authorship.
The handoff itself is hashed by that inventory; the inventory does not attempt to hash itself.

No scope simplifications were made.
No requested combat role or audio role was dropped, and no fallback geometry, procedural rig, formula-authored action, synthetic sound or placeholder was shipped.
The changed choreography is documented above; existing geometry, textures, skin weights, animation identifiers and runtime filenames are preserved.
No unit definition, gameplay script, localisation, shared registry or counter was changed.

Review limitations are explicit: Blender Workbench renders inspect the decoded runtime mesh/animation and diffuse appearance, not the engine?s material/light playback.
There was no subjective audio audition because the model cannot receive audio input; source performer descriptions, provenance, waveform/spectrum and loudness/format checks support the audio delivery instead.
There was no live-game validation.
The unchanged zombie gaits were reviewed for visible regressions and were not re-authored into symmetric walks; their inherited shambles are not certified as newly repaired gait.
Retained parasitic attack endpoints have a small sampled minimum-Z excursion of ?0.026714 source units, and mutant attack recovery reaches approximately 0.0618 source units of clearance at frame 105; these unchanged measurements are recorded rather than represented as perfect ground locking.
Demonic wing/arm weight and other geometry findings belong to the separate demon job; this combat handoff does not certify that whole model as one repaired connected shell.
No new visible limb collapse or hole was found in the replacement combat renders.

No commit was made, as requested.
Skills used: `chaos-redux-3d-model-pipeline` and its required operation references, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-units-divisions`.
No skill was created or modified.

## Storage cleanup note (18 October 2026)

The parent applied the 3D skill's workspace-size rule to the zombie job roots after reviewing and committing this work, because the user's disk was nearly full.
Superseded checkpoints, working copies, preview renders, adapter logs and the PNG renders under `evidence/` were deleted, including the contact sheets named above; the parent viewed `final_reimported_actions_contact_sheet.png` before deletion.
Provider downloads, refs, exports, textures, receipts and the two newest checkpoints per job were kept, so any sheet can be re-rendered from the installed animations.
