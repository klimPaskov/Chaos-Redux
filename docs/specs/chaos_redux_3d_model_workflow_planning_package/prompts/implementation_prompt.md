# Implementation Prompt

Implement the planning package `chaos_redux_3d_model_workflow_planning_package` inside the Chaos Redux repository.

Read AGENTS.md and every relevant existing skill first. Use `chaosx_skill_maintainer` for the non-trivial skill and routing update. Preserve the package's no-fallback, fork_context=false, evidence, security, and budget rules.

Hard start gate:
- before anything else, verify that `MESHY_API_KEY` exists as an environment variable
- if it is missing or blank, stop immediately and tell the user to run this PowerShell command, then restart the shell or Codex:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

- do not continue until the key exists and the Meshy route is available

Work in this order:

1. Verify the Meshy key gate and Meshy availability before any downstream work.
2. Inspect the offline Paradox wiki pages and local HOI4 documentation for graphical assets, models, materials, entities, skeletal animation, and the first pilot consumer.
3. Inspect direct vanilla model, material, `.asset`, `.mesh`, `.anim`, and entity precedents for one static prop and one animated humanoid.
4. Validate Blender, Blender MCP, Meshy MCP, and `io_pdx_mesh` versions on the local machine.
5. Run the dry-run bootstrap, review its actions, then run it with `-Apply`.
6. Prove clean-machine add-on persistence and MCP connectivity.
7. Promote the skill, tools, and subagent TOMLs into the repository, adapting only paths that the repository actually uses.
8. Update AGENTS.md and chaos-redux-subagents only with concise routing rules. Do not create a central MCP router skill.
9. For each pilot asset, resolve the working paths automatically. If no ready Meshy reference image exists, generate exactly one Meshy-ready reference image autonomously from the asset brief and save it into the resolved job path. Do not generate side-profile sheets or multi-view boards for Meshy.
10. Run a static prop pilot from one final reference image. Produce the full manifest, DDS, mesh, reimport evidence, handoff, and in-game capture.
11. Run an animated humanoid pilot. Test Meshy rigging and three required actions, clean them in Blender, export, reimport, wire, and capture in game.
12. Run `chaosx_3d_model_auditor` for each pilot.
13. Resolve or report every blocker. Do not promote broad production until both pilots pass.
14. Write an implementation handoff listing files changed, versions, hashes, exact MCP config, pilot assets, validations, remaining risks, and any package rule changed with reason.

Do not store secrets. Do not enable Blender MCP external asset providers. Do not use Meshy auto-rigging for non-humanoids. Do not claim the workflow complete from installation alone.
