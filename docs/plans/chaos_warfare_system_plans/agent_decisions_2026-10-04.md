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

## 4. Both containment maxima are bound in the containment scripted localisation

Disposition: `implemented`.
`GetDiseaseContainmentBoardMaximum` and `GetBlackPlagueTerminalMaximum` both live in `common/scripted_localisation/biowarfare_disease_containment_scripted_localisation.txt`, even though the royal-campaign maximum is an Event 020 constant.
Basis: the containment localisation file is the only consumer of either maximum, the getter only reads the constant, and placing it beside its consumer avoids adding a second owner's localisation surface for one number.
The Event 020 constant category itself is untouched.

## 5. The Warfare help page teaches the loop in five named sections

Disposition: `implemented`.
`chaosx.help.body.warfare` keeps its existing Chaos Warfare, Chemical Warfare, Biological Warfare and Contamination sections and gains Authorization, Raids, Protection and Condemnation between them.
Every number comes from source: the policy price is `cbrn_doctrine_policy_command_power_cost.policy_change` (5) and the interval is `cbrn_doctrine_timing.policy_reassessment_days` (90); the two categories are `chemical_raids` and `biological_raids` in `common/raids/categories/chaosx_raid_categories.txt`, both with `intel_source = army`; the raid requirements are the documented native source, division and target-state behaviour recorded in `common/raids/cbrn_chemical_land_raids.txt`; the Condemnation band is `condemnation_threshold.total_cap` (1000) with `cost_multiplier_maximum` (3) and the inspection burden `inspection_consumer_goods_minimum` to `_maximum` (5% to 15%) over `condemnation_duration_days.inspection` (180) days.
Only that one key changed in the shared file; its mixed line endings were restored byte-for-byte after an editor normalised them.

## 6. CXT facility placement treats the supply requirement as the cause

Disposition: `implemented`.
The candidate search now requires a borrowed foreign state to neighbour CXT-controlled territory, and the construction pass prefers a supply-connected owned state before any other owned state.
Basis: every special-project facility declares `need_supply`, the installed facility documentation requires a supply-connected province to start construction, and a randomly grabbed foreign state that touches no CXT territory can never join CXT's network, which matches every tested candidate failing the native gate.
No gate is bypassed, no DLC lock is claimed, the retry bound is unchanged and rejected transfers still restore owner and controller.
Supply connectivity is expressed as capital, supply node or railway in the new `chaosx_test_country_state_is_supply_connected` trigger, because the installed trigger documentation exposes no state-level "is on the supply network" check; the native `can_construct_building` remains the decider, so the trigger only orders candidates.

The harness documentation update is recorded in the CXT audit note rather than in `docs/testing/chaosx_test_country.md`.
Basis: that file currently holds another owner's uncommitted Event 029 paragraph together with a whole-file line-ending rewrite, and the shared-tree rules forbid reformatting another owner's file.

## 7. The Event 020 board gets one spacing rhythm, and its evidence is kept as one record

Disposition: `implemented`.
The pre-fix inspect reported exactly one genuine layout finding, `GUI_INCONSISTENT_SPACING` with sibling vertical gaps from 3px to 16px. I gave the 282px window 14px top and bottom padding and a uniform 9px gap between all six rows, and centred the summary panel's labels at y=21 inside its 70px height.
Basis: the window height, the six row heights and five gaps determine the padding exactly, so a uniform 9px gap with symmetric 14px padding is the only even rhythm that fits without resizing a row or the window; nothing was resized.
The repeated 20px margin and 480px content width became named constants, and the five meter band offsets became named constants beside the existing segment-width constant, which is documented as matching the 96x27 fill sprite.

The fourteen `GUI_ACCIDENTAL_CLIPPING` and `GUI_INVALID_SIZE` warnings are hidden-element `0x0` reports and the one `GUI_UNRESOLVED_DYNAMIC_VALUE` is the offline renderer not evaluating scripted localisation.
Basis: every element the fixture shows is sized and placed normally in the same result, so the reports are a renderer limit for hidden elements rather than a defect; no visible element's finding was dismissed.
Both limits are recorded rather than waved away, and category-level visibility stays a source review because the fixture cannot set the country and global flags the gate reads.

The round's evidence is appended to the existing recovery README instead of a new report folder, and the stale 144 KB schema dump in that folder was dropped.
Basis: the task brief forbids new verification machinery, and the dump has no value now that the shared route returns results.

## 8. The eighteen legacy chemical-tank companies are kept as a recorded exception

Disposition: `implemented`.
The accepted amendment removes them, but they stay in source with a recorded accepted compatibility exception rather than being deleted.
Basis: their identifiers are entries in the ordered `common/synchronized_dynamic_tokens/chaosx_tokens.txt` list, whose own header states that keeping the identifiers synchronized prevents multiplayer out-of-sync token allocation; removing eighteen entries from an order-sensitive shared list would shift every later identifier for every package that reads it, in a working tree other engineers are using right now.
Unreachability is proven rather than assumed: each definition carries `active = no`, which the offline unit-modding reference defines as usable only through an explicit technology unlock; no technology anywhere declares `enable_subunits` for any of the eighteen; they appear in no AI template, no history order of battle and no CXT unlock; and the only script naming them, `common/scripted_triggers/chemical_tank_shell_triggers.txt`, is itself called from nowhere.
The three armored chassis roles stay intact and keep their technology unlock.
The basis and the exact condition for a later removal are written into the unit file header and the requirement ledger so the deviation cannot be mistaken for an oversight.

## 9. The three CBRN procurement factory commitments are accepted exceptions

Disposition: `implemented`.
`BF-CBRN-013` to `BF-CBRN-015` now record Rebuild Old Masks, Convert Mask Factories and Simplify Mask Filters as fixed native factory commitments with an accepted-exception status rather than converting them to sale-aware variants.
Basis: the accepted procurement adapter `docs/plans/026_black_friday_plans/2026-09-27_cbrn_protection_pp_support_adapter.md` states in its own terms that each action "retains its existing project duration, output, AI weight, and civilian-factory commitment", and its price table heads the factory column "Unchanged factory commitment", so the sale was accepted as applying to the two spendable components only.
`civilian_factory_use` is a static decision-modifier field that rejects a variable, so a discounted commitment would need duplicated ordinary and sale decision definitions, which that accepted adapter did not request for these three actions. Event 026's own `BF-CBRN-008` already carries a fixed one-factory commitment under the same reasoning.
Parity is verified rather than assumed: the visible tooltip values come from `GetCbrnValueReconditionMasksFactories`, `GetCbrnValueConvertIndustryFactories` and `GetCbrnValueSimplifyFiltersFactories`, which read `cbrn_protection_decision_cost.recondition_masks_factories` (1), `convert_industry_factories` (3) and `simplify_filters_factories` (2), the same values the three `civilian_factory_use` modifiers commit through their file-scoped mirrors, so the displayed price equals the deducted price.
Only the CBRN rows of the Event 026 registry were edited.
