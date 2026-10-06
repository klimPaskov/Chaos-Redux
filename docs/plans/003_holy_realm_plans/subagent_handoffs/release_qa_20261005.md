# Event003 Release QA Handoff — 2026-10-05

## Status

Source remediation is complete for the bounded Event003 files listed below. Release QA remains incomplete because the HOI4 event, focus, decision, GUI, and probability inspection routes timed out without artifacts, the shared settings gate suppresses no-host entry before the owned fallback can run, catalog alignment is pending, and several design and runtime questions remain unresolved.

## Owned files changed

- `events/003_the_holy_realm.txt`: adds visible no-host fallback `chaosx.nr3.5`; routes the three formation paths through one refuge-news helper; preserves the Tibet-first host choice and Bhutan/Nepal eligibility only after Tibet is gone; corrects the `.nr3.2.e` indentation; removes the repeatable `.nr3.110.b`/`.nr3.111.b` PP farming scale.
- `common/scripted_effects/003_holy_realm_effects.txt` and `.md`: adds `holy_realm_publish_refuge_news`, which sets `holy_realm_refuge_news_sent` before firing `chaosx.news.9`; makes Bhumi milestone PP, CP, and stability rewards one-time.
- `common/script_constants/003_holy_realm_constants.txt`: centralizes Bhumi milestone thresholds/rewards, bounded PP refunds, peacekeeping minimum supplies/manpower, and reduced teaching PP outcomes.
- `common/decisions/003_holy_realm_decisions.txt`: uses capped recurring PP refunds below the maximum Black Friday quote; prevents repeat use of the Bodhisattva-to-council action; makes exact resource checks inclusive; supplies readable cost/gate tooltips; states Buddha power charge costs in player-facing descriptions.
- `common/scripted_triggers/003_holy_realm_triggers.txt`: peacekeeping affordability now compares `manpower_k >= 6`, infantry equipment `>= 800`, and support equipment `>= 80`.
- `common/on_actions/003_holy_realm_on_actions.txt`: replaces broad generic `on_daily` with bounded `on_daily_TIB`, `on_daily_BHU`, and `on_daily_NEP` callbacks, each checking Holy Realm status and the active Bodhisattva mandate before preserving the doctrine pulse.
- `common/national_focus/003_holy_realm.txt`: adds the six existing, localized filter priorities and maps them onto the matching existing focuses. Existing focus prerequisites, hidden branch visibility, positions, vanilla filters, and AI weights remain unchanged. The assigned filters are Bodhi, Teaching, Governance, Compact, Nirvana, and Hidden.
- `localisation/english/003_the_holy_realm_l_english.yml` and `003_holy_realm_requirement_flags_l_english.yml`: rewrites visible status, decision, event, tooltip, and event-detail text to describe current people, places, costs, and consequences; removes bookkeeping/update wording; aligns Final Silence threshold prose to Chaos strictly greater than 1000; retains UTF-8 BOM.
- `docs/events/003_holy_realm/overview.md` and `systems/buddhahood_progression.md`: documents the owned behavior above.
- `common/scripted_effects/003_holy_realm_effects.md`, `docs/plans/003_holy_realm_plans/agent_decisions_2026-10-05.md`, and `catalog_changes_pending.md`: records system behavior, accepted QA edits, and the deferred workbook edit.

No shared settings, shared GUI, shared Black Friday price, achievement, shared event log/details framework, GFX, interface, or spreadsheet file was edited. No AI weights or other probability-bearing values were changed.

## Balance and route findings

The previous three mutually exclusive formation paths could each fire the Holy Realm refuge news. They now set a campaign-wide sent flag before firing the one shared report, so source has one `.9` broadcast inside the helper and three helper call sites. The supplied run screenshot shows one `.9` popup; it does not prove every recipient or all branch permutations.

Bhumi advancement could pay its PP, CP, and stability milestone grants again each time the effect ran. Each milestone is now guarded by a one-time country flag and uses constant-backed threshold/reward values. The repeatable teaching choices that returned 75 or 100 PP are now 5 PP, while their teaching, reach, legitimacy, and Bhumi consequences remain. The recurring Scribes, Border Courts, and Open Lotus Audit refunds are now bounded below their maximum discounted prices.

Exact-cost checks for Command Power, equipment, and manpower now accept a country holding exactly the displayed requirement. The Mandala peacekeeping cost reads 6,000 manpower, 800 infantry equipment, and 80 support equipment. The Bodhisattva council memory flag now blocks a repeated decision.

The daily pulse previously ran under generic `on_daily`, which iterates every country. The replacement runs only for TIB, BHU, or NEP and only when that country is an active Holy Realm host. Offline On Actions wiki guidance and vanilla tagged daily callbacks support the bounded form; no world scan was added.

The six custom focus filters were authorized for this QA pass because the accepted focus specification lists these navigation groups, the matching labels already existed, and current focus source had omitted them from its active priority/navigation table. The change assigns only existing focuses that match the established route semantics; no route family or AI behavior was added.

## Live evidence inspected

- `C:/Users/klimp/Videos/chaos_redux_trailer/records/qa/evt003_sheet.jpg` was inspected directly.
- `C:/Users/klimp/Videos/chaos_redux_trailer/screenshots/evt003_pop00.png` shows the USA 1936 run's 10 January report with readable, unclipped Holy Realm refuge news.
- `evt003_pop01.png` through `evt003_pop06.png` are unrelated vanilla popups in the contact sheet. `evt003_pop07.png` shows the map on 21 March, more than two months after the run begins.
- `C:/Users/klimp/Videos/chaos_redux_trailer/screenshots/cs/GP07_news_holy_realm_refuge.png` was also inspected.
- These artifacts show one Holy Realm refuge news popup in that recorded run. They do not establish all recipients, hidden host branches, fresh-save forced-entry behavior, or the absence of duplicates in every chain.

No HOI4 session or desktop window was launched. The requested fresh USA 1936 forced-entry scenario was not run by this agent.

## MCP and reference evidence

- Narrow event inspect/render/compare requests timed out at 600 seconds. No event scenario artifacts, revision, coverage, or comparison were returned.
- Focus inspect/render requests timed out at 600 seconds. No final rendered layout or diagnostics were returned.
- Decision scenarios `usa_1936_entry`, `holy_realm_tibet_setup`, and `holy_realm_two_months` timed out at 600 seconds. No engine result was produced.
- Script validation did not return a result before cancellation. Weighted `probability_inspect` requests for event chances, MTTH, decision AI, focus AI, and AI strategy timed out; no `probability_compare`, normalized selection, scenario hash, or numeric balance evidence exists.
- `holy_mandala_category_container` inspect/render and GUI reference-context requests timed out at 600 seconds. No before/after screenshot or artifact exists. No layout file was changed; the in-game panel's visual review remains blocked.
- Offline Event modding wiki revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` was read at lines 180–229 and 703–852. Installed `effects_documentation.md` revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` was read at lines 2943–2967 for `country_event`. Offline Data structures revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` was read at lines 263–328 for event targets.
- Offline On actions wiki revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` was read at line 97 for `on_daily_TAG`. Installed `_documentation.md` was located at lines 7–19; direct local reading confirmed the tagged callback documentation, while the MCP section read timed out.
- Script Constants documentation was read locally from `documentation/script_concept_documentation.md` lines 216–252 and `common/script_constants/documentation.md` lines 1–120, revision `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C`.
- Decision modding offline wiki revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` and installed decision documentation revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` were retrieved for decision costs/availability/removal behavior.
- Focus search filter guidance was read from `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md` at `search_filters` and `search_filter_prios`. Vanilla generic focus structure was checked at `common/national_focus/generic.txt:1`.
- Tagged daily vanilla precedents were read at `common/on_actions/00_on_actions.txt:243` (SHA-256 `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9`) and `common/on_actions/07_nsb_on_actions.txt:1824` (SHA-256 `939EA1C0CC25C2CE4390D7DDA4A8AC84547978931FAE36C09D0FAB7D7EC79966`).

The full pre-edit owner-file copies are under `source_snapshots/release_qa_20261005/`; they cover the event, decisions, focus, on-actions, constants, scripted effects/triggers, and both edited localisation files. The requirement-flag YAML copy was restored from its initial unchanged content after its exact owned value changes were made.

## Remaining blockers and unresolved design

- **No-host entry is blocked upstream.** `common/scripted_effects/chaosx_settings_effects.txt:4047-4052` suppresses the Event003 candidate when `holy_realm_has_valid_refuge_host` fails, before the owned root can run through the settings selector. The `chaosx.nr3.1` valid-host trigger has been removed, so a direct forced entry can reach the owned `chaosx.nr3.5` fallback if host selection fails. Parent integration should add the player-readable shared unavailable reason: "No eligible refuge host is available. Tibet must be unavailable before Bhutan or Nepal can host." The shared selector currently prevents its fallback from surfacing through that path.
- The Nuclear Sutra decision still quotes `global.black_friday_price_pp_130` and applies a hidden 25 PP debit. The queued shared fix is a proper `pp_155` Black Friday quote, then switch the owner decision to that quote and remove the hidden debit. The shared price files are outside this ownership boundary.
- Three hidden decisions have no source caller/reveal route: `THR_bodhisattva_mission_refuge_circuit`, `THR_bodhisattva_mission_white_scarf_envoys`, and `THR_bodhisattva_mission_wounded_border`. Their positive AI weights cannot make them visible. Parent must decide whether they are obsolete or need an accepted activation design.
- `THR_bodhisattva_guard_pilgrimage_route` checks division presence on activation and expiry, not throughout its 60-day duration. No world iteration or weaker narrative substitute was added.
- The final-focus route and Event Details currently disagree over whether `world_end_final_silence`/super-event delivery is part of the Final Silence ending or whether it delegates to Fallout. No accepted decision resolves the nested spec versus current overview conflict.
- The main Mandala category and Final Silence panel need visual evidence. Their GUI reference/inspect/render requests timed out; no screenshot evidence was generated and no `chaosx_event_ui_worker` layout patch was made.
- Probability balance is unverified across 47 event option `ai_chance` blocks, 113 decision `ai_will_do` blocks, 63 focus `ai_will_do` blocks, direct host random selection, and 14 AI strategy packages. No weighted value was changed, so there is no post-patch probability comparison.
- Workbook `Events!C4` still differs from the revised game Event Details text and `Events!M4` remains `Needs Testing`. The catalog owner must update the workbook row and export the three CSVs using `python .tools/export_event_catalog_csv.py` after parent acceptance.
- The exact requested two-month live chain result and fresh forced-entry result remain unresolved; the supplied screenshots show a run through 21 March, but do not identify its full event choices or branch state.

## Checks run

- `python .tools/report_colour_audit.py --event 003` returned `total keys with colour: 0` after the final localization wording pass.
- The no-colour report covers in-scope Event003 report/title/body/option families and reachable scripted report strings.
- Required Event003 English localization files retain UTF-8 BOM.
- Source count: 47 event declarations with no duplicate event IDs or broken direct event references per the completion auditor; the event's 65 referenced textures resolved during its bounded asset scan.
- The post-edit source snapshot hashes are in the repo state and can be recomputed after parent integration. No commit or shared index operation was performed.

No completion claim is made for in-game behavior, probability balance, GUI layout, catalog alignment, or full route acceptance.
# Parent closure of shared integration

The Settings no-host gate now invokes the event-owned refuge-failure helper only for a manual request.
It sends `chaosx.nr3.5` and marks `chaosx_manual_event_failure_shown`, preventing a duplicate generic failure report.
The Nuclear Sutra fee is registered as one 155 PP native price and its hidden 25 PP debit is removed.
The parent reviewed the actual on-action diff: the bounded balance pulses use `has_power_balance` and `holy_realm_daily_doctrine_balance_pulse`, preserving the prior balance-of-power behavior.
These source changes resolve the shared requests above without establishing the still-missing MCP layout, probability, or live-game evidence.
