# Event 016 Directorate and Kruger State decision and mission audit

## Scope and evidence

This is a read-only audit of the current Event 016 Directorate high-speed materials trial, finite country-settlement choices, and the Kruger State decision and mission layer.

The source review covered `common/decisions/016_brilliant_scientist_directorate_synthesis.txt`, `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt`, `events/016_brilliant_scientist_synthesis_events.txt`, the Event 016 context event and effects files, all eight `common/decisions/016_brilliant_scientist_kruger_state_*.txt` files, the relevant constants and dynamic modifiers, and the matching English localisation.

The review also used the offline Decision modding, Data structures, Triggers, Effects, Localisation, Scopes, AI modding, and related required wiki snapshots, official vanilla effect and trigger documentation, and vanilla formable-decision precedents.

`hoi4.event_inspect` reported zero blocking diagnostics for `chaosx.nr16.195` on workspace revision `d4554138622a675f8893ef2eb6a2475018c90d98c1d33b88aaacf8e22fae440f`.

The MCP artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72fb5177282710c010fafa9cb685d199bf2011110fcd6e2c1b01b8eb26da60c0/05977fad2afe522ba13009eb8c54d8aab0c0fda5537f15fdafb098063a3f11d8/event-lint-d4554138622a.json`.

That artifact is partial evidence only because its inline source inventory was truncated and it deliberately deferred workspace-wide helper and lifecycle validation.

No decision-owned scripted GUI was changed or required inspection because the reviewed surfaces use normal category, state-target, event, and mission UI rather than a scripted GUI action.

## Issue list

### Medium: quantitative settlement AI acceptance remains unproven

The ten country-specific `.5` choices have valid non-zero base weights, compatible-context preference factors, and cautious war or pressure factors where authored.

The required full candidate-pool score and rank-reversal evidence from `docs/specs/016_brilliant_scientist_specs/acceptance/016_balance_and_exploit_review.md` was not produced by this audit.

An attempted targeted probability inspection did not return before the tool process was stopped, so this is an acceptance-evidence gap rather than a confirmed AI script defect.

Recommended follow-up: run the project's supported weighted-logic evaluation against every intended host, compatible context, pressure state, and generic-option competitor before accepting the finite-settlement AI scenarios.

### Low: no confirmed local gameplay defect

No missing prerequisite, duplicated reward path, stale high-speed corridor target, unsafe former-host copy, free retry, or unwired event/localisation consumer was confirmed in the reviewed scope.

No gameplay patch is recommended from this audit.

## Directorate category lifecycle

`brilliant_scientist_prepare_high_speed_materials_trial` is visible only while the current host has a ready, pending, or active trial state and accepts a state target only when it is owned, controlled, core, non-impassable, and not already an active or certified corridor.

The start gate requires both healthy project ledgers, Materials Deployment, Rocketry Prototype, expanded prototype works, two valid facilities, an idle and non-terminal Directorate state, the complete material gate, and a valid target.

The decision charges its normal political-power `cost` and manually debits Air Experience, support equipment, motorized equipment, fuel, and manpower in `complete_effect`, while occupying three civilian factories for 180 days.

The saved global corridor target and state active flag are cleared by the shared fail and cleanup helpers on lost host control, facility or ledger failure, containment, incident, terminal transition, or invalid target.

Valid expiry opens `chaosx.nr16.195`; invalid expiry uses the failure helper rather than granting either outcome.

The national board is a former-host result with a certified state corridor, while Kruger's proprietary tables are carried and rebuilt only through the documented Kruger transfer and formation history path.

The trial has no `fire_only_once` because a failed or cancelled unpaid completion may be attempted again, but both successful receipts and Kruger's personal completed-history guard block a second reward.

## Finite country-settlement lifecycle

`chaosx.nr16.5` is host-only and requires the pending assistant-conflict context and no resolved receipt.

The ten final country options are present as `chaosx.nr16.5.d_eng` through `.m_cze`, each has a matching country tag and context gate, matching custom effect tooltip, hidden resolver call, and English localisation in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`.

Each resolver first clears the pending conflict, writes the common resolved receipt, writes its own host-local country-settlement receipt, applies the shared generic settlement resolution once, applies only its bounded national delta, and schedules the existing lecture follow-up.

The ordinary host-transfer and Kruger-formation effect files contain no country-settlement receipt or helper reference, so these receipts are not accidentally copied into a recipient or fixed-tag formation state.

The generic conflict-resolved flag prevents selecting a generic option and a national option from the same context, and the individual receipt guards prevent duplicate national rewards.

## Mission quality notes

The Kruger layer contains eleven declared missions across the Clone and Machine, Foundation, Portal and Temporal, and Terminal categories.

The four repeatable-reward-risk missions below were read at their declaration and timeout paths because they are the relevant paid-objective safeguard surface.

| Mission | Owner/category and region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| `brilliant_scientist_krg_clone_drift_review_mission` | Clone and Machine; controlled clone-growth site | Active KRG layer, paid lineage objective, containment duration | Grants registry repair and minor stability only when the objective and site proof survive; otherwise invokes the failure helper | Completion receipt closes the producer; no repeat stability loop found. |
| `brilliant_scientist_krg_rogue_node_containment_mission` | Clone and Machine; controlled machine node | Active KRG layer, paid isolation objective, containment duration | Grants rogue-node containment and minor stability only after the full-success trigger; otherwise invokes the failure helper | Completion receipt closes the producer; no free completion path found. |
| `brilliant_scientist_krg_maintenance_audit_mission` | Foundation; canonical primary facility | Active KRG layer, paid service objective, maintenance duration | Rebuilds the runtime package only after the objective and facility proof survive; otherwise invokes the failure helper | The completion receipt guards the rebuild producer; no free rebuild loop found. |
| `brilliant_scientist_krg_transit_breach_closure_mission` | Portal and Temporal; controlled operational transit terminal | Active KRG layer, paid sealing objective, containment duration | Grants breach closure and minor stability only after the full-success trigger; otherwise invokes the failure helper | Completion receipt closes the producer; no repeat stability loop found. |

The timeout paths clear active and transient objective state on success, call named failure helpers on unmet proof, and the reviewed cancellation paths clear active state and objective scratch state without rewards.

The remaining declared missions are clone identity pressure, ministry consolidation, primary facility defense, ministry replacement, temporal rescue survival, temporal stabilization supervision, and singularity disarmament hold.

Their detailed balance and route design were outside this bounded pass, but the inventory confirmed that they are mission declarations rather than hidden recurring on-actions.

## Cost and requirement clarity

The high-speed trial exposes one player-facing cost string that matches the political power, Air Experience, equipment, fuel, manpower, factory burden, and 180-day commitment in its constants and effects.

Its stockpile and experience gates use values one below the exact debit, so an exact available amount can pay the corresponding debit without a one-unit shortfall.

The ten settlement choices are outcome selections rather than flat political-power exchanges; they use mutually exclusive context and national receipts instead of a paid repeat loop.

KRG's common material-cost helpers centralize visible gates and debits, while the reviewed objective decisions commit costs before their mission outcome and do not refund cancellation.

## AI and route-lock notes

The high-speed producer AI has reserve checks for the paid resources, a severe-surrender block, war, Rocketry Deployment, and project-capacity modifiers.

`chaosx.nr16.195` has two non-zero outcome choices with explicit national and Kruger receipt preferences, so neither player-visible outcome is AI-dead in the inspected script.

The settlement options have tag and context locks, use their own settlement base and preference constants, and retain the generic choices as competitors rather than replacing the entire event.

The national board has no ordinary-transfer or formation copy path, while the proprietary tables rebuild only for Kruger's personal history; this matches the intended ownership split.

## Localisation, cleanup, and exploit-risk notes

The high-speed decision, cancellation consequence, report title and description, both outcome tooltips, and both ownership statements have localisation consumers.

The report description uses the existing country-settlement facility clause, and all ten settlement receipts have matching scripted-localisation branches and text consumers.

The high-speed failure and terminal/transfer cleanup clear pending and in-progress flags, the saved corridor target, and the state active flag without refunding sunk costs.

The proprietary dynamic modifier is removed from an old host and rebuilt only for the valid current host, preventing a former-host modifier leak.

No CBRN-stockpile workaround, model work, new event-log row, or new scripted GUI surface was introduced or needed by the reviewed materials and settlement features.

## Recommended follow-up

1. Produce the missing full weighted-logic candidate-pool evidence for the ten settlement choices, including the specified rank reversals and generic alternatives.

2. Retain the existing high-speed transfer and formation scenarios in targeted validation: national former-host persistence, proprietary ordinary transfer, proprietary KRG formation, invalid corridor cancellation, and no-refund failure.

3. Do not patch the current high-speed or settlement gameplay from this audit unless the quantitative AI evaluation exposes a concrete rank or zero-weight defect.

## Changed files and validation

This audit changed no gameplay, localisation, scripted GUI, focus, event, or asset file.

The only new file is this handoff.

Meaningful validation was source-level lifecycle tracing of the high-speed producer, resolution event, helper effects, transfer/world-end cleanup, settlement option-to-resolver-to-localisation wiring, and the four KRG paid-objective mission timeout paths.

The deferred meaningful validation is the full numerical AI ranking sweep described above.

No simplification or fallback was made.
