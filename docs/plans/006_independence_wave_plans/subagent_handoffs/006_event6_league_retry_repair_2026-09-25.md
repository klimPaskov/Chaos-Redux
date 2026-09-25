# Event 006 League retry repair handoff — 2026-09-25

## Disposition

Status: **IMPLEMENTED, broader League dossier HOLD/PARTIAL**.

This parent-owned bounded repair gives the accepted `CongressFailed -> RegionalConferences` transition a caller through the existing DM45 `independence_wave_convene_founding_congress` decision.

It does not close the League lifecycle dossier or establish live-game behavior, quantitative balance, or whole-event completion.

## Design basis and implementation interpretation

The accepted state-machine diagram contains the retry transition, and the 2026-09-22 League reachability audit found that `independence_wave_reopen_regional_conferences` had no caller.

The repair uses the existing `independence_wave_decision_cooldown.standard` constant for the retry wait and records reconciled active-origin and network-member counts when congress preparation fails.

After the cooldown expires, an eligible network leader can use DM45 for another attempt only when the active-origin count or network-member count has grown beyond its failure-time snapshot and the ordinary living-origin and member minimums still hold.

The precise cooldown duration and either-count growth predicate are the parent implementation of the accepted cooldown/changed-condition gate; they are recorded as implementation interpretation, not as separately approved design text.

DM45 remains one-shot per country, retains its strategic cost and timeout, and keeps its prior AI score block unchanged.

## Files and identifiers changed

- `common/decisions/006_independence_wave_decisions.txt`: DM45 exposes the retry only when the retry trigger is satisfied, spends the existing strategic cost, invokes the reopen effect, and then follows the established founder, preparation, and charter path.
- `common/scripted_effects/006_independence_wave_effects.txt`: `independence_wave_fail_congress` reconciles registries and snapshots the active-origin/member counts before starting the timed global cooldown; `independence_wave_reopen_regional_conferences` checks the retry gate and clears the cooldown and snapshots on success.
- `common/scripted_triggers/006_independence_wave_triggers.txt`: `can_independence_wave_retry_congress` checks failed phase, cooldown expiry, network leadership, minimum counts, snapshot presence, and growth in at least one count.
- `localisation/english/006_independence_wave_decisions_l_english.yml`: DM45 description explains the failure retry conditions.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: current authority override records the bounded repair and its evidence limits.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`: resume authority records the repair and outstanding lifecycle work.
- `docs/plans/006_independence_wave_plans/006_event6_next_safe_tranche_improvement_addendum_2026_08_29.md`: League retry repair is dispositioned as implemented, while the broader dossier remains open.

## Validation evidence

- `.tools/audit_event6_flags.py --strict` passed with 102 registered tags, 102 complete flag families, and zero incomplete families.
- Parent source assertions confirmed the DM45 retry caller and ordinary caller, retained strategic cost, one-shot behavior and timeout failure path, centralized cooldown assignment, failure snapshots, growth gate, snapshot cleanup, and localized retry explanation.
- The exact DM45 AI weight block was compared with its pre-change version and is unchanged.
- English localisation retains its UTF-8 BOM and the edited description key appears once.
- `hoi4.probability_inspect` identified the post-change DM45 candidate pool as complete with one candidate and eight required inputs; source revision is `32100d3779ca1595916b9b9cada32f4dd3ae97d53aaf72ace19c63952153db7d` and source hash is `b2970b16f0dd076971b1b8b09a16b132fe206b5e6bf7eff38a835509306078d8`.
- Before and after `hoi4.probability_evaluate` runs used scenario set `LEAGUE_DM45_RETRY_BASELINE_2026_09_25` and the same scenarios, `LEAGUE_CONGRESS_FAILURE` and `LEAGUE_CONGRESS_RETRY_READY`; the before analysis was partial with four unresolved inputs, and the after analysis was partial with 17 unresolved inputs and zero diagnostics.
- `hoi4.probability_compare` compared the exact pre-change DM45 source snapshot with the current decision source using those same named scenarios; it returned `PROBABILITY_ANALYZED_PARTIAL`, two scenarios, two candidates, 17 unresolved inputs, zero diagnostics, and two comparison changes.
- Comparison JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3da784610140a55c9bda07b2cfb139ac224811d40a9d1b1a8122720c30e2c87/b688f9179b243f47b660db1bda0327533d3379e0caccf6e8079aea0178b47dbc/probability-466ba1dec12a60410c138b0d.json`.
- Comparison image artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16cf6b67b7ccba44cbcfcaf2dee6fc36df9b474db8bff081eedb175cf77d2078/65f9f189eaec08abb55474a1e73f44cb4ec43add3adf6109fc52fe77ba5423b2/probability-probability-466ba1dec12a60410c138b0d-comparison.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cadf9c42043110c49ea298aa6b384f80009b434f51c9734166456503971be7b9/294ca39caad810453926b5a0ba034f5443a41a2bcf95fc578958bf779a8b9b19/probability-probability-466ba1dec12a60410c138b0d-comparison.png`.

The probability adapter did not resolve the compound Clausewitz eligibility semantics, so these results are not a probability or balance PASS.

The dedicated `chaosx_ai_probability_auditor` route could not complete because the available subagent run hit the account usage limit; the parent performed the required MCP inspect, evaluation, and comparison directly, and keeps auditor review outstanding.

No HOI4 process, live scenario, save/load path, timer progression, or GUI rendering was run.

## Remaining League work

The wider named League scenario set still needs source/MCP lifecycle closure, typed probability coverage and auditor review, and user-owned live validation of formation, timers, event-target persistence, crisis and split paths, reunification, durable publication, and generation cleanup.

The possible need for a global congress-in-progress latch remains an unresolved concurrency question; this repair did not add one without evidence of a duplicate-congress failure.

Whole Event 006 remains **HOLD / PARTIAL**.
