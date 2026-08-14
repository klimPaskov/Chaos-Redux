# Event 006 focus surface constant and alias cleanup

Date: 2026-08-14

This bounded focus-surface tranche preserves the shared Event 006 tree while closing three player-facing focus tooltip aliases and making the territorial-defense doctrine reward use parser-safe file-scoped constants in the effect field that does not accept the shared script-constant token form.

Changed files:

- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/scripted_localisation/006_independence_wave_focus_scripted_localisation.txt`
- `localisation/english/006_independence_wave_focus_l_english.yml`

The effect file now mirrors the authoritative doctrine reduction and use-count values with local `@` constants for `add_doctrine_cost_reduction`. The scripted-localisation definitions use the documented `localization_key` field. The English focus localisation adds the missing `_tt` aliases for `build_permanent_foreign_service`, `discover_regional_identity`, and `coordinate_reclamation_fronts`; each alias exactly mirrors its established completion tooltip.

MCP evidence was refreshed after the edits. `hoi4.focus_inspect` returned `FOCUS_INSPECTED` and `hoi4.focus_render` returned `FOCUS_RENDERED` for `independence_wave_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The tree remains 184 focuses and 196 connectors with zero crossings and zero node intersections. The aggregate validation remains false only because the existing shared/vanilla continuous-focus icon and layout diagnostics are outside this alias/constant scope; no new Event 006 tree node or connector was introduced.

No gameplay route, focus prerequisite, AI weight, package admission, asset, or central dispatcher behavior changed.
