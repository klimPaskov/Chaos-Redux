# Event 020 Shared Disease Response

Event 020 uses the existing `chaosx_disease_containment_category` and the existing disease board. It does not register a second Black Plague decision category. State actions are selected from the board, check the selected state's phase and control, and resolve through a bounded project that pays equipment, fuel, civilian production, command power, or stability as appropriate.

## State actions

`common/decisions/020_black_plague_shared_response_decisions.txt` registers prevention, transport, military-route, hospital, travel, relief, burial, evacuation, containment, recovery, cured-state, and anti-rat actions. `common/scripted_triggers/020_black_plague_shared_response_triggers.txt` owns the phase and state gates. `common/scripted_effects/020_black_plague_shared_response_effects.txt` owns population-band scaling, payment, action ownership, outcomes, cooldowns, weekly pulses, cancellation, and terminal cleanup.

The action ids are centralized in `black_plague_shared_action` in `common/script_constants/020_black_plague_shared_response_constants.txt`. Durations, costs, burden, pulse reductions, recovery gains, and anti-rat results are kept in the same constants file. A state action uses the selected state's population bands (`minimum`, `standard`, `large`, and `metropolitan`) to scale support equipment, motorized equipment, and fuel. The country-level knowledge programmes use the country cost band and commit `country_program` response burden while active.

State pulse flags are cleared when the state becomes Cured or when the disease episode's terminal cleanup runs. A cancelled action pays no second outcome and releases the action burden. The terminal cleanup also clears the shared country flags and re-evaluates the shared crisis board.

## Country knowledge actions

The shared category includes Publish Findings, Restricted Alliance Exchange, Hoard Protocol, Steal Foreign Progress, International Medical Mission, Emergency Countermeasure Drive, route-crisis responses, Royal Node strikes, Crown Strike, and post-defeat Seal Royal Burrows. They require the countermeasure programme or recorded findings, use equipment and fuel rather than political power, and feed the existing 0–100 countermeasure progress producer. Intelligence theft requires a real intelligence agency and operative; it does not use a synthetic `operative_recruited` flag.

After Evolution V opens its earned route, a human country that still holds established Black Plague ground can start one of two native missions in the same category. Hold the Line pays support, motorized, infantry, train, fuel, manpower, command-power, factory, stability, and war-support costs and gains weekly progress from war, countermeasure readiness, and held states. Secure the Refuge uses the same payment surface at a higher cost, requires a held terminal capital, refuge node, or city, and gains an additional node bonus. Success lowers global Rat King terminal preparation, raises countermeasure progress, and improves containment without curing a state. Timeout raises terminal preparation and Rat King hunger and adds incoming exposure to the remaining human-established states. Both missions are removed by the event-owned runtime when the last eligible ground is lost or when the terminal takeover begins.

## Integration points

`black_plague_process_current_state_persistent_response` calls `black_plague_apply_shared_action_pulse` after Black Plague-specific response deltas and before the final state delta application. National capacity recomputation counts an active shared state action and an active country programme. The response registry retains shared-action states and owners so a live project cannot disappear from burden accounting.

## Icons and UI wiring

The decisions use existing vanilla decision sprites for generic research, civil support, intelligence operation, quarantine, faction integration, and medical missions. Event-020-specific decision art is defined in `interface/020_black_plague_response.gfx` and stored under `gfx/interface/decisions/020_black_plague/`. Crown Strike uses `GFX_decision_black_plague_strike_the_crown`, and post-defeat sealing uses `GFX_decision_black_plague_seal_royal_burrows`. The final icon package, source frames, DDS files, contact sheet, and crosswalk are documented in `docs/plans/020_black_plague_plans/subagent_handoffs/2026-07-24_black_plague_response_decision_icons_handoff.md`.

## Future depth

Future response work can add state-specific scripted tooltips for each population band and faction-level findings diplomacy without changing the shared category or action API. Crown Strike and Seal Royal Burrows currently use the shared timed state-action API; the parent must decide before converting them to native mission fields. Any new action must reserve a new constant id, add a phase-gated trigger, define a real cost and duration, add a player-facing name/description/cost tooltip, and extend terminal cleanup.
