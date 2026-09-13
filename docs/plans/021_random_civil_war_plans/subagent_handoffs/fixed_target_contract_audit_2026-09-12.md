# Event 021 fixed-target contract audit — 2026-09-12

Status: blocked by a shared-framework contract gap. Event 021 remains ready for explicit testing, but this dependency is not a reason to invent a second event-weight API.

The bounded `chaosx_scripted_system_architect` audit confirmed that `apply_individual_crisis_fixed_target_event_pressure` is named by `docs/systems/event_system/individual_crisis_targeting.md`, but is not declared or consumed by `common/scripted_effects/individual_crisis_targeting_effects.txt` or any verified Event 021 caller.

The implemented shared candidate contract is country scope, a caller-supplied temporary `individual_crisis_candidate_base_weight`, and a temporary `individual_crisis_candidate_adjusted_weight` output. It applies the documented ticket multiplier and returns zero at the individual crisis cap without mutating persistent state or event targets. Event 021 consumes this candidate contract in `event021_parent_add_target_to_selection_pool` and `event021_parent_add_scenario_target_to_weighted_pool`.

The missing fixed-target contract still needs an owning shared-system decision for calling scope, event identity, target input, resolution timing, input and output semantics, defaults, invalid-target behavior, rounding, persistent versus transient weight application, reservation and repeated-evaluation behavior, rejection, and cleanup ownership. The existing fixed-target owner list also needs reconciliation with current source because several named events resolve their targets through event-specific preflight rather than a common fixed-target weight call.

No Event 021 source change was made for this dependency. The candidate-ticket integration remains intact, and the missing helper is reported as an external shared-framework blocker rather than aliased or reimplemented locally.

Evidence: the architect returned `blocked` with no files changed. The current Event MCP lint remains partial because workspace-wide helper and lifecycle projections are deferred. No live Hearts of Iron IV run is claimed.
