# Event 012 compact-host promotion writer gap

Date: 2026-08-02.

Status: Implemented as an explicit paid congress evidence docket; live campaign acceptance remains open.

## Scope

The host playbook matrix permits a compact signature to become a full dossier after at least two of six documented campaign criteria are true.

The runtime gate is `africa_reconcile_compact_host_promotion_criteria` followed by `africa_compact_host_can_be_promoted` and `africa_promote_compact_host_package` in `common/scripted_effects/012_africa_effects.txt`.

## Evidence

The six criterion flags are `africa_compact_long_campaign_survived`, `africa_compact_leads_regional_council_or_rival`, `africa_compact_route_contradiction_proven`, `africa_compact_post_unification_legacy`, `africa_compact_opening_depth_failure_proven`, and `africa_compact_tier_a_identity_received`.

`africa_record_compact_promotion_proof` now writes `africa_compact_long_campaign_survived` and `africa_compact_route_contradiction_proven` only when the compact host has published its mapped weakness, completed or recovered the first proof, fulfilled the public obligation, seated the provisional congress, completed both compact signature focuses, retained its capital, reached the regional phase, and stayed above the stability and war-support floors. `africa_promote_compact_host` is the paid caller for `africa_promote_compact_host_package` after the shared two-criterion reconciliation and all existing overlap, access, refusal, and control gates.

The two existing compact signature focus rewards still write only the four base viability flags. The evidence decision deliberately writes the two campaign criteria only after the focus, proof-mission, obligation, congress, control, and resilience evidence is present, so opinion alone cannot qualify a host.

## Disposition

The fail-closed gate remains in force until the evidence decision's conditions are met. Promotion changes only the host-depth variable and promotion flag, preserves the original country, clears stale refusal/access failure flags on successful promotion, and leaves evidence flags as lifetime campaign receipts. A refused docket remains blocked by the existing refusal flag; no opinion-only or automatic promotion path exists.

Action 102 remains the separate priority-member package gate and is not treated as compact-host promotion.

No new country tag, fallback route, broad world scan, or opinion-only promotion was introduced.
