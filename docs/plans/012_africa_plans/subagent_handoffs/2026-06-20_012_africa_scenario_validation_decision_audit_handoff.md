# Event 012 Africa Scenario-Validation Decision Audit Handoff

Date: 2026-06-20

Scope: read-only static/script audit of Event 012 Africa scenario-validation coverage. This is static/script audit evidence, not live in-game testing. No gameplay, localisation, asset, spreadsheet, or code files were edited.

Parent follow-up, 2026-06-20: the high-risk cross-continent union mismatch was patched by adding `has_africa_any_sponsored_cross_continent_charter` and using it for `AFR_congress_of_continents`, `africa_proclaim_dynamic_cross_continent_union`, and the matching AI weights. Intermediate dynamic unions now require one or more sponsored charters, while World Is One certification still requires all four external proof routes. The two scenario-profile risks were also narrowed: Fragile Unifier records small-host versus fallback markers, and Ally Under Attack is blocked unless an outside holder still owns or controls African land. Live scenario proof remains queued.

Primary inspected implementation files:

- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
- `events/012_african_union.txt`
- `localisation/english/012_african_union_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

Reference docs read for the audit:

- `docs/specs/012_africa_specs/matrices/012_africa_acceptance_criteria.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`
- `docs/specs/012_africa_specs/specs/012_africa_ai_balance_validation.md`
- `docs/specs/012_africa_specs/prompts/012_africa_coding_prompt.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md`

## Severity-Sorted Issues

| Severity | Issue | Evidence | Parent follow-up |
| --- | --- | --- | --- |
| High | Dynamic cross-continent union validation is too narrow for single-continent union tests. The decision text says "at least one prepared cross-continent charter," and the effect can choose African-Middle Eastern, Afro-Asian, Afro-Atlantic, Afro-Eurasian, or Congress identities, but the decision currently requires all four sponsorship flags. | `africa_proclaim_dynamic_cross_continent_union` in `common/decisions/012_africa_decisions.txt` requires `africa_sponsored_middle_east_charter`, `africa_sponsored_asia_charter`, `africa_sponsored_europe_charter`, and `africa_sponsored_south_atlantic_charter`. `africa_apply_dynamic_cross_continent_union_identity` in `common/scripted_effects/012_africa_effects.txt` has one-charter and mixed-charter branches. Localisation says "at least one prepared cross-continent charter." | Decide whether the validation target is "any cross-continent union" or "all-charter Congress of Continents." If any union is intended, loosen the availability trigger to one-or-more sponsored charters while keeping the World Is One certification path all-four. |
| Medium | Weak/small unifier scenario can silently fall back to a non-weak actor. | `africa_select_fragile_unifier_candidate` first searches for an eligible candidate with fewer than `constant:africa_triggerable_scenario_validation.fragile_controlled_state_threshold` controlled states, then falls back to WAC creation, existing WAC, weighted valid selection, or no-valid flag. | Add a scenario-specific visible/status flag or report when the fragile branch falls back, or create a guaranteed weak host package so the weak/small validation case cannot accidentally become an ordinary unifier test. |
| Medium | African ally under attack can launch without an actual attack if no external colonial holder is found. | `africa_apply_triggerable_ally_under_attack_opening` seeds/saves WAC or SAH as `africa_triggerable_scenario_ally`, then randomly chooses `is_africa_external_colonial_holder_for_prev`; if no holder exists, the branch still leaves the scenario flag and liberation state but no war. | Add a fallback colonial-holder setup, blocked launch condition, or failure/status report so the "under attack" validation case always proves an actual ally war. |
| Medium | Full Africa unification scenario is synthetic, not proof of integration mechanics. | Continental Pole sets `africa_is_one_complete`, emits Africa Is One and Scramble super-events, and at high intensity fills regional authority/living-core/dossier/Bestiary counters. It does not prove map control, integration missions, resistance, or live full-Africa ownership. | Treat Continental Pole as late-route scaffolding only. For "full Africa unification" validation, add or run a separate live integration scenario/check that verifies state control, living cores, regional authorities, and resistance cleanup through the normal mechanics. |
| Low | High-chaos Covenant scenario opens Bestiary/Archive preview but does not by itself validate a complete Green Covenant route. | `africa_apply_triggerable_high_chaos_opening` sets `africa_route_archive_bestiary`, opens Authority Atlas/no-caricature, adds the Authority Atlas spirit, adjusts mythic/bestiary/habitat values, and unlocks one to three high-chaos packages by intensity. | Keep as valid high-chaos launch coverage, but parent should not count it as full Green Covenant route validation without testing Covenant decisions, Bestiary containment, package actions, and failure states. |

## Eight-Scenario Matrix

| Scenario | Current evidence | Status | Exploit/validation risks | Concrete parent follow-up |
| --- | --- | --- | --- | --- |
| Ordinary unifier | `standard_unifier = 1` exists in `triggerable_scenario_africa_type`; `select_triggerable_scenario_africa` selects SCN-012; `trigger_africa_is_one_scenario` calls `africa_triggerable_scenario_launch_selected`; non-RSA non-fragile launch selects a valid African-capital candidate, calls `africa_establish_union_start`, then applies `africa_triggerable_scenario_standard_unifier` with legitimacy/cohesion deltas. Event entry `chaosx.nr12.2` uses the same normal/RSA branch split. | Pass for static launch scaffolding. | Weighted candidate selection is not deterministic, so a static audit cannot prove a specific ordinary host profile. Scenario can create WAC only when no valid candidate exists. | Parent should run or record one live/manual SCN-012 standard launch and capture selected host, focus tree load, Charter League creation, paper-claim state, decision categories, and event-log actor. |
| Weak/small unifier | `fragile_unifier = 6`; scenario type cycling/localisation exposes Fragile Unifier; `africa_select_fragile_unifier_candidate` prefers candidates with controlled states below `fragile_controlled_state_threshold = 3`; `africa_apply_triggerable_fragile_unifier_opening` lowers legitimacy/authority and raises trust/debt. | Partial. | Fallbacks can make the scenario WAC or weighted ordinary selection, which weakens the weak/small validation case. Static audit cannot prove the candidate pool contains a qualifying country. | Add visible fallback reporting or guaranteed weak seed. In live validation, record controlled-state count and opening values before treating this scenario as passed. |
| RSA in Allies | `is_africa_rsa_allies_unifier_candidate` requires SAF, valid Africa candidate, and ENG in faction with SAF. Triggerable scenario RSA branch requires this candidate and calls `africa_start_rsa_allies_civil_war`. Event `chaosx.nr12.2` also branches RSA to civil war. RSA emergency decisions and `africa_white_peace_allies_after_rsa_continental_victory` support the branch and Allied peace. | Pass for static branch support. | Peace-out depends on continental victory state and event targets being set by the civil-war chain; static audit cannot prove civil-war winner detection fires in live play. | Parent should live-trigger RSA Civil War with SAF in ENG faction, verify continental/loyalist targets, civil-war active flags, Pretoria mission, victory flag, and Allied white peace. |
| African ally under attack | `ally_under_attack = 7`; scenario type/localisation exposes Ally Under Attack. `africa_apply_triggerable_ally_under_attack_opening` opens Charter/military/liberation flags, seeds first authority, saves WAC or SAH as the scenario ally, picks an external colonial holder, declares holder war on the ally, and declares the unifier war on the holder if needed. | Partial. | If no WAC/SAH member can be saved or no external holder exists, the scenario may launch without the defining ally-under-attack war. Targeting is narrow: only WAC or SAH can be the saved ally. | Add fallback/blocked-state handling or a status event. Live validation should confirm `africa_triggerable_scenario_ally`, `africa_triggerable_scenario_holder`, both wars, and aid/corridor/member-confidence decisions. |
| High-chaos Green Covenant | `high_chaos_covenant = 4`; scenario opens Authority Atlas, no-caricature clause, Archive/Bestiary route, Authority Atlas spirit, high mythic/bestiary/habitat values, and unlocks one package at low/medium, two at high, three at maximum. It records Evolution II when enabled. | Partial. | This is a high-chaos Bestiary/Archive preview, not a complete Green Covenant victory or stress test. It does not by itself prove Bestiary containment, habitat seats, package actions, or Covenant failure states. | Parent should validate high/max intensity separately: package count, actor creation/classification, Bestiary decisions, containment mission, package-action counter, and no-human-caricature route locks. |
| Full Africa unification | Continental Pole type sets `africa_is_one_complete`, `africa_continental_pole_ready`, opens post-unification/sponsor/proof flags, fires Africa Is One and Scramble super-events, and at high intensity fills regional authority, living-core, historical dossier, macro-region, case, and Bestiary counters to World Is One thresholds. | Partial. | This is synthetic gate scaffolding. It validates late-route surfaces but not actual full-continent control, integration temperatures, resistance watches, live core conversion, or map ownership. | Parent should keep this as a fast late-route launcher and separately validate normal full-unification through integration decisions/missions and map-state checks. |
| Cross-continent union | Continental Pole opens sponsor staff and gives logistics. Sponsor decisions exist for Middle East, Asia, Europe, and South Atlantic; `africa_proclaim_dynamic_cross_continent_union` applies a dynamic union identity and fires a super-event; scripted effect has identity branches for several union combinations. | Partial. | Current decision availability requires all four sponsor charters, so one-charter African-Middle Eastern, Afro-Asian, or Afro-Atlantic union paths cannot be validated through that decision despite the effect supporting them. | Fix or intentionally document the all-four requirement. Then validate at least one single-route union and one all-route Congress/World Is One progression. |
| World Is One gate | Continental Pole maximum sets Totalen Chaos and external world-end-ready hooks but does not set proof-verified flags, `all_continent_unifiers_world_end_ready`, `africa_world_is_one_gate_prepared`, `world_end_africa_world_is_one`, or terminal flags. Proof decisions must run and register four proofs; certification sets `all_continent_unifiers_world_end_ready`; `africa_prepare_world_is_one_gate` sets `africa_world_is_one_gate_prepared`; final focus `AFR_the_world_is_one` calls `africa_mark_world_is_one_gate_ready` only when `can_africa_start_world_is_one_gate = yes`. | Pass for static gate safety; not live-tested. | Scenario can synthesize many prerequisite counters, so it is not evidence the normal campaign can reach the gate. Final trigger is strongly gated, but live ordering and proof-decision timers still need in-game proof. | Parent should run a maximum Continental Pole validation: sponsor all four, proclaim dynamic union, complete all four proof audits, certify, prepare gate, then confirm the final focus is unavailable until the prepared gate exists and only then sets `world_end`/`world_end_africa_world_is_one`. |

## Decision Category Lifecycle Notes

- `chaosx_triggerable_scenarios_triggers.txt` blocks SCN-012 when `world_end` or `event_012_africa_fired` is already set, which limits repeat-launch exploit risk.
- The Event 012 runtime context is centralized through `africa_prepare_runtime_context_from_this`, `africa_unifier_country`, and `event_012_africa_fired`.
- RSA has a separate civil-war emergency category gated by `africa_rsa_continental_side` and `africa_rsa_civil_war_active`.
- Continental Sponsorship decisions are gated by Africa Is One, sponsor readiness, route staff flags, no active `world_end`, and one-time sponsorship flags.
- The World Is One terminal focus is not directly unlocked by the scenario; it requires the prepared-gate decision and `can_africa_start_world_is_one_gate`.

## Mission Quality Notes

| Mission/surface | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_rsa_pretoria_deadline_mission` | RSA continental side | `africa_rsa_civil_war_emergency_category` | Transvaal, Cape, Natal | Hold mine/port belt, force Allied negotiators, prepare victory settlement, continental victory, Allied peace, control named states | `@africa_rsa_pretoria_mission_days` / 120 | Raises liberation momentum and legitimacy; clears active flag | Raises alarm, lowers momentum/war support, marks failure | Low; branch-specific and map-bound |
| External proof audits | Africa unifier | `africa_continent_sponsor_category` | Middle East, Asia, Europe, South Atlantic proof routes | Matching sponsor charter, dynamic union, proof ledger, external world-end-ready flag, no active world-end | `constant:africa_decision_days.external_unifier_proof` | `remove_effect` registers proof and advances proof count | `cancel_effect` applies proof failure pressure if route invalidates | Low; four intentional variants with different costs/routes |
| `africa_prepare_world_is_one_gate` | Africa unifier | `africa_continent_sponsor_category` | Global terminal gate | Totalen Chaos, Africa Is One, super-event, certified proofs, one-charter focus, internal thresholds, no prepared gate | Decision duration via sponsor mission day constant | Sets `africa_world_is_one_gate_prepared` | No explicit timeout failure; it is a preparation decision, not a mission | Low |
| Ally-under-attack opening | Africa unifier plus seeded WAC/SAH authority | Triggerable scenario setup | WAC or SAH seat plus external holder | Saved ally and external colonial holder | Instant setup, not a timed mission | Starts defensive war context and opens aid/liberation flags | No explicit fallback if no holder/ally | Medium, because absence of holder can make the validation scenario inert |

## Cost and Requirement Clarity Notes

- Sponsor, proof, certification, RSA, and World Is One gate localisation uses custom requirement/cost text with equipment, convoys, trains, manpower, command power, and XP, matching the decision skill's non-PP-store guidance.
- RSA and proof decisions use custom trigger tooltips instead of exposing raw trigger blocks.
- Cross-continent union localisation and code diverge: text says "at least one prepared cross-continent charter," while code requires all four sponsor flags.
- The World Is One gate tooltip explicitly tells the player the late thresholds: Totalen Chaos, Africa Is One, super-event, proof/certification, regional authority, living-core, historical cases, macro-regions, Bestiary, and sponsor thresholds.

## AI Validity and Route-Lock Notes

- RSA branch validity is route-locked to SAF in faction with ENG and a valid unifier candidate.
- Scenario launch is blocked after Event 012 has fired or any world-end is active.
- Sponsor/proof decisions have `NOT = { has_global_flag = world_end }` and require matching route/staff/proof flags.
- Proof decisions require external continent world-end-ready flags before proof audits can start.
- Ally-under-attack target selection is valid when WAC/SAH and an external holder exist, but lacks a blocked/fallback state when those targets are absent.
- AI weights exist for major RSA, sponsor, proof, certification, and World Is One decisions, but this audit did not test AI execution live.

## Cleanup and Exploit-Risk Notes

- Repeat SCN-012 launch is blocked by `event_012_africa_fired`.
- Continental Pole grants large resources for validation but remains one-launch scoped by Event 012 fired state.
- The scenario does not directly set proof-verified, certification, prepared-gate, terminal World Is One, or `world_end` flags; this is good gate discipline.
- Proof audits consume resources and can fail if route mandates become invalid before completion.
- The main exploit/validation risk is not direct terminal bypass; it is synthetic counter filling in Continental Pole high/maximum intensity being mistaken for proof that normal integration and Bestiary mechanics work.

## Recommended Fixes

1. In `common/decisions/012_africa_decisions.txt`, decide whether `africa_proclaim_dynamic_cross_continent_union` should require one sponsored charter or all four. If one is intended, update the availability trigger to match the existing effect and localisation while keeping all-four proof/certification requirements for World Is One.
2. In `common/scripted_effects/012_africa_effects.txt`, add visible fallback/status handling for `africa_select_fragile_unifier_candidate` when it falls back to WAC or weighted selection.
3. In `common/scripted_effects/012_africa_effects.txt`, add a fallback, blocked launch condition, or visible failure/status event for `africa_apply_triggerable_ally_under_attack_opening` when no valid ally or external holder exists.
4. In parent validation docs, classify Continental Pole as "late-route validation scaffolding" and require separate live full-unification proof for map control, living cores, regional authority integration, resistance watches, and cleanup.

## Validation Performed

- Static read-through of the requested Event 012 scenario, decision, trigger, effect, focus, constant, event, and localisation surfaces.
- Compared implementation gates against the eight requested scenario names and the accepted Event 012 source-of-truth/acceptance docs.
- No live in-game testing was performed.

## Changed Files

- Added this handoff only: `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_scenario_validation_decision_audit_handoff.md`.

No gameplay, localisation, asset, spreadsheet, or commit changes were made by this audit.
