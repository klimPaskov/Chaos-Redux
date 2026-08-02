# Event 012 common-reserve deployment generation gate

## Scope

This handoff closes the stale-callback defect in the bounded common-reserve deployment kernel without adding tags, models, stores, or recurring world iteration.

## Changed files

- `common/scripted_effects/012_africa_common_reserve_effects.txt`
- `common/on_actions/012_africa_world_order_on_actions.txt`
- `docs/events/012_africa/common_reserve_deployment.md`

## Runtime contract

`africa_common_reserve_deploy_on_defensive_war` already snapshots `africa_host.africa_host_generation` into `africa_common_reserve_deployment_host_generation`. `africa_common_reserve_resolve_deployment` now proves that the snapshot matches a live, committed `event_target:africa_host` before it can write reserve achievement outcomes or clear the host's active reserve posture.

The annex callback delegates capital-loss accounting to the resolver instead of writing a receipt before the generation gate. Peace, capitulation, and annex callbacks therefore share one lifecycle rule.

Stale, missing-host, missing-generation, or uncommitted-host callbacks still clear the deployed partner's flag and transient variables, but they cannot award `africa_achievement_record_reserve_war_answered`, write deadline or capital-loss receipts, or mutate a successor host's reserve flag.

## Validation

The focused read-only Event Chain Viewer lint for `chaosx.nr12.1` returned `status=ok`, `code=EVENT_INSPECTED_PARTIAL`, `blockers=[]`, and `blockingDiagnostics=0` after the patch. The adapter deferred workspace-wide helper and lifecycle projections, so this is structural source evidence rather than live campaign acceptance.

The targeted source review confirms that the deployment generation snapshot is now consumed before accounting, local cleanup remains unconditional, and the separate annex-side capital-loss writer is removed. The common-reserve achievement row remains blocked until the six-war live scenario matrix and all failure paths are accepted.

## Scenario receipts still required

- Current generation with on-time peace and capital held: positive war-answer receipt and host posture cleanup.
- Current generation with capitulation, capital loss, deadline expiry, or annexation: exact sticky failure receipt and local cleanup.
- Stale generation after host transfer: no achievement or successor-host mutation, with local cleanup.
- Missing host, missing generation, or missing commit proof: fail closed with local cleanup.
