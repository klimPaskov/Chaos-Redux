# Event 006 post-formation focus-overlay producer handoff

Date: 2026-07-28.

## Scope

This tranche closes the dead `post_formation_overlay` assignment path for Event 006 countries that already own the shared Independence Wave framework. It does not replace a meaningful vanilla focus tree and does not claim live formation or save/load proof.

## Source changes

- `common/scripted_effects/006_independence_wave_focus_effects.txt` now preserves the full-framework flag when the assignment input is `post_formation_overlay`.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` supplies that assignment input after a successful formable commit only when the carrier still has `independence_wave_full_focus_framework` and is an active Event 006 country.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt` permits the full framework and additive overlay gates to coexist only while `independence_wave_post_formation_focus_overlay` is set. This keeps the loaded Event 006 tree visible while exposing the post-formation shared branch.

## Preservation contract

The producer only preserves the loaded framework, sets the additive/post-formation flags, and refreshes the focus layout. It never calls `load_focus_tree`, changes an existing tree, transfers territory, changes country identity, or grants a free reward. A country that retains a meaningful vanilla tree cannot satisfy the full-framework guard and is therefore untouched by this assignment.

## Validation boundary

Static source inspection confirms one producer call site, one named assignment path, and paired full/additive trigger gates. `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `independence_wave_focus_tree`; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2db3b75cf4b6b1551d4b12d29de6d18384914389dd54956aa1b12840d4f030b4/eb990f801087cfad5af1fa1a0b5cc395dac43b4e4855e54a40eccf6dab1eb21f/focus-inspect.6b0f1c16ad437b5c.json`. The existing focus audit remains the geometry authority: 308 unique focus blocks are present, but the MCP baseline still has 14 blocking geometry diagnostics and no live formable or save/load evidence. The accepted overlay-hook matrix remains open for the other twelve exact vanilla route overlays.

No Hearts of Iron IV process was launched. No fallback tree, country, portrait, advisor icon, or package admission was introduced.
