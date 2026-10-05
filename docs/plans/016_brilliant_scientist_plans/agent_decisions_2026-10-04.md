# Event 016 agent decisions, 2026-10-04

Disposition: accepted and implemented under the full-authority mandate that the user granted for the Event 016 takeover.
Each decision below records the choice, the reason, and the implementation evidence.
Runtime behaviour that only a live session can prove is marked as such.

## D1. Host project board: review selector instead of approval

Decision: the meaningless approval order is removed, and one instant review selector drives the generic board.
The direct family rows already start every stage, so a separate approval only cost Political Power without changing anything.

Selector semantics:

- The review moves to the next family after the current one with a recorded stage, wrapping once through all fifteen families.
- The selected stage and the active, suspended, damaged, replicable, replicated, publishable, and published flags are derived from the aligned ledgers by `brilliant_scientist_refresh_directorate_project_selection`.
- The refresh runs after the selector, after each board order, at the end of `brilliant_scientist_refresh_project_counts`, and at the end of `brilliant_scientist_sync_project_force_runtime_after_ledger_change`, so incident damage, suspension, and dismantling keep the flags current.
- "Not replicated" means the independent stage has not reached the current stage, so a family that advances after replication can be replicated again at its new stage; the replicated-family count still counts each family once.
- "Public or mixed governance" means the public compact, or a secret Directorate answering to a Public Science Council, a University Research Network, or a Cabinet Safety Board.
- "Kruger not openly hostile" means Grievance below the extreme band and government control not lost.

Related corrections:

- The never-cleared native suspend, resume, cancellation, and approval request flags, their command variables, and the replication and publication receipt variables had no consumer and are removed; each order now acts and then refreshes the selection.
- Suspend, cancel, and replicate are unavailable while the reviewed family's own stage order is running, so a pending completion callback cannot resurrect a dismantled or suspended stage.
- A suspended family can no longer begin its next stage: every Deployment, Weaponization, native Prototype integration, and no-DLC Prototype row has a not-suspended requirement. Without it, suspension released capacity that the player could immediately spend advancing the same family.
- Replication completes against its locked stage even if the family advances meanwhile; only a family change, suspension, or host loss cancels it.

AI decision: the review selector is used by the AI. It stops on a programme with affordable replication, permitted publication, a resumable suspension, or active damage, and it is blocked when no programme needs board work.
The existing order weights are kept, with one guard: the AI suspends or cancels only a damaged programme or when government control is compromised or lost.
Before this change the six controls were unreachable, so no live AI behaviour regressed; the guard prevents the revived low weights from dismantling healthy programmes at random.
The suspend, resume, and cancel AI weights are refined by D21.

Evidence: `common/decisions/016_brilliant_scientist_directorate_project_board.txt` (generic block and stage-row guards), `common/scripted_effects/016_brilliant_scientist_effects.txt` (selector and refresh), `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` (refresh hook), `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` (idle, payment, publication, and AI triggers), `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` (selected programme name, stage, and status), and `docs/events/016_brilliant_scientist/systems/directorate.md`.

Reachability trace: replication calls `brilliant_scientist_replicate_project_to_requested_stage`, which raises the independent stage and recounts `brilliant_scientist_independently_replicated_family_count` through `brilliant_scientist_refresh_project_counts`.
Publication sets `brilliant_scientist_directorate_publication_completed`.
Both are the remaining inputs of `brilliant_scientist_achievement_public_method_is_complete` and `brilliant_scientist_achievement_clean_break_is_complete`, and `brilliant_scientist_reconcile_old_host_after_transfer` copies the independent stages into the former host's ledger.

Needs live game: decision-list presentation of the scripted programme names, and AI cycling cadence.

## D2. Portal raid province checks without a province scope

Decision: every `var:<province> = { ... }` scope in the Portal raid and beachhead code is replaced, because HOI4 has no province scope and the raid framework exposes `var:target_province` as an integer.

- The facility raid's native `building = { tags = facility }` target guarantees a facility in the selected province, so the target-validity trigger drops its province block and keeps the state, war, and destination checks.
- Extraction copies the raid province once and pastes it through `meta_trigger` into `any_province_building_level` for each facility family; `remove_building` keeps its documented `province = var:ROOT.target_province` argument.
- The breach state is registered on itself, so the runtime trigger drops the province-to-state test.
- Breach control uses a new STATE-scope trigger, `brilliant_scientist_portal_breach_province_is_controlled_by_root`, which pastes the stored province into a country-scope `controls_province`; the sealing decision's target and cancel triggers and the sealing settlement share it.

Evidence: `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, `common/decisions/016_brilliant_scientist_portal_containment_decisions.txt`, `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`.
References: installed `common/raids/_documentation.md` (raid instance variables and building target types), `documentation/triggers_documentation.md` (`any_province_building_level`, `controls_province`, `meta_trigger`), `documentation/effects_documentation.md` (`remove_building` province argument), and the offline wiki Triggers page (`controls_province = <id>`).

Needs live game: the native building raid supplying `var:target_province` for a facility target, and the meta-trigger province paste resolving in state scope.
Not changed: the state-target Portal raid still lands in `var:ROOT.target_province`; whether the engine fills that variable for a state target remains a live-game question recorded for the raid owner.

## D3. Portal breach cadre is a paid new cadre

Decision: the open raid-lifecycle blocker is resolved as a paid new cadre, because no documented primitive relocates one exact division and `teleport_armies` moves every qualifying army in a state.
The cadre keeps its 0.50 experience factor and arrives with 0.60 equipment and 0.70 manpower factors, read from `brilliant_scientist_portal_lifecycle` and pasted into the `create_unit` division string through the existing meta effect.
It refills through ordinary reinforcement, so a damaged raiding formation can no longer turn into a full-strength one.
The success and critical-success actor tooltips say the formation arrives under-strength.

Evidence: `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, `localisation/english/chaosx_raids_l_english.yml` (two lines), `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`.
Needs live game: the spawned cadre's initial strength readout.

## D4. Institutional-capture proof counters

Decision: the three never-written proof counters are rebuilt by `brilliant_scientist_recompute_institutional_capture_record` from permanent history only.

- Warned incidents: recorded project incident reports (`brilliant_scientist_project_incident_count`), plus one for a loyalty review that found Kruger loyalists, one for a review that found transformed personnel, and one once foreign operations against the programme have been detected. The loyalty-review flags record the latest finding, so each finding counts once.
- Domains: military command (final technical authority or the compartmentalized military office), civil administration (Kruger-selected institutions or a dismissed ethics chair), communications and logistics (Electronics or Teleportation deployment), laboratory security (the internal security section under delegated authority, or Kruger's private guard), clone replacement (Cloning deployment), machine administration (Robotics deployment), and temporal authority (Temporal deployment).
- Statewide domains: every captured domain except laboratory security held only through the private guard.

Triggers cannot run effects, so "before every caller" is met by recomputing at every writer boundary that can change the inputs or precede a reader: the end of every government-control refresh (every Mandate, Dependence, Exposure, Independent Capacity, and Grievance change), the evolution pulse before the Evolution IV check, takeover resolution, and host transformation.
The gate is wrapped in a plain-language custom tooltip.
Military command is satisfied whenever the gate's own final-authority requirement holds, so the effective bar is three further domains, which keeps takeover rare.

Evidence: `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt`, `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_triggers.txt`, `localisation/english/016_brilliant_scientist_containment_l_english.yml`, `docs/events/016_brilliant_scientist/systems/containment.md`.

## D5. Multi-site network from real facility state

Decision: `brilliant_scientist_multi_site_network_verified` is derived by `brilliant_scientist_reconcile_multi_site_network`, set while the current host owns and controls a valid primary laboratory in a core state and a valid secondary laboratory in a distinct state, and cleared otherwise.
The two distinct facility states are the network minimum. `brilliant_scientist_formation.multi_site_minimum_states` (4) stays the multi-site formation band's territory minimum, checked by `brilliant_scientist_can_form_multi_site`; reusing it as a facility-count minimum would demand four laboratory states that no host can build, and the band would stay dead.
The helper runs after primary campus and secondary laboratory establishment, after a successful relocation, in the existing `on_state_control_changed` handler for the gaining and losing host, and at the start of territory planning and containment scoring. No world iteration is added.

## D6. Temporal anchor capture

Decision: the existing `on_state_control_changed` handler calls `brilliant_scientist_lose_temporal_anchor` once for the previous controller of the anchor state when that country held the anchor (authenticated anchor, current host, or Kruger State) and has not already lost it.
Debt and history are kept; the cleared global target reopens the Kruger State discovery and authentication decisions.

Evidence for D5 and D6: `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/decisions/016_brilliant_scientist_directorate_facilities.txt`, `common/scripted_effects/016_brilliant_scientist_directorate_outcome_effects.txt`, `common/scripted_effects/016_brilliant_scientist_territory_effects.txt`, `common/scripted_effects/016_brilliant_scientist_containment_effects.txt`, `common/on_actions/016_brilliant_scientist_project_on_actions.txt`, `docs/events/016_brilliant_scientist/systems/directorate.md`, `docs/events/016_brilliant_scientist/systems/projects.md`.

## D7. Small player-visible and guard defects

- `brilliant_scientist_mengele_computation_incident` gets plain name and description keys ("Corrupted Computation Model"), matching its sibling conventional incident modifiers.
- The Kruger State recognition focus path reads the scripted trigger `brilliant_scientist_formed_by_charter = yes`; the old check read a flag that never existed, so chartered states could not use the recognition focus.
- The project incident report event checks `has_global_flag = world_end`; the old country-flag check never fired.
- Alien Arms "fielded" checks read the new public reader `alien_infantry_has_fielded_landing_cohort`, which is true once the country's landing-state registry holds a committed landing site. Seven world-threat, news, host-flavour, aftermath, and achievement reads of the never-written `brilliant_scientist_project_force_alien_arms_formation_count` now use it.

## D8. Capitulation cancels a pending alien landing

Decision: `alien_infantry_landing_reservation_is_valid` and `alien_infantry_can_call_landing_without_reserve` require `has_capitulated = no`.
A capitulated caller can no longer request a landing, and a pending one is cancelled by the mission's existing cancel trigger, whose cancel effect refunds the 2,000 laser weapons once.
The Event 026 adapter file is untouched; it reads the shared request gate and therefore inherits the same capitulation rule.

Evidence for D7 and D8: `localisation/english/016_mengele_computation_incident_l_english.yml`, `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt`, `events/016_brilliant_scientist_project_incident_events.txt`, `common/scripted_triggers/016_alien_infantry_api_triggers.txt`, `common/scripted_effects/016_alien_infantry_api_effects.md`, and the five consumer files listed in the commit.

## D9. Host project rows in three programme categories

Decision: the 118 host project rows move out of the Directorate category into Conventional, Biological, and Advanced programme categories with the same family grouping as the user-approved Mengele split of 2026-09-26.
The four xenobiological control choices join the Biological category; the Singularity audit, command node, power link, and six no-DLC component rows join the Advanced category; every family's incident mission and recovery decision joins its family's category.
The Directorate category keeps its GUI, governance, security, facilities, foreign liaison, and the six-row-maximum programme review board.
The categories reuse `GFX_decision_category_brilliant_scientist_directorate`, `GFX_decision_category_brilliant_scientist_krg_exotic_biological`, and `GFX_decision_category_brilliant_scientist_krg_portal_temporal`, add no scripted GUI, and are visible to the current host.
Decision bodies were moved verbatim: a per-decision hash comparison before and after the move matched for all 124 decisions in the file.
Known limit: while Xenobiological Synthesis sits at Theory without a chosen control, the Biological category can show its five stage rows and the four control choices together.

Evidence: `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`, `localisation/english/016_brilliant_scientist_directorate_l_english.yml`, `docs/events/016_brilliant_scientist/systems/projects.md`.
Needs live game: category ordering and density in the decision list.

## D10. Sensor Saturation is region-dependent

Decision: Sensor Saturation becomes a genuine regional operation.
The selected anchor state and every neighbouring state the actor controls receive the state modifier `brilliant_scientist_sensor_saturation_region` for the action duration: enemy army speed -30%, enemy attrition +20%, enemy local supplies -25%, and local intelligence to enemies -50%.
The modifier records its actor per state and lapses if another country takes control.
The former overwhelming national air bonus (+100% to four air values) is reduced to a minor coordination component (+20% air detection, +10% air mission efficiency, +15% interception detection and static anti-air targeting), so the action's value now depends on where it is placed.
All values are constants in `brilliant_scientist_technology_action`; costs, cooldown, targeting, and AI weights are unchanged, so no weighted surface changes.
The effect tooltip names the anchor state and its controlled neighbours.

Evidence: `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt`, `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`, `common/script_constants/016_brilliant_scientist_technology_action_constants.txt`, `localisation/english/016_brilliant_scientist_technology_actions_l_english.yml`, `docs/events/016_brilliant_scientist/systems/projects.md`.
Needs live game: state-modifier display and the regional effect on enemy divisions.

## D11. Survivable surrender and temporal escape

Decision: both Singularity alternatives from the accepted 100-focus architecture and spec part 8 are implemented inside the existing terminal and aftermath pipeline, with no new super-event, achievement, focus, or country.

- Targeting: arming registers the Kruger State in the bounded `global.brilliant_scientist_armed_singularity_holders` array, which the targeted offer decision reads; this avoids a world-scanning targeted decision and covers both the KRG tag and a transformed host.
- Survivable surrender: a country at war with an armed Kruger State above the failsafe surrender threshold can send a paid offer (50 Political Power, 25 Command Power, 60-day re-enable) from the new Singularity Counterplay category. Acceptance sets `brilliant_scientist_survivable_surrender_active` at once, so the failsafe cannot fire even if the state capitulates during the 60-day supervised disarmament mission; the mission completes controlled disarmament and verifies the nonterminal state. The surrender does not force a peace: the state still loses the war, but the world survives its capitulation.
- Temporal escape: a 14-day Kruger State decision requiring an armed device, Temporal Deployment, and an authenticated, owned, and controlled anchor. It disarms through controlled disarmament without Fallout, spends the anchor, keeps debt and history, retires Kruger, and resolves through `brilliant_scientist_evaluate_defeat_after_global_threat` as an ambiguous defeat. The custodian input is the surviving former host, then a major enemy, then any enemy.
- AI: enemies offer whenever possible, doubled when fail-deadly is live; the Kruger State accepts by default (base 10 against 1) because the offer already requires near capitulation, and refuses on the deliberate-use route (world-conquest decision or authorized detonation protocol). The AI escapes only past the surrender threshold and never on the deliberate-use route.
- Presentation: three KRG report events (`chaosx.brilliant_scientist_krg.100` to `.102`), two one-time world news events (`chaosx.nr16.319` and `.320`), and two Directorate GUI Singularity status lines. Existing pictures are reused: the sovereignty-confrontation and alien-singularity report art and the containment-coalition and Kruger State formation news art.
- Event Log: superseded by D18, which writes one Events Log history row for each alternative through the existing shared system-row API.

Evidence: `common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt`, `common/decisions/016_brilliant_scientist_aftermath_decisions.txt`, `common/decisions/categories/016_brilliant_scientist_aftermath_categories.txt`, `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`, `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`, `events/016_brilliant_scientist_kruger_state_events.txt`, `events/016_brilliant_scientist_news_events.txt`, the three localisation files, the Directorate scripted localisation and GUI localisation, and `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`.
Needs live game: the offer decision's target list, the KRG answer flow, and the caretaker succession after Kruger is retired (D20).

## D12. Project modifier remove triggers are exact negations

The third clause of 41 project modifier remove triggers was a two-condition `NOT`, which HOI4 evaluates as NOR, so a modifier whose Mengele provider became invalid while its completion flag remained was never removed.
Each such clause is now `NOT = { AND = { provider valid, stage completed } }`.
A scripted comparison confirmed that all 41 wrapped clauses match the `AND` branch of their enable blocks; enable blocks and modifier values are unchanged.

Evidence: `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`.

## D13. Biological raid AI zero factors

The 18 Event 016 biological raids zeroed their AI weight with `NOT = { ready unlocked target_valid }`, a NOR that applied only when all three conditions failed together.
Each zero factor is now `NOT = { AND = { ... } }`, so it applies whenever any of the three fails.
A scripted comparison confirmed that each wrapped condition set is identical to that raid's `available` gate, so the change only zeroes weights for raids that are already unavailable; no eligible raid's selection probability changes, and no other weight is touched.
Probability evidence: the HOI4 MCP exposes no raid adapter (`hoi4.probability_inspect` lists decision, mission, focus, technology, event, random-list, strategy, and custom-pool adapters only), and one narrow `hoi4.probability_inspect` call on `brilliant_scientist_anthrax_battlefield_biological_raid` returned `INTERNAL_ERROR`; it was not retried.

Evidence: `common/raids/016_brilliant_scientist_biological_raids.txt`.

## D14. Caller-owned incident pressure outputs

Both Mengele incident dispatchers now set `mengele_event016_computation_incident_pressure` and `mengele_event016_computation_incident_complement` to zero before calling `brilliant_scientist_mengele_load_computation_incident_pressure`, following the repository rule that a temporary first created inside a scripted effect may not survive its return.
The pressure formula, weights, and incident outcomes are unchanged, and the two API documents record the caller-owned outputs.
This closes the follow-up in `016_funded_provider_cold_lifetime_2026-10-03.md`.

Evidence: `common/scripted_effects/016_mengele_computation_incident_effects.txt` and `.md`, `common/scripted_effects/016_mengele_conventional_incident_effects.txt` and `.md`.

## D15. D'Rhondan focus rewards name their real unlocks

The four remaining D'Rhondan diplomacy focuses called `dhrondan_focus_add_diplomatic_credit`, which only set an unread flag and granted Political Power.
Each completion reward keeps its receipt flag and now shows a `custom_effect_tooltip` naming what the receipt unlocks: Covenant ratification gates the Two-World Compact offer, the map exchange gates both the compact and the Terrestrial Partner Accord, partner selection gates the accord, and the enclave congress is the Covenant's integration contract.
No extra Political Power is granted.
The helper was removed after a repository scan found no other caller and no reader of `dhrondan_diplomatic_credit_established`; the 88-focus layout and AI weights are unchanged.

Evidence: `common/national_focus/016_dhrondan_focus_tree.txt`, `common/scripted_effects/016_dhrondan_focus_effects.txt`, `localisation/english/016_dhrondan_focus_l_english.yml`, `docs/plans/016_brilliant_scientist_plans/016_final_dhr_diplomatic_rewards_plan_2026-09-02.md`.

## D16. Event 028 asteroid impact reaches the Kruger host again

The accepted asteroid-incident connection from commit `49a7a68ad` was lost when Event 028 was reworked, leaving `brilliant_scientist_record_asteroid_impact` without a caller.
One line in `asteroid_incoming_add_state_receipt_to_country` (`common/scripted_effects/028_asteroid_incoming_effects.txt`) now calls the hook in the country scope of each owner or controller of a state the impact actually damaged.
The hook acts only for the current Kruger host and is guarded by its country and character receipt flags, so it records once; no other Event 028 behaviour changes.
The Event 028 file was clean before the edit, and the edit is the single added line, made after re-reading the current file.

## D17. Exact provenance for the reused High Energy and Biological Weapons sources

Decision, under the accepted 2026-10-03 native Prototype ownership amendment: High Energy and Biological Weapons now record exact source and mode in the existing provenance arrays, with no new selection controls.

- High Energy keys on the completing project itself: the Event 016 mirror of `sp_nuclear_reactor` calls the literal wrapper `brilliant_scientist_mengele_native_completion_sp_nuclear_reactor` from its project output, and the completion hook no longer rescans it.
- Biological Weapons: the six agent projects belong to other workstreams and carry no Event 016 output hook, so the completion hook observes each agent once and treats a completed-but-unobserved agent as the completing one. The first such agent settles the family; unrelated completions observe and settle nothing. This avoids editing CBRN, Event 002, and Event 020 project files.
- A source completed after the private Theory is recorded as fresh output; a source completed earlier is adopted when the Theory settles (Biological Weapons adopts the first completed agent in fixed order). An active paid Prototype timer is never replaced.
- The nine provider-exclusive Event 016 projects (Computation, Materials, Biomedical, Teleportation, Robotics, Paleogenetics, Xenobiological Synthesis, Alien Arms, Temporal) need no selection controls: their project outputs already emit their literal family wrappers, so their source is exact by construction.

Evidence: `common/script_constants/016_mengele_native_prototype_constants.txt` (source codes 5 to 11), `common/scripted_effects/016_mengele_native_prototype_effects.txt` and `.md`, `common/scripted_effects/016_mengele_project_stage_effects.txt` and `.md`, `common/special_projects/projects/nuclear_projects.txt` (one hidden wrapper call), `docs/events/016_brilliant_scientist/systems/native_prototype_ownership.md`.
Needs live game: reactor and agent completion order against a running Mengele Theory.

## D18. Events Log rows for the Singularity alternatives

Decision: the survivable surrender and the temporal escape each append one Event 016 row to the shared Events Log history, as the lead's acceptance for the alternatives requires.
No new shared history type is needed: the existing system-row API `record_events_log_system_history_entry` already carries an event id, the event's registered type (read through `get_event_type`), a payload, and two actors, and Events 006, 012, and 028 use the same payload pattern.
`brilliant_scientist_krg_record_singularity_alternative_history` writes the row with payload 1 (surrender, Kruger State and offering country) or 2 (escape, Kruger State), then refreshes open Events Log views through `refresh_events_log_system_history_views`.
The shared scripted localisation receives four entries placed ahead of the ordinary Event 016 entries: two payload titles in `GetEventsLogHistoryEventName` and two history-context details in `GetEventsLogEventDetailDescription`, mirroring the Event 028 history-detail pattern. All other Event 016 rows keep their current name and details.

Evidence: `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt` (`brilliant_scientist_singularity_history`), `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` (four entries only), `localisation/english/016_brilliant_scientist_evolutions_l_english.yml`, `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`.
Needs live game: the two rows' titles and details in the Events Log history tab.

## D19. AI programme review stops cycling without real work

The AI continuation check for the programme review counted a suspended programme as replicable and compared the replicated-family count with the published count, so a suspended and damaged programme, or one replicated only at an earlier stage, could keep the free review control cycling indefinitely.
`brilliant_scientist_refresh_directorate_project_selection` now also derives two board-wide flags with the reviewed-programme rules, `brilliant_scientist_directorate_replication_candidate_exists` and `brilliant_scientist_directorate_publication_candidate_exists`, and `brilliant_scientist_ai_any_project_has_board_work` reads them together with the live payment and permission checks.
No order weight changes: the review control keeps its base and its two zero factors, and only the condition of the continuation zero factor is corrected.
The running-stage limit and the suspended-without-capacity loop recorded here are closed by D20.
Probability evidence: one narrow `hoi4.probability_inspect` call (`decision_ai_will_do`, candidate `brilliant_scientist_review_next_directorate_project`, source the project board file) returned `INTERNAL_ERROR` and was not retried; the change is a source-reviewed correction of a zero-factor condition only.

Evidence: `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, `docs/events/016_brilliant_scientist/systems/directorate.md`.

## D20. Round 1 review corrections

Disposition: implemented by the round 1 reviewer under the same full-authority mandate; each item corrects a defect found while reviewing the round 1 commits.

- AI programme review: D19 still let the free review control cycle while a suspended, undamaged programme lacked the Project Capacity to resume, and while the lone replication candidate's own stage order was running. `brilliant_scientist_refresh_directorate_project_selection` now also derives `brilliant_scientist_directorate_resume_candidate_exists`, the smallest resume need `brilliant_scientist_directorate_resume_capacity_needed`, the replication candidate count, and the last replication candidate family. `brilliant_scientist_ai_any_project_has_board_work` reads them with the live capacity check and skips a lone candidate whose stage is running, using the same rule as `brilliant_scientist_selected_project_stage_is_idle`. Stage, suspension, and damage changes already refresh these values; capacity is read live. No order weight changes.
- Sensor Saturation: the region took every neighbouring state the actor controlled, including occupied foreign states. The state-scope `enemy_*` and `local_intel_to_enemies` modifiers act against enemies of the state's owner (offline wiki Modifiers page, `enemy_army_speed_factor` and `enemy_attrition` rows), so in an occupied state they slowed, starved, and blinded the actor's own divisions. Neighbours must now be owned and controlled by the actor, and the modifier's enable and remove triggers require the recorded actor to own and control the state. Values and costs are unchanged.
- Temporal escape succession: when Kruger ruled in person, retiring him left the party leader to the engine, which could install the machine continuity network or another route office. The escape now promotes `KRG_project_command_council` as the despotism leader after the retirement when the state holds it, mirroring the machine-continuity `promote_character` precedent; the machine route keeps its network leader, and a transformed host without the council keeps the engine's succession. The effect tooltip says a caretaker government takes over.
- Temporal escape requirements: the `available` block printed eight raw flag identifiers. They are now one plain tooltip, `brilliant_scientist_krg_temporal_escape_device_tt`, beside the existing anchor tooltip.
- Institutional capture tooltip: the gate requires a control score of 29 or less, which is the lost band (compromised is 30 to 49); the text now says the government has lost control of the Directorate.
- Programme review description: before the first review it read "No programme, Unstarted." A summary text shows "No programme is under review yet." until a programme is selected.
- Programme category descriptions use the programme names shown in the review (for example High-Energy Physics, Temporal Mechanics).
- D5 wording: the primary laboratory is a core state; the secondary laboratory may be any distinct valid state.

Probability evidence: one narrow `hoi4.probability_inspect` call (`decision_ai_will_do`, candidate `brilliant_scientist_review_next_directorate_project`) again returned `INTERNAL_ERROR`; the AI correction is a source-reviewed zero-factor condition only.

Evidence: `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt`, `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`, `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`, `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`, the containment, directorate, technology-action, and Kruger State decision localisation files, and `docs/events/016_brilliant_scientist/systems/directorate.md`, `projects.md`, and `super_events_and_aftermath.md`.
Needs live game: the caretaker council promotion, the regional modifier on owned neighbours only, and the review summary text.

## D21. Round 1 review corrections, second pass

Disposition: implemented by the round 1 reviewer under the same full-authority mandate after reviewing every round 1 commit and the D20 corrections.

- AI suspend and resume no longer alternate. The AI suspends any active programme while government control is compromised (weight 4) or lost (weight 2), but resumed it at weight 10 whenever Project Capacity allowed, so under weak control it could suspend and resume the same programme indefinitely, paying 10 Political Power per cycle and toggling capacity and stage modifiers. The new AI-only trigger `brilliant_scientist_ai_may_resume_project` (control neither compromised nor lost) zeroes the resume weight and gates the resume branches of `brilliant_scientist_ai_selected_project_has_board_work` and `brilliant_scientist_ai_any_project_has_board_work`, so the review neither stops on nor cycles toward a programme the AI will not resume. Suspended programmes resume once control recovers.
- AI cancellation is limited to lost control. The revived cancel order kept its original preference for damaged programmes (weight 4 whenever the reviewed programme was damaged), so an AI host could permanently dismantle a whole family after one severe incident, although the family's incident response repairs it. The AI now cancels only after government control is lost, to keep programmes from Kruger; a damaged programme is suspended (unchanged weight) and repaired through its incident response. This supersedes the cancel half of the D1 AI guard.
- Survivable surrender offers cannot overlap. Event `chaosx.brilliant_scientist_krg.100` cleared `brilliant_scientist_survivable_surrender_offer_pending` in its `immediate` block, so a second enemy could send an offer while the first was still open for a human Kruger State, and both could be accepted, starting the disarmament mission twice. The flag now stays set until an option is chosen (acceptance clears it through `brilliant_scientist_krg_accept_survivable_surrender`, refusal clears it in its own effect), and acceptance also requires that no surrender or temporal escape is already underway. The 13-day default event timeout still resolves an unanswered offer.

Checked and left unchanged: the replication and publication effect tooltips omit their Independent Capacity and Grievance changes on purpose, because the Directorate design keeps both measures hidden (`docs/events/016_brilliant_scientist/systems/directorate.md`: "Independent Capacity and Grievance remain hidden").

Probability evidence: one narrow `hoi4.probability_inspect` call (`decision_ai_will_do`, candidates `brilliant_scientist_resume_selected_project`, `brilliant_scientist_cancel_selected_project`, and `brilliant_scientist_suspend_selected_project`, source the project board file) returned `INTERNAL_ERROR` and was not retried. The AI corrections are source-reviewed: one added zero factor on resume, the cancel damaged-programme factor removed, and two board-work branches gated by the same control rule.

Evidence: `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `events/016_brilliant_scientist_kruger_state_events.txt`, `docs/events/016_brilliant_scientist/systems/directorate.md`, `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`.
Needs live game: AI suspension and resumption cadence under compromised control, and a second surrender offer being unavailable while the first is open.

## D22. Xenobiological control doctrine selector and soft-lock repair

Disposition: implemented under the full-authority mandate as the round 2 lead's first item; the design choices below follow the lead's recorded direction (gate integration and the native advance, allow recovery at any stage, carry the doctrine with Kruger, and reuse the D1 selector pattern).

Defect: Deployment and Weaponization require a locked control doctrine, but the four doctrine rows were visible only at Theory. Three paths reached Prototype without one: a native synthesis completion advanced the family through `brilliant_scientist_record_new_project_prototype`, the native integration decision had no doctrine check (and the AI weighted it above the doctrine rows), and an ordinary Kruger transfer rebuilt the recipient's stage from Kruger's personal history without the doctrine. Each left the host's chain blocked for good. The four simultaneous rows also pushed the Biological category past its six-row budget (the D9 known limit).

Decision:

- Gate: `brilliant_scientist_project_family_control_is_ready` (Xenobiological Synthesis needs `brilliant_scientist_xeno_control_is_locked`, every other family passes) is added to `brilliant_scientist_complete_native_prototype_stage` and `brilliant_scientist_begin_native_prototype_integration`. A native completion without a doctrine leaves the family at Theory, and the integration row stays visible because the project stays completed. The integration row shows the plain requirement `brilliant_scientist_xeno_control_required_tt`. The no-DLC adapter keeps its existing gate.
- Recovery: the doctrine rows are visible from Theory onward while no doctrine is locked (`brilliant_scientist_xeno_control_can_be_chosen`), so existing Prototype or Deployment states without a doctrine can adopt one and continue.
- Selector: the four rows become two. `brilliant_scientist_review_xeno_control_doctrine` is a free instant cycler (chemical, neural, machine, researched) and `brilliant_scientist_adopt_xeno_control_doctrine` is one timed order that takes the reviewed doctrine's existing cost and time from `brilliant_scientist_project_board` through variable `cost` and `days_remove` fields (vanilla precedent: `cost = var:SIA_thai_cultural_mandates_pp_cost`, `days_remove = var:INS_realign_supply_chains_time`). One civilian factory, the stage-in-progress lock, and mutual exclusivity are unchanged; the adopting doctrine is fixed when the order starts and the cycler is unavailable while it runs. The Biological category now holds at most two doctrine rows, which retires the D9 known limit.
- Affordability: the strict `greater_than` Political Power check inside the requirement tooltip is removed; the native cost field is the only Political Power gate, so exactly the displayed amount is enough.
- Transfer: `brilliant_scientist_set_xeno_control_doctrine` sets one doctrine flag, mirrors it on Kruger as `brilliant_scientist_personal_xeno_control_*` while he is present, and calls `chaosx_reconcile_custom_xeno_control_grants` so no other control channel survives. `brilliant_scientist_inherit_kruger_xeno_control_doctrine` restores it during the ordinary-transfer personal-history rebuild, before `brilliant_scientist_apply_project_inheritance_outputs` grants the matching control technology at Weaponization. The Kruger State formation copy is unchanged, and the Kruger State control event `chaosx.brilliant_scientist_krg.30` uses the same helper so Kruger also carries a doctrine chosen there.
- AI: the adopt order keeps the former base weight (`ai_medium`) and the same per-doctrine preference factor (chemical at war, neural above 60% stability, machine once Robotics passes Theory, researched under the public compact). The new AI-only trigger `brilliant_scientist_ai_prefers_reviewed_xeno_control` blocks the cycler once the reviewed doctrine is preferred (or any doctrine when no preference holds) and blocks adoption of a non-preferred doctrine. Integration is gated, so the AI adopts first.

No `hoi4.probability_inspect` call was made: the route has returned `INTERNAL_ERROR` on every narrow call this run (D19 to D21), and the weight values are unchanged; the cycler and the zero factors are source-reviewed.

Evidence: `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt` (inheritance hook), `events/016_brilliant_scientist_kruger_state_events.txt`, `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`, `localisation/english/016_brilliant_scientist_projects_l_english.yml`, and `docs/events/016_brilliant_scientist/systems/projects.md` (Xenobiological control doctrine).
Needs live game: the variable cost and duration readout on the adopt row, the scripted decision title, and the AI cycling cadence.

## D23. Counter-Kruger countermeasures have real effects

Disposition: implemented under the full-authority mandate as the round 2 lead's second item; the consumer list and the KRG-targeted idea route follow the lead's recorded direction.

Defect: a successful counter-Kruger programme (120 days, 60 Political Power, 250 support equipment) only recorded arrays whose single reader was a success bonus in later foreign operations, so spec part 7's countermeasure families and the acceptance line requiring an evidence-gated opposing countermeasure for temporal actions were unmet.

Decision:

- Storage: `brilliant_scientist_countermeasure_record_family` (called from the success branch of `brilliant_scientist_foreign_apply_counter_program_result`) sets one standing flag per studied family, `brilliant_scientist_countermeasure_<family>`, and installs that family's effect once. Countermeasures answer Kruger's methods wherever they are used, since those methods travel with him, so most consumers check the holder's flag rather than a specific opponent. The only opponent-specific reader, the foreign-operation bonus, now also accepts the Kruger State formed from a studied host through `brilliant_scientist_foreign_has_countermeasure_against_operation_host` and the persistent former-host target.
- Teleportation: a state-scope custom success modifier gives Portal raids against the holder's states -15% success (both Portal raid types), and sealing a recaptured breach costs 10 Command Power instead of 25 (`brilliant_scientist_can_pay_portal_sealing`, scripted cost text).
- Biological Weapons: the same pattern gives all eighteen Event 016 biological raids -15% success against the holder's states. The precedent is the mod's state-scope modifiers in `common/raids/biological_facility_recovery_raids.txt` and the installed raid documentation's custom success modifiers.
- Temporal: `brilliant_scientist_commit_bounded_temporal_action` adds 10 temporal debt, with a tooltip line, while the user is at war with a holder (`any_enemy_country`, so only enemies are checked). Calibration debt and the temporal escape do not use the bounded helper and are unchanged.
- Singularity: a holder can offer the survivable surrender from 50% surrender progress instead of 75%; command power and Political Power costs are unchanged.
- Robotics, Cloning, Paleogenetics, Xenobiological Synthesis, Alien Arms: five permanent spirits with `targeted_modifier = { tag = KRG ... }` attack, defense, or breakthrough bonuses (vanilla `aat_dynamic_modifiers.txt` notes targeted modifiers do not work in dynamic modifiers). Known limit: a host transformed into the Kruger State in place keeps its own tag, so these spirits do not apply against it.
- Computation, Electronics, Materials, Rocketry, High Energy, Biomedical: the operation bonus stays, and one dynamic modifier, `brilliant_scientist_counter_kruger_studies`, carries a family value written as a country variable (decryption, air detection, factory air-damage reduction, static anti-air damage, factory repair speed, army attrition).
- Presentation: report `chaosx.nr16.194` shows `brilliant_scientist_countermeasure_result_tt`, which names the family and its effect through `GetBrilliantScientistCountermeasureEffect`. The decision effect tooltip, report text, and surrender-offer description describe the standing effect. Values live in `brilliant_scientist_countermeasure`; file-scoped mirrors exist only in raid and idea fields that reject constants.
- AI: no new decision, and no AI weight changed.

Evidence: `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`, `common/raids/016_brilliant_scientist_portal_raids.txt`, `common/raids/016_brilliant_scientist_biological_raids.txt`, `common/decisions/016_brilliant_scientist_portal_containment_decisions.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`, `common/ideas/016_brilliant_scientist_countermeasure_ideas.txt`, `common/dynamic_modifiers/016_brilliant_scientist_countermeasure_modifiers.txt`, `common/script_constants/016_brilliant_scientist_foreign_constants.txt`, `common/scripted_localisation/016_brilliant_scientist_foreign_scripted_localisation.txt`, `events/016_brilliant_scientist_foreign_events.txt`, the foreign, aftermath, and shared raid localisation (two sealing-cost lines in `localisation/english/chaosx_raids_l_english.yml`), and `docs/events/016_brilliant_scientist/systems/foreign_operations.md`.
Needs live game: the state-scope raid modifier resolving on the special-project facility raid's building target, the success-chance breakdown text, the variable-valued modifier lines, and the KRG-targeted spirit bonuses in combat.

## D24. D'Rhondan regime focus rewards replaced with mechanics

Disposition: implemented under the full-authority mandate as the round 2 lead's third item, under final completion contract line 237 (weak rewards replaced in place).

Defect: thirteen regime focuses (the shared convention and four focuses in each of the Imperial, Synod, and Covenant routes) paid only Political Power, Stability, Command Power, or experience plus flags nothing read, so the three regimes played alike between their roots and capstones.

Decision: each reward now changes a live D'Rhondan system, and each regime has its own character.

- Shared: Convene the Two-World Throne underwrites the next paid landing (its 2,000 lasers return on success).
- Imperial, coercive and expansionist: Restore the Ninth Diadem fortifies the border provinces of every owned landing state and of each later landing state; Bind the Landing Lords returns a 500-laser tithe per landing; Codify Imperial Service lets integration proceed during war; Crown the Enclave Empire cores every owned landing state at -2% stability each.
- Synod, predictive and efficient: Audit Every Command Node shortens landing recovery by 6 days (floor 6); Elevate the First Calculants refunds half the Political Power of reclamation, bridge, and integration orders; Replace Decree with Prediction adds infrastructure to disconnected enclaves and a second level to every bridge; Enthrone the Synod builds a civilian factory in up to three landing states.
- Covenant, consensual and population-based: Write the Dual Citizenship Code gives landing states a state modifier with non-core manpower and recruitable population; Elect the Landing Councils makes each integration raise recruits from the state's population and stability; Guarantee the Right to Depart makes compact partners grant military access and send manpower; Submit the Military to Debate lets the chamber authorize reclamation without the predictive capstone and doubles debated war-goal duration.

Implementation choices:

- Per-landing results run through one DHR hook, `dhrondan_apply_landing_dividends`, called from `dhrondan_record_successful_landing` while the landed state id is still set; recovery and descent time run through `dhrondan_adjust_landing_cooldown` and `dhrondan_adjust_landing_reservation`, called by the shared landing API only for DHR. Other API callers are unchanged.
- Dual Citizenship is a state-scoped dynamic modifier, so no fourth national spirit exists; the political lifecycle is unchanged.
- The unread flags `dhrondan_political_convention_complete` and `dhrondan_enclave_empire_crowned` are no longer set; every other flag these focuses set has a reader.
- Focus IDs, positions, prerequisites, and AI weights are unchanged; decision AI weights are unchanged.

Evidence: `common/national_focus/016_dhrondan_focus_tree.txt`, `common/scripted_effects/016_dhrondan_focus_effects.txt`, `common/scripted_triggers/016_dhrondan_country_triggers.txt`, `common/decisions/016_dhrondan_country_decisions.txt`, `common/scripted_effects/016_dhrondan_contact_effects.txt`, `common/scripted_effects/016_alien_infantry_api_effects.txt` and its `.md`, `events/016_dhrondan_country_events.txt`, `common/dynamic_modifiers/016_dhrondan_focus_modifiers.txt`, `common/script_constants/016_dhrondan_focus_constants.txt`, `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt`, the focus, country, and landing API localisation, and `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md` (Reward mechanics).

## D25. D'Rhondan military, diplomacy, expansion, and crisis rewards replaced

Disposition: implemented under the same mandate as the round 2 lead's fourth item.

Defect: eleven support focuses paid flat Political Power, Command Power, Stability, War Support, or experience plus flags nothing read; the tree doc promised that the expansion lane would expose reclamation, integration, and world-order contracts, yet `dhrondan_imperial_reaches_claimed` and `dhrondan_two_world_federation_ready` had no consumer.

Decision:

- Laboratory: The Exoplanetary Materials Board opens a laser production line requesting three military factories at 50% starting efficiency. No lasers are granted outright.
- Army: Train Human Signal Teams unlocks the Signal Company and shortens the landing reservation from 7 to 4 days; Rebuild the Expeditionary Cadres gives 5 army experience per successful landing; The Thousand-Branch Wargame advances the existing military lifecycle to Predictive Command early (Perfect Predictive Warfare keeps its tactics technology and reclamation authority); Delegate to the Field Calculants gives every army commander +1 Planning; The Foreseen Counterstroke shortens landing recovery by 4 days in wartime.
- Diplomacy: Seed the Enclave Network gives 10 civilian and 10 army intel over every country holding a marked landing state; The Embassy Beyond the Stars adds a lasting opinion bond with neighbors and partners and allows one more Terrestrial Partner Accord (`dhrondan_can_conclude_another_partner_accord`).
- Expansion: Restore the Imperial Reaches claims every marked landing state held by another country, feeding the existing Reclaim decision; Federate the Two Worlds founds the Two-World Federation faction and brings current and later Two-World Compact partners into it.
- Crisis: Offer a Shared Horizon makes cored disconnected enclaves count as supported when resolving the enclave crisis, so integration and reconciliation reinforce each other while the cipher path still needs every bridge.

The two state passes (enclave intelligence and imperial reaches) are one-time `every_state` passes filtered first on the landing-state flag; nothing periodic is added. The unread flags `dhrondan_exoplanetary_materials_board_active`, `dhrondan_field_calculants_delegated`, `dhrondan_enclave_intelligence_network_active`, and `dhrondan_imperial_reaches_claimed` are no longer set. Focus IDs, layout, and AI weights are unchanged, and no focus spirit is added.

Probability evidence: no weighted surface changed, so no `hoi4.probability_inspect` call was made.
Needs live game: land-fort placement on border provinces, the starting efficiency of the laser line, the federation faction under Deeper Factions (deprecated `create_faction`), the dual-citizenship state modifier, and the per-landing results in a real landing.

## D26. Implementation wording removed from player-facing Event 016 text

Disposition: implemented under the full-authority mandate as the round 2 lead's fifth item.

Player-visible strings no longer use receipt, provider, DLC, board-chain, registry-repair, cleanup, world-transition, or "exact ... ledger" wording. The no-special-project Prototype rows are titled "Build the ... Prototype" and the six Singularity component rows "Build the Singularity ...", their descriptions and requirements describe what the order does, the component completion tooltips say the component is complete and cannot arm or fire the device on its own, the native integration descriptions say the special project is complete and Prototype capacity is committed, and the Mengele Singularity requirement and stage tooltips describe component special projects instead of naming the DLC. Narrative uses of "ledger" (personnel ledgers, the Restoration Ledger focus, the identity ledger) and "registry" as an in-world institution stay. Keys are unchanged and every edited file keeps its UTF-8 BOM.

Evidence: `localisation/english/016_brilliant_scientist_projects_l_english.yml`, `016_brilliant_scientist_focus_l_english.yml`, `016_brilliant_scientist_requirement_flags_l_english.yml`, `016_mengele_singularity_stage_l_english.yml`, `016_mengele_teleportation_stage_l_english.yml`, `016_mengele_native_prototype_selection_l_english.yml`, `016_mengele_singularity_construction_l_english.yml`, and `016_mengele_singularity_terminal_l_english.yml`.

## D27. Mengele Rocketry AI source selection follows the researched project

Disposition: implemented under the full-authority mandate as the round 2 lead's sixth item.

Defect: the AI weighted both mutually exclusive Rocketry source selections (flying bomb and jet engine) at the high base with no link to the project it was researching, and both release decisions had weight 0. If the AI selected one source and natively completed the other, the completion could not settle Rocketry, the other selection stayed hidden, and the AI never released, so its Mengele Rocketry chain could stall short of Prototype.

Decision: the AI selects a Rocketry source only while that exact project is being researched or is complete, or when the other source cannot be researched at all; otherwise a zero factor applies. The AI releases a held selection when its project is neither being researched nor complete while the other source is, after which the other source's selection adopts the completed project. Base weights and the existing war and factory-margin factors are unchanged; the release decisions use the board's high base behind the stale-selection gate. Player controls, costs, and payload ownership are unchanged.

Probability evidence: one narrow `hoi4.probability_inspect` call (`decision_ai_will_do`, the four Rocketry selection and release decisions, source the selection decision file) returned `INTERNAL_ERROR` and was not retried; the change is source-reviewed.

Evidence: `common/decisions/016_mengele_native_prototype_selection_decisions.txt`, `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt`, `docs/events/016_brilliant_scientist/systems/native_prototype_ownership.md`.
Needs live game: AI selection timing against its native research choice.

## D28. Round 2 review touch-ups

Disposition: implemented under the full-authority mandate during the round 2 re-run review of D22 to D27.

- The adopt order reads its cost and duration as `cost = var:brilliant_scientist_xeno_control_review_cost` and `days_remove = var:brilliant_scientist_xeno_control_review_days`, matching every vanilla variable decision cost (`AST.txt` `cost = var:AST_call_on_fascists_cost`) and the `INS.txt` duration precedent that D22 cites.
- The adopt order's requirement tooltip names its real conditions (no other project stage or incident response underway, one free civilian factory) instead of a vague readiness phrase.
- The fourteen incident recovery descriptions and the Singularity dismantle guard no longer speak of repairing or dismantling a "project ledger"; they say the project is restored or dismantled and the incident stays on its record.
- Convene the Two-World Throne returns the Alien Laser Weapons the underwritten landing actually cost. The landing API keeps the settled reservation amount in the temporary `alien_infantry_landing_settled_amount` before clearing it, so a discounted Event 026 reservation is refunded at its discounted price instead of the full 2,000; ordinary and Event 019 landings still return 2,000.

Evidence: `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `localisation/english/016_brilliant_scientist_projects_l_english.yml`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, `common/scripted_effects/016_dhrondan_focus_effects.txt`, `localisation/english/016_dhrondan_focus_l_english.yml`, `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md`.
Needs live game: the variable cost and duration readout on the adopt row (unchanged from D22).

## D29. Round 2 skeptical review corrections

Disposition: implemented under the full-authority mandate during the skeptical review of the round 2 commits (05bf6bfb5, 1c93a891e, e995ef8c8, d0ceff0b2, e0af8603d, 2a2ca9ac5, dd10a3f3e).

- The Kruger State control event `chaosx.brilliant_scientist_krg.30` wraps its doctrine helper in `hidden_effect`, so its four options showed no doctrine result. Each option now shows that doctrine's effect line (`brilliant_scientist_xeno_control_effect_<doctrine>`), the same text the adopt order shows.
- The Rocketry countermeasure line claimed static anti-air damage "against rockets and jets"; `static_anti_air_damage_factor` is general static anti-air damage, and the line now says so.
- The Temporal countermeasure line coloured the holder's benefit red and used the internal "bounded temporal intervention" wording; it now shows the extra debt in green and names the actions that pay it (temporal guard batches and temporal rescues, the two callers of `brilliant_scientist_commit_bounded_temporal_action`).
- Replace Decree with Prediction printed a literal infrastructure level; it now reads `dhrondan_decision_reward.infrastructure_levels`.
- The researched control doctrine description named a fixed three-month duration; the adopt order already shows the live duration, so the description now says only that the method takes longer.
- Train Human Signal Teams grants the Signal Company with `popup = no`, matching the Support Company grant beside it.

Probability evidence: one narrow `hoi4.probability_inspect` call (`decision_ai_will_do`, the review and adopt doctrine decisions, source the project board file) returned `INTERNAL_ERROR` again and was not retried. One `hoi4.decision_inspect` call on `brilliant_scientist_adopt_xeno_control_doctrine` recognised `cost = var:brilliant_scientist_xeno_control_review_cost` as an engine Political Power cost and scored the chemical-at-war scenario at the preferred weight, with the stability, Robotics stage, and civilian-factory inputs unresolved; no AI weight changed in this pass.

Evidence: `events/016_brilliant_scientist_kruger_state_events.txt`, `localisation/english/016_brilliant_scientist_foreign_l_english.yml`, `localisation/english/016_dhrondan_focus_l_english.yml`, `localisation/english/016_brilliant_scientist_projects_l_english.yml`, `common/scripted_effects/016_dhrondan_focus_effects.txt`.

## D30. Round 2 second skeptical review corrections

Disposition: implemented under the full-authority mandate during the second skeptical review of the round 2 commits (05bf6bfb5, 1c93a891e, e7782ef8a, e995ef8c8, d0ceff0b2, e0af8603d, 2a2ca9ac5, dd10a3f3e).

- The three control-doctrine strings added in D22 (`brilliant_scientist_review_xeno_control_doctrine_desc`, `brilliant_scientist_adopt_xeno_control_doctrine_desc`, `brilliant_scientist_xeno_control_adopt_effect_tt`) broke across physical lines, which stopped the projects localisation file from loading past them. They were joined onto one line each with `\n` in 874fdc0bd and ce195cbe3 before this review; a scan of every localisation file the round 2 commits touched now finds no other line outside a key.
- The D26 wording pass left implementation phrasing in player text. The fifteen incident mission descriptions said the "exact project family will be marked damaged" and now say the project will be damaged; the Biological Weapons Prototype and Weaponization descriptions no longer say "exact"; the sabotage tooltip damages "the selected project"; the sabotage report says the project keeps its stage instead of naming a ledger; and the counter-Kruger report option reads "File the countermeasure."
- `dhrondan_enclave_crisis_resolved_tt` read as if Offer a Shared Horizon were the thing becoming a core; it now says an enclave counts once it has a supply bridge or, after Offer a Shared Horizon, is a core of D'Rhonda.

Probability evidence: one narrow `hoi4.probability_inspect` call (`decision_ai_will_do`, the four Rocketry selection and release decisions, source the Mengele selection decision file) returned `INTERNAL_ERROR` again and was not retried; no AI weight changed in this pass.
`hoi4.decision_inspect` on `brilliant_scientist_review_xeno_control_doctrine` returned only partial coverage (`DECISION_ANALYZED_PARTIAL`).

Evidence: `localisation/english/016_brilliant_scientist_projects_l_english.yml`, `localisation/english/016_brilliant_scientist_foreign_l_english.yml`, `localisation/english/016_dhrondan_country_l_english.yml`.
