# Gorilla Heavy Infantry runtime audit

Date: 2026-09-08

Disposition: The bounded 3D runtime promotion and six-file PCM16 audio integration are implemented in the current workspace and pass the source-to-runtime hash, role-chain, material-stream, scale, consumer, cue-time, and shared-file-scope checks described below.
This disposition records current implementation evidence and parent acceptance within the authorized runtime-promotion scope; it does not establish live-game acceptance or complete the inherited counter work.

## Source-of-truth map

| Surface | Current evidence | Finding |
| --- | --- | --- |
| Selected payloads, action crosswalk, geometry, scale, and reimport receipts | `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/runtime_copy_manifest_20260908.json` | The manifest identifies nine selected files, five source actions starting at frame 0, five actual-byte reimport receipts, three mesh streams, 29 bones, 24,852 triangles, and entity scale 1.0 applied once. |
| Animation registry | `gfx/models/units/animation_012_africa_strange_forces.asset` | All five Gorilla animation types resolve to the selected runtime animation filenames. |
| Mesh and materials | `gfx/entities/012_africa_strange_forces.gfx` | `chaosx_gorilla_heavy_infantry_mesh` resolves to the selected mesh and binds both `Mesh_0.003` streams plus `Gorilla_Hammer` to the three selected BR29 DDS files. |
| Entity states | `gfx/entities/012_africa_strange_forces.asset` | Idle, move, attack, recovery, and death actions reach their intended state aliases; death is non-looping and terminal. |
| Common consumers | `common/units/012_africa_strange_forces.txt` and `common/scripted_effects/012_africa_action_effects.txt` | The sub-unit sprite and spawned division override both use `chaosx_gorilla_heavy_infantry`, which resolves to `chaosx_gorilla_heavy_infantry_entity`. |
| Contact reconciliation | `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/evidence/blender_repair_20260906/death_support_reconciliation.json` | All 151 selected source vertices reconcile, with maximum source-to-reimport position error `2.1757886664866485e-06`. |
| Audio payload and cues | `docs/assets/012_africa/models_3d/gorilla_heavy_infantry/audio/pcm16_copy_manifest_20260908.json`, `sound/012_africa_strange_forces_sound.asset`, and `sound/012_africa/units/gorilla_heavy_infantry/` | All six selected PCM16 files match source/runtime hashes and byte counts; the installed state cues match the selected runtime-cue ledger. |

## Payload verification

Every listed source file, runtime destination, SHA-256 value, and byte count matches the copy manifest.

| Runtime destination | SHA-256 |
| --- | --- |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_attack.anim` | `2570C45E371330B9D5EC2EBEEBF75AB7805A0C8D14BDD150EC910D224CF289A4` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_death.anim` | `A80A5E2FF64A2EB9B0538E02C83E615269E36C585368E5345DEDA10D834D777A` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry.mesh` | `27ECA3BE70D4AA92628C80E49C74DA647A9581CDD423BA4E07BA5B948A70B70D` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_br29_diffuse.dds` | `0B0F72A572C7B73D8A1B63CAF942EEE25888704878DEF43C3A590189CE076C3E` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_br29_normal.dds` | `ED9A05BE266D98C50C3BA53B829E33CB922F53F21C745E033BEA30128E779DB8` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_heavy_infantry_br29_specular.dds` | `63935BD65A57F4FBEE73EE4767F6C35AD1067CE8C296934A11825970F00586C1` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_idle.anim` | `D16FD842D9CEBCCB5CA246703FD94B3C79F095181A8652567C7CA0461BC0EF77` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_move.anim` | `E94862455824D802B8D3193CB17021CFB0A450AA94FF154446ED77136043F2BF` |
| `gfx/models/units/012_africa_gorilla_heavy_infantry/chaosx_gorilla_recovery.anim` | `5F8268C3043997B391B48AE27C493A62D531182D5742B659AC4DAC71AEA11BD1` |

The selected mesh hash makes the manifest's three-stream geometry proof applicable to runtime: `Mesh_0.003` contributes 20,000 and 4,656 triangles, while `Gorilla_Hammer` contributes 196 triangles, for 24,852 total.
The same source proof records a 29-bone rig, zero unweighted body vertices, and rigid hammer weighting to `hammer_R`.

## Action and state audit

| Authored role | Registry and mesh id | Runtime state consumers | Loop and transition result | Source timing evidence |
| --- | --- | --- | --- | --- |
| idle | `chaosx_gorilla_idle_animation` / `idle` | `idle` | Loops | Frames 0-60 at 30 FPS; starts at 0.0 seconds. |
| move | `chaosx_gorilla_move_animation` / `move` | `move`, `retreat` | Both states loop | Frames 0-48 at 30 FPS; starts at 0.0 seconds. |
| attack | `chaosx_gorilla_attack_animation` / `attack` | `attack`, `defend`, `support_attack` | Each state is one-shot and returns to idle | Frames 0-60 at 30 FPS; starts at 0.0 seconds and the authored hammer impact is frame 30, or 1.0 seconds. |
| recovery | `chaosx_gorilla_recovery_animation` / `recovery` | `training` | Loops | Frames 0-60 at 30 FPS; starts at 0.0 seconds. |
| death | `chaosx_gorilla_death_animation` / `death` | `death` | Non-looping with no `next_state` | Frames 0-60 at 30 FPS; starts at 0.0 seconds and settles terminally. |

Entity scale is `1.0` exactly once, matching the manifest's effective-runtime-height calculation.
The manifest contains one actual-byte reimport receipt and immutable reimport checkpoint hash for each of the five roles.
The parent accepted the hammer implementation and the 151-vertex contact reconciliation within this integration scope.

## Shared-file containment

The current diff of the two shared entity files changes only the Gorilla block.
`gfx/entities/012_africa_strange_forces.gfx` replaces one old Gorilla stream with the three manifest streams, and `gfx/entities/012_africa_strange_forces.asset` removes the Gorilla death fallback while adding the selected Gorilla-only sound cue times.
No Pan, Stone, Forest Giant, Oracle, Riverborn, or Plague Carrier block changed in those files.
The shared animation registry has no current diff and retains the five expected Gorilla registrations.

## Audio integration

All six copy sources and runtime destinations match `pcm16_copy_manifest_20260908.json` by SHA-256 and byte count.
Each file is mono 44.1 kHz signed PCM16, and all six loaded sound and soundeffect ids resolve through `sound/012_africa_strange_forces_sound.asset`.
The installed attack, defend, and support-attack cues use `0.979955`, placing the measured metal onset at the authored 1.0-second hammer impact.
The installed death cue uses `0.339864`, placing the measured chimp-vocal onset at the authored 0.4-second stagger; this is a vocalization cue and is not evidence of floor collision.
The training cue uses `0.984966`, placing its metal onset at the authored 1.0-second grip check.
Move triggers at state time `0.0` once per cycle as equipment rattle without a footstep-contact claim, while idle triggers at `0.0` with `trigger_once = yes`.
The sixth loaded sound is the separately invoked selection cue through `scoped_sound_effect = "chaosx_gorilla_heavy_infantry_select_sfx"`.
Runtime `ATTRIBUTION.md` records Pawel Fedurek et al. under CC BY 4.0 and Camshaft64 under CC BY-SA 4.0, including ShareAlike treatment for the metal derivatives.
No auditory review was performed in this audit; the chimp vocal and metal-rattle character remain inherited source limitations, and the movement sound is not represented as footsteps.

## Remaining companion dispositions

| Companion | Disposition | Evidence and blocker |
| --- | --- | --- |
| Audio | Implemented with audition limitation | Six PCM16 hashes, loaded definitions, selected cue seconds, selection invocation, and attribution pass; no auditory acceptance is claimed. |
| Counter | Unresolved pending parent or user acceptance of the inherited exception | `validation/counter_revalidation_2026-08-24.md` verifies the retained bytes and consumers but records `needs_user_review` because the source used chroma-key removal without evidence of a failed native-alpha generation attempt. |
| Live runtime | Outside agent validation scope | No live-game validation was performed or claimed; this does not block the implemented bounded 3D repair and audio integration. |

The copy manifest still labels runtime copying as parent-pending because it is immutable worker handoff evidence; the current filesystem hashes prove that the parent copy has since occurred.
No duplicate documents, superseded prompts, or additional contradictions were found within this bounded audit.

## Audit handoff

This audit created only `docs/plans/012_africa_plans/subagent_handoffs/2026-09-08_gorilla_runtime_audit.md`.
No gameplay, GFX, animation, mesh, texture, sound, counter, spreadsheet, or source-manifest file was edited by the auditor.
Meaningful checks included all nine model source/runtime hashes and sizes, all six PCM16 source/runtime hashes and sizes, explicit five-role registry-to-mesh-to-state tracing, selected audio cue times, three-stream triangle reconciliation, scale-count verification, common-consumer tracing, terminal-death inspection, five reimport-receipt checks, contact-reconciliation evidence, and a shared-file diff review.
Binary visual inspection and live-game validation were not repeated; the report preserves the parent's accepted hammer/contact review and states the remaining consumer limitations.
