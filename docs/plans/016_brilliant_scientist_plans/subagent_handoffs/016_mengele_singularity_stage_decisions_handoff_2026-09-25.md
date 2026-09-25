# Event 016 Strategic Singularity Stage Decision Handoff

## Scope and acceptance basis

This handoff covers only the provider-owned Theory, DLC-offline Prototype, Deployment, and Weaponization decision rows under `mengele_clone_army_category`.

The accepted source is `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md`, especially its provider decision route and stage lifecycle rules, together with `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, which permits early preparation and preserves all six Singularity components.

The user-authorized slice requires the paid Prototype row only when Gotterdammerung is absent, while the native six-component route remains authoritative when it is present.

## Changed files

- Added `common/decisions/016_mengele_singularity_stage_decisions.txt` with the four timed decision rows, existing stage icons, duration constants, factory reservations, PP hints, and existing AI factors.
- Added `common/scripted_triggers/016_mengele_singularity_stage_decision_triggers.txt` with private receipt visibility, stage requirements, cost checks, and cancellation checks for the four rows.
- Updated only the Singularity Prototype clause in `common/scripted_triggers/016_mengele_project_stage_triggers.txt` so the paid offline Prototype can complete after Theory without six native component receipts, while DLC-present Prototype still requires all six authenticated receipts.
- Added `localisation/english/016_mengele_singularity_stage_l_english.yml` with UTF-8 BOM, decision text, requirements, effects, icon-first cost rows, blocked costs, and cost tooltips.
- Added this handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_mengele_singularity_stage_decisions_handoff_2026-09-25.md`.

No native special-project gate or callback, incident wiring, Fallout logic, model file, random weight, or GUI file was changed.

## Decision and trigger identifiers

| Stage | Decision ID | Decision trigger prefix | Private stage selector |
| --- | --- | --- | --- |
| Theory | `mengele_event016_singularity_theory` | `brilliant_scientist_mengele_singularity_theory_decision_` | `brilliant_scientist_project_family.singularity` + `brilliant_scientist_project_stage.theory` |
| Prototype | `mengele_event016_singularity_prototype` | `brilliant_scientist_mengele_singularity_prototype_decision_` | `brilliant_scientist_project_family.singularity` + `brilliant_scientist_project_stage.prototype` |
| Deployment | `mengele_event016_singularity_deployment` | `brilliant_scientist_mengele_singularity_deployment_decision_` | `brilliant_scientist_project_family.singularity` + `brilliant_scientist_project_stage.deployment` |
| Weaponization | `mengele_event016_singularity_weaponization` | `brilliant_scientist_mengele_singularity_weaponization_decision_` | `brilliant_scientist_project_family.singularity` + `brilliant_scientist_project_stage.weaponization` |

Singularity is family ID 15 and uses private provider receipt-array row 14; no Kruger identity or stage array is read or written by these wrappers.

## Before and after behavior

Before this patch, the provider had no four-stage Singularity decision wrapper, and the shared Prototype predecessor unconditionally required all six native component receipts.

After this patch, Theory is the first paid timed stage, followed by a paid Prototype only without Gotterdammerung, then Deployment and Weaponization through the existing private begin, cancel, and finish helpers.

With Gotterdammerung present, the paid Prototype row stays hidden and the shared predecessor still requires all six authenticated component receipts; the existing native component projects and callbacks remain the only Prototype route.

Theory and offline Prototype remain available as early preparation stages; Deployment and Weaponization require at least the existing constant-count of currently owned-and-controlled qualifying facilities, and loss of that live facility gate cancels the active stage through the existing refund and reservation lifecycle.

Deployment and Weaponization also require the live Mengele provider, its registry receipt, an empty family receipt, and the exact completed predecessor stage.

## Lifecycle, cognitive load, and mission audit

The four rows use one private family receipt, so only the next incomplete stage can be started and a second Singularity stage cannot start while the first is active.

Each active row remains visible through its matching receipt so the player can see cancellation; provider invalidation cancels and refunds the current row, and live facility loss also cancels Deployment or Weaponization.

The category adds at most one ready primary Singularity action at a time, adds no mission, and introduces no secondary tab, counter, or extra public mechanic.

Duration and direct costs are explicit and dynamic through the existing shared constants; the required facility threshold displays its existing `minimum_facilities` constant, and the tooltip states the control requirement and its consequence.

No visible value is an unexplained counter or raw value dump, and there are no active missions to assess for owner, region, duration, success, failure, or duplicate risk.

## Costs and requirement clarity

Every stage uses no more than three consumed types: political power, support equipment, and fuel; civilian factories are a temporary native reservation, keeping each stage at four or fewer distinct commitments.

Theory uses 100 PP, 180 support equipment, and reserves 2 civilian factories for 720 days.

The offline Prototype uses 150 PP, 450 support equipment, 1,000 fuel, and reserves 4 civilian factories for 900 days.

Deployment uses 200 PP, 1,350 support equipment, 5,000 fuel, and reserves 8 civilian factories for 1,080 days.

Weaponization uses 300 PP, 2,700 support equipment, 15,000 fuel, and reserves 12 civilian factories for 900 days.

All displayed direct payments use `£pol_power`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon`; temporary factory reservations use `£civ_factory` in the cost hover and stage requirement context.

The custom-cost affordability trigger and the availability tooltip use the same stage-specific predicate, including the civilian-factory reservation check.

Non-consumed material reserves, military factories, manpower, trucks, trains, and XP are not added to this provider wrapper cost design.

## AI, route locks, localisation, cleanup, and exploit risk

Each row reuses `brilliant_scientist_project_board.ai_high` and the existing `brilliant_scientist_project_ai.preferred_factor` war modifier used by the conventional provider wrappers; no random pool or native project weight changes.

The Prototype wrapper checks `NOT = { has_dlc = "Gotterdammerung" }` in both visibility and availability, while the native component callback retains its six-receipt authentication.

The new localisation file supplies all four names, descriptions, effect and requirement tooltips, cost rows, blocked cost rows, and cost hover text with a UTF-8 BOM.

Cancellation and completion set the exact literal family/stage selectors and call `brilliant_scientist_mengele_cancel_project_stage` or `brilliant_scientist_mengele_finish_project_stage`; starting calls `brilliant_scientist_mengele_begin_project_stage`.

The private helper snapshots and settles the direct payments, clears the active receipt, and prevents duplicate same-family starts; no free completion loop or payment refund duplication was added.

The output of Weaponization does not itself authorize arming; all six components and separate live facility and terminal checks remain required by the existing terminal route.

## Validation and remaining blocker

A focused source check confirmed all four decision IDs have matching visible, requirements, affordability, and cancel trigger definitions, all four referenced sprite names exist in `interface/016_brilliant_scientist_project_icons.gfx`, and the new localisation file has a UTF-8 BOM.

The decision, stage-trigger, shared predecessor, localisation, and accepted-plan source paths were reviewed directly; no broader syntax or test suite was run for this bounded source patch.

The mandatory baseline audit and same-scenario `hoi4.probability_compare` were routed to `chaosx_ai_probability_auditor` for these scenarios: `sing_theory_peace_provider_ready`, `sing_theory_war_provider_ready`, `sing_offline_prototype_peace_provider_ready`, `sing_offline_prototype_war_provider_ready`, `sing_deployment_peace_provider_ready`, `sing_deployment_war_provider_ready`, `sing_weaponization_peace_provider_ready`, and `sing_weaponization_war_provider_ready`.

The auditor had not returned a status or probability artifact after a 30-second wait, an interrupt-priority request to stop optional exploration, and a further 10-second wait; AI probability validation therefore remains open, and no claim is made that the weights passed the required MCP comparison.

The probability tool descriptions were present in the parent session, so this is an auditor nonresponse rather than a confirmed MCP route outage; the adapter's ability to evaluate these exact decision candidates remains unverified.

Parent follow-up, 2026-09-25: a separate read-only auditor also remained in a running MCP call and was closed after a bounded stop request.
The parent ran `hoi4.probability_inspect`, `hoi4.probability_evaluate`, and a same-source `hoi4.probability_compare` directly on the four stage decisions, as recorded in [the stage AI audit](016_mengele_singularity_stage_ai_audit_2026-09-25.md).
MCP discovered all four candidates under `mission_ai_will_do`, but evaluation and comparison were partial with four unresolved items each; no historical AI delta or effective score is claimed.

No GUI MCP inspection or render was run because this patch adds ordinary decision rows to the existing category and does not introduce or edit a scripted GUI surface.

No HOI4 process was launched and no game logs were accessed; live gameplay acceptance remains with the user and parent integrator.

The parent retains incident wiring and final integration review; this slice is uncommitted as requested.

## Parent review correction

The parent restored the six-component requirement in the shared Prototype predecessor whenever Gotterdammerung is present, while retaining the no-DLC paid route's exception.
The parent also added the enabled Strategic Singularity scenario to all four decision visibility and requirement gates and to their active cancellation triggers, with matching cancellation tooltip text.
These corrections preserve the native component route and prevent paid stage work from remaining active after its scenario is disabled.
The parent documented the four-stage flow, reused icon paths, provider interaction, and remaining terminal work in `docs/events/016_brilliant_scientist/systems/mengele_singularity_stages.md`.

## Skills used

Used `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`; no skill files were created or updated.
