# Fallout Captain's Articles Chain Proof

## Scope

This proof records the static implementation of The Captain's Articles. The chain is survivor-country content that becomes eligible only through the Fallout-owned candidate registry and scheduler. It is not Fallout itself. It does not create a normal Fallout Event Log entry, evolution, ordinary super-event, country tag, state transfer, or automatic scheduler activation.

## Identity ledger

| Surface | Value |
| --- | --- |
| Namespace | `chaosx.fallout` |
| Human opening | `chaosx.fallout.768` |
| Hidden AI opening | `chaosx.fallout.769` |
| Human delayed result | `chaosx.fallout.770` |
| Hidden AI delayed result | `chaosx.fallout.771` |
| Human callback | `chaosx.fallout.772` |
| Hidden AI callback | `chaosx.fallout.773` |
| Cleanup | `chaosx.fallout.774` |
| Candidate | `768` |
| Transaction | `710081` |
| Scheduler route | `7194` |
| Route upper bound | `7195` |
| Event Log history | `9187` |
| Country memory | `fallout_country_memory.west_african_port_confederacies` `74` |
| Government archetype | `fallout_government_archetype.maritime_remnant` `10` |

The global id and candidate tables are extended in `common/script_constants/fallout_world_end_event_constants.txt`. Event-local branches, timing, costs, thresholds, modifier values, and Event Log payloads are in `common/script_constants/fallout_world_end_captains_articles_constants.txt`.

## Candidate and admission evidence

`common/scripted_effects/fallout_world_end_event_candidate_effects.txt` clears the `fallout_event_768_candidate_state_id` scratch value during registry rebuild. The producer gates on the exact West African Port Confederacies memory and maritime-remnant archetype, initializes the dedicated port ledgers before state inspection, and chooses the lowest owned state id that passes `fallout_event_pilot_captains_articles_state_is_current`. The state trigger requires current identity, durable survival resources, current Supply Access, surviving population, Shelter, Adaptation, Exposure, Disease, a valid Air Winter phase, a coastal state or surviving naval base, and a foreign neighboring state.

The producer calls the existing candidate-row initializer and appender. The row carries candidate `768`, transaction `710081`, routine-incident class, regional-and-biome family, recovery cooldown, human and hidden-AI event tokens, rival-orders preferred phase, open-continuation secondary phase, Fuel resource requirement, state target type, target state id, route `7194`, and one required maritime archetype and Air Winter match. It never sets a scheduler activation flag and never fires an event directly.

`fallout_event_768_country_is_current` authenticates the current registry country row, durable resource row, ordinary-event receipt, maritime-remnant archetype, country memory `74`, campaign window, candidate state id, port legitimacy, piracy pressure, Medicine, Cohesion, Recognition, branch affordability, and no pending or committed chain. Its final owned-state loop revalidates the selected state through the state trigger.

## Human and AI chain

`common/scripted_triggers/fallout_world_end_captains_articles_event_triggers.txt` provides generation-bound opening, delayed result, callback, cleanup, state, target, registry, and affordability triggers. Human and hidden-AI lanes use separate event tokens and dispatch modes. Hidden AI evaluates four authored priorities and can only select a branch that remains affordable.

`events/fallout_world_end_events.txt` contains the seven dedicated blocks. The human opening has four options. The delayed result has twelve branch and outcome descriptions. The callback has success, partial, and failure descriptions. The cleanup is hidden and triggered only by the authenticated delayed-cleanup receipt. All three visible blocks use `GFX_report_event_fallout_captains_articles`.

## Ledger, grading, and delayed receipts

`fallout_event_768_initialize_ledgers` is idempotent. It initializes and clamps port legitimacy, piracy pressure, rescue duty, prize-law funds, refugee berth pressure, fleet fatigue, and Cause Memory. The registry snapshot freezes owner, controller, generation, port legitimacy, piracy pressure, rescue duty, prize-law funds, refugee berth pressure, fleet fatigue, and one lowest foreign neighbor with its owner and controller.

The result is scheduled forty-two days after the opening transaction. Grading combines frozen state values, Medicine, Recognition, port legitimacy, piracy pressure relief, rescue duty, and refugee berth pressure relief, with a maritime-remnant government bonus. Each branch has distinct success, partial, and failure thresholds. Result effects update Air Winter, Supply Access, Shelter, Exposure, Adaptation, Reclamation, Disease, Medicine, Cohesion, Recognition, Stability, War Support, the port ledgers, a branch memory, a state outcome flag, and one dedicated neighbor opinion modifier. Failure routes a bounded request through `apply_exact_state_civilian_population_loss` with the Fallout aftermath Deaths reason and a building-damage value.

The callback is scheduled three hundred days after the result. It grades current port legitimacy, Cohesion, Recognition, rescue duty, prize-law funds, Cause Memory, Supply Access, Reclamation, and Disease. Its success, partial, and failure effects update the same ledger family and add a callback memory. Callback failure uses the bounded Deaths contract. Each delayed lane records a survivor-country history payload and authenticates transition generation, owner, controller, target state, foreign neighbor, candidate id, and committed reservation before writing.

## Event Log and localisation

`common/scripted_localisation/fallout_world_end_captains_articles_event_log_scripted_localisation.txt` defines `GetFalloutEvent768EventLogDetail` for the four choices, twelve branch outcomes, three callback outcomes, and cancellation. Shared routing in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` maps history `9187` to the detail and name surfaces. The UTF-8 BOM localisation file is `localisation/english/fallout_world_end_captains_articles_l_english.yml`. It contains concrete West African port, rescue berth, prize hearing, harbor council, crew vote, and neighboring-government wording.

## Assets

The generated fictional report image is retained at `docs/assets/768_captains_articles/`. The source, processed preview, runtime DDS, hashes, dimensions, and source-mode disclaimer are in `manifest.md`. The runtime file is `gfx/event_pictures/fallout/report_event_fallout_captains_articles.dds`. The sprite is registered in `interface/fallout_world_end.gfx`. No zombie asset, audio, sprite, or path is referenced.

## Static review boundary

Static review confirms the seven event ids, candidate row, global constants, event-local constants, scripted effects, scripted triggers, dynamic modifiers, opinion modifiers, scripted localisation, shared Event Log routing, player localisation, sprite registration, runtime DDS, manifest hashes, and cleanup references are present in the source tree. The chain remains dormant because scheduler activation is intentionally unset. This proof does not claim live event delivery, save recovery, multiplayer ownership, runtime Event Log rendering, or Hearts of Iron IV execution.

A focused read-only `hoi4.event_inspect` lint request for selector `{ kind: event, eventId: chaosx.fallout.768 }` used `expandHelpers = false`, depth `1`, thirty nodes, eighty edges, and refresh enabled. It returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and artifact `event-lint-d70e71878d3d.json` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0adbb056ce218c405715ce925422f2ebfdc1eef44d53479f97dd62d59b5c071/e585132e51ea6003619ec8c9a7080c4de3d13ee74dd484052d72c26571fad547/event-lint-d70e71878d3d.json`. The report marked validation incomplete because workspace-wide helper and lifecycle projections were deferred. That tooling boundary is recorded rather than treated as live acceptance.
