# Event 005 Focus Icon Overlay Removal Report

Date: 2026-08-12

The scope follows the user's clarified rule: existing genuine artwork may be reused, including one icon across a whole tree, while the rejected shared-base-plus-accent/medallion construction must not remain active.

## Resolution

- 1,760 focus assignments are covered.
- 1,408 former overlay rows reuse their documented genuine existing source texture.
- 322 rows retain individually generated ImageGen source PNGs, processed transparent PNGs, runtime DDS files, and per-row prompt/source-mode records.
- 30 UWR/KMB specialist rows remain preserved bespoke focus artwork.
- 43 current focus-tree contact sheets were rendered from the active runtime textures.

## Runtime and source surfaces

- Runtime textures: `gfx/interface/goals/005_soviet_collapse/`.
- Active generated/reuse registry: `interface/005_soviet_collapse_focus_icons.gfx`.
- Specialist registry: `interface/005_soviet_collapse_uwr_kmb_icons.gfx`.
- Legacy duplicate focus sprite definitions were removed from `interface/005_soviet_collapse.gfx`.
- No Event 005 focus source file, localisation file, focus ID, or authored tree position was changed.

## Evidence

- `docs/assets/005_soviet_collapse/focus_icon_regeneration/final_focus_icon_manifest.json`.
- `docs/assets/005_soviet_collapse/focus_icon_regeneration/final_contact_sheets/`.
- `docs/assets/005_soviet_collapse/focus_icon_regeneration/final_prompt_records/`.

The former overlay contact sheets and processed images remain under the original audit paths and are superseded evidence, not active runtime inputs.

## Validation

The local asset audit found zero missing runtime textures, zero reuse-source mismatches, zero generated DDS round-trip mismatches, and zero missing focus sprite registrations across all 1,760 rows.

The previously completed MCP focus inspection for AAX reported zero Event 005 diagnostics and preserved its layout hash. A fresh MCP inspection after the asset pass is currently blocked by the server's `ARTIFACT_MANIFEST_INVALID` workspace error before source scanning; no new MCP pass is being represented as successful.
