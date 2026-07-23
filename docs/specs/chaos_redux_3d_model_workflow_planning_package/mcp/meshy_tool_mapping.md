# Meshy MCP Tool Mapping

## Current official tool names

The official server reviewed for this package exposes these relevant tools:

| Workflow need | MCP tool | Policy |
| --- | --- | --- |
| Check available credits | `meshy_check_balance` | Required before paid calls |
| Generate from one image | `meshy_image_to_3d` | Primary generation path |
| Check task | `meshy_get_task_status` | Poll same attempt, no paid retry |
| List or recover task context | `meshy_list_tasks` | Diagnostic use only |
| Cancel task | `meshy_cancel_task` | Use when a queued task is no longer wanted and cancellation is supported |
| Download local model files | `meshy_download_model` | Required immediately after success |
| Remesh | `meshy_remesh` | Only after geometry route decision |
| Retexture | `meshy_retexture` | Only after geometry approval |
| Rig humanoid | `meshy_rig` | Clear standard humanoid biped only |
| Apply provider action | `meshy_animate` | Source animation candidate only |
| Convert format | `meshy_convert` | Use when a required local format is missing |
| UV unwrap | `meshy_uv_unwrap` | Optional, after explicit UV decision |
| Resize real-world dimensions | `meshy_resize` | Not used for final HOI4 scale normalization by default |

The live MCP tool schema is authoritative. At startup, record the server version, tool list, and relevant input schemas.

## Tools disabled by default for this workflow

- `meshy_text_to_3d`
- `meshy_multi_image_to_3d`
- Creative Lab tools
- text-to-image and image-to-image
- 3D printing tools
- slicer integrations

They may belong to other workflows, but the user requested one reference image as the normal source.

## Call sequence

```text
meshy_check_balance
meshy_image_to_3d
meshy_get_task_status until terminal state
meshy_download_model
optional meshy_remesh
optional meshy_retexture
optional meshy_rig
optional meshy_animate for each approved action
meshy_download_model after every successful post-process task
```

## Evidence captured from each call

- MCP server version
- tool name
- redacted arguments
- request time
- task ID
- task status
- provider error code and message
- consumed credits when supplied
- output URLs in restricted evidence
- immediate local output paths
- SHA256 and file size

## Schema-drift rule

If the live tool schema changes:

- stop before a paid call
- compare required and removed fields
- update the dependency and tool-schema lock
- rerun a no-cost smoke test
- update the request builder and relevant docs
- rerun the affected pilot before promotion

Do not send guessed fields to a paid endpoint.

## Image-to-3D request policy

Required intent:

- one approved image
- triangular topology
- profile target count when available
- texture state
- PBR state
- lighting-removal state
- pose state
- output-format capture

The adapter stores geometry instructions even when the endpoint cannot consume them. Those instructions become candidate-review and Blender requirements rather than being presented as provider prompt support.

## Rigging policy

Before `meshy_rig`:

- candidate geometry approved
- clear humanoid biped confirmed
- face count within live endpoint limit
- orientation requirement met
- source file format accepted
- rig cost within budget

After rigging:

- download immediately
- inspect skeleton in Blender
- do not call animation until rig gate passes

## Animation policy

Before `meshy_animate`:

- rig task succeeded and was approved
- action inventory or ID was verified from current service data
- action maps to a required semantic role
- FPS is approved
- cost fits the remaining budget

Provider animation is never automatically final. It must be cleaned, mapped, baked, exported, and tested in Blender and HOI4.
