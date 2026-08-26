# Event 016 asset workspace cleanup handoff

Date: 2026-08-26

> Current-status correction: this earlier aggregate cleanup snapshot is retained as historical evidence. The later V13-specific compaction recorded in `016_alien_infantry_docs_reconcile_current_2026-08-26.md` removed a further 2,100 ignored alien-infantry artifacts (3.166 GiB) and retained the accepted V13 exports, seven reimport checkpoints, previews, manifests, and provenance. Use that later handoff and the V13 manifest for the current workspace size and runtime status.

## Outcome

The disposable bulk in `docs/assets/016_brilliant_scientist/` was compacted without deleting the workspace. Before cleanup the folder was approximately 3.15 GB across 4,248 files. After cleanup it is 2,014,398,979 bytes across 4,022 files (approximately 1.876 GB), freeing roughly 1.13 GB of local storage.

The cleanup was evidence-only. It did not change gameplay, interface, GFX, sound, special-project, decision, event, focus, country, or model runtime wiring. No runtime source points into the deleted evidence paths.

## Removed categories

- The superseded `dhrondan_focus_icon_package/` source package was removed after all forty source PNGs were verified byte-identical to the accepted `dhrondan_icon_asset_completion/source_png/focus/` package.
- The temporary `hidden_technology_icons/_tmp_alpha/` directory was removed.
- Failed or superseded Alien Infantry Blender `.blend` checkpoints, `.blend1` backups, provider copies, rejected action probes, and duplicate Quaternius/KayKit/MoCap source binaries were removed after their hashes and rejection evidence were retained.
- Extracted binary payloads and archives from rejected professional animation packages were removed. Their rights findings, provenance, checksums, and rejection records remain in the compact evidence files; the accepted Quaternius Universal Animation Library Standard archive remains.

All removed files were ignored/untracked workspace artifacts. The pre-existing tracked Event 016 asset files were checked before deletion; no tracked asset was removed and there were no pre-existing tracked asset modifications caused by the cleanup.

## Retained evidence and runtime support

- Accepted source and processed PNG/DDS families, portraits, frames, UI pieces, focus and country art, event/news art, and existing validation/contact sheets remain in place because the event is not complete.
- The accepted Meshy 7 V13 generation, remesh, 24-bone rig, seven action FBXs, packed texture maps, actual-byte reimport proofs, audio provenance, hashes, manifests, and licences remain under `models_3d/alien_infantry/`; earlier V8, V10, V11, and Quaternius material remains historical evidence only.
- The model manifest and runtime handoff label former provider paths as historical or pruned so provenance is not mistaken for a live dependency, while the V13 static entity/GFX/animation/sound package is the current parent-review package.
- Runtime-facing Alien Infantry 2D assets and their registrations were not touched. The promoted V13 package still lacks a supported authored muzzle locator/effect binding, strict audio-role coverage, positional playback proof, and live acceptance.

## Scope and remaining blocker

The event-assets workflow requires retaining this temporary workspace while Event 016 is incomplete or blocked; deleting the whole folder would discard source and provenance needed for the remaining review. The Alien Infantry runtime gate is still open because a supported Meshy/Blender-authored muzzle locator, particle/light binding, strict audio-role coverage, positional playback proof, and live acceptance are missing, while the V13 seven-action package and static entity/GFX/animation/sound registrations are promoted. This cleanup does not claim model or in-game completion.

The cleanup was performed in the working tree. Because the deleted binaries were ignored, Git records the cleanup through this handoff and manifest note rather than as individual deletion entries.

## V10 model-attempt prune after parent review

After the Meshy V10 handoff was reviewed and committed as `f59f042b7`, the explicitly rejected or redundant provider binaries were pruned from the ignored job workspace. Removed paths were `models_3d/alien_infantry/provider/downloads/generation_user_source_recovery_v10.glb`, `generation_user_source_recovery_v10.fbx`, `animation_user_source_recovery_v10_attack_action4.fbx`, `animation_user_source_recovery_v10_laser_attack_action104.fbx`, `animation_user_source_recovery_v10_run_and_shoot_action98.fbx`, `rig_user_source_recovery_v10_running.fbx`, and the corresponding `generation_user_source_recovery_v10_textures/` directory. The accepted V10 walking, idle, defend, retreat, and death source FBXs, rig, remesh materials, protected Blender previews/checkpoints, adapter logs, task hashes, and the authoritative firearm-capability rejection report remain available. No runtime-facing file or accepted provenance record was removed. The current folder measurement after the V10 work is 4,369 files and 2,864,585,505 bytes (2.668 GiB); the increase versus the pre-V10 snapshot is accepted model evidence, not an unreviewed failed-attempt cache.

## Further evidence compaction after V10 review

The parent then removed 622 additional ignored files and 727,464,854 bytes (0.678 GiB), reducing `docs/assets/016_brilliant_scientist/` to 3,747 files and approximately 2.137 GB (1.990 GiB). The deletion set contained only superseded V7/V8 preview frames and provider downloads, reproducible Blender `00`-through-`05` checkpoints and `.blend1` backups, per-action/source review blends superseded by the retained V10 base/remesh/rig sources, and the rejected candidate `models_3d/alien_infantry/export/` payload. Rejection reports, hashes, adapter logs, current V10 source-role FBXs, current V10 base/remesh/rig Blender sources, runtime-facing 2D assets, and all tracked manifests remain. Historical references in the Alien Infantry manifest and runtime handoff to the deleted export/checkpoint/preview paths are provenance records only and must not be treated as runtime dependencies.
