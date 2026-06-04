# Event005 Focus Tree Audit Patch - CFR Gate Cleanup

Subagent role: `chaosx_focus_tree_auditor`

## Scope

Required references consulted before editing:

- Offline Paradox wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_formatter_documentation.md`.
- Vanilla precedent: `common/national_focus/generic.txt` and `common/national_focus/soviet.txt` focus syntax/layout patterns.
- Repo skill: `hoi4-focus-trees`.

No `gfx/flags` or `interface/flags` files were read or edited.

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`

## Focus IDs Changed

- `CFR_the_board_becomes_the_cabinet`

## Before

`CFR_the_board_becomes_the_cabinet` was the gate into the CFR strategy row, but it had only one prerequisite:

- `CFR_contracts_before_ideology`

That made the main strategy row reachable only after selecting the foreign contract governance route, even though the immediately preceding row presents four mutually exclusive governance choices. Selecting site committees, the planners' charter, or the concrete committee blocked the downstream tree.

The gate also sat at `x = 20 y = 8`, visually under the foreign-contract child rather than centered under the mutually exclusive governance children.

## After

`CFR_the_board_becomes_the_cabinet` now uses one OR prerequisite block over the four parallel governance follow-up focuses:

- `CFR_minutes_from_every_workshop`
- `CFR_the_engineers_overrule_the_party`
- `CFR_contracts_before_ideology`
- `CFR_housing_as_discipline`

The node moved to `x = 17 y = 8`, keeping it visually centered under the governance follow-up row before the strategy row branches out.

This is a bounded path-quality patch. It does not add ideas, new flags, new localisation keys, new helper effects, or asset references.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt`: passed with no output.
- Brace-balance check on `common/national_focus/005_soviet_collapse_factory_successors.txt`: passed.
- Unsupported operator scan for `<=` and `>=` in `common/national_focus/005_soviet_collapse_factory_successors.txt`: no matches.

## Remaining Gaps

- The CFR tree still has several visually awkward one-line `x/y` placements and indentation inconsistencies from surrounding work; this tranche intentionally avoided a broad formatting pass.
- The CFR high-chaos branch still needs deeper identity payoffs beyond this gate cleanup.
- Other Event005 focus trees remain shallow in places and still need route-depth, filter, and pathline passes.
