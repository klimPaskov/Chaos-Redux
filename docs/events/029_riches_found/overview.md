# Event 029 - Riches Found

## Documentation status and acceptance

This overview describes the current source implementation and accepted design, with unresolved validation recorded in the [2026-10-03 progress report and resume packet](../../plans/029_riches_found_plans/2026_10_03_resume_packet.md).
Acceptance comes from the user's explicit request to implement `docs/specs/029_riches_found_specs/` fully, without simplifications, fallbacks, placeholders, or omitted routes.
Source presence does not prove engine behavior, balance, route acceptance, or gameplay completion.
The parent is reviewing mission and custom-cost integrity, new specialist audits remain pending, and same-scenario probability comparison evidence is incomplete.
The 2026-08-29 repository exploration and probability baseline are historical snapshots superseded for current progress by the dated resume packet.

Event 029 is a Minor Repeatable event rooted at `chaosx.nr29.1`. It selects one uniformly random eligible ordinary country, grants that country exactly 1,000 political power once, and registers one valid owned and controlled state as a persistent mine. The mine record belongs to the state, while decisions, risks, contracts, presentation, aggregate benefits, and the controller idea are rebuilt for the current controller.

Event 029 is not an event cluster member. Its ordinary lifecycle remains separate from Event 018 Resources Found: it does not add ordinary strategic resources, create or enter Event 018 caves, reveal Oth-Kesh, call The World Opens Below, or use Event 018 terminal routes. Event 018 field and cave markers and existing Event 029 mine records are explicit target exclusions.

## Discovery and state ownership

The shared random-event dispatcher calls `riches_found_prepare_random_event_fire`.
That helper builds a pool with one entry per eligible ordinary country, then selects a valid state through its preferred/broad weighted branches and saves the owner/state pair as regular event targets.
Event Details and manual availability use the preparation contract.
The accepted design requires a fresh valid pair and `N/A` when none exists.
Preparation resets readiness for each call, records a fresh state selection through `riches_found_save_prefire_state`, and validates that exact country/state pair before publishing readiness.
An empty pool or a call that selected no state leaves readiness at zero, even when regular event targets from an earlier call remain in the effect chain.
Same-scenario MCP evidence for that transaction remains unresolved.

`riches_found_commit_discovery` initializes the state record and pays the discovery grant only after the state was registered successfully. The state flag `riches_found_discovery_grant_paid` makes the 1,000-political-power grant idempotent, so direct refiring, controller cycling, occupation, and repeatable Event 029 occurrences cannot pay twice for the same mine.

The persistent state record contains the mine sequence, original discoverer, current recorded controller, four public values, hidden risk values, phase, operating state, contracts, missions, route history, controller-transfer history, evolution history, achievement state, and presentation state. A bounded global array contains at most 64 registered Event 029 mine states and is the only cross-mine registry.

### Deposit profiles

Each mine is an alluvial field, deep vein, gemstone bed or platinum lode (`riches_found_mine_profile`).
The discovery report and category header name it; it sets the quality factor, shifts incident weights (claims and rush crime for alluvial, theft and smuggling for gemstones, foreign interference for platinum, collapse for deep veins), raises foreign interest for platinum and gemstones, adds collapse pressure to unreinforced deep veins, and steers AI development priorities.

### Opening conditions

`riches_found_apply_starting_conditions` shapes each mine's opening values once, at discovery, from `riches_found_starting_value`: the owner's stability below 0.4 lowers Local Order and Revenue Legitimacy and above 0.7 raises them, a core state starts more legitimate and a non-core state less legitimate and less orderly, each infrastructure level adds Mine Development, an owner at war or local resistance above its band lowers order, a Chaos Meter above its band raises Extraction Pressure, and a democratic owner starts with more legitimacy and less illicit capture.
The deposit profile adds its own opening: alluvial fields start with weaker order and more illicit capture, deep veins with less development, gemstone beds with more illicit capture, and platinum lodes with foreign claim pressure.
All values are clamped afterwards.

## Controller transfer and aggregate benefit

The narrow `on_state_control_changed` hook uses the documented scope contract in which `ROOT` is the new controller, `FROM` is the old controller, and `FROM.FROM` is the changed state. It reconciles only when that state is an Event 029 mine. Annexation, peace-conference completion, and capitulation traverse only the bounded mine registry to cover ownership and occupation transitions that do not necessarily emit the same control change.

Reconciliation removes the old controller's contribution, records the new controller once, migrates selected-mine and mission ownership, refreshes the state modifier and controller idea, and rebuilds both affected country aggregates. It does not copy the state record or leave a second contribution behind.

The country aggregate applies marginal factors of 1.00 to the first controlled mine, 0.60 to the second, 0.25 to the third, and 0.10 to later mines. Contribution components are capped and rebuilt from the bounded registry, so transfer cannot duplicate them and temporary occupation receives the explicit occupied-control factor rather than an owner-equivalent windfall.
That occupied factor is further scaled when the contribution is refreshed: the state's resistance lowers it and its compliance raises it, a damaged route and a state that is not the occupier's core cut it, and `riches_found_occupied_output` keeps it between a floor and a cap; a requisition then multiplies it by one plus `riches_found_occupation_choice.requisition_output_bonus` until the occupation ends.
The occupier's choices move the engine values this reads (`riches_found_occupation_choice`): sharing the revenue lowers resistance and raises compliance, keeping the administration raises compliance, and requisitioning output or stripping equipment raises resistance.
The same rebuild replaces one mutually exclusive controller stage—Windfall Receipts, Managed Mineral Revenue, Resource-Dependent Treasury, Captured Revenue State, Gold-Sick Administration, Infernal Accounts, or Reformed Resource Settlement—rather than adding one permanent idea per mine.

## Decision category and public values

`riches_found_mine_management` is one ordinary decision category with the static picture `GFX_decision_cat_picture_riches_found`. There is no Event 029 scripted GUI.

The category description presents:

- Extraction Pressure as the primary value;
- Mine Development as a supporting value;
- Local Order as a supporting value;
- Revenue Legitimacy as a supporting value.

Scripted localisation converts exact values into concise bands and adds only the phase, operating state, contract, active-mission, transfer, and evolved-track context currently relevant to the selected mine. State-targeted decisions select the mine directly; a multiple-mine controller can change the selected mine without creating a duplicate state record.

The baseline phases are discovery and claims, the rush, physical development, revenue settlement, foreign concessions, armed protection and raids, and consolidation, closure, or control crisis.
The accepted presentation requires three to five primary actions per ordinary phase, at most six, and one to three active missions.

### Decision layers

`riches_found_phase` stores only the highest ordinary milestone the mine has reached: claims, rush, development, revenue or foreign concessions.
`riches_found_reconcile_mine_phase` advances it one step at a time when the current milestone is complete (a survey and a claims policy; camp administration, sanitation and a labor route; a transport route, reinforced shafts and one settlement work; one revenue settlement) and never lowers it.
Armed protection and the closure or control crisis are not stored phases: they are overlays worked out from current conditions on every refresh, so a mine that faces a raid during development returns to its development decisions, including any not yet taken, once the raid crisis ends.

The same refresh shows exactly one decision layer per mine, in this order:

1. Occupation (`riches_found_phase_occupation`): the occupier's own actions.
2. An open Bottomless Account (`riches_found_layer_account`).
3. Demons Beneath the Mine (`riches_found_layer_demons`).
4. Gold Disease (`riches_found_layer_gold`).
5. The emergency overlay (`riches_found_phase_emergency`): a temporary closure, quarantine, collapse, terminal mine or severe collapse, or Extraction Pressure, Local Order or Revenue Legitimacy in crisis (`riches_found_mine_needs_emergency_response`).
6. The security overlay (`riches_found_phase_security`): armed claimants, a wage dispute, a crime crisis, a raid crisis, an enemy holding a neighbouring state (`riches_found_front_line`) while supplied troops stand in the district and no Army Cordon holds the mine (`riches_found_army_cordon_holds`), a mine about to fall to the enemy (`riches_found_mine_about_to_fall`), or private forces beyond control (`riches_found_mine_needs_security_response`).
7. An unanswered Gilded Sovereignty (`riches_found_layer_gilded`); any one of its six answers settles the district.
8. The Resource Curse (`riches_found_layer_curse`).
9. The milestone layer (`riches_found_phase_claims`, `_rush`, `_rush_services`, `_development`, `_revenue` or `_foreign`).

Repair is offered in every layer except an unanswered Gilded Sovereignty, whose authority holds the works; the mine selector, the return-to-list action and the Court a Partner rows are navigation and are not counted below.
Missions are not counted.
The largest set any combination of flags can show in each layer, with the exclusions that keep it there:

| Layer | Most decisions visible at once | What keeps it within six |
| --- | --- | --- |
| Claims | 5 and Repair | Survey hides the four claims policies until it completes |
| Rush | 1 and Repair, then 5 and Repair | Camp administration opens the services set |
| Development | 5 and Repair | Rail Spur, Port Route and Drive Deeper exclude each other: Port Route only where rail is invalid or the state is an island, Rail Spur only without any route, Drive Deeper only with one; Drive Deeper stays offered in the revenue and foreign layers (`riches_found_drive_deeper_is_layer_action`) |
| Revenue | 5 and Repair | Dividend needs a working administration, Replace the Administration a compromised one; the Stabilization Fund needs order and legitimacy above their floors, Tolerate Patronage legitimacy below its floor; Central Revenue needs a state, military or predatory policy or a war; Drive Deeper stays open to a mature mine |
| Foreign, no contract | 5 and Repair | Offers follow the opening policy (a concession economy sells concessions and offtake rights, not infrastructure access); mine police or private guards by policy, and Drive Deeper takes that slot once the force stands; Trade Access for Infrastructure needs development below the Drive Deeper line, so the two never show together; the Independent Revenue Authority only after an audit and without a contract |
| Foreign, running contract | 5 and Repair | Audit, publication, at most two term extensions, and the standing force or, once it stands, Drive Deeper |
| Foreign, strained contract | 5 and Repair | A due renewal, dispute, exposed meddling, ledger irregularities or foreign claim pressure at its gate (`riches_found_contract_under_strain`) replaces the offers, the standing force and Drive Deeper with disclosure and the exits; Buy Out needs working relations and Nationalize with Compensation broken ones; Nationalize without Compensation needs war, a non-democratic government, exposed corruption or meddling; at renewal Renegotiate replaces the audit |
| Security | 5 and Repair | One standing force by policy; Army Cordon, Escort the Pay Train and Clear the Barricades need a supplied force, Arm the Workers its absence; Disarm Private Forces waits until no claimants or raids remain; Deny the Mine to the Enemy only when the mine is about to fall, which hides Escort the Pay Train |
| Emergency | 5 and Repair | A collapse or severe collapse offers the cordon, sealing, evacuation and permanent sealing; a closure offers reopening or repair, sealing, workforce replacement and the cordon; an open crisis offers closure, the aftermath quarantine, workforce replacement, sealing and the cordon |
| Occupation | 5 and Repair | Reopening only for a closed mine and the exploitation choices only for an open one; Deny the Mine only when the hold is about to break (`riches_found_retreat_imminent`), which hides keeping the administration and replacing the concession |
| Bottomless Account | 4 and Repair | Spend Authority and Predatory Prosperity answer different obligations |
| Demons Beneath the Mine | 5 and Repair | Evacuation and the purge exclude each other; the three kinds of assistance come once the district is cleared and give way to Controlled Exploitation once one is taken; Seal the Mine Permanently needs a cleared district, evacuated or purged (`riches_found_demons_district_cleared`) |
| Gold Disease | 5 and Repair | Closure, quarantine and rationed access are offered while movement is unrestricted; revenue sharing, workforce replacement, sealing and destroying seized material once it is restricted; Military Control only against gangs, sick guards, claimants or disorder |
| Gilded Sovereignty | 6 | Repair waits until the authority is answered |
| Resource Curse | 5 and Repair | Tolerate Corruption needs Local Order below the stable band, the Independent Revenue Authority stable order |

While Gold Disease is active its own quarantine, workforce replacement and sealing replace the baseline emergency versions; the baseline quarantine serves a district that keeps Gold Disease susceptibility after containment.
Army Cordon is offered with a supplied force in either overlay when a raid crisis, a war or a collapse of local order gives it cause, and starts Hold the Mine During War.
A front line alone no longer freezes the milestone: once an Army Cordon stands with supplied troops in the district, the mine returns to its milestone decisions, while Hold the Mine During War keeps running in any layer.
Where no cordon can be raised because the mine has no supplied route, the front alone does not hold the overlay, so a route-less mine with troops in it keeps its milestone decisions (including the Rail Spur) during the war.
`riches_found_refresh_mine_threat_position` marks an owner-held mine as about to fall when its controller is past `riches_found_overlay.retreat_surrender_progress` surrender progress or keeps no troops in the district (`riches_found_state_has_controller_troops`, which does not depend on a mine route; the occupier's `riches_found_retreat_imminent` uses the same test); that raises the security overlay even under a cordon and offers Deny the Mine to the Enemy (`decision_riches_found_deny_mine`), which wrecks and closes the workings (`riches_found_owner_denial`, persistent damage, -25 development, -10 Revenue Legitimacy) and stops an occupier from denying the same mine again until Restore the Shaft repairs it.
The AI takes Deny the Mine to the Enemy only while its war is being lost (surrender progress past `riches_found_overlay.retreat_surrender_progress`).

The overlay flags follow the controller pulse (`riches_found_review_mine_crisis_flags`): the crisis, crime and compromised-administration flags lift on the pulse after their value recovers (crime once Local Order leaves its crisis band, a compromised administration once Revenue Legitimacy is stable and illicit capture below its gate), a severe mutiny is a wage dispute that has broken local order, and a raid crisis ends after `riches_found_duration.raid_memory_days` without a raid or at once when Army Cordon, Clear the Barricades or a Mine Truce succeeds.
Worker cooperatives, a dividend, local revenue or a truce settle a wage dispute.

## Baseline lifecycle

The claims phase surveys the deposit, registers claims, freezes claims, recognizes local claims, reserves the deposit, or opens a claims court.
Rush actions establish camp administration, licensed traders, local or specialist labor, worker cooperatives, and sanitation.
Development actions build rail or port access, processing works, housing, shaft reinforcement and a development fund.
Drive Deeper is open to any operating mine with a route, Mine Development above the high band and steady order, in the development, revenue and foreign concession layers, so repeated deepening stays possible after the development milestone.
Revenue actions choose central receipts, local revenue, citizens' dividends, a stabilization fund, a replaced administration, or tolerated patronage.
The settlement is a standing revenue route, shown on the category header's Revenue line.
`riches_found_refresh_mine_contribution` multiplies an owner-held mine's score by a route factor (`riches_found_revenue_route`): central receipts add 20 percent, while a dividend (10), a local share (8), a stabilization fund or the curse diversification program (6), a development fund (5), worker housing (4) and a workers' share (4) hold output back and patronage leaks 12, clamped between 0.6 and 1.25.
`riches_found_apply_revenue_route_drift` runs once per controller pulse interval while the mine yields to its owner: central receipts without an audit or independent revenue authority (`riches_found_revenue_has_oversight`) add 2 illicit capture, a dividend adds 1 Local Order and removes 2 capture, a local share adds 2 Local Order and removes 1 capture, and patronage adds 2 capture; the dividend and local relief stop at the illicit-capture gate, so a one-time settlement does not erase entrenched corruption.
Central receipts also raise the mine's share of national receipts, which is what `riches_found_refresh_controller_receipt_dependence` turns into treasury dependence.
The Stabilization Fund (and the curse diversification program when no reserve is held) builds one `riches_found_stabilization_reserve`.
It is spent once, on the first bill it meets while the owner holds the mine: Repair's stockpile costs are returned when the crews arrive, or the idle crews of one closure are paid so Revenue Legitimacy does not slip (`riches_found_closure_crews_paid`); `riches_found_stabilization_reserve_spent` then records it, and only a new fund builds another.
Audits, disclosure, publication, contract exits and the independent revenue authority belong to the foreign concession layer.

Foreign participation is represented by one state-owned contract record with one partner, review clock, renewal state, and term flags.
Interested governments form a bounded ranked list on the mine.
`riches_found_prepare_scored_foreign_partner` runs only at discovery and after deliberate actions (through `riches_found_refresh_selected_foreign_offer`), scores every plausible actor once and keeps the `riches_found_partner_list.size` (4) most interested in `riches_found_foreign_candidates`; at war, hostile (below -25 opinion), excluded and capitulated actors are never listed.
The offer (`riches_found_foreign_target`) goes to the most interested actor, which is what the AI always keeps.
A human controller may court any other listed actor through the country-targeted Court a Partner decision (`decision_riches_found_choose_partner`, `target_array = riches_found_partner_candidates`, copied from the selected mine by `riches_found_refresh_partner_display`); the courted partner (`riches_found_partner_chosen`) then receives every offer and is named in the offer tooltips.
The courtship ends when the controller signs a contract, closes the mine view or moves to another mine (`riches_found_clear_partner_choice`), when control changes (`riches_found_clear_stale_targets`), or when the courted government drops off the rebuilt list; the controller pulse (`riches_found_review_foreign_offer`) moves an offer whose partner went to war, turned hostile or vanished to the next valid listed actor without scanning the world.
Compatible limited-concession, offtake, and infrastructure-access terms use the existing partner record, while exclusive concessions block amendments.
The parent corrected `riches_found_begin_contract` to require exclusive request 1 and the stored exclusive contract type, and corrected limited-contract amendment refresh to run through the current `CONTROLLER`.
These source repairs and their validation limits are recorded in `docs/plans/029_riches_found_plans/subagent_handoffs/2026_10_03_parent_contract_repairs.md`.
Signing a contract gives the partner one bounded `riches_found_country_concession_share` modifier (however many Event 029 contracts it holds) and gives both governments the `riches_found_concession_partner` opinion modifier (`common/scripted_effects/029_riches_found_partner_effects.txt`).
The share modifier ends with the partner's last contract; the opinion pair is added once per partner and controller, is stored with the controller that holds the share (`riches_found_contract_share_controller`), and is removed with the last contract between those two, read through `riches_found_partner_pair_has_other_share`.
When a suspended contract resumes after a control or ownership change, `riches_found_repoint_contract_partner_share` moves the share and the opinion pair from the previous controller to the current one.
A buyout or compensated nationalization pays the partner `riches_found_concession.compensation_political_power` and leaves a fading settlement opinion; an uncompensated nationalization gives the sponsor the hostile `riches_found_concession_expropriated` modifier and records it on the mine as an aggrieved sponsor that is preferred as the interference actor and raises the foreign-interference weight for `riches_found_concession.grievance_days`.
Partners at war with the controller or below the hostile-opinion threshold toward it are never offered cooperative terms, and decision tooltips name the selected mine's current or offered partner.
Land-only foreign availability, including the required distant naval-power route, remains unresolved.
Renewal, expiry, publication, audit, nationalization, buyout, and payment integrity remain subject to the pending audits.

The security and crisis layer includes mine police, private guards, army cordons, pay-route protection, raid responses, occupation administration, transfer settlements, temporary closure, repair, collapse response, restoration, permanent sealing, and cleanup. Mission sequence and cooldown proofs prevent repeated completions from farming counters, benefits, or achievement progress. Permanent historical disqualifiers are not cleared by ordinary mission cleanup.

### Physical works

Rail Spur, Port Route, Processing Works, Housing, Shaft Reinforcement, Sanitation and Repair commit two civilian factories (three for Processing Works) while they run, in place of political power, and the AI builds one of them at a time on a mine.
`common/scripted_effects/029_riches_found_works_effects.txt` adds one infrastructure level when the Rail Spur completes and one naval base level on the coast when the Port Route completes, and damages the naval base or infrastructure on destructive raids and the infrastructure on a closing collapse.
When Open the Railhead succeeds on a rail route, `riches_found_lay_mine_railway` lays one railway level from the mine state to the controller's capital through `build_railway` (start and target state, allied ground only, with fallback), guarded by `can_build_railway` with the same arguments; a capital mine or one without a land path keeps its spur alone, and `riches_found_railway_laid` keeps it from being laid twice.

### Occupation and recapture

Occupation choices belong to one occupation: `riches_found_clear_occupation_choices` clears them when the occupation ends or a different occupier takes over.
When an occupation begins or passes to a new occupier, `riches_found_record_previous_administration` marks a working civil administration (`riches_found_previous_administration_valid`): the camp administration was built, it is not compromised, and no private enclave or Gilded Sovereignty governs the works.
That record is what Retain the Administration keeps; it is lifted when the occupation ends, the occupier changes, or the administration is compromised.
An occupier's reopening lifts only an undamaged ordinary closure; depths contained as a guarded, monitored or protected closure stay shut, as they do for the controller's own Reopen the Mine action.
Stripping and denial leave lasting damage, a damaged mine produces `riches_found_closure.damaged_output_factor` of its output, and the header shows a repair objective until Restore the Shaft completes.

### Closure, collapse, and recovery

Every closing action (Temporary Closure, the Gold Disease closure, and an occupier's Deny the Mine) runs `riches_found_begin_temporary_closure`, so the closure state, operating state, review date, and suspended contract persist across presentation refreshes.
While a mine is temporarily closed, `riches_found_service_closed_mine` in the maintenance pulse lowers Extraction Pressure each pulse interval by `riches_found_closure.pressure_decay_per_pulse`, lowers collapse pressure until the closure review date, and lowers Revenue Legitimacy unless the workers hold a standing share (worker cooperatives or a public revenue share) or a revenue settlement (dividend, local revenue, curse revenue distribution or Gold Disease revenue sharing) was paid within `riches_found_containment.revenue_cycle_days`.
At the review date the mine gains `riches_found_closure_review_complete`; a closure kept in place after that slowly raises collapse pressure unless the shafts were reinforced.
A Demons Beneath the Mine closure end state (`riches_found_demons_contained_closure`) is kept under watch: it keeps relieving collapse pressure, does not lose Revenue Legitimacy for unpaid crews, and a reopening inspection that is still running when the depths are contained this way is cancelled and refunded.
Reopen the Mine is a state-targeted action in the ordinary category, visible only while `riches_found_mine_closure_can_reopen` holds.
It requires the safety and order check `riches_found_mine_reopening_is_safe` (pressure below the reopening ceiling, a rail or port route, and adequate Local Order or a security force), costs light political power, standard manpower and standard support equipment, and runs a recovery inspection for `riches_found_duration.recovery_review_days`.
At the end of the inspection `riches_found_finish_reopening` returns the mine to regulated operation (sealed deep sections stay sealed), reviews any suspended contract with its partner, and sets a reopening cooldown that blocks an immediate second closure; if the payer lost the mine or the check failed, the reopening is cancelled and the payment refunded.

Damage is a persistent physical fact that only a completed restoration clears.
A collapse always implies damage; major-failure and catastrophic collapse incidents close the workings through `riches_found_collapse_mine`, which records harm once per collapse.
Event 029 deaths reach the Deaths window under two reasons of their own (`chaos_meter_deaths_reason.mine_disaster` 291 for collapses and supernatural losses, `mine_violence` 292 for raids, barricade clearances, forced workforce replacement, the Military Purge, violent nationalization, Gold Disease violence and predatory prosperity); each harm wrapper in `common/scripted_effects/029_riches_found_harm_effects.txt` passes its reason through `riches_found_harm_reason`, the shared Chaos Meter files count both in the resource-field incident country bin and chaos weight, and both have their own labels in the last-reason and detail lookups.
Abuses that are not public when they happen enter the responsible controller's Condemnation as hidden or suspected sources, once per mine and kind (`common/scripted_effects/029_riches_found_harm_effects.txt`, `riches_found_hidden_abuse` constants): guards that answer to no one (an enclave, or private guards past the private-security gate; checked on the controller pulse), records burned by the controller's own guards or a corrupt unit over a mine that has cost lives, corruption tolerated over a lethal history, and soldiers' control of a gold-sick district (suspected).
The mine keeps each hidden amount and the country that holds it, and `riches_found_expose_hidden_abuse` brings it to light once through `condemnation_expose_hidden_bucket` when the concession audit succeeds, owners are disclosed, the contract is published, another country occupies the mine, or foreign agents, a hostile neighbour or the resistance raid the records.
Repair is visible on any damaged mine and starts Restore the Shaft; its crews deliver after the decision's removal period only if the payer still holds the mine with the mission running, otherwise the payment is refunded.
The mission completes when `riches_found_restore_shaft_works_ready` holds, and its completion runs `riches_found_complete_shaft_restoration`, which clears damage, route damage and any severe collapse and returns a collapsed mine to regulated operation through the shared recovery helpers.
A partial result reopens a collapsed mine's upper workings as a partial seal (marked `riches_found_restoration_partial_seal`) while its damage and any severe collapse remain for a later restoration; that later completed restoration lifts this seal unless a Gold Disease sealing, bound account terms or a Demons containment now holds the deep sections shut, and a collapsed mine left without repairs after its recovery date loses development each pulse interval.

## Evolutions and late outcomes

Event 029 registers exactly three evolution rows:

1. The Resource Curse at Chaos Tier, 600+.
2. Gold Disease at Totalen Chaos, 800+.
3. Demons Beneath the Mine at World Collapse, 1,000+.

The active mine pulse can enter an enabled evolution after its state gates and MTTH resolve. Before the opening event is shown, the prepared state can also receive an evolved opening when the current chaos level and state profile satisfy the same track contract. Each registered track records one evolution-log row and cannot record it twice.

The Resource Curse layers dependence, patronage, concession capture, illicit revenue, reform, and sovereign-control pressure over the ordinary mine lifecycle. The Gilded Sovereignty is a late Resource Curse outcome, not a fourth evolution row.

### The Gilded Sovereignty answers

Each answer has its own outcome and constraint (`riches_found_gilded` constants, helpers in `common/scripted_effects/029_riches_found_late_outcome_effects.txt`).
- Revoke the Charter rolls success (weight 60, times 1.5 with a supplied force) against failure (weight 40, times 2 when private-security autonomy is at its gate) in `riches_found_gilded_resolve_revocation`. Success voids the charter and costs 12 Mine Development; failure leaves the authority unanswered, either shuts the works through `riches_found_begin_temporary_closure` or raises armed claimants, guard autonomy and foreign claim pressure, and blocks another attempt for 365 days (`riches_found_gilded_revoke_cooldown`). The Gilded report event `chaosx.nr29.111` describes the outcome.
- Buy Back the District needs a negotiable authority (`riches_found_gilded_authority_negotiable`: no governing enclave, guard autonomy below 80) and a treasury that can carry it (`riches_found_country_can_fund_buy_back`: more than 20 civilian factories or 150 political power).
- Share Sovereignty costs the controller 0.10 political power a day per shared district through the country modifier `riches_found_country_mine_authority`, and the shared district can no longer be closed through Temporary Closure or given an exclusive concession.
- Recognize the Board seats a captured board when the guards or owners run the district (`riches_found_gilded_board_would_be_captured`: autonomy at its gate, private dominance or an exclusive concession), which raises illicit capture and guard autonomy, and a representative board otherwise, which raises Revenue Legitimacy and Local Order (`riches_found_gilded_seat_board`).
- Let the Board Govern costs 2 percent stability and 15 percent opinion gain per governing district and makes law changes 15 percent dearer through the same country modifier, which `riches_found_refresh_authority_terms` rebuilds with every controller aggregate.
- Seize the Enclave keeps its harm, Chaos Meter and condemnation consequences.

An authority that was never answered or that governs as an enclave outlives a change of controller (`riches_found_handle_gilded_transfer`): an occupier's arrival raises guard autonomy by 15, and the new controller receives `chaosx.nr29.113`, which offers continuity for recognition (the board governs as an enclave and order rises) or confrontation (guard autonomy rises, order falls and an enclave loses its standing, so the authority must be answered again).
The No Man Owns the Mountain hooks are unchanged: a successful revocation, a buy-back, shared sovereignty and a recognized board still record the reform, and a governing enclave or a seizure still disqualifies it.

Gold Disease is a fictional compulsive administrative and social crisis. It uses Event 029-specific pressure, movement, sanitation, quarantine, administration, and containment state and never invokes the biological outbreak, disease, or plague systems.

Demons Beneath the Mine uses an Event 029-specific supernatural-force record, deep-excavation pressure, bargains, evacuation, scientific, religious, engineering, sealing, and containment routes. It does not reuse Event 018 underground actors, Oth-Kesh, or any existing terminal entity. The Bottomless Account is a late Demons Beneath the Mine outcome, not a fifth evolution row.

### Gold Disease movement routes

`common/scripted_effects/029_riches_found_gold_route_effects.txt` moves Gold Disease only through the specification's six bounded routes, each called by one action or result: Replace the Workforce (and the emergency workforce replacement) sends the old crews to another active mine of the same controller, raising its gold pressure, or to the capital; a completed Protect the Pay Train delivers a shipment to the capital; the Pay Train escort carries wages; Military Control rotates soldiers into the army; guard-theft and false-permit incidents sell stolen material to one foreign controller of a neighbouring state; and a contract that ends while the fever is active sends the sponsor's staff home.
Each route rolls `riches_found_gold_route.spread_weight` against `contained_weight`, multiplied by `restricted_factor` under a quarantine, rationed access or closure.
A spread gives the receiving country a temporary `riches_found_country_gold_fever` (or `riches_found_country_gold_fever_army` for the rotation route) for `country_effect_days`, or raises gold pressure at the receiving mine, and the source mine reports the route and its destination by name.
A country that receives the modifier, whether a neighbour, the sponsor or the controller's own capital, also gets one short report per spread (`chaosx.nr29.140`, the Gold Disease report picture) naming the source mine and the route, with the modifier as its option tooltip.
No route scans the world, runs on a timer or uses the biological outbreak systems.

### Containment and aftermath

Each evolution has an active flag (`riches_found_resource_curse_active`, `riches_found_gold_disease_active`, `riches_found_demons_beneath_mine_active`) separate from its permanent history flag and log row.
`common/scripted_effects/029_riches_found_containment_effects.txt` keeps one per-mine progress value per active track (0 to `riches_found_containment.progress_complete`), reviewed once per controller pulse interval from the maintenance pulse.
Each condition that currently holds adds `step_gain`; fewer than the track minimum decays the progress, and a breaking condition decays it faster and blocks gains.

- The Resource Curse counts an audit (or an independent revenue authority where no concession exists), public terms or state operation, beneficial-owner disclosure where a concession exists, a revenue settlement paid within the last cycle, a development or stabilization fund, Extraction Pressure below the warning band, reined-in private security, and a replaced administration or independent authority. Tolerated corruption, tolerated patronage or illicit capture at its gate break it. Containment sets the Reformed Resource Settlement stage, records a successful reform and can relapse if corruption, patronage or private dominance returns.
- Gold Disease counts gold pressure below its gate, stopped movement (quarantine, rationed access or closure), a revenue settlement, replaced crews or administration without gold-sick guards, no seized material, shipment threat or gang control, and undamaged workings. Severe Extraction Pressure breaks it, and high pressure on an operating mine feeds the fever each review. Containment leaves the permanent `riches_found_state_gold_susceptible` modifier; gold exposure resumes with a susceptibility bonus and the disease relapses when pressure and gold pressure both return.
- Demons Beneath the Mine counts supernatural pressure below its gate, sealed sections or a closure, an evacuated district, active religious, occult or scientific assistance, Extraction Pressure below the warning band, a security force, and sealed-depth integrity at its gate. An open infernal account or deep digging breaks it. The end state is a monitored closure (scientific assistance), a protected closure (religious or occult assistance), a guarded abandoned district (any other closure) or upper workings under strict limits (partial seal); closure end states cannot be reopened, and renewed deep digging relapses the crisis. Permanent sealing remains its own end.

Crisis responses are reusable: revenue distributions and Gold Disease measures last a set number of days and can be renewed, assistance stays for a year, and the capture choices toggle against nationalization and the independent authority. Projects (funds, sealing the deep sections) and population-affecting actions (purge, evacuation) stay one-time per mine, and the corruption bribe pays only once.
The first unmet condition of the highest-priority active track becomes the category header objective, and containment queues one report (`chaosx.nr29.121` to `.123`).

## Chaos Meter

`riches_found_apply_chaos_source` changes the shared Chaos Meter through `add_chaos_meter_value` with the Riches Found history reason (`chaos_meter_history_reason.special.riches_found`) and the mine's controller as history actor.
Each source applies at most once per mine through its own receipt flag (`riches_found_chaos_<source>_applied`), so closures, reopenings, repeated raids and transfers cannot farm it, and the mine's output never adds chaos.
The changes are in `riches_found_chaos_change`:

| Source | Trigger | Change |
| --- | --- | --- |
| Lasting public settlement | Complete the Public Settlement succeeds | -4 |
| Claim war | Claim jumpers, a violent eviction or a rival claimant arm the workings | +3 |
| Major raid | A destructive or lethal raid | +3 |
| Corrupt seizure | Nationalize without Compensation or Violent Nationalization | +4 |
| Massacre | Mass death inflicted by people at the mine (not a collapse) | +10 |
| Foreign intervention | Foreign military intervention is recorded | +8 |
| Catastrophic collapse | The catastrophic collapse incident | +10 |
| Demonic bargain | Make an Agreement or the Bottomless Account opens | +12 |

## AI and probability contract

AI willingness is centralized through Event 029 constants and file-scoped aliases for country scale, ideology, war pressure, desperation, occupation, neighboring interest, concession seeking, raiding, public-value thresholds, route state, and crisis state. Controller, occupier, partner, neighbor, and raider behavior is evaluated through the named scenarios in `docs/specs/029_riches_found_specs/029_riches_found_ai_probability_scenarios.md`.

Decision weights follow the action's family rather than one shared template, with every factor in `riches_found_decision_ai` and the situation facts in the decision AI section of `common/scripted_triggers/029_riches_found_triggers.txt`:

- War state: peace (`peace_factor`) favours development, settlement, governance and long-term contracts; a war away from the mine favours central receipts, the state reserve, reopening and the Rail Spur and Port Route (`distant_war_factor`) and raises no security action; a front beside the mine (`riches_found_ai_front_near_mine`: an enemy holds a neighbouring state, or the mine is about to fall) favours the Army Cordon that starts Hold the Mine During War, the pay-train escort and evacuation (`front_factor`) and holds back dividends, local revenue, worker housing and the development fund (`front_suppress_factor`); a civil war holds back the physical projects, the development fund and Drive Deeper (`civil_war_factor`).
- Low Local Order (below `order_low`): camp administration, mine police, the truce, the pay-train escort, the Army Cordon, private guards and temporary closure gain `low_order_response_factor` while no order response already works at the mine (`riches_found_ai_order_response_in_place`), so the AI keeps one primary response; the physical projects, the development fund and Drive Deeper lose `low_order_development_factor`.
- Capacity: a major favours audits, the Rail Spur, Processing Works, Shaft Reinforcement and nationalization (`major_factor`) and avoids an exclusive concession (`major_exclusive_factor`); a weak minor (`riches_found_ai_is_weak_minor`: not a major, civilian factories below `weak_factory_count`) favours the concession auction, Trade Access for Infrastructure, renegotiation, Let Private Interests Dominate and Let the Board Govern (`weak_minor_factor`).
- One project at a time: Rail Spur, Port Route, Processing Works, Worker Housing, Shaft Reinforcement, Sanitation and Repair mark the mine while they are built (`riches_found_mark_works_project`, cleared on landing, refund or control change), and the AI never starts one of them or Drive Deeper while a works or deep project runs (`riches_found_mine_has_running_project`).
- Bargains: Strike an Infernal Bargain, Spend Public Authority and Accept Predatory Prosperity have no weight for a stable democracy at peace (`riches_found_ai_stable_democracy_at_peace`) and start very low or low otherwise; desperation (stability below the floor, a war being lost or a civil war), authoritarian rule and the treasury's dependence on the mine each multiply them by `desperation_factor`. Closing, binding and paying the account in material keep their ordinary weights.
- The baseline Permanent Seal stays at `untried_containment_factor` until a lesser containment step has been tried (`riches_found_ai_lesser_containment_tried`: a closure, a partial or deep-section seal, a quarantine, an evacuation or outside help); an exhausted deposit counts as tried.

Missions start and complete on their own, so their weights carry no situation factors.

Every AI and incident input the Event 029 files read has a producer.
`riches_found_refresh_mine_capabilities` derives the planning facts on each refresh: `riches_found_transport_need` without a rail or port route, `riches_found_transport_ready` while a route has working capacity, `riches_found_worker_claim_war` while a wage dispute runs beside armed claimants or armed workers, and `riches_found_allied_target_available` while the current foreign offer comes from a faction partner.
Effects record the rest: a failed concession audit sets `riches_found_failed_audit` (which also speeds the Resource Curse evolution), Nationalize without Compensation sets `riches_found_nationalized_without_compensation` (which opens the sanctions threat), a hostile foreign operation keeps `riches_found_foreign_operation_active` for `riches_found_duration.foreign_operation_memory_days`, smuggling and theft open `riches_found_smuggling_route` for `smuggling_route_memory_days`, a partner holding concessions carries `riches_found_foreign_contract_network`, and the account's payment warning (`riches_found_account_breach_imminent`) holds from the warning date until the promise is paid, breached or closed.
The HOI4 MCP probability workflow treats the computed values as relative willingness scores among currently available actions, not literal click probabilities. Baseline inspection, named scenario evaluation, threshold sweeps, bounded owner patches, and same-scenario comparison belong in `docs/plans/029_riches_found_plans/`.

## Achievements

The accepted package requires seven achievements using historical flags, dates, counters, transfer proofs, disqualifiers, and bounded registry checks.
Tracking helpers exist in `common/scripted_effects/029_riches_found_achievement_effects.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.
At the 2026-10-03 documentation observation, none of the seven IDs below was found in `common/achievements/chaos_redux_achievements.txt`, despite the older icon handoff's registry claim.
Registry integration and unlock/disqualifier validation remain unresolved.


- `029_public_fortune` rewards the original discoverer for mature, legitimate, orderly public development without an exclusive concession or Resource Curse.
- `029_claim_jumper` rewards a valid new controller that settles and holds another country's operational mine without leaving the old contribution behind.
- `029_the_pay_train_runs` requires three distinct route-risk protection successes without an intervening robbery or duplicate mission count.
- `029_all_that_glitters` requires three safe, active mines under one valid capped aggregate for the verification period.
- `029_no_man_owns_the_mountain` requires non-destructive recovery from The Gilded Sovereignty.
- `029_close_the_account` requires controlled evacuation and sealing after The Bottomless Account while removing the positive supernatural contribution.
- `029_the_last_shift` requires evacuation, a valid assistance route, permanent sealing, and avoidance of mass death, purge, reopening, and supernatural agreement.

Claim Jumper reads `riches_found_claim_jumper_settled`, which the occupation settlements, a renegotiated contract, a replaced administration and a completed repair set; every controller change clears it with the Claim Jumper hold window and invalidation, so a later controller must settle and hold the mine itself while the discovery and transfer history stays.
Foreign military intervention (`riches_found_foreign_intervention_history`) is recorded when foreign agents or a hostile neighbour raid the mine, when a foreign-armed group or seizure incident lands, and when a foreign country at war with the owner takes control; diplomatic and economic interference is not recorded, and No Man Owns the Mountain is disqualified only by an intervention after The Gilded Sovereignty arose.
Close the Account is not disqualified by a payment warning, and a pay train whose route is damaged while it runs loses its route (`riches_found_pay_train_route_lost`), failing Protect the Pay Train and ending the run of escorted pay trains.
`interface/029_riches_found.gfx` declares completed, grey, and not-eligible sprite aliases pointing into `gfx/achievements/` for each ID.
All seven exact IDs are registered in `common/achievements/chaos_redux_achievements.txt` and have Career Profile title and description keys.
Commit `01bc85ee3c9f25be8bda48dbdd7dc4d0ed1f98fe` records that integration and the persistent exclusivity, transfer, and aggregate-cap disqualifier repairs.
Full tracking and unlock acceptance remains unresolved.

## Runtime files

- Event definitions: `events/029_riches_found.txt`.
- Constants and MTTH: `common/script_constants/029_riches_found_constants.txt` and `common/mtth/029_riches_found_mtth.txt`.
- Core, incident, harm, history, achievement, and CXT effects: `common/scripted_effects/029_riches_found_effects.txt`, `common/scripted_effects/029_riches_found_incident_effects.txt`, `common/scripted_effects/029_riches_found_harm_effects.txt`, `common/scripted_effects/029_riches_found_log_effects.txt`, `common/scripted_effects/029_riches_found_achievement_effects.txt`, and `common/scripted_effects/029_riches_found_cxt_effects.txt`.
- Lifecycle systems: `common/scripted_effects/029_riches_found_maintenance_effects.txt` (controller pulse, closure servicing), `029_riches_found_containment_effects.txt` (evolution containment), `029_riches_found_gold_route_effects.txt` (Gold Disease movement), `029_riches_found_works_effects.txt` (buildings and building damage), `029_riches_found_partner_effects.txt` (concession partners), `029_riches_found_account_effects.txt`, `029_riches_found_aggregate_stage_effects.txt`, `029_riches_found_exposure_effects.txt` and `029_riches_found_late_outcome_effects.txt`.
- Gameplay, cost and achievement triggers: `common/scripted_triggers/029_riches_found_triggers.txt`, `common/scripted_triggers/029_riches_found_cost_triggers.txt` and `common/scripted_triggers/029_riches_found_achievement_triggers.txt`.
- Opinion modifiers: `common/opinion_modifiers/029_riches_found_opinion_modifiers.txt`.
- Terminal verification callback: `events/029_riches_found_verification.txt`.
- Decisions, missions, and category: `common/decisions/029_riches_found_decisions.txt` and `common/decisions/categories/029_riches_found_categories.txt`.
- State presentation and country ideas: `common/dynamic_modifiers/029_riches_found_state_modifiers.txt` and `common/ideas/029_riches_found_ideas.txt`.
- Narrow lifecycle and CXT hooks: `common/on_actions/029_riches_found_on_actions.txt` and `common/on_actions/029_riches_found_cxt_on_actions.txt`.
- Scripted localisation and English text: `common/scripted_localisation/029_riches_found_scripted_localisation.txt`, `common/scripted_localisation/029_riches_found_account_localisation.txt`, `localisation/english/029_riches_found_l_english.yml`, `localisation/english/029_riches_found_decisions_l_english.yml` and `localisation/english/029_riches_found_requirement_flags_l_english.yml`.
- Sprite registration: `interface/029_riches_found.gfx`.
- Authoritative event catalog: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Shared registration and presentation adapters remain in the event-system, Event Logs, Event Details, settings, achievement, and scripted-localisation owner files. Event 029 does not own or add a dedicated GUI file.

## Icon and sprite wiring

The asset inventory and evacuation-action/evacuation-mission semantic reuse are recorded in `docs/assets/029_riches_found/icon_manifest.md`.
That manifest and the inherited asset handoffs remain evidence for parent review, rather than independent acceptance of every asset or reuse claim.
Event 029 sprite declarations live in `interface/029_riches_found.gfx`.
The parent's individual source, processed-PNG, and decoded-DDS review of the nine reports and static category picture is recorded in `docs/plans/029_riches_found_plans/subagent_handoffs/2026_10_03_parent_report_art_review.md`.
That review reports ten current validator passes with exact processed-to-decoded pixels and evidence-to-runtime byte equality.
It establishes standalone art and file-chain review rather than event-chain, category-action, icon-family, or package acceptance.

- Report cards use `GFX_report_event_riches_found_*` and live in `gfx/event_pictures/029_riches_found/`; the discovery report shows the found deposit through `GetRichesFoundDiscoveryPicture` (`_discovery_alluvial`, `_deep_vein`, `_gemstone`, `_platinum`, with the general discovery card as default).
- Reopen the Mine has its own `GFX_decision_riches_found_reopen_mine` art.
- The category picture and category icon are `GFX_decision_cat_picture_riches_found` and `GFX_decision_category_riches_found` in `gfx/interface/decisions/029_riches_found/`.
- Decision icons use `GFX_decision_riches_found_*` in the same decision folder.
- Mission icons use `GFX_mission_riches_found_*` in the same decision folder.
- State modifier icons use `GFX_riches_found_state_*` in `gfx/interface/state_modifiers/029_riches_found/`.
- Controller, route, and evolution ideas use `GFX_idea_riches_found_*` in `gfx/interface/ideas/029_riches_found/`.
- Achievement triplets use `GFX_achievement_029_*` and runtime files under `gfx/achievements/`.

## CXT registration

Event 029 registers the modifier-free carrier `chaosx_cxt_extension_event029_riches_found`, which names the idempotent `chaosx_cxt_extension_event029_riches_found_apply` effect.
Startup registers the carrier through one existing country.
The initialized CXT daily fallback registers unseen content and calls `chaosx_test_country_sync_registered_content`, whose current body only sets `chaosx_test_country_registered_sync_pending`.
It performs no daily grants.
Initial CXT setup consumes registered carriers, and later pending content is applied through the player-triggered **Apply Registered Systems** debug decision.

The Event 029 `_apply` effect requires initialized CXT and the absence of `riches_found_cxt_fixture_initialized`.
It attempts to initialize a mine in the capital only when that state is unregistered and passes `riches_found_state_is_valid_target`.
A registered capital mine receives `riches_found_cxt_fixture_mine`, regulated operation, the physical-development phase, public-development policy, and the configured development, order, and legitimacy fixture values.
The helper refreshes presentation, contribution, and controller aggregate, then sets its one-time country guard only after the capital has the fixture flag.
It does not call the discovery-grant transaction or pay the 1,000 political power.
This is an active mine fixture, rather than an inert readiness-only fixture.
The Event 029 entry in `docs/testing/chaosx_test_country.md` describes that same active fixture and the player-triggered pending-package application.

## Future plans

A future non-mutating diagnostic could render a compact registry ledger showing each mine sequence, state, recorded controller, aggregate slot, contribution, contract partner, mission owner, and evolution flags for faster transfer debugging.

A future balance review could expand the named scenario matrix with observed campaign telemetry while retaining the same bounded MCP comparison contract and without turning willingness scores into claimed click probabilities.
