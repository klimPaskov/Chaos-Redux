# Event 008: Tensions Rising

This overview records implementation evidence and its limits following the [release audit](../../plans/008_tensions_rising_plans/subagent_handoffs/event_completion_audit_2026-10-05.md).
The 2026-10-06 refresh records the parent-accepted report-batching and callback tranche in current source and the [updated owner evidence](../../plans/008_tensions_rising_plans/subagent_handoffs/owner_fixes_2026-10-05.md), with required runtime, complete MCP, GUI, and probability validation still unresolved.
The authoritative workbook audit records Event 8 as `Needs Testing`, and this document does not claim gameplay completion or design approval.
The [current source map](../../plans/008_tensions_rising_plans/documentation_state_2026-10-05.md) separates source design, catalog facts, implementation findings, and unresolved acceptance.

Event 008 Tensions Rising is a minor repeatable diplomatic-pressure event. In calm campaigns it is a straightforward world-tension incident. Once the Chaos Meter reaches evolved tiers, the same report becomes a staged diplomatic-pressure system with direct chaos gain, relation damage, timer pressure, follow-up incidents, AI posture pressure, rare high-stage border wars, achievements, and event-log evolution rows.

## Runtime Flow

1. Hidden canonical entry `chaosx.nr8.1` fires from the standard repeatable random-event pool and applies each eligible shock. Event 8 remains registered in `global.repeatable_events`.
2. `tensions_rising_prepare_random_event_fire` uses automatic availability that rejects `world_end` and rejects full world tension when no enabled evolved stage is available.
3. The hidden root opens one visible `chaosx.nr8.16` report while the recipient has no pending report batch. Its description is flavour text and its option shows the accumulated packet tooltip, then clears report fields and the pending flag on acknowledgement.
4. `get_tensions_rising_stage` maps the current `chaos_tier` flag to Stage I-IV and falls back to baseline stage `0` when that evolution stage is disabled.
5. Baseline firings distribute `+100` world tension across existing non-placeholder countries and update the global highest-world-tension tracker.
6. Each eligible evolved root records any unlogged Diplomatic Fever milestone, distributes its packet, adds its Chaos packet, applies pulse/relation/posture pressure, and updates achievement tracking. Separate per-batch flags allow the first effectful evolved root to attempt one follow-up and the qualifying displayed report stage to count Only Headlines once.

Report getters read recipient-country fields `tensions_rising_report_stage`, `tensions_rising_report_world_tension`, and `tensions_rising_report_chaos` rather than the mutable post-effect Chaos tier.
Further roots while `.16` is pending apply their real eligible shocks, accumulate WT/Chaos packet values into that report, and preserve its first effectful stage instead of opening another root report.
Manual Settings firing during `world_end` reaches a terminal report context without applying the Event 008 packet, and baseline/full-WT manual firing reports no added tension.
The terminal report describes an existing world state and does not create an Event 008 world-end branch.
If a new batch begins with a terminal or full-WT zero-effect root, its first later effectful root adopts the report stage and clears the no-effect flags.
Source batching replaces the earlier overwrite behavior, while held reports, mixed-stage totals, zero-effect adoption, and acknowledgement timing remain unobserved.
`tensions_rising_report_followup_attempted` prevents a second follow-up attempt after the first effectful evolved root, including a root that adopts an initially zero-effect batch.
`tensions_rising_report_headlines_counted` limits Only Headlines to one count when the batch's first effectful displayed stage is Stage II+ and peaceful-world conditions hold.
Both flags clear when a new batch starts and when `.16` is acknowledged.

## Stage Values

| Stage | Chaos gate | World tension | Chaos | Notes |
| --- | --- | ---: | ---: | --- |
| Baseline | Calm World | `+100` | `0` | blocked at full world tension |
| Stage I | Gathering Storm | `+100` | `+10` | light relation and timer pressure |
| Stage II | Rising Chaos | `+200` | `+15` | broader relation shocks and more follow-up incidents |
| Stage III | Chaos Tier | `+500` | `+25` | heavy relation pressure, Thin Wire tracking, and rare border clashes |
| Stage IV | Totalen Chaos+ | `+1000` | `+50` | strongest pressure and best border-clash odds |

The world tension trigger uses HOI4's documented `0-1` `threat` scale. The full-tension gate is centralized as `constant:tensions_rising_gate.full_world_tension`. World-tension packets are distributed through `apply_tensions_rising_distributed_world_tension`. Each selected existing non-placeholder country receives an equal named-threat slice. The recipient count is capped only when an all-country split would fall below `0.1` world-tension percentage points.

## Timer Pulse

The evolved Tension Pulse uses `tensions_rising_timer_pulse_active`, `global.tensions_rising_timer_pulse_strength`, `global.tensions_rising_timer_pulse_days`, and `global.tensions_rising_timer_pulse_expiry_date`.
Stronger stages replace weaker active pulses.
Equal-stage repeats convert the exact expiry-minus-current-date offset into remaining days, add the stage extension, clamp the result to the stage cap, and set an exact deadline.
The timer consumer reads the exact deadline, with parser-safe timed-flag buckets retained for the supporting flag.
This source change supersedes the release audit's stale-budget description, while late renewal, replacement, and expiry behavior remain pending final owner validation and MCP evidence.
The event timer reads the active strength in `calculate_next_timer_value` through `apply_tensions_rising_timer_pressure_to_next_timer`, without an Event 008 periodic world scan.

## Diplomatic Shocks

Stage I-IV firings select a small number of country pairs through `select_tensions_rising_relation_pairs`.
Selection prefers major or faction-leader actors and filters capitulated, subject, zombie-outbreak, and direct war opponents.
Primary selection avoids recent relation actors, but the release audit found actor and target fallbacks that omit that cooldown check.
Relation modifiers are timed through the existing opinion system:

- Stage I: `tensions_rising_leaked_cables`
- Stage II: `tensions_rising_mobilization_suspicion`
- Stage III: `tensions_rising_border_alarm`
- Stage IV: `tensions_rising_permanent_alert` for twelve months

Each direction of a stage-specific opinion modifier uses a partner-keyed timed flag and contributes one ledger entry only when that direction/stage/partner record is absent.
The hidden expiry event `chaosx.nr8.21` decrements one directed entry per scheduled expiry.
Repeated applications while the matching flag is active do not add or renew that owned entry in the reviewed source.
This replaces the release audit's unconditional two-per-application counter, while exact native expiry, duplicate delivery, and same-partner cross-stage behavior remain unobserved.

## Follow-Up Incidents

Each recipient-country pending batch presents one visible `.16` report and can schedule at most one selected delayed follow-up report from its first effectful evolved root.
The canonical `.1` is hidden and contributes no additional popup, while overlapping roots join the existing batch.
The ten visible follow-ups are `chaosx.nr8.2` through `.10` and `.12`, and `.11` is deliberately unused.
There is no live Event 008 `news_event` definition.
The scheduling is hidden from the main option tooltip, but the selected incident is a visible report when delivered.
Each incident recalculates the current Diplomatic Fever stage, treats a missing evolved stage as Stage I pressure, and applies a smaller aftershock without recursing into the main event effect.
All ten public follow-up definitions use `can_tensions_rising_followup_fire`, which requires an enabled current evolved stage and rejects `world_end` at delivery.
The first Stage IV briefing and Stage II+ recent-relation branches retain priority, followed by the full-WT branch and then Stage I/II defaults.
The full-WT branch therefore precedes those defaults in current source, while recent relation damage can still shadow later pools and numerical reachability remains unresolved.
The helper retains a Stage I fallback for internal calls, but public queued reports cannot enter it when the current evolved stage is disabled or absent.

Incident effects are centralized in `common/scripted_effects/008_tensions_rising_effects.txt` and tuned through `common/script_constants/008_tensions_rising_constants.txt`:

- Telegram, embassy, frontier, insurance, rumour, staff-car, and fleet incidents add extra distributed world tension, small chaos packets, and timed opinion shocks.
- Embassy, staff-car, fleet, and last-briefing incidents also push selected AI countries into short-lived readiness ideas.
- Border Lamps, One Denial Too Many, and The Last Normal Briefing can attempt a true non-transfer `start_border_war` at Stage III+.
- Insurance Rates Jump in Neutral Ports still owns the Insurance Market achievement hook for peaceful player countries with a large convoy reserve.

Border-war attempts require independent, non-capitulated, non-zombie countries that are not subjects, not faction partners, not in active wars or civil wars, not already in border wars, not recent border-war actors, and able to field a small army. The helper then stores adjacent owned-and-controlled state IDs before starting a non-transfer clash. If no safe adjacent pair exists, the incident still applies its other world-tension, chaos, opinion, and posture effects.

## AI Posture

AI posture hooks apply short timed national spirits to selected AI countries that are majors, faction leaders, or already at war:

- `tensions_rising_cautious_alignment`
- `tensions_rising_alarmist_rearmament`
- `tensions_rising_general_staff_fever`
- `tensions_rising_permanent_alert`

These ideas nudge diplomacy, readiness, and defensive behavior without creating war goals, new countries, cores, focus trees, or formables.

## Event Log and Cluster

The event-log detail body is `chaosx.events_log.window.event_details.tensions_rising`. The Diplomatic Fever evolution type uses `constant:tensions_rising_event_log.evolution_type`, records one milestone for each reached stage, and exposes stage title/body text through the history, evolution view, event-detail preview, and selected-evolution panes.

The authoritative workbook audit records repeatable cluster ID 3 as `Diplomacy`, with members 8/17/36/59 at Medium/Medium/High/High and status `Partially Available`.
The earlier overview and parent handoff report the same four-member implementation and identify `constant:event_cluster_id.diplomacy`, `chaosx.event_cluster.diplomacy.name`, and `chaosx.events_log.window.cluster_details.description.diplomacy`, with Diplomatic Panic aliases retained for compatibility.
A direct reconciliation read instead found `constant:event_cluster_id.diplomatic_panic` and a two-member Low-severity branch in `common/script_constants/event_cluster_constants.txt:17` and `common/scripted_effects/chaosx_event_cluster_effects.txt:1327`.
Both evidence sets are retained pending the cluster owner's source and acceptance basis, and the reported four-member implementation is not verified by that branch.

## Terminal scope

Stage IV is Event 008's strongest state and remains non-terminal. It leaves diplomacy under extended alert rather than transitioning into a world-end branch, so the event does not own a super-event package.

## Achievements

Event 008 adds five achievements:

- `achievement_tensions_thin_wire`: remain at peace and full world tension through the Stage III+ 180-day watch.
- `achievement_tensions_only_headlines`: receive three qualifying report batches whose first effectful displayed stage is Stage II+ while the world has no active wars, counting each batch at most once.
- `achievement_tensions_insurance_market`: receive the insurance follow-up while at peace with at least `30` convoys.
- `achievement_tensions_one_denial`: have an actor with its own 120-day eligibility flag enter a war relation during the global relation-damage window.
- `achievement_tensions_blackout`: have at least ten active Event 8 timed opinion modifiers at once.

All five achievement definitions, localisation, tracking hooks, and DDS triplets exist in source.
Their intended unlock conditions remain subject to the release-audit tracking gaps listed below.
The fifteen achievement DDS files are registered in `interface/chaosx_achievements.gfx`, while provenance and final-art acceptance remain unresolved.

Thin Wire sets a 180-day `global.date`-based expiry for the eligible human recipient and uses `tensions_rising_thin_wire_callback_pending` to keep one scheduled `.20` callback chain.
Each callback clears its pending flag on entry, checks peace, full world tension, and absence of `world_end`, then either grants readiness at the exact deadline or schedules one next-day callback.
War-hook `ROOT` and `FROM` clear an active watch and expiry immediately while retaining the already-pending callback.
A same-day peace and new watch can adopt that callback without creating a parallel chain or shortening the new 180-day expiry.
A failed daily check clears the watch and expiry, while an inactive callback consumes its pending marker without continuing.
Daily WT sampling can miss a dip and recovery between checks, so continuous full-tension observation is not established.
The duration is 180 days, with 120 days applying to One Denial actor eligibility and a separate 150-day relation-selection cooldown.

## Assets

- Report image: `GFX_report_event_tensions_rising`, backed by `gfx/event_pictures/008_tensions_rising/report_event_tensions_rising.dds`
- News image: `GFX_news_event_tensions_red_line`, backed by `gfx/event_pictures/008_tensions_rising/news_event_tensions_red_line.dds`, remains registered as an available news asset. Follow-up incidents use the report image instead of a news image.
- Historical achievement source, processed PNG, contact-sheet, and DDS-manifest archive: `docs/assets/008_tensions_rising/`. This package is absent and Git records deletion in `87d441ac758d515e1abca34167fcd45b51acf028`. No replacement source archive was established by this review.

The release audit parsed all 17 runtime DDS headers and dimensions: report 210x176, unused news 397x153, and fifteen achievement images 64x64.
These checks establish container metadata only and do not establish source provenance, artwork review, pixel quality, or live consumption.

## Evidence and unresolved release findings

The QA collage `C:\Users\klimp\Videos\chaos_redux_trailer\records\qa\evt008_sheet.jpg` shows Event 008 only in `pop00`.
`pop01–05` contain unrelated vanilla popups, and `pop06` is map-only.
The collage supports the baseline report picture and acknowledgement at its supplied resolution, without proving evolved, follow-up, Event Log, achievement, or cleanup coverage.

The release findings remain historical baseline evidence, with current owner source changes recorded below rather than treated as final validation:

| Finding | Current source status | Remaining validation or decision |
| --- | --- | --- |
| F1 evolution controls | Root stage selection falls back to baseline when disabled, and public delayed reports require an enabled current evolved stage. | Root/toggle/queued-delivery scenarios remain pending engine evidence. |
| F2 terminal safety | Automatic availability rejects `world_end`, public delayed reports have delivery guards, and a manual root has no-effect terminal context. | Queued delivery and existing border callback cleanup need engine evidence. |
| F3 packet display | Hidden roots accumulate into one `.16` report per recipient pending batch, preserving its first effectful stage and adopting a later effectful stage after an initial zero-effect context. | Mixed-stage totals, held-report updates, no-effect adoption, and acknowledgement timing remain unobserved. |
| F4 pulse renewal | Equal-stage extension debits date-based remaining days and sets an exact deadline. | Late renewal, replacements, expiry, and native timer consumption remain unobserved. |
| F5 relations/Blackout | Unique directed stage+partner entries and per-direction expiry replace application counting. | Last-resort relation fallbacks still omit recent-actor cooldown, and native ledger/expiry behavior needs validation. |
| F6 One Denial | Every selected pair shock refreshes actor-owned 120-day eligibility outside modifier dedupe, separate from the 150-day selection cooldown. | Actor expiry and unrelated-pair refresh scenarios remain unobserved. |
| F7 follow-up routing | Full-WT branch precedes Stage I/II defaults after higher-priority special branches. | Earlier recent-relation branch still shadows later pools, and required probability comparison has no usable result. |
| F8 Thin Wire | One pending callback chain follows a 180-day date expiry, with immediate war-hook cancellation and same-day new-watch adoption. | Callback ordering, watch restart, and duplicate prevention remain unobserved, and daily WT sampling can miss intra-day dips. |

The [localisation handoff](../../plans/008_tensions_rising_plans/subagent_handoffs/localisation_audit_2026-10-05.md) documents concrete report/detail prose and constant-backed main-packet display values, pending parent review and rendered validation.
Its final title for `.4` is `Unease Along the Frontier`, while `apply_tensions_rising_incident_calm_map` remains the source helper name.
Workbook Details and evolution wording still require the parent's exact pending catalog wording, and this reconciliation changed no workbook or CSV.
The release audit's event inspect, render, compare, source lookup, and reference-context calls timed out after 600 seconds without usable artifacts or source revisions.
Historical curator event calls timed out, while the 2026-10-06 inspect and render returned partial artifacts at revision `0f7411e7faa6030bd9a0b378146a88fb89cbe631cbcce8ad6524a093cca570e7`.
The verified render manifest has `complete = false`, an empty branch list, broad source inventory, and unresolved helpers under focused analysis, so it does not prove batching or watcher lifecycles.
That curator manifest predates the final per-batch accounting flag correction, while the owner separately reports partial reachability evidence and current `.1`/`.16`/`.20` source lookup.
Exact artifact references and retrieval limits are in the reconciliation handoff, and source review does not replace missing complete MCP evidence.
The [probability baseline handoff](../../plans/008_tensions_rising_plans/subagent_handoffs/probability_baseline_2026-10-05.md) preserves named unresolved scenarios, reference discovery identities, and analyzer delivery blockers.
The [probability comparison handoff](../../plans/008_tensions_rising_plans/subagent_handoffs/probability_compare_2026-10-05.md) records earlier timeouts and a stopped-pending batch for the previous effects bytes.
The batching/callback tranche has no returned same-scenario numerical comparison evidence, so balance remains unresolved.
Shared Event Log/Details wrapping, states, click regions, and resolution behavior remain unrendered, and source-design acceptance remains unresolved.

## System boundary

Event 008 owns diplomatic pressure: international tension, chaos, temporary crisis pacing, timed relation damage, follow-up reports, AI readiness, event-log milestones, cluster history, achievements, and bounded frontier clashes. Territorial conquest, country creation, national routes, and terminal scenarios remain owned by their dedicated event systems.

## Future Plans

These retained proposals have unresolved current acceptance and do not authorize implementation through this documentation cleanup.

- Add pair-specific named follow-up incidents only if the event-log UI later supports short-lived relation-pair references cleanly.
- Consider adding a generic relation-pair helper if other event families need the same timed diplomatic-shock pattern.
- Add further Diplomacy members only through the authoritative cluster membership catalogue after their event-system eligibility, localisation, Event Log detail, and cooldown behavior are complete.
