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

## Murdered rulers and their replacements

The opening murder and a foreign cell's high-value murder both target only the sitting ruler, resolved through the synchronous anchor-trait helper `murder_mystery_capture_current_ruling_character`; an unresolved or ambiguous ruler fails the transaction closed, so an opposition party leader is never killed in the ruler's place.
The replacement takes office before the victim is retired, through `murder_mystery_install_emergency_successor`:

1. A curated native successor row applies first. The only row is Britain: a murdered `ENG_stanley_baldwin` is succeeded by `ENG_neville_chamberlain`, recruited and promoted in the ruling democratic party, with his vanilla portrait.
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
The country cleanup helper explicitly removes all sixteen named objective missions without firing their complete or timeout effects.
Global cleanup visits the original host, the central movement, and the existing bounded cell and derivative registries.
It adds no periodic whole-world scan.

Government partial results improve Case Progress and reduce Network Reach while allowing enemy adaptation.
Assassin partial results expand Reach at a Cohesion cost.
Assassin failures reduce Reach and Cohesion, rather than increasing the movement's strength.
These objective outcomes do not add Chaos.

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
| A cell country is annexed | Its cell row is retired |

## Inheritance and resolution

The inheritance test is announced to the government that owns the case with `chaosx.nr39.23` after `murder_mystery_inheritance.announcement_delay_days`; the pulse classifies it itself if the announcement is overdue.
The classification runs once:

1. If a territorial state ever existed and the territorial inheritance has not been used, the best active derivative becomes the new center.
   Ranking is owned states, then industry (capped), then Cohesion, over the bounded derivative registry.
   The heir takes the central flags and pointer, suffers a Cohesion and Reach loss, and the other derivatives rebind to it when its Cohesion reaches `rebind_cohesion`; otherwise they detach as autonomous countries.
   Report: `chaosx.nr39.24`.
2. Otherwise, if a cell at stage 3 or higher survives, the network continues underground with no leader change, centered on its most mature cell.
   Report: `chaosx.nr39.25`.
3. Otherwise the movement ends.

The movement ends when its center (or heir) is gone, no derivative still fights for it, and no cell at stage 3 or higher survives; before any territorial state, the captured core plus the same cell rule ends it.
Ending retires the lower-stage remnant cells, applies the movement-ended Chaos reversal once, finalizes the runtime, and reports `chaosx.nr39.61` and `chaosx.nr39.62` (or `chaosx.nr39.20` when no territorial state ever existed).
No inheritance step retires or creates a character.

## Government cell raids

Raid an Identified Cell (host) and Dismantle the Local Cell (foreign government) cost command power, infantry equipment and manpower from `murder_mystery_action_cost.government_raid_*`, shown as the decision cost.
Operations kits remain an Assassin-only cost.
A foreign government's case opens when a cell is registered in its country; after mapping the network it moves straight to breaking the cell.
A successful local raid dismantles the cell (immunity, Chaos decrease for the first few cells, report `chaosx.nr39.10`); a partial raid costs the cell maturity and one stage.

## Assassin Network scenario launch

The manual launch selects its host from the same weighted pool without the shared individual-crisis load cap, and High or Maximum intensity requires a host with more than `murder_mystery_scenario.split_minimum_host_states` controlled states.
The opening runs at once on that host through `murder_mystery_run_opening`, the same effect the event-pool opening uses, so the launch never waits on a delayed event that could be rejected.
The launch either commits and applies its intensity setup, or fails, leaves the runtime dormant and sets `murder_mystery_scenario_launch_failed`; the in-progress flag and stored intensity are always cleared.
Intensity setup commits evolutions in order, opens the Assassin State at High and Maximum before recording Evolution III and IV, seeds cells and raises Maximum-intensity revolts within attempt budgets of `murder_mystery_seeding.maximum_attempts` per requested cell or revolt.

## Runtime ownership and presentation

| Surface | Source |
| --- | --- |
| Phase actions and sixteen objective missions | `common/decisions/039_murder_mystery_decisions.txt` |
| Recipient binding, snapshots, outcomes and removal | `common/scripted_effects/039_murder_mystery_decision_effects.txt` |
| Objective receipt, full control, rail and sector predicates | `common/scripted_triggers/039_murder_mystery_objective_triggers.txt` |
| Country loss and split integration | `common/scripted_effects/039_murder_mystery_integration_effects.txt` |
| Shared Event 039 cleanup | `common/scripted_effects/039_murder_mystery_runtime_effects.txt` |
| Movement pulse, incidents, country outcomes, inheritance | `common/scripted_effects/039_murder_mystery_lifecycle_effects.txt` |
| Lifecycle classifiers | `common/scripted_triggers/039_murder_mystery_lifecycle_triggers.txt` |
| Pulse, incident, growth, seeding, defeat and inheritance tuning | `common/script_constants/039_murder_mystery_lifecycle_constants.txt` |
| Capitulation and annexation hooks | `common/on_actions/039_murder_mystery_on_actions.txt` |
| Incident office names | `common/scripted_localisation/039_murder_mystery_scripted_localisation.txt` |
| Objective types, durations and tuning | `common/script_constants/039_murder_mystery_constants.txt` |
| Mission titles, named states and requirements | `localisation/english/039_murder_mystery_l_english.yml` |
| Mission sprites | `interface/039_murder_mystery_icons.gfx` |

The sixteen objective sprites use `GFX_mission_039_murder_mystery_<objective>` and runtime textures under `gfx/interface/decisions/039_murder_mystery/`.
The objective names are `protect_witness_transfer`, `hold_government_quarter`, `secure_evidence_convoy`, `guard_named_route`, `place_supplied_divisions`, `keep_capital_connected`, `capture_safehouse_chain`, `preserve_target_attack_window`, `prevent_revolt_preparation`, `secure_depots_rail_hubs`, `dismantle_local_recruitment`, `protect_local_government`, `intercept_support_shipment`, `hold_parent_capital_revolt_border`, `survive_opening_war`, and `complete_terminal_sector`.
The current repair reuses their existing bespoke textures and does not create or replace image files.
The asset audit remains governed by the full per-asset review and consumer crosswalk in `docs/assets/039_murder_mystery/visual_asset_audit.md`.

## Remaining acceptance work

The mission family count is not proof of complete objective coverage.
The agency operation, foreign shipment receipts, witness state-to-state transfer, recruitment network outcomes, protected-character survival, derivative support, subject obedience, and all six terminal mandate families still require comparison against their accepted gameplay requirements.
Route rewards, country viability, native technology and focus evidence, probability comparisons, both Meshy model packages and actions, licensed audio, workbook reconciliation, and the full Part 18 matrix remain separate completion gates.
No runtime or persistence claim in this document substitutes for observed game state.

## Further development

Complete the accepted objective families using operation-specific receipts, named evidence locations, guarded transport, and actual cell or administration transactions.
Any proposal beyond the accepted package should receive its own recorded acceptance basis before implementation.
