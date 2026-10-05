# Event 032 agent decisions — 2026-10-04

Authority: the user granted the implementing agent full authority to take the recommended, spec-consistent option and record it here.
Each entry is an agent decision with its acceptance basis; implementation evidence is linked where it exists.

## Lead decisions carried into this round

1. The stopped thread's uncommitted fixes for the seven routed lint defects are adopted rather than rewritten. Basis: they match the routed fixes, use the shared `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days` helpers with the output temporaries preset, and every `.tools/test_event32_*.py` test passes. Disposition: `implemented`.
2. Evolution pacing uses one bounded delayed job per track, armed when the track first becomes eligible, with a randomised delay derived from its base MTTH and shortened by pressure; firings remain a fallback. The architect's full pressure ledger, hostile-pair registry and hazard-clock worker from `subagent_handoffs/032_evolution_pacing_architecture_2026-10-03.md` are `rejected` for this round. Basis: spec part 4 allows bounded delayed evolution jobs created when a threshold is first met, and the larger design adds maintenance cost with no player-visible difference.
3. Saturation doctrine and retaliation posture are explicit country decisions, and an unlock grants access only. Basis: spec part 4 lets a country decline or delay adoption and requires posture adoption to carry requirements, costs and a cooldown.
4. Missing decision families reuse the existing localisation keys, cost keys and same-family decision icons. No new art and no scripted GUI. Basis: spec decision 4.
5. `rejected` optional scope: changing the participating site or increasing preparation effort for a prepared operation (part 5 says "where allowed"), and redirecting the retaliation target after new evidence (the decision prompt allows it only when the accepted spec and engine proof permit it).
6. The physical custody model stays: the aggregate reserve is authoritative with a greedy whole-missile projection onto sites. Only the equal-split operation allocation is fixed.
7. No native raid route or icon is added; the accepted conditional scripted route in spec part 8 stands.
8. Event 032 returns to the default-enabled list only after the priority 1 and 2 gameplay items land. The catalog status change is staged in `catalog_changes_pending.md`; the workbook and CSV exports are not edited.
9. HOI4 MCP is used only with narrow queries, and timeouts are recorded as exact blockers rather than retried.
10. The duplicate native id stays a live-only item, and the temporary allocation markers remain until a fresh log attributes the error.

## Implementation decisions taken during the round

- The stray `.tools/commit_event32_scn015_qa_message_temp.txt` commit-message scratch file from the SCN-015 repair is removed; it was never part of the mod.
- The untracked probability-matrix audit handoff and its evolution-gate scenario fixture from 2026-10-03 are adopted as finished read-only evidence. Their legacy-toggle findings were already repaired by `032_evolution_toggle_binding_repair_2026-10-03.md`; the handoff stays as dated evidence.

## Item 2: project missions with reachable success paths

Disposition: `implemented` (source evidence below; live behaviour `needs_live_game`).

- Each project owns a separate state pointer and due date: `missiles_survey_site_state`, `missiles_secondary_site_state`, `missiles_repair_site_state`, and `missiles_recovery_site_state`. The shared `missiles_pending_site_state` is retired so a survey, construction, repair, and recovery can never overwrite each other.
- New timing constants: `survey_mission_days = 60` (spec part 5 asks for a short survey) and `site_recovery_mission_days = 14`. Secondary construction keeps 90 days, repair 45, verification 3, and restoration 60. Every due date is shorter than its native mission timeout.
- The rogue-site recovery mission timeout is 30 days, aligned with `missiles_rogue_tuning.crisis_window_days`; after that the rogue crisis resolves through its own timeout event and the mission cancels. Recovery needs more than `@m32_mission_recovery_division_floor = 1` divisions in the rogue site's state; AI countries are exempt from the division test because the AI cannot be ordered to garrison a named state.
- A successful repair clears all damage, applies one capacity-recovery step, and returns the site to service. A cancelled or expired repair returns the suspended site to service in its current condition. Suspension uses the new state flag `missiles_site_suspended`, which `missiles_site_can_launch` rejects, and can target wrecked (`damaged_beyond_use`) sites that previously had no repair route.
- Suspension is offered in the incident and maintenance phases (target array: the country's own site registry), because a damage incident can be inspected and closed before repair starts.
- Survey and secondary-site failure refunds are `rejected`: spec part 5 suggests returning resources according to progress, but the survey fee is small and represents completed field work, and refund arithmetic would need the decision-file cost literals moved into script constants. Failure clears only the project's own pointer, flag, and due date.
- Secondary-site construction is justified by a single working site, by stored missiles exceeding total site capacity, or by the existing mature-program signal, below the four-site cap and with Command Control at least the operation minimum.
- `missiles_establish_command_authority` is repeatable on its medium cooldown while Command Control is not yet secure, so a program whose first attempt fell short of the secure gate is not left in the establishment phase.
- Severing the network through the warning event option also starts the restoration mission, matching the decision. A completed restoration returns the network to Supervised when the evolution is available and otherwise leaves posture at Off.
- HOI4 MCP: `hoi4.decision_inspect` (inspect, `missiles_launch_state_survey_mission`, scenario `survey_due_valid`) returned `DECISION_ANALYZED_PARTIAL` at source revision `bfdfaa1e04dc…`, report `decision-21180934b5bdb71d…`: activation `always = no`, timeout 120 from `@m32_mission_survey_days`, completion/cancel/timeout effects present, and the due-date and state-pointer gates unresolved because the scenario model cannot bind `global.date` or a state-valued variable. `hoi4.probability_inspect` (`decision_ai_will_do`, four changed decisions, source `common/decisions/032_missiles_decisions.txt`) returned `INTERNAL_ERROR`; it was not retried. The AI weight changes (core-state and capital factors on survey and secondary-site targets, zero weight for suspension during a prepared operation, reduced restoration weight below secure Command Control) are therefore unaudited by the probability route.

## Item 3: captured-site resolution

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`).

- The four existing key families map to spec part 5's resolutions: guard is "hold inactive", study is "secure and inspect" (with the existing guidance-training gain), integrate, and scuttle. The "transfer through an explicit diplomatic route" resolution is `rejected` for this round; the lead's acceptance names four resolutions and no transfer localisation exists.
- Resolutions are final per state: guard and study mark `missiles_site_capture_resolved`, integrate clears the capture, and scuttle retires the site. A guarded or studied site keeps its sealed missiles in `missiles_captured_reserve_held`; it cannot later be integrated. This keeps the decisions mutually exclusive as accepted.
- One captured state is shown at a time through the one-entry array `missiles_captured_site_focus`, so the incident phase shows at most four resolution actions plus neutral-victim compensation. Incident inspection and site suspension hide while a captured site awaits resolution.
- Integration requires a guided national program (not a capture-only shell), matching the existing effect's technology rule.
- AI weights follow the stored doctrine profile: integration is preferred by guided programs and at war, halved for brittle command; scuttling is preferred at war by programs that cannot integrate, by brittle command, and for sites in foreign-owned states; guarding is preferred in peace by programs that cannot integrate and by restrained deterrents; studying is preferred by programs that cannot integrate and by counterforce guardians.
- Pre-existing ROOT-binding defects found in the capture path are repaired here because they decide whether the former controller's captured-site marker clears: the former controller and a scuttled site's controller now refresh through the new immediate receiver `chaosx.nr32.7`; `missiles_cleanup_operation` compares against `PREV.missiles_active_operation_id`; `missiles_scuttle_site` records the removed site id from the state (`PREV.id`) instead of the country.
- Network totals use controlled states and skip unresolved captured sites, so integrated sites in occupied states count toward site count and capacity.
- MCP probability inspection for the new AI weights was not re-attempted after the `INTERNAL_ERROR` recorded under item 2.

## Item 4: wartime maintenance and war/peace phase refresh

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`).

- The four maintenance actions use `missiles_maintenance_actions_are_visible`: always in the maintenance phase, and in the operations phase when no strike can be prepared, when a human has neither selected a target nor opened the country selector, or for the AI. The AI has no decision-list budget, so it can replenish and secure codes during a war without first exhausting its reserve.
- Human operations view without a target: the target selector plus four maintenance actions, plus network restoration when severed, is at most six actions. Once a human opens the selector or picks a target, maintenance steps aside for selection and preparation.
- `on_war_relation_added` refreshes the phases of ROOT and FROM when they own a program; `on_peace` refreshes the country making peace and clears an unfinished target choice (`missiles_clear_target` keeps the target of an operation already in preparation). No world iteration is added.
- Replenishment, readiness, guidance, and launch-code effects refresh phases, and `missiles_resolve_warning_queue_receipt` refreshes phases instead of forcing the operations view, which previously put a peacetime country into the operations phase after a warning closed.

## Item 7: incident aftermath decisions

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`).

- Deny responsibility is offered only for this country's own neutral accident while attribution is not confirmed; it costs 25 political power (a genuinely political act, with `ai_hint_pp_cost`), applies the existing denial opinion modifier, records the incident as disputed, and closes it.
- Emergency recalibration and debris investigation require this country's own guidance failure (breakup, wrong-state hit, dud, neutral accident, or self-strike). Debris additionally needs the impact state to be controlled by the country or a faction partner. Recalibration now also costs 5 Launch Readiness, as its tooltip and spec part 5 already state.
- Once-per-incident rule: accelerated recovery and debris investigation reset when an incident opens or closes; recalibration stays armed until the next launch consumes it. Every action also has a native cooldown.
- Budget: aftermath actions, compensation, and site suspension step aside while a captured site awaits resolution, and suspension steps aside during an own guidance failure, so the incident phase shows at most six actions.
- Icons reuse the same-family Event 032 decision icons (readiness, compensation, guidance, and inspection).

## Item 6: saturation doctrine and retaliation posture as country choices

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`).

- `missiles_evaluate_country_evolution_adoption` no longer adopts Saturation Arsenals and no longer arms the retaliation network. The Automatic Retaliation unlock still sets `missiles_evolution_automatic_retaliation`, which now means access to the warning network; posture stays Off until chosen.
- Adopt Saturation Doctrine: offered while the track is unlocked, enabled, and not adopted; requires stage Guided or higher, an active site, more than `missiles_tuning.saturation_adoption_factories = 15` factories, Command Control at the operation minimum, Launch Readiness at the floor, and no rogue command; costs 25 command power, 140 support equipment, and 700 fuel. Adoption raises the reserve ceiling to the saturation cap at once.
- Reserve packages and the mature package read `missiles_saturation_active` (enabled and adopted) instead of the raw adoption flag, so disabling the track also suspends the larger ceiling on later packages.
- Set Retaliation Posture: 15 command power and 5 Launch Readiness, 70-day cooldown, blocked during a warning, a committed retaliation operation, or a severed network; it fires `chaosx.nr32.40`, whose options now carry public tradeoff tooltips. The Automatic option keeps `missiles_posture_can_be_automatic`.
- Budget: both decisions share the maintenance visibility rule; the doctrine decision additionally hides in the human war view while a strike can be prepared, so the operations view stays within six actions. Posture and network restoration are mutually exclusive (posture requires an intact network).
- AI: the doctrine is weighted toward war, majors, multi-site programs, and away from restrained deterrents; posture changes are weighted toward war, away from countries with false-warning history, and suppressed in peace once a posture other than Off is set.
- HOI4 MCP: `hoi4.probability_inspect` (`decision_ai_will_do`, the two new decisions, source path) returned `INTERNAL_ERROR` again; `hoi4.decision_inspect` (inspect, `missiles_adopt_saturation_doctrine`, scenarios `war_major_two_sites` and `peace_restrained`) returned `DECISION_ANALYZED_PARTIAL`, report `decision-fcf01ed57b09121a…`, source revision `ae9c5befede8…`, with unbound scenario inputs. No numeric probability comparison was produced.

## Item 5: special-payload selection, use policy, and reservation

Disposition: `implemented` with one recorded deviation (source evidence; live behaviour `needs_live_game`).

- The integration decision now opens `chaosx.nr32.30` instead of fitting the first family automatically; each successful family option queues `chaosx.nr32.32` one day later so a newly fitted warhead receives standing orders instead of staying prohibited. The decline option shows only when no unfitted family remains.
- New decisions `missiles_select_special_payload` (8 command power, 35-day cooldown, opens `.31`, where conventional is always available) and `missiles_set_special_payload_policy` (15 command power, 70-day cooldown, opens `.32`, whose options now carry tooltips). All three orders require Special Warheads enabled and adopted and are hidden while an operation is prepared.
- Placement: humans issue payload orders at the objective step after selecting an enemy (two objective families, clear target, and three orders, six actions). The AI uses them in the maintenance and operations phases.
- Reservation: nuclear, thermonuclear, and biological warheads move into a held receipt at preparation, return once through `missiles_cleanup_operation`, and are consumed once at release. Deviation (`accepted and queued` for a future CBRN refund route): chemical agent is proven sufficient at preparation but still debited at release, because the shared CBRN ledgers span several storage models and expose no refund route; reimplementing their refund inside Event 032 would duplicate shared ownership.
- Event `.2` already had a single `ai_chance` block in its only option; no change was needed.
- HOI4 MCP: `hoi4.probability_inspect` for `event_option_ai_chance` (`.30`, `.31`, `.32`) returned `INTERNAL_ERROR`. No same-scenario compare was possible; the new decision weights and the `.30` decline trigger are unaudited by the probability route.

## Item 8: independent, MTTH-paced evolution unlocks

Disposition: `implemented` (source evidence; timing distribution and live delivery `needs_live_game`).

- Pacing follows lead decision 2: one bounded delayed job per track, armed at first eligibility. Delay = base MTTH (120/105/90/120/150) x 0.5 under high pressure x 1.5 when fewer than two programmes exist x a uniform random factor in [0.75, 1.25). The first evaluation above a threshold (the first high-chaos firing) arms short jobs 21 days out, staggered 14 days apart in track order. The architect's pressure ledger, hostile-pair registry, and hazard-clock worker remain `rejected`.
- The job event is `chaosx.nr32.190` on `global.missiles_evolution_host`, the first living programme in the new durable registry `global.missiles_program_registry`; `chaosx.nr32.8` refreshes each programme's access after an unlock. Both ids were collision-checked against the event file.
- Eligibility decisions per spec part 4: Rogue needs one vulnerable programme (vulnerability includes damaged, captured, or occupied sites and low stability below 0.30); Unreliable Guidance needs real strain (two low-readiness programmes, an overstocked programme, three committed launches worldwide, or half of advanced programmes without guidance investment); Saturation needs a 40% operational share of the live pool, a two-programme floor, and two programmes at war; Special Warheads counts physical payload owners only; Automatic Retaliation needs 900 chaos, no `world_end`, two operational programmes, and a responding programme at war with another operational programme. "Maturity" for the responder is taken as stage Advanced or higher (the complete line would make the track nearly unreachable); hardened command is a surviving `missiles_site_is_secure` site; the response reserve is `missiles_reserve.retaliation_reserve_cap`.
- A track whose eligibility has lapsed by its due date is dropped and re-arms when it qualifies again. The job commits at most one track per run and re-queues itself after `job_stagger_days = 7` when another track is due, so several unlocks never land on one day.
- `missiles_record_evolution_unlock` no longer sets the per-pulse marker flag and now clears the committed track's pending state, which also covers SCN-015 direct unlocks.
- Pressure shortening: Rogue at two vulnerable programmes, Guidance at two programmes at war, Saturation at four programmes at war, Special at two payload owners, Retaliation at two responder pairs.
- HOI4 MCP: `hoi4.probability_inspect` (`direct_random`, candidate `missiles_arm_evolution_track`, source `common/scripted_effects/032_missiles_operations_effects.txt`) returned `INTERNAL_ERROR`, as every probability inspect in this session did; the 2026-10-03 audit recorded 600-second timeouts for the same adapter family. No compare was possible, so the EVO timing distribution is unaudited by MCP.

## Item 9: whole-missile allocation by capacity

Disposition: `implemented` (source evidence and a Python model of the allocation; live behaviour `needs_live_game`).

- Allocation is a bounded water-fill (at most `operation_max_sites_per_strike + 1` passes): each pass offers every site with spare capacity an equal whole share (floor of remaining divided by open sites, at least one) capped by its room. This keeps every site of a saturation barrage participating where possible, unlike a greedy fill of the first site, and sums exactly to the cost whenever the combined capacity covers it. Capacities 10 and 2 with a cost of 10 now allocate 8 and 2 instead of being refused.
- A site that receives no missiles leaves the operation, so every listed site holds a positive allocation.
- Settlement decision: a capture, owner scuttle, destruction by strike, or wrecking natural disaster of a reserving site ends the order, refunds the reservation, and then debits exactly that site's allocation once (the readied missiles are lost); a non-wrecking disaster refunds everything. Captured readied missiles are not credited to the captor, keeping the settlement exact and single.
- The natural-disaster settlement previously compared against the disaster chain's ROOT instead of the site controller; the new helper matches the operation id inside the controller's own scope.

## Item 10: default enable and catalog staging

Disposition: `implemented` for source; catalog `accepted and queued`.

- Event 32 (`constant:missiles_event.id`) is added to `event_log_event_is_reworked_default_enabled` in the shared `chaosx_settings_triggers.txt` with a single-line edit; another owner's uncommitted line in the same list is left unstaged and untouched.
- `catalog_changes_pending.md` stages `Events!M33` to `Needs Testing` and the Evo I and Evo V wording, which now matches the updated `missiles.evolution.saturation.body` and `missiles.evolution.automatic_retaliation.body` localisation (Saturation is a chosen doctrine; posture is a chosen delegation).
- The test matrix gains live cases for this round; the test-results record lists the passing source modules and the MCP limits.

## Round 1 review (skeptical reviewer)

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`). Basis: the user's grant of full implementation authority; each change repairs a defect in this round's own work and keeps its accepted design.

- A suspended site carried none of the flags `missiles_state_has_registered_site` accepts, so capture, strike damage, natural disasters, inheritance, civil-war splits, and annexation skipped it and a suspended site lost in war stayed dead in its owner's registry. `missiles_site_suspended` now counts as a registered site; the capture handler already clears it.
- `missiles_record_incoming_operation_site_damage` rewrote `missiles_site_repair_due_date` and the repair flags for a newly damaged site, which postponed a running repair programme at another site, and a scuttled second site cleared `missiles_site_repair_active` and cancelled that programme. Both writes now run only when no repair mission is active.
- A programme whose only site was suspended entered the establishment phase and could survey a second state for the survey fee, bypassing the secondary-site limit and justification. `missiles_country_can_start_survey` now waits for the repair mission.
- AI: a special warhead selected under a policy other than Military Targets Only or Unrestricted War (at war) makes every ordinary preparation fail. The `.31` special options now carry a reject factor through the new `missiles_special_payload_policy_permits_ordinary_use` trigger, and `missiles_select_special_payload` never makes such a selection and swaps an existing one back. At war, the AI no longer suspends a damaged site that can still launch.
- Player text: "program" in four new tooltips reads "programme" like the rest of the Event 032 text, and the survey and secondary-site requirement tooltips state the owned-and-controlled rule.
- HOI4 MCP: one more `hoi4.probability_inspect` call (`decision_ai_will_do`, candidate `missiles_set_retaliation_posture`, source path) returned `INTERNAL_ERROR`; the AI changes above are source-reviewed only.
- Left as recorded limits: two evolution jobs due on the same day can each commit one track (each job commits at most one); special-payload selection and posture changes can repeat at war on their cooldowns; a suspended site transferred by planned inheritance or a civil-war split is released inactive.

## Round 1 review, second pass (skeptical reviewer)

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`). Basis: the user's grant of full implementation authority; each change repairs a defect in Event 032's own warning and evolution flow and keeps the accepted design.

- Warning outcome flags were sticky. `missiles_warning_false_or_conflicting` was never cleared, so after one false alarm an Automatic posture never answered any later warning; `missiles_warning_delayed` was never cleared, so the event's delay option disappeared for every later warning; and the Delay Retaliation decision was `fire_only_once`. The new `missiles_clear_warning_outcome_flags` clears the four per-warning outcome flags when a warning opens (impact queue and the Retaliation Network scenario seed), when it resolves, and in removed-country cleanup; each route records its outcome after resolution. Delay Retaliation is once per warning on its existing cooldown. `missiles_false_warning_history` stays as the long-term record.
- The Accept the Current Response decision called `missiles_commit_operation`, which does nothing without a prepared operation, so the decision spent nothing and did nothing. It now runs the same `missiles_accept_retaliation_response` route as the warning event, and the event option, the decision, and the posture route share the new gate `missiles_retaliation_response_can_be_accepted` (actionable and unanswered warning, chain caps, launch slot, launch-capable controlled site, response reserve, and the ordinary preparation checks). Decision and event-option texts describe the order and its requirements.
- Event `chaosx.nr32.80`: the verify option hides once verification was ordered through the decision and activates the mission only when verification actually started; the verify, delay, and accept options show their effect tooltips.
- Evolution pacing armed tracks only during Event 32 firings, so a track that became eligible between firings (most war-dependent tracks) waited for the next firing, contradicting `EVO-PACE-02`. One evolution watch (`chaosx.nr32.191`, `watch_days = 30` in `missiles_evolution_pacing`) now reruns the registry-bounded evaluation on the host while an enabled track is locked, arms newly eligible tracks, and re-queues itself; a removed host hands it to a living programme and a lost watch is replaced once its date passes. No all-country scan is added.
- Player text: "incident root", "command ledger", "bounded participant group", and "precision ledger" are replaced by plain wording.
- The previous pass's uncommitted warning work was adopted after review; its flag-interpreter test was replaced by static source checks in `.tools/test_event32_retaliation_warning.py`, and `.tools/test_event32_evolution_gates.py` pins the watch.
- HOI4 MCP: see the round-1 review entry in `032_missiles_test_results.md` for the routes attempted in this pass.

## Round 2 lead decisions

Made by the lead under the user's full-authority grant and recorded here as each item landed.

1. The stopped thread's uncommitted rogue-site and isolation work (six Event 32 files written between 02:09 and 02:12 on 5 October) is finished and adopted rather than discarded. Basis: it repairs a real exploit (isolating or scuttling any launchable site ended a rogue crisis) and a dead end (an isolated site could never return to service), and follows spec part 4's rogue resolution.
2. The Event 13 bridge is one guarded line at the end of Event 13's state-scope building-damage helper, and every controller-side mutation runs under the controller's ROOT through a hidden immediate country event.
3. Chemical warheads stay checked at preparation and debited at launch; holding chemical agent stays `accepted and queued` for the CBRN owner, and Event 32 re-checks the agent at launch instead.
4. Events 5 and 6 need no new edits; the uncalled planned-inheritance helpers stay, and only their suspended-site handling is fixed.
5. Previously rejected options stay rejected and previously accepted limits stay accepted (see the round-1 entries).
6. The catalog change stays staged in `catalog_changes_pending.md`, and the probability checks remain a recorded blocker (`hoi4.probability_inspect` returned `INTERNAL_ERROR` again for `missiles_scuttle_rogue_site`; not retried).

## Round 2 item 1: rogue-site resolution and isolation

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`). Basis: lead decision 1.

- Adopted after review: rogue isolation and scuttling target only the rogue crisis site (`missiles_site_is_rogue_incident_site`, matched by the id recorded when the crisis opened) through `state_target = yes` and `target_array = missiles_launch_site_states`; `missiles_isolate_site`, `missiles_scuttle_site`, and the strike or disaster adapter `missiles_scuttle_site_from_current_controller` close the crisis only for that site; isolation settles a reserving order in refund mode once, stops re-hardening, and the isolated site can be suspended and repaired back into service; the regional-seizure timeout isolates the seized site and leaves it compromised; the AI scuttle weight favours destruction only for a site holding a special warhead.
- Finished in this round: the missing `missiles_rogue_site_target_tt` (and `missiles_retaliation_site_target_tt`) are localised; the suspension requirement, effect, and isolation texts name isolated sites; `missiles_isolate_retaliation_site` now targets `missiles_launch_site_states` with the same tooltip pattern; the source test reads the captured-reserve block by its limit instead of the first `if`.
- Agent decision: instead of temporarily repointing `missiles_incident_site` (the stopped pass's `missiles_point_incident_at_rogue_site`, removed), the rogue crisis never writes the general incident pointer. The candidate site is selected straight into `missiles_rogue_site_state`, and every rogue path (family weights, open, launch, custody payload, timeout, recovery, the two rogue triggers, and the rogue-resolution achievement inputs) reads that pointer. Basis: lead acceptance allows either using the rogue pointer directly or restoring the previous one; the direct pointer cannot leak and needs no restore bookkeeping.
- Agent decision: `missiles_close_rogue_incident` no longer clears `missiles_incident_site`, and it closes the general incident record (`missiles_last_incident_closed`, `missiles_incident_active`, `missiles_active_incident_id`) only while the rogue incident is the current one. Basis: the same cross-incident defect as the pointer overwrite; a damage, disaster, or capture incident opened during the crisis must stay open with its own site.
- Agent decision: the Command Breakdown scenario seed selects actors, sets the family, and opens the crisis only when a crisis can open, so a crisis that is already open keeps its own actors and family; a breakdown candidate that opens no crisis is cleared.
- Evidence: `.tools/test_event32_captured_sites.py` gains `RogueSiteResolution` (registry targeting, crisis-site trigger, closure only for the rogue site, no general-pointer writes, current-incident-only closure, isolated-site repair path, single refund, localisation keys); all 12 `.tools/test_event32_*.py` modules pass.
- HOI4 MCP: not re-attempted for the AI weight change on `missiles_scuttle_rogue_site` (lead decision 6); the change is source-reviewed only.

## Round 2 item 2: Event 13 natural-disaster bridge

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`, test `BRIDGE-13`). Basis: lead decision 2 and spec `032_missiles_system_connections.md` (Event 13 calls a narrow Event 32 adapter; a disaster never activates an evolution).

- Event 13 change: one guarded line at the end of `natural_disaster_apply_family_building_damage` in `common/scripted_effects/013_natural_disasters_effects.txt`, added right after re-reading the file with a byte-level insertion that keeps its mixed line endings. That helper serves the primary, repeated, neighbour, and chain-arrival impacts. Nothing else in Event 13 changes, and Event 13's own documentation is left to its owner.
- `missiles_natural_disaster_damage_site` is now queue-only: it validates the registered site and its proven controller, reads the severity from Event 13's unscoped temporary `natural_disaster_current_severity` through `check_variable` only (no `has_variable`), stores the strongest pending severity on the state, adds the state to the controller's `missiles_disaster_pending_sites`, and fires the new hidden immediate receiver `chaosx.nr32.9` on the controller.
- Agent decision: the receiver carries the state through the controller's pending-site array rather than through event targets or `FROM`, so it works whether the event runs at once or later in the tick; the first receiver applies every queued site once and empties the array, later receivers do nothing, and two impacts on one site before the receiver runs apply once at the stronger severity.
- `missiles_apply_natural_disaster_site_damage` (STATE, ROOT is the controller) holds the former adapter body with every `event_target:missiles_disaster_controller` block replaced by `ROOT`, so the reserve settlement, allocation settlement, network counts, custody, incident id, repair request, phase refresh, and achievements land on the controller. A wreck settles once through `missiles_scuttle_site_from_current_controller`; a lesser hit leaves a damaged site that the site-damage incident phase offers for suspension and repair. The helper calls no evolution code.
- `.tools/test_event32_state_scope.py` gains `NaturalDisasterBridge`; `.tools/test_event32_ordinary_preparation.py` now checks the settlement in the receiver-side helper.
- HOI4 MCP: `hoi4.event_inspect` (`lint`) rejected two selector forms with `Invalid tool arguments`; with the documented selector `{ kind = event, eventId = chaosx.nr32.9 }` (`trace`, upstream, depth 1, no refresh) it returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics at revision `6d739c748137…` (graph `d425874a5aff…`); whole-workspace helper projections were deferred by the server, so the adapter-to-receiver path is source-reviewed.

## Round 2 item 3: refused retaliation orders

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`, test `WARN-03`). Basis: the round-1 recorded limit and the lead's acceptance.

- `missiles_accept_retaliation_response` now saves the current target choice (`missiles_save_target_choice_for_retaliation`: selected enemy and id, objective, target state, and objective lock) before it writes the attacker. When `missiles_operation_preflight_result` is not accepted it clears the pending parent, root, root-country, and generation values and the retaliation operation type, strike profile, payload, and target-state id, and `missiles_restore_target_choice_after_retaliation` restores the saved choice or calls `missiles_clear_target` when there was none. The warning is not resolved, no outcome flag is set, and the accepted branch is unchanged.
- Agent decision: the saved choice uses persistent country variables cleared at the end of every accept call rather than temporaries, because the preparation chain between save and restore is long and shares temporary names.
- `.tools/test_event32_retaliation_warning.py` gains `RefusedResponse`.

## Round 2 item 4: chemical agent re-checked at launch

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`, test `PAY-04`). Basis: lead decision 3.

- `missiles_commit_operation` runs `missiles_check_chemical_payload_stock` for a chemical operation before committing. A failed check takes the invalidated path: `missiles_abort_operation` (exact reserve refund) and `missiles_cleanup_operation`, with no launch and no payload dispatch. The decision and the delayed retaliation commit (`chaosx.nr32.83`) both reach it, so the AI follows the same path. Other payloads commit exactly as before.
- Agent decision: the player sees the reason in the category context line through a new preparation-failure value `missiles_preparation_failure.chemical_agent = 11` and the key `missiles_preparation_failure_chemical_agent`, and the launch effect tooltip states that a chemical strike is called off when the stores no longer hold enough agent. Basis: the check is an effect over CBRN temporaries and cannot run inside the launch decision's `available` trigger, so the abort report is the reliable place.
- Holding chemical agent at preparation stays `accepted and queued` for the CBRN owner: it needs a CBRN refund route that Event 32 must not duplicate.
- `.tools/test_event32_special_payload.py` gains `ChemicalLaunchCheck`.

## Round 2 item 5: suspended sites that change hands

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`, test `MISSION-07`). Basis: the round-1 recorded limit ("a suspended site transferred by planned inheritance or a civil-war split is released inactive"), now resolved, and lead decision 4.

- `missiles_finalize_civil_war_split_child` and `missiles_finalize_planned_inheritance` clear `missiles_site_suspended` on the transferred site, which stays compromised and isolated, so the new controller can suspend and repair it. The capture handler already did this.
- Agent decision: the same clear is applied to both controller receipts in `missiles_cleanup_removed_country`, the annexation counterpart of the same transfer; `missiles_finalize_civil_war_split_parent` is left unchanged because the parent keeps its own sites and a suspended one stays under its running repair programme.
- The former owner's programme ends through its own cleanup: the repair and recovery missions already cancel once their target state is no longer controlled, and `missiles_cancel_site_repair_project` now releases a suspended site only while the country still controls it, so a late cancellation never clears the new owner's suspension; its flags, due date, and pointer are always cleared. The recovery cancellation already touched only its own fields.
- `.tools/test_event32_project_missions.py` gains two tests for the transfer and the former owner's cleanup.

## Round 2 review (skeptical reviewer)

Disposition: `implemented` (source evidence; live behaviour `needs_live_game`, tests `ROGUE-SITE-05`, `ROGUE-SITE-06`, `WARN-04`). Basis: the user's grant of full implementation authority; each change repairs a defect in this round's own work against the accepted design and keeps it.

- A single-site program whose only site was isolated (rogue isolation, the regional-seizure timeout, or Isolate One Retaliation Site) had no working site and fell back to establishment, where suspension was never offered, so the isolated site could never return to service and the round-2 repair claim failed for most programs. `missiles_site_suspension_is_offered` now also covers the establishment phase outside a capture shell; this also lets a single damaged site be repaired after its incident closes.
- Agent decision: Isolate One Retaliation Site stays open to a human for any working site, but its AI weight is zero for a site that is not compromised. Basis: spec part 4 and part 6 ("isolate compromised sites") and probability scenario `WARN-05`; the AI used to cut off a working site on every warning and then spend a 45-day repair on it.
- A retaliation against a different attacker inherited the human's target state and objective chosen against the earlier enemy, so `missiles_select_operation_target_state` looked for that state inside the attacker and refused every such order. The accept route now clears the pending target state and requested objective when the attacker is not the saved enemy, as selecting a new enemy does, and a refused order restores both with the rest of the saved choice.
- Chemical launch check text: the check also fails when chemical use is no longer permitted or ready, so the failure line and launch tooltip say the chemical weapons are no longer available or permitted instead of naming only the stores.
- A country removed during an open rogue crisis left `global.missiles_rogue_active_incidents` counted forever; removed-country cleanup now releases it and clears the rogue site pointer and id.
- Reviewed without change: rogue-only resolution and pointer separation, the Event 13 one-line bridge and receiver `chaosx.nr32.9` (severity ordering, controller ROOT, single settlement), the refused-order cleanup, the chemical re-check placement, and the transfer-time suspension clearing.
- HOI4 MCP: `hoi4.probability_inspect` (`decision_ai_will_do`, candidate `missiles_isolate_retaliation_site`, source path, no refresh) returned `INTERNAL_ERROR`; the AI weight change is source-reviewed only and was not retried.

## Round 3 item 1: former controller bound before the site capture handler (inbox 032 L1)

Disposition: `implemented` (source evidence; live capture behaviour `needs_live_game`, tests `CAP-04` and `CAP-05`). Basis: lead round-3 decision 1 and the routed live-load defect L1 (`exists` evaluated on FROM resolving to a State in `missiles_handle_site_control_changed`).

- `missiles_handle_site_control_changed` no longer reads FROM. Its limit requires `has_event_target = missiles_capture_former_controller` and that target to exist as a country other than ROOT, and every former-controller read and write (the stored former controller and id, the reserve cap, the lost allocation, the network debit and receiver event `chaosx.nr32.7`, the Empty the Silos tracking loop, and the incident actor id) goes through that target.
- `on_state_control_changed` saves its own FROM as the target before entering `FROM.FROM`; `missiles_reconcile_released_country_sites` saves each site's stored `missiles_site_current_controller` and skips a site without one.
- Agent decision: the target is a regular event target, so it clears when the callback chain ends; the release pass rebinds it for every state before each call, so no state reads another state's holder.
- Agent decision: every write of `missiles_site_controller_id` (registration, repair, rogue recovery, integration, inheritance, civil-war split, annexation receipts) now stores the same country in `missiles_site_current_controller`, and every reset clears it. Basis: the variable was previously written only by the capture handler, so the release pass named in the acceptance would have skipped every site that had never been captured.
- `.tools/test_event32_state_scope.py` gains `SiteCaptureFormerController` (no FROM token in the handler, `exists` only in country scopes, both callers bind the target before the call, and every controller-id write keeps the stored controller in step).
- Committed as `dcf3822f3` ("Bind the former controller before the Event 32 site capture handler"); this commit is the reply to inbox 032 L1.

## Round 3 item 2: Event Logs identity, names, detail text, pre-unlock toggles, and history row

Disposition: `implemented` (source evidence; display and toggles `needs_live_game`, tests `LOG-01` to `LOG-04`). Basis: lead round-3 decisions 2 and 6, spec part 1 (Event Logs coverage), and CLAUDE.md section 6.

- Evolutions use the canonical identity: event id `constant:missiles_event.id`, type `constant:missiles_event.evolution_type` (32), stage = catalog number (I Saturation 1, II Guidance 2, III Special Warheads 3, IV Rogue 4, V Automatic Retaliation 5). The new `missiles_set_evolution_log_context` sets it for both `missiles_record_evolution_unlock` and `missiles_commit_evolution_track`. Before this, the record wrote type 1 to 5 with stage 1, so the shared name views showed the Zombie, Communism, and Holy Realm titles for Saturation, Guidance, and Special Warheads.
- Every toggle flag was renamed from `events_log_disabled_evolution_32_<N>_1` to `events_log_disabled_evolution_32_32_<N>` across the six owner script files and the gate test; no old spelling remains in `common/`, `events/`, or `.tools/`. Saves from before the rename need no migration (lead decision 2).
- Agent decision: the logged tier is the chaos tier id of each track's minimum chaos (Saturation 3, Guidance 2, Special Warheads 4, Rogue 1, Automatic Retaliation 4) for the record, the commit gate, and the Event Details preview. The commit gate's tier check in `is_current_evolution_enabled` is implied by each track's own eligibility, so pacing is unchanged; SCN-015 calls the record directly and is not tier-gated.
- Shared Event Logs files (minimal Edit-tool inserts; other owners' uncommitted Equipment From Heavens hunks left untouched and uncommitted): one Event 32 preview block in `events_log_rebuild_open_event_details_view` (five rows, each with its toggle before unlock), and entries in `GetEventsLogEvolutionTypeView`, `GetEventsLogEvolutionNameView`, `GetEventsLogSelectedHistoryEvolutionTypeView`, `GetEventsLogSelectedHistoryEvolutionNameView`, `GetEventsLogEventDetailEvolutionTypeView`, `GetEventsLogEventDetailDescription`, `GetEventsLogEventDetailEvolutionTitle`, `GetEventsLogSelectedEvolutionTitle`, `GetEventsLogSelectedEvolutionBody`, `GetEventsLogSelectedEvolutionSummary`, and `GetEventsLogHistoryRowText`.
- Agent decision: the history row uses `missiles.event_log.history.row` only for firings with at least one recipient (payload above zero) and now carries the standard sequence, date, id, type, and event header; a firing with no valid recipient keeps the generic row instead of reporting zero programmes. New key `missiles.evolution.type` ("Missiles") labels the evolution type.
- `.tools/test_event32_evolution_gates.py` gains `EvolutionLogIdentity` (constants, shared context helper, old-spelling scan, Event Details preview rows, and every log surface's key).
