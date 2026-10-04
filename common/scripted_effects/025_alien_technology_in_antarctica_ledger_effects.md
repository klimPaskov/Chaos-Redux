# Shared alien recovery ledger

Event 025 and Event 036 share reward provenance through the Event 016 external owner API.
Physical material is a separate ledger from researched technology and historical recovery receipts.
No custody transaction grants technology, changes the winner, or creates Event 016 history.

## Reward bridge contract

`chaosx_alien_recovery_ledger_resolve_event025` claims the single Event 025 owner, then calls `chaosx_grant_external_alien_recovery_reward` with a base reward allowed.
When the country already holds an Event 036 recovery in the flight, propulsion and weapons field, the request carries that overlap and the API excludes only the overlapping alien arms family; another missing base family, then an upgrade, then the Integration capstone follow.
`chaosx_alien_recovery_ledger_resolve_event036` keeps Event 036's own jet reward when there is no overlap.
When the same country's applied Event 025 reward is in the flight, propulsion and weapons field, it records an overlap and asks the API for an upgrade or the capstone only.

| Output | Kind | Meaning |
| --- | --- | --- |
| `chaosx_alien_recovery_event025_result`, `_field`, `_tier`, `_overlap` | Country variables | Historical Event 025 receipt, written once |
| `chaosx_alien_recovery_event025_reward_applied` / `_reward_pending` | Country flags | Whether the Event 025 reward was really granted; achievements and reports read these |
| `chaosx_alien_recovery_event036_*` | Country variables and flags | The matching Event 036 receipt |
| `chaosx_alien_recovery_result`, `_result_field`, `_result_tier`, `_result_overlap`, `_result_source_event`, `_reward_applied` | Country variables | Latest ledger call only; reset at the start of every call |
| `chaosx_alien_recovery_reward_applied_flag`, `chaosx_alien_recovery_reward_pending` | Country flags | Latest ledger call only; never use them as history |
| `chaosx_alien_recovery_*_output` | Temporary variables | Same-chain copies of the latest call, named apart from the country variables so they never shadow them |
| `chaosx_alien_recovery_overlap_conversion_used` | Country flag | Set only when an applied reward was converted because of an overlap |

Field codes come from `chaosx_nr25_alien_field` and match `chaosx_custom_technology_recovery`: aircraft 1 and propulsion 2 (both shown as flight control, propulsion and weapons), computation 3, spatial 4, temporal 5, biological 6, integrated 7.

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
Before calling either custody transaction, the caller must initialize all temporary custody outputs it reads afterward to zero.
Before public fragment acquisition, initialize `chaosx_alien_recovery_fragment_assigned` to zero in the calling effect frame.
The helper's own default assignments do not establish caller-owned storage.

Example of the internal call after caller preflight and explicit recipient permission:

```text
# In the selected recipient scope, whose PREV is the giver:
save_event_target_as = chaosx_alien_recovery_custody_recipient
# In the giver scope, store the selected recipient's numeric country ID:
set_variable = { chaosx_alien_recovery_custody_recipient_id = my_selected_recipient_id }
set_temp_variable = { chaosx_alien_recovery_custody_applied = constant:chaosx_nr25_value.zero }
set_temp_variable = { chaosx_alien_recovery_core_moved = constant:chaosx_nr25_value.zero }
set_temp_variable = { chaosx_alien_recovery_fragments_moved = constant:chaosx_nr25_value.zero }
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
Destruction dispatch uses the physical ledger with support-equipment and stability costs, receipt-gated consequences, and a retired-material incident guard.
Transfer still needs recipient permission UI, actual dispatch, validated route commitments, Dependence consequences, and independent decision/probability review.
The reward bridge is covered by source review only; physical-custody tests do not validate it.

## Future work

Finish the accepted policy callers before treating either custody helper as a complete playable route.
Integrate Event 036 material holders through a bounded direct seam instead of expanding the active pulse into a whole-world scan.
No additional country, portrait, formation, unrelated equipment, or technology copy is authorized by this ledger.
