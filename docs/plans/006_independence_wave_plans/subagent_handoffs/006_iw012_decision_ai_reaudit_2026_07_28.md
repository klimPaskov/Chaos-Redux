# IW-012 post-commit decision AI re-audit — 2026-07-28

## Scope and result

Read-only audit after commits `3570ed8ff` and `72d8549e3`.

No actionable source issue was found in the requested IW-012 decision surfaces.

No gameplay, localisation, focus, GUI, or documentation source was changed by this audit.

## Six project AI blocks

| Project ID | State-aware weighting verified |
| --- | --- |
| `independence_wave_ice_reconcile_shipping_registers` | Doubles below the shipping-security and port-authority gates, then halves during war. |
| `independence_wave_ice_charter_municipal_council` | Doubles below the civic-cohesion route gate and during severe instability, then halves during war. |
| `independence_wave_ice_expand_coastwatch` | Uses major host-threat and doubled war priorities. |
| `independence_wave_ice_negotiate_north_atlantic_compact` | Uses `has_independence_wave_ice_compact_ai_posture` plus League membership. |
| `independence_wave_ice_settle_former_host_charter` | Uses `has_independence_wave_ice_former_host_charter_pressure`, favors a non-severe threat context, and halves during war. |
| `independence_wave_ice_declare_armed_neutrality` | Starts very low, rises under severe host threat or war, and is explicitly blocked in peacetime without severe threat. |

The two new nested package triggers resolve exactly once each and are consumed by their intended decision AI blocks in [common\\scripted_triggers\\006_independence_wave_ice_package_triggers.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_ice_package_triggers.txt:57).

Their shared dependencies are valid: former-host existence and non-war scope, `independence_wave_host_outcome`, reconquest fear, network standing, formable registration, severe-host-threat, and severe-instability triggers all already exist and use the appropriate country scope.

## Armed Neutrality route safety

`independence_wave_ice_declare_armed_neutrality.remove_effect` no longer sets `independence_wave_government_route_input` or calls `independence_wave_select_government_route` in [common\\decisions\\006_independence_wave_ice_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_ice_decisions.txt:265).

It retains its existing route-lock availability and cancel guard, one-time flag, security cost, ledger updates, idea grant, and security-progress effect.

The remaining package-local route-selection calls belong to the four explicit focus-route effects in [common\\scripted_effects\\006_independence_wave_ice_package_effects.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_effects\006_independence_wave_ice_package_effects.txt:206), not to the decision.

## Costs and durations

The gameplay commit changes only `ai_will_do` blocks, the two AI helper triggers, and the Armed Neutrality route side effect.

All six cost contracts, availability gates, cancellation guards, payment effects, civilian-factory burdens, and duration references are unchanged.

The unchanged serialized durations are shipping 120, municipal council 180, coastwatch 180, compact 300, former-host charter 270, and Armed Neutrality 180 days in [common\\script_constants\\006_independence_wave_ice_constants.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\006_independence_wave_ice_constants.txt:39).

The 1,440-day harbour crisis remains unchanged.

## Lifecycle, localisation, cleanup, and exploit notes

The six projects remain serialized by `has_independence_wave_ice_active_package_project`, with the harbour mission correctly excluded from that project-only lock.

All project AI blocks retain package and availability gating before the AI weights are evaluated.

No localisation or tooltip key changed, so no new player-facing text gap was introduced.

No cleanup, cooldown, free-unit, equipment, core, war-goal, or route-overwrite exploit was introduced by these commits.

No decision-owned GUI change was in scope, so no GUI inspection was required.

## Evidence and validation

Compared both commits against their parents and inspected the current decision, package-trigger, constants, shared-threat, and route-effect sources.

The relevant diff contains no change to `custom_cost_trigger`, `custom_cost_text`, `complete_effect` payment calls, `days_remove`, mission timeout, decision availability, or cancellation conditions.

`72d8549e3` changes only an implementation handoff document and does not alter gameplay source.

Live game validation was not run because this was a read-only source audit and live validation belongs to the user.

## Remaining issues

None within the requested post-commit AI, route-write, cost, duration, and nested-trigger scope.
