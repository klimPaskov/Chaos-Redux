# Event 006 generic focus MCP receipt

Date: 2026-08-03

Scope: fresh read-only inspection of the accepted shared `independence_wave_focus_tree` after the visible prerequisite repair. No focus source, reward, icon, or localisation file was edited in this receipt.

## Result

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

- 184 Event 006 focus nodes and 193 connectors resolved.
- Event 006 layout metrics have zero crossings, zero node intersections, zero isolated-focus diagnostics, and zero too-close same-row pairs. One intentional long connector spans 13 columns and one row from `independence_wave_adopt_military_archetype_program` to `independence_wave_preserve_independent_command`.
- Layout hash: `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4903b81078870392f289cda445588dfb84f3ccf978eceb831547558b896503b/5151e650145dcfd2be699fe3a54e2c9fdbeac0b20d98abb229a35dc8fd484794/focus-inspect.cf77e3b3ed8b421e.json`.

The overall inspector validation remains false because it scans the vanilla continuous-focus palette and reports fourteen pre-existing missing vanilla icon references plus one vanilla localisation warning. The only Event 006 diagnostic is the intentional long connector described above. This receipt does not convert those unrelated vanilla diagnostics into an Event 006 blocker and does not claim live or save/load validation.

## Disposition

The one-tree generic focus contract remains source/static PASS for the accepted narrowed scope. Bespoke country trees remain out of scope. No fallback tree or icon was added.
