# Event 016 Directorate implementation handoff

## Ownership and result

This handoff covers the bounded host-Directorate tranche: one category header, host institutions, facilities, staffing, priorities, security, technical authority, foreign liaison, and generic project-board controls. It does not own the Event 016 opening flow, shared architecture, fifteen native project families, project rewards/incidents, technologies, equipment, units, Kruger country/focus content, evolutions, super-events, achievements, workbook, raster assets, or existing `interface/016_brilliant_scientist.gfx` registrations.

### Files added

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `common/dynamic_modifiers/016_brilliant_scientist_directorate_modifiers.txt`
- `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`
- `common/decisions/016_brilliant_scientist_directorate_institutions.txt`
- `common/decisions/016_brilliant_scientist_directorate_facilities.txt`
- `common/decisions/016_brilliant_scientist_directorate_foreign.txt`
- `common/decisions/016_brilliant_scientist_directorate_project_board.txt`
- `localisation/english/016_brilliant_scientist_directorate_l_english.yml`
- `docs/systems/016_brilliant_scientist_directorate.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_directorate_implementation_handoff.md`

No existing shared Event 016 gameplay, interface, asset, or project-family file was edited by this tranche.

## Primary identifiers

Category:

- `brilliant_scientist_directorate_category`

Institutional decisions:

- `brilliant_scientist_convene_public_science_council`
- `brilliant_scientist_establish_compartmentalized_military_office`
- `brilliant_scientist_grant_private_industrial_concession`
- `brilliant_scientist_assemble_exile_scholar_network`
- `brilliant_scientist_recruit_research_cohort`
- `brilliant_scientist_charter_university_research_network`
- `brilliant_scientist_prioritize_fundamental_inquiry`
- `brilliant_scientist_prioritize_prototype_delivery`
- `brilliant_scientist_prioritize_distributed_replication`
- `brilliant_scientist_establish_internal_security_section`
- `brilliant_scientist_rotate_security_clearances`
- `brilliant_scientist_conduct_loyalty_review`
- `brilliant_scientist_lay_false_procurement_trails`
- `brilliant_scientist_establish_cabinet_safety_board`
- `brilliant_scientist_delegate_technical_authority`
- `brilliant_scientist_grant_final_technical_authority`

Security mission:

- `brilliant_scientist_loyalty_review_mission`

Facility decisions:

- `brilliant_scientist_formalize_primary_research_campus`
- `brilliant_scientist_expand_primary_prototype_works`
- `brilliant_scientist_establish_secondary_laboratory`
- `brilliant_scientist_relocate_primary_laboratory`
- `brilliant_scientist_harden_primary_laboratory`
- `brilliant_scientist_mobilize_primary_laboratory_repairs`

Foreign decisions:

- `brilliant_scientist_review_foreign_approaches`
- `brilliant_scientist_offer_controlled_research_access`
- `brilliant_scientist_open_joint_laboratory`
- `brilliant_scientist_accept_foreign_protection_framework`
- `brilliant_scientist_restrict_foreign_research_access`
- `brilliant_scientist_terminate_foreign_research_frameworks`

Generic project-board decisions:

- `brilliant_scientist_approve_selected_project`
- `brilliant_scientist_suspend_selected_project`
- `brilliant_scientist_resume_selected_project`
- `brilliant_scientist_cancel_selected_project`
- `brilliant_scientist_commission_independent_replication`
- `brilliant_scientist_publish_verified_methods`

Persistent dynamic modifiers:

- `brilliant_scientist_public_science_council`
- `brilliant_scientist_compartmentalized_military_office`
- `brilliant_scientist_private_industrial_concession`
- `brilliant_scientist_exile_scholar_network`
- `brilliant_scientist_facility_network`
- `brilliant_scientist_research_cohort`
- `brilliant_scientist_university_research_network`
- `brilliant_scientist_priority_fundamental_inquiry`
- `brilliant_scientist_priority_prototype_delivery`
- `brilliant_scientist_priority_distributed_replication`
- `brilliant_scientist_internal_security_section`
- `brilliant_scientist_cabinet_safety_board`
- `brilliant_scientist_delegated_technical_authority`
- `brilliant_scientist_sovereign_technical_authority`

## Exact loyalty-review outcome contract

`brilliant_scientist_conduct_loyalty_review` starts `brilliant_scientist_loyalty_review_mission`. The mission is explicitly activated, lasts 45 days, cannot auto-complete from an always-true `available` block, cancels if the country stops being the current host, and permits only one pending findings context. The pending-request guard belongs on the initiating review decision; clearance rotation is not blocked by it.

At timeout the host receives flag `brilliant_scientist_directorate_loyalty_review_requested` and these normal-variable snapshots:

- `brilliant_scientist_directorate_loyalty_review_mandate_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_dependence_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_exposure_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_independent_capacity_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_grievance_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_prototype_count_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_deployment_count_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_weaponization_count_snapshot`;
- `brilliant_scientist_directorate_loyalty_review_intelligence_score` (0-4 from agency, mature agency, any operative, and a multi-operative team).

Boolean evidence is persisted with these country flags:

- `brilliant_scientist_directorate_loyalty_review_agency_present`;
- `brilliant_scientist_directorate_loyalty_review_mature_agency`;
- `brilliant_scientist_directorate_loyalty_review_operatives_present`;
- `brilliant_scientist_directorate_loyalty_review_operative_team`;
- `brilliant_scientist_directorate_loyalty_review_cloning_history`;
- `brilliant_scientist_directorate_loyalty_review_robotics_history`;
- `brilliant_scientist_directorate_loyalty_review_paleogenetics_history`;
- `brilliant_scientist_directorate_loyalty_review_xenobiological_history`;
- `brilliant_scientist_directorate_loyalty_review_singularity_history`.

The parent must implement country-scope `brilliant_scientist_resolve_directorate_loyalty_review_request` and insert this exact call at the end of the mission timeout after the request context is complete:

```txt
brilliant_scientist_resolve_directorate_loyalty_review_request = yes
```

The resolver must require the request flag and choose a weighted finding from the captured context: foreign agent, Kruger loyalist, project-gated transformed personnel, inconclusive review, or wrongful purge. It must not award a guaranteed captive operative or deterministic Exposure reduction. After exactly one result, clear the request flag, all nine boolean context flags, and all nine snapshot variables.

## Exact primary-relocation outcome contract

The relocation decision accepts only an owned, fully controlled prepared core state distinct from the current primary site. It requires at least two infrastructure levels plus an industrial complex or military factory. A land route requires `is_in_home_area = yes`; otherwise a naval base and a paid 20-convoy commitment are required. Trucks, fuel, time, and political power are always committed. The destination is revalidated while the timer runs.

At timeout the host receives:

- request flag `brilliant_scientist_directorate_relocation_requested`;
- route flag `brilliant_scientist_directorate_relocation_land_route` or `_sea_route`;
- risk flag `brilliant_scientist_directorate_relocation_requested_under_fire` when applicable;
- state targets `event_target:brilliant_scientist_relocation_requested_origin` and `event_target:brilliant_scientist_relocation_requested_destination`;
- snapshots `brilliant_scientist_directorate_relocation_mandate_snapshot`, `_exposure_snapshot`, `_dependence_snapshot`, `_capacity_snapshot`, `_independent_capacity_snapshot`, `_grievance_snapshot`, `_prototype_count_snapshot`, `_deployment_count_snapshot`, and `_weaponization_count_snapshot`.

The producer also starts `brilliant_scientist_primary_relocation_recent` for the 365-day anti-reroll cooldown. It does not clear, replace, or grant any facility/building itself.

The parent must implement country-scope `brilliant_scientist_resolve_directorate_relocation_request` and insert this exact call after the request context and both targets are saved:

```txt
brilliant_scientist_resolve_directorate_relocation_request = yes
```

The resolver must revalidate origin and destination, then weight success, interception, prototype loss, staff refusal, and escape. On success it clears the origin's `brilliant_scientist_primary_facility` state flag and `brilliant_scientist_facility_type` variable, moves the primary-facility global target, and sets the destination state flag plus `brilliant_scientist_facility_type = constant:brilliant_scientist_facility.primary_type`. It must not add or copy infrastructure, factories, shared slots, facilities, prototypes, project stages, or equipment. Every outcome clears the request, route, and under-fire flags, both request targets, and all nine snapshot variables. Invalid context resolves as interruption/failure, never silent success.

## Exact project-builder caller contract

The native project builder owns selection presentation and all family-specific eligibility, progress, outcomes, incidents, rewards, technology, equipment, and units. It must never call the approval decision as a stage-advance effect.

### Inputs the native project builder must publish

Set these normal variables on the current host whenever the board selection changes:

- `brilliant_scientist_directorate_selected_project_family`
- `brilliant_scientist_directorate_selected_project_stage`

Set `brilliant_scientist_directorate_project_selection_ready` only when both values identify a valid family and stage. The Directorate checks them against `constant:brilliant_scientist_project_family.none`, `.max_exclusive`, `constant:brilliant_scientist_project_stage.none`, and `.max_exclusive`.

Rebuild these selection-derived country flags whenever selection or native state changes:

- `brilliant_scientist_directorate_selected_project_active`
- `brilliant_scientist_directorate_selected_project_suspended`
- `brilliant_scientist_directorate_selected_project_damaged`
- `brilliant_scientist_directorate_selected_project_replicable`
- `brilliant_scientist_directorate_selected_project_replicated`
- `brilliant_scientist_directorate_selected_project_publishable`
- `brilliant_scientist_directorate_selected_project_published`

Flags that do not match the selected family/stage must be cleared. Do not leave a status flag from the previous selection.

### Approval request produced by the Directorate

After the timed approval decision finishes, it writes:

- flag `brilliant_scientist_directorate_project_approval_requested`;
- variable `brilliant_scientist_directorate_approved_project_family`;
- variable `brilliant_scientist_directorate_approved_project_stage`.

The native project builder must validate the request against its family rules, begin only the requested family/stage if valid, update the shared project ledger through the accepted family helper, and then clear the request flag and both approved variables. The Directorate deliberately does not call `brilliant_scientist_advance_project` during approval.

### Suspend request produced by the Directorate

The decision first calls the common `brilliant_scientist_suspend_project` ledger helper, using `brilliant_scientist_project_family` as the required temporary input. It then writes:

- flag `brilliant_scientist_directorate_native_project_suspend_requested`;
- variable `brilliant_scientist_directorate_project_command_family`;
- variable `brilliant_scientist_directorate_project_command_stage`.

The native project builder must apply its family-specific suspension state and burdens, rebuild selected-status flags, and clear the request flag plus both command variables.

### Resume request produced by the Directorate

The decision first calls `brilliant_scientist_resume_project` with the selected family as the temporary input. It then writes:

- flag `brilliant_scientist_directorate_native_project_resume_requested`;
- variable `brilliant_scientist_directorate_project_command_family`;
- variable `brilliant_scientist_directorate_project_command_stage`.

The native project builder must restore the matching family-specific work, rebuild selected-status flags, and clear the request flag plus both command variables.

### Cancellation request produced by the Directorate

The decision records the selected family/stage, calls `brilliant_scientist_dismantle_project` with the selected family as the temporary input, and writes:

- flag `brilliant_scientist_directorate_project_cancellation_requested`;
- variable `brilliant_scientist_directorate_project_command_family`;
- variable `brilliant_scientist_directorate_project_command_stage`.

The native project builder must remove the matching native project state, units/burdens/hooks that its own cancellation contract requires, rebuild or clear the board selection, and clear the request flag plus both command variables.

### Independent replication completion produced by the Directorate

The decision locks the selected family/stage at start, requires the selection to remain unchanged and replicable, then calls `brilliant_scientist_replicate_project_to_requested_stage` with:

- temporary `brilliant_scientist_project_family` from the locked family;
- temporary `brilliant_scientist_requested_project_stage` from the locked stage.

On completion it writes:

- flag `brilliant_scientist_directorate_replication_completed`;
- variables `brilliant_scientist_directorate_replication_completed_family` and `_stage`;
- selection flag `brilliant_scientist_directorate_selected_project_replicated`.

The native project builder may consume the completion flag for family-specific aftermath or achievement hooks. If consumed, clear the completion flag and both completed-family/stage variables after all consumers have run. The common ledger is already authoritative for replication state.

### Publication completion produced by the Directorate

The decision locks the selected family/stage, requires the selection to remain unchanged, replicated, publishable, and unpublished, then calls `brilliant_scientist_publish_project` with the locked family as `brilliant_scientist_project_family`.

On completion it writes:

- flag `brilliant_scientist_directorate_publication_completed`;
- variables `brilliant_scientist_directorate_publication_completed_family` and `_stage`;
- selection flag `brilliant_scientist_directorate_selected_project_published`;
- proof flags `brilliant_scientist_public_reputation_established`, `brilliant_scientist_research_advantage_exposed`, and `brilliant_scientist_sovereign_science_authority`.

The native project builder may consume the completion flag for family-specific publication aftermath. Clear it and its two completed-family/stage variables only after all consumers have run. The common ledger is already authoritative for publication state.

### Concurrency rule

`brilliant_scientist_project_board_action_in_progress` blocks overlapping generic board actions. Approval, replication, and publication also store `brilliant_scientist_directorate_locked_project_family` and `_stage` during their timers. Shared host-loss cleanup must clear the action flag and locked variables even if the decision engine cancels the visible timer.

## Parent integration and cleanup requirements

The parent/shared Event 016 lifecycle owns initialization, transfer, host removal, Kruger death, country formation, takeover, and terminal cleanup. It must integrate the following Directorate state.

### Foreign global targets

Controlled access creates:

- country target `brilliant_scientist_controlled_research_access_partner` and the same-named country flag on that actor.

The joint laboratory creates:

- country target `brilliant_scientist_joint_laboratory_partner` and the same-named country flag on that actor;
- state target `brilliant_scientist_joint_laboratory_site` and the same-named state flag.

Foreign protection creates:

- country target `brilliant_scientist_foreign_protection_partner` and the same-named country flag on that actor.

The ordinary termination decision clears these. Shared invalidation and terminal cleanup must also:

1. check `has_event_target` before scoping to each target;
2. clear the actor/state flag in the target scope;
3. call `clear_global_event_target` for all four targets;
4. clear host flags `brilliant_scientist_controlled_research_access_opened`, `brilliant_scientist_joint_laboratory_framework_active`, and `brilliant_scientist_foreign_protection_framework_active`.

Partner defeat, annexation, loss of the joint site, or a no-longer-valid host should route to the same cleanup contract rather than leave a stale global target.

### Transient host state

Host-loss cleanup must clear all in-progress flags:

- `brilliant_scientist_institutional_form_in_progress`
- `brilliant_scientist_facility_action_in_progress`
- `brilliant_scientist_staffing_action_in_progress`
- `brilliant_scientist_priority_action_in_progress`
- `brilliant_scientist_security_action_in_progress`
- `brilliant_scientist_authority_action_in_progress`
- `brilliant_scientist_foreign_action_in_progress`
- `brilliant_scientist_foreign_approach_under_review`
- `brilliant_scientist_project_board_action_in_progress`

It must also call `remove_mission = brilliant_scientist_loyalty_review_mission`, clear both pending Directorate request flags, both relocation route flags, the relocation under-fire flag, all loyalty evidence flags, and the two relocation request targets. Pending loyalty and relocation snapshot variables listed above must be cleared on terminal cleanup. A host transfer must either resolve each request before transfer or explicitly cancel it and clear its context; it must never let the new host inherit an unexplained pending outcome.

It must also clear pending project request flags, selection-derived flags, and the following normal variables:

- selected family/stage;
- locked family/stage;
- approved family/stage;
- project command family/stage;
- replication completed family/stage;
- publication completed family/stage.

Timed flags `brilliant_scientist_primary_relocation_recent` and `brilliant_scientist_priority_recently_changed` naturally expire, but terminal cleanup may clear them when destroying the Directorate state outright.

Initialization should clear all pending request/completion flags and variables before publishing the first board selection. It must not overwrite shared visible/hidden meter initialization owned by the Event 016 architecture.

### Persistent route state

The dynamic modifiers remove themselves when their country ceases to satisfy `brilliant_scientist_is_current_host`. The parent cleanup still owns route flags and permanent Directorate-state flags if the programme is being destroyed rather than transferred. If the programme transfers, the parent must decide which institutional facts migrate and which remain as aftermath; this tranche does not silently copy host flags to another country.

## Proof-flag causal paths

- `brilliant_scientist_facility_network_invested`: set by the first completed permanent facility-network investment.
- `brilliant_scientist_public_reputation_established`: set by publishing an independently replicated eligible method.
- `brilliant_scientist_research_advantage_exposed`: set by controlled foreign research access, a joint laboratory, or publication.
- `brilliant_scientist_sovereign_science_authority`: set by final technical authority or publication of a verified method.

The Directorate does not set `brilliant_scientist_impossible_prototype_completed` or `brilliant_scientist_impossible_autonomy_proven`; those belong to family-native project outcomes.

## Repeat-action exploit locks

- `brilliant_scientist_primary_laboratory_hardened` hides the hardening decision after its single successful anti-air/fort grant.
- `brilliant_scientist_controlled_research_access_ever_opened`, `brilliant_scientist_joint_laboratory_ever_established`, and `brilliant_scientist_foreign_protection_framework_ever_accepted` survive ordinary termination. A host cannot reopen those frameworks to repeat institutional or infrastructure gains.
- `brilliant_scientist_priority_fundamental_inquiry_ever_selected`, `_prototype_delivery_ever_selected`, and `_distributed_replication_ever_selected` make each priority's institutional meter shift one-time. Later returns still replace the active priority modifier and apply the common cooldown, but do not repeat the initial meter changes.
- Clearance rotation and false procurement remain repeatable because their beneficial Exposure changes carry bounded Grievance, capacity, logistics, time, and political costs; they grant no construction or project stage.

## Validation evidence

- Task-specific checks verify the loyalty request guard is attached only to the review initiator, the manual mission cannot auto-activate or instantly complete, and the request context is written only at mission timeout.
- Relocation checks verify both route modes, persistent origin/destination targets, the cooldown, and the absence of any building, slot, facility, prototype, project-stage, or equipment grant in the request producer.
- Facility-effect checks verify that the primary and secondary campus tooltips say Infrastructure, matching their `add_building_construction` effects, while the prototype-works tooltip alone reports its military factory.
- Repeat-action checks verify that hardening, controlled access, joint-laboratory construction, foreign protection, and first-adoption priority meter shifts cannot be looped for additional permanent gains.
- The prototype works reads the persistent shared `brilliant_scientist_project_deployment_count`, which is rebuilt from `brilliant_scientist_project_stage_entries`; it cannot be unlocked by a transient selection flag.
- The foreign scan exists only inside the explicit `Review Foreign Approaches` completion effect. No recurring daily, weekly, or monthly on-action was added.
- Long-running project-board actions lock family/stage and cancel if the selection changes, preventing commands from landing on a different project.

## Remaining parent-owned checks and risks

- The native family builder must implement and exercise the exact request/status contract above; no family-native implementation is part of this commit.
- Shared lifecycle cleanup must adopt the global-target and transient-state requirements before Event 016 can be called terminal-safe.
- The parent event/effect layer must implement and directly call the two named loyalty and relocation resolvers. Until then the producers deliberately leave one pending request instead of inventing a deterministic local fallback.
- The category-header decision UI is implemented. The richer optional scripted-GUI window remains a separate bounded interface tranche and must use the ordinary decisions/effects as its gameplay authority.
- Balance should be revisited after native project burdens, accident frequencies, and family AI weights are stable. This tranche's costs and AI weights were reviewed against their own effects, but cannot establish portfolio-wide balance in isolation.
- Live engine presentation and interaction remain part of the parent Event 016 integration audit; this handoff does not claim whole-event completion.

## Simplifications, omissions, and blockers

No fallback or functional simplification was used inside this bounded Directorate tranche. Existing vanilla icons are the documented intended sprites, not substitutes for missing required assets. The two context producers are complete, but their narrative outcome resolvers are parent-owned and not present in the shared Event 016 effects/events at this handoff. The exact effect names, call sites, inputs, outcomes, and cleanup duties are specified above; whole-event completion remains blocked until the parent implements them. Family-native content, the optional richer scripted GUI, and shared lifecycle edits remain explicit ownership boundaries. There were no unresolved file overlaps in the owned paths at handoff time.
