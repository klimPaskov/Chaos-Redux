# Event 002 base and demonic zombie animation remediation handoff

Date: 2026-08-22

Scope owner: `chaosx_3d_model_pipeline`

Runtime packages in scope: base `chaosx_zombies` and `chaosx_demonic_zombies`

## Outcome

No paid Meshy operation, provider generation, rigging task, animation task, Blender mutation, PDX export, runtime copy, or gameplay/GFX/entity edit was performed.

The shared Meshy/Blender production lane was reserved by another package, and the parent explicitly limited this pass to read-only preparation. Process contention is not recorded as a package blocker.

The substantive results are:

- `chaosx_demonic_zombies`: `blocked` for the requested Meshy-only animation route. The accepted creature has a mandatory winged-biped/digitigrade identity and must visibly articulate its wings. Meshy's official rigging endpoint currently supports standard humanoid bipeds and explicitly identifies non-humanoid assets as unsuitable. `meshy_animate` accepts a completed Meshy `rig_task_id`; it cannot consume the existing custom Blender wing rig. A successful body-only humanoid rig would therefore leave the wings outside the provider action skeleton and would not satisfy the user's animation requirement.
- base `chaosx_zombies`: `needs_user_review` before provider work. The deterministic root is absent and there is no repository-owned base-zombie model job, authorized source, approved one-image reference, or source/search record. A complete proposed intake, reference brief, scale crosswalk, action map, output layout, and credit plan is provided below so the parent can conduct the source-first search, create one native-transparent approval image, and obtain user approval without guessing.

No simplification or fallback was used. The demonic creature was not silently reduced to a wingless humanoid, and the existing base runtime mesh was not rendered and recycled as a Meshy input.

## Required reading and precedents used

- `AGENTS.md`
- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/002_custom_model_animation_quality_audit_2026-08-22.md`
- `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- the required core offline wiki pages named by `AGENTS.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset`
- `gfx/entities/chaosx_zombies.gfx`
- `gfx/entities/chaosx_zombies.asset`
- `common/units/zombies.txt#zombies`
- official Meshy Rigging API: `https://docs.meshy.ai/en/api/rigging`
- official Meshy Animation API: `https://docs.meshy.ai/en/api/animation`
- official Meshy Animation Library: `https://docs.meshy.ai/en/api/animation-library`

The installed vanilla entity maps distinct `idle`, `attack`, `support_attack`, `move`, `retreat`, `death`, and `training` animation IDs and confirms an entity scale of `0.8`. The Event 002 quality requirement is stricter than the current base entity aliases: `defend`, `support_attack`, `retreat`, and `training` must receive distinct accepted source actions.

## Dependency and route evidence

The dependency locks were inspected before any provider work.

| Surface | Verified record |
| --- | --- |
| Meshy MCP | official `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, wrapper `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd`, compatibility revision `meshy-7-v4` |
| MCP SDK | `@modelcontextprotocol/sdk` `1.29.0`, git head `e12cbd7078db388152f6e839abdbe09ba01f3f32` |
| Required generation model | exact `meshy-7`; `.tools/3d_pipeline/config/meshy_tool_schema.lock.json` accepts only `meshy-7` for image-to-3D production |
| Live Meshy tools inspected | `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, `meshy_animate` |
| Live `meshy_animate` contract | required `rig_task_id` and integer `action_id`; optional `post_process` with `change_fps` at 24/25/30/60 FPS, `fbx2usdz`, or `extract_armature` |
| Blender | `5.1.2`, build `ec6e62d40fa9` |
| Blender HOI4 adapter | `chaosx_blender_hoi4` `1.7.0`; all four source checksums matched the dependency lock |
| `io_pdx_mesh` | `0.91.0`; archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; live adapter health reported mesh and animation export functions available |
| Dependency lock SHA-256 | `B5D0D00099F33BDB5C896760A333EFE0B1FED4C6B1287842995904B7BB821C5C` |
| Meshy schema lock SHA-256 | `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233` |
| Blender adapter config SHA-256 | `0F4A0E916FF37E1C91EA142D6DC3554A13ED98BFCC0687BC85502C2094F66C23` |

The free live Meshy balance observation was `894` credits. The free Blender adapter health request was `c80f2c3d6a9c417eac3854968bc4ebe2`; it reported Blender `5.1.2`, loaded `io_pdx_mesh`, and available `export_meshfile`/`export_animfile` functions. Request and result evidence are under `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/logs/adapter/`, with SHA-256 values `2F1301827AF1891F80A5E8B4C9E2673040CF34F9B74E62775FD11A1FC08354A4` and `BC1D091E20047ED1ECC5E37BC7407E0806F5ADFE54E41B4672FA7D552E0FE072` respectively.

The balance is evidence only, not a request for spend confirmation. No provider task was submitted.

## Demonic zombie blocker assessment

### Accepted identity and current geometry lineage

The deterministic root is `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/`.

The accepted job profile is `nonhumanoid_winged_biped`, rig family `winged_biped`, with mandatory elongated arms, digitigrade hind legs, clawed feet, and a folded pair of articulated membranous wings. The selected Meshy 7 geometry task is `01a02581-9921-795c-a4a0-d1c298ea4155`; it consumed `30` credits and produced:

| Artifact | SHA-256 |
| --- | --- |
| `refs/original/meshy_input.png` | `3899AD441676879A58002E15A99156F5B83CE348B48263CC33179A00EAB7EAA2` |
| `provider/downloads/generation_meshy7_2_model.glb` | `EDF33C66FEC92DE48C1CB884CCE6B67948D3F9FC81AD06C4A8ED6E06B48D5B4D` |
| `provider/downloads/generation_meshy7_2_model.fbx` | `91A683E925BAFA7393D2837B1688CCCD9A04EE7B6FC6C2863CBCB06EF6E5861B` |
| existing non-accepted `export/mesh/chaosx_demonic_zombies.mesh` | `1C17E2C4B425F1791E45869EF85B8FB4C3CB417BDE69A08A65E95991D66D831C` |

The current candidate is visually a true winged/digitigrade creature, not a standard humanoid. Its prepared geometry is 30,000 triangles, approximately `3.8441 x 3.7939 x 7.3624` Blender units, grounded at approximately zero, and calibrated against the installed infantry source height. Its existing local 23-bone rig explicitly contains `wing_root_left`, `wing_mid_left`, `wing_tip_left`, `wing_root_right`, `wing_mid_right`, and `wing_tip_right`. Those bones prove that wing motion needs a nonstandard skeleton; they do not provide acceptable source motion because the rig and current clips were locally authored.

The original provider reference is an 8-bit RGB PNG (`IHDR` color type `2`) and has no alpha channel. It may remain immutable evidence for the already-created geometry, but it does not satisfy the current native-transparency rule for any future regeneration. Any regeneration reference must be a newly approved, genuinely transparent derivative with its own checksum; the existing image must not be overwritten.

### Why Meshy cannot satisfy the required wing animation

The official Meshy rigging documentation states that programmatic rigging currently works well only for standard humanoid bipedal assets, identifies non-humanoid assets as unsuitable, and can fail pose estimation when a model is not a valid humanoid character. The live MCP `meshy_rig` route accepts only `input_task_id` or `model_url`; it exposes no custom skeleton, wing-bone, or rig-map input. The live `meshy_animate` route accepts only a completed Meshy `rig_task_id` plus an `action_id`; it exposes no Blender armature input and no custom wing channel mapping.

Therefore:

1. The existing custom 23-bone Blender wing rig cannot be submitted to `meshy_animate`.
2. A body-only Meshy humanoid rig, even if the provider accepted the mesh, would not establish provider-authored animation on the six wing bones.
3. Retargeting a humanoid clip onto the local wing rig and keying the wings locally would make the wing motion Blender-authored, which the user explicitly forbids.
4. Leaving the wings static would fail the explicit requirement that the body and wings visibly articulate as appropriate.
5. Generating eight body-only Meshy actions would spend at least `29` credits after rigging while the known wing-source blocker remained unresolved. That is not a valid completion path and was not attempted.

### Required recovery path

The non-simplifying recovery is an explicitly user-approved professional winged-biped animation source that includes a compatible custom skeleton or retargetable body-and-wing channels for all eight roles: `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`. Blender may then import, retarget, clean, ground, normalize, bake, validate, export, and reimport those professional clips without replacing their substantive motion.

The professional package must visibly prove:

- idle: body weight shift, breathing or tension, and restrained wing membrane/root motion suitable for a loop
- move: digitigrade locomotion, grounded contacts, and counterbalancing wing articulation
- attack: anticipation/aim, claw or body discharge, impact/recoil, and recovery with purposeful wing participation
- defend: a distinct braced/guard response with wings protecting or balancing the body
- support attack: a distinct secondary assault, not the attack clip under another name
- retreat: a distinct withdrawal gait with contacts and wing balance, not reversed or aliased move
- training: a distinct rehearsal/display action, not idle
- death: articulated collapse, wing/body impact, and settling

Every role requires a source identifier, original artifact checksum, final action name, FPS, frame range, loop policy, root policy, representative phase previews, grounding/deformation evidence, PDX `.anim`, reimport report, and exported/reimport/runtime hash comparison. The current locally authored actions remain rejected evidence and must not be promoted.

A wingless standard-humanoid regeneration would be a material identity change and forbidden simplification. It is not proposed.

## Proposed base `chaosx_zombies` model job

### Status and deterministic paths

Status: `needs_user_review` before reference creation and `blocked` before any paid call until the source-first and approval gates are complete.

Deterministic job root:

`docs/assets/002_zombie_outbreak/models_3d/zombies/`

Required working/output folders:

```text
docs/assets/002_zombie_outbreak/models_3d/zombies/
  job.yaml
  manifest.md
  history.jsonl
  refs/source/
  refs/original/meshy_input.png
  refs/original/input_manifest.json
  refs/derived/
  refs/briefs/
  provider/requests/
  provider/responses/
  provider/tasks/
  provider/credits/
  provider/downloads/
  provider/rejected/
  blender/source/
  blender/reference/
  blender/working/
  blender/checkpoints/
  blender/previews/
  blender/reports/
  textures/source/
  textures/processed/
  textures/dds/
  export/mesh/
  export/anim/
  validation/
  evidence/
  logs/
  runtime/handoff.md
  runtime/crosswalk.md
```

Stable intake identifiers:

| Field | Proposed value |
| --- | --- |
| owner | Event 002 Zombie Outbreak |
| asset id | `chaosx.event002.zombies` |
| asset slug | `zombies` |
| job id | `002_zombie_outbreak_zombies` |
| profile | `humanoid_unit` |
| runtime stem | `chaosx_zombies` |
| proposed PDX mesh | `chaosx_zombies_mesh` |
| proposed entity | `zombies_entity` |
| runtime consumer | `common/units/zombies.txt#zombies` -> `sprite = zombies` -> `zombies_entity` |
| model output | `export/mesh/chaosx_zombies.mesh` |
| action output root | `export/anim/` |
| final parent handoff | `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/` |

### Asset identity brief

Create one generic base infantry zombie that reads clearly as the common, unspecialized Event 002 zombie rather than infected, rabid, parasitic, mutant, undead, necrotic, demonic, Wendigo, or armored variants.

Required components:

- one complete standard humanoid biped with clearly separated head, torso, arms, hands, legs, and feet
- a true weapon-free T-pose suitable for Meshy's standard humanoid rig: arms horizontal, elbows straight but not hyperextended, palms neutral/open, legs separated, feet fully visible, no crossed or touching limbs
- corpse-pale or grey-green skin, sunken eyes, slack predatory expression, and mild non-graphic decay cues
- worn 1936-1945 civilian or field-labor clothing with a readable shirt/jacket-and-trouser silhouette, torn hems, and restrained dirt/weathering
- asymmetric but rig-safe damage limited to clothing, staining, and superficial skin discoloration; no missing limbs or skeletal exposure
- grounded bare feet or simple worn boots that can make stable contact

Forbidden additions and simplifications:

- weapons, tools, backpacks, shields, helmets that hide the head, wings, tails, horns, extra limbs, attached victims, or extra characters
- gore, exposed organs, severed anatomy, dangling geometry, floating parts, fused limbs, or cloth that bridges the arms to the torso
- modern tactical equipment, modern logos, readable text, insignia, flags, scenery, terrain bases, cast shadows, watermark, collage, turnaround, or side-profile sheet
- any identity motif belonging to a specialized zombie subtype
- a Blender render or current runtime mesh render as the Meshy input

Unseen-side policy: complete ordinary human rear anatomy and the rear of the clothing consistently with the approved front/three-quarter design. Do not invent a backpack, weapon, wound cavity, insignia, special growth, armor, or subtype-specific feature on unseen surfaces.

Texture direction: muted corpse pallor and faded earth-tone cloth, with PBR maps and no baked dramatic lighting. Runtime model textures should be rebuilt to the verified PDX `PdxMeshAdvanced` diffuse/packed-normal/packed-specular pattern at a maximum dimension of 1024 pixels unless fresh installed evidence requires less.

### Source-first search plan and approval image requirements

Source mode begins as `licensed_search`. Before ImageGen, search specifically for modern unit/character artwork suitable as a generic riggable zombie reference. Prioritize official artist portfolios, game or tabletop concept-art pages, OpenGameArt, Wikimedia Commons where the work itself has clear reuse rights, institutional collections of modern licensed illustrations, and creator pages with explicit Creative Commons/public-domain terms.

Suggested query families:

- `generic zombie infantry concept art t pose Creative Commons`
- `undead humanoid character design zombie CC0`
- `zombie game unit concept art reusable license`
- `zombie miniature concept art Creative Commons`
- `walking dead humanoid character sheet public domain modern art`

For every candidate, record the source page, direct image URL, title, creator/publisher, exact license, modification permission, retrieval date, dimensions, and rejection/selection reason in `refs/source/source_search.md`. Archive selected source bytes unchanged as `refs/source/untouched.<ext>` with SHA-256 and `provenance.json`.

Reject archival photographs, museum paintings/drawings, historical plates, antiquities, archaeological/documentary images, film stills, unlicensed game screenshots, fan art without modification rights, gore-heavy anatomy, proprietary named characters, multi-character scenes, unclear licenses, and images with no complete riggable silhouette.

If a suitable licensed/user-authorized source is selected, use ImageGen adaptation to create a substantially original one-subject T-pose reference that preserves only broad silhouette/material/role cues and does not copy protected identity details. If all reasonable modern-art candidates fail, record the failed search and request explicit parent/user approval for `from_scratch_after_failed_search` before generation.

The only provider input must be `refs/original/meshy_input.png`. It must be:

- exactly one clean single-subject image, never a multi-view board
- a complete true T-pose viewed near eye level with a slight three-quarter camera angle
- weapon-free and fully inside the canvas with clear gaps between arms, torso, legs, fingers, and clothing hems
- genuinely transparent RGBA from the initial ImageGen request, with zero-alpha unused canvas and no checkerboard, matte, halo, cast-shadow remnant, clipped geometry, or internal alpha holes
- accompanied by the exact ImageGen prompt, source-to-derivative comparison, dimensions, checksum, provenance/authorization note, and explicit parent/user visual approval before Meshy

If native transparency fails, first use a targeted ImageGen transparency edit. Local background removal is fallback-only after that failure and requires preserved original/derivative hashes and edge QA.

### Numeric scale crosswalk and provider settings

Use the installed vanilla infantry calibration already measured in the Event 002 packages:

| Quantity | Required value |
| --- | ---: |
| installed vanilla mesh | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh` |
| installed entity | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity` |
| selected source object | `polySurface106`, collision-only geometry excluded |
| vanilla source mesh height | `7.351824797689915` Blender units |
| runtime entity scale | `0.8` |
| vanilla effective runtime height | `5.881459838151932` runtime units |
| custom Blender target height | `7.351824797689915` Blender units |
| custom effective runtime height | `5.881459838151932` runtime units |
| source provider height | `1.7` metres, retained separately from Blender/PDX calibration |
| forward/up axes | `-Y` / `+Z` |
| ground contact | lowest approved foot/boot contact at `Z = 0` before entity scale |
| conversion factor | measure candidate provider height after import, then apply one uniform factor `7.351824797689915 / measured_provider_height`; do not guess or reuse `1.8 m` |

Apply entity scale exactly once. The exported mesh matches the measured vanilla source height; the parent entity retains `scale = 0.8`. Do not normalize to effective runtime height and apply `0.8` again.

Provider settings after reference approval:

- exact `ai_model = meshy-7`
- one `file_path` input only
- `pose_mode = t-pose`
- `model_type = standard`
- `topology = triangle`
- `target_polycount = 30000`
- `should_texture = true`
- `enable_pbr = true`
- `remove_lighting = true`
- `target_formats = [glb, fbx]`
- `multi_view_thumbnails = false`

Reject geometry before rig/animation spend if it has missing or fused limbs, a non-T pose, floating pieces, major open holes, clothing bridges across joints, subtype identity drift, unacceptable rear invention, or more than 300,000 faces. Download and checksum every successful GLB/FBX immediately.

### Eight distinct Meshy action sources

The proposed map uses eight different official Meshy action IDs. It is a paid-call plan, not acceptance evidence. Each provider result must be visually reviewed on the final base-zombie geometry; the action name alone is insufficient.

| Runtime role | Proposed official action | ID | Loop/root policy | Acceptance requirement |
| --- | --- | ---: | --- | --- |
| `idle` | `Idle` | 0 | loop, in place | subtle full-body undead tension/breath/weight shift; loop endpoints compatible |
| `move` | `Mummy_Stagger_inplace` | 650 | loop, in place | recognizable stagger with alternating grounded contacts and no net root travel |
| `attack` | `Attack` | 4 | non-loop, in place | must read without an imaginary weapon as reach/strike, contact, recoil, recovery; reject otherwise |
| `defend` | `Block1` | 138 | short loop or held non-loop after inspection, in place | distinct braced guard/reaction, not attack reuse |
| `support_attack` | `Punch_Combo_3` | 203 | non-loop, in place | distinct secondary multi-phase assault with separate timing from attack |
| `retreat` | `Injured_Walk_Backward_inplace` | 638 | loop, in place | visibly backward/withdrawal gait with stable contacts, not reversed move |
| `training` | `Boxing_Practice` | 87 | non-loop or bounded loop after inspection, in place | distinct rehearsal/training sequence, not idle or attack alias |
| `death` | `Fall_Dead_from_Abdominal_Injury` | 188 | non-loop, in place after contact correction | articulated collapse, ground impact, and settling; no transform-only fall |

All eight calls must use `post_process = { operation_type = change_fps, fps = 24 }` unless the downloaded source already proves a better verified 24 FPS path. Each successful task must retain the `rig_task_id`, `action_id`, animation task ID, response/status, downloaded GLB and FBX checksums, source action name, and recipient import/retarget record.

Expected source export names:

- `export/anim/chaosx_zombies_idle.anim`
- `export/anim/chaosx_zombies_move.anim`
- `export/anim/chaosx_zombies_attack.anim`
- `export/anim/chaosx_zombies_defend.anim`
- `export/anim/chaosx_zombies_support_attack.anim`
- `export/anim/chaosx_zombies_retreat.anim`
- `export/anim/chaosx_zombies_training.anim`
- `export/anim/chaosx_zombies_death.anim`

Blender is processing/export only: import, retarget, non-destructive cleanup, contact/root correction, deliberate unit conversion exactly once, bake, validate, export, and reimport. It may not author replacement motion, whole-rig transforms, static aliases, semantic reuse, or simple procedural clips.

For looped actions retain first, quarter, middle, three-quarter, and last phase previews; for attacks retain anticipation/contact/recoil/recovery; for death retain upright/collapse/impact/settling. Require no zero-weight deforming vertices, no unapproved opposite-side influences, no scale F-curves after sanitation, grounded contacts, valid deformation, and exact exported/reimported action evidence.

### Planned credits

Normal planned operations are pre-authorized but still require a live balance check immediately before each paid tranche.

| Planned operation | Estimated credits |
| --- | ---: |
| one textured Meshy 7 image-to-3D generation | 30 |
| conditional planned remesh if the accepted source exceeds the rig/target envelope | 5 |
| one standard humanoid Meshy rig | 5 |
| eight distinct `meshy_animate` calls | 24 |
| conditional format conversion only if the required source format is absent | 1 |
| maximum ordinary planned path | 65 |

Extra recovery limit: `0` credits and `0` attempts until a concrete failure occurs and the parent/user explicitly approves the additional retry with the failed operation, consumed credits, proposed recovery, estimate, and remaining balance. This does not restrict the ordinary first attempt for each planned operation.

### Existing audio and counter companion boundary

The base unit currently consumes `chaosx_zombie_idle`, `chaosx_zombie_move`, `chaosx_zombie_attack`, and `chaosx_zombie_death` through `gfx/entities/chaosx_zombies.asset`, and the `ZZZ_infantry_idle` selection identity exists. The existing audio inventory is documented in `specialized_zombie_audio_counter_intake.md`, which also records that durable original-source provenance for the current base WAVs was not found. Animation synchronization points must be recomputed from the final eight actions; existing event times cannot be assumed.

The exact base counter consumers are:

- `GFX_unit_zombies_icon_medium` -> `gfx/interface/counters/divisions_large/zombies_icon.dds`, `152x42`, two `76x42` frames
- `GFX_unit_zombies_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_zombies_icon.dds`, `60x12`, two `30x12` frames

The installed references are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `.../gfx/interface/counters/divisions_large/unit_infantry_icon.dds`, and `.../gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`. The matching skill-local families are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `units/land/map_counters/`. The sampled large-counter green anchors include `#496A49`, `#4A6B4A`, `#537253`, and `#648064`.

This pass does not assert that the existing base counter or audio provenance satisfies a fresh package completion gate. The parent must either promote existing durable evidence into the new base job or carry explicit companion blockers. No audio or counter was copied, generated, or edited here.

## Meaningful validation performed

- Inspected the exact Event 002 animation-quality audit and both current runtime entity registration patterns.
- Inspected installed vanilla infantry mesh/entity action registrations and the separate state bindings for support attack, retreat, and training.
- Verified the locked dependency versions and adapter/io_pdx_mesh checksums.
- Performed a free live Meshy balance observation and a free Blender adapter health probe before the lane restriction arrived; no paid task was created.
- Inspected the demonic source reference and front/rear/side/three-quarter Blender candidate previews.
- Confirmed the demonic candidate's 30,000-triangle geometry, numeric scale crosswalk, selected Meshy task, source artifact hashes, and explicit 23-bone local wing rig.
- Confirmed the demonic input PNG lacks an alpha channel and therefore cannot be treated as a current-rule transparent regeneration input.
- Verified from the official Meshy documentation and live MCP schema that auto-rigging is standard-humanoid-only and `meshy_animate` accepts a Meshy rig task rather than a custom Blender wing rig.
- Mapped eight distinct base-zombie semantic roles to eight official Meshy action IDs with role-specific acceptance gates.

## Skipped validation and why

- No Meshy rig or animation task: the production lane was reserved, the demonic route has a known custom-wing incompatibility, and the base job lacks an approved provider image.
- No base source search, ImageGen reference, or reference approval: the parent requested a search plan and later approval-image handoff, not autonomous generation during the occupied lane.
- No Blender mutation/export/reimport: there were no accepted provider actions to process.
- No PDX `.anim` checksum or visual comparison: no new export exists.
- No runtime synchronization or entity-state rewrite: parent-owned and explicitly out of scope.
- No in-game validation: parent/user-owned.

## Files created or changed by this pass

- `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/002_base_and_demonic_zombie_animation_remediation_handoff_2026-08-22.md`
- `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/logs/adapter/c80f2c3d6a9c417eac3854968bc4ebe2.json` (free adapter health request evidence)
- `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/logs/adapter/c80f2c3d6a9c417eac3854968bc4ebe2.result.json` (free adapter health result evidence)

No commit was created, as required by the parent.

## Parent actions required

1. Carry the demonic package as `blocked` without spending on body-only Meshy actions. Obtain explicit user approval and a professional winged-biped action source for all eight roles; do not simplify away the wings.
2. Conduct and archive the proposed base-zombie source-first search. If no licensed source survives, record the failure and request approval for from-scratch ImageGen.
3. Generate one native-transparent base-zombie T-pose reference, retain prompt/provenance/checksums, and show it to the user for explicit visual approval before Meshy.
4. Materialize `docs/assets/002_zombie_outbreak/models_3d/zombies/job.yaml` from this intake only after the source mode, selected reference, approval state, and companion sound/counter disposition are known.
5. After the shared lane is free and all gates pass, run the normal base generation/rig/eight-animation path with a live balance check before every paid tranche, immediate downloads, checksums, Blender processing, PDX export, actual reimport, and per-role visual evidence.
6. Keep runtime wiring and source-to-runtime copying parent-owned. Replace the current semantic aliases only after all eight accepted `.anim` files and their lineage/reimport evidence exist.
