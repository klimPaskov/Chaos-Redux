# Event 012 Africa route-AI pressure handoff — 2026-08-01

## Scope

This tranche removes the audited flat route-body focus AI surface without changing focus ownership, layout, route availability, tags, portraits, models, or member-package selection.

The seven constitutional routes now share one live-state trigger that branches on the committed constitution and raises the weight of the next route focus when that route has a low payoff axis, an unresolved route action, a documented constitutional crisis, or a pending postwar review.

## Changed files

- `common/script_constants/012_africa_focus_route_constants.txt` adds `africa_focus_ai_route.pressure_multiplier = 2` as the single tuning value.
- `common/scripted_triggers/012_africa_focus_route_triggers.txt` adds `africa_focus_ai_route_pressure` with route-specific axis pressure for Federal Union, Continental Republic, Council of Crowns, Peoples Union, Military Continentalism, Continental Confederation, and Ancestral Covenant.
- `common/national_focus/012_africa_continental_focus_tree.txt` adds the pressure modifier to all 107 route-body `ai_will_do` blocks that previously used only `@africa_ai_normal`.

## Route pressure map

- Federal Union prioritises representation, resources, command, withdrawal protection, and crisis resilience.
- Continental Republic prioritises representation, executive power, resources, crisis resilience, and post-unification rule.
- Council of Crowns prioritises representation, executive power, withdrawal protection, crisis resilience, and post-unification rule.
- Peoples Union prioritises representation, executive power, resources, command, and crisis resilience.
- Military Continentalism prioritises command, executive power, representation, crisis resilience, high emergency-rule debt, and low war readiness.
- Continental Confederation prioritises representation, withdrawal protection, crisis resilience, and resource governance.
- Ancestral Covenant prioritises ecological pressure, command, resources, and crisis resilience.

All routes additionally respond to `africa_focus_route_action_ai_contract_pending`, `africa_route_viability_under_review`, `africa_constitutional_crisis_escalated`, `africa_postwar_constitutional_review_pending`, and the unresolved mapped route-action trigger.

## Evidence

- A bounded source scan found 107 route-body `ai_will_do` blocks and zero remaining flat `factor = @africa_ai_normal` blocks in the route families.
- `hoi4_focus_inspect` returned `FOCUS_INSPECTED` with no new parser blocker; its 570 layout diagnostics and 1,028 node intersections are the previously documented branch-unaware layout findings.
- `hoi4_event_inspect` for namespace `chaosx.nr12` returned `EVENT_INSPECTED_PARTIAL` with no new Event 012 blocker; the result remains workspace-bounded and defers large helper projections.

## Deliberate boundaries

This tranche does not add country tags, new portraits, models, unit entities, audio, W5 receipts, dormant priority tags, or terminal World identity readiness.

The existing completion audit remains authoritative for the unresolved W5 atomic certification, terminal/super-event/achievement gate, audio rights and masters, model-gated action rows, dormant niche-tag bindings, controlled-pool provenance, native-language review, and branch-aware focus layout review.
