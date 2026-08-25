# Event 016 asset workspace cleanup handoff

Date: 2026-08-26

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
- The accepted Meshy V8 neutral generation, remesh, R2 rig FBX, packed texture companions, accepted Quaternius Standard archive, actual-byte reimport proofs, animation exports, audio provenance, hashes, manifests, and licences remain under `models_3d/alien_infantry/`.
- The model manifest and runtime handoff now label former provider paths as formerly staged or pruned so historical provenance is not mistaken for a live dependency.
- Runtime-facing Alien Infantry 2D assets and their registrations were not touched. The model package remains diagnostic evidence rather than an accepted runtime entity.

## Scope and remaining blocker

The event-assets workflow requires retaining this temporary workspace while Event 016 is incomplete or blocked; deleting the whole folder would discard source and provenance needed for the remaining review. The Alien Infantry runtime gate is still open: a stable Meshy-compatible muzzle locator and verified firing/effect/audio synchronization are missing, and distinct defend, support-attack, retreat, and genuine death actions plus parent entity wiring are not accepted. This cleanup does not claim model or in-game completion.

The cleanup was performed in the working tree. Because the deleted binaries were ignored, Git records the cleanup through this handoff and manifest note rather than as individual deletion entries.
