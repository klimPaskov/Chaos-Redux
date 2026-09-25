# Event 006 REG04 branch tooltip clamp audit

Status: patched within the assigned localisation scope. The parent owns final integration and live-game review.

## Changed files and keys

- `localisation/english/006_independence_wave_focus_l_english.yml`: `independence_wave_kar_guarantee_language_appeals_tt`, `independence_wave_kar_commission_border_ski_guard_tt`, `independence_wave_cri_ratify_land_hearings_tt`, `independence_wave_cri_audit_peninsular_service_rolls_tt`.
- This handoff only. No gameplay file, spreadsheet, or other documentation was edited by this pass.

## Wording decision and before/after

Each positive measure previously promised `+[?constant:independence_wave_karelia_crimea_pressure.standard_gain|0]`; it now says `up to +[?constant:independence_wave_karelia_crimea_pressure.standard_gain|0]`. Each negative measure previously displayed `[?constant:independence_wave_karelia_crimea_pressure.minor_loss|0]` as an exact delta; it now says `down by up to [?constant:independence_wave_karelia_crimea_pressure.minor_gain|0]`. The measure names and positive/negative pairings remain unchanged for all four keys. Script still applies `minor_loss`; `minor_gain` only expresses its positive maximum magnitude in text.

The change repairs a misleading exact reward claim. No other prose was rewritten: these four short measure statements had no separate vagueness, bloat, obvious explanation, repetition, overcomplication, or style issue within the assigned patch. No sourced quotation appears in these four tooltips. Dynamic constant tokens and formatting were preserved apart from the intentional `minor_loss` to `minor_gain` display substitution.

## Source and audit evidence

- Each key occurs once in the assigned localisation file and once as a `custom_effect_tooltip` reference in `common/national_focus/006_independence_wave_focus.txt`, at lines 4787, 4820, 4943, and 4976 respectively. No missing or duplicate key was found among the four. No scripted-localisation reference is involved.
- Each focus reward sets one delta from `standard_gain` and the other from `minor_loss` before calling `independence_wave_kc_apply_reg04_focus_deltas`. `common/script_constants/006_independence_wave_constants_registry.txt` defines the Karelia/Crimea bounds as 0–100 and the values as `standard_gain = 12`, `minor_gain = 6`, and `minor_loss = -6` at lines 5964–5974. `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt` clamps the four measures to those bounds at lines 97–105. This supports maximum-change language; the actual change can be smaller at a bound.
- UTF-8 BOM remains `EF BB BF`; all four changed lines remain single-line English localisation entries. No encoding concern was found for this file.
- Read-only `hoi4.focus_inspect` and `hoi4.focus_render` returned `ok` for `common/national_focus/006_independence_wave_focus.txt`. The focus render source map is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39898857c8fc1acd3325fd57b0cd1ee4b924f948e69db0b531cfbafa3d15eb19/524a5d78fc80fc2a4dbe425e1d5f66e0bc2f5ed17d11e05b9a6f29e4ab575278/independence_wave_focus_tree.focus.source-map.json`. The render gave no tooltip-text overflow or wrapping view, so in-game visual fit remains unverified. Unrelated render diagnostics were outside this patch.
- No standalone Technology Tree Viewer tool was exposed in the available package; this is a package availability gap, distinct from the exposed technology inspect/render/compare routes. No technology surface was in scope.

## Cross-surface and validation limits

The prior tooltip wording overstated the focus ledger delta near the 0 or 100 bound. The four revised focus tooltips now match the clamp behavior. No event catalog wording mismatch was identified in this narrow four-key pass; no spreadsheet handoff is needed. No further dynamic-text opportunity was identified within these four keys.

Meaningful checks were limited to exact key/reference uniqueness, the focus reward-to-ledger source path, constant sign/magnitude, BOM, and read-only focus MCP inspection/rendering. No automated tests or live-game validation were run. No unresolved wording decision, implementation handoff plan, or simplification was introduced.
