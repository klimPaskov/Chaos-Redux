# Alien Infantry firearm recovery V11 handoff

> Superseded by the Meshy V13 package and static runtime promotion recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`; retain this file for V11 rejection evidence only.

Date: 2026-08-26

Status: **blocked — a new Meshy 7 raw model passes two-hand firearm contact, but every provider remesh breaks topology or exceeds the rig ceiling; no new rig, firing actions, or muzzle locator can be produced**.

## Scope and immutable source

This recovery owned only `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/` plus this handoff. Gameplay, entity, GFX, particle, light, sound-definition, and event wiring were not edited.

The immutable user-supplied source remains `refs/source/user_supplied_alien_reference.png`, SHA-256 `17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F`. It was not modified and was not used as the final V11 provider input.

## Dependency and route verification

- Official `@meshy-ai/meshy-mcp-server` 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK 1.29.0, compatibility revision `meshy-7-v5`.
- Exact generation identifier: `meshy-7`; one local `file_path` input only.
- Blender 5.1.2, build commit `ec6e62d40fa9`.
- Repository adapter `chaosx_blender_hoi4` 1.10.14.
- io_pdx_mesh 0.91.0, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Adapter health request `42a2ef4c1e4f4a6394969a10c830beaf` passed after the lock-selected hidden Blender bridge was started on `127.0.0.1:9876`.
- Vanilla calibration: `gfx/models/units/western_european_infantry.mesh` and `gfx/entities/units_infantry.asset#infantry_rifle_entity`; target source height 7.3518242835, entity scale 0.8 exactly once, effective runtime height 5.8814594268, forward -Y, up +Z.

## V10 support-action recovery

Meshy action 234 `Walk_Forward_While_Shooting` was applied to the existing V10 rig as a materially different support-fire attempt. Task `01a03d2c-6a68-7c9b-90af-5e79adc4f75c` consumed 3 credits. FBX SHA-256 is `DDB3E6004A3D0DB38E59415C293AE0F7D0871F1A7F7F719D675C77FA032158C2`.

Locked-adapter review sampled frames 1, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, and 99. Trigger contact is absent, support contact is absent, and the firearm is fixed diagonally across the back/shoulder. Aim, discharge, recoil, and recovery are all absent. The 24-bone rig contains no firearm or muzzle locator. This is a genuine rejection, not a semantic-name judgment.

## Prepared source and parent approval

Native ImageGen created a source-informed derivative. The first one-hand candidate was rejected at parent review because the left/support hand was free. A further faithful edit created a two-hand low-ready grip. The opaque ImageGen source SHA-256 is `360E0496BA9EB3F817A8052DE4D8B3E1C75BB98690BFCEA15A814FF4589B1756`; it baked a checkerboard, so installed `rembg` 2.0.61 was used as the documented fallback after native-alpha edits failed.

The exact approved provider input is `refs/original/meshy_input_v11_two_hand_firearm.png`, SHA-256 `CFF2E684F0D7D50A01084CEA76F2BA22CC4CF11BEB5D48AD829AD733FA2976D1`. It is 1024x1536 RGBA with alpha 0-255 and zero-alpha corners. It preserves alien identity, uniform, boots, one ray pistol, right trigger-hand grip, left support-hand contact, complete barrel, and unobstructed circular muzzle. Pose mode is `two_hand_low_ready`; a T/A pose was not forced because it would break firearm contact. Parent approval covered provider work only.

Exact prompts, rejected derivatives, checksums, comparison, and alpha checks are in `evidence/imagegen/v11_firearm_recovery/preparation.md`.

## Meshy 7 lineage and credits

Observed live balance was 255 before the V10 support action, 228 immediately before V11 generation, 198 before the first remesh, 163 before the second remesh, 158 before the quad remesh, and 153 at closure. Other concurrent provider work changed the shared balance between this worker's checks; this worker consumed exactly 48 credits:

- V10 action 234: 3 credits.
- V11 Meshy 7 generation: 30 credits.
- Three V11 remesh attempts: 5 credits each, 15 total.
- V11 rig/animation: 0 credits.

Generation task `01a03d3b-927e-72fc-99fc-b260df1dc178` used one exact local image, `ai_model=meshy-7`, triangle topology, PBR textures, lighting removal, no image enhancement, and no provider pose conversion. The GLB was downloaded immediately to `provider/downloads/generation_firearm_recovery_v11_model.glb`, 64,429,320 bytes, SHA-256 `4C9349EE589DC5DE5E3BF633946F23E31BADB8572A370BAA7F738895FFB64D3F`, with base-color, metallic, roughness, and normal maps.

Adapter request `93e2312f9e694be685f9e47d71e9473b` passes the raw contact gate from seven views. Right trigger hand, left support hand, weapon body, and muzzle remain continuous. The raw model is 1,577,348 triangles / 817,649 vertices with 57,512 loose boundary edges, so it is above the Meshy rig ceiling and not runtime-ready.

The provider remesh results are all rejected:

| Task | Request | Result | Adapter evidence |
|---|---:|---|---|
| `01a03d40-48d2-735d-b087-a328ecfc2c7c` | 100k triangle | 101,683 triangles; SHA `206974D2...` | Request `5c03156aa9324edaba16e551d253dde8`; 59,507 loose edges; severe visible breakup |
| `01a03d44-1037-7422-b378-17a3ea098c2e` | 299k triangle | 302,019 triangles; SHA `A530793D...` | Request `0bc21eb0d6394c22885be628b45a4d59`; 111,943 loose edges; perforated; above rig ceiling |
| `01a03d48-6562-7571-95f1-5eb38dfa20b0` | 250k quad | 497,610 triangles; SHA `9FD0E97B...` | Request `7bd820f38ad84dabab1cdb47bc6436a9`; 74,264 loose edges, 1,991 boundary components, 150 branched components, 9 degenerates; above rig ceiling |

No rejected remesh was rigged. Local repair or decimation cannot be uploaded into the locked Meshy rig route, and no manual weapon attachment or locally authored replacement action was attempted.

## Licensed package and locator audit

The existing Quaternius Universal Animation Library Standard remains the only audited free package with genuine pistol aim/discharge/recoil/recovery and retained integrated-pistol contact. It is CC0 and retargetable; archive SHA-256 is `18FF1A7215F4852B320203E8AAF02A1578B5C8EEF9027FBAEDFCEDC7B85A3AC2`. `Pistol_Shoot` has verified frame 6 discharge and recovery, but it has no independent support-fire action and no firearm or muzzle locator.

The official source and license are `https://quaternius.com/packs/universalanimationlibrary.html`; the page states FBX/GLB/Blend, universal humanoid retargeting, combat/gun coverage, and CC0.

The official CC0 Quaternius Animated Guns Pack at `https://quaternius.com/packs/animatedguns.html` contains six animated firearm props in FBX/OBJ/Blend. It does not provide retargetable humanoid aim/recoil/support-fire motion and cannot supply a locator for the already integrated alien pistol without forbidden weapon replacement/manual attachment. It was not downloaded.

Pichuliru Flat Guns West at `https://pichuliru.itch.io/cc0-flat-guns-west` advertises rigged gun props and attachment bones, but its page conflicts between CC0 prose and an itch.io CC BY 4.0 asset-license field. It also supplies separate props rather than humanoid firearm motion. It was not downloaded or used.

No package found provides all required pieces: usable source format, unambiguous compatible license, genuine humanoid aim/fire/recoil/recovery, distinct support fire, retarget compatibility, and a stable locator belonging to this integrated pistol. A locator from another gun prop is not equivalent and cannot be inferred or transplanted.

## Export, synchronization, sound, and counter state

No V11 `.mesh` or `.anim` was exported because no accepted provider rig/action exists. Therefore no V11 io_pdx_mesh reimport proof, packed PDX material promotion, muzzle particle/light binding, discharge frame, laser sound synchronization, or selected-source-to-runtime hash exists.

The inherited sourced-audio and bespoke-counter package state is unchanged. This recovery did not create, synthesize, replace, or wire audio and did not edit counter art or GFX. The missing firearm/muzzle synchronization prevents final model-package completion regardless of those inherited surfaces.

## Changed and created files

Tracked documentation:

- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/manifest.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/handoff.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/history.jsonl`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/evidence/imagegen/v11_firearm_recovery/preparation.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/rejections/firearm_recovery_v11.md`
- this handoff

Ignored job artifacts preserved locally include the approved/refused ImageGen derivatives, four downloaded provider GLBs plus texture folders, action 234 FBX, adapter source blends, adapter logs, and all V11 review previews named in the rejection report. No API key or signed URL is recorded.

## Exact blockers and next permitted recovery

Blocked requirements: `alien_infantry_laser_attack`, distinct `alien_infantry_support_attack`, stable model-compatible muzzle locator, discharge frame/effect/sound synchronization, final `.mesh`, complete `.anim` set, packed materials, and current export/reimport proof.

Remaining live Meshy balance at closure: 153 credits.

The next permitted recovery is a future Meshy provider capability that can remesh this accepted raw-contact generation into a closed sub-300k humanoid mesh without breaking the firearm, followed by provider rigging and genuinely verified firearm actions with a provider-exposed muzzle node. Alternatively, the user must explicitly approve a professional package that includes both compatible humanoid firearm motion and a locator solution for the accepted integrated weapon. Manual Blender action authoring, transform-only motion, inferred muzzle points, weapon replacement, and manual attachment remain forbidden.

No simplification or fallback was promoted. Parent-owned runtime wiring and in-game validation remain untouched.
