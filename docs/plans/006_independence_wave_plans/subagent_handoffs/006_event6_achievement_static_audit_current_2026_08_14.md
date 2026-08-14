# Event 006 achievement static audit — current 2026-08-14

## Scope and disposition

This is a source and asset audit of the sixteen accepted Event 006 achievement rows. It verifies definition, localisation, icon-family, and proof-writer coverage without claiming live unlock, save/load, or campaign reachability. The whole-event status remains HOLD / PARTIAL because package breadth, formable gates, League reachability, super-event 23, GUI evidence, and MCP lifecycle evidence remain open.

## Matrix and definition coverage

The accepted matrix `docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv` contains 16 unique `chaosx_006_*` IDs. `common/achievements/chaos_redux_achievements.txt` contains exactly the same 16 IDs, with one balanced achievement block and a `happened` clause for every row.

The verified IDs are `chaosx_006_one_state_to_statehood`, `chaosx_006_no_master`, `chaosx_006_peace_with_host`, `chaosx_006_break_reconquest`, `chaosx_006_found_league`, `chaosx_006_cross_regional_league`, `chaosx_006_rescue_member`, `chaosx_006_regional_formable`, `chaosx_006_volga_bulgaria`, `chaosx_006_assyria_survives`, `chaosx_006_small_to_major`, `chaosx_006_radical_bloc`, `chaosx_006_every_flag_survival`, `chaosx_006_balanced_patrons`, `chaosx_006_league_arbitrator`, and `chaosx_006_host_remnant`.

## Localisation coverage

`localisation/english/006_independence_wave_achievements_l_english.yml` is UTF-8 with BOM and provides all 48 expected player-facing keys: one `NAME`, one `DESC`, and one achievement tooltip for each of the 16 rows. No matrix-owned name, description, or tooltip key is missing or duplicated in the audited file.

Tooltip keys intentionally use the established `independence_wave_achievement_<suffix>_tooltip` convention rather than inventing an ID-shaped `_tooltip` alias. The text describes player-visible conditions and avoids implementation-history wording.

## Icon coverage

`gfx/achievements/` contains 48 files matching the 16 Event 006 IDs across the normal, grey, and not-eligible variants. No achievement row lacks its icon family. This is file-presence evidence; runtime sprite loading and in-game presentation are outside the static audit.

## Proof-writer coverage

Every matrix ID and its corresponding `independence_wave_achievement_<suffix>` proof namespace is referenced by the current achievement definition, scripted effect, or scripted trigger surfaces. The audited Event 006 proof surfaces are:

- `common/scripted_effects/006_independence_wave_achievement_effects.txt`
- `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`
- `common/on_actions/006_independence_wave_achievement_on_actions.txt`
- `common/achievements/chaos_redux_achievements.txt`

The proof system uses generation-local flags, dates, variables, arrays, and bounded transaction hooks. The source contains no periodic world scan in this achievement surface.

## Remaining limits

This audit does not prove that every achievement can be earned in a live campaign. That claim still depends on the 32/29/161/40 package authority, admitted formable and League contracts, high-chaos/super-event gates, scenario provenance, and the deferred Event MCP lifecycle projection. It also does not substitute for user-owned live gameplay validation.

No achievement source, localisation, icon, event, package, or workbook file was changed by this audit. This handoff records current evidence only.
