# Event 033 decision and mission audit, 2026-10-03

Disposition: actionable read-only audit, with mandatory MCP decision and probability evidence blocked or unresolved as recorded below.
The author changed only this handoff.
No gameplay, AI weight, GUI, shared event log, pacing, achievement, migration, validator, or spreadsheet source was changed, and no commit was made.
The parent owns fixes and final review.

## Scope and source identity

The latest parent request authorizes review of four permanent projects, five urgent actions, four recovery actions, their costs, quotes, eligibility, reservations, refunds, durations, targets, interruption, and paid AI.
The exact cost matrix and coding/decision prompts are the comparison basis, rather than a newly chosen balance target.
Recommendations below are proposals within that scope, not implemented or automatically accepted design changes.
The protected migration commit is `f26768187`.
At inspection the repository HEAD was `33a6c622afa1ee09fad8aec463b5880f241025d4`, with substantial concurrent work preserved.

Root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Current `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` guidance was read and applied.
GUI presentation changes and visual completion are outside this bounded pass.
The scripted-GUI skill was inspected earlier in the task, but no GUI acceptance is claimed here.

The requested `common\scripted_triggers\033_acid_rain_preparedness_triggers.txt` is absent.
Its relevant definitions were recovered by exact identifier search in `common\scripted_triggers\033_acid_rain_triggers.txt:288-605`.
This filename gap did not prevent source review, and does not establish MCP coverage.

| Inspected source | SHA-256 |
| --- | --- |
| `common\decisions\033_acid_rain_decisions.txt` | `E72D281DABD6F699A4248062AEC34817ED921C14F0DE6B541531F4306D213679` |
| `common\scripted_effects\033_acid_rain_preparedness_effects.txt` | `CECBFFDFC281FCECA23AF4764D3C3E1C3D276BC6257C4B9E04BA4143DDEB1C6A` |
| `common\scripted_triggers\033_acid_rain_triggers.txt` | `6686EC5F09D9745A51113DC6DE142AA641784AB80E178440B0DDECE194369944` |
| `common\scripted_localisation\033_acid_rain_scripted_localisation.txt` | `0194D8BC4DB4522DFEE9DDB09F7A0C2E56DBE342D8BA0CEE73B0C3090CA76F45` |
| `common\script_constants\033_acid_rain_constants.txt` | `2AE19FA866A83B6626653B7A27C3024E6361E8B9532A901405B3D4D97D6A9425` |
| `common\scripted_effects\033_acid_rain_effects.txt` | `9BDFB2ABFA1A29BEA9FDF073026DB787E2597295EE7B02AA0FE7F25DA1FA8D53` |
| `common\decisions\categories\033_acid_rain_categories.txt` | `FA9EBD20F67157126B0BCEA1F162D38F0D6675A0BD92BE693479F8073D3AEB7D` |
| `common\dynamic_modifiers\033_acid_rain_dynamic_modifiers.txt` | `7EC577585356769CF4944EA5D29D37A30B9265FA60918D0960CF89F1DF6D521F` |
| `docs\specs\033_acid_rain_specs\matrices\033_acid_rain_decision_cost_matrix.md` | `4137985C9A4F5938F6BD6AEA2AFFA1AE9A9BA664DAF3BF9EA7F7EB9298B5BB00` |
| `docs\specs\033_acid_rain_specs\prompts\033_acid_rain_decision_mission_prompt.md` | `54623863E38164BE78BF35AB8DCA14E1547759F3010FB9C00299AA0ECD3EA190` |
| `docs\specs\033_acid_rain_specs\prompts\033_acid_rain_coding_prompt.md` | `E5891447B94C27AA89135BE6837B5E98D67E97B4D0CC40BD21558699270BDA2B` |

The five principal gameplay/quote files retained those hashes at the final source identity check.
Other agents' existing achievement calls, GUI-only localisation additions, and constant aliases were preserved.

## Findings sorted by severity

### Critical: public quotes are disconnected from their persistent rows

All 13 public decisions read one generic `acid_rain_quote_*` set in `custom_cost_trigger`.
All require `has_variable = acid_rain_quote_duration_days` and `has_variable = acid_rain_quote_civilian_factories`.
Neither variable has a writer in the inspected engine source.
The actual loaders use temporary `acid_rain_quote_days` and `acid_rain_quote_civ`, with different names, at preparedness effects lines `9-16`, `421-434`, and `598-611`.
Their other generic quote fields are temporary transaction scratch, not a persistent per-country public row.
They cannot provide a country's pre-click quote in a later independent decision trigger/localisation evaluation.

The persistent project values are `acid_rain_<component>_next_<resource>` at effects `264-305`.
The persistent action values are `acid_rain_action_<resource>_entries^<action_id>` at `568-590`.
Refreshes occur during country recalculation and bounded runtime work, and again from the decision completion aliases at `335-344`.
The public cost blocks and cost localisation do not consume those persistent row values.
Row selection occurs only inside each `complete_effect`, after the public quote was needed.

The four public project timers also read the unwritten `var:acid_rain_quote_duration_days?1` at decisions `121`, `186`, `252`, and `318`.
The fallback is one day, whereas the actual project receipt/end date uses the loaded matrix duration at effects `692-694`.
The source therefore does not establish a matching displayed quote, native timer, availability row, and actual debit.
The generic custom-cost predicate is false in a fresh record because its mandatory aliases are absent.
Whether that false predicate independently prevents native selection was not observed, and is not assumed below.

### Critical: the four permanent project slot checks use an unwritten capacity

`acid_rain_country_has_free_project_slot` reads `acid_rain_country_project_capacity` at triggers `325-331`.
Country initialization and recalculation write `acid_rain_project_capacity`, at runtime effects `576`, `678-687`, `778-787`, and `989-999`.
No writer for the trigger's name was found.
With an unset capacity read as zero, a fresh `acid_rain_active_projects = 0` cannot satisfy `0 < 0`.
This affects both the four public `available` blocks and `acid_rain_start_project` at effects `668-674`.
It is an availability defect independent of the custom-cost uncertainty.

### High: action manpower is removed twice, then returned once

`acid_rain_debit_loaded_quote` removes `acid_rain_quote_manpower` at effects `633-635`.
`acid_rain_start_action` calls that helper at `925`, records one reservation at `933`, and removes the same manpower again at `936`.
`acid_rain_release_current_action_commitments` returns one quote at `1019-1023`.
The permanent project path has one manpower debit and a captured reservation, so this second debit is an action-path defect.

Affected public actions: Shelter Protocols, Emergency Water, Medical Surge, Evacuation, Decontamination, and Industry Recovery.
For a C-band Medical Surge the matrix reservation is 1,000.
Under the intended row, starting with 11,000 manpower passes the implemented 1,000 quote plus 10,000 deployment reserve requirement, but two debits leave 9,000.
Normal completion returns 1,000, leaving a permanent 1,000 loss.
This is source arithmetic under that loaded-row assumption, not an observed campaign result.

### High: national Water and state-targeted actions lack valid start targets

Both urgent Water rows set `acid_rain_quote_target_required = 1` at effects `462` and `472`, although the public Water decision is national and supplies no state pointer.
The target-required start whitelist at `898-920` only accepts evacuation or recovery actions.
Water therefore cannot pass that branch even if an unrelated state pointer happens to exist.

The four state-targeted public decisions are Evacuation and the three state recoveries.
Their `complete_effect` blocks at decisions `660-664`, `740-744`, `812-816`, and `884-888` only set an action number, refresh quotes, and call start.
None copies `FROM` into `acid_rain_selected_action_state` or the action target id.
The only resolver at effects `798-812` reconstructs an already stored `acid_rain_action_target_state`, and is called on completion/release rather than on a new start.
After normal release both target fields are cleared.
A fresh state-targeted click consequently has no target for the transaction gate.
A retained pointer would not prove it names the currently selected `FROM`.

### High: action refunds reload mutable pricing rather than the paid reservation

Action start stores the action id, end day, generation, and country totals, but does not capture an immutable manpower/civilian-factory reservation receipt.
Release reloads the action's current quote array at `1017-1020`.
Runtime recalculation refreshes every action quote at runtime effects `815-816` and `4466-4467`, including during a running operation.
Country bands can change on control transfer and industry changes.

For example, an A Medical row quotes 650 reserved manpower and a D row quotes 1,350.
If the row is refreshed after such a band change, release returns 1,350 and subtracts it from a ledger that originally recorded 650.
That can make the commitment ledger negative and produce an incorrect return.
The separate double debit does not make a mutable refund correct.
Projects already capture `acid_rain_project_manpower_entries` and `acid_rain_project_civ_entries`, which is the safer existing pattern to mirror.

### High: D-band recovery factory payment, commitment, and affordability disagree

Recovery base civilian-factory cost is one before band scaling.
The action loader scales it at effects `559`, so band D quotes two.
The shared loaded-quote payment gate supports two factories, but the persistent recovery payment helpers at triggers `554-604` only accept civilian quotes of zero or one.
The start path adds only `acid_rain_action_commitment_one` at effects `937`.
That modifier reserves exactly one factory at dynamic modifiers `147-150` and constants `611`.
Thus D-band Transport, Decontamination, and Industry recoveries quote and record two while committing one.
Wiring the existing persistent helper without fixing its two-factory branch would instead block those D rows entirely.

### High: project cancellation leaves the active visibility flag set

`acid_rain_cancel_project` at effects `754-776` returns captured reservations and clears active ledger entries, but never clears the matching `acid_rain_project_<component>_active` flag.
All four public project decisions hide behind that flag.
Normal project completion clears it at `738-741`, and full country initialization clears it at runtime `553-556`.
Demobilization and administrative interruption call cancellation without reinitializing the country.
A cancelled component can therefore remain hidden for the rest of the same generation.
The captured project ledger does correctly guard against a second reservation return when its active entry has been cleared.

### High: evacuation timing and the promised partial effect are not implemented together

The matrix duration is exactly seven days in both land and island variants.
Part 5 lines `275-284` explicitly grants partial protection after one full day and full protection on completion.
The decision prompt requires completion before the first severe pulse for full protection.

Both actual forecast leads are three days: constants `1032` (`severe_forecast_lead_days`) and `1071` (`superstorm_lead_days`).
The planners use them at runtime effects `3294-3315` and `4025-4038`.
This conclusion uses the actual cell/episode planners, not the separate three-day evolution notification.
A new seven-day operation selected when those forecasts are published cannot complete by their three-day arrival.

The only production mortality read found is `has_state_flag = acid_rain_evacuated` at runtime `2423-2425`.
That flag is set only when `acid_rain_apply_action_effect` runs on completion at preparedness effects `828-835`.
No mortality check reads `acid_rain_action_start_day` to award the specified one-day partial effect.
The current start/completion receipt also lacks the forecast visit/episode identity used by the target planner.
Generation equality alone cannot distinguish successive forecasts in one Event 033 generation.
The tooltip's one-day partial-protection claim is therefore unsupported by the inspected effect path.
The owner must resolve the seven-day/full-before-first-impact contract without silently choosing a shorter duration or a new forecast lead.

### Medium: action concurrency is narrower than the documented caps

`acid_rain_country_has_free_action_slot` permits only one `acid_rain_national_action_active` operation in the entire country.
There is one country action id, target, timer, and reservation ledger.
This serializes all national actions, recovery actions, and evacuation starts.
Part 5 permits one active version of each national action and two/four/eight simultaneous state evacuations by band.
The public evacuation cap checks completed/protected states through `acid_rain_evacuations_active`, which increments at completion, rather than counting in-progress operations.
Removing the single-operation guard alone would overwrite targets and reservations, so the concurrency gap requires parent/architect ownership rather than a one-line relaxation.

After fixing the capacity alias, a D country with the global extra-capacity condition can also calculate `3 + 1 = 4` permanent project slots at runtime `778-787`.
The decision prompt limits this to three.
The parent should keep the accepted global exception but enforce its maximum explicitly.

### Medium: demobilization is unavailable when its cancellation work is needed

The public Demobilize decision requires the entire runtime to be inactive, zero active projects, and zero active evacuations at decisions `908-920`.
Its effect cancels unfinished projects and returns their reservations at preparedness effects `779-790`.
That cancellation purpose cannot be reached from this decision while any project is active.
Part 5 specifies local exposure ending, rather than world-wide Event 033 dissipation, as the gate.
Standalone medical fatigue is also absent from the demobilization/category visibility alternatives.
The source can therefore leave a locally quiet country waiting on the global event, or with fatigue and no relevant visible cleanup action.

### Medium: medical fatigue is written but never blocks another surge

Medical completion sets `acid_rain_medical_fatigue` at preparedness effects `819`, with the same 21-day length as the protection effect.
Exact source search found its setters and clears, but no `has_country_flag` consumer that gates another Medical Surge.
The Medical public `available` block at decisions `477-486` requires a general free action slot and local threat, without a fatigue check.
Once the previous operation finishes, another surge can start while that fatigue flag remains set.
The advertised fatigue cooldown is consequently absent from the inspected gameplay gate.
The generic start transaction also omits the public stale-runtime and national threat checks, so the fresh payment defense does not fully mirror the action's public requirements.
Add those existing requirement rechecks before debit, with a precise player-facing blocked reason for fatigue.

### Medium: recovery variants share broad targeting and common tier reduction

All three state recovery entries target any controlled unresolved aftermath state using substantially identical gates.
`acid_rain_apply_recovery_result` lowers one common aftermath tier at effects `970-1014`.
The transport and industry modifiers have real infrastructure/railway and factory repair-speed effects at dynamic modifiers `125-145`.
They must not be dismissed as cosmetic.
However, the current target gates do not require the corresponding type of damage, and the helper does not reconcile an Event 033-specific damaged-building receipt before granting that repair speed.
The tooltip promise that repairs affect only rain-recorded damage is therefore stronger than the source evidence.
Decontamination supplies a resource/supply/construction modifier plus common aftermath reduction, without a distinct environmental-pressure debit in this helper.
The expensive variants can substitute for one another in the same common tier loop.
Priority, harm-specific applicability, and outcome distinctions need owner review before accepting the advertised recovery behavior.
No inspected recovery effect erases Deaths history or subtracts previously added Air Contamination.

### Medium: visibility can exceed the action budget

A quiet country during the live runtime can show four unfinished project families plus the four recovery families when it retains aftermath/commitments.
A threatened country can show five urgent families plus recovery entries whose `visible` remains true while their `available` is false.
Each eligible target can multiply the three state recovery rows.
This exceeds the six-primary-action content budget in reachable source states.
These are source visibility counts, not a clipping or render claim.
The parent should phase recovery visibility with local urgent activity and expose only actions relevant to the selected harm/target, while retaining accepted gameplay.

## Exact row evidence

All row references below are in `common\decisions\033_acid_rain_decisions.txt`.
Persistent caches exist, but no public row currently obtains its correct quote from them before selection.
Every row shares the quote/key problem described above.
All counts include factory commitments and manpower reservations as spendable types.

| Public id suffix after `chaosx_acid_rain_` | Definition / completion / duration line | Authoritative stored row | Matrix duration | Types | Additional row findings |
| --- | --- | --- | --- | ---: | --- |
| `project_shelter` | `76 / 122 / 121` | `acid_rain_shelter_next_*`, project `1` | `21,25,29,34` for tiers 1-4 | 3 | Capacity alias blocks, native duration wrong alias, cancellation flag remains |
| `project_water` | `141 / 187 / 186` | `acid_rain_water_next_*`, project `2` | `21,25,29,34` | 4 | Same project issues, loader correctly zeros train or convoy according to country route |
| `project_medical` | `207 / 253 / 252` | `acid_rain_medical_next_*`, project `3` | `24,28,33,39` | 4 | Same project issues, captured reservation is single-debit |
| `project_transport` | `273 / 319 / 318` | `acid_rain_transport_next_*`, project `4` | `24,28,33,39` | 4 | Same project issues, archetype gate versus concrete truck debit needs alignment |
| `urgent_shelter` | `347 / 392 / 391` | action `1` | 14, effect 21 or exposure end | 3 | Double manpower, mutable return, no explicit exposure-end clearing in tail helper |
| `urgent_water` | `405 / 450 / 449` | action `2` land or `3` island | 21, effect 30 | 3 | Impossible target-required branch, double manpower, route must be identical in quote/gate/start |
| `urgent_medical` | `464 / 509 / 508` | action `4` | 14, effect 21 plus fatigue | 3 | Double manpower violates reserve floor, fatigue has no blocking consumer |
| `urgent_transport` | `523 / 568 / 567` | action `5` | 14, effect 21 | 3 | Paid consumed resources, stale start rechecks incomplete, truck type alignment |
| `urgent_evacuate` | `583 / 660 / 659` | action `6` land or `7` island | 7, severe episode | 4 | No FROM binding, no one-day partial effect, arrival conflict, episode receipt and in-progress cap gaps |
| `recovery_transport` | `680 / 740 / 739` | action `11` | 28 | 4 | No FROM binding, D factory mismatch, broad harm gate, mutable factory return |
| `recovery_decontaminate` | `752 / 812 / 811` | action `12` land or `13` island | 35 | 4 | No FROM binding, double manpower, mutable return, D factory mismatch, route OR is not target-gated |
| `recovery_industry` | `824 / 884 / 883` | action `14` | 35 | 3 | No FROM binding, double manpower, D factory mismatch, rain-only repair claim not proved |
| `recovery_demobilize` | `897 / 943 / 942` | action `15` | 7 | 1 | Gate excludes active reservations it is meant to cancel, no fixed verified PP hint |

### Permanent project matrix comparison

The mechanical read-only comparison found **80 rows, 384 scalar duration/cost checks, zero mismatches** between the exact matrix and `acid_rain_project_cost` constants at `616-950`.
A separate dispatch check found **64 project loader branches, zero wrong band/tier constant bindings** in preparedness effects `24-155`.
An additional assignment check found zero wrong component/resource bindings in those loaders.
Water's land and island views share each of its 16 loader branches.
Preparedness gains are the intended `7.5 / 6.25 / 6.25 / 5` per tier and total 100 at four tiers each.
These facts prove source table/dispatch agreement, not successful engine payment or the broken public quote path.

Each cell below lists the exact source tuple for tiers 1, 2, 3, 4 in that order.
`F` is temporarily committed civilian factories, `S` consumed support equipment, `M` reserved manpower, `T` consumed trains, `C` consumed convoys, `V` consumed trucks, and `U` consumed fuel.

| Project / band | Resource order | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
| --- | --- | --- | --- | --- | --- |
| Shelter A | F,S,M | 1,59,700 | 1,74,900 | 2,91,1100 | 2,112,1300 |
| Shelter B | F,S,M | 1,77,900 | 2,96,1100 | 2,119,1400 | 2,146,1700 |
| Shelter C | F,S,M | 1,90,1000 | 2,113,1300 | 2,140,1600 | 2,171,1900 |
| Shelter D | F,S,M | 2,122,1400 | 2,152,1700 | 3,189,2100 | 3,231,2600 |
| Water land A | F,S,T,M | 1,39,1,400 | 1,49,1,500 | 2,61,2,600 | 2,75,2,700 |
| Water land B | F,S,T,M | 1,51,1,500 | 2,64,2,600 | 2,80,2,700 | 2,97,2,900 |
| Water land C | F,S,T,M | 1,60,1,500 | 2,75,2,700 | 2,93,2,800 | 2,114,2,1000 |
| Water land D | F,S,T,M | 2,81,2,700 | 2,102,2,900 | 3,126,3,1100 | 3,154,3,1300 |
| Water island A | F,S,C,M | 1,39,4,400 | 1,49,5,500 | 2,61,6,600 | 2,75,7,700 |
| Water island B | F,S,C,M | 1,51,5,500 | 2,64,6,600 | 2,80,7,700 | 2,97,9,900 |
| Water island C | F,S,C,M | 1,60,5,500 | 2,75,7,700 | 2,93,8,800 | 2,114,10,1000 |
| Water island D | F,S,C,M | 2,81,7,700 | 2,102,9,900 | 3,126,11,1100 | 3,154,13,1300 |
| Medical A | F,S,M,U | 1,78,700,200 | 1,98,900,250 | 2,121,1100,300 | 2,149,1300,350 |
| Medical B | F,S,M,U | 1,102,900,250 | 2,128,1100,300 | 2,159,1400,350 | 2,194,1700,450 |
| Medical C | F,S,M,U | 1,120,1000,250 | 2,150,1300,350 | 2,186,1600,400 | 2,228,1900,500 |
| Medical D | F,S,M,U | 2,162,1400,350 | 2,203,1700,450 | 3,252,2100,550 | 3,308,2600,650 |
| Transport A | F,T,V,U | 1,1,17,200 | 1,1,21,250 | 2,2,26,300 | 2,2,31,350 |
| Transport B | F,T,V,U | 1,1,22,250 | 2,2,27,300 | 2,2,33,350 | 2,2,41,450 |
| Transport C | F,T,V,U | 1,1,25,250 | 2,2,32,350 | 2,2,39,400 | 2,2,48,500 |
| Transport D | F,T,V,U | 2,2,34,350 | 2,2,43,450 | 3,3,53,550 | 3,3,65,650 |

Shelter and Water durations for every band are `21,25,29,34`.
Medical and Transport durations for every band are `24,28,33,39`.
They do not scale by country band.

### Urgent and recovery band quotes

Base values at constants `952-1008` agree with the matrix.
The loader uses the final band multiplier and `round(base × multiplier + 0.49)` at effects `558-565`.
For every currently authored base value in the table this equals the matrix's upward whole-item rounding.
The table records intended loaded quotes before the double debit and refund defects, not observed expenditures.
`P` is consumed political power and the other abbreviations retain the meanings above.

| Action variant | Resource order | A, 0.65 | B, 0.85 | C, 1.00 | D, 1.35 |
| --- | --- | --- | --- | --- | --- |
| Shelter Protocols | P,S,M | 17,39,325 | 22,51,425 | 25,60,500 | 34,81,675 |
| Emergency Water land | S,T,M | 52,2,325 | 68,2,425 | 80,2,500 | 108,3,675 |
| Emergency Water island | S,C,M | 52,7,325 | 68,9,425 | 80,10,500 | 108,14,675 |
| Medical Surge | S,M,U | 91,650,325 | 119,850,425 | 140,1000,500 | 189,1350,675 |
| Reroute Transport | T,V,U | 2,26,488 | 2,34,638 | 2,40,750 | 3,54,1013 |
| Evacuation land | M,V,T,U | 650,33,2,488 | 850,43,2,638 | 1000,50,2,750 | 1350,68,3,1013 |
| Evacuation island | M,C,V,U | 650,13,33,488 | 850,17,43,638 | 1000,20,50,750 | 1350,27,68,1013 |
| Transport Recovery | F,T,V,U | 1,2,26,488 | 1,2,34,638 | 1,2,40,750 | 2,3,54,1013 |
| Decontamination land | F,S,M,T | 1,65,650,2 | 1,85,850,2 | 1,100,1000,2 | 2,135,1350,3 |
| Decontamination island | F,S,M,C | 1,65,650,7 | 1,85,850,9 | 1,100,1000,10 | 2,135,1350,14 |
| Industry Recovery | F,S,M | 1,78,650 | 1,102,850 | 1,120,1000 | 2,162,1350 |
| Demobilization | P | 7 | 9 | 10 | 14 |

## Cost validation, localisation, and shared helper evidence

The `NOT = { has_equipment = { <type> < <quote> } }` form is an inclusive affordability check: exact stock passes, and one item below fails.
The offline trigger table explicitly permits a variable amount.
Installed vanilla `_exiled_governments_decisions.txt:475-481` computes a temporary amount in `available` and uses it directly as the `has_equipment` RHS.
The claim in the local reserve-helper comment that stockpile triggers cannot accept variable RHS values is contradicted by that precedent.
No replacement of these valid comparisons is recommended merely because they use variables.
Installed dynamic-variable documentation at `431-433` and `743-744` documents both `has_political_power` and the `political_power` country reader, so the shared `check_variable` reader is not flagged as an invalid token.

Installed vanilla `AFG_recruit_turkestan_legion` at `AFG.txt:1685-1747` repeats equipment affordability in `available` and `custom_cost_trigger`, then explicitly debits equipment in `complete_effect`.
Installed `_documentation.md:18-22` states that `available` controls whether a visible decision can be taken.
The offline Decision modding section `305-335` documents custom-cost normal/blocked text, its tooltip suffix, and the absence of automatic payment.
It does not establish that a false custom-cost trigger alone blocks selection.
This audit consequently does not infer native selection behavior from a red cost row.
All 13 public `available` blocks lack their authoritative row affordability predicate, even though matching persistent helpers already exist.

The existing row predicates are at triggers `424-605`:

| Decision family | Existing predicate to review and wire into both `available` and `custom_cost_trigger` |
| --- | --- |
| Shelter project | `acid_rain_country_can_pay_project_shelter` |
| Water project | `acid_rain_country_can_pay_project_water` |
| Medical project | `acid_rain_country_can_pay_project_medical` |
| Transport project | `acid_rain_country_can_pay_project_transport` |
| Shelter urgent | `acid_rain_country_can_pay_action_shelter` |
| Water urgent | `acid_rain_country_can_pay_action_water` |
| Medical urgent | `acid_rain_country_can_pay_action_medical` |
| Transport urgent | `acid_rain_country_can_pay_action_transport` |
| Evacuation | `acid_rain_country_can_pay_action_evacuate` |
| Transport recovery | `acid_rain_country_can_pay_recovery_transport` |
| Decontamination | `acid_rain_country_can_pay_recovery_decontaminate` |
| Industry recovery | `acid_rain_country_can_pay_recovery_industry` |
| Demobilization | `acid_rain_country_can_pay_recovery_demobilize` |

The Water, Evacuation, and Decontamination predicates currently OR their land/island prices without requiring the branch that matches the selected country/state route.
They can accept the cheaper wrong route if wired as-is.
The predicates must select the same route used by display and start before affordability is accepted.
Transport's persistent predicates test concrete `motorized_equipment_1`, whereas the loaded/shared/public gates test the archetype `motorized_equipment` and debit the concrete type.
The resource definition used for payment and availability must be identical, with any all-variant stockpile behavior verified rather than assumed.

None of these three custom-cost families exists in any searched localisation file, nor do their `_blocked` or `_tooltip` keys:

- `acid_rain_project_dynamic_cost`
- `acid_rain_urgent_action_dynamic_cost`
- `acid_rain_recovery_action_dynamic_cost`

The different `acid_rain_dynamic_cost`, `_blocked`, and `_tooltip` keys exist at `033_acid_rain_l_english.yml:77-79`, but are not the keys used by decisions.
Those strings also read the unwritten duration/factory aliases and temporary generic fields.
Changing only the three key names to the existing generic key would leave the wrong-row defect intact.
Cost localisation ownership in this report is confined to those decision strings and the first 98 lines of scripted localisation.
The appended GUI-only selectors are not recommended for modification.

Every intended spendable family has a matching existing texticon:

| Value | Current token | Definition evidence |
| --- | --- | --- |
| Political power | `£pol_power` | Vanilla `interface\texticons.gfx:262`, `GFX_pol_power` |
| Civilian factories | `£civ_factory` | Vanilla `interface\texticons.gfx:172`, `GFX_civ_factory` |
| Manpower | `£manpower_texticon` | Vanilla `interface\texticons.gfx:111` |
| Support equipment | `£support_equipment_text_icon` | Mod `interface\chaosx_texticons.gfx:90` |
| Trains | `£GFX_train_texticon` | Vanilla `interface\texticons.gfx:2563`, actual vanilla cost use in `SEA_decisions_l_english.yml:747-748` |
| Convoys | `£convoy_texticon` | Vanilla `interface\texticons.gfx:34` |
| Motorized equipment | `£GFX_motorized_equipment_text_icon` | Mod `interface\chaosx_texticons.gfx:95` |
| Fuel | `£GFX_fuel_texticon` | Vanilla `interface\texticons.gfx:123` |

No row has a fifth distinct cost type in the authored matrix.
There is no literal-resource-name fallback in the intended cost fragments at localisation `81-96`.
The generic strings would print four nonzero values on four-cost rows, exceeding the skill's three-value inline presentation limit if connected unchanged.
The complete tooltip must retain the fourth cost explicitly and distinguish reserved manpower/factories from consumed resources.
The generic blocked string colors every printed cost red rather than identifying only the missing resource.
Native rendered fit and resolved texticon appearance remain unverified in this pass.

## Category, mission, and interruption notes

The category retains itself for active runtime, recovery tail, a running action, projects, evacuation receipts, commitments, or unresolved controlled-state aftermath at categories `10-24`.
The global-active alternative is not filtered to a valid country in the metadata, though public project/urgent rows generally apply the runtime-record gate.
`visible_when_empty = no` can suppress an otherwise retained category if every row is hidden.
Player-facing Preparedness has a clear range and direction through the four component descriptions and gains.
No decision-specific next-tier price or completion date is currently connected to its public row.
The lengthy category/decision descriptions are not substitutes for a current quote, missing-resource reason, local arrival comparison, or target requirement.

| Timed family | Owner / category / region | Requirement and duration | Success | Failure/interruption | Duplicate/cap risk |
| --- | --- | --- | --- | --- | --- |
| Permanent components | Country, Event 033 category, national | Next component tier, project slot, physical quote, tier-specific 21-39 days | Component tier plus 7.5/6.25/6.25/5 Preparedness, captured commitments released | Captured reserves returned, consumed resources retained, no tier granted | Four distinct components, but cancellation flag hides cancelled family and effect-time duplicate-active check is missing |
| Four national urgent families | Country, same category, national | Local warning/exposure, fixed 14/21-day operations | Family protection window | Country/administrative cleanup clears running receipt and returns reservation, subject to double-debit/mutable-return defects | One global operation slot suppresses permitted parallel distinct families, Water cannot start |
| Evacuation | Acting country and selected forecast state | Current severe/superstorm forecast, 7 days, partial after 1 promised | State protection receipt and later release of active protection count | Control change or stale target records interruption, consumes equipment, releases reservation | No FROM binding, no partial effect, one in-progress operation, no bound episode identity |
| State recovery | Acting country and selected controlled aftermath state | Relevant harm should be required, 28/35 days | Common aftermath tier decrement plus family modifiers | Target lost or resolved before completion gives no success, releases commitments | Three broad target gates/common result overlap, state rows multiply |
| Demobilization | Country, national | Local exposure ended, 7 days, political cost | Cancels project ledger and clears fatigue | Must retain consumed costs and reject stale exposure state | Current public gate excludes active project commitments and uses global runtime ending |

There are no active replacement native timeout missions in this decision package.
The two legacy save identities at decisions `52-70` have `allowed`, `activation`, and `available` set to `always = no`, immediate cancellation, and no weather/payment/timeout effects.
They belong to the protected migration work and were not altered or revalidated through its parent-owned validator.

Positive cleanup evidence: project completion requires an active entry, matching generation, and current end date at effects `720-727`.
Action completion requires the active country flag, generation, and end date at `1056-1062`, then checks target controller and lock-owner/type before success.
The control-change hook at on-actions `34-47` and runtime `868-917` releases the old controller's targeted operation before rebinding responsibility.
Administrative cleanup is called by on-actions `64` and runtime `1017`.
Late callbacks after a cleared action flag do not pass the normal completion gate.
These source guards are useful, but they do not repair the wrong targets, double debit, mutable refund, or lingering project flags.

## AI and probability evidence

The decision owner did not alter weights or select balance targets.
The source has no separate AI-only free-grant path in the inspected transaction API.
Both project and action start attempt a fresh reserve computation and gate AI through `acid_rain_country_ai_reserves_allow_loaded_quote` before using the shared debit helper.
The helper uses normal/emergency equipment retention, flat train/convoy/factory floors, band fuel floors, and a 10,000 manpower deployment floor at effects `157-249` and constants `253-283`.
Threat-three uses the severe forecast or live global layer at triggers `350-356`.
The start recheck is useful, but the double manpower debit invalidates the promised post-payment floor.
Cached per-row reserve-pass entries are not wired into public availability and do not establish current willingness or eligibility.
No verified `ai_hint_pp_cost` appears on Shelter Protocols or Demobilization.
A dynamic hint must not be invented, since the offline wiki documents a fixed amount.

The mandatory `chaosx_ai_probability_auditor` was spawned without inherited context as `01a101a5-d137-7ac3-98dd-6d31ebcee101`, bounded to these 13 decisions and A1-A20.
Its completion and exact route findings are appended below when returned.
The existing `validation\033_acid_rain_probability_audit.md` was inspected, but it is a cluster-pacing report and explicitly does not certify the earlier decision/weather audit.
It cannot be substituted for these decision scores.
Raw source bases are not click probabilities, and no normalized selection share, effective rank, starvation clearance, or reserve-safe campaign outcome is certified here.
Any later weight, route-weighted eligibility, or probability-bearing patch requires the auditor's baseline, an owner-applied patch, and `hoi4.probability_compare` under the same scenarios.

## Suggested localized owner patches

These are reviewable call-site proposals and have not been applied.

1. At triggers `328`, change the capacity reader to the actual `acid_rain_project_capacity` ledger.
After the reviewed global extra-slot calculation at runtime `687` and `787`, explicitly enforce the accepted maximum of three.
Do not change country-band balance anchors as part of this correction.

2. Replace every public generic custom-cost predicate with its matching persistent row predicate from the table above, and call the same predicate in `available` through `hidden_trigger` where the cost row already explains payment.
First fix route-specific land/island branches and D-band two-factory affordability in those helpers.
The cached AI reserve-pass bit must also be replaced or supplemented by a fresh read-only reserve check against current stock before it can govern public availability.
An earlier pass bit can remain true after another action spends resources, while the fresh start gate then rejects the selection and creates a no-op timer risk.
Keep the inclusive `NOT <` comparisons.
Refresh row caches on the existing tier/band/route-change paths, and make the effect-time quote and reservation receipt use the same declared row contract.

3. Give each of the 13 public decisions a row-specific `custom_cost_text` key with actual normal, `_blocked`, and `_tooltip` definitions in `033_acid_rain_l_english.yml`.
For example, use `acid_rain_project_shelter_cost` reading `acid_rain_shelter_next_*`, rather than publishing a shared selected-row variable.
Water/Evacuation/Decontamination selectors must resolve the exact route used by payment.
Limit inline costs to three values and retain all four explicit texticons and reservation semantics in the full tooltip.
Use the matching component `*_next_days` for the four native project timers instead of the absent generic alias/fallback.
Leave GUI-only localisation appended after scripted localisation line `98` with its owner.

4. Remove the second action manpower subtraction at preparedness effects `936`.
The common debit helper already charges that reservation.
Capture actual paid/reserved manpower, factory amount, resource-family count, effect window, target generation, and forecast/episode identity in the active receipt before any quote refresh can change them.
Release the captured reservation exactly once behind its active receipt, then zero the receipt.
Mirror the existing project ledger rather than recalculating a refund from price arrays.

5. At state-target completion call sites `660`, `740`, `812`, and `884`, bind the actual `FROM` state into the transaction before start, for example by entering `FROM` and assigning `ROOT.acid_rain_selected_action_state = THIS`.
Recheck full control, frozen validity, target generation/episode, relevant harm/forecast, and lock ownership at start.
Clear a rejected start's temporary target selection.
For the national Water rows, set `target_required` to zero and retain their national effect path.
Do not make national Water depend on an arbitrary retained state pointer.

6. In `acid_rain_cancel_project`, clear the corresponding active component flag in the same guarded transaction that clears its active ledger.
Add a selected-component active-entry and tier-cap recheck to `acid_rain_start_project`, so a stale repeated start cannot overwrite an existing reservation.

7. Reserve the quoted two factories for D-band state recoveries through a matching two-factory commitment modifier and release exactly that captured commitment.
Keep one-factory modifiers for A-C.
Do not reduce D's authored price merely to fit the current modifier.

8. Restore the documented one-day evacuation partial effect in the production protection calculation using a live, controller-valid, generation/episode-bound in-progress receipt.
Keep seven days as the matrix duration pending parent resolution of full-before-first-impact versus the three-day forecasts.
The tooltip must compare the actual completion date with that forecast's arrival, rather than promise an unreachable full first-pulse benefit.
The multi-operation evacuation/national-action ledger is a broader parent/architect follow-up, and must not be approximated by removing the single-operation guard.

9. Align local demobilization availability with its existing cancellation effect, including valid outstanding projects and fatigue after local exposure ends.
Recheck those local conditions at effect time.
Add the Medical Surge fatigue gate to both public availability and the fresh transaction preflight, and localise its blocked reason when it becomes player-visible.
Phase recovery visibility away from urgent phases and require the appropriate harm before offering each state recovery.
Review the rain-only repair and environmental-pressure claims against real receipts, retaining the existing real repair-speed modifiers and Deaths/Air history.

10. Preserve transaction selectors across bulk quote refresh and declare helper outputs in the consuming effect before helper invocation.
Bulk refresh uses temporary `acid_rain_selected_project` and `acid_rain_selected_action`, while decision selection is persistent with the same names.
The offline wiki warns that outputs created inside scripted helpers may not survive their return unless declared by the caller.
Wrong-row selection or lost output was not executed here, so this is an unresolved scope/output risk rather than a claim that every click necessarily selects the last loop row.
Use private quote-loop scratch or explicit save/restore, and verify all four component and all action selectors in the owner scenario pass.

## Meaningful validation and limits

Completed source checks: exact matrix comparison of 80 permanent rows/384 scalars, 64 band/tier dispatch checks, all urgent/recovery base values and current band rounding, every public cost-key family/suffix lookup, generic alias writer search, per-row affordability call-site search, texticon definition/vanilla-use lookup, debit/return tracing, factory commitment comparison, forecast lead versus action duration, mortality partial-effect consumer search, and control-transfer/late-callback cleanup tracing.
These checks found substantive defects and are source evidence only.
No game launch, live session, save mutation, log request, synthetic substitute for MCP, or parent migration-validator run was performed.
No gameplay simplification was implemented.
This audit does not claim decision or feature completion while the listed defects and mandatory engine evidence remain open.

### Exact MCP route gap

The live tool catalog exposed `hoi4.decision_inspect`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
Tool exposure did not establish service health.
An initial narrow inspect without scenarios returned the exact schema error `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.decision_inspect: Decision inspection requires declared scenarios at scenarios`.
The request was corrected with one explicit scenario rather than treating this input error as a workspace failure.

The corrected narrow call used `mode = inspect`, `id = chaosx_acid_rain_project_shelter`, `refresh = false`, and scenario `C1_before_click_known_persistent_row`, actor `GER`.
The scenario declared tier zero for all components, Preparedness zero, C band, zero active projects, and the known persistent Shelter row `days=21,civ=1,support=90,manpower=1000`.
It deliberately did not invent ownership/control/world flags or an alias writer to make the fixture pass.
Unspecified engine state would remain unresolved even had the tool returned a model.

The corrected inspection and narrow reference retries all returned `isError = true` and no artifacts:

| Route and narrow input | Exact returned failure |
| --- | --- |
| `hoi4.decision_inspect`, one Shelter decision and scenario | `tool call error: tool call failed for hoi4_agent_tools/hoi4.decision_inspect. Caused by: timed out awaiting tools/call after 600s` |
| `hoi4.reference_context`, decision surface, limit 2 | `tool call error: tool call failed for hoi4_agent_tools/hoi4.reference_context. Caused by: timed out awaiting tools/call after 600s` |
| `hoi4.reference_search`, `custom_cost_trigger`, limit 4, game_doc/wiki | `tool call error: tool call failed for hoi4_agent_tools/hoi4.reference_search. Caused by: timed out awaiting tools/call after 600s` |
| `hoi4.reference_search`, `has_equipment`, limit 2, game_doc/wiki | `tool call error: tool call failed for hoi4_agent_tools/hoi4.reference_search. Caused by: timed out awaiting tools/call after 600s` |

The wire failure text for each route was:

```text
tool call error: tool call failed for `hoi4_agent_tools/<route>`

Caused by:
    timed out awaiting tools/call after 600s
```

No source revision, scenario hash, decision analysis, artifact URI, continuation, or engine payment certificate returned.
`reference_read` could not consume revision-bound citation ids because the preceding retrievals returned none.
No `source_lookup` certificate is claimed, and exact vanilla sources were read locally.
An earlier broad inventory's wait also returned `cell 26 belongs to a stale code-mode host generation`, which is prior routing failure evidence rather than a decision finding.
The required narrow retry was performed in the current host.

### Local reference citations retained after failed retrieval

| Local source | Relevant lines read | SHA-256 |
| --- | --- | --- |
| Installed `common\decisions\_documentation.md` | `1-43`, especially available and target cadence | `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` |
| Installed `common\decisions\AFG.txt` | `1685-1747`, custom-cost/available/manual debit precedent | `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7` |
| Installed `documentation\triggers_documentation.md` | `3835-3842` has_equipment, `5006-5013` has_variable | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `common\decisions\_exiled_governments_decisions.txt` | `475-484`, variable stockpile amount computed in availability | `6057199A9654485DE804ABDA9F76DBF29F927CE66A569E86D78B11ACC324623C` |
| Installed `documentation\dynamic_variables_documentation.md` | `431-433`, `743-744`, political-power readers | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |
| Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | `305-355`, custom costs, fixed AI hints, native timer/cancel lifecycle | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | `437-442`, temporary lifetime/output/scoping, `557-567` unset/existence behavior | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | `1509-1540`, stockpile amounts, variable RHS and comparison syntax | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |

The installed docs' `state_trigger` description and actual vanilla `state_target = yes` precedent do not independently prove that this mod's `state_target = any_controlled_state` is accepted by the connected engine version.
That target-selector form remains an explicit syntax/consumer uncertainty for the restored decision route.
The variable-valued timed flags at effects `815-819` also require engine validation, since the short installed `set_country_flag` documentation does not settle that parameter form.
Neither uncertainty was promoted to an observed runtime defect.

## Probability auditor handoff

Pending the routed read-only auditor's final response at the initial write of this handoff.
The owner must retain the returned exact route failures and unresolved A1-A20/effective-score status, and must not treat the numeric cost tables above as MCP balance evidence.
