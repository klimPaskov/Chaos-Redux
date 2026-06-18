# Event 012 Africa Decision/Mission Follow-Up Handoff

Date: 2026-06-18

Scope: Decision/mission audit and narrow local patch for Event 012 Africa. No focus, country history, or state files were edited. No staging or commit was performed.

## Changed files

- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_decision_followup_handoff.md`

Unrelated dirty files were present in the workspace, including Event 010 files and existing non-decision Event 012 surfaces. They were not edited for this audit.

## Patch summary

Changed decision ids:

- `africa_charter_local_dossier_office`
- `africa_settle_selected_dossier_observer`
- `africa_settle_selected_dossier_direct_archive`

Changed localisation ids:

- `africa_charter_local_dossier_office_cost_tt`
- `africa_charter_local_dossier_office_cost_tt_blocked`
- `africa_charter_local_dossier_office_cost_tt_tooltip`
- `africa_settle_selected_dossier_observer_cost_tt`
- `africa_settle_selected_dossier_observer_cost_tt_blocked`
- `africa_settle_selected_dossier_observer_cost_tt_tooltip`
- `africa_settle_selected_dossier_direct_archive_cost_tt`
- `africa_settle_selected_dossier_direct_archive_cost_tt_blocked`
- `africa_settle_selected_dossier_direct_archive_cost_tt_tooltip`

Before:

- The local dossier office and both dossier settlement decisions used only the built-in `cost = constant:africa_decision.old_seat_mission_cost`.
- That made the Authority Atlas office/settlement lane behave like a flat political power exchange even though the spec expects dossier offices and settlements to require tangible administrative and security commitments.

After:

- `africa_charter_local_dossier_office` now uses `custom_cost_trigger` and spends political power, support equipment, and manpower.
- `africa_settle_selected_dossier_observer` now uses `custom_cost_trigger` and spends political power plus support equipment.
- `africa_settle_selected_dossier_direct_archive` now uses `custom_cost_trigger` and spends political power, support equipment, and command power.
- Matching custom cost text was added for player readability.

## Issue list, sorted by severity

1. Fixed: Authority Atlas office/settlement costs were PP-only despite being part of the old-seat administrative/security loop. This was an acceptance failure against varied non-PP costs and objectives.
2. Remaining: scripted GUI button text still describes some buttons as PP-only, especially `africa_gui_authority_seats_button_tt` and `africa_gui_bestiary_terms_button_tt`. This may be accurate for the helper calls behind those buttons, but it is still weaker than the active-gameplay standard if those buttons are used as primary player actions.
3. Remaining: some low-risk category management decisions are still PP-first or PP-only, including register refresh and some route-opening actions. They are less severe because most consequential missions and targeted actions already use equipment, manpower, command power, convoys, trains, XP, state control, or deadline requirements.
4. Remaining: I did not verify every dossier profile spend branch in live execution. The scripted trigger/effect structure appears profile-gated, but the full profile matrix is broad enough that a dedicated dossier-profile pass would be higher confidence.
5. No high-severity target-dead-country issue found in the inspected decision surface. Targeted country decisions generally check `exists = yes`, avoid `ROOT`, and use arrays or state triggers tied to current ownership/control.

## Decision category lifecycle notes

- Continental Congress: Has recurring political/congress actions, register refreshes, and mission unlock effects. Lifecycle is readable and mostly gated by runtime-unifier flags and event route flags.
- Charter League / Charter Member: Uses target arrays and confidence/aid corridor missions with event target cleanup. Costs are varied for major aid and corridor actions.
- Liberation War Office: Has active objective selection, state target checks, deadlines, rail/column requirements, and cleanup helpers. It is one of the stronger active-gameplay surfaces.
- Regional Integration: Uses targeted state completion, rail belt security, integration deadlines, and authority/trust/paper-core variables. Requirements are visible through custom tooltips.
- Diaspora: Uses return cadre, settlement, officer-school, and Pan-Atlantic follow-through. Costs include convoys, support equipment, manpower, and route flags.
- Authority Atlas: Has survey, local office, guard, settlement, direct archive, and archive deadline loops. This patch closes the obvious PP-only gap in local office/settlement actions.
- High Chaos / Green Covenant / Bestiary: Uses package selection, habitat seats, omen review, containment deadlines, actor-specific one-time actions, and alarm/trust/pressure variables. Costs are mostly non-PP and profile-like.
- Sponsorship / cross-continent: Uses readiness missions, region-specific proof, and certification costs with convoys, equipment, manpower, command power, and XP.
- RSA branch: Has route-specific Pretoria/supply/mine-port style requirements. I did not edit this branch.

## Mission quality notes

- Owner: Africa runtime unifier / Continental Congress. Category: `africa_continental_congress_category`. Requirement: legitimacy/cohesion/register gates. Duration: recurring decisions and mission unlocks. Success/failure: mostly immediate values or category unlocks. Duplicate risk: low, controlled by flags and arrays.
- Owner: Charter League. Category: `africa_charter_league_category`. Region: Charter member targets. Requirement: member flags, target arrays, aid/corridor cost gates. Duration: confidence and corridor missions use timeouts. Success/failure: confidence/corridor effects and cleanup. Duplicate risk: low if target event targets clear as scripted.
- Owner: Liberation War Office. Category: `africa_liberation_war_office_category`. Region: external-holder/liberation objective states. Requirement: liberation office flags, state control/ownership, rail/objective counters. Duration: `africa_liberation_front_deadline_mission`. Success/failure: objective progress or alarm/debt penalties. Duplicate risk: low because state operation flags and objective progress cleanup exist.
- Owner: Regional Integration. Category: `africa_regional_integration_category`. Region: African owned/controlled states and authority subjects. Requirement: living core, authority, rail, trust, paper-core burden gates. Duration: `africa_regional_integration_deadline_mission`. Success/failure: integration value changes or pressure penalties. Duplicate risk: moderate only if state target arrays become stale; current cleanup appears intentional.
- Owner: Authority Atlas. Category: `africa_authority_atlas_category`. Region: selected historical dossier seat state. Requirement: selected dossier, secured seat, office, guard, settlement route. Duration: survey, direct archive seal, and archive guard deadline missions. Success/failure: opens/settles dossiers or raises restoration debt/local pressure. Duplicate risk: low to moderate; selected dossier state and register advancement are central, so profile-specific retesting is recommended.
- Owner: Bestiary / High Chaos. Category: high-chaos and covenant decision surfaces. Region: selected package/habitat states. Requirement: package gate, habitat seat, omen reliability, containment pressure. Duration: omen review and containment deadline missions. Success/failure: trust/alarm/volatility outcomes. Duplicate risk: low due to one-time flags on actor decisions, but scenario balance should be watched because several actions push related variables.
- Owner: Sponsorship. Category: sponsor/cross-continent category. Region: Middle East, Asia, Europe, South Atlantic proof lines. Requirement: readiness mission, unifier proof, dossier/living-core counts. Duration: readiness/proof missions. Success/failure: sponsor readiness and certification. Duplicate risk: low; costs are varied and route-gated.
- Owner: RSA route. Category: RSA Africa decision surface. Region: Pretoria/mine-port/supply path. Requirement: RSA route flags and controlled objectives. Duration: Pretoria deadline mission. Success/failure: route progress or penalties. Duplicate risk: not fully audited in this pass.

## Cost and requirement clarity notes

- Fixed: three Authority Atlas decisions now expose clear custom cost text and spend non-PP resources.
- Most major Event 012 decisions already avoid being passive PP stores: aid, corridors, liberation, integration, diaspora, dossier survey, old-seat guard, Bestiary, sponsor, proof, and RSA actions use equipment/manpower/XP/convoys/trains/command power/state objectives/deadlines.
- Some button localisation and low-level management actions still read as PP-only. If those buttons are intended to be primary gameplay, they should be upgraded or clearly framed as administrative refreshes.
- Requirements generally use custom trigger tooltips instead of raw trigger walls. The direct archive mission and dossier req text are readable and use dynamic dossier/state localisation.

## AI validity and route-lock notes

- Targeted country decisions inspected generally include `exists = yes`, `NOT = { tag = ROOT }`, ownership/control checks, route flags, or membership flags.
- AI weights are present on the inspected decisions, including low/preferred route weighting on direct archive settlement.
- The patched decisions retained existing AI weights. Because the new cost triggers are real availability gates, AI cannot bypass the resource checks through those decisions.
- No broad AI equivalent for every scripted GUI button was confirmed in this pass. Existing decision equivalents cover most major gameplay actions, but GUI helper buttons should remain a follow-up audit item.

## Localisation and tooltip gaps

- Fixed: missing cost tooltip family for `africa_charter_local_dossier_office`, `africa_settle_selected_dossier_observer`, and `africa_settle_selected_dossier_direct_archive`.
- Remaining: `africa_gui_authority_seats_button_tt` and `africa_gui_bestiary_terms_button_tt` still advertise PP-only costs. That may be intended, but it is a visible weak point against the Event 012 active-cost target.
- Dynamic dossier name/state text is present for the inspected Authority Atlas decisions and missions.

## Cleanup and exploit-risk notes

- Confidence, corridor, liberation objective, dossier survey, direct archive, archive guard, sponsor readiness, and Pretoria-style missions all appear to have explicit success/failure or cleanup paths.
- The patched decisions spend resources in `complete_effect`; because `cost = 0` is paired with `custom_cost_trigger`, the player sees one custom cost line and the spend happens once on completion.
- No new repeat loop was introduced. Existing dossier settlement calls still advance the dossier register after observer/direct archive settlement.
- Remaining exploit risk: full dossier profile matrix should be tested for repeatable profile rewards after failed survey/settlement edge cases. This audit did not exhaustively simulate each selected dossier profile.
- Remaining balance risk: support equipment cost `120` is reused for several legal/office/protection actions. This is acceptable as a local fix, but a later balance pass may want a distinct dossier office constant if office staffing should be cheaper or more expensive than federal court protection.

## Checks performed

- Read required Event 012 specs and matrices under `docs/specs/012_africa_specs/`, especially the decision/mission UI spec, decision map, acceptance criteria, and decision/mission prompt.
- Read repo rules and the required decision/mission, events, subagent, and improvement-loop skills.
- Consulted offline Paradox wiki decision, trigger, effect, localisation, scope, event, idea, modifier, data structure, on action, and AI modding pages.
- Consulted vanilla decision documentation in `~/projects/Hearts of Iron IV/common/decisions/_documentation.md` and relevant vanilla script documentation for constants, effects, and triggers.
- Inspected `common/decisions/012_africa_decisions.txt`, directly related Event 012 scripted effects/triggers/scripted localisation/localisation/constants.
- Reviewed the resulting diff for the two gameplay/localisation files.
- Verified the new decision cost keys are referenced by the changed decisions.
- Verified `localisation/english/012_african_union_l_english.yml` still begins with UTF-8 BOM.
- Checked brace counts on `common/decisions/012_africa_decisions.txt` after the patch.

Skipped meaningful validation:

- No live HOI4 launch or in-game scenario run was performed.
- No exhaustive selected-dossier profile simulation was performed.
- No focus, country history, state, or unrelated Event 010 validation was performed because those surfaces were outside the user-approved scope.

## Concrete recommended follow-ups

1. Audit scripted GUI helper buttons in `common/scripted_effects/012_africa_effects.txt`, matching GUI/localisation surfaces, and `localisation/english/012_african_union_l_english.yml` for PP-only button actions. Start with `africa_gui_authority_seats_button_tt` and `africa_gui_bestiary_terms_button_tt`.
2. Run a focused Authority Atlas profile pass over `common/scripted_triggers/012_africa_triggers.txt`, `common/scripted_effects/012_africa_effects.txt`, and `common/scripted_localisation/012_africa_scripted_localisation.txt` to confirm every dossier profile has matching cost, spend, success/failure, and profile outcome text.
3. Consider adding distinct script constants for dossier office and dossier settlement support costs if later balance review decides `constant:africa_force.dossier_protection_support_equipment` is too generic.
4. Recheck cross-continent/RSA branches after the active Africa route is playable end-to-end, especially for AI use of GUI-equivalent actions and route-locked target selection.
