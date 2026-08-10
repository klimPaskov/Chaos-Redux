# Event 016 final decision and mission audit

> **Superseded provider-inventory notice (2026-08-09):** This audit predates
> provider 522, the expanded 18-ID Event 19 census, and the provider-side
> management-cost display/profile-cache callback. Its `504-510` statements are
> historical evidence only; use `016_core_runtime_handoff_map.md`,
> `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`, and
> `.tmp/event19_docs_curator_current.md` for current provider facts.

Date: 2026-08-03

Mode: read-only final audit.

## Disposition

The Event 016 decision and mission layer is broadly coherent in static source review, with no confirmed local cost, target-validity, duplicate-ID, missing-decision-localisation, or missing-AI declaration defect.

Event 016 remains partial and blocked at the package level.

The outstanding blocker is the accepted KRG biological stockpile and delivery design, which cannot be implemented safely until the native CBRN raid owner exposes stable idempotent reservation, outcome, cancellation, and expiry callbacks.

No gameplay, localisation, GUI, asset, focus, or provider source was edited in this pass.

## Issue list, ordered by severity

### Blocker: native CBRN stockpile and delivery lifecycle remains unavailable

The accepted Event 016 KRG stockpile contract needs an exact receipt across native payload reservation, outcome, cancellation, expiry, transfer, and defeat.

`common/decisions/016_brilliant_scientist_kruger_state_safeguard_decisions.txt` deliberately stops at `brilliant_scientist_krg_open_canonical_last_resort_raid_authority` and delegates payload, agent, state selection, delivery risk, and consequence processing to the native biological raid and intelligence systems.

`brilliant_scientist_krg_record_confirmed_offensive_biological_use` only records confirmed hostile use, rather than inferring it from research, custody, authorization, reservation, or an attacker accident.

The documented callback re-audit confirms that the native raid API exposes outcome-time resolvers only and no stable pre-reservation, cancellation, or expiry callback.

Do not add an Event 016 local stockpile, delayed debit, parallel payload, or outcome-only deduction as a substitute.

Evidence: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_krg_cbrn_callback_boundary_reaudit_2026-08-03.md`, `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:150`, and `common/decisions/016_brilliant_scientist_kruger_state_safeguard_decisions.txt:283`.

### Medium: quantitative AI, affordability, and persistence acceptance is still absent

All 298 non-mission decisions declare `ai_will_do`, and the finite settlement, high-speed-materials, portal, KRG, and foreign-operation layers contain non-zero contextual AI surfaces in source.

The required candidate-pool ranking, affordability, transfer, formation, cancellation, exploit, and scenario evidence has not been produced for the current final source state.

This is an acceptance-evidence gap, not a confirmed AI or cost-script defect.

The highest-value missing cases are the ten `chaosx.nr16.5.d_eng` through `.m_cze` settlement competitors, `brilliant_scientist_prepare_high_speed_materials_trial`, the paid KRG production and hazardous-objective actions, and the Event 019 provider payment and refund paths.

### Low: primary-facility-defense cancellation has no distinct failure record

`brilliant_scientist_krg_primary_facility_defense_mission` is a 120-day hold objective.

It cancels when the canonical primary facility ceases to exist, be controlled, or retain its facility role, but has no `cancel_effect`, failure receipt, retry cooldown, or player-facing failure consequence in its own declaration.

The paid start decision sinks the light material commitment and the mission grants no reward on cancellation, so no free reward loop was found.

This is a mission-presentation and consequence-risk rather than a confirmed engine defect, because external state loss may already carry consequences and a recovered facility may intentionally permit another attempt.

Parent decision: either accept the recovery-friendly retry behavior or add a bounded cancellation receipt, consequence, and retry rule after confirming desired facility-loss behavior.

Evidence: `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt:510` and `:543`.

### Info: Directorate GUI visual fidelity remains unresolved

The Directorate scripted GUI is read-only, human-only presentation.

Its buttons only refresh display records, toggle animation, collapse the panel, or select tabs, while every costed action, mission, duration, map requirement, and AI path remains in normal decisions.

`hoi4.gui_inspect` could not produce a source-linked artifact because the current workspace exceeded the configured scan limit with `SCAN_BYTE_LIMIT`.

Source-level contract review found no gameplay-bypassing GUI button, but rendered layout, clipping, click-region, and state fidelity are unresolved.

## Reviewed decision and category inventory

The audit read every Event 016 decision and category source under `common/decisions/`.

| Surface | Files reviewed | Declarations |
| --- | --- | ---: |
| Directorate, containment, foreign, recovery, evolution, aftermath, achievement | `016_brilliant_scientist_achievement_decisions.txt`, `016_brilliant_scientist_aftermath_decisions.txt`, `016_brilliant_scientist_containment_decisions.txt`, `016_brilliant_scientist_directorate_facilities.txt`, `016_brilliant_scientist_directorate_foreign.txt`, `016_brilliant_scientist_directorate_institutions.txt`, `016_brilliant_scientist_directorate_project_board.txt`, `016_brilliant_scientist_directorate_synthesis.txt`, `016_brilliant_scientist_evolution_missions.txt`, `016_brilliant_scientist_foreign_decisions.txt`, `016_brilliant_scientist_former_host_recovery_decisions.txt` | 198 |
| Kruger State | `016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt`, `016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`, `016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt`, `016_brilliant_scientist_kruger_state_foundation_decisions.txt`, `016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt`, `016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`, `016_brilliant_scientist_kruger_state_safeguard_decisions.txt`, `016_brilliant_scientist_kruger_state_terminal_decisions.txt` | 128 |
| Categories | `categories/016_brilliant_scientist_achievement_categories.txt`, `aftermath_categories.txt`, `directorate_categories.txt`, `foreign_categories.txt`, `kruger_state_categories.txt`, and `recovery_categories.txt` | 19 categories |

The 326 declared decisions and missions have unique IDs.

All 298 non-mission declarations have an `ai_will_do` block.

No Event 016 decision source contains an `entity =`, `.mesh`, or `.anim` reference.

## Decision category lifecycle notes

`brilliant_scientist_directorate_category` remains visible to the current host or sovereign KRG, including between actions so its display can explain Mandate, Dependence, Exposure, and Capacity.

The Directorate category includes the read-only `brilliant_scientist_directorate_scripted_gui`, while its actual project board, facility, institutional, foreign-framework, containment, synthesis, and sovereignty actions retain ordinary decision lifecycle controls.

`brilliant_scientist_foreign_operations_category` requires a valid initialized Evolution II observer and uses the controlled host-target array.

`brilliant_scientist_former_host_recovery_category` is limited to the viable former host, and the four aftermath categories require the active postwar custodian.

`brilliant_scientist_origin_investigation_category` requires the rare origin-investigation actor gate.

The ten KRG categories are focus-receipt gated, use `visible_when_empty = yes`, and divide foundation, security, clone or machine, paleogenetic, xenobiological, portal or temporal, exotic or biological, foreign policy, integration, and terminal work.

Focus-side flags and `brilliant_scientist_kruger_focus_is_active` prevent route-closed actions from appearing as active choices.

Host transfer, sovereignty formation, world-end, containment, invalid target, and terminal cleanup trace into the shared project, foreign-context, temporal-target, and state receipts rather than leaving stale visible actions.

## Mission quality notes

| Mission family | Owner/category and region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| Loyalty review | Current host, Directorate institutions, country scope | Paid security review, 45 days | Timeout snapshots intelligence and project context before resolving the established loyalty request; transfer cancellation clears the in-progress lock | Re-enabled only after the 180-day review interval |
| Fifteen project incidents | Current host, Directorate project board, family scope | An active family incident, with 120-day technical, 150-day industrial, 180-day biological, or 240-day exotic deadline | Matching paid response decision resolves the incident; timeout calls the family failure helper and cancellation removes the incident modifier and locks | One active incident family and global incident gate prevent parallel duplicate rewards |
| Sovereignty deadline | Current host, Directorate, country scope | Dynamic 30 to 120 days based on Mandate, dangerous portfolio, war, good faith, and incident pressure | External resolution cancels cleanly; timeout marks the deadline expired for the sovereignty resolver | One active deadline and resolved guard |
| Clone drift, rogue node, maintenance, transit breach | KRG Clone and Machine, Foundation, or Portal and Temporal categories; named controlled site or facility | Paid in-mission objective, 90-day containment or 180-day maintenance window | Full outcome requires the transient objective receipt plus surviving site proof; failed history receives a 90-day retry cooldown | Exact full-completion receipts close the reward producer |
| Clone identity pressure | KRG Clone and Machine, country scope | Three institutional proofs within 90 days, or paid reconciliation after pressure begins | Unresolved pressure records the permanent revolt history and fires the confrontation; reconciliation resolves the immediate state without erasing history | Permanent historical disqualifier prevents achievement laundering |
| Ministry consolidation and replacement | KRG Foundation or Clone and Machine, country scope | Route-gated 180-day passive administrative pressure | Timed resolution or declared timeout path advances the existing institution state; no recurring material reward | Deliberately passive in the current design |
| Primary facility defense | KRG Foundation, canonical primary facility | Paid start, controlled intact facility for 120 days | Timeout grants the defense completion and army experience; facility loss cancels without reward or direct failure receipt | Completion flag closes the producer; cancellation behavior is the low-severity issue above |
| Temporal rescue and stabilization | KRG Portal and Temporal, exact bound capital or singularity state | 60-day survival followed by 180-day stabilization supervision | Every terminal path clears the bound state and global target; lost proof or civil war calls the failure helper | One bound target ID and use receipt prevent reuse |
| Singularity disarmament hold | KRG terminal program, terminal facilities | Route- and facility-gated 180-day hold | Success and timeout are separated through the terminal helper contracts | Terminal commitment and receipt guards prevent a second terminal result |

The 28 mission declarations are mission declarations rather than hidden periodic loops.

## Cost and requirement clarity

The project portfolio and KRG production systems centralize political-power, equipment, fuel, manpower, command-power, civilian-factory, consumer-goods, duration, capacity, output, temporal-debt, and AI tuning in Event 016 constants and matching gate or payment helpers.

Project advances, incident responses, high-speed materials, portal calibration, facilities, foreign actions, and KRG construction or production use concrete burden combinations rather than political power alone.

Examples include paid support equipment, motorized equipment, fuel, manpower, 1, 2, 4, or 6 factory loads in KRG decisions, and the project board's escalating 1 to 12 civilian-factory bands.

The three explicit zero-PP actions are bounded utility actions, not reward production: `brilliant_scientist_krg_review_interrupted_project_audit`, `brilliant_scientist_krg_clean_invalid_foreign_target`, and `brilliant_scientist_krg_begin_temporal_stabilization_supervision`.

The first two only record or clear state, and the third begins a 180-day strategic-factory supervision mission.

Completed vanilla special-project integration decisions do not add a second material debit because they only convert an already completed native special project after capacity and incident locks; the follow-up stage and receipt helpers prevent repeat payout.

All 216 decision-facing custom trigger or effect tooltip keys resolve in the Event 016 English localisation set.

## AI validity and route-lock notes

The 46 state- or country-targeted decisions use root and target gates.

All 43 timed targeted decisions revalidate the exact target through `cancel_trigger` while active.

The only three targeted actions without cancellation are immediate, one-time foreign invitation, protection, and public-challenge choices, which validate their target immediately and have no timer to become stale.

No Event 016 decision opts into `target_non_existing = yes`.

Foreign actors require the initialized contest observer state, target lifecycle validity, and relevant availability gate.

KRG foreign decisions target valid foreign capitals or saved former-host scopes, and their stale-target cleanup helper is isolated from ordinary operation resolution.

The KRG terminal, sovereignty, biological-authority, temporal, focus, and project-stage actions all include route, evolution, facility, control, or project-ledger guards rather than relying on visible text alone.

## Localisation and tooltip gaps

All 326 decision and mission IDs have both title and description keys in the Event 016 English localisation files.

The audit found no missing direct custom requirement or effect-tooltip key among the 216 decision-facing references.

The existing cost and requirement tooltips correctly carry the nonstandard material, capacity, target, and route checks instead of exposing raw long trigger blocks.

The remaining GUI limitation is visual, not missing-localisation evidence.

## Cleanup and exploit-risk notes

Static tracing found dedicated cleanup for active project variables and arrays, incident report pending state, foreign context targets, sovereignty deadline variables, temporal anchor and rescue targets, project capacity markers, and terminal world-state transitions.

The temporal rescue helpers clear `brilliant_scientist_krg_temporal_rescue_target` on all success, failure, cancellation, and cleanup paths reviewed.

The project, production, and hazardous-mission layers use transient action flags, one-time completion receipts, retry cooldowns, target revalidation, and no-refund cancellation to prevent free unit, equipment, project-stage, stability, and temporal-capacity loops.

The Laboratory Guard cap remains 12, and no decision reviewed spawns an unbounded free division.

The KRG biological authority does not fabricate a stockpile or take ownership of native CBRN payload accounting.

## No-model provider surface

`common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` statically registers Event 019 provider IDs 504 through 510 for clone, robot, paleogenetic, xenobiological, alien-interface, portal, and temporal project-force families.

Each provider has the eleven required registry callback names, including eligibility, template, spawn, sustainment, management payment and refund, derivative setup, public-addition removal, and cleanup.

The provider source and all Event 016 decision sources contain no entity, mesh, or animation declaration.

The current no-model boundary is respected.

Live derivative management, refund, defeat, final cleanup, and cross-save parent-isolation scenarios remain user-owned validation work.

## Meaningful validation and evidence

- Read the current authority and status sources: `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`, `016_core_runtime_handoff_map.md`, `016_nonmodel_content_closure_handoff_2026-08-03.md`, the current completion audit, the CBRN callback re-audit, the provider-isolation audit, and the Event 016 system documents.
- Read the required offline Decision, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event, Idea, AI, Interface, Scripted GUI, and Focus wiki references, plus vanilla effect, trigger, script-concept, script-constants, decision, and focus precedents.
- Confirmed 326 unique decision or mission IDs, 298 of 298 non-mission `ai_will_do` declarations, 46 targeted actions with 43 of 43 timed target cancellations, 0 missing decision titles or descriptions, 0 missing custom tooltip localisation keys, and 0 Event 016 decision model references.
- Ran focused read-only Event Inspector lint for `chaosx.nr16.195` at workspace revision `abcb2d5afb2d6b9a5046c8ce0db309048da2984751d0487ea8e87f974d27a814`.
- The Event Inspector returned `EVENT_INSPECTED_PARTIAL`, zero blockers, and zero blocking diagnostics, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/729ec1861673dd7c1d373dfe09aced866bbaf768d2a3bfc44982ee3a66d5ee65/227dbb239ee75c029cfeb1200471aa9045c98762ee96bcfb67020fadb66d19b0/event-lint-abcb2d5afb2d.json`.
- The Inspector deliberately deferred workspace-wide helper and lifecycle projection, so it is focused source evidence rather than whole-package proof.

## Skipped meaningful validation and why

- No in-game validation was run because live game validation belongs to the user.
- No numerical weighted-logic sweep was run because the current accepted scenario manifest and full competitor pool are not yet supplied as completed acceptance evidence.
- No GUI render artifact is claimed because `hoi4.gui_inspect` stopped at `SCAN_BYTE_LIMIT` before producing an artifact.
- No Event 019 live provider lifecycle validation was run because it extends beyond this read-only Event 016 audit and remains user-owned.

## Simplifications, remaining issues, and parent follow-up

No gameplay fallback, placeholder CBRN action, free payload, model surrogate, or broad decision-system rewrite was introduced.

The no-model boundary is an explicit scope constraint, not a simplification in this audit.

Parent follow-up should keep the native CBRN callback dependency blocked until the shared owner supplies its contract, choose whether the primary-facility-defense cancellation needs a distinct failure state, and run the documented AI, cost, persistence, provider, transfer, formation, terminal-cleanup, and live-presentation scenarios before any whole-event completion claim.

## Changed files

- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_decision_mission_audit_2026-08-03.md`

No decision, mission, scripted GUI, localisation, focus, event, asset, or provider ID changed.
