# Event 016 Foreign Operations Implementation Handoff

## Scope

This tranche implements the Evolution II international contest: bounded actor initialization, targeted diplomatic and covert decisions, dynamic MTTH AI weights, separate success and detection calculations, host response events, actor reports, project-family targeting, transfer safety, assassination continuity, opinion memory, scripted localisation, and English text.

## Files

Added:

- `common/script_constants/016_brilliant_scientist_foreign_constants.txt`
- `common/mtth/016_brilliant_scientist_foreign_mtth.txt`
- `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`
- `common/scripted_localisation/016_brilliant_scientist_foreign_scripted_localisation.txt`
- `common/decisions/categories/016_brilliant_scientist_foreign_categories.txt`
- `common/decisions/016_brilliant_scientist_foreign_decisions.txt`
- `common/opinion_modifiers/016_brilliant_scientist_foreign_opinion_modifiers.txt`
- `events/016_brilliant_scientist_foreign_events.txt`
- `localisation/english/016_brilliant_scientist_foreign_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/foreign_operations.md`
- this handoff

Modified integration:

- `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` calls `brilliant_scientist_foreign_initialize_contest = yes` after Evolution II's base state is committed.

## Stable interfaces

- `brilliant_scientist_foreign_initialize_contest = yes` — current-host scope; one bounded actor scan
- `brilliant_scientist_foreign_start_operation = yes` — targeted actor scope with temporary operation type
- `brilliant_scientist_foreign_resolve_covert_operation = yes` — targeted actor decision completion
- `brilliant_scientist_foreign_finish_operation = yes` — actor report cleanup
- `brilliant_scientist_foreign_cancel_operation = yes` — actor/host lock cleanup

Successful foreign transfers call the preexisting `brilliant_scientist_transfer_kruger_atomically = yes` contract and then reinitialize the contest on the new host.

## Coverage

- Nine foreign actions: observation, formal invitation, assistant recruitment, archive theft, project sabotage, encouraged defection, extraction, protection offer, and assassination attempt.
- Eighteen event IDs: `.100`, `.101`, `.110`, `.111`, `.120`, `.121`, `.130`, `.131`, `.140`, `.141`, `.150`, `.151`, `.160`, `.161`, `.170`, `.171`, `.180`, and `.181`.
- Per-actor one-live-operation lock and per-host two-incoming-operation cap.
- Per-host persistent arrays for observation, invitation, recruitment, theft, sabotage, transfer, protection, and assassination history.
- Exact selected project-family and stage ledger for theft, sabotage, recruitment, and partial extraction.
- AI weights react to ideology, faction, war, intelligence agency, network strength, threat, host Exposure, project weaponization, Grievance, Dependence, and Independent Capacity.
- Security responds through detection, bilateral opinion, political/stability cost, host alert, hardened facilities, protection, and loyalty review.

## Validation

- All nine targeted decisions have a registered icon, cost, availability tooltip, effect tooltip, AI weight, cancellation path where timed, and target lifecycle gate.
- All eighteen event IDs are unique within the Event 016 namespace and every title, description, option, and scripted-localisation key resolves in English.
- Source files have balanced delimiters and contain no unsupported comparison operators.
- The localisation file is UTF-8 with BOM and uses no `:0` keys.
- No periodic whole-world on-action exists. Contest setup uses one explicit scan at Evolution II opening or successful host transfer.
- Transfer routes revalidate the single Kruger identity and degrade to a partial result when the final rendezvous is invalid.

## Remaining integration

- Foreign outcomes must be added to the shared Event 016 event-details and event-log surfaces during the final integration tranche.
- The KRG country package should consume patron, thief, exposed-operation, protection, and assassin history for route weights and diplomacy.
- The Event 016 completion and decision/mission auditors must review the integrated foreign chain before acceptance.
