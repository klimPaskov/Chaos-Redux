# Isolated Event 16 state-flag parser repair

Launch 13 reports the unsupported `set_timed_state_flag` effect in `brilliant_scientist_execute_long_range_delivery_strike`.
The parent changed only that keyword to `set_state_flag` in `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt`.
The flag identifier, existing duration temporary, its constant-backed initialization, target state scope, and all other active Event 16 source bytes remain unchanged.
This is the explicitly authorized isolated parser-repair exception to protecting active Event 16 work.

The offline Effects page documents `set_state_flag = { flag = ... days = ... }`.
Installed effects documentation confirms state scope, and vanilla `RAJ_GOE_scripted_effects.txt:526` uses a timed state flag with that schema.
The immediate original is under `pre_patch_event16_state_flag14/`, and `event16_state_flag14.json` records both hashes.
Exact keyword reversal reproduces the complete immediate original.

The narrow Event 16 MCP trace was partial with helper projections deferred; it does not prove timer behavior.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c9eef6b362c3e0a088e515aa02929cc446072b716a38299efc68642e30697c7/6371b86ec2f1b41e7f848f3bf803d383e6c7cf8caa8b4c7af5681662010b597a/event-trace-1102e50fad94.json`.
Native parser clearance and cooldown expiry in a live test remain pending.
