# Fallout Completion Audit

Date: 2026-07-25

Superseded for current-state counts and tranche status by `2026-07-26_fallout_completion_reconciliation.md`. This audit remains retained as dated evidence. Its 52-row and 446-block counts and its stale-document list are not current source-of-truth values.

Overall verdict: **INCOMPLETE AND RELEASE-BLOCKED**.

The current repository contains substantial static Air Winter, blackout, transition, manual-sweep, scheduler, and event-content foundations, but it cannot yet produce or validate the accepted complete post-Fallout campaign.

The living-world release count remains `0 of 660`, both scheduler activation flags remain without setters, the public manual scenario remains withheld, and the transition cannot yet prove a complete successor allocation and player continuation.

## Scope and evidence boundary

This is a bounded current-state audit of the authoritative source index, baseline acceptance requirements, living-world and Ashline specifications, current implementation/status maps, the named scheduler and presentation proofs, and their current source files.

The audit read the required repository guidance, event/planning/improvement/subagent/asset skills, core offline HOI4 wiki pages, and relevant installed vanilla documentation.

The audit did not launch Hearts of Iron IV, did not edit gameplay, did not mutate the workbook, and did not claim runtime behavior from static script.

The audit did not perform a fresh line-by-line audit of every file in the 100-file source-spec tree or every historical plan in the 192-file plan tree.

It used [SOURCE_OF_TRUTH_AND_SCOPE.md](../../../specs/air_cleanliness_fallout_specs/SOURCE_OF_TRUTH_AND_SCOPE.md), [SOURCE_SPEC_INDEX.md](../../../specs/air_cleanliness_fallout_specs/SOURCE_SPEC_INDEX.md), the baseline acceptance specifications, [01_living_world_event_ecosystem.md](../../../specs/air_cleanliness_fallout_specs/specs/01_living_world_event_ecosystem.md), [02_winter_climate_visual_overhaul.md](../../../specs/air_cleanliness_fallout_specs/specs/02_winter_climate_visual_overhaul.md), [52_reviewed_regional_ashline_firebreak.md](../../../specs/air_cleanliness_fallout_specs/specs/52_reviewed_regional_ashline_firebreak.md), and the current proof/status documents as the bounded authority set.

Relevant working-tree files were already modified during the audit: `common/scripted_effects/fallout_world_end_effects.txt`, `FALLOUT_EVENT_ID_LEDGER.md`, and `source_of_truth_map.md`.

The findings therefore describe the live working-tree snapshot and must not be treated as proof of a clean committed state.

## Completion status by surface

| Surface | Status | Current evidence | Completion gap |
| --- | --- | --- | --- |
| Fallout event ownership | Static pass | `events/fallout_world_end_events.txt` is the only event file declaring `add_namespace = chaosx.fallout` or defining `chaosx.fallout.*` event ids. | A complete cross-feature visual/audio path audit was outside this bounded pass. |
| Normal super-event removal | Static pass | [FALLOUT_BLACKOUT_GUI_PROOF.md](../FALLOUT_BLACKOUT_GUI_PROOF.md) and current GUI/effect source show an independent Fallout blackout and dedicated audio path. | Live z-order, input capture, audio, save, pause, and multiplayer behavior remain unobserved. |
| Air Winter state model and events | Partial | Current status records phases 0–6, state ledgers, Deaths integration, physical damage, decisions, and a separate 52-block Air Winter event pilot. [AIR_WINTER_EVENT_SCHEDULER_PROOF.md](../AIR_WINTER_EVENT_SCHEDULER_PROOF.md) records static scheduler coverage. | Event delivery, delayed target retention, AI frequency, seasonal save recovery, map presentation, treaty delivery, and performance remain runtime gates. |
| Air Winter ordinary-map visuals | Source-level pass, runtime blocked | [AIR_WINTER_NORMAL_MAP_PROOF.md](../AIR_WINTER_NORMAL_MAP_PROOF.md) and [air_winter_normal_map_static_reaudit_2026-07-22.md](air_winter_normal_map_static_reaudit_2026-07-22.md) report all 1,081 states, nine classes, six active phases, cleanup, registries, and 85 runtime meshes. | Creation, placement, scale, visibility, layering, cleanup, multiplayer behavior, and performance have not been observed. The unused full-screen grade-plate route is not promoted. |
| Blackout GUI and phased coordinator | Partial, runtime blocked | `interface/fallout_world_end.gui` declares the independent full-screen window and click blocker. The scripted GUI is gated by `fallout_transition_active`, and `fallout_lock_transition` schedules `chaosx.fallout.1001` through the saved coordinator. | Static review cannot establish real click interception, every-DLC z-order, pause behavior, save persistence, multiplayer presentation, or performance. |
| World rewrite and player continuation | Blocked | Transition schemas, coordinator receipts, survival ledgers, diplomacy-reset surfaces, and conflict inventories exist. | No active general successor allocator, required successor materializer, current country/focus package producer, player candidate-choice assignment, or complete player continuation exists. Map-return postconditions must remain blocked. |
| Manual exact-province scenario | Static substrate complete, release blocked | [FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md](../FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md) records 10,154 valid land provinces, 1,081 state rows, 41 batches, exact callback accounting, and a literal seven-day post-verification delay. | SCN-014 is reserved but has no public row or launch dispatch. Native acceptance, impassable-state behavior, exactly-once `on_nuke_drop`, frame cost, save integrity, multiplayer synchronization, and the possible 121,848 vanilla news-event attempts remain unproven. |
| Living-world scheduler | Partial and deliberately dormant | The numerical, registry, candidate, dispatch, delayed, bilateral, cleanup, and hidden-AI transaction substrate exists. No setter for `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active` was found. | There is no live living-world caller. Major-arc and relationship payloads remain fail-closed, actor exclusion and atomic pair-family reservation are incomplete, and runtime delivery/save/multiplayer behavior is unproven. |
| Ash-week orientation | Partial and dormant | All 23 reserved ids `62–84` are defined, with current localisation, six assets, result memory, Event Log routing, and transaction receipts. | The caller is absent, 96 of the accepted 108 region/archetype cells remain design-only, installation packages and approvals are absent, infrastructure repair lacks a proven exact effect, and runtime delivery is unproven. |
| Living-world event library | Partial and dormant | The current reviewed ordinary pool has 52 candidate chains and 446 defined blocks. Human choices, hidden-AI paths, delayed results, callbacks, cleanup, localisation, Event Log routes, and art exist for the reviewed pilots. | All 446 blocks remain ineligible for release credit. The raw pool is 214 blocks below 660, while the countable pool is 660 blocks below the accepted floor. |
| Regional/biome content | Design gap after first slice | Ashline Firebreak provides the first explicitly reviewed regional/biome chain with 11 blocks. | One chain is not a nine-class regional pool. The remaining regional class coverage, recurrence balance, and live scheduling are absent. |
| Government, successor, character, diplomacy/war, cause, recovery, and late-world families | Incomplete | Several current ordinary pilots touch these themes and the source matrices define their intended coverage. | No authoritative block-by-block primary-family ledger demonstrates accepted coverage, and no release-countable pools exist for these families. Relationship and major-arc scheduling remain fail-closed. |
| Country and focus packages | Blocked | The dormant NZL pilot contains substantial bespoke country content and proof documents. | General allocation, all-survivor package coverage, non-generic focus content for every playable successor, focus/decision/idea/AI activation, overlap dispositions, and final asset coverage are incomplete. |
| AI | Partial | Air Winter and reviewed ordinary chains include deterministic AI choices or hidden-AI parity, and the dormant scheduler has bounded AI review. | Live AI frequency, full country-package AI, major-arc AI, bilateral AI, focus AI, and save/multiplayer behavior remain unproven or absent. |
| Event Log, Event Details, evolutions, and catalog | Partial | Current pilots have many Event Log/detail routes. The workbook export contains current `FALLOUT-541` and `FALLOUT-554` rows marked `Needs Testing`. | Runtime rendering is unobserved, the full 660-block crosswalk is absent, and this audit did not perform a full workbook/localisation/evolution reconciliation. No complete late-world evolution coverage was demonstrated. |
| Assets | Partial | Ashline has a registered dedicated DDS, source workspace, manifest, and GFX handoff. Air Winter has the documented regional model package. | The complete event, successor, focus, leader, flag, achievement, and late-world asset matrices are not fulfilled. Runtime rendering remains unobserved. |
| Achievements | Partial/design gap | The NZL pilot records three dormant achievements. | A complete accepted Fallout achievement package and runtime validation were not demonstrated. |

## Current event-count evidence

Static parsing of `events/fallout_world_end_events.txt` found:

- 605 `chaosx.fallout.*` event blocks.
- 605 unique suffixes, with no duplicate definition.
- Minimum suffix `1` and maximum suffix `1018`.
- 52 Air Winter blocks: `1–6`, `10–18`, `20–51`, `60–61`, and `201–203`.
- 23 Ash-week orientation blocks: `62–84`.
- 446 dormant living-world pilot blocks: `100–126`, `1009–1018`, `153–200`, and `204–564`.
- 84 other transition, manual, history, country-pilot, or infrastructure blocks not assigned to the living-world floor by this bounded audit.

The current documented total of 446 is correct.

A naive continuous count through suffix 564 produces 449 because `chaosx.fallout.201`, `.202`, and `.203` are Air Winter response/recovery events, not living-world pilot blocks.

The 446 living-world blocks currently divide into 435 blocks across the first 51 reviewed ordinary chains and 11 Ashline Firebreak blocks.

All 446 remain dormant and count as `0 of 660`.

## Ashline Firebreak disposition

The accepted Ashline specification is implemented as a dormant vertical slice at `chaosx.fallout.554–564`.

Current source contains each of those 11 ids exactly once.

The candidate uses identity `554`, transaction `710052`, route `7152`, and Event Log history `9157`.

The proof records deterministic owner-controlled state selection, three branches, a 28-day result, a 210-day callback, Air Winter and Supply Access ledgers, building and military consequences, Deaths-backed failure, hidden-AI parity, cleanup, localisation, Event Log detail, and dedicated art.

It remains ineligible for release credit because scheduler activation, real popup delivery, delayed state retention, Event Log secondary-actor rendering, host behavior, save recovery, and multiplayer behavior are unproven.

The DDS was produced through the repository converter's BGRA ffmpeg path because DirectXTex was unavailable.

The final 210×176 DDS header was inspected, but this remains a documented asset-processing simplification and not runtime presentation proof.

The source workspace under `docs/assets/air_cleanliness_fallout/fallout_ashline_firebreak/` correctly remains present while the chain is incomplete.

## Accepted-plan disposition

| Accepted design or plan | Disposition |
| --- | --- |
| Baseline Air Cleanliness and Fallout source design | Partially implemented; not promoted to completion because the manual scenario, successor rewrite, player handoff, country/focus coverage, scheduler activation, content floor, and runtime evidence remain open. |
| Fallout scheduler numerical contract | Accepted values are promoted into source specs and implemented in dormant constants and transaction receipts. Gameplay activation is queued behind explicit blockers. |
| Ash-week orientation and live-ledger contracts | Accepted and partially promoted into 23 dormant blocks and transaction schemas. The remaining 96 matrix cells, caller, install packages, and runtime proof are unresolved. |
| Manual Fallout scenario plan | Exact static ledger and sweep substrate are implemented. Public registration and launch are blocked rather than replaced with a one-strike-per-state or variable-only fallback. |
| Air Winter scheduler and ordinary-map visual plans | Static implementation and proof are present. Runtime acceptance remains outstanding. |
| Dedicated blackout plan | GUI and coordinator substrate are implemented. Runtime presentation and the complete successor rewrite remain blockers. |
| Living-world 660–910 content plan | Fifty-two reviewed candidate chains and 446 dormant blocks are present. The accepted 660-block release floor, family coverage, live cadence, and 90–180 human-visible-event campaign target remain unmet. |
| Reviewed Ashline regional specification | Implemented as a documented dormant chain and cataloged, but not activated or release-counted. |
| NZL Lifeboat State pilot | Substantial package implemented but deliberately dormant and outside the 660 floor. Allocator, activation, final Radio Service Coordinator asset, overlap dispositions, host behavior, and runtime proof remain unresolved. |

No accepted requirement was found formally rejected in the bounded authority set.

Unimplemented accepted requirements are generally described as queued, dormant, or blocked.

The shared-focus versus compiled-tree approach, wasteland ownership, player successor selection scope, and direct treaty-to-Fallout political effects remain unresolved design decisions in `BLOCKERS_AND_DECISIONS.md`.

## Stale or contradictory documentation

- [source_of_truth_map.md](../source_of_truth_map.md) calls fifty rows and 422 blocks “current” near line 33 and thirty-one rows and 289 blocks “current” near line 64, while the current reconciled state is fifty-two rows and 446 blocks.
- [FALLOUT_EVENT_SCHEDULER_PROOF.md](../FALLOUT_EVENT_SCHEDULER_PROOF.md) has a correct 52-row/446-block head and tail, but its accepted-contract introduction still says 48 rows/408 blocks and its omission section still says the candidate producer covers sixteen rows.
- [README_IMPLEMENTATION_STATUS.md](../README_IMPLEMENTATION_STATUS.md) correctly reports 52 rows near the current summary and 446 blocks in the Ashline section, but older “current” prose still reports sixteen producer rows and earlier range totals.
- [FALLOUT_EVENT_ID_LEDGER.md](../FALLOUT_EVENT_ID_LEDGER.md) has the correct current reconciliation at its head; its historical snapshots are explicitly described as superseded and are not completion evidence.

These contradictions do not change the authoritative `0 of 660` count, but they make resumption and family accounting error-prone.

## Meaningful validation performed

- Parsed all current `chaosx.fallout.*` definitions and established 605 blocks, 605 unique suffixes, the exact living-world and Air Winter ranges, and no duplicate suffix.
- Confirmed that only `events/fallout_world_end_events.txt` owns the Fallout namespace and Fallout event definitions.
- Searched current `common/` and `events/` source for setters or clearers of both scheduler activation flags and found none.
- Confirmed Ashline ids `554–564` once each and confirmed the dormant schema-promotion gates explicitly require both activation flags to be absent.
- Rehashed `common/scripted_effects/fallout_manual_province_sweep_effects.txt`; SHA-256 is `D803BD0972FCE3F69DB50829687A2C35733FCC5018CC7F582BB6A493216089E3`, matching the manual proof.
- Confirmed the current spreadsheet export includes `FALLOUT-541` and `FALLOUT-554` rows with player-facing detail and `Needs Testing` status.
- Confirmed the blackout window, full-screen declaration, click blocker, transition-active visibility gate, coordinator target, and `chaosx.fallout.1001` phase issue path in current source.

Some historical bounded `hoi4.event_inspect` requests recorded in chain proofs exceeded the 20,000 issue limit and returned no diagnostics.

Those failed inspections are not validation passes.

No runtime observation was performed, so popup display, delayed scopes, live AI, GUI input blocking, normal-map presentation, save recovery, multiplayer authority, and performance remain missing validation rather than presumed passes.

## Asset and handoff gaps

Ashline's implementation commit includes its chain proof, manifest, and asset GFX handoff.

No Ashline-specific implementation handoff was found under `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/`.

Git evidence does not identify whether that gameplay patch was produced by a subagent, so this audit cannot claim a subagent-handoff violation.

If any part was subagent-produced, the required changed-files, identifiers, validation, and residual-risk handoff still needs to be added.

The broader accepted Fallout asset matrices remain incomplete, especially successor flags, leader portraits, focus and decision icons, achievements, country-memory packages, regional event coverage, and late-world content.

The workbook is the editable catalog authority.

This bounded audit checked the current exported rows for A New Funeral and Ashline but did not perform a full workbook-versus-localisation audit.

## Simplifications, omissions, and blockers

- No weaker gameplay fallback was found for the exact province sweep, successor rewrite, scheduler activation, or regional normal-map route.
- Ashline's ffmpeg-based BGRA DDS conversion is a documented processing simplification.
- The manual scenario intentionally has no public fallback; exact native runtime behavior remains a hard blocker.
- Static blackout input-blocking is not a substitute for observed input capture.
- Static ordinary-map entity coverage is not a substitute for observed presentation.
- The 446 dormant blocks are not a substitute for 660 manually reviewed, wired, balanced, and live blocks.
- The NZL pilot is not a substitute for all-survivor country and focus coverage.
- The first Ashline regional chain is not a substitute for the nine-class regional event pool.
- Hidden-AI event branches are not a substitute for complete scheduler, country-package, focus, diplomatic, and war AI.
- Event Log and catalog entries are not substitutes for runtime delivery and complete Event Details/evolution coverage.

## Recommended next actions

The next implementation tranche should close a critical transition prerequisite instead of adding another dormant ordinary chain.

Recommended bounded tranche: **B7 successor allocation and player-continuation vertical slice**.

1. Implement and prove the active allocator start/finalize path for one existing-continuity case and one fragmentation case.
2. Materialize the exact required successor, apply current-generation country and focus package receipts, reserve and verify its capital, and expose the player candidate assignment without a generic fallback.
3. Prove the tag-switch and human-control receipt sequence statically, preserve fail-closed behavior for the unresolved runtime timing boundary, and keep map return blocked outside the two reviewed cases.
4. Add the required country, focus, decision, idea, AI, localisation, asset, and handoff evidence for those cases.
5. Do not set either scheduler activation flag until general successor allocation, all required packages, player continuation, full orientation coverage, and release-countable event review are complete.

Parallel non-gameplay reconciliation should update the stale “current” counts in `source_of_truth_map.md`, `FALLOUT_EVENT_SCHEDULER_PROOF.md`, and `README_IMPLEMENTATION_STATUS.md` without rewriting historical snapshots.

After the transition vertical slice, the next content tranche should expand regional coverage rather than add another globally framed survival chain.

It should add reviewed chains for contrasting unrepresented presentation classes with the same full candidate, human/AI, delayed-result, callback, Deaths, Event Log, catalog, asset, and cleanup standard used by Ashline.

The user-owned runtime acceptance queue remains necessary for the manual native sweep, blackout input capture, ordinary-map visuals, delayed event scopes, save interruption, multiplayer authority, and tag-switch human-control timing.

Until those blockers and the accepted content/package floors are closed, Fallout must remain reported as incomplete.
