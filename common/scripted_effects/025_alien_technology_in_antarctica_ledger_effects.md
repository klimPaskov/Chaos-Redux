# Shared alien recovery ledger

Event 025 and Event 036 share reward provenance through the Event 016 external owner API.
Physical material is a separate ledger from researched technology and historical recovery receipts.
No custody transaction grants technology, changes the winner, or creates Event 016 history.

## Physical custody contract

`chaosx_alien_recovery_event025_owner` is the historical winner pointer.
`chaosx_alien_recovery_core_custodian` is the current physical-core pointer.
The initial Event 025 resolver initializes the latter once; its initialization receipt survives destruction and abandonment.
Six persistent `chaosx_alien_recovery_fragment_owner_<1..6>` targets are authoritative fragment owners.
Each slot also has an assigned flag, a bounded role, and a permanent destroyed flag when retired through destruction.

| Effect | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `chaosx_alien_recovery_ledger_assign_fragment` | Country; temporary `chaosx_alien_recovery_fragment_id` and `chaosx_alien_recovery_fragment_role`, each an integer 1–6 | Temporary `chaosx_alien_recovery_fragment_assigned`, zero on rejection; acquires only an unowned, non-destroyed slot for a valid independent country |
| `chaosx_alien_recovery_ledger_transfer_physical_custody` | Sender country; normal `chaosx_alien_recovery_custody_recipient_id`, matching chain-local `chaosx_alien_recovery_custody_recipient` target, recipient's giver-specific consent flag | Temporary `chaosx_alien_recovery_custody_applied`, `chaosx_alien_recovery_core_moved`, `chaosx_alien_recovery_fragments_moved`, all zero by default; atomically moves the sender's core and fragments, preserves recipient material and roles, consumes consent, clears selected ID |
| `chaosx_alien_recovery_ledger_destroy_physical_custody` | Valid independent country holding consistent physical material; no selection input | Same temporary outputs; retires only that country's core and fragment slots permanently; preserves learned knowledge and historical reward records |
| `chaosx_alien_recovery_ledger_cleanup_invalid_targets` | Any scope | Retires invalid physical targets, releases abandoned fragments, preserves the historical winner and claimed receipts; projects six rows without scanning countries |
| `chaosx_alien_recovery_ledger_refresh_country_fragments` | Country | Rebuilds slot flags, roles, `chaosx_alien_recovery_ledger_fragment_count` and `chaosx_nr25_fragment_count` from persistent targets |

The transfer preflight rejects self-transfer, war between sender and recipient, missing or mismatched selection, absent giver-specific consent, invalid country institutions, and inconsistent sender-owned fragment receipts.
Normal recipient IDs are mandatory because chain-local targets do not persist as selection authority across unrelated GUI or decision refreshes.
The caller must resolve its stored choice into the chain-local target immediately before the transaction.
The caller owns route access, recipient preparedness, payments, cooldowns, Dependence movement, opinion changes, confirmation text, and player/AI policy selection.
It must not publish a paid-success outcome without a positive transaction receipt.

Example of the internal call after caller preflight and explicit recipient permission:

```text
# In the selected recipient scope, whose PREV is the giver:
save_event_target_as = chaosx_alien_recovery_custody_recipient
# In the giver scope, store the selected recipient's numeric country ID:
set_variable = { chaosx_alien_recovery_custody_recipient_id = my_selected_recipient_id }
chaosx_alien_recovery_ledger_transfer_physical_custody = yes
if = {
	limit = { check_variable = { var = chaosx_alien_recovery_custody_applied value = constant:chaosx_nr25_value.one compare = equals } }
	# Caller-owned payment and policy consequences belong here.
}
```

Do not call private `assign_fragment_slot_<1..6>` helpers for field acquisition.
They intentionally support the validated transfer transaction and can replace an old owner.
Public acquisition cannot steal a living owner's slot or re-create a destroyed slot.
Callbacks must not increment `chaosx_nr25_fragment_count` after acquisition because the ledger already rebuilds it.

## Presentation and assets

The ledger itself owns no additional sprite or window.
The Event 025 Board uses existing sector and fragment supporting icons registered in `interface/025_alien_technology_in_antarctica.gfx`.
Historical result displays must use per-event receipts; current material displays must use physical-custody targets and their rebuilt projections.
Do not expose exact foreign fragment holdings without the Board's intelligence/privacy gate.

## Evidence and limits

`.tools/test_event025_custody.py` executes the selected source helpers for all six slots, rejected transfers, consent consumption, retained recipient fragments, destruction, abandonment, projections, and historical separation.
It is a limited source interpreter, not engine scheduling, rendering, multiplayer, or save/reload evidence.
The current policy caller still needs recipient permission UI, actual transfer/destruction dispatch, validated resource commitments, Dependence consequences, and independent decision/probability review.
The reward bridge and owner API pool/filter contract are separately pending review; physical-custody tests do not validate them.

## Future work

Finish the accepted policy callers before treating either custody helper as a complete playable route.
Integrate Event 036 material holders through a bounded direct seam instead of expanding the active pulse into a whole-world scan.
No additional country, portrait, formation, unrelated equipment, or technology copy is authorized by this ledger.
