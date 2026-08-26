# IW-040 Kuban conservatism-role receipt repair

Date: 2026-08-25

## Finding

`independence_wave_initialize_kub_politics` records `independence_wave_kub_conservatism_role_added` only when the current setup generation adds Ivanis Vasily Nikolaevich's conservatism role. The setup entry effect cleared other generation receipts but did not clear this one. A retried generation could therefore inherit a stale receipt, and cleanup could remove a conservatism role that the current generation did not add.

## Patch

`common/scripted_effects/006_independence_wave_kuban_package_effects.txt`

`independence_wave_setup_iw_040_kuban` now clears `independence_wave_kub_conservatism_role_added` beside the other setup-entry receipts before package initialization. Cleanup remains unchanged: it still removes the role only when the receipt is set by the active generation, then clears the receipt at teardown.

## Boundary

This is a one-line lifecycle hardening patch. It does not alter the IW-040 admission gate, package identity, state 234 anchor, decisions, localisation, focus graph, AI weights, assets, rights, or the 32/161 whole-event boundary.

## Validation

The source crosswalk confirms the setup clear at `independence_wave_setup_iw_040_kuban`, the writer in `independence_wave_initialize_kub_politics`, and the guarded cleanup at `independence_wave_cleanup_iw_040_kuban`. Run:

```text
python -B .tools/audit_event6_allocator.py
```

The bounded `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97`, with zero selected blocking diagnostics; its workspace-wide helper/lifecycle projection remains deferred. A matching bounded `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` at the same revision with zero selected blocking diagnostics. The render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e6a0fc7ab8d56690f3cb8c58a4845e571f658fe4c7d986b7ded02f948d59e27/99be07e42c1ff4185d9ae11940dbac110ab934cabfdcd9937aff58146676b954/event-overview-43388d6b2737-manifest.json`. No live game execution or runtime receipt is claimed.
