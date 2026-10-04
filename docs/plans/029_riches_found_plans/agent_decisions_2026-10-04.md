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
