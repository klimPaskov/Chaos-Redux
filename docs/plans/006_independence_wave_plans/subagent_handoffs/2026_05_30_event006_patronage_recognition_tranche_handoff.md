# Event 006 Patronage and Recognition Tranche Handoff

## Scope

Implemented the first major/regional-power decision family for Event 006. This tranche does not touch flag assets, country definitions, history files, or Event 005 Soviet Collapse systems.

## Files Changed

- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Identifiers

- Category: `independence_wave_patronage_recognition_category`
- Category gate: `can_independence_wave_open_patronage_recognition`
- Shared target gate: `can_independence_wave_major_target_release`
- Decisions:
  - `independence_wave_major_recognize_committee`
  - `independence_wave_major_supply_rifles`
  - `independence_wave_major_offer_military_mission`
  - `independence_wave_major_demand_cabinet_seats`
  - `independence_wave_major_sabotage_rival_patron`
- Effects:
  - `independence_wave_major_recognize_committee_effect`
  - `independence_wave_major_supply_rifles_effect`
  - `independence_wave_major_offer_military_mission_effect`
  - `independence_wave_major_demand_cabinet_seats_effect`
  - `independence_wave_major_sabotage_rival_patron_effect`

## Behavior

- Eligible actors are non-subject, non-Event-006 countries that are majors or regional powers by factory count after an Event 006 wave has released countries.
- Targets come from `global.independence_wave_released_countries` and must be living, independent Event 006 releases, not self-targets, and not at war with the actor.
- Recognition raises target legitimacy and foreign attention, then marks recognition secured for existing achievement tracking.
- Rifle supply and military missions spend real actor equipment or command resources, strengthen the target, and mark patron acceptance.
- Cabinet-seat demands require existing target patron leverage and deepen dependency without creating a puppet.
- Rival-patron sabotage spends command power, lowers target patron leverage, and raises foreign attention.

## Validation Notes

- Decision audit completed in `2026_05_30_event006_patronage_recognition_audit_handoff.md`.
- Audit patched `can_independence_wave_open_patronage_recognition` to use the persistent `global.independence_wave_released_countries` ledger and require at least one living independent Event 006 release, instead of relying on the current-wave release counter.
- Static validation completed after the audit patch: brace balance passed for the Event 006 decision, decision-category, constants, trigger, effect, event, achievement, and achievement-interface files; bounded Clausewitz scan found no unsupported `<=` or `>=`; Event 006 and achievement localisation files are UTF-8 with BOM and have no `:0` keys.
- No flag asset, country-definition, history, or Event 005 paths are part of this change.

## Remaining Risks

- This is a bounded first-pass major-power loop. It does not implement direct host-border guarantees, autonomy brokering, or full patron-vs-patron intelligence chains.
- Runtime UI validation has not been performed.
