# Political-power affordability parser repair

Launch 13 identifies invalid `political_power` triggers in the shared universal-cost affordability helper and the Event 26 medical-capacity fallback gate.
The parent changed exactly one keyword in each of `common/scripted_triggers/chaosx_universal_cost_triggers.txt` and `common/scripted_triggers/026_black_friday_triggers.txt` to `has_political_power`.
Both conditions remain `NOT = { balance < cost }`, preserving the intended inclusive affordability boundary.
No cost value, resource kind, scope, payment, AI weight, or other source byte changed.

Installed `documentation/triggers_documentation.md` documents `has_political_power` in country scope.
The offline Triggers page documents strict comparisons, and vanilla `common/decisions/anti_japan_infiltration.txt` and `ARG.txt` provide `<` precedents.
The immediate originals are under `pre_patch_pp_affordability14/`, with hashes in `pp_affordability14.json`.
Both full post-edit files match the corresponding one-keyword transformation of their archived originals.

The narrow Event 26 MCP trace returned `EVENT_INSPECTED_PARTIAL` with helper projections deferred.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9402af7c43a8c8322ffc0449b9acfb88e3cd519f0a226761b879bb06ff36c48/e5f5c529db3555d232be3b037bae95258078a98dd314c22b45012b5105f6c8c0/event-trace-1102e50fad94.json`.
Native parser acceptance and live payment tests at below-cost, exact-cost, and above-cost balances remain pending.
