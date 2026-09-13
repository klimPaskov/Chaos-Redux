# Event 28 command-power reserve gates

Two unsupported has_command_power keywords in common/scripted_triggers/028_asteroid_incoming_triggers.txt use the documented command_power country trigger.
The crater-security and material-survey helpers retain their strict greater-than comparison against decision_command_power_after_reserve, all other resources, and their hidden-trigger containers.
Both callers are ordinary available/custom_trigger_tooltip gates in common/decisions/028_asteroid_incoming_decisions.txt, not weighted modifiers.
No threshold, payment, tooltip key, scope, or AI weight changed.
Installed documentation/triggers_documentation.md and the offline Triggers command_power entry specify numeric comparisons; vanilla common/decisions/GER.txt includes a command_power comparison precedent.
Exact originals and hashes are in pre_patch_event28_command_power15/ and event28_command_power15.json.
Launch 14 contained two invalid-trigger records plus their paired unknown-trigger diagnostics; native retest and exact-boundary gameplay checks remain pending.
MCP trace returned EVENT_INSPECTED_PARTIAL with helper projections and lifecycle checks deferred: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/148e60347ad23d3255e343f94e9d5a7583c67db5049a0889db88c0ee43e19dd0/9e018abc7736eaad637da18f4f121bfb9c05b0e6807faf5648a1ab257c5e2bed/event-trace-94c858964b40.json

MCP rendering returned EVENT_RENDERED_PARTIAL, manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5576ff00e356efefa7d1463232fb00feab3a03f90b3508de73876b069c90d2cd/27e21df4bbfdd33959f4bbb7214f4999682a76868bcefce36cfae3532de7740c/event-neighborhood-94c858964b40-manifest.json
Comparison returned EVENT_REVISION_NOT_CACHED and produced no delta; helper-level MCP validation remains unavailable.
