# Open Decisions and Promotion Blockers

This package defines the workflow, contracts, setup assets, and acceptance gates. The following items require evidence from the target Windows workstation and the live Chaos Redux repository before the pipeline can be promoted.

## Promotion blockers

| ID | Decision or evidence needed | Owner | Resolution evidence | Blocked surface |
| --- | --- | --- | --- | --- |
| `3D-BLK-001` | Select one Blender version that passes both Blender MCP and `io_pdx_mesh` compatibility tests | Pipeline implementer | Dependency lock plus clean-profile test report | All Blender work |
| `3D-BLK-002` | Pin the Blender Lab MCP release or commit and archive checksum | Pipeline implementer | Approved dependency-lock row | Development Blender MCP |
| `3D-BLK-003` | Pin the `io_pdx_mesh` archive and SHA256, then prove mesh and animation export | Pipeline implementer | Export and reimport evidence | PDX export |
| `3D-BLK-004` | Implement and package `chaosx_blender_hoi4_mcp` | Scripted-system or tooling owner | Installed package, tool-schema snapshot, allowlist tests | Production Blender MCP |
| `3D-BLK-005` | Calibrate each asset profile from local vanilla models, materials, actions, entities, and camera-scale tests | 3D pipeline owner | Signed calibration records | Geometry, scale, materials, animation |
| `3D-BLK-006` | Confirm the project MCP host and destination config path | Parent agent | Selected Codex or other host config with secret-safe launch | Workstation setup |
| `3D-BLK-007` | Confirm `MESHY_API_KEY` entitlement and an approved credit budget | User or account owner | Balance check and per-job budget approval | Paid generation |
| `3D-BLK-008` | Supply and approve one reference image for each pilot | Parent and reviewer | Preflight checklist plus image hash | Pilot generation |
| `3D-BLK-009` | Identify the exact runtime consumer, entity, animation roles, material pattern, and target folders for each pilot | Parent implementer | Requirement-to-runtime rows | Runtime wiring |
| `3D-BLK-010` | Run one clean-machine or clean-profile bootstrap reproduction | Independent reviewer | Setup transcript and environment report | Environment promotion |
| `3D-BLK-011` | Complete the four-pilot matrix without an undisclosed fallback or unresolved hard blocker | Parent implementer | Pilot reports and audit | Pipeline promotion |
| `3D-BLK-012` | Obtain in-game evidence at relevant zoom, speed, terrain, lighting, and action states | Parent implementer | Screenshots or video plus runtime report | Completion claim |

## Decisions that may be made per job

These are not global blockers. They belong in the job file and require an explicit reviewer decision.

- whether the reference needs an approved derived image to clarify hidden or dark geometry
- smart-topology generation versus detailed generation followed by remesh
- provider texturing versus Blender-authored texture repair or retexture
- provider humanoid rig versus Blender rig
- provider action candidate versus Blender-authored action
- rigid component weighting versus deforming weights
- whether root motion is stripped, retained, or split into a dedicated semantic action
- whether disconnected geometry is intentional articulation or a generation defect
- whether an asset can share a material, skeleton, action, or entity family with an existing asset
- whether a model is rejected and regenerated or repaired locally

Every decision must record its evidence, cost impact, affected artifacts, and reviewer.

## Explicit non-decisions

The following are already locked by this package:

- one reference image is the default Meshy input
- AI output is source material, not a completion artifact
- final HOI4 scale and orientation are normalized in Blender against approved references
- export topology is triangulated
- paid retries require a new attempt record and budget check
- the web tutorial's free-retry behavior is not assumed to exist in the API
- nonhumanoid, vehicle, aircraft, naval, and articulated rigs are Blender-owned unless a later verified provider contract is explicitly approved
- the production Blender tool surface cannot expose arbitrary code execution
- requested animation cannot be silently replaced with a static model
- missing runtime wiring or in-game evidence prevents completion

## User choices that improve first implementation

The first implementation becomes more concrete once these values are supplied:

1. The Windows path to the Chaos Redux repository.
2. The Blender executable that should be the initial compatibility candidate.
3. The MCP host in daily use. The included Codex template is ready for a Codex project config.
4. The first four reference images, or approval to reduce the pilot set to a smaller staged set while keeping promotion blocked.
5. The first real target asset, including its runtime consumer and required actions.
6. The maximum Meshy credits allowed per candidate and per accepted asset.
7. Whether the isolated Blender Lab development profile may be installed alongside the production adapter.

## Stop condition

Do not resolve a blocker by inventing a budget, a Blender version, a vanilla reference, a Paradox material mapping, an action name, a runtime consumer, or a fallback. Mark the affected row blocked and carry it into the parent handoff.
