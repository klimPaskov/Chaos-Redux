# Event 012 terminal retry callback fix

## Scope

This narrow decision-surface repair fixes the retry lifecycle after a terminal World protocol is refused or rejected.
It does not add tags, depend on the Independence Wave, alter model work, create a new decision system, or change public text.

## Changed files and identifiers

- `events/012_africa_world_package_union_war.txt`: `africa_world_package.757` now fires the existing `africa_world_package.758` choice event after setting `africa_world_terminal_protocol_retry_requested`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_terminal_retry_callback_fix_2026-08-03.md`: this implementation handoff.

## Behaviour

Before this patch, event `africa_world_package.757` set the retry receipt but never fired the only event that consumes it.
Because `africa_world_package.758` is `is_triggered_only`, a refusal left `africa_world_terminal_protocol_blocked` and the active protocol flag in place indefinitely.
After this patch, accepting the retry prompt immediately opens event `africa_world_package.758` in the same host-country scope.
Each existing retry option clears the receipt, blocked state, and prior protocol flags before beginning the selected protocol again.

## Validation

Static source review confirmed one call from `africa_world_package.757` to `africa_world_package.758`, the retry receipt trigger on event `.758`, and cleanup in both `.758` options.
The reviewed lifecycle is refusal or rejection, retry prompt, protocol-choice event, state cleanup, and selected protocol restart.
The read-only Event MCP trace returned `EVENT_INSPECTED_PARTIAL` for workspace `mod_chaos_redux_ea3b2d67c2c0` and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25920d36f7cb88eaa33de81518722e3f1b0ba51254a6ed20369ba9f05a69f17f/b567c4d24939aad4e7d62617c9503d006f47e36128297e8dd282e72abee301b9/event-trace-546c6275d972.json`.
The matching Event MCP lint produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bdd1cdd54ca731c3e768ed89daaa0b5c4a6d302f66bf91f45431feb64bd98529/941c9e3919c68577f86eeb89d1407d301dc77d0e22f56b88bf4233dc8affd839/event-lint-546c6275d972.json`.
Both MCP reports include whole-workspace unresolved diagnostics, so they are structural evidence and not patch-specific runtime acceptance results.
No decision-owned GUI file changed, so GUI inspection and rendering were not applicable.
Live HOI4 validation was intentionally skipped because it is outside this task's authorized validation scope.

## Remaining audit findings

The sixteen priority-member force decisions charge political power in visible costs while their shared effect also removes a trained cohort from manpower, which is mechanically valid but not fully clear in the visible cost presentation.
Actions 71 and 72 remain deliberately gated behind `africa_fictional_pathogen_review_authorized` pending their real fictional disease package.
Actions 74 through 76 remain deliberately unavailable until `africa_strange_formation_package_ready` because model work is deferred.
`africa_priority_member_has_active_event6_shell_receipt` is an unused compatibility-named alias to direct carrier tags, not a runtime Event 006 or Independence Wave dependency.
