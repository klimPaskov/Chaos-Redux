# Locations Closure-Locked Reference v3 Handoff

Status: complete as a scripted-GUI design reference; this file is not a runtime asset.

## Provenance

Source image: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/references/camp_admin_locations_reference_v2.png`.

Source SHA-256: `264A52F6D451BFB977EE1EB7B5229E5A939C3F029099F49B1FA93ECF67236E61`.

Source canvas: 1672×941 pixels, RGB.

Generation used the official built-in ImageGen edit flow with v2 as the local edit target; the generated result was saved directly without raster compositing or resizing.

Generated candidate path: `C:/Users/klimp/.codex/generated_images/01a0e233-8ff9-7400-af56-dc2f15233603/exec-38c6c3d7-b532-4070-bb27-6263295e61c3.png`.

## Output

Output image: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/references/camp_admin_locations_resource_locked_reference_v3.png`.

Output SHA-256: `30173E38A6A445B22EAC5080F8504323CC48EB8368D2A4C0DC104F73F217952C`.

Output canvas: 1672×941 pixels, RGB. The GUI design remains intended for a 900×540 native layout; the reference raster retains v2's full framing.

## Changed region

Only the bottom-right action button changed: its label is `Closure Locked`, with a dark subdued face, muted gray edge, and dim but legible gray lettering. The control occupies approximately x=1202–1337 and y=688–739 on the 1672×941 source canvas.

All six location rows, the Brandenburg selection, the 14.8 thousand custody value, other labels and values, tabs, background, alignment, and the three active action buttons remain visually as in the supplied reference. Full-size inspection found no button-label overlap; `Closure Locked` is centered and spelled exactly.

## Decision reason and correction

The output is a neutral `Closure Locked` design state with no painted cost or specific blocked reason. A post-generation source review corrected the initial rationale: 14.8 thousand living detainees alone do not block `camp_rework_can_dismantle_selected_site` when their rows reconcile, because an accepted dismantlement start releases the recorded survivors. The v3 image is used for an insufficient Political Power or support-equipment quote while custody remains reconciled and Release Survivors is available. The [three-scale resource-lock review](../mcp/locations_resource_locked_actions_2026-09-27.md) is its matching native fixture. The earlier custody-only justification is rejected and the separate forced custody-lock MCP diagnostic is archived as invalid route evidence.

## Remaining fidelity risks

ImageGen returned a full-frame edit, so subtle texture and antialiasing differences may exist beyond the button even though the layout, lettering, values, and controls were visually reviewed at source size. The label and disabled appearance are clear at the reference's saved resolution.
