---
description: Make Hearts of Iron IV graphical assets (40 families: focus, ideas, decisions, technology and event pictures, flags, portraits, counters and more) with the hoi4-imagegen MCP. Use for any new or replaced Chaos Redux art that is generated or processed rather than hand-drawn. Covers plan, generate, process, validate, preview, review and install.
---

### In Facts to keep straight

Chaos Redux settled three canvases that differ from vanilla, in its own `.tools/gfx/profiles.json` rows: focus 94x86, idea 64x64 and decision 32x32. `hoi4.image_families` shows each override next to the vanilla value. Every other family uses its vanilla canvas. Name the difference to the user when you plan one of these three.

### In Where things land

`chaos-redux-event-assets` holds the Chaos Redux asset rules (folders, naming, handoff files, real-person rules) and keeps the manual tools in `.tools/` and its `tools/` folder as the fallback when the MCP is unavailable. Read it first.
