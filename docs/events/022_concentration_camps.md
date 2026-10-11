# Event 22 Concentration Camps

## What the event is

Event 22 is a repeatable minor event in the Domestic Unrest cluster (Severe member).
It selects one country that has a campaign marker for detention, registers camps in about a fifth of its eligible states through the shared Camps and Repression system and hands the country a real crisis to manage.
It is an entry and escalation layer. Camp buildings, responsibility, custody cohorts, the monthly processor, deaths, evidence and Condemnation all belong to the shared system (`docs/systems/camp_administration_dispatch.md`, `camp_forced_labor.md`, `camp_institutional_mortality.md`, `common/scripted_effects/camp_administration_effects.md`).

## Event map

| Id | Kind | Role |
| --- | --- | --- |
| `chaosx.nr22.1` | hidden | entry on the selected country: opening, or an incident when a network is live |
| `chaosx.nr22.2` | report | opening report and policy choice |
| `chaosx.nr22.3` | hidden | monthly monitor, one self-rescheduling chain per live network |
| `chaosx.nr22.101` | report | escape networks |
| `chaosx.nr22.102` | report | sickness in the camps |
| `chaosx.nr22.103` | report | reports leave the camps |
| `chaosx.nr22.201` / `.301` / `.401` | report | Evolution I, II and III |
| `chaosx.nr22.601` | report | a hostile country takes a camp |
| `chaosx.nr22.701` | report | a new ruling ideology inherits a live network |
| `chaosx.nr22.510` | report | foreign report of credible camps (neighbour and enemy) |
| `chaosx.nr22.800` / `.801` | report | closure after destroyed records / closure with open records |
| `chaosx.nr22.802` | hidden | proof that an open closure stayed closed (Close Every Gate, The Machine Stopped, A Government Answers, Against the Order) |
| `chaosx.nr22.803` / `.804` | hidden | proofs of Safe Harbor and The Evidence Survives, 180 days after their conditions are met |
| `chaosx.nr22.511` | report | the front reaches a camp that holds prisoners |
| `chaosx.nr22.512` | hidden | carries out the retreat orders whose day has come |
| `chaosx.nr22.811` | report | the camp administrators refuse the closure order |
| `chaosx.news.22` | news | publicly documented network |

## Flow

1. The shared random-event picker rolls Event 22 (repeatable, `global.repeatable_events`). `concentration_camps_prepare_random_event_fire` builds a weighted country pool and saves `concentration_camps_prefire_target`, which is also the Event History actor.
2. `chaosx.nr22.1` runs `concentration_camps_open`: it counts eligible states (controlled and large enough), counts live compatible sites toward the target, takes `ceil(20 percent)` of eligible states and fills the rest from a weighted candidate pool. Each site goes through `genocide_register_concentration_site_for_root` and receives a first cohort through `camp_admin_admit_detainees` from a campaign marker.
3. `chaosx.nr22.2` offers closure (the shared national reform), case review (custody mandate), forced labour (coercive mandate and labour roles at sites with an economic base) and expansion (coercive mandate and the expansion decision). Each sets the shared Ledger controls. There is no Event 22 policy engine.
4. The monitor visits every 28 days (`camp_admin_dispatch.period_days`) while the network is live. It refreshes the shared values, ends the network when no site operates, and fires at most one incident.
5. Closure through the shared reform ends the network, sets the refire protection (540 days for an open closure, half that if records were destroyed) and reports it. Event 22 never removes buildings or population.

## Evolutions

The shared evolution context (event 22, type 22, stage and tier 1 to 3, gated by `is_current_evolution_enabled`) drives three stages. An active network advances through a due day of about 90 days (75 to 140 percent) that the monthly monitor sets and checks. A country whose first firing begins while a stage is active opens directly in that stage and records one evolution row.

| Stage | Active network | Pre-fire opening |
| --- | --- | --- |
| I Killing orders | `floor(n / 2)` of the valid concentration camps receive the shared killing role through `genocide_register_extermination_site_for_root` | the opening sites are split the same way |
| II A month of deaths | 1 percent of the current civilian population of every operating camp state, once per state | the same, applied to the opening sites |
| III Half the country | coverage to 50 percent of eligible states, an even concentration and killing split, then 2 percent once per state | 50 percent opening, even split, only the 2 percent loss |

Every loss is requested through `camp_admin_record_deaths` and clamped to the people the camp holds (cause custody for detention camps, violence for killing camps), so a small cohort takes a smaller shock and the state marker is set even when the applied amount is zero. Conversion needs `camp_admin_can_use_radical_mandate`. A country without the radical route keeps its concentration camps and still advances. Killing begins only when the Ledger mandate is radical, which the report options set (accept, or the extremist option of the late report). Review and the Ledger mandate stop it. A site added later takes the shock of the active stage once.

## Control loss, succession and the shared links

- Control loss: `genocide_on_state_control_changed` calls `concentration_camps_on_state_control_changed`. A camp site taken by a country at war with its operator is marked liberated and relief-protected (no new camp is built there) and the new controller gets one report every 60 days at most. The three answers are relief supplies (stability and war support), securing the records for investigators (a tribunal severity and opinion modifier on the operator) or leaving the site. Discovery, the captured site's closure, the release of survivors in place, responsibility and Condemnation stay with the shared system.
- Succession: the monitor stores the ruling ideology group (fascism, communism, democratic, neutral). A change reports once. Opening the archives closes the camps through the shared reform, a review sets the custody mandate, continuing starts a new network generation under the new government, and burning the files is the shared cover-up. Original responsibility stays on the shared immutable records.
- Famine and air: the sickness incident needs a camp state past supply strain in the famine stages and adds one weight when global air contamination passes the 25 percent spread threshold.
- Migration, tribunals and the Soviet adapter are shared-owner content and are not repeated here.

## Liberated camps

The hook above is the contract between the shared owner and Event 22.
`concentration_camps_register_liberation` (state scope, ROOT is the new controller) runs inside it and gives the state the dynamic modifier `concentration_camps_unrelieved_state` (less local manpower and construction speed, more resistance target), adds the state to the controller's `concentration_camps_liberated_states`, caches the aid costs and starts the relief mission.
It records no death and changes no population.
The category `concentration_camps_relief_category` (Liberated Camps) shows while a liberated state waits for relief or records.

- Relieve the Camp (state target): costs support equipment, trains and fuel, scaled by the number of liberated states still waiting (5 percent each, at most doubled). It removes the modifier and gives stability and war support.
- Record the Camp (state target): costs political power and support equipment and needs a verified site. It collects the site (always), the survivors' statements (when survivors were released there) and the papers (when the operator did not destroy them), and prepares tribunal records against the operator.
- Relieve the Liberated Camps (mission, 150 days): complete when every liberated state held has received relief. Failure costs stability and keeps the penalties.

The event options of the liberation report use the same state effects, so a state is relieved and recorded once however the player acts.

## Front approaches and retreat orders

The monthly monitor of a live network in a war looks for an operating site with prisoners that sits next to enemy divisions or enemy held territory (`genocide_state_has_enemy_forces_near_root`, the shared proximity test).
It reports one site per visit, with a 45 day country cooldown and a 120 day cooldown per site, and the operator answers with `chaosx.nr22.511`.

- Open the gates: the shared custody owner releases the survivors in place.
- March the prisoners away, or order the camp cleared (radical route only): an order that runs 21 days later through `chaosx.nr22.512`. If the state is still held and operating, the loss share (25 or 90 percent of the living cohort) is requested through `camp_admin_record_deaths`, the rest is released, the shared evidence destruction runs and the shared pressure values rise. If an enemy took the state first, the order was interrupted and nobody is lost.
- Burn the records: the shared evidence destruction at the camp, with its own failure branch.
- Hold the camp.

The shared custody owner offers no generic transfer, so nobody is moved to another site, and the loss shares and the 21 days are constants in `concentration_camps_retreat` and `concentration_camps_timing`.

## Closure orders

When the monitor first sees the shared national reform running (from the opening report, an evolution report, the succession report or the Ledger), the administrators may refuse (`chaosx.nr22.811`).
The chance is 15 percent, plus 25 percent with a killing site, 10 percent under a fascist or communist government and 10 percent from Evolution II.
The cabinet can arrest the commandants (political power and a little stability, the closure stays open), send soldiers (stability and war support fall, the closure is not peaceful) or let the administrators keep the files (the closure becomes quiet).
The reform closes the sites at once, so there is no separate regional closure mission and no inspection chain beyond the review decision and the leak report.

## Intake

Widen the Intake is a state target decision for the operator. A live site takes another cohort from its remaining campaign source through `camp_admin_admit_detainees`, which the shared custody owner clamps to the source, capacity and population share, and the source persists so nobody is taken twice. It costs the guard bundle and raises resistance pressure, exposure and overstretch.

## Achievements

Seven of the eight kept achievements are implemented (the Long Return is not, see Limitations).
The pool follows the accepted P-022-E: Names Restored, No Second Operator and From Camps to Care duplicate shared achievements and are dropped.
All proofs are event driven, only a human player's country receives a flag, and none rewards deaths, conversion or concealment.

| Achievement | Proof |
| --- | --- |
| Close Every Gate | open closure through the reform, no network 180 days later (`.802`) |
| The Machine Stopped | Evolution III with both detention and killing camps in the network, an open closure inside the 730 day window that starts at Evolution III, no camp added or converted after the closure began, and no network 180 days later |
| The Evidence Survives | records collected in liberated camps for the site, statements and papers, a verified responsible government, an operator that destroyed or concealed records, and every recorded state still held 180 days after the last category (`.804`) |
| No One Disappears Twice | three camps taken from one operator while its march or clearing order was pending, every one relieved and held, and the operator never completed such an order |
| A Government Answers | succession report answered with the archives and the closure, the network never continued, an open closure and 180 days closed |
| Safe Harbor | the border opened to the people leaving the camps of three different countries through the foreign report, no own network, and 180 days without opening one (`.803`) |
| Against the Order | the administrators refused, the commandants were arrested, no soldiers and no concession, an open closure and 180 days closed |

## Selection

A country is a valid target only when it has no bespoke camp package (`camp_rework_country_uses_generic_kit`), has not capitulated, is not protected or on cooldown, and has a controlled state with a campaign source: non-core territory, resistance above the floor, or a regime that names political enemies (fascist, communist, civil war, or emergency rule at war with low stability). Ethnicity is never read.
Germany, Japan, the Soviet Union, Britain, the United States, France, Italy and Belgium are excluded because their national camp kits expose no registration or expansion contract that another event may call, see "Excluded countries" below.
Weights rise with occupied and resisting states, war, civil war, authoritarian government, low stability and existing shared camp networks. They fall for democracies and stable countries. A country with a live network is drawn at a fraction of a fresh candidate's weight and only when an incident threshold is met.

## Opening balance

The shared site registration lowers stability by 0.015 for every site (`genocide_political_effect.hardliner_stability`), and it also adds one timed hardliner idea, a point of popularity for fascism or communism and a point lost by democratic and neutral politics per site.
The opening registers `ceil(20 percent)` of the eligible states, and an evolved opening registers 50 percent.

| Eligible states | Baseline sites | Stability lost | Evolution III sites | Stability lost |
| --- | --- | --- | --- | --- |
| 12 | 3 | 4.5 percent | 6 | 9 percent |
| 30 | 6 | 9 percent | 15 | 22.5 percent |
| 60 | 12 | 18 percent | 30 | 45 percent |

A country at 40 percent stability that opens 12 sites would end at 22 percent, below the 35 percent band where the opening report's collapse weights and the civil war pressure start, with no way to answer before the loss lands.
`concentration_camps_soften_opening` therefore returns the part of the measured loss above `concentration_camps_opening.stability_loss_cap` (0.12, eight sites) at the end of the opening, so the same country ends at 28 percent and a country with 60 states at Evolution III ends 12 points down instead of 45.
The measure uses the real stability before and after, so a country already near zero is never given more than it lost.
Expansion by decree (one site) keeps the full shared cost.
The popularity shifts stay with the shared owner: a 30 site opening moves democratic and neutral support by 30 points each.

## Excluded countries

`camp_rework_country_uses_generic_kit` is false for Germany, Japan, the Soviet Union, Britain, the United States, France (and Vichy), Italy and Belgium, and `concentration_camps_target_basics` requires it.
The kits were read against the major and colonial kit implementation maps and their effect files.
They expose decisions routed through `camp_rework_route_country_specific_action`, not a registration or expansion API.
Their state pools are ordered and strict (Germany takes occupied Poland before other occupied Europe and the core fallback only when both are empty, Japan takes the China and Manchuria pool first, the Soviet Union uses the remote gulag pool), their active and radicalized site caps live in `camp_ai_*` triggers, their cohorts come from country-owned sources and exact transfers, and their ideas, country values and monthly bridges are refreshed by the kit.
`genocide_register_concentration_site_for_root` bypasses every one of those, and `camp_rework_colonial_register_current_state` is a primitive of the colonial decision actions with its own subject-authority authorization.
Calling either from Event 22 would create sites the kit does not know about, with none of its caps, ideas or source rules, which is a second framework beside the kit and not an entry through it.
Those countries reach the same crisis through their own kit and the shared Ledger.

## Shared values

Exposure is `camp_foreign_visibility` and Resistance Pressure is `camp_resistance_pressure`, both 0 to 100 and recalculated by the shared system. Bands use `camp_rework_threshold`: above 8 persistent rumours or escape networks, above 18 credible leaks or coordinated sabotage, above 35, above 60. Event 22 changes them only through `camp_policy_*` impulses, which the shared monthly recalculation decays.

## Decisions and mission (categories `concentration_camps_category` and `concentration_camps_relief_category`)

- Widen the Camp Network: state-targeted, non-democratic, coercive mandate, costs support equipment, trains and manpower, cached in `concentration_camps_cost_*` and scaled with the live network.
- Review the Detention Cases: custody mandate and a share of every living cohort released in place through `camp_admin_release_detainees`.
- Widen the Intake: state-targeted, non-democratic, coercive mandate, another cohort at a live site from its remaining campaign source.
- Contain the Escape Networks (mission): resistance pressure back below the disorganized band within 120 days, otherwise prisoners reach the border and the leak incident follows.

The operator sees three decisions and the escape mission, the controller of liberated camps sees two decisions and the relief mission.

Routine management (mandate, priority, budget, roles, release, closure, records) stays in the Camp Administration window.

## Constants and files

- `common/script_constants/022_concentration_camps_constants.txt`
- `common/scripted_triggers/022_concentration_camps_triggers.txt`
- `common/scripted_effects/022_concentration_camps_effects.txt` (selection, opening, monitor, incidents) and `..._action_effects.txt` (policies, decisions, answers)
- `..._evolution_effects.txt`, `..._aftermath_effects.txt`, `..._relief_effects.txt` (liberated camps, records, intake), `..._retreat_effects.txt` (front, orders, closure refusal) and `..._proof_effects.txt` (achievement proofs)
- `common/dynamic_modifiers/022_concentration_camps_dynamic_modifiers.txt`
- `common/decisions/022_concentration_camps_decisions.txt`, `common/decisions/categories/022_concentration_camps_categories.txt`
- `common/scripted_localisation/022_concentration_camps_localisation.txt`, `localisation/english/022_concentration_camps_l_english.yml`
- `events/022_concentration_camps.txt`, `events/_chaosx_news.txt` (news 22)
- `interface/022_concentration_camps.gfx`
- Registration: `initialize_event_categories`, the unavailability reason `concentration_camps_target` (53), the event-log actor mapping, the Domestic Unrest member row 16004 and the reworked allowlist.

The legacy Spain proposal (events, ideas `jews_massacre`, their localisation and three DDS) is removed. No other file read it.

## Icons and assets

Reports use `GFX_report_event_SWE_internment_camp`, `generic_riot`, `generic_ruins`, `generic_read_write`, `generic_conference`, `generic_parliament` and `generic_train`. The news uses `GFX_news_event_global_atrocity_evidence`. The categories use `GFX_decision_category_repression_ledger`. Decisions use `GFX_decision_oppression`, `GFX_decision_generic_political_discourse`, `GFX_decision_sov_famine_relief` and `GFX_decision_generic_site_inspection`, the missions `GFX_decision_generic_civil_support`. The dynamic modifier uses `GFX_idea_germany_dormant_ss_camp_legacy`.

The seven achievements use the dedicated 64x64 icon sets in `gfx/achievements/chaosx_achievement_022_<name>.dds` with `_grey` and `_not_eligible` states, registered as `GFX_achievement_chaos_redux_022_<id>` in `interface/022_concentration_camps.gfx`. The sets for Names Restored, From Camps to Care, No Second Operator and The Long Return exist in the same folder and are not wired, because those achievements are not implemented.

### Assets still needed

| Sprite | gfx file | DDS location | Note |
| --- | --- | --- | --- |
| Report pictures for the opening, escape networks, sickness and the front | `interface/022_concentration_camps.gfx` | `gfx/event_pictures/022_concentration_camps/` | optional, the reused pictures work |

## Limitations

See `docs/plans/022_concentration_camps_plans/subagent_handoffs/022_release_pass_2026-10-11.md`.

## Future plans

Displaced-person and tribunal follow-up events, the restricted chemical integration, the Long Return and the Germany, Japan and Soviet adapters follow the spec parts 4 and 5 once the migration owner traces camp survivors and the national kits publish a registration contract.
