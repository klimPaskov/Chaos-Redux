# Event 006 decision and mission completion audit — 2026-07-25

## Verdict

**FAIL — Event 006 is not ready for a completion claim.**

The presently admitted core and package decision surfaces are substantially implemented, but the accepted decision contract is not complete and DM-58 can permanently lock a shared high-chaos lane without producing or resolving its promised operation.

This is a read-only audit handoff.
No gameplay, localisation, GUI, or asset files were changed.

## Scope and evidence

I reviewed the accepted Event 006 specification package, its decision-mission and formable matrices, the current source-of-truth map, the current decision, category, scripted-effect, trigger, localisation, script-constant, allocator, rival-bloc, formable, and Event Log sources.

The audit used the offline Paradox wiki snapshot for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event, decision, idea, AI, interface, and scripted-GUI modding, together with the vanilla `formable_nation_decisions.txt`, `foreign_influence.txt`, script-constant documentation, effects documentation, and triggers documentation.

The static inventory found 370 Event 006 action blocks in 41 categories.
The main `006_independence_wave_decisions.txt` surface contains the accepted DM-01 through DM-62 action layer, with the DM-43 refusal response as an additional response action rather than a second independent family.

## Issues, ordered by severity

### Critical — DM-58 creates a permanent global lock with no consumer or reset

`independence_wave_coordinate_reclamation_fronts` in `common/decisions/006_independence_wave_decisions.txt:3477` is a 180-day high-chaos mission with strategic and major-security costs.
Its completion at lines 3505–3513 sets `independence_wave_reclamation_fronts_coordinated`, marks every league member `independence_wave_reclamation_front_ready`, and applies league-value losses.
The only runtime uses of the global flag are its own activation, completion guard, and cancellation guard at lines 3484, 3505, and 3535.
No execution, allocator, target-selection, war/ultimatum, dissolution, or reset effect consumes the ready members or clears `independence_wave_reclamation_fronts_coordinated`.

`independence_wave_cleanup_decision_layer` in `common/scripted_effects/006_independence_wave_decision_effects.txt:662` removes the active mission and clears the owner-local ready flag at line 730, but it does not clear the global lock or the other members' ready flags.
`independence_wave_clear_league_phase_flags` in `common/scripted_effects/006_independence_wave_effects.txt:2288` likewise does not clear either reclamation state.
The accepted DM map handoff requires a shared planner to consume the same global flag and member readiness, create compatible synchronized actions, and clear the flags on resolve, rejection, dissolution, and stale state.

Before behaviour: the mission can charge the owner, mark every member ready, and permanently prevent any later DM-58 without starting or resolving a shared reclamation operation.
After the bounded repair: only valid current-generation league members should be collected into a compatible reclamation transaction; every success, rejection, stale record, member departure, league reset, and origin cleanup must clear the global flag and every member-ready flag exactly once.

Recommended bounded repair: add one narrow reclamation resolver in `common/scripted_effects/006_independence_wave_decision_effects.txt` or the existing league lifecycle file, call it from the current formal-league planner and each league terminal/reset path, and keep the existing decision as its paid preparation stage.
The resolver must use the existing generation, active-country, route-lock, living-target, and compatible-objective checks before issuing any existing war or ultimatum action.
Do not add a generic fallback target, free claim, or unconditional war declaration.

### High — 39 `custom_cost_text` entries lack blocked and hover localisation

The Decision modding wiki contract for `custom_cost_text = key` requires `key`, `key_blocked`, and `key_tooltip`.
The static localisation scan found all 100 base custom-cost keys, but 39 bases have neither the required `_blocked` nor `_tooltip` key.
This yields missing or unhelpful player-facing text when a cost is unavailable or hovered.

The affected bases are:

- Core surface in `localisation/english/006_independence_wave_decisions_l_english.yml`: `independence_wave_cost_administration_light`, `independence_wave_cost_administration_standard`, `independence_wave_cost_border_ultimatum`, `independence_wave_cost_breakaway_sponsorship`, `independence_wave_cost_corridor`, `independence_wave_cost_diplomatic_light`, `independence_wave_cost_diplomatic_standard`, `independence_wave_cost_integration`, `independence_wave_cost_pacific_island_strategic`, `independence_wave_cost_patron_balance`, `independence_wave_cost_reclamation_front`, `independence_wave_cost_rescue_aid`, `independence_wave_cost_safe_reserve`, `independence_wave_cost_security_light`, `independence_wave_cost_security_major`, `independence_wave_cost_security_standard`, `independence_wave_cost_selected_formable_commit`, and `independence_wave_cost_strategic`.
- Registry surface in `localisation/english/006_independence_wave_formable_registry_l_english.yml`: `independence_wave_form0124_administrative_diplomatic_cost`.
- FORM-05 surface in `localisation/english/006_independence_wave_form05_l_english.yml`: `independence_wave_form05_capital_cost`, `independence_wave_form05_coastal_warning_cost`, `independence_wave_form05_customs_clearinghouse_cost`, `independence_wave_form05_customs_cost`, `independence_wave_form05_defense_cost`, `independence_wave_form05_delegation_cost`, `independence_wave_form05_first_board_ratification_cost`, `independence_wave_form05_first_board_reconvening_cost`, `independence_wave_form05_opening_cost`, `independence_wave_form05_proclamation_cost`, `independence_wave_form05_reopening_cost`, `independence_wave_form05_shipping_board_cost`, and `independence_wave_form05_shipping_cost`.
- FORM-48 surface in `localisation/english/006_independence_wave_pacific_l_english.yml`: `independence_wave_form48_carrier_basing_cost`, `independence_wave_form48_carrier_convoy_cost`, `independence_wave_form48_carrier_procurement_cost`, `independence_wave_form48_invitation_acceptance_cost`, `independence_wave_form48_member_basing_cost`, `independence_wave_form48_member_convoy_cost`, and `independence_wave_form48_member_procurement_cost`.

Recommended bounded repair: add the missing `<base>_blocked` and `<base>_tooltip` keys beside each existing base key, preserving the exact material, factory, command, legitimacy, and state conditions exposed by the matching `can_pay_*` trigger.
This is localisation-only and does not require changes to a decision effect.

### High — accepted package and formable decision coverage remains intentionally incomplete

The accepted registry has 48 formable families in `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`.
The current source-of-truth map records `FORM-01` through `FORM-05` as implemented, `FORM-06` through `FORM-47` as fail-closed, and FORM-48 as implemented but unreachable because HAW and FSM are not runtime-admitted.
It also records FORM-12, FORM-13, and FORM-18 as implemented for CHU/ASY carriers whose runtime admission is closed.

The same map records nine currently content-attested runtime packages and states that the ten-country automatic bands remain unavailable until another package is admitted.
The specification README states that most country packages and FORM-06 through FORM-48 remain incomplete.
This is correct fail-closed behaviour, but it blocks an Event 006 completion verdict because accepted host, package, ambition, and formable lanes are not all reachable.

Recommended resolution: retain the current fail-closed protections, then complete package-level admission and the exact accepted contracts before promoting each relevant FORM family.
Do not substitute generic regional decisions, generic portraits, or a fallback tag for an unattested carrier.

### Medium — the five country values are not visible in the core decision header or a dedicated decision GUI

The accepted mechanics specification requires Legitimacy, Recognition, Government Capacity, Security, and Instability to be visible in a decision category header or a dedicated scripted GUI.
`common/decisions/categories/006_independence_wave_categories.txt` gives the core categories only visibility gates and icons.
`localisation/english/006_independence_wave_decisions_l_english.yml:2-9` provides narrative descriptions for Founding, Government, Recognition, and Security rather than those five live values.
The League category does correctly show its six league values at `006_independence_wave_decisions_l_english.yml:17`.

The only Event 006 references found in `common/scripted_guis` belong to the generic Event Log's rival-bloc detail data, not a decision-owned value surface.
No decision-owned scripted GUI was therefore available for `hoi4.gui_inspect` or `hoi4.gui_render`, and no GUI artifact was produced.

Recommended bounded repair: add dynamic value lines to the founding or government category description, or implement the already accepted compact decision header surface when that work is separately authorised.
The category-description option is the smallest scoped repair and must use the five current variables, not duplicated static text.

## Decision-category lifecycle notes

| Category group | Owner and reveal | Retirement and cleanup | Assessment |
| --- | --- | --- | --- |
| Founding, Government, Security | Any active Event 006 country | `independence_wave_end_active_origin` calls `independence_wave_cleanup_decision_layer`, which removes active central missions and clears their flags | PASS, except the missing country-value presentation |
| Recognition and Patron | Provisional-or-later country | Route, failure, and cleanup flags gate individual actions | PASS on static review |
| Former Host | Active country with a living former host | Disappears when that host relation is no longer valid and is cleared on origin end | PASS on static review |
| Network, League, Borders, Formables, High Chaos | Recognition, regional-power, unlock, league-member, target, and route gates | Individual actions have activation, target validation, cancellation, cooldown, `fire_only_once`, or terminal cleanup appropriate to their family | Conditional PASS; DM-58 is the material exception |
| Package and FORM categories | Package marker or exact FORM stage/consent gate | Package-local state and origin/formable cleanup control retirement | Conditional PASS for implemented packages; accepted families still fail closed as documented |
| SCN-008 ledger controls | Frozen scenario ledger only | No gameplay effect and AI base is blocked | PASS; the three `cost = 0` controls are navigation, not a political-power store |

## Mission-quality and duplicate-risk notes

| Family | Owner, category, region/objective, and requirement | Duration and settlement | Failure, cleanup, and duplicate risk | Assessment |
| --- | --- | --- | --- | --- |
| DM-01–05 founding | Released active country, Founding, capital/revenue/census/settlement objective | Central 150/120-day dynamic mission constants; country-value and route effects on success | Explicit timeout flags; terminal cleanup removes missions and flags; one-shot gates prevent repetition | PASS |
| DM-06–16 administration and recognition | Active or provisional country, Government/Recognition, civil service and named diplomatic/host objectives | 75–180-day central durations or delayed decisions; costs use administration or diplomatic helpers | Cancellation checks and mature-route flags retire obsolete actions | PASS |
| DM-17–23 security | Active country, Security, militia/depot/officer/border/army objective | 120–360-day central durations with equipment, manpower, command, and security costs | Timeout/crisis outcomes are defined; DM-22 is bounded by `independence_wave_emergency_units_raised` and `independence_wave_emergency_formations_active` | PASS |
| DM-24–30 former-host | Active country with a living former host, Former Host, settlement/ceasefire/reclamation objective | Central dynamic durations and diplomatic, administration, security, or map conditions | Host validity and route checks cancel invalid actions; no free claim loop found | PASS |
| DM-31–38 patron | Provisional country, Patron, named patron or concession objective | Central dynamic durations and material/diplomatic costs | Patron, route, and crisis conditions limit reuse and cleanup clears state | PASS |
| DM-39–44 network and DM-45–47, 60–62 league | Recognized network or charter-compliant league member, named member/target and charter condition | 45–180-day dynamic durations; DM-60 is 120 days and DM-62's mandate is consumed against the matching declaration | Target, membership, generation, and mandate checks constrain effects; immediate DM-61 has no lingering target | PASS on static review |
| DM-48–52 ambitions | Regional power, Borders, valid ambition or settled state highlighted on map | Dynamic delays and state-target requirements; integration is state/origin marked | State flags and generation/proof checks prevent repeated core or transfer rewards | PASS on static review |
| DM-53–56 formables | Recognized country with unlocked discovery, exact selected family, consent, and territorial proof | Dynamic congress and integration timings with selected-family costs | Registry commit owns family-specific transaction and no generic fallback tag exists | Conditional PASS; family reachability remains incomplete |
| DM-57 high-chaos sponsor | High-chaos regional power, valid state target, allocator-compatible sponsorship record | 180-day delayed decision with diplomatic, security, and civilian-factory commitment | Reconciliation deletes only stale records; post-commit consumer is idempotent and generation-checked | PASS |
| DM-58 high-chaos reclamation | High-chaos radical charter member, formal league, minimum membership, shared reserve | 180-day mission with strategic and major-security cost | Completion does not trigger or settle its shared operation and leaves permanent global state | FAIL |
| DM-59 high-chaos charter | High-chaos league route and charter conditions | Dynamic timed transformation | Crisis, route, and cleanup conditions prevent a repeated route flip | PASS on static review |
| Rival-bloc invitation and responses | Rival authority and exact pending target, targeted invitation contract | 90-day invitation, 90-day response deadline, 30-day acceptance ratification, and 120–180-day shared actions | `independence_wave_rival_bloc_respond_to_invitation` now expires the invite, and the rival cleanup clears event target, generation, member arrays, and flags | PASS |
| FORM-01–05, FORM-12/13/18, FORM-48 and admitted package missions | Exact carrier, member, state, consent, and package predicates | FORM-specific constants own durations and material obligations | Package/formable cleanup and staged flags limit duplicate rewards; FORM-48 remains unreachable and other families are fail-closed | Conditional PASS for implemented, reachable contracts only |

## Costs, requirements, AI, and exploit-risk notes

The central DM-01 through DM-62 layer uses script constants in `common/script_constants/006_independence_wave_decision_constants.txt` rather than decision-local magic numbers.
Its central timings range from 45 through 720 days, and cooldowns are 90, 180, or 365 days according to the action family.
The rival bloc uses separate concrete 30–180-day constants and paid command power, equipment, train, convoy, fuel, and experience commitments.

The static source scan found no generic political-power store in the central layer.
The six direct political-power costs in `common/decisions/006_independence_wave_iw093_iw098_decisions.txt` are each a mutually exclusive  conference route commitment with a central timed transaction, route-specific eligibility, success or failure, cancellation, and AI conditions.
They are not repeatable passive exchanges, although any later redesign should preserve that route-lock structure.

DM-22 is the only emergency unit creation path found in the central decision layer.
It is gated to severe host threat and a one-shot flag, uses a fixed owner-local unit id, and `independence_wave_decision_demobilize_emergency_formations` deletes that id on professionalization and terminal cleanup.
No repeatable decision-surface free-unit loop was found in this source pass.

DM-57 writes a generation-stamped state record, the package planner calls `independence_wave_reconcile_breakaway_sponsorship_queue`, and the post-commit consumer removes only a matching committed record.
This passes the requested allocator integration check.

Every active decision block has an `ai_will_do` block in the static inventory except automatic deadline missions that use `activation = { always = no }` and are not selectable by AI.
AI target safety is supplied by named target triggers for host, patron, network, state, invitation, charter, and FORM actions.
The practical AI risk is DM-58: its current high AI weight can create the same permanent global lock described above.

All 370 static decision titles and descriptions, all 41 category titles and descriptions, and all 71 icon identifiers resolve against the mod or vanilla.
`GFX_decision_generic_ignite_civil_war` is supplied by vanilla `interface/decisions.gfx:693`.
This passes title, description, category, and icon registration coverage, but does not override the 39 custom-cost localisation failures.

## Required follow-up order

1. Repair and test the DM-58 shared reclamation resolver, including global/member cleanup through success, failure, stale state, departure, dissolution, and origin end.
2. Add all 78 missing custom-cost localisation keys (`_blocked` and `_tooltip` for each of the 39 bases) and verify both available and unavailable hover states.
3. Surface the five country values in the core decision UI with dynamic localisation.
4. Keep the unadmitted package and FORM lanes fail closed until their exact carriers, package decisions, missions, assets, and runtime admission criteria are complete.

## Validation performed and limits

Static source validation covered all Event 006 decision files, categories, linked cost keys, decision/category localisation keys, icon identifiers, central duration and cooldown constants, current cleanup entry points, allocator integration, rival invitation expiry, direct political-power exceptions, global reclamation flag references, and selected unit cleanup.

I did not launch Hearts of Iron IV, run live scenario execution, or render a decision-owned GUI because no such Event 006 GUI surface exists in the current source.
No synthetic runtime fallback or in-game validation is claimed.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_decision_mission_completion_audit_2026_07_25.md`

## Simplifications, omissions, and blockers

No implementation was simplified or altered by this audit.
The accepted Event 006 scope remains incomplete because most package/formable lanes are intentionally fail closed, FORM-48 is unreachable, DM-58 lacks its shared operation lifecycle, cost feedback is incomplete, and the five core country values are not presented in the decision UI.
