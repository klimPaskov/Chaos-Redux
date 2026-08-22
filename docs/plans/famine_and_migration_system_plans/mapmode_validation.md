# Famine and migration mapmode validation

## Accepted scope

The shared system owns exactly two engine-native scripted state mapmodes: `famine_state_map_mode` and `migration_state_map_mode`. No third route, reception, cohort, or return mapmode and no full scripted GUI is authorized.

The famine mapmode reads the live food-security stage, normalized score, exposure duration, eight component ledgers, and recorded famine deaths. The migration mapmode combines displacement origins, trapped populations, exact state reception load, overcrowding, resettlement outcomes, and return outcomes. It does not invent route geometry or move population.

## GUI MCP evidence

The pre-change `hoi4.gui_inspect` request used window `mapmodes` and scenario `famine_migration_mapmodes_prechange` at 1920x1080 and UI scale 1. It returned `GUI_INSPECTED` and retained artifact `gui-inspect.c5caf2b7c631d4b9.json`, SHA-256 `56eb29f6db23450b8faa388f5577aed5f53b0bb94aca74b50a56cc0222f8de15`, shared revision `c5caf2b7c631d4b9240cdf6bdb3c941c8a63232da6af82c1deac12cb99c4550c`. The offline graph approximated or missed the hardcoded `mapmodes` window and inspected zero elements. Its global graph diagnostics were truncated after unrelated workspace-wide collisions and unresolved references.

An intermediate post-change explorer retry retained `gui-inspect.96e4822a03aa7c97.json`; like the pre-change artifact, it resolved no elements for the engine-hardcoded `mapmodes` window and therefore could not prove button layout or click regions.

The final post-change `hoi4.gui_inspect` request used scenario `famine_migration_mapmodes_post_change`. It returned `GUI_INSPECTED`, status `ok`, and one artifact after 59.8 seconds. The client response exposed the workspace ID but not the artifact URI or element diagnostics, so it does not supersede the documented hardcoded-window limitation.

The final post-change `hoi4.gui_render` request used the same scenario, normal/hover/selected/warning states, and 1920x1080 plus 2560x1440 at UI scale 1. It returned `GUI_RENDERED`, status `ok`, and one artifact after 54.6 seconds. The client response again exposed no artifact URI or raster payload. Earlier requests timed out or returned `ARTIFACT_STORAGE_LIMIT`. The successful route proves that the mandatory renderer accepted the post-change source request, but the unavailable linked payload remains an exact blocker to visual and click-region comparison; source and DDS review are not presented as equivalent engine-render evidence.

## Map MCP evidence

The broader system map inspection covers the historical-profile anchors and state consumers. Spain's previously unmapped historical profile was closed with an exact 22-state inspection of IDs 41, 165-178, and 788-794. The retained artifact is `map-inspect.a672f4ba67035c47.json`, revision `a672f4ba67035c4776c1660e9f5783507574fd4263329b240f0856996adcb38b`, SHA-256 `01e2214cf4c25a9f39d32a7317c205984140281c120885e91905db7f2982c723`; all 22 requested states were inspected. The route also repeated unrelated map-building and port-position diagnostics and a malformed Event 14 localisation diagnostic; none belongs to these mapmode files.

The final `hoi4.map_render` state-layer request included coastlines, ports, supply nodes, and railways at scale 1. It returned `MAP_RENDERED`, status `ok`, revision `080b7a870be68fd95ec8ed8cb464c2508b35d6b41abb1ea8c43f28a32c779841`, and passed validation with no blockers. The 5632x2048 PNG artifact is `map-state.png`, SHA-256 `52b108966ee8fa0c47ca7458c9be87112fed5d84a5836a4c5f9bb313cb021685`; the linked JSON and HTML representations have SHA-256 values `375a72c749a85d60ac8b179999f6385600238e0af6413930b5e920942df58b29` and `b6ae05fb6a49c9893898f4f1970f3eed75510c6a676d48e10aec85afeb10f04e`. This proves the complete state and transport substrate consumed by both mapmodes without changing map data.

## Static asset evidence

The two button families provide separate selected and deselected 20x18 DDS consumers under `gfx/interface/mapmode/custom/`. Each file is a one-level legacy uncompressed BGRA8 texture with native alpha and no mipmaps. The decoded DDS payloads match the processed RGBA PNGs byte-for-byte. The exact manifest, prompts, reference inspection, and contact sheets live under `docs/assets/famine_and_migration_system/mapmode/`, with the subagent handoff at `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mapmode_icon_artist.md`.

## Source validation

The two definitions use the existing `scripted_map_modes` container, daily visual refresh, state top and bottom layers, and the established exact per-mode sprite naming contract. Color, opacity, thickness, and highlight values are centralized in `common/script_constants/state_map_modes_constants.txt`. Tooltips reveal exact ledgers only to the state's owner or controller; public viewers receive qualitative stage or role information. Script, constants, scripted-localisation, and GFX brace counts remain balanced, and the English mapmode localisation retains its UTF-8 BOM.
