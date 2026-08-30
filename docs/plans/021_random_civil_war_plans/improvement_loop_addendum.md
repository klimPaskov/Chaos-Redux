# Event 021 Random Civil War Improvement-Loop Addendum

Date: 2026-08-30

Entry event: `chaosx.nr21.1`

Status: Open implementation addendum

Recommendation: Continue with one bounded expansion tranche. Event 021 has a substantial framework, but it is not ready for closure because several accepted promises are represented by generic proxies, Scotland-only adapters, shallow or unreachable branches, and weighted systems that do not yet have complete probability evidence.

## Addendum gate and ownership

This is the first improvement-loop addendum for Event 021.

No earlier `improvement_loop_addendum.md` exists under `docs/plans/021_random_civil_war_plans/`.

The existing architect, completion-audit, probability-audit, localisation, art, icon, and spreadsheet handoffs were reviewed as evidence, but none is a prior improvement-loop addendum.

The parent must implement, promote, explicitly queue, or reject this addendum with reasons before requesting another Event 021 improvement-loop pass.

This document is a plan only.

It does not claim gameplay implementation, balance approval, visual approval, or completion.

## Focused design problem

Event 021 currently has most of the promised containers: pressure and authority variables, target preparation, route and severity values, state reservation and rollback, ordinary/Event 006/same-tag openings, a normal decision category, evolution events, a bounded global pulse, Wars cluster registration, a scenario, AI strategies, logs, details, achievements, and static assets.

The remaining problem is not a lack of more features.

The problem is that the existing containers do not consistently prove the fiction and gameplay state they claim to represent.

Generic country facts open political routes, archetypes are effectively uniform among valid routes, severity is selected as a deterministic band, connected-state planning grows only one neighbor pass, force validation treats factory count as equipment, the Event 006 adapter is Scotland-specific, the same-tag route has almost no contest, Evolution I cannot reach four belligerents, exposure randomly chooses policy for the player, scheduler order can starve entries, recurrence is evaluated while its own grace lock is active, scenario intensities do not implement their percentage promise, and cluster reservations do not cover every actor/target role before delayed launches.

The expansion tranche should therefore be titled **Evidence-backed fracture transaction and lifecycle completion**.

It should deepen the existing mechanic without adding unrelated countries, a custom scripted GUI, a super-event, a new focus route family, technology, doctrine, 3D content, animation, or portrait work.

## Evidence reviewed

The review covered every file under `docs/specs/021_random_civil_war_specs/`, the Event 021 implementation and documentation, the Event 004 Random War collision predicates, the Event 006 Independence Wave runtime package and focus adapters, the Event 007 Fury collision predicates, the Wars cluster implementation and documentation, the existing Event 021 handoffs, the event catalog workbook, the offline wiki pages required by `AGENTS.md`, relevant vanilla documentation, and vanilla civil-war and dynamic-country precedents.

The research model already accepted by the Event 021 specs remains appropriate:

- UCDP's organized political-claim threshold supports requiring an identifiable claimant, institution, command, or territorial project instead of treating every low-stability country as equivalent.
- Fearon and Laitin support state weakness as a risk factor without making diversity or state count a sufficient cause.
- Cederman, Wimmer, and Min support exclusion plus mobilization as stronger regional evidence than geography alone.
- Salehyan and Gleditsch support cross-border exposure and networks while cautioning against treating displaced civilians as automatic belligerents.
- Walter supports recurrence when settlements fail to preserve credible political means.
- Cunningham and Bakke support more difficult settlement when several autonomous actors remain.
- SIPRI material supports tracking external assistance as a relationship with a recipient and duration, not as an unowned random flag.

The strange-incident material in the source spec remains fictional or attribution-uncertain inspiration only.

It must not become claims about real religions, ethnic groups, or atrocities.

## Already covered and to be preserved

| Surface | Current evidence | Addendum disposition |
|---|---|---|
| Event availability | Event 021 is present in the default event allowlist and has availability, prefire, and no-target handling. | Preserve. The old default-disabled audit finding is stale. |
| Reusable state core | `event021_initialize_country_state`, `event021_refresh_country_state`, `event021_reduce_pressure`, `event021_add_authority`, clamping, and pressure/authority bands exist. | Extend through evidence receipts and expiry; do not replace the core variables. |
| Target weight application | `event021_random_civil_war_prepare_target`, `event021_parent_add_target_to_selection_pool`, and `event021_parent_prepare_random_event_fire` make target weight affect the draw. | Preserve the concept, but replace repeated array copies and the world prefire scan with a declared fair pool. The old claim that target weights were ignored is stale. |
| Transaction safety | `event021_parent_begin_target_transaction`, state reservations, `event021_parent_validate_opening_plan`, and `event021_parent_rollback_transaction` exist. | Preserve and expand final topology, remnant, actor, and receipt validation. |
| Ordinary force split | `event021_parent_prepare_start_ratios` passes `size`, `army_ratio`, `navy_ratio`, and `air_ratio` to `start_civil_war`. | Preserve the real engine shares. Remove false precision from factory-derived equipment estimates. |
| Event 006 origin safety | Event 021 uses separate adapter flags and does not intentionally set Event 006 fired/evolution/generation/league/congress origin state. | Preserve this hard boundary. Generalize package content without invoking Event 006's origin lifecycle. |
| Event 006 focus visibility | `independence_wave_focus_tree` and `can_use_independence_wave_full_focus_framework` already include Event 021 adapter branches. | Preserve. Do not rewrite the tree or its layout. |
| Decision surface | `event021_civil_war_crisis_category` contains seven decisions and two missions with centralized costs and role-aware fragments. | Preserve the normal category and current actions. Add only missing phase choices and correct target binding. |
| Global pulse | Event 021 runs through the existing global-host daily pulse and does not add an unrestricted daily `every_country` on action. | Preserve. Do not introduce a new world-iteration hook. |
| Wars cluster | Row 1003 registers Events 004, 007, and 021 and emits one pacing event. | Preserve the row and pacing event. Add role reservations and exact skip receipts inside the shared transaction. |
| Scenario registration | The workbook and implementation use current scenario identifier `SCN-018`. | Preserve the identifier. Replace fixed counts with the promised proportional locked-pool transaction. |
| Logs and details | Event 021 has system-log, event-log, detail, evolution, and achievement plumbing. | Preserve the shared framework. Extend Event 021 snapshots and localisation only. |
| Static assets | `interface/021_random_civil_war.gfx` references 35 unique textures and the inspected files exist, including report/news art, category art, decisions, missions, ideas, and achievements. | Reuse. No broad art tranche is justified. |
| Workbook | Event row 22, Wars cluster row 2, and `SCN-018` row 15 are present. | Preserve as source of truth; update only after implementation facts are accepted. |

## Priority map

| Priority | Gap | Why it blocks closure |
|---|---|---|
| P0 | Evidence-backed pressure, route, target, archetype, and severity selection | The opening fiction and weighted behavior are not yet demonstrated by actual organized claim evidence or complete probability pools. |
| P0 | Connected theater, capital, remnant, and force transaction | The current single-pass geography and factory-derived equipment proxy cannot prove a viable civil war or viable parent remnant. |
| P0 | Generic origin-neutral Event 006 package adapter | The accepted package reuse promise is currently Scotland-specific, while some Event 006 decision gates intentionally hide package content from Event 021. |
| P0 | Fair global scheduler, proportional scenario, and cluster role reservations | Current registration and review order can starve countries, scenario intensities contradict their percentage text, and delayed cluster members can collide after preparation. |
| P1 | Front-plan registry and same-tag contest | Evolution I cannot reliably produce two to four belligerents and the one-state/all-island route lacks a meaningful internal contest. |
| P1 | Phase decisions, exposure, sponsors, and actor-bound missions | Several implemented helper effects are not exposed and the current exposure roll makes foreign policy choices for the player. |
| P1 | Settlement obligations, reconstruction, recurrence, and caps | Several accepted outcomes are unreachable or cosmetic, and recurrence is tested while its grace lock prevents eligibility. |
| P2 | AI evidence, durable logs/details/evolution records, docs, workbook, and final assets audit | The framework exists, but it cannot close until every weighted surface has measured scenarios and every player-facing record matches actual committed state. |

## P0.1 Evidence-backed pressure and route state

### Current contradiction

`event021_parent_prepare_route_evidence` makes ideology broadly valid for a normal government, legal-institution valid for any ruling leader, regional valid for more than one state, and command valid for more than one division.

The associated pressure flags are largely set by low stability, low political power, war, manpower, state count, and factory count, but they are not consistently cleared when their evidence disappears.

This conflicts with the accepted organized-opposition, institutional-claim, regional-grievance, and command-fracture model.

### Required design

Keep pressure and authority as reusable country state, but make each non-generic route depend on at least one live or unexpired evidence receipt.

The parent should add a documented receipt API to `common/scripted_effects/021_random_civil_war_effects.txt` and matching validity triggers to `common/scripted_triggers/021_random_civil_war_triggers.txt`.

Use these proposed public identifiers unless the owner documents a conflict with an existing reusable helper:

- `event021_register_fracture_evidence`
- `event021_clear_fracture_evidence`
- `event021_refresh_fracture_evidence`
- `random_civil_war_has_live_ideological_evidence`
- `random_civil_war_has_live_legal_evidence`
- `random_civil_war_has_live_regional_evidence`
- `random_civil_war_has_live_command_evidence`
- `random_civil_war_has_live_event6_package_evidence`

Each receipt needs source type, strength band, start date, expiry date or live proof, actor/package/region scope when applicable, and a cleanup owner.

Country size, a normal government, and the existence of a leader may modify weight, but none may independently open a route.

Pressure flags derived from recoverable country conditions must clear when the condition recovers unless a dated historical receipt explicitly keeps residual pressure.

`event021_parent_prepare_route_evidence` should aggregate the receipts and live conditions; it should not invent missing opposition evidence.

The external adapter contract should accept narrow registered receipts from other events without treating those events as fired and without importing their lifecycle flags.

### Acceptance checks

- IL021-01: A stable two-state country with a leader, two divisions, and no evidence receipts has no ideological, legal, regional, command, or Event 006 route solely because of those generic facts.
- IL021-02: A live command receipt opens the command route, raises its weight, expires on its recorded date, and is cleared when its referenced command actor no longer exists.
- IL021-03: Recovering stability, authority, manpower, and administrative capacity clears live-condition pressure contributions while preserving only explicitly dated residual receipts.
- IL021-04: A source event can add and later clear pressure or authority evidence through the public helpers without setting Event 021 fired or Event 006 fired state.

## P0.2 Target, archetype, and severity weighted pools

### Current contradiction

The target weight is used, but `event021_parent_prepare_random_event_fire` scans `every_country` and duplicates each candidate in a temporary array up to its weight cap.

`event021_prepare_archetype_weights` assigns equal weight to each valid route, so evidence strength does not distinguish valid routes.

`event021_prepare_opening_severity` and `event021_parent_select_severity` select bands deterministically rather than maintaining a weighted severity distribution inside hard safety gates.

### Required design

Declare complete candidate manifests for target, archetype, and severity pools so the probability tooling can see every candidate, condition, base weight, modifier, zeroing gate, and fallback.

Use the existing `random_civil_war_target_weight`, route validity triggers, and severity safety gates, but change their consumption:

- Target selection draws once from the registered due-country pool without repeated array copies.
- Archetype weight includes route-specific receipt strength, receipt recency, actor viability, pressure/authority interaction, Event 006 package attestation, and the same-tag safety route.
- Severity has Limited, Contained, Severe, and Critical candidates inside a complete weighted pool.
- One-state and all-island safe routes hard-zero Severe and Critical.
- Major-country Severe or Critical remains hard-zero until an accepted evolution or scenario gate allows it.
- Critical pressure and occupation may raise high-severity weight, but they must not bypass remnant, actor, generation, or global-cap safety.

The owner must define balance targets before patching.

This addendum does not invent percentages because current MCP evidence cannot normalize the incomplete pools.

### Acceptance checks

- IL021-05: The complete TGT, ARC, and SEV manifests enumerate all candidates and hard-zero reasons, and the weighted-logic auditor can evaluate the named low-pressure minor, high-pressure minor, one-state, all-island, major, Event 006 package, and blocked-cap scenarios.
- IL021-06: Repeated seeded simulation demonstrates that stronger matching evidence raises the intended archetype share without making other valid routes unreachable, while one-state/all-island and major safety gates remain absolute.
- IL021-07: After the owner patch, `hoi4.probability_compare` uses the same named scenarios as the baseline audit and reports target, archetype, and severity changes separately.

## P0.3 Connected theater, capitals, remnants, and force receipts

### Current contradiction

`event021_parent_plan_connected_states` chooses a random anchor and grows through only one `every_neighbor_state` pass, with a maximum of five states.

It does not recursively prove a coherent region, use rail/supply/port/industry value in anchor selection, prove a connected route to the actor capital, or revalidate the parent remnant after every planned transfer.

The Event 006 opening hardcodes Scotland and state 121.

`event021_parent_prepare_dynamic_force_package` derives a requested equipment amount from military-factory count and assigns fixed support/artillery minima, but ordinary `start_civil_war` actually transfers stockpile through `size` and transfers armed forces through `army_ratio`, `navy_ratio`, and `air_ratio`.

The engine documentation does not expose a separate `stockpile_ratio` field for `start_civil_war`.

### Required design

Replace the single-pass plan with a recursive bounded connected-region transaction.

The transaction should:

1. Build an anchor pool from owned and controlled states while excluding the protected parent capital and reserved states.
2. Score anchors with route evidence, population or victory-point value, factories, infrastructure, supply node, railway, naval base or coastal access, package anchor, cores, and claims where those facts are valid.
3. Grow only through adjacent eligible states until the severity target or cap is reached.
4. Never add a disconnected bonus state to meet a number.
5. Store the selected actor capital before mutation.
6. Validate that every non-island actor state is connected to the actor capital and that the actor has a viable supply or port route.
7. Validate that the parent retains its protected capital, a connected viable remnant, minimum industry, manpower, and force capacity.
8. Roll back every state flag, array row, capital receipt, and tag/package reservation if any final validation fails.

Use proposed helpers `event021_parent_build_anchor_pool`, `event021_parent_grow_connected_region`, `event021_parent_validate_actor_region`, `event021_parent_validate_parent_remnant_after_plan`, and `event021_parent_record_opening_receipts` around the current `event021_parent_plan_connected_states` transaction.

For ordinary civil wars, treat `start_civil_war.size` as the authoritative stockpile and fuel share and `army_ratio`, `navy_ratio`, and `air_ratio` as the authoritative force shares.

Do not describe military-factory count as an equipment quantity.

Use actual division, manpower, and equipment-availability bands for preflight capacity where engine triggers support them, including `has_army_size` or `count_in_collection` where appropriate.

After actor creation, record actual actor division and manpower values plus an equipment-availability band.

Fail closed or use the accepted same-tag route when no viable actor package exists.

The Event 006 manual-release path may use package-owned force effects, `transfer_units_fraction`, or `send_equipment_fraction` only after the package owner proves the exact ownership and release sequence.

### Acceptance checks

- IL021-08: For continental, archipelagic, landlocked, coastal, and Event 006 package fixtures, the map inspection proves the selected states, adjacency chain, actor capital, supply/rail/port basis, and surviving parent remnant.
- IL021-09: A two-division low-stock host never receives a fixed oversized package; a high-capacity Severe fixture transfers more than a low-capacity Limited fixture; the parent retains its configured defense floor; and all force-share sums remain within their configured caps.
- IL021-10: A failed final topology or force receipt invokes `event021_parent_rollback_transaction` and leaves no reserved state, tag, package, front, or origin flag behind.

## P0.4 Generic origin-neutral Event 006 package adapter

### Current contradiction

`event021_parent_event6_dormant_candidate`, `event021_parent_event6_package_complete`, `event021_parent_find_event6_package`, and `event021_parent_start_event6_front` are effectively bound to SCO, `IW-001`, state 121, and `independence_wave_setup_iw_001_scotland`.

Event 006 already owns generic runtime package admission and dispatch through `has_independence_wave_runtime_package_adapter_for_execution_id`, `has_independence_wave_runtime_package_content_attestation_for_execution_id`, `is_independence_wave_runtime_package_preflight_ready`, `independence_wave_dispatch_package_setup`, `independence_wave_dispatch_package_final_validation`, and `independence_wave_dispatch_package_cleanup`.

The Event 006 focus tree already recognizes Event 021 adapter flags.

However, the accepted Event 021 spec promises full package-local content reuse, while the current Event 006 SCO category guard deliberately requires `is_independence_wave_active_country` and hides Event 006 decisions from an Event 021-origin actor.

### Required design

Generalize Event 021 to every package admitted by Event 006's current runtime content-attestation registry.

Do not copy a fixed package count into Event 021.

Add an origin-neutral Event 006 content predicate, proposed as `is_independence_wave_package_content_active`, whose only valid branches are a real Event 006 active country or an Event 021 actor with `random_civil_war_event6_adapter_complete`, package identity, and content-attestation proof.

Use that predicate only for package-local government, formation, formable, former-host settlement, focus, and AI content promised by the package.

Keep `is_independence_wave_active_country` for Event 006 pre-event, active-origin arrays, network, league, congress, patron, global generation, evolution, and event-log lifecycle.

Add an origin-neutral validation dispatcher, proposed as `independence_wave_dispatch_package_origin_neutral_validation`, or parameterize the existing dispatcher so it can validate package identity, setup, focus, ideas, AI, decisions, and formables without requiring Event 006 origin registration.

Generalize `event021_parent_find_event6_package`, `event021_parent_event6_dormant_candidate`, `event021_parent_event6_package_complete`, and `event021_parent_start_event6_front` around stored package ID, host, package actor/tag, anchor, and validation result.

Event 021 must never set `independence_wave_active_origin`, register the actor in Event 006 active/network/league/congress arrays, increment Event 006 generation or cap counters, publish Event 006 evolution records, or mark Event 006 fired.

### Acceptance checks

- IL021-11: At least one audited package from each available Event 006 region family completes an Event 021-origin preflight, release, package-local content validation, and cleanup with no Event 006 origin/network/league/congress/evolution receipts.
- IL021-12: The SCO package and every other currently attested package use the same generic adapter path; no Event 021 effect contains a package-specific tag, execution ID, setup effect, or anchor state outside a declarative package registry.
- IL021-13: Package-local focuses, formation/formable decisions, former-host settlement, ideas, and AI are visible when their own gates are met, while Event 006 pre-event and global institutional content remain hidden.

## P0.5 Fair scheduler, proportional scenario, and cluster reservations

### Global scheduler

`event021_parent_global_scheduler_pulse` samples random countries with replacement during registration and reviews the registry from its beginning.

The temporary review index does not establish a persistent round-robin cursor.

Later entries and later critical-queue rows can therefore wait indefinitely behind earlier entries.

Keep the current global-host pulse, but add persistent `global.random_civil_war_review_cursor` and `global.random_civil_war_critical_cursor` variables.

Registration must exclude already registered countries so bounded samples are without replacement until the eligible roster is covered.

Review must advance its cursor after every considered row, repair the cursor after stale-row removal, wrap at most once per pulse, and process no more than the configured budget.

The critical queue must be FIFO by due date or use the same rotating rule so one blocked row cannot starve later due rows.

`event021_parent_prepare_random_event_fire` should draw from registered due countries rather than execute a fresh `every_country` scan.

Do not add an unrestricted country-iterating on action.

### Fracture Cascade scenario

Low, Medium, High, and Maximum currently request fixed counts 1, 2, 3, and all, while localisation and workbook text promise approximately 10, 25, 50, and 100 percent.

At confirmation, lock one eligible-country array and its denominator.

Compute target count as the nearest integer to 10, 25, 50, or 100 percent, with minimum one when the pool is nonempty and clamp to the locked pool size.

Select without replacement from a working copy.

Queue all selected rows through the existing bounded global-host scheduler and complete the accepted transaction within seven days.

Maximum may bypass the scenario's ordinary global concurrency cap only if the parent confirms that accepted spec rule, but it must never bypass tag safety, state reservations, remnant safety, route proof, or generation safety.

Record the locked denominator, requested count, committed count, skipped count and exact reasons, and completion date.

### Wars cluster

Row 1003 already owns one queue and one pacing event, but delayed members do not reserve all actor and target roles during cluster preparation.

Add aligned shared reservation rows for Event 004 aggressor and target, Event 007 actor and target, and Event 021 host, ordinary opposition, Event 006 package actor, and package anchor before any delayed member fires.

`random_war_country_can_be_aggressor` must reject Event 021 reservations as its target predicate already does.

Event 021 must see the exact Fury target receipt, not only Fury actor or recent-actor flags.

Required skip IDs are `no_eligible_actor`, `no_eligible_target`, `role_collision`, `tag_occupied`, `state_reservation_failed`, `cap_reached`, `generation_blocked`, and `stale_delayed_reservation`.

Baseline excludes incompatible cross-use.

Any high-chaos overlap must be an explicit named evolution gate and may never assign one country to incompatible simultaneous roles.

### Acceptance checks

- IL021-14: A roster larger than one review budget reaches every eligible row within a calculable maximum number of pulses; removing the current cursor row does not skip its successor; and a blocked critical row does not starve later due rows.
- IL021-15: Scenario fixtures with eligible pools of 1, 2, 3, 7, 10, 11, and 100 countries produce the documented rounded target count, never select a country twice, finish within seven days, and reconcile every requested row as committed or skipped with an exact reason.
- IL021-16: A seeded Wars cluster collision suite proves that all 004/007/021 roles are disjoint at baseline, delayed launches consume their own reservations, stale reservations clean up, and exactly one pacing event is emitted.

## P1.1 Front-plan registry and same-tag contest

### Multi-front plan

The baseline ordinary opening creates one opposition.

Evolution I can create one nested secondary front, so it does not yet implement the accepted two-to-four-belligerent theater with independently tracked goals and settlements.

Before mutation, create a bounded front plan whose rows contain generation, archetype, route, actor type, package ID where relevant, anchor, capital, connected-state array, actor scope, goal, status, and settlement.

Use proposed aligned arrays:

- `random_civil_war_planned_front_archetype_entries`
- `random_civil_war_planned_front_anchor_entries`
- `random_civil_war_planned_front_goal_entries`
- `random_civil_war_planned_front_status_entries`
- `random_civil_war_planned_front_actor_entries`
- `random_civil_war_planned_front_generation_entries`

Baseline plans one opposition actor.

Evolution I may add up to two more opposition actors only when each actor passes connected-region, tag/package, parent-remnant, front-cap, and generation checks.

The fourth belligerent may be ordinary or an attested Event 006 package actor through the generic adapter.

Extend `event021_register_front`, `event021_set_priority_front`, `event021_parent_try_secondary_front`, `event021_parent_review_secondary_front`, and `event021_parent_close_secondary_front` to consume the plan rows rather than relying on one special secondary actor.

Each front receives an actor-specific goal and terminal settlement.

The crisis closes only after every registered front row is terminal or explicitly rolled back.

### Same-tag route

Keep one country, one tag, and one owner for the one-state/all-island safe route.

Do not create a duplicate country and do not transfer ownership merely to imitate a civil war.

Add a bounded dual-power contest with `random_civil_war_same_tag_government_leverage` and `random_civil_war_same_tag_claimant_leverage`.

Store government and claimant objective nodes in `random_civil_war_same_tag_government_nodes` and `random_civil_war_same_tag_claimant_nodes` using the capital, supply, railway, naval-base, and depot evidence available in the host.

Actions and missions move leverage and objective receipts until the current deadline.

Resolution may preserve the government, replace the cabinet or governing coalition for the claimant, or accept autonomy/coalition terms when those terms have a valid internal claimant.

Represent claimant zones through state flags, state modifiers, decision targets, and durable receipts, not through a fake duplicate country.

### Acceptance checks

- IL021-17: Baseline produces two belligerents; eligible Evolution I fixtures produce three or four; ineligible fixtures remain at two; every added actor has a unique safe scope, capital, connected states, goal, and settlement row.
- IL021-18: A one-state and an all-island fixture expose a meaningful same-tag contest, never create a duplicate tag or transfer the sole state, and resolve from objective and leverage state rather than only whether talks were opened.

## P1.2 Phase decisions, missions, exposure, and sponsors

Keep a normal decision category with three to five visible actions and one to three missions per phase.

Do not introduce a dedicated scripted GUI.

Wire the existing but unexposed helpers `event021_decision_monitor_border`, `event021_decision_support_government`, `event021_decision_support_opposition`, and `event021_decision_integrate_formations` into explicit decisions where their phase and actor targets are valid.

The required phase surface is:

- Opening: preserve `event021_secure_arsenals`, `event021_defend_capital`, `event021_review_loyalty`, and opposition-only `event021_seize_depot`.
- Multi-front: expose integration of formations and a priority-front target action using `event021_set_priority_front`; keep only role-valid capital or depot actions.
- Neighbor exposure: expose monitor border, relief corridor, support government, support opposition, mediation, and no commitment, but show only three to five choices appropriate to the country's actual exposure channel and capacity.
- Settlement: preserve `event021_offer_emergency_settlement` and add mediator or sponsor disengagement only when a real mediator or sponsor exists.
- Reconstruction: preserve `event021_reconstruct_administration` and add one settlement-obligation mission.

Bind `event021_secure_rail_spine_mission` to a stored planned railway or supply target instead of accepting any controlled state above an infrastructure threshold.

Give the mission dynamic localisation for the named target state and front.

Separate exposure from commitment.

`event021_parent_expose_neighbor` and `event021_apply_regional_exposure` should record source crisis, border/maritime/network channel, severity, and expiry only.

They must not randomly choose armed support, relief, or no aid for a player.

Use proposed `event021_parent_record_exposure`, `event021_apply_sponsor_commitment`, and `event021_clear_sponsor_commitment` helpers.

Every sponsor commitment stores sponsor, recipient side and front, support type and amount band, dependence, start date, end or cleanup condition, and recognition or mediation state.

Displaced civilians remain a relief and capacity issue, not an automatic security threat.

### Acceptance checks

- IL021-19: Every phase has no more than five visible actions and no more than three missions, and each action disappears when its actor, front, exposure, or phase is no longer valid.
- IL021-20: The rail mission names and checks its planned target; controlling an unrelated high-infrastructure state cannot complete it.
- IL021-21: Human exposed neighbors receive a choice; AI exposed neighbors use audited weights; every material commitment names a recipient front and cleans up on expiry, sponsor death, recipient death, settlement, or rollback.

## P1.3 Settlements, reconstruction, recurrence, and caps

`event021_parent_select_settlement_terms` currently selects government victory, opposition victory, independence, autonomy, or coalition.

Partition, merger, and evolution flags exist in the accepted design language but are not selected by the current implementation.

Do not leave dead outcome labels.

Implement them only with these gates, or explicitly remove them from the accepted spec during promotion:

- Partition requires at least two durable territorial front rows with non-overlapping connected regions and viable surviving capitals/remnants.
- Merger requires a surviving successor that can legally absorb a resolved front without destroying the protected remnant contract.
- Evolution is a log classification for a systemic multi-front settlement and must not substitute for territorial or legal effects.

Every settlement stores front-bound obligations selected from disarmament, recognition or autonomy, capital and railway restoration, sponsor withdrawal, reconstruction, and any package-specific former-host term.

`event021_parent_review_settlement_obligation` must mark a violation only for an actual breached obligation or a committed recurrence, not merely because recurrence is eligible.

Fix recurrence ordering.

`event021_parent_apply_settlement` may calculate a recurrence score while successor grace is active, but it must not try to make the recurrence immediately eligible through `random_civil_war_recurrence_valid` while that same grace flag blocks the trigger.

Store `random_civil_war_recurrence_earliest_date` and `random_civil_war_recurrence_latest_date`.

The fair scheduler must reevaluate the country when grace expires, launch only inside the window with generation, recurrence cap, global cap, cooldown, route, remnant, and tag checks, and clear eligibility after the latest date while preserving historical memory.

Do not remove the country from the review roster before its due recurrence evaluation is reconciled.

### Acceptance checks

- IL021-22: Every selectable settlement has distinct legal, territorial, reconstruction, and cleanup effects; every non-selectable documented outcome is explicitly rejected from the promoted spec.
- IL021-23: Recurrence cannot launch during grace, is reevaluated on the earliest date, cannot launch after the latest date, respects generation and global caps, and never marks an obligation violated merely for becoming eligible.
- IL021-24: Every settlement and recurrence path closes all front, sponsor, reservation, mission, package-adapter, and queue rows without deleting the durable history receipt.

## P2 Closure tranche

### AI and probability evidence

Keep the existing role profiles in `common/ai_strategy/021_random_civil_war_ai_strategy.txt`, but extend them only after the missing choices exist.

Required role scenarios are government consolidator, hardliner, negotiator, revolutionary claimant, legal claimant, regional claimant, Event 006 package claimant, command claimant, same-tag claimant, neighbor containment actor, mediator, sponsor of government, sponsor of opposition, and reconstruction survivor.

The one-state route must hard-zero impossible territorial-transfer actions.

The Event 006 adapter must inherit package-local AI without gaining Event 006 network, league, congress, or origin behavior.

The mandatory probability matrix remains TGT, ARC, SEV, EVO, FRT, SPN, STR, SET, REC, GLB, CLU, and SCN.

Each surface needs a complete candidate manifest, named inputs, hard-zero gates, deterministic fixtures, seeded simulation where selection is random, threshold sweeps where weights are continuous, and sequence analysis where a scheduler or queue is involved.

The owner must apply balance changes.

`chaosx_ai_probability_auditor` remains read-only and must run the baseline and the mandatory `hoi4.probability_compare` on the same scenarios after the owner patch.

### Logs, details, and evolutions

Extend `event021_parent_record_system_log`, the Event 021 branch in `common/scripted_effects/chaosx_events_log_effects.txt`, and the matching scripted localisation so each durable record snapshots numeric, tag, and state facts at commit time.

Do not depend on a temporary event target or a country that may later die.

Required payload includes host, claimant or package actor, actor archetype, evidence route, severity, capital, connected region summary, force-share bands, front count and selected priority front, sponsor and recipient, settlement and obligations, recurrence generation, cluster skip reason, and scenario requested/committed/skipped counts.

Add exact cluster skip localisation and wire the existing no-target text or remove it if the owner proves it is unreachable.

The authority localisation fallback must not display Collapse for an uninitialized country.

Do not redesign the shared event-details GUI in this addendum.

### Assets, docs, and workbook

Reuse the current static asset family.

Request a new icon only after a new visible decision or mission identifier is registered and only when no existing Event 021 icon is semantically exact.

If needed, route that bounded icon list to `chaosx_icon_artist` after source identifiers are stable.

No new report art, news art, portrait, flag, animation, custom panel, super-event, 3D model, or sound package is required.

After implementation and audit, reconcile `docs/events/021_random_civil_war/overview.md`, the Event 021 asset manifest and handoffs, the accepted specs, and `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Keep the workbook event status `To Be Reworked` and scenario status `Needs Testing` until the implementation and scenario evidence pass.

After a successful workbook update, run `python .tools/export_event_catalog_csv.py` and never edit the exported CSV files directly.

### Closure acceptance

- IL021-25: Every new or changed player-visible identifier has localisation, trigger and effect descriptions, a valid icon reference, AI behavior where AI-usable, and an exact Event 021 log/detail payload.
- IL021-26: The completion, decision/mission, country-package, focus, localisation, AI/probability, asset, and documentation audits contain no unresolved accepted gap, fallback, placeholder, or stale Event 021 fact.
- IL021-27: The parent may issue a closure handoff only after all P0 and P1 checks pass, P2 evidence is reconciled, every accepted plan is promoted or explicitly rejected, and no blocker below remains unresolved.

## Exact implementation surfaces

Primary Event 021 owners:

- `common/script_constants/021_random_civil_war_constants.txt`
- `common/scripted_effects/021_random_civil_war_effects.txt`
- `common/scripted_effects/021_random_civil_war_effects.md`
- `common/scripted_effects/021_random_civil_war_parent_effects.txt`
- `common/scripted_effects/021_random_civil_war_parent_effects.md`
- `common/scripted_effects/021_random_civil_war_decision_effects.txt`
- `common/scripted_triggers/021_random_civil_war_triggers.txt`
- `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`
- `common/scripted_triggers/021_random_civil_war_parent_triggers.md`
- `common/decisions/021_random_civil_war_decisions.txt`
- `common/decisions/categories/021_random_civil_war_categories.txt`
- `common/ai_strategy/021_random_civil_war_ai_strategy.txt`
- `events/021_random_civil_war.txt`
- `common/scripted_localisation/021_random_civil_war_localisation.txt`
- `localisation/english/021_random_civil_war_l_english.yml`

Shared and adjacent owners, only where the contracts above require them:

- `common/scripted_effects/006_independence_wave_effects.txt` and its paired documentation for the generic origin-neutral dispatcher.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for package attestation and origin-neutral validation.
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `common/decisions/categories/006_independence_wave_categories.txt`, `common/decisions/006_independence_wave_decisions.txt`, and `common/decisions/006_independence_wave_shared_decisions.txt` for origin-neutral package-content visibility.
- `common/decisions/006_independence_wave_scotland_wales_decisions.txt`, `common/decisions/006_independence_wave_formable_decisions.txt`, and `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt` are the first explicit package/formable registry checks; touch another `common/decisions/006_independence_wave_*_decisions.txt` file only when its currently attested package-local predicate requires the same origin-neutral gate.
- `common/national_focus/006_independence_wave_focus.txt` only if adapter visibility gates need correction; no route or layout rewrite is authorized.
- `common/scripted_triggers/004_random_war_triggers.txt`, `common/scripted_effects/004_random_war_effects.txt`, `common/scripted_triggers/007_fury_triggers.txt`, and `common/scripted_effects/007_fury_effects.txt` only for the shared Wars role-reservation contract.
- `common/scripted_effects/chaosx_event_cluster_effects.txt` and its documentation for row 1003 reservation and skip receipts.
- `common/on_actions/chaosx_on_actions_chaos_meter.txt` only to keep the existing bounded global-host pulse wired; no new all-country hook.
- `common/scripted_effects/chaosx_events_log_effects.txt` and `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` for Event 021 payload fields.
- `interface/021_random_civil_war.gfx` only if accepted new visible identifiers require icons.
- `docs/events/021_random_civil_war/overview.md` and Event 021 asset documentation after implementation facts are stable.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` followed by the required CSV exporter.

## Required validation sequence

1. Reinspect Event 021, Events 004/006/007, and row 1003 through the read-only event tools after implementation.
2. Reinspect and render the Event 006 focus tree to prove adapter availability and confirm that the tree layout was not changed accidentally.
3. Inspect and render every continental, archipelagic, coastal, landlocked, same-tag, and Event 006 theater fixture through the map tools.
4. Start every weighted audit with `hoi4.probability_inspect`, route it through `chaosx_ai_probability_auditor`, and do not accept source-only arithmetic as equivalent evidence.
5. Run the same named TGT/ARC/SEV/EVO/FRT/SPN/STR/SET/REC/GLB/CLU/SCN scenarios before and after the owner patch through `hoi4.probability_compare`.
6. Inspect and render the shared event-details window for Event 021 payload length, missing localisation, state visibility, clipping, overflow, and click regions, but route any framework layout patch to the shared GUI owner rather than Event 021.
7. Run focused country-package, focus, decision/mission, localisation, completion, asset, docs, workbook, and collision audits.
8. The user retains in-game validation; agents do not launch Hearts of Iron IV.

## MCP evidence and unresolved tooling limits

### Event chains

Event 021 and Events 004, 006, and 007 were inspected and rendered through the read-only event routes at revision `ac2516cf55a8`.

All four returned partial structural evidence because helper and lifecycle workspaces were deferred.

The evidence proves current entry/option/event structure but does not prove helper state flow, cleanup, or runtime cluster collision behavior.

Event 021 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a541eaf4bd06cd481d6c42e0eb2a8ee1293a3ed4a570e8dd784e10b2f3d8c4f3/ce22f0e163e1d547e2478245f2f7943a287e6676fca2181d665c7914ba1d0c20/event-trace-ac2516cf55a8.json`.

Event 021 render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/229079536a8a055be3f91ea4ab23d2cc57f10df7ad412c98a2afb740232d6534/4ae0b47d10c3c306e611869fc7e2b6033827dacbc17cf682c447e53cffc61ecb/event-overview-ac2516cf55a8.svg`.

The Event 004, 006, and 007 trace and render artifacts are retained in the MCP workspace and should be compared after the owner patch.

### Focus tree

The Event 006 `independence_wave_focus_tree` was inspected and rendered read-only.

The inspect route found 184 focuses and no source-local blocking diagnostic; the only reported localisation warning belonged to a vanilla continuous focus.

The tree contains explicit Event 021 adapter gates, so a broad focus rewrite is not justified.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f333da91d52df38ef5664959f242837a0072474a75d9aa782abba28803fb1452/a8a24d6f1858258a854023c94c5dc317c2345cb987b1ad09f78572d05285e4a6/focus-inspect.d38dae6e78f07993.json`.

Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e81ed3efc2a2d7463e50fc6ff674ac37eceabc359b14f398b5ea21cb87b7500/92aa5795124b2667329ab608e2a45905b20fc1414206d9a6ce3525b33b3eaa63/independence_wave_focus_tree.focus.svg`.

### Map

The read-only map inspection covered state 121, the full map overview, adjacency, supply, and railway data at revision `22036681622a558c`.

Network validation passed and proves the engine data needed for connected-region planning exists.

Global positions and locators did not validate because of unrelated map diagnostics and truncated bulk diagnostics.

Those global diagnostics do not authorize map edits and do not prove Event 021's current state planner is connected.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dc25b6d72897e739ab91571d154a619de2b7422c5c5657f965922a7e3dfda15/52316aac36aee55bd3e957550de4a62768449af60090e162e00e9d623c0b5058/map-inspect.22036681622a558c.json`.

Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a2aa6c1032fec7c705d767b5a310f77ee50a92e084e2e4994bfa3a926533af6/ce67dd944f9911b05c54b371c0a5336495f4c4cf5190c35f31cddb5e864b1cff/map-state.png`.

### Weighted logic

The probability route was started with `hoi4.probability_inspect` as required.

Direct read-only source inspections found the Event 021 parent random-list source, Event 021 core and parent custom pools, seven decision `ai_will_do` rows, two mission `ai_will_do` rows, the AI strategy file, and the Wars cluster source.

The parent random-list aggregate reported 11 candidates but no available candidates under the incomplete input context.

The Event 021 custom-pool adapters and Wars cluster custom-pool adapter extracted zero declared candidate rows and reported `poolComplete=false`.

The decision and mission routes identified source rows but no available scenario candidates.

The AI strategy adapter reported no weighted surface.

Therefore no normalized TGT, ARC, SEV, EVO, FRT, SPN, STR, SET, REC, GLB, CLU, or SCN conclusion is accepted from this pass.

The exact blocker is incomplete auditor-readable candidate-pool declaration and missing complete named scenario inputs.

The required `chaosx_ai_probability_auditor` route was invoked, but the auditor remained running after bounded waits and an explicit instruction to conclude from gathered evidence, then had to be shut down without a final report.

That missing final auditor report is a second exact blocker.

The direct MCP source inspections above are supplemental evidence and do not substitute for the required auditor-owned scenario audit.

`hoi4.probability_compare` is not applicable to this planning-only turn because there is no owner patch or before/after source pair.

The owner must supply complete manifests and rerun the dedicated auditor after implementation.

Representative parent random-list artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1a5f4099ebb7a2c5253d9d06a489dc572051aecaf45d7f8d561edbef5b271dc/7927d4f27d836db91314509b57fe28ab18406b59b8687e0b2590fd70ff5472c3/probability-inspect-6109e0652a34.json`.

Decision artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c46e6e71d30158e6c959e9a9c515375053a6f639d975393a7eb1da1b944e7bd/a36ba486c0c6e4baa724310f407a2bf2a5029688ef4b78f427e5568da94f4fca/probability-inspect-8fd2f71bfcae.json`.

Mission artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87bb74f43597973456630489b82790a581ae9cf08e9d26f66c23ecd836910cd0/67cd97715c994e5669d631bcfe970da962bec0675d135c5294cd119ecd1f7c5c/probability-inspect-8fd2f71bfcae.json`.

Cluster artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d50fc43a9344a1d8c7b632360adbf230885391166b3679079c8fe06884ada7d3/2286f984470e56575b8a564a39038752e8cf3eba8cfb2b5a04484d612dcd0a3f/probability-inspect-7ed8b9859e5e.json`.

### Shared event-details GUI

The shared `events_log_event_details_window` was inspected and rendered at revision `7e3be3661c50cf62` for an Event 021 baseline scenario, 1366x768 and 1920x1080, and normal, long-text, and missing-localisation states.

Inspection completed, but validation failed on shared framework diagnostics including active symbol collisions and overlapping enabled/disabled toggle click regions.

Rendering completed, but the response was truncated and retained only the full SVG artifact; its validation status remained false.

These are shared framework findings, not authority for Event 021 to patch the GUI.

The Event 021 conclusion is limited to defining complete payload and localisation contracts.

Layout fit, click behavior, and long-text acceptance remain unresolved until the shared GUI owner corrects or dispositiones the diagnostics and reruns the same scenario.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e13763b482c3b530a222b8bba97c5e748ed4e68a027a5a694a5a3ad704ebbc87/806a04bf7e19e8b92f378a923d779c50706d96f1101c7d1ac373dfe99979ae2f/gui-inspect.7e3be3661c50cf62.json`.

Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb4b47f09ca242fd1aa96903b4ea5cca9ac6c30a1a883247e4ee6d10f4a35bb1/576e803e7b1fc72e084715e663294625fe38253792050fed7a28ee741183e9af/events_log_event_details_window-full.svg`.

Event 021 introduces no dedicated scripted GUI, so no Event 021 GUI rewrite is proposed.

### Technology viewer limitation

The installed planner package has no Technology Tree Viewer route for this workflow.

No technology or doctrine surface is proposed by this addendum, and no technology conclusion is claimed.

If implementation later introduces technology or doctrine effects, that conclusion remains unresolved until the required viewer is available.

## Open parent decisions

1. Accept the proposed origin-neutral Event 006 package-content predicate so package-local decisions and formables can be reused without Event 006 lifecycle state. The recommendation is yes.
2. Confirm nearest-integer scenario rounding with a minimum of one for a nonempty eligible pool. The recommendation is yes because it matches the approximate percentage promise and remains deterministic.
3. Decide whether high-chaos Wars overlap is an intentional named evolution. The recommendation is baseline exclusion and no overlap until a concrete evolution case is accepted.
4. Implement topology-gated partition and merger plus evolution-as-log-classification, or remove those dead outcomes from the accepted spec. The recommendation is to retain partition only for genuine multi-front territorial settlements, retain merger only for a legal successor absorption, and keep evolution as classification rather than an effect.
5. Disposition the shared event-details GUI diagnostics through the shared GUI owner before closure. Event 021 should not own that patch.

## What should not be added

- No dedicated Event 021 scripted GUI.
- No second global scheduler or unrestricted country-iterating on action.
- No duplicate same-tag country.
- No generic fallback focus tree and no Event 006 focus layout rewrite.
- No Event 006 origin, network, league, congress, generation, or evolution state for Event 021 package actors.
- No fixed Event 006 package count or Scotland-specific Event 021 branch.
- No hardcoded factory-to-equipment conversion described as real stockpile transfer.
- No disconnected states added merely to reach a severity quota.
- No new report/news art family, super-event, portrait, flag batch, animation, 3D model, or sound package.
- No technology or doctrine expansion.
- No historical claim that ethnic, religious, or refugee presence is itself a sufficient cause of civil war.

## Promotion and closure handoff

Keep this file under `docs/plans/021_random_civil_war_plans/` while it is open.

If accepted, merge its contracts into spec parts 2, 3, 4, 5, 6, 7, 8, 9, and 10, the probability scenario matrix, package manifest, overlap reconciliation, revision notes, and master spec.

The promoted spec must record every accepted identifier, scenario, cap, route gate, state rule, outcome disposition, and audit requirement.

After promotion, mark this addendum promoted or superseded rather than leaving two active design sources.

The parent implementation problem is to make the existing Event 021 framework prove its actors, territory, resources, choices, queues, settlements, and records.

The proposed expansion is one evidence-backed fracture transaction and lifecycle tranche, not a new subsystem family.

The research basis is state weakness plus organized political claim, mobilized exclusion rather than geography alone, cross-border networks with civilian-protection restraint, external support as an actor relationship, multi-actor settlement difficulty, and recurrence under failed political guarantees.

Affected implementation surfaces are Event 021 core/parent effects and triggers, the normal decision category, Event 021 AI/events/localisation/log payload, the origin-neutral portion of Event 006's package contract, narrow Event 004/007 collision predicates, Wars row 1003 reservations, the existing global-host pulse, static icon wiring if required, documentation, and the workbook.

No prior improvement-loop addendum remains unresolved because this is the first one.

This addendum itself remains unresolved until the parent implements, promotes, explicitly queues, or rejects it.

Closure is not recommended yet.

After this tranche, the next improvement-loop decision should be a closure audit rather than another broad expansion unless implementation evidence reveals a distinct accepted gap.
