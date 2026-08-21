# Current Tool Research Snapshot

**Access date:** 2026-07-22

This snapshot supports planning. Recheck live documentation before implementation or dependency promotion.

## Meshy MCP

Official repository:

- https://github.com/meshy-dev/meshy-mcp-server

Findings:

- the official server exposes image-to-3D, remesh, retexture, rig, animation, task, download, conversion, and balance operations
- the repository documents 24 tools in release `0.4.0`
- prerequisites include Node.js 18 or newer and an API key available to Pro-tier API users
- stdio is the default transport
- Windows configuration uses `cmd /c npx`
- official manual configuration uses the npm package `@meshy-ai/meshy-mcp-server`
- the current latest release shown during research was `v0.4.0`, dated 2026-06-24

## Meshy Image-to-3D and post-processing

Official documentation roots:

- https://docs.meshy.ai/en/api/image-to-3d
- https://docs.meshy.ai/en/api/remesh
- https://docs.meshy.ai/en/api/rigging
- https://docs.meshy.ai/en/api/animation
- https://docs.meshy.ai/en/api/pricing
- https://docs.meshy.ai/en/api/rate-limits
- https://docs.meshy.ai/en/api/changelog

Findings:

- Image-to-3D accepts a single image URL or data URI in supported image formats
- the current API includes standard and smart-topology model routes
- smart topology uses triangular output and supports a target polygon count
- PBR maps and lighting removal are available
- the API exposes texture-direction text through a texture prompt
- a separate general geometry prompt was not present in the reviewed Image-to-3D parameter surface, so the workflow does not promise it
- Remesh accepts an earlier task or model URL and can reduce or reorganize topology
- programmatic rigging is documented primarily for standard humanoid bipeds with clear limbs and body structure
- rigging has face-count and orientation constraints that must be checked against the current endpoint
- Animation consumes a rig task and action selection, with approved FPS values exposed by the endpoint
- rate limits are account-scoped and can return HTTP 429
- provider responses can expose consumed credits, which the workflow records

## Meshy API credit snapshot

Official source:

- https://docs.meshy.ai/en/api/pricing

Snapshot:

- smart-topology Image-to-3D: 5 credits without texture, 15 with texture
- Meshy 7 Image-to-3D: 20 without texture, 30 with texture
- retexture: 10
- remesh: 5
- convert: 1
- resize: 1
- auto-rig: 5
- animation: 3 per call
- the reviewed pricing table linked the UV Unwrap endpoint but did not publish an explicit UV unwrap price row. The estimator therefore requires a live unit-cost override for that operation

Pricing can change. The live pricing page and account response override this file.

## Meshy retention

The reviewed official documentation states a limited API asset retention period for non-Enterprise accounts. The pipeline therefore downloads successful results immediately and treats provider URLs as temporary.

## Blender Lab MCP

Official sources:

- https://www.blender.org/lab/mcp-server/
- https://www.blender.org/news/introducing-blender-lab/
- https://www.blender.org/development/blender-lab-activity-report-q1-2026/
- https://projects.blender.org/lab/blender_mcp

Findings:

- Blender Lab provides an official lightweight MCP server for interacting with Blender's Python API
- it is appropriate for isolated development and operator-assisted work
- the official page warns that generated code is executed without general safety guards
- production use therefore requires a narrow allowlisted adapter and local path confinement
- exact Blender and server versions must be resolved and tested together at implementation time

## Community Blender MCP compatibility backend

Repository reviewed:

- https://github.com/ahujasid/blender-mcp

Findings:

- it exposes broad Blender control, including arbitrary Python execution
- it commonly connects to a Blender add-on over loopback
- it has optional external integrations and telemetry considerations
- it may serve as an approved compatibility backend, but never as an undisclosed production fallback

## Blender extension command line

Official manual:

- https://docs.blender.org/manual/en/latest/advanced/command_line/extension_arguments.html

The manual exposes `blender --command extension install-file`. The exact repository and enable flags must be confirmed against the installed Blender version before the setup script is promoted.

## Paradox `io_pdx_mesh`

Official repository:

- https://github.com/ross-g/io_pdx_mesh

Findings:

- the project imports and exports Clausewitz mesh and animation files
- the README states Blender 3.64+ support
- Blender 4.2+ installs from disk through the Extensions interface
- the current release shown during research was `0.91`, dated 2024-09-23
- the extension is GPL-3.0
- current compatibility with the selected Blender Lab MCP version must be proven locally

## Local sources still required

Internet research cannot replace:

- the offline Paradox wiki snapshot required by the repository
- vanilla HOI4 documentation under the installed game directory
- vanilla model, entity, asset, material, mesh, and animation precedents
- existing Chaos Redux model definitions
- the actual installed exporter and Blender behavior

These local sources are mandatory in implementation tranche 0.

## Codex MCP configuration

Official sources:

- https://developers.openai.com/codex/mcp
- https://developers.openai.com/codex/config-reference
- https://developers.openai.com/codex/config-sample

Findings:

- Codex MCP servers are configured under `[mcp_servers.<name>]`
- stdio servers use `command`, optional `args`, optional `env`, and optional `env_vars`
- configuration can set `startup_timeout_sec`, `tool_timeout_sec`, `enabled`, `required`, `enabled_tools`, `disabled_tools`, and approval behavior
- the normal user configuration is under `~/.codex/config.toml`, while a trusted project can use a project-scoped `.codex/config.toml`
- the package's Codex template forwards `MESHY_API_KEY` by environment-variable name rather than embedding the secret
