# Remaining constant localisation repair

Disposition: implemented display bindings, with native visual and achievement semantics unresolved.

Parent acceptance: bounded repair of raw constant expressions in the three assigned English files, using the existing direct temporary-variable quote pattern.

## Changes

Replaced 15 expressions across 10 player-facing keys with 12 distinct constant-backed getters.
Three English files retain their original prose, formatting codes, texticons, numeric formatters, costs, and requirements.
Added common/scripted_localisation/cbrn_achievement_value_localisation.txt and biological_facility_recovery_value_localisation.txt.
Appended six getters to the existing 020_black_plague_shared_response_cost_localisation.txt family.
No gameplay, other-language text, workbook, CSV, index, or commit changes were made.

### localisation\english\cbrn_achievements_l_english.yml

Script owner: common\scripted_localisation\cbrn_achievement_value_localisation.txt

Changed player-facing keys:
- chaos_warfare_prepared_army_tooltip
- chaos_warfare_air_still_breathable_tooltip
- chaos_warfare_antidote_arrived_tooltip

| Constant | Getter | Value key | Current display |
| --- | --- | --- | --- |
| cbrn_achievement_threshold.high_military_protection | GetCBRNAchievementHighMilitaryProtectionQuote | cbrn_achievement_quote_high_military_protection_value | 75 |
| cbrn_achievement_threshold.strict_air_contribution_points | GetCBRNAchievementStrictAirContributionPointsQuote | cbrn_achievement_quote_strict_air_contribution_points_value | 3 |
| cbrn_achievement_threshold.low_nerve_civilian_deaths | GetCBRNAchievementLowNerveCivilianDeathsQuote | cbrn_achievement_quote_low_nerve_civilian_deaths_value | 1000 |
| cbrn_achievement_threshold.low_nerve_military_loss_fraction | GetCBRNAchievementLowNerveMilitaryLossFractionQuote | cbrn_achievement_quote_low_nerve_military_loss_fraction_value | 1% |

### localisation\english\biological_facility_recovery_raids_l_english.yml

Script owner: common\scripted_localisation\biological_facility_recovery_value_localisation.txt

Changed player-facing keys:
- bio_facility_capture_secure_limited_tt
- bio_facility_capture_destroy_limited_tt

| Constant | Getter | Value key | Current display |
| --- | --- | --- | --- |
| bio_facility_capture_payload.secure_limited_fraction | GetBioFacilityRecoverySecureLimitedFractionQuote | bio_facility_recovery_quote_secure_limited_fraction_value | 40% |
| bio_facility_capture_payload.destroy_limited_fraction | GetBioFacilityRecoveryDestroyLimitedFractionQuote | bio_facility_recovery_quote_destroy_limited_fraction_value | 50% |

### localisation\english\020_black_plague_response_l_english.yml

Script owner: common\scripted_localisation\020_black_plague_shared_response_cost_localisation.txt

Changed player-facing keys:
- black_plague_shared_armored_clearance_cost_tooltip
- black_plague_shared_start_last_response_hold_desc
- black_plague_shared_start_last_response_hold_cost_tooltip
- black_plague_shared_start_last_response_refuge_desc
- black_plague_shared_start_last_response_refuge_cost_tooltip

| Constant | Getter | Value key | Current display |
| --- | --- | --- | --- |
| black_plague_shared_cost.country_infantry_equipment | GetBlackPlague020ArmoredClearanceInfantryRequirementQuote | black_plague_020_quote_armored_clearance_infantry_requirement_value | 250 |
| black_plague_last_response.hold_stability_floor | GetBlackPlague020LastResponseHoldStabilityFloorQuote | black_plague_020_quote_last_response_hold_stability_floor_value | 20% |
| black_plague_last_response.hold_war_support_floor | GetBlackPlague020LastResponseHoldWarSupportFloorQuote | black_plague_020_quote_last_response_hold_war_support_floor_value | 20% |
| black_plague_last_response.refuge_stability_floor | GetBlackPlague020LastResponseRefugeStabilityFloorQuote | black_plague_020_quote_last_response_refuge_stability_floor_value | 20% |
| black_plague_last_response.refuge_war_support_floor | GetBlackPlague020LastResponseRefugeWarSupportFloorQuote | black_plague_020_quote_last_response_refuge_war_support_floor_value | 20% |
| black_plague_last_response.launch_days | GetBlackPlague020LastResponseLaunchDaysQuote | black_plague_020_quote_last_response_launch_days_value | 1 |

## Validation and limits

Ran python docs/testing/2026-10-08_remaining_constant_localisation/validate_bindings.py.
The portable baseline is the three immutable files under `docs/testing/2026-10-08_remaining_constant_localisation/before/`, with Git blob identities and raw SHA-256 values in `before_manifest.json`.
These are exact canonical Git blobs from commit `0819dc70d724badbe30b74128648976245d6b4ad`, not original checkout-newline bytes; the test does not depend on a moving `HEAD`.
The test reads the production getter assignments, resolves their actual script constants, checks formatter/value-key agreement, and checks unique getter, key, and temporary-variable ownership.
All twelve bindings resolved to current values: achievement protection 75, air contribution 3, civilian deaths 1000, nerve military loss 1%, secure fraction 40%, destroy fraction 50%, infantry requirement 250, all four final-response floors 20%, and launch duration 1 day.
Negative mutations reject a raw constant expression and an absent value key.
The protection getter deliberately renders 75, with the original surrounding percent sign retained in each achievement tooltip.
The test establishes source binding contracts, not engine evaluation or visible wrapping.

Source claims checked: biological_facility_capture_effects.txt limited callbacks select the same secure/destroy constants, shared_response_triggers.txt lines 483-490 require the constant infantry floor without spending it, terminal_response_triggers.txt hold/refuge gates use the four original floor constants, and shared_response_decisions.txt uses launch_days for days_remove.
Limited native raid tooltips occur under var:actor_country in biological_facility_recovery_raids.txt lines 243 and 429.
No numerical overpromise was established in these bounded source reads.
The initial suspicion about a discounted armored floor was disproven: the discounted helper belongs to Royal Node, and the actual armored gate uses the quoted constant.

MCP decision inspect first rejected the missing scenarios argument; retry with scenario localisation_binding_scope, actor GER, empty declared state returned DECISION_ANALYZED_PARTIAL, complete=false, unresolvedDefinitions=100, source revision 8a47e3aeda06c3dc7716e42a4743c8529d530bd2e00da469908e7e905984aec6.
Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68a026aa8f9334c00247b61b94ec11967155fc0b1530d87c00077d4b6ede0524/e18890d8e3e757d7093ee1253e8f185ce568f8ed865d353c2d1e172fe9fe3889/decision-11950c1f2b0fd4dccadc77b2.json
The inspect summary covers partial scenario/source evidence and does not establish native tooltip rendering.
No decision tooltip render, native raid tooltip render, or achievement tooltip render route is exposed; overflow and native display remain unverified.
Standalone Technology Tree Viewer is absent from the exposed tool inventory, a package gap; no technology tree was assigned.
No helper_expansion, job route, task negotiation, game launch, logs, or live-game validation was used.
MCP source_lookup for GetBlackPlagueLastResponseMissionDaysQuote returned zero indexed definitions despite its on-disk consumer; on-disk source review is retained rather than claiming indexed coverage.

## Reference evidence

Live reference_context(localisation, limit=4) included both installed game docs and offline wiki, omittedSources empty and missing empty.
Offline paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md lines 656-705, revision 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064, read through reference_read: trigger temporary variables remain set while displaying the selected localisation key, and implicit current scope is supported.
Installed documentation/triggers_documentation.md lines 7482-7488, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, read through reference_read: set_temp_variable supports any scope.
Vanilla precedent read directly: common/scripted_localisation/SEA_PRC_scripted_loc.txt lines 37-57 GetFiveYearPlanGoalCivFactoriesText computes a temporary variable in text.trigger; the patch follows the repository stronger pattern of a real YML value key.
Installed common/raids/_documentation.md Raid Outcomes section was read directly to confirm actor_effects uses raid-instance scope and requires var:actor_country for country consumers.

## Audit and prose preservation

Missing key list: none among new bindings and assigned consumers.
Duplicate key list: none in assigned files or the twelve new value keys across English localisation.
Scripted localisation issues repaired: fifteen unresolved direct constant reads.
Dynamic text opportunities completed: all twelve assigned constants have independent temporary bindings.
Encoding concerns: none in assigned English files; UTF-8 BOM retained.
Cross-surface mismatches: none established for assigned numerical constants; broader achievement native semantics remain unresolved.
Spreadsheet handoff: no catalog prose changed, so no workbook mirroring is needed for this numeric-binding-only repair.
Prose before/after by vagueness, bloat, obvious explanation, repetition, overcomplication, and style-rule repair: no prose rewrites were authorized by this bounded token-only task, and these categories remain unchanged.
Sourced quotations: no attributed quotation occurs in the ten assigned player-facing keys; none changed.
Dynamic tokens, names, formatting, literal percent suffixes, and numerical requirements were preserved except for the fifteen explicitly replaced unsupported reads.
No design-depth plan was created.
No implementation simplification was made; native visual proof and broader achievement mechanics remain explicit coverage gaps.

Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, and chaos-redux-native-raids for the limited callback scope review.
No skills created or updated.
