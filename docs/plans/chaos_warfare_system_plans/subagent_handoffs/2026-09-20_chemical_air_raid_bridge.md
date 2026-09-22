# Chemical air and rocket raid actor bridge

Disposition: implemented in the current working tree for the user-authorized CBRN raid overhaul, pending parent integration review and live-game validation by the user.

## Owned files and behavior

- `common/raids/cbrn_chemical_air_raids.txt`: All 44 native outcome callbacks across 11 raid types save chain-local regular event targets for actor, exact selected state, victim, agent, route, outcome, and payload tier, then fire one immediate hidden country event on the actor. The original native plane loss, XP, raid history, sound, visual effect, and victim tooltip remain on their original outcomes. All 11 types remain in the shared `chemical_raids` category.
- `events/cbrn_chemical_air_bridge_events.txt`: `cbrn_chemical_air_bridge.1` verifies one marker in each finite family, route-to-payload consistency, rocket agent eligibility, actor identity, victim existence, selected-state controller, and continued war, then rebuilds temporary inputs in actor-country ROOT and calls the existing resolver once. An invalid target or malformed marker set cannot dispatch a chemical release or attempt through this event.
- `common/scripted_effects/cbrn_chemical_raid_effects.txt`: The existing resolver reads the saved regular targets instead of raid-instance variables. Native `essential_equipment` collection is the only payload debit. The script no longer manufactures an unused-payload refund, and the recorded consumed payload equals the full 120-lot ordinary or 240-lot rocket collection. Partial and catastrophic delivered dose continue to vary independently of that payment.

The ordinary air agents are chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, and behavioral agent. The strategic rocket agents are sarin and soman. Every agent has native failure, limited success, success, and critical success callbacks.

A source audit matched all 44 callbacks to the expected agent, route, outcome, and payload tier, and found no global event-target writer for the `cbrn_chem_air_bridge_*` marker family. The installed vanilla trigger documentation and existing mod use support checking the selected state's controller through a saved country target.

## Sources and checks

The offline Paradox wiki Data structures and Event modding pages establish that regular event targets carry into fired events while temporary variables do not. The installed vanilla `common/raids/_documentation.md` establishes that `actor_effects` runs in raid-instance scope and that `essential_equipment` is collected after raid creation. The installed vanilla effects and triggers documentation confirms country-event and event-target syntax. Vanilla `common/raids/air_raids.txt` preserves raid-scoped damage, XP, history, and outcome presentation in the raid definition.

The event MCP focused scan/lint and scope render used revision `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964`. The focused scan found 9,827 indexed events and zero blocking diagnostics, but returned `EVENT_INSPECTED_PARTIAL` because it deferred workspace-wide helper projections and lifecycle passes. The event-ID scope selector selected zero nodes, while the file-path overview selector selected two nodes, so the current render does not establish a source-linked bridge call path by event ID. The selector-free full scan used earlier revision `35101b9db1e7f8b4a676e4d5d9ffe26563dcfb25dd1d5fa896fab1c8ce4cfb07`, before the new event entered the index, and reported 3,905 workspace-wide blocking diagnostics; it is not evidence specific to this bridge. The probability MCP inspected the existing resolver with the `direct_random` adapter and reported no supported weighted candidate in that source. Native raid `success_factors` are outside that adapter's reported candidates. Source mapping and script structure need parent review; no game process or logs were used.

## Integration limits

Native raid cancellation/refund semantics are not specified in the installed raid documentation. This repair does not invent a manual cancellation refund. The invalid-target guard deliberately skips scripted release and attempt while retaining native raid outcome/history effects and the engine's already-collected cost. Shared delivery documentation still needs the parent-owned terminology update from partial net consumption and script refund to native full collection plus separate delivered dose.
