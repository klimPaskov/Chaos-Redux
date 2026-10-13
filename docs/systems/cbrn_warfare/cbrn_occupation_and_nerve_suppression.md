# CBRN occupation, protective aid, and historical nerve-suppression records

## Current source-of-truth map

| Surface | Current disposition | Source evidence |
| --- | --- | --- |
| Occupied-state Sarin and Soman attack decisions | Retired by the user-approved 2026-09-25 decision to remove decision-based CBRN attacks without an owned-state native replacement. | `common/decisions/cbrn_occupation_decisions.txt` has no Sarin or Soman attack entry; `common/scripted_effects/cbrn_occupation_effects.txt` has no direct nerve-suppression execution helper. |
| Protected Occupation Administration | Retained occupation law and authorization decision. | `common/decisions/cbrn_occupation_decisions.txt`; `common/occupation_laws/chaosx_occupation_laws.txt`; `common/scripted_effects/cbrn_occupation_effects.txt`. |
| CBRN Coercive Security | Hidden compatibility authorization and retained law for prior records; it does not provide a current attack action. | The `cbrn_authorize_coercive_security` decision has `visible = { always = no }`; the law and its AI compatibility gates remain in `common/occupation_laws/chaosx_occupation_laws.txt` and `common/scripted_triggers/cbrn_occupation_triggers.txt`. |
| External protective aid | Retained state-targeted, timed decision with selection-time mask reservation and cancellation or failed-delivery refund. | `cbrn_deploy_protective_aid` in `common/decisions/cbrn_occupation_decisions.txt`; reservation and delivery helpers in `common/scripted_effects/cbrn_protection_effects.txt` and `common/scripted_effects/cbrn_occupation_effects.txt`. |
| Occupation decision amounts and tooltips | Costs, durations, coverage targets, and consequence values use temporary scripted-localisation quotes from the same constants as gameplay. | `common/scripted_localisation/cbrn_occupation_value_localisation.txt`; `localisation/english/cbrn_occupation_l_english.yml`. |
| Exact-record disclosure and aftermath | Retained for historical nerve-suppression records; these readers do not create a new attack. | Four record-response decisions, exact UID helpers, trauma, discovery, backlash, and control-change helpers in the occupation decision, effect, and trigger files. |
| Native battlefield CBRN attacks | Separate native raid surface. | `common/raids/cbrn_chemical_land_raids.txt` and `common/raids/cbrn_chemical_air_raids.txt`; the parent owns the final raid-category and wiring review. |
| Camp nerve-agent method | Separate camp transaction and infrastructure. | `common/scripted_effects/cbrn_camp_effects.txt` and the camp repression decision and effect files; it is not an occupied-state attack replacement. |

Implementation evidence in this table describes the current source snapshot; it does not establish live-game behavior or final integration approval. The parent reviews final source and required MCP evidence, and live-game validation belongs to the user.

## Occupation laws

Protected Occupation Administration requires Basic Gas Masks and advanced protection. Its one-time authorization costs 50 Political Power, and the law increases garrison and protective-equipment burden while supporting compliance and limiting resistance in vulnerable occupied territory.

CBRN Coercive Security and its authorization flag remain for compatibility with existing policy records. The authorization decision is hidden for both player and AI, and its retained stock, protection, and route predicates serve the law compatibility gate only. The old `concentration` law identifier remains a hidden, unselectable migration token with no gameplay modifiers; its native fallback is Military Governor.

The separate Nerve Agent Suppression Detachment is still defined in the regimental-support subsystem pending the accepted unit consolidation. Its presence does not release an agent, and this occupation package has no current Sarin or Soman preparation, payment, target-selection, or attack action.

## Protective aid to occupied civilians

Deploy Protective Aid is a 21-day state-targeted project with 25 Political Power and two Civilian Factories committed at selection. The donor needs an established CBRN program and real respirator stock. The target must be a populated state controlled by another country, non-core to that controller, under a chemical alert, chemical contamination, biological outbreak, or recorded nerve-suppression trauma, and still below its occupied-population protection target.

The cost quote and affordability gate use the same exact-state respirator requirement. Selection reserves the donor's real mask models against that state before debiting Political Power; the in-flight project uses continuation and reserved-target checks rather than requiring the committed stock or factories to remain free. Completion consumes at most the reserved receipts, records actual consumed and useful crates, updates the recipient and donor ledgers, and refunds unused crates. Cancellation, lost target validity, or failed delivery closes the reservation and returns unused stock to the existing original donor. The reservation counter prevents a paid in-flight project from disappearing from the decision surface or being closed twice.

Aid changes civilian protection and records a bounded opinion effect. It does not create equipment, erase chemical history, or reduce Condemnation. Source-level AI modifiers favor the donor's own cores, allied cores, and states with recorded trauma; no normalized AI selection outcome has been established for this documentation pass.

The cost row distinguishes Political Power spent immediately, model-aware respirator crates reserved at selection, and civilian factories assigned during delivery. Its hover explains cancellation and unused-crate refunds without repeating the amounts. The player-facing occupation response text describes attacks, evidence, resistance, inspections, and Condemnation; exact record identifiers and liability accounting remain internal to the scripted effects.

## Historical record, disclosure, and aftermath

The retained response decisions are Seal State, Destroy Contaminated Records, Admit Accidental Release, and Permit Inspection. They require the recorded responsible country and the exact chemical-record UID for a historical nerve-suppression action. Seal and destruction can suppress evidence on that exact row and create concealment liability; admission and inspection can advance attribution and reveal liability. None substitutes a latest-row or same-country record if the exact UID is missing, and none erases the action, casualties, contamination, or use history.

Seal State and Destroy Contaminated Records retain Political Power as their only payment. Their ordinary 40 and 60 Political Power costs scale with current public Condemnation from 1× to 3× and appear once in custom cost rows; a failed exact-record dispatch refunds the amount just charged. At Condemnation 0, 500, and 1000 the two quotes are 40/60, 80/120, and 120/180 respectively. The [occupation cover-up cost correction](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_occupation_coverup_pp_scale.md) records the shared quote, inclusive affordability, settlement, and AI-hint source limits. Native row rendering and execution remain unverified.

Stored state trauma retains its resistance and compliance effects and its exact-state decay schedule. A pending delayed backlash remains tied to its due day and responsible controller. A control change removes temporary operational benefits while retaining responsibility, trauma, evidence, deaths, and discovery liability. These readers and scheduled effects preserve historical aftermath; the retired occupied-state attack route does not generate new records for them.

## Separate camp method and native raids

The doctrine-linked nerve method in an active camp network remains a camp repression action with its own site, payload, death, contamination, evidence, and consequence transaction. It is governed by camp files and does not restore the retired mobile occupied-state Sarin or Soman decisions.

The native chemical land and air raid types remain the battlefield chemical attack route. The occupation documentation does not infer an owned-state raid target or a replacement action from their existence.

## Evidence limits and follow-up

The 2026-09-25 occupation probability baseline fixture at `docs/plans/chaos_warfare_system_plans/2026-09-25_cbrn_occupation_probability_baseline_fixture.json` is an unbound, partial score result for the former Sarin and Soman decision candidates: 96 inputs were unresolved, and it established no normalized choice. Its post-edit comparison and any surviving weighted-surface scenario review belong to the parent and the probability auditor. Source presence and exposed MCP tool names alone do not prove service health or a completed read-only scenario audit.

The parent must review final raid categories, retained law and aid AI, localisation, assets, exact-record consumers, and any required MCP evidence before an integration claim. No live-game result is asserted here.

## Human holder boundaries

The two CBRN occupation laws require a human occupier and, when present, a human occupied-country scope in their native availability blocks.
Their state action gate requires existing human OWNER and CONTROLLER.
Both native AI score blocks retain their original human formulas and end with a zero factor when the state holders or occupier are nonhuman.

`cbrn_occupation_clear_nonhuman_state_policy` is STATE-scoped, has no input variables or outputs, and clears only a CBRN law or recorded CBRN policy in an ineligible state.
It enters CONTROLLER then PREV so the native law reset receives the actual occupier as PREV, as required by installed `set_occupation_law` documentation.
The existing `default_law` reset removes the CBRN override and preserves ordinary occupation rules.
`cbrn_occupation_clear_nonhuman_country_policy` is COUNTRY-scoped, has no inputs or outputs, revokes inherited CBRN authorization and clears only matching country/default/state CBRN policies.
It is called by the shared synchronous nonhuman transition helper, and the state helper is also called by `on_state_control_changed` for FROM.FROM.
Human actors keep their existing law values, costs and policy choices.
No sprite, icon, asset, event target, periodic hook or new tuning table is required.
Future extensions should use the same current-holder gate and exact owner policy teardown.
