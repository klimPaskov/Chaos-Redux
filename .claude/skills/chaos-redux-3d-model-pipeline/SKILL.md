---
name: chaos-redux-3d-model-pipeline
description: Use when creating, rigging, animating, converting, exporting, auditing, or documenting a custom Hearts of Iron IV 3D model, Internet-sourced sound-design handoff, and bespoke vanilla-green counter handoff for a Chaos Redux unit, building, vehicle, aircraft, ship, creature, or articulated asset.
---

# Chaos Redux 3D Model Pipeline

Use this skill for final 3D geometry and skeletal animation assets. It covers the bounded path from one approved reference image through provider generation, provider rigging and provider animation for provider-eligible bipedal models, Blender normalization, live skeleton, skinning, and skeletal action authoring where the provider route does not apply, PDX materials, Paradox export, QA evidence, and a parent-owned runtime handoff.

Do not use it to draw 2D equipment illustrations, unit counters, focus or idea icons, 2D frame-sheet animation, leader portraits, or concept-only requests. The 3D workflow owns the custom-unit counter requirement, vanilla-reference gate, and bounded artist handoff, while final counter art remains with `chaos-redux-event-assets` and `chaosx_icon_artist`. Other 2D surfaces remain with `chaos-redux-event-assets` and `chaos-redux-frame-animation` where applicable.

## Reference map

- [Hard start gates](references/start-gates-and-adapter.md): read before any provider, dependency, adapter, or Blender-route work (key gate, dependency and wrapper verification, nonhumanoid preflight, adapter publication).
- [Reference images](references/reference-images.md): read before searching for, approving, or preparing any model reference image or portrait-derived input.
- [Blender authoring, processing, and PDX export](references/blender-processing-and-export.md): read before skeletal authoring, Blender processing, material or geometry repair, action review, export, or reimport.
- [Custom-unit audio and counter delivery](references/unit-audio-and-counters.md): read for every custom-unit package, for the sourced sound and bespoke counter handoffs.
- [Unit model rebuild workflow](references/unit_rebuild_workflow.md): read only for explicitly requested custom land-unit repair or rebuild work.

## Skeleton, skinning, and action policy

No repository Python script and no adapter operation may generate bones, skin weights, or keyframes from a declarative spec, a template, or a formula. Provider results are ingested as authored assets and are never synthesized by repository code.

The Meshy provider route is the preferred route for rigging and animating provider-eligible bipedal models. The worker generates the body, drives the Meshy rig task and the Meshy animation tasks, and ingests the provider results into the job.

A provider-eligible biped has clearly defined limbs and body structure and need not be human; a suitable bipedal creature or machine may use the provider route. Verify the live locked route against the actual anatomy before a supported attempt. Quadrupedal, serpentine, amorphous, or otherwise unsupported body structures require live Blender authoring. Wings, tails, machinery, and other extra articulations need their own supported controls and actions; a bipedal body alone does not establish support for those parts. Do not classify an asset as static or provider-ineligible merely from its creature, mechanical, vehicle, building, air, or naval label; use its required motion and the actual provider constraints.

Live Blender authoring remains for everything the provider route does not cover well: non-bipedal and non-humanoid anatomy, creature rigs, mechanical and articulated assemblies, firearm-specific rig and attachment work, measured creature rigs, missing or faulty provider results, and component and prop modeling.

Skeletons, skinning, and skeletal actions that the provider route does not supply are authored live in Blender by the model agent itself through the Blender MCP bridge, iteratively, with visual and deformation review of the real result before it is accepted. The worker saves the accepted result as a job checkpoint for the export and reimport proof steps.

A Meshy-rigged body arrives with its skeleton inside the downloaded provider model, so `prepare_candidate` imports it, and `import_animation_action`, `import_bvh_animation_action`, and `retime_animation_action` bring the provider's actions onto that rig. `import_animation_action` transfers one receipt-verified provider or professional skeletal action onto the target armature by its exact source action id with hash-bound provenance, `import_bvh_animation_action` native-imports and retargets one receipt-verified BVH action with explicit bone chains, root-motion policy, scale and axes, and `retime_animation_action` retimes one already-ingested action between frame rates without changing its motion. `export_animation` and `reimport_export` prove the exported bytes.

An operation that would generate a rig, transfer skin weights automatically, or synthesize an action is outside this surface and must not be introduced.

## No shortcuts in model work

Shortcut work is a failed package, not a simplification to disclose afterwards. Every element this pipeline produces must be authored, reviewed, and evidenced deliberately, and a missing capability is reported as a blocker rather than covered by a shortcut.

This rule covers the whole surface, not only animation: geometry repair, component modeling, materials and textures, skeleton construction, skin weights, and every skeletal action.

- No skeleton, skin weight set, or keyframe may come from repository Python, a declarative spec, a template, or a formula. Bones, weights, and keys are either ingested from the provider route as authored assets or authored deliberately in the live Blender session.
- No incomplete or mismatched rig: no missing limb, spine, neck, finger, jaw, wing, or tail segments, no floating or unweighted bones, no joint placed by guesswork rather than measurement, no humanoid armature carrying nonhumanoid anatomy, and no bone set that cannot reach the poses its actions need.
- No skinning: no unreviewed automatic or bulk weighting, no uncorrected nearest-bone assignment, no rigid single-bone binding across a deforming region, and no weights that were never checked in representative poses.
- No motion: no static pose, no single-frame or transform-only stand-in, no whole-rig translation or rotation presented as an action, no formulaic loop with no role content, no reuse or light retiming of one role's action for another role, and no action copied from another model without real re-authoring on this rig.
- No component: no omitted required element, no painted or flat stand-in replacing modeled geometry, no fused provider weapon or prop kept as the final assembly, and no prop attached through whole-object transforms rather than a real control.
- No evidence: no reuse of another model's renders, previews, measurements, or acceptance, no role reported as validated from a viewport glance, and no pass claimed from file existence without decoded or reimported proof of the delivered bytes.
- No export or runtime: no skipped reimport proof, no entity scale that compensates for authored scale or proportion errors, no baking of a defective rig or action to hide the defect, and no runtime candidate shipped without checking its consumer source bindings.

When the live session cannot produce a required element or role to this standard, stop and report the exact capability or blocker.

## Ownership and completion boundary

Keep `.tools/3d_pipeline/` limited to shared adapters, clients, libraries, wrappers, and maintained tests.
Put unit-specific runners, fixed checkpoint probes, pilot specifications, and repair batches in `.tmp/<task>/` or the owning job workspace; do not embed them in the shared toolchain.
Temporary placement does not relax any authoring, source, licensing, dependency, or approval rule in this skill.

A provider result is a source candidate, a `.blend` is a working artifact, and a `.mesh` or `.anim` is a runtime candidate. Worker completion requires the requested production, review, export/reimport, sound-source, counter, and handoff outputs; the parent completes exact runtime registration and source consumer checks. User-supplied in-game evidence is reviewed when available but never requested or awaited as a delivery gate under AGENTS.md. Do not claim live validation from production or source checks.

The 3D worker may create source files, Blender checkpoints, textures, `.mesh`, `.anim`, sourced unit-audio candidates, mechanically derived audio, previews, manifests, reports, and handoffs. It must not edit gameplay, sound definitions, localisation, `.gfx`, `.gui`, `.asset`, entity, event, focus, decision, country, history, AI, on-action, or spreadsheet files unless the parent grants a narrow exception explicitly. The parent owns runtime identifiers, source wiring, final review, and the overall completion claim. The user performs live consumer validation.

`chaos-redux-event-assets` remains the owner of broad asset inventories, source provenance conventions, texture/DDS conventions, and requirement-to-runtime coverage across asset types. Keep model geometry, model materials, entity wiring, and any separate 2D concept reference distinct. `chaos-redux-frame-animation` governs 2D frame-sheet animation. It does not replace skeletal 3D `.anim` production.

Every new custom unit, custom subunit, creature, vehicle, aircraft, or ship also requires a custom sound-design package, defined under `Custom unit sound-design companion`, and every new custom unit requires new counter art for every counter surface it uses, defined under `Custom unit-counter companion`. For both packages the parent owns final definitions, runtime wiring, and evidence review, and the user performs in-game validation.

Final unit audio is source-only. The worker must never create, synthesize, record, generate, or manually author sound, and must never replace a missing source with test tones, primitive waveforms, placeholder beeps, noise beds, or an unlicensed stock effect. If a suitable sourced file cannot be found and licensed, mark the affected role or package `blocked`.

## Required reading and local calibration

Before 3D work, read the applicable inputs below. Retrieve wiki and installed documentation through the MCP reference workflow in `AGENTS.md`; their paths identify sources and local fallback locations, not an additional manual-reading step:

- `AGENTS.md`.
- `.claude/skills/chaos-redux-event-assets/SKILL.md`.
- `.claude/skills/chaos-redux-subagents/SKILL.md` when a subagent is used.
- `.tools/3d_pipeline/README.md`, `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, and the operation array in `.tools/3d_pipeline/config/dependencies.lock.json` for the adapter surface and job-root rules.
- The parent brief, accepted spec, plan, manifest, job, dependency lock, and handoff.
- The offline Paradox wiki pages relevant to the target surface, especially `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md`.
- Relevant character or interface pages when the target consumes those systems.
- Relevant documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.
- Local vanilla `.mesh`, `.anim`, `.asset`, entity, material, texture, and model precedents for the exact domain, plus existing Chaos Redux model precedents.
- For custom units, the exact installed vanilla sound, voice, soundeffect, and entity precedents used by the closest matching unit surface.
- For custom units, the exact installed vanilla counter consumer, sprite definition, DDS, canvas, frame order, alpha treatment, and closest visual precedent, plus the matching `chaos-redux-event-assets/assets/gfx_references/units/` counter family and contact sheet.

Use existing Chaos Redux paths under `gfx/models/` and `gfx/entities/` as local precedents where applicable, but confirm the final path, shader, material channels, scale, axes, skeleton, action names, and entity structure against the installed vanilla version. Do not lock tutorial values or assume that a nearby asset belongs to the same runtime surface. Treat tutorial polygon counts, texture dimensions, and provider defaults as starting heuristics only. The installed game and latest verified toolchain decide acceptance.

For a humanoid land-unit pilot, this is a hard calibration gate, not a suggestion: import the installed vanilla infantry `.mesh` into the Blender reference collection read-only, identify the exact entity and runtime `scale`, exclude collision-only geometry, and record the measured source-mesh height, effective runtime height, forward axis, ground contact, and the comparison result in the job and manifest. When the custom entity retains the vanilla entity scale, normalize the exported mesh to the measured source-mesh height so the engine applies that scale exactly once. Do not normalize to the effective runtime height and then multiply it by the entity scale again. Do not use a generic real-world height or an arbitrary entity `scale` as a substitute. Keep the provider/animation height and the Blender source-mesh calibration height as separate fields when the provider and HOI4 coordinate spaces differ.

For a static map-building pilot, this is also a hard calibration gate: import the installed vanilla mesh used by the actual building entity, identify the exact `pdxmesh` and entity scale, measure the source dimensions and effective runtime dimensions, and record the reference in the job and manifest. Height-only calibration is invalid for buildings. The current `building` profile uses `facility_land.mesh` with `building_land_facility`, source height `3.4697628021`, entity scale `0.6`, effective runtime height `2.0818576813`, and a hard runtime X/Y footprint ceiling of `4.0` meters. A candidate over that ceiling must be explicitly fit with one uniform X/Y factor and must record before/after dimensions. Silent anisotropic stretching is forbidden.

## Route selection and component completion

Choose the route from the requested operation before provider calls. Geometry generation uses Meshy 7: prepare exactly one item-free body image and a separate item-only image and geometry task for each required firearm or other held item. Download each item independently. For provider-eligible bipedal bodies, try the supported Meshy rig once and each required action once on a usable rig, then ingest the usable results. Blender supplies assembly, rigid item controls, locators, contact corrections, missing components, and fallback rig/action authoring. A static profile needs no skeleton; an articulated asset needs a rig suitable for its anatomy and motion, with provider eligibility determined from the actual body and supported operation, not a mechanical, creature, vehicle, or building label. Repair, assembly, retexturing, export, and explicitly requested rebuild work retain their own required operations; the mere existence of a model never mandates generation or excludes an otherwise appropriate route.

Always create or restore every missing required model component, anatomy element, equipment piece, weapon, or held tool in Blender without renewed approval, preserving intended identity and source-informed design. Record an inventory that maps each required element to its modeled geometry, material, rig/attachment, action usage, and export/reimport evidence. Use verified bounded modeling and authoring operations; absent capability is a blocker, not permission to omit the element or replace it with a static/action alias. The authorization covers required component completion and modest budget-preserving reduction, while other provider/source substitutions retain their separate approval rules. Never store credentials in job files, skill files, manifests, prompts, logs, or handoffs.

### Equipped items are generated separately and animated as an assembly

Meshy is unreliable at a subject holding an object, so a body is never generated with anything in its hands. Every held or equipped item — firearm, melee weapon, tool, shield, staff, banner, instrument, or carried object — uses the separated route, and a provider candidate that already holds an item is historical evidence only. A firearm is the special case of this rule: the item-free body for a firearm unit is a weapon-free body, and that unit's extra requirements are the `fires_in_combat` or `non_firing` declaration, per-firing-state discharge timing, muzzle or weapon locator, particle and light effects, licensed weapon-matched sound, and grip and stock contacts, or the zero-state audit of firing states, effects, locators, and sounds for `non_firing`.

- The body input shows the subject with empty, neutral hands and no held or wielded item, and the body geometry task receives that item-free image alone.
- Each required equipped item is generated through its own Meshy 7 geometry task from exactly one item-only image, firearms under `refs/firearms/<firearm_id>/meshy_input.png` and other items under `refs/equipment/<item_id>/meshy_input.png`. Never submit the body and an item in one task, and never submit two items in one task.
- Archive the identity, proportions, materials, and reference of every excluded item so its item-only input and the Blender fitting reproduce it faithfully, and record the item inventory with its task id, source evidence, and download.
- Attach each item in the live Blender session with rigid controls, real contacts, and the bones, parenting, or constraints the part needs. An item attached through a whole-object transform, or left fused in a provider result, does not satisfy this route.
- Animate the assembled model. Provider actions authored for an empty-handed body are a source candidate, not the final equipped performance: author and review the grip, carry, aim, discharge, recoil, recovery, and retention behaviour of every role on the assembled model, per frame, and re-check the item's contacts through the whole action. Detached item animation, where the body alone is animated and the item is parented afterwards, fails acceptance.
- Report each item's provider task, input proof, attachment evidence, and per-frame contact validation in the manifest.

## Hard start gates
These gates run before any provider call, paid operation, or export. They cover: the `MESHY_API_KEY` check for provider-dependent work (Blender-only repair needs no key and makes no provider call); verification of the exact Blender build, repository-owned `chaosx_blender_hoi4` adapter, checksum-locked `io_pdx_mesh` archive, and the Meshy 7 route against `.tools/3d_pipeline/config/dependencies.lock.json`; compatibility-wrapper integrity and probe-process cleanup; standing authorization for live Blender rig, weight, and skeletal action work wherever the provider route does not apply; the nonhumanoid `scale_crosswalk` preflight; and adapter publication coherence between the adapter config and the lock. A required route, schema, version, or checksum that cannot be verified is reported as `required installation/verification` or `blocked`, never replaced by an invented tool or unverified route.

Read the complete requirements in [Hard start gates](references/start-gates-and-adapter.md#hard-start-gates) before this work.

## Job intake and deterministic layout

Validate the job before any paid work. The parent must provide:

- event or system owner, stable asset ID, and lowercase asset slug
- one ready reference image path, or enough brief input for the documented modern-designed-artwork source search and one source-informed model-ready image-generation preparation (Claude Code: the gptimage MCP generate_image tool with reference_images, one image per call, each reference's role stated in the prompt, alpha verified on the saved PNG; Codex: native ImageGen) on a separate derivative. The intake must include the source-style decision, the selected `pose_preparation_mode`, and a source-free reference remains a separate explicit fallback only after documented search failure
- source mode (`licensed_search` or `reference_only_user_authorized`), immutable Internet source path or documented search record, source URL/page, title, creator/publisher, stated license/terms, retrieval date, provenance/rights and AI-use status, explicit user authorization where reference-only use is required, exact image-generation prompt, source-to-prepared comparison, pose mode or `pose_preparation_mode = none` with its reason, and parent approval evidence
- one asset profile declared in `.tools/3d_pipeline/config/asset_profiles.json`
- geometry intent, required components, forbidden additions, texture direction, and unseen-side/rear-geometry policy
- a hard style-preflight result that rejects anime, manga, manhwa, chibi, cel-shaded anime-game-character, exaggerated anime facial or body proportions, and similar anime-derived presentation while keeping grounded professional fantasy, horror, tabletop, and game concept illustration eligible when it is not anime-derived
- for every firearm-bearing unit, an explicit `fires_in_combat` or `non_firing` declaration. The body Meshy input must be the item-free body, which for a firearm unit is weapon-free, with source firearm identity archived for a separate firearm-only Meshy 7 task; assembled firing actions must pass grip, stock, muzzle, and recoil/contact gates, while a declared non-firing unit receives no firing effects
- period-fit declaration for the event or system, including every explicitly intended anachronistic, electronic, advanced-optical, plastic, modern-tactical, or science-fiction element. Absent an explicit exception, the source must fit the 1936-1945-era world
- color status and palette direction. Black-and-white, grayscale, desaturated monochrome, clay-render, and untextured sources require an approved faithful image-generation colorization before Meshy, while already colored sources retain their exact palette
- named vanilla reference paths and the expected scale relationship
- for buildings, the measured runtime footprint budget and whether the consumer is a dedicated provincial map building or a state-level gameplay building with a provincial visual anchor
- required action roles with their in-place or root-motion policy, the required bone set or anatomy map, the runtime consumer, baseline paid provider operations including the humanoid rig task and the preset-action or Text-to-Motion animation tasks, live balance and preflight records, the provider ingestion route and the live Blender authoring route for every asset the provider route does not cover, the requested operation and its route selection, and exact capability and budget stop conditions. Every firing role and state must have a discharge synchronization crosswalk, and a `non_firing` declaration must exclude firing roles and states
- for every custom unit, a sound-design brief with a mandatory selection role plus applicable acknowledgement, movement, idle or engine loop, attack, impact, special-action, and death or destruction roles, the selected vanilla precedents, the exact selection consumer, and animation synchronization points
- for every custom unit, a counter brief naming each exact runtime counter consumer, token, required state and size, final sprite and DDS path, inspected installed-vanilla definition and texture paths, matching skill-local counter reference family, and `chaosx_icon_artist` handoff path
- the locked provider, Blender, adapter, and `io_pdx_mesh` dependencies
- the deterministic job root and exact handoff path

When the parent does not supply a root, derive it from the resolved repository root, a normalized stable owner id, and a normalized asset slug:

```text
docs/assets/<owner_id>/models_3d/<asset_slug>/
  job.yaml
  manifest.md
  history.jsonl
  refs/
    source/
      untouched.<ext>          # immutable selected or user-supplied source; evidence only
      provenance.json
      source_search.md         # required when no authoritative source is supplied
    original/
      meshy_input.png        # the only image sent to Meshy
      input_manifest.json
    firearms/<firearm_id>/
      meshy_input.png        # one firearm-only image per required gun
    equipment/<item_id>/
      meshy_input.png        # one item-only image per other required equipped item
    derived/                  # prepared image-generation derivatives, comparisons, and processing evidence
    briefs/
  provider/
    requests/
    responses/
    tasks/
    credits/
    downloads/
    rejected/
  blender/
    source/
    reference/
    working/
    checkpoints/
    previews/
    reports/
  textures/
    source/
    processed/
    dds/
  export/
    mesh/
    anim/
  validation/
  evidence/
  logs/
  runtime/
    handoff.md
    crosswalk.md
```

Use the same derived path every time and pass job-relative paths to provider and adapter calls after root-containment checks. Do not use chat assumptions, timestamps, random IDs, pilot names, or workstation paths as the primary path. Keep append-only task history, manifest state, copy provenance, and dependency records inside the job root. Never archive secrets. Final runtime files must not remain runtime-referenced from `docs/assets/`.

Keep the job root small, because every repair round otherwise adds gigabytes. When a stage is accepted, delete the superseded `.blend` checkpoints and working copies except the accepted one and its immediate predecessor, every `.blend1`/`.blend2` and `.signs_orig` file, preview and phase renders of rejected or superseded candidates, and adapter logs of operations that succeeded; keep one contact sheet per accepted action set as the review record. Never delete provider downloads, refs, the accepted export and texture set, manifests, handoffs, receipts, or audio and counter sources, because those cannot be regenerated. When a job is closed, its handoff names the kept checkpoint and the cleanup it performed.

Read and write job YAML, JSON receipts, and Markdown handoffs with explicit UTF-8, preserving the existing BOM and line endings.
Write metadata updates to a new sibling, parse and validate their required fields and array shapes, then replace the original; an unsupported parser option or failed parse must never overwrite a good receipt with null or `{}`.
If evidence metadata is recovered, mark it reconstructed and name the surviving measured inputs; leave lost fields unavailable instead of inventing them.

When `owner_id` identifies an event, the model job belongs under that event's temporary `docs/assets/<event_id>_<event_slug>/models_3d/<asset_slug>/` evidence workspace. Keep source files, checkpoints, exports, manifests, QA evidence, and handoffs there while work is active, blocked, awaiting review, or undergoing acceptance scenarios. Before the event goal is genuinely complete, promote durable provenance, licensing, QA/reimport results, crosswalk facts, and runtime-handoff facts into permanent event, plan, spec, or other owner-approved documentation, place final runtime files in engine-facing folders, verify that no runtime reference points into `docs/assets/`, then delete the complete event-scoped workspace. Never delete skill-local references, durable portrait archives, or another event's workspace. Retain this workspace for blocked or incomplete work and report the blocker.

## Reference images
Every model starts from actual Internet-sourced modern designed artwork (game, tabletop, fantasy or horror, and professional creature design art; never archival photographs, historical works, or anime-derived presentation) that passes provenance, rights, AI-use, and 1936-1945 period-fit review. The source is immutable evidence, and all preparation such as colorization, pose cleanup, and item exclusion happens on separate derivatives. Each Meshy geometry task receives exactly one approved, fully colored, full-subject image, either the item-free body or one item-only image, and never a board, sheet, or turnaround. A portrait-inspired unit also needs the portrait fidelity gate with explicit parent or user acceptance before any paid call. If no eligible source survives review, mark the job `needs_user_review` or `blocked`; a source-free reference needs explicit approval.

Read the complete requirements in [Reference images](references/reference-images.md#reference-images) before this work.

## Provider generation and lineage

For a new model, the provider sequence is:

```text
verified balance -> image-to-3D -> status -> immediate download
                 -> optional remesh/retexture
                 -> Meshy rig task for a provider-eligible bipedal body
                 -> Meshy preset actions or Meshy Text-to-Motion
                 -> receipt-verified ingestion onto the rig
                 -> live Blender authoring for every asset the provider route does not cover
                 -> deformation/visual QA -> PDX export/reimport
```

Each provider stage keeps its own task id, credit preflight, reconciliation, and download record, and a paid rig or animation attempt is not repeated. Meshy keeps task outputs only three days (signed URLs expire after three days and later status calls return not found), so download every GLB, FBX, texture and motion file the moment its task succeeds and record its SHA-256; an unrecorded or undownloaded task cannot be recovered. Provider results are ingested into the job through the ingestion operations listed under `Adapter publication`.

Failed geometry generation, remesh, retexture, or conversion retains the authorized provider-recovery path while balance and verified capability permit it. A rig result or an action result that the provider cannot deliver to this standard is repaired in the live Blender session or reported as the exact blocker, under the generation policy in `Skeleton, skinning, and action policy`. Inspect the live schema and balance before paid calls, preserve estimates and task/response IDs, and never expose the API key. Do not promise a general geometry prompt when Image-to-3D exposes only texture-direction text.

Before a humanoid source over 300,000 triangles reaches `meshy_remesh`, every job manifest and generated spec must declare the verified `remesh_estimate_credits = 5` estimate, or the loader must apply and materialize that verified default. The runner must never index an undeclared `remesh_estimate_credits` key.

Use **Meshy 7** as the only image-to-3D generation model. Require the verified repository-owned route to expose the exact `meshy-7` identifier and record it in task evidence. Never silently downgrade or use a model alias. If Meshy 7 is unavailable or incompatible, stop with `needs_user_review` or `blocked`.

The ordinary planned paid path is pre-authorized. Do not ask for confirmation before the initial model generation, before planned remesh, retexture, and conversion calls belonging to the accepted brief, or before the planned humanoid rig task and its planned animation tasks. Check the live balance before each batch of paid operations and record estimates, operations, attempt numbers, and consumed credits, but routine credit use and balance checks are not confirmation gates.

For the live locked Meshy MCP route with `ai_model=meshy-7`, `enable_pbr=true`, and `should_texture=true`, require a live cost/preflight record before the image-to-3D call and reconcile it with the response and post-call balance. The documented textured Meshy-7 charge is 30 credits. Never use the upstream MCP package's stale 20-credit prose for planning or reconciliation.

When geometry recovery is authorized, keep the rejected task, responses, downloads, and QA evidence immutable. Give the retry an explicit attempt-scoped provider stage such as `generation_recovery_2`, and derive its model filenames, extracted texture directory, credit preflight, selected task, and every downstream Blender source from that stage. Never let a generic `generation` task or filename select a rejected predecessor. Do not use broad response-name recovery for an attempt-scoped stage because provider response filenames do not encode the logical attempt. Resume it only from its exact task record. Preserve the earlier evidence in place rather than renaming, deleting, or overwriting it.

For geometry, remesh, retexture, or conversion recovery, do not repeat an identical input after two failures. Where separately authorized and supported by the official MCP schema, `model_url` may use an official `https://assets.meshy.ai/` artifact URL from the immutable completed source-task record; bind it to that source, redact signed URLs, and retain its own attempt record. Do not use URL substitution, changed identifiers, or a new stage name to bypass the provider attempt and recovery rules.

Prefer smart topology when suitable, triangular output, PBR maps when textures are required, and removal of baked lighting when supported. A humanoid body reference should depict a complete readable body. Each equipped item is generated through its own Meshy 7 geometry task from one item-only prepared image, then imported into Blender for scale, topology, material, fit, attachment, locator, and contact work under `Equipped items are generated separately and animated as an assembly`. Use image generation on a separate derivative to attempt a neutral T-pose or A-pose when feasible, while retaining the original pose with `pose_preparation_mode = none` and a recorded reason when neutralization would break required body anatomy or intended identity. Use the suitable provider pose or `none` for static or mechanical assets. Download every successful artifact immediately, retain the GLB as the canonical provider archive, retain FBX when a downstream route needs it, and record exact arguments, provider version, task IDs, request/response lineage, credits, and local download paths. Remote URLs are never the only accepted copy.

Treat every provider result as a candidate. Review textured/untextured, wireframe, and relevant front/rear/side/top/underside views for identity, topology, anatomy, and component completeness. Author or restore missing required components and repair detached, fused, or broken geometry in Blender without renewed approval, preserving intended identity and source evidence. Regenerate only when a usable body or separate firearm candidate cannot be repaired through verified operations. Item-free bodies intentionally omit equipped items until the separately generated item assets are fitted and attached in Blender; the assembled candidate must contain every required element before acceptance. Do not spend provider credits on a rejected geometry candidate. Preserve all candidate lineage.

Tutorial values near 10,000 vertices and the 25,000–30,000 caution band are seed heuristics only. Local vanilla calibration and measured runtime evidence decide the profile target.

## Skeletal authoring gate

Required articulated motion needs real bones, skinning, and authored skeletal actions. Use the verified live authoring session for unsupported or unusable provider results.
Read the complete requirements in [Skeletal authoring gate](references/blender-processing-and-export.md#skeletal-authoring-gate) before this work.

## Blender processing and checkpoints

Preserve provider originals and work in staged Blender checkpoints with the required dependency and topology checks.
Read the complete requirements in [Blender processing and checkpoints](references/blender-processing-and-export.md#blender-processing-and-checkpoints) before this work.

## Geometry, materials, rigging, and actions

Complete all required components, calibrated geometry and PDX materials, weights, semantic actions, contacts, and family consumers.
Read the complete requirements in [Geometry, materials, rigging, and actions](references/blender-processing-and-export.md#geometry-materials-rigging-and-actions) before this work.

## Custom unit-counter companion

Every custom unit needs bespoke counters for all of its runtime surfaces, using exact installed-vanilla definitions, DDS references, and the matching reference family.
Read the complete requirements in [Custom unit-counter companion](references/unit-audio-and-counters.md#custom-unit-counter-companion) before this work.

## Custom unit sound-design companion

Every custom unit needs legally usable Internet-sourced audio with selection and applicable action roles, exact attribution, and animation synchronization. Generated or placeholder audio cannot satisfy this contract.
Read the complete requirements in [Custom unit sound-design companion](references/unit-audio-and-counters.md#custom-unit-sound-design-companion) before this work.

## PDX export and reimport evidence

Export and reimport the actual deliverables, checking skeleton, materials, scale, and action coverage before handoff.
Read the complete requirements in [PDX export and reimport evidence](references/blender-processing-and-export.md#pdx-export-and-reimport-evidence) before this work.

## Evidence package and handoff

The job package must contain, as applicable:

- job intake and append-only history
- selected source and source-informed model-ready preparation or documented failed-search fallback, preflight, non-anime style decision, source URL/page, title, creator/publisher, stated license/terms, retrieval date, provenance and AI-use decision, explicit user authorization, declared period-fit review and intentional exceptions, source color status, palette direction, colorization evidence when applicable, preparation prompt, source-to-prepared comparison, `pose_preparation_mode` and reason, parent approval, and evidence that any archived source bytes are non-shipping
- for every firearm-bearing unit, firearm/body route selection, `fires_in_combat` or `non_firing`, weapon-free prepared-body proof and separate firearm-only input/task records when generating that geometry, complete prop inventory, the provider body rig and its ingested action lineage, Blender fit/attachment and contact evidence, and assembled per-frame trigger-hand, support-hand, stock/shoulder, muzzle and recoil checks. Every firing state requires discharge timing, locator, synchronized effects/light, licensed weapon-matched sound; `non_firing` records zero firing-state/effect/sound requirements
- provider requests, responses, task IDs, versions, balance, credits, downloads, and retained passing outputs
- requested operation and route selection, the complete required-component inventory and added-geometry/prop provenance, the provider rig and animation tasks with their exact source action ids and provenance receipts, the ingestion or live Blender authoring session record, exact adapter operations and arguments, rig/weight/action checkpoints, and before/after deformation and role-motion review
- source and checkpoint `.blend` files
- geometry, material, rig, weight, action, and export reports
- source and final textures, animation previews, `.mesh`, and `.anim`
- immutable Internet-sourced unit audio candidates, licensing records, derived files, and transformations
- export/reimport evidence, manifest, and requirement-to-runtime crosswalk
- a runtime handoff with proposed stable names, paths, material/shader mapping, action mapping, and the exact files/identifiers the parent must wire
- for every custom unit, a sound-design handoff with sourced audio files, source URLs, attribution, licensing evidence, sound roles, voice direction where applicable, vanilla precedents, animation synchronization points, proposed runtime identifiers, and remaining parent-owned wiring
- for every custom unit, a counter handoff with inspected installed-vanilla definitions and DDS files, matching skill-local counter family, exact consumers and tokens, required frames/states/sizes, original counter-art paths, final DDS paths, sampled vanilla green evidence, comparison evidence, proposed sprite definitions, and remaining parent-owned wiring
- for static buildings, footprint/scale evidence, meshsettings object-name evidence, dedicated spawn or provincial-anchor evidence, and runtime-consumer evidence

Each model manifest entry records the asset ID/slug, profile, source mode, source reference, source URL/page, title, creator/publisher, stated license/terms, retrieval date, explicit authorization where applicable, provenance and AI-use decision, non-anime style-gate status, declared period fit and every intentional exception, source and final color status, palette direction, colorization prompt/comparison/approval when applicable, source-informed preparation prompt, route selection, weapon-free input proof where applicable, missing-component inventory, Blender-authored component/prop and attachment evidence, source-to-prepared comparison and approval, `pose_preparation_mode` and reason, firearm intent (`fires_in_combat` or `non_firing`) and explicit complete-weapon, trigger-hand, support-hand, stock/shoulder, and muzzle-continuity results when applicable, provider lineage, the provider rig task and animation tasks with their exact source action ids and provenance receipts, selected candidate, the ingestion or live authoring session and accepted checkpoint, geometry counts, objects/materials, armature/bones, actions/frame data, explicit `attack`, `defend`, `support_attack`, and additional-state discharge and muzzle/effect/sound synchronization rows or a zero firing-state/effect/sound audit for `non_firing`, custom-unit sound requirements and synchronization points, custom-unit counter consumers, installed-vanilla counter references, sampled green evidence, bespoke counter handoff and status, source/final textures, exports, exporter version/settings, proposed runtime identifiers, actual runtime registration only after parent wiring, live consumer, user-provided in-game evidence only after parent review, and status. Use `complete`, `needs_user_review`, `blocked`, or `canceled`. Never create a fallback completion state.

For nonhumanoid/creature jobs, `manifest.md` and `runtime/handoff.md` must repeat the measured numeric scale crosswalk, dedicated rig route, `scale_crosswalk_status`, `rig_route_status`, provider/export route status, and the exact blocker text for every unavailable or pending route. A bare `blocked` or `pending` label is insufficient.

When the event/system owner and slug are known, place the subagent handoff under the parent-provided `docs/plans/<owner_id>_<owner_slug>_plans/subagent_handoffs/` path. The parent must review every artifact and either wire it, queue it with a reason, reject it with a reason, or carry its blocker forward.

### Runtime copy synchronization

Treat the selected source exports, staged runtime copies, and active consumer files as separate surfaces. A runtime file can be stale or be overwritten by an older mapped texture even when the current source export is correct. Select the final geometry, material maps, and actions first, then lock the selected source paths in the manifest before synchronizing any runtime copy. Record each source and destination path, source and destination SHA-256, copy tool or actor, copy time, and provenance link, then compare destination hashes after synchronization. Never synchronize from an older provider or processed path, never let a filename alone choose the source, and never synchronize before final source selection. The parent owns active runtime copies, `.asset`, entity, `.gfx`, gameplay wiring, and live consumer bindings. The user supplies in-game screenshots and live validation. The worker owns the evidence and exact handoff needed for parent wiring and review.

## Bounded subagent route

Use `chaosx_3d_model_pipeline` only when the parent provides the exact job root, approved source or model-input paths, output folders, handoff path, profile, named vanilla references, scale relationship, required actions with their rig map and root policy, custom-unit sound roles and Internet-source requirements, custom-unit counter consumers and tokens, inspected vanilla counter definition/DDS paths, matching skill-local counter family, counter-artist handoff path, synchronization requirements where applicable, source mode and permissions, dependency lock, and forbidden simplifications. The subagent's production scope, including crosswalk rows and handoffs, and its ban on final gameplay, GFX, entity, sound-definition, localisation, and spreadsheet wiring are the ones in `Ownership and completion boundary`, and the user performs live consumer validation and supplies in-game evidence.

### Source eligibility in the prompt

The prompt must require the source, style, and period gates stated in `Designed-artwork source-first reference gate`, including the `reference_only_user_authorized` path, the `NoAI` and no-derivatives rejections, and the eligible non-anime source families. The prompt must also declare the event or system's period boundary and every explicitly intended exception.

### Firearm route in the prompt

For every firearm-bearing unit, the prompt must carry the route in `Route selection and component completion` and the input rules in `Equipped items are generated separately and animated as an assembly`, and must declare `fires_in_combat` or `non_firing`. Require independent body and item task IDs, credits, downloads, source-identity comparisons, the Meshy rig task for the body, the Meshy preset-action or Text-to-Motion tasks, receipt-verified ingestion of every transferred action, rigid-control attachment, and completion of all missing specified parts without renewed approval. Require grip, stock, and muzzle contact; aim, discharge, recoil, and recovery phases; independent `attack`, `defend`, `support_attack`, and additional firing-state timing, locator, particle/light, licensed sound, and synchronization rows; and, for `non_firing`, retained equipment with the zero firing-state/effect/sound audit.

### Prepared-input evidence in the prompt

The prompt must require the prepared-input gates in `Designed-artwork source-first reference gate` and `Exactly one reference image per Meshy geometry task`. Colorization may accompany authorized item exclusion, pose cleanup, and source-informed body restoration; preserve the intended identity, material distinctions, and non-anime style, and record source/final color status, prompt, comparison, and parent review. For a selected source, image generation must create one source-informed model-ready derivative with a full colored body, an identity- and period-appropriate palette, a suitable transparent or plain background, and non-anime style. Preparation may strip equipped items, restore obscured or missing body detail, and normalize to a useful T-pose or A-pose without preserving source item contacts. Archive the identity of every excluded item and its reconstruction references for Blender. Complete all missing specified model elements through the authorized Blender route rather than accepting omissions, and record the prompt, source-to-prepared comparison, pose mode, reconstructed and excluded elements, and parent review. Sources and prepared references remain non-runtime evidence.

### Failed search and provenance in the prompt

If the documented search across eligible artwork families finds no suitable source, mark the reference `needs_user_review` or `blocked`, and hold the source-free from-scratch fallback to the separate approval gate in `Designed-artwork source-first reference gate`. Record that section's provenance and archival fields, including the exact image-generation preparation prompt, the source-to-prepared comparison, and `pose_preparation_mode` with its reason.

### Provider tasks and context in the prompt

Each Meshy 7 geometry task must receive exactly one approved, fully colored source-informed image under the paths in `Exactly one reference image per Meshy geometry task`; sources and comparison sheets remain evidence only. The provider sequence is the one in `Provider generation and lineage`; the route, separate item generation, ingestion onto the rig, live fitting and attachment, and Blender-only operations are the ones in `Route selection and component completion` and `Equipped items are generated separately and animated as an assembly`. All missing required model components are authorized Blender completion work without renewed approval. Keep geometry-recovery rules, live credit preflight for provider calls, and recorded attempt/source lineage. Put every needed conversation constraint into the prompt or named repository files.

## Final state and fallback disclosure

Mark each requested 3D requirement as `complete`, `needs_user_review`, `blocked`, or `canceled` in the package. A requirement produced through a shortcut is not `complete`: mark it `blocked` or `needs_user_review` and name the shortcut that was avoided. For a custom unit, the package must also record the sourced sound candidates, licensing evidence, synchronization handoff, bespoke counter package, installed-vanilla counter inspection evidence, and parent-owned audio/counter wiring status. A package-level `complete` means the worker's requested source, processing, export, sound-source research, counter handoff, and evidence outputs are present. It does not mean the Chaos Redux runtime feature is complete. Report every omitted component, rejected candidate, unverified capability, budget stop, missing reimport proof, missing sound source, missing counter, and proposed static companion explicitly. Never hide a simplification behind a successful export or a parent-owned runtime handoff.
