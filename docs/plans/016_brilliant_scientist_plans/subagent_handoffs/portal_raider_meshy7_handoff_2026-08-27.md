# Portal Raider Meshy 7 handoff — 2026-08-27

## Outcome

Status: **blocked; fail closed**.

The deterministic provider/source/evidence package is at `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider/`. Meshy 7 produced an excellent generic retro-futurist raider with helmet/goggles/respirator, durable transit gear, teleportation pack, and a complete integrated two-hand/shoulder laser rifle. Meshy also supplied a humanoid rig and all nine required provider-authored motions. However, the integrated backpack deforms catastrophically during the genuine firing action under the provider weights and every usable locked-adapter automatic transfer mode. The model therefore has no accepted runtime `.mesh` or `.anim` exports and no reimport proof.

Do not wire this package as a completed unit model. No fallback motion, static action, semantic alias, transform-only action, procedural action, manual weapon attachment, or hand-authored replacement action was used.

The authoritative detailed package manifest is `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider/package_manifest.md`. Machine provider lineage is `provider/tasks/action_lineage.json`; phase evidence is `validation/action_phase_inspection.json`; Blender action preparation evidence is `blender/reports/action_prepare_summary.json`.

## Source and one-image lineage

- CC0 designed-art source: *Sci Fi Soldier and Guns* by DasBilligeAlien, `https://opengameart.org/content/sci-fi-soldier-and-guns`, direct file `https://opengameart.org/sites/default/files/marinestheydieforyoumarines.png`, retrieved 2026-08-27.
- Archived source: `refs/source/untouched.png`, SHA-256 `B704CC7286C3F76DC20A80D9DDEF44EADE350DA535E35B9DA64D02246A03F4DC`; non-shipping evidence.
- Sole approved Meshy input: `refs/original/meshy_input.png`, SHA-256 `40B4E7EAE15208322881408671A48204E4AB61FD4223200BC0F8377F8E243D84`.
- Native ImageGen prompt and source-to-refinement records are `refs/briefs/meshy_input_prompt.md`, `refs/source/provenance.json`, `refs/source/source_search.md`, and `evidence/reference_preflight.md`.
- Native transparency and a targeted transparency edit both returned opaque checkerboard pixels. The accepted image used the skill-owned chroma-key repair, retained real alpha, and passed the complete-rifle/hand/shoulder/muzzle gate.
- Parent approval was the 2026-08-27 instruction to proceed with the validated CC0 source and deterministic new root.

## Provider tasks, files, and credits

Initial balance was 140 credits. Total consumed was 67: image-to-3D 30, remesh 5, rig 5, and nine animations at 3 each (27). The rejected first direct rig attempt did not consume a rig charge. The final recorded expected balance was 73.

- Generation `01a042fd-0754-7040-9024-f429c6b841f2`: `portal_raider_generation.glb` SHA `BFD15BBB9CE2A75C258DE868C9E88B29AF72C5D012BB941D6C795745905D6AEB`; FBX SHA `ED28232A1290D775E38EC0F23D1979193EE896DC4B8944185907384591EA8C28`.
- Remesh `01a04309-ce59-7545-bdb0-fbf6a74c5dbe`: GLB SHA `6CAA6C37DF91E884F455825B11003000A72248E4B2CA4339A102D0000BE86EB4`; FBX SHA `DC4993F5AA56E7C24D768DC81A598F98617CCEF216E2EC9CD68FCB5CF41E830B`.
- Rig `01a0430e-8742-7619-bd3b-a64ea3601991`: GLB SHA `10535E28F2A334AC3318E88AD2B133DFF64E2A53C860128F4782EEF082708C25`; FBX SHA `BCAAF43C2B526C1FA0EB70B214D89E1A00510DA4C73439747B62CF5E817E50DA`.
- Idle `01a04312-c55a-77e4-8bf1-f7cbc34cf199`, action 0 `Idle`, accepted as a provider motion candidate only.
- Move `01a04313-6e62-7730-90a9-6fac50a4d676`, action 692 `walking_2_inplace`, accepted as a provider motion candidate only.
- Attack `01a04314-13fe-7842-9433-8290ec2849d9`, action 223 `Draw_and_Shoot_from_Back_1`, rejected for pack deformation despite genuine draw/aim/discharge/recoil/recovery motion.
- Defend `01a04315-229a-7aa2-901f-d4f433ff622d`, action 89 `Combat_Stance`, provider candidate blocked with the shared rig.
- Support attack `01a04316-6088-756a-ab90-509d3d966f4e`, action 234 `Walk_Forward_While_Shooting`, provider candidate blocked with the shared rig.
- Retreat `01a04317-0bc8-75a8-b952-14f483ec2dac`, action 685 `Walk_Backward_with_Gun_inplace`, provider candidate blocked with the shared rig.
- Portal arrival `01a04318-32dd-7958-9e8a-72b17e6513bf`, action 470 `Jumping_Down`, provider candidate with genuine descent/landing; blocked with the shared rig.
- Wounded `01a04318-e8bd-7ff9-98fc-78bbdf4fb45d`, action 177 `Gunshot_Reaction`, provider candidate blocked with the shared rig.
- Death `01a04319-9f6c-7c24-992a-8036cd944145`, action 183 `Shot_and_Fall_Backward`, provider candidate contains articulated collapse/impact/settling but is blocked with the shared rig.

The exact GLB/FBX paths, byte sizes, and SHA-256 values for every action are in `provider/tasks/action_lineage.json`. All nine were immediately downloaded and checksummed.

## Dependency and Blender evidence

- Meshy MCP: official `@meshy-ai/meshy-mcp-server` 0.4.0, git `d8c77d1cb897e345eb41d38b510b8391b1664346`; exact model `meshy-7`; MCP SDK 1.29.0.
- Blender: 5.1.2 build `ec6e62d40fa9`; adapter `chaosx_blender_hoi4` 1.10.14; live bridge socket 9876.
- `io_pdx_mesh`: 0.91.0, checksum-locked archive SHA `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Adapter health request: `b7506ffeec294e94913826bf692b0064`.
- Vanilla/source preparation request: `42951fb2f9ba499599d0619bc0cb4786`; static protected geometry request: `31c68d50c471493eafda3de372f73c63`.
- Four-nearest base request: `d06c33c302284d3fa198a10d6e7c10cf`; exact provider action import request: `3ec723ebea814bcdb43ffd336ad4ef16`.
- Nearest-face rejected request: `3eb93680a1e342178ea7d7d1e62e10eb`.
- Automatic bone-heat base request: `69245121d7804ec292c5993b193aa95f`; provider action import request: `f7b67fd214e4455b8a6e279aa3a8bf88`.
- All adapter receipts and worker outputs are preserved in `logs/adapter/`.

The repository adapter's `portal_raider` job override still points at the old shared root. Per parent instruction, this worker did not change the lock/config or gameplay. A temporary directory junction supplied the deterministic root to the verified adapter; it was removed after evidence finalization and is not part of the package/runtime boundary.

## Scale and vanilla crosswalk

The exact installed reference was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`; `polySurface106` was measured with collision-only geometry excluded. The entity precedent was `gfx/entities/units_infantry.asset#infantry_rifle_entity`, scale 0.8, with `-Y` forward and `+Z` up.

The imported vanilla source geometry measured `7.351824797689915`; the calibrated package mesh target was `7.3518242835`, giving effective runtime height `5.8814594268` at entity scale 0.8 applied exactly once. The protected 29,999-triangle candidate retained ground contact and passed scale persistence within `4.77e-7` model units.

## Exact rejection and export status

The ordinary provider-skin attack has the required semantic phases but stretches a backpack panel toward the rifle at frames 118, 145, and 177. Automatic recovery was restricted to allowed adapter operations:

- `four_nearest`: rejected; severe radial backpack stretching. Checkpoint `blender/checkpoints/attack_dualsource_four_nearest_action.blend` SHA `8CBDD40343D092999EC1D366C89C7DD556F3B76EB5EC0DFB0130FF834EF857C5`. Frame-145 proof `blender/previews/portal_raider_attack_dualsource_f145_right.png` SHA `6BAF7449FF80BA5F66D5BCDEBF2D668F831412273A95BF5338DF0C30FBCDAF62`.
- `bone_distance`: adapter resolved it to the same four-nearest deform-bone distance policy; rejected visually.
- `nearest_face_interpolated`: adapter failed closed on invalid barycentric coordinates at target vertex 58/source triangle 101896.
- `automatic_bone_heat`: zero unweighted vertices and four-influence cap, but the pack stretches across the torso into spikes at frames 145–177. Checkpoint `blender/checkpoints/attack_dualsource_automatic_bone_heat_action.blend` SHA `EAC8CDAFB116DB0698CFD0209307114EC51FC8FA19CF0BF33674743E9A303A8F`; frame-145 proof SHA `33FCE5A5DBBA6A3D5F321F7B323EA887B1618F01E4B37E69706AFA30AC0D689E`.

Because attack is a hard requirement and the same integrated rig/geometry is shared by all roles, no action was promoted to runtime acceptance. No `.mesh` or `.anim` file exists. Export-coordinate conversion, final DDS model texture production, PDX export, and mesh+animation reimport were deliberately skipped. There are no export/reimport hashes to report.

## Sourced audio

The complete licensed generic audio package was copied with originals and transformation records into `evidence/audio/`. `licensing/source_ledger.md` records the exact Internet source pages and direct downloads for selection, six movement contacts, electrical idle, laser attack, metal impact, teleport arrival, and power-failure death. Licenses are CC0 except the idle hum (CC BY 4.0, Hansjörg Malthaner/Varkalandar) and death sound (CC BY 3.0, OptimusDu, Cough-E, Little Robot Sound Factory). `audio_manifest.md` records every original/derived checksum and the FFmpeg mono 44.1 kHz PCM normalization recipe.

Exact runtime sync is blocked with the action package. Candidate-only inspection placed attack discharge near frame 145 at 30 FPS and support discharge near frame 50, but these are not runtime bindings. The full copy receipt and limitation are `evidence/audio/copy_provenance.md`.

## Bespoke counter

The complete bespoke counter package was copied into `evidence/counter/`, including original/alpha PNGs, processed two-frame strips, DDS outputs, roundtrip proofs, contact sheet, manifest, and `gfx_handoff.md`. Required tokens are `unit_portal_raider_icon` and `onmap_unit_portal_raider_icon`.

The exact installed definitions were inspected in `interface/subuniticons.gfx`. The reference DDS files were the large `unit_infantry_icon.dds` and small `onmap_unit_infantry_icon.dds`; matching skill-local families were `units/land/counters_large` and `units/land/map_counters`. The package uses the sampled vanilla dominant green `(73,106,73)` and highlight anchors `(100,128,100)` / `(116,141,116)`, with the required green and selected-state frame behavior.

Counter DDS evidence checksums: large `4236DF5183605AF540D44339EED96F29B2B59A40D9F82E1472C5178963EF920E`; map `FB009C5EEED40C1AAD867D15C066422CB142AA24DC2C38D7311857BFA284D85E`. Parent-owned GFX/runtime validation remains outside this 3D worker.

## Parent runtime boundary and remaining work

Stable proposed identifiers remain `portal_raider_mesh`, `portal_raider_entity`, and `portal_raider_*`, with `fires_in_combat = yes`. The intended consumer boundary is existing Event 016 `portal_raider` and Event 019 provider-509.

This worker edited no gameplay, entity, `.asset`, `.gfx`, localisation, event, decision, focus, country, history, AI, spreadsheet, or sound-definition file. Live in-game validation is skipped and cannot be inferred from provider or Blender evidence.

To resume, obtain a provider-authored firearm-bearing rig whose integrated backpack and rifle deform correctly through genuine aim/discharge/recoil/recovery and articulated death, or an explicitly user-approved professional skeletal source. The resumed Blender work may only retarget, clean, ground/root-correct, scale, bake, export, and reimport the approved source.
