# Event 014 Cannibal Model Family Handoff

Historical supersession notice: this broad model-family gate is retained for source and provider history only. The 2026-08-26 approved visual-reuse decision removes Bone Riders and Network Cadre from custom model production and assigns them vanilla `cavalry` and `infantry` sprites; their old job rows are not current work queues.

## Status

`blocked_before_provider_generation` as of 2026-08-22.

The parent’s final source gate requires actual Internet-sourced or user-supplied modern artwork followed only by faithful enhancement for resolution, alpha, background, padding, or edge cleanup. The earlier substantially original ImageGen inputs listed below are rejected evidence; this handoff does not prove an eligible provider input for any job. Feast Guard is now separately recorded with the user-supplied source and faithful input checksum in `event014_cannibal_feast_guard_3d_handoff.md`.

No source-first Meshy task, balance call, Blender mutation, export, runtime synchronization, or runtime wiring was performed in this resumed tranche.

## Owned jobs

- `cannibal_scavenger_warband`
- `cannibal_feast_guard`
- `cannibal_feast_cohort`
- `cannibal_bone_guard`
- `cannibal_island_reavers`
- `cannibal_siege_eaters`
- `cannibal_march_predation_column`
- `cannibal_network_cadre`

Each job requires one parent-approved provider input derived from an actual sourced or user-supplied modern artwork. The canonical `refs/original/meshy_input.png` path is usable only after that source and faithful-enhancement record is approved.

All earlier generated-from-scratch or substantially redesigned references, provider tasks, downloaded geometry, Blender candidates, rigs, actions, previews, and exports remain rejected evidence and are forbidden from selection, export, synchronization, or runtime wiring.

## Superseded generated-input validation

The following table records integrity checks for the former generated-input batch only. These checks do not establish current source eligibility and must not be used to authorize Meshy submission.

All eight current inputs have these shared decoded properties:

- dimensions: `1148x1722`
- pixel format: `rgba`
- decoded alpha range: `0..254`
- maximum alpha on the outermost border: `0`
- the SHA-256 checksum matches `refs/original/input_manifest.json`
- the input manifest records `parent_review = approved_for_meshy_input`

| Job | Superseded generated-input SHA-256 | Historical intake result |
| --- | --- | --- |
| `cannibal_scavenger_warband` | `CE1D002E66864A08F52DF1DA94C399146E16A0F90CE33BF69BE90129EF70B417` | Image integrity passes; assigned long spear is visible. |
| `cannibal_feast_guard` | `6ACD1D8D9CF4AFE408F8D1EAE8F59BA72CA7E0B8B35B9BCE2E84DC7D37EB8092` | Image integrity passes; cleaver and shield are visible. |
| `cannibal_feast_cohort` | `B2A6A28BC97A8B6D6C7FC7728D0BD4D6E06B4E796F2443AEC0B84F94BE1E6A1E` | Image integrity passes; long forked polearm is visible. |
| `cannibal_bone_guard` | `0966093155490EC1C8121C17D3E3054ACCD4B646BC4A0385EBC98C65598FB52D` | Image integrity passes; heavy two-handed bone-armoured axe silhouette is visible. |
| `cannibal_island_reavers` | `199849DCAB81BCEC38BEE7E9259F70F11C541047D0F4D01AEC234C2D972328C2` | Image integrity passes; long boarding spear, shield, and belt axe are visible. |
| `cannibal_siege_eaters` | `3E6944C0E94F4E52AFA91987490B938EABDC06FDF42A284B2850C531B8C7FFEB` | Image integrity passes; two-handed sledgehammer is visible. |
| `cannibal_march_predation_column` | `9C5D0C210D0F0DEFEFD2392A41A846EA641CAE2B331E3BA61679A7FD99D332F2` | Image integrity passes, but the model identity gate fails: paired axes are visible and the required self bow, quiver, and machete are absent. |
| `cannibal_network_cadre` | `5EAF7F2E58BF7941923D64A9CF1BBC93387F1873EBCCE19E861CF5DEA43585BA` | Image integrity passes; short bow, quiver, and belt knife are visible. |

The March input conflicts with `014_cannibal_irregular_unit_model_plan.md`, which requires a plain self bow, quiver, machete, and a rapid bow draw/release attack. Provider generation is blocked until that input is replaced with an approved source-first adaptation or the authoritative plan and action contract are explicitly amended. Accepting the current axes would silently remove a required component and invalidate the weapon-specific animation contract.

## Dependency-lock verification

The process `MESHY_API_KEY` hard gate passed before repository/job intake.

The current dependency files declare:

- Meshy MCP package: `@meshy-ai/meshy-mcp-server` `0.4.0`
- Meshy compatibility revision: `meshy-7-v4`
- only verified image model: `meshy-7`
- Blender HOI4 adapter: `1.7.0`
- Blender: `5.1.2`, build `ec6e62d40fa9`
- io_pdx_mesh: `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`

`python .tools/3d_pipeline/verify_environment.py` did not pass. It reported:

- file: `.tools/3d_pipeline/adapter/blender_worker.py`
- locked SHA-256: `F61F2D63E7BED9B850FC3CA50030D7B427C835CE5F9F064D25EE3D9A63C3C27D`
- current SHA-256: `A6E26FAD55EED34E928E060219B0CBFAD1848490CCABBE7944EB8E03D6DD3B2B`

This is a hard dependency-lock blocker. No balance call, paid provider call, adapter health call, Blender operation, or export was attempted after the mismatch. The model-family owner did not edit `.tools/3d_pipeline/**`.

## Animation acceptance boundary

Every final job still requires eight distinct actions: `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`.

Primary motion for every role must come from verified Meshy `meshy_animate` or another explicitly approved professional animation source. Blender may import, retarget, clean, correct ground/root contact, normalize, bake, validate, export, and reimport that motion. Locally improvised, procedural, transform-only, static, role-aliased, or whole-rig motion is not eligible as a final action.

The current Meshy schema lock documents verified action ids only for `idle = 0`, `attack = 4`, and `death = 8`. The remaining professional role sources must be verified from the live locked action library before the family can be complete; absent roles remain blocked rather than being filled by local authoring.

## Vanilla calibration and runtime boundary

- vanilla mesh: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh`
- source object: `polySurface106`
- source height: `7.351824797689915`
- axes: forward `-Y`, up `+Z`
- vanilla entity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity`
- entity scale: `0.8`, applied exactly once
- effective runtime height: `5.881459838151932`
- live consumer contract: `common/units/014_cannibalism_irregular_infantry.txt#<slug> -> <slug>_entity`

Runtime `.gfx`, `.asset`, entity, gameplay, sound-definition, localisation, and in-game validation remain parent-owned. No in-game completion is claimed.

## Existing adjacent packages preserved

The previously sourced six-role audio packages and the completed three-surface bespoke counter handoff were left untouched. They are not evidence that the new source-first geometry or action package is complete.

## Changed files

- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_cannibal_model_family_handoff.md`

## Required next actions

1. Reconcile the adapter `1.7.0` dependency lock with the current shared-tree adapter source and rerun `verify_environment.py` to zero findings.
2. Replace the March source-first Meshy input with an approved bow/quiver/machete reference, or explicitly amend the authoritative plan and weapon-specific action contract.
3. Re-run the full input integrity and visual gates.
4. Probe the live locked Meshy schema and professional action library, then establish eligible sources for all eight semantic roles before provider spend.
5. Only after all hard gates pass, submit eight fresh Meshy 7 jobs using the current exact-one-image inputs and preserve the complete new lineage separately from rejected evidence.

## Skills used

- `chaos-redux-3d-model-pipeline`
- `chaos-redux-event-assets`
- `chaos-redux-event-planning`
- `chaos-redux-subagents`
