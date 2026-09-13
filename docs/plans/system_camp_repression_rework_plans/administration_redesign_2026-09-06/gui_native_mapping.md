# Administration reference acceptance and native mapping

Status: accepted for implementation under the user's explicit reference-led redesign authorization.
The parent inspected all three generated references on 6 September 2026 and selected their composition, restrained framing, horizontal navigation and context-dependent actions.
The reference files and ImageGen provenance are in `references/` alongside this document.
Generated numbers, currency, labels and hypothetical coal-stock controls are compositional examples, not accepted mechanics or historical claims.

## Native translation

The existing system-owned `repression_ledger_window` remains attached to the top bar through its player-context scripted GUI, with the existing decision-category entry point.
The native container is 900 by 540 logical pixels so the complete window fits 1280 by 720 at 125 percent scale.
The reference's broad header, three horizontal tabs, left list/right detail arrangement and compact attention strip are retained.
Vanilla `GFX_tiled_window_2b_border`, `GFX_tiled_window_small`, `GFX_tiled_window_small_selectable`, native buttons and installed HOI4 fonts supply functional controls rather than a flattened reference image.

| Reference region | Native consumer | Behavior |
| --- | --- | --- |
| Header and three tabs | `camp_admin_title`, existing close button, administration/locations/records tabs | Current view has a selected mark; each navigation hit region matches its background. |
| Administration summary | `camp_admin_summary` | Derived national industrial contribution, surviving detainees, assigned workforce and accepted monthly deaths; details on hover. |
| Three standing controls | Priority, mandate and budget selectors | Explicit choices, with separate eligibility and affordability; radical policy is never reached by cycling an economic control. |
| Two project panels | Economic project and institution program | Dynamic names/progress, target, waiting requirement and contextual country actions; no maintenance purchase grid. |
| Amber attention region | Consolidated national attention and crisis state | One current material interruption, no periodic popup; actions act on the same shared budget/control contracts. |
| Locations list | Native scrolling grid bound to a filtered camp-owned state array | Persistent selection, non-colour status text, long-name bounds and empty state. |
| Selected location | Native heading, assignment, contribution, people and consequence text | Three contextual actions, costs and requirements on hover, future programs hidden. |
| Records | Cause-separated accepted totals and scrolling institutional history | No sum of overlapping custody/occupation totals; history does not transfer responsibility to a captor. |

## Justified adaptations

The interface reports country factory-output contribution rather than money or a fictional resource currency because `industrial_capacity_factory` is a country modifier in the installed modifier documentation.
Local works and extraction remain state effects and receive accurate selected-state descriptions.
Surviving detainees and assigned workforce are subsets, never quantities that the interface adds together.
Native text uses installed fonts with genuine glyph-centering evidence; generated typography is not rasterized into controls.
Policy choices open a small contextual selection area so all options are explicit without increasing the normal screen's action burden.
The crisis reference's reserve-draw illustration becomes a supported budget review or development pause; no unsupported coal inventory is introduced.

## Evidence status

The first implementation baseline `hoi4.gui_inspect` CLI attempt failed during MCP initialization after 60000 milliseconds.
A second attempt uses the same installed production server with a longer client initialization timeout; no server source or configuration was altered.
Fresh inspect/render artifacts, intermediate image reviews and matched final scenarios remain required and will be recorded in `mcp/` and the completion report.
The earlier preserved render does not establish fresh implementation validation.
