# Cross-state occupation movement handoff

Disposition: implemented package infrastructure; this handoff's original single-wave Łódź caller description is superseded by `common/scripted_effects/camp_administration_occupation_effects.md` and `historical_benchmark_2026-09-25.md`. In-engine receipt, rollback, dated control and natural-play route availability remain unresolved.
Acceptance basis: the user-authorized camp/repression rework and parent instruction to preserve exact living cohort provenance and physical population conservation.
This handoff does not approve or claim a Hungarian 1944 caller.

## Implementation

`common/scripted_effects/camp_administration_occupation_effects.txt` owns country-aligned, append-only cohort rows and a same-chain, route-gated physical transfer transaction.
New registration appends one native row; the existing bounded monthly authority pass adopts older state records once.
Each row carries stable ID, root ID, original state, current host, original authority, profile, live survivors, own deaths, outside removals, releases, moved out, moved in and status.
The state retains aggregate `camp_occ_remaining_k` for custody admission, while row IDs distinguish two origins at the same destination.
The monthly country pass iterates active rows, causing any later measured death at the actual row host and exactly one existing shared Deaths projection, then updates that one row and the state aggregate.
Outside-loss reconciliation retires exposure across that host's authority rows without attributing deaths.
Capture, annexation and reform close the host's rows and release only living exposure in place; no dead people are restored.

`camp_occ_stage_transfer_destination` must be invoked in the actual destination state by a named caller and creates a regular event target for the effect chain.
`camp_occ_transfer_survivors_exact` must be invoked in the actual source state with `camp_occ_transfer_route_proven = 1`, a specific `camp_occ_transfer_row_id`, and a positive whole-person `camp_occ_transfer_requested_people`.
The helper rejects an absent destination, same-state target, wrong/currently inactive source authority or host, invalid row, unaligned arrays, insufficient finite row/state/physical headroom, invalid destination authority/control, and fractional amount before physical population changes.
It performs one measured source debit and one measured destination credit using the existing shared physical loss primitive and a package-owned positive credit with owner/controller manpower reconciliation.
It commits row and aggregate metadata only if both actual whole-person receipts match the request exactly.
On a mismatch, it measures physical inverse operations on both states and commits no metadata; an inverse mismatch raises `camp_occ_transfer_rollback_failed` on the source to stop another attempt.
Living movement creates no Deaths record and no casualty amount from a historical quota.
The source origin and authority persist in the appended destination row.

## Generic occupation-to-occupation caller contract and known route gap

The parent owns any adapter for the generic occupation-to-occupation helper and final route review.
Any adapter must prove the date, source row membership, actual source and destination control, destination ownership or custody authority, and an explicit route-sized living cohort; it must not select a protected group or convert a historical deportation number into deaths.
Do not call this helper from a whole-world on-action.
No adapter currently calls `camp_occ_transfer_survivors_exact`; that generic movement path remains inert, while the separate Łódź occupation-to-custody path has a dated caller in source.

[USHMM's account of the Holocaust in Hungary](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-in-hungary) documents a May 15–July 9, 1944 deportation movement from Hungary to Auschwitz, including joint German and Hungarian action, but does not prove a Clausewitz state-43 source cohort under German control or provide a survivor amount for this package.
The `hoi4.map_inspect` result for states 43 and 88 was `MAP_INSPECTED` at source revision `22824ec9592fad364d4764c73200982adc3419cdd29fdbe6223784162fa1fd4b` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f634aba6679442e3e262646bf8baacb03e254322e86db54f59557d21f06ed4fd/ed12bb77b2135db05cb1a66dd3ae1ed68d40ea73bf29a74cd0944d3cac76e6df/map-inspect.22824ec9592fad36.json`.
Vanilla state 43 is Northern Hungary, owned and cored by HUN, and includes Budapest province 9660.
Vanilla history names the file `88-Kielce.txt`, while English `STATE_88` is **Kraków** (`GER_STATE_88` is Krakau); the starting owner and core are POL.
The mod-specific `camp_rework_germany_register_auschwitz_layers` scopes state 88 and sets `genocide_auschwitz_experiment_site`, and its Auschwitz control trigger also scopes state 88, establishing the package's state-level site abstraction rather than a vanilla state-name claim.
The map inspector describes source map/history, not a May–July 1944 control scenario, and its overall validation reported unrelated map/building-position findings.
The earlier 85/87 map query timed out after 180 seconds, but the 43/88 retry returned the artifact above.

The original `genocide_germany_transfer_prisoners_to_experiment_site_in_from` helper and its decision required GER-controlled source and destination 88, and the decision targeted occupied-Poland noncore camp states. That was the pre-2026-09-26 route; the retained decision now uses the exact occupation-to-custody source and destination contract in `docs/camp_exact_cohort_transfer.md`.
That path sets zero Deaths for its movement but has no source physical debit, destination physical credit, HUN-to-88 occupation-row receipt or proof that 43 is GER controlled.
It therefore is a related control pattern, not an accepted caller for this helper.
The narrow `hoi4.event_inspect` result was `EVENT_INSPECTED_PARTIAL` at revision `f50fb76d44de057fe86eff72c777b7748ed6d79862f47b0fef136453dabd22de`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/accd06456b0a5a39d3714f85d86c1c650d3db79cc35955ea35faf8be5c495612/ed976002f8ef6a3a310ea82faabf9764070f157ec814752023f0015722a12a1d/event-scan-f50fb76d44de.json`.

## Validation and limits

`python -m unittest discover -s docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation -p 'test_*occupation*.py'` passed 16/16 existing accounting tests.
`python -m unittest docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/test_cross_state_transfer.py` passed 8/8 targeted model/source scenarios for partial split, two origins at one destination, later destination death, physical rollback, capture preflight, annexation and release.
The full focused occupation test discovery passed 29/29.
These are arithmetic and source assertions, not an executable Clausewitz transaction or proof that the engine's state `add_manpower` and inverse return exact receipts under the proposed dated route.
An engine-backed same-route receipt/rollback check and scenario-time map/control validation remain required before a completion claim; the later Łódź section records the dated custody call site now present in source.
When an unlabelled outside population loss occurs after two origins share a host, the current bounded reconciliation retires exposure from rows in reverse append order because the shared all-cause state ledger does not identify a source cohort.
That row choice is conservative for later campaign losses but cannot prove which original cohort experienced the outside loss; an exact original-cohort claim across such an event remains unresolved and needs an explicit source-labelled receipt or an accepted uncertainty policy.
No new icons, sprite names, localisation, AI weights or probability surfaces were introduced.

## Łódź dated caller and custody transaction

[USHMM's Łódź article](https://encyclopedia.ushmm.org/content/en/article/lodz) and [timeline](https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1942-1945/liquidation-of-the-lodz-ghetto) document German deportations from the Łódź ghetto to Auschwitz-Birkenau in August–September 1944; the first transport arrived on August 9 and the timeline estimates about 67,000 people deported.
The country-owned `camp_occ_try_lodz_auschwitz_transfer` runs inside `camp_occ_monthly_country` after the month guard and examines state 87 from 1944-08-09 through 1944-09-30 inclusive. It requires the original GER authority, active radical campaign, direct current GER control of states 87 and 88, a live native occupation row at 87, and state 88's operational supported killing-center role with `extermination_camp > 0`. It does not require the optional Mengele experiment marker.
The post-cutover `camp_admin_ger_establish_krakow_site` decision and guarded AI monthly call can first establish a base detention site in state 88 from 1943-05-30 for Nazi GER at war and in control, when no camp or responsible authority occupies the state, development spending is active and the separately checked 25 PP payment succeeds.
The setup writes a site-establishment history row but does not grant the killing role; the monthly source calls paid radical mandate, setup and paid selected-role conversion in that order, with later retries if a gate fails, so the route's operational killing-center and support gates remain distinct.
The registered-country hidden timer now reaches the same bounded monthly site and role attempts even with Chaos Meter disabled; source/calendar tests pass, while engine scheduling and natural 1944 availability remain unproven.
Vanilla `87-Lodz.txt` contains Łódź victory point province 9508, starts POL owned/core, and is localized `STATE_87: "Łódz"` (`GER_STATE_87: "Litzmannstadt"`).
The 87/88 `hoi4.map_inspect` returned `MAP_INSPECTED`, revision `0735a1fee370655f8100269df64c54790e71fd94777590d33f2406bf59c1fb6c`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f886b05ad72730bda49bdf52f9b3f053451944723759923f7b2b9922e9f1187/b58946ac123a81fb5eeefa1f3759d5c923fe91e00afb81b698ab60fb14e73574/map-inspect.0735a1fee370655f.json`.
Its state membership and map geometry checks passed, while overall validation failed on unrelated map building positions and port adjacency findings.
The map inspector validates source geometry/state membership but not scenario-time control; the source caller checks both controls at runtime, whose natural-play satisfaction remains unverified.
The relevant hidden monthly event scan returned `EVENT_INSPECTED_PARTIAL`, revision `f50fb76d44de057fe86eff72c777b7748ed6d79862f47b0fef136453dabd22de`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e03db30a5e53cbf898310c549ab0dc77c122e08713119af7b4cd9c41dd440a7/a076ad23e859cdcac2db4c991c1b4bb762244445132ef8882dfe1eb6cd06726f/event-scan-f50fb76d44de.json`.

The generic `camp_occ_transfer_survivors_exact` remains an occupation-to-occupation movement and therefore cannot be used as an Auschwitz admission.
The foundation now supplies aligned origin-tagged custody rows and state-scoped `camp_admin_preflight_import`, `camp_admin_bind_import` and `camp_admin_inverse_import_bind` helpers.
The separate source-state `camp_occ_transfer_to_custody_exact` uses those APIs without calling the ordinary local admission helper or appending a destination occupation row.

### Exact occupation-to-custody sequence

1. The dated caller reserves one proven native state-87 source row, then stages state 88 through `camp_occ_stage_custody_destination` for each bounded wave. Each whole-person request is capped by the live row, resident/share headroom, supported monthly throughput and the remaining living movement budget before it supplies `camp_occ_custody_route_proven = 1` and the exact row ID.
2. `camp_occ_preflight_custody_source` checks current authority, aligned authority-owned rows, the selected live row at this host, immutable original state and root ID, and finite physical/occupation headroom without mutation.
3. The helper passes original state, original authority, occupation root and requested people to destination `camp_admin_preflight_import`; that API requires an initialized aligned custody registry, operational site, matching custody authority, direct control, capacity and share headroom.
4. Only after both preflights pass does it make one measured physical source debit and one measured physical destination credit, in that order.
5. After both physical receipts exactly match the request, destination `camp_admin_bind_import` appends one origin-tagged custody row and increases only `camp_admin_detainees_k` and `camp_admin_total_admitted_k`; it makes no physical change.
6. Only after a matching bind amount, positive bound row ID and pending inverse token does the source re-prove its selected row and aggregate snapshot, subtract the living amount from that occupation row and `camp_occ_remaining_k`, record moved-out history, and clear `camp_admin_import_bind_pending_inverse` on successful commit.
7. On any postdebit failure it inverses the exact custody bind first if one exists, then undoes the measured destination credit and restores the measured source debit; mismatched inverse or physical receipts set sticky `camp_occ_custody_rollback_failed` and block another transfer from that source.
8. Movement writes no Deaths entry. Later custody death at the actual destination consumes the selected origin-tagged custody row, performs one physical death debit and writes one shared Deaths entry under the original authority; release/reform consumes living custody only.

The helper returns `camp_occ_custody_result`, `camp_occ_custody_committed_people`, `camp_occ_custody_preflight_valid`, `camp_occ_custody_source_debit_people`, `camp_occ_custody_destination_credit_people`, `camp_occ_custody_bind_people`, `camp_occ_custody_bound_row_id`, `camp_occ_custody_inverse_people`, `camp_occ_custody_destination_undone_people`, `camp_occ_custody_source_restored_people` and `camp_occ_custody_rollback_complete` as same-chain temporary receipts.
It consumes the route proof, row ID and amount inputs after each call; the dated caller sets `camp_occ_lodz_auschwitz_transfer_recorded` when the one source-row movement budget is proved, reduces the budget only on exact positive receipts, and writes one institutional-history summary for each month with any committed wave.
After a valid bind, `camp_occ_apply_killing_arrival_loss` may record measured site-88 violence against the bound custody row; the transfer itself still writes no death.
The request derives from a living row and available destination capacity, not the historical deportation estimate; no quota-derived deaths or protected-group selector are used.
Natural 1944 play has not established the killing role and site support, actual GER control at the dated tick, or exact engine receipt and rollback behavior; parent source/MCP review and user live-game validation remain outstanding.

`test_occupation_custody_transfer.py` covers exact source-to-custody membership, short source debit, short destination credit, rejected bind, postbind source failure with inverse-first rollback, failed inverse quarantine, two original cohorts at one custody destination and later origin-tagged destination death.
The focused occupation discovery now passes 55 source/model tests, including dated bounded-wave caller, monthly history summary and exact origin-row assertions alongside the custody-transfer and foundation origin-row scenarios.
These tests do not interpret Clausewitz script or establish in-engine acceptance.

## Documentation reconciliation, 2026-09-25

The accepted implementation contract named in `../accepted_implementation.md` supplies the user-authorized population and conservation design; this handoff records implementation evidence and cannot by itself approve a new historical route.
`common/scripted_effects/camp_administration_occupation_effects.txt`, `common/scripted_effects/camp_administration_effects.txt` and the country setup files are current source evidence for the helper, dated caller and site bridge, while their package Markdown describes the public contracts, `historical_benchmark_2026-09-25.md` remains the source-linked arithmetic comparison, and `../implementation_execution_2026-09-25.md` remains the unresolved execution ledger.
The older Hungary discussion remains historical route context without a proved state-43 cohort or caller. The legacy German discussion above is superseded: the 2026-09-26 retained decision invokes the exact custody transaction from a verified living occupation row; engine receipt proof remains pending.

| Plan or handoff item | Disposition and basis | Remaining limit |
| --- | --- | --- |
| Aligned occupation rows and generic physical survivor transfer | Implemented in `camp_administration_occupation_effects.txt` under the accepted provenance and conservation contract | No named generic occupation-to-occupation caller or engine receipt |
| Origin-tagged destination custody and occupation-to-custody transaction | Implemented in `camp_administration_effects.txt` and `camp_administration_occupation_effects.txt` under the same contract | No in-engine debit, credit, bind or inverse receipt proof |
| Dated Łódź to state-88 caller | Implemented in `camp_occ_try_lodz_auschwitz_transfer` and called by `camp_occ_monthly_country`; historical source basis remains the cited USHMM Łódź account | Natural 1944 role, support and control gates, along with engine receipts, are unverified; source implementation does not establish final design acceptance |
| State-88 detention setup before later killing conversion | Implemented in `camp_admin_ger_establish_krakow_site`, its decision, and deterministic AI helpers as a source-level bridge under the accepted institution and finite-cohort contract | The exact 25 PP bootstrap and bounded timer have source tests, but no route-valid engine scenario yet proves later killing role, support and control |
| Hungary state-43 candidate | Unresolved historical candidate, with no accepted route or source caller | State-43 German control and a finite, source-labelled cohort have not been proved |
| Original-cohort assignment after unlabeled outside loss | Unresolved | Shared all-cause state ledger carries no original-cohort label; parent must approve an uncertainty policy or supply a source-labelled receipt |
| German six-million calibration | Blocked by current modeled source envelope and missing dated control and cause coverage | The source benchmark is about 3.64 million below the historical comparison and is not a complete campaign simulation |

The contradictory “no dated caller” and “transaction still outstanding” claims in this handoff, the occupation helper documentation and the implementation ledger were corrected to distinguish the generic helper from the wired custody route.
No document was merged, deleted or marked superseded; the older route investigation and its MCP artifact references remain useful context.
No prompt file was in the assigned cleanup scope, and no stale prompt instruction was identified in the three owned documents.
The four owned Markdown files were checked for accidental mid-sentence physical line breaks; none required repair, and existing headings, tables, lists and source quotations were preserved.
The parent accepted the bounded living-wave and measured arrival path; its current movement ceiling is the whole proven living state-87 row, subject to exact paid throughput, resident headroom and the two-month cutoff. Unknown original-cohort attribution after outside losses remains unresolved.

The 2026-09-25 read-only MCP refresh returned `EVENT_INSPECTED_PARTIAL` for a bounded scan of `events/chaosx_genocide_events.txt`, with workspace-wide helper and lifecycle analysis deferred: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08aeb3743d96cbfab9e6f28888085b9acc8d69225a66d8c08ad0ae80ae95eab7/3ff840808586ef9a64196d8c5b7ffc1b4bfb116af38d30eed2ec9458c3b7739d/event-scan-0106e3d60ec5.json`.
The same refresh returned `GUI_INSPECTED` for `repression_ledger_window` with `validation.passed = false`: the complete artifact has 1,398 diagnostics, including 173 click-region errors, 742 overlap warnings, 206 z-order warnings and 137 clipping warnings. Exactly 1,396 belong to the automatically generated `docs_reconciliation-generated-1` fixture, whose first click-region finding pairs country action and crisis controls from potentially exclusive panels; the two remaining warnings concern vanilla `core.gfx` declared sprite sizes. Those counts are a review lead, not proof of visible defects in the owner's mutually valid scenarios: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/877fed49cb5d37366f34f7793773b7401ffb16e658589d5ce0e19ab9bfbb5e2f/fe22f34aa91d7497cb315dca69ad54b2787bc8b6216ce88f7a4ce8992bf448dd/gui-inspect.97283e74cfeb7e59.json`.
The refreshed `hoi4.map_inspect` for states 43, 87 and 88, `hoi4.tech_inspect` bonus coverage for `industry`, and `hoi4.focus_inspect` for GER each timed out awaiting the tool call after 180 seconds; the older linked artifacts above remain historical evidence, not fresh proof of current source or scenario health.
The GUI and event tool names were exposed and those two read-only calls returned artifacts; this does not prove complete service health or standalone viewer availability. Probability scenarios remain with the dedicated read-only probability auditor and are not inferred from source inspection here.

After the state-88 setup source edit, a bounded `hoi4.event_inspect` scan of `events/camp_administration_country_events.txt` returned `EVENT_INSPECTED_PARTIAL` with workspace-wide helper and lifecycle passes deferred: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/245b05864811f0970dacccb7f7f99b4ed61d5a37dca59e58b36607779c915f54/227cd65c8aaa7e4687589ea3b16dadd6c9f776694cccfcb49fdeab1ac64f1144/event-scan-f38750d657aa.json`.
An explicit `repression_ledger_window` GUI inspection with generated scenarios disabled returned `GUI_INSPECTED` but `validation.passed = false`, including 717 non-blocking overlap findings in that documentation fixture; this does not replace the owner's populated render matrix or prove a visible defect without image review: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0598588192f003623a8437678d9f58ec3c89b3c2b81924ba7084fed06fb90377/c96b2a7ec8986cbbb7defe62d1209a45727a73cd610db6e7783eb3deaf9fedb9/gui-inspect.5f7089cd25b0eeb8.json`.
A focused `hoi4.map_inspect` for state 88 returned `MAP_INSPECTED`, with province/state membership checks passing and unrelated map positions/locators validation failing; it does not provide 1944 German control or site-role evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b542f9f8e7279a91bb4cf4e221844fcf0e3d9343f038e6015e5b45be5e18fe63/19530e86519286a29ad93b646bbf4df31103d0376edaa5a335f41ab03276d937/map-inspect.70f1f01380d28992.json`.

## State-88 documentation follow-up

The 2026-09-25 follow-up changed only `common/scripted_effects/camp_administration_country_effects.md`, `../implementation_execution_2026-09-25.md`, this handoff, and `historical_benchmark_2026-09-25.md`; no document was merged, deleted or superseded, and no gameplay, localisation, GUI, asset or spreadsheet file was edited by the documentation curator.
The country helper documentation maps the one-time 25 PP detention decision, guarded source-order AI calls, Records history kind, existing decision icon and package-owned registered-country timer to their current source identifiers.
The historical benchmark now distinguishes installed vanilla `STATE_88` Kraków from the `88-Kielce.txt` filename and the mod's Kraków/Auschwitz-area site abstraction, while preserving the unchanged arithmetic envelope and unresolved six-million comparison.
The 58 focused occupation source/model scenarios pass after the state-88 setup, bounded arrival-wave and German home-origin exclusion additions; they do not execute Clausewitz or prove a 1944 route-valid transfer.
The parent still needs to review the exact bootstrap design, disabled-setting monthly dispatch, source-labelled outside-loss attribution, natural 1944 control and killing-role gates, engine debit/credit/bind/rollback receipts, populated GUI edge states, and historical cause calibration.
