# Event 014 Country-Package Post-Closure Remediation

Date: 2026-07-13

Requested audit-series filename date: 2026-07-12

Owner: `event014_focus_closure_planner`

Source audit: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_package_postclosure_reaudit_2026-07-12.md`

## Outcome

The two country-package P1 defects are patched. The parent also supplied authoritative scorer-scope evidence and four focus-audit findings while remediation was in progress. Those findings are included in the same bounded patch.

No asset, Event Details, localisation, spec, spreadsheet, or unrelated documentation file was changed. No commit was created.

## Mixed Pack-batch capacity closure

Added shared trigger:

- `cannibalism_wendigo_requested_pack_batch_fits_capacity`

The helper accepts temporary input `cannibalism_wendigo_requested_pack_batch`, computes current `cannibalism_wendigo_trained_pack_count` plus that batch, and requires the result to be less than or equal to live `cannibalism_wendigo_pack_capacity`.

It is used by both payment gates:

- `cannibalism_wendigo_can_pay_train_pack_cost` with `cannibalism_wendigo_decision.train_pack_batch`, which is two Packs.
- `cannibalism_wendigo_can_pay_enemy_death_receipt_muster` with `cannibalism_wendigo_enemy_death_receipt.muster_pack_batch`, which is one Pack.

Both click-time effects set the requested batch and defensively call the same helper before invoking `cannibalism_prepare_consumption_context`:

- `cannibalism_train_wendigo_pack_from_selected_anchor`
- `cannibalism_muster_wendigo_pack_from_enemy_death_receipt_effect`

The existing paid transaction order is preserved. Capacity, actor resources, and state validity are proven first. The exact population transaction runs next. Larder and stockpile payments, manpower credit, zero-start Pack creation, counter movement, and cooldowns happen only after the exact applied-population result is confirmed.

At every even live-capacity tier, a current count of capacity minus one accepts the one-Pack receipt batch and rejects the ordinary two-Pack batch. A rejected batch reaches neither the population helper nor the Larder payment.

## Bounded enemy receipt epochs

Added actor-owned registry:

- `cannibalism_wendigo_enemy_death_receipt_tracked_countries`

Added helpers:

- `cannibalism_clear_current_wendigo_enemy_death_receipt_epoch`
- `cannibalism_initialize_wendigo_enemy_receipt_epoch_for_target`
- `cannibalism_prune_wendigo_enemy_death_receipt_registry`
- `cannibalism_clear_wendigo_enemy_death_receipt_registry`
- `cannibalism_handle_wendigo_receipt_war_relation_added`

The first sample for every newly encountered or re-encountered enemy clears and initializes:

- `cannibalism_wendigo_enemy_casualties_snapshot`
- `cannibalism_wendigo_enemy_death_remainder`
- `cannibalism_wendigo_enemy_death_receipts_issued`

That first sample grants zero receipts. The country is then registered once in the actor-owned array.

Each Event 014 Wendigo pulse prunes the tracked registry before sampling current enemies. Tracked countries that no longer have a war relation with the Wendigo actor have all three epoch variables cleared and are omitted from the rebuilt registry. Current enemies not already registered receive a fresh snapshot instead of delta processing.

`on_war_relation_added` now invokes the narrow relation helper. If a peace and re-war occur before the next Event 014 pulse, the new war relation still clears and reinitializes the target before any later delta sample. The hook handles either ROOT/FROM orientation and does not iterate countries.

`cannibalism_clear_wendigo_enemy_death_receipt_registry` clears the target-owned epochs without closing unrelated focus unlocks. Receipt initialization uses it so completing Winter Victories after Open the Pack Musters cannot erase the muster unlock. `cannibalism_clear_wendigo_enemy_death_receipt_runtime` calls the registry helper, then clears the actor receipt pool, cooldown, and opening flags. The existing pre-lock cleanup calls the full runtime helper for route break, terminal lock, actor capitulation or annexation, and Event 014 global cleanup.

Continuous-war sampling retains the authored behavior:

- 50,000 positive new casualties per receipt.
- Two receipts maximum per enemy epoch.
- Five receipts maximum in the actor pool.
- A casualty-counter decrease resets the snapshot and remainder without minting a receipt. The issued count remains in place during the same continuous war, so a counter reset cannot bypass the per-enemy cap.
- Receipt sampling reads `casualties` and does not call the population or Deaths transaction.

## Scorer scope correction

The parent supplied the authoritative offline wiki contract after the country audit was written:

- scorer `target_trigger` default and ROOT are the initiating actor, with the candidate in FROM;
- scorer `score` default and THIS are the candidate, with the initiating actor in FROM;
- targeted decisions use actor ROOT/default and candidate FROM.

Added explicit scorer-target aliases:

- `cannibalism_unified_scorer_target_is_valid`
- `cannibalism_wendigo_scorer_target_is_valid`

Both aliases delegate to the existing actor-ROOT/candidate-FROM hard-validity wrappers. Both scorer `target_trigger` blocks now call those aliases. Score factor predicates remain candidate THIS/FROM actor. The scorer and trigger headers now document both contracts without reversing them.

All six unified targeted decision blocks and the Wendigo terminal-hunt and inherited-cell blocks retain their existing `_from_decision` validity calls.

## Paid-only Pack and AI reserve closure

`cannibalism_wendigo_focus_preserve_pack_contract` now sets `force_allow_recruiting = no` for `Wendigo Pack`. The template remains locked and available only through the two exact paid scripted musters.

Added shared AI trigger:

- `cannibalism_wendigo_ai_preserves_countdown_larder_after_cost`

The helper requires current Larder to cover the selected action's cost plus `cannibalism_wendigo_countdown.minimum_larder`. These AI paths now use it:

- terminal-hunt launch requires 1,200 Larder before its 400 payment;
- terminal-hunt press requires 1,000 before its 200 payment;
- ordinary two-Pack training requires 1,040 before its 240 payment;
- one-Pack receipt muster requires 1,000 before its 200 payment;
- inherited winter-cell activation requires 950 before its 150 payment.

Player availability and exact player costs are unchanged. The reserve gate applies to AI willingness so AI cannot strand the active countdown below its existing 800-Larder floor.

## Duplicate AI reward closure

`cannibalism_wendigo_focus_preserve_pack_contract` is called by two focuses. Its `template_prio` and `role_ratio` strategy additions are now guarded by permanent country flag `cannibalism_wendigo_pack_contract_ai_applied`, making the shared reward idempotent.

The pre-lock score consumer can also be called by three focus milestones. Added:

- `cannibalism_wendigo_apply_new_scored_enemy_priority`
- actor-owned array `cannibalism_wendigo_prelock_scored_priority_targets`

Each valid pre-lock target receives one score-banded strategy package. Later focus calls can add newly valid enemies but cannot stack another identical package on a previously prioritized target. The terminal helper remains a separate one-shot post-lock escalation and applies the terminal band once when the pulse locks the transformation.

## Files changed

- `common/decisions/014_cannibalism_wendigo_decisions.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `common/scorers/country/014_cannibalism_target_scorers.txt`
- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt`
- `common/scripted_effects/014_cannibalism_target_scoring_effects.txt`
- `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt`
- `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt`
- `common/scripted_triggers/014_cannibalism_focus_closure_triggers.txt`
- `common/scripted_triggers/014_cannibalism_target_scoring_triggers.txt`
- `common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt`
- this handoff

## Validation evidence

- The shared batch helper is called from both payment gates and both click-time effects. In both effects, the capacity recheck precedes the population transaction and Pack creation.
- The receipt muster still requests `100 * 1,000 = 100,000` people, requires `cannibalism_population_loss_applied` to equal that request, then pays one receipt, 200 Larder, 500 infantry equipment, and 100 support equipment before adding 50,000 manpower and one zero-start Pack.
- Both Pack callers still use `cannibalism_spawn_empty_wendigo_pack_batch`, whose equipment and manpower start factors remain zero. The ordinary caller passes two and the receipt caller passes one.
- The tracked registry has one bounded add path, one pulse rebuild, and one full shutdown clear. Shutdown clears all three target-owned epoch variables before clearing actor state.
- No `every_country`, `random_country`, daily, weekly, or monthly scan was added. Receipt initialization and sampling retain `every_enemy_country`; inactive cleanup iterates only the tracked actor registry.
- Both scorer target-trigger call sites use the actor-root aliases. All 16 targeted-decision validity references remain on the actor-ROOT/candidate-FROM wrappers.
- Five AI action paths call the shared post-payment Larder reserve helper.
- The Pack queue has no `force_allow_recruiting = yes` call in the preserved contract.

The code was not represented as having been executed in-game by this subagent. The parent-requested country, focus, and decision re-audits should re-read the final files and exercise the runtime sequences.

## Remaining risks and simplifications

No gameplay simplification or fallback was introduced.

The documented effects database provides `add_ai_strategy` but no corresponding scripted removal effect. The pre-lock target registry therefore prevents duplicate additions and permits later discovery of new enemies, but it does not rewrite an already applied target's band if that target's score changes before lock. The post-lock terminal band is a separate one-time escalation. This bounded behavior should be checked in the final focus/AI re-audit.

The engine has no `on_war_relation_removed` hook in the current official on-action documentation. Inactive epochs are cleared by the next bounded Event 014 pulse. A relation-added hook force-resets the epoch before any re-war sampling, including the edge case where peace and re-war occur between pulses.

No skill was created or updated. Skills used were `chaos-redux-events`, `hoi4-decisions-missions`, and `chaos-redux-subagents`.
