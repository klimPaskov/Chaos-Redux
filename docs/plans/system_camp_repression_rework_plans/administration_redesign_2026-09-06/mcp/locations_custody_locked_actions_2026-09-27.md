# Rejected Locations custody-lock diagnostic

Disposition: rejected as a route-valid GUI fixture; the saved images remain diagnostic only.

The three installed HOI4 MCP 3.5.1 renders used unchanged current GUI source and showed separate active Work, Purpose and Release rectangles plus a nonclickable `Closure Locked` rectangle at 1280×720, 1920×1080 and 125% UI scale.
The [hash-verified artifact manifest](after/locations_brandenburg_custody_locked_3_5_1/manifest.json) retains the exact source revision, inputs, 18 original images/JSON artifacts and their checksums.
Those geometry observations remain true, but the declared reason for the locked closure was false.

The fixture pictured 14.8 thousand living detainees and forced `camp_admin_site_dismantle_locked_custody` visible on the assumption that living custody alone blocks dismantlement.
Current `camp_rework_site_can_start_dismantlement` accepts an active initialized site with valid authority and reconciled rows even when people remain in custody; `camp_rework_start_dismantlement` calls `camp_admin_integration_reform_site` before starting the timer, so the survivor release is part of the accepted start.
The actual custody-locked variant covers a closed site under another order, changed authority, or unreconciled living rows, as its localisation tooltip says.
This fixture declares none of those conditions and its active Release button would be misleading if rows were unreconciled.
Therefore the images must not be counted as a route-valid, native-availability or accepted UI state.

The corrected three-scale fixture uses reconciled living custody, an open reform route and insufficient resources for the additional physical-closure quote, making `camp_admin_site_dismantle_locked_resources` the fourth control while Work, Purpose and Release remain available.
Its evidence is recorded separately in [the resource-lock review](locations_resource_locked_actions_2026-09-27.md).
The painted [Locations v3 reference](../references/camp_admin_locations_resource_locked_reference_v3.png) remains usable as a neutral `Closure Locked` design state for an insufficient resource quote. Its original custody-only rationale was corrected in the art handoff.
