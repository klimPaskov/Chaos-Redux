# Event 26 Black Friday completion baseline

Audit snapshot: 2026-08-29 19:55 +03:00, repository revision `f0127acc1`.

Overall status: **blocked / not implemented**. The accepted Black Friday specification is complete, but the runtime still contains the old desert-industry Event 26. No completion claim is supportable. The only Black Friday production evidence present at this snapshot is staged visual work plus read-only localisation and asset handoffs; none is installed or wired at runtime.

## Evidence boundary

- This was a read-only source and artifact audit. No gameplay, localisation, UI, asset, achievement, workbook, or catalog source was patched.
- The only file written by this auditor is this handoff.
- The worktree contains unrelated concurrent work. No unrelated file was reverted or modified.
- The configured MCP server is declared at `.codex/config.toml:11-14`. The parent runtime exposed no direct HOI4 callables, so the mandatory weighted pass was routed through a `fork_context=false` `chaosx_ai_probability_auditor`. That worker reached the MCP server, but event-option probability inspection and structural event inspection timed out; event rendering returned partial artifacts and custom-pool inspection returned source discovery only. Mandatory engine evidence therefore remains incomplete; source inspection below is not treated as equivalent evidence.

## Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Accepted specification | **Finished design** | `docs/specs/026_black_friday_specs/README.md:32-40` explicitly identifies the package as accepted design, not implementation. All Parts 1-9, prompts, catalog brief, registry template, and closure were audited. |
| Accepted-plan disposition | **Finished design; queued implementation** | The improvement closure is already incorporated and requires no separate addendum (`026_black_friday_improvement_loop_closure.md:31-43`). Its implementation tasks remain undone. |
| Event identity and chain | **Blocked / old implementation active in source** | `events/026_industry_to_desert.txt:23-36` keeps `chaosx.nr26.1` as a hidden desert dispatcher; `:45-106` keeps the desert report and options. No `events/026_black_friday.txt` exists. |
| Friday reservation lifecycle | **Blocked / absent** | No Black Friday reservation, Friday activation, chaos-change activation, snapshot, expiry, cancellation, or terminal-cleanup identifiers exist in runtime text. The generic dispatch records fire-once completion immediately after dispatch (`common/scripted_effects/chaosx_settings_effects.txt:4794-4821`; `common/scripted_effects/chaosx_logic_effects.txt:1086-1110`), which cannot satisfy reservation-without-history. |
| Save/reload state | **Blocked / absent** | No persistent reserved, active, snapshot, activation, expiry, force-disqualifier, achievement-progress, or paid-refund state exists for Event 26. The eight Part 8 save checkpoints therefore have no implementation evidence. |
| Multiplayer, tag switch, annexation | **Blocked / absent** | The shared daily hook has generic tag-switch tracking (`common/on_actions/chaosx_on_actions_system.txt:59-129`) but no Event 26 status refresh or global sale synchronization. The old event selects a country/state scope (`events/026_industry_to_desert.txt:30-38`) rather than owning actorless global sale state. |
| Disable, re-enable, pause, manual, force, terminal | **Blocked / absent** | Event 26 has no special lifecycle integration. Generic manual dispatch is at `common/scripted_effects/chaosx_settings_effects.txt:1758-1767`; Event Details permits force mode or chaos eligibility at `common/scripted_effects/chaosx_events_log_effects.txt:1509-1520`; neither records the required ordinary/manual/force distinction or achievement disqualification. The daily timer merely stops under `world_end` at `common/on_actions/chaosx_on_actions_system.txt:132-165`; it does not clean a reserved or active sale. |
| Event-system registration and pacing | **Partial shared base; Event 26 wrong** | ID 26 remains Minor Fire-Once but is labelled `MOVE INDUSTRY TO DESERT` (`common/scripted_effects/chaosx_logic_effects.txt:235-250`). It receives the default lowest chaos tier because the registry only special-cases White Peace (`:156-175`), not the required 200-chaos gate. ID 26 is absent from the default-enabled allowlist (`common/scripted_triggers/chaosx_settings_triggers.txt:10-32`) and is therefore still queued disabled by `common/scripted_effects/chaosx_logic_effects.txt:349-363`. No reservation path preserves the already-reset timer or delays history/pacing until Friday. |
| Universal discounted-cost framework | **Blocked / absent** | Runtime text contains no `black_friday`, `universal_cost_modifier`, `cost_surface_registry`, `payment_ratio_bp`, or `five_departments` contract. There is no shared quote, affordability, payment, commit, refund, display, source-composition, upward-quantization, or per-resource adapter API. |
| Universal cost registry | **Blocked / template only** | `026_black_friday_cost_surface_registry_template.md:3-20` still contains `To be recorded` metadata and one `Example only` row. Every family summary is blank at `:53-74`; no Strategy A-D dispositions, engine-inaccessible evidence, baseline/evolution/save tests, or final-commit sign-off exists. |
| AI and weighted probability | **Blocked / unresolved** | The old report still has `ai_chance = 100` and `0` at `events/026_industry_to_desert.txt:52-54` and `:104-107`; Event 26 also remains in the weighted fire-once pool at `common/scripted_effects/chaosx_logic_effects.txt:235-250`. The probability auditor's option inspection timed out after 180 seconds. Custom-pool discovery returned `no_weighted_surfaces`, zero candidates, and no adapter, so normalization remains unresolved. No Black Friday source or evidence exists for `bf_ai_01` through `bf_ai_08` (`026_black_friday_spec_part_5_ai_multiplayer_balance_and_exploit_controls.md:33-50`). |
| Event Log and Event Details | **Partial shared selectors; Black Friday missing** | ID 26 name selectors exist, but resolve to stale `chaosx.event_name.26: "Industry to Desert"` (`localisation/english/chaosx_event_names_l_english.yml:28`). Event 26 has no Event Details description branch and falls through to the generic placeholder (`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6610-6618`; text at `localisation/english/chaosx_gui_l_english.yml:616-617`). No Reserved/Active Today status exists; only generic `N/A` exists at `chaosx_gui_l_english.yml:533-537`. |
| Actorless history and evolution | **Partial generic actorless base; Event 26 payload absent** | The logger defaults to no actor (`common/scripted_effects/chaosx_events_log_effects.txt:198-200`), but actorless history falls through to `Actor: Unattributed` (`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:801-804`; `chaosx_gui_l_english.yml:592-596`). No Event 26 history payload, Evolution I registry/log, preview, title/body/summary, stage/tier, or disabled-evolution behavior exists. |
| Localisation and stale identity | **Blocked / old text remains** | `localisation/english/026_industry_to_desert_l_english.yml:2-11` still owns Desert Industry, Operation Desert Forge, both options, and `chaosx.news.27`. No Black Friday localisation file or key family exists. The read-only `localisation_baseline.md` handoff identifies the required branches but patches nothing. |
| Old news and GFX cleanup | **Blocked, with shared-consumer caveat** | Event 26 still triggers `chaosx.news.27` (`events/026_industry_to_desert.txt:101`), defined at `events/_chaosx_news.txt:339-355`. Old report/news sprites remain at `interface/chaosx_pictures.gfx:135-157`. `GFX_news_desert` is also consumed by Event 40 at `events/_chaosx_news.txt:650-665`, so cleanup must preserve or deliberately reassign that unrelated consumer rather than blindly deleting the shared sprite. |
| Achievement contract | **Blocked / absent at runtime** | No `Five Departments` achievement definition, localisation, transaction ledger, natural-selection gate, family crediting, refund handling, force/manual/AI disqualifier, expiry cleanup, or runtime achievement DDS exists. Runtime searches of `common/achievements/chaos_redux_achievements.txt`, `interface/`, and `localisation/english/` found no Event 26 achievement identifiers. |
| Visual assets | **Partial staging; blocked for runtime** | Report source/preview/DDS and contact-sheet evidence are staged under `docs/assets/026_black_friday/`; `generated_report_art.md:3`, `:37-39` records `needs_user_review` and parent promotion/wiring. `icon_art.md:3`, `:34` owns the staged idea icon and achievement triplet, records native ImageGen provenance, the grey/not-eligible alpha-repair fallback, hashes, DDS checks, and leaves review/promotion/wiring to the parent. Both contact sheets were visually inspected and are legible at review scale. No DDS is promoted to `gfx/event_pictures/026_black_friday/`, `gfx/interface/ideas/026_black_friday/`, or `gfx/achievements/`, and no runtime sprite registry or consumer wiring exists. |
| Dedicated scripted GUI | **Not applicable by accepted design** | The spec uses the existing Event Log, Event Details, popup, and temporary status surfaces and explicitly declines an event-owned mechanic window (`026_black_friday_spec_part_9_implementation_crosswalk.md:162`; `026_black_friday_subagent_review_record.md:24`). A `chaosx_event_ui_worker` handoff is therefore not required unless implementation later introduces a dedicated Event 26 scripted GUI. Mandatory Event Log/event MCP evidence remains required. |
| Event documentation and API documentation | **Blocked / absent** | `docs/events/026_black_friday.md` and universal discounted-cost/API documentation do not exist. No completed cost registry, asset crosswalk, implementation handoff, or validation report exists. |
| Catalog and exports | **Blocked / stale** | Read-only workbook inspection found `Events!A27:N27` as `26 / Desert question / ... / Minor Fire-Once / Chaos level 1 / To Be Reworked`. The export mirrors this at `docs/spreadsheets/chaos_redux_events_catalog.csv:113`. No current no-ID Black Friday backlog row was found, so that older conflict is already absent and must not prompt deletion of an unrelated row. The required Black Friday wording, tier encoding, Evolution I mirror, and `Needs Testing` status are missing. |
| Part 8 acceptance | **Blocked / no execution evidence** | Part 8 defines 94 numbered scenarios: BF-T 19, BF-P 6, BF-R 13, BF-C 6, BF-X 14, BF-F 20, BF-M 6, and BF-U 10, plus the eight Part 5 AI scenarios and eight save/reload checkpoints. No scenario has implementation or live evidence. Several fail by direct source inspection because the old event, stale catalog, absent API, absent achievement, and absent runtime assets remain. |

## Lifecycle and transaction checklist

- [ ] Chaos 200 eligibility and `N/A` below threshold.
- [ ] Atomic, idempotent global reservation that does not create history, fired state, pacing pressure, popup, or a second timer reset.
- [ ] Existing bounded daily-pulse Friday activation plus same-Friday chaos-change activation.
- [ ] Reservation survival below 200, pause, annexation, and tag switch.
- [ ] Disable-while-reserved cancellation and re-enable return to the pool.
- [ ] Disable-while-active completion without duplication.
- [ ] Ordinary manual launch following Friday/reservation rules.
- [ ] Force launch using the same activation/expiry path with persistent achievement disqualification.
- [ ] One activation snapshot: 5000 basis-point payment ratio at baseline, 2500 at Evolution I when activation chaos is at least 600 and the evolution is enabled.
- [ ] One synchronized popup per human and bounded active-status refresh for joins/tag switches.
- [ ] Next-daily-tick expiry, source-specific removal, refundable-payment survival, and explicit terminal cleanup policy.
- [ ] Shared quote/affordability/payment/commit/refund/display source with upward quantization and one positive minimum quantum.
- [ ] Separate treatment for zero, negative/reward/refund values, multi-resource components, and source composition.
- [ ] One complete final-commit registry row per reachable Vanilla and Chaos Redux voluntary purchase surface.
- [ ] Five Departments natural-selection achievement and per-country five-family ledger.

## Accepted-plan and handoff disposition

- **Accepted and promoted into specs:** the improvement-loop closure (`026_black_friday_improvement_loop_closure.md:41-43`). It is not an unresolved expansion plan.
- **Accepted design, not implementation evidence:** the historical role review says no subagent process was available in that earlier environment (`026_black_friday_subagent_review_record.md:3-7`). Its conclusions informed the specs but do not prove patches or MCP validation.
- **Informational baseline:** `subagent_handoffs/localisation_baseline.md` is a read-only source audit and explicitly reports missing MCP routes and no patched surfaces.
- **Pending review/promotion:** `subagent_handoffs/generated_report_art.md` owns only the report image and explicitly leaves visual approval, runtime DDS promotion, and `.gfx` wiring to the parent.
- **Pending review/promotion:** `subagent_handoffs/icon_art.md` owns the staged idea and achievement families, records the native-alpha failure and fallback repair, and leaves visual approval, runtime DDS promotion, `.gfx` registration, and gameplay/achievement wiring to the parent.
- **No implementation disposition exists:** there is no gameplay implementation handoff, universal-cost owner handoff, decision/mission coverage audit, spreadsheet-worker handoff, or completed acceptance report.

## Meaningful validation performed

- Read all Event 26 specification parts, prompts, registry template, catalog brief, manifest, source/review records, and improvement closure.
- Traced current ID 26 registration, chaos eligibility, default-disable behavior, automatic/manual/force dispatch, fire-once history/pacing, shared daily/tag hooks, Event Log selectors, actor fallback, Event Details fallback, evolution surfaces, old news, and sprite consumers.
- Performed a runtime-text search for Black Friday, universal-cost, payment-ratio, registry, and achievement identifiers; none exists outside design/staging documentation.
- Opened the authoritative XLSX read-only and inspected `Events!A27:N27`; compared its current export row.
- Checked all required proposed runtime paths. Event script, localisation, sprite registry, report DDS, idea DDS, and achievement triplet are absent from runtime locations.
- Visually inspected both available asset contact sheets. This confirms reviewable staged images only; it does not replace promotion, wiring, MCP render, or in-game evidence.
- Confirmed there is no changed Event 26 runtime revision in the scoped worktree at the snapshot, so no source patch can be dispositioned as implemented.

## MCP and probability blockers

1. `hoi4.event_inspect` was attempted by the probability auditor with the correct Event 26 file selector and timed out after 180 seconds. The event chain therefore has no completed inspect diagnostic.
2. `hoi4.event_render` returned partial old-event structural evidence at revision `fc004230aebc47f013434598a54b3f98da50c59b8fe79c1e1f2272b4eea95d23`:
   - Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdfb1d877dcceed2133d7b0f4556d6191bf02f3e8f4d3e61b1b222252bd0b732/5317da312454061d7473e9912f2f9bca5495dabbb2f26d3b231b845531b05e31/event-options-fc004230aebc-manifest.json`
   - SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d5e71561409a8982f6e6cb588b21057a246b73e5de0680e4f799a444fc217c9/5baa55a68dd2360c6b9609827cc74d50364bf261e198649ca6c78252ab6f52d9/event-options-fc004230aebc.svg`
3. `hoi4.probability_inspect` for `chaosx.nr26.2` option `ai_chance` timed out after 180 seconds. Inspection of `common/scripted_effects/chaosx_logic_effects.txt` succeeded only as source discovery at revision `e8a296e6117af0bae60cf8fa679937a1585b17c13eeddf45063f5d76707f65d7`, source hash `2ffd392d3e89c49edf44ee2ced4f1a48f5302e1154625413c81fcb660680f8a7`, and reported no weighted surfaces or adapters:
   - Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f668c1ee7c8b3e5d3732b25066c0137625cd1697db07c8bda0d4135ee1515f48/91203783d79ab2971843161b2bb47432433023d8e4d31bc70e49152862e32dfe/probability-inspect-2ffd392d3e89.json`
4. All eight `bf_ai_*` scenario conclusions remain unresolved. No `probability_evaluate`, sweep, probability-render, or comparison artifact exists.
5. No changed Black Friday revision or Black Friday baseline artifact exists, so `hoi4.event_compare` and `hoi4.probability_compare` were not run. Once an implementation revision exists, before/after event comparison and the same named `bf_ai_01`-`bf_ai_08` probability scenarios are mandatory; source-only reasoning cannot close either gate.

## Remaining blockers and recommended next actions

1. Keep ID 26 disabled and assign a parent-owned implementation plan for the special reservation/activation dispatch. Preserve `chaosx.nr26.1` and Minor Fire-Once classification, but delay fired/history/pacing updates until Friday activation and avoid a second timer reset.
2. Implement the universal cost-source and transaction API first, then complete the exhaustive registry against the exact final commit. Route each decision/mission and other weighted owner through its required auditor; do not accept a sample registry or undisclosed Strategy D fallback.
3. Implement persistent lifecycle, save/reload, multiplayer, tag/join refresh, disable/manual/force behavior, expiry, refunds, and one documented terminal-cleanup rule.
4. Complete Event Log/Event Details/history/evolution/status and achievement wiring, replace all stale desert identity, and preserve Event 40's current use of `GFX_news_desert` during cleanup.
5. Obtain explicit report-art review, a complete icon-artist handoff for the idea/achievement families, family manifests/prompts/fallback disclosure, then promote and wire all runtime DDS files.
6. Add Event 26 and universal-cost documentation. Update only the authoritative workbook, set the implemented row to `Needs Testing`, and regenerate all CSV exports.
7. Restore the mandatory HOI4 MCP routes and run event inspect/render/compare plus probability inspect/evaluate/render/compare. Then execute and record all Part 8 scenarios and save checkpoints. Event 26 cannot be re-enabled or claimed complete before these gates pass.

No simplification is accepted by this audit. The current state is a design-complete, implementation-blocked baseline.
