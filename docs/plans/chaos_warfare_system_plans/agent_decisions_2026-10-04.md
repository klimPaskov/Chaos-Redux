# CBRN workstream agent decisions - 2026-10-04

Disposition: `accepted and queued` or `implemented` per entry, as stated.
Acceptance basis for every entry: the user transferred this workstream with full design authority and asked that the implementing agent choose the recommended, spec-consistent option itself and record it here.
The controlling accepted design is `../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` with the corrections folder beside it.

## 1. Biological sabotage AI target gate calls the actor contract directly

Disposition: `implemented`.
`bio_sabotage_ai_may_target_state` now calls `ROOT = { bio_sabotage_actor_relationship_with_from_is_valid = yes }` instead of the raid-target wrapper `bio_sabotage_raid_target_from_is_valid`.
Basis: the installed `common/raids/_documentation.md` names `FROM` and `var:target_state` only inside the raid's own `ai_will_do` (lines 66-69), `show_target`, `available`, `launchable` and `launchable_from` blocks (lines 100-126).
The AI predicate already runs inside the raid's `var:target_state` block, so the wrapper would re-read `var:target_state` after a nested `ROOT = { ... }` country entry, where the documentation gives no guarantee.
No restriction is lost: the same predicate checks the selected state's own physical profile through `bio_sabotage_common_target_state`, rejects friendly owners, and the engine enumerates only the victim's states for AI selection, while the human show/prepare/launch gates keep the full wrapper with its `is_controlled_by = FROM` check.
Evidence: `node docs/testing/2026-10-04_bio_sabotage_scope_source_tests.js` returns 106/106 after the change; the recorded source identity for `biological_sabotage_triggers.txt` moves to `6aa9f022c49579f296f0c5921ed4130d83b3f54b8a7fd8e733cf35d11f679500`.

## 2. The temporary CXT facility trace helper is committed, not deleted

Disposition: `implemented`.
`common/scripted_effects/chaosx_test_country_facility_diagnostics.txt` is published so that `HEAD` holds both the helper and the caller another owner already committed in `eb08e1dde`.
Basis: deleting the helper alone would leave every checkout of `HEAD` calling an unknown effect, and CLAUDE.md requires temporary debug code to be removed only once the issue it exposes is resolved.
The helper stays read-only, runs only under `has_country_flag = chaosx_test_country_setup_trace_active`, and its file header states the removal condition.

## 3. Quarantine reconciliation is two bounded player actions, with write-off as the terminator

Disposition: `implemented`.
`cbrn_occupied_transaction_recovery_pending` and `cbrn_export_native_mismatch_@FROM` now have a player-triggered route that closes them.
Three choices inside that route were mine.

The route is two decisions rather than one, because the occupied block is country-scoped while the export block is per recipient.
A single non-targeted decision cannot reach a recipient as `FROM`, and a single targeted decision would make the occupied audit depend on an unrelated export partner existing.
Both are player-triggered, both are bounded, and neither adds a periodic or world-wide hook, which is what the accepted contract actually requires.

The audit retries the measured native return once and writes off only what the engine refuses a second time.
Basis: the accepted contract forbids blindly clearing quarantine, refunding an unknown delta and reversing retained positive coverage, but a route that can only retry would leave the decision family dead whenever the native delta is permanently unaccountable.
A write-off credits nothing to the stockpile and never touches a delivered total, so an unverified movement cannot read as a delivery, and the counts are stored and shown to the player.

The unrecorded fee is written off instead of credited a second time.
Basis: its first credit attempt already reported failure, so a retry cannot be proven not to double-credit, and the accepted contract requires that no duplicate refund is possible.
The amount is recorded in `cbrn_occupied_written_off_fee_total` and reported in the decision description rather than silently discarded.

The occupied state pass uses `every_state` limited to receipts this donor owns and marked for recovery, so a receipt in a state the donor no longer controls is also closed.
Basis: one player click is neither periodic nor a hook, and the alternative would strand any receipt whose state changed hands while blocked.
