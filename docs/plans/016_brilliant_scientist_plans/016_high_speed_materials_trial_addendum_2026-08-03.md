# Event 016 high-speed materials trial addendum

## Disposition

**Recommendation: implement now.**

This is the highest-value bounded non-model, non-CBRN Event 016 tranche after the Electronics plus Teleportation portal-calibration network.

The project portfolio explicitly promises an Advanced Materials plus Rocketry synergy producing high-speed delivery and improved strategic range, but the current runtime has no joint host action that consumes those two project ledgers.

The proposed tranche adds one costly state-targeted test programme, one two-outcome governance event, two durable but mutually exclusive output packages, explicit transfer behavior, and bounded AI variation based only on the accepted ten-country settlement receipts.

It does not add a project stage, unit, equipment type, technology, focus branch, KRG route, CBRN mechanic, 3D model, report-art request, or generic flavor event.

## Prior-plan audit

The source-of-truth map records the broad Event 016 improvement addendum as closed and dispositioned.

The ten-country settlement addendum is implemented for exactly `GER`, `ENG`, `FRA`, `SOV`, `USA`, `JAP`, `ITA`, `CHI`, `POL`, and `CZE`.

The portal-calibration tranche is implemented and must not be duplicated.

The KRG biological stockpile addendum remains queued and blocked by the native CBRN callback.

The Event 016 3D backlog remains deliberately deferred.

No unresolved addendum already owns the Advanced Materials plus Rocketry host synergy described here.

## Design problem

Advanced Materials and Rocketry currently progress as adjacent but independent project families.

Their stage rewards establish industrial materials applications and strategic high-speed flight, yet the player never has to choose how a tested airframe and propulsion envelope are certified, who owns the resulting tables, or whether range is purchased through Kruger dependence.

The missing play is not another passive modifier grant at stage completion.

It is a joint qualification programme with a geographic test site, a meaningful wartime resource burden, interruption risk, and a transfer-sensitive institutional choice.

## Proposed playable sequence

### 1. Select and fund the test corridor

Add the state-targeted decision `brilliant_scientist_prepare_high_speed_materials_trial` to `brilliant_scientist_directorate_category`.

Working player-facing title direction: “Prepare the High-Speed Materials Trial.”

The decision represents a 180-day series of structural, propulsion, telemetry, and recovery tests at one owned and controlled state selected on the map.

The decision should use `state_target = any_owned_state`, `on_map_mode = map_and_decisions_view`, and the same ROOT/FROM scoping pattern as vanilla state-targeted decisions such as the decisions around `AFG.txt:1069` in the vanilla decision files.

The target state must:

- be owned and controlled by ROOT;
- be a core of ROOT;
- not be impassable;
- not already have `brilliant_scientist_high_speed_test_corridor_active` or `brilliant_scientist_high_speed_test_corridor_certified`.

Do not require a non-capital or non-facility state.

That restriction would create avoidable one-state and displaced-host failures, including inside the accepted ten-country surface.

On start, FROM receives `brilliant_scientist_high_speed_test_corridor_active` and is saved as the global event target `brilliant_scientist_high_speed_test_corridor`.

The global target is justified because the selected state must persist beyond the decision's initial effect block and must be cleared explicitly on cancellation, transfer, and terminal cleanup.

### 2. Revalidate after the 180-day trial

At normal completion, call `brilliant_scientist_high_speed_materials_trial_resolution_is_valid`.

If valid, fire `chaosx.nr16.195` immediately.

If invalid, call `brilliant_scientist_fail_high_speed_materials_trial` instead of firing the event.

Failure consumes the paid resources, sets `brilliant_scientist_high_speed_materials_trial_failed_ever`, clears the active/pending country flags, clears the state flag, and clears the global event target.

Failure does not set the personal completion receipt, so the current or a later host may fund a fresh trial.

There is no refund and no fallback result.

### 3. Choose who owns the flight envelope

Add country event `chaosx.nr16.195` to `events/016_brilliant_scientist_synthesis_events.txt`.

Working title direction: “The Flight Envelope.”

Use `GFX_report_event_016_brilliant_scientist_breakthrough_materials_rocketry`, which already exists and already presents the two relevant project families.

The event has exactly two mutually exclusive outcomes.

#### Option A: certify a national qualification standard

Working option direction: “The qualification board will own the tables.”

Call `brilliant_scientist_resolve_high_speed_materials_trial_national_board`.

Set:

- `brilliant_scientist_high_speed_materials_trial_completed`;
- `brilliant_scientist_high_speed_materials_national_board`;
- `brilliant_scientist_high_speed_test_corridor_certified` on the selected state;
- character flag `brilliant_scientist_personal_high_speed_materials_trial_completed` on `KRG_warren_kruger` only as a one-time guard.

Apply the durable dynamic modifier `brilliant_scientist_high_speed_qualification_board` with:

- `air_accidents_factor = -0.15`;
- `air_mission_efficiency = 0.05`.

Apply the following Directorate ledger vector through the existing change effects and new script constants:

- Mandate `+5`;
- Dependence `-15`;
- Exposure `+10`;
- Project Capacity `-5`;
- Independent Capacity `+15`;
- Grievance `-5`.

The causal reading is that public qualification, independent inspectors, redundant test articles, and auditable materials standards reduce operational accidents and improve ordinary air operations, but slow the Directorate and expose more of its work.

This receipt belongs to the national institution.

It remains on the former host after Kruger transfers and is never copied to an ordinary recipient or KRG.

#### Option B: accept Kruger's proprietary envelope tables

Working option direction: “Use Kruger's envelope and push the range.”

Call `brilliant_scientist_resolve_high_speed_materials_trial_kruger_tables`.

Set:

- `brilliant_scientist_high_speed_materials_trial_completed`;
- `brilliant_scientist_high_speed_materials_kruger_tables`;
- character flags `brilliant_scientist_personal_high_speed_materials_trial_completed` and `brilliant_scientist_personal_high_speed_materials_kruger_tables` on `KRG_warren_kruger`.

Clear `brilliant_scientist_high_speed_test_corridor_active` without leaving the national certified-state receipt.

Apply the durable dynamic modifier `brilliant_scientist_high_speed_kruger_envelope` with:

- `air_range_factor = 0.10`;
- `air_mission_efficiency = 0.05`.

Apply the following Directorate ledger vector:

- Mandate `+5`;
- Dependence `+15`;
- Exposure `+10`;
- Project Capacity `+10`;
- Independent Capacity `+15`;
- Grievance `-5`.

Also add `+10` to Rocketry accident pressure when `brilliant_scientist_refresh_project_accident_pressure` evaluates the Rocketry family and the proprietary receipt is active.

The causal reading is that Kruger releases a more aggressive, less auditable envelope that gives aircraft and high-speed systems greater reach while increasing reliance on his private calculations and increasing the risk of a future project incident.

This receipt follows Kruger.

The old host loses the proprietary country receipt and modifier during transfer reconciliation, while a valid recipient reconstructs them from Kruger's personal history.

## Exact gates

Create `brilliant_scientist_high_speed_materials_trial_projects_are_healthy` in `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt`.

It must require:

- `brilliant_scientist_project_stage_entries^2` at least `constant:brilliant_scientist_project_stage.deployment` for Advanced Materials;
- `brilliant_scientist_project_stage_entries^3` at least `constant:brilliant_scientist_project_stage.prototype` for Rocketry;
- neither family present in `brilliant_scientist_project_suspended_families`;
- neither family present in `brilliant_scientist_project_damaged_families`;
- neither family present in `brilliant_scientist_project_dismantled_families`;
- neither family present in `brilliant_scientist_project_stolen_families`.

Create `brilliant_scientist_high_speed_materials_trial_is_ready` and require:

- `brilliant_scientist_is_current_host = yes`;
- `brilliant_scientist_project_board_is_ready = yes`;
- `brilliant_scientist_primary_facility_is_valid = yes`;
- `brilliant_scientist_secondary_facility_is_valid = yes`;
- `has_country_flag = brilliant_scientist_primary_prototype_works_expanded`;
- the two-family health trigger above;
- no `brilliant_scientist_containment_action_in_progress`;
- no pending or in-progress trial flags;
- neither country outcome flag;
- Kruger lacks `brilliant_scientist_personal_high_speed_materials_trial_completed`;
- no `brilliant_scientist_terminal_commitment_locked`;
- no global `world_end` flag.

Create `brilliant_scientist_high_speed_materials_trial_resolution_is_valid` with the same host, facility, project-health, selected-state control, and terminal checks plus both transaction flags and the saved global target.

The decision must cancel if the host changes, the selected state is no longer owned and controlled by ROOT, either facility becomes invalid, either family becomes suspended/damaged/dismantled/stolen, another project stage or incident begins, terminal commitment locks, or `world_end` appears.

## Exact cost and timing envelope

Place all tuning in `common/script_constants/016_brilliant_scientist_directorate_constants.txt`.

Create `brilliant_scientist_high_speed_materials_trial` constants for:

| Cost or value | Exact plan value |
| --- | ---: |
| Political Power | 100 |
| Air Experience | 25 |
| Support Equipment | 150 |
| Motorized Equipment | 200 |
| Fuel | 5,000 |
| Manpower | 3,000 |
| Civilian factories occupied | 3 |
| Trial duration | 180 days |

Use separate positive gate values and negative spend values, matching the current portal-calibration cost pattern.

The decision uses `custom_cost_trigger` and `custom_cost_text` so the equipment, fuel, manpower, Air Experience, political-power, and factory requirements are visible before commitment.

The decision pays all stockpile, fuel, manpower, and Air Experience costs in `complete_effect` and occupies three civilian factories for the full 180 days.

The project is intentionally more expensive and slower than the 150-day portal-calibration network because it consumes a geographic test corridor and produces a national air-system output.

## AI behavior

Create named constants under `brilliant_scientist_high_speed_materials_trial_ai` rather than literal factors.

### Starting the trial

The AI should normally take the decision once affordable.

Raise priority when at war, when Rocketry is already at Deployment, or when the host has high Project Capacity.

Reduce priority to zero when the AI cannot preserve a stockpile reserve above the exact payment gates or when it is under severe surrender pressure.

Do not create AI-only cost relief or a bypass outcome.

### Choosing the national board

Favor the national-board option when Dependence or Independent Capacity is high, when an independent safety board exists, or when one of these exact settlement receipts is present:

- `brilliant_scientist_country_settlement_british_research_associations`;
- `brilliant_scientist_country_settlement_french_laboratories`;
- `brilliant_scientist_country_settlement_polish_university_shelter`;
- `brilliant_scientist_country_settlement_czechoslovak_research_charter`.

Give `brilliant_scientist_country_settlement_american_federal_contracts` no unconditional option bias; let the current Dependence, Exposure, war, and safety-board state decide.

### Choosing Kruger's tables

Favor the proprietary range option when Project Capacity and Mandate are high, when the strategic-security or military-security posture is active, or when one of these exact settlement receipts is present:

- `brilliant_scientist_country_settlement_german_research_board`;
- `brilliant_scientist_country_settlement_soviet_academy_plan`;
- `brilliant_scientist_country_settlement_japanese_riken_council`;
- `brilliant_scientist_country_settlement_italian_procurement_compact`;
- `brilliant_scientist_country_settlement_chinese_technical_bureau`.

These are AI and presentation consumers of the already-accepted ten-country layer, not new national options or an expanded country list.

All other hosts use the ledger and context defaults.

## Localisation direction

Add decision, custom-cost, effect-tooltip, event-title, event-description, option, and modifier localisation to `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`.

The event description should identify `[brilliant_scientist_high_speed_test_corridor.GetName]` while the target exists and append `[This.GetBrilliantScientistCountrySettlementFacilityClause]` so the accepted country settlement affects the institutional argument without adding more tags.

The description must explain that materials qualification and propulsion trials have produced two incompatible archives: a slower auditable national standard and a more aggressive set of tables controlled by Kruger.

Tooltips must disclose the two ledger vectors, the exact air modifiers, the Rocketry accident-pressure change on the proprietary route, and the transfer ownership of each result.

Use “flight envelope,” “control tables,” “materials qualification,” “instrumented test vehicle,” and “test corridor.”

Do not use “cybernetics,” which would be anachronistic for most of the playable period, and do not describe either outcome as a patch, rework, cap, or implementation change.

## Asset reuse

No new art, animated sprite, portrait, flag, model, entity, mesh, or animation is required.

Use `GFX_decision_brilliant_scientist_project_rocketry_propulsion_deployment` for the state-targeted decision.

Use `GFX_report_event_016_brilliant_scientist_breakthrough_materials_rocketry` for `chaosx.nr16.195`.

Both sprites are already registered, so no `.gfx`, DDS, manifest, or 3D pipeline change belongs in this tranche.

## Transfer, snapshot, and cleanup contract

### Interrupted transaction

Extend `brilliant_scientist_reconcile_old_host_after_transfer` to clear the two transaction flags, remove `brilliant_scientist_high_speed_test_corridor_active` from the saved state, and clear `brilliant_scientist_high_speed_test_corridor`.

No resources are refunded and no outcome flag is granted.

Extend `brilliant_scientist_cleanup_transient_targets_after_world_end` with the same transient cleanup.

### National-board result

The former host keeps `brilliant_scientist_high_speed_materials_national_board`, the certified state flag, and `brilliant_scientist_high_speed_qualification_board` after Kruger leaves.

Do not add the national-board receipt to `brilliant_scientist_inherit_kruger_personal_history_portfolio` or the KRG formation snapshot.

### Proprietary result

The old host clears `brilliant_scientist_high_speed_materials_kruger_tables` and removes `brilliant_scientist_high_speed_kruger_envelope` in `brilliant_scientist_reconcile_old_host_after_transfer`.

In `brilliant_scientist_inherit_kruger_personal_history_portfolio`, reconstruct the proprietary country receipt and modifier when Kruger has `brilliant_scientist_personal_high_speed_materials_kruger_tables`.

For fixed-tag KRG formation, add `brilliant_scientist_formation_carried_high_speed_materials_kruger_tables` to `brilliant_scientist_snapshot_kruger_state_portfolio` and restore it in `brilliant_scientist_inherit_kruger_carried_portfolio`.

Do not replay the ledger vector, state selection, costs, or event when restoring the portable receipt.

### Final terminal cleanup

The final Event 016 runtime cleanup should clear any active transaction and global target.

Completed national or proprietary receipts may remain as historical facts, but their dynamic modifiers must be removed from countries that are deleted or converted by the terminal outcome in the same places existing Directorate modifiers are removed.

## Exact implementation surfaces

| File | Required implementation |
| --- | --- |
| `common/decisions/016_brilliant_scientist_directorate_synthesis.txt` | Add `brilliant_scientist_prepare_high_speed_materials_trial` and its three-factory file-scoped mirror only where the field rejects script constants. |
| `common/script_constants/016_brilliant_scientist_directorate_constants.txt` | Add cost, timing, ledger-delta, modifier-value, and AI-factor constants. |
| `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt` | Add project-health, ready, cost, target-state, resolution-valid, and active-receipt triggers. |
| `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt` | Add start cleanup, failure, common completion, national-board resolution, and proprietary-table resolution effects. |
| `common/scripted_effects/016_brilliant_scientist_effects.txt` | Add proprietary Rocketry accident pressure and ordinary-transfer restore/clear hooks. |
| `common/scripted_effects/016_brilliant_scientist_country_effects.txt` | Add KRG snapshot and carried-receipt restore hooks. |
| `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt` | Add the two mutually exclusive dynamic modifiers. |
| `events/016_brilliant_scientist_synthesis_events.txt` | Add `chaosx.nr16.195`; the ID is unused in the current Event 016 namespace. |
| `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` | Add all decision, event, option, tooltip, cost, and modifier strings with UTF-8 BOM. |
| `docs/events/016_brilliant_scientist/systems/projects.md` | Document the Advanced Materials plus Rocketry qualification path and both ownership results. |
| `docs/events/016_brilliant_scientist/systems/directorate.md` | Document costs, ledger effects, transfer behavior, and the ten-country AI/presentation consumer. |
| `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md` | Mark this addendum accepted, implemented, queued, or rejected after parent disposition. |
| `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` | Add the implementation handoff and remaining validation status if implemented. |

The implementation owner should inspect the Event 016 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after implementation.

Only update the workbook if its existing project-detail field enumerates individual synergy actions; never add a standalone row for `chaosx.nr16.195`, and never edit exported CSV files directly.

## Historical and regional research basis

The Smithsonian National Air and Space Museum records that the A-5 became the guidance test bed after the four A-3 launches failed in 1937, and that black-and-white test patterns helped observers track vehicle attitude.

That supports a design centered on repeated instrumented trials and ownership of the resulting control tables rather than a one-click weapon grant.

The Museum also records that the Hs 293 programme used unpowered control-test vehicles and then improved early powered flights through extensive testing.

That supports a sequence in which an expensive test corridor produces either auditable qualification or a more aggressive envelope.

The Smithsonian Peenemünde archive includes aerodynamic work on the A-4, A-5, and Wasserfall and documents raw-material requirements, semi-finished materials, and manufacturing procedures for the A-4.

That is the direct historical bridge between the Advanced Materials and Rocketry project families.

The historical programme was tied to Nazi weapons development and, in production, forced and enslaved labor.

The event should use the technical test-and-certification connection without romanticizing the institution, concealing its coercion, or presenting dictatorship as inherently efficient.

Research links:

- Smithsonian National Air and Space Museum, “V-2 Missile”: https://airandspace.si.edu/collection-objects/missile-surface-surface-v-2-4/nasm_A19600342000
- Smithsonian National Air and Space Museum, “Henschel Hs 293 A-1”: https://airandspace.si.edu/collection-objects/missile-air-surface-henschel-hs-293-1/nasm_A19840793000
- Smithsonian National Air and Space Museum, “Peenemünde Aerodynamics Reports”: https://airandspace.si.edu/collection-archive/peenemunde-aerodynamics-reports/sova-nasm-xxxx-0193
- Smithsonian National Air and Space Museum, “The Myth of the German ‘Wonder Weapons’”: https://airandspace.si.edu/stories/editorial/myth-german-wonder-weapons

## Validation scenarios

1. A generic host with Materials at Deployment and Rocketry at Prototype, valid facilities, expanded prototype works, healthy ledgers, and sufficient resources can select exactly one owned and controlled core test state.
2. A host missing either stage, a facility, the prototype-works expansion, or any cost component sees an exact unavailable reason.
3. Suspending, damaging, dismantling, or stealing either family during the 180 days cancels the transaction, consumes costs, and leaves no outcome.
4. Losing control of the selected state cancels the transaction and clears the saved global target and state flag.
5. Host transfer during the 180 days cancels without a refund or free receipt; the recipient may start a new trial only if Kruger's personal completion guard was never set.
6. The national-board option applies the reliability modifier, exact ledger vector, certified state receipt, and no portable Kruger flag.
7. The proprietary option applies the range modifier, exact ledger vector, Rocketry accident pressure, and personal portable receipt.
8. After an ordinary transfer, the old host keeps the national-board result but loses the proprietary result; the new host receives only the proprietary result and never replays costs or ledger deltas.
9. Fixed-tag KRG formation restores the proprietary receipt once and never fabricates the national-board result or a test-corridor state.
10. `GER`, `ENG`, `FRA`, `SOV`, `USA`, `JAP`, `ITA`, `CHI`, `POL`, and `CZE` use only their existing settlement receipts for AI weights and the existing settlement facility clause for text; no eleventh tag receives bespoke content.
11. A host outside the ten-country set receives the complete generic mechanic with ledger-driven AI and an empty settlement clause.
12. Terminal commitment or `world_end` removes an active transaction and its global target, and no delayed `.195` event appears afterward.
13. The two outcome modifiers are mutually exclusive and remain within the planned `0.10` range, `-0.15` accident, and `0.05` mission-efficiency values.
14. The existing portal-calibration, cross-domain synthesis, KRG machine-command, KRG strategic-delivery, CBRN, and 3D surfaces remain unchanged except for shared cleanup hooks that are strictly necessary for this transaction.

## Acceptance criteria

- The player receives one real Advanced Materials plus Rocketry action rather than a passive stage bonus.
- The selected state, 180-day burden, cancellation rules, and two ownership outcomes are visible before commitment.
- Each outcome has a distinct gameplay consumer and transfer identity.
- The national-board result cannot follow Kruger.
- The proprietary result cannot remain on the former host after Kruger leaves.
- No route replays the costs, event, ledger deltas, or state selection.
- Exactly the accepted ten country-settlement receipts influence bounded AI and presentation; the playable mechanic remains available to all otherwise-valid hosts.
- No new asset or model is requested.
- No biological stockpile, CBRN callback, or fallback is touched.
- The parent records this addendum's disposition before requesting another Event 016 improvement-loop pass.

## Explicit disposition of unselected directions

### Computation plus Robotics machine-command charter

**Rejected as a duplicate.**

KRG already has `KRG_write_the_machine_command_protocol`, `brilliant_scientist_krg_choose_machine_command_protocol`, human supervisory keys, air-gapping, rogue-node containment, and bounded robot assembly.

A host-side machine-command charter would repeat an existing governance and safety surface rather than open a new project promise.

### Computation plus Temporal prediction cell

**Not selected.**

The temporal route already has a dense capacity, debt, anchor, authentication, warning, and KRG action surface.

It needs validation more than another adjacent action.

### Biological Weapons plus Teleportation remote delivery

**Blocked and not designed around.**

The native CBRN callback remains the accepted blocker for KRG biological stockpile production, reservation, and consumption.

No workaround, substitute stockpile, or fallback delivery mechanic is proposed.

### New country packages or an eleventh settlement tag

**Rejected for this tranche.**

The accepted settlement boundary is exactly ten countries.

This addendum consumes those receipts but does not expand the set.

### New 3D test vehicle or missile entity

**Deferred.**

The user explicitly excludes 3D models at this stage, and the mechanic has complete existing 2D asset coverage.

## Tooling limitation

The installed package has no Technology Tree Viewer.

This plan therefore relies on static source inspection for project stages and technologies and does not claim rendered technology-tree evidence.

Event, focus, GUI, and map inspection were not used because the exact source files already established the gap and no additional read-only viewer evidence would change the bounded design.

No rewrite tool was used.

## Promotion rule

Keep this file in `docs/plans/016_brilliant_scientist_plans/` until the parent explicitly accepts, queues, or rejects it.

If accepted and implemented, promote the project promise, gates, two outcomes, transfer contract, AI rules, and validation criteria into `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_3_project_portfolio.md` and the relevant project/decision matrices.

Then update the source-of-truth map to identify the promoted spec sections and retain this addendum only as implementation history.
