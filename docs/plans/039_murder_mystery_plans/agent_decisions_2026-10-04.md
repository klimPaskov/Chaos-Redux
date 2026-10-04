# Event 039 agent decisions, 2026-10-04

These are implementation decisions taken by the Event 039 engineer under the full design authority granted for this workstream.
Each entry is an accepted agent decision; the acceptance basis is the lead's round-1 planning decisions and the accepted Event 039 specification package under `docs/specs/039_murder_mystery_specs/`.

## D1. Adopt the stopped thread's character-safety, capture and objective rework

Disposition: implemented (commit `c47cf7769`).
The uncommitted rework was coherent, contained routed inbox fixes 1 to 4, and removed the last character-scope `exists` checks from HEAD.
The capture shock subtracts its computed loss directly instead of negating it first.

## D2. Event 39 is a fire-once pool event dispatched to a weighted host

Disposition: implemented (commit `926a3eabf`).
Event 39 moves from the repeatable list to the fire-once list.
`fire_event_by_temp_id_no_cluster` runs `murder_mystery_prepare_random_event_fire` and sends `chaosx.nr39.1` to `event_target:murder_mystery_prefire_host`.
When no host is valid the fire is refused, the automatic timer is recalculated, and nothing is recorded.
The Events Log uses four Event 39 unavailability reasons (IDs 47 to 50: investigation active, case closed, world ended, no eligible host), which were the next free IDs in `event_system_event_unavailability_reason` when the change was made.
Event 39 still is not in `event_log_event_is_reworked_default_enabled`, so a new game starts with it disabled until that shared rework list is updated by its owner.

## D3. Evolution logging and toggles

Disposition: implemented (commit `928c262b7`).
Evolution rows use `constant:murder_mystery_evolution_log.evolution_type` (39) and tiers 1 to 5, matching the Chaos thresholds 200, 400, 600, 800 and 1000.
Readiness triggers read `events_log_disabled_evolution_39_39_<stage>` directly, the same way Event 006 does, because a trigger cannot set the temp inputs that `is_current_evolution_enabled` needs.
A disabled stage is a ceiling: natural pacing and scenario setup stop before it.
Scenario setup creates the Assassin State only after Evolution III is committed and derivatives only after Evolution IV.
The opening transaction records its own history row only for scenario launches, because the event pool already records natural and manual fires.

## D4. The movement escalates through one hidden pulse event

Disposition: implemented (commit recorded in the round report).
A hidden, self-rescheduling event (`chaosx.nr39.90`) runs every 10 days on one anchor: the original host, then the central Assassin State, then the underground center, then the government that owns the case.
Part 12 forbids only new whole-world loops; the pulse touches the anchor, the host and the bounded cell and derivative registries.
A recorded due date, not a per-country ticket, rejects a pulse that was queued before the chain was rescheduled, so a lost anchor never leaves two chains running.
The government decisions that committed evolutions and prepared or committed the Assassin State are removed: the victim government no longer escalates its own crisis.
Evolution III selects its split cluster on the pulse only when every other Evolution III condition holds, and records only after the state transfer and war commit; a failed split retries after the evolution retry delay.
`murder_mystery_commit_evolution_stage` no longer requires the never-set `murder_mystery_evolution_owner_enabled` flag, which had made every natural evolution commit fail.

## D5. Scheduled incidents are generic office casualties

Disposition: implemented.
Incidents strike the surviving host or a registered cell country at stage active or higher, rotate across four office role groups with a 60-day role cooldown, and use the existing 21-day country incident cooldown.
No named character is killed by a scheduled incident; named murders stay with the safe-target transactions.
Witness Safety and protected targets give up to a 60 percent chance to stop the attack, which turns the government's protection decisions into real counterplay.
Each generic casualty now takes a fresh transaction number, because a repeated casualty without one reused the previous target ID and failed registration.
The evolution readiness flags that nothing produced are wired: an escaped final operation records the foreign-route incident for Evolution II, four host incidents during a compromised investigation record the Evolution III murder sequence, and Evolution IV reads the focus milestone as the global flag the focus sets.

## D6. Country-loss outcomes

Disposition: implemented.
Capitulation and annexation hooks run only for countries with an Event 039 actor flag while the runtime is active.
A capitulated Assassin State or derivative is absorbed by its winner one day later, so a defeated movement country does not survive as a landless or partial shell.
Host capitulation or annexation by the movement grants the Assassin State Cohesion and Reach, completes its opening-war objective, and adds Chaos; annexation by anyone cleans up the host runtime.
Cell and derivative reconciliation no longer drop rows whose parent country is gone, because that wiped every foreign cell when the host was annexed and every derivative before inheritance could read them.

## D7. Inheritance replaces leader replacement

Disposition: implemented; the curated-successor and opening-targeting work in item 8 is separate.
The old same-country leader replacement (`murder_mystery_apply_limited_inheritance`) is removed.
The classification runs once per announcement: territorial heir (best active derivative by owned states, then industry capped at 99, then Cohesion; one allowance), else underground continuation in the most mature cell at stage 3 or higher, else the end of the movement with a bounded remnant cleanup.
Heirs keep their own leader; no inheritance step retires or creates a character.
Global resolution is checked on every pulse, on cell retirement by a raid, and on country loss.

## D8. Government cell raids use ordinary resources

Disposition: implemented.
Raid an Identified Cell and Dismantle the Local Cell cost 15 command power, 300 infantry equipment and 2000 manpower, shown as the decision cost and refunded if the action transaction rolls back.
The host raids its own national cell, so its raid no longer needs a selected foreign cell; a foreign government raids the cell registered in its own country.
Registering a cell opens the foreign government's local case, and foreign cases move from mapping the network straight to breaking the cell because the protection phase has no foreign actions.

## Validation limits

The HOI4 MCP probability route returned `INTERNAL_ERROR` for a narrow `mission_ai_will_do` inspect of the two raid missions; no baseline or compare evidence exists for the changed blocked-weight conditions.
All lifecycle behaviour is source-reviewed only and needs live-game confirmation: pulse cadence, incident frequency, evolution timing, capitulation and annexation hooks, heir rebinding, and the winner absorbing a capitulated movement country.

## D9. Murdered rulers are resolved by the anchor helper and replaced by an institution

Disposition: implemented; the institutional portrait art is blocked (see below).
The opening and foreign-leader transactions resolve exactly the sitting ruler through `murder_mystery_capture_current_ruling_character` and fail closed when it cannot be resolved; the inheritance path no longer selects or retires anyone (D7).
Grounded governments receive an institutional replacement named from the country adjective through a meta effect (the cannibalism warlord-name precedent): an Emergency Council after the opening murder and an Acting Cabinet after a foreign murder, each with a marker trait that the post-install ruler check reads.
The curated native row is Britain only: `ENG_stanley_baldwin` to `ENG_neville_chamberlain`, same party and ideology, vanilla portrait, verified as ruling after promotion; this follows the stopped thread's ENG succession audit.
A general per-country focus-route dependency check is not available in script, so the host gate excludes civil wars and stale anchors; the institutional replacement keeps the ruling ideology, which keeps ideology-gated focus routes open.
Asset blocker: Part 3 classifies an institution of a real polity as grounded, which requires sourced institutional material through `chaosx_portrait_creator`; this session cannot spawn that worker and needs the user's permission to download a source image.
`GFX_portrait_039_emergency_council` is registered and wired to the vanilla unknown-leader texture (`gfx/leaders/leader_unknown.dds`) until a sourced, people-free institutional emblem replaces the texture at the same sprite name.

## D10. Starting forces and AI for movement countries

Disposition: implemented; AI template and strategy effects need live confirmation.
The Assassin State receives its first three Assassin technologies (cadre, kits, Saboteur Cell support), an Assassin Cadres template and a Movement Militia template, divisions scaled one per owned state within constant bounds, and reinforcement stockpiles; derivatives receive a reduced package plus research slots, neutrality politics, stability, war support and the recruitment idea.
Template names are literal strings because HOI4 template names are not localisation keys.
`create_unit` division strings carry their start factors literally (the CXT precedent); everything else reads `039_murder_mystery_forces_constants.txt`.
`add_ai_strategy` and AI strategy files reject script constants, so the AI weights are file-scoped `@` values, as in Event 014.
The AI template avoids `available_for` because movement countries are dynamic tags; it relies on zero upgrade priority outside movement countries and on the cadre sub-units being locked behind movement-only technology.

## D11. Derivatives come from mature registered cells

Disposition: implemented.
The derivative transaction read the cleared Assassin State candidate target, so every derivative creation was rejected; it now reads the committed Assassin State.
Revolts select the most revolt-ready insurrection cell (Evolution IV reveal) or the first cell to reach full readiness (pulse), take a connected anchor-plus-neighbour cluster, and declare war on the government they rose against.
A failed revolt returns every moved state to its government; the old rollback gave them to the Assassin State.
The derivative follows the central state's route instead of the caller's, which had made every pulse- or event-driven revolt a Cells Without Masters revolt.
Maximum-intensity scenarios prime their first seeded cells as ready insurrection cells before raising their revolts.
Cell seeding uses a land border with the host, a land border with an existing cell, or an ally of the host, one route per attempt.

## D12. The scenario opening runs synchronously

Disposition: implemented.
The launch used to queue `chaosx.nr39.1` one day later and leave `murder_mystery_scenario_launch_in_progress` set forever if that event's trigger failed; it now runs the shared opening effect immediately on the chosen host and always clears the in-progress flag and intensity.
A manual launch ignores the shared individual-crisis load cap, because the player explicitly asked for this crisis; High and Maximum prefer hosts with more than six controlled states so the opening split can succeed.
The seeding and revolt loops stop after a constant attempt budget; the old loops could retry up to the engine's 1000-iteration limit.
