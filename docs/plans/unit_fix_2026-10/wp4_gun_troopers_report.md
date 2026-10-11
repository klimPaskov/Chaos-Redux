# WP4 gun troopers repair report

Status: incomplete.

## Takeover review, 11 October 2026

The user authorized finishing the stopped agent's WP4 work, preserving WP5/WP6 ownership, using existing licensed audio only, and committing each model separately.
The current source review below supersedes older firing-tranche statements where explicitly identified; mesh, material, grip and action repairs remain separate open requirements.

### Assassin Cadre, Shadow Company and Master Assassin

The inherited three stacked MG emitters per burst are replaced by one compact three-shot emitter and one finite smoke event per burst.
Attack, support attack and defend retain three, four and three burst starts respectively; both clones inherit the base entity's state events.
The dedicated `chaosx_039_smg_muzzle_particle` uses the installed vanilla MG textures, with internal flame starts at 0.0, 0.1 and 0.2 seconds and a maximum source-derived visible lifetime of 0.35 seconds.
Its registry scale is 0.15; the maximum nominal glow size is 1.5 source units against the Cadre's measured head spans of approximately 0.91, 0.93 and 1.16 units.
These are emitter/mesh-source measurements, not rendered orange-pixel or in-game area measurements.

The reviewed archived three-transient gunshot and two death takes are wired through the Event 039 infantry-family sound definitions, with their CC BY 3.0 and CC0 notices shipped beside the WAVs.
The three waveform hashes match the preserved accepted source receipts and pass fresh short-cue format/level checks.
No sound was downloaded or synthesized.
The mechanized definitions are separated into their own Event 039 sound file without changing identifiers or category membership, so they can be reviewed and committed with that model.

Changed runtime paths for this family are `gfx/entities/chaosx_assassin_cadre.asset`, `gfx/entities/chaosx_039_unit_particles.gfx`, `gfx/particles/039_murder_mystery/smg_muzzle.asset`, `sound/039_murder_mystery_units_sound.asset`, and the three WAVs and attribution under `sound/039_murder_mystery/units/`.
Evidence is retained in `.tmp/unit_takeover_wp4/`: `smg_particle_derivation.json`, `sound_partition_parity.json`, `audio_receipt_verification.json`, and the before/after inventory, event crosswalk and lint files.
The offline Entity modding Event section, lines 139-150, revision `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`, and installed vanilla `gfx/particles/infantry/mg_muzzle.asset`, SHA-256 `875c1d7424509278ee48dd3d8f29f92eb1162f9922a1f995a6ba5cb05a307420`, supply the event and particle precedents.
The broad MCP source lookup stalled and was stopped; direct vanilla source inspection supplied that evidence instead.

Remaining: the measured cartridge locator, coherent body/weapon atlases and material masks, topology repair, final grip and recoil/contact review, and fresh model export/reimport.
The firing-source repair does not close those model requirements or claim live-game validation.
No requested functionality was removed in this family tranche; model requirements are retained as unfinished work.
Meshy credits spent on this firing tranche: 0.

### Silent Guard

Attack, support attack and defend use two, two and one compact SMG burst emissions, each paired with one smoke event and the recorded infantry-family burst cue.
The two-take death pool fires at 0.3 seconds.
This model consumes the Cadre commit's shared 0.35-second particle and licensed audio definitions; its own changed runtime file is `gfx/entities/chaosx_silent_guard.asset`.
Source resolution and inherited timing checks are retained in the same WP4 event crosswalk and lint evidence.
Coat deformation, low-ready idle, recoil, UVs/materials and topology remain open, with no model-byte replacement or live validation in this source tranche.
Meshy credits spent: 0.

### Clone Infantry

Attack discharges at 0.75 seconds and ejects at 1.5833 seconds; support attack and defend discharge at 1.0 second and eject at 1.8333 seconds.
The decoded 24 FPS actions and existing `muzzle`/`cartridge` locators support these frame-to-time bindings, and attack/support continue into the firing defend state.
The single 0.45-second Lee-Enfield report is the reviewed CC0 source derivative, SHA-256 `42f23c496111944c41489a0d295750808777a216f3aa9dc48ae1170962746bfd`, with its source notice in `sound/shared_clone_system/clone_infantry/WP4_ATTRIBUTION.md`.
This removes the missing defend effects and obsolete report/casing times while preserving the current mesh and actions.
Aim/stock/elbow contacts, rifle/body materials, idle and transition repairs remain required; numerical event placement does not establish those pose requirements.
The complete source-derived shout is 0.791859 seconds at -3 dBFS; wound and death fades retain their captured -6.677 and -7.667 dBFS peaks.
The 0.9-second licensed body-fall cue is wired at 1.5 seconds from the preserved authored frame-37 marker at 24 FPS.
The marker's selected death-action SHA-256 matches the installed action; this establishes source timing, not a fresh anatomical contact observation.
Exact source, waveform, transformation, destination-hash and playback-rate evidence is retained in `docs/assets/shared_clone_system/models_3d/clone_infantry/evidence/wp4_audio_takeover/`.
Spoken-word content and in-game playback were not audited through the unavailable audio-input route.
Meshy credits spent on this source tranche: 0.

### Portal Raider

The four laser events retain their authored times and use finite particle lifecycles.
Idle and guard start one source-bound electrical loop with `trigger_once`, `loop = yes` and `max_audible = 1`.
The one-second archived-source derivative measures -20 LUFS and a 2.58 dB inner head/tail RMS difference; source and installed hashes are recorded in `sound/portal_raider/WP4_ATTRIBUTION.md`.
The ray uses the verified existing source stretched to 0.6 seconds with pitch fixed and a 60 ms terminal fade, played at the requested volume of 0.75.
The rejected early-decay candidate is not installed; the selected waveform retains its body through the extended clip and fits the 0.916667-second minimum interval between support shots.
Six original footstep takes have source-derived edge fades at -6 dBFS, and death combines the existing power-down sound with a licensed human grunt.
The first boot-step derivative is an explicitly shared Portal/Alien pool member, not an independent new take.
Per-file provenance, exact transformations, waveforms, copies and cue-rate checks are retained in `docs/assets/shared_portal_raider_system/models_3d/portal_raider/evidence/wp4_audio_takeover/`.
Live state-exit playback and perceived timbre remain unverified.

The selected September 6 weapon-free provider body/maps and `wf_export2.blend` are missing from the current job, local scratch, archive and exact-hash LFS checks.
The runtime 45-bone mesh and matching native installed-byte reimport remain available.
The older shared-job Meshy 6 maps belong to a rejected predecessor and must not be applied to this body's UVs.
The requested original-provider normal repack is therefore blocked by those missing source maps; current-geometry action and material review can proceed independently.
Meshy credits spent on this source tranche: 0.

### Alien Infantry

The ticket-permitted idle-hum removal and finite laser effects are retained.
The existing CC0 bart laser sound is shortened from 1.2 to 0.9 seconds and layered with the archived CC0 Kenney `laserSmall_000` tonal cue.
Both originals, the source-bound preimage and installed derivative are verified in the takeover audio receipts and `sound/shared_alien_system/alien_infantry/WP4_ATTRIBUTION.md`.
At the slowest configured playback rate of 0.97, its 0.92784-second duration fits the 1.066667-second interval between support shots.
The original shortened-only candidate retained a 0.988637 correlation over its first 0.78 seconds; the selected layered follow-up supersedes that candidate, so this is not a correlation claim about the final mix.
Movement uses the licensed Gbox boot-step source at -6 dBFS, explicitly shared with Portal Raider's first take; impact has source-derived edge fades at -6 dBFS.
Exact transformations, source licenses, waveforms, installed hashes and cue-rate checks are retained in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/wp4_audio_takeover/`.
The existing recordings were edited and mixed without sound downloads or agent synthesis; their original creators' production methods are not established by this review.
Body/pistol materials and scan/idle/recoil remain open.
The selected provider normal itself has masked X/Y standard deviations of only 2.90/3.07; an unamplified 512-pixel repack measures 1.95/2.03 and cannot satisfy the 15-35 detail gate.
The source-to-current UV triangle comparison matches 49,784 of 52,098 triangles; modified regions and a meaningful detail-bake source still require native review.
No auditory or live-game acceptance is claimed; the parent audio input route reported that this model cannot consume audio.
Meshy credits spent on this source tranche: 0.

### Autonomous Robot

Attack and support attack each start one finite sustained emitter and one recorded burst per gun, preserving the 0.125-second left/right offset.
Defend starts one short burst per gun at 0.75 and 2.75 seconds.
The sustained emitter contains eleven flashes at 0.25-second intervals and ends at 2.6 seconds; the short emitter contains four flashes and ends at 0.6 seconds.
Each gun receives one reduced-scale smoke emitter rather than the original per-shot smoke stack.
The two intentionally overlapping gun recordings are limited to two audible sources at volume 0.36.
The new emitter files and registry reuse installed vanilla texture assets; source derivation and exact timings are in `robot_particle_derivation.json` and the final firing crosswalk.

The source-approved footfall is 0.2 seconds, or 0.20833 seconds at the slowest configured rate, below the 0.291667-second retreat event gap.
The second casing take is shortened to 0.7 seconds, below its 0.75-second gap.
Both destination hashes match the reviewed candidates; source licenses, transformations and hashes ship in the robot's `WP4_ATTRIBUTION.md`.
The final source lint clears those specific overlaps while retaining the intentional paired-gun polyphony and the generic lint's smoke-classification limitations.
No model, skeleton, weights, actions or maps changed in this source tranche; topology, materials, sensor/servo motion and anatomical contacts remain required.
Rendered smoke size, orange-pixel area and in-game playback are unmeasured.
Meshy credits spent on this source tranche: 0.

### Mechanized Assassin

The plan's explicitly permitted single-burst path is retained: one timed barrel flash/report at 0.7667 seconds in attack, 0.9667 in support attack and 0.2333 in defend.
Attack/support reference the five installed vanilla MG takes; defend references the four takes that fit its 50-frame cycle, without random onset delay.
The dedicated destruction cue plays at 0.1 seconds and retains the archived source's complete 1.36-second decay, with no fabricated extension to the ticket's approximate two seconds.
Its licensed source, exact derivative hash and processing are in `sound/039_murder_mystery/units/mechanized_assassin/ATTRIBUTION.md`; definitions reside in `sound/039_murder_mystery_mechanized_sound.asset`.
Definition and Effects-category membership are unchanged by the sound-file partition.

The source choice does not repair the two existing chassis recoil troughs at attack frames 24/48 and support frames 30/60.
That motion still needs deliberate reconciliation with the accepted one-burst path, alongside hull/turret/wheel UVs, materials, topology and visible scan/traverse work.
No final recoil synchronization or model completion is claimed.
Meshy credits spent on this source tranche: 0.

Acceptance basis: the user's assignment of all nine WP4 models and every ticket in `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md`.
The implemented firing/audio tranche is documented in `wp4_firing_audio_tranche.md`; geometry, materials, rig/actions and filmed acceptance remain required.

## Runtime changes and per-model findings

| Model | Found in installed bytes | Implemented | Still required |
|---|---|---|---|
| Assassin Cadre | 9/12/9 flashes in attack/support/defend; no cartridge locator; fragment atlas and failed topology/action gates | 3/4/3 finite flash emissions, one smoke and dry recorded cue per burst; two recorded death takes at 0.3 s | Measured ejection locator, <60-island UV rebake with >90% coverage, holes/winding, class-specific specular, planted rear foot and recoil |
| Shadow Company | Shares Cadre mesh/actions/events; slate-blue dye retains its fragment atlas | Inherits corrected bursts, death pool and timing | Derive the slate-blue diffuse after the Cadre rebake; verify occupied texels and inheritance |
| Master Assassin | Shares Cadre mesh/actions/events; oxblood dye retains its fragment atlas | Inherits corrected bursts, death pool and timing | Derive the oxblood diffuse after the Cadre rebake; verify occupied texels and inheritance |
| Silent Guard | 6/6/3 flashes; no cartridge locator; low-contrast diffuse and coat deformation | 2/2/1 finite flashes with smoke and sourced burst/death audio | UV/body/SMG rebake, holes/winding, wool/leather/steel masks, deliberate skirt weights, low-ready idle and recoil |
| Mechanized Assassin | Two reports per state against one continuous emitter; defend shorter than one vanilla take | One timed barrel flash/report per cycle; four shorter vanilla takes in defend; 1.36 s recorded destruction cue at 0.1 s | Hull/turret/wheel UV/material rebake, holes, scan/settle and traverse actions; optional engine loop |
| Clone Infantry | No particles; silent defend; obsolete firing times; inherited simulated rifle cue | Timed shots/casings and defend chaining; recorded rifle report, full source shout, level-preserving voice fades and frame-37 landing cue | Aim/grip/shoulder pocket, entry/recovery and idle, rifle UV/normal/materials, sleeve values and physical-contact review |
| Portal Raider | Dark diffuse, weak normal detail, stale rejected-candidate docs and one-shot idle | Finite laser effects, electrical idle/guard loop, 0.6-second ray, faded six-take footsteps and human-layered death | Missing selected provider maps; source-to-current-UV proof, recoil/second attack, low-ready idle and rifle normals |
| Alien Infantry | Frozen idle, weak normals/flat pistol maps, one-shot vehicle hum and overlapping 1.2 s laser | Finite laser particles; permitted hum removal; 0.9 s source-layered tonal laser, licensed boot step and faded impact | Body grade/normal and proper pistol UV/materials; breathing/scan/recoil; modified UV/tangent review |
| Autonomous Robot | 22 flash/smoke/report emissions in attack/support, 8 in defend; 28 non-manifold edges; faceting/flat gun maps and long audio tails | Two finite gun emissions/cues per burst cycle; 2.6 s sustained and 0.6 s braced recorded bursts at volume 0.36/max two; 2 s wreck blast | Winding/topology/smooth normals and weapon material rebake; sensor/servo idle; short footfall and casing fades/tail fixes |

The four 039 infantry consumers share a declared recorded burst/death pool.
The two robot guns share a declared recorded weapon pool and retain their first-discharge offsets.
The mechanized destruction file preserves its complete 1.36 s archived decay rather than fabricating the ticket's approximate two-second length.
The first tail-heavy SMG candidate and a loud first death take failed the unchanged RMS gates and were not installed.
Original archives and rejected candidates remain evidence.

## Model measurements before and after firing/audio changes

`wp4_evidence/model_baseline_compact.json` retains exact mesh/action hashes, parser revision and measurements.
`mesh_action_integrity_after_firing.json` confirms all nine registrations retain their captured mesh and action hashes.
These 0.0005-tolerance measurements are unchanged; the complete geometry gate also checks other requested weld tolerances, winding and degeneracy.
A zero at one tolerance does not establish the full gate.

| Model | Boundary/non-manifold edges before -> current | Geometry gate | Structural action gates passed/registered |
|---|---|---|---|
| Assassin Cadre | 63/66 -> 63/66 | blocked | 1/8 |
| Shadow Company | 63/66 -> 63/66 | blocked | 1/8 |
| Master Assassin | 63/66 -> 63/66 | blocked | 1/8 |
| Silent Guard | 75/59 -> 75/59 | blocked | 1/8 |
| Mechanized Assassin | 207/283 -> 207/283 | blocked | 6/8 |
| Clone Infantry | 0/0 -> 0/0 | pass | 2/9 |
| Portal Raider | 0/0 -> 0/0 | pass | 8/10 |
| Alien Infantry | 0/0 -> 0/0 | blocked across requested tolerances | 4/7 |
| Autonomous Robot | 0/28 -> 0/28 | blocked | 2/8 |

Seven unique meshes serve nine registrations.
Seven registrations remain geometry-blocked; 26/74 registered actions pass structural checks and 48 remain blocked.
Structural checks do not establish readable idle, grip, recoil, grounded stride or action semantics.
No completed model reconstruction, action export or reimport is asserted by this firing/audio tranche.
Shadow Company and Master Assassin inherit scale 0.8; the earlier inventory default of 1 for an absent clone field is superseded by the effective entity review.

## Section 3 delivery baseline

The shared owner already installed 512-pixel BC1/BC3 maps with complete ten-level mips, occupancy dilation, packed-normal cleanup and removal/archive of nine unused legacy DDS files.
The obsolete alien/robot/clone triplets are absent and the current inventory finds no unreferenced files in those three folders.
Those earlier deliveries are baseline facts, not newly produced WP4 repairs.
`pipeline_report.md`, `per_model_delivery_metrics.json` and their install manifests retain those facts.
The requested `unit_s3_report.md` is absent and is recorded as an input-path gap.
Material-class provenance, weak normal detail and fragmented atlases remain unresolved; compression does not establish material acceptance.
The model worker's source/UV comparisons and independently prepared candidates belong in `wp4_models_handoff.md`.

## Evidence and validation limits

`wp4_evidence/references.json` retains offline wiki and installed vanilla source paths, spans and hashes.
The inherited 6 October session lacked HOI4 reference routes; the 11 October takeover successfully read the offline reference context, search and cited Event section.
The broad source lookup stalled, so exact installed vanilla files were inspected directly.
The genuine pre-edit entity baseline uses preserved blocks with clone inheritance.
Current locators, cue definitions, copied WAV hashes, category registration and state timing are reviewed in `.tmp/unit_takeover_wp4/` inventories, crosswalks and source audits.
The shared lint's smoke-as-flash and intentional paired flash/smoke overlap findings remain visible beside the genuine overlaps.
The two robot gun cues intentionally overlap; their quieter two-source cap is the accepted weapon-pair design.

`wp4_audio_evidence/install/accepted_tranche*.json` retains runtime preimages, candidate/source/report hashes, mastering checks and destination verification.
Runtime attribution retains creators, terms, URLs and actual edits.
Held recordings and take-coverage gaps remain in `wp4_gun_troopers_audio_needs.md` and `wp4_audio_handoff.md`.
Final visible flash area/duration, material/deformation, authored contacts and live playback are independent acceptance requirements.

## Authoring blocker and omissions

Blender 5.2.2, adapter 1.11.0 and io_pdx 0.91 are the locked production stack.
WP5 holds the machine-wide Blender lease during this takeover; its scene and processes are preserved while independent source and provider work proceeds.
The recovered current model selections are recorded in `.tmp/unit_takeover_wp4_models/intake_inventory.json`.
Geometry, UV, weights, idle, recoil and action repairs need the verified authoring route; repository code may not synthesize replacements.
The parent coordinates lease acquisition through `%TEMP%/chaosx_blender.lock`; no user confirmation or game launch is required.
Every pending model row remains required, and WP4 is incomplete.
No substitute model or unverified recording is represented as an accepted final.
No workbook or exported catalog CSV was edited.

## Decisions and orchestrator checks

Event 039: `docs/plans/039_murder_mystery_plans/agent_decisions_2026-10-05.md`.
Event 016/shared consumers: `docs/plans/016_brilliant_scientist_plans/agent_decisions_2026-10-05.md` and `wp4_agent_decisions_2026-10-05.md`.
CXT setup, state actions, expected visible/audio outcomes and stationary capture checks are in `wp4_firing_audio_tranche.md`.
All nine models need re-filming after the remaining requirements: Assassin Cadre, Shadow Company, Master Assassin, Silent Guard, Mechanized Assassin, Clone Infantry, Portal Raider, Alien Infantry and Autonomous Robot.
Film at least two cycles per state with the crop locked to the entity's combat position, retaining zoom/audio settings.

Skills used: chaos-redux-3d-model-pipeline, chaos-redux-event-assets, chaos-redux-subagents and chaos-redux-shared-git-commit.
Shared pipeline/skill files remain owned by their tools worker; WP4 records the float pre-attenuation lesson in task evidence without rewriting them.
