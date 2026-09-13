# Event 32 capture-readiness declaration repair

Launch 13 reports the absent `missiles_tuning.program_capture_readiness_loss_negative` constant in two site-loss paths, repeated across both parser passes.
The same file already implements capture-shell readiness loss using `subtract_from_variable` and the existing positive `missiles_tuning.program_capture_readiness_loss` constant, whose declared value is 30.
The parent applied that existing operation to the two rejected calls: site inheritance loss and site capture loss.
No new tuning value was introduced, and their country scopes, reserve deductions, flags, subsequent clamps, network refreshes, and other source bytes remain unchanged.

Installed `effects_documentation.md` documents variable subtraction, and vanilla `GER_scripted_effects.txt` supplies subtraction precedents.
The existing capture-shell implementation is the closest package-owned precedent.
Immediate originals are under `pre_patch_event32_capture_loss14/`, with hashes and counts in `event32_capture_loss14.json`.
The complete resulting file matches exactly the two prescribed replacements.

The narrow Event 32 MCP trace returned `EVENT_INSPECTED_PARTIAL`, with helper projections deferred.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/436d1e0a930d8069916f2fd5495992664d02793f087b0c554a5a8e8c46cd45c6/ae29c1aa3157c798d30b877a2ff3a0e5a0c3d2b1bd538c3d5df6c34dfc1ac944/event-trace-1102e50fad94.json`.
Native parser clearance and live readiness/custody checks after capture and inheritance remain pending.
