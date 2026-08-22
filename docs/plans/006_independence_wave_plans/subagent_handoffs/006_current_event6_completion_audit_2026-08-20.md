# Event 006 Independence Wave current completion audit

> Historical snapshot notice (2026-08-22): This dated audit preserves its 2026-08-20 HOLD/PARTIAL evidence and remains historical. Use the 2026-08-22 authority override in `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` for current routing. Its focus receipt records 184 focuses and 196 connectors; the current receipt supersedes that connector count with 184 focuses and 195 connectors, zero crossings, and zero node intersections. Current joint-capacity evidence is 32 readiness wrappers, 32 capacity tries, and 32 caller entries matching 32 content attestations; live release and terminal receipts remain unproven.

Date: 2026-08-20

Mode: read-only completion audit

Effective source revision reviewed: `256ba7140bb65c32d104926b20e448145d0ba11c`

Overall disposition: **HOLD / PARTIAL**

## Audit boundary

This audit compares the accepted seven-part design under `docs\specs\006_independence_wave_specs\specs\` with the effective source, current authority documents, current package handoffs, current asset evidence, and the mandatory HOI4 MCP event, focus, probability, GUI, and map routes.

The accepted specifications remain the design authority.

Working plans and handoffs do not narrow an accepted requirement unless an explicit supersession or parent disposition says so.

The accepted no-pre-event supersession is current: Event 006 has no player-facing crisis category, mission, cost, queue, pressure surface, or pre-report history row.

This pass did not edit gameplay, asset, localisation, workbook, focus, decision, GUI, map, or probability source.

## Executive result

Event 006 is not complete.

The core release system is materially implemented and the six repository-specific static audits pass, but whole-event completion remains blocked by the current admission boundary of 32 content-attested selectable packages across 29 compatible reservation groups, leaving 161 of the 193 non-overlay rows unattested.

The central dispatcher contains 40 runtime adapters, eight of which remain adapter-only and fail closed: IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179.

The active automatic ladder is the accepted `3/4/5/7/10`, with World Collapse also targeting 10.

The retained 20-package standalone witness proves bounded static capacity only.

It does not prove that all accepted candidate packages, all SCN-008 cells, every formable family, or every factual world-state transaction can execute.

The narrow manual-entry defects identified by the preceding audit are already repaired in the effective source.

No additional narrow source defect was proven by this pass, so no speculative gameplay patch is recommended.

## Narrow source-defect disposition

### Repaired: unattested rows receiving the minimum allocation floor

Commit `e7992bbbb` makes the final minimum-weight clamp conditional on `has_independence_wave_runtime_package_content_attestation_for_execution_id = yes` in `common\scripted_effects\006_independence_wave_package_planner_effects.txt:689-698`.

The canonical attestation check also remains present before the weight calculation and before anchor reservation.

The effective result is that an unattested candidate cannot be revived from zero weight by the minimum floor and cannot starve admitted rows by entering the weighted pool.

### Repaired: stale standalone plan blocking a later manual entry

Commit `256ba7140` adds `independence_wave_reset_stale_standalone_plan` in `common\scripted_effects\006_independence_wave_execution_effects.txt:619-647` and calls it before `independence_wave_capture_wave_tuning` and `liberation_release_begin_plan` at lines 662-667.

The reset is narrowly limited to a plan owned by Event 006, marked as including Event 006 but not Event 005, not past either the execution-started or finalizer-started barrier, and still in collecting, allocating, or locked phase.

A locked stale plan first restores host capitals, and the abort occurs only if that restoration did not publish a failure receipt.

Joint Event 005 plus Event 006 plans and post-execution plans remain untouched.

This is a source-level manual-entry invariant repair rather than an audit-only recommendation.

### No further safe patch identified

The current root entry still relies on the large shared transaction system, but the remaining uncertainty is MCP helper/lifecycle projection, package breadth, and scenario evidence rather than a proven local predicate or scope error.

The parent should not add a synthetic completion receipt or weaken the transaction gates merely to make the manual path easier to observe.

## Completion status by surface

| Surface | Status | Evidence and remaining boundary |
| --- | --- | --- |
| Accepted design and no-pre-event supersession | **Finished as design authority** | The seven accepted spec parts remain authoritative; the August 15 supersession removes the visible pre-event crisis system. |
| Root event and standalone manual entry | **Source-repaired / evidence-partial** | `chaosx.nr6.1` reaches the standalone transaction effect; the attestation-floor and stale-plan defects are repaired. Fresh event MCP analysis is partial because helper projection and lifecycle passes were deferred. |
| Automatic allocator and synchronized transaction | **Partial** | The exact `3/4/5/7/10` ladder, anchor-to-compact-to-extended order, joint Event 005-first order, protected-host witness, rollback, and central attestation gates exist. Only 32 packages are content-attested and the static witness is not full-scope transaction proof. |
| Pre-event crisis surface | **Finished at source** | Static audit reports no category, mission, cost, or queue. Commit `97383c514` also retires the annex callback. Stale documentation still mentions preserving a crisis queue sentence. |
| Country registry and package API | **Partial** | The API audit resolves 191 unique carriers from 242 broad tags with zero missing or duplicate carriers, but central admission remains 32 of 193 selectable rows. Package-local source is not central admission evidence. |
| IW-057 Far Eastern Republic | **Package-local partial / fail-closed** | The exact FER/408-409 wrapper and anchor-owned readiness gate exist, but IW-057 is absent from central attestation, normal and SCN-008 preflight, and deterministic Join. Institutional-roster acceptance, neutral-flag provenance, and typed probability evidence remain open. |
| Decisions, missions, values, and relationship mechanics | **Partial** | Shared mechanics and bounded admitted-package consumers exist, but 161 selectable rows lack complete central packages and current event-wide probability evidence does not close all decision and mission scores. |
| Shared focus framework | **Partial / HOLD** | Fresh MCP resolves 184 focuses and 196 connectors with zero crossings and zero node intersections, but six Event 006 authored detour or long-connector warnings remain. Fourteen blocking diagnostics reported by the tool are missing icons in imported vanilla continuous-focus source and are not evidence of an Event 006 source defect. |
| Evolutions and incident chains | **Partial** | The five accepted evolution identities and incident source exist, but fresh namespace inspection cannot complete helper/lifecycle projection in the large workspace. Full accepted route and terminal coverage is therefore not proven by MCP. |
| Formable system | **Partial / fail-closed by family** | The registry, bounded commit adapters, and fourteen GUI geometry manifests exist. FORM-07 and many other families remain fail-closed; the current authority explicitly keeps FORM-06 and FORM-08 through FORM-47 closed except for specifically implemented families, and FORM-48 remains unreachable through a complete admitted HBX/HAW/FSM carrier/member set. |
| Event-owned formable puzzle GUI | **Source-present / visual-evidence partial** | Event ownership, exact identifiers, and a `chaosx_event_ui_worker` handoff exist. Fresh inspect resolves 93 elements, but the MCP result is dominated by workspace-global diagnostics and the renderer returns an aggregate SVG instead of clean family-isolated state, hierarchy, click-region, resolution, and comparison evidence. No safe GUI source defect was proven. |
| Statehood Ledger GUI | **Source-present / visual-evidence partial** | The dedicated Event 006 worker handoff exists. Fresh inspect resolves 48 elements and fresh render produces an aggregate SVG, but validation is false under workspace-global GUI diagnostics and the current response does not isolate every requested state, click region, hierarchy, resolution, or comparison. |
| Event Log and Event Details | **Partial** | Shared log/detail registrations and wording exist for the current partial feature set. They cannot be accepted as whole-event complete while package, formable, scenario, super-event, and evolution availability remains partial and stale documentation survives. |
| SCN-008 | **Source-matrix PASS / availability partial** | `.tools\audit_event6_scenario_matrix.py` passes all 32 declared cells and eight edge-case receipts. The accepted requirement that all viable candidates work at every intensity is not met while 161 rows remain unattested and weighted evidence is bounded. |
| Ordinary super-event 23, The League of New States | **Blocked** | Image and text dispatch are registered, but accepted rights-cleared audio, sound wrappers, and firing remain blocked. No fallback or substitute is authorized. |
| Ordinary super-event 24, Every Border a Casus Belli | **Source-wired / reachability partial** | Final audio, wrappers, dispatch, factual predicates, and queued playback exist. Hidden-formable reachability lacks a complete admitted FORM-48 set, and the exact-ten route still depends on live factual transaction qualification beyond the static witness. |
| Achievements | **Source-wired / reachability partial** | Sixteen definitions and their icon-state surface are recorded, including the league-expulsion writer. Whole-matrix factual reachability is not proven across the partial package and formable set. |
| Flags and non-portrait visual assets | **Partial overall** | The registered Event 006 flag families pass the static flag audit, and the Statehood Ledger animation packages are wired. The accepted event-wide asset contract remains incomplete for unimplemented or unadmitted packages and blocked formables. |
| Character portraits | **Partial overall** | Bounded grounded portraits have attributed source-placeholder and portrait-worker evidence, while some retained candidates remain `needs_user_review`. The accepted package set is far broader than the completed portrait consumers; no event-wide portrait completion claim is supported. |
| Custom 3D units and unit sound/counters | **Not in accepted Event 006 scope** | No accepted Event 006 package requires a custom 3D model, bespoke unit-audio package, or bespoke counter package, so this is not a completion blocker. |
| Localisation | **Partial** | Current bounded package and shared-surface localisation exists, but no fresh whole-event localisation completion audit closes all accepted packages, formables, incidents, super-events, achievements, and UI states. |
| Catalog workbook | **Aligned to partial availability** | The current catalog correctly reports Event 006 and Liberations as partially available and SCN-008 as unavailable or incomplete. The workbook should not be promoted to complete until the source blockers close. |
| Documentation and plan authority | **Partial / stale items remain** | Current counts are consistent, but multiple older accepted plans retain stale proposed or zero-weight wording and the source-of-truth map still instructs preservation of a retired crisis queue sentence. |
| AI and weighted probability | **Partial / separately audited** | Weighted surfaces were routed to `chaosx_ai_probability_auditor`. Its exact result is recorded in the probability section below; source-only inspection is not treated as equivalent typed probability evidence. |

## Accepted-plan disposition

| Plan or requirement family | Disposition |
| --- | --- |
| Core allocator, synchronized transaction, exact ladder, protected-host handling, and no-overlap rules | **Implemented in bounded source; whole-event acceptance remains partial.** |
| Dormant shell and partial-wave execution repairs | **Implemented and promoted.** The older `exists = no` audit wording is superseded by dormant-country scope semantics. |
| Joint Event 005 plus Event 006 expected-count repair | **Implemented and promoted.** Older handoffs that call the overwrite unresolved are stale for that defect, while full joint execution remains only partially evidenced. |
| Pre-event crisis supersession and removal | **Implemented and promoted.** Any retained crisis-queue plan wording is historical residue, not a queued gameplay request. |
| IW-038 Ruthenia plan | **Implemented/admitted; plan status stale.** Its old zero-weight sentence must not control current routing. |
| IW-014 Catalonia admission addendum | **Implemented/admitted; FORM-07 remains separately fail-closed.** Its old “proposed” status is stale. |
| IW-047, IW-048, IW-050, IW-051, IW-052, IW-053, IW-054, IW-057, and IW-060 bounded package plans | **Package-local or research work implemented in varying depth; central promotion not accepted.** Preserve their exact identity, map, source, asset, roster, and probability blockers. |
| IW-043, IW-058, IW-093, and IW-098 adapters | **Source adapters present; central admission blocked.** Do not infer package completion from an adapter, portrait, tag, or formable consumer. |
| Shared focus plan | **Partially implemented and still on HOLD.** The broad shared framework exists, but package breadth and clean focus acceptance remain open. |
| Formable-family plans | **Bounded subset implemented; remaining accepted family breadth queued or blocked.** FORM-48 design is source-present but not fully reachable, and FORM-07 remains fail-closed. |
| SCN-008 matrix plan | **Source matrix implemented; full accepted viability not achieved.** All 32 declared cells exist, but full candidate admission and weighted scenario evidence remain incomplete. |
| Super-event 23 | **Blocked on exact audio rights and parent approval.** No fallback may be substituted. |
| Super-event 24 | **Source-wired; factual reachability partial.** |
| Sixteen-achievement plan | **Source-wired; factual reachability partial.** |
| Event-wide asset and portrait completion | **Incomplete.** Per-package evidence cannot be promoted into event-wide coverage. |

## Mandatory MCP evidence

### Events

Fresh namespace lint for `chaosx.nr6` returned `EVENT_INSPECTED_PARTIAL` at revision `98ac244e0b194a88389dbe53658d4876e5d76d2c5eb52b52ff572abea77b4fe3`.

The report scanned 9,500 workspace events, selected the Event 006 namespace, reported zero blocking event diagnostics, and explicitly deferred workspace-wide helper projections and lifecycle passes because of the large workspace.

The durable lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bcab04d728c804dc38ed407fbf1d4ad2a90db307e90386930fcf73060a6aa71e/fcb15b9e40cf1548397183391caa38da65c4aeee002f858ed332b3d1709221c5/event-lint-98ac244e0b19.json`.

Fresh namespace overview render returned `EVENT_RENDERED_PARTIAL`, selected the maximum 240 nodes, and omitted 40,910 nodes from the bounded inline view.

The manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6bf4a46c545211eed16e4571ef35c52fb8ec4273704ff63aed200d9d74e4ad8c/b3df3cf88fe0352254ea0fdd794680c51d9040b361290ac670d9d0829cb142ad/event-overview-98ac244e0b19-manifest.json`.

The SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/141cd994cbb1d8d49f3c5f420aab7f420d5d487b68c40597df2a15068c63d101/d3a937242a39f1114aa2ce4c58e6114063fd2a453dfd1688a9c51b78c00c9a75/event-overview-98ac244e0b19.svg`.

The root-specific lint, trace, and state render reached the same partial-analysis boundary and reported zero selected blocking diagnostics.

`hoi4.event_compare` was attempted against the previous recorded event revision and failed with `EVENT_REVISION_NOT_CACHED`.

The MCP compare route does not accept Git commit identifiers as an equivalent baseline, so source diffs for `e7992bbbb` and `256ba7140` are not presented as event-graph comparison evidence.

### Focus

Fresh inspection of `common\national_focus\006_independence_wave_focus.txt` and tree `independence_wave_focus_tree` returned 184 focuses, 196 connectors, zero crossings, zero node intersections, and two long connectors at revision `32d76f0bd352703571884f1c3966b7d13125545235375be3d208ac2b195f7a5c`.

Six Event 006 authored detour or long-connector warnings remain.

The tool's fourteen blocking diagnostics come from missing icons in imported vanilla `game:common/continuous_focus/generic.txt`; they are not a proved Event 006 source defect and do not justify a rewrite.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5b39e7b9a120bd964c0e0711c416004bf2a80a11491157591bd50f8611617b7/5841878221a4deac6921fb3ca661240e55143bbd9d128057e95c15bb5db0516e/focus-inspect.32d76f0bd3527035.json`.

The render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84838e459573ed2a968b3371200cd049388c6122a30bc5fb0e59175777ca139e/76ca9eb4a76f62736d04edef6efc2374c39a62241c8267b6df0ad2ca7167780c/independence_wave_focus_tree.focus.html`.

### Map

Fresh map inspection covered the 43 unique state IDs used by the fourteen Event 006 formable GUI manifests.

Definitions, states, regions, and network checks passed at revision `7c0b0196de715c918162a52ffa6c8d80a900215b3ba48c96061e5986417251ff`.

The global positions and locators collections failed under thousands of workspace-wide building and floating-harbor diagnostics, and the fixed diagnostic ceiling prevents treating the result as clean family-isolated placement proof.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8340c0863502c5939f4ed14e51e33a9710bb1e63286db2d12fc9cbd1c15ad2f0/0da33b852f1909de44b9006248f7c3233607656546014682c3c3c2d113cab348/map-inspect.7c0b0196de715c91.json`.

The bounded state-layer render with coastlines, ports, victory points, state buildings, supply nodes, railways, and adjacencies passed and is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/455cc8c5e85bf213caf4b9edc37bcaccbd7bed96a443f754722cfc7909580cb8/e7c2fcd9d3f7177e835c49a09d4741c39cff5e5312995e0ff8ace3295dde3b0c/map-state.png`.

This proves that the selected state geometries and network records exist.

It does not prove formable eligibility, state ownership, or runtime attachment.

### Scripted GUIs

Fresh inspection of `independence_wave_status_window` under scenario `independence_wave_status_default` resolved 48 elements.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ee61a93b5165ec4064fd6204186d2ae545a3fbed73ec38c241425434a54b076/5f36366417f7f2132081878c113f81986db8b6fef0d383cae70cd8ae1e5389d9/gui-inspect.9868081b82d9c2db.json`.

Its aggregate render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b41ddb01cf9908e8e7596331a39e292b019c0af251c2908f9be7a245d702d211/3b63c4f53f23c7be63163cd94ed0330e90fcfce90fb7c5a135463c9bc541863e/independence_wave_status_window-full.svg`.

Fresh inspection of `chaosx_independence_wave_formable_state_puzzle_window` under scenario `event006_formable_activated_normal` resolved 93 elements.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6cc77108dc9ceda1f2d91f3e54f835f3dede1bac0ae8a74b635fb81376e14825/3aeb40fba628edb8342c5b297e0f856475444ab8db8f6f66125492bc66219cfc/gui-inspect.09be51e499799bbd.json`.

Its aggregate render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e97c70599faf55199598d778b73ce41c67572b64ff8845a17ea5d05b8e4eabab/735a81e8b330fe2aebf1067e21a3425bfe5dfb2fae2e2aac0f2066d3651c7d24/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

Both GUI inspections are complete source scans, but their validation is false because the fixed 2,000-diagnostic global graph ceiling contains unrelated repository collisions and unresolved references.

The render responses contain only aggregate SVG evidence and do not expose clean per-state or per-family comparison artifacts for every requested resolution and interaction state.

No `hoi4.gui_rewrite` was used because this is a read-only audit and neither route isolated a concrete Event 006 layout defect.

The existing `chaosx_event_ui_worker` handoffs satisfy the required ownership and routing record, but the fresh MCP limitation prevents a new visual-completion claim.

### Probability

The Event 006 weighted surface was routed to `chaosx_ai_probability_auditor` as required.

The auditor returned **PARTIAL / UNRESOLVED** at probability source revision `f7640688dafc72fbf8ba0db3454b1a6d190185571a981e745e80b30d6bf1582e`.

The core event option surface exposed 20 candidates, an incomplete pool, 13 required inputs, and one unresolved input.

Its inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5fd2e9eaed9d49d9e7242ec17910f04837d2ee9bdd2704ea22b5e2a99729e31c/b7fcda3f4555bd578629f53c7267733055db7922bd9c7cd8041b644b83a87224/probability-inspect-7d6b13bcd04ec.json`.

Scenario `E6_CORE_EMPTY_CURRENT_2026_08_20` returned `PROBABILITY_ANALYZED_PARTIAL` with 23 unresolved values, so normalized event-option probabilities were withheld.

Its analysis artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed20352a5de697f49a1ffca100b396c9bc884eeb0feb8bcdc30b909910bc853c/d82c7f5c0d5849e7d2344aa2ff37b36b47b306ad587e579f893c1a7f106e6854/probability-193b21719557fc415b346110.json`.

The allocator `random_list` adapter exposed a complete declared 14-candidate pool.

Its inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/234755596b0875f5e729ad0b689459a1a3447ec043a6155313d2ea17167220de/21cc9a4ad74ae9181dcf9c0b719b23cecae74e0695d78a33e09e8d8340157f2f/probability-inspect-9cab0bffea71.json`.

The named allocator scenario set `E6_ALLOCATOR_REQUIRED_SCENARIOS_CURRENT_2026_08_20`, covering R03 MAC open, all R04 open, R04 KAR blocked, R04 CRI blocked, and the retained capacity-20 witness, returned `PROBABILITY_ANALYZED_PARTIAL` with 70 rows and 14 unresolved values.

Its analysis artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef028c989c81e00c7c7f21cb1cbc7ed7c1ed7a351fd12d1bbe00205996cd6a6a/888a952ab94a4c74740974e20a6b72e6c4847737861e6f9fba945152eba2cab0/probability-2e15c0035c470074c923e2c1.json`.

The same source inspected as `custom_weighted_pool` returned no candidates, while `direct_random` discovered `random_list` as the supported adapter.

This prevents a custom sequence or state-transition claim.

The allocator sweep was blocked with `PROBABILITY_SWEEP_RANGE_REQUIRED` because every swept path requires explicit numeric ranges or alternatives.

Shared decisions exposed 10 candidates, an incomplete pool, and 88 required inputs.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b524fa24c203d75d91c8a601a447ccdd5a89ee80fc2cf4653f3a12cce2ed6d0/2dc8cbb5c7acd9fbc81637176f60953b7702f97cc7e3d7d699e1f629f46b675d/probability-inspect-35b229abc47d.json`.

The shared-decision scenario set returned a partial score race with 40 rows and 2,889 unresolved values.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/272457603206cd1c7710cf522f498b27403ab7e360f56f1093a9d4d290e51d6e/e719d3ed18c8dd9cb1d0cdd8e4bd9880350ed43d0115c8e7b27f07442abbd856/probability-54405428466cb7c083429774.json`.

Shared missions exposed 54 candidates, an incomplete pool, and 50 required inputs.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/60fca91bde6293214dbfd454b9086cbe8875d8f5746d55fcbf97d45411986feb/45dbbb3575fbbc2e67c7f29def7f0a3d52fe92569c55083936648833730316b1/probability-inspect-35b229abc47d.json`.

The shared-mission scenario set returned a partial score race with 216 rows and 548 unresolved values.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/438b571f77f92803df2e6c7442415eacd60ba8b4ae1ef55479f4775151cf269c/ca9021948ef35d153c90f04903cd3c06ac9650d3f455a26aa62499bf4a4c356a/probability-f54c87a3d193d001d2885c48.json`.

The main focus source exposed 184 candidates, an incomplete pool, and 15 required inputs.

Its inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c3cd4e52584e628534b6023ab965d73d8e6cb0a109304a2c5f05d858232da08/24dab9a94bbca2ea019155617e441187be75f0c4a20289aea3b143b42e66d0ad/probability-inspect-e4da929678f3.json`.

The generic Event 006 AI strategy source and the Event 006 evolution MTTH source both returned `no_weighted_surfaces`, so neither supports a numeric strategy or MTTH conclusion through the selected adapters.

Other Event 006 event files were inspected and consistently returned incomplete pools or unresolved eligibility, including the evolution incidents, FORM-01/02/04, FORM-05, IW-043/IW-058, IW-093/IW-098, Mediterranean, Rhineland/Bavaria, and Wallonia/Frisia chains.

The tool reported unsatisfied modifiers and never-eligible choices inside decision and mission pools.

Those rows require source review under exact route states before any dominance or starvation claim is valid.

`probability_sequence` was not completed because the custom cadence and state-transition manifest is unavailable.

`probability_simulate` was not completed because no declared uncertainty distributions exist.

Most importantly, `probability_compare` was not completed because the auditor had no approved cached MCP baseline or proposed revision for the weighted patch.

Commit `e7992bbbb` changes a weighted allocator surface, so the missing same-scenario comparison remains a mandatory acceptance blocker even though the deterministic source audit passes.

Source-only checks and the deterministic allocator witness are not substitutes for typed probability scenarios.

## Task-specific static validation

The following repository audits were run against the effective source with Python bytecode generation disabled.

| Check | Result | Material evidence |
| --- | --- | --- |
| `.tools\audit_event6_allocator.py` | PASS | 149 publishers; 126 automatic/high-chaos rows; 138 SCN-008 ranked rows; 40 adapters; 32 attestations; 29 compatible groups; 161 unattested rows; 20-package witness; exact `3/4/5/7/10` ladder; no pre-event crisis surface. |
| `.tools\audit_event6_country_api.py` | PASS | 242 broad unique tags; 191 resolved unique carriers; 34 Soviet rows; 45 African rows; zero missing and zero duplicate carriers. |
| `.tools\audit_event6_scenario_matrix.py` | PASS | All 32 declared SCN-008 cells and all eight edge-case receipts exist. |
| `.tools\audit_event6_flags.py` | PASS | 102 registered Event 006 tags; 102 complete flag families; zero incomplete families. |
| `.tools\audit_event6_form16.py` | PASS | ARM/GEO/AZR exact three-state, consent/refusal, mutation, rollback, cleanup, and fail-closed readiness contract. |
| `.tools\audit_event6_gui_matrix.py` | PASS | Five Ledger tabs, 16 semantic status frames, four cleanup variables plus animation flag, and four static/animated sibling pairs. Runtime rendering and save/load evidence are explicitly not claimed. |

These checks materially validate registry arithmetic and bounded source contracts.

They do not replace event, GUI, focus, map, or probability MCP evidence and do not convert partial accepted scope into completion.

## Missing, simplified, blocked, or stale requirements

### Missing or blocked implementation breadth

1. The accepted candidate catalog contains 193 non-overlay selectable rows, but only 32 are content-attested.

2. Eight adapter-only rows remain fail-closed, and numerous package-local or research-only rows are not in central attestation, preflight, deterministic Join, or reservation.

3. The accepted formable design is broader than the implemented and reachable runtime subset.

4. The accepted all-candidate SCN-008 viability requirement is not met by a source matrix that can draw only from the admitted subset.

5. Ordinary super-event 23 remains blocked by exact recording rights, final audio production, wrappers, and firing.

6. Ordinary super-event 24 and the sixteen achievements remain only partly reachable because their factual predicates depend on incomplete package and formable breadth.

7. Event-wide AI and balance acceptance remains bounded by typed MCP surface gaps and unimplemented packages.

8. Event-wide character portrait and visual evidence remains incomplete; a package-local source candidate, placeholder, flag family, or DDS does not itself prove central package acceptance.

### Simplifications

The shared focus framework is a documented breadth simplification compared with bespoke country identity for every accepted package.

It is tolerated for current admitted packages where explicitly accepted, but it does not satisfy the complete accepted package catalog.

The 20-package static witness is a bounded capacity substitute for full dynamic campaign-state evidence.

It must remain labelled as static capacity evidence and not as proof that every ladder, SCN-008 cell, or factual super-event predicate can complete.

No new simplification was introduced by this audit.

### Stale documentation and plan status

1. `docs\plans\006_independence_wave_plans\006_source_of_truth_map.md:167` instructs the parent to preserve a “crisis queue sentence,” contradicting the accepted no-pre-event supersession.

2. `docs\plans\006_independence_wave_plans\006_core_dynamic_system_improvement_addendum_v67_2026_08_01.md:21` retains crisis-queue wording as historical residue.

3. `docs\plans\006_independence_wave_plans\006_iw038_ruthenia_implementation_plan_current_2026_08_10.md:143` describes IW-038 as zero-weight even though IW-038 is in the current 32-package attestation set.

4. `docs\plans\006_independence_wave_plans\006_iw014_cat_standalone_admission_and_form07_late_binding_addendum_2026_08_05.md:5` still says “proposed” and retains historical arithmetic even though IW-014 is admitted; FORM-07 remains separately fail-closed.

5. `docs\plans\006_independence_wave_plans\006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md:3` still presents all IW-057 work as proposed, while the package-local source tranche exists and only central identity, roster, flag, probability, and route-leadership gates remain.

6. `docs\plans\006_independence_wave_plans\006_source_of_truth_map.md:172` omits IW-055 and IW-057 from a parent follow-up list even though the top authority block names both as current package-boundary work.

7. `docs\plans\006_independence_wave_plans\006_source_of_truth_map.md:99` and `docs\plans\006_independence_wave_plans\006_independence_wave_resume_packet.md:89` still say `chaosx.nr6.350` recruits NAV and GLC commanders.

8. Current `events\006_independence_wave.txt:143-281` uses `.350` as a roster and portrait checkpoint for bounded packages and contains no NAV or GLC recruitment block; the NAV and GLC character definitions are fixed-tag source under `common\characters\006_independence_wave_iberian_commanders.txt`.

9. Older August 15 audit statements that require `exists = no` for dormant carriers are superseded by the current dormant-country-scope implementation.

10. Older handoffs that call the joint Event 005 plus Event 006 expected-count overwrite unresolved are superseded by the implemented recomputation, though full joint runtime evidence remains partial.

## Remaining blockers in priority order

1. Close or explicitly reject the remaining 161 selectable package rows under their exact identity, map, roster, source, asset, gameplay, cleanup, and probability contracts.

2. Complete typed weighted-surface evidence for the admitted packages and custom allocator scenarios without changing balance targets merely to satisfy the tool.

3. Finish the accepted formable breadth and promote only families with complete carrier, member, territory, symbol, integration, cleanup, GUI, and probability evidence.

4. Obtain explicit rights clearance and parent approval for ordinary super-event 23 audio, then perform parent-owned conversion, wrapper, dispatch, and firing work.

5. Re-run family-isolated GUI inspect, render, state, hierarchy, click-region, resolution, and comparison evidence when the MCP route can return those artifacts without global-diagnostic truncation.

6. Resolve the six Event 006 focus layout warnings or formally accept their authored geometry; do not patch around unrelated vanilla continuous-focus icon diagnostics.

7. Reconcile the stale authority and plan-disposition statements listed above through a documentation-only pass.

8. Run a fresh event-wide localisation audit and update the workbook only after implementation facts change.

## Recommended next action

Do not add another manual-entry patch.

The next implementation tranche should be a bounded accepted-package promotion or typed probability-evidence closure for an already admitted package, with its exact country, decision, focus, asset, localisation, cleanup, and probability owners named before source changes begin.

The parent should separately queue a documentation-only authority cleanup for the stale crisis, IW-038, IW-014, IW-057, parent-list, NAV/GLC `.350`, dormant-shell, and joint-count claims.

## Files changed by this audit

Only `docs\plans\006_independence_wave_plans\subagent_handoffs\006_current_event6_completion_audit_2026-08-20.md` was created.

No gameplay, asset, localisation, workbook, GUI, map, focus, decision, event, or probability source was edited.

Nothing was staged or committed.
