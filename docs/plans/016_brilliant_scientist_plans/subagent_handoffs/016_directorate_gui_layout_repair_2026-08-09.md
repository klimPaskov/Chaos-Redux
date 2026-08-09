# Event 016 Directorate GUI layout repair handoff

Status: source and asset repair implemented; mandatory pre-change MCP inspection and render evidence completed; post-change inspection and the full requested render matrix completed, with the render response wire-truncated; the final bounded rewrite returned `REWRITE_STRUCTURE_LIMIT`.

## Ownership and scope

This handoff covers only the Event 016 Directorate window `kruger_directorate_container`, its displayed localisation, its two text-bearing four-state control sheets, and the layout documentation that owns its painted background bays. Gameplay effects, decision costs, AI behaviour, the shared event log, and unrelated interfaces were not changed.

The runtime entry point remains decision category `brilliant_scientist_directorate_category`, and the scripted GUI binding remains `brilliant_scientist_directorate_scripted_gui`.

## Implemented layout

- The 500x620 window is aligned to the decoded painted background bays: header `x38-462 y8-65`, profile `x38-163 y72-289`, telemetry `x169-464 y72-225`, government control `x169-464 y228-292`, navigation and content `x38-462 y301-542`, and footer `x38-449 y552-604`.
- The profile frame and Kruger portrait use the same scale and remain inside the dossier bay.
- Mandate, Dependence, and Exposure each use a dedicated meter row with the value beside the art rather than over it.
- Government Control text is centred above two balanced status graphics instead of occupying their painted surface.
- The five tab controls use equal pitch from `x40` through `x460`. Centred overlay labels replace intrinsic button text so label placement is independent of the four-state sheet ornament.
- Every tab panel uses a 420x194 clipped content area ending at `y538`, clear of the footer divider.
- Overview uses equal 198-pixel columns. Projects use a compact active-project block, separate Capacity display, and three 132-pixel ledger columns. Facilities and Foreign use an art column and two text columns. Authority reserves the left column for deliberately line-broken prose and the right column for sovereignty and Singularity art.
- The Presentation control and its transparent 124-pixel centred label occupy `x40-164`, while the explanatory footer occupies `x176-446`; both remain inside the dedicated footer bay.

## Control-sheet repair

`directorate_tab_button.dds` and `directorate_animation_control.dds` retain their exact dimensions, state order, borders, and normal/hover/pressed/disabled colours. Decorative interior stars, circles, and lines were cleared so the separately centred GUI labels have an unobstructed surface. Source sheets remain preserved in the ignored asset workspace.

The runtime sheets validated as uncompressed 32-bit BGRA DDS and decoded pixel-for-pixel to their processed PNGs:

- Tab sheet: 368x30, four 92x30 frames, DDS SHA-256 `6f0a31be60578cf05e9cd966638b339ff3666dd0664ad7b67fd5b213b8002baf`.
- Presentation sheet: 496x34, four 124x34 frames, DDS SHA-256 `59acd7ada90bc4346c5c593ed97aee5e845825243cbbcb3f3aea3089dc7d22f9`.

Local production evidence is recorded under `docs/assets/016_brilliant_scientist/directorate_ui/validation/directorate_control_layout_repair_2026-08-09.json` and `contact_sheets/directorate_control_layout_repair_2026-08-09.png`. The `docs/assets/` tree is intentionally ignored by repository policy and is not part of the runtime commit.

## MCP evidence

The mandatory pre-change `hoi4.gui_inspect` completed for all 58 Event 016 elements. Its source-linked report is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66ab39d0157e87d3d0deb728380be1a5463b01a09624b36029fa8b7cc36b2499/0c638f9f8011606719762a206ee2cdaec67309a2bc3a4bf95411f1ed10dfe536/gui-inspect.c0177f5faf93f087.json`

The mandatory pre-change render also completed at 1366x768, 1920x1080, and 2560x1440 with state, resolution, click-region, source-map, hierarchy, layout, validation, and comparison artifacts. The baseline source revision was `291abb1a`.

Post-change `hoi4.gui_inspect` completed with status `ok` for `kruger_directorate_container`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf09f2696a0e02a70c1bb40112ea012c5293e379656098e446bcab84e46be821/cc92c3f15cb62481daae8dbd40b19c0484c07ab348cc140957cb4e02e4128ead/gui-inspect.0ef7ae9fba658eab.json`. The inline diagnostics include repository-wide unresolved references and MCP collection truncation; these are separate from the Event 016 geometry review.

Post-change `hoi4.gui_render` completed with status `ok` for normal, hover, selected, disabled, warning, active, completed, empty-list, full-list, long-text, and missing-localisation states at 1366x768, 1920x1080, and 2560x1440, UI scale 1. The representative linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf9181dc3a24911ccc995eea4da1e79066cda5a7d3001bffbc0dd02cb1446c4e/ceb7d4c4b2cda3e8fe05c3ebfaaaf01fd67fe6c2aa94cfe165bff46496b1b23e/kruger_directorate_container-full.svg`. The response carried `MCP_RESPONSE_TRUNCATED` and exposed only one linked artifact inline, so this handoff does not claim a per-cell visual comparison beyond the completed matrix request.

The final bounded `hoi4.gui_rewrite` attempt used source mode after the footer and Authority copy corrections. It returned exactly `status = error`, `code = REWRITE_STRUCTURE_LIMIT`, `artifactCount = 0`, `changedFiles = []`, and blocker `Rewrite could not be completed`. Earlier parent rewrite attempts reached the MCP server's exact 180-second timeout while establishing the runtime source/art package. The final local source was retained and reviewed through the repository patch workflow. Parent visual composites of the Overview, Projects, and Authority states were reviewed against the exact decoded 500x620 background; they are local review evidence under `.tmp/gui_review/` and are not engine-equivalent MCP evidence.

After the successful matrix, parent review found that the worker's scaled footer experiment centred the Presentation label across the footer rather than within its control. The final source restores the button to its native 124x34 footprint at `x40 y566`, centres the transparent label over exactly that footprint, and returns the explanatory footer to the separate `x176 y568` text bay. A final `hoi4.gui_inspect` refresh against those four bounded scalar changes again reached the tool server's exact 180-second timeout. The successful post-change inspection and state matrix therefore precede only this documented footer correction.

## Changed runtime and documentation files

- `interface/016_brilliant_scientist_directorate.gui`
- `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`
- `gfx/interface/016_brilliant_scientist/directorate/directorate_tab_button.dds`
- `gfx/interface/016_brilliant_scientist/directorate/directorate_animation_control.dds`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_background_refresh_handoff.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_ui_asset_handoff.md`
- this handoff

## Remaining acceptance boundary

No known source-layout collision remains in the reviewed Event 016 panels, and all existing button, icon, panel, sprite, tooltip, and localisation identifiers remain wired. Post-change MCP inspection and render evidence exists, but the wire-truncated response prevents a complete per-state/per-resolution comparison artifact claim, and the final footer-only refresh timed out. The rewrite structure-limit result is recorded above. Live in-game consumer acceptance remains user-owned and is not claimed here.
