# Parent Tranche Handoff: Dynamic War Pressure and High-Chaos Helper Routing

## Scope

Bounded Event005 Soviet Collapse scripted-logic tranche.

No flag, sprite, gfx, interface, or `.tga` files were touched.

## Files Changed

- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

## Identifiers Changed

- `has_soviet_collapse_anti_soviet_breakaway_war`
- `soviet_collapse_apply_focus_legal_recognition`
- `soviet_collapse_apply_focus_socialist_sovereignty`
- `soviet_collapse_apply_focus_military_consolidation`
- `soviet_collapse_apply_focus_depot_and_supply_control`
- `soviet_collapse_apply_focus_league_preparation`
- `soviet_collapse_apply_focus_diplomatic_plan`
- `soviet_collapse_apply_focus_republican_compact_plan`
- `soviet_collapse_apply_focus_security_supply_plan`
- `soviet_collapse_apply_focus_foreign_recognition_plan`
- `soviet_collapse_apply_focus_foreign_league_plan`
- `soviet_collapse_apply_focus_league_security_plan`
- `soviet_collapse_apply_focus_lawful_supply_plan`
- `soviet_collapse_apply_focus_foreign_supply_plan`
- `soviet_collapse_apply_focus_league_logistics_plan`
- `soviet_collapse_apply_focus_civil_military_authority_plan`
- `soviet_collapse_apply_focus_foreign_security_plan`
- `soviet_collapse_apply_focus_foreign_channel`

## Before

`has_soviet_collapse_anti_soviet_breakaway_war` used a hardcoded tag list. Special successors, late dynamic releases, and event-created republics outside that list did not count as anti-Soviet breakaway war pressure.

Several common focus reward helpers advanced ordinary republic variables, recovery, or route payloads without calling the high-chaos payload. A high-chaos successor using those helpers could finish focuses without receiving the aggressive claims, assault-column, neighbor-conflict, and SOV pressure behavior expected from high-chaos countries.

## After

`has_soviet_collapse_anti_soviet_breakaway_war` now detects any existing non-SOV country at war with SOV if it has one of the Soviet Collapse breakaway flags:

- `soviet_collapse_breakaway`
- `soviet_collapse_event_created_republic`
- `soviet_collapse_high_chaos_successor`

The common focus helper families now also call `soviet_collapse_apply_high_chaos_focus_payload = yes`. That helper is self-gated by `has_country_flag = soviet_collapse_high_chaos_successor`, so normal republics keep the same behavior while high-chaos countries convert common political, military, depot, foreign, and league focuses into aggressive gameplay.

## Validation

- `git diff --check -- common/scripted_triggers/005_soviet_collapse_triggers.txt common/scripted_effects/005_soviet_collapse_effects.txt` passed.
- Brace balance ended at zero for both touched script files.
- No unsupported `<=` or `>=` operators were found in the touched files.
- `git status --short -- gfx/flags interface/flags` returned no scoped flag changes.

## Remaining Gaps

This is not the full Soviet Collapse focus-tree rewrite. The current focus audit still identifies Ukraine route-row crossings, Belarus rail/league convergence issues, repeated helper-packet reward rhythm, shallow compact special trees, weak decision integration in several republic trees, and missing postwar/settlement handling on some claim and wargoal focuses.
