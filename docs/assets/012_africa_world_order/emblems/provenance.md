# Event 012 External-Continent Package Emblems

This package contains six fictional, symbolic, alternate-history institutional emblems for the Event 012 world-order continent packages: Middle East, Europe, Asia, North America, South America, and Oceania.

The source masters were generated with the built-in OpenAI image-generation tool on 2026-08-03. Each prompt requested one centered HOI4-style painted heraldic emblem on a perfectly flat `#00ff00` chroma-key background, with no people, flags, map outlines, readable text, watermarks, UI frames, modern props, or 3D models.

The canonical vanilla references inspected before generation were `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/factions/contact_sheet.png`. These references established the compact dark-outline, enamel-and-metal, transparent-corner visual language and small-size silhouette target without copying any specific emblem.

The official `remove_chroma_key.py` helper removed the flat green background with auto-key border sampling, soft matte, despill, and the repository thresholds. Each alpha result was cropped to non-transparent bounds, resized with LANCZOS to fit an 88x80 interior, centered on a transparent 94x86 RGBA canvas, and converted with the repository `convert_to_dds.py` workflow to one-level 32-bit BGRA DDS.

`manifest.json` records the source, processed preview, final DDS, sprite proposal, dimensions, and SHA-256 checksums for each region. `contact_sheet.png` is a review-only enlarged sheet; it is not a runtime asset. `gfx_handoff.md` contains the parent-owned GFX registration suggestions and final runtime paths.
