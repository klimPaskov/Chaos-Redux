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

Decision: `brilliant_scientist_multi_site_network_verified` is derived by `brilliant_scientist_reconcile_multi_site_network`, set while the current host owns and controls a valid primary and a valid secondary laboratory in two distinct core states, and cleared otherwise.
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
- Event Log: no separate Events Log row is written. Event 016 logs its firing and evolutions in the shared log; its terminal outcomes, including these two, surface through report events, news, and the Directorate status line. Adding a new shared system-history type was judged a shared-framework change outside this round.

Evidence: `common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt`, `common/decisions/016_brilliant_scientist_aftermath_decisions.txt`, `common/decisions/categories/016_brilliant_scientist_aftermath_categories.txt`, `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`, `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`, `events/016_brilliant_scientist_kruger_state_events.txt`, `events/016_brilliant_scientist_news_events.txt`, the three localisation files, the Directorate scripted localisation and GUI localisation, and `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`.
Needs live game: the offer decision's target list, the KRG answer flow, and the escape's leaderless-state handling after Kruger is retired.

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
