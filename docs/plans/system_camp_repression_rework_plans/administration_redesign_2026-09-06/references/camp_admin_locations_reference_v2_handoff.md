# Camp Administration Locations Reference v2

Status: review-only composition reference. Generated with built-in ImageGen; output is 1672×941 PNG. The four action labels are legible and match the requested wording. No text repair was needed.

## Provenance

- Output: `references/camp_admin_locations_reference_v2.png`
- Existing layout target: `references/camp_admin_locations_reference.png`
- Populated content and value source: `mcp/after/locations_current_source_1920.png`
- Institutional metal-style reference: `.agents/skills/chaos-redux-event-assets/assets/gfx_references/scripted_guis/institutional_boards/skoda_priority_mcp.png`
- Matching-family browsing aids inspected: `.agents/skills/chaos-redux-event-assets/assets/gfx_references/scripted_guis/contact_sheet.png` and `.../institutional_boards/contact_sheet.png`
- Prompt record: this file, section “Prompt record.” ImageGen received the three image paths listed above in that order.

Prompt record: Create a centered HOI4 dark-metal Camp Administration window on a muted blue-gray background, using the existing reference for framing and the populated render for content. Preserve the Administration, Locations, and Records tabs; six specified state rows with Brandenburg selected; and the supplied Brandenburg labels and values. Add exactly four separate buttons on one bottom row, left to right: “Pause Work,” “Change Purpose,” “Release Survivors,” and “Dismantle Site.” Keep text crisp and exact; add no other controls or wording.

The art is a compositional reference for the planned 900×540 native window. It does not establish native layout fit or MCP acceptance; the parent owns those checks.

## Bottom action row mapping

Each region is one button face in the selected-site pane. IDs below are proposed native element identifiers for the parent to register.

| Region, left to right | Button label | Proposed native element ID |
|---|---|---|
| Bottom action row, first face | Pause Work | `camp_admin_locations_pause_work_button` |
| Bottom action row, second face | Change Purpose | `camp_admin_locations_change_purpose_button` |
| Bottom action row, third face | Release Survivors | `camp_admin_locations_release_survivors_button` |
| Bottom action row, fourth face | Dismantle Site | `camp_admin_locations_dismantle_site_button` |

“Dismantle Site” represents a paid, selected-site closure mission. Put its requirements, cost, and consequences in the native tooltip; the reference shows only the action label.
