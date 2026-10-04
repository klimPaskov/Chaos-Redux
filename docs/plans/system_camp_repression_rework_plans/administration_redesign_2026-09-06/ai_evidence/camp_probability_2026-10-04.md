# Camp AI surfaces after the 2026-10-04 tranche: probability evidence

Disposition: `implemented` for the evidence below; no AI weight was found broken, so no weight changed.
Every decision result is `score_only` (raw willingness and eligibility); the adapter never gives a selection probability or timing for decisions.
Workspace `mod_chaos_redux_ea3b2d67c2c0`, adapter `decision_ai_will_do`, game `Operation Postern 1.19.2.0 (d245)`.

## Route status

- `hoi4_probability_compare`: worked for every request below.
- `hoi4_probability_inspect`: returned `INTERNAL_ERROR` with no artifact for `common/decisions/germany_mengele_decisions.txt` (candidates: the three imports) and, on the next pool, for `common/decisions/camp_administration_civil_decisions.txt` (the civil policy pair, explicit workspace id). It was not retried further; the compare results carry the same candidate discovery and eligibility traces.
- Baseline snapshots (pre-tranche bytes from `72aa7ba56^`) are in `baseline_sources_2026-10-04/` and are bound by `snapshotPath` plus SHA-256.

| Snapshot | SHA-256 |
| --- | --- |
| `germany_mengele_decisions_pre_tranche.txt` | `ade430ff243598ba98479dff02167c9cda39fea17c3b57548fef035e6b33e156` |
| `camp_repression_colonial_country_decisions_pre_tranche.txt` | `9126c384173fbc38d3cdd2018007bda71093845f0497a0060cfb108acad844ec` |
| `soviet_gulag_pre_tranche.txt` | `d8b5a6d6f4a91c6d37873fad4f87f674805ec95811054a0b88774cb9020557b2` |

## Retired Mengele foreign imports

Compare `probability-cb91b93419eb1f1c7a128a0a` (scenario hash `ec299a40…b118`), scenarios `GER_1941_PROGRAM_ACTIVE_PRE_ADMIN` and `GER_1943_PROGRAM_ACTIVE_ADMIN_INITIALIZED`.
Before: base `germany_mengele_decision_ai.silence_dissenting_file` (12) behind an availability `OR` with an unresolved `FROM` target.
After: `available = { always = no }` and base 0; all three candidates report `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` in both scenarios.
Result: zero eligibility for players and the AI, as decision 4 requires.

## USA supervised release and Italian security and closure

Compare `probability-acde43cc110f96fc6517d358` (scenario hash `088960db…c413`), candidates `usa_release_detainees_under_supervision`, `ita_raise_colonial_security_battalions`, `ita_close_desert_camps`; scenarios USA 1944-12-18 review before and after administration starts, ITA 1941 war, ITA 1943 with the postwar colonial reform focus.

- USA release: weight unchanged (`usa_reform` 90). Eligibility moved from inline resource checks and a cooldown flag to `camp_rework_usa_release_order_ready` (country eligible, political power covers the order, at least one releasable site); its array-backed site check stays unresolved in the adapter. The decision has no re-enable delay: each click releases one ready site and charges the political power again, which is the intended pace for closing the internment network once review is open.
- Italian security battalions: weight unchanged (`guard_allocation` 35); after administration starts the decision is ineligible (raw −35 versus the unresolved baseline), as the cutover intends.
- Italian closure: the new fascist reform-focus modifier (`italy_reform` 70) is present; with the focus flag it is still unresolved because government and the site-readiness array are not modelled. The exposure modifier is inactive in all four scenarios, as expected.
- Eight `UNRESOLVED_ANALYSIS_INTRODUCED` rows come from the new array-backed readiness helpers; they are analyzer coverage signals, not engine regressions.

## Civil policy pair (reform under sticky provenance)

The decision file did not change; the change is in its availability helpers (`camp_admin_country_sites_ready_for_reform`, commit `19b19be08`), which the origin country/civil source suite covers (ENG civil review beside an ambiguous host).
Weight record `probability-f5a36a2b317a32e013f1a1dc` with eligibility assumed: ENG 1941 at war authorize 1 / review 10; ENG 1946 at peace authorize 0 / review 10; USA 1943 at war authorize 1 / review unresolved (custody authority helper); USA 1945 authorize 1 / review 10.
Result: once records-incomplete hosts no longer block reform, the AI prefers review (10) over authorization (1), so countries close their camps instead of stalling.

## Soviet famine shortfall options

The same-scenario before/after compares are the 2026-10-03 results in `soviet_famine_shortfall_probability_2026-10-03.md` (warning and crisis pools, eleven cases).
The `invalid-GER` contradiction (probability 1 with eligibility false and weight 0) cannot occur in play: both events carry `trigger = { original_tag = SOV }`, and their only callers are the Soviet branch of `camp_repression_major_country_effects.txt` (lines about 2083 and 2104).
Option coverage for a Soviet recipient is complete: famine pressure above zero without relief underway gives the funded (`.a`) or shortfall (`.c`/`.shortfall`) option, relief underway gives its acknowledgement, and zero pressure without relief gives `famine_eased`; concealment (`.b`) and collapse (`.2.c`) are added only with a valid target.
Options keep the engine default weight 1, as the 2026-10-03 audit concluded.

## Source fix found during this pass

`uk_hold_raj_security_line` had `NOT = { is_italy_libya_repression_pool_state = yes }` in its cancel trigger, so the mission was cancelled on its first check (a Raj state is never a Libyan pool state). The stray line is removed; the remaining checks match `camp_rework_uk_security_line_requirements_met`. This affects only the pre-administration UK route.

## Limits

Every result is offline and score-only; AI selection frequency and timing are `needs_live_game`.
