# Event 016 KRG biological stockpile and delivery re-audit

Date: 2026-08-03

Status: superseded historical re-audit, retired 2026-09-02. No gameplay, localisation, CBRN, model, or shared lifecycle file was changed.

> This re-audit remains valid evidence against the former parallel Event 016 numeric stockpile and native-reservation ledger, but it is not an active callback blocker for the current architecture. The binding [`016_final_completion_contract.md`](../../../specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md) and current [`biological_operations.md`](../../../events/016_brilliant_scientist/systems/biological_operations.md) establish that actual pathogen equipment is authoritative, native raids own reservation and outcome lifecycle, and Event 016 production, staging, and decision-led deployments use separate transactions. Tranche 4 source remains under review and MCP transaction acceptance is unresolved. See [`016_final_raid_docs_reconciliation_2026-09-02.md`](016_final_raid_docs_reconciliation_2026-09-02.md).

## Result

The proposed Event 016-owned biological quantity ledger is not safe to implement in the current native raid boundary. No gameplay, localisation, CBRN, model, or shared lifecycle file was changed by this re-audit.

## Evidence

- `common/raids/biological_battlefield_raids.txt` declares `essential_equipment` for the four ordinary pathogen raid types. Vanilla raid documentation states that essential equipment is collected when a raid is created, before the outcome effects run.
- `bio_resolve_strategic_raid_outcome` in `common/scripted_effects/biological_raid_effects.txt` receives the already-created raid instance and resolves lifecycle outcome, consumption, refunds, history, and command refund. It has no reservation callback, cancellation callback, or expiry callback owned by Event 016.
- The current resolver records the exact native payload requirement and consumed amount, refunds only unused native equipment, and treats context rejection as consumed payload loss. A separate Event 016 debit at this point would double-charge native equipment; an Event 016-only debit without a native reservation hook would create a free-payload path.
- Native raid preparation can therefore expire, cancel, or be invalidated outside the Event 016 resolver. Adding a per-agent Event 016 receipt without a guaranteed native lifecycle callback could leave a reservation orphaned through transfer, defeat, or raid cancellation.
- The existing KRG bridge remains valid: project history restores native delivery technologies and the correct biological delivery idea; the native raid and biological lifecycle remain authoritative for payload, contamination, evidence, deaths, attribution, Condemnation, and confirmed-use history.

## Historical disposition of the retired proposal

Do not add the proposed Event 016 biological stockpile variable, parallel native-reservation debit, consumption callback, or transfer/defeat cleanup ledger. The proposal is retired by the binding completion contract. Native raids retain their native reservation, cancellation, expiry, outcome, refund, history, contamination, condemnation, and confirmed-use ownership, while the separate Event 016 production, staging, and decision-led deployment receipts follow the current biological-operations surface.

The design addendum is retired rather than queued for this callback. No free payload, placeholder production, model dependency, or fallback was introduced. Tranche 4 source review and MCP transaction acceptance remain open.

## Remaining validation

Live raid creation, cancellation, expiry, transfer, and defeat scenarios remain user-owned validation. The shared CBRN lifecycle files were intentionally left untouched because unrelated dirty edits are present in the worktree.
