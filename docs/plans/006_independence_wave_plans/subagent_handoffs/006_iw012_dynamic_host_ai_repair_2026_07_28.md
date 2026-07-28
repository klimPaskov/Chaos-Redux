# IW-012 dynamic former-host AI repair

Date: 2026-07-28.

## Scope and disposition

This bounded repair closes the static-DEN target identified by the IW-012 focus and country re-audits. The Event 006 ICE carrier stores its former host in the synchronized `independence_wave_setup_former_host` event target, so a literal `DEN` strategy was unsafe for later releases or alternate host ownership.

The static AI plan in `common/ai_strategy/006_independence_wave_ice.txt` now retains only untargeted production/build priorities. Targeted host diplomacy is applied once by `independence_wave_ice_apply_host_ai` in `common/scripted_effects/006_independence_wave_ice_package_effects.txt`, using `event_target:independence_wave_setup_former_host` for trade, host charter, preparation, and compact relations. Per-channel flags record exactly which dynamic weights were added. Cleanup reverses those same weights before the regular Event 006 target is discarded, then clears the receipt flags.

## Validation evidence

- `rg -n "id = DEN|event_target:independence_wave_setup_former_host" common/ai_strategy/006_independence_wave_ice.txt common/scripted_effects/006_independence_wave_ice_package_effects.txt` shows no remaining targeted `DEN` entry in the ICE AI plans and dynamic target use in the setup/cleanup helpers.
- The helper is called after the ICE setup publishes the AI profile and formable-family flags, and cleanup runs before generation-local Event 006 state is removed.
- Static target-specific AI syntax follows the installed vanilla `add_ai_strategy` precedent using `event_target:` IDs. Integer weights remain centralized in `independence_wave_ice_ai` constants, including negative cleanup values.
- No new tag, history, portrait, flag, advisor icon, or vanilla tree replacement was introduced.

## Remaining boundaries

Live AI activation, route choice, former-host transition, save/load, and synchronized release evidence remain parent-owned runtime checks. This source repair does not promote the package beyond the static IW-012 admission and does not change the whole-event `HOLD / PARTIAL` status.
