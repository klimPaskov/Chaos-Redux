# Fallout Harbor Without a City Chain Proof

## Scope

This proof records the static implementation of The Harbor Without a City. The chain is survivor-country content that becomes eligible only through the Fallout-owned candidate registry and scheduler. It is not Fallout itself. It does not create a normal Fallout Event Log entry, evolution, ordinary super-event, country tag, state transfer, or automatic scheduler activation.

## Identity ledger

| Surface | Value |
| --- | --- |
| Namespace | `chaosx.fallout` |
| Human opening | `chaosx.fallout.782` |
| Hidden AI opening | `chaosx.fallout.783` |
| Human delayed result | `chaosx.fallout.784` |
| Hidden AI delayed result | `chaosx.fallout.785` |
| Human callback | `chaosx.fallout.786` |
| Hidden AI callback | `chaosx.fallout.787` |
| Cleanup | `chaosx.fallout.788` |
| Candidate | `782` |
| Transaction | `710083` |
| Scheduler route | `7198` |
| Route upper bound | `7199` |
| Event Log history | `9189` |
| Country memory | `fallout_country_memory.west_african_port_confederacies` `74` |
| Government archetype | `fallout_government_archetype.maritime_remnant` `10` |
| Required prior memory | `fallout_event_775_memory_closed` |

The global id and candidate tables are extended in `common/script_constants/fallout_world_end_event_constants.txt`. Event-local branches, timing, costs, thresholds, modifier values, and Event Log payloads are in `common/script_constants/fallout_world_end_harbor_without_city_constants.txt`.

## Candidate and admission evidence

`common/scripted_effects/fallout_world_end_event_candidate_effects.txt` clears the `fallout_event_782_candidate_state_id` scratch value during registry rebuild. The producer gates on the exact West African Port Confederacies memory and maritime-remnant archetype, initializes the dedicated harbor ledgers before state inspection, and chooses the lowest owned state id that passes `fallout_event_pilot_harbor_without_city_state_is_current`. The state trigger requires current identity and survival rows, durable resources, current Supply Access, surviving population, Shelter, Adaptation, Exposure, Disease, a valid Air Winter phase, the closed Ghost Convoy state memory, a coastal state or surviving naval base, and a foreign neighboring state.

The producer calls the existing candidate-row initializer and appender. The row carries candidate `782`, transaction `710083`, crisis-incident class, diplomacy-trade-war-settlement family, diplomacy cooldown, human and hidden-AI event tokens, rival-orders preferred phase, open-continuation secondary phase, Fuel resource requirement, state target type, target state id, route `7198`, and one required maritime archetype and Air Winter match. It never sets a scheduler activation flag and never fires an event directly.

`fallout_event_782_country_is_current` authenticates the current registry country row, durable resource row, ordinary-event receipt, maritime-remnant archetype, country memory `74`, campaign window, candidate state id, harbor authority, inland grievance, Medicine, Cohesion, Recognition, branch affordability, and no pending or committed chain. Its final owned-state loop revalidates the selected state through the state trigger.

## Human and AI chain

`common/scripted_triggers/fallout_world_end_harbor_without_city_event_triggers.txt` provides generation-bound opening, delayed result, callback, cleanup, state, target, registry, and affordability triggers. Human and hidden-AI lanes use separate event tokens and dispatch modes. Hidden AI evaluates four authored priorities and can only select a branch that remains affordable.

`events/fallout_world_end_events.txt` contains the seven dedicated blocks. The human opening has four options. The delayed result has twelve branch and outcome descriptions. The callback has success, partial, and failure descriptions. The cleanup is hidden and triggered only by the authenticated delayed-cleanup receipt. All three visible blocks use `GFX_report_event_fallout_harbor_without_city`.

## Ledger, grading, and delayed receipts

`fallout_event_782_initialize_ledgers` is idempotent. It initializes and clamps harbor authority, inland grievance, garrison trust, claim pressure, evacuee capacity, port food reserve, and Cause Memory. The registry snapshot freezes owner, controller, generation, harbor ledgers, and one lowest foreign neighbor with its owner and controller.

The result is scheduled forty-five days after the opening transaction. Grading combines frozen state values, Medicine, Recognition, harbor authority, inland grievance relief, garrison trust, evacuee capacity relief, and the maritime-remnant government bonus. Each branch has distinct success, partial, and failure thresholds. Result effects update Air Winter, Supply Access, Shelter, Exposure, Adaptation, Reclamation, Disease, Medicine, Cohesion, Recognition, Stability, War Support, the harbor ledgers, a branch memory, a state outcome flag, and one dedicated neighbor opinion modifier. Failure routes a bounded request through `apply_exact_state_civilian_population_loss` with the Fallout aftermath Deaths reason and a building-damage value.

The callback is scheduled three hundred thirty days after the result. It grades current harbor authority, Cohesion, Recognition, garrison trust, claim pressure, Cause Memory, target-state Supply Access, Reclamation, Disease, inland grievance, evacuee capacity, and port food reserve. Its success, partial, and failure effects update the same ledger family and add a callback memory. Callback failure uses the bounded Deaths contract. Each delayed lane records a survivor-country history payload and authenticates transition generation, owner, controller, target state, foreign neighbor, candidate id, and committed reservation before writing.

## Event Log and localisation

`common/scripted_localisation/fallout_world_end_harbor_without_city_event_log_scripted_localisation.txt` defines `GetFalloutEvent782EventLogDetail` for the four choices, twelve branch outcomes, three callback outcomes, and cancellation. Shared routing in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` maps history `9189` to the detail and name surfaces. The UTF-8 BOM localisation file is `localisation/english/fallout_world_end_harbor_without_city_l_english.yml`. It contains concrete dock council, inland road seal, garrison gate, lighthouse lens, clinic ledger, and convoy evacuation wording.

## Assets

The generated fictional report image is retained at `docs/assets/782_harbor_without_city/`. The source, processed preview, runtime DDS, hashes, dimensions, and source-mode disclaimer are in `manifest.md`. The runtime file is `gfx/event_pictures/harbor_without_city/report_event_fallout_harbor_without_city.dds`. The sprite is registered in `interface/fallout_world_end.gfx`. No zombie asset, audio, sprite, or path is referenced.

## Static review boundary

Static review confirms the seven event ids, candidate row, global constants, event-local constants, scripted effects, scripted triggers, dynamic modifiers, opinion modifiers, scripted localisation, shared Event Log routing, player localisation, sprite registration, runtime DDS, manifest hashes, and cleanup references are present in the source tree. The chain remains dormant because scheduler activation is intentionally unset. This proof does not claim live event delivery, save recovery, multiplayer ownership, runtime Event Log rendering, or Hearts of Iron IV execution.

The read-only Event Inspector lint query for `chaosx.fallout.782` returned `EVENT_INSPECTED_PARTIAL` with `blockingDiagnostics = 0` and a focused-analysis deferral notice. The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/025339838178da0e75200aa0b78c868057b49d035cc42b459396743a270ad480/2775d99cdb6845f32ec0c28976c3212425d327f59c39489a55db69d9cf213429/event-lint-865a19479acc.json`. This is supplemental static evidence, not runtime acceptance.
