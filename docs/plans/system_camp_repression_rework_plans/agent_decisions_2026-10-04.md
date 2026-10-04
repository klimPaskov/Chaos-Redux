# Camp workstream agent decisions, 2026-10-04

Authority: the user granted the implementing engineer full authority to take the recommended, spec-consistent option, record it here, and continue without asking for input.
Each entry names the decision, its basis in the accepted contract (`administration_redesign_2026-09-06/accepted_implementation.md` and the handoff `administration_redesign_2026-09-06/handoff_to_claude_2026-10-04.md`), the implementation, and its limits.
Disposition of every entry below is `implemented` unless it says otherwise; source-contract suites are not engine acceptance, and every in-game check is `needs_live_game`.

## 1. Publish the implemented working-tree tranche

Decision: commit the implemented administration, occupation, country, civil, dispatch, UI, famine, USA-release and Mengele-retirement source even though the stopped thread had gated publication on GUI, AI and native evidence.
Basis: the game already loads the working tree, live verification belongs to the orchestrator, and HEAD held the passive origin library without its callers.
Implementation: commit `72aa7ba56e031229c9eb3b550a4696ecbd38c6dc` (source, 69 files, shared files by hunk: the Event 005 UWR aftermath hunks and the camp lines of `_chaosx_events_l_english.yml` and `chaosx_decisions_l_english.yml`); commit `b0a0f9ea4ea8cad2896328f47bc664f0e01ab151` (plans, suites, evidence and spec reconciliation, without the duplicate `mcp/after/gui351_current_matrix` copy).
Validation: a static check of the published tree found every scripted effect, trigger, constant, localisation key and event id called by the camp files defined, no duplicate camp definitions, and no `$PARAM$`, `clear_temp_variable`, `<=`, `>=` or unguarded `remove_dynamic_modifier`; foundation, major, institutional, dispatch, famine shortfall, Soviet release, observer, owner, country/civil, closed archive, lifecycle, Records projection, USA and native-cleanup suites passed from a scratch copy.
Inbox item #3 (parameter-block calls to `camp_origin_commit_endpoint_observation`) is published in `72aa7ba56`.

## 2. Spent origin generators cannot rewrite common/

Decision: keep the five one-shot `occupation/integrate_*.py` generators as provenance, but make each stop immediately when run, and change the movement generator's template to the temp-variable call form.
Basis: their output is committed and later hand edits supersede it; rerunning the movement generator would have re-emitted the forbidden `camp_origin_commit_endpoint_observation = { OPEN_SEQUENCE = ... }` block.
Implementation: committed in `b0a0f9ea4`.

## 3. Reform closes hosts with sticky provenance as records-incomplete

Decision: a host that carries `camp_origin_ambiguous`, `camp_origin_baseline_unverified`, `camp_origin_transaction_unresolved` or `camp_origin_counter_regressed` no longer blocks national, generic or civil reform. Reform closes it through the existing terminal branch of `camp_admin_close_site` (custody) or `camp_occ_close_state` (occupation).
Basis: nothing clears those flags, and `camp_admin_country_sites_ready_for_reform` gated every reform route, so one unexplained loss at a mixed-origin host permanently stranded a country. The user's 2026-10-03 PAUSE decision forbids assigning the unknown loss by newest-first, proportional or unknown-pool rules and forbids recovering origin-specific actions; a terminal closure claims no per-origin survivors, moves no population and attributes no deaths, so it does neither.
Behaviour: release, transfer and per-site dismantlement stay paused at flagged hosts while they operate (they still require `camp_origin_host_provenance_ready`). Reform sets `camp_admin_closed`, `camp_origin_ambiguity_terminal` and `camp_admin_closed_records_incomplete`, records one `records_incomplete_closure` history entry ("Closed; survivors released without complete origin records"), keeps the frozen rows, original authority, deaths and history, creates no civilian replacement target, and changes no population or Deaths counter. Genuinely inconsistent ledgers without a sticky reason still block reform.
Out of scope: the legitimate labelled restoration provider (handoff priority 5) remains unimplemented.
Implementation: `camp_origin_host_records_incomplete` (origin triggers), `camp_admin_known_site_reformable` and the relaxed `camp_admin_country_sites_ready_for_reform` (administration triggers), generic availability (integration triggers), `camp_admin_reform_site` and the terminal OR in `camp_admin_close_site`, generic reform row check and history, the new history kind and Records, conditions and reform tooltip text; paired docs updated. Suites extended: closed archive (new reform case, capture/evidence/annexation and 1001-entry cases), country/civil (GER country reform and ENG civil review beside an ambiguous occupation host), owner integration (occupation-only ambiguous host closes without release, debit or death) and foundation (generic order availability and payment with a sticky host).
Limits: `needs_live_game` for the native reform click, the Records history entry and the tooltip text.
Commit: `19b19be08a82d7aebf00a24ee81ad5651c095360`.

## 4. Retired Mengele foreign purchases are fully hidden

Decision: `import_subjects_from_japanese_china`, `import_subjects_from_india` and `import_subjects_from_africa` keep their IDs for save compatibility but are never visible, targetable or available for players or the AI.
Basis: the accepted retirement says no fabricated foreign transport replaces them. Before administration started they stayed visible and clickable, completed instantly with no `days_remove` and only refunded their own cost, so the player saw a decision that did nothing and the AI retook it after every re-enable.
Implementation: `allowed`, `visible`, `target_root_trigger` and `available` are `always = no` and `ai_will_do = { base = 0 }`; the unreachable completion refunds the charged Black Friday price variable rather than the ordinary constant. Nothing else in the Mengele category changed and the inert import helpers are unchanged. The retirement handoff and the import AI handoff record the change; the AI audit is a zero-eligibility result. The retirement fixture asserts the hidden gates and zero weight (33 scenarios passed).
Commit: `4bc95e81d9e7c9fc99f0f718c1ee01dd14dc073e`.

## 5. Annexation and terminal cleanup clear the dispatch timer

Decision: `camp_admin_integration_close_country` (shared by annexation and special-country exclusion) clears `camp_admin_dispatch_timer_active` and the new `camp_admin_dispatch_timer_earliest` date, and every scheduled call records that earliest date.
Basis: the flag was cleared only inside `camp_administration_country.2`; an annexed country's pending event may never arrive, so a re-released country was never rescheduled and its administration stopped when the Chaos Meter setting is disabled.
Behaviour: a re-released country starts a fresh chain on registration. If the old event is still delivered, it arrives before the stored earliest date (period minus a one-day tolerance, converted with `chaosx_convert_days_to_date_offset`) and stops without running the month or rescheduling, so one timer stays outstanding; the calendar month guard still blocks a double monthly run. Older saves without the stored date keep their timer as current.
Implementation: `camp_rework_schedule_country_timer` (rework effects), `camp_admin_dispatch_timer_is_due` (integration triggers), the stale branch and helper reschedule in `camp_administration_country.2`, `camp_admin_dispatch.due_tolerance_days`, dispatch documentation; the dispatch fixture adds annexation then re-release before and after the stale event (one outstanding timer, no duplicate month).
Limits: `needs_live_game` for engine delivery of delayed events to annexed and re-released countries.
