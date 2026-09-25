# Event 021 / Event 006 package-boundary audit

Status: **INCOMPLETE; bounded source audit only.** This handoff records current-source findings for the Event 021 adapter boundary. It is not a full country-package certification. No runtime, country, art, asset-wiring, or workbook files were edited.

## Scope checked

- Read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and the applicable event, focus-tree, decisions/missions, and event-assets skills, plus the required offline Paradox Wiki pages and relevant installed-game documentation.
- Re-read the Event 021 live host/package selector, Event 006 adapter registry and package dispatch gate, the Event 021 package setup proof, its adapter preparation/rollback/finalization paths, the Event 006 adapter-only setup entry point, the shared Event 006 focus-tree identity, and the external-war fallback sources named below.
- Source checks were limited to the selector/adapter boundary and shared package contract. I did not individually audit every admitted country package's complete identity, art, gameplay, and lifecycle surfaces.

## Verified findings

### Dynamic live eligibility versus authored package identity

- `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:9-25,46-63` predicates over existing countries with live state/control and lifecycle conditions. `random_civil_war_is_normal_human_country` in `common/scripted_triggers/021_random_civil_war_triggers.txt:37-40` means `exists = yes` and not `is_actual_nonhuman_country`; it does not mean player-controlled-only, so ordinary AI countries can qualify.
- The shared immunity classifier is `is_actual_nonhuman_country` in `common/scripted_triggers/chaosx_dynamic_triggers.txt:45-68`. The Event 021 normal-country predicate calls it, and inspected host/live-country selectors reuse that predicate. This verifies immunity only on those selector paths; it does not certify every actor, event, decision, or package consumer.
- `event021_parent_find_event6_package` in `common/scripted_effects/021_random_civil_war_parent_effects.txt:154-277` scans the current `global.independence_wave_event021_complete_package_ids` array from a rotating cursor, loads each authored package, and tests the current host's eligible anchor and the carrier's runtime preflight. It does not select from a fixed list of currently eligible live countries.
- Event 006's static authored package inventory in `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:12-50` has 32 package IDs: `IW-001/SCO`, `002/WLS`, `004/BRI`, `006/AFX`, `007/AGX`, `008/RHI`, `009/BAY`, `010/AJX`, `012/ICE`, `014/CAT`, `017/COR`, `018/ARX`, `019/ASX`, `023/TRA`, `024/AXX`, `026/MAC`, `027/BAX`, `028/BBX`, `029/BOS`, `030/MNT`, `031/KOS`, `033/KAR`, `038/RUT`, `040/KUB`, `041/CRI`, `044/TAT`, `045/BSK`, `070/ARM`, `071/GEO`, `072/AZR`, `173/HAW`, and `184/HBX`.
- The tag/carrier and anchor maps in `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:56-129` and `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt:8-43` are static authored identity crosswalks. That is valid package content data, not evidence of a fixed live-country candidate roster or a predetermined crisis-wide territory split. For the Transcaucasus rows specifically, the anchors are `IW-070/ARM/state 230`, `IW-071/GEO/state 231`, and `IW-072/AZR/state 229`; the selector checks current ownership/control, population/infrastructure, and dormancy.
- `scheduler_registration_samples = 4` in `common/script_constants/021_random_civil_war_constants.txt:684` limits one scheduler batch, not the eligible live-country roster. The inspected scheduler uses `random_country` with the normal-country predicate (`common/scripted_effects/021_random_civil_war_parent_effects.txt:438-457`). This is bounded work scheduling, not proof that all eligible countries are registered in one pulse.

### Adapter completeness blocker

- `event021_parent_event6_package_setup_proven` in `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:69-133` dynamically calls `has_prepared_independence_wave_iw_[ID]_package_setup` after shared setup.
- A current-source search of all `common/scripted_triggers/*.txt` found the expected `has_prepared_independence_wave_iw_###_package_setup` predicate for 29 of the 32 registered IDs, but none for `IW-070`, `IW-071`, or `IW-072`. `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt:57-77` defines `is_independence_wave_exact_package_iw_070/071/072_runtime_ready`, not the prepared-trigger names the Event 021 proof requests. This is a dangling adapter proof reference for all three entries; engine behavior and the practical effect on admission remain unvalidated. The current source also lists these IDs in the Event 006 runtime adapter table (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`), so their presence in the static inventory does not establish Event 021 adapter completeness.
- For the other 29 entries, this check establishes only that a matching prepared-trigger name exists. It does not prove each predicate's correctness or the full package's completeness.

### Dynamicity constraint violation in Event 021 capacity

- Eligible hosts, candidate country state, anchors, and selected territorial states are evaluated dynamically in the inspected selectors and reservation/expansion code. However, current Event 021 source has fixed numeric ceilings: `maximum_multifront_states = 5` (`common/script_constants/021_random_civil_war_constants.txt:325-326`), `maximum_major_belligerents = 5` and `maximum_minor_belligerents = 3` (lines 636-638). The derived belligerent cap is clamped to those constants in `common/scripted_effects/021_random_civil_war_parent_effects.txt:2525-2545`, and state expansion and scenario freezing are explicitly capped at five in the same file around lines 1350-1370 and 6170-6190.
- Specific paths also assign fixed counts: the Event 006 opening sets host-plus-actor total/cap to two (`parent_effects.txt:4495-4496`), while the same-tag route sets both to one (`parent_effects.txt:4614-4615`). These are static participant ceilings/assignments, not merely static identity crosswalk data. They conflict with the stated requirement of no fixed participant count or fixed territorial-allocation limit. The actual selected country/state identities remain live-tested; the size is not uncapped.
- No static authored live-country tag roster or static external-war target list was found in the selector paths reviewed. This finding is limited to those inspected files and paths, not a repository-wide proof.

### Immunity, setup isolation, and cleanup evidence

- The Event 021 adapter path calls `event021_prepare_event6_admission`, `independence_wave_prepare_event021_adapter_origin`, and the shared Event 006 package dispatcher, then requires `event021_parent_event6_package_complete` before accepting the carrier (`common/scripted_effects/021_random_civil_war_parent_effects.txt:3915-4016`). The shared adapter entry `independence_wave_prepare_event021_adapter_origin` in `common/scripted_effects/006_independence_wave_effects.txt:858-868` is gated by Event 021 adapter flags and routes through reversible setup rather than the normal Event 006 origin activation entry.
- The Event 021 package proof explicitly rejects `independence_wave_active_origin`, `independence_wave_network_member`, and `independence_wave_league_member` (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:92-99`). The inspected adapter entry does not call Event 006 origin activation/commit. This supports the narrow conclusion that this adapter setup path does not intentionally enroll the actor in Event 006 history/network/league activation; it is not a full audit of every Event 006 evolution or league path.
- Failure cleanup is present in `event021_parent_cleanup_failed_event6_adapter_actor`, `event021_parent_abort_event6_opening`, `event021_parent_abort_event6_secondary_front`, and `event021_parent_clear_event6_package_transaction` (`common/scripted_effects/021_random_civil_war_parent_effects.txt:4023-4230`). The inspected rollback resets the current Event 006 generation, restores a saved prior Event 021 generation when available, returns the anchor, restores the prior capital, and annexes only a newly released actor; a pre-existing carrier is preserved. Finalization in `event021_parent_finalize_event6_actor` and `event021_parent_finalize_event6_secondary_actor` closes the temporary Event 021 front/cleanup state while preserving package identity. This is source-level evidence for these paths only; startup and all terminal/runtime paths were not audited.

### External-war fallback

- The current external-war implementation is in `common/scripted_triggers/021_random_civil_war_external_war_triggers.txt`, `common/scripted_effects/021_random_civil_war_external_war_effects.txt`, and `events/021_random_civil_war_external_war_events.txt` (`chaosx.nr21_external.1/.2`). It snapshots current predecessor enemy relations dynamically, prompts only when the successor's current relation is absent, and exposes generic core/claim declarations only as human choices after validating a presently held core/claim. The post-adoption trigger rejects AI. This matches the approved relation-continuity fallback at source level; no AI auto-declaration or fixed target array was seen in these files.

## Coverage checklist and exact limit

- [x] Event 021 host and Event 006 package selector distinction; 32 authored package IDs and tag/anchor crosswalk counted.
- [x] `is_actual_nonhuman_country` immunity checked in the shared normal-country predicate and inspected live selector paths.
- [x] Event 021 adapter admission contract, Event 006 adapter-only setup entry, and selected rollback/finalization paths reviewed at source level.
- [x] External-war relation snapshot and human-only generic core/claim fallback reviewed at source level.
- [x] Fixed capacity constants and explicit participant assignments identified.
- [ ] Full country-by-country package audit is not complete: leader/character identity and gender, portraits/provenance, flags/cosmetic tags, country definitions/localisation, politics, starting ideas, forces/reinforcement, formables, decisions, AI, and all startup/runtime cleanup were not individually verified for the 32 packages. The shared setup proof's existence is not a substitute.
- [ ] State/map MCP inspect/render evidence was not obtained; map/anchor conclusions above are source-only.
- [ ] Event MCP inspect/render evidence for `chaosx.nr21.1`, `chaosx.nr6.1`, and the external-war events was not obtained. Live schemas were exposed, but bounded route calls did not return an artifact/result before they were stopped. Connected server version/health was not independently confirmed; the locally installed npm package reported `hoi4-agent-tools@3.0.7`.
- [ ] Focus MCP inspect/render for `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt` was not obtained. Source contains that tree and the Transcaucasus setup predicate checks for it, but this is not a rendered/route audit.
- [ ] No technology-tree inspect/render evidence was obtained. Standalone Technology Tree Viewer availability was checked separately and remains absent: project MCP documentation lists no viewer and local command discovery found no standalone viewer executable; exposed technology inspect/render/compare routes are not a standalone viewer. Technology dependencies were not audited package-by-package.
- [ ] Required read-only `chaosx_ai_probability_auditor` scenario pass was requested and had not returned by this handoff's cutoff. No probability/AI balance claim is made.
- [ ] Vanilla country-package file precedents, live game behavior, and user playtest evidence were not completed.

The MCP gaps above are unresolved validation, not evidence that the source is valid or invalid at runtime. No MCP artifact references are available from this attempt.

## Remaining blockers / next bounded steps

1. Resolve the `IW-070/071/072` prepared-trigger name mismatch and then verify all 32 adapter predicates against their actual package setup contracts; do not infer engine behavior from the missing name alone.
2. Decide whether the existing fixed caps (`maximum_multifront_states`, major/minor belligerent ceilings, and explicit one/two assignments) are compatible with Event 021's current no-fixed-count/no-fixed-territorial-limit requirement. As written, they are direct source-level conflicts.
3. Complete the event, focus, map, and probability MCP workflows after confirming connected service health/version; retain returned revisions, diagnostics, scenario names, and artifact references.
4. Continue the full 32-package identity/asset/gameplay/AI/startup cleanup matrix only if that broader audit is still required; it is outside the coverage achieved here.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-event-assets`. No skills were created or updated.
