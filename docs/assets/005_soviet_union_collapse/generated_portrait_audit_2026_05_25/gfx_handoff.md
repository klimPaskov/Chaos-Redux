# Event 005 Generated Council Portrait Handoff

No `.gfx`, gameplay, localisation, history, country, focus, decision, event, or spreadsheet files were edited.

## Result

The active Event 005 fictional/council leader portrait set is complete as audited on 2026-05-25.

- Final DDS folder: `gfx/leaders/005_soviet_collapse/`
- Target size: `156x210`
- Contact sheet: `docs/assets/005_soviet_union_collapse/generated_portrait_audit_2026_05_25/contact_sheets/event005_active_generated_council_portraits.png`
- Active audited portrait sprites: `37`
- Missing active DDS files: `0`
- Blocked real/uncertain leaders requiring sourced portrait work: none found in the active audited set

## Main Agent Wiring Notes

The existing active portrait sprite registrations already cover all audited leaders:

- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`

No wiring is required for the current active portrait set. If the main agent adds new Event 005 countries or reactivates stale tags, route those new or reactivated leaders through the same fictional/council portrait workflow unless the leader is a real historical person, in which case the asset should be sourced rather than generated.

## Stale/Inactive Assets Left Untouched

The final portrait folder still contains inactive or stale DDS files for `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS`. They were not removed or changed because this sidecar was not authorized to alter gameplay or wiring, and the active audited set does not reference them.
