# 020 The Black Plague release review, 2026-10-05

Status: source repairs implemented; release sign-off remains incomplete because required current-source MCP and live evidence is unavailable.

## Accepted decisions and implementation

- Accepted under the user's G2-G7 authority: distinguish runtime initialization from an actual outbreak, publish one outbreak news line, warn exposed countries once, and simplify actual emergency costs.
- Implemented: natural and shared pool availability use black_plague_outbreak_has_begun rather than the initialized system flag.
- Implemented: the requester owns the selected-state pointer across bootstrap, revalidates it and clears it on exit.
- Implemented: only a state commit publishes natural-start success; .904 explains active, eradicated, terminal or unsuccessful-origin rejection.
- Implemented: recognition names the district and country and marks the district public on the disease map.
- Implemented: .15 and .16 aggregate nearby and domestic cases by human country and freeze each first place name on its recipient.
- Intentional notification simplification: severe-origin duplicate, first containment/cure/recovery broadcasts are suppressed; state progression and the containment interface retain those outcomes.
- Implemented: reconstruction news following eradication requires Rat King defeat.
- Accepted: the existing national response GUI uses Countermeasure Progress, National Deaths and Response Capacity; Medical Reserve is available through the national decision/stockpile surface.
- Implemented: Rat Nation archetype requirements identify RTA rather than calling it the Rat Kingdom, and both rat trees have native navigation shortcuts.
- Cost changes are traced in subagent_handoffs/decision_costs_2026-10-05.md, including actual factory and response-capacity reservations.
- Implemented: .906 returns the post-state global pass to a country ROOT and consumes each pulse sequence once, correcting state-scope news and country effects.
- Raw spread weights, progression timers, mortality, country routes, unit packages, world-end conditions, achievements and super-event assets were retained.

## Owned files and surfaces

- `events/020_black_death.txt`
- `common/scripted_effects/020_black_plague_effects.txt`
- `common/scripted_triggers/020_black_plague_triggers.txt`
- `common/scripted_effects/chaosx_logic_effects.txt (one owned line)`
- `common/national_focus/020_black_plague_rat_focus_tree.txt`
- `common/national_focus/020_black_plague_rat_king_focus_tree.txt`
- `localisation/english/020_black_plague_reports_l_english.yml`
- `localisation/english/020_black_plague_requirement_flags_l_english.yml`
- `localisation/english/020_black_plague_rat_focus_l_english.yml`
- `docs/events/020_black_plague/overview.md`
- `.tools/test_event020_outbreak_entry.py`

- `common/scripted_effects/020_black_plague_shared_response_effects.txt`
- `common/scripted_effects/020_black_plague_terminal_response_effects.txt`
- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`
- `common/scripted_triggers/020_black_plague_terminal_response_triggers.txt`
- `common/script_constants/020_black_plague_shared_response_constants.txt`
- `common/script_constants/020_black_plague_terminal_response_constants.txt`
- `common/decisions/020_black_plague_shared_response_decisions.txt`
- `localisation/english/020_black_plague_response_l_english.yml`

## Evidence and limits

- Read-only save evidence: qa_001_fresh_head.hoi4, USA, 1936.1.1.12, and qa_evt020.hoi4, USA, 1936.2.28.3, both HOI4txt v1.19.2.0.a729.
- Both saves have initialized/active runtime flags dated January 1, zero active/established states and plague deaths, no origin targets and no outbreak receipts.
- Commands used the save-inspection info/find workflow under flags, variables, countries/USA, saved_event_target and states; saves were not modified or committed.
- The baseline/end comparison proves that initialization alone cannot exclude the first natural outbreak; it does not identify which earlier initializer produced that state.
- Eight source tests execute production entry gates and notification helpers, proving initialized-empty acceptance, actual/terminal exclusion, country deduplication, frozen notice locations and once-per-sequence country aftermath dispatch under declared fixture boundaries.
- Current-source response GUI inspection/render and event/focus/probability evidence remain blocked by route timeouts; the status getter's production rendering is unresolved.
- The source route inventory covers 52 RTA and 71 RTX focuses and resolves registered runtime assets.
- The research-note request for a personal sovereign-name pool has no acceptance basis established by this pass; the existing Rat King identity remains an unresolved design claim, not an implemented pool.
- Portrait/model provenance and live playback remain evidence limits, despite present runtime files.
- A nested focus-weight auditor violated the no-refresh constraint with four refresh=true requests; no payload or usable evidence was returned, the calls were stopped and their results were discarded.

## Exact orchestrator checks

- Load qa_001_fresh_head as USA and force Event 020 from Settings, then advance one day: expect one world news naming a real origin, public disease-map marking, and any applicable local notices.
- Repeat direct chaosx.nr20.1 while an outbreak exists, after eradication, and during a terminal state: expect the appropriate .904 explanation and no second natural outbreak.
- In the active outbreak fixture, establish a public infected Canadian state bordering USA using the production phase helper: expect one Plague Near Our Border report to USA, even when several border states qualify.
- Establish a second neighbouring case, then a US case and another US case: expect no repeated nearby report and exactly one domestic report preserving the first domestic location.
- Run the seven-day scheduler for two months: source counts and state phases should advance without repeated opening or local notices.
- At 1920x1080 and 1366x768, UI scale 1, inspect response 0/0, active, exhausted and 100-percent states: labels must resolve, meter bounds must fit, and warning/unorganised labels must remain exclusive.
- Exercise ordinary, royal and last-response actions at exact quoted reserves; verify every direct debit and reservation, payment rejection, completion and cancellation release.
- Use the existing Rat/King scenario to inspect the two focus trees and shortcuts, counters, unit actions/audio, five evolution rows, public terminal controls and defeat aftermath.

## Catalog and assets

The catalog workbook and exports were not edited.
Catalog alignment notes are in catalog_changes_pending.md.
Existing runtime art, sound, flags, portraits and models were reused.
No live HOI4 session or desktop window was opened by this task.

## Required reference evidence

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:117-150`, local source SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-328`, local source SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2943-2967`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:5053-5074`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3624-3640`, local source SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:146-167`, local source SHA-256 `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/germany.txt:42-80`, local source SHA-256 `4cfd72972e19bcc560684dfc2f170e62ce786153ee01cf06ee7acc9609996095`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:3997-4016`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:530-530`, local source SHA-256 `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.

Reference context/search/read routes returned some citations; failed and omitted sections were read locally.
Context inventories do not establish rule or engine coverage.
The connected service version and standalone viewer availability were not independently confirmed.
No repository-wide state-flow or helper-expansion query was used.

## Remaining source review risk

The 26 ordinary state actions share a visibility gate but have distinct target predicates.
Their exact simultaneous visible count remains unresolved without decision/GUI scenario evidence.
No source-only action count is presented as proof of clipping or native panel overflow.
