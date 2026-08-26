# IW-024 Banat leader-role and force-contract repair

Date: 2026-08-26

## Findings

The admitted AXX Banat package promoted `AXX_independence_wave_banat_presidium` through five route ideologies. Its character definition supplied country-leader roles for conservatism, marxism, and centrism, but not despotism or liberalism. The emergency and patron route effects therefore targeted missing ideology roles.

The durable Banat package note and the Banat AI strategy comment also retained the superseded `mountain_frontier` / terrain-and-professional-officer description. Current setup and readiness source use the accepted p24 `industrial_security` profile with militias, regional guards, depots, factory/rail guards, and capital-border defence.

## Patch

- `common/characters/006_independence_wave_characters_registry.txt` now adds empty `despotism` and `liberalism` country-leader roles to the existing AXX character, matching the route promotion calls without changing traits or balance.
- `docs/events/006_independence_wave/banat_package.md` now describes the installed p24 `industrial_security` force contract and its five active reinforcement pathways.
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` now uses the current industrial-security profile in its source comment.

## Boundary

This is a narrow leader-role runtime repair plus documentation alignment. It does not change AXX identity, state 82/ROM reservation gates, admission, Join order, costs, AI weights, focus assignment, assets, or the 32/161 whole-event boundary.

## Evidence and validation

The source audit confirmed AXX/state 82/ROM remnant and capital gates, dormant laws, reservation and optional state 764 handling, roster/portrait/flag consumers, force application, setup/final/cleanup dispatch, ideas, decisions, focus hooks, league/formable registration, central attestation, Join/capacity, and SCN-008 preflight. The character role set now contains all five promotion ideologies used by `independence_wave_install_axx_*_government`.

The scoped Event 006 allocator, country API, strict flag-family, FORM-16, GUI semantic, and SCN-008 matrix checks passed. A bounded `hoi4.event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d18fed93442496541610637a339e2c49e6355784fe517a030766beac3eee3bc/90084e74eb3e9f372d7b20f73a7d5e6132fdddf641d61211227dd28ed150e513/event-lint-43388d6b2737.json`. The matching overview render returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1b4646e1599856b8be190e487c9423099b9283951d5f0d45bf2135c1a11de8d/3594f3fd3327208521ca75f603aa73aa53406ff5460861953a55402c846f3093/event-overview-43388d6b2737-manifest.json`. The workspace deferred large helper/lifecycle projections. No quantitative AXX AI claim or live game/runtime receipt is made.
