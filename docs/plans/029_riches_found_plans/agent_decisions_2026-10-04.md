# Event 029 agent decisions, 2026-10-04

Disposition: accepted and recorded by the implementing agent under the owner's full-authority grant for this round.
Acceptance basis: the lead's round-one owner decisions (relayed in the orchestration task) and the accepted Event 029 specification in `docs/specs/029_riches_found_specs/`.
Each entry names the decision, the reason, and the files it governs.
Implementation evidence is source review only unless an entry says otherwise; live-game behaviour remains with the orchestrator.

## D1. Adopt the stopped thread's uncommitted tranche

The stopped thread's 15 modified and 8 new Event 029 files were reviewed for load hazards before adoption: brace balance with comments stripped, unsupported `<=`/`>=` operators, `$PARAM$` tokens, timed flags with `days = constant:`, country-only effects inside state scopes (heuristic scope walk over every scripted effect and decision), undefined `riches_found_*` helpers, undefined script constants and missing localisation keys.
No hazard was found.
The routed date-unit defects 3 (account, late outcome, exposure and maintenance dates) and 5 (discovery receipt, controller pulse and terminal verification dates) are fixed inside this tranche, so it is committed as a whole.

Two corrections were made during adoption.
The event file header and the direct-invocation comment still described a load-weighted recipient; the dispatcher draws uniformly from the eligible pool, so both comments now say so, and the misindented state selection block was re-indented.
The terminal verification callback `chaosx.nr29.907` read its mine through a regular event target saved before a delay of up to a year; the callback is a state event whose scope is already the sealed mine, so it now reads `THIS` directly and no longer depends on the target surviving the delay.

The unrelated re-indent in `common/scripted_effects/chaosx_settings_effects.txt` belongs to another owner and is left untouched.

## D2. Catalog clusters 7 and 15 stay

The authoritative cluster workbook was written after the 2026-08-19 specification and keeps Event 029 in clusters 7 and 15.
No Event 029 cluster has a runtime consumer, so the specification's "no cluster" line is superseded rather than enforced in script.

## D3. Native 2,000 political power cap

The one-time 1,000 political power discovery grant uses the native cap.
No global define change, deferred credit or workaround is added; behaviour at the cap is a live-game check.

## D4. Constant-driven event delays

`days = constant:` inside `country_event` and `state_event`, and timed flags fed through a temporary variable, follow the repository convention used by more than one hundred other call sites.
They remain live-game checks and are not rewritten.

## D5. Closure, collapse and recovery lifecycle

Every closing action (Temporary Closure, the Gold Disease closure and an occupier's Deny the Mine) calls `riches_found_begin_temporary_closure`, because the derived `riches_found_mine_closed` flag was cleared by the next presentation refresh and the mine never closed.
The closure is serviced by the maintenance pulse: Extraction Pressure and collapse pressure fall each pulse interval, Revenue Legitimacy slips unless the workers are paid or share the revenue, and the closure review date opens the reopening route.
A closure kept past its review stops relieving collapse pressure and slowly raises it unless the shafts were reinforced, which follows the specification's "temporary closure without maintenance" collapse risk.

Reopening is a paid, state-targeted Reopen the Mine action in the existing ordinary category, consistent with the lead's decision to add no GUI and to stay inside the phase budget: it swaps with Temporary Closure, since one requires an open mine and the other a closed one.
It requires the specification's safety and order check (pressure below 60, a rail or port route, and Local Order of at least 45 or a security force) and costs light political power, standard manpower and standard support equipment.
The reopening is an inspection that lasts the existing recovery review period; at its end the mine returns to regulated operation, any suspended contract is reviewed with its partner, and a 180-day cooldown blocks an immediate second closure so closure and reopening cannot loop to erase pressure for free.
A reopening whose payer lost the mine, or whose check failed by the end of the inspection, is cancelled and refunded.
The decision uses a new stable sprite name, `GFX_decision_riches_found_reopen_mine`, pointing at the existing returning-crews art; bespoke art is accepted and queued.

Damage is a persistent physical fact rather than a value re-derived from the repair receipt, which was why the restore mission could never succeed.
Major-failure and catastrophic collapse incidents close the workings through `riches_found_collapse_mine`, and collapse harm is keyed to one collapse rather than to the mine's whole history.
Repair is visible on any damaged mine instead of only in the emergency phase, because raid and incident damage can occur in any phase.
Restore the Shaft completes when the repair crews have delivered, a rail or port route still serves the mine and the progress date has passed; its completion clears damage, route damage and severe collapse and returns a collapsed mine to regulated operation through the shared recovery helpers.
A partial result reopens a collapsed mine's upper workings as a partial seal while damage and severe collapse remain, so only a completed restoration ends a severe collapse.
A collapsed mine with no restoration under way after its recovery date loses development each pulse interval.
Recovery keeps deliberately sealed deep sections sealed.
The occupier's reopening no longer recovers a damaged or collapsed mine; it lifts only an undamaged temporary closure.

## D6. One owner for the district evacuation preparation

Evacuate the District resolves its own preparation: its removal period equals the evacuation preparation period, and its removal effect either starts Evacuate the Workforce through `riches_found_start_demons_evacuation` or withdraws the authorization and refunds the exact political power, manpower, trains and convoys it took.
The decision no longer queues `chaosx.nr29.906` on the same day as its own cleanup, which removed the undefined ordering that could cancel a paid evacuation.
`chaosx.nr29.906` remains as a thin wrapper around the same guarded helper so a preparation already queued in a running campaign still finishes.
The decision now requires a free evacuation mission slot and a rail or port route before payment, and its tooltip states that a lost route, slot or mine calls the evacuation off and returns the costs.
Evacuate the Workforce can start and finish from collapsed workings, because the specification offers it for severe collapse; the mission no longer requires an undamaged active mine or the absence of a severe collapse.

## D7. Evolution containment, aftermath and reusable responses

Containment follows the lead's decision: one per-mine progress value per active track, fed by the specification's listed steps and sustained conditions on each controller pulse and decayed when they break.
The thresholds are tuned so a mine meeting every condition contains its crisis in five pulse intervals and a mine meeting only the minimum needs about seven; falling below the minimum loses ten points an interval and a breaking condition twenty.
Reaching the threshold clears only the active flag, so history, log rows and achievement predicates keep working, while presentation, contribution, incident pools, aggregate stages and response visibility follow the active flag.
Reformed Resource Settlement now requires a contained curse instead of any single reform flag.

Where no concession exists, an independent revenue authority stands in for the concession audit, because the audit action only exists for contracts.
Independent revenue authority and administration replacement end tolerated corruption and patronage, which otherwise would block containment forever.
Gold Disease susceptibility is a permanent state modifier plus a gold-exposure bonus after containment, so the fever can return under heavy extraction; the modifier uses a file-scoped constant because modifier fields do not read script constants.
Gold incidents that expose hidden hoards or guard theft now leave seized material, which makes the existing Destroy or Secure Confiscated Material action reachable; it can be repeated whenever new material is seized.
Demons containment end states are chosen from how the mine was contained, as listed in the specification, and closure end states block the ordinary reopening action.

Crisis responses are reusable as timed measures (180 days for Gold Disease measures and the curse distribution cooldown, 365 days for assistance, worker screening and a revenue settlement cycle).
Project and population-affecting responses stay one-time per mine, consistent with the lead's decision and the anti-farming rules: the purge, evacuation, sealing projects and funds.
The tolerated-corruption bribe pays political power only the first time, so toggling the policy cannot farm political power.
AI willingness for each response gains a factor when that response is the mine's next containment step; this is a weighted-logic change and remains subject to the probability audit item.
Three report events announce containment, reusing the existing evolution and concession report pictures.

## D8. Gold Disease movement routes

Each of the specification's six movement routes is wired to exactly one action, mission result, incident or contract end, with no periodic scan: workforce replacement (to another mine of the same controller, or the capital when there is none), shipment delivery by Protect the Pay Train, pay transport by the Pay Train escort, guard or army rotation by Military Control, stolen material sold to one foreign neighbour after guard-theft or false-permit incidents, and concession staff returning to the sponsor when a contract ends.
Every route rolls 40 against 60 and the spread weight is quartered under a quarantine, rationed access or closure, so containment measures visibly protect the rest of the country.
A spread to a country is a temporary 180-day dynamic modifier (civil Gold Fever, or Gold Fever in the Ranks for the army rotation) rather than a new crisis record, matching the specification's "incidents or temporary country effects"; a spread to a mine raises that mine's gold pressure so its own Gold Disease gate can fire.
The source mine's report names the route and destination; a smuggling spread replaces the theft report so one report covers both.
The receiving neighbour and sponsor are not sent their own report event in this round; their modifier carries its own description.

## D9. Payer-validity guard on every delayed decision result

One shared state trigger, `riches_found_mine_still_valid_for_payer`, decides whether a delayed decision result may land: the deciding country still controls the registered mine and the mine is not terminal.
All 66 existing control-only guards use it, so a result no longer lands on a sealed or exhausted mine.
The 15 staged transactions that had no guard (rail spur, port route, claim register, claim freeze, recognize local claims, reserve deposit, claims court, development fund, stabilization fund, audit, army cordon, pay train, clear barricades, truce and the curse diversification program) now apply their result only behind that guard and otherwise refund exactly the debits their payment took; the refund list is derived from each payment block so the two cannot drift apart.
Repair and the district evacuation received their own guards in D5 and D6.
Missions started by these decisions are already cancelled by the control-change, sealing, exhaustion and collapse cleanups, and those cancellations refund nothing, so a refund cannot be paid twice.
The account and Drive Deeper decisions keep their stricter receipt guards, which already require the original payer and a nonterminal or active mine.

## D10. Occupation choices reset per occupation; recapture keeps the damage

The seven occupation choice flags (reopened, output requisitioned, administration retained, concession replaced, revenue shared, stripped, denied) are cleared when an occupation ends and when a different occupier takes over, so every occupier sees the full occupation set.
Stripping and denial leave persistent damage (and denial a temporary closure), recorded with history flags; the returning controller repairs them through Repair and Restore the Shaft.
A damaged mine contributes `riches_found_closure.damaged_output_factor` of its normal output, so the recapture contribution follows the current damage, and the category header shows a repair objective while damage remains.

## D11. Physical projects commit civilian factories and build real works

The seven physical projects (Rail Spur, Port Route, Processing Works, Housing, Shaft Reinforcement, Sanitation and Repair) replace their political-power payment with a civilian-factory commitment for the decision's removal period: two factories for standard projects and three for Processing Works, through `modifier = { civilian_factory_use = ... }` with file-scoped mirrors of `riches_found_decision_cost.civ_standard` and `civ_heavy`.
Each still has four spendable costs; affordability requires that many free civilian factories through `num_of_available_civilian_factories`, matching the Event 016 precedent, and the cost rows show `£civ_factory` beside the remaining resources.
A refund after a lost or terminal mine returns the stockpiled resources; factories already worked during the period are not refundable.
The development fund and the curse diversification program stay political-power actions because they are financial programmes rather than construction.

Rail Spur completion adds one level of state infrastructure below the vanilla cap of five, and Port Route completion adds one naval base level to an existing port or a new naval base on the state's coast, following the vanilla `add_building_construction` precedents (including the all-coastal-provinces form used by the Afghanistan focus tree).
Destructive and lethal raids damage the naval base when they struck the sea route and the infrastructure otherwise; a collapse that closes the workings damages the infrastructure, with slower repair; the game repairs these buildings through ordinary construction while Restore the Shaft repairs the mine itself.
Railway lines are not built because the railway effects need explicit province pairs that a generic mine state cannot supply; this is recorded as a limitation.

## D12. Event Log actor, evolution previews and the global N/A lock

The shared default-actor helper gains a Riches Found branch that records `riches_found_prefire_owner` as the history actor, mirroring the Event 018 branch, so discovery rows carry their recipient.
The Event Details producer adds the three Riches Found evolution preview rows from the evolution type, tier and stage constants; the existing title and body lookups already resolved those rows.
The Event Details weight lock now reads `riches_found_has_no_valid_discovery_pair`, a non-mutating trigger that is true only when no eligible ordinary country owns and controls a valid discovery state anywhere, so the event shows N/A only when it truly cannot fire rather than whenever the viewer's own country is ineligible.
It prepares no receipt during UI refresh; its `any_country` check stops at the first eligible country.
All three shared-file changes were made as minimal hunks and committed alone, leaving another owner's uncommitted Event Log hunks in those files untouched.

## D13. Concession partner consequences

The partner's share is a single country dynamic modifier (+0.05 daily political power and +1% factory efficiency growth) with a per-partner contract count, so several contracts cannot stack it and it ends with the partner's last contract.
Both governments receive a +15 opinion modifier for the contract's lifetime.
Compensation is paid as political power equal to the heavy political-power cost the controller pays for a buyout or compensated nationalization, which keeps the transfer bounded and visible; the partner also gains a fading +10 settlement opinion.
An uncompensated nationalization gives the sponsor a -40 opinion modifier that fades over twenty months and marks it as the mine's aggrieved sponsor for two years: it becomes the preferred interference actor and doubles the interference pool weight, and it falls below the hostile-opinion threshold, which excludes it from new cooperative offers.
Hostile partners (at war or below -25 opinion toward the controller) are excluded both from the scored offer and from the offer validity check.
Decision tooltips name the partner through a country variable refreshed with the selected mine's offer and the controller aggregate, because a second-level variable reference in localisation is not a verified syntax.

## D14. AI follows the mine's policy profile and value bands

Every paid Event 029 decision except Survey and Repair (which every profile needs) reads the mine's stored opening or claims policy through five profile triggers: Public Development (public development or local claims), State Extraction (state extraction or state reserve), Concession Economy (concession economy, emergency concession or minimal interference), Militarized, and Predatory (predatory or open claims).
Actions that fit a profile get `riches_found_decision_ai.policy_favored_factor` (2.5) and actions that contradict it get `policy_disfavored_factor` (0.4); the mapping follows the specification's profile descriptions, for example dividends and sanitation for public development, central revenue and nationalization for state extraction, concessions and renegotiation for the concession economy, cordons and pay trains for militarized controllers, and patronage, stripping and agreements for predatory ones.
High Extraction Pressure (above 65) favours cooling actions (claim freeze, truce, sealing, stabilization fund, workforce replacement, revenue distributions) and disfavours pressure-raising ones (Drive Deeper, exclusive concessions, private interests, patronage); Revenue Legitimacy below 40 favours audits, dividends, local revenue, disclosure, publication and the independent authority.
Active-crisis containment weighting was added in D7; the AI cannot take an action blocked by cost or route because those are `available` gates.

Probability evidence: a narrow `hoi4_probability_inspect` for three decisions returned "Invalid tool arguments" without a source selector and `INTERNAL_ERROR` with one.
A narrow `hoi4_probability_compare` over six revenue-phase decisions, the frozen pre-change snapshot `evidence/2026_10_04_ai_policy_before/common__decisions__029_riches_found_decisions.txt` (SHA-256 `a65710567441b29eda4f07e01c7fd2ef536fda2644998517be8b8529dd245355`) and four profile scenarios from `evidence/2026_10_04_ai_policy_typed_scenarios.json` returned `PROBABILITY_ANALYZED_PARTIAL` (analysis `probability-9cf906c0e35787d336b8116a`) with zero eligible candidates, eighteen unresolved candidates, zero comparison changes and the adapter reported as `mission_ai_will_do`, so it is not usable numerical evidence.
Its one actionable diagnostic, a duplicated legitimacy modifier on Local Revenue, was fixed.
The final same-fixture comparison with resolved eligibility therefore remains blocked by the route, and the weighting is supported by source review only.
