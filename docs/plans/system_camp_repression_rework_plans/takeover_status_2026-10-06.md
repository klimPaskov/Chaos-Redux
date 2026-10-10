# Camps takeover status, 6 October 2026

Superseded in part on 10 October 2026: the calendar gates described below (Western, Greek and Italian origin dates, the dated partner windows, the Kraków and Mengele dates) now open on gameplay conditions, and the window was redesigned; see [gameplay_gates_ui_decisions_2026-10-10.md](gameplay_gates_ui_decisions_2026-10-10.md). The QA steps that set calendar dates need campaign, domination or front conditions instead.

Disposition: the latest audit's source changes are implemented and reviewed, with the explicit modeling limits below.
The workstream is not approved as fully complete because current GUI evidence, complete weighted eligibility and live-engine acceptance remain open.
No game or desktop window was launched.

## Commits and ownership

Implementation commit: 4bc25bb29c4b9bec4193cf7585fb4c9c3ec876ff.
This status and accepted-contract cross-reference are committed separately after review of the implementation commit.
Both messages carry the requested Codex co-author trailer.

At intake no camp source file had an unpublished hunk.
The excluded untracked `mcp/after/gui351_current_matrix/` folder remains untouched.
Changes to the shared achievement registry contain only achievement 68's camp conditions.
Shared achievement localisation contains only the six 65, 66 and 68 description/tooltip lines, and shared decision localisation contains only the German transfer source-date explanation.
The legacy Mengele trigger file contains only the one Auschwitz authority helper change.
Other worktree and real-index changes remain outside the isolated commits.
No workbook or exported catalog CSV was edited.
Camps is an existing system, so this pass needs no event-catalog row or new random-event identity.
The new reports are supporting partner reports fired from the existing administration, rather than Settings-selectable random events.

## What is implemented

The r1 and r2 fixes were checked against current source: prepared endpoint-observation inputs, no parameter-block helper calls, guarded modifier removal, finite movement/death attribution, reform through incomplete-origin closure, retired foreign imports, dispatch cleanup and stale timer protection, dated Danish rescue, sale-aware payments/refunds, quiet monthly processing, Hungarian response and the earlier Western date gates.
The independent review is `subagent_handoffs/completion_audit_2026-10-06.md`.

The current pass implements all five source items of audit r3.

| Item | Result and evidence |
| --- | --- |
| German administrations | Shared state authority accepts GER and eligible German subjects, excludes sovereign partners and special Chaos countries, and keeps GER responsibility through state handover. Registration, closure, custody, Kraków setup, AI role conversion, Mengele, Łódź, Hungary and manual transports share the rule. |
| Japanese clients | Eligible China-region states held by Japanese clients register under JAP responsibility. MAN/MEN cores stay outside the war-zone profile and Pingfang retains its separate gate. |
| Achievements | ENG review sets the retained Raj flag, USA wartime court review sets the before-victory flag while claims remain dated to July 1948, and Italian review replaces the retired road/guard requirements without removing Libya development or the stationed division. |
| Wider partners | Slovakia, Croatia, Bulgarian-held Thrace/Macedonia/Pirot and Vichy receive dated, finite handover orders with comply, delay and permanent halt choices. One demand covers every province and both Croatian waves. Successful physical movement precedes destination deaths and no research or material award follows those deaths. |
| Campaign dates | State 731 retains the Salonika date, other Greek origins use 24 March 1944, and Italian origins use 16 October 1943. The monthly and manual-source paths use the same predicate and the source tooltip names the dates. |

Parent review also removed a campaign-active condition from control tracking, so a state captured before the campaign opens remains queued for later admission.
It replaced the direct-control legacy Mengele helper and removed a redundant direct-controller import check, both of which would otherwise defeat the GEN-held Auschwitz route.
A production-helper test executes custody import into GEN-held state 88 and confirms matched physical movement and retained German responsibility.

Main implementation files are the camp administration occupation, country and civil effects/triggers, `camp_occ_partner_constants.txt`, `camp_occ_partner_effects.txt`, `camp_occ_partner_triggers.txt`, the partner events and decisions, the UI history constant/selector, and `camp_occ_partner_l_english.yml`.
The full path inventory is available from `git show --name-only 4bc25bb29c4b9bec4193cf7585fb4c9c3ec876ff`.
The decisions and acceptance basis are in `agent_decisions_2026-10-05.md`.
The mechanic contract and source crosswalk are `common/scripted_effects/camp_occ_partner_effects.md` and `docs/systems/camp_partner_orders.md`.

## Balance, presentation and source evidence

Twenty-nine source suites passed on a scratch snapshot, covering finite origin observation, movements, closure, country/civil programs, research limits, famine, release, timer cleanup, native camp cleanup, historical envelopes and costs at ordinary, half and quarter prices.
Later narrow checks cover seven authority cases and 23 wider-partner cases after final review corrections.
The source suite artifacts are under `administration_redesign_2026-09-06/mcp/takeover_2026-10-06/`, with focused results in the occupation folder.
These execute parsed production logic with mocked engine primitives and declared campaign inputs, and do not prove game execution.

The wider halt decision uses the already registered sale-aware 50 PP quote.
Halting applies the existing stability, war support, opinion and subject-autonomy pressure, and the tooltip states those consequences.
It hides when no living source remains, rechecks before execution, and refunds rejected stale clicks without a purchase credit.
Delay reduces small source offers as well as total transport capacity.
The arrival fraction and ordinary campaign rate remain the existing tuning, with no forced historical casualty quota.
The previous AI weights remain the tuning source for the additional answer pool.

Visible report counts are zero for routine monthly processing, one demand to each partner for its order, and at most one German notification for that partner's halt.
Hungary remains separate, so Germany can receive at most five distinct-country halt notices across all dated orders, with no repeated province or monthly reports.
World news is not added.
The German notice carries the saved regular `camp_occ_halted_partner` target instead of assuming nested FROM inheritance.

The camp and Soviet Gulag report-colour audits each returned zero coloured parchment keys.
The four new triggered descriptions were also directly read, with plain text and no scripted colour helper.
The wider reports reuse vanilla's visually inspected 210-by-176 `GFX_report_event_generic_train`, with no Hungarian national photograph assigned to another partner.
Hungary retains its national pictures and both halt actions reuse `GFX_decision_generic_protection`.
No new portrait, icon, flag, texture or model was required.

The unchanged direct stdio client reports `hoi4-agent-tools 3.8.1` and serves the narrow reference routes.
Revision-bound reads include installed `meta_trigger` and Script Constants sections and offline Meta triggers, Event modding and Variable types sections.
Exact requests, paths, line spans, source revisions and route gaps are saved in the MCP evidence folder.
The installed validator returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with argument blocks unchecked, so it is not represented as full syntax/semantics proof.
The partial event inspection/render includes an inspected diagram with unresolved helper nodes and focused-analysis coverage limits.
The inverse event comparison against the recorded HEAD source timed out, and current Records inspect/render timed out both before and after the history-label change, each after 60 seconds.
No current GUI PNG or `validation.json` was delivered.
The missing render remains a visual gate, with the earlier 4 October images retained only as earlier-source evidence.
Weighted scenario evidence and its exact unresolved inputs are recorded in `subagent_handoffs/probability_2026-10-06.md`.

## Design abstractions and incomplete acceptance

The director's G6 authority and audit r3 authorize the wider partner route, superseding round 2's rejection within this pass's scope.
The implementation explicitly uses state 92 as aggregate reception for handover and the wider killing campaign, rather than claiming historically exact individual killing-center geography.
Croatia's 70/30 scheduling split preserves a May remainder because the cited source gives two operations and their combined total without a reliable split.
Bulgarian state 803 is wider than Pirot, and Bulgarian control of all state 731 is a counterfactual that includes Salonika.
The Vichy 0.042 share uses the takeover's rounded 10,500 anchor over the existing 250,000-person French source ceiling, rather than a claimed precise USHMM ratio for the unoccupied zone.
The existing 0.65 arrival fraction remains a strategic model parameter, not a sourced per-partner fatality observation.
All of these are disclosed modeling choices rather than omitted requested routes.
The monthly cadence can miss a window's first partial month, including Vichy's 11 August start, and is not presented as an exact train timetable.

Incomplete: current GUI visual approval, complete probability eligibility under real state/control/row inputs, and live transaction, timing, AI and save-persistence proof.
Full-period historical calibration against actual campaign control and engine losses remains an acceptance limit, rather than a claim made from the fixture subtotals.
No requested source route, country response, achievement repair or date gate is omitted.

## Exact orchestrator checks

The read-only save inspector confirms `qa_001_fresh_head.hoi4` is plain text, USA, democratic, at `1936.1.1.12`, version `Operation Postern v1.19.2.0.a729 (2bce)`.
It already contains German `camp_admin_initialized` and `camp_occ_origin_seeded` flags.
The inspector commands used were `info` and a bounded `find` under `countries/GER`.
Use separate QA copies for the dated checks, with the actual game calendar set to the listed date through the orchestrator's date-fixture workflow.
Changing a displayed variable alone does not satisfy the native date trigger.
Pause while entering the setup, keep the random-event timer parked, and preserve a before-action save.

1. **Authority and native handover, 1 June 1944, Germany.** Give Germany an active radical campaign and Poland war context, then set up state 88 with `eval_effect GER = { add_political_power = 500 set_variable = { camp_admin_mandate = constant:camp_admin_mandate.radical } camp_admin_ger_establish_krakow_site = yes }` when its source prerequisites are met.
Use the vanilla Generalgouvernement decision, or mirror its order in one console effect: `eval_effect GER = { 88 = { transfer_state_to = GEN } set_autonomy = { target = GEN autonomy_state = autonomy_integrated_puppet } }`.
Run `eval_effect 88 = { camp_occ_track_controlled_state = yes }` for a synthetic fixture that did not undergo the normal control hook.
Open the window with `eval_effect GER = { camp_rework_open_ledger = yes }`, select state 88, choose the killing role through its paid command, and meet the normal Mengele program authorization.
Expected: no premature closure from the native transfer/autonomy sequence, GER responsibility in the site and rows, available Mengele gate and a working manual transport into GEN-held Auschwitz.
Repeat with an RKO-controlled Baltic origin and a POL subject, then with HUN/SLO subjects and a special Chaos subject.
Expected: administrations qualify, sovereign partners and the special subject do not become direct German campaign authority.

2. **Japan, 1 August 1938.** In a Japanese war/campaign QA copy, use `eval_effect JAP = { 613 = { transfer_state_to = RNG } set_autonomy = { target = RNG autonomy_state = autonomy_integrated_puppet } }`, then `eval_effect 613 = { camp_occ_track_controlled_state = yes }` and `eval_effect JAP = { camp_occ_monthly_country = yes }`.
Expected: state 613 enrolls under JAP, not RNG, and a later client handover does not close it.
Repeat with a Chinese state controlled by MAN that has no MAN/MEN core, a MAN/MEN home core, and a client of another country.
Expected: only the eligible Japanese-client Chinese state enters the war-zone profile, with Pingfang unaffected.

3. **Partner answers, separate copies.** Use Slovakia on 1 April 1942, Croatia on 13 August 1942 and again 1 May 1943, Bulgaria on 1 March 1943, Vichy on 11 August or 1 September 1942, and Hungary on 1 June 1944.
For a synthetic Slovak fixture create the recipient and core with `eval_effect 70 = { add_core_of = SLO transfer_state_to = SLO }` and place it in Germany's faction with `eval_effect GER = { add_to_faction = SLO }` when GER has a faction.
Give Germany the active radical campaign, and make state 92 a German-controlled or GEN-subject-controlled reception host for the wider routes.
Use `eval_effect GER = { camp_occ_monthly_country = yes }` once, or `eval_effect GER = { camp_occ_try_extended_partner_orders = yes }` for the wider order's isolated entry test.
Switch to the receiving partner and answer the actual report, using separate copies for comply, delay and halt.
Expected: one demand covers all provinces, no wider-route movement before the answer, immediate current-month dispatch after comply/delay, reduced delayed movement, and no same-month replay.
Croatia retains a living remainder through the gap and sends it in May without another demand.
Halt releases the waiting remainder at home by the next monthly close, sends one accurately named German notice, adds one capital-located Records entry, hides the halt action and never restarts.
Repeat Bulgaria with states 106/184/731/803 and home state 107, outside German influence, after its March window, and with the reception host captured by SOV.
Expected: no home-province or wrong-authority enrollment and no rejected-route population debit.

4. **Costs, ordinary price and Black Friday 50/25 percent.** Select the existing sale scenario through the orchestrator's Event 026 setup, then compare every displayed camp price with the native debit, including the wider and Hungarian halt actions, the manual Auschwitz order and the administration commands.
Exercise a stale halt completion after its window and a refusable release order.
Expected: exact current quote debited, exact refund on rejection, no purchase credit for refunded orders and one credit for each kept purchase.
Inspect halt hover text for stability, war support, opinion and autonomy consequences.

5. **Greek and Italian boundaries.** Compare state 731 on 14/15 March 1943, Greek core state 47 on 23/24 March 1944, and Italian core state 114 on 15/16 October 1943, under valid German authority.
Use the real monthly pass and the manual transfer's source display/preflight.
Expected: no ordinary campaign or manual source before the boundary, eligibility from the boundary, and the tooltip gives the matching dates.
Use the existing October 1943 Danish rescue and August/September 1944 Łódź cases as route-preservation checks.

6. **Civil achievements.** As ENG complete the funded civil review with the Raj loyal and no revolt, and close active sites, then inspect achievement 65.
As USA end relocation authority and finish the court review during war in one copy, during peace in another, then complete the dated July 1948 property claims.
Expected: only the wartime review earns the before-victory receipt for achievement 66.
As ITA finish civil review, close desert camps, retain developed Libya and station an Italian division there.
Expected: achievement 68 reads those live requirements without demanding retired road/guard decisions.

7. **Twelve-month lifecycle and UI.** Run administration for twelve months with Chaos Meter enabled and disabled in separate copies, through ordinary delayed dispatch.
Expected: one administration pass per calendar month, no routine visible popup, maintenance before development, preserved output caps and at most two research awards per year.
Inspect before/after population and Deaths for movements, later losses, reform with incomplete provenance, capture, annexation and re-release, then use `savecheck` for persistence.
Expected: equal source debit/destination credit for transport, each death once under its original responsible country, no population restoration from closure, and one restarted timer after re-release.
Review Administration, Locations, Records and all five pickers at 1280x720, 1920x1080 and 1920x1080 with UI 1.25.
Expected: readable costs/reasons, no overlap/clipping/raw key, selected-row highlight, long-name ellipsis/full tooltip, and readable halted-transport history.
Finally observe the full Raj security mission, German GEN/RK creation, German manual-order and killing-role choices, partner answers, and USA/Soviet/Italian release choices.
Record actual AI observations beside the conditional probability evidence rather than equating scores to campaign frequencies.

## Skills

Used: events, decisions/missions, scripted GUI, event assets for vanilla image inspection/reuse, subagent routing, shared Git commit and save inspection.
No focus, MTTH, super-event, portrait or model surface was edited, and no skill was created or modified.
