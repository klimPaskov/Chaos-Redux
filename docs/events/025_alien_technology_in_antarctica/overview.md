# Event 025 Alien Technology in Antarctica

## Purpose

Implementation status: the 2026-10-04 completion pass implemented every gameplay, presentation, AI and asset item of the accepted package, and Event 25 is enabled by default in new campaigns (`event_log_event_is_reworked_default_enabled`).
Live campaign, multiplayer and save/reload behaviour and the MCP probability baseline remain open; the source tests described below cover specific transactions only.

Event 025 is a Calm World Major event with entry event chaosx.nr25.1 and one opening super-event. Human-controlled countries receive the same entry offer, while the bounded AI roster is selected after human entrants and accepts only the documented active Kruger State exception.

The expedition race is a country-scoped competition for alien-derived systems buried beneath Antarctic ice. Player-facing text describes alien-derived systems, survey evidence, and recovered fragments and never attributes the technology to Kruger.

## Runtime flow

The hidden entry event initializes one global race, six sector records, the persistent participant array, the fragment-owner registry, the same-day candidate fields, and the opening super-event audio and art.

The entry window sends one event to each human-controlled country and then closes once, through whichever controller event or expedition pulse reaches the stored close date first.
An expedition that goes 720 days (`chaosx_nr25_stall.phase_stall_days`) without entering a new phase or opening an objective or final recovery attempt, and has nothing running, is recalled with its verified evidence (`chaosx.nr25.89`), and the race closes once no expedition remains.

The controller registers human entrants first and fills only remaining bounded AI slots from eligible AI majors. The participant array is stored once and each participant receives its own country-scoped pulse event.

The phase sequence covers entry, mobilisation, crossing, outpost, survey, final recovery, and analysis settlement.
Human and AI decisions dispatch through the same action helpers, with phase timing, reserve behavior, and complete cost-budget review still required.

The recurring pulse is scheduled only for registered participants. It is not an on_daily, on_weekly, or on_monthly whole-world scan.

A valid final recovery submits one candidate into a same-day window. The deterministic order is higher survey evidence, higher logistics readiness, higher outpost security, lower exposure risk, earlier final-readiness date, and lower stable participant entry order. A later day cannot displace an earlier candidate.

The winner settlement calls the Event 016 external owner API through the Event 025/Event 036 ledger.
The reward order is a valid missing base family, then a compatible upgrade, then Alien Systems Integration when both pools are exhausted.
When the winner already holds an Event 036 recovery, the API excludes only the overlapping alien arms family while another base family remains.
Every result is mapped to one broad public field (flight control, propulsion and weapons; computation and autonomous machinery; spatial manipulation; temporal instrumentation; biological synthesis; or integrated alien systems), and the winner report names the kind of result and its field.

Losing countries receive only verified survey notes and exclusive fragment records. The loser path has no technology grant, and the loser report names the recovering country and the expedition's fragment or survey tier.

## Gateways and route burden

Four gateway groups map to live staging states in `chaosx_nr25_gateway_state` (ids never shown to players): Cape Horn (Tierra del Fuego 953, Magallanes 507, the Falklands 299), Cape Town (the Cape 681, Natal 719), Tasman (Tasmania 518, Victoria 517) and Ross Sea (Canterbury 723, Otago 1081).
`chaosx_nr25_refresh_gateway_bands` rates each group for one expedition by reading only those nine states and their controllers: direct when the expedition controls a port, allied when the port holder is a faction partner, a subject, its overlord or has an opinion of the expedition above 50, long ocean otherwise, and chartered for an expedition on chartered passage. A port held by a country at war with the expedition offers nothing, and a group whose ports are all held by enemies is closed.
The bands are refreshed at registration, on every phase change, on each participant pulse and at the moment a gateway is ordered; each gateway decision also checks live that the port holder of its best band is not at war with the expedition.
The band (`chaosx_nr25_gateway` constants) sets the gateway cost (direct 8 convoys, 100 fuel, 75 support equipment; allied 12 convoys, 150 fuel, 15 political power; long ocean 18 convoys, 250 fuel, 125 support equipment; chartered 30 political power, 150 fuel, 100 support equipment), the reach-the-gateway objective's length (90, 120, 150 and 150 days, with the native mission timer moved to match) and the Logistics Readiness each pulse costs on that route (1, 2, 3 and 3; 4 on an improvised landing or a cut route; 2 before any gateway).
Gateway cost rows, their tooltips and the board cards show each route's band and terms, and the board's route row shows the route and its band.
If every port of the chosen group falls to countries at war with the expedition, the pulse cuts the route (`chaosx.nr25.13`): readiness falls by 8, the route counts as one collapse for AI withdrawal, and the crossing, outpost and supply-route objectives cannot complete until the expedition prepares an alternate landing (an improvised route) or takes Charter Emergency Passage (40 political power, 100 fuel, a chartered route).
A failed reach-the-gateway objective also leaves an improvised route that the emergency charter can replace.
The AI adds 30 to a gateway with a direct band and 15 to an allied one, so it takes the best open route.

## Field hazards, rare incidents and the solo pace

Each expedition's own pulse calls `chaosx_nr25_run_field_events` (`common/scripted_effects/025_alien_technology_in_antarctica_field_effects.txt`); nothing scans the world and nothing depends on an evolution.
Once the expedition has a camp on the ice, the pulse rolls at most one field hazard. The chance is the MTTH entry `chaosx_nr25_hazard_chance`: 12% a pulse, +6 at Exposure Risk 50 and +8 more at 80, times 0.85 for each of the forward depot, radio net and polar crew, 0.75 at Logistics Readiness 60 or more, 1.3 below 20, 0.8 with a logistics depot or fortified camp emphasis, 1.25 for a solo expedition, capped at 40%.
The draw picks one of seven hazards, each weighted 10, or 4 when its own preparation was made: pack ice (escorted convoys or a direct route), whiteout (polar crew), crevasse field (aerial route survey), radio loss (radio net), engine failure (forward depot), lost sledges and vehicles (logistics depot or traverse camp emphasis) and sickness (crew rotation).
Consequences are bounded constants in `chaosx_nr25_hazard`: progress, readiness, exposure, intelligence, national fuel, and for crevasses and sickness one crew and four recorded deaths. A prepared hazard does half the damage and kills no one. Each hazard has its own report (`chaosx.nr25.301` to `.307`) with the losses and the preparation that softens it.
When no hazard struck, a 5% roll offers one of eight rare incidents the expedition has not met, each at most once (`chaosx.nr25.311` to `.318`): an abandoned camp, a rival's call for help (a random rival on the ice, which can gain readiness and a rescue opinion), a meteorite mistaken for wreckage, a clear weather window, a neutral ship (which can turn a cut or improvised route into a chartered one), a wrecked survey aircraft, a scientists' dispute and a recovered fragment reacting to current. Each offers two or three options with real trade-offs and AI chances; none hints at an evolution.
A solo expedition (one active participant) gains 1 Exposure Risk each pulse on the ice and loses 1 Expedition Progress each pulse in the survey and final phases, and meets hazards 25% more often.

## Reports and news

Every state change reaches only the affected country, once per change: the departure (`chaosx.nr25.10`), a failed gateway (`.12`), the first camp (`.20`), a lost or restored camp (`.21`, `.22`), a probable or confirmed site (`.30`, `.31`), a discovered false lead (`.32`), a recovered or lost fragment (`.40`, `.41`), a rescue for both countries (`.50`, `.51`), sabotage (`.60` unidentified, `.61` identified), an armed clash for its target (`.165`), and the end of an evacuation, with its dead when it collapses (`.14`).
Expedition deaths enter the shared Deaths ledger under the dedicated `antarctic_expedition` reason, on the military side and in the military country bucket, in the casualty bands of `chaosx_nr25_casualty`: a field accident costs 12 lives, a forced shutdown incident 6, a seized camp 30 and a collapsed evacuation 45.
A human-controlled actual nonhuman country or special chaos country reads entry, mobilisation and casualty text written for its own kind of expedition, selected by the shared `is_actual_nonhuman_country` and `is_special_chaos_country` classifiers; nonhuman wording takes precedence.
A sabotage victim learns the acting country only when a prepared countermeasure catches the operation or its intelligence reaches 20; only then does it gain the suspicion opinion, and undetected false coordinates stay silent until the expedition discovers them.
Public news fires once per milestone: the first camp or verified fragment (`.90`), the first armed clash (`.91`), the first accident of an open alien programme (`.92`), and each exposed concealed programme (`.93`).
The dispatch helpers live in `common/scripted_effects/025_alien_technology_in_antarctica_report_effects.txt`.

## Expedition Board

The event-owned scripted GUI is nr25_expedition_board_window and is attached through chaosx_nr25_expedition_board_scripted_gui.

The main value column contains exactly Expedition Progress, Logistics Readiness, and Exposure Risk. When Evolution V is active for the current holder, the third value is replaced by Alien Dependence without adding a fourth value.

Route, outpost security, survey evidence, crew, intelligence, wreck condition, fragment count, rival evidence, and cooldown state are supporting text, icons, action status, or hidden state.

The board contains a phase header, deadline control, history and details controls, six Antarctic sector click regions, state emblems, rival cards, and a phase action tray capped at five primary action slots.

The source layout uses a 1024x640 board canvas and a four-frame 384x58 sector-hitbox atlas.
The board root sits at a fixed offset from the screen centre, so it fits whole at 1920x1080, 1600x900 and 1366x768.
The status column stacks two compact cards and one tall card, drawn as cornered tiles of one panel texture; the tall card also carries the route, outpost and target rows.
Each sector state emblem reads its frame from the viewer's `chaosx_nr25_sector_N_frame` variable, which `chaosx_nr25_refresh_sector_frames` maps from the survey state (`chaosx_nr25_sector_frame` constants), and each sector has its own selection highlight.
Rival cards show the rival's flag and name with the public card text.
Each action card shows a short board label and, below it, the cost while the action can be taken or the blocking status otherwise; the tooltip repeats the full name, effect, cost and status, and the confirmation window keeps the full name and one-line cost.
MCP inspect and render evidence for the board, including the before and after scenarios, is recorded in `docs/assets/025_alien_technology_in_antarctica/visual_asset_audit.md`; hover, pressed and disabled states were not rendered.

The board uses participant-country scope and opt-in rival visibility flags so multiplayer players do not see another country’s hidden exact resources or hidden action state.

## Costs and action limits

The resource model includes convoys, fuel, support equipment, political power, civilian industry commitments, crew, scientific capacity, access, and time.
The accepted maximum is four spendable cost types per action, including committed industry.
Authorization commits convoys, fuel, support equipment, and civilian industry, with three upfront resource entries and the industrial duration in its cost tooltip.
Authorization uses inclusive resource predicates shared by its three cost-display components.
A human country without owned convoys, including a landlocked one, can enter by chartered passage: political power, more fuel, more support equipment and the civilian commitment replace convoys.
Every later shipping cost of a chartered expedition is paid in political power, and its organising and gateway objectives run longer.
Either entry warns when the civilian base or fuel reserve is thin, and such an entry starts with lower Logistics Readiness.

The Antarctic Expedition Board category mirrors the board's action tray and never lists more than five orders at once: entry (up to four), mobilisation (four), crossing (the three gateways), outpost (the outpost plus the alternate landing and convoy escort only while their situation holds), survey (three surveys, rival reconnaissance, and fragment recovery giving way to fragment analysis once a fragment is held) and final recovery (five approaches).
Outpost upkeep (reinforce, rotate crews, emergency shelter while the emergency lasts) sits in the Antarctic Outpost category with the outpost priorities, which hide the current priority and are listed only in the outpost and survey phases.
The Rival Operations category holds the five hostile operations and the countermeasure; a human sees operations only against the rival selected on the Expedition Board, and the category description asks for a selection when none is made, while the AI weighs every valid rival.
Evolution I, II and IV responses are listed once the expedition has a camp on the ice and Evolution III responses once it sails; every race-time response, the outpost, rival and safety categories disappear when the race resolves or the expedition leaves it.

Rival actions require a selected valid participant target, one-use or cooldown cleanup, evidence state, counterplay, AI weights, and partial outcomes. Sabotage applies a partial result when the target has insufficient evidence or countermeasures, and the target can answer through the bounded countermeasure path.
The hostile operations and the data exchange are targeted decisions: the actor's own cooldown gates the decision, and `target_trigger` checks the target through FROM (live participant, received-operation cooldown clear, one exchange per partner).

## AI behaviour

The AI keeps two reserve levels.
Optional spending keeps the roster-entry reserves (`chaosx_nr25_ai_keeps_reserve`: political power, fuel, support equipment and, on its own shipping, convoys).
Phase-gate actions (authorisation, the gateways, the outpost, the survey actions while the survey gate is open and the five final approaches), survey actions that would reopen the site-confirmation objective, and the depot and polar-crew actions while Logistics Readiness is below the organising threshold use the smaller progress reserve (`chaosx_nr25_ai_keeps_progress_reserve`).
That reserve is the core floor in `chaosx_nr25_ai_floor` (higher at war) plus the cost of the current phase's gate, so the AI keeps the core floor after paying; mobilisation saves for the coming gateway.
`chaosx_nr25_refresh_ai_progress_floor` stores the floor on entry, on every phase change and on each participant pulse.
Restoring the outpost, crew rotation and shelter have no reserve check so the AI can always recover.
Withdrawal has no weight unless a spec 009 condition holds (`chaosx_nr25_ai_should_withdraw`): the route has collapsed twice (a failed gateway or supply-route objective counts once each), readiness has stayed below the objective failure floor for five pulses in a row, the expedition has gone 360 days without a new phase or objective while unable to pay for its next phase, its homeland is close to surrender, or a rival already works the wreck while it is still off the survey ground with nothing recovered.
It never withdraws while holding major fragments, in or ready for the final recovery, or while gambling on the technology in a losing war.
Hostile operations and armed Evolution III actions prefer rivals ahead in the race, avoid rivals with a countermeasure ready, lean towards a rival caught operating against the actor, and never repeat the last operation back to back; no weight reads whether the target is a player.
Outpost reconfiguration happens only when the situation calls for that emphasis, and the Evolution V policies favour containment for stable or accident-hit programmes, risky integration only for countries losing a war or collapsing, and destruction only as a last resort.
Evolution I, II and IV responses follow spec 009's tendencies through posture triggers that read only the expedition's own state: a scientific expedition (Scientific Capacity 3 or more) listens remotely, maps the survivor's path and studies the debris fields; an aggressive one (at war or fascist) follows the signal; a risk-averse one (Exposure Risk 60 or more) shields its instruments and avoids replying; a weak one (Logistics Readiness below 30) avoids contact and never attempts a capture; a desperate or militarised one captures or guards; a leading expedition (no rival in a later phase) leaves the unstable core alone to press for it; a trailing one cuts, maps and distributes fragments and recovers them; a capable expedition stabilises a failing wreck.
Factors live in the `chaosx_nr25_ai` constants; agent decision D19 in the plans folder lists the source-level scenario reads and the blocked MCP probability routes.

## Evolutions

The five independently enabled evolutions are Active Signal, Something Survived, Militarised Antarctica, The Wreck Is Breaking Apart, and The Technology Changes Its Users.

Each evolution has a separate Chaos gate and MTTH source.
Delayed callbacks and recurring pulse hazards read their own enable/disable setting.
An evolution that is enabled and already past its Chaos gate when Event 25 fires shapes the opening (agent decision D15); a disabled evolution changes nothing, including its board overlay and AI weights.

Militarised Antarctica changes the expedition threat and diplomacy state without forcing a global war.

Every evolution in force keeps its own response decisions while its hazard lasts, so a later evolution, or an opening that starts several at once, never removes the answers to an earlier one.
A disabled evolution offers no responses.

An evolution whose own setting is enabled and whose Chaos gate is already met when Event 25 fires shapes the opening, and the entry and mobilisation reports describe it.
Active Signal starts with the signal already answering, Something Survived with tracks and a missing survey party, Militarised Antarctica with escorted AI expeditions that fortify their first camp as a security zone, and The Wreck Is Breaking Apart with an unstable hull and open fragment fields.
These four begin at once and log once; The Technology Changes Its Users stays latent, raising every crew's starting Exposure Risk and starting their Dependence as soon as it activates during the race.
Every baseline phase remains.

### Active Signal (Evolution I)

Signal Intensity is one global value, `global.chaosx_nr25_signal_intensity` (0 to 100), in `025_alien_technology_in_antarctica_signal_effects.txt` with its tuning in `025_alien_technology_in_antarctica_signal_constants.txt`.
It starts at 10 when the evolution activates during the race and at 20 when the race opens with it, and the first expedition pulse of every pulse period raises it by 3 for the whole race.
Its band (faint, steady from 25, strong from 50, violent from 75) appears in the Expedition Board's Exposure Risk tooltip and in every signal response tooltip.

Each expedition with a camp on the ice rolls a strong pulse on its own pulse.
The chance is the MTTH entry `chaosx_nr25_strong_pulse_chance` (10% at full intensity, scaled by the current intensity), multiplied by 0.5 after Shield the Instruments, 0.6 after Listen from a Distance and 0.75 while the radio net works, and by 1.25 for a signals station outpost; it is zero while the evolution is not in force.
A strong pulse draws one of five consequences with equal weight: burned-out radios (readiness and intelligence loss, and the radio net no longer covers radio failures for 60 days), a drained camp (readiness), injured crews (one crew and the Antarctic expedition deaths band), corrupted survey records (survey evidence, drawn only while the expedition holds some), or a revealed position (Exposure Risk, every other camp on the ice gains intelligence, the concealed departure is lost, and AI rival operations favour the revealed expedition for 45 days).
Shielded instruments halve the damage and remote listening cuts it to three quarters; either keeps the crews out of harm.
Each consequence has its own report (`chaosx.nr25.321` to `.325`), and the pulse discharges 15 intensity.

The responses read the signal: following the carrier wave adds survey evidence that grows with intensity and raises the signal by 2; broadcasting raises it by 8 and is then either answered by a strong pulse (25% plus half the intensity) or clears the first unexplored sector other than the hidden core from the expedition's charts (`chaosx.nr25.327`); jamming lowers the signal by 6, costs the jammer 6 Logistics Readiness, and for 60 days halves the signal response gains of the rival selected on the board (or otherwise the rival with the most progress), which learns who did it when its intelligence reaches the attribution threshold (`chaosx.nr25.326`).
AI tendencies follow spec 009: scientific expeditions listen remotely, more so on a strong signal; aggressive ones follow the wave; any unshielded camp shields once the signal is strong; jamming rises when a rival is in its final recovery, most for an aggressive expedition; weak logistics avoid following and broadcasting into a strong signal, and nobody broadcasts into a violent one.

Evolution V has contain, destroy, transfer, conceal, and integrate decision surfaces.
They follow physical custody: a country sees them while it holds the recovered core, a fragment, or an Event 036 recovery, and loses them once the material has left.

### Material holders and the Evolution V aftermath

Countries that hold recovered material join the bounded holder registry `global.chaosx_nr25_holders` at settlement, on a custody transfer, or when an Event 036 recovery follows the race.
Each holder runs its own monthly watch pulse, `chaosx.nr25.281`; nothing iterates the world.
After the race the watch checks the Evolution V setting, Chaos gate and MTTH, so the evolution can begin after the recovery, and it re-arms an opening that could not be delivered.
Once Evolution V is in force, every holder outside a live race opens its aftermath: Alien Dependence rises while the material is held (faster under integration or concealment, slower under containment) and falls once it has left.
Above the accident threshold a holder suffers one reported accident per cooldown (`chaosx.nr25.225`), with a shutdown, run-on, or, under concealment, cover-up choice.
Six observed-behaviour incidents (`chaosx.nr25.231` to `.236`) appear with a chance that grows with Dependence; each offers a costly correction or a useful concession that deepens Dependence.
The holder drifts towards one of five institutional states, Contained Exotic Technology, Independent Human Adaptation, Integrated Alien Systems, Alien Systems Reliance, or Autonomous Research Network, and a state settles into a national spirit after 180 days in its band (`chaosx.nr25.240`).
Alien Dependence is the unsettled stage of the same lifecycle, and a later policy or Dependence change can move the country to another state.
Disabling Evolution V in the settings stops the pulse effects and hides the policy decisions.

### Custody transfer

The transfer decision targets a country from the holder's candidate list: registered expeditions, other holders, and the holder's allies, excluding countries at war with it.
The chosen country receives an offer (`chaosx.nr25.250`); AI accepts more readily inside the same faction or with good relations.
On acceptance the ledger moves the core and fragments exclusively, then the holder pays the shipping, its Dependence falls, and a concealed programme is exposed.
The recipient joins the holder watch, opens its own aftermath with at least the transfer Dependence floor, gains the artifact decisions, trusts the giver, and is distrusted by other expeditions and holders.
Learned technology and the historical winner record stay with the original owner.
A lapsed, refused or invalid offer changes nothing and charges nothing (`chaosx.nr25.252`, `.253`), and both countries have a transfer cooldown after a handover.

### Physical destruction policy

A prepared independent participant can dismantle the alien material in its physical custody.
The action uses 50 support equipment and two percentage points of stability, with inclusive affordability checks, a shared AI/player executor, and a fresh transaction preflight.
Payments, cooldown, exposure consequences, and 60 points of Dependence relief require a successful six-slot ledger retirement.
Only the country's physical core and fragments are retired, with learned technology and the historical winner record preserved.
A running containment project is removed without completion or timeout effects.
Retired material cannot produce further active-material incidents or support integration, including through a stale direct dispatch.
Acquiring different unretired material restores its hazard and integration context.

The executor is `chaosx_nr25_execute_destroy_material` in the event-owned custody-policy effect file.
Its cost, context, and retirement predicates are in the paired trigger file, and tuning lives in `025_alien_technology_in_antarctica_custody_constants.txt`.
Cost text uses the existing `GFX_support_equipment_text_icon` and vanilla `GFX_stability_texticon`, with no new visual asset or stockpile grant.
The caller initializes all nested temporary outputs before dispatch, and the source tests discard newly created helper temporaries on return.

## Cross-event recovery ledger

common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt owns the shared Event 025/Event 036 arbitration contract.

Fragment slots are persistent and exclusive. Invalid saved event targets are cleaned before resolution.

Exact overlap is country-scoped: Event 036 overlaps only with an applied Event 025 reward in the flight, propulsion and weapons field, and then receives an upgrade or the Integration capstone instead of its jet package.
The architect's proposed aviation-owner extension remains a proposal.

Event 025 does not create a Kruger country, Warren Kruger, Directorate state, Event 016 history, Event 016 evolution, Strategic Singularity, free formation, or unrelated equipment.

## Assets and wiring

The visual inventory and its remaining consumer gaps, provisional paths, and MCP limitations are recorded in docs/assets/025_alien_technology_in_antarctica/visual_asset_audit.md.

The phase banner is a real eight-frame asset package with a static disabled-animation fallback.
Each evolution (signal, survivor trace, militarised zones, fragment field, Dependence) has its own real eight-frame map overlay with a frame-000 static fallback; the header animation control switches the viewer between animated and static presentation.

Event 025 uses the following dedicated GFX files and consumers.

| Asset family | GFX registration | Consumer |
| --- | --- | --- |
| Reports and news | interface/025_alien_technology_in_antarctica.gfx | events/025_alien_technology_in_antarctica.txt and events/_chaosx_news.txt |
| Super-event | interface/chaosx_super_events.gfx | opening super-event dispatch |
| Board art | interface/025_alien_technology_in_antarctica.gfx | interface/025_alien_technology_in_antarctica.gui |
| Decision art | interface/025_alien_technology_in_antarctica.gfx | common/decisions/categories/025_alien_technology_in_antarctica_categories.txt |
| Ideas | interface/025_alien_technology_in_antarctica.gfx | common/ideas/025_alien_technology_in_antarctica_ideas.txt |
| Achievements | interface/025_alien_technology_in_antarctica.gfx | common/achievements/chaos_redux_achievements.txt |

## Validation and future depth

The source acceptance matrix is docs/specs/025_alien_technology_in_antarctica_specs/matrices/025_requirement_coverage.md and the pass/fail contract is docs/specs/025_alien_technology_in_antarctica_specs/specs/014_acceptance_criteria.md.

The 58 source tests cover recovery arbitration, lifecycle, delayed callbacks, physical custody, report bindings, active pulse guards, physical destruction policy, and authorization's source cost budget.
The tests use explicit callback spies for shared Chaos, Board refresh, and achievement internals, and do not emulate native scheduling or live economic state.
The catalog row update is staged in `docs/plans/025_alien_technology_in_antarctica_plans/catalog_changes_pending.md`; the MCP probability baseline and compare (agent decision D19) and supplied live-game evidence remain acceptance gates.

Any future board extension must preserve the three-main-value rule, participant privacy, bounded action trays, and the no-recurring-world-scan contract.
