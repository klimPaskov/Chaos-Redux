# Chaos Redux 3D Model Workflow Planning Package

This package specifies a reusable autonomous workflow for creating Hearts of Iron IV 3D assets. It can generate its own single Meshy-ready reference image when the user provides only an asset brief, and then continue through Meshy, Blender, and Paradox export. Meshy AI creates the first model and may create a humanoid rig and library animation. Blender performs topology cleanup, scale, orientation, custom rigging, action cleanup, PDX material construction, and Paradox export. The wider workflow produces the entity handoff, reimport proof, in-game evidence, and completion audit.

The package is planning and bootstrap material. It does not claim that Meshy, Blender, or the Paradox exporter were installed on the user's machine from this hosted environment. The included scripts are designed for a future local implementation pass and use explicit apply flags.

## Locked design decisions

- One final reference image is the standard Meshy input. If the user does not provide one, the workflow must generate one autonomously before Meshy starts.
- Additional instructions guide reference preparation, texture prompting, quality checks, rig choice, animation requirements, and Blender processing. The current single-image Meshy endpoint does not expose a general geometry text prompt, so geometry instructions are acceptance criteria rather than a promise that Meshy will follow arbitrary shape edits.
- Meshy auto-rigging is used only for textured humanoid bipeds with clear limbs.
- Creatures, vehicles, buildings, weapons, and unusual bodies use Blender custom rigs when animation is required.
- Meshy output size is provisional. Blender owns final scale and orientation against a named vanilla or approved Chaos Redux reference.
- Triangle topology is required for the final production mesh.
- The tutorial's roughly 25,000 to 30,000 vertex range is treated as a review envelope, not as a proven engine hard limit. Every asset profile must be checked against a comparable vanilla model.
- No paid retry loop runs without a configured attempt budget.
- Meshy receives exactly one clean final reference image. Do not create a multi-view board, turnaround sheet, or separate side-profile images for Meshy.
- The workflow resolves or creates its own deterministic job paths and working folders from the repository structure and asset slug.
- The workflow must not begin until `MESHY_API_KEY` is present as an environment variable and Meshy availability has been checked.
- No silent provider switch, rigging substitution, topology simplification, missing animation, placeholder texture, or unverified export is allowed.
- Every completed asset keeps source provenance, Meshy task identifiers, generated files, Blender source, final PDX files, manifests, screenshots, and a runtime handoff.

## Package map

- `PACKAGE_VALIDATION.md` records completed structural checks and the remaining local pilot gates.
- Numbered root documents `00` through `14` define architecture, installation, profiles, rigging, state transitions, security, output layout, and completion proof.
- `research/`, `references/`, and `mcp/` record source reading, current external research, catalog demand, tool mapping, and security constraints.
- `proposed_skill/` contains the proposed reusable Chaos Redux skill.
- `proposed_subagent/` contains the proposed production subagent.
- `config/` contains environment, MCP, pipeline profile, and job examples.
- `schemas/` contains JSON Schemas for model jobs and model manifests.
- `prompts/` contains reusable request, Meshy, Blender, audit, implementation, and goal prompts.
- `bootstrap/`, `wrappers/`, and `tools/` contain the dry-run-first bootstrap material, tool wrappers, and package-local tool notes.
- `templates/` contains manifest, HOI4 handoff, and QA report templates.

## Recommended implementation order

1. Review `PACKAGE_VALIDATION.md`, `01_system_architecture.md`, `02_mcp_installation_and_security.md`, and `09_failure_recovery_cost_and_security.md`.
2. Review the bootstrap material under `bootstrap/` before any local installation work.
3. Run one static prop pilot and one animated humanoid pilot before enabling batch work.
4. Inspect the required offline Paradox wiki pages, local HOI4 documentation, vanilla model files, and a direct vanilla model precedent during the pilot.
5. Promote the skill and subagent files into the repository only after the pilot proves the exact Blender and exporter versions.
6. Use the auditor before any asset is marked complete.

## Primary deliverable

The intended result for one job is a self-contained model package with:

- reference image and source-rights note
- Meshy request settings and task IDs
- raw GLB or FBX outputs and textures
- reviewed Blender file
- final DDS textures
- final `.mesh` and `.anim` files where required
- entity and model runtime handoff
- static and animated viewport captures
- in-game scale and animation captures
- machine-readable manifest and QA report
