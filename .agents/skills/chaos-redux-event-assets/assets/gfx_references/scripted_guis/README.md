# Scripted GUI and native interface references

This shelf contains tightly cropped, native-pixel views of installed vanilla and Chaos Redux interfaces. The `.png` examples are review references, not runtime assets. `contact_sheet.png` and each category contact sheet are browsing aids; compare the native-size PNG before drawing layout conclusions.

The `*_ingame.png` files are exact copies of the user-supplied game captures.
The `*_mcp.png` files come from `ScriptedGuiStudio.renderAndStore`, the production renderer behind `hoi4.gui_render`, using `hoi4-agent-tools` 3.5.0.
Each render uses a declared scenario in [render_scenarios.json](render_scenarios.json).
The full 1920×1080 renderer output is retained under `source_full/`, and the review PNG is a lossless, unscaled crop at the bounds in [REFERENCE_MANIFEST.md](../REFERENCE_MANIFEST.md).
[render_manifest.json](render_manifest.json) records the renderer implementation hash, source revision, exact scenario, diagnostics, and fidelity limits for every image.
These are production-renderer source views; they do not execute native input, gameplay effects, or timers.

The vanilla Options Video and Škoda Priority scenarios use the values and selected states visible in the supplied in-game captures. The Chaos Redux Tag Manager scenario uses the supplied capture and the window's own `show_position`. The Event Log shows a declared empty Events tab with filter names from current localisation. Chaos Meter Status and Deaths show the source-defined initial zero state. These declared values make the examples reproducible; they do not claim to represent a later live campaign.

The installed GUI and linked script definitions own layout and behavior. The source revision, files, crop, SHA-256, and known fidelity limits are recorded in the manifest. The Škoda focus inlay is positioned inside a focus tree in game; its isolated MCP crop uses the installed 552×516 background canvas so none of that art is cut off. The game capture, not the isolated inlay coordinate, is the reference for its in-game placement.

Before adding another reference, inspect its owning `.gui` and scripted or native consumer, declare one coherent state, render with the production GUI renderer at UI scale 1, review the full image, and crop only to the painted composition. Keep the full render, record its revision and crop bounds, and run `python build_contact_sheets.py`. A blank, clipped, overlapping, or contextless output is not a full-window reference. Pixel similarity to the game is not assumed from a successful render.

The supplied Tag Manager capture predates the current source's +5/−5 controls and wider action buttons.
The Options gamma value is not supplied, so the neutral renderer knob placement is not a matched engine setting.
Native compound-control overlap diagnostics and unsupported behavior remain in the manifest; image inspection does not waive them.
