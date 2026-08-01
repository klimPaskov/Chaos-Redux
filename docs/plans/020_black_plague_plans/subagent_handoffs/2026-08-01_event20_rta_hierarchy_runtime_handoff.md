# Event 020 RTA hierarchy runtime handoff

Parent follow-on note (2026-08-01): the current worktree extends this runtime handoff with three shared-category continuing actions. Distributed Instinct uses `black_plague_rat_distribute_the_nests`, Dominant Beast uses `black_plague_rat_seat_the_alpha`, and Emergent Cunning uses the selected-state `black_plague_rat_decode_route_memory` action. The latter now consumes the canonical internal-transport exposure ledger for a valid human enemy logistics target; the original ownership note below is historical for the bounded hierarchy-runtime tranche.

## Scope

This handoff covers the bounded Package A runtime tranche for the shared `RTA` Rat Nation carrier.
The patch preserves the existing two-tag model, route-module flags, cap refresh, pulse scheduler, state-marker absorption, and Rat King source selection.
No tags, focus nodes, assets, models, or world-periodic on-actions were added in the bounded tranche recorded below. The parent follow-on adds only the three route actions named above inside the existing shared category.

## Files changed

- `common/script_constants/020_black_plague_rat_constants.txt`
- `common/scripted_effects/020_black_plague_rat_effects.txt`
- `common/scripted_triggers/020_black_plague_rat_triggers.txt`
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt`

The scripted effects and AI files already contained concurrent route-module edits from the parent worktree, and those edits were preserved.

## Helper and constant map

### Constants

`black_plague_rat_hierarchy_route` centralizes the positive tuning values for Distributed, Dominant, and Emergent runtime behavior.
It contains state-scaled cap gain, pulse mass gain or penalty, merger cooldown bands, marker inheritance, King candidacy adjustments, and the hierarchy AI priorities.
`emergent_route_exposure_gain = 3` is reserved for the valid transport or rat-occupation exposure consumer in the spread-effects surface, which is outside this assigned file ownership.

### Scripted triggers

- `black_plague_rat_hierarchy_is_distributed` checks the existing country variable against `constant:black_plague_rat_hierarchy.distributed`.
- `black_plague_rat_hierarchy_is_dominant` checks the existing country variable against `constant:black_plague_rat_hierarchy.dominant`.
- `black_plague_rat_hierarchy_is_emergent` checks the existing country variable against `constant:black_plague_rat_hierarchy.emergent`.
- `black_plague_rat_merger_cooldown_ready` gates state-marker consolidation against `black_plague_rat_merger_ready_date` and `global.date`.
- `black_plague_rat_state_has_logistics_pressure_target` identifies capital, coastal, rail, and supply-node state targets for Emergent AI front requests.

### Scripted effect call sites

- `black_plague_rat_refresh_division_cap` adds 2 cap per controlled state for Distributed, adds 12 persistent cap for Dominant, and subtracts 10 from the aggregate cap for Emergent before the existing base and maximum clamp.
- `black_plague_rat_process_country_pulse` subtracts 2 Brood Mass for Distributed, adds 4 for Dominant, and subtracts 2 for Emergent during each normal pulse before the existing state-count gain and clamp.
- `black_plague_rat_try_absorb_adjacent_brood` now requires the merger cooldown trigger, adds one inherited capped brood unit for Dominant when a valid marker is absorbed, and schedules a 45-day Distributed, 75-day Dominant, or existing 60-day fallback cooldown after a successful consolidation.
- `black_plague_rat_select_king_source` subtracts 15 from Distributed candidacy, adds 10 for Dominant, and adds 20 for Emergent before the existing best-score comparison.

### AI call sites

- `black_plague_rat_hierarchy_distributed_ai` favors burrow and swarm templates, coverage requests, and reserve coverage.
- `black_plague_rat_hierarchy_dominant_ai` favors brutes and carrion guards, concentrated fronts, and nation-state pressure.
- `black_plague_rat_hierarchy_emergent_ai` favors dock and brute templates and logistics-target pressure across capitals, coasts, rail, and supply nodes.

The focus tree remains the owner of the one-time route choice and its route graph.

## Before and after behavior

Before this tranche, `black_plague_rat_hierarchy` was written by the RTA focus tree but had no runtime consumer outside focus availability and localisation.
After this tranche, the same variable changes the RTA cap, Brood Mass pulse, marker inheritance and cooldown, Rat King candidacy, and AI template and target preferences.
The global 180-division maximum remains authoritative, and all subtractive effects use explicit `subtract_from_*` operators with positive constants.

## Validation and evidence

- Constant-reference audit found all 23 `black_plague_rat_hierarchy_route` consumers declared in the constants table.
- Brace-count hygiene was balanced for all four touched gameplay files after the patch.
- Read-only Event Chain Viewer scan completed with workspace revision `59b15a49d1943ed9e58437c21d0e5149d214fde76addb5dc7c7c73dd8d188948` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4bd8342971e4e9e2117b08f8227aa2d6b014713149732d67ede31ea8492ea253/682d5fa2baa6869354af34a5eb62c44eac83027e7a59f0b2124aef5fb5f2d058/event-scan-59b15a49d194.json`.
- Read-only focus inspection completed with revision `e5a6750c69277663ac5d8ee1ffccd21c5d9990b533e8ad1b483824cc11ff1f97` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4afe69f7bbc31e13e16ffd61dc04c019dd25888fa447f3b2b27600318e1b182a/c3c60a892a156969a3fc3e723c70e2c8ccc5040da476ab618f9f28f6be521002/focus-inspect.e5a6750c69277663ac5d8ee1ffccd21c5d9990b533e8ad1b483824cc11ff1f97.json`.
- The focus inspection reported 42 blocking generic or missing focus-sprite diagnostics in the existing tree inventory, which are outside this runtime helper tranche.

## Risks and follow-up

- The historical Emergent `+3` route-exposure constant remains a separate pulse tuning value. The parent follow-on's selected-state route-memory action uses its own centralized exposure amount and the canonical transport ledger; it does not bypass ordinary establishment rules.
- The focus tree currently contains concurrent hierarchy graph work, so the parent must re-run focus inspection after its three-way route rewrite and confirm that each route writes exactly one hierarchy value.
- No HOI4 runtime launch or live save validation was performed, in line with repository instructions.
- No dedicated Clausewitz parser is installed in the repository, so validation is limited to targeted reference checks, brace hygiene, and read-only MCP evidence.

## Parent follow-up

The parent follow-on has supplied the route-memory action in the shared decision category. Re-run the RTA focus and AI audits after any future hierarchy graph changes and preserve the two-tag `RTA` and `RTX` invariant.
