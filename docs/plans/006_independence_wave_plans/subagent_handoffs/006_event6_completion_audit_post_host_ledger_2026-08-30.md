# Event 006 completion audit after the standalone host-ledger repair — 2026-08-30

## Disposition

Event 006 remains **HOLD / PARTIAL**.

This bounded read-only audit does not claim completion and does not authorize a new gameplay, localisation, asset, GUI, focus, country, formable, or balance patch.

The highest-impact source-backed runtime defect found by the current audit sequence was the standalone host-ledger mismatch recorded in `006_event6_standalone_host_ledger_fix_2026-08-30.md` and repaired by commit `70231664a`.

The current source uses the populated shared liberation host ledger, and commit `d727d6a2b` added the missing focused regression guard after this audit reported the gap.

The only safe source action identified by this audit was a narrow regression assertion in `.tools/audit_event6_allocator.py`; the parent implemented it without changing gameplay, and the strengthened allocator audit passes.

The other safe action is documentation reconciliation through `chaosx_documentation_curator`, because the files that present themselves as current authority are stale after several accepted 2026-08-30 fixes.

No gameplay, localisation, asset, test, spec, spreadsheet, or runtime file was edited by this auditor.

## Authority and method

The audit read `AGENTS.md`, the complete `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and `chaos-redux-event-assets` skills, and the accepted Event 006 specs, matrices, diagrams, research packets, prompts, plans, validators, current source, and dated subagent handoffs.

The applicable offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, countries, maps, interfaces, and scripted GUI.

The corresponding installed vanilla documentation was consulted for effects, triggers, modifiers, script concepts, script constants, dynamic variables, event targets, country iteration, and weighted selection.

The source review treated the specs as design authority, current script and asset files as implementation authority, and dated handoffs as evidence rather than executable truth.

The audit did not use source-only review as a substitute for unavailable engine evidence.

## Requirement-to-evidence map

| Surface | Accepted requirement | Current evidence | Status |
| --- | --- | --- | --- |
| Entry and public boundary | The repeatable incident begins at `chaosx.nr6.1`, creates no public Event 006 surface before a committed plan, and publishes the public report only after commit. | `events/006_independence_wave.txt:11-68` keeps `.1` hidden and triggered-only, unlocks the runtime only on committed joint or standalone delivery, and dispatches `.2` only on those committed paths. The retired callback at `events/006_independence_wave.txt:107-128` is cleanup-only. | Source-complete; Event MCP proof partial; live proof unavailable. |
| Release ladder and planner | The exact ladder remains `3/4/5/7/10`, allocation is anchor-first, and no origin may lose unrelated content. | The focused allocator audit reports 149 publishers, 126 automatic/high-chaos packages, 138 SCN-ranked packages, 40 adapters, 32 attestations, 29 reservation groups, and the exact ladder/order. Current admission remains 32 content-attested packages and 161 unattested rows out of 193 non-overlay rows. | Partial by explicit admission boundary. |
| Standalone execution host ledger | Execution validation and achievement initialization must read the host ledger populated by the shared coordinator. | `common/scripted_effects/chaosx_liberation_release_effects.txt:416-420` populates `global.liberation_plan_hosts` and aligned host arrays. `common/scripted_effects/006_independence_wave_execution_effects.txt:342` validates the former host against that shared array. `common/scripted_effects/006_independence_wave_achievement_effects.txt:463-465` iterates the same array. Commit `70231664a` repaired the former stale `global.independence_wave_plan_hosts` consumers, and `d727d6a2b` protects both consumers in the focused validator. | Source/static repaired; no live execution receipt. |
| SCN-008 publication | Failed or invalid scenario generations must not publish a visible Event 006 result, while committed generations publish the public report before the frozen result. | `events/006_independence_wave.txt:534-578` keeps the launch barrier hidden and failure paths non-public. `events/006_independence_wave.txt:582-610` requires committed and non-failed state for `.80`. The accepted P0 commits are `3ce4b3468` and `713306f2e`; the 32-cell and eight-edge-case validators pass. | Source/static complete; engine comparison and live execution remain unavailable. |
| No pre-event decision surface | No Event 006 category, mission, cost, queue, or history surface may appear before the public incident. | The 13 overlays retain the post-commit runtime gate. IW-043/IW-058 and IW-093/IW-098 use setup receipts at `common/decisions/categories/006_independence_wave_categories.txt:304-320` and `:339-353`. The SCO adapter reuse is isolated by the active-origin and setup receipts at `:649-658`. | Source/static complete for audited categories; live UI reachability unavailable. |
| Package completeness | A package without complete identity, territory, country, asset, AI, integration, and cleanup evidence must be skipped rather than represented by a generic substitute. | The allocator reports 32 content-attested packages, 29 reservation groups, 40 adapters, and 161 unattested rows. The eight adapter-only rows IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179 remain fail-closed where central attestation is absent. | Partial by accepted fail-closed design. |
| Formables and League | The registry contains 48 family rows, uses the shared state-puzzle transaction, and keeps unadmitted families unavailable. | `006_event6_formable_league_completion_2026-08-30.md:11` records 14 reviewed identity/integration family adapters and 34 fail-closed families. Its source crosswalk at `:153` confirms all 48 registry rows and family constants. | Partial: 14/48 families admitted. |
| Event-owned scripted GUI | Dedicated Event 006 GUI work requires event ownership, the decision layout contract, and mandatory MCP visual evidence. | The statehood-ledger and formable-state-puzzle windows have named `chaosx_event_ui_worker` handoffs. The current formable handoff records a complete 93-element GUI inspection with no missing/unsupported elements or visible overlap at `006_event6_formable_league_completion_2026-08-30.md:155`; the read-only clean result did not warrant a rewrite or comparison at `:169`. | Source/MCP-inspect evidence present; family-isolated and live consumer proof remains partial. |
| Evolutions and re-entry | All five canonical stages must be independently selectable, idempotent for active actors, and generation-safe. | `006_event6_formable_league_completion_2026-08-30.md:77-87` records the five stages, one-stage-per-due-invocation behavior, idempotent aligned-array delivery, pending log preservation, and generation cleanup. | Source/static complete; MTTH probability evidence required below; live re-entry unavailable. |
| Achievements | All 16 matrix rows require definitions, proof triggers, text, icons, lifecycle callbacks, and host-remnant accounting. | `006_event6_formable_league_completion_2026-08-30.md:89-95` records 16 definitions, 16 final proof triggers, matching localisation, complete/grey/not-eligible triplets, and the narrow callbacks. Host-remnant initialization now uses the shared ledger at `common/scripted_effects/006_independence_wave_achievement_effects.txt:463-465`. | Source/static complete; award and save/load proof unavailable. |
| Focus architecture | The shared focus tree must remain connected, non-crossing, route-aware, localised, and AI-addressable. | The accepted focus audit records 184 engine focuses, 195 connectors, and zero crossings. No source-backed new route was proven by this completion audit. | Source/MCP layout evidence present; route reachability and weighted AI proof remain partial. |
| Event details, logs, evolutions, docs, and catalog | Player-facing event records and authoritative docs must match current implementation. | Event details/catalog work is recorded and the workbook exports identify Event 006 and SCN-008 as `Needs Testing`, but the current-authority markdown is stale as detailed below. | Partial/stale documentation authority. |
| Assets and portraits | Every visual consumer requires accepted source/rights, processing, wiring, manifest, and portrait-owner evidence. | The ASSET-004 grayscale image is resolved. Portrait wiring has a current owner handoff, while IW-179 identity/rights, AEX/NWE/BWX/chunk-3 flags, and ASSET-046 emblems remain gated. | Partial; rights and identity blockers remain. |
| Super-events and audio | Accepted slots require text, quote, art, licensed audio, wiring, and runtime evidence. | Slot 24 is wired. Slot 23 remains blocked because the accepted London Brass Players recording lacks the required redistribution clearance. | Partial/rights-blocked. |
| Custom 3D units, unit audio, and counters | Any accepted custom 3D unit would require the Meshy pipeline, sourced unit audio, bespoke vanilla-green counters, checksums, synchronization, and parent wiring. | No accepted Event 006 custom 3D unit or unit-sound package exists in the reviewed specs and plans. | Not applicable; no missing 3D handoff is asserted. |

## Highest-impact safe gaps

### P0 — protect the repaired shared host-ledger contract in the allocator validator — closed during audit

Before commit `d727d6a2b`, `.tools/audit_event6_allocator.py:803-847` extracted and validated `independence_wave_validate_execution_metadata` without asserting which host array the helper consumed.

The validator also did not extract `independence_wave_achievement_initialize_committed_wave`, so the second stale-ledger consumer could regress without failing the focused Event 006 audit.

Commit `d727d6a2b` now requires the exact token `array = global.liberation_plan_hosts` inside the extracted execution-metadata block and rejects `global.independence_wave_plan_hosts`.

The same commit reads `common/scripted_effects/006_independence_wave_achievement_effects.txt`, extracts `independence_wave_achievement_initialize_committed_wave`, and applies the same two assertions.

This is a regression guard only; it changes no gameplay and relaxes no admission, readiness, pre-event, reservation, or host-survival gate.

Owner: Event 006 parent.

Validation: the focused allocator audit passes with the new assertions and retains 149 publishers, 126 automatic/high-chaos selectors, 138 SCN-ranked selectors, 40 adapters, 32 attestations, 29 reservation groups, and the exact `3/4/5/7/10` ladder.

### P1 — reconcile the files that claim current authority

`docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:3` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:5` still identify the current override only through the absent-country and IW-086 work.

Neither current override records the standalone host-ledger repair, the setup-gated category repair, or the SCO adapter category isolation now present in current source.

`006_source_of_truth_map.md:59` and `006_independence_wave_resume_packet.md:53` still call ASSET-004 strict grayscale open.

That statement is stale: `006_event6_next_safe_tranche_improvement_addendum_2026_08_29.md:66` marks commit `49d9a577c` resolved and tells future workers not to regenerate the congress news picture.

The processed PNG is 397 by 153 with alpha, all 60,741 pixels have equal red, green, and blue channels, and the maximum and mean channel spread are zero.

The current processed PNG SHA-256 is `C1BBCA9B8083731FAFAAB384E341BE27B8FB990A035405FF443DDD4D56B7E9C7`; the DDS SHA-256 is `4AD0366DC87D54599D77AA2735CC832ADCA657DD212C3585B7948A91D5E57CEF`.

`006_event6_next_safe_tranche_improvement_addendum_2026_08_29.md:39` also preserves the older conclusion that the zero-country observation had no safe source target.

That conclusion is historical rather than current after commit `70231664a` identified and repaired the populated-versus-stale host-ledger mismatch.

Recommended owner: `chaosx_documentation_curator`.

Required action: update only the current-authority override and continuation disposition, preserve dated historical handoffs, point to the latest repair receipts, and keep the whole-event status at HOLD/PARTIAL.

### No additional safe gameplay patch proven

No source evidence authorizes a fallback release, a relaxed attestation gate, a generic package, a copied portrait, a substitute emblem, an unlicensed audio track, or a new formable admission.

The root defect already repaired in `70231664a` does not justify widening the allocator or bypassing package readiness.

## Accepted-plan disposition

| Accepted or queued item | Current disposition |
| --- | --- |
| P0 SCN-008 success-only publication | Implemented at source/static level by `3ce4b3468` and `713306f2e`; current MCP comparison and live execution remain unavailable. |
| Standalone zero-country observation | The earlier no-safe-patch disposition is superseded by the source-backed shared host-ledger repair in `70231664a`; focused regression coverage is complete in `d727d6a2b`, while live execution remains unavailable. |
| IW-179 FSM identity and atomic admission | Blocked by grounded identity, image, derivative-rights, and independent review; `independence_wave_fsm_sourced_identity_ready` must remain unset and FORM-48 remains unreachable through FSM. |
| IW-108 Buganda first-footprint package | Blocked by Event 012 ownership collision and missing Event 006 roster, force, lifecycle, adapter, attestation, Join, AI, cleanup, flag, and approved portrait evidence. |
| IW-013 NAV/Basque admission | Blocked by authoritative state reconciliation: the baseline registry/research evidence uses state 172, current runtime/vanilla-capital evidence uses 792, and optional 806 is separately recorded. No automatic correction is authorized. |
| IW-015 GLC admission | Blocked by duplicate Castelao ownership and requires parent disposition. |
| FORM-48 reachability | Queued behind IW-179 admission and exact HBX/HAW/FSM consent and transaction proof. |
| Remaining 34 formable families | Intentionally fail-closed until package, territory, tag, flag, identity, integration, GUI, and validation evidence exists. |
| League and evolution reachability dossier | Queued for current event/focus/GUI/probability evidence; no new League code is justified by this audit. |
| Additional package batch, focus branch, GUI, formable family, or super-event breadth | Rejected by the accepted stop line until current execution, rights, admission, and evidence gaps close. |

## Mandatory MCP evidence and exact limitations

### Root chain `chaosx.nr6.1`

Fresh `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` at revision `ac2516cf55a82d5ce3152e98d00c31e148f74b85a13a09c3ad7791c0453bef18`, with zero helper expansion, 8,569 unresolved nodes, 18 blocking diagnostics, and overall validation false.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65e13522a36bdc5706e716e5081578999c37a8bb0b7d8b6f966afa43cfcdfe3b/3918f52970c3fef4f00f6f7777dabd29aa781ee6af3db468eb1a5d64e939de8a/event-trace-ac2516cf55a8.json`.

Fresh `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` for root reachability.

Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b27383673d6ee996f015317a560d2d02f951fc321e0228bd40fe64b1af69cde/2cdea6ed8d7876cb729c0ccf4d0c8a1bf6c2dd6e9509817a66bbdaa007a016df/event-reachability-ac2516cf55a8-manifest.json`.

### Consolidated support-event chain

Fresh `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` for the support-event file.

Scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/978d15b1ffbcc61d00ab2225079424435639d5b5e0646cbd1f925de61b88f0f4/472f8726b9006c6adfcf11ed0d7e7c1f129f23725bf5234a0ae644ce368c3055/event-scan-ac2516cf55a8.json`.

Fresh `hoi4.event_render` returned a partial support overview.

Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f92a12e3840684e01844397e77b88a32861bfa157e4875b1ae310c7b3fe80aa/929e3ac69e1d4c1acb76fe71b964890e9e58c2f32cce0428f4a21225b2ff823b/event-overview-ac2516cf55a8-manifest.json`.

### SCN-008 chain `chaosx.triggerable_scenarios.8`

Fresh `hoi4.event_inspect` returned a partial trace.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c32abdf84d5b59861238dd767693b5b3bcdd9eabc0af75afb1592ac7d381da81/fdbd2a7bfe1b2aa0bfbe9f5d8f7450b078a5ec249a4c4fcb446c881b1055dabf/event-trace-ac2516cf55a8.json`.

Fresh `hoi4.event_render` returned a partial state render.

Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b390373b13c685a4e97aea07cbb12503950b20d705eaa67534ce3d150eca0cde/f30f282dac09c7cd136ecf96dc6faadf9eca3c9608ce1185a456391d1c44454d/event-state-ac2516cf55a8-manifest.json`.

### Comparison blocker

The correctly shaped `hoi4.event_compare` request from the earlier `3ab4ef70be0beb8fdb94320b71fc0769ac1bf50c76f6529abc50afc42fb1d20e` revision to the current `ac2516cf55a82d5ce3152e98d00c31e148f74b85a13a09c3ad7791c0453bef18` revision failed with `EVENT_REVISION_NOT_CACHED` and produced no comparison artifact.

Source diff review is not treated as equivalent event comparison evidence.

The partial Event Chain Viewer results expose no isolated new Event 006 defect because helper projection is absent and the diagnostics are whole-workspace aggregates.

## Weighted logic

All Event 006 weighted surfaces were routed to the required read-only `chaosx_ai_probability_auditor` for a fresh current-revision pass.

The routed scope includes the outer 14-region allocator and nested package weights, root event `ai_chance`, five evolution MTTH stages, Event 006 decisions and missions, shared-focus AI weights, Event 006 AI strategy factors, League choices, and SCN-008 weighting.

The routed auditor had not returned a completed typed scenario dossier at the parent-directed evidence cutoff and was stopped without making changes.

This is an evidence limitation rather than proof of a balance defect: the parent must append the current probability-auditor handoff or its exact MCP capability blocker before any balance, AI, or probability completion claim.

No weighted value was changed by this audit, and no probability comparison is claimed.

## Focused validation evidence

The following current read-only checks passed before this handoff was written:

- `.tools/audit_event6_allocator.py` passed after commit `d727d6a2b` added the shared-host-ledger assertions, with 149 publishers, 126 automatic/high-chaos selectors, 138 SCN-ranked selectors, 40 adapters, eight adapter-only rows, 32 attestations, 29 reservation groups, the exact `3/4/5/7/10` ladder, and the retired pre-event surface.
- `.tools/audit_event6_country_api.py` passed with 242 broad API tags, 191 resolved carriers, zero missing or duplicate bindings, and the IW-031 crosswalk intact.
- `.tools/audit_event6_flags.py --strict` passed 102 of 102 registered Event 006 flag families.
- `.tools/audit_event6_form16.py` passed the admitted ARM/GEO/AZR FORM-16 contract.
- `.tools/audit_event6_gui_matrix.py` passed the five-tab statehood-ledger semantic matrix, frame coverage, and animation cleanup contract.
- `.tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight documented edge cases.

These static validators do not establish engine execution, country release, live decision reachability, achievement award, save/load persistence, or visual consumer behavior.

## Asset, portrait, audio, and documentation gaps

- ASSET-004 is resolved in current binaries and evidence; the current-authority markdown must stop listing it as open.
- ASSET-046 remains incomplete because only FORM-05 and FORM-48 have accepted emblem evidence; other league/formable identity consumers must remain unwired until motif and rights approval exists.
- The AEX cross-event basename collision, 48 NWE ideology aliases, BWX family, and fourteen chunk-3 flag source/rights gates remain owner or user approval blockers.
- Every character portrait remains under `chaosx_portrait_creator` authority. IW-179 has no rights-cleared grounded identity packet and remains a completion blocker for its package and FORM-48 reachability.
- Super-event slot 23 audio remains blocked by redistribution rights. Generated, synthesized, placeholder, recorded-without-clearance, or unlicensed audio is not an accepted substitute.
- The Event 006 source-of-truth map, resume packet, and next-safe continuation disposition are stale after current accepted repairs and must be reconciled without erasing historical evidence.
- The catalog's `Needs Testing` and cluster `Partially Available` labels remain consistent with the current HOLD/PARTIAL disposition.

## Remaining blockers and recommended order

1. Preserve commit `d727d6a2b` and its passing focused allocator audit as the regression proof for the shared host-ledger repair.
2. Route the current-authority reconciliation to `chaosx_documentation_curator`, including the host-ledger repair, setup-category gates, SCO adapter guard, and resolved ASSET-004 evidence.
3. Append the fresh probability-auditor result and preserve any MCP capability blocker exactly; do not infer balance from raw source if typed evaluation is unavailable.
4. Repair or repopulate the Event Chain Viewer revision cache, then rerun current root, support-chain, and SCN-008 inspect/render and a same-scope compare.
5. Keep IW-179, IW-108, IW-013, IW-015, the 34 unadmitted formable families, slot 23 audio, ASSET-046, and unresolved flag/portrait packages fail-closed until their named authority, rights, identity, territory, and MCP evidence gates are satisfied.
6. Leave live country release, re-entry, save/load, achievement-award, super-event playback, and in-game GUI validation to the user.

No simplification, fallback package, relaxed gate, invented identity, copied asset, substitute audio, or completion claim was made by this audit.
