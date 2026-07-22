# Fallout NZL sea-road and Event Log completion audit

Date: 2026-07-22
Mode: read-only completion audit
Runtime boundary: HOI4 was not launched

## Verdict

| Surface | Verdict | Completion finding |
| --- | --- | --- |
| Numbered sea-road correction | **PASS** | The promoted current-generation licence, paid 90-day patrol-window loop, score pressure, AI reserve, cleanup, and fixed content counts are implemented without an activation caller or recurring poll. |
| Fallout country-memory Event Log correction | **PASS** | Dedicated history ids, type/filter 4, exact sequence-keyed snapshots, per-generation/per-transaction deduplication, partnered external rows, exact-sequence reload, generation-isolated Fallout package details, and all negative ownership boundaries are implemented. |
| New correction regression | **PASS / none unresolved** | Three defects found in an earlier audit snapshot were corrected before this final snapshot: reset no longer clears durable non-external dedup receipts, package-card live reads are scoped through NZL for every viewer, and the NZL card augments rather than replaces the base Fallout description. |
| Broader NZL Lifeboat pilot | **PARTIAL implementation; completion/activation FAIL** | The two promoted corrections are closed, but the package remains deliberately dormant and still has unresolved asset, conflict-ledger, allocator, vanilla-AI, runtime, map-return, and scenario-release blockers. |

The parent shorthand "90-day current-generation licence" is implemented in the promoted spec's more precise form: a permanent current-generation licence receipt plus one renewable 90-day patrol window.

## 1. Numbered sea-road correction: PASS

### Licence and operating window

- `fallout_nzl_license_every_sea_road` retains its immediate seven-point Sea-Lane Security reward, opens Last-Berth Closure, and calls the licence helper at `common/national_focus/fallout_nzl_lifeboat_focus.txt:288-304`.
- `fallout_nzl_activate_sea_road_licensing` writes the active flag and exact Fallout generation and opens Fishery Quota Compact at `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:75-79`.
- `fallout_nzl_issue_sea_road_patrol_window` writes the timed flag through `fallout_nzl_duration.cooldown`, stamps the generation, increments the serial, and reuses one dynamic modifier at `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:82-103`. The constant is 90 days.
- The fail-closed current triggers require a current package, current licence generation, timed patrol flag, matching patrol generation, and a positive serial at `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt:80-102`.
- Exactly one lifecycle dynamic modifier exists. Its enable and remove triggers both use the current-window trigger at `common/dynamic_modifiers/fallout_nzl_lifeboat_dynamic_modifiers.txt:8-14`.

### Paid action contract

- Licensed Fishery Quota Compact requires and consumes five convoys in addition to its existing 25 Political Power and 350 manpower costs, then applies +7 Food Security and +4 Sea-Lane Security and refreshes the window at `common/decisions/fallout_nzl_lifeboat_decisions.txt:187-253`.
- Licensed Quiet-Seas Patrol requires and consumes ten convoys and twelve Navy Experience, retains its factory commitment, applies +12 Sea-Lane Security, and refreshes the same window at `common/decisions/fallout_nzl_lifeboat_decisions.txt:913-999`.
- Non-licensed branches retain the earlier fail-closed costs and results. The correction therefore does not grant free convoys, equipment, or a passive value loop.
- The licensed Fishery AI weight is zero below ten convoys while the payment is five, preserving the specified five-convoy reserve at `common/decisions/fallout_nzl_lifeboat_decisions.txt:240-253`.

### Score-only pressure, cleanup, and fixed architecture

- `fallout_nzl_add_sea_road_score` changes only temporary `fallout_nzl_chain_score`: +4 for a current isolation window and -4 for a lapsed licensed window at `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:114-128`.
- Its only call sites are the external and Year 10 calculators at `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:1233` and `:1306`. Opening and domestic scoring do not read the window.
- Package reset closes the modifier and clears the licence flag, licence generation, serial, timed flag, and patrol generation. No correction helper is called from `common/on_actions/`, and an exact non-documentation search found zero `fallout_nzl_activate_lifeboat_package = yes` callers.
- Static source counts remain exactly 42 focus blocks, 18 decisions/missions, 14 ideas, and 26 authored event blocks (`chaosx.fallout.127` through `.152`).

No sea-road requirement is missing or simplified in the final snapshot.

## 2. Fallout country-memory Event Log correction: PASS

### Dedicated ownership and shared history

- `common/script_constants/fallout_nzl_event_log_constants.txt:16-24` assigns dedicated system ids `9101`, `9102`, `9103`, and `9104`. The authored roots remain `.127`, `.133`, `.139`, and `.147`.
- `common/script_constants/event_system_constants.txt:80` assigns `event_system_event_type.fallout_country_memory = 4`. History filter cycling, range validation, and row matching include filter 4 at `common/scripted_effects/chaosx_events_log_effects.txt:2855-2926` and `:3218-3229`.
- `record_events_log_system_history_entry` prepends the shared sequence, date, dedicated id, type, compact result payload, primary actor, optional secondary actor, and existing history statistics without changing `global.last_fired_event_id` at `common/scripted_effects/chaosx_events_log_effects.txt:442-534`.
- The NZL wrapper records NZL as primary actor and the exact current external country as secondary actor when present at `common/scripted_effects/fallout_nzl_event_log_effects.txt:100-138`.

### Exact private ledger and commit cardinality

- `fallout_nzl_event_log_append_snapshot` prepends 18 parallel fields: shared sequence, exact date, dedicated id, detailed payload, country-memory id 91, choice, result, domestic prior result, route, actor and marker, secondary actor and marker, all four package values, and transition generation at `common/scripted_effects/fallout_nzl_event_log_effects.txt:163-228`.
- Opening, domestic, and Year 10 wrappers are generation-deduplicated at `common/scripted_effects/fallout_nzl_event_log_effects.txt:140-161`, `:230-251`, and `:293-314`. Package reset now preserves their recorded flags and generation variables; a same-generation reactivation cannot duplicate committed rows, while a later generation can replace the receipt.
- External logging is one row per transaction. A new external transaction clears only the transaction receipt at `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:644-657`. The authored external chain records before cleanup in `fallout_nzl_close_external_chain` at `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:826-831`.
- Rescue Passage records its successful second external partner before transaction cleanup at `common/decisions/fallout_nzl_lifeboat_decisions.txt:519-525`. The no-partner branch keeps the secondary-actor marker false and does not fabricate a country.
- Opening and domestic calls occur after their result application in the delayed resolvers at `events/fallout_world_end_events.txt:8978-8982` and `:9108-9112`. Year 10 logs only after its final receipt is written.

### Exact reload and package-card isolation

- `fallout_nzl_load_open_history_payload` first resolves the selected dedicated id and exact shared sequence, then loads the private row with the same sequence and id at `common/scripted_effects/fallout_nzl_event_log_effects.txt:559-685`. It does not substitute later live values into an old history row.
- `fallout_nzl_prepare_event_log_card` selects one transition generation. It uses live values only when NZL has a current package and at least one current-generation memory; otherwise it selects the newest stored generation. All four chain summaries and external contacts are filtered to that generation at `common/scripted_effects/fallout_nzl_event_log_effects.txt:316-557`.
- Current live values, route, and aggressor are read inside `NZL = { ... }` and copied to the viewing human country's display variables at `common/scripted_effects/fallout_nzl_event_log_effects.txt:363-442`. The card is therefore not dependent on the viewer playing NZL.
- `fallout_nzl.event_log.card.composite` embeds both the base Fallout detail and the NZL package card at `localisation/english/fallout_nzl_event_log_l_english.yml:37`. The scripted-localisation branch uses that composite only when NZL memory exists and otherwise retains the base Fallout key at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:10763-10773`.

### Negative ownership contract

- The four dedicated ids are not added to `global.all_events`, have no entries in `localisation/english/chaosx_event_names_l_english.yml`, and cannot enter the ordinary Events catalogue or its weight system. Type 4 exists only on the History/detail path. Manual event trigger controls exclude type 4.
- Event 2 remains mapped to `"Zombie Outbreak"` and no NZL or Fallout text was added to its ordinary event-name mapping.
- A read-only scan of `docs/spreadsheets/chaos_redux_events_catalog.xlsx` across Events, Clusters, Scenarios, Info, and Legend found no `SCN-014`, `fallout_nzl`, `New Zealand Lifeboat`, Lifeboat State, or `9101`-`9104` cell. The exported CSV files also contain none of those terms.
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md:127` remains `0 of 660`; the 26 country-memory blocks were not promoted into that count.
- No ordinary workbook row, SCN-014 row, evolution row, super-event, audio package, report image, recurring on action, or activation caller was added by this correction.

No Event Log requirement is missing or simplified in the final static implementation.

## 3. Regression review

The audit initially found three correction regressions in a moving shared-workspace snapshot. All three are closed in the audited snapshot:

1. **Closed: same-generation duplicate risk.** Runtime reset no longer clears the opening, domestic, or Year 10 Event Log recorded flags or generation receipts. External dedup remains transaction-local.
2. **Closed: viewer-dependent current card.** The card reads the current package through NZL and writes presentation variables on each viewer.
3. **Closed: base Fallout detail replacement.** The memory-present branch now uses a composite key containing the base Fallout description followed by the NZL card.

No remaining source-level regression was found in ordinary Event Log registration, History filtering, Events-list population, manual dispatch controls, Event 2 ownership, spreadsheet ownership, focus/decision/idea/event counts, or dormancy.

## 4. Accepted plans and documentation disposition

| Input | Disposition |
| --- | --- |
| `docs/specs/air_cleanliness_fallout_specs/fallout_nzl_lifeboat_state_pilot_spec.md` | Current source of truth. Both promoted corrections are implemented. Broader activation requirements remain open. |
| `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NZL_LIFEBOAT_PILOT_DEPTH_REVIEW.md` | Accepted and promoted. Its only two bounded corrections are closed. Its explicit stop-expansion decision remains appropriate. |
| `subagent_handoffs/2026-07-22_fallout_nzl_numbered_sea_road_decision_mission_audit.md` | Still valid for the sea-road decision/mission surface. |
| `subagent_handoffs/fallout_nzl_lifeboat_event_log_details_2026-07-22.md` | Implemented and reconciled with compact shared result payload, detailed private payload, durable dedup, partner rows, cross-viewer NZL scope, and composite Fallout details. |
| `FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md` | Reconciled with the final licence/window distinction and Event Log fixes. It correctly retains runtime uncertainty and activation blockers. |
| `subagent_handoffs/fallout_nzl_lifeboat_completion_audit_2026-07-22.md` | Historical pre-correction audit. Superseded by this report for sea-road and Event Log status. |
| `subagent_handoffs/fallout_nzl_lifeboat_status_reconciliation_2026-07-22.md` | Historical mid-tranche status. Superseded by the current spec, engine proof, implementation handoffs, and this report. |

The two older status files still contain statements that these corrections are absent or pending. They are retained as dated history, not current completion evidence. Marking them explicitly superseded later would improve document hygiene but does not block the implemented corrections.

## 5. Meaningful validation and remaining uncertainty

Performed:

- Traced both paid action transactions from availability and displayed cost through payment, result, window issue, scoring calls, cleanup, and AI reserve behavior.
- Counted the unchanged architecture directly: 42 focuses, 18 decisions/missions, 14 ideas, and 26 event blocks.
- Enumerated 12 shared History append destinations and 18 NZL private append destinations and checked their sequence handoff and exact-sequence loader.
- Traced opening, domestic, normal external, no-partner external, Rescue Passage, Year 10, stale/reset dedup, current-viewer, historical-viewer, and base-Fallout-detail paths statically.
- Searched ordinary event registration/name surfaces, on actions, caller sites, workbook sheets, exported CSVs, and the release ledger for forbidden ownership.

Not performed or not available:

- HOI4 was not launched by instruction. Timed-flag expiry, modifier removal, live AI selection, Event Log rendering, flag navigation, actual save/reload persistence, numeric country-scope recovery, and multiplayer observation remain unproved at runtime.
- The earlier read-only GUI inspection attempt recorded in the engine proof returned no artifact because the service transport closed. There is no `hoi4.event_render` or GUI artifact URI to cite for this final audit.
- These runtime uncertainties do not conceal a source fallback, but they prevent activation proof and remain part of the broader pilot's failed completion status.

Audited moving-surface SHA-256 snapshot:

- `fallout_nzl_lifeboat_effects.txt`: `923AE0CC35F20A5D491A200EA0EFE96FB615862587F80CCB3A8867ADEBC9D6E3`
- `fallout_nzl_event_log_effects.txt`: `D1187A6651FADBF30CE289D35491F13ACE2C204EC9E65B896510A60C11065FA5`
- `chaosx_events_log_effects.txt`: `106BC9E95FA102F0A4D5CDE991A92A39110C4F1DE11A4464290DD7011B2450CF`
- `chaosx_scripted_gui_events_log.txt`: `504ACDD3AD2DA4C27A28FBC274D1D112A3B48A3612AB1265C2520F06E4074E81`
- `chaosx_scripted_localisation_events_log.txt`: `B1E654DEE8963E391EF6B6F9FEFEB714CBDEC6356CACF981E237441A7E74F57F`
- `fallout_nzl_event_log_l_english.yml`: `F2BDC7E8A9EE1386D6447657DB4211AD4F025557DA58E1FC0D64713D553EC96E`
- `FALLOUT_NZL_LIFEBOAT_ENGINE_PROOF.md`: `900F2C4AC90498A961673C222D2E6BC046BC3B99BDA769905798D1801A0827E1`

## 6. Asset and documentation gaps

- Neither correction requires new report art, animation, a super-event, audio, or advisor portrait. Existing static report and flag surfaces remain sufficient.
- The Radio Service Coordinator portrait remains a broader pilot blocker. No candidate PNG, review sheet, metadata record, approved DDS, or sprite is claimed. Because no advisor asset was produced or approved in these corrections, there is no DDS/provenance approval claim to validate here.
- The workbook boundary is intentionally unchanged while SCN-014 is absent. That is the accepted ownership design, not an omitted correction row.
- The current spec, depth review, effect documentation, Event Log handoff, engine proof, and this audit agree. Only the two dated pre-correction status reports remain historically stale.

## 7. Retained broader-pilot blockers

The package must remain dormant. These blockers are unchanged:

1. Radio Service Coordinator final portrait approval, DDS, and sprite wiring.
2. Samoa state 726 disposition and the Aotearoa overlap on states 284 and 723, including the GRX conflict surface.
3. Live allocator assignment, capital, player-continuation, materialisation, package-generation, and activation-caller receipts.
4. Engine-safe additive retirement of the eligible vanilla NZL AI plans.
5. Runtime proof for event-target retention, generated-character promotion, exact province sweep, host/multiplayer authority, save recovery, and map return.
6. SCN-014 registration and workbook representation remain blocked until the exact manual province sweep passes.
7. The Fallout living-world release ledger remains `0 of 660` until its separate review floor is met.

## 8. Recommended next actions

1. Accept both promoted corrections as source-complete and keep the package dormant.
2. Treat this report as the current correction audit and the earlier completion/status reports as superseded history.
3. Resolve the radio asset, Samoa/Aotearoa dispositions, allocator/materialisation path, and vanilla NZL AI retirement before adding any caller.
4. When activation authority and a testable allocator exist, run the nine runtime scenarios in `FALLOUT_NZL_LIFEBOAT_PILOT_DEPTH_REVIEW.md:293-305`, including save/reload, second-partner, no-partner, stale callback, cross-viewer multiplayer, ownership, and dormancy cases.
5. Do not add Event 2 text, an ordinary Events/workbook row, SCN-014, or any 660-count increment as a substitute for the blocked activation work.

## Improvement-loop recommendation

Do **not** route this pilot to `chaosx_improvement_loop_planner`. The accepted depth review already supplied the bounded addendum, both corrections are implemented, and the same plan explicitly rejects further volume. The remaining work is blocker closure and runtime proof, not missing design depth.
