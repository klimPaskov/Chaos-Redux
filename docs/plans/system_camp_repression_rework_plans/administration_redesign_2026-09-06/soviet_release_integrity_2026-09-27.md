# Soviet paid prisoner-release integrity

Status: implemented and source-tested; native decision click, refund timing and AI eligibility remain unproved.
Acceptance basis: the accepted finite-custody administration contract requires a paid order to release measured living prisoners before it grants policy relief. On 2026-10-03 the user explicitly chose one national quota, famine, grievance and reform settlement after the first successful release; later paid orders still release survivors without repeating that settlement, as recorded in `accepted_implementation.md`.
Disposition: the one-time settlement design is promoted into [Part 3's Soviet prisoner-release section](../../../specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_3_germany_japan_soviet_deepening.md) on the user's 2026-10-03 basis; the source implementation and native limits remain tracked here.

## Failure and correction

The retained `sov_release_prisoners_for_military_service` decision previously became available when any operating Gulag had positive aggregate custody, even if its aligned custody rows were inconsistent or another affected Gulag could not release anyone.
The shared `camp_admin_release_detainees` correctly rejects such a row, but the Soviet effect still reduced forced-work quotas, famine pressure and grievances and added reform credit after the native 45-Political-Power payment.

The package-owned `camp_rework_soviet_service_release_ready` trigger now requires at least one living reconciled SOV-responsible operating Gulag and requires every affected operating Gulag to have reconciled rows.
The direct decision uses that predicate inside a player-facing custody-records requirement tooltip; execution repeats it after the native payment.
The release loop visits only positive reconciled SOV-responsible sites. The national relief effects run only when the recorded aggregate actual release is positive and the one-time national policy flag has not yet been set; a later positive release still consumes custody rows, records survivors and pays the decision cost without a second national settlement.
It closes census intake at a site only when that site actually releases survivors, so an externally exhausted cohort does not leave a false release consequence after the national cost is refunded.
If execution finds no accepted release, the effect returns the existing 45-Political-Power quote and grants no quota, famine, grievance or reform relief.
The shared action router records its country-action cooldown only after a positive Soviet release receipt; all other country actions retain their prior routing.
The action adds no army manpower, creates no civilian population and never restores a death.
The present scripted GUI does not bind the old four-slot Ledger control for this action, so this patch does not reactivate or redesign that obsolete entry.

## Source scenarios and balance

The [parsed production-source result](soviet_release_integrity_source_results.json) covers five cases with a mocked native PP debit.
With two operating Gulags holding 10,000 each but only 9,000 in the second site's living row, the decision is unavailable and a forced stale routed effect refunds 45 PP without a release, policy relief, census-intake closure or country-action cooldown.
With aligned 10,000 and 5,000 cohorts, the routed order pays 45 PP once, releases exactly 15,000 survivors, closes intake at those sites, sets one country-action cooldown, leaves both physical state populations unchanged and applies one national relief set.
When the population headroom is exhausted after the availability check, the effect records zero released and returns 45 PP without policy relief or a new census-intake closure flag; the ordinary capacity refresh may separately reconcile already-observed outside attrition.
The existing foundation and major-country suites still pass 34 and 15 parsed-source scenarios respectively.
These are mocked engine primitives, not an observed native click or a live save receipt.

The existing `GFX_decision_sov_prisoner_transfer` icon and decision category remain the consumers; this change requires no new sprite or DDS.
The current requirement key is `sov_release_prisoners_for_military_service_rows_tt` in the existing UTF-8-BOM English country-kit file. The description uses `GetSovServiceReleaseConsequence` to show the first-settlement consequences before the flag and the survivor-only consequence afterward; neither branch implies a direct NKVD-authority reduction.
The scoped workbook audit found no event-catalog row about this prisoner-release decision or its relief outcome. The Soviet-collapse, liberation-cluster and republic-release rows describe different surfaces, so the workbook and its generated CSV exports remain unchanged.
The earlier scoped read-only localisation auditor found the title, description and row-requirement keys unique and accurate before the user-approved one-time policy text was added; the first/repeat scripted-localisation branches require a fresh scoped audit. The cooldown flag already has a player-facing key, the 45-PP native cost has no conflicting printed quote, and the archived MCP result remains partial without tooltip pixels.
The tuning source remains `camp_rework_cost.review_pp = 45`; no new cost, reward or casualty target was introduced.
The national policy package is quota −7, famine −12, grievance −7 and reform +6 after the first positive release, with a 150-day decision cooldown. A fourth source sensitivity measures that full first-settlement package after exactly one surviving prisoner is released for 45 PP; the user accepted one-time relief rather than an unapproved minimum cohort. The order releases every currently valid positive Gulag row and closes each accepted site's future census intake. A fifth sensitivity declares a later eligible new Gulag and native re-enable: a second one-person release spends another 45 PP and records that survivor, while reform remains +6 and every national pressure receives zero additional policy delta. The declared new-site setup and timer are not proven in the engine.

## Engine references and remaining proof

Direct installed HOI4 MCP 3.6.0 `reference_context`, three targeted `reference_search` calls, four `reference_read` calls and `source_lookup` all returned successfully for this decision surface; the context reports no omitted or missing required sources. The exact returned section text and source-linked vanilla lookup are archived with a [hash manifest](mcp/soviet_release_references_3_6_0_2026-09-27/manifest.json).
The offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 284–336, revision `7713b9f1ad43a16c2d85d25b307d261fcc9e60292b4e164c335c03816535e4d8`, documents native Political Power cost and the distinction from custom cost.
The offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` lines 343–345, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, documents `if`, hidden triggers and custom requirement tooltips.
Installed `common/decisions/_documentation.md` lines 1–30, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, defines the per-frame `available` check; installed `documentation/triggers_documentation.md` lines 1052–1061, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, defines `all_of_scopes` over an array; installed `documentation/effects_documentation.md` lines 1854–1862, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, confirms the country-scoped PP refund effect.
Installed vanilla `common/decisions/_generic_decisions.txt` lines 143–161, SHA-256 `83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187`, provides a native-cost decision with an `available` gate; live `source_lookup` resolved that `dismantle_maginot` definition at revision `6ced07b1f3f0faeefb0785819f5ae15b548ba62a469d3346d1500bfb3f348700`. It does not prove refund ordering.
The offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` lines 891–906, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, defines country flags as Boolean state without an effect tooltip; live `reference_read` retrieved this section. Installed `documentation/effects_documentation.md` lines 6730–6737 (`2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`) confirms country scope for `set_country_flag`. Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` lines 656–705, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, was retrieved with `reference_read` for topmost matching `defined_text`; installed vanilla `common/scripted_localisation/00_war_propaganda_scripted_loc.txt` lines 12–35 (SHA-256 `d8d4bd0aef2e3ae2dbc1603f62ac5b833c9386001ad8bad093c3e574b7ef3f6d`) supplies the corresponding country-scope precedent.
The [policy-reference archive](mcp/soviet_release_policy_references_3_6_0_2026-10-03/manifest.json) retains the direct HOI4 MCP context, search and read wrappers with source paths, revisions and no reported omitted required source kind. The installed game has no dedicated scripted-localisation documentation file in its `documentation/` directory, so the offline wiki and installed vanilla script are the relevant precedents for that surface.

The [direct installed decision inspection](mcp/soviet_release_decision_3_6_0_2026-09-27/review.md) returned `DECISION_ANALYZED_PARTIAL`: it resolved the 45-PP native cost and raw Soviet AI score 40, but could not bind the `any_of_scopes`/`all_of_scopes` custody arrays or native click. The matched score-only probability comparison remains a pending specialist result.
The native `days_re_enable` timer may still start after a stale paid click even when the effect refunds PP; this is not modeled by the source interpreter and remains a consumer-evidence limit.

## Future work

If the live engine exposes a repeatable stale-click cooldown despite the refund, use a supported package-owned availability or decision-timer remedy proven by an exact vanilla precedent before changing this route.
If a future Soviet program needs proportional relief by survivor count, define a separate accepted tuning rule; the current order's nationwide settlement is explicitly one-time.
