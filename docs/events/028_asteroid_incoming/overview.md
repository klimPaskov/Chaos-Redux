# Event 028: Asteroid Incoming

Status: implemented in source and held disabled in the default event-log queue until the required engine-backed event, probability, map, and final audit evidence is available.

Event 028 is a global fire-once Major event with a Calm World baseline. The shared Major-event registry owns its pacing and history classification, while `events/028_asteroid_impact.txt` owns the visible chain and the Event 028 scripted effects own the transaction.

## Gameplay flow

The opening transaction selects exactly three distinct valid country/state pairs from current controlled land. It persists each country and state as a global event target, refuses wasteland and previously registered asteroid sites, and exposes a genuine miss option. If three complete pairs cannot be built, the opening event exposes `N/A` with an explicit reason instead of presenting an invalid coordinate.

The chooser selects one of the three saved pairs and receives a confirmation event. Confirmation copies the selected pair into locked targets and stores the original state id and capital status. The lock lasts two days and the resolver uses the saved scope pointers, so owner, controller, tag, and subject changes cannot silently reroll the coordinates. The locked target country chooses one preparedness stance before the impact.

The impact resolver plans the main footprint and optional fragments before changing any state. It merges overlapping profiles by severity, processes each state once, measures population before and after the loss, registers only actual deaths through the shared Deaths ledger, removes civilian buildings from the main crater, and sends one consolidated report per affected country. If the destroyed center was the target capital, the controller relocates it to a valid surviving backup state.

The main state receives a permanent nonradioactive asteroid crater marker and no civilian population or buildings. Three shortest land-adjacency rings receive the accepted 50 percent, 25 percent, and 5 percent civilian-loss profiles with severity-scaled infrastructure, railway, supply, factory, and military-site damage. Fragment centers and their two rings use the separate fragment profiles and do not create nuclear or radioactive records.

Actual deaths, destroyed capacity, affected states, fragments, and bounded supported secondary disasters feed Atmospheric Dust Load. The shared world dust state moves through Residual Haze, Global Dust Veil, Impact Winter, and Severe Impact Winter, applies production, supply, air, and weather penalties, writes a separate Air Cleanliness source slot, and decays through the Event 028 maintenance hooks. Countries can purchase three levels of national dust protection, while bounded Event 013 callbacks and recovery actions provide mitigation without a world-scan on-action.

At 600 Chaos, Global Fragmentation adds three to six independently planned fragment sites, two damage rings, overlap resolution, grouped reporting, and additional dust. Fragment centers prefer a valid land neighbor whenever the remaining global pool provides one, with a bounded fallback for genuinely isolated candidates. At 800 Chaos, Extraordinary Minerals is eligible only when fragmentation actually applied. The main crater controller receives `+100%` land-division armour and each currently controlled fragment site contributes `+20%`; the control refresh removes stale ownership benefits and rebuilds the uncapped current-control total.

Ordinary recovery uses the shared decision framework under `asteroid_incoming_recovery_category`. It exposes exact state targets, reason-specific blocked tooltips, meaningful manpower/equipment/fuel/logistical costs, reserve floors for AI and players, bounded missions, national closeout, cleanup, and one-time action flags. There is no dedicated Event 028 scripted GUI.

Five persistent achievements track the near miss, capital recovery, mineral collection, crater armour conquest, and global reconnection routes. They use persistent flags and counters, continuous-control hold windows, manual/evolution/difficulty disqualifiers, hold resets, final localisation, and completed/grey/not-eligible icon triplets.

## Runtime surfaces

The main source files are `events/028_asteroid_impact.txt`, `common/scripted_effects/028_asteroid_incoming_effects.txt`, `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt`, `common/scripted_effects/028_asteroid_incoming_recovery_effects.txt`, `common/scripted_triggers/028_asteroid_incoming_triggers.txt`, `common/scripted_triggers/028_asteroid_incoming_achievement_triggers.txt`, `common/decisions/028_asteroid_incoming_decisions.txt`, `common/decisions/categories/028_asteroid_incoming_categories.txt`, `common/ideas/028_asteroid_incoming_ideas.txt`, and `common/dynamic_modifiers/028_asteroid_incoming_dynamic_modifiers.txt`.

The event-owned tuning and identifiers live in `common/script_constants/028_asteroid_incoming_constants.txt`. The Event History and Event Details integration is in the Event 028 scripted localisation and the shared event-log registries. The super-event uses the shared event presentation slot with Event 116 text/image/audio registration, a settings-aware audio dispatch, and the final public-domain Brahms recording `sound/028_asteroid_incoming/super_event_028_asteroid_impact.wav` documented under `docs/super_events/028_asteroid_incoming_super_event_research.md`.

The visual consumer trace, DDS dimensions, source/master provenance, repair record, aliases, rejected candidates, and limitations are maintained in `docs/assets/028_asteroid_incoming/asset_audit.md`, `manifest.md`, `coverage_crosswalk.md`, and `gfx_handoff.md`. The runtime sprite definitions are in `interface/028_asteroid_incoming.gfx`; achievement triplets remain in `interface/chaosx_achievements.gfx`.

The shared Air Cleanliness source registry reserves source 4 for asteroid dust and source 5 for Acid Rain. Event 028 writes only the asteroid slot, preserving distinct chemical, biological, fallout, aerosol, and Acid Rain histories.

## Icon inventory

The accepted runtime package includes four report images, two news images, one decision-category picture plus the vanilla generic-crisis category icon, seven distinct state-modifier icons, eight 64x64 idea icons, fourteen unique 32x32 decision icons with a documented three-action reconnaissance alias, one super-event image, and five complete achievement triplets. The live fragment-center recovery modifier is explicitly audited as a second consumer of the accepted fragment-crater state icon because the specification defines no separate recovery icon.

## Future plans and extension suggestions

The package should remain disabled in the default queue until the mandatory HOI4 MCP routes return current event, probability, and map evidence. After those routes are healthy, run the ten named AI scenarios plus the recovery decision scenarios against the same implementation and record before/after probability comparisons.

Possible future extensions are a separately commissioned rival-action icon family, a recovered master for the inherited impact-news DDS, and a bounded preflight availability trigger that can prove three viable pairs before the automatic pool selects the event. None of these extensions is required to change the accepted seven-state-icon design, and none should be introduced by silently aliasing an unrelated asset.
