# SCN-008 dead-option repair

Date: 2026-09-20.

Status: implemented as a narrow source repair; Event 006 remains HOLD / PARTIAL.

## Finding

The frozen `chaosx.triggerable_scenarios.80` event is success-only. Its event trigger requires `independence_wave_scenario_committed`, while the `.80.b` option required `NOT = { has_global_flag = independence_wave_scenario_committed }` and could never be visible during ordinary firing. The option's blocked-package count condition did not create a valid failure publication path because the event itself rejects every non-committed state.

## Change

The unreachable `.80.b` option was removed from `events/006_independence_wave.txt`. Its orphaned `chaosx.triggerable_scenarios.80.b` localisation key was removed from `localisation/english/006_independence_wave_scenario_l_english.yml`.

The success-only publication contract is unchanged: `independence_wave_scenario_committed` is set once, `chaosx.nr6.2` is dispatched before `chaosx.triggerable_scenarios.80`, and failed or rolled-back generations clear the committed receipt without dispatching either public result event. No allocator, package admission, FORM-48, Join, failure dispatch, or pre-Event-006 surface changed.

## Evidence

The static SCN-008 scenario matrix passes with 32 declared cells and eight edge cases. It reports one committed setter, one ledger-visibility setter, one scenario-result dispatch, one scenario-log dispatch, the required `chaosx.nr6.2 -> chaosx.triggerable_scenarios.80` order, and zero failed-branch result dispatches.

The focused read-only `hoi4.event_inspect` lint for `events/006_independence_wave.txt` returned `EVENT_INSPECTED_PARTIAL` with source revision `7bc390e9516d5b5dfe63dbd72b96eddd673953d1ad2177f259c603cef9509573`, graph hash `7515b51df827657755d7d03350ee5786cd35f05604a1ce64ad805354fb596225`, zero blocking diagnostics, and zero skipped sources. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af452b5945fc2a0b003bfc922cad7ae52ec772a4e21f2e3f776ca69fc0c2b06f/22cadfc583893d533b19ad3342934ef8e50b9e1ae1f1eac76643cee611d50c1c/event-lint-7bc390e9516d.json`.

The matching read-only options render returned `EVENT_RENDERED_PARTIAL` at the same revision with layout hash `7b3cb4b8de71491ff47129c5191eb650d16451f4c5f579321e111141b9b56ebc`, 24 selected nodes, and 42,772 omitted nodes. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3efcc592ffd04c3a7dbed725d72102853f15fd4c8682e1caad74d82f0ca9b125/d4ae4b9dc505b065393c6d5f720d5bd14f52edd5517665e63e3c112b0783877d/event-options-7bc390e9516d-manifest.json`.

An attempted read-only semantic comparison against the immediately preceding Event MCP revision `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964` returned `EVENT_REVISION_NOT_CACHED`, so no before/after semantic comparison artifact is claimed.

## Scope limits

This repair does not establish helper or lifecycle semantics, native UI fidelity, live firing, save/load behavior, package reachability, or whole-event completion. The completion follow-up remains the current read-only status receipt: 161 selectable rows remain unattested, identity/portrait/flag gates remain open, typed probability comparison remains incomplete, and Event 006 remains HOLD / PARTIAL.

Historical handoffs may continue to mention the removed `.80.b` option as prior audit evidence. They are not current source authority and were not rewritten.
