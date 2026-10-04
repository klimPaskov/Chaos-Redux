# Historical campaign intake and cause calibration addendum

Disposition: implemented in package source for the bounded Łódź and manual-order arrival path; engine and wider historical acceptance remain unresolved.
Acceptance basis for the existing task boundary: the user's accepted contract in `../accepted_implementation.md` and execution plan in `../implementation_execution_2026-09-25.md`; this addendum proposes a bounded way to satisfy their historical-control and exact-receipt requirements and is not itself an accepted spec or implementation claim.
Parent acceptance on 2026-09-26 applies only to the exact per-wave receipt, source-informed arrival-rate sensitivity, role restriction and conservative stop contract described here, under the user's full rework request and prohibition on casualty quotas and shared-core edits.
The unresolved `historical_benchmark_2026-09-25.md` is measurement evidence for this same gap, not an earlier expansion addendum to stack over.
Implementation evidence: `common/scripted_effects/camp_administration_occupation_effects.txt` now reserves one proven row, runs bounded supported living waves with exact transfer receipts, and requests actual bound-row arrival violence through `camp_occ_apply_killing_arrival_loss`; `common/scripted_effects/camp_administration_effects.txt` records arrival as a subset of cause-separated violence in aligned state, original-authority country and custody-row records. The German home-origin admission guard keeps the domestic census and foreign-origin occupation campaign disjoint at enrollment.
The parsed-source and dated arithmetic tests in `foundation_source_tests.py`, `occupation/test_occupation_custody_transfer.py`, `occupation/test_occupation_accounting.py` and `occupation/test_historical_envelopes.py` pass, with the source-control sensitivity and all-origin initial inventory recorded in `occupation/historical_envelope_results.json`; `occupation/europe_origin_coverage_matrix_2026-09-26.md` separates the counterfactual upper calculation from still-missing dated controller evidence. No HOI4 engine population receipt or full European campaign calibration has been obtained.

## Design problem and source boundary

At proposal time, the dated source-control fixture assumed one supported 25,000-person killing level in state 88, and `camp_occ_try_lodz_auschwitz_transfer` capped a single living Łódź transfer by that resident capacity.
It therefore moved 25,000 people and its first post-transfer month measured only 499 killing-role violence deaths, whereas the [United States Holocaust Memorial Museum](https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1942-1945/liquidation-of-the-lodz-ghetto) describes about 67,000 deportations to Auschwitz-Birkenau in August–September 1944 and about two-thirds murdered upon arrival.
The [Auschwitz-Birkenau State Museum](https://www.auschwitz.org/en/museum/news/the-70th-anniversary-of-deportations-of-jews-from-the-lodz-ghetto-to-auschwitz%2C1091.html) also gives roughly 67,000 deportees and about 45,000 murders, while noting that some deaths followed time in depot camps and that only a little over 3,000 were registered at Auschwitz while about 19,000 were transferred onward.
Thus resident detention capacity, intake throughput, killing-center arrival violence, later custody mortality and later forced-labor mortality are distinct historical and gameplay quantities; the addendum uses “arrival phase” as an abstraction of arrival and short depot time, not a claim that every death occurred in one instant.

The existing restricted German envelope is about 2.356 million campaign-plus-custody deaths, compared with the [USHMM's approximately six-million Holocaust estimate and broad cause breakdown](https://encyclopedia.ushmm.org/content/en/article/documenting-numbers-of-victims-of-the-holocaust-and-nazi-persecution).
That restricted envelope includes only Poland, the Netherlands, Hungary and one domestic sensitivity, assumes persistence and control, and does not execute a killing-center receipt; its difference from six million is a coverage warning, not a deficit to fill with casualties.
The [USHMM account of Operation Reinhard](https://encyclopedia.ushmm.org/content/en/article/operation-reinhard-einsatz-reinhard) places Bełżec, Sobibór and Treblinka in the 1942–1943 campaign; it would be historically wrong to assign their losses to the state-88 Auschwitz abstraction.
The [Auschwitz Museum chronology](https://www.auschwitz.org/en/history/evacuation/the-cessation-of-mass-extermination) says mass extermination there ended in November 1944 and evacuation began in mid-January 1945.
The existing 1943-05-30 gate remains appropriate for the distinct hidden Mengele branch under the accepted contract, and should not silently be used as a historical opening date for every killing center.

## Exact bounded arrival path

Keep `camp_occ_transfer_to_custody_exact` as the sole physical source-debit, destination-credit and origin-tagged custody-bind transaction; preserve its inverse/rollback rules and its returned `camp_occ_custody_bound_row_id` and `camp_occ_custody_committed_people`.
Add one package-owned wrapper, provisionally `camp_occ_process_killing_arrival`, called by `camp_occ_try_lodz_auschwitz_transfer` only after the existing regime, date, control, supported site, killing-role and registered-row gates pass.
The wrapper maintains a remaining **living movement request** and a separate, paid and supported monthly **arrival throughput allowance**; neither is a desired death count.
For each bounded iteration it requotes the current live source row and state-88 resident free capacity, asks for no more than the lesser of those amounts and remaining throughput, and calls the exact transfer once.
Only a fully matched source debit, destination credit and bound origin row is an accepted arrival.
After that commit, while the same authority still controls the operational supported killing-role site and shared deaths are enabled, request arrival-phase violence against **that returned custody row ID only** via `camp_admin_record_deaths` and its existing exact shared civilian-loss receipt.
The requested fraction is a source-informed model parameter applied to actually accepted living arrivals, not a historical victim quota, and the amount projected is the physical death receipt `camp_admin_death_actual_k`, never the request or an archival estimate.
Use the existing camp `violence` cause and shared `camp_atrocity` reason exactly once; add a package-owned “arrival-phase killing” subtotal of that violence cause at site, country and origin-row level rather than creating another shared death or a second aggregate death debit.
The surviving portion of each imported row remains living state-88 custody; ordinary detention and forced-labor arrivals use their existing resident-capacity path and do not acquire this arrival-phase violence.
The pre-existing monthly custody, labor and killing-role rates still apply later to their measured survivors and must not reprocess the same arrival as an additional arrival event.

Recompute free capacity and the remaining source/throughput allowance after each **actual** receipt, allowing another exact batch only when all three remain positive and route gates still pass.
A conservative fixed maximum iteration count, a strictly decreasing remaining throughput value and a positive committed-person test make the loop finite.
If a physical death receipt is lower than requested, the additional survivors occupy capacity and shrink the next possible batch; do not manufacture the difference as a death, release, or population removal.
If deaths are disabled, all accepted arrivals remain alive, so the path stops when resident capacity fills; no catch-up killing is queued after re-enabling deaths.
If the site loses role, support, control or authority between batches, stop with the already committed living rows and receipts intact, and leave the untransferred remainder at its source.
If preflight, debit, credit or bind fails, use the existing same-chain inverse/rollback; record no arrival death, do not consume throughput for an uncommitted batch, and make no paid-decision success claim.
If the shared death API accepts zero or a clipped amount after a committed batch, keep the entire measured survivor stock and stop or continue only within newly measured free capacity.
No provisional arrival queue, invented transit death, protected-group selector, reward per casualty, technical killing procedure, or shared Chaos Meter edit is proposed.

Illustrative arithmetic, not a balance target: with 67,000 independently available living arrivals, 25,000 resident places, a throughput allowance above 67,000, and an arrival-phase request rate of 0.65, the **unclipped mathematical request** is 43,550 deaths and 23,450 living residents.
The source-informed candidate rate 0.65 should be held in one package script constant and tested at 0.55, 0.65 and 0.75 against actual receipts; historical estimates do not set a required game total.
The existing source-row, geography, setup and control assumptions may produce a different arrival count, and the final rate and throughput are accepted only after route-valid calibration and parent review.

## Original tuning proposal and implemented resolution

In `common/script_constants/camp_administration_occupation_constants.txt`, centralize a Łódź living-movement share, a state-88 killing-role **throughput per supported level per month**, a maximum batches-per-month safety bound and an arrival-phase violence request fraction; no absolute 67,000 or 45,000 token belongs in gameplay.
Keep resident places in `camp_admin_value.capacity_per_building_k` distinct from the new throughput parameter; do not raise every detention site's capacity to make one killing route work.
At drafting time `lodz_auschwitz_living_share = 0.5`; the implemented source instead reserves 1.0 of the **measured living state-87 row** as a movement ceiling, while exact source headroom, paid throughput, resident capacity and the two-month cutoff limit accepted movement. This is not an absolute transport count.
The implemented central values are 75,000 supported arrivals per undamaged killing level per month, a 0.65 arrival-phase violence request fraction and a 12-batch monthly safety bound against the current 25,000-place fixture. The dated arithmetic sensitivity and 0.55/0.65/0.75 variants are in `historical_envelope_results.json`; the rate is not historically verified by an engine receipt.
The dated automatic route still requires GER authority and control of states 87 and 88, one active source root, an operational supported state-88 killing role and August–September 1944 dates; its once-only flag is set when that single source-row budget is proved, and monthly history is written only after a positive exact receipt.
Do not turn an unavailable site or unproven source into a synthetic historical transport.
The separately user-approved `germany_transfer_prisoners_to_experiment_site` remains an explicit paid national order with its oldest eligible source selector and exact living transaction; it must not become an automatic Łódź fallback.
The parent accepted arrival-phase consequences for the manual transfer within the user's retained exact-cohort decision: after its valid bind, it calls the same measured bound-row loss helper and charges only when a positive living transfer commits.
The `camp_admin_ger_establish_krakow_site` decision and guarded AI source order establish detention first, then pay for the killing-role conversion; the new wrapper cannot bypass either cost or mandate gate.
Do not move the Mengele permission gate earlier to satisfy the 1944 fixture.

## Campaign coverage without a six-million quota

Keep `camp_occ_seed_origin`, `camp_occ_origin_assigned` and the country-owned aligned origin rows as finite geographic exposure ceilings; a ceiling is neither a casualty target nor evidence that all people within it died.
Build a dated fixture matrix for the already seeded European origins in `camp_occ_historical_setup` rather than extrapolating the current three-row envelope to the whole continent.
For each fixture, enumerate original owner, eligible state IDs, actual controller by month, source seed date, pre-enrollment outside declines, other custody reservations, active occupation rows, monthly measured campaign receipts, movements and closures.
Separate actual controller paths from an expressly counterfactual all-controlled-Europe upper sensitivity, and do not relabel the latter historical reconstruction.
Keep `camp_occ_project_receipt` territorial campaign violence distinct from state-88 arrival-phase killing, later site violence, custody, labor and institutional deaths, and keep `camp_occ_reconcile_external_population` removals un-attributed unless the external owner provides an actual death receipt.
After a full controlled-origin matrix, compare measured categories with the USHMM broad ranges and report uncovered periods, origins, centers and other non-modeled causes; never multiply `german_campaign_monthly_fraction` merely until the sum equals six million.
An expanded site network for Bełżec, Sobibór or Treblinka, a new protected-population classifier, or a staged 1944 Hungarian transport belongs to a separately accepted map and source plan, because the present source has no route-valid destination/control proof for those movements.
The [USHMM Hungarian account](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-in-hungary) documents about 437,000 deported in May–July 1944 and about 420,000 sent to Auschwitz, but those figures cannot establish a German-controlled mod source state or an unbounded state-88 receipt.
For Japan, retain combined China occupation losses as their own control series and Pingfang/institutional losses as separately measured causes; the existing 160-million occupied-area claim and 38-month persistence sensitivity are not a verified census or an institutional casualty estimate.

## Conservation and receipt contract

For every source root at each checkpoint: initial admitted exposure equals current live occupation rows plus live imported custody rows plus measured campaign and site deaths plus documented releases and external exposure removals, with movements counted as reclassification rather than new people.
For every committed wave: source population decrease in whole people equals destination population increase before any death, equals exact bound custody amount, and equals the committed movement receipt; an abort restores both physical sides and leaves the source row and site row unchanged.
After the arrival-phase loss: destination population decrease equals the shared death receipt equals custody-row decrement equals the new arrival subtotal increment, while the existing `violence` and all-deaths totals each increase once by the same receipt.
Every imported row retains its original state, immutable responsible authority and occupation root through later killing, custody, labor, release, capture and annexation; two distinct roots sharing state 88 must never merge silently.
No source can be debited for a destination death, no death can be recorded before destination receipt, and reform releases only surviving custody without restoring the dead or site infrastructure.
History rows may display a moment, but their 96-entry rolloff means durable origin/cause totals require aligned permanent rows or counters rather than history alone.

## Dated verification fixtures and AI policy

Update `occupation/test_historical_envelopes.py` and the JSON/benchmark together: rerun 1941-07 to 1944-09 with the existing state-87 geographic proxy and one 25,000-place state-88 killing level, printing each monthly live source row, actual wave, arrival subtotal, resident stock, occupation violence and other causes.
Test a 67,000-person **input sensitivity** separately from natural source enrollment to isolate capacity/throughput mathematics; label the historical reference as a comparison, not a scripted intake target.
Add a route-valid August and September 1944 control fixture using GER ownership/control, a paid supported role, the current source row and physical state population, then rerun it with 0.55/0.65/0.75 arrival rates and with one versus multiple supported levels.
Test no killing role, empty support, destination capture between waves, source capture, insufficient source headroom, a nearly full resident site, deaths disabled, clipped death receipt, partial credit, bind failure and failed inverse; in each case assert actual conservation and no invented deaths.
Test two independent approved source roots reaching one destination, followed by later custody/labor deaths and release, and verify original authority attribution and row-specific cause subtotals.
Run a realistic controlled-origin Europe matrix to 1945-04 and a separate counterfactual envelope; report headroom and external competing debits, not just totals.
Keep a one-month China snapshot and explicitly labeled 38-month persistence sensitivity separate from any Pingfang receipt.

The automatic Łódź route should be deterministic after its historical gates; AI still has to buy and sustain the same mandate, site and role through existing helpers, and lack of payment or support leaves the movement unexecuted.
Do not add an AI-only population grant or unguarded site conversion to make a historical graph fit.
The existing `germany_transfer_prisoners_to_experiment_site` uses `ai_will_do`; the parent-owned `chaosx_ai_probability_auditor` baseline must start with `hoi4.probability_inspect`, and any changed AI weight or timed decision behavior needs the matching scenario comparison before acceptance.
This addendum selects no new AI weight, MTTH, random pool or exact selection probability.

## Concrete parent implementation order and evidence limits

1. Preserve an immutable pre-edit source and scenario set for any weighted AI edit, and reconcile the parent-owned probability audit before choosing a weight.
2. Extend only package constants, `camp_administration_occupation_effects.txt` and its markdown contract, `camp_administration_effects.txt` and its markdown contract, and the necessary package triggers/row arrays for the bounded arrival wrapper and durable origin/cause receipt.
3. Reuse the existing state-88 setup and paid role helper in `camp_administration_country_effects.txt`; change `camp_repression_major_country_effects.txt` and `genocide_crisis_decisions.txt` only if the parent accepts applying the same arrival phase to the manual paid decision.
4. Keep the shared Chaos Meter core, world-wide recurring hooks, event log, common GUI framework, localisation, workbook and assets outside this planner's edit scope; the parent reconciles any player-facing wording or UI after mechanics are accepted.
5. Run source fixtures, then inspect the dated state route with the read-only HOI4 map tools and current decision AI with the probability workflow; use a route-valid engine scenario to prove physical receipt, rollback, cause attribution and control before treating historical calibration as accepted.
6. Compare the resulting categories to the archival ranges, document every residual cause/region gap, and retain `historical_total_acceptance_complete = false` until the accepted full-period evidence is present.

For this planning pass, `hoi4.map_inspect` inspected states 87 and 88 and returned `MAP_INSPECTED` at source revision `24649b4f4cd9de0eeef824349303157090b09b61cbdae00944874cc080865918`; its [artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b6b7e4b120de95ae4a037f6fd6c9046353b71d6baf634e716441a6bbe531313/bccc703a12ed4ead850dfb33d3e1e8a194aabeeaac274611ab0de0d5f7601789/map-inspect.24649b4f4cd9de0e.json) is a map catalog, not 1944 control evidence.
`hoi4.map_render` returned `MAP_RENDERED` for the state layer at the same revision with [PNG artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2bf654fe1fc69bb1d744cc187c83e11314a368893a0c6ecd38948ae3e7c901e/766997984b2f3b8713199c0f6f54f22643edea7d4319a2d5d9eef5a06ef6172c/map-state.png).
The map inspection reported unrelated position/port diagnostics and a truncated diagnostic list, so it does not clear every map issue; the render and source files do not prove an engine debit, dated controller or historically exact state-88 geography.
The route uses no new focus, event, technology, doctrine or GUI design surface in this addendum; an existing package-owned delayed event and the existing Records view remain parent validation surfaces if implementation changes their consumer facts.
No standalone Technology Tree Viewer command was found on PATH under the checked names `hoi4-tech-viewer`, `hoi4-technology-tree-viewer` or `technology-tree-viewer`, nor was a viewer-named file found under the checked Codex installation tree; read-only technology MCP tools are exposed, but the standalone viewer is a package gap in this environment, not a substitute for later `tech_inspect`/`tech_render`/`tech_compare` if technology scope changes.

## Promotion and stop rule

If the parent accepts the bounded arrival design, promote its transaction order, cause definitions, chronology, constants and acceptance scenarios into the corresponding source specification under `docs/specs/system_camp_repression_rework_specs/` with the parent's explicit acceptance basis and this addendum's disposition `promoted into an accepted spec`.
If implementation is deferred, mark it `accepted and queued` with the reason; if the parent rejects the arrival-phase model, record the reason here and retain the benchmark unresolved rather than quietly increasing the monthly violence rate.
Do not expand this pass into further centers, methods, rewards, country routes, interfaces or super-events while the bounded receipt and full-origin coverage evidence remain unresolved.
