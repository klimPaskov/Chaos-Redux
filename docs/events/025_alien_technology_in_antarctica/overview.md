# Event 025 Alien Technology in Antarctica

## Purpose

Implementation status: incomplete against the accepted package and its pass/fail contract.
The source tests described below cover specific transactions and do not establish live campaign, multiplayer, save/reload, GUI, technology, or probability acceptance.

Event 025 is a Calm World Major event with entry event chaosx.nr25.1 and one opening super-event. Human-controlled countries receive the same entry offer, while the bounded AI roster is selected after human entrants and accepts only the documented active Kruger State exception.

The expedition race is a country-scoped competition for alien-derived systems buried beneath Antarctic ice. Player-facing text describes alien-derived systems, survey evidence, and recovered fragments and never attributes the technology to Kruger.

## Runtime flow

The hidden entry event initializes one global race, six sector records, the persistent participant array, the fragment-owner registry, the same-day candidate fields, and the opening super-event audio and art.

The entry window sends one event to each human-controlled country and then closes once through a controller event.

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

## Reports and news

Every state change reaches only the affected country, once per change: the departure (`chaosx.nr25.10`), a failed gateway (`.12`), the first camp (`.20`), a lost or restored camp (`.21`, `.22`), a probable or confirmed site (`.30`, `.31`), a discovered false lead (`.32`), a recovered or lost fragment (`.40`, `.41`), a rescue for both countries (`.50`, `.51`), sabotage (`.60` unidentified, `.61` identified), and an armed clash for its target (`.165`).
A sabotage victim learns the acting country only when a prepared countermeasure catches the operation or its intelligence reaches 20; only then does it gain the suspicion opinion, and undetected false coordinates stay silent until the expedition discovers them.
Public news fires once per milestone: the first camp or verified fragment (`.90`), the first armed clash (`.91`), the first accident of an open alien programme (`.92`), and each exposed concealed programme (`.93`).
The dispatch helpers live in `common/scripted_effects/025_alien_technology_in_antarctica_report_effects.txt`.

## Expedition Board

The event-owned scripted GUI is nr25_expedition_board_window and is attached through chaosx_nr25_expedition_board_scripted_gui.

The main value column contains exactly Expedition Progress, Logistics Readiness, and Exposure Risk. When Evolution V is active for the current holder, the third value is replaced by Alien Dependence without adding a fourth value.

Route, outpost security, survey evidence, crew, intelligence, wreck condition, fragment count, rival evidence, and cooldown state are supporting text, icons, action status, or hidden state.

The board contains a phase header, deadline control, history and details controls, six Antarctic sector click regions, state emblems, rival cards, and a phase action tray capped at five primary action slots.

The source layout uses a 1024x640 board canvas and a four-frame 384x58 sector-hitbox atlas.
The GUI worker's layout handoff and all state, resolution, click-region, and comparison evidence require parent review.

The board uses participant-country scope and opt-in rival visibility flags so multiplayer players do not see another country’s hidden exact resources or hidden action state.

## Costs and action limits

The resource model includes convoys, fuel, support equipment, political power, civilian industry commitments, crew, scientific capacity, access, and time.
The accepted maximum is four spendable cost types per action, including committed industry.
Authorization commits convoys, fuel, support equipment, and civilian industry, with three upfront resource entries and the industrial duration in its cost tooltip.
Authorization uses inclusive resource predicates shared by its three cost-display components.
A human country without owned convoys, including a landlocked one, can enter by chartered passage: political power, more fuel, more support equipment and the civilian commitment replace convoys.
Every later shipping cost of a chartered expedition is paid in political power, and its organising and gateway objectives run longer.
Either entry warns when the civilian base or fuel reserve is thin, and such an entry starts with lower Logistics Readiness.

Entry, mobilisation, crossing, outpost, survey, and final-recovery trays normally expose three to five primary actions and never exceed six. Evolution responses and the countermeasure are secondary routes.

Rival actions require a selected valid participant target, one-use or cooldown cleanup, evidence state, counterplay, AI weights, and partial outcomes. Sabotage applies a partial result when the target has insufficient evidence or countermeasures, and the target can answer through the bounded countermeasure path.

## Evolutions

The five independently enabled evolutions are Active Signal, Something Survived, Militarised Antarctica, The Wreck Is Breaking Apart, and The Technology Changes Its Users.

Each evolution has a separate Chaos gate and MTTH source.
Delayed callbacks and recurring pulse hazards read their own enable/disable setting.
Evolved first openings, full policy/GUI disabled behavior, timed-achievement guards, and the required probability evidence remain unfinished.

Militarised Antarctica changes the expedition threat and diplomacy state without forcing a global war.

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
Four static-only evolution overlays remain pending animation work under the user's no-simplifications requirement.

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
Source-boundary evidence, independent audits, the authoritative catalog update, all accepted assets and routes, and supplied live-game evidence remain acceptance gates.

Any future board extension must preserve the three-main-value rule, participant privacy, bounded action trays, and the no-recurring-world-scan contract.
