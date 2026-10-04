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

Disposition: implemented (commit `e83c64376`).
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

## D13. World of Anarchy uses the shared world-end toggle

Disposition: implemented.
The 039 world branch checked `murder_mystery_world_branch_disabled`, a flag nothing set, so the branch could not be switched off from Event Details.
World of Anarchy is now a registry row with scenario ID 16, the next free world-end ID after Global Jihad (15), owner event 39, and super-event 112, which is the World of Anarchy super-event in the shared numbering.
The branch toggle reads `global.disabled_world_end_scenarios` through a scripted trigger in `chaosx_world_end_scenario_triggers.txt`, matching the Event 031 Global Jihad row it was cloned from.
The shared edits are four minimal insertions in the registry constants, the registry and active-state blocks of `chaosx_events_log_effects.txt`, three scripted-localisation rows, and one trigger.

## D14. Achievements read one-shot receipts

Disposition: implemented; unlock behaviour needs live confirmation.
The eight Part 16 achievements follow the Event 033 layout (`possible` and `happened` with custom tooltips, criteria triggers, receipt flags), with one change: `possible` reads only run-wide disqualifiers that are false at game start, because the offline wiki states that an achievement whose `possible` is false at game start can never be earned.
Event 033's `possible` requires a tracking flag that does not exist at game start; that is outside this event and is reported rather than changed.
Departures from Part 16, each kept within the spec's intent:
A Net Without Knives counts five simultaneous foreign cells through the existing `murder_mystery_five_foreign_cells_reached` flag rather than five unique cell countries, and only the original host can earn it because no intelligence-coordinator role exists.
The Knife Breaks contribution floor is dealing the central defeat or completing two case objectives after the split.
The Empty Chair Holds forgives up to two consecutive pulses (about twenty to thirty days) without the original capital.
Necessary Hypocrisy proves the Mechanized Assassin formation with a majority template and one fielded mechanized division; it does not measure the division's supply.
The Last Safe Cabinet treats any Event 39 office casualty after activation as losing a protected office, and keeps the activation ruler through a character flag.

## D15. Decision costs come from fourteen cost families

Disposition: implemented; affordability and debit need live confirmation.
Every action used to pay a hidden flat 20 political power, plus 5 command power for two actions, and only the two raids showed a real cost.
Each decision and selectable mission now names one cost family when it is taken, and the family decides what the payer spends: seven government families (case authority, security detail, forensic inquiry, route watch, armed raid, capture planning, public strain) and seven movement families (Brotherhood council, cell supply, field operation, revolt preparation, local administration, terminal settlement, terminal campaign).
Each family spends two or three resources, shows them through `custom_cost_text` with texticons, and uses one inclusive affordability trigger in both `available` and `custom_cost_trigger`.
Political power remains only on political, legal and council actions; security work spends manpower, support equipment and command power, raids spend rifles and manpower, route work spends trucks, and movement actions spend operations kits, rifles, trucks and manpower.
The government response profile surcharge now applies only to the political power of the case authority and public strain families, where a profile changes how much political cover an action needs.
The debit records one receipt per resource and a rolled-back transaction refunds exactly those receipts, replacing the four fixed refund flags.
Cell actions are paid by the central movement state while it can act, matching where `murder_mystery_decision_run_cell_support` runs the transaction; the cost tooltip says so.
Operations kits have no vanilla texticon, so a 24x24 texticon was downscaled from the existing kit equipment icon rather than generated.
The cost text colours every amount red when the payer cannot afford the action, the repository's established blocked-cost pattern; per-resource colouring would need a scripted localisation entry for every family and resource.
The HOI4 MCP `probability_inspect` route returned `INTERNAL_ERROR` for a narrow `decision_ai_will_do` query on one decision, so no baseline or compare evidence exists for the changed AI blocked conditions; each changed condition only swaps the old political power gate for the family affordability trigger.

## D16. Fourteen new objective missions complete the Part 8 families

Disposition: implemented; binding, timers and outcomes need live confirmation.
The missing families are now objectives: Run the Agency Operation for the host; Contest the Supply Route, Capture the Case Archive, Keep the Cell Supplied, Grow the Cell Quietly, Prepare the Revolt Cluster, Hold the Subjects Together and Synchronize the Cells for the central state; and Dismantle the Command Network, Force a Capitulation, Hold the Sector Capitals, Protect the Central Command, Protect the Successor Government and Reduce the Sector Governments for the terminal campaign.
Each one binds concrete targets (a host border state, the selected cell's registry row, the current campaign target, the smallest derivative, or the sector snapshot) and has separate success, failure and, where the objective can be half done, partial outcomes with their own effects.
A country still runs one objective at a time, as the existing sixteen do, because every objective shares one context and sets the phase-mission flag; the spec's one to three concurrent missions per country would need a second context and is not attempted.
New objectives are started only through `murder_mystery_decision_offer_objective`, which refuses while an objective runs, so a later action never overwrites the running objective's type or targets.
Starts follow the action that creates the objective: a successful Commit a Case Team or Audit Communications starts the agency operation; the Brotherhood's own cell missions start the three cell objectives; the opening war chains Survive the Opening War into Contest the Supply Route and then Capture the Case Archive while the war with the host lasts; each terminal decision starts the objective it implies; Complete the Terminal Sector chains into Hold the Sector Capitals.
Hold the Subjects Together is also opened by the movement pulse when the central state's Cohesion falls below 40 while a derivative is bound to it, because a subject can break away without any player action.
Cell values are read directly from the bounded cell registry; the synchronized-cell count and the sector count are published by the pulse, which already runs every ten days on one anchor, so those two objectives can complete up to one pulse late.
The agency operation is host-only because missions belong to one category and foreign governments use a different category.
Terminal objectives add a conquer or protect AI strategy toward their target; the AI has no other way to read a non-selectable mission.
The fourteen missions reuse existing Event 039 decision textures (including the five previously unused ones) under new `GFX_mission_039_murder_mystery_<objective>` sprite names, so bespoke art can replace them later without renaming.

## D17. The Assassin technology line is a visible infantry-folder branch

Disposition: implemented; on-screen placement needs live confirmation.
The seven technologies had no folder, no position and an AI weight of zero, so they existed only as focus grants.
They now form one branch at the bottom of the infantry folder, the closest thematic folder with free space below its special forces branch; the support folder has no free rows and a new folder would need new tabs in the shared tech tree interface.
A new folder branch needs a gridbox in `interface/countrytechtreeview.gui`, so one gridbox (`murder_mystery_clandestine_combat_training_tree`) was inserted beside the special forces gridbox as a minimal edit in that shared file, preserving its CRLF line endings.
The other six technologies hang from the root through `path`, which the engine uses both to draw the lines and to require the parent.
`allow_branch` on the root hides the branch from every ordinary country, and every `allow` keeps research to Assassin States and derivatives.
Master Cadre Command can be researched only after Evolution V and Mechanized Infiltration only on the pragmatic route (`murder_mystery_conventional_support_unlocked`), the gates Part 9 attaches to those units; the focus grants still bypass them through `set_technology`.
AI weights are 3, doubled at war, so movement countries research their own line ahead of generic technologies.
MCP evidence: `hoi4.tech_inspect` trace before the change showed the root with no descendants; after it, the trace shows the six path edges in five layers, the `lint` of the root in the infantry folder reports no issues, and `hoi4.tech_render` of the infantry folder resolves all seven icons with source-accurate layout.
The `hoi4.probability_inspect` route returned `INTERNAL_ERROR` for a narrow `technology_ai_will_do` query, so no probability baseline or compare exists for the new weights.

## D18. The Intelligence cluster takes runtime ID 20

Disposition: implemented; cluster rolls and Events Log rows need live confirmation; the workbook change is queued in `catalog_changes_pending.md`.
The workbook lists Intelligence as cluster 8 with members 39 and 52, but runtime cluster 8 is Diseases (workbook 13), so the workbook ID cannot be used.
Intelligence takes `event_cluster_id.intelligence = 20`, free in both the runtime registry and the workbook.
It is a one-time cluster at unlock tier 0 (Chaos level 1), matching the workbook's Minor Fire-Once type.
Event 52 is the required Low baseline and Event 39 the optional Medium member, following the Negative Economy pattern where the Low event anchors the cluster and the heavier event joins by chance.
Both members fire through `fire_event_by_temp_id_no_cluster`, so Event 39 still passes through its weighted prefire host selection and its pool unavailability reasons; the cluster cannot pick a host itself, bypass the succession gate or open a second network, and a refused Event 39 is recorded as a skipped member.
Existing saves receive the cluster through an append-only migration beside the Random Stuff one; new games receive it from the definitions list.
The Events Log and settings name rows and the cluster description were added beside Negative Economy as minimal insertions in the shared files; the two localisation keys live in the Event 039 localisation file because the shared GUI localisation file has mixed line endings.
Another engineer's uncommitted Various Anomalies hunks in the same shared files were left uncommitted and untouched; this commit contains only the Intelligence lines.
