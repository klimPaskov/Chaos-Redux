# Autonomous Robot 3D recovery audit

Date: 2026-08-27

Owner: `chaosx_3d_model_pipeline`

Status: **blocked; fail closed**.

The installed generic Autonomous Robot mesh, rig, textures, actions, audio, and counters were audited without generating or replacing the base model. No gameplay, entity, GFX, sound-definition, localisation, or runtime asset was edited. The existing attack, defend, support-attack, and retreat actions do not meet the current semantic-action standard, so this package must not be represented as animation-complete.

## Scope and cost

- Deterministic job root: `docs/assets/shared_robot_system/models_3d/autonomous_robot`.
- Runtime model root inspected read-only: `gfx/models/units/autonomous_robot`.
- Existing model identity was preserved. No ImageGen, image-to-3D, retexture, remesh, rig, conversion, animation generation, manual motion, attachment, weighting, or runtime wiring operation was performed.
- Live Meshy balance observed: **13 credits**.
- Recovery spend in this pass: **0 credits**.
- One no-charge capability probe attempted animation action `690` against historic rig task `01a0043b-dc34-7795-a542-7d9657a3820e`; the provider returned `Resource not found`. No task or response ID was created or exposed, and the balance remained 13.
- Further paid calls were stopped under the parent coordination hold.
- Historic attributable package spend remains 63 credits, as recorded in `validation/credit_ledger.md`.

## Dependency and route evidence

The `MESHY_API_KEY` process-environment hard gate passed before repository intake. `python .tools/3d_pipeline/verify_environment.py --probe-meshy` returned no findings and wrote `.tools/3d_pipeline/reports/environment_report.json`.

| Surface | Verified value |
| --- | --- |
| Official Meshy MCP | `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d89ca7f2d032a90c25aabf895763b23b99d`, SDK `1.29.0` |
| Locked Meshy generation model | exact identifier `meshy-7` |
| Blender | `5.1.2`, build `ec6e62d40fa9` |
| Blender HOI4 adapter | `chaosx_blender_hoi4` `1.10.14` |
| Adapter health request | `3c513aa9f7784ccb817851ac2a18b58e` |
| Adapter bridge | `127.0.0.1:9876` listening |
| io_pdx_mesh | `0.91.0`, locked checksum `A683F2079017E5295F088324ED4ED60E606F547A35D3AB7BA93E18E3684AF7C2` |

Lock-file SHA-256 values at audit time:

- `.tools/3d_pipeline/config/dependencies.lock.json`: `c27768297fb7ad5acc9c555e7c83dc77856908e2c628bf16d9a420095c64266a`
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: `e45fe80f3b8ac49a365ea2d4221e82e969ae55279639f817bb6fa75407d1c233`
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: `4bc97ca0b07580f5aa04b49e7b9fbd1c07ec88df5c4d56cd3ba8846e630117ab`
- `.tools/3d_pipeline/reports/environment_report.json`: `8ab8a91bed9ad3aac98170ca684278d70cab6f5e87c28164244bbe6ee5e94724`

The historic package metadata is stale relative to the current lock: `manifest.json` records a Meshy 6 base-generation task and adapter `1.2.2`. This audit did not regenerate the model because the parent explicitly required reuse of the installed package and prohibited a new base model.

## Model, rig, material, and scale evidence

- Accepted remesh task: `01a00422-4450-762d-8fbd-db589e6e9bf9`.
- Historic provider rig task: `01a0043b-dc34-7795-a542-7d9657a3820e`.
- Final mesh: 29,971 triangles, 24 bones, no recorded degenerates or non-manifold edges, no negative-scale objects, no zero-weight vertices, and no vertices over four influences.
- Recorded intentional open panel/component edges: 1,973 after position-weld diagnostics.
- Vanilla calibration precedent: `gfx/models/units/infantry/western_european_infantry.mesh` with `gfx/entities/units_infantry.asset#infantry_rifle_entity`.
- Recorded source geometry height: `7.3518247604`; entity scale: `0.8` exactly once; effective runtime height: `5.8814598083`.
- Runtime mesh SHA-256: `694352c5778e608120474773728317efa776572a2ebe0175f70b67ae7825f3c5`.
- Runtime textures: diffuse `48f9e5488deb14cd2d058c907a9f00bd8c4a4d09c887731334d7ce875b117922`; normal `da1253f4def8caa054d2fc84f4478f8b77d432eff94421c919e72d90ed72e65a`; specular `ca4cfd87de234b63480ba32d07c21d45d6d2a1214ea27ca84b78ebb79fafef1f`.

## Action audit

The former `runtime/crosswalk.md` completion labels are superseded by this semantic audit. Export/reimport proof demonstrates that files load; it does not prove that a motion performs the required role.

| Role | Provider lineage and runtime evidence | Audit result |
| --- | --- | --- |
| idle | Alert 2, task `01a00442-8ca3-7e46-b403-9bff559e5c1a`; 24 FPS, frames 0-97; runtime SHA-256 `ff043370ea408294a3f0e069c0f17542ce5dac20f9ee4388a9258dd9de4a060f` | **Pass**. Substantive provider-authored in-place idle loop. |
| move | Real walking action bundled with rig task `01a0043b-dc34-7795-a542-7d9657a3820e`; 24 FPS, frames 0-26; runtime SHA-256 `bd86173d096c45b4cb8a4b292bd01ce2d3a842a8b3270afe75747b8258489fbd` | **Pass**. Substantive in-place locomotion with alternating contact. |
| attack | Attack 4, task `01a00442-7eef-7531-8c14-afad751cd55c`; 24 FPS, frames 0-68; runtime SHA-256 `5b1f24b1b87d3baf9242e42da6164414dc61ffed0bf4023369f00fe2356f1e0a` | **Blocked**. The robot begins and ends crouched with the forearm guns approximately forward, raises both arms overhead, then lunges with the muzzles toward the ground. There is no coherent aim, discharge, firearm recoil, and recovery sequence. |
| defend | Combat Idle Turn Left 575, task `01a00442-7afb-7b69-9064-439c3aae2c87`; 24 FPS, frames 0-32; runtime SHA-256 `b76bc8952e04d9348030653069f1c2b609f66d082eda3345f9023014c71dcb1a` | **Blocked**. The overhead-arm movement is not a credible armed defensive stance and cannot be relabelled as one. |
| support attack | Side Shot 104, task `01a00442-7654-7e44-bba4-fe07e5c42650`; 24 FPS, frames 0-97; runtime SHA-256 `652f2f04442fdc0d2c1c29120f42f10f88c957376cdc50ebfc448a995a10542b` | **Blocked**. Crouch/kneel/lateral movement exists, but the phase evidence does not show a defensible dual-gun aim, discharge, recoil, and recovery progression. It cannot inherit attack timing as a semantic alias. |
| retreat | Real running action bundled with rig task `01a0043b-dc34-7795-a542-7d9657a3820e`; failed/refunded BackLeft run-in-place 606 task `01a00442-7010-787d-b3cb-48e9e1972191`; 24 FPS, frames 0-16; runtime SHA-256 `ef427279c18abb21cd9404d0ab145b9106d55957770efb38f5d84272166b1985` | **Blocked under the present brief**. The clip is substantive locomotion, but reusing generic running as retreat is semantic reuse, which the parent explicitly forbade. |
| training | Skill 01 17, task `01a00442-84bc-7b6b-a7fd-2b155fce3fbd`; 24 FPS, frames 0-27; runtime SHA-256 `c48167ec8e6c57b3a7490fb218dda46bfc23527c6e79fb231bafb8d37c5b3295` | **Pass for training/drill**. Unique provider-authored multi-frame motion, not an alias. |
| death | Dead 8, task `01a00442-886a-7e45-ae66-9a49fcb64afe`; 24 FPS, frames 0-72; runtime SHA-256 `b9e97aa5f6466f7bfa3e17d3020e30c7506ea1b4c40ae9afeabcf932ba9bfb32` | **Pass**. Articulated collapse, ground impact, and settling are visible. |

Primary visual evidence is `previews/action_phase_contact_sheet.png` and the per-frame front/left/three-quarter images listed by `validation/reimport_autonomous_robot_*_reimport.json`. The attack was additionally inspected at reimport frames 1, 18, 35, 52, and 69 from front and left views. Provider source hashes include attack FBX `91ebf401927895665182c8e51c1c43cbd61df136b7a7e7ac763ab5ef8cc28744`, defend FBX `0e9f61e754589759f2ec18f77ef1b3b5021ff68641a349fa210e490606e37526`, support-attack FBX `2ba90fcc249dca1ac80f5d3bd62d2a4419a3e5710ec29c8a554f1706d2f1db6c`, training FBX `22df05fa7f2e4f9828a55f567c0518e24d9c382433135e52768d3c4765d907f0`, and death FBX `22fc1e892d73da39cc10a783f5bc360d06b8286605ee050fe07e12edf0d44975`.

## Discharge particle, light, locator, and sound-event evidence

Read-only inspection of `gfx/entities/autonomous_robot.asset` found sound events at normalized time `0.3333` for attack and support attack, but **no particle event, no light event, and no `node` locator assignment**. Repository searches found no robot-specific muzzle particle or robot-specific muzzle light registration. The mesh export log emits the generic io_pdx_mesh `Writing locators` stage, but the runtime entity and production evidence name no left- or right-muzzle locator. Therefore no discharge particle, flash light, or muzzle locator can be certified.

Even the existing attack sound timing cannot be approved as synchronized discharge evidence because the action itself has no defensible discharge/recoil phase. Adding effects to a semantically invalid motion would not repair it. Parent-owned wiring must remain unchanged until a replacement provider action supplies an auditable discharge frame and stable left/right locator strategy.

## Sourced audio audit

The audio sources are defensibly documented and immutable originals are retained. The selected attack recording is Lubini, `MG 42 (Solo) WW2.wav`, CC BY 4.0, source page `https://freesound.org/people/Lubini/sounds/338242/`, archived official preview SHA-256 `f95eb1b9fe8e5889d56bd68ca602472b751fa3d287e708f229dff0827bd6f9fc`. Other originals are Mx. Granger's CC0 `Door knocker audio.ogg` (`3362b0bd105382bd8f5e0d268b8e7318233abd966c43449241bfee1f35b47c35`), Maximilian Schonherr's CC BY-SA 4.0 cordless screwdriver recording (`a53525ce339297e1536a6efe0c0d7a6d867e53567e40edc2b8e2ff1376d112cb`), stephan's public-domain `Metal drop thump.ogg` (`b8f5506893d2871c86f5c7e01305bff788df156a265e63bb9b00cbbd51647c5`), and tcpp's public-domain `Explosion 10.ogg` (`a663703652971302e911e513cbde7550577508efc878087894b5464a63f35b2a`). Exact page and direct-download URLs and permitted transformations are in `evidence/audio/source_plan.md` and `evidence/audio/source_ledger.md`.

All six installed WAVs probe as mono 44.1 kHz 16-bit PCM:

| Runtime role | Duration | Runtime SHA-256 | Sync status |
| --- | ---: | --- | --- |
| select | 1.2 s | `757f4da4ac152b061d869b0e4dbf7520b7cd180e13081d050ceda7e4b8c23b00` | Source package valid; per-unit selection consumer remains parent-owned. |
| move servo | 3.0 s | `883ae761aa0881341595b61840501ac2cd8be50b1dadb86f45a49991d30d0017` | Existing move loop is usable. |
| idle loop | 4.0 s | `e256cf3ef13a6d5c45eeebe5955167e02e89208fce2c53fab130c36236af9700` | Existing idle loop is usable. |
| impact/footfall | 1.5 s | `c58b61376a3f480c52e3028e6c9dcc83d82329cab29de32f1e108702396c0123` | Move contacts are documented at frames 1 and 14; retreat sync is blocked with the retreat role. |
| dual-MG attack | 2.75 s | `ee4e57f0ff5c650d2584a0a199046505b9f82e4403c5725f21ab3d585d7e6060` | **Blocked from final synchronization** until valid attack and support-attack discharge frames exist. |
| death | 2.6 s | `39b28b0759a84223d8017f12b82a62c9011d304faf76ae8f3231430d61ae3036` | Death start at frame 1 with collapse phases at 37 and 55 remains defensible. |

Attribution and ShareAlike obligations in the source ledger remain mandatory. No generated, synthesized, placeholder, or unclear-license audio was introduced.

## Bespoke vanilla-green counter audit

The existing counter package passes the file, format, palette, and visual-comparison audit; live consumer validation remains parent-owned.

- Exact installed definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, SHA-256 `0d7b62caf328b3c296ec27ab85318f3cc78cc760b02923538bf5240815963335`.
- Matching skill-local reference families: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png` and `units/land/map_counters/contact_sheet.png`.
- Large consumer: `GFX_group_autonomous_robot_icon` and `GFX_unit_autonomous_robot_icon_medium`; `152x42`, two `76x42` frames; runtime DDS SHA-256 `147cf90c3d053947640f7865f1dade6d8ffaba99942e8401ed4575d53db61b09`.
- On-map consumer: `GFX_unit_autonomous_robot_icon_medium_white`; `60x12`, two `30x12` frames; runtime DDS SHA-256 `bdeb527f8a73494b918adec27c26aec97c299f51ad00d2da2946a37a278edd4b`.
- Frame order: green selected state first, pale/white alternate state second; BGRA 32-bit uncompressed with alpha.
- Sampled vanilla green anchors: `(73,106,73)`, `(81,113,81)`, `(119,144,119)`, `(151,170,151)`, `(186,199,186)`, `(198,208,198)`; dark anchors `(32,44,32)`, `(9,13,9)`, `(0,0,0)`.
- Contact sheet: `evidence/counter/contact_sheet.png`, SHA-256 `463c2d5484950c9a569b04838efb164b3afc60f1c2363cec990114bd16d19c36`. Visual review confirms an original robot silhouette, transparent unused canvas, green/white state distinction, and comparison against installed vanilla medium-tank/mechanized families.
- Existing art-owner handoff: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/autonomous_robot_counter_art_handoff.md`.

## Blockers and recovery boundary

1. Attack, defend, support attack, and retreat fail the current semantic-action requirements. Existing `.anim` files must not be treated as accepted final actions merely because they export and reimport.
2. Historic provider rig task `01a0043b-dc34-7795-a542-7d9657a3820e` is no longer addressable through `meshy_animate`; the provider returned `Resource not found`.
3. The live balance is 13 credits and the parent placed an explicit coordination hold on paid calls. No recovery spend is authorized in this pass.
4. The locked Meshy rig route accepts a provider task ID or model URL, not a local file upload. A future recovery needs a provider-addressable reuse route for the existing model/rig; no new base generation is authorized.
5. No left/right muzzle locator, robot muzzle particle, robot muzzle light, or valid discharge frame is currently certifiable.
6. Audio sourcing and counter art are present, but the dual-MG audio cannot receive final animation synchronization until valid firearm actions exist.

When the coordination hold is released, the compliant recovery is to preserve the installed model identity, establish a provider-addressable rig through the locked Meshy route, obtain separate provider-authored firearm actions with genuine aim/discharge/recoil/recovery plus a distinct retreat action, and then use the allowlisted Blender adapter only for import, retarget, cleanup, normalization, bake, export, and reimport. If Meshy cannot provide those roles, they remain blocked unless the user explicitly approves a professional source.

## Parent-owned remaining work

- Decide when the shared Meshy balance may be used and whether a provider-addressable re-rig of the existing model is allowed.
- Review replacement action candidates before any runtime binding changes.
- Define and wire left/right muzzle locators, particle/light events, and corrected sound timing only after a valid discharge phase exists.
- Retain required audio attribution and ShareAlike notices.
- Register or verify the counter tokens and perform live consumer validation.
- Validate the final unit in game. This handoff does not claim in-game completion.

## Files changed by this audit

- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-08-27_autonomous_robot_3d_recovery_audit.md`

The environment verifier refreshed `.tools/3d_pipeline/reports/environment_report.json`; that shared generated report is not owned or committed by this handoff. No simplification or fallback was applied. The package is explicitly incomplete because four required animation roles and firearm effect synchronization remain blocked.
