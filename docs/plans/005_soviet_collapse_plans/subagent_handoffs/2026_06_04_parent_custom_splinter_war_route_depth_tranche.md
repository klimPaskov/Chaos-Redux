# Event005 Parent Custom Splinter War Route Depth Tranche

Date: 2026-06-04

## Scope

Parent implementation tranche for the Soviet Collapse focus-depth complaint. This pass targeted shared custom-splinter focus reward helpers rather than adding more national spirits.

Touched files:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

No flag files, `.tga` files, flag sprites, flag `.gfx`, or visual flag assets were touched.

## Gameplay Changes

Changed helper behavior:

- `soviet_collapse_apply_custom_splinter_enemy_front_identity_payload`
- `soviet_collapse_apply_custom_splinter_hidden_doctrine_identity_payload`

Before:

- Enemy-front focuses prepared the front, but the stronger war-route bonus helper only fired from later war-plan flags.
- Hidden-doctrine focuses gave route preparation and local rewards, but did not consistently create an immediate aggressive map payoff.

After:

- Enemy-front focuses now apply the custom splinter war-route bonus immediately through `soviet_collapse_apply_custom_splinter_war_plan_bonus`.
- Enemy-front focuses now apply expansion claims directly and high-chaos neighbor expansion planning for high-chaos successors.
- Hidden-doctrine focuses now spawn assault columns, core currently held territory through the expansion package, create expansion war plans, and apply high-chaos neighbor expansion planning.
- This affects the shared focus-helper surface used by 36 enemy-front focus calls and 19 hidden-doctrine focus calls in `005_soviet_collapse_custom_splinters.txt`.

Localisation updated:

- `soviet_collapse_apply_custom_splinter_enemy_front_identity_tt`
- `soviet_collapse_apply_custom_splinter_hidden_doctrine_identity_tt`

## Why This Is Aligned

The user complaint was that focuses still felt shallow, generic, and idea-spammy. This tranche does not add new ideas. It turns existing military and hidden-doctrine focuses into concrete mechanics: war-route packages, assault formations, cores on held ground, claims, war plans, and AI expansion pressure.

## Validation

Ran brace/BOM scan:

- `common/scripted_effects/005_soviet_collapse_effects.txt`: final brace depth 0, min depth 0.
- `localisation/english/005_soviet_collapse_l_english.yml`: final brace depth 0, min depth 0, UTF-8 BOM preserved.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: final brace depth 0, min depth 0, UTF-8 BOM preserved.

Ran `git diff --check` on touched files and the scoped custom splinter focus file: passed.

Ran unsupported operator scan on touched files and the scoped custom splinter focus file: no matches.

Ran direct focus idea operation scan on all four Event005 focus files:

- `005_soviet_collapse_republics.txt`: 0 direct idea ops.
- `005_soviet_collapse_custom_splinters.txt`: 0 direct idea ops.
- `005_soviet_collapse_factory_successors.txt`: 0 direct idea ops.
- `005_soviet_collapse_ancient_restorations.txt`: 0 direct idea ops.

Ran no-flag diff guard: no `gfx/flags`, `.tga`, flag sprite, flag `.gfx`, or flag asset path appeared.

## Remaining Work

- The focus trees still need more country-specific direct decision/event payoff surfaces beyond shared helpers.
- The active focus auditor subagent is still reviewing `005_soviet_collapse_custom_splinters.txt` for layout/crowding and pathline risk.
- Major republic layout and Ukraine/Belarus/Kazakhstan depth still need separate parent passes.
