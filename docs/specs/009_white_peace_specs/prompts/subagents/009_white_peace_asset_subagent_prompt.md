# Subagent Prompt — Asset Routing for Event 009 White Peace

Spawn the appropriate asset subagent with `fork_turns="none"` after the main agent has confirmed final sprite names and final asset paths.

Use `prompts/009_white_peace_asset_prompt.md` as the source asset prompt.

Routing:

- `chaosx_generated_event_art` for the generated report event image and accepted all-AI observer-news image after reviewing its existing handoff.
- `chaosx_asset_source_researcher` only if a real archival/source image is deliberately chosen for the report/news image.
- `chaosx_icon_artist` for all achievement icons.

Required outputs:

- source PNGs;
- processed PNG previews;
- final DDS files;
- manifest entries under `docs/assets/009_white_peace/manifest.md`;
- `docs/assets/009_white_peace/gfx_handoff.md`;
- contact sheet for achievement icons;
- clear blocked/needs-review notes if any asset cannot be produced.

Do not edit `.gfx`, gameplay, localisation, events, or spreadsheets.
