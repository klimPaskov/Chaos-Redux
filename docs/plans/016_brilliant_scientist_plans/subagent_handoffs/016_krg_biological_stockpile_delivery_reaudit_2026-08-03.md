# Event 016 KRG biological stockpile and delivery re-audit

Date: 2026-08-03

## Result

The proposed Event 016-owned biological quantity ledger is not safe to implement in the current native raid boundary. No gameplay, localisation, CBRN, model, or shared lifecycle file was changed by this re-audit.

## Evidence

- `common/raids/biological_battlefield_raids.txt` declares `essential_equipment` for the four ordinary pathogen raid types. Vanilla raid documentation states that essential equipment is collected when a raid is created, before the outcome effects run.
- `bio_resolve_strategic_raid_outcome` in `common/scripted_effects/biological_raid_effects.txt` receives the already-created raid instance and resolves lifecycle outcome, consumption, refunds, history, and command refund. It has no reservation callback, cancellation callback, or expiry callback owned by Event 016.
- The current resolver records the exact native payload requirement and consumed amount, refunds only unused native equipment, and treats context rejection as consumed payload loss. A separate Event 016 debit at this point would double-charge native equipment; an Event 016-only debit without a native reservation hook would create a free-payload path.
- Native raid preparation can therefore expire, cancel, or be invalidated outside the Event 016 resolver. Adding a per-agent Event 016 receipt without a guaranteed native lifecycle callback could leave a reservation orphaned through transfer, defeat, or raid cancellation.
- The existing KRG bridge remains valid: project history restores native delivery technologies and the correct biological delivery idea; the native raid and biological lifecycle remain authoritative for payload, contamination, evidence, deaths, attribution, Condemnation, and confirmed-use history.

## Disposition

Do not add an Event 016 biological stockpile variable, production decision, reservation debit, consumption callback, or transfer/defeat cleanup until the shared CBRN raid system exposes an idempotent reservation/outcome/cancellation contract. The required contract must carry a stable raid-instance identifier, agent identity, actor identity, and exact native reservation result, and must invoke Event 016 callbacks exactly once for success, failure, accident, cancellation, expiry, transfer, and defeat.

The current design addendum remains queued, not implemented. No free payload, placeholder production, model dependency, or fallback was introduced.

## Remaining validation

Live raid creation, cancellation, expiry, transfer, and defeat scenarios remain user-owned validation. The shared CBRN lifecycle files were intentionally left untouched because unrelated dirty edits are present in the worktree.
