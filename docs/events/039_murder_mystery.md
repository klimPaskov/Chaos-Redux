# Event 039 Murder Mystery

Event 039 opens a national investigation after the sitting leader is murdered.
The investigation can uncover a cult, foreign cells, an armed territorial movement, and a campaign against ordinary governments.
The Assassin movement is fictional and has no connection to the Nizari Ismailis, any real religion or ethnicity, historical societies, or anarchism as a whole.

## Design authority and implementation status

The active user goal explicitly authorizes implementation from the accepted Event 039 package under `docs/specs/039_murder_mystery_specs/`.
This is the acceptance basis for the package requirements, including Part 8's real objectives, bounded target management, and lifecycle cleanup.
Current implementation is incomplete and this document does not certify the package or the Part 18 acceptance matrix.
Character validation checks exact membership in the recorded owner's recruited roster, unused target disposition and a frozen row generation.
Consumed rows retain their identity as tombstones during the active lifecycle, so reconciliation cannot reauthorize a second removal.
The validator returns its ownership proof to the actual calling country through a regular event target, including calls made inside a chain rooted in another country.
The First Knife pointer is resolved from the sitting leader through a synchronous modifier-free native trait anchor after its generated package name is verified.
The anchor is removed before the helper returns and never supplies a death authorization by itself.
Founder capture installs and verifies the current route's successor before removal and records a persistent core-capture receipt.
Baseline offender identity is allocated once for the original host and cannot replace a missing, invalid or previously captured territorial founder.
A surviving Assassin State loses bounded Cohesion and Reach after capture and keeps its country, forces, route and foreign network active.
Capture alone does not certify worldwide dismantling or territorial inheritance.
The implementation and evidence limits for the current objective repair are recorded in `docs/plans/039_murder_mystery_plans/validation/mission_repair_2026_10_03/repair_evidence.md`.
The agent design decisions taken under the round-1 authority (D1 to D20: pool firing, evolution logging, the movement pulse, country outcomes, inheritance, ruler targeting, starting forces, scenario launch, World of Anarchy, achievements, decision costs, objective families, the technology branch, the Intelligence cluster, localisation and the default event queue) are recorded in `docs/plans/039_murder_mystery_plans/agent_decisions_2026-10-04.md`, and pending workbook corrections in `docs/plans/039_murder_mystery_plans/catalog_changes_pending.md`.

## Murdered rulers and their replacements

The opening murder and a foreign cell's high-value murder both target only the sitting ruler, resolved through the synchronous anchor-trait helper `murder_mystery_capture_current_ruling_character`; an unresolved or ambiguous ruler fails the transaction closed, so an opposition party leader is never killed in the ruler's place.
The replacement takes office before the victim is retired, through `murder_mystery_install_emergency_successor`:

1. A curated native successor row applies first. The only row is Britain: a murdered `ENG_stanley_baldwin` is succeeded by `ENG_neville_chamberlain`, attached to the country with `set_nationality` when it does not already hold him (character recruitment is history-only, and a 1936 start recruits him only in the 1939 history block) and then promoted in the ruling democratic party, with his vanilla portrait.
2. Otherwise an institutional body named from the country's adjective takes office in the ruling party's ideology: the "Emergency Council" after the opening murder, the "Acting Cabinet" after a foreign murder.
   It carries a marker trait (`murder_mystery_emergency_council` or `murder_mystery_acting_cabinet`) with a small stability penalty and uses `GFX_portrait_039_emergency_council`, an institutional portrait that shows no individual.

The transaction verifies through the anchor helper that the replacement, not the victim, is the sitting ruler before it retires the victim.
No invented individual is created for a real government; the generated individual portrait previously used for every host is no longer referenced.
The opening host gate excludes countries in a civil war and countries carrying a stale anchor trait.

## Objective lifecycle

Ordinary phase actions start event-owned missions through `murder_mystery_decision_start_bound_objective`.
The actor retains its mission type, recipient country, original capital, objective state, selected country when relevant, starting public values, and terminal sector snapshot in country variables and arrays.
The binder captures its actual recipient in the regular `murder_mystery_objective_actor` event target, so a setup chain rooted in the original host can still bind an Assassin State objective to the Assassin State.
The regular target is needed only during setup and does not become a persistent shared selector.

The capital and quarter objectives retain the original capital's state identity.
Automatic capital relocation after a loss cannot satisfy those objectives.
Evidence transport and restored capital connections use `has_railway_connection` between the stored endpoints and require full control of both endpoint states.
Force and depot objectives require actual divisions, a supply hub, and the rail connection at the named state.
These checks establish logistical prerequisites but do not measure individual divisions' live supply percentages.
That remaining validation and implementation question stays unresolved.

The terminal mission copies only the countries already assigned to its selected sector from the bounded government registry.
Changing or losing the presentation selector cannot alter that snapshot.
Full mission success requires every snapshot country to capitulate, cease to exist, or become the actor's subject.
Partial success requires at least one such country outcome.
An empty snapshot provides neither full nor partial success.
Sector mission completion does not by itself resolve the entire World of Anarchy campaign.

Every objective checks `murder_mystery_objective_owner_is_valid` in cancellation and reward delivery.
Country loss, runtime resolution, or cleanup retires its receipt and prevents later mission rewards.
The country cleanup helper explicitly removes all thirty named objective missions without firing their complete or timeout effects.
Global cleanup visits the original host, the central movement, and the existing bounded cell and derivative registries.
It adds no periodic whole-world scan.

Government partial results improve Case Progress and reduce Network Reach while allowing enemy adaptation.
Assassin partial results expand Reach at a Cohesion cost.
Assassin failures reduce Reach and Cohesion, rather than increasing the movement's strength.
These objective outcomes do not add Chaos.

### Agency, movement and terminal objectives

A country runs one objective at a time, and the objective sets the phase-mission flag, so no other selectable mission can start while it runs.
New objectives are offered through `murder_mystery_decision_offer_objective`, which does nothing while an objective is already running; this keeps a later action from overwriting the running objective's context.
`murder_mystery_decision_bind_movement_objective` binds their targets, and `murder_mystery_objective_binding_is_valid` refuses to start an objective whose target could not be found.
Thresholds and outcome sizes live in `murder_mystery_objective_tuning` and `murder_mystery_objective_tuning_float`; durations in `murder_mystery_action_tuning`.

| Objective | Owner and start | Target | Success | Partial | Failure |
| --- | --- | --- | --- | --- | --- |
| Run the Agency Operation | Original host, after a successful Commit a Case Team or Audit Communications | Case Progress target, Evidence Integrity floor, Network Reach ceiling | Case Progress reaches the target with evidence intact; the host's national cell loses `murder_mystery_objective_tuning.agency_cell_maturity_loss` maturity (a registered foreign cell row would instead lose maturity and a stage) | Any Case Progress gained by the deadline | Network Reach passes the ceiling (the cell moved) or nothing gained |
| Contest the Supply Route | Central state, after Survive the Opening War while still at war with the host | A host supply-hub state bordering the movement | Full control of the state; host route security falls, the movement captures fuel; Capture the Case Archive follows | The state is held but still contested; the archive objective follows | The state is not taken |
| Capture the Case Archive | Central state, after Contest the Supply Route | The host capital if it borders the movement, otherwise a host border state | The state is taken; the host loses Case Progress and Evidence Integrity, the movement gains Reach | none | The state is not taken |
| Keep the Cell Supplied | Central state, after Supply the Selected Cell | The selected cell | The cell survives; it gains maturity and revolt readiness | The cell survives with its local case advanced; small maturity gain | The cell is destroyed |
| Grow the Cell Quietly | Central state, after Dispatch a Shadow Company | The selected cell's maturity target and exposure ceiling | Maturity target reached below the exposure ceiling; the cell sheds exposure | Some maturity gained | No growth, or the cell is lost |
| Prepare the Revolt Cluster | Central state, after Prepare a Territorial Revolt | The selected cell and a non-capital state of its government | Insurrection stage with full readiness; the cell is first in line for the next revolt | Half readiness | Less, or the cell is lost |
| Hold the Subjects Together | Central state, after Reconcile a Command Dispute, or opened by the pulse when Cohesion falls below `subject_loyalty_start_cohesion` | Every active derivative | No derivative leaves the subject settlement; Cohesion rises | none | A derivative leaves; Cohesion falls |
| Synchronize the Cells | Central state, after a successful high-value operation | Registered insurrection cells (counted by the pulse) | Enough insurrection cells; every insurrection cell gains readiness, Reach rises | At least one insurrection cell | None |
| Dismantle the Command Network | Central state, after Break the Command Spine | The current campaign target | Its capital held by the movement or a subject, or it surrendered | Part of its territory held | Nothing taken |
| Force a Capitulation | Central state, after World of Anarchy activates | The current campaign target | It capitulates, becomes a subject or is gone | Surrender progress above `capitulation_partial_surrender`; small Cohesion gain | Otherwise |
| Hold the Sector Capitals | Central state, after Complete the Terminal Sector | The sector snapshot | At least one sector capital held to the deadline | none | Every sector capital lost |
| Protect the Central Command | Central state, after Reconstitute the Campaign Council | Its original capital and a Cohesion floor | Both held; Cohesion rises | none | Capital lost or Cohesion below the floor |
| Protect the Successor Government | Central state, after Establish a Successor Administration | Its smallest active derivative | The derivative survives as a subject; its Cohesion rises | none | It capitulates, leaves or is destroyed |
| Reduce the Sector Governments | Central state, after selecting a second or third campaign sector | The sector snapshot | At least `reduce_governments_minimum` governments settled | At least one settled | None |

Terminal objectives add a conquer or protect AI strategy toward their target, so an AI center pursues them.
The pulse publishes `global.murder_mystery_insurrection_cell_count` and refreshes the central state's sector count while Reduce the Sector Governments runs.
The new missions reuse existing Event 039 decision art through `GFX_mission_039_murder_mystery_<objective>` sprites in `interface/039_murder_mystery_icons.gfx`.

## Movement pulse

The movement acts on its own through one hidden, self-rescheduling event, `chaosx.nr39.90`, that runs every `murder_mystery_pulse.interval_days` days on a single anchor country.
The anchor is the original host while it survives, then the central Assassin State, then the underground center, then the government that owns the case.
Every schedule records a due date; a pulse that fires before it was queued earlier and is ignored, so rescheduling on a new anchor after a country is lost never runs two pulse chains.
The pulse starts when the opening murder commits and stops when the runtime resolves or cleans up.

Every pulse, in order:

1. Reconciles the cell and derivative registries.
2. Classifies an overdue inheritance announcement.
3. Grows the host's national cell and Network Reach while the host's Case Progress is below the suppression thresholds, and matures every registered foreign cell by a base amount plus Network Reach divided by `murder_mystery_cell_growth.reach_divisor`.
   A cell's stage rises with its maturity up to a cap set by the current evolution: active before Evolution II, entrenched after it, insurrection after Evolution III.
   Insurrection cells build revolt readiness after Evolution IV.
4. After Evolution II, seeds one foreign cell when the seeding countdown expires, through one bounded route: a land border with the host, a land border with an existing cell, or an ally of the host.
   A country whose cell was destroyed can be chosen again once its `murder_mystery_cell.immunity_days` immunity has lapsed.
5. Runs a scheduled incident when the incident countdown expires.
6. Commits a ready evolution once its pacing delay has run out.
7. Checks whether the movement has been defeated everywhere.

### Scheduled incidents

The incident interval is `murder_mystery_incident.base_days` minus Network Reach and the highest cell maturity times their weights, minus a step per committed evolution, clamped between the minimum and maximum days.
The target is drawn from the surviving host and every registered cell country at stage active or higher that is not on its incident cooldown.
A role group (investigators, magistrates, cabinet officials, intelligence officers) that was struck stays off the list for `role_cooldown_days`.
Witness Safety and protected targets give a chance to stop the attack, which raises Case Progress and reports `chaosx.nr39.11`.
A successful attack records a generic office casualty (no named character is killed), costs stability, raises the movement's Reach and the cell's maturity, and reports `chaosx.nr39.9`.
Four host incidents while the investigation is compromised count as the murder sequence that can open Evolution III.

### Evolution pacing

When an evolution becomes ready, its countdown starts at the host's computed pacing days (base 90, shortened or lengthened by the existing pacing factors) and falls by the pulse interval on every pulse.
Losing readiness clears the countdown.
Evolution III is the territorial split: the pulse selects the split cluster only when every other Evolution III condition holds, and records the stage only after the Assassin State transfer and war commit; a failed split retries after `murder_mystery_cooldown.evolution_retry_days`.
No government decision escalates the movement against its own country.

## Starting forces

`common/scripted_effects/039_murder_mystery_forces_effects.txt` runs once per new movement country, before its war starts.

| Country | Technology | Templates | Divisions (per owned state, clamped) | Stockpiles |
| --- | --- | --- | --- | --- |
| Assassin State | Clandestine Combat Training, Compartmented Logistics, Urban and Rough-Terrain Infiltration | Assassin Cadres (4 Assassin Cadres, Saboteur Cell support), Movement Militia (6 infantry) | 1 cadre and 1 militia per state, 2 to 8 cadre and 2 to 10 militia | 3000 infantry equipment, 300 support equipment, 200 trucks, 10 trains, 5000 fuel |
| Derivative | Clandestine Combat Training, Infantry Weapons I | Assassin Cadres (3 Assassin Cadres), Movement Militia (4 infantry) | 1 cadre and 1 militia per state, 1 to 3 cadre and 1 to 4 militia | 1200 infantry equipment, 100 support equipment, 60 trucks, 3 trains, 1500 fuel |

Derivatives also receive two research slots, neutrality politics without elections, stability and war support from `murder_mystery_starting_forces_float`, political power, and the Cells Under Arms idea.
Shadow Companies, Silent Guards, Master Assassins and Mechanized Assassins stay locked until their technologies are researched or granted by focus.

The committed Assassin State loads `murder_mystery_assassin_focus_tree` explicitly in `murder_mystery_commit_assassin_state_transaction`, because `create_dynamic_country` picks a tree before the commit sets the flags that the tree's `country` block reads; a rolled-back candidate is annexed before the commit and never receives the tree.
The `country` block stays as a fallback for the same validated countries.

### Assassin technology line

The seven technologies in `common/technologies/039_murder_mystery_assassin_technologies.txt` form one branch at the bottom of the infantry folder, rooted in the `murder_mystery_clandestine_combat_training_tree` gridbox of `interface/countrytechtreeview.gui` (pixel origin 140, 1730, below the special forces branch).
`allow_branch` on the root hides the whole branch from every country that is not an Assassin State or derivative, and each technology's `allow` limits research to the same countries.

| Technology | Row, column | Reached from | Extra research gate | Unlocks |
| --- | --- | --- | --- | --- |
| Clandestine Combat Training | 0, 2 | root | none | Assassin Cadres, operations kits |
| Compartmented Logistics | 0, 4 | Clandestine Combat Training | none | cadre supply and defence |
| Urban and Rough-Terrain Infiltration | 0, 6 | Compartmented Logistics | none | Saboteur Cells |
| Shadow Operations Doctrine | 0, 8 | Urban and Rough-Terrain Infiltration | none | Shadow Companies |
| Protected Command Doctrine | 1, 8 | Urban and Rough-Terrain Infiltration | none | Silent Guard |
| Mechanized Infiltration | 0, 10 | Shadow Operations Doctrine | the pragmatic route's `murder_mystery_conventional_support_unlocked` | Mechanized Assassins |
| Master Cadre Command | 1, 10 | Protected Command Doctrine, also requires Shadow Operations Doctrine | Evolution V committed | Master Assassins |

Movement countries weight the line at 3, doubled at war, and focuses still grant the same technologies through `set_technology`.
Technology icons are the existing `GFX_murder_mystery_<technology>_medium` sprites.
Each new country adds conquer and antagonize AI strategies against the government it split from.
`common/ai_strategy/039_murder_mystery_ai_strategy.txt` keeps active movement countries building an army of roughly one third cadres and two thirds infantry, and `common/ai_templates/039_murder_mystery_ai_templates.txt` gives them an Assassin cadre target template; every other country has zero upgrade priority for that role.

## Foreign revolts

Derivatives come from registered cells at insurrection stage.
The Evolution IV reveal (`chaosx.nr39.33`) raises a revolt in the most revolt-ready insurrection cell whose government can lose a cluster, unless the central state already holds a selected cell; after that the pulse raises one revolt whenever an insurrection cell reaches `murder_mystery_revolt.readiness_threshold`.
A revolt takes a non-capital anchor state plus `cluster_extra_states` neighbouring states owned by the same government, and never leaves that government with fewer than `minimum_source_states` controlled states.
The new country becomes a subject of the central state, follows its route, receives its starting forces, declares war on the government it rose against, and announces itself with news `chaosx.news.4404`; the source cell row leaves the cell registry because the derivative registry now owns it.
If any postcondition fails, every moved state returns to its government and the empty carrier is retired.

## Country outcomes

`common/on_actions/039_murder_mystery_on_actions.txt` handles `on_capitulation` and `on_annex` only for countries with an Event 039 actor flag while the runtime is active.

| Outcome | Result |
| --- | --- |
| Assassin State capitulates or is annexed | Defeat receipt, Chaos decrease, objective cleanup; the winner absorbs the capitulated state the next day (`chaosx.nr39.64`); during World of Anarchy the terminal defeat resolves the campaign, otherwise the inheritance test begins |
| Derivative capitulates or is annexed | Its row leaves the registry, Chaos decreases, the winner absorbs it, and global resolution is checked |
| Host capitulates to or is annexed by the movement | The Assassin State gains Cohesion and Reach, its opening-war objective succeeds, Chaos increases, and both sides receive `chaosx.nr39.63` |
| Host annexed by anyone | Its runtime is cleaned up and the pulse moves to the next anchor |
| Host annexed before the movement ever held territory | The winner takes over the case; if a cell at stage 3 or higher survives, the network goes underground around its most mature cell and the winner receives `chaosx.nr39.25`, otherwise the movement ends at once and the winner receives `chaosx.nr39.62` |
| A cell country is annexed | Its cell row is retired |

## Inheritance and resolution

The inheritance test is announced to the government that owns the case with `chaosx.nr39.23` after `murder_mystery_inheritance.announcement_delay_days`; the pulse classifies it itself if the announcement is overdue.
The classification runs once:

1. If a territorial state ever existed and the territorial inheritance has not been used, the best active derivative becomes the new center.
   Ranking is owned states, then industry (capped), then Cohesion, over the bounded derivative registry.
   The heir takes the central flags and pointer, loads the Assassin focus tree (an heir already on that tree keeps its finished focuses, any other heir starts it fresh), suffers a Cohesion and Reach loss, and the other derivatives rebind to it when its Cohesion reaches `rebind_cohesion`; otherwise they detach as autonomous countries.
   Report: `chaosx.nr39.24`.
2. Otherwise, if a cell at stage 3 or higher survives, the network continues underground with no leader change, centered on its most mature cell.
   Report: `chaosx.nr39.25`.
3. Otherwise the movement ends.

The movement ends when its center (or heir) is gone, no derivative still fights for it, and no cell at stage 3 or higher survives; before any territorial state, the captured core or the annexation of the host, plus the same cell rule, ends it.
Ending retires the lower-stage remnant cells, applies the movement-ended Chaos reversal once, finalizes the runtime, and reports `chaosx.nr39.61` and `chaosx.nr39.62`; when no territorial state ever existed it reports `chaosx.nr39.20` after a capture, or only `chaosx.nr39.62` when the host fell first.
No inheritance step retires or creates a character.

## Decision costs

Every Event 039 decision and selectable mission names one cost family (`murder_mystery_cost_profile`) in its completion effect.
The family decides what the payer spends; its amounts live in `murder_mystery_cost` and `murder_mystery_cost_float` and feed the cost text, the affordability check in `available` and `custom_cost_trigger`, the debit in `murder_mystery_pay_action_cost`, and the refund when the action transaction rolls back.
Each family spends at most three resources, and every affordability check is inclusive.

| Family | Spends | Decisions |
| --- | --- | --- |
| Case authority | political power (plus the response profile surcharge), command power | Establish the Case Command, Commit a Case Team, Join the Evidence Exchange |
| Security detail | manpower, support equipment, command power | Secure the Government Quarter, Protect Witnesses, Choose a Protection Priority, Harden a Target Group |
| Forensic inquiry | support equipment, political power | Preserve the First Evidence, Audit Communications, Request the Original Case File |
| Route watch | trucks, manpower, command power | Trace Movement Logistics, Interdict a Known Route, Foreign Interception |
| Armed raid | command power, infantry equipment, manpower | Raid an Identified Cell, Dismantle the Local Cell, Silent Arrest, Coordinated Raids |
| Capture planning | command power, support equipment | Prepare the Final Operation |
| Public strain | political power (plus the surcharge), stability | Replace a Compromised Office, Baited Target |
| Brotherhood council | political power, command power | Reconcile a Command Dispute, Discipline an Unauthorized Cell |
| Cell supply | operations kits, infantry equipment, trucks | Supply the Selected Cell, Request Central Support |
| Field operation | operations kits, manpower, command power | Order a High-Value Operation, Dispatch a Shadow Company, Raise Local Assassin Cadres |
| Revolt preparation | operations kits, manpower, infantry equipment | Prepare a Territorial Revolt, Create a Derivative Administration, Secure the Revolt Capital, Seize a Depot or Rail Hub |
| Local administration | political power, manpower | Integrate Local Cells, Manage Captured Officials, Negotiate a Local Settlement |
| Terminal settlement | political power, command power | Complete the Terminal Command Settlement, Establish a Successor Administration, Reconstitute the Campaign Council |
| Terminal campaign | command power, operations kits, manpower | Activate World of Anarchy, Synchronize Uprisings, Select a Campaign Sector, Break the Command Spine |

Cell actions run their transaction on the central movement state while it can act in its final phase, and on the acting country otherwise; the `murder_mystery_cell_payer_can_pay_*` checks read the same condition, so the shown cost always belongs to the payer.
Operations kits are an Assassin-only cost and use the `GFX_murder_mystery_operations_kit_texticon` texticon (`gfx/texticons/039_murder_mystery/operations_kit_texticon.dds`, 24x24, downscaled from the kit equipment icon, registered in `interface/039_murder_mystery_icons.gfx`).
Shared amounts are published as `global.murder_mystery_cost_*` display variables; the case authority and public strain political power quotes are per country because they carry the response profile surcharge.
`ai_hint_pp_cost` uses file-scoped literals in the decisions file that mirror the political power of each family.

## Government cell raids

Raid an Identified Cell (host) and Dismantle the Local Cell (foreign government) pay the armed raid family.
A foreign government's case opens when a cell is registered in its country; after mapping the network it moves straight to breaking the cell.
A successful local raid dismantles the cell (immunity, Chaos decrease for the first few cells, report `chaosx.nr39.10`); a partial raid costs the cell maturity and one stage.

## Assassin Network scenario launch

The manual launch selects its host from the same weighted pool without the shared individual-crisis load cap, and High or Maximum intensity requires a host with more than `murder_mystery_scenario.split_minimum_host_states` controlled states.
The opening runs at once on that host through `murder_mystery_run_opening`, the same effect the event-pool opening uses, so the launch never waits on a delayed event that could be rejected.
The launch either commits and applies its intensity setup, or fails, leaves the runtime dormant and sets `murder_mystery_scenario_launch_failed`; the in-progress flag and stored intensity are always cleared.
Intensity setup commits evolutions in order, opens the Assassin State at High and Maximum before recording Evolution III and IV, seeds cells and raises Maximum-intensity revolts within attempt budgets of `murder_mystery_seeding.maximum_attempts` per requested cell or revolt.

## World of Anarchy in Event Details

World of Anarchy is registered in the shared world-end registry as scenario ID `world_end_scenario_id.world_of_anarchy` (16), owned by Event 39, public, enabled by default, and linked to super-event 112.
Its row appears in the Event Details world-end list beside the other terminal outcomes, and the shared toggle adds or removes ID 16 from `global.disabled_world_end_scenarios`.
`murder_mystery_world_branch_is_enabled` reads that toggle through `world_end_murder_mystery_world_of_anarchy_scenario_enabled` and the global `world_end_disabled` flag, so disabling the row blocks only the Evolution V world branch; the movement, its cells and its Assassin State keep running.
The row shows as active while `world_end_murder_mystery` is set.

## World of Anarchy war

Activation registers every ordinary government once (`murder_mystery_register_terminal_country`): it must exist, use normal civilian systems, own at least one state, and be neither special Chaos, nonhuman, exempt, nor on the movement's side (the central state, a derivative, or a subject of either or of a successor administration).
The registry holds up to `murder_mystery_terminal.maximum_registry_rows` rows, and each row is sorted into a sector by the distance from its capital to the central capital: the home front within 1500, the near sector within 4000, the distant sector beyond (file constants in `039_murder_mystery_runtime_triggers.txt`, because `distance_to` reads literals).
The central state starts with the home front selected.

Opening a sector (Synchronize the Uprisings for the home front, Open the Near Sector, Open the Distant Sector) runs one bounded war wave over that sector's rows (`murder_mystery_run_terminal_war_wave`).
A government already at war with the central state is only marked; an independent government, or a subject whose overlord is outside the campaign, receives `declare_war_on` with `annex_everything` from the central state, at most `wave_declaration_limit` per wave, after being expelled from a faction the central state leads.
A subject of an open target follows its overlord into the war.
The movement pulse repeats the wave for every active sector, so the remaining governments of an opened sector come under attack a few at a time.
No daily or weekly scan is added: the pulse and every hook iterate only the registry.
After each wave the largest government at war becomes the current campaign target (`murder_mystery_terminal_target`) that Break the Command Spine and the terminal objectives act on.

A registered government that capitulates while at war with the movement, or to a movement country, is flagged and queued; the pulse also queues any open row that is fully occupied while at war with the central state or that a peace made a movement subject.
The queue sends `chaosx.nr39.65` to the central state after `administration_delay_days`, with the government as the regular event target `murder_mystery_terminal_choice`; a choice that never arrives is offered again after `administration_retry_days`.
Establish a Successor Administration is a targeted decision over the registry for a defeated government that has no choice pending, and it sends the same choice for the settlement cost.
The three options run `murder_mystery_dismantle_terminal_target` once:

| Outcome | Favoured by | Result |
| --- | --- | --- |
| Subject administration | The Hidden Hand | The government leaves its faction and becomes a subject of the central state with the Successor Administration idea. |
| Cell territory | Cells Without Masters | A local derivative that rose against this government annexes it; otherwise a new autonomous derivative from the derivative registry takes every state (cores only where the old government held them) and absorbs it. A full derivative registry falls back to a subject administration. |
| Staged integration | The Necessary Mask | The capital and up to `strategic_state_limit` states with more than one civilian or military factory join the central state; the rest goes to the local derivative, stays a subject administration, or is annexed when nothing is left. |

The route's own outcome gives `route_outcome_cohesion` Brotherhood Cohesion and the others cost `off_route_outcome_cohesion`.
A government that stays a subject loses its ruler only through the existing safe successor (`murder_mystery_execute_foreign_leader_transaction`, which installs the Acting Cabinet without the world news or rally of a murder in a living state), and its cabinet loss is a generic office casualty; a ruler the safety rules protect stays in office and the row records the protection.
No outcome grants universal cores.

The row is settled (`victory_contribution`) only by that transaction or by the annexation hook when a movement country annexes the government (a conquest, recorded as staged integration).
Annexation by an ordinary government settles the row as absorbed (`victory_exempt`) and registers the annexing government if it was not yet a target, declaring war on it at once when its sector is open.
No decision writes a settled value.
`murder_mystery_evaluate_terminal_victory` passes only when every row is settled; a subject administration that has broken free reopens its row, and once every row is settled one bounded reconciliation registers any ordinary government created since activation, so victory waits for those as well.

Break the Command Spine needs the current campaign target at war with the central state and more than 20% of the way to surrender; on success it adds Command Spine Broken (`command_spine_disruption_days`), lowers the target's stability and war support, strikes its command staff as a generic office casualty and adds `command_spine_cohesion`, but it never settles the row.
Reconstitute the Campaign Council appears while Cohesion is below `council_cohesion_ceiling`, restores `council_cohesion_repair` Cohesion and adds Campaign Council Reconstituting for `council_vulnerability_days`.
Synchronize the Uprisings opens the home front the first time; afterwards it raises up to `uprising_wave_size` revolts from ready insurrection cells in the selected sector through the existing derivative path and continues that sector's war wave.

## Achievements

The eight achievements are registered in the Event 039 section of `common/achievements/chaos_redux_achievements.txt`.
Each `happened` block reads one receipt flag; `common/scripted_effects/039_murder_mystery_achievement_effects.txt` writes the receipt once from the criteria in `common/scripted_triggers/039_murder_mystery_achievement_triggers.txt`.
Every `possible` block is true at game start and reads only one-shot run-wide disqualifiers, because an achievement whose `possible` fails at game start can never be earned.
Icons are the existing normal, grey and not-eligible triplets in `gfx/achievements/039_murder_mystery_<id>.dds`; the achievement interface resolves them by filename, so no sprite is needed.
Names and descriptions use the `_NAME` and `_DESC` keys, and the requirement text uses `_tooltip`, in `localisation/english/039_murder_mystery_l_english.yml`.

| Achievement | Earned by | Receipt edge | Main conditions |
| --- | --- | --- | --- |
| No Second Victim | Original host, natural run | Permanent resolution, movement end | The host's own final operation captured the original murderer, and no later Event 39 office casualty or leader killing happened anywhere (`murder_mystery_later_murder_recorded`) |
| The Empty Chair Holds | Original host, natural run | Permanent resolution, movement end | No territorial split or Evolution III, verified successor installed at the opening and no later leader killing, no emergency repression, original capital controlled at resolution and never lost for more than `capital_grace_pulses` consecutive pulses, stability at least `empty_chair_stability` |
| A Net Without Knives | Original host, natural run | Movement end | Evolution II, five simultaneous foreign cells (`murder_mystery_five_foreign_cells_reached`), the core captured, no derivative ever created, no heir or underground inheritance, no mature cell or active derivative left |
| The Knife Breaks | Original host whose player stayed at the split | Movement end, terminal defeat | Natural run, the original player kept the host, the center defeated, no active derivative or mature cell, and either the host dealt the central defeat or completed `knife_breaks_minimum_objectives` case objectives after the split |
| No Masters Above Us | Center on Cells Without Masters | Pulse, route capstone focus | Survive Without a Chair, original host defeated, its original capital controlled, at least `minimum_decentralized_derivatives` viable self-governing derivatives |
| Necessary Hypocrisy | Center on The Necessary Mask | Pulse, route capstone focus | Return the Mask, the three pragmatic spirits, a Mechanized Assassin majority template with at least one fielded mechanized division, faction leader of the Veiled Compact with at least `minimum_pragmatic_derivatives` viable derivatives bound to it, Cohesion at least `necessary_hypocrisy_cohesion` |
| Every Chair Empty | Center or its heir | Terminal victory | World of Anarchy activated through the normal transaction and every registry row resolved |
| The Last Safe Cabinet | Player governments recorded at activation | Terminal defeat | Still independent and ordinary, the leader recorded at activation still rules, no Event 39 office casualty after activation, at least `minimum_terminal_contribution` case objectives completed during the war |

Scenario launches disqualify the four investigation achievements; the route and terminal achievements stay open because the scenario setup never grants their conditions.
The Last Safe Cabinet marks the sitting ruler at activation with the character flag `murder_mystery_achievement_cabinet_leader`, resolved through the existing anchor trait that is removed at once.
A derivative counts as viable when its registry row is active, its starting forces package exists, it has not capitulated, and it owns at least `murder_mystery_inheritance.minimum_heir_states` states.

## Intelligence cluster

Event 39 is the optional Medium member of the Intelligence cluster (`event_cluster_id.intelligence`, runtime ID 20), whose required Low baseline is Event 52.
The cluster is one-time and unlocks at Chaos level 1.
Members fire through the normal event dispatcher, so Event 39 keeps its weighted host selection and its pool unavailability reasons, and a refused Event 39 is recorded as a skipped member.
The workbook still lists the cluster as ID 8; the correction is queued in `docs/plans/039_murder_mystery_plans/catalog_changes_pending.md`.

## Default event queue

Event 39 is a fire-once event in the automatic event pool and is listed in `event_log_event_is_reworked_default_enabled` (`common/scripted_triggers/chaosx_settings_triggers.txt`), so a new campaign starts with it enabled (agent decision D20).
The Events Log toggle can still disable it for a campaign.

## Runtime ownership and presentation

Timed flags (the action, incident, role and immunity cooldowns, the aftermath window and the three super-event flags) receive their durations and the super-event slot as integers through `meta_effect`, because a timed flag reads only literals; the helpers are `murder_mystery_start_action_cooldown`, `murder_mystery_start_incident_cooldown`, `murder_mystery_start_cell_immunity`, `murder_mystery_start_aftermath_visibility` and `murder_mystery_show_super_event` in the runtime effects, and `murder_mystery_start_incident_role_cooldown` in the lifecycle effects.

| Surface | Source |
| --- | --- |
| Phase actions and thirty objective missions | `common/decisions/039_murder_mystery_decisions.txt` |
| Recipient binding, snapshots, outcomes and removal | `common/scripted_effects/039_murder_mystery_decision_effects.txt` |
| Objective receipt, full control, rail and sector predicates | `common/scripted_triggers/039_murder_mystery_objective_triggers.txt` |
| Country loss and split integration | `common/scripted_effects/039_murder_mystery_integration_effects.txt` |
| Shared Event 039 cleanup | `common/scripted_effects/039_murder_mystery_runtime_effects.txt` |
| Achievement receipts and criteria | `common/scripted_effects/039_murder_mystery_achievement_effects.txt`, `common/scripted_triggers/039_murder_mystery_achievement_triggers.txt` |
| Movement pulse, incidents, country outcomes, inheritance | `common/scripted_effects/039_murder_mystery_lifecycle_effects.txt` |
| Lifecycle classifiers | `common/scripted_triggers/039_murder_mystery_lifecycle_triggers.txt` |
| Pulse, incident, growth, seeding, defeat and inheritance tuning | `common/script_constants/039_murder_mystery_lifecycle_constants.txt` |
| Capitulation and annexation hooks | `common/on_actions/039_murder_mystery_on_actions.txt` |
| Incident office names | `common/scripted_localisation/039_murder_mystery_scripted_localisation.txt` |
| Objective types, durations and tuning | `common/script_constants/039_murder_mystery_constants.txt` |
| Mission titles, named states and requirements | `localisation/english/039_murder_mystery_l_english.yml` |
| Mission sprites | `interface/039_murder_mystery_icons.gfx` |

The original sixteen objective sprites use `GFX_mission_039_murder_mystery_<objective>` and their own runtime textures under `gfx/interface/decisions/039_murder_mystery/`; the fourteen later objectives reuse existing decision textures from the same folder under the same sprite naming.
The objective names are `protect_witness_transfer`, `hold_government_quarter`, `secure_evidence_convoy`, `guard_named_route`, `place_supplied_divisions`, `keep_capital_connected`, `capture_safehouse_chain`, `preserve_target_attack_window`, `prevent_revolt_preparation`, `secure_depots_rail_hubs`, `dismantle_local_recruitment`, `protect_local_government`, `intercept_support_shipment`, `hold_parent_capital_revolt_border`, `survive_opening_war`, and `complete_terminal_sector`.
The current repair reuses their existing bespoke textures and does not create or replace image files.
The asset audit remains governed by the full per-asset review and consumer crosswalk in `docs/assets/039_murder_mystery/visual_asset_audit.md`.

## Remaining acceptance work

The mission family count is not proof of complete objective coverage.
Every Part 8 mission family now has an objective, but foreign shipment receipts, the witness state-to-state transfer, recruitment network outcomes and protected-character survival still use the simplified checks described above.
The agency operation, movement and terminal objectives need live confirmation of their binding, timers and outcomes.
Route rewards, country viability, native technology and focus evidence, probability comparisons, both Meshy model packages and actions, licensed audio, workbook reconciliation, and the full Part 18 matrix remain separate completion gates.
No runtime or persistence claim in this document substitutes for observed game state.

## Further development

Complete the accepted objective families using operation-specific receipts, named evidence locations, guarded transport, and actual cell or administration transactions.
Any proposal beyond the accepted package should receive its own recorded acceptance basis before implementation.
