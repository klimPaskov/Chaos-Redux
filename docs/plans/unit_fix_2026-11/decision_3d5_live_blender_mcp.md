# Decision 3D-5: live authoring through the Blender Lab MCP

Disposition: `accepted and queued`. The basis is a user decision of 2026-11-06, relayed by the coordinating session, approving an interactive Blender MCP with code execution and viewport capture for live re-authoring. Implementation of the unit re-authoring it enables is queued on branch `cr-3d-reauthor`.

## Why

Decision 3D-3 keeps new rigs and new actions as live work in Blender through the Blender MCP. The only Blender server in `.mcp.json` was the `chaosx_blender_hoi4` adapter. That adapter imports, retimes, repairs and exports existing data. It cannot pose a bone, insert a key, attach a prop to a control or show the viewport, and the skill forbids adding an adapter operation that writes keys from a spec. So the live route needed its own server.

## Decision

- **Server.** `.mcp.json` gets a `blender_lab` server that runs the locked Blender Lab MCP route already recorded in `.tools/3d_pipeline/config/dependencies.lock.json` (`routes.blender_lab_mcp`: v1.0.3, commit `2cea8d566dde07fbac28a61d698909d69724e853`, wrapper `.tools/3d_pipeline/wrappers/run_blender_lab_mcp.cmd`). It connects to `127.0.0.1:9877`, the lock's `blender_mcp_addon.socket_port`, and uses the locked Blender 5.2.2 for its command-line tools.
- **Version.** The kit pins the Lab MCP at `dbbf836`, which reports server version 1.0.2. Chaos Redux keeps its own lock at v1.0.3, which is newer and was already verified on Blender 5.2.2 with the add-on installed. The installed add-on code matches the v1.0.3 checkout file for file, and only its manifest version line differs.
- **Blender instance.** The authoring agent starts its own hidden background Blender on port 9877 as the start-gate reference describes. It never connects to, or stops, a Blender started by someone else on another port, such as 9876.
- **What counts as live.** The agent sets each key pose deliberately in the live session, one pose or one small group of related bones at a time, and checks a viewport render or screenshot before the next change. Templates, formula or procedural gaits, and code that generates keys in a batch from a table, loop, curve or another unit's clip do not count, even through the same bridge. Read-only, render, measurement and save helpers are allowed.
- **Unchanged.** Decision 3D-3 still governs scripted geometry, weight and grounding repair. Every unit still needs the independent fresh-context review before it is accepted. Paid provider steps still need user approval after a unit fails review.

## Evidence

On 2026-11-06 the route was proven end to end before wiring. A hidden Blender 5.2.2 started with `--background --online-mode --command blender_mcp --host 127.0.0.1 --port 9877` loaded `io_pdx_mesh` and answered `execute_blender_code`. A Workbench render wrote a PNG in background mode. The wrapper, run with `BLENDER_MCP_PORT=9877`, completed the MCP handshake, listed 26 tools including `execute_blender_code`, `render_viewport_to_path` and `get_screenshot_of_area_as_image`, and ran code in that Blender.

Area and window screenshots need a visible Blender window. The background instance renders the viewport camera through `render_viewport_to_path` or Workbench renders instead, so no window appears on the shared desktop.
