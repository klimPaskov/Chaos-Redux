# Goal Prompt Under 4000 Characters

Implement the autonomous Chaos Redux 3D model workflow package in the repository. Read the full package first and then follow it carefully.

This workflow must be autonomous. It should verify Meshy access first, generate its own single Meshy-ready reference image when the user only provides an asset brief, resolve its own working paths, and then complete the Meshy to Blender to PDX pipeline.

Hard gate:
- `MESHY_API_KEY` must exist as an environment variable before anything else can start
- if the key is missing, stop and tell the user to run this PowerShell command:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

Then tell the user to restart the shell or Codex. Only continue after the key exists and Meshy is available.

Required outcomes:
- install and verify the Meshy MCP route, Blender MCP route, and version-locked `io_pdx_mesh` setup
- integrate the `chaos-redux-3d-model-pipeline` skill and `chaosx_3d_model_pipeline` subagent
- generate exactly one final Meshy input image per pilot asset when a ready reference is not already present
- do not generate side-profile sheets or multi-view boards for Meshy
- run one static prop pilot and one animated humanoid pilot
- produce manifests, provider task lineage, Blender checkpoints, processed textures, `.mesh` and `.anim` outputs, reimport proof, QA evidence, runtime handoff, and in-game screenshots
- do not mark the workflow complete until both pilots pass

Use the full package, then implement and finish with a detailed handoff.
