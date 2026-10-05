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
Basis: the task brief forbids new verification machinery.

Review correction, 2026-10-05: this section is accurate about the pre-change inspect and the spacing fix, and inaccurate about everything after it.
The "exactly one genuine layout finding" claim is sound but belongs only to the pre-change inspect result in the recovery folder, which is complete and whose negative checks genuinely report no visible overlap.
The shared route does not return results: all three 2026-10-04 attempts failed, three further reviewer attempts on 2026-10-05 were rejected as `Invalid tool arguments`, and no post-change inspect or render artifact of any resolution exists for this window.
Visual acceptance for the board is therefore `unresolved`, not `implemented`; the layout and visibility source change stays `implemented` on source review and arithmetic.

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

## 10. The assault-battalion audio lineage is settled by measurement, and no runtime file is replaced

Disposition: `implemented`.
The nine runtime WAVs are WAVE_FORMAT_IEEE_FLOAT mono 44,100 Hz 32-bit float, installed in `a48e000bf` on 2026-08-15 and unchanged since. The 2026-09-12 recovery derivatives are PCM signed 16-bit mono 44,100 Hz, with one duration match, eight mismatches and no byte-identical pair.
Basis: the headers and data sizes were read directly from each file, and the recovery set's own `derived_manifest.json` records `status: needs_user_review` with `runtime_wiring: parent-owned; not copied`, so the two sets are separate lineages rather than a broken conversion.
Commit `802006bf5` touched no WAV and not the sound asset; it retimed the entity's sound events against the rebuilt animations, which is what its message calls retimed sound consumers.
I replaced no runtime file: choosing which lineage ships is a listening decision, and the recovery set is still marked as needing the user's review.

Per-subunit selection audio is recorded as an engine limitation rather than implemented.
Basis: the engine's selection cues are the global `select_army`, `select_vehicle` and `select_tank` groups in the installed `sound/soundeffects.asset` at lines 1001, 1014 and 1024; no file under the installed `common/` references any of them, and entity audio attaches only to animation-state events, so the only route would replace every country's infantry selection voice.

The package manifest carries the same reconciliation under a new `audio_reconciliation` section and its status now describes the runtime that `802006bf5` produced. `docs/assets/` is listed in `.gitignore`, so that file is updated on disk and cannot be committed.
## 12. The broken cumulative gas-mask production read is removed rather than rewritten

Disposition: `implemented`.
`cbrn_chaos_warfare_adopt` stored `cbrn_doctrine_mask_production_baseline` from `total_equipment_produced_gas_mask_equipment`, and `cbrn_chaos_warfare_has_post_adoption_mask_production` compared the same read against that baseline.
The installed dynamic-variable documentation defines `total_equipment_produced_<equipment type>` across the equipment type enum only, and `gas_mask_equipment` is an archetype whose `type` is `support`, so the read resolved to zero and the predicate compared zero against zero and was always false. The archetype is also `is_buildable = no`, so no cumulative figure for it could exist.
Basis for removal rather than repair: the predicate has no caller in any script file, no accepted requirement asks for a cumulative-production proof, and it is a leftover of the retired reserve-and-formation establishment package whose neighbouring compatibility name is the only part Event 027 still reads.
The engine exposes no per-archetype cumulative production figure, and substituting a stockpile read would make the predicate's name untrue, because masks leave the stockpile when they are issued. The existing `cbrn_chaos_warfare_has_protective_foundation_reserve` already measures live masks for the cases that need a reserve test.
Removed: the baseline assignment in `common/scripted_effects/cbrn_doctrine_effects.txt`, the predicate in `common/scripted_triggers/cbrn_doctrine_triggers.txt`, and its entry in `common/scripted_triggers/cbrn_scripted_triggers.md`. No other behaviour changes.

## 13. The Event 020 GUI evidence route is recorded as unusable from this client, not retried further

Disposition: `blocked`.
Four `hoi4.gui_inspect` and `hoi4.gui_render` calls on `black_plague_response_category_window` were rejected with `Invalid tool arguments`, including the minimal inspect carrying only `windowName`, and including object, named-scenario and string forms of `scenario`.
Basis for stopping: `hoi4.source_lookup` answered normally in the same session at revision `fc979ea536b5` and resolved the window to `interface/020_black_plague_response.gui` lines 25 to 190, so the service is healthy and the rejection belongs to those two routes' argument contract as this client sees it.
The source change and its spacing fix stay accepted on source review; visual acceptance of the five scenarios remains a live-game item and no substitute evidence is manufactured.

## 14. The Contamination map mode reads the fallout record, and the Fallout sweep keeps its marker removal

Disposition: `implemented`.
`mapmode_state_has_nuclear_contamination` in `common/scripted_triggers/cbw_triggers.txt` now accepts either the `nuclear_fallout_state` marker or a live fallout record, through the new `mapmode_state_has_live_nuclear_fallout_record`: positive `nuclear_fallout_intensity` and a `nuclear_fallout_expiry_day` later than `global.num_days`.
Basis: the removal at `common/scripted_effects/fallout_consolidated_effects.txt` line 16916 is accepted Fallout design, not an ordering slip. `docs/specs/air_cleanliness_fallout_specs/specs/68_fallout_consequence_boundary.md` line 69 states that `fallout_manual_apply_state_aggregate_consequence` removes the ordinary marker after recording the intensity and expiry ledger so a native strike cannot leave a second daily nuclear Air contamination or Deaths source behind the fixed Fallout source, and `chaos_meter_apply_daily_contamination_and_outbreak_deaths` and `air_contamination_monthly_update` in `common/scripted_effects/chaos_meter_effects.txt` do read that marker for daily deaths and monthly contamination.
Asking the Fallout owner to keep the marker would reopen that double count, so the lead's proposed acceptance (marker still present when the effect returns) is replaced by the consumer-side reading, and the Fallout file is not edited.
The expiry check is required because `chaos_meter_apply_nuclear_fallout_to_state` never clears `nuclear_fallout_intensity` when fallout ends; for ordinary strikes the marker's own duration is the same expiry, so both readings agree. A swept state shows as nuclear for the `fallout_manual_aggregate.fallout_duration_days` window (540 days), and the tooltip's existing `Fallout intensity` line reads the same variable.
The chemical and disease branches were traced against their real writers and need no change: `cbrn_chemical_refresh_state_modifier` adds `chem_state_contamination` for the remaining contamination days after every chemical dispatch that sets `cbrn_chemical_contamination_expiry_day`, and `bio_lifecycle_refresh_detected_modifier_for_current_agent` adds the four `*_contaminated_state` modifiers while an agent is active and detected. Undetected outbreaks carry only `bio_ambiguous_health_pressure_state`, which the map mode deliberately does not show.
`docs/systems/state_map_modes.md` lists the record as a nuclear input.
Observation for other owners, not acted on: migration, famine and Event 014 triggers also read `nuclear_fallout_state`, so after the Fallout sweep they treat swept states as unirradiated; whether that is intended under Fallout is theirs to decide. The Deaths and Terror Activity parts of B037 belong to the Chaos Meter and Event 031 owners; the Deaths ledger stores people in `chaos_state_civilian_deaths_total`, which can exceed the variable range for a large Fallout state loss, but that is an unverified lead, not a finding.
The `hoi4.mechanic_test` route rejected a minimal call with `Invalid tool arguments`, so the trigger result is proven by source reading only; the colours themselves are a live-game check.

## 15. The Warfare help page reads its figures from the constants, and the line-ending churn is not content

Disposition: `implemented`.
The Authorization paragraph of `chaosx.help.body.warfare` now quotes the policy price and the reassessment period through the existing `GetCBRNPolicyChangeCostQuote` and `GetCBRNPolicyReassessmentDaysQuote`, and the Condemnation paragraph's first three sentences come from the new `GetCBRNHelpCondemnationSummary` in `common/scripted_localisation/cbrn_simplification_scripted_localisation.txt`, which returns `cbrn_help_condemnation_summary` in `localisation/english/cbrn_simplification_l_english.yml`.
The getter reads the scale from `condemnation_decay.minimum_total` and `condemnation_threshold.total_cap` (the clamp bounds of `condemnation_total`), the concealment ceiling as `condemnation_cost.cost_multiplier_base` plus `cost_multiplier_score_maximum` divided by `cost_multiplier_score_divisor` (the same formula `condemnation_prepare_cost_multiplier` applies to the occupation cover-up quotes), and the inspection period and consumer-goods band from `condemnation_duration_days.inspection` and `condemnation_cost.inspection_consumer_goods_minimum` and `_maximum`, the values the inspection decision tooltip already quotes. The page reads exactly as before: 5, 90, 0-1000, 3 times, 180 days and 5% to 15%.
Basis for editing the shared key now: the 333 "changed" lines in `localisation/english/chaosx_gui_l_english.yml` are line endings only. The committed blob mixes CRLF and LF lines and the working copy is all CRLF, so `git diff --ignore-cr-at-eol` is empty; no thread has uncommitted content there. The commit carries a blob built from HEAD with only line 58 replaced and its CRLF kept, so the line-ending state of every other line is untouched in both the commit and the working tree.
The paragraph body moved into a CBRN-owned key so later tuning text changes stay in this workstream's file; the shared key changed on one line.
Whether nested scripted localisation renders three levels deep in this text box is not separately proven, but the Chaos Meter tab of the same page already renders getters such as `GetChaosMeterValueColored` through the same `GetChaosxHelpBody` chain, so the route is the established one.

## 16. The facility placement rule is in the harness document as its own hunk

Disposition: `implemented`.
`docs/testing/chaosx_test_country.md` (Special facilities) now states that every special-project facility declares `need_supply`, that a borrowed foreign candidate must border territory CXT already controls, that owned, controlled, supply-connected states (capital, supply node or railway, through `chaosx_test_country_state_is_supply_connected`) are tried first, and that native `can_construct_building` still decides.
Basis: the file's other uncommitted content is one Event 029 paragraph about forty lines further down plus line-ending differences; the commit carries a blob built from HEAD with only the two new lines inserted, so the Event 029 owner's paragraph and the line endings stay uncommitted and untouched in the working tree. This supersedes the "recorded in the CXT audit note instead" clause of section 6.
Whether the supply rule makes construction succeed is still a live-game item: the October playtest never entered the harness.

## 17. The runtime assault-battalion sounds ship; the archived set stays archived

Disposition: `implemented`.
The nine 32-bit float runtime WAVs referenced by `sound/chaos_assault_battalion_sound.asset` remain the shipped set, and the 2026-09-12 16-bit recovery derivatives stay in the archive.
Basis: the runtime set is the one installed in `a48e000bf`, and `802006bf5` retimed the entity's sound events against the rebuilt animations with these files in place, so it is the set the current animations are timed to. The archived set's own `derived_manifest.json` says `needs_user_review` and `runtime_wiring: parent-owned; not copied`, and eight of its nine durations differ, so swapping it in would change cue lengths against animations it was never timed to. A listening preference cannot be formed by an agent, and replacing working runtime audio on a guess is the riskier option.
If the user later prefers the archived set after listening, all nine runtime files must be replaced together and the event timings rechecked against the new durations; that is a user-initiated change, not open work for this workstream.
