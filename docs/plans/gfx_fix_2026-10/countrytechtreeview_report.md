# Country technology-view sprites

Added the exact installed-vanilla `GFX_special_forces_doctrine_folder_icon` block.
The registry matches all 295 current vanilla sprite definitions; no mod-specific definition was lost.
The four-line change is committed as `151dbe4b8556a45fd2de8ae6b19197cb420ea382`.
Exact source hashes, comparison and consumer/texture evidence are in `vanilla_overrides_report.md`.

The orchestrator should open the technology/doctrine view on a paused 1936 USA fixture at 1920x1080, UI scale 1, and inspect the Special Forces folder.
Expected: its native folder icon is visible and the other doctrine/folder sprites remain present.

A bounded MCP folder lint request returned `TECH_INSPECTED_PARTIAL` with validation false because helper projections were deferred.
The linked lint artifact could not be read after the transport closed, and the assets render also returned `Transport closed`.
`technology_mcp_evidence.json` preserves the requests, result, artifact URI/hash and exact transport gap; no successful folder render or standalone viewer availability is claimed.
