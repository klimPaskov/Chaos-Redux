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
The thresholds are tuned so a Resource Curse mine meeting all seven conditions is contained in five pulse intervals and one meeting the minimum five needs seven, while Gold Disease and Demons Beneath the Mine (six conditions each, minimum four) need six and nine intervals; falling below the minimum loses ten points an interval and a breaking condition twenty.
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
Railway lines are not built because the railway effects need explicit province pairs that a generic mine state cannot supply; this is recorded as a limitation. Disposition: superseded by D29.

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

## D15. Mine profiles are visible and change play

The discovery report names the deposit (alluvial field, deep vein, gemstone bed or platinum lode) with one sentence on what to expect, and the category header shows it on the phase line.
Incident weights follow the specification's profile lines through the existing `riches_found_incident_factor.high` weight: alluvial fields raise claim jumping and rush theft, gemstone beds raise rush theft, smuggling, guard theft and false permits, platinum lodes raise the foreign-interference pool, and deep veins raise the collapse pool.
Platinum adds `riches_found_foreign_interest.platinum_profile` and gemstones `gemstone_profile` to the foreign partner score.
A deep vein without reinforced shafts adds `pulse_deep_vein_collapse_add` collapse pressure each pulse interval.
AI development priorities follow the profile: shaft reinforcement and sealing for deep veins, camp administration and sanitation for alluvial fields, mine police for gemstone beds, and processing works and the port route for platinum.
Profile-specific report imagery is not added because no profile art exists; the existing report pictures stay, and this is recorded as an asset limitation.

## D16. In-game Event Details text follows the catalog

The in-game Event Details description and the three evolution bodies use the catalog's player-facing wording verbatim, except the catalog's interface sentence about N/A, which is requested for removal in `catalog_changes_pending.md`.
The workbook and exported CSV files are not edited.

## D17. Plain requirement text in every Event 029 availability block

The mine-list selection flag reads "The mine list is open" (committed with D5), and the three flags that the containment work exposed (the revenue distribution cooldown and the active Resource Curse and opened-depths flags) have player labels.
The 28 scripted triggers that appear in availability blocks have localisation keys with their own names, which is the vanilla convention for scripted-trigger tooltips (for example `is_controlled_by_ROOT_or_ally`).
The 93 affordability triggers in availability blocks are wrapped in `hidden_trigger`, as the decisions skill allows when the cost row already shows each resource in its ready or blocked colour, so the requirement list no longer repeats raw resource comparisons.
A source audit of every `available` block found no remaining flag or scripted trigger without a label; tooltip fit remains a live-game check.

## Commit index

Each decision landed in the commit named here; source review is the evidence, and items marked as live-game checks above remain with the orchestrator.

| Decision | Commit |
| --- | --- |
| Routed date-unit, cooldown, political power scope and building-read fixes (before adoption) | `6ee17482a` |
| D1, including routed inbox defects 3 and 5 | `75490fe32` |
| D5 | `3abc6b387` |
| D6 | `e4bff3c6f` |
| D7 | `706829b7e` |
| D8 | `fc520044f` |
| D9 | `0b89f720c` |
| D10 | `e4bca26e1` |
| D11 | `026d7a519` |
| D12 | `5777c32b1` |
| D13 | `705f58424` |
| D14 | `0738ea7f7` |
| D15 | `81ff45863` |
| D16 | `0a72eefa1` |
| D17 | `3327378de` |

D2, D3 and D4 record accepted behaviour and need no source change.

## Round 1 review corrections

Disposition: implemented by the round 1 reviewer under the same full-authority grant; source review only, live-game behaviour remains with the orchestrator.

R1. A closure's Revenue Legitimacy slip (D5) read the one-time dividend and local revenue flags, so a single payment made years earlier shielded every later closure.
The slip now reads a standing share (worker cooperatives or a public revenue share) or a revenue settlement paid within `riches_found_containment.revenue_cycle_days`, the same cycle the containment tracks use, and both closure tooltips say so.

R2. A Demons Beneath the Mine closure end state (D7) blocks reopening, yet the closure service kept straining its unreinforced shafts and docking legitimacy for unpaid crews each pulse, which eventually collapsed a guarded or monitored district and let restoration reopen it.
A contained closure is now kept under watch: it keeps relieving collapse pressure after its review and does not lose legitimacy for unpaid crews.
A reopening inspection still running when the depths are contained as a closure is cancelled and refunded instead of reopening the contained mine.

R3. A partial Restore the Shaft result (D5) partially sealed a collapsed mine, and no later completed restoration lifted that seal, so the mine stayed at the partial-seal output factor and in the closure phase for good.
The partial result now marks a seal it imposes with `riches_found_restoration_partial_seal`; a later completed restoration lifts that seal and returns the mine to regulated operation unless a Gold Disease sealing, bound account terms or a Demons containment now holds the deep sections shut.
A seal that existed before the repair is never marked, and the closure cleanup clears the marker.

R4. Containment reports (D7) and Gold Disease route reports (D8) overwrote the single report slot even while another report waited for delivery, so the waiting report showed the wrong title or incident text.
They now queue only when no report is waiting; the containment and route effects still apply, and the category header shows the new state.

R5. The D7 timing sentence above was corrected: only the Resource Curse has seven conditions, so Gold Disease and Demons Beneath the Mine take six to nine pulse intervals rather than five to seven.

Not changed after review: Port Route builds a naval base level in every coastal province of a state without a port, which follows the vanilla Afghanistan focus precedent the decision cites; the receiving neighbour and sponsor of a Gold Disease spread still get no report event of their own; and the probability comparison remains blocked (a narrow `hoi4_probability_inspect` over two decisions returned `INTERNAL_ERROR` again on 2026-10-04).

## Round 2 decisions

Disposition: accepted and recorded by the round 2 implementing agent under the same full-authority grant; source review only unless an entry says otherwise, and live-game behaviour remains with the orchestrator.

D18. The partner validity trigger reads opinion through scope keywords.
`has_opinion` accepts only scope keywords as its target (`triggers_documentation.md`, `has_opinion`), so `riches_found_foreign_target_is_valid` steps into `var:PREV.riches_found_recorded_controller` and back through `PREV`, following the vanilla `var:FROM.<variable> = { ... }` scope switch in `common/decisions/AST.txt:699`.
The meaning is unchanged: the foreign target's opinion of the controller excludes hostile partners and admits friendly ones.

D19. One writer owns the report slot.
`riches_found_queue_report` is the only writer of `riches_found_report_kind`, and every producer passes the temporary inputs `riches_found_report_input_kind` and `riches_found_report_input_text`.
The slot stores its own text id (`riches_found_report_text`) and the contract partner at queue time (`riches_found_report_partner`), so the incident id that drives repeat memory no longer leaks into unrelated reports; `riches_found_complete_report` clears all three.
Concessions report their contract type (limited, exclusive, offtake, infrastructure access) and name the partner; a collapse reports its cause (the incident, neglected shafts, or the account default).
Collapses, evolution entries and containment results are priority reports: they replace an undelivered ordinary report, or wait in one deferred slot that is queued when the open report closes, so a waiting evolution report is never replaced and is not lost.
Any other report arriving while one waits is dropped, and a report of the same kind that has not been delivered takes the newer text (the collapse pool and its collapse helper share one report).
New ids live in the `riches_found_report_text` constant category (2001 and up), outside the incident id range.

## Round 1 review, second pass

Disposition: implemented by the round 1 reviewer under the same full-authority grant; source review only, and live-game behaviour remains with the orchestrator.

R6. Concession opinion pairs (D13) were removed through the mine's current controller and only when the partner held no other Event 029 contract, so a contract that ended after the mine changed hands, or a partner holding contracts with two controllers, left a permanent `riches_found_concession_partner` pair behind.
The share now stores the controller that holds it (`riches_found_contract_share_controller`), adds one opinion pair per partner and controller, and removes that pair with the last contract between those two, read through `riches_found_partner_pair_has_other_share`, a bounded check over the mine registry.
A suspended contract that resumes under a new controller moves its share and opinion pair to that controller through `riches_found_repoint_contract_partner_share`, called from the resume branch of `riches_found_review_contract`.

R7. An occupier's Reopen the Occupied Mine (D5, D10) still lifted a Demons Beneath the Mine closure end state, which the controller's own Reopen the Mine refuses; it now leaves a guarded, monitored or protected closure shut.

R8. The Evacuate the Workforce mission description still said a severe collapse stops the evacuation, although D6 lets it start and finish from collapsed workings.
It now says workers can be brought out of collapsed workings and that a new collapse or a closure during the evacuation stops it, which is what `riches_found_clear_mission_state` does when either begins.

R9. The R5 timing sentence undercounted Demons Beneath the Mine: like the Resource Curse it has seven containment conditions, so a Demons mine meeting all seven is contained in five pulse intervals and one meeting the minimum four needs nine, while Gold Disease (six conditions, minimum four) takes six to nine.

R10. The comment describing the foreign-phase policy menus sat above the D14 profile triggers after their insertion; it is back above `riches_found_policy_allows_concession_auction`.

R11. Three D8 and D11 tooltips did not match their effects: Port Route said the state gains one naval base level, but `riches_found_build_port_route` expands every existing port or, without one, builds a level in every coastal province; Rail Spur did not say it adds nothing at the infrastructure maximum; and the Protect the Pay Train success text did not mention that the delivered shipment can carry Gold Disease to the capital.
Each tooltip now states what happens.

Reviewed and not changed: the refund branch of every paid decision returns exactly what its payment block took (a scripted comparison of each `complete_effect` debit list with its `remove_effect` refund list found no mismatch); every flag and scripted trigger shown in an `available` block has a label; every constant, helper, event id, sprite, dynamic modifier and opinion modifier the package references is defined; the shared Event Log hunks of `5777c32b1` contain only Event 029 lines; and no engineer commit touched another owner's file.
A report event whose trigger fails at delivery would leave the mine's report slot pending; the only state-dependent triggers are the containment reports, whose tracks cannot relapse within the one-day delivery delay or an open report's timeout, so this is recorded rather than changed.
MCP routes: `hoi4_event_inspect` in `lint` mode rejected string and object selectors for `chaosx.nr29.123` with "Invalid tool arguments", `hoi4_decision_inspect` returned only a workspace-wide `DECISION_ANALYZED_PARTIAL` inventory, and a narrow `hoi4_probability_inspect` (adapter `decision_ai_will_do`, the closure and reopening decisions, source path `common/decisions/029_riches_found_decisions.txt`) returned `INTERNAL_ERROR` again, so this pass rests on source review and the D14 probability comparison stays blocked.

## Round 2 lead items

Disposition: implemented by the round 2 implementing agent under the full-authority grant, following the lead's round 2 decisions; source review only, and live-game behaviour remains with the orchestrator.

D20. The stored phase is a milestone and crises are layers.
Basis: lead decision 1, spec part 2 ("The phases overlap ... present one readable current phase and a limited set of relevant actions") and the acceptance criteria "Decision category clarity" (six primary decisions at most, emergency actions replace obsolete ordinary actions).
`riches_found_phase` stores the highest ordinary milestone (claims, rush, development, revenue, foreign) and `riches_found_reconcile_mine_phase` advances it one step at a time when the current milestone is complete; closure, collapse, recovery and reopening helpers no longer write it, and a stored value above the last milestone is rebuilt from the completed route.
On every refresh the mine shows one decision layer: occupation, an open Bottomless Account, Demons Beneath the Mine, Gold Disease, the emergency overlay, the security overlay, an unanswered Gilded Sovereignty, the Resource Curse, then the milestone.
Emergency covers a closure, quarantine, collapse, terminal mine, severe collapse, or Extraction Pressure, Local Order or Revenue Legitimacy in crisis; security covers armed claimants, a wage dispute, a crime crisis, a raid crisis, private forces beyond control (an enclave, a lapsed guard contract, or autonomy at the private-security gate) and an enemy holding a state beside the district.
The front-line condition is an agent addition to the lead's security list: spec part 3 makes war a reason for an Army Cordon and Hold the Mine During War starts on front proximity, and the check reads only the mine's neighbouring states.
Agent decisions inside the layer model, each needed to keep every layer at six primary decisions or fewer:
- Evolution sets replace the ordinary sets while they are the mine's most urgent layer, because the Gold Disease and Demons sets alone held eight actions and the Curse and Gilded sets six each; Gold Disease and Demons rank above the emergency overlay because they carry their own closure, sealing, workforce and evacuation actions, while the Curse and the Gilded Sovereignty rank below the security overlay.
- A Gilded Sovereignty is answered by any one of its six responses (the spec lists one end state per district), after which the Curse or the milestone returns; before this the six responses stayed visible one by one and the Curse set never came back.
- Gold Disease is staged: closure, quarantine and rationed access while movement is unrestricted, then revenue sharing, workforce replacement, sealing and destroying seized material; Military Control needs gangs, sick guards, claimants or disorder, and rationed access needs camp administration and stable order (spec part 4: "requires high administration and order").
- Demons Beneath the Mine is staged: evacuation or a purge (they exclude each other), then one kind of assistance, then Controlled Exploitation once Extraction Pressure is below the warning band and order is stable (spec part 4: "requires low pressure, strong order, and repeated containment work").
- The Resource Curse's Tolerate Corruption needs Local Order below the stable band and its Independent Revenue Authority stable order.
- Revenue: Dividend needs an uncompromised administration (spec: "a functioning administration"), the Stabilization Fund order and legitimacy above their decision floors (patronage is offered below the legitimacy floor), and Central Revenue a state, military or predatory policy or a war (spec: "State-extraction or emergency government route").
- Foreign concessions: a concession economy no longer offers Trade Access for Infrastructure, which needs Mine Development below the Drive Deeper line (spec: "Low development and a valid foreign builder"); the baseline Independent Revenue Authority, previously unreachable because audits only exist after the revenue milestone, moves to the foreign layer after an audit and without a contract; a strained contract (`riches_found_contract_under_strain`) replaces the offers and the standing force with disclosure and the exits, Buy Out needs working relations and Nationalize with Compensation broken ones, Nationalize without Compensation needs war, a non-democratic government, exposed corruption or meddling, and at renewal Renegotiate replaces the audit.
- Security: each mine raises one standing force by policy (mine police, or private guards under a concession or predatory policy); Arm the Workers needs the absence of a supplied force (spec: "weak state security"); a Mine Truce also answers wage disputes, because the overlay hides the milestone actions that settle them; Disarm Private Forces waits until no claimants or raids remain (spec: "after the immediate threat passes").
- Emergency: a collapse or severe collapse hides closure, the aftermath quarantine and workforce replacement; Workforce Replacement also answers criminal capture of the workings (spec: "entrenched criminal capture"); Reopen the Mine is part of the emergency layer.
- Development: Rail Spur is offered only without any route and Drive Deeper only with one (spec: "working transport"), and Drive Deeper belongs to the development milestone.
- Occupation: reopening only for a closed mine; Deny the Mine only when the occupier's hold is about to break (`riches_found_retreat_imminent`: the occupier on the front is losing its war past `riches_found_overlay.retreat_surrender_progress` or keeps no supplied force there; spec: "deny the mine before retreat"), which hides keeping the administration and replacing the concession.
- Repair is offered in every layer except an unanswered Gilded Sovereignty, whose authority holds the works.
The static enumeration of every layer is the table in `docs/events/029_riches_found/overview.md` (Decision layers): no layer shows more than six primary decisions, with missions and the mine selector excluded.

D21. Crisis flags follow current values.
`riches_found_review_mine_crisis_flags` runs on every controller pulse: crisis_active is raised and lifted with the three value crises, crime_crisis lifts once Local Order is back in the stable band, and administration_compromised once Revenue Legitimacy is stable and illicit capture is below its gate.
A raid crisis is no longer raised by severe pressure; each raid records `riches_found_last_raid_date`, the crisis ends after `riches_found_duration.raid_memory_days` (an existing, previously unused constant) without a raid, and Army Cordon, Clear the Claimant Barricades and a Mine Truce end it at once.
A severe mutiny is a wage dispute that has broken local order, which gives the flag a producer; worker cooperatives, a dividend, local revenue or a truce settle a wage dispute.
Army Cordon is visible with a supplied force in either overlay when a raid crisis, a war or an order crisis gives it cause (lead decision 1), so Hold the Mine During War can start.

D22. Gold Disease duplicates (lead decision 3).
While Gold Disease is active its own quarantine, workforce replacement and sealing replace the baseline emergency versions.
The baseline quarantine required an active Gold Disease, so hiding it would have left it unreachable; it now serves a district that keeps Gold Disease susceptibility after containment, which spec part 3 allows ("Gold Disease or another defined internal contamination of behavior") and which still restricts the movement routes.

D23. Port Route only where rail does not serve (lead decision 2): Port Route needs a port route and an invalid rail route, so islands and railless coasts only.

MCP routes for D20 to D23: a narrow `hoi4_decision_inspect` (`inspect` mode, `decision_riches_found_army_cordon`, one declared wartime raid scenario) returned only a workspace-wide `DECISION_ANALYZED_PARTIAL` result with a failed coverage check, so the layer counts rest on the source enumeration. No `ai_will_do` block changed in this tranche.

D24. Retain the Administration is reachable.
No Event 029 file set `riches_found_previous_administration_valid`, so the occupier's Retain the Administration (one of the seven occupation actions in spec part 3 and a Claim Jumper settlement route) could never be taken.
`riches_found_record_previous_administration` now sets it when an occupation begins or passes to a new occupier and the mine has a working civil administration (camp administration built, not compromised, no private enclave, no Gilded Sovereignty); `riches_found_clear_occupation_state` lifts it when the occupation ends, and the refresh lifts it as soon as the administration is compromised.
Source trace: `riches_found_handle_state_control_change` calls `riches_found_handle_occupation_change`, which records the administration before the presentation refresh puts the occupier in the occupation layer, where the decision needs only an open mine, the record and no imminent retreat.

D25. Achievement history has producers and Claim Jumper is per controller (lead decisions 6, 7 and 8).
Foreign military intervention is recorded by `riches_found_mark_foreign_intervention` for a raid by foreign agents or a hostile neighbour, a foreign-supported armed group or seizure incident, and capture by a foreign country at war with the owner; bribes, inspections, sanctions and offers are not recorded.
The permanent history flag is `riches_found_foreign_intervention_history`; the No Man Owns the Mountain disqualifier (`riches_found_achievement_foreign_intervention_recorded`) is set only once the mine has Gilded Sovereignty history, because the achievement prompt asks for a recovery from that authority without foreign military intervention and a wartime capture years earlier is not part of that recovery (agent decision).
Claim Jumper reads one per-controller flag, `riches_found_claim_jumper_settled`, set beside the four settlement history flags, and every controller change clears it with the hold deadline, ready state and invalidation; the four history flags stay, because Resource Curse and Gold Disease containment read the replaced-administration flag.
The never-set transfer invalidation, the two never-set All That Glitters flags (its started-window `permanent_loss` already covers a break during verification) and the imminent-breach check in Close the Account were removed from the achievement checks; the breach flag stays an AI input only.
`riches_found_check_pay_train_route` produces `riches_found_pay_train_route_lost` when the route is damaged during an active pay train, from the raid that damages it and from each pulse, so Protect the Pay Train fails and the pay train run ends.
A scripted read-versus-set comparison over every Event 029 file finds no flag read by the achievement triggers or effects without a producer.

D26. Event 029 changes the Chaos Meter once per source and mine (lead decision 5).
`riches_found_apply_chaos_source` calls the shared `add_chaos_meter_value` with `chaos_history_reason_custom = 1`, the new history reason `chaos_meter_history_reason.special.riches_found` and the controller saved as `chaos_history_actor`, following the Event 002 and Event 008 precedents.
Sources and changes (constants `riches_found_chaos_change`): a completed public settlement -4; a claim war (claim jumpers, a violent eviction or a rival claimant) +3; a destructive or lethal raid +3; an uncompensated or violent nationalization +4; mass death inflicted by people +10 (a collapse's deaths count as the collapse, not a massacre); foreign military intervention +8; a catastrophic collapse +10; a demonic bargain or the opening of the Bottomless Account +12 (one source, so the account does not add a second bargain).
Each source sets its own receipt flag on the mine, so none can be farmed through closure, reopening, repeated raids or transfer.
The reason id 260 sits apart from the sequential ids so concurrent owners appending to the shared list do not collide; the shared constant and the scripted-localisation lookup were added as single minimal hunks, and the history text lives in the Event 029 localisation file so the shared localisation file is untouched.
Tooltips on the seizures, the bargain and the public settlement mission state the change.

D27. Every AI and incident input has a producer.
A read-versus-set comparison of every `has_state_flag` and `has_country_flag` in the Event 029 files now finds no flag without a producer.
Producers added: `riches_found_multiple_mine_priority` (controller with two or more mines), `riches_found_transport_need` (no route), `riches_found_transport_ready` (route with capacity), `riches_found_worker_claim_war` (wage dispute beside armed claimants or armed workers), `riches_found_allied_target_available` (current offer from a faction partner), all derived on each refresh; `riches_found_failed_audit` on a failed concession audit, which also lets the MTTH failed-audit factor of Evolution I apply (RF_TEST_EVO1_02_CAPTURED); `riches_found_nationalized_without_compensation` on that decision, so the Threaten Sanctions incident can fire; `riches_found_foreign_operation_active` for `foreign_operation_memory_days` (an existing, previously unused constant) after a hostile actor's interference incident; `riches_found_smuggling_route` for the new `smuggling_route_memory_days` after smuggling, guard theft or false permits; `riches_found_foreign_contract_network` on a partner from its first to its last contract; and `riches_found_account_breach_imminent` from the warning date until payment, breach or closure.
Earlier items produced `riches_found_severe_mutiny` and `riches_found_retreat_imminent` (D21, D20) and `riches_found_pay_train_route_lost` (D25).
Removed as dead reads, which changes no weight because they never held: the occult-network factor on Seek Occult Assistance and the occupation-state factor on Reopen the Occupied Mine (no system defines either), and the unused target-exclusion and terminal-site markers in `riches_found_state_is_excluded_target`.
Probability evidence: the producers turn on existing `ai_will_do` factors and one MTTH factor, so a same-scenario comparison is required. A narrow `hoi4_probability_inspect` (adapter `decision_ai_will_do`; candidates `decision_riches_found_truce`, `decision_riches_found_trade_access_infrastructure`, `decision_riches_found_processing_works`; source path `common/decisions/029_riches_found_decisions.txt`) returned `INTERNAL_ERROR` on 2026-10-05, so the baseline and comparison remain blocked by that route; the pre-change source is the parent of this tranche's commit for a later same-fixture comparison.

D28. Opening values follow the state and occupied output follows resistance.
Spec part 1 asks the starting values to vary with the state; `riches_found_apply_starting_conditions` adds constant deltas (`riches_found_starting_value`) at discovery for the owner's stability bands, core or non-core status, infrastructure level, war or local resistance, a high Chaos Meter, democratic government and the deposit profile, and the values are clamped afterwards.
Spec part 3 asks occupied output to fall with resistance, low compliance, damaged transport and non-core status; the occupied control factor is multiplied by one minus resistance times `resistance_slope`, plus compliance times `compliance_slope`, then by `damaged_route_factor` for a damaged route and `non_core_factor` when the state is not the occupier's core, clamped between `floor` and `cap` (`riches_found_occupied_output`).
Resistance, compliance, infrastructure and stability are the engine's state and country dynamic variables (`dynamic_variables_documentation.md`); they are read only at discovery and at the contribution refresh, with no new scan.

D29. Rail Spur lays a real railway (lead decision 4; supersedes the D11 railway limitation).
`effects_documentation.md` (`build_railway`, option 3) takes a start and target state, and vanilla `common/national_focus/soviet.txt` lays railways with `start_state = ROOT.capital` and `target_state = THIS.capital` behind `can_build_railway`, so the D11 reading was wrong.
When Open the Railhead succeeds on a rail route, `riches_found_lay_mine_railway` runs in the controller's scope with `start_state = PREV` (the mine), `target_state = THIS.capital`, level 1, `build_only_on_allied = yes` and `fallback = yes`, guarded by `can_build_railway` with the same arguments, and skipped when the mine is the capital; `riches_found_railway_laid` marks it once.
The Rail Spur's infrastructure level is still added when the decision completes.
Whether the railway appears on the map needs the live game.
