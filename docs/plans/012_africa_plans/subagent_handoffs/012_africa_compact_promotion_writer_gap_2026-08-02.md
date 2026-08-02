# Event 012 compact-host promotion writer gap

Date: 2026-08-02.

Status: Documented blocker; no gameplay fallback or speculative writer was added.

## Scope

The host playbook matrix permits a compact signature to become a full dossier after at least two of six documented campaign criteria are true.

The runtime gate is `africa_reconcile_compact_host_promotion_criteria` followed by `africa_compact_host_can_be_promoted` and `africa_promote_compact_host_package` in `common/scripted_effects/012_africa_effects.txt`.

## Evidence

The six criterion flags are `africa_compact_long_campaign_survived`, `africa_compact_leads_regional_council_or_rival`, `africa_compact_route_contradiction_proven`, `africa_compact_post_unification_legacy`, `africa_compact_opening_depth_failure_proven`, and `africa_compact_tier_a_identity_received`.

The current gameplay source has no accepted writer for any of those six flags, and the promotion helper has no caller.

The two existing compact signature focus rewards write only the four base viability flags, so adding a caller alone would leave promotion permanently fail-closed.

## Disposition

The fail-closed gate is retained until an approved focus, action, event, or congress owner writes at least two criteria with documented refusal and cleanup semantics.

Action 102 remains the separate priority-member package gate and is not treated as compact-host promotion.

No new country tag, fallback route, broad world scan, or opinion-only promotion was introduced.
