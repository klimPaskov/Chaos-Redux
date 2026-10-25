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
| `global.chaosx_alien_recovery_event036_recoverers` | Global array of countries | Every country that recorded an Event 036 recovery, added once by `chaosx_alien_recovery_ledger_resolve_event036`; read by `chaosx_nr25_enroll_event036_recoverers` |
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
Evolution IV can also retire an unowned slot: the wreck effects set the same permanent destroyed flag, or a permanent buried flag (`chaosx_alien_recovery_fragment_<N>_buried`), and the acquisition gate rejects both. Neither ever applies to an owned slot or to the hidden core sector.

| Effect | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `chaosx_alien_recovery_ledger_assign_fragment` | Country; temporary `chaosx_alien_recovery_fragment_id` and `chaosx_alien_recovery_fragment_role`, each an integer 1–6 | Temporary `chaosx_alien_recovery_fragment_assigned`, zero on rejection; acquires only an unowned, non-destroyed slot for a valid independent country |
| `chaosx_alien_recovery_ledger_transfer_physical_custody` | Sender country; normal `chaosx_alien_recovery_custody_recipient_id`, matching chain-local `chaosx_alien_recovery_custody_recipient` target, recipient's giver-specific consent flag | Temporary `chaosx_alien_recovery_custody_applied`, `chaosx_alien_recovery_core_moved`, `chaosx_alien_recovery_fragments_moved`, all zero by default; atomically moves the sender's core and fragments, preserves recipient material and roles, consumes consent, clears selected ID |
| `chaosx_alien_recovery_ledger_seize_fragment` | Seizing country; chain-local `chaosx_nr25_rival_target_scope` naming the expedition whose outpost fell; caller-initialized temporary `chaosx_alien_recovery_fragment_seized` and `chaosx_alien_recovery_fragment_assigned` (both zero) | Temporary `chaosx_alien_recovery_fragment_seized`, one when a slot moved, and `chaosx_alien_recovery_seized_slot`, the slot (caller-initialized to zero); forcibly moves only the target's lowest owned fragment slot to the seizer with its role, never the core; refreshes both countries and the projected arrays. Called only by the Evolution III seizure (`chaosx_nr25_take_seized_material`), which owns the seizure preconditions |
| `chaosx_alien_recovery_ledger_return_fragment` | Current holder; temporary `chaosx_alien_recovery_return_slot` (1–6), chain-local `chaosx_alien_recovery_return_recipient`; caller-initialized temporary `chaosx_alien_recovery_fragment_returned` and `chaosx_alien_recovery_fragment_assigned` (both zero) | Temporary `chaosx_alien_recovery_fragment_returned`, one when the slot moved. Moves that slot with its role only while the caller holds it and refreshes both countries and the projected arrays. The matched seizure settlement calls it once for each victim-specific claim through `chaosx_nr25_return_seized_fragments` |
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

`chaosx_nr25_return_seized_fragments` belongs to Event 025's restitution layer, not the shared reward bridge.
Its caller initializes `chaosx_nr25_returned_fragment_count` and `chaosx_alien_recovery_fragment_returned` to zero and resolves the victim into `chaosx_alien_recovery_return_recipient`.
It examines exactly six targeted claims and clears a claim only after a positive physical-ledger receipt.
An integer legacy single-slot receipt can preserve its recorded slot, but previously overwritten slots cannot be reconstructed and are never inferred from unrelated ownership.
Recorded crew detention is deducted at seizure and restored once at the matching settlement, separate from technology and physical fragment ownership.

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

`.tools/tests/test_event025_custody.py` executes the selected source helpers for all six slots, rejected transfers, consent consumption, retained recipient fragments, destruction, abandonment, projections, and historical separation.
It is a limited source interpreter, not engine scheduling, rendering, multiplayer, or save/reload evidence.
Destruction dispatch uses the physical ledger with support-equipment and stability costs, receipt-gated consequences, and a retired-material incident guard.
Transfer is dispatched by `chaosx_nr25_complete_custody_transfer` in the Event 025 holder effects after the recipient accepts the offer event; it pays, moves Dependence, and records diplomacy only on a positive transaction receipt.
The reward bridge is covered by source review only; physical-custody tests do not validate it.
`.tools/tests/test_event025_seizure_restitution.py` executes the production demand, seizure, matched acceptance/refusal and six-slot return helpers with conservative helper-local temporary cleanup.
Its twelve cases cover all six slot roles, multiple claims, partial returns, distinct victims, valid refusal, repeated answers, invalid or expired demands, third-party ownership, exact legacy slot migration and crew conservation.
Native flag duration, event delivery, opinions and threat effects remain observations in the harness, not engine execution.

## Future work

Event 036 holders join the holder watch through the Event 036 resolver once Event 025 has fired. A country that recovered Event 036 material earlier is kept in `global.chaosx_alien_recovery_event036_recoverers` and enrolled by `chaosx_nr25_enroll_event036_recoverers` when Event 025 opens and again when Evolution V activates; if Evolution V is already active it opens its aftermath and receives the holder notice (`chaosx.nr25.221`) at once. Both paths are idempotent. A recovery recorded in a save made before the registry existed is not in the array and is not enrolled retroactively.
No additional country, portrait, formation, unrelated equipment, or technology copy is authorized by this ledger.
