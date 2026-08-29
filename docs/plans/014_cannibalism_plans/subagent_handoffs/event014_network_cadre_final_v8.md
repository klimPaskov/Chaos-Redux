# Event 014 Network Cadre 3D package — v8 handoff

Historical supersession notice: this v8 custom-model attempt is retained as failure and provenance evidence only. The 2026-08-26 approved visual-reuse decision assigns Network Cadre vanilla `sprite = infantry`, so no custom model, action, entity, provider, or v8 completion is required.

## Status

Historical status: incomplete and blocked at the approved external archery-action import stage before the vanilla-visual decision. No runtime wiring or in-game completion is claimed.

The static model, authoritative 1.10.3 normalization checkpoint, rig, six retained Meshy actions, sourced audio package, and existing bespoke counter handoff remain preserved. Parent visual QA accepted the death action and rejected the original/recovery attack and support-attack clips because the drawing hand never contacted the physical bowstring.

## Approved replacement sources

- Attack: KayKit Character Animations 1.2 `Shoot(2h)Bow.fbx`, CC0, SHA-256 `B02F8DDB094DA36C458B23CBA89AB9C4EE796153C1E8BF2EB89ADE22333A3184`.
- Support attack: CMU Graphics Lab trial `79_86`, Bruce Hahne 2010 BVH conversion pinned at commit `09a07f54f3bbb58797325f009282d0b2048a2871`, SHA-256 `FABE071C2C3FB0A636035CCA5D82FF282F851D711CF1B3736E2B12D355283056`.
- Rights, source pages, license bytes, official preview evidence, hashes, provenance JSONs, and mapping plan are under `evidence/external_archery_sources/`.

## Current blocker

At repository HEAD `a3e0a1497b6926b025070267eb9c75bd00b77c93`, adapter 1.10.7 passes its full environment gate, but the live wrapper and locked files do not register a native external-action/BVH importer. Direct `tools/list` exposes only the legacy `chaosx_blender_hoi4_import_animation_action`, whose source formats exclude BVH.

Required unblock: commit and checksum-lock the structured native BVH professional-source importer, reload Codex/MCP registration, and prove it appears in direct wrapper `tools/list` and the environment gate. Only then import the unchanged BVH, retarget both approved independent actions, and perform front/right/three-quarter preparation, draw, release, recoil, and recovery QA.

Exact evidence: `validation/external_action_import_blocker_v8.md`.

## Remaining work after unblock

1. Import and retarget the approved KayKit attack and CMU support-attack without authored replacement keys.
2. Reject unless each action shows visible bow-hand control, drawing-hand/string contact, aim, release, recoil, recovery, bounded deformation, and a distinct silhouette.
3. Preserve the accepted death and other retained actions; revalidate all eight actions at 24 FPS.
4. Process final DDS materials, export the HOI4 mesh and eight genuine animations, reimport them, and record checksums.
5. Synchronize the final manifest, evidence ledger, action/runtime crosswalk, previews, audio synchronization, counter consumer handoff, and this handoff.
6. Commit only this exact package and handoff after every gate passes.

## Credits

Known provider spend for the v8 line is 71 Meshy credits: 30 generation, 5 rigging, 24 original actions, and 12 rejected bow-action recovery attempts. No external cash purchase was made.
