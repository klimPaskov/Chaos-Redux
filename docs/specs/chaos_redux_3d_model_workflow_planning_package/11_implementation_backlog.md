# Implementation Backlog

## Tranche 0: Local evidence and calibration

### Work

- locate all Chaos Redux and vanilla 3D model, material, entity, and animation definitions relevant to each domain
- read local game documentation for meshes, entities, assets, materials, and animation where present
- inspect `io_pdx_mesh` usage and any repository scripts
- measure at least three vanilla examples for the first four profiles
- identify action names, skeleton patterns, axes, scale, material channels, and final paths
- write profile calibration records

### Acceptance

- no pilot profile relies on tutorial numbers alone
- exact local paths and identifiers are recorded
- unsupported or unclear engine surfaces are listed as blockers
- no provider credits are spent before this tranche passes

## Tranche 1: Dependency lock and workstation bootstrap

### Work

- select the Blender version
- lock Meshy MCP
- lock official Blender Lab MCP
- lock `io_pdx_mesh`
- create an isolated Blender profile
- implement guarded setup and verification scripts
- create project-scoped MCP configuration
- verify secret handling

### Acceptance

- every external dependency has source, version or commit, checksum, and license
- both MCP servers connect in an isolated test
- PDX mesh and animation smoke exports succeed
- production Blender adapter still rejects free-form Python

## Tranche 2: Job schema and artifact vault

### Work

- implement `model_job.schema.json`
- implement evidence schema
- implement JSONL history
- create job initialization command
- create SHA256 and download verification
- create cost and attempt ledger
- add append-only state transitions

### Acceptance

- invalid jobs fail before paid work
- a successful mock job retains complete lineage
- secrets are absent from all archived records
- cancellation and resume preserve history

## Tranche 3: Meshy MCP orchestration

### Work

- discover current tool schemas at startup
- implement balance gate
- implement image-to-3D submission
- implement status polling and transient retry
- implement immediate downloads
- implement remesh and retexture branches
- implement humanoid rig and animation source branches
- record consumed credits

### Acceptance

- no paid call runs without a job and budget approval
- expired remote URLs are not the only copy of an accepted artifact
- provider errors map to the failure taxonomy
- request evidence matches the actual MCP tool schema

## Tranche 4: Blender HOI4 adapter foundation

### Work

- implement path confinement
- implement allowlisted operations
- create versioned scene template
- import GLB and FBX
- implement scene and geometry reports
- import read-only vanilla reference
- normalize orientation, scale, origin, and transforms
- save checkpoints

### Acceptance

- arbitrary code and shell arguments are rejected
- adapter cannot write outside the job and approved output roots
- mock geometry audit produces stable machine-readable output
- source collection remains unchanged after processing

## Tranche 5: Materials and PDX export

### Work

- implement PBR-to-PDX material conversion from local precedents
- implement texture processing and DDS handoff
- implement exporter invocation
- capture exporter logs
- implement optional re-import or parser checks
- package runtime handoff

### Acceptance

- one static pilot loads in game with correct material, scale, orientation, and pivot
- all texture paths are relative and valid
- exporter version and settings appear in evidence

## Tranche 6: Rigging and animation

### Work

- implement provider-rig audit and mapping
- implement custom rig recipes for humanoid, creature, and mechanical profiles
- implement weight reports
- implement action cleanup, bake, root policy, and loop report
- implement preview rendering
- export `.anim` files

### Acceptance

- one humanoid and one nonhumanoid pilot pass Blender and in-game deformation checks
- one mechanical pivot animation passes
- skeleton changes correctly invalidate downstream approvals

## Tranche 7: Pilot promotion

Complete the pilot matrix in `12_pilot_and_test_matrix.md`.

### Acceptance

- four primary pilot assets pass end to end
- failure-injection tests pass
- cost estimates and actual credits are compared
- runtime crosswalk has no uncovered accepted row
- no requested action was replaced with a static fallback

## Tranche 8: Repository skill and subagent rollout

### Work

- use `chaosx_skill_maintainer` to review the proposed skill
- add routing to `AGENTS.md`, event-assets, and subagents skills
- install the subagent definition
- add templates and examples to the skill
- document parent prompt contract

### Acceptance

- the new workflow does not duplicate or conflict with 2D asset skills
- subagent ownership is narrow and context-free
- parent remains responsible for runtime wiring and completion

## Tranche 9: Hardening and scale

### Work

- add queue and concurrency controls
- add webhook support only after secure HTTPS infrastructure exists
- add regression test assets
- add performance capture in a repeatable HOI4 scene
- add profile-specific semantic checks
- add dependency update test harness
- add archival and cleanup policy

### Acceptance

- dependency updates can be tested without changing production
- a failed task cannot corrupt an approved job
- high-instance assets have measured performance evidence

## Recommended issue breakdown

| Issue | Deliverable | Dependency |
| --- | --- | --- |
| 3D-001 | Local vanilla and exporter reference map | None |
| 3D-002 | Dependency lock and Windows discovery | 3D-001 |
| 3D-003 | Isolated Blender profile and MCP smoke tests | 3D-002 |
| 3D-004 | Job and evidence schemas | 3D-001 |
| 3D-005 | Meshy client and artifact vault | 3D-002, 3D-004 |
| 3D-006 | Blender adapter security boundary | 3D-003, 3D-004 |
| 3D-007 | Geometry and scale operations | 3D-006 |
| 3D-008 | PDX material conversion | 3D-001, 3D-006 |
| 3D-009 | PDX mesh export | 3D-003, 3D-008 |
| 3D-010 | Provider rig mapping | 3D-006 |
| 3D-011 | Custom rig recipes | 3D-006 |
| 3D-012 | Action processing and export | 3D-009, 3D-010, 3D-011 |
| 3D-013 | Static building pilot | 3D-005, 3D-009 |
| 3D-014 | Humanoid unit pilot | 3D-005, 3D-012 |
| 3D-015 | Nonhumanoid creature pilot | 3D-005, 3D-011, 3D-012 |
| 3D-016 | Vehicle pilot | 3D-005, 3D-012 |
| 3D-017 | Runtime crosswalk and audit | 3D-013 through 3D-016 |
| 3D-018 | Skill and subagent rollout | 3D-017 |

## Stop conditions

Implementation must stop for user or parent review when:

- a fallback or simplification would be required
- the selected Blender version cannot run both the approved MCP and exporter
- a required HOI4 model surface lacks a local precedent
- source rights are unclear
- provider cost exceeds the approved hard limit
- a profile cannot meet performance or visual requirements
- the requested animation cannot be produced or exported
