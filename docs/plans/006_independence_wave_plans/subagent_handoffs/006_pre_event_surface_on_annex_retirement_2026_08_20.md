# Event 006 pre-event annex callback retirement

Date: 2026-08-20

## Disposition

Implemented and narrowly validated. The retired pre-event crisis surface no longer registers a global annexation callback. Event 006 remains hidden and triggered-only until a release plan is committed, so no pre-event pressure, crisis category, queue, mission, or decision is exposed to the player.

## Source change

- Deleted `common/on_actions/006_independence_wave_crisis_on_actions.txt`.
- This removes the global `on_annex` registration that called `independence_wave_recover_crisis_requester_loss`.
- The compatibility scripted-effect definition remains inert in `common/scripted_effects/006_independence_wave_crisis_effects.txt`; it is not called by any active source.
- Hardened `.tools/audit_event6_allocator.py` so the retirement audit requires the on-actions file to be absent and rejects external calls to the retired requester-loss effect. The inert definition file is intentionally excluded from the call-site scan.

## Evidence

The allocator audit passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 content attestations across 29 compatible groups, and the 3/4/5/7/10 wave ladder. It reports the pre-event crisis surface retired, with no active category, mission, cost, or queue.

The scoped static audits also pass for the country API, 102 Event 006 flag families, Statehood Ledger GUI source semantics, the SCN-008 scenario matrix, and FORM-16. Fresh Event MCP inspection and rendering of `chaosx.nr6.1` return `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` with zero selected blocking diagnostics; the workspace-wide helper/lifecycle validation remains deferred by the large-workspace limit. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f11c3aae0af46fc146bd0971f94e487046ae4ff189077457fe03956752e6ef1c/cf6ce5626e1ad2bc8000744ebb3bfbf3f90ad5df2cf19a69ec3226edc4c10f06/event-state_flow-eb1d6f6a42dc.json`. Render artifacts are recorded in the MCP result at revision `eb1d6f6a42dc91c2b61559da7ea48ff716b500692e7160ef5f9f73a8e0af7714`.

## Scope boundary

No country package, central adapter, content attestation, scenario preflight, Join order, focus tree, asset, or spreadsheet was changed. The whole event remains HOLD/PARTIAL because 161 selectable rows are still unattested and typed probability evidence plus full workspace MCP validation are incomplete. This tranche only removes the last active global callback from the intentionally retired pre-event surface.
