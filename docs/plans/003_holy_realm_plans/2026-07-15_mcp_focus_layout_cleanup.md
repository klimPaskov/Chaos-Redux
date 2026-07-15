# Holy Realm focus layout cleanup — MCP pass

## Scope

This pass cleans the 111-focus `THR_focus` national tree in `common/national_focus/003_holy_realm.txt` using the HOI4 focus-tree skill, the offline HOI4 references, and MCP workspace `mod_chaos_redux_ea3b2d67c2c0`.

## Changes

Only fixed coordinates changed:

- `THR_sit_beneath_prayer_flags`: moved from column 9 to 12 to shorten its doctrine connector.
- `THR_fourth_quiet`: moved from column 9 to 7 to clear the mountain-granary connector.
- `THR_buddha_mandate`: moved from column 17 to 15 to reduce node-intersection pressure at the governance convergence.

No focus IDs, prerequisites, rewards, AI, localisation, icons, or gameplay flags changed. No new icon assets are needed.

## MCP evidence

Final inspection returned `status: ok`, `tooClose: 0`, and these layout metrics:

- connector crossings: `31`
- node intersections: `22`
- long connectors: `11`
- maximum horizontal span: `30`
- maximum Manhattan span: `32`

The final MCP diagnostics returned three governance convergence through-node warnings. The earlier long doctrine connector and mountain-granary through-node warning no longer appear in the bounded layout diagnostics. The tree was rendered through MCP as HTML, SVG, PNG, JSON, source-map, and layout-plan artifacts.

## Follow-up

The remaining governance warnings are attached to a deliberate multi-parent convergence into `THR_buddha_mandate`. A full removal would require moving or redesigning the three governance support branches, so it is not included in this small cleanup.
