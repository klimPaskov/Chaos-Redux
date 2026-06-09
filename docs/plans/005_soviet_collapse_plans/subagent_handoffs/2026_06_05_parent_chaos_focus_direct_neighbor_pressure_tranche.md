# Event005 Parent Handoff: Chaos Focus Direct Neighbor Pressure Tranche

Parent role: main Codex implementation agent

This is not an Event005 completion claim.

## Scope

The user-reported blocker is that Soviet Collapse focus trees still feel passive, helper-heavy, and disconnected from the intended chaos gameplay. This tranche strengthens the common chaos focus payoff path so existing chaos identity, assault, and supply focuses create direct map pressure without adding more national-spirit or idea spam.

Flags, sprites, images, and other visual assets were not touched.

## References Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- Current focus audit subagent handoff: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_173628_event005_custom_chaos_focus_audit_readonly.md`

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_parent_chaos_focus_direct_neighbor_pressure_tranche.md`

## Gameplay Changes

Added `soviet_collapse_apply_chaos_direct_neighbor_pressure`.

The helper:

- dynamically scans neighboring countries instead of hardcoding target tags;
- targets Moscow, Soviet breakaways, event-created republics, and high-chaos successors;
- adds claims on neighbor-controlled states;
- cores controlled claimed states for high-chaos or very high chaos contexts;
- applies conquer and antagonize AI strategies against valid neighboring targets;
- creates annexation war goals against valid targets;
- declares direct wars for high-chaos successors, hidden-doctrine/endgame chaos states, terminal collapse, chaos scenario launches, and chaos tier 4 or 5;
- also applies Soviet war-goal and direct-war pressure through the same conditions.

Wired the helper into:

- `soviet_collapse_apply_high_chaos_focus_payload`
- `soviet_collapse_apply_focus_chaos_assault_plan`
- `soviet_collapse_apply_focus_chaos_supply_plan`
- `soviet_collapse_apply_focus_high_chaos_identity`

This makes the existing repeated helper call sites in republic and custom splinter focus trees materially more aggressive without adding more `add_ideas`, `remove_ideas`, or timed idea churn.

## Localisation

Updated `soviet_collapse_apply_focus_chaos_assault_plan_tt` to describe immediate pressure against Moscow and neighboring breakaways, including direct neighbor wars for extreme chaos successors.

## Subagent Result Integrated

The focus audit subagent completed a read-only audit and reported:

- 32 trees / 1,197 focuses parsed across custom splinters, factory successors, and ancient restorations;
- 0 duplicate focus IDs;
- 0 duplicate coordinates;
- 0 same-row/upward prerequisites;
- 0 mutex-AND blockers;
- 0 missing `ai_will_do`;
- 0 direct focus reward idea churn in the audited three files;
- no flag, sprite, image, or asset edits.

The audit's main unresolved finding is design depth: many focus trees remain helper-heavy and need parent-level route identity work.

## Validation

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt localisation/english/005_soviet_collapse_l_english.yml`
- Brace balance on the touched scripted effects and localisation files
- Localisation BOM check for `localisation/english/005_soviet_collapse_l_english.yml`
- Exact call-site scan for `soviet_collapse_apply_chaos_direct_neighbor_pressure`

## Remaining Gaps

- This does not finish the requested full focus-tree rework.
- Many custom splinter trees still read as helper-heavy when inspecting focus file rewards directly.
- Compact chaos and ancient trees still need more country-specific visible route payoffs.
- The next parent tranche should pick the weakest custom splinter groups and convert repeated settlement/radical forks into bespoke branches with visible decisions, targets, units, and state packages.
