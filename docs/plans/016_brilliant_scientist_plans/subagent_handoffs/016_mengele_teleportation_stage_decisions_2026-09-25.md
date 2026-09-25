# Event 016 Mengele Teleportation provider stage decision handoff

Status: implemented source wrappers for parent integration; engine acceptance and probability audit remain open.

## Ownership and changed files

- `common/decisions/016_mengele_teleportation_stage_decisions.txt`: four fixed family/stage timed decision wrappers in the existing `mengele_clone_army_category`.
- `common/scripted_triggers/016_mengele_teleportation_stage_decision_triggers.txt`: exact private family receipt, visibility, inclusive cost, and cancellation gates.
- `localisation/english/016_mengele_teleportation_stage_l_english.yml`: UTF-8 BOM titles, descriptions, costs, requirements, and lifecycle effects.
- This handoff records implementation evidence and unresolved gates.

No other files were edited, staged, or committed.

## Source contract and review

The accepted provider plan at `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md` specifies private family ID 7, one family receipt, four stages, the native `sp_brilliant_scientist_quantum_transit` Prototype, and persistent Portal entitlement at Prototype. The accepted `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` requires paid no-DLC progression without a second native payment.

The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` describes `visible`, `available`, `custom_cost_trigger`, timed decision callbacks, and the factory modifier. The installed `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, and `documentation/triggers_documentation.md` establish fixed-point script constants and the tooltip effects/triggers. Vanilla `common/decisions/GER.txt` uses `days_remove`, `modifier = { civilian_factory_use = ... }`, `custom_cost_trigger`, and separate `complete_effect`, `remove_effect`, and `cancel_effect`. The installed wiki and documentation were read without opening the online Paradox wiki.

The shared private core at `common/scripted_effects/016_mengele_project_stage_effects.txt` quotes Teleportation Theory, Prototype fallback, Deployment, and Weaponization costs/durations and uses literal family/stage selectors to begin, cancel, and finish. Its Teleportation Prototype branch records the provider flag and modifier, while its Deployment and Weaponization branches use the existing neutral Portal technology API. The exact native bridge in `common/scripted_effects/016_mengele_project_bridge_effects.txt` grants the Portal operational API after native Prototype completion. The new paid no-DLC Prototype wrapper grants that same neutral API only after the private finish reports a successful Teleportation Prototype output. This preserves the operational entitlement when no native project is presented and does not add native project payment or output.

The shared family constants in `common/script_constants/016_brilliant_scientist_constants.txt` define Teleportation as family 7 and stage durations of 240, 360, 540, and 720 days. The new receipt gates use aligned array index 6. The shared cost constants in `common/script_constants/016_brilliant_scientist_project_constants.txt` define factory reservations 2/3/6/9 and political power 60/90/120/180, with the Prototype values in the fallback table. File-local mirrors are used only for `civilian_factory_use` and `ai_hint_pp_cost`; payment and display read shared constants. The four icon names already exist in `interface/016_brilliant_scientist_project_icons.gfx` and match the Kruger Teleportation stage rows in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`.

Manual stage review:

| Stage | Entry gate | Settlement | Entitlement behavior |
| --- | --- | --- | --- |
| Theory | Valid provider, empty family receipt, unfinished Theory | Private begin/cancel/finish with exact family 7 and Theory | Records private Theory history. |
| Prototype | Theory complete, empty receipt, no Götterdämmerung, native quantum transit incomplete | Fallback quote and exact Prototype callbacks | Records private Prototype history, then grants neutral Portal operations only after successful finish. |
| Deployment | Prototype complete, empty receipt, unfinished Deployment | Exact Deployment callbacks | Uses private stage core; its neutral API is idempotent when Portal operations were already learned. |
| Weaponization | Deployment complete, empty receipt, unfinished Weaponization | Exact Weaponization callbacks | Uses existing `portal_weaponization` upgrade in the private core. |

Each decision calls the same inclusive `can_pay` predicate in `available` and `custom_cost_trigger`. Its direct quote is Political Power, Support Equipment, and Fuel where nonzero; native timed-decision factory use reserves and releases civilian factories. The inline row contains at most three icons, and its separate cost tooltip shows all committed axes. Each wrapper supplies exact literal family and stage in begin, cancel, and finish. Cancellation is keyed to the exact private receipt or loss of provider authority, not later resource depletion. The decisions write no Kruger capacity, history, or receipt identifiers.

## Validation and unresolved gates

Source review found exactly four decision IDs, each with an icon, four-stage order, shared duration, cost gate, direct payment callback, exact cancellation callback, and AI weight. The new decision and trigger files have balanced blocks; the localisation file begins with UTF-8 BOM. The referenced sprite definitions exist. This is source evidence only; no HOI4 process was launched and no engine acceptance is claimed.

The shared private Deployment core calls `chaosx_grant_custom_operational_technology` again. Its Portal grant core checks for existing technology before setting it and the provenance writer is designed to be idempotent, so the wrapper does not create a second technology; the parent should still verify the native consumer and provenance array do not display a duplicate operational award. The parent owns final integration, the required probability MCP baseline/comparison for the new `ai_will_do` surfaces, engine verification of native decision factory reservation and callback order, and commit. The accepted plan also records a same-family re-entry ordering gate that source inspection cannot resolve. No fallback, extra project, new icon, or Kruger receipt was introduced.

Skills used: `chaos-redux-decisions-missions` and `chaos-redux-events`; no skill was created or updated.

## Parent review

The parent checked the four literal stage selectors, family array index six, shared quote values, existing icon definitions and DDS files, the no-DLC Prototype post-finish guard, and the custom Portal API's idempotent operational grant and provenance writer.
The custom operational grant reports success for an already learned Portal family, so Deployment can record its private stage without granting a second technology.
The parent replaced implementation-facing Prototype requirement prose with a player-facing funding choice and added `docs/events/016_brilliant_scientist/systems/mengele_teleportation_stages.md` for the lifecycle, assets, and acceptance limits.
The AI probability audit, native decision-list presentation, same-family timer ordering, and live consumer behavior remain open; this review does not certify those surfaces.
The parent attempted a read-only `hoi4.gui_inspect` for `countrydecisionview` with scenario `event016_directorate_compact_current`; the bounded call returned no structured inspection envelope or artifact, so no visible cost or tooltip conclusion follows from it.
The AI auditor captured a prepatch four-decision `mission_ai_will_do` baseline, analysis `probability-eca01ee959a4290dd4190473`, with scores 10 at peace and 20 at war for all four rows. That exposed the worker draft's incorrect high base for Theory, Deployment, and Weaponization, which Kruger's corresponding rows score 5 at peace and 10 at war. The parent corrected those three bases to `ai_medium`, retained Prototype `ai_high`, and applied the existing cautious factor only when available factories do not exceed the current stage's reservation quote. The final-source audit in `016_mengele_teleportation_ai_audit_2026-09-25.md` reports peace score traces 5/10/5/5 and war traces 10/20/10/10 before unresolved cautious predicates; its same-scenario `hoi4.probability_compare` request was rejected because the captured baseline evaluation is not a valid comparison manifest and the prepatch source has no immutable path.
