# Event 006 DM-16 recognition-campaign cost-localisation handoff

Date: 2026-08-14

Scope: One bounded cost-text selector correction for the shared DM-16 recognition decision.

## Disposition

`independence_wave_coordinate_recognition_campaign` now uses the existing factory-aware diplomatic cost localisation.

No new cost, effect, AI, admission, Join, asset, or workbook behavior was designed.

## Exact change

File: `common/decisions/006_independence_wave_decisions.txt:882`.

Identifier: `independence_wave_coordinate_recognition_campaign` (DM-16).

Before: `custom_cost_text = independence_wave_cost_diplomatic_standard`.

After: `custom_cost_text = independence_wave_cost_diplomatic_standard_factory`.

The decision already used `can_pay_independence_wave_diplomatic_standard_cost` for availability and `custom_cost_trigger`.

The decision already reserved `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT` through `civilian_factory_use`.

The selector change therefore makes the card disclose the factory commitment already present in the source.

## Localisation reuse

The selector reuses the existing triplet in `localisation/english/006_independence_wave_decisions_l_english.yml`:

- `independence_wave_cost_diplomatic_standard_factory`.
- `independence_wave_cost_diplomatic_standard_factory_tooltip`.
- `independence_wave_cost_diplomatic_standard_factory_blocked`.

The triplet displays standard Command Power, convoy-or-train capacity, and the dynamic `independence_wave_decision_cost.civilian_factory_light` value.

No localisation file was changed in this tranche.

## DM-16 lifecycle notes

DM-16 belongs to the Recognition category and is a shared timed mission for a recognized Event 006 network or league member.

Its target is a capital whose owner passes the existing network-target helper and has lower recognition than the applicant.

The target-root gate requires a recognized-or-later applicant, network membership, and no active diplomatic action.

The decision uses the existing long recognition duration and standard re-enable cooldown.

Completion pays the existing diplomatic-standard helper.

Removal raises recognition and network standing for both sides and applies the existing league ledger deltas.

Cancellation requires the applicant to remain a network member and the target owner to remain an active Event 006 country.

The existing high AI weight and target legality checks are unchanged.

The one-factory commitment remains light and is not altered by this patch.

## Safety and boundaries

This is a player-facing disclosure fix for a cost already applied by the source.

It does not change the diplomatic trigger, factory modifier, duration, success effect, cancellation cleanup, AI, package admission, deterministic Join, portraits, flags, or workbook.

DM-42 is not touched by this change and remains outside this handoff.

## Probability evidence

A prior DM-16-only `hoi4.probability_inspect` pass for `common/decisions/006_independence_wave_decisions.txt` used the `decision_ai_will_do` adapter and returned `PROBABILITY_SOURCE_INSPECTED`.

Receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9bf7dfac09026fe7f23e15f120ae2fd61ce962aeca4f7fcecbccef59c5267fc/d7f46b95ce9adfdb0c069a63f9f3cf1ec4218a1699886369c42fa77f00b74d10/probability-inspect-8347179f8dce.json`.

The inspect saw source revision `7d379ab9956e5d7dbb8156f6191d1c3f5a3db6f567aedfc7542632eedfd53879`, source hash `8347179f8dce88637c2a819bdccd9564e82fce7b2432500c0b4ca88ec88efc54`, 10 candidates, 79 required inputs, zero unresolved items, and `poolComplete=false`.

No AI field changed, so no probability evaluate or before/after compare was run.

The incomplete pool limits quantitative AI claims and is recorded rather than treated as a balance result. The post-DM-62/DM-42 current-source receipt is recorded in `006_post_dm62_recognition_cost_disclosure_gap_audit_2026_08_14.md` and supersedes this earlier DM-16-only receipt for current-source provenance.

DM-16 uses the ordinary decision framework and does not introduce or modify a decision-owned scripted GUI, so no GUI rewrite was attempted.

## Validation

- Confirmed the DM-16 block retains the diplomatic-standard availability and cost trigger, factory-light modifier, long duration, standard cooldown, diplomatic payment helper, recognition/network success effects, cancellation gate, and high AI weight.
- Confirmed the DM-16 source contains exactly one factory-aware selector for this decision.
- Confirmed all three reused factory-aware localisation keys exist globally and reference `civilian_factory_light`.
- Confirmed the English localisation source remains UTF-8 BOM from the prior localisation patch.
- Ran focused `git diff --check` after isolating this selector change.

Live HOI4 execution, save/load, and runtime card rendering were skipped because this is a cost-text-only change and live consumer validation remains parent/user-owned.

## Remaining issues

The probability pool remains incomplete, and Event 006 whole-event admission remains governed by the current authority boundary.

DM-42 remains a separate surface and was intentionally not modified.
