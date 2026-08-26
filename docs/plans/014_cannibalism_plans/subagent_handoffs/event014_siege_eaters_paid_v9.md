# Event 014 Siege Eaters paid v9 handoff

> Historical blocked handoff. Superseded by the accepted installed Siege Eaters runtime receipt; retain this file for provider and adapter failure evidence only.

Status: `blocked` on a second uncommitted shared Blender-adapter dependency change. Provider production, accepted 1.10.3 preparation, and accepted 1.10.7 death-grounding evidence are preserved; runtime export is not complete.

## Completed provider and preparation milestones

- Immutable sole Meshy input: `refs/original/meshy_input.png`, SHA-256 `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`; it was not replaced or modified.
- Accepted Meshy 7 recovery generation: task `01a0345b-055f-787c-b99c-9b8051d5756b`, triangular PBR T-pose GLB+FBX, 30 credits. The first v9 task `01a03451-bb5f-7597-9284-e4ef69c641a2` consumed 30 credits but was rejected because it reconstructed the sole mace as two symmetric appendages.
- Genuine provider rig: task `01a0345f-2dbd-7362-92e4-43280c2a9ed6`, 5 credits, archived as `provider/downloads/v9_rigged_model.fbx`, SHA-256 `92A838633704C4FA2771600EFF2D24E60EC1E3249992E05AF3A135F362A82816`.
- Eight distinct dedicated Meshy animation sources were archived for idle, move, attack, defend, support attack, retreat, training, and death. The rig-bundled walking clip remains non-final comparison evidence only.
- Adapter 1.10.3 preparation persisted the normalized geometry height at `7.351823806762695` m against the installed-vanilla target `7.351824797689915` m, delta `-0.0000009909272193908691` m within the `0.00007351824797689916` m tolerance after save/reopen.
- Working geometry: 29,999 triangles, 14,968 vertices, zero non-manifold edges, zero degenerate faces, no negative scales, and zero zero-weight working vertices. The 24-bone working armature is `Armature.001`.
- Seven licensed audio roles were revalidated as 44,100 Hz mono signed 16-bit PCM in `evidence/audio_sources/v9_audio_revalidation.json`.
- Provider PBR maps from the accepted generation were packed into PDX normal/specular layouts and converted to 1024x1024 runtime DDS. Evidence and hashes are in `evidence/v9_texture_runtime.json`; raw grayscale roughness is not used as the runtime specular map.

## Motion QA and authorized recovery

The original attack action 237 (`Charged_Axe_Chop`) was rejected after phase renders showed one-hand mace control. Recovery action 128 (`Heavy_Hammer_Swing`), task `01a034a2-51dc-7093-b261-d46e5018d2ab`, also retained one-hand control and was rejected. Recovery action 102 (`Sword_Judgment`), task `01a034aa-55a2-7392-aff5-85884857938c`, was re-imported and rendered under committed adapter 1.10.7, then rejected because its wind-up, strike, and recovery remained one-handed. Distinct two-hand recovery action 327 (`kettlebell_swing`), task `01a034e4-f425-7751-9c34-80229a8c0c10`, is archived and was imported under 1.10.7; its phase QA remains pending.

The original death action 187 (`Knock_Down`) was rejected because its terminal frame remained airborne. Recovery action 8 (`Dead`), task `01a034a2-554d-7094-a50d-aa518fdb55bb`, provides substantive articulated collapse. Adapter 1.10.7 applied the allowed Hips/root-Z-only contact correction across 72 frames while retaining all body-motion keys; post-correction contact remained within `-0.0000276566` to `0.0000135899` m. A final terminal-frame render remains pending.

All action attempts are genuine `meshy_animate` tasks. No local final motion, transform-only clip, action alias, alternate provider, model downgrade, or placeholder was used.

Total v9 provider spend to date is 101 credits: 60 generation, 5 rig, 24 for the initial eight dedicated actions including move, and 12 for four recovery animation calls. Full task lineage and artifact hashes are in `evidence/v9_provider_lineage.json`.

## Current blocker

Adapter 1.10.7 became authoritative at commit `a3e0a1497`; the fresh environment gate and health check passed, and Sword Judgment revalidation plus death grounding ran under that exact version. Immediately after the action-327 import, the next fresh retime call unexpectedly reported adapter `1.10.8`; the shared worker/config/dependency-lock files are again modified beyond the committed lock. The mixed 1.10.8 retime checkpoint is rejected. Further Blender inspection, mutation, export, and reimport are paused fail-closed until the new adapter bytes receive an authoritative committed hash and clean gate.

## Remaining work after the shared lock is committed

- Re-run the exact environment gate and adapter health against the authoritative commit.
- Render and accept or reject the Sword Judgment attack phases; only a coherent two-handed mace strike may become final.
- Apply allowed contact/root correction to the recovery death action and prove collapse, impact, ground contact, and terminal settling without replacing provider body motion.
- Relink the accepted PDX DDS maps in the final checkpoint.
- Export one `.mesh` and eight distinct `.anim` files through checksum-locked `io_pdx_mesh`, then reimport the mesh with every animation and archive proof.
- Record exact audio synchronization frames, final previews, action manifest, runtime identifiers, final manifest/checksums, and complete this handoff.

## Counter and runtime boundary

The bespoke counter package remains documented by `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_counter_art_handoff.md`. Proposed consumer tokens are `GFX_unit_cannibal_siege_eaters_icon_medium`, `GFX_unit_cannibal_siege_eaters_icon_medium_white`, and `GFX_unit_cannibal_siege_eaters_icon_small`.

Runtime entity/GFX/sound-definition wiring and in-game QA remain parent-owned. No in-game completion is claimed.

## Simplifications, omissions, and blockers

No simplification or fallback was used. The package remains incomplete solely because the shared uncommitted adapter dependency blocks the final motion-QA, texture-relink, export, and reimport chain.
