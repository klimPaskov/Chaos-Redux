# Event005 Parent Focus Tree Cleanup Tranche

Timestamp: 2026-06-04 17:39 UTC

## Scope

This tranche addresses the latest Soviet Collapse focus-tree cleanup request in a bounded way. It does not claim the full focus-tree overhaul is complete.

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_173429_event005_soviet_collapse_focus_delta_audit.md` was produced by the read-only focus audit subagent.

No `gfx/flags` files were edited.

## Gameplay Changes

- Strengthened `soviet_collapse_apply_focus_high_chaos_identity` so high-chaos focus rewards are not only light stats:
	- first qualifying high-chaos focus grants assault templates, assault columns, stockpile support, claims, and Moscow/neighbor expansion pressure
	- later qualifying focuses still apply neighbor expansion and breakaway conflict planning
	- the package is guarded by `soviet_collapse_high_chaos_focus_war_package_granted` to avoid repeated free army bursts from every high-chaos focus
- Repositioned Ukraine focus lanes so the early military, industry, League, and expansion paths are easier to distinguish:
	- military lane pulled into the center instead of crossing the late expansion lane
	- industry/logistics lane moved left
	- late expansion/high-chaos focuses moved right and staggered below their prerequisites
	- one diplomacy coordinate collision introduced during this pass was fixed
- Repositioned Belarus rail and forest branches:
	- rail logistics path is more evenly spaced
	- forest mutually exclusive branches are separated from their surrounding path lines
- Fixed the Moldova simple axis-blocking pathline identified by the focus audit:
	- `moldova_soviet_collapse_the_river_state` moved off the same vertical line as `moldova_soviet_collapse_tiraspol_depot_belt`
	- its prerequisites now route through `moldova_soviet_collapse_republic_of_crossings` plus one of the relevant river/road/state branches, instead of drawing a long line through earlier focuses

## Validation

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_republics.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_173429_event005_soviet_collapse_focus_delta_audit.md`
- Brace balance check on:
	- `common/scripted_effects/005_soviet_collapse_effects.txt`
	- `common/national_focus/005_soviet_collapse_republics.txt`
- Unsupported operator scan:
	- no `<=`
	- no `>=`
- Focus coordinate parser:
	- no duplicate focus coordinates in `common/national_focus/005_soviet_collapse_republics.txt`

## Remaining Issues

The full Soviet Collapse focus-tree goal is still incomplete. The current audit report lists the remaining priority order:

- Moldova needs real crossing/Dniester/Prut decision mechanics, not only layout cleanup.
- Generic helper rhythm is still high across many custom splinter trees.
- Baltic, internal republic, generic breakaway, and many custom splinter trees still need focus-staged decisions.
- Kazakhstan and Central Asia still need pathline/payoff passes.
- Compact chaos and ancient-restoration trees still need either accepted compact status or deeper mechanics.
