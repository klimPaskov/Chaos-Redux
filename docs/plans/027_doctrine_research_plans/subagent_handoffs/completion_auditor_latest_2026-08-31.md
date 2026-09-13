# Event 027 Doctrine Research independent completion audit

> **Superseded status notice (2026-09-01):** This dated completion audit is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its default-enable recommendation is stale as a current source claim, while its acceptance blockers remain relevant.

Date: 2026-08-31

Role: `chaosx_event_completion_auditor`, read-only

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`

## Verdict

Event 027 is **source-playable with qualifications**, but it is **not acceptance-complete**.

“Source-playable” here means that the current source contains a coherent global firing path, country-owned batches, human pages, an AI resolver, explicit doctrine adapters, native-effect dispatch, receipts, queue continuation, lifecycle callbacks, achievements, localisation, assets, and shared integration. It does not mean that the native mastery transaction, persistence, visual consumers, or weighted behavior have been proven in the engine.

The event is not ready for an unconditional default-enable claim. It is currently in `event_log_event_is_reworked_default_enabled` at `common/scripted_triggers/chaosx_settings_triggers.txt:34`, while `docs/specs/027_doctrine_research_specs/027_doctrine_research_acceptance_criteria.md:13` permits default enablement only after the full rework is ready for normal selection. The unresolved blockers below make that acceptance condition false.

No Hearts of Iron IV process was launched. No gameplay, localisation, asset, workbook, or MCP configuration file was edited. This handoff is the only file written by this audit. No commit was created.

## Audit basis

I read `AGENTS.md`, all 16 files in `docs/specs/027_doctrine_research_specs/`, the current implementation and integrations, and the Event 027 historical handoffs. I applied the `chaos-redux-events`, `chaos-redux-event-planning`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-assets`, and read-only workbook guidance.

I also consulted the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, AI, technologies, and doctrines, plus the installed vanilla documentation for effects, triggers, script concepts, on-actions, and the doctrine folder/track/subdoctrine formats.

The current source anchor hashes at the time of this audit were:

| Surface | SHA-256 |
| --- | --- |
| `events/027_doctrine_research.txt` | `134FD2AEB6F1C2354D3758A46BBF13CA476FAA5567E52B2B0F4CBA09388FBEF7` |
| `common/scripted_effects/027_doctrine_research_effects.txt` | `CB5F51FB295ACFAF1815900D8ED4671528E8B27DB977FD78CB77C3E575207112` |
| `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt` | `51B94513DDD690D7FD45E945F1A9C76E002AB527670117843CC6A176EBC1F525` |
| `common/scripted_effects/027_doctrine_research_ai_effects.txt` | `6C4B7E9B776682496C2FB7ABAC627FAF22B72A56B7789FB3F38657AA733B9D39` |
| `common/scripted_triggers/027_doctrine_research_triggers.txt` | `0C88AFC1C8F51F0074ED6C6BB98CF0501219C3E0CD4F13A9E308D80FEB95669C` |
| `localisation/english/027_doctrine_research_l_english.yml` | `30C894D867252F715A8D81EED89458681E9C5856D7ECD04F1ED568AE85CFB923` |

## Completion status by surface

| Surface | Status | Current evidence and limit |
| --- | --- | --- |
| Entry event and global snapshot | Finished in source; runtime unproven | `chaosx.nr27.1` calls one `doctrine_research_fire_global_batch`; `common/scripted_effects/027_doctrine_research_effects.txt:1744-1755` contains one bounded `every_country` fanout over countries with a valid action. |
| Batch stage, size, queue, and continuation | Finished in source; persistence blocked | `doctrine_research_append_country_batch` stores immutable ID, stage, size, remaining choices, status, date, human-start state, and five empty-domain snapshots. `doctrine_research_start_next_batch` promotes the oldest queued row. Save/reload, interruption, and overlapping-firing traces are missing. |
| Human flow | Finished in source; presentation blocked | Thirty-one unique Event 027 IDs cover `.1-.13` and `.60-.77`; deterministic two-page pagination exists for large track lists. No one-to-one popup render or live overflow/navigation evidence exists. |
| AI flow | Finished in source; probability blocked | AI uses the human validity predicates, scores five domains, 13 Grand Doctrines, 18 tracks, and 107 track-qualified subdoctrine rows, and recalculates after each choice. The named scenario set is not acceptance-proven. |
| Native active-track mastery | Partial / engine-blocked | The implementation no longer mistakes `amount = 1` for one level: it adds one raw point at a time and reads the native level after every point until exactly `pre + 1`. Engine traces for low, middle, final, fractional, banked, Special Forces, and Chaos Warfare states are missing. |
| Empty-track transaction | Partial / engine-blocked | There are 107 explicit `set_sub_doctrine` branches followed by native readback and the same exact-step loop. Atomicity, bank preservation, native multi-level completion, and the no-choice `native_adoption` branch remain unproven in the engine. |
| Receipt and idempotency ledger | Finished in source; runtime blocked | Receipt rows are keyed by batch and choice and carry action/domain/Grand Doctrine/track/index/subdoctrine/pre/post/state. Prepared, effect-applied, native-adoption, consumed, invalid, and ambiguous paths exist. Interrupted save/reload scenarios have not been demonstrated. |
| Army adapter | Finished in source; engine-blocked | Explicit Land folder, four tracks, Grand Doctrine adoption, active and empty-track dispatch, readback, UI, and AI rows exist. |
| Navy adapter | Finished in source; engine-blocked | Explicit Naval folder, four tracks, adoption, dispatch, readback, UI, and AI rows exist. |
| Air adapter | Finished in source; engine-blocked | Explicit Air folder, four tracks, adoption, dispatch, readback, UI, and AI rows exist. |
| Special Forces adapter | Partial / design gap and engine-blocked | Both Grand Doctrines, two tracks, and eight reusable subdoctrine tokens are mapped. Empty-track selection is index-specific and active mastery is allowed only while the other track is empty. Once both tracks are occupied, Event 027 silently omits all Special Forces mastery actions. That conservative fail-closed limitation is documented, but the accepted requirement is “fully adapted or explicitly absent under the current ruleset”; no owner disposition explicitly accepts this state-level partial absence. |
| Chaos Warfare adapter | Finished in source; engine-blocked | `chaos_warfare`, the four Land-folder track identities, four Chaos subdoctrines, establishment/readiness gates, downstream ownership, icons, and AI state are mapped. Event 027 does not directly change the Chaos Meter. |
| Evolution lifecycle | Finished in source; timing blocked | Baseline and Evolutions I-IV snapshot 1/2/3/4/5 choices. The global-host scheduler advances an enabled stage after 90 days and records evolution history, but the exact timing and disabled-lower-stage cases lack accepted runtime/MCP evidence. |
| Country lifecycle | Partial / runtime blocked | Exact-country callbacks exist for state control, puppet/release, subject autonomy/free/annexation, government change, exile/reinstatement, civil-war end, and annexation. The shared global-host branch reconciles its former and new host on a player switch, but no general Event 027 tag-change callback or proof for a non-host human country was found. All lifecycle outcomes remain untested. |
| Achievements | Finished in source and art; runtime blocked | The three root IDs are registered, localised, receipt-driven, and have full DDS triplets/GFX aliases. Positive and negative runtime cases, save/reload behavior, and final consumer display are unproven. |
| Event Log and History | Finished in source; consumer blocked | One actorless global history row uses the firing batch-size payload. Country-specific duplicate history was not found. The Event Log consumer has not been visually/runtime proven. |
| Event Details and evolutions | Finished in source; consumer blocked | Shared Event Details includes the overview and four evolution records. Dynamic substitutions and final layout have not been proven in the consumer. A dedicated Event 027 scripted GUI is not part of the accepted design, so `chaosx_event_ui_worker` is not required. |
| National Breakthroughs cluster | Finished in source; probability/runtime blocked | Cluster 9 is canonical; Event 027 is Medium and optional by default, the selected trigger row is marked guaranteed, and source dispatch calls the event fanout once. Optional-member probability and no-duplicate runtime behavior remain unproven. |
| English localisation | Source-complete; visual blocked | The file is UTF-8 with BOM, has 338 unique keys and no duplicates; 69 direct Event 027 localisation references had no missing key. The scripted localisation file defines 119 `GetDoctrineResearch...` names. Popup/Event Details/Event Log visual substitution remains unproven. |
| Workbook and exports | Current target rows aligned | The XLSX Event 027 row is Minor Repeatable, cluster 9, `Needs Testing`; cluster 9 is National Breakthroughs and `Partially Available`. The Event 027 and cluster 9 CSV rows exactly match the current workbook. The honest testing statuses must remain until blockers close. |
| Static report and achievement assets | Runtime files finished; documentation/consumer partial | The report DDS and all nine achievement DDS files exist and are wired. The shared manifest and GFX handoff document only the achievement set; the report provenance and wiring are stranded in `generated_event_art_2026-08-29.md` instead of being promoted into the durable asset manifest/handoff. Consumer evidence and final temporary-workspace disposition are missing. |
| Decisions, focus trees, country packages, formables, dedicated scripted GUI, 3D units, frame animation, super-events | Not required by accepted closure | `027_doctrine_research_review_and_closure.md:235` explicitly closes broad expansion. No missing worker handoff is demanded for these out-of-scope surfaces. |

## Native mastery and empty-track findings

Installed vanilla documentation defines `add_mastery` as adding mastery points, not levels. It defines `set_sub_doctrine` with explicit folder and zero-based track forms. `has_mastery_level` checks the number of unlocked rewards for a subdoctrine, but the exposed trigger has no folder or track selector and the documentation exposes no direct numeric mastery-point getter.

The current source correctly responds to that limitation at the script level:

- `common/script_constants/027_doctrine_research_constants.txt:37-38` sets a one-point increment and a 1,000-iteration guard.
- `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt` contains 107 explicit `add_mastery` dispatches and 107 explicit `set_sub_doctrine` dispatches.
- Each exact-step wrapper calculates `expected = observed + 1`, adds one point with explicit folder/subdoctrine/track/index, re-runs the `has_mastery_level` readback, and succeeds only when observed equals expected.
- Empty-track wrappers call `set_sub_doctrine`, re-read after native banked mastery resolves, rewrite the receipt pre-level to that post-adoption native level, and then target one additional Event 027 level.
- If assignment immediately completes the branch, the transaction records `native_adoption`, does not consume the choice, and does not create a mastery receipt.
- Confirmation revalidates before mutation. `effect_applied` recovery requires both the stored and current post-level to equal recorded pre-level plus one. Current `native_adoption` recovery also verifies that the recorded Grand Doctrine remains active; the historical handoff that said this guard was absent is stale.

This is credible source-level exact-step logic, but it is not engine acceptance evidence. A one-point native mutation can be observed only after it happens; if the engine resolves banked progress or rewards in an unexpected way and readback overshoots, source quarantines the receipt but cannot roll the native doctrine mutation back. The same limitation applies to a rejected or unexpectedly completing `set_sub_doctrine` operation. Those are precisely the cases the accepted engine matrix was intended to settle.

Required unresolved native cases are:

1. Low, middle, and final reward transitions in Army, Navy, Air, and Chaos Warfare.
2. Fractional mastery immediately below and above a threshold.
3. Empty track with no bank, partial bank, enough bank for one reward, enough bank for several rewards, and enough bank to complete the branch.
4. Separate proof that native banked rewards are not attributed to the Event 027 receipt.
5. Special Forces track 0 and track 1 identity, including the two-occupied-track limitation.
6. Chaos Warfare identity and its owning establishment/downstream gates.
7. Prepared, effect-applied, native-adoption, and choice-consumed receipt recovery across save/reload.

## Queue, flow, and lifecycle findings

The append-only batch and receipt structures are materially stronger than the early implementation. Source now preserves stage and size, does not merge later firings, promotes the oldest queued row, rebuilds options at use time, closes exhausted rows without compensation, and consumes a choice only after a successful receipt finalization.

The human route has opening, domain, Grand Doctrine, track, branch, confirmation, result, continuation, completion, no-option, ambiguous, and native-completion pages. Pagination is free and deterministic. AI uses the same validity triggers and re-scores after each result.

The remaining acceptance cases are behavioral rather than missing source blocks: two overlapping firings, queued-stage immutability, no-option closure, human-to-AI and AI-to-human control changes, annexation without transfer, subject and exile transitions, government/ideology change, controller change, pure tag switch, countries created after the snapshot, and save/reload at every receipt state.

The pure tag-switch claim is narrower than the accepted requirement. `common/on_actions/chaosx_on_actions_chaos_meter.txt:37-56` handles the shared global host when control moves from an AI host to a new human host. It does not, by itself, prove that an arbitrary non-host human country's open Event 027 page is resumed exactly once after a player tag switch.

## Weighted AI and probability audit

The required probability pass was routed to `chaosx_ai_probability_auditor` for the shared repeatable-event selection/decay/recurrence, National Breakthroughs participation and trigger guarantee, AI domain, Grand Doctrine, track, empty-track subdoctrine, active-track subdoctrine, and multi-choice recalculation surfaces. The auditor changed no files.

The current source declares the full five-domain, 13-Grand-Doctrine, 18-track, and 107-subdoctrine weighted pools. It uses native force, production, war, geography, theatre, doctrine/role, continuity, completion, and Chaos owner-readiness signals rather than the stale flag-only strategy gates described in older handoffs.

Fresh inspection used source revision `17f12f50d2d90efa6405e47e8d53253f802dc69ce57225e2229e9a17efc24e61`. It returned `PROBABILITY_SOURCE_INSPECTED` for all requested surfaces:

| Weighted surface | Fresh disposition |
| --- | --- |
| Automatic repeatable Event 027 selection/recurrence | Custom adapter discovered zero `global.all_events` candidates and `poolComplete:false`; blocked, not zero probability. A direct source inspection of `chaosx_settings_effects.txt` also returned `INTERNAL_ERROR` with no revision or artifact. |
| National Breakthroughs participation | Seven source members exist, but the custom adapter discovered zero normalized candidates; optional-member probability remains blocked. The selected trigger's source guarantee is not a normalized probability result. |
| Domain | Five candidates; fresh evaluation produced 185 rows with five unresolved candidates. |
| Grand Doctrine | Thirteen candidates; fresh evaluation produced 481 rows with 13 unresolved candidates. |
| Track | Eighteen candidates; fresh evaluation produced 666 rows with 18 unresolved candidates. |
| Empty/active subdoctrine | 107 track-qualified candidates; fresh evaluation produced 3,959 rows with 107 unresolved candidates. |
| Multi-choice recalculation | Reuses the four chooser pools, but typed state, cadence, reset, and terminal inputs were unavailable; no accepted sequence result. |

The shared AI inspection reported 143 source candidates, zero runtime candidates, 143 required inputs, and one unresolved source surface. The typed fixture contained only empty state/flags; country, doctrine, mastery, templates, production, navy, geography, strategy, DLC, queue, cadence, and terminal state were not materialized.

Fresh evaluations all returned `PROBABILITY_ANALYZED_PARTIAL` and no accepted ranking or probability:

- Domain analysis `probability-d30bc0ec064fea14386ed7dc`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c406b844ef4b89205d57a5ee301aa674867daf8c4d117654dd803de27d851dfa/8e5b88a21e7ba529a32529fd7a6f0ecf4bdefaa1b7c5b210fda2357cd83a1048/probability-d30bc0ec064fea14386ed7dc.json`.
- Grand Doctrine analysis `probability-80eec446667ce92d4a051592`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1147cf8d05c1bc30e2a692b44a37a1b3e402580926304e1e03061f3cf4165b20/4d9978caf553d7e926ae0e8c96707c606e58278b6db74a0cd7e3a9e1b1ea7adb/probability-80eec446667ce92d4a051592.json`.
- Track analysis `probability-5333c119ae7bd5ad3109050a`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da1c252cb5aac8a6de5915b07d189ba99bc3628ba6521609990f482b485f808b/b029887af3d86d97a5170fcc90b233ebe0353e54dcbee94bed418942a4dcdf70/probability-5333c119ae7bd5ad3109050a.json`.
- Subdoctrine analysis `probability-315aec4b6ecd63e1a53974a6`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/213e1bded374426dddbb1a36ecb0b833e046dc860a9de4518b50ad9b47e68090/fbc7e61ce57cbafbadf4bbdceacb5098ab2e24dcd870619293822e135303080c/probability-315aec4b6ecd63e1a53974a6.json`.

The automatic-pool inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11baa6a2c8c92f31cad2234c8a5bde3c714eb225c8b916596fceb4a45498d2b2/f629b8381ff1fc3d2395b799962f14ae4ef6f43c81b6832b66d99dc90c487136/probability-inspect-f12c120215a4.json`. The cluster inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a343a06b38227395a5d5d6c309ceb66bfe98116ec56478173d1512c97dc1497a/a933d0d1d9aab10576e042e66760738e393338f84196092efd0a5bd80ca0cf58/probability-inspect-0637a6ffbe20.json`. The shared chooser inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8e23c4beee8da4827b9b506063b031bf20e33d4448461297c7923bd67245491/a359b7991974c6b761e9ccc275f9f544b1a5a2b9db6371f68607ed63973d49e3/probability-inspect-db288f956997.json`.

Same-current-source comparison controls returned zero changes for the four chooser layers, but all remained partial/unresolved. Their analysis IDs were `probability-e0e9302897b3ed625a9e2019`, `probability-e8a79c50668b40e981b9fbf5`, `probability-9ed1dfb1d13ce3a227572672`, and `probability-ea7a74d7096c060cb8634dd7`. These are not accepted before/after comparisons because no historical MCP baseline was available.

The 37-scenario set DR-A01 through DR-G03 used scenario hash `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb` and remains unresolved. No dominance, starvation, rank-reversal, repetition, timing, or exploit conclusion is accepted. A zero-candidate analyzer result is not evidence of zero probability or correct balance. No fresh sweep, simulation, or sequence result was accepted because the typed fixture and complete cadence/state/reset/terminal manifest were unavailable. AI/probability acceptance is **not complete**.

## MCP evidence and exact limits

### Event chain

Fresh `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` for Event 027 at revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`, graph hash `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`.

The lint artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa10236282b2d2200baa6cc7790147fe6293888a5aedfa7769f1575c6a4c3a41/7bf6f22e0ed6ca2a66cd4ec2e0ce818cc329c6b1f56b4139dc45461c1c66ad9a/event-lint-2725045f62d1.json`

The selected lint itself did not identify a direct Event 027 blocker, but validation is partial: helper and lifecycle projections were deferred, helper expansion returned zero helpers, and the workspace report retained one blocking diagnostic among 2,206 issues. Consequently the MCP graph does not inspect the transaction helpers that own almost all Event 027 behavior.

Fresh `hoi4.event_render` calls produced reachability, state, and options artifacts. The namespace reachability render selected 240 nodes and omitted 42,216; `.7` state selected 155; `.60` options selected 17. All were `EVENT_RENDERED_PARTIAL` and expanded zero helpers. Representative manifests are:

- Reachability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bca9b049feb2c24aeb3145a276549a9173809f491c8dedfb6e3f3607514dea28/78229e4b810cf8c26a9b479ef43b416fff944a815bd22d74240e098f6c37bf9e/event-reachability-2725045f62d1-manifest.json`.
- Confirmation state: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26655687493d066986d4034e74dc6f5307ee5912d5285af0c41d307d1d5edd1e/7d321416cf988ca7f0bd0037b8cc83d40ba10c891f3d2a0d69006fcdc8b82cb3/event-state-2725045f62d1-manifest.json`.
- First branch page: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d030988abb8de1829837ab6a24a8c1563ad642a2607c902033b4ee2da45707a/0f3e25184ec5940ad8280674b2275ee71fc2fc4d965a7e303b163cd3fdaaec40/event-options-2725045f62d1-manifest.json`.

The required changed-revision `hoi4.event_compare` call was attempted against the historical Event 027 revision and the current revision. It returned `EVENT_REVISION_NOT_CACHED`, no artifacts, and no comparison. Source-only reconciliation is not equivalent evidence.

### Doctrine and technology

Fresh `hoi4.tech_inspect` folder discovery returned `TECH_INSPECTED` at revision `ac84d6b4584c027ec973b87a5912b722369a97cce2400ff615bdac2149c3051a`, graph hash `2f912286e003f600c3d8a040d8c73b996150500ee84b228dffe886d634c2ea7c`. It indexed 679 technologies, 18 folders, 475 placements, 457 edges, 857 unlocks, and 520,298 references. Aggregate validation failed with 1,421 blocking technology diagnostics; focused Land, Naval, Air, and Special Forces lint calls did not isolate those aggregate diagnostics as Event 027 defects.

Fresh doctrine renders resolved Land/Chaos Warfare, Naval, Air, and Special Forces with 6, 4, 4, and 3 selected nodes. Every render returned `sourceAccurate: false` and the same failed aggregate validation. Their JSON hashes were respectively `4adb29301461403d974b96bd236fdf4454f2738a12177a03d8923691806e5701`, `2e1e4d0a346939e71c7bd2992fb09b5da02620ee1a924a7a905fd9afca49dc05`, `e6c7903e827b3a287a2a600ffb9b34c22a1d376a4555093bb97051292bc9e7a0`, and `9f07d323029cf9c42ea96d4cfba5eaaa4984ff0360687db6f57a14e4962a6d41`.

The required changed-revision `hoi4.tech_compare` call was attempted from historical revision `778e8f9b2c296c6626ce5d82788e15da1a80e0c3c0d4484d90218b0f93fd71cc` to the current revision. It returned `TECH_REVISION_NOT_CACHED`, no artifacts, and no comparison. The older same-revision zero-delta control proves only that the route once responded; it is not a before/after comparison.

## Event Log, Event Details, cluster, localisation, and catalog

The current source has the requested actorless global history behavior, Event Details overview, four evolution rows, Minor Repeatable classification, Event 027 debug/name mappings, and National Breakthroughs cluster membership. The compatibility `scientific_research` aliases remain, but cluster 9's canonical display and workbook name are National Breakthroughs.

The cluster source marks Event 027 optional when another member triggers the cycle and guaranteed when Event 027 is the selected trigger member. The root's global fanout is called once by the event itself. The actual optional roll distribution, delayed-member order, and duplicate-suppression outcome remain part of the probability/runtime blocker.

The localisation source audit found no duplicate Event 027 key or missing direct event-key reference. It does not replace consumer rendering: the largest popup pages, confirmation substitutions, native-completion page, Event Details, history row, and Event Log still require final visible evidence.

At the time of the final workbook read, the current XLSX Event 027 and cluster 9 rows exactly matched their CSV exports. Current hashes were:

| File | SHA-256 |
| --- | --- |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | `5453B77254A735465ABC8911F084AE90097E440782CAE1186A2D72E9B3E25A48` |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | `8D8AB229416FB30A0AE14720256583BF9E416542244248C5455F3B248814A88D` |
| `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | `4A3324F384F1B6180CB15F5B57B1F096405EF9F26F7FBD824EBCB1ABF69E7FF1` |
| `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | `05A5E47238CF23E12A3AC6BA09720106460B42A212B553563F1069E70F139EEE` |

The workbook was being modified elsewhere during this audit: its hash changed while the Event 027 and cluster 9 rows remained stable. Any later completion pass must re-read the live XLSX and regenerate exports through the repository exporter if the workbook is changed; these hashes are evidence anchors, not permission to overwrite concurrent work.

## Assets and achievements

The runtime report image exists at `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`, is registered as `GFX_report_event_027_doctrine_research`, and is used by the Event 027 pages. The generated-art handoff records a 210x176 BGRA DDS and SHA-256 `D7299954367B8374142A8A8242CEB8DE9117E80D3809D92CAED1339F188281A5`.

All three achievement IDs exist in the root registry and all nine 64x64 state DDS files exist with matching GFX aliases:

- `027_doctrine_research_first_lesson`.
- `027_doctrine_research_single_school`.
- `027_doctrine_research_joint_curriculum`.

The predicates are receipt-based. First Lesson requires a human-started multi-choice batch, a domain that was empty at batch start, a consumed adoption receipt, then a later consumed mastery receipt in that domain. Single School requires five exact `post = pre + 1` receipts on one branch in an Evolution IV batch and a final level of at least five. Joint Curriculum deduplicates stable domain/track pairs and unlocks on the fourth distinct mastery track.

The asset package is not documentation-complete. `docs/assets/027_doctrine_research/manifest.md` and `gfx_handoff.md` were replaced by achievement-only documents after the report-art worker said it had written the report crosswalk. Report provenance survives only in `generated_event_art_2026-08-29.md` and the report prompt/source files. The durable Event 027 manifest and GFX handoff must be reconciled to cover both the report and achievement families. The temporary asset workspace may remain while the event is blocked, but final acceptance requires promotion/disposition and consumer evidence.

## Historical handoff reconciliation and accepted-plan disposition

The following older findings are stale against current source:

- First-batch array alignment and receipt-parent alignment are now checked.
- Empty-track dispatch is no longer merely gated as “verified”; 107 explicit `set_sub_doctrine` wrappers and post-assignment readback exist.
- The large branch pages now have deterministic pagination.
- First Lesson now checks the immutable empty-domain snapshot.
- AI strategy scoring no longer depends only on unproduced country flags; native observable signals are used.
- `effect_applied` recovery rereads current level, and `native_adoption` recovery now checks the recorded active Grand Doctrine.
- The overview uses National Breakthroughs rather than the stale cluster name.

The following historical conclusions remain current:

- The event is source-playable but not acceptance-complete.
- Native mastery/banked-mastery and save/reload behavior are unproven.
- Event and doctrine changed-revision comparisons are unavailable.
- Named probability scenarios are unresolved without typed country/doctrine fixtures.
- Both occupied Special Forces tracks are a documented fail-closed limitation.
- Final popup/shared-consumer/achievement/asset presentation evidence is missing.

The improvement-loop review accepted closure rather than adding decisions, a dedicated GUI, focus trees, country packages, formables, super-events, 3D units, or animation. Current source follows that disposition. No later Event 027 expansion addendum was found that is both accepted and undisposed.

The parent implementation and follow-up plans have source implementations or explicit blocker dispositions. They have not been promoted to an acceptance-complete state because the evidence gates remain open. `docs/plans/027_doctrine_research_plans/mcp_evidence.md` is stale where it records older technology revision/artifact counts and obsolete workbook/export hashes; it must not be treated as the final evidence index until refreshed.

## Exact remaining blockers

1. **Premature default enablement.** Event 027 is in the default reworked allowlist despite its own acceptance file requiring full readiness first.
2. **Native exact-step proof.** No accepted engine trace proves one event-attributed level at low/middle/final, fractional, and banked states in every supported domain.
3. **Empty-track atomicity and bank preservation.** No accepted trace proves `set_sub_doctrine`, native bank resolution, Event 027's additional step, and receipt attribution in all required cases.
4. **Special Forces disposition.** Both-occupied-track mastery is suppressed. The owner must either provide a fully provable adapter or explicitly accept Special Forces as absent for that state/ruleset and align the spec/docs/UI.
5. **Persistence and idempotency.** Prepared, effect-applied, native-adoption, and consumed receipts plus overlapping queued batches lack save/reload traces.
6. **Lifecycle.** Annexation, subject/controller/ideology/exile transitions and arbitrary pure tag switches lack accepted evidence; the global-host switch branch is not proof for every human country.
7. **Evolution timing.** The 90-day scheduler and disabled-lower-stage cases lack accepted timing evidence.
8. **Probability.** DR-A01 through DR-G03 and changed-revision comparisons are not accepted until the probability auditor resolves typed scenario inputs and returns artifacts.
9. **Event MCP comparison.** The required before/after comparison is blocked by `EVENT_REVISION_NOT_CACHED`; helper expansion also returned zero, so the event graph does not certify the transaction helpers.
10. **Doctrine/technology MCP acceptance.** All focused renders report `sourceAccurate: false`, aggregate validation reports 1,421 blocking diagnostics, and changed-revision compare is blocked by `TECH_REVISION_NOT_CACHED`.
11. **Human and shared presentation.** Pagination/overflow, confirmation text, native-completion flow, Event Details, Event Log/history, and report art lack final consumer evidence.
12. **Achievement acceptance.** Positive/negative attribution cases, save/reload duplication resistance, and visible achievement consumers have not been demonstrated.
13. **Asset documentation.** The durable manifest/GFX handoff omits the report-art family, and the temporary workspace lacks final promotion/disposition.
14. **Evidence documentation.** The overview correctly says incomplete, but `mcp_evidence.md` contains stale technology and catalog artifact anchors.

Any one of blockers 1-10 is sufficient to reject an acceptance-complete claim under the Event 027 specification. The missing visual, achievement, asset, and documentation evidence independently prevents completion as well.

## Recommended next actions

1. Remove Event 027 from default automatic selection until the remaining acceptance gates close, or complete all gates before releasing the current default state.
2. Produce the owner-observed native test matrix for ordinary domains, Chaos Warfare, and Special Forces, including all banked-mastery and interruption states. Do not substitute source inspection for those traces.
3. Resolve the Special Forces both-occupied-track contract explicitly in the source-of-truth spec before changing behavior.
4. Restore typed country/doctrine fixtures in the probability MCP path and rerun every DR scenario, sweeps/sequences where specified, and same-scenario comparisons through `chaosx_ai_probability_auditor`.
5. Restore comparison-compatible Event and Technology revision caches, then rerun changed-revision `event_compare` and `tech_compare`; obtain source-accurate doctrine renders or record the exact server limitation.
6. Run the accepted queue, save/reload, lifecycle, evolution, achievement, and presentation scenarios without launching the game from an agent session; retain user-supplied/live-consumer evidence in the handoff package.
7. Merge the report-art records into the durable asset manifest and GFX handoff, dispose or explicitly retain temporary asset working files, and refresh `mcp_evidence.md` from the final source state.
8. Re-read the live workbook/export rows after concurrent work settles, rerun the localisation/spreadsheet audits if any target text changes, then rerun this completion audit.

## Final classification

- **Finished:** core source architecture, global fanout, country-owned batch/receipt structures, human chain, AI chooser structure, ordinary and Chaos adapter declarations, achievements and runtime assets, actorless history/Event Details/cluster source wiring, English source localisation, and current Event 027/catalog-row alignment.
- **Partial:** native mastery transaction, empty-track behavior, Special Forces, lifecycle, evolutions, visual consumers, achievements, asset documentation, and evidence documentation.
- **Blocked:** engine-native exact-step/banked behavior, persistence/idempotency traces, all accepted probability scenarios, changed-revision Event/Technology comparisons, source-accurate doctrine renders, and final consumer evidence.
- **Design gap:** Special Forces when both tracks are occupied and default enablement while acceptance blockers remain.

Therefore: **source-playable (qualified): yes. Acceptance-complete: no. Default-ready: no.**
