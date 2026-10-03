# Event 028: Asteroid Incoming

Status: implemented in source and held disabled in the default event-log queue until the required engine-backed event, probability, map, and final audit evidence is available.

Event 028 is a global fire-once Major event with a Calm World baseline. The shared Major-event registry owns its pacing and history classification, while `events/028_asteroid_impact.txt` owns the visible chain and the Event 028 scripted effects own the transaction.

## Gameplay flow

Before automatic selection, a read-only preflight requires three distinct countries other than the chooser, each with two usable owned and controlled states. The opening transaction selects exactly three distinct valid country/state pairs from that eligible population. It persists each country and state as a global event target, refuses wasteland and previously registered asteroid sites, and exposes a genuine miss option. Countries with only one usable state, occupied backups, or the CXT system identity cannot consume a target slot. When enabled, an invalid world shows `N/A` with the target-pool reason in the shared event view and remains outside automatic selection. A forced invalid opening retains its explicit `N/A` option.

The shared dispatcher builds the target board before dispatch and Major history accounting, and rejects a failed board without consuming the event. The chooser selects one of the three saved pairs and receives a confirmation event. Cancel returns through the internal `chaosx.nr28.8` board, preserving the existing pairs, chooser, opening date, and evolution snapshot without re-firing the native fire-once entry. Confirmation copies the selected pair into locked targets and stores the original state id and capital status. The lock lasts two days and the resolver uses the saved scope pointers, so owner, controller, tag, and subject changes cannot silently reroll the coordinates. The locked target country chooses one preparedness stance before the impact.

The impact resolver plans the main footprint and optional fragments before changing any state. It merges overlapping profiles by severity, processes each state once, measures population before and after the loss, registers only actual deaths through the shared Deaths ledger, removes civilian buildings from the main crater, and sends one consolidated report per affected country. It relocates only a country whose current capital is the locked center. Backup selection prefers controlled cores and safer territory, then uses surviving ring states when no safer candidate exists. A current planned fragment center remains a surviving candidate, while an existing or processed crater does not. Relocation accounting names the country that actually moved, even when owner and controller differ, and an annexer receives no original-target achievement identity.

The main state receives a permanent nonradioactive asteroid crater marker and no civilian population or buildings. Three shortest land-adjacency rings receive the accepted 50 percent, 25 percent, and 5 percent civilian-loss profiles with severity-scaled infrastructure, railway, supply, factory, and military-site damage. Fragment centers and their two rings use the separate fragment profiles and do not create nuclear or radioactive records.

Actual deaths, destroyed capacity, affected states, fragments, and bounded supported secondary disasters feed Atmospheric Dust Load. The shared world dust state moves through Residual Haze, Global Dust Veil, Impact Winter, and Severe Impact Winter, applies production, supply, air, and weather penalties, writes a separate Air Cleanliness source slot, and decays through the Event 028 maintenance hooks. Basic, organized, and hardened national protection reduce the active stage's penalties by 15 percent, 30 percent, and 45 percent. A hidden country dynamic modifier supplies the compensation beneath the existing visible protection idea, so protection cannot turn fading dust into a production bonus.

The opening Air Cleanliness injection is consumed once. Monthly reservoir pressure follows the current dust stage and global mitigation, and a date receipt prevents repeated coordinator calls on the same day from charging it twice. Falling stages and zero dust reduce the source's current pressure without refunding its historical injection. The shared Air Cleanliness recovery remains responsible for removing atmospheric contamination.

Event 013 secondary calls use one exact supported family, the affected state, and an explicit main-impact or fragment origin. The gateway validates geography and family availability. The four-call limit counts accepted scheduled jobs, and rejected families add no dust. Its own sequence and reports retain Event 028 as the caller.

At 600 Chaos, Global Fragmentation adds three to six independently planned fragment sites, two damage rings, overlap resolution, grouped reporting, and additional dust. Fragment centers prefer a valid land neighbor whenever the remaining global pool provides one, with a bounded fallback for genuinely isolated candidates. At 800 Chaos, Extraordinary Minerals is eligible only when fragmentation actually applied. The main crater controller receives `+100%` land-division armour and each currently controlled fragment site contributes `+20%`; the control refresh removes stale ownership benefits and rebuilds the uncapped current-control total.

Ordinary recovery uses the shared decision framework under `asteroid_incoming_recovery_category`. Each country stores its own exact project or mission state in `asteroid_incoming_recovery_target_state`. A pending paid project blocks another project in that country, while other countries retain independent targets. Finish callbacks recheck the reserved state and current control. Cancellation, timeout, lost control, and annexation release only that country's receipts. The category exposes reason-specific blocked tooltips, meaningful manpower/equipment/fuel/logistical costs, reserve floors for AI and players, bounded missions, national closeout, cleanup, and one-time action flags. There is no dedicated Event 028 scripted GUI.

Five persistent achievements track the near miss, capital recovery, mineral collection, crater armour conquest, and global reconnection routes. Continuous-control achievements measure elapsed days from persistent start-day receipts. Loss of control and annexation reset unfinished holds. The global reconnection award checks the protection program before zero-dust cleanup removes it. The achievements retain manual and evolution disqualifiers, final localisation, and completed/grey/not-eligible icon triplets.

## Runtime surfaces

The main source files are `events/028_asteroid_impact.txt`, `common/scripted_effects/028_asteroid_incoming_effects.txt`, `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt`, `common/scripted_effects/028_asteroid_incoming_recovery_effects.txt`, `common/scripted_triggers/028_asteroid_incoming_triggers.txt`, `common/scripted_triggers/028_asteroid_incoming_achievement_triggers.txt`, `common/decisions/028_asteroid_incoming_decisions.txt`, `common/decisions/categories/028_asteroid_incoming_categories.txt`, `common/ideas/028_asteroid_incoming_ideas.txt`, and `common/dynamic_modifiers/028_asteroid_incoming_dynamic_modifiers.txt`.

The event-owned tuning and identifiers live in `common/script_constants/028_asteroid_incoming_constants.txt`. The Event History and Event Details integration is in the Event 028 scripted localisation and the shared event-log registries. The super-event uses the shared event presentation slot with Event 116 text/image/audio registration, a settings-aware audio dispatch, and the final public-domain Brahms recording `sound/028_asteroid_incoming/super_event_028_asteroid_impact.wav` documented under `docs/super_events/028_asteroid_incoming_super_event_research.md`.

The visual consumer trace, DDS dimensions, source/master provenance, repair record, aliases, rejected candidates, and limitations are maintained in `docs/assets/028_asteroid_incoming/asset_audit.md`, `manifest.md`, `coverage_crosswalk.md`, and `gfx_handoff.md`. The runtime sprite definitions are in `interface/028_asteroid_incoming.gfx`; achievement triplets remain in `interface/chaosx_achievements.gfx`.

The shared Air Cleanliness source registry reserves source 4 for asteroid dust and source 5 for Acid Rain. Event 028 writes only the asteroid slot, preserving distinct chemical, biological, fallout, aerosol, and Acid Rain histories.

## Icon inventory

The accepted runtime package includes four report images, two news images, one decision-category picture plus the vanilla generic-crisis category icon, seven distinct state-modifier icons, eight 64x64 idea icons, fourteen unique 32x32 decision icons with a documented three-action reconnaissance alias, one super-event image, and five complete achievement triplets. The live fragment-center recovery modifier is explicitly audited as a second consumer of the accepted fragment-crater state icon because the specification defines no separate recovery icon.
The seven state textures live under `gfx/interface/state_modifiers/028_asteroid_incoming/`, with their stable sprite IDs registered in `interface/028_asteroid_incoming.gfx`.

## Dust helper contracts

`asteroid_incoming_refresh_national_dust_protection` runs in country scope after a protection choice or global stage update. It reads the current dust flags and the country's highest protection idea, overwrites six country compensation variables, adds or updates the hidden `asteroid_incoming_national_dust_protection` modifier, and removes it at zero dust or without protection. It changes no population, building, or other event modifier.

`asteroid_incoming_refresh_air_cleanliness_source` runs after the opening calculation or a monthly stage update. It reads the dust stage and global mitigation, publishes source 4's current reservoir, and records the opening injection only while its persistent receipt is absent. Its zero-dust update retains source history and removes current pressure without subtracting the original injection.

`asteroid_incoming_apply_monthly_air_pressure` is called only by the existing global-host monthly dust pulse. It applies the published reservoir once for the current date, attributes the actual shared-ledger change to the asteroid source, and resets its public temporary ledger inputs and Fallout-skip input after returning. A repeated call on the same date has no effect.

## Future plans and extension suggestions

The package should remain disabled in the default queue until the mandatory HOI4 MCP routes return current event, probability, and map evidence. After those routes are healthy, run the ten named AI scenarios plus the recovery decision scenarios against the same implementation and record before/after probability comparisons.

Possible future extensions are a separately commissioned rival-action icon family and a recovered master for the inherited impact-news DDS. Neither changes the accepted seven-state-icon design.
