# Event 006 League transition callers — 2026-09-13

Disposition: implemented for the accepted League state-machine caller gap; whole Event 006 remains HOLD/PARTIAL because unrelated asset, provenance, package-admission, route-cost, GUI, and probability gates remain unresolved.

## Scope

The accepted League state machine already contained effects for consultative formation, formalization, durability, reform, normalization, rival-bloc reunification, dissolution, and network restart, but source review found no normal-play decision caller for those transitions and no writer for `independence_wave_league_durability_mission_complete`.

## Changed source

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
  - Added the shared `has_independence_wave_league_route_proposal` predicate.
  - Added phase-safe caller predicates for all eight lifecycle transitions.
  - Every predicate requires a live Event 006 origin through `is_independence_wave_active_country`, except that the restart predicate intentionally permits a network member after dissolution because dissolution clears League membership.
- `common/scripted_effects/006_independence_wave_effects.txt`
  - Added `independence_wave_capture_league_route_proposal`, storing the selected focus-tree proposal in a country-scoped value while the upgrade timer runs.
  - Cleared durability watch/completion receipts whenever the shared League phase flags are reset.
- `common/decisions/006_independence_wave_decisions.txt`
  - Added post-recognition League callers for consultative formation, consultative upgrade, durability proof, reform, reformed normalization, rival reunification, dissolution, and informal-network restart.
  - All callers remain in `independence_wave_league_category`, whose existing visibility gate requires active Event 006 content, recognition, and the League Congress unlock.
  - The durability action uses the accepted `constant:independence_wave_league.durable_days` timer. Its expiry writes `independence_wave_league_durability_mission_complete` only while the League is still formal with the required member count and cohesion, then invokes the existing guarded durability effect.
- `localisation/english/006_independence_wave_decisions_l_english.yml`
  - Added player-facing names and descriptions for the eight new actions.

## Validation evidence

- `python .tools/audit_event6_allocator.py --strict` passed.
- `python .tools/audit_event6_country_api.py` passed.
- `python .tools/audit_event6_scenario_matrix.py` passed.
- `python .tools/audit_event6_form16.py` passed.
- Fresh read-only `hoi4.event_inspect` namespace lint returned `EVENT_INSPECTED_PARTIAL`, revision `3ac0bcfca142cdb797cca8faf293cfa1085b9019421045d9f385374ad094fc2a`, graph hash `18501dff365ddaeb371f8e07696cd36dafd3f74a24012df8ba7714f6df9da62f`, and zero blocking diagnostics. Large-workspace helper/lifecycle validation was deferred by the service.
- Fresh read-only `hoi4.event_render` state render returned `EVENT_RENDERED_PARTIAL` at the same revision with zero blocking diagnostics. It is source-linked structural evidence only; it does not replace live gameplay validation.

## Remaining limits

- No live game, save/load, or in-game decision visibility claim is made; the user performs that validation.
- The accepted Event 006 completion boundary remains HOLD/PARTIAL for the unrelated asset rights/provenance, package/formable admission, six IW-093/IW-098 cost contracts, slot-23 audio selection/rights, GUI dynamic-state evidence, and incomplete probability comparison fixtures recorded by the current audit handoffs.
- The existing League helpers and the new callers still rely on the project's current member/founder ledgers and rival-bloc contract. No fallback roster, pre-event category, pressure surface, periodic world iteration, or new country package was introduced.
