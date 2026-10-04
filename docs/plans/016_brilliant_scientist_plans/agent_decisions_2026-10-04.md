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
