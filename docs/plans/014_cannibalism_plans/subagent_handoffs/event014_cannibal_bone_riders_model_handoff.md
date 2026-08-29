# Event 014 Cannibal Bone Riders model handoff

Historical supersession notice: this source-audit handoff is retained for failure and provenance evidence only. The 2026-08-26 approved visual-reuse decision assigns Bone Riders vanilla `sprite = cavalry` and removes the custom model/action/provider requirement; the former model workspace was removed and no statement below is a current production queue.

The parent’s final source gate permitted faithful ImageGen enhancement of an approved actual source for resolution, alpha, background, padding, or edge cleanup only. It did not permit redesign, generated-from-scratch input, or invented horse, rider, sling, or pouch components.

Historical status: `blocked_no_eligible_exact_source_selected` before the approved vanilla-visual simplification. This package is not a current runtime deliverable, and its absence does not block Bone Riders gameplay.

## Corrected source disposition

Generated or regenerated references are forbidden for this asset. `refs/original/meshy_input.png`, SHA-256 `D3929E3D7584FDFBD42B596C26AF316195341F0BB3A730AA7CFBD4B78721AC15`, and every candidate derived from it are superseded evidence only. They must not be submitted to Meshy or promoted into runtime artifacts.

The selected input must be one actual Internet-sourced game, concept, tabletop, or fantasy artwork image that already shows one complete living horse in skull/rib/long-bone barding, one feral painted skull-helmet rider, a visible sling and stone pouch, no spear, and no recognizable living Indigenous motifs. Processing is limited to crop, background/alpha work, and cleanup. The audit in `refs/source/source_search_2026-08-22.md` found no candidate that passes the exact design, readable-anatomy, artwork-family, and reuse-rights gates simultaneously. The archived Abe Taraky and MyMiniFactory images are not licensed for provider submission and also fail the design gate; the reusable sculpture/anatomical and generic horse candidates fail the source-family or identity gate.

## Dependency and route evidence

The former adapter-declaration blocker is resolved. The dependency lock is SHA-256 `39BEC68E5B356D6BB0BD0B7463C9FF761F8572E0453405DB929AAAC4292289F2`; Meshy schema lock `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config `C8CF20F9C177D32AB0593BF9CA128BB369E9E24640BB436E310EE42EB9698F29`. Locked/live components are Meshy MCP `0.4.0`, SDK `1.29.0`, exact `meshy-7`, Blender `5.1.2` build `ec6e62d40fa9`, adapter `1.8.1`, and io_pdx_mesh `0.91.0` with archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

The bridge at `127.0.0.1:9876` was listening. Adapter health request `e283a4d0a4b24a98a87171854bdf4301` passed. Repository wrapper `tools/list` exposed 25 operations, including creature segmentation, scale calibration, rig/action authoring, grounding, root offset, and runtime sanitization.

No Meshy call of any kind was made: no balance, image-to-3D, task status, download, remesh, rig, convert, or animate. Provider task IDs and response IDs: none. Planned upper estimate: 64 credits. Consumed: 0. A parent-issued serialized lease naming the exact task and cost remains mandatory before any future Meshy call.

## Numeric vanilla crosswalk

The installed `cavalry_horse.mesh` was copied read-only into the job with SHA-256 `DCACBB930CB84AB58EAA9EB012D36C5CE10B36052AED0BDE3585E98E1BCB9044` and measured through adapter 1.8.1:

- bounds min: `[-3.2977614402770996, -12.498510360717773, -0.002540622605010867]`
- bounds max: `[3.2977614402770996, 7.8376851081848145, 15.64350414276123]`
- source dimensions X/Y/Z: `6.595522880554199 / 20.336195468902588 / 15.646044765366241`
- pdxmesh scale from `infantry.gfx#infantry_cavalry_horse_mesh`: `0.45`
- dimensions after pdxmesh scale: `2.9679852962493896 / 9.151287961006165 / 7.040720144414808`
- separate attached horse-entity scale precedent from `units_cavalry.asset`: `0.65`
- dimensions if that nested attachment scale applies: `1.9291904425621033 / 5.948337174654008 / 4.576468093869625`

The installed `cavalry_frame.mesh`, SHA-256 `335891E4DD7E987BD374AE3E6A84C58475C120D37CDC80834B76046D4AE36102`, measured:

- bounds min: `[-0.018676867708563805, -0.01885000802576542, -0.5446255803108215]`
- bounds max: `[0.009907562285661697, 0.01885000802576542, -0.5411446690559387]`
- dimensions X/Y/Z: `0.028584429994225502 / 0.03770001605153084 / 0.0034809112548828125`
- frame scale: `1.0`

Evidence reports are `blender/reports/vanilla_cavalry_horse_measurement_prepare.json` SHA-256 `367C91A0EF63F7C5790BAF7B1CF4C305BC437F34C80349B8FF0DEE7F27642519` and `blender/reports/vanilla_cavalry_frame_measurement_prepare.json` SHA-256 `18F95727A6FCC1FEF0B7222C2C5AE5D48185D99B8BFB01692745EA370BC75233`. `blender/reference/measurement_probe.glb` is an adapter carrier only, never a Bone Riders candidate.

The crosswalk is complete only on the vanilla side. Candidate dimensions, target dimensions, conversion factor, and candidate contact comparison are explicitly null because no approved Bone Riders candidate exists.

## Animation precedent and remaining production

Installed `animation.asset` registers professional horse idle, idle-forward, walk, charge, and charge-2 actions and cavalry rider rifle idle/move actions. Those can be technical source candidates only where actual retargeting proves compatibility. Vanilla does not supply a genuine mounted sling cycle or articulated horse+rider death, and it cannot justify aliases for defend, support attack, retreat, or training. All eight 24 FPS roles remain blocked: idle, move/canter, sling attack, defend, support attack, retreat, mounted sling training, and articulated horse+rider death.

No Bone Riders geometry, material, DDS texture, rig, weights, final action, `.mesh`, `.anim`, export, reimport, preview, or source-to-runtime synchronization exists. Sourced 44.1 kHz audio was not researched in this source-audit-only tranche. The parent-reported counter package was not re-audited, so consumers, tokens, vanilla DDS/definition evidence, palette, frame states, hashes, and GFX wiring remain unverified.

## Files created or changed by this tranche

- `job.yaml`, `manifest.md`, `history.jsonl`, `runtime/handoff.md`
- `refs/source/source_search_2026-08-22.md`
- `blender/reference/README.md`, copied vanilla horse/frame meshes, and adapter-only measurement carrier
- vanilla measurement reports, previews, checkpoints, sources, and adapter request/result logs
- `evidence/preflight_report.md`, `evidence/dependency_route_audit_2026-08-22.md`
- `evidence/vanilla_cavalry_precedents.md`
- this handoff

No gameplay, event, focus, decision, country, localisation, GUI, GFX, entity, sound-definition, spreadsheet, shared skill, dependency lock, adapter source, or runtime consumer file was edited.

## Simplifications, omissions, and blockers

No fallback or simplification was accepted. The exact blocker is the absence of one eligible sourced artwork image satisfying both the design and rights gates. Production, audio, counter verification, runtime wiring, and in-game validation remain incomplete.
