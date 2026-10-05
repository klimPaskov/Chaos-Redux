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
Event 39 is listed in `event_log_event_is_reworked_default_enabled`, so a new game starts with it enabled (D20).

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

## D19. Localisation polish

Disposition: implemented.
The opening report (`chaosx.nr39.2`) now speaks in the same neutral voice as the later reports and names whoever took charge through `[ROOT.GetLeader]` in the host's own scope, which shows the curated successor or the institutional council.
The legacy news event `chaosx.news.44` and its three keys are removed: nothing fires the alias, and its text described the pre-rework murder with an invented leader biography; the opening news is `chaosx.news.4401`.
Player text no longer uses ledger, transaction, callback, runtime or validation wording; the requirement texts that flag checks show in tooltips now describe the situation (for example "The Murder Mystery crisis is under way" instead of "The murder mystery runtime is active").
The shared decision tooltips are neutral, so movement decisions no longer mention the government's case team.
The inheritance reports (`chaosx.nr39.24` and `.25`) already describe the territorial heir and underground continuation from D7 and needed no change.

## D20. Event 39 starts enabled in new campaigns

Disposition: implemented; the default queue and first automatic fire need live confirmation.
Reworked events join `event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt` through their own owners (Events 028 and 032 added their own rows), so Event 39 adds its row after Event 32 as a one-line insertion in that shared file.
Basis: the round-1 work makes Event 39 a complete fire-once pool event with its host gate, Events Log rows, cluster membership and outcomes; the catalog already lists it as Needs Testing, the same state in which Events 028 and 032 were enabled.
The Events Log toggle still disables it for a campaign.

## Round-1 review corrections

Disposition: implemented; each correction is source-reviewed and needs live confirmation with the rest of the round.

- Revolt clusters respect their size cap. The derivative neighbour loop read its remaining-state counter in the iterator `limit`, which the engine can evaluate before the body runs, so a revolt could take every eligible neighbour of its anchor state. The counter is now checked inside the body.
- A completed Run the Agency Operation sets the host's national cell back by `murder_mystery_objective_tuning.agency_cell_maturity_loss` maturity. The objective is host-only and the host never holds a row in the foreign cell registry, so its only cell outcome could never apply.
- Mechanized Infiltration's research requirement shows readable text for `murder_mystery_conventional_support_unlocked` instead of the raw flag name.
- Dismantle the Local Cell states its cell requirement through `murder_mystery_local_cell_registered_tt` instead of exposing the cell flag and registry array check.
- `murder_mystery_technology` holds only integers; its three fractional values moved to `murder_mystery_technology_float`, matching the category schemas.
- The host-fall report (`chaosx.nr39.63`) says the government has fallen, which is true for both capitulation and annexation.

## D21. The host can fall before the movement holds territory

Disposition: implemented (second round-1 review); needs live confirmation with an annexed host.
Basis: the full design authority for this workstream; Part 5 requires the network to revalidate or retire its rows when a country is annexed, and D6 cleaned up an annexed host without resolving the movement.
Before this change an annexed host left the runtime active with no pulse anchor, so the movement froze, Event 39 stayed "under way" in the Events Log, and the case could never close.
When the original host is annexed before any Assassin State or derivative has existed, the winner takes over the case (`murder_mystery_record_host_lost_before_center`).
If a cell at stage 3 or higher survives, the network continues underground around its most mature cell, the pulse anchors there, and the winner receives the existing underground report `chaosx.nr39.25`.
Otherwise the global resolution check ends the movement at once; the winner receives the existing epilogue `chaosx.nr39.62`, not the capture report `chaosx.nr39.20`, because nobody caught the murderer.

## Round-1 second review corrections

Disposition: implemented; each correction is source-reviewed and needs live confirmation with the rest of the round.

- Timed flags take literal durations. The action cooldown, the country incident cooldown, the four role-group cooldowns, the cell immunity, the aftermath window and the three super-event flags passed a variable or a constant token as `days` (and the super-event slot as `value`), which a timed flag does not read (the Event 002, 005, 023 and 028 pattern). They now go through `meta_effect` helpers that inject the tuning constants as integers. Without this the action cooldown could block every Event 039 action after the first one, and the super-events could show the wrong slot.
- A country whose cell was destroyed can receive a new cell again once its immunity lapses. The permanent `murder_mystery_cell_retired` flag made every later seeding attempt on that country fail silently, wasting the bounded seeding attempts; it is cleared when the country is chosen as a new candidate.
- Three mission texts that open with a country name use `GetNameDefCap`.

## D22. Chamberlain joins Britain by nationality, not recruitment

Disposition: implemented (round 2); the Baldwin-to-Chamberlain succession needs live confirmation in a 1936 start.
Basis: the lead's round-2 decision 1 and routed load defect B033, where `recruit_character` in a scripted effect logged "recruit_character should only happen in game/history files" at every load.
The curated Britain row attaches `ENG_neville_chamberlain` with `set_nationality = PREV` when the country does not already hold him, then promotes him and keeps the ruling-only verification before the victim is retired.
This mirrors the Assassin State setup, which attaches its predefined commanders the same way, and Kaiserreich's `CHN_recruit_character_effect`; vanilla recruits Chamberlain only in its 1939 history block, so he is unrecruited when Baldwin is murdered in a 1936 start.
No Event 039 file calls `recruit_character`.

## D23. The Assassin focus tree is loaded explicitly

Disposition: implemented (round 2); the tree's appearance on the committed state and on a territorial heir needs live confirmation.
Basis: the lead's round-2 decision 2 and Event 005's dynamic packages, which call `load_focus_tree` on their created countries.
The tree's `country` block reads `murder_mystery_assassin_state_active`, which the commit sets only after `create_dynamic_country` has already chosen a tree, so the 83-focus tree was unreachable.
`murder_mystery_commit_assassin_state_transaction` now calls `load_focus_tree = { tree = murder_mystery_assassin_focus_tree keep_completed = no }` on the validated state inside its postcondition branch, so a rolled-back candidate never gets it.
`murder_mystery_install_territorial_heir` loads the same tree on the heir unless the heir already has it (`has_focus_tree`), so an heir that was already on the tree keeps its finished focuses and any other heir starts it fresh.
The `country` block stays as a fallback; focus rewards, route shortcuts and the Evolution V shortcut read country flags and variables that both paths set before or independently of the load.
MCP evidence: `hoi4.focus_inspect` of `murder_mystery_assassin_focus_tree` reports 83 focuses, zero tree diagnostics and zero connector crossings; the only blocking diagnostic in the result is a vanilla file (`TSR_lingguang_incident_joint_branch.txt`).

## D24. World of Anarchy is a real war settled by conquest

Disposition: implemented (round 2); the war waves, capitulation choices, cell territories and victory need live confirmation in a terminal campaign.
Basis: the accepted Part 10 design and the lead's round-2 decision 4 (native puppet, annexation and state transfer plus the existing derivative path; safe successor and generic office casualties for leaders; victory only from conquest, capitulation or reconciled annexation).
Before this change sector activation only appended to an array, no war was declared, Break the Command Spine, Establish a Successor Administration and Reconstitute the Campaign Council marked registry rows settled with no conquest, every row was hard-coded to a central subject administration, and Force a Capitulation could never succeed.

- Registration: every eligible ordinary government is registered at activation (cap raised from 64 to 128 rows so a crowded map fits), sorted into the home, near or distant sector by capital distance from the central capital (1500 and 4000 map units, the scale vanilla's Spanish and Chinese scripts use for regional reach). The old round-robin sector cursor is removed.
- War: opening a sector runs one bounded wave of at most 12 declarations (`annex_everything`); targets already at war are only marked, subjects follow their overlords unless the overlord is outside the campaign, and a target in a faction the central state leads is expelled first so the movement's own faction cannot shelter an ordinary government. The pulse continues waves for opened sectors; nothing new scans the world daily or weekly.
- Settlement: only the capitulation and annexation hooks and the successor administration transaction write a settled row. The player (and AI, weighted 90 to 5 toward its route) chooses among the three Part 10 outcomes in `chaosx.nr39.65`; the route's own outcome raises Cohesion and the others cost it. A local derivative that rose against the government receives it ("existing derivative elevation") instead of a new tag. A full derivative registry turns a cell territory into a subject administration so the transaction never fails half-way.
- Subjects of subjects: a subject of a successor administration counts as on the movement's side and receives its own administration through the pulse, so it cannot block victory.
- Leaders: the existing foreign-leader transaction is reused in a dismantling mode that allows any defeated government and skips the world news and rally of a living-state murder; a protected ruler stays and the row records it.
- Victory: when every row is settled, one bounded reconciliation registers ordinary governments created since activation (releases, civil wars, peace-conference liberations); a subject administration that broke free reopens its row. This is the "rare bounded reconciliation event" Part 10 allows.
- Decisions: Break the Command Spine now disrupts the current campaign target (timed idea, stability and war support loss, generic command-staff casualty, Cohesion) and needs it more than 20% of the way to surrender; Reconstitute the Campaign Council repairs Cohesion below 70 at the cost of a timed vulnerability idea; Synchronize the Uprisings raises up to two revolts from ready cells in the selected sector through the existing derivative path. None of them settles a row.
- The three new ideas reuse existing Event 039 idea pictures (Foreign Derivative Administration, Succession Crisis, World of Anarchy Command); no new texture is needed.

## D25. A World of Anarchy victory is the movement's rule, not its defeat

Disposition: implemented (round 2); the victory report, the command promise, post-victory play and the gated defeat aftermath need live confirmation.
Basis: the accepted Part 10 sections "Victory presentation and post-victory play" and "Defeat aftermath", and the lead's round-2 decision 4.
Before this change the movement's own victory fired "The Network Breaks" (a government restoration text with the capture picture), applied the brotherhood-defeat Chaos value with the defeat history reason, cleared the world end and finalized the runtime, ending all play; and every defeat after a territorial state showed the brotherhood-defeat super-event however small the movement had been.

- `chaosx.nr39.60` is reused as the victory report rather than leaving a dead event: new title and text, the `murder_cult_revealed` report picture (the movement fully in the open), shown only to the central state.
- Victory Chaos is a new mapping, `murder_mystery_chaos.world_of_anarchy_victory = 4`, under the World of Anarchy history reason; activation already added 8, and the world remains ruled by the movement, so the value adds rather than reverses.
- The command promise follows the four Part 10 outcomes, one per route plus the mixed settlement, each with a permanent idea, a Cohesion change and a subject-autonomy change through `every_subject_country` and `add_autonomy_ratio` (literal steps as file constants, since the effect reads literals). New ideas reuse existing Event 039 idea pictures.
- Post-victory play keeps the World Without Leaders category with two administration decisions and Reconstitute the Campaign Council. Reconstruction and local conflict beyond autonomy and Cohesion are left to the native subject and resistance systems.
- The movement no longer seeds cells in, strikes, or raises revolts from its own subjects, which after a victory would otherwise turn the pulse against the movement's administrations.
- Defeat aftermath gate: Evolution IV or V and at least 4 countries held or administered (the center counts once; derivatives are counted by a new `global.murder_mystery_derivatives_ever_created` incremented in the shared derivative commit). Only then does `chaosx.nr39.61` show the super-event and world news and grant the existing (previously unused) Postwar Protection Compact to the government that owns the case; otherwise it is a plain report with its own text. Part 10 also names duration, deaths and coalition breadth; country count and evolution stage are the measurable, recorded proxies.
- A movement that won World of Anarchy and is later destroyed clears `world_end_murder_mystery` and `world_end` when the movement ends.

## D26. Event 039 wars opt out of Event 009 White Peace

Disposition: implemented (round 2); needs live confirmation that Event 009 skips the protected actors.
Basis: Part 11 (host wars and World of Anarchy wars must not receive an unrelated automatic white peace) and the lead's round-2 decision 8.
Event 039 uses Event 009's existing opt-out flag `white_peace_protected_war_actor` from its own files only, with a private marker `murder_mystery_white_peace_protection_set` so it never clears a protection another owner gave.
Protected: the central state (commit and heir), every active derivative (the shared derivative commit, so revolts and cell territories), the original host while at war with the central state, and every World of Anarchy target at war with it.
The movement pulse reconciles the set every ten days, which also covers wars that end by separate peace; cleanup, defeat, annexation, successor administrations, terminal cleanup and victory clear it.
Event 009's flag blocks a country from every white peace, not one war; Part 11's concern is that any white peace of these actors strands the split, inheritance or administration state, so the country-wide opt-out is the intended behaviour.

## D27. The three missing Part 8 decisions

Disposition: implemented (round 2); targets, costs, the interception roll and the spirits need live confirmation.
Basis: Part 8 (Support a Threatened Partner, Reinforce a Derivative, the derivative's choice of obedience, autonomy or local campaign) and the existing transaction and cost-family pattern.

- Support a Threatened Partner targets countries in the cell registry, because the local case of a foreign government lives in its cell row; "route access" is a land border, a shared faction or military access, the native relations a convoy of investigators and vehicles would need. It uses the existing route watch family (trucks, manpower, command power). Interception is a 35% roll while the movement's Reach is above 60, so a strong network makes help unreliable without making it pointless; an intercepted convoy exposes the sender and feeds the movement, and only then fires a report.
- Target protection is the partner's witness safety and target vulnerability, the two country values Event 039 already uses for protecting likely victims.
- Reinforce a Derivative sends real equipment with `send_equipment` (the Event 006 pattern with script-constant amounts) and moves manpower from the central pool. Distance scaling reuses the cell supply family: a distant derivative pays it twice, an obedient one never does; the affordability trigger computes the doubled amount with temporary variables, which triggers support, so no parallel constants are needed.
- "Several derivatives supported" means a second derivative reinforced within 180 days.
- The priority choice is three decisions sharing one variable, mutually exclusive by visibility, each swapping one spirit and changing subject autonomy through `add_autonomy_ratio`; "more central support" for obedience is the neighbour reinforcement rate everywhere plus a higher central AI weight to reinforce it. The decisions are paid by the derivative itself (local administration family), since the choice is its own.
- New icons reuse existing Event 039 decision textures under new sprite names (`GFX_decision_039_murder_mystery_priority_*`); Support and Reinforce consume their already registered sprites.

## D28. Movement countries carry host-derived names and distinct carriers

Disposition: implemented (round 2); the names and flags need live confirmation on the political screen and the map.
Basis: Part 6 (names derived from the host or region) and Part 5 (each derivative tied to its parent, no duplicate cosmetic identities), with the lead's round-2 decision 5 (the existing pool tags and the Event 014 scripted-name precedent; no new tags).

- The Assassin State stores its host country as a variable at creation and is "The [host adjective] Brotherhood" (adjective "Brotherhood"), through scripted localisation like Event 014's CBA names. A country variable keeps resolving to that tag's name after the host is annexed; a dynamic host whose slot is later reused by another dynamic country would follow the new country's name, an accepted edge case since dynamic hosts are rare and the event host gate prefers established governments.
- Derivatives draw the first carrier no living country uses from AXT, AXU, AXV, AXW, AXY and AXZ (AXX belongs to Event 006). The check is a one-time `any_country` test of six tags at creation, not a recurring scan. The concurrent cap drops from 12 to 6 (and the unused registry row ceiling to match) so the pool can never run out while the registry still has room; the evolution and achievement thresholds (3 and 4 derivatives) stay reachable.
- Each derivative is "The [parent adjective] [carrier name]", for example "The Polish River Cell", keeping each carrier's distinct flag and flavour while tying the name to the government it rose against or, for a cell territory, the government it replaced.
- The shared carrier setup moved into `murder_mystery_initialize_derivative_carrier`, so revolts and cell territories start from identical runtime, spirit, manpower and kits.

## D29. The four case objectives bind real targets

Disposition: implemented (round 2); the bindings, the shipment delivery and the mission outcomes need live confirmation.
Basis: Part 8 (a witness transfer between named states, preventing a specific support shipment, dismantling recruitment before a deadline, protecting local leadership during a crisis) and the event doc's own list of simplified checks.

- Every bound objective records its start date and its completion triggers require a later date, so none can resolve on its first day (the old recruitment and shipment checks were true at activation for any immature cell).
- Witness transfer: origin is the capital, destination a random fully controlled state rail-connected to it at the start; the old witness-safety threshold is dropped because the named route is the objective.
- Shipments: Supply the Selected Cell's maturity (+20) and readiness (+15) now travel as a recorded shipment that the pulse delivers after 45 days; the other supply effects stay immediate. Shipments are identified by a unique generation from the transaction sequence, so the interception mission binds exactly one shipment. Raids that damage or destroy the cell cancel it; a cell turning into a derivative counts as delivery, so it cannot hand the government a success. Delivery runs in the pulse (every 10 days), so arrival can lag the date by up to one pulse.
- Recruitment: the cell row is bound by its unique generation rather than its country, so the trigger compares numbers only (`any_of` over the generation array, reading the maturity at the same index); the floor is 20 maturity below the start value.
- Local government: the protected government's `murder_mystery_incident_history_count` (raised by every office casualty and ruler murder the movement commits there) is recorded at the start; any increase fails the objective. The old capital-control and target-vulnerability proxies are dropped.

## D30. Round-1 review leftovers

Disposition: implemented (round 2).
Basis: the round-1 review findings and the revolt-cluster fix already recorded under "Round-1 review corrections".

- The Assassin State split checks its size cap inside the `every_neighbor_state` body before each registration, as the revolt cluster already does, so one expansion round can never take more than `murder_mystery_split_state_limit` states and the original government keeps its remnant.
- Objective AI strategies (`conquer` for Dismantle the Command Network and Force a Capitulation, `protect` for Protect the Derivative) record their target on the objective owner and are removed exactly once by adding the same strategy with the negated value (`@murder_mystery_objective_ai_*_undo`) when the objective context is cleared, which every success, partial result, failure, cancellation and cleanup does; a new binding first removes any strategy still recorded.
- The `murder_mystery_action_cost` category was already removed when the cost families replaced it (commit `d4b41da92`); this pass removes the remaining dead tuning that nothing reads: 21 superseded per-action values in `murder_mystery_action_tuning`, the stale registry ceilings (`maximum_derivative_rows`, `maximum_terminal_rows` = 64 against the live 128, `maximum_terminal_sector_rows`), three unused World of Anarchy readiness values and the carrier `pool_size` mirror. A repository scan confirms none of them is referenced.

## D31. The institutional successor portrait is a people-free emblem

Disposition: implemented (round 2); the portrait needs live confirmation on the political screen.
Basis: the lead's round-2 decision 6 and Part 18, which treats any placeholder portrait as a hard blocker.
`GFX_portrait_039_emergency_council` read the vanilla `leader_unknown.dds`.
The portrait stands for a generic Emergency Council or Acting Cabinet, named only from the country's adjective, and shows no person and no real institution's insignia, so it is classified as a fictional, people-free emblem; Part 3's grounded mode is for real individuals and real institutions' actual insignia.
It was generated with native ImageGen (an empty council chair at a cabinet table with a blank-sealed folder, no text, faces, insignia or religious imagery), processed with the roster's cover fit to 156x210, converted with the skill's `convert_to_dds.py`, and wired to the unchanged sprite name. The prompt, source, processed PNG, hashes and review are in the local portrait manifest (`docs/assets/039_murder_mystery/portraits/manifest.md`; `docs/assets/` is not tracked by git).

## D32. Vanilla unit sounds are the final Event 039 unit audio

Disposition: accepted; closes the round-1 unit-audio blocker.
Basis: the lead's round-2 decision 7.
The five Event 039 units already play fitting vanilla infantry, machine-gun and armoured-car sounds bound to their real actions (the 2026-09-28 model handoff). New audio would need a download that only the user can authorize, and the bound vanilla sounds already match the units' weapons and vehicles, so they are accepted as final rather than recorded as a pending gap.

## D33. Part 11 reactive connections and collision guards

Disposition: implemented (round 2); the gates and pulse adjustments need live confirmation alongside Events 005, 006, 022, 033, 034 and 035.
Basis: the accepted Part 11 design; all reads are of other owners' existing triggers and flags, with no edit to their files.

- Collision guard: Event 005 and 006 expose their in-progress state through the shared liberation-release predicates (`is_soviet_collapse_active_origin_country`, `is_independence_wave_active_origin_country`, `is_liberation_release_current_reserved_country`) and Event 006's `independence_wave_origin_prepared`; Event 039 refuses its split preflight, revolts and cell seeding for such a country. The preflight check sits in the split validation itself, so a split prepared earlier fails closed when a collapse starts.
- Pulse context (bounded, constants in `murder_mystery_pulse_context`): war and the Great Depression each add 1 cell maturity and remove 1 case or local case per pulse; an industrial boom adds 1 case; acid rain at the capital removes 1 from both. These are deliberately small next to the base growth so the other events shape, but never decide, the investigation.
- Event 022 detention is one explicit government decision, available only with an operational detention site and a cell on the country's soil. It uses the public strain cost family and trades 15 cell maturity and 15 exposure for 5% stability, 10 Evidence Integrity and 5 movement Reach; the AI weight is low and blocked below 50% stability or 40 Evidence Integrity, so detention is never the default investigation method. Condemnation is left to the shared source adapters, as Part 11 requires.
- Contamination and CBRN connections stay with their shared owners; Event 039 grants its units no immunity and adds no new adapter.
