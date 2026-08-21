# Operating Runbook

## Before opening a job

1. Run environment verification.
2. Confirm Meshy balance.
3. Confirm no stale Blender MCP listener is running.
4. Confirm dependency-lock hashes.
5. Confirm the job root is on a backed-up local drive.
6. Confirm reference provenance and approval.
7. Confirm profile calibration exists.
8. Confirm credit and retry limits.

Do not start from an untracked Blender scene.

## Create the job

1. Copy `templates/model_job.example.yaml`.
2. Assign the stable job and asset IDs.
3. add the single reference image.
4. calculate its SHA256.
5. fill source provenance and license state.
6. choose the profile.
7. list required actions.
8. name the vanilla reference family.
9. set credit and attempt ceilings.
10. validate against the schema.

## Run reference preflight

Use `checklists/reference_image_preflight.md`.

Output:

```text
references/preflight_report.md
```

When a derived reference is approved, keep both original and derived files and write a diff note.

## Estimate cost

Example:

```powershell
python .tools/3d_pipeline/tools/estimate_meshy_credits.py `
  --model smart_topology `
  --textured `
  --rig `
  --animations 3
```

Copy the estimate into the job and verify the live balance.

## Generate the candidate

1. start Meshy MCP through the wrapper
2. confirm tool inventory
3. call the balance tool
4. submit the approved image-to-3D request
5. record task ID immediately
6. monitor status using the same attempt
7. download every returned artifact immediately
8. hash and open files
9. record consumed credits
10. create the multi-view review package

Stop the Meshy server when the paid work session ends if it is not needed by other approved jobs.

## Review the candidate

Use the generation gate.

- inspect wireframe and shaded geometry
- inspect all sides
- mark every missing, floating, fused, invented, or deformed component
- choose approve, local repair, retry, revise reference, or block

Do not start texture or rig work on a rejected candidate.

## Optional Meshy post-processing

### Remesh

Use when the approved core needs lower or better-distributed topology. Compare with the original.

### Retexture

Use only after geometry approval. Preserve the original texture set.

### Rig and animate

Use only for a suitable humanoid. Download each rigged or animated result separately and treat it as a source candidate.

## Open the Blender job

1. start Blender in the isolated profile
2. create the job scene from the versioned template
3. import the provider source into the protected collection
4. duplicate into the working collection
5. save the first checkpoint
6. import the approved vanilla reference read-only
7. run scene and geometry inspection

## Normalize and repair

1. set forward and up axes from the profile
2. align ground plane
3. match approved relative scale
4. apply transforms
5. inspect origin and pivots
6. perform only bounded repairs
7. triangulate before final rig and export QA
8. rerun geometry report
9. save geometry-approved checkpoint

## Materials

1. inspect source PBR maps
2. map them to the local PDX precedent
3. convert textures through the approved repository workflow
4. assign relative runtime paths
5. render the material preview
6. save materials-approved checkpoint

## Rig

1. select provider-map or custom-rig route
2. write or confirm rig map
3. create hierarchy
4. add IK and controls when needed
5. parent with the approved method
6. assign weights
7. run weight and influence audit
8. run deformation test poses
9. save rig-approved checkpoint

## Actions

For each required role:

1. import, retarget, or author the action
2. set FPS and frame range
3. enforce root policy
4. clean scale and accidental keys
5. bake constraints
6. inspect loop or one-shot ending
7. render preview
8. write action manifest
9. approve the action

Do not change the skeleton after this point without invalidating all actions.

## Export

1. create pre-export checkpoint
2. verify `io_pdx_mesh` version
3. isolate the export collection
4. run the export operation
5. capture all logs
6. hash `.mesh` and `.anim` outputs
7. run re-import or parser checks when available
8. create runtime handoff

## Runtime wiring

The main agent:

1. inspects the same local precedent
2. copies final files into approved runtime paths
3. adds model, asset, entity, material, and action registrations
4. adds the exact consumer
5. updates the crosswalk
6. validates file references

## In-game test

Use the repeatable pilot scene or scenario.

Capture:

- model at standard zoom
- model at close zoom
- front and side orientation
- idle
- movement
- every attack or special action
- material and texture behavior
- scale against a vanilla peer
- performance evidence for the expected instance count

Write the result to `runtime/validation/`.

## Close the job

A job closes only when:

- state is `complete`, `blocked`, or `canceled`
- manifest matches actual files
- consumed credits are final
- crosswalk has no unexplained row
- rejected candidates are documented
- remote-only dependencies are gone
- all secrets are absent
- parent has reviewed the handoff and runtime evidence

## Recover from common problems

### Meshy task succeeded but no local model

- query the task immediately
- download all URLs
- if the URL has expired and cannot be renewed, mark artifact capture failure
- do not pay for a new task until the cause is documented

### Blender scene corrupted

- close without saving
- restore the last checkpoint
- rerun the last operation from the append-only history
- compare source collection checksum

### Exporter disappeared after Blender update

- stop production
- restore the locked Blender profile or install the approved extension into a new profile
- rerun smoke exports
- do not edit jobs until compatibility passes

### Wrong scale in game

- capture the exact observed comparison
- return to the normalization checkpoint
- update profile evidence if the vanilla reference was wrong
- re-export and rewire paths only if names changed

### Animation plays the wrong role

- inspect entity action mapping first
- then inspect exported action name and frame range
- return to Blender only when the source action is wrong

## Maintenance cadence

### Before each job

- environment verification
- balance check
- lock check

### Monthly or before a large batch

- review Meshy pricing, retention, and tool schema
- review MCP releases and security notes
- review `io_pdx_mesh` issues affecting the selected Blender version
- rerun one static and one animated regression asset

### Before dependency promotion

- clean-profile install
- all smoke tests
- four primary pilot regression tests when the change affects Blender, exporter, materials, or actions
- rollback instructions verified

## Update: autonomous Meshy start gate and single-image reference rule

Before any modeling work begins, verify that `MESHY_API_KEY` exists as an environment variable. If it is missing, stop and instruct the user to run the documented PowerShell command, then restart the shell or Codex.

This workflow may generate its own Meshy-ready reference image when the user provides only an asset brief. Ask ImageGen for a real transparent background in that initial generation and preserve the alpha channel. Background removal is fallback-only when native transparency fails or an inherited, sourced, or user-provided reference has an unwanted opaque backdrop. Meshy still receives exactly one clean final reference image. Do not create side-profile sheets, multi-view boards, or other multi-image collages for Meshy. The workflow resolves its own deterministic working paths and saves the final reference image there before Meshy starts.
