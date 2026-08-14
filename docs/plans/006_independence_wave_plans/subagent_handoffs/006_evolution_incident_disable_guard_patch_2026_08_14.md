# Event 006 Evolution Incident Disable Guard Patch

Date: 2026-08-14

## Disposition

Applied a narrow lifecycle-safety patch to the five paid Event 006 evolution incident decisions and their five resolution events.

## Source changes

Changed `common/decisions/006_independence_wave_evolution_incident_decisions.txt` so each incident row hides while its exact Event Log evolution row is disabled and cancels an in-progress paid timer when that row is disabled.

Changed `events/006_independence_wave_evolution_incidents.txt` so each resolution event rejects a stale pending flag when its exact Event Log evolution row is disabled.

The stage-specific disable flags are `events_log_disabled_evolution_6_21_1` through `events_log_disabled_evolution_6_21_5`.

This preserves the existing paid costs, timers, AI willingness values, incident options, ledgers, and generation cleanup. It only prevents a disabled evolution from resolving a queued incident after the player turns that evolution off.

## Evidence

The required pre-change weighted-surface inspection used `event_option_ai_chance` on `events/006_independence_wave_evolution_incidents.txt` and returned `PROBABILITY_SOURCE_INSPECTED` with ten candidates, zero available candidates, one unresolved item, and no inspect diagnostics.

The post-change Event 006 namespace scan returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with zero selected blocking diagnostics. The linked scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11ee4c4435b3233258fc72f5015a679c5c1963d042b6b11d57ba3fe0a1cf8db/c53e95bc9917338d68f7304e2a13ee2ff6cac5dca7b830dbea03bed3619792ab/event-scan-741883f50501.json`.

The post-change event state render returned `EVENT_RENDERED_PARTIAL` with JSON, SVG, PNG, HTML, and manifest artifacts. The render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd1e6c6e607fff006a0e15c939864571e0b5c78104c85f4ce594239b886e0652/f47f231fe9c8f580dff6552d36267a43ee4e6f402aa45d5736a2a9dab7809f7e/event-state-741883f50501-manifest.json`.

The same-source probability compare used `event_option_ai_chance` with one explicitly empty scenario on both sides. It returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=0`, ten discovered candidates, one unresolved item, and `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d9c8655f369ff7c24bcbf9928b9eddf833f7a882d424126c531e758a3a4e0a/e32ffc91fad67e97105de861421f9cdf55011f0a1d612d7450224cc59ef72e19/probability-27db0cdabd97ce5e692cb071.json`.

## Limits and follow-up

The event MCP report remains workspace-wide partial because helper and lifecycle projections are deferred. The probability compare is a same-source capability receipt, not a before-and-after balance proof, and normalized option probabilities remain withheld because the candidate pool is incomplete.

No central adapter, attestation, preflight, Join, package, asset, localisation, workbook, or super-event wiring was changed by this patch.
