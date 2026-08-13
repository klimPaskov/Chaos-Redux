# Source Register

## Review completion

Every project source supplied with the task was read in full before this package was written. No supplied source was skipped.

## Project sources

| Source | How it informed this package |
| --- | --- |
| `AGENTS(3).md` | Repository authority, required local references, coding and documentation rules, completion proof, no silent fallback, subagent ownership, and source-of-truth rules |
| `CHAOS_REDUX_MECHANICS(3).md` | Scale of the project, event architecture, major-event presentation, dynamic systems, and the range of unusual unit or object concepts the asset pipeline must support |
| `Pasted text(6).txt` | User request and tutorial transcription for Meshy generation, geometry inspection, remeshing, triangular topology, Blender import, scale, rigging, IK, weights, PDX materials, and animation |
| `chaos-redux-event-assets(3).md` | Asset manifests, source and processed files, runtime placement, requirement-to-runtime crosswalks, unit-visual separation, DDS handling, and asset completion rules |
| `chaos-redux-event-planning(4).md` | Asset-class planning, country and unit package depth, animation planning, dynamic identity, source modes, and implementation-ready specification standards |
| `chaos-redux-events(3).md` | Parent integration ownership, event-linked assets, docs, runtime consumers, validation, and completion expectations |
| `chaos-redux-frame-animation(3).md` | Evidence discipline for animated work, source versus preview distinction, static fallbacks, state semantics, and wiring handoffs. The 3D pipeline adapts these principles without treating a GIF or frame sheet as the runtime 3D animation format |
| `chaos-redux-improvement-loop(3).md` | Anti-bloat rule, closure conditions, playable depth, visual state design, and the need to connect assets to real mechanics |
| `chaos-redux-subagents(3).md` | `fork_context=false`, narrow role ownership, required handoffs, asset routing, patch boundaries, and parent responsibility |
| `chaos-redux-super-events(3).md` | Complete-package thinking, source verification, unique runtime assets, and no placeholder completion |
| `chaos-redux-decisions-missions(3).md` | Clear visible costs and requirements, state-driven UI, no passive reward-store design, and task-specific validation principles |
| `chaos-redux-focus-trees(10).md` | Route identity, visual coverage, asset variety, playable payoff, and local vanilla-precedent requirements |
| `chaos_redux_clusters_catalog(1).csv` | Existing event-cluster scope and the need for reusable asset routing across linked events |
| `chaos_redux_events_catalog(1).csv` | Full event catalog review. It demonstrates demand for humanoids, nonhuman hosts, creatures, machines, vehicles, structures, aircraft, naval assets, transformations, and route-specific identities |
| `chaos_redux_scenarios_catalog(1).csv` | Manual scenario breadth and the need for reproducible asset variants and scenario-safe runtime wiring |

## Subagent sources

The following supplied subagent definitions were read in full:

- `chaosx_asset_source_researcher.toml`
- `chaosx_country_package_auditor.toml`
- `chaosx_decision_mission_auditor.toml`
- `chaosx_documentation_curator.toml`
- `chaosx_event_completion_auditor.toml`
- `chaosx_focus_tree_auditor.toml`
- `chaosx_generated_event_art.toml`
- `chaosx_icon_artist.toml`
- `chaosx_improvement_loop_planner.toml`
- `chaosx_localisation_auditor.toml`
- `chaosx_repo_explorer.toml`
- `chaosx_scripted_system_architect.toml`
- `chaosx_skill_maintainer.toml`
- `chaosx_spreadsheet_doc_worker.toml`
- `chaosx_super_event_audio_researcher.toml`
- `chaosx_super_event_text_researcher.toml`

These definitions established the model for a new bounded asset-production subagent: exact inputs, narrow reads, explicit outputs, hard scope boundaries, manifest evidence, and no gameplay wiring without parent-granted scope.

## Tutorial workflow extracted from the transcription

The tutorial establishes the following manual reference process:

1. Generate a model from one source image.
2. Inspect the entire model for disconnected, floating, open, or hallucinated geometry.
3. Retry generation when the core silhouette or connectivity is wrong.
4. When low-poly generation loses necessary structure, generate a higher-detail model and remesh it down.
5. Use triangular topology for the HOI4 candidate.
6. Preserve PBR texture output.
7. Import FBX into Blender.
8. Compare the asset against a vanilla model to set direction and scale.
9. Build a root bone, body bone, limb chains, mirrored limbs, and suitable IK controls.
10. Parent bones with intentional offsets and keep IK controls disconnected where required.
11. Parent the mesh to the armature with empty groups.
12. Assign vertices deliberately to named bone groups and avoid accidental cross-limb weights.
13. Use X-ray selection when assigning rear vertices.
14. Replace imported generic materials with PDX materials.
15. Use final DDS texture inputs for the PDX material.
16. Create readable idle, movement, and attack actions.
17. Test loops and judge animations at the zoom level where HOI4 players will see them.
18. Export and wire the result through the Paradox tooling.

The planning package turns each manual step into a state gate with recorded evidence.

## Tutorial guidance that remains a heuristic

The tutorial suggests a target near 10,000 vertices and warns against roughly 25,000 to 30,000 or more. This package preserves those values as seed heuristics for the first pilot, not as universal HOI4 engine rules. The production profile must be calibrated against the closest vanilla model, material, skeleton, animation, and entity precedent on the user's installed game version.

The tutorial describes a free retry in the Meshy web interface. The API and MCP workflow does not assume that an API retry is free. API calls use the current API credit schedule unless a documented Meshy policy says otherwise. Failed API tasks are handled according to the API's current refund behavior, while user-requested or quality-driven retries remain budgeted actions.

## Current external research snapshot

External facts were verified against primary sources where available. The detailed source table is in `references/current_tool_research_2026-07-22.md`.

Key findings:

- Meshy publishes an official MCP server with image-to-3D, remesh, retexture, rig, animate, task, download, and balance tools.
- Meshy Image to 3D accepts one source image, can use smart topology or standard generation, can produce triangular topology, can generate PBR maps, and can accept a text prompt specifically for texturing.
- The current Image to 3D API does not expose a general geometry instruction prompt. The workflow therefore stores geometry instructions as orchestration and QA constraints, and optionally uses an approved derived reference image when preprocessing is necessary.
- Meshy programmatic rigging documentation currently limits reliable use to clear humanoid bipeds.
- Meshy animations are selected by `action_id` from the animation library and applied to a completed rigging task.
- Meshy API assets have a short retention window for non-Enterprise users, so the workflow downloads every successful artifact immediately and records checksums.
- Blender now has an official Blender Lab MCP path, but the official page warns that generated code may run without guards. The package therefore requires an allowlisted project adapter and isolated job workspace.
- The community Blender MCP path also supports arbitrary Python execution. It is a compatibility backend, not the production permission model.
- `io_pdx_mesh` supports Blender and Clausewitz mesh and animation workflows. Its documented Blender installation differs between Blender 4.2 or newer and older supported versions.
- Codex supports project or user MCP configuration through `[mcp_servers.<name>]` tables, including stdio commands, environment-variable forwarding, tool allowlists, timeouts, and approval controls.

## Required local references before implementation

The planning environment did not have access to the user's local Chaos Redux repository, offline Paradox wiki snapshot, installed vanilla game files, or existing `.mesh`, `.anim`, `.asset`, and entity definitions. The first implementation tranche must therefore read and retain local evidence from:

- the graphical asset, interface, character, and relevant model pages in `paradox_wiki/`
- the full vanilla documentation folder
- the closest vanilla land, air, naval, building, character, and animation examples
- existing Chaos Redux 3D model, material, asset, and entity patterns
- the user's installed `io_pdx_mesh` version and Blender version

No exact production budget, bone limit, material channel mapping, action name, or entity syntax should be locked before that calibration pass.
