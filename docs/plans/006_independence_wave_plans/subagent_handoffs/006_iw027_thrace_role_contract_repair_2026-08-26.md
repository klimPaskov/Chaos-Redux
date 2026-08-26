# IW-027 Thrace leader-role contract repair

Date: 2026-08-26

## Finding

The admitted BAX Thrace package promotes `BAX_independence_wave_thrace_council` through conservatism, marxism, centrism, despotism, and liberalism in its five government-route effects. The character definition supplied only conservatism, marxism, and centrism country-leader roles, leaving the emergency and patron routes without applicable promotion roles.

## Patch

`common/characters/006_independence_wave_characters_registry.txt` now adds empty `despotism` and `liberalism` country-leader roles to `BAX_independence_wave_thrace_council`, matching the existing route promotion calls without changing portraits, traits, balance, identity, or admission.

## Boundary

This is a narrow character-role runtime repair. No BAX state-184/GRE reservation gate, force mapping, decision, focus, AI, asset, Join, SCN-008, or 32/161 admission boundary was changed. No live game or save/load receipt is claimed.

## Validation

The source crosswalk confirms all five `independence_wave_install_bax_*_government` promotion ideologies now have matching country-leader blocks. The scoped Event 006 allocator, country API, strict flag-family, FORM-16, GUI semantic, and SCN-008 matrix checks passed. A bounded `hoi4.event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d18fed93442496541610637a339e2c49e6355784fe517a030766beac3eee3bc/90084e74eb3e9f372d7b20f73a7d5e6132fdddf641d61211227dd28ed150e513/event-lint-43388d6b2737.json`. The matching overview render returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1b4646e1599856b8be190e487c9423099b9283951d5f0d45bf2135c1a11de8d/3594f3fd3327208521ca75f603aa73aa53406ff5460861953a55402c846f3093/event-overview-43388d6b2737-manifest.json`. The large workspace projections remain partial and do not substitute for live runtime evidence.
