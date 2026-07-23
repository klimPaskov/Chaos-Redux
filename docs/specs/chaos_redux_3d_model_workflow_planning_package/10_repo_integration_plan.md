# Repository Integration Plan

## New workflow owner

Create one reusable skill:

```text
.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md
```

Create one bounded asset-production subagent alongside the existing custom subagent definitions:

```text
chaosx_3d_model_pipeline.toml
```

The proposed files are included under `proposed_skill/` and `proposed_subagent/`.

## Ownership boundaries

### 3D pipeline skill owns

- single-reference 3D job intake
- Meshy generation, remesh, texture, humanoid rig, and animation candidate workflow
- Blender geometry cleanup and normalization
- armatures, weights, and actions
- PDX material preparation
- `io_pdx_mesh` verification and export
- 3D manifests, previews, QA, and runtime handoff
- 3D dependency locks and adapter contracts

### `chaos-redux-event-assets` continues to own

- broad asset requirement inventory
- 2D unit concept references and equipment art
- source-mode rules for real or fictional visual references
- DDS and manifest conventions that also apply to model textures
- requirement-to-runtime coverage across all asset types

It should route a final 3D model request to the new 3D skill and subagent rather than treating a concept image as a finished model.

### `chaos-redux-frame-animation` continues to own

- 2D frame-sheet animation
- animated icons, portraits, and UI sprites

It does not own skeletal 3D `.anim` production. Cross-reference the new skill so agents do not apply the 2D per-frame rule to a skeletal model action.

### Main implementation agent owns

- final `.asset`, entity, equipment, unit, building, GUI, event, focus, decision, country, and localisation source changes
- final runtime identifiers
- final in-game validation
- completion claims

### 3D subagent must not edit

- gameplay files
- localisation
- `.gfx`, `.gui`, `.asset`, or entity files unless the parent explicitly expands scope
- spreadsheets
- unrelated assets

It produces final model files and a handoff that lets the parent wire them without guessing.

## Proposed repository paths

```text
.agents/skills/chaos-redux-3d-model-pipeline/
  SKILL.md
  references/
  templates/

.tools/3d_pipeline/
  adapter/
  blender_scripts/
  schemas/
  config/
  wrappers/
  bootstrap/
  tests/

config or MCP-host project file
  project-scoped Meshy and Blender entries

docs/assets/<event_id>_<event_slug>/models_3d/<asset_slug>/
  source and evidence package

gfx/models/<domain>/<event_id>_<event_slug>/
  final runtime files when the local engine precedent permits this layout
```

The final `gfx/models` path must be confirmed against local vanilla and existing Chaos Redux model paths. Engine-required root placement overrides the event-scoped preference and must be documented.

## Documentation changes

### `AGENTS.md`

Add concise routing rules:

- use `chaos-redux-3d-model-pipeline` for custom units, buildings, vehicles, aircraft, ships, creatures, skeletal animations, and PDX export
- use `chaosx_3d_model_pipeline` for bounded production
- Meshy and Blender MCP guidance remains in the owner skill, not a central MCP router
- all exact budgets and exporter rules require local vanilla and documentation review
- final completion requires in-game evidence

### `chaos-redux-event-assets`

Add:

- route 3D model requirements to the new skill
- distinguish 2D equipment/model reference art from final 3D geometry
- add 3D manifest fields for mesh, armature, action, material, entity handoff, and runtime consumer
- preserve source, processed texture, final DDS, and coverage rules

### `chaos-redux-subagents`

Add:

- the new subagent's scope
- required context-free prompt fields
- patch and handoff boundaries
- no gameplay wiring by default
- no fallback or completion authority

### `chaosx_skill_maintainer`

Use this existing agent to review and apply the new skill plus routing updates. It should not add event-specific content.

## Parent prompt contract for the 3D subagent

A complete prompt includes:

- event or system ID and slug
- asset slug and purpose
- exact reference image path
- provenance and license status
- asset profile
- final source package path
- proposed runtime folder
- target vanilla reference paths
- expected scale relationship
- material and texture direction
- required action roles
- source-mode permissions
- credit budget and attempt ceiling
- Meshy and Blender dependency locks
- required handoff path
- explicit forbidden simplifications
- `fork_context=false`

If these inputs are missing, the subagent reports the missing fields rather than exploring the whole repository.

## 3D manifest extensions

Every model entry should include:

- asset ID and slug
- profile
- source reference and checksum
- provider task IDs and versions
- source GLB and FBX
- selected candidate
- `.blend` checkpoint
- triangle and vertex counts
- object and material counts
- armature and bone counts
- action list and frame data
- source and final textures
- final `.mesh` and `.anim` files
- exporter version and settings
- proposed runtime identifiers
- actual runtime registration after parent wiring
- live consumer
- in-game evidence
- status

## Handoff location

When the event ID and slug are known:

```text
docs/plans/<event_id>_<event_slug>_plans/subagent_handoffs/
  <asset_slug>_3d_model_handoff.md
```

The source asset package remains under `docs/assets/.../models_3d/`.

## Runtime registration workflow

1. The 3D worker inspects a named local precedent.
2. It proposes stable file and action names.
3. It exports and creates `runtime/handoff.md`.
4. The main agent adds runtime source definitions.
5. The main agent writes exact registration and consumer IDs into the crosswalk.
6. The main agent validates in game.
7. The manifest status changes from `handed_off` to `wired`, then `complete` only after evidence.

## Catalog and documentation impact

The event catalog workbook remains owned by the spreadsheet worker. A 3D asset should appear in event docs, manifests, or spreadsheet text only when it is relevant to the player-facing event description or asset coverage. The 3D subagent does not edit the workbook.

## Existing catalog relevance

The supplied event catalog includes ordinary, military, supernatural, nonhuman, technological, environmental, and world-end content. The workflow therefore cannot be optimized only for human infantry. Profile support for buildings, creatures, vehicles, aircraft, naval models, and strange articulated assets is part of the first design, even if implementation is promoted in stages.

## Proposed AGENTS routing snippet

```text
- Use `chaos-redux-3d-model-pipeline` when a task creates, rigs, animates, converts, exports, audits, or documents a custom HOI4 3D model for a unit, building, vehicle, aircraft, ship, creature, or articulated asset.
- Use `chaosx_3d_model_pipeline` for bounded 3D asset production. The subagent may create source models, Blender files, PDX materials, textures, `.mesh`, `.anim`, previews, manifests, and handoffs. The main agent owns final runtime source wiring and in-game completion.
- Meshy and Blender MCP servers are privileged dependencies. Use the versions, allowlisted adapter, secret handling, cost gates, and evidence rules in the 3D pipeline skill. Do not expose unrestricted Blender Python to unattended production work.
```
