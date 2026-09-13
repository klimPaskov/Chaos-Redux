# Event 027 Doctrine Research final read-only completion audit

Date: 2026-09-01.

Role: `chaosx_event_completion_auditor` final read-only completion review.

Scope: Event 027 Doctrine Research only.

## Audit boundary

This audit read `AGENTS.md`, all sixteen files under `docs\specs\027_doctrine_research_specs\`, the current Event 027 event/effect/trigger/on-action/constants/localisation packages, shared registration and Event Log/Event Details/cluster integrations, achievements, GFX and DDS assets, CXT registration, current event documentation, the authoritative XLSX and generated CSV exports, and the latest Event 027 handoffs.

The required `chaos-redux-events`, `chaos-redux-event-planning`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-assets`, and repository `xlsx` skills were applied.

The offline Paradox wiki core event, trigger, effect, scope, localisation, on-action, decision, idea, AI, technology, and doctrine pages were consulted together with the installed vanilla documentation, including `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.

The official effects documentation confirms that `set_grand_doctrine`, `set_sub_doctrine`, and `add_mastery` are native country-scope effects.

No gameplay, localisation, asset, documentation-state, or workbook source was edited by this audit.

The only write is this requested handoff.

HOI4 was not launched.

Source inspection is not treated as live-engine, in-game, or final-consumer proof.

## Verdict

Event 027 is **source-playable with a known achievement correctness defect**.

The ordinary source path contains a global repeatable firing, one immutable country-owned batch per eligible country, queued batch progression, human and AI selection, native Grand Doctrine adoption, native empty-track assignment, exact-step mastery attempts, receipts, lifecycle recovery, evolutions, Event Log/Event Details integration, cluster integration, localisation, report art, achievements, and CXT registration.

Event 027 is **not acceptance-complete**.

No completion claim or completion commit is authorized by this audit.

The acceptance blockers include one newly identified source defect in Joint Curriculum tracking, unclosed live/native mastery and persistence scenarios, incomplete weighted-scenario evidence, partial and validation-false Event/Doctrine MCP evidence, missing accepted before/after comparisons, missing final consumer presentation evidence, stale evidence ledgers, default enablement before acceptance readiness, and an uncommitted implementation surface.

## Current source snapshot

| File | Current SHA-256 |
| --- | --- |
| `events\027_doctrine_research.txt` | `134FD2AEB6F1C2354D3758A46BBF13CA476FAA5567E52B2B0F4CBA09388FBEF7` |
| `common\scripted_effects\027_doctrine_research_effects.txt` | `01A05E7652E25F9A3CADD51386F74C9FB899E171A59512114DDE281E400899F4` |
| `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt` | `51B94513DDD690D7FD45E945F1A9C76E002AB527670117843CC6A176EBC1F525` |
| `common\scripted_effects\027_doctrine_research_ai_effects.txt` | `76919A4F84DE2C15DBF4387CDDD0FF869C4BAB6DCB00FE22FC196BB4D970E749` |
| `common\scripted_effects\027_doctrine_research_achievement_effects.txt` | `955D7C51C0A3105ABB9ABEB7A929F2AB2A23093A7C3909361D42FE3529F1ABE1` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt` | `A3774818D99F2F82DC26175330A23C192EABC1A4578A1124F44FC9D176F883B0` |
| `common\on_actions\027_doctrine_research_on_actions.txt` | `0531B4AA65C5AA09D0BC893C35721ACA50734F1B8C6917724CA9F366F1C01404` |
| `common\script_constants\027_doctrine_research_constants.txt` | `69F7412D01047D19638B49A215DB03847C8D7BADE0B68A0DADA563F8B0220C1B` |
| `localisation\english\027_doctrine_research_l_english.yml` | `BCADE443732B5D38ADD8CE73F0FB1A196ED322DA7821040020A993BE4F6690E9` |

The Git worktree does not contain a promoted Event 027 completion revision.

The main event file and workbook/exports are modified, while the Event 027 effect, trigger, on-action, constants, CXT, documentation, report GFX, and many handoff files are untracked.

`common\achievements\chaos_redux_achievements.txt` is `MM`.

This dirty/untracked state is not itself proof of a gameplay defect, but it is a release and completion blocker because the implementation has not been reviewed and committed as one complete plan.

## Completion status by surface

| Surface | Source status | Acceptance status | Evidence and disposition |
| --- | --- | --- | --- |
| Root, category, repeatability, and global firing | Implemented | Partial | `events\027_doctrine_research.txt:13-18` defines hidden actorless root `chaosx.nr27.1`. `common\scripted_effects\chaosx_logic_effects.txt:325` registers Event 027 as repeatable and lines 188-190 assign tier 0. `common\scripted_effects\027_doctrine_research_effects.txt:1744-1751` performs one bounded `every_country` pass limited to countries with a valid adapter action. Runtime fanout and exact eligibility are not proven. |
| Default automatic selection | Implemented | Design deviation / blocker | `common\scripted_triggers\chaosx_settings_triggers.txt:31` includes Event 027 in the default-enabled reworked-event allowlist. `docs\specs\027_doctrine_research_specs\027_doctrine_research_acceptance_criteria.md:13` permits default enablement only when the full rework is ready for normal selection. The event is not acceptance-ready. |
| Country batch snapshot and queue | Implemented | Partial | `027_doctrine_research_effects.txt:1757-1787` appends immutable batch id, stage, size, remaining choices, status, date, human-start state, and five start-empty domain values. Lines 1791-1825 activate only the first queued row. Overlap, save/reload, and resumed ordering still lack accepted runtime traces. |
| Receipt and transaction lifecycle | Implemented with fail-closed paths | Partial / blocked | Receipt rows begin in `prepared`, move through `effect_applied`, `native_adoption`, `choice_consumed`, `invalid`, or `ambiguous`, and decrement a choice only in finalization at lines 3037-3050. Effect-applied mastery recovery rereads native state and requires stored and observed levels to equal pre-level plus one at lines 3166-3205. Native-adoption recovery reloads the recorded Grand Doctrine and requires it to remain active at lines 3208-3220. Interruption and save/reload idempotency remain unproven. |
| Grand Doctrine adoption | Implemented | Partial | The main effects package contains 13 explicit `set_grand_doctrine` operations covering 4 Army, 3 Navy, 3 Air, 2 Special Forces, and Chaos Warfare. Source guards prevent replacing an active Grand Doctrine. DLC and owner-state behavior still requires live proof. |
| Native mastery and empty-track assignment | Implemented | Blocked for acceptance | `027_doctrine_research_exact_mastery_effects.txt` contains 107 explicit `add_mastery` operations and 107 explicit `set_sub_doctrine` operations. The source rereads `has_mastery_level`, adds one raw point at a time, and accepts only the expected pre-level plus one. Constants are `mastery_point_increment = 1`, loop limit 1000, scan limit 20, normal maximum 5, and Peoples War maximum 4 at `027_doctrine_research_constants.txt:35-39`. This is not live proof of fractional/banked mastery, exact threshold behavior, or rollback safety if native state skips the expected level. |
| Army, Navy, Air, and Chaos Warfare adapters | Implemented in source | Partial | Registry, validity, adoption, empty-track, active-track, completion, display, and AI rows are present. The corrected Doctrine Viewer renders resolve Land/Chaos, Naval, and Air nodes, but are validation-false and `sourceAccurate: false`. Direct low/mid/final and DLC matrix traces remain missing. |
| Special Forces adapter | Fail-closed in source | Design gap / blocked | Empty-track assignment is explicit, but active mastery is withheld when reused Special Forces subdoctrine tokens cannot prove a unique track identity. This is disclosed rather than silently mapped, but the current-ruleset fully-adapted-or-explicitly-absent contract and both occupied-track cases still lack accepted native evidence. |
| Human event chain and pagination | Implemented | Partial | The source contains 31 unique Event 027 IDs with no duplicates: `.1-.13` and `.60-.77`. It provides opening, domain, Grand Doctrine, track, subdoctrine, confirmation, result, continuation, summary, no-option, ambiguous, and adoption-only paths. Native event-popup overflow, navigation, disabled states, and click-through have not been accepted. |
| Dynamic presentation and localisation | Implemented in source | Partial | The current English file contains 336 string keys plus its language header, and all 256 direct Event 027 title/description/option references found by the static scan resolve. The current file has a BOM. The post-fix localisation file is newer than `localisation_auditor_current_2026-09-01.md`, so no independent current-hash localisation handoff or final popup render exists. |
| AI chooser and recalculation | Implemented in source | Blocked for weighted acceptance | Four `random_list` surfaces select 5 domains, 13 Grand Doctrines, 18 track identities, and 107 subdoctrines. Scoring uses force, production, war, geography, theater, strategy, continuity, completion, and owner-readiness signals, and the chooser is rerun after each successful choice. Current named-scenario and baseline/current evidence is recorded separately below. |
| Evolution I-IV scheduling | Implemented in source | Partial | Baseline through Evolution IV use batch sizes 1-5 and centralized 90-day staged promotion in `027_doctrine_research_effects.txt:99-214`. Actorless evolution records are emitted at lines 1705-1741. Pacing, already-high-chaos startup, disabled-stage behavior, and repeat firing after promotions lack accepted runtime traces. |
| Lifecycle, controller, annexation, and tag-switch recovery | Implemented in source | Partial | `027_doctrine_research_on_actions.txt:12-70` covers state control, puppet/release/subject/autonomy, annexation, government change, exile/reinstatement, and civil-war end. The shared host logic reconciles a player-host switch at `common\on_actions\chaosx_on_actions_chaos_meter.txt:37-56`. Save/reload, annexation, subject, controller, exile, and pure tag-switch behavior remain unproven. |
| Event history, Event Log, Event Details, and evolutions | Implemented in source | Partial | Event 027 records the firing batch size as immutable actorless history payload at `chaosx_logic_effects.txt:1304-1312`. Shared Event Details adds four evolution previews at `chaosx_events_log_effects.txt:3041-3065`, and scripted localisation resolves the history sizes, evolution titles/bodies, cluster, and details. No accepted Event 027-specific final consumer capture exists. |
| National Breakthroughs cluster | Implemented | Partial | `chaosx_event_cluster_effects.txt:1900-1939` defines the seven-member cluster and Event 027 as slot 1, Medium severity. Event 027 maps to cluster 9 at lines 833-842. Cluster status honestly remains `Partially Available` because other members are not all complete; that status is not an Event 027 defect. Complete cluster probability evidence remains missing. |
| Achievements | Partial with source defect | Blocked | First Lesson and Single School have receipt-backed predicates. Joint Curriculum has a cross-batch accumulation defect described below. All three definitions, localisation entries, and active/grey/not-eligible icon triplets are present, but positive and negative runtime matrices are missing. |
| Report and achievement assets | Produced, documented, and wired | Partial | The report source/generated/processed/runtime chain and three native-ImageGen achievement source chains are recorded in `docs\assets\027_doctrine_research\manifest.md`. The report DDS hash matches the manifest and all nine achievement DDS files exist at 64x64 and 16,512 bytes. GFX wiring is present at `interface\027_doctrine_research.gfx:10-11` and `interface\chaosx_achievements.gfx:1564-1572`. Final in-game consumer evidence is absent. |
| CXT extension | Implemented | Partial | The package-owned idempotent apply effect, modifier-free hidden carrier, one bounded startup registration, and `on_daily_CXT` fallback are present in the three `027_doctrine_research_cxt_*` files. No accepted CXT consumer trace is present. |
| Catalog workbook and exports | Current data; stale worker evidence | Partial | The workbook Event 027 row is `Doctrine Research`, Minor Repeatable, chaos level 1, cluster `9`, status `Needs Testing`, with baseline and Evolution I-IV text aligned to current player-facing wording. Cluster 9 is National Breakthroughs with members `27, 54, 65, 67, 83, 85, 89`, matching severities, and `Partially Available`. The three CSVs were regenerated one second after the workbook save and their Event 027/Cluster 9 rows match. The current file hashes no longer match the spreadsheet worker handoff. |
| Documentation and handoff state | Present but stale in places | Blocked from closure | Specs, overview, status ledger, MCP ledger, asset handoffs, probability handoffs, localisation handoffs, spreadsheet handoffs, and parent audits exist. Several current-status hashes and promoted evidence statements predate current source and are enumerated below. |
| Dedicated Event 027 scripted GUI | Not in scope | Not applicable | Event 027 introduces no event-owned `.gui` or scripted GUI mechanic window. It uses native event pages and the shared Event Log/Event Details framework. A `chaosx_event_ui_worker` handoff is therefore not required for this event. |
| Portraits, 3D units, sounds, counters, animations, super-events, focus trees, decisions, countries, and formables | Not in scope | Not applicable | No character portrait, custom 3D unit, unit audio, custom counter, frame animation, super-event, focus tree, decision/mission package, country package, or formable is introduced by Event 027. Their specialist handoff gates do not apply. |

## Confirmed source defect

### Joint Curriculum can combine progress from different batches

`common\scripted_effects\027_doctrine_research_achievement_effects.txt:167-174` initializes `doctrine_research_joint_curriculum_found` once before iterating candidate batches.

For each human-started batch of at least four choices, lines 185-203 correctly reset every per-track `*_seen` temporary variable and lines 204-231 inspect only receipts whose batch id matches the current candidate batch.

Lines 234-268 increment `doctrine_research_joint_curriculum_count` for each distinct track seen in that candidate batch.

There is no `set_temp_variable = { doctrine_research_joint_curriculum_count = 0 }` before the outer loop or inside the per-batch block.

Line 270 unlocks when the accumulated count is greater than `evolution_ii_batch_size`, which is 3, meaning four or more.

Because temporary variables persist through this effect chain, a first eligible batch with two distinct mastery tracks can leave count 2, and a later eligible batch with two different mastery tracks can raise the same count to 4 and unlock the achievement even though neither batch contains four distinct tracks.

This violates the accepted requirement that Joint Curriculum record four distinct track identities **in one evolved batch**.

The achievement is therefore not source-correct and cannot be accepted until the owner resets the count for every candidate batch and reruns positive and cross-batch negative cases.

This audit did not patch the defect.

## Native doctrine operation audit

The current source uses the native operations requested by the specification.

- Grand Doctrine adoption uses 13 explicit `set_grand_doctrine` calls in `common\scripted_effects\027_doctrine_research_effects.txt`.
- Active mastery uses 107 explicit `add_mastery` calls in `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt`.
- Empty-track assignment uses 107 explicit `set_sub_doctrine` calls in the same generated exact-adapter file.
- Every active wrapper carries an explicit folder, subdoctrine, track token, and zero-based track index.
- Empty-track wrappers select a branch with `set_sub_doctrine`, reread native mastery, and attempt one exact step only while the branch remains incomplete.
- If native assignment itself completes the branch, the source records adoption-only and does not consume a curriculum choice.
- No generic military experience reward, research-bonus substitute, technology grant shortcut, active-Grand-Doctrine replacement, or fixed multi-level mastery dump was found.

The implementation is deliberately conservative, but the exact one-level contract remains engine-sensitive.

The loop adds one raw mastery point until the observed level is exactly pre-level plus one or the 1000-point guard is exhausted.

Static review cannot prove how fractional or banked mastery is represented, that one raw point cannot skip the expected level under every supported modifier/DLC state, that assignment preserves all native banked progress, or that an over-advance can never occur before quarantine.

Required direct evidence remains missing for low, middle, and final levels in every domain; fractional and banked mastery; empty-track assignment; native completion during assignment; Peoples War's four-level maximum; both Special Forces reused-token tracks; and Chaos Warfare.

## Fresh HOI4 MCP evidence

### Event Chain Viewer

Fresh read-only `hoi4.event_inspect` trace for `{ kind: "event", eventId: "chaosx.nr27.1" }` returned status `ok`, code `EVENT_INSPECTED_PARTIAL`, current revision `b8b928ac6119099215dd486990704d24c5ac36e2b4a305713954081663d1884d`, and graph hash `4de181295a914d2f86f42d604a900365f19e2e39651179608128d3cca756127e`.

The authoritative trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c071aaeda8cda9358f3bfc8fffa5a9eb2b1fd4437d2b139733b72c72de022fa6/2e569930699a537fca65287405caa13a177c861c51439a8cb8f9438552f2019a/event-trace-b8b928ac6119.json`.

Validation is false because the large workspace deferred workspace-wide helper and lifecycle projections.

The graph reports zero expanded helpers, 8,682 unresolved nodes, 2,206 issues, and one aggregate blocking diagnostic.

The current Event 027 file overview render returned `EVENT_RENDERED_PARTIAL`, selected 120 bounded nodes, omitted 42,338 nodes, and produced manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11d7d02868a9f0f99ead01352f8c20efc7d062d9ec96841d5a07f190ca9d316e/2cca0448ee16547cd2f91e2ff0a2161e1a9dd75a64b7699918007d9328dda7c0/event-overview-b8b928ac6119-manifest.json`.

The confirmation-event state render for `chaosx.nr27.7` returned `EVENT_RENDERED_PARTIAL`, selected 150 nodes, omitted 42,308 nodes, and produced authoritative JSON hash `ede599f881bd7a70ee353351791abe04a66f985775629e97b519866cfd967b18`.

These artifacts establish current static graph visibility, not helper-complete or live chain proof.

The required comparison from prior audited revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570` to current revision `b8b928ac6119...` returned status `error`, code `EVENT_REVISION_NOT_CACHED`, zero artifacts, and blocker message `Requested event graph revision is not cached`.

Source diff review is not treated as an event comparison substitute.

### Doctrine and Technology Viewer

Fresh `hoi4.tech_inspect` folder inspection returned `TECH_INSPECTED` at revision `fa3a43bcfac33c1f2d3955e64f4fdfb1fcedd39f438f630e2d6e8eb2c757c3be`, graph hash `3065735c93c843d1d6584a1704f3cd8f2befa250ef9b44cd2362fe2dc10ae158`, 679 technologies, 18 folders, 475 placements, 457 edges, 857 unlocks, 520,298 references, and three unresolved index entries.

Its authoritative folder artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b660f6d6323de25ab5978a538f640ce994fb6b338dcb1548d699a7900e610240/b6b073725adda267e930035e2f9f9c6d4330402f4a88dc9df83e567e1f293b8a/technology-folders-fa3a43bcfac3.json`.

Validation is false because the workspace reports 1,417 blocking technology diagnostics.

Corrected doctrine renders using the native folder tokens selected 6 Land/Chaos Warfare nodes, 4 Naval nodes, 4 Air nodes, and 3 Special Forces nodes.

Their authoritative JSON hashes are Land/Chaos `34040b1cc320681944889a861a2ecc336a3795b8fb6d763bf42c8b6772bd3cf3`, Naval `59f4eb19a8d52796bc5742f9127c84bcd93148a94e1a444cf484d4b5e8c8479b`, Air `89e193e4a8ace07cae8fa50ca55bfad31701e26956ccbd0be55a293526625806`, and Special Forces `f862de438c7e3a220db2f9cd5e3b98aa90244d3ca4333dfc3ec1a82926e5df5d`.

Every doctrine render reports `sourceAccurate: false` and inherits the 1,417 aggregate blocking diagnostics.

The required comparison from prior audited revision `7080c50bf1467579a159640153bbb2d43902b0b7a42a6c35daa41609a5124ed9` to current revision `fa3a43bcfac3...` returned status `error`, code `TECH_REVISION_NOT_CACHED`, zero artifacts, and blocker message `Requested technology revision is not cached`.

The current doctrine artifacts are useful source-resolution evidence but do not satisfy the accepted inspect/render/compare or native-operation proof gates.

## Weighted AI and probability evidence

The current weighted implementation was routed to a fresh `chaosx_ai_probability_auditor` with `fork_context=false` and no write authority.

The specialist independently fingerprints `common\scripted_effects\027_doctrine_research_ai_effects.txt` as `76919A4F84DE2C15DBF4387CDDD0FF869C4BAB6DCB00FE22FC196BB4D970E749`, matching this audit and differing from the stale parent handoff fingerprint `6C4B7C58...`.

The MCP probability source hash is `cbf30e6c9ce4e64721b69dac436017e7c4c856b8b855e2ac27c12040567bb550`.

Fresh focused `hoi4.probability_inspect` calls found all four declared pools and reported `poolComplete = true` at inspect revision `d572589f3028e5860ab081ad7ed0da120de7d18988b86dce80f1e75bbdd6f2f1`:

| Weighted surface | Selector span | Candidate count | Fresh evaluation result |
| --- | --- | ---: | --- |
| Domain | `:19.entry.2` through `:19.entry.6` | 5 | 37 scenarios; 5 unresolved candidates |
| Grand Doctrine | `:147.entry.2` through `:147.entry.14` | 13 | 37 scenarios; 13 unresolved candidates |
| Track | `:328.entry.2` through `:328.entry.19` | 18 | 37 scenarios; 18 unresolved candidates |
| Subdoctrine | `:2005.entry.2` through `:2005.entry.108` | 107 | 37 scenarios; 107 unresolved candidates |

The inspect artifacts are:

- Domain: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/393e3bce4d73b2901c8aa96a119ad7ce9088bcbdcf2b02e1c4afb1a94c5c2529/fb2abb2d55ad89fd161fea770056f6f8c90f237c3577f6849dd307440529b44f/probability-inspect-cbf30e6c9ce4.json`.
- Grand Doctrine: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56bd66d5b7f10d37bbf283b1740dcb15f9bc11b480008cf7067160b328bb5f7a/92065a6e214eab1ebf6724b46b6fe20703ef295c43454260143135ef6277668a/probability-inspect-cbf30e6c9ce4.json`.
- Track: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04ca127f85a7cbb9272a5946edbb99e1f02b08777d54a84761e4123caaaacb59/01663e114d93bb78c5d08786c560bc6273583715ecef96db00afeaa8a7fe6547/probability-inspect-cbf30e6c9ce4.json`.
- Subdoctrine: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed8f04f928aa4cc9d04eb5e8c2a055cb38b24ce508990a36764264fdf624e616/00071dd3b540a7be9ceefa52b08dec5785f1865c369d434b0a93d9c689e12d9c/probability-inspect-cbf30e6c9ce4.json`.

The fresh scenario set `DR_027_CURRENT_2026_09_01_REAUDIT`, hash `c0fc406e405dd91b00da4865451d51fb25b11a1e50cf642aaae0701b67b6994a`, contains exactly all 37 required scenario IDs: `DR-A01` through `DR-A06`, `DR-B01` through `DR-B04`, `DR-C01` through `DR-C07`, `DR-D01` through `DR-D06`, `DR-E01` through `DR-E06`, `DR-F01` through `DR-F05`, and `DR-G01` through `DR-G03`.

All four evaluations returned `PROBABILITY_ANALYZED_PARTIAL`; unresolved values were not treated as zero or impossible.

The fresh analysis identifiers and artifact hashes are:

- Domain: `probability-15e84b720ed4f5e4cf4adb7f`, artifact SHA-256 `ad9c9f43aeb46d9298de46a49a5c389a45764b256b533b0a54aec03d2c979ace`.
- Grand Doctrine: `probability-879217d53bb7a9f4d5fa4a5d`, artifact SHA-256 `da308b970e1c188626a378da880f29e29178fd54f29e6189358953e0511d876d`.
- Track: `probability-e0823a01cdb342ade5b4689c`, artifact SHA-256 `c33d7e3657965cc5f0e7b6f5ecb7d21454cd797839d4d156538bf2047a150f41`.
- Subdoctrine: `probability-460fcc071f63709618a98cb0`, artifact SHA-256 `698dd9ba4128d97bbc9dc4ea6611ce1308e14d1476d62f3b6a515ccdf257b311`.

The declared domain-score fixture produced exact normalized score-only results:

| Scenario | Raw scores `(Army, Navy, Air, Special Forces, Chaos)` | Conditional probabilities |
| --- | --- | --- |
| `DR-A01` | `(30, 5, 10, 0, 0)` | `(.6667, .1111, .2222, 0, 0)` |
| `DR-A02` | `(8, 30, 12, 0, 0)` | `(.1600, .6000, .2400, 0, 0)` |
| `DR-A03` | `(15, 8, 30, 0, 0)` | `(.2830, .1509, .5660, 0, 0)` |
| `DR-A04` | `(18, 0, 8, 0, 0)` | `(.6923, 0, .3077, 0, 0)` |
| `DR-A05` | `(20, 18, 8, 0, 0)` | `(.4348, .3913, .1739, 0, 0)` |
| `DR-A06` | `(0, 0, 0, 0, 0)` | all probabilities `null` |

These values prove only normalization of supplied primitive scores.

They are not native GER/JAP/USA/SOV/FRA/ITA adapter evidence.

The analyzer reported starvation warnings for zero-valued candidates and `PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO` for `DR-A06`.

The unresolved scenario groups are material:

- `DR-B01` through `DR-B04` lack native force, production, war, doctrine, armor/manpower, plan, and DLC state.
- `DR-C01` through `DR-C07` lack selected domain/Grand Doctrine, track state, mastery, banked progress, and transition state.
- `DR-D01` through `DR-D06` lack CBRN readiness, DLC, special-country adapter, and owner-system binding.
- `DR-E01` through `DR-E06` lack batch size, active stage, queue, mastery, and between-choice transition state.
- `DR-F01` through `DR-F05` lack completed repeatable-event and National Breakthroughs custom-pool and sequence evidence.
- `DR-G01` through `DR-G03` lack human parity, DLC boundaries, unavailable-adapter, and invalid-adapter behavior.

`hoi4.probability_render` succeeded for Grand Doctrine, track, and subdoctrine analyses and emitted ranking, matrix, and unresolved artifacts.

The domain render returned `PROBABILITY_ANALYSIS_STALE` because analysis revision `d572589f...` no longer matched current revision `3e88d4ef...`.

The repeatable/cluster custom-pool final probe was interrupted before returning a result.

No current sweep, simulation, sampled sequence, timing, or campaign-level balance conclusion is available because no adapter-supported native numeric ranges, explicit uncertainty distribution, or complete custom pool was available.

The mandatory `hoi4.probability_compare` was not run.

Exact blocker: no reconstructable baseline/current source pair exists; the AI file is untracked in `HEAD`, and the old handoff's `6C4B7E9...` source and `12845...` MCP revision do not match the current checkout.

Source-only comparison is not treated as an MCP probability comparison substitute.

Weighted-source implementation exists, but probability acceptance is blocked.

## Catalog freshness

The authoritative workbook is `docs\spreadsheets\chaos_redux_events_catalog.xlsx`.

Current workbook SHA-256 is `EC766D3E74E15240BD6E504BF14D8F6F630FE6F1D2FB062AF4F5AF818912B72A`, saved at 2026-09-01 11:33:03.

The generated exports were all saved at 2026-09-01 11:33:04:

- `chaos_redux_events_catalog.csv`: `101B547AB121EABD7AA191FF2A9295F6B35066C19B506A75C07C060BA51560A7`.
- `chaos_redux_clusters_catalog.csv`: `D91CBFED210ACB72A67EF46A4C48D50A0A49F023E583615628388DF276DDFB33`.
- `chaos_redux_scenarios_catalog.csv`: `05A5E47238CF23E12A3AC6BA09720106460B42A212B553563F1069E70F139EEE`.

The XLSX and CSV Event 027 rows match on name, baseline details, Evolutions I-IV, Minor Repeatable type, chaos level 1, cluster 9, and `Needs Testing` status.

The XLSX and cluster CSV agree on National Breakthroughs membership and severities.

The cluster membership row for slot 1 reads: `The selected breakthrough is guaranteed and grants each eligible country one doctrine curriculum.`

The catalog content is fresh and honestly not marked complete.

The evidence handoff is stale: `spreadsheet_worker_current_2026-09-01.md` records workbook hash `3B131756...` and Event CSV hash `E8A5A833...`, which do not identify the current files.

## Asset and consumer audit

The asset workflow satisfies the source/package side of the event-assets skill.

The report is a fictional native-ImageGen period documentary scene processed to the 210x176 report consumer and converted to final DDS.

The current runtime report DDS hash is `D7299954367B8374142A8A8242CEB8DE9117E80D3809D92CAED1339F188281A5`, matching the manifest.

The processed report image was visually reviewed and presents an appropriate monochrome joint-service training scene with an officer, armor/artillery, and aircraft cues and no readable modern branding.

The three achievement motifs and their grey/not-eligible states were visually reviewed through the contact sheet and are distinct and legible at the review scale.

All nine final achievement DDS files exist, are 64x64, and are 16,512 bytes.

The source, processing, reference-family, checksums, final paths, and parent wiring are documented in `docs\assets\027_doctrine_research\manifest.md` and `gfx_handoff.md`.

No placeholder art was found on the final Event 027 runtime paths.

Final in-game event-report and achievement consumer proof remains missing.

Because Event 027 has no portraits, custom units, animations, unit sounds, or counters, their mandatory specialist handoffs are not required.

## Documentation and evidence freshness gaps

The current status ledger fingerprints `027_doctrine_research_effects.txt` as `CB5F51FB...`, while the current file is `01A05E76...`.

The latest AI probability handoff fingerprints `027_doctrine_research_ai_effects.txt` as `6C4B7E9B...`, while the current file is `76919A4F...`.

The latest AI probability handoff also fingerprints the main effects file as `CB5F51FB...`, so it does not cover the current weighted/source snapshot.

The latest localisation auditor handoff predates the current `BCADE443...` localisation file and therefore does not certify the post-fix wording.

The spreadsheet worker handoff predates the current XLSX and Event CSV hashes even though the workbook and generated exports are data-current.

The current overview and `documentation_state.md` correctly avoid a completion claim and list major runtime/MCP blockers, but their hash-ledger and promoted-evidence sections need another reconciliation after the current source and audit findings.

The new Joint Curriculum defect is not disclosed in the latest parent static audit or current documentation state.

The accepted criteria file remains intentionally unchecked and the catalog remains `Needs Testing`, which is consistent with the actual acceptance status.

## Accepted-plan and handoff disposition

The accepted design authority is the specification package under `docs\specs\027_doctrine_research_specs\`.

No standalone improvement addendum or accepted plan exists under `docs\plans\027_doctrine_research_plans\` beyond the MCP ledger, documentation-state ledger, and handoffs.

No undisposed accepted expansion plan was found.

The implementation broadly realizes the accepted core, choice-flow, evolution, presentation, registry, cluster, asset, achievement, and CXT design, subject to the defects and evidence gaps in this audit.

Historical explorer, architecture, probability, transaction, and completion handoffs are correctly treated as superseded current-status authorities where later source changed their findings.

Generated report art and icon handoffs were promoted into source wiring, but final consumer acceptance is still queued.

The spreadsheet handoff was promoted into the workbook/exports, but its recorded hashes are stale after the latest save/export.

The post-fix localisation audit remains queued and unpromoted for the current hash.

Probability baseline/final handoffs are not accepted as complete weighted evidence.

All named Event 027 subagent patches or asset outputs found in scope have corresponding handoff files; the problem is currentness and acceptance, not absence of handoff notes.

The Event 027 implementation itself remains uncommitted and therefore unpromoted as a completed plan.

## Meaningful validation performed

- Read all sixteen specification files and reconciled them against current source rather than relying on earlier completion summaries.
- Confirmed 31 unique Event 027 definitions and zero duplicate Event 027 IDs.
- Confirmed all 256 direct Event 027 event localisation references found by the static scan resolve in the current English file.
- Confirmed the source counts of 13 native Grand Doctrine adoption operations, 107 native mastery operations, and 107 native empty-track assignment operations.
- Traced batch append, queue activation, receipt finalization, effect-applied recovery, native-adoption recovery, quarantine, AI batch resolution, lifecycle callbacks, and annex cleanup in current source.
- Inspected the current XLSX read-only and compared Event 027, Cluster 9, and membership rows to the generated CSV exports.
- Verified current hashes and timestamps for the gameplay snapshot, localisation, workbook, exports, documentation, and latest handoffs.
- Verified the report DDS against its manifest, enumerated all nine achievement DDS files, checked GFX wiring, and visually reviewed the processed report and achievement contact sheet.
- Ran fresh read-only Event Chain Viewer inspect/render and Doctrine Viewer inspect/render calls and attempted the mandatory changed-revision comparisons.
- Routed every weighted Event 027 surface to the required read-only `chaosx_ai_probability_auditor`.

## Validation still missing

- Direct engine/runtime proof for exact one-level mastery at low, middle, and final levels in Army, Navy, Air, Special Forces, and Chaos Warfare.
- Fractional and banked mastery preservation, empty-track assignment, native completion during assignment, Peoples War, and reused Special Forces identity traces.
- Save/reload and interruption traces for `prepared`, `effect_applied`, `native_adoption`, `choice_consumed`, ambiguous, and quarantined receipts.
- Overlapping batch ordering, repeat firing, zero-option exhaustion, branch completion removal, and immutable snapshot persistence through save/reload.
- Annexation, puppet/release, controller, exile/reinstatement, civil-war end, government change, and pure tag-switch traces.
- Evolution startup-at-high-chaos, 90-day promotion, disabled-stage, and repeat-firing timing evidence.
- Accepted Event 027 before/after event comparison and doctrine comparison.
- Source-accurate, validation-passing doctrine renders for every supported domain and Chaos Warfare.
- Complete current-hash weighted evidence for all 37 named scenarios, complete custom pools, sweeps, sequence/simulation where specified, and same-scenario baseline/current comparison.
- Positive and negative runtime matrices for First Lesson, Single School, and Joint Curriculum, including a cross-batch negative case after the source defect is fixed.
- Final native event-popup presentation for the largest paginated pages and dynamic mastery strings.
- Final Event History/Event Log/Event Details/cluster/evolution consumer presentation.
- Final in-game report art and achievement-state consumer presentation.
- A current independent localisation audit, current spreadsheet evidence handoff, and refreshed documentation/hash ledger.
- A clean reviewed completion commit after every blocker is closed.

## Simplifications, omissions, and blockers

1. Joint Curriculum currently permits cross-batch count accumulation and is a confirmed source-level correctness blocker.
2. The exact one-level mastery implementation is source-present but not engine-proven for fractional, banked, final-level, assignment, Special Forces, or Chaos Warfare cases.
3. Receipt persistence, idempotency, overlap, and lifecycle behavior are source-present but lack accepted save/reload and runtime traces.
4. Special Forces active-track mapping deliberately fails closed in ambiguous reused-token states; accepted proof of the current-ruleset limitation is missing.
5. Default automatic selection is enabled before the acceptance criteria are complete.
6. Event inspect and render are current but partial and validation-false; helper and lifecycle projection is deferred.
7. Event comparison is blocked by `EVENT_REVISION_NOT_CACHED`.
8. Doctrine inspect/render resolves current source but remains validation-false, reports 1,417 aggregate blockers, and marks every focused render `sourceAccurate: false`.
9. Doctrine comparison is blocked by `TECH_REVISION_NOT_CACHED`.
10. Fresh probability inspection found every declared candidate pool, but all four 37-scenario evaluations are partial; native B-G state, repeatable/cluster sequence evidence, domain render currency, sweeps/simulations, and a genuine baseline/current `hoi4.probability_compare` remain blocked or missing.
11. Largest native event pages, shared log/details surfaces, achievements, and final assets lack accepted consumer evidence.
12. Current localisation, workbook/export, AI, effects, and documentation snapshots are not consistently fingerprinted by the latest handoffs.
13. The implementation is still modified/untracked and has no honest completion commit.

No undisclosed fallback reward, generic experience substitute, technology shortcut, active-doctrine replacement, reduced country pool, copied counter, portrait placeholder, 3D placeholder, unlicensed audio package, or event-owned GUI shortcut was found.

## Recommended next actions

1. Have the gameplay owner reset `doctrine_research_joint_curriculum_count` for every candidate batch and add a two-batch negative proof alongside the four-distinct-tracks positive proof.
2. Decide the default-enable release state against acceptance criterion line 13; the accepted conservative disposition is to keep normal selection disabled until the remaining gates close.
3. Run the owner-controlled native doctrine matrix for low/mid/final, fractional/banked, empty-track, native-completion, Peoples War, Special Forces, Chaos Warfare, and DLC combinations.
4. Run interruption/save/reload, overlapping queue, annexation, subject/controller, exile, government, civil-war, and tag-switch scenarios with receipt and batch-state evidence.
5. Restore cacheable baseline/current Event and Doctrine Viewer revisions and rerun `hoi4.event_compare` and `hoi4.tech_compare`; do not substitute source diffs.
6. Complete the 37-scenario probability contract through `chaosx_ai_probability_auditor` using the current AI/effects hashes, complete candidate pools, required sweeps/sequences/simulations, and genuine same-scenario comparisons.
7. Capture final consumer evidence for native event pages, History/Event Log/Event Details, cluster/evolution text, report art, and all achievement states.
8. Rerun the independent localisation audit against `BCADE443...`, refresh the spreadsheet evidence handoff against `EC766D3E...` and `101B547A...`, and refresh `documentation_state.md`, `overview.md`, and `mcp_evidence.md` with current hashes and this achievement finding.
9. Preserve the workbook status `Needs Testing` and do not issue a completion commit until the source defect and all mandatory evidence blockers are closed.

## Final status

**Source-playable:** yes, for the core ordinary gameplay path, with a known Joint Curriculum achievement defect and unproven engine-sensitive edge cases.

**Acceptance-complete:** no.

**Completion claim:** not issued.
