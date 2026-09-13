# Event 027 current completion audit

> **Superseded status notice (2026-09-01):** This dated completion audit is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its old receipt-defect and keep-out-of-default recommendation are contradicted by the current source evidence recorded there.

Date: 2026-08-31

Mode: isolated read-only completion audit

Audit target: the current working-tree Event 027 implementation after the parent's receipt-recovery hardening and concurrent presentation updates

## Verdict

Event 027 is source-playable for ordinary fresh adoption and mastery transactions, queued batch progression, human pages, AI dispatch, evolution scheduling, lifecycle hooks, history/details integration, and achievements.

Event 027 is **not acceptance-complete** and must not receive a completion commit.

The most important current-source defect is in recovery of a receipt already stored as `native_adoption`: `common\scripted_effects\027_doctrine_research_effects.txt:3208-3214` clears the durable pending marker and records the no-choice result without rechecking `doctrine_research_selected_grand_doctrine_is_active`.

That branch does not satisfy the required rule that native-adoption recovery verify that the recorded Grand Doctrine remains active before accepting the terminal receipt.

The ordinary `effect_applied` adoption recovery branch at `common\scripted_effects\027_doctrine_research_effects.txt:3187-3193` does contain the active-Grand-Doctrine check, so the defect is limited to the distinct `native_adoption` recovery state rather than every adoption path.

The implementation therefore remains qualified source-playable, but its interrupted native-adoption recovery contract is defective and its default automatic-pool enablement is premature.

## Required receipt-hardening re-audit

| Requirement | Current disposition | Current evidence |
| --- | --- | --- |
| `effect_applied` mastery recovery must reread native mastery | Source pass | `common\scripted_effects\027_doctrine_research_effects.txt:3166-3185` calls `doctrine_research_capture_transaction_level` on every retry at line 3176, including when a positive post-level was already stored. |
| Stored and current post-level must both equal pre-level plus one | Source pass | Lines 3174-3182 derive the expected level from the receipt pre-level plus `constant:doctrine_research_event.mastery_point_increment`, then require both the stored receipt post-level and the current observed level to equal it. The increment is exactly one at `common\script_constants\027_doctrine_research_constants.txt:37`. |
| Recovery target must still own the recorded Grand Doctrine | Source pass for `effect_applied`; source fail for `native_adoption` | Mastery recovery checks the recorded doctrine at line 3179, and ordinary adoption recovery checks it at line 3190. The separate `native_adoption` branch at lines 3208-3214 has no such check. |
| Pending marker without matching receipt must quarantine | Source pass | `common\scripted_effects\027_doctrine_research_effects.txt:3112-3118` performs the receipt lookup when pending, and lines 3128-3136 record an ambiguous transaction and quarantine when no matching receipt is found. |
| Unproven prepared, ambiguous, or abandoned receipt must fail closed | Source pass | `common\scripted_effects\027_doctrine_research_effects.txt:3220-3225` marks the receipt ambiguous and quarantines the active batch. |

The defect contradicts the accepted parent handoff `docs\plans\027_doctrine_research_plans\subagent_handoffs\parent_transaction_followup_2026-08-31.md:23`, which says adoption recovery requires the recorded Grand Doctrine to remain active.

It also makes `docs\events\027_doctrine_research\overview.md:47` stale where that paragraph presents the same rule as fully implemented.

## Older warning re-audit

### Dynamic mastery presentation

The older warning that mastery presentation was static or missing is **no longer true in the current files**.

`common\scripted_effects\027_doctrine_research_effects.txt:373-456` computes current level, next level, native maximum, branch completion, and Grand Doctrine Milestone state, including the four-level Peoples' War exception.

`common\scripted_effects\027_doctrine_research_effects.txt:1638-1646` prepares the active branch display, and lines 1648-1658 restore the receipt selection and rebuild the confirmation display.

The hidden router calls `doctrine_research_prepare_track_display` at `events\027_doctrine_research.txt:587-605` before opening one of the visible `.60` through `.77` pages.

The current source has 107 unique `GetDoctrineResearchOptionStatus*` localisation calls and 107 matching scripted-localisation definitions.

The confirmation description distinguishes adoption from mastery, so adoption does not display irrelevant mastery values while mastery retains current, next, maximum, completion, and milestone context.

This closes the old source-level warning only.

The MCP Event Chain Viewer is a structural event diagram, not a one-to-one native popup renderer, so largest-page overflow, text clipping, and final in-game presentation remain unproven.

### First Lesson batch-start emptiness

The older warning that First Lesson did not use immutable batch-start emptiness is **no longer true in the current files**.

`common\scripted_effects\027_doctrine_research_effects.txt:1763-1786` appends one immutable empty-domain value for Army, Navy, Air, Special Forces, and Chaos Warfare when each new batch row is created.

`common\scripted_effects\027_doctrine_research_achievement_effects.txt:10-77` requires a human-started multi-choice batch, finds a consumed adoption receipt, maps its domain to the corresponding batch-start array at lines 42-47, and searches for a later same-domain consumed mastery receipt only when that stored empty-domain value is positive at lines 48-67.

This is a source-level pass.

Positive and negative runtime cases remain missing, including adoption in a domain that was already established at batch start, cross-domain adoption/mastery, reversed receipt order, AI completion, and a two-choice human success.

## Completion status by surface

| Surface | Source status | Acceptance status | Evidence and remaining issue |
| --- | --- | --- | --- |
| Root, registration, and global firing | Finished in source | Partial | `chaosx.nr27.1` is the actorless triggered root; Event 027 is repeatable at `common\scripted_effects\chaosx_logic_effects.txt:325`, registered at chaos tier 0 around lines 188-190, and included in the default reworked-event trigger at `common\scripted_triggers\chaosx_settings_triggers.txt:35`. One bounded country fanout appends immutable batches. Runtime fanout and eligibility traces remain missing. |
| Default automatic selection | Implemented | Design deviation / blocker | `docs\specs\027_doctrine_research_specs\027_doctrine_research_acceptance_criteria.md:13` makes default enablement conditional on the full rework being ready for normal selection. Event 027 is default-enabled while the native-adoption recovery defect, native engine proof, and required comparisons remain open. |
| Country participation and queue | Finished in source | Partial | The live-country gate includes non-capitulated countries and governments in exile. Batches append rather than overwrite and preserve stage/size. Save/reload, overlap, exile, and country-creation timing matrices remain unproven. |
| Fresh adoption and mastery transaction | Finished in source | Blocked for final acceptance | Static native adapters use `set_grand_doctrine`, `set_sub_doctrine`, 107 exact `add_mastery` wrappers, native readback, and postconditions. Low, middle, final, fractional, and banked runtime behavior is unproven. |
| Receipt recovery and idempotency | Partial | Blocked | `effect_applied` mastery and adoption recovery and orphaned-pending quarantine pass source review. The `native_adoption` receipt branch lacks the recorded-Grand-Doctrine check. No accepted interruption/save/reload trace exists. |
| Human chain and pagination | Finished in source | Partial | Thirty-one unique Event 027 IDs cover `.1-.13` and `.60-.77`; deterministic two-page navigation exists. Native popup overflow and click-through evidence remains missing. |
| Dynamic mastery presentation | Finished in source | Partial | Current/next/max/completion/milestone values and action-specific confirmation are wired. Final consumer rendering is missing. |
| AI chooser and recalculation | Finished in source | Blocked for probability acceptance | Five domains, 13 Grand Doctrines, 18 track rows, and 107 subdoctrine rows feed weighted `random_list` surfaces. All 37 named scenarios remain unresolved by typed state. |
| Evolution scheduler | Finished in source | Partial | The centralized 90-day progression enables one next stage and records the promoted stage. Live timing and MCP timing evidence remain missing. |
| Lifecycle and controller transitions | Finished in source | Partial | Exact-country hooks cover control, puppet/release, autonomy, government, exile/reinstatement, civil-war end, and annexation; shared tag-switch handling reconciles old and new hosts without an Event 027 recurring world fanout. Save/reload, annexation, subject/controller, exile, and pure tag-switch traces remain missing. |
| Special Forces | Fail-closed in source | Design gap / blocked | Empty-track assignment is exact and active mastery is exposed only while branch-to-track identity is unambiguous. When both reusable-token tracks are occupied, Event 027 suppresses all Special Forces mastery. The limitation is now disclosed, but accepted proof that this state-level absence satisfies the spec's fully-adapted-or-explicitly-absent contract is missing. |
| Chaos Warfare | Finished in source | Partial | Native owner gates, exact adapters, scoring, and doctrine-owned effects are used without migration or technology shortcuts. Native graph and runtime identity evidence remains missing. |
| History, Event Log, and Event Details | Finished in source | Partial | Actorless history stores immutable batch size and shared details present the progression range. Final consumer evidence for History/Event Log/Event Details is missing. |
| Achievements | Finished in source | Partial | Three predicates and active/grey/not-eligible icon triplets are wired; First Lesson's batch-start rule passes source review. Positive/negative runtime matrices are missing. |
| Localisation | Finished in source | Partial | Current file is UTF-8 with BOM, has 340 unique string keys, no duplicate string key, and no missing direct event reference in the current static scan. Consumer layout proof remains missing. |
| Report and achievement assets | Finished and wired in source | Partial | The report DDS and nine achievement DDS files exist with expected dimensions and headers; GFX aliases are present. Final in-game consumer evidence and completion-time temporary-workspace disposition remain open. |
| Catalog and cluster | Current and honest | Partial by design | The XLSX and exports identify Event 027 as `Needs Testing`, Minor Repeatable, cluster 9, Medium severity. Cluster 9 remains `Partially Available` because unreworked members remain; that cluster status is not itself an Event 027 defect. |
| Documentation and handoffs | Partial | Blocked from closure | Specs, overview, implementation handoffs, asset handoffs, and spreadsheet handoff exist. The overview and `mcp_evidence.md` contain stale MCP claims, and the overview/transaction follow-up overstate native-adoption recovery. |

## Current mandatory MCP evidence

### Event chain

The current MCP route did **not** return `Transport closed` in this audit.

The historical `Transport closed` blocker recorded in the overview, `mcp_evidence.md`, and several parent handoffs is therefore not the current transport state.

`hoi4.event_inspect` for `chaosx.nr27.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`, and graph hash `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`.

It returned no direct Event 027 blocker, but validation is false because the large-workspace helper and lifecycle projections were deferred; helper expansion remained zero, the aggregate graph retained one blocking diagnostic, and the linked lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51124d9c1ef13722c3f1e674c5e449fd861c321682c21750384686cab3ba759/dc4e06dd225ab711903c94dea37fc64df2af94eb9085fd210adde625686f035f/event-lint-2725045f62d1.json`.

The root overview render returned `EVENT_RENDERED_PARTIAL` on the same revision, selected two nodes, omitted 42,454 nodes, and remained validation-false.

The `.7` options render returned `EVENT_RENDERED_PARTIAL`, selected 11 nodes, omitted 42,445 nodes, and remained validation-false.

The current overview and options artifacts are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da779ec7c789e8eb89c26068bcbc010c902ac912a58f054fa5fc6e52f5fd2163/aa200f7ea14fae71ae7977400ca286a90246c3c1ffda290a352f74246dd884b9/event-overview-2725045f62d1-manifest.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e41b70b1c3bbccf2bb8de1c4a1fbc6f9c3a80caa29ef0bc144676ab0b4f1d8b/66cb11c439235d1ca4c5b3f832ced01ecc83d9045e6901ac36208b1cb5a58412/event-options-2725045f62d1-manifest.json`

`hoi4.event_compare` from the immediately preceding audited revision `3a6b790bec8c1a4849cc984be80622aaac6b0c0bfe8b30a117042e95fd7c2205` to `2725045f62d1...` returned `EVENT_REVISION_NOT_CACHED` with zero artifacts.

The required comparison is still unavailable, and source diff review is not treated as equivalent evidence.

### Doctrine and technology

Focused `hoi4.tech_inspect` for `peoples_war` timed out after 180 seconds.

`hoi4.tech_render` did return `TECH_RENDERED` for the current doctrine view at revision `8b168861b8681377c62de173fda1fb474189b5cd9f66404930711479d454167d`, graph hash `132212cf7a6dfef84ff13aa10e081e9cb4ccddc449c08a0415e51e92a1f32c04`, with 80 selected and 483 omitted nodes.

That render explicitly reports `sourceAccurate:false`, validation false, and 1,425 blocking technology diagnostics, so it is not accepted native-doctrine proof.

Its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c81d2987a423241d92a7d822d8458e8cb0167d8efeb335671d787de5941d9d18/44e52b4e4092e6e34d0c8c9eac5ae0117b6f8bd2e74ce455e21aa75349fbc6c9/technology-doctrine-8b168861b868-manifest.json`.

`hoi4.tech_compare` against the older partial scan artifact returned `TECH_GRAPH_ARTIFACT_INVALID` because that baseline uses an incompatible schema.

Thus Army, Navy, Air, Special Forces, and Chaos Warfare still lack accepted inspect/render/compare doctrine evidence.

### Weighted AI and probability

The required `chaosx_ai_probability_auditor` completed a read-only pass and changed no files.

Current `hoi4.probability_inspect` returned `PROBABILITY_SOURCE_DISCOVERED` for `common\scripted_effects\027_doctrine_research_ai_effects.txt`, workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `faf0ba9ef8abd701aa8ac67c79ef98c88830e7258a7fd22eaa93cd72f5b5df89`, source hash `db288f9569977cf12980a03908f6138a328ee3963f8df522a8ebecc6565e50a4`, adapter `random_list`, and 143 unrestricted candidate matches.

The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e75b26f8863cfa8356c0a6b79a25a6530c4e7fc34d212bdad72428def5bce92a/cb975062452df5fc1b42284d3375ef16258ae3d1e6a0ac14e35724de975f1d26/probability-inspect-db288f956997.json`.

Focused domain, Grand Doctrine, and track source ranges returned zero candidate matches because the historical requested line ranges no longer match the current parsed structure, and the subdoctrine inspection was interrupted before a result.

The historical 37-scenario set `DR_027_FINAL_2026_08_30`, hash `2e0e1ba67d5dc17a2982d15c2c35568382f8e7d8d16badde45cbbbe94a6d8daa`, remains unresolved for acceptance because the analyzer cannot materialize typed country/doctrine state.

The prior evaluations produced unresolved candidate rows on every layer: five domain rows, 13 Grand Doctrine rows, 18 track rows, and 107 subdoctrine rows.

No valid complete before/after `hoi4.probability_compare` exists for the current implementation; prior comparisons timed out, remained partial/unresolved, or used incomplete custom-pool manifests.

No current scenario-specific simulate or sequence evidence exists because typed fixtures and a complete cadence/state/reset/terminal manifest are unavailable.

The synthetic five-entry arithmetic smoke test proves only adapter arithmetic and is not Event 027 probability evidence.

All 37 scenarios, DR-A01 through DR-G03, remain unresolved for acceptance.

## Meaningful source and artifact validation

- Current source snapshot has 31 Event 027 event IDs and 31 unique IDs.
- The exact native adapter source contains 107 `add_mastery` blocks and 107 `set_sub_doctrine` blocks.
- The player presentation has 107 unique option-status calls and 107 matching scripted-localisation definitions.
- The main Event 027 effects file contains 7,743 opening and 7,743 closing braces.
- The current English localisation begins with `EF BB BF`, has 340 unique string keys, no duplicate string key, and no missing direct Event 027 title/description/name reference in the current static scan.
- Current source hashes include `common\scripted_effects\027_doctrine_research_effects.txt` SHA-256 `7e55b61b203e0ad525901aed2ac9fa3298a820e7b39572803f2748c61c5cde49`, exact mastery SHA-256 `51b94513ddd690d7fd45e945f1a9c76e002ab527670117843cc6a176ebc1f525`, AI SHA-256 `6c4b7e9b776682496c2fb7abac627faf22b72a56b7789fb3f38657aa733b9d39`, triggers SHA-256 `11667391af4fa10ce9870c9d3be9a993ca80efd3ecdbcf66d1c78bb752a69b76`, and achievement effects SHA-256 `955d7c51c0a3105abb9abeb7a929f2ab2a23093a7c3909361d42fe3529f1abe1`.
- The workbook SHA-256 is `54a8b0b8204be66da541c5f5b513e0d11d8621fa820894e04862391a45f4eba3`; the Event 027 row is `Needs Testing`, Minor Repeatable, cluster 9, Medium severity.
- The Event CSV SHA-256 is `4ccd1546561e3112e3dc90527eb73da9cbae7f0c5bb90608d4e036ad9a790fbd`; its Event 027 text matches the workbook.
- The Cluster CSV SHA-256 is `77b2509d31b0e86cc20a1cfb226fa9412b31eed59ec713e9c1afe2e352a8597e`; cluster 9 remains `Partially Available` with Event 027 listed among its members.
- The report DDS parses as 210 by 176 with the expected legacy DDS header, and all nine achievement DDS files parse as 64 by 64 with non-empty alpha.
- Report GFX wiring is present in `interface\027_doctrine_research.gfx:10-11`; achievement aliases are present in `interface\chaosx_achievements.gfx:1564-1572`; achievement registry entries are present in `common\achievements\chaos_redux_achievements.txt:4244-4256`.

These checks establish source coverage and artifact presence.

They do not establish native engine semantics, one-to-one consumer rendering, persistence, event comparison, doctrine comparison, or probability acceptance.

## Accepted-plan and handoff disposition

| Plan or handoff family | Disposition |
| --- | --- |
| Repository exploration and scripted-system architecture | Promoted into the implementation. The numeric fail-closed registry, static native adapters, owner gates, queue/receipt design, and integration map exist in source. |
| Parent implementation and pagination | Implemented in source. Pagination and remaining-choice presentation are present; native popup overflow evidence remains open. |
| Folder/track guard and native mastery edge | Implemented in source. Folder-owned emptiness guards close Army/Chaos track collisions; one-point/readback adapters and native-adoption return flow exist. Native graph/runtime proof remains open. |
| Parent transaction follow-up | **Partially implemented.** Effect-applied mastery proof and orphaned-pending quarantine are present. The handoff's assertion that adoption recovery always rechecks the recorded Grand Doctrine was not implemented in the separate `native_adoption` recovery branch. |
| Parent AI strategy audit | Implemented at source level. Dead flag-only strategy signals were replaced with native observable triggers. Probability acceptance remains unresolved. |
| Localisation audits | Later source closes the old static mastery-presentation and remaining-choice warnings. Final consumer rendering remains open. |
| Generated report art and achievement icon handoffs | Assets were promoted and wired. Final in-game consumer evidence remains open. |
| Spreadsheet handoff | Promoted. XLSX and export rows are aligned and retain the honest `Needs Testing` status. |
| Probability baseline and final audit | Not accepted as final balance proof. All 37 named scenarios remain unresolved, no complete current compare exists, and source-range routing is stale. |
| Earlier completion audits | Superseded as current snapshots but still valid for unclosed runtime, doctrine, comparison, consumer, and Special Forces blockers. Their old dynamic-presentation and First Lesson source warnings are closed. |
| Improvement-loop planning | No unresolved Event 027 addendum was found that is both accepted and left without implementation, queue disposition, rejection, or promotion. |

No Event 027 subagent patch was found without a corresponding handoff.

## Asset, UI, and adjacent-surface disposition

Event 027 introduces no named event-owned scripted GUI.

Its visible flow uses native event popups, and the shared Event Log/Event Details framework is outside the `chaosx_event_ui_worker` ownership rule, so no event UI worker handoff is missing.

No character portrait is in scope, so no `chaosx_portrait_creator` handoff is required.

No custom 3D unit, animation, unit sound package, or custom unit counter is in scope, so the 3D/audio/counter completion gates do not apply.

No super-event, focus tree, decision/mission package, country package, formable, or achievement outside the three Event 027 achievements is introduced by this event.

The temporary asset workspace under `docs\assets\027_doctrine_research\` may remain while the event is blocked, but durable provenance and final evidence must be promoted and temporary material disposed according to the asset handoff before a true completion claim.

## Deviations, simplifications, stale claims, and blockers

1. `native_adoption` recovery accepts a terminal receipt without verifying that the recorded Grand Doctrine remains active.
2. Event 027 is in the default automatic selection pool despite not satisfying the acceptance-complete gate and despite the live receipt-recovery defect.
3. Both occupied Special Forces tracks suppress Event 027 Special Forces mastery; this is a disclosed fail-closed limitation, not full support.
4. Native low, middle, final, fractional, banked, empty-track, branch-completion, Special Forces, and Chaos Warfare behavior lacks accepted engine/runtime proof.
5. Save/reload interruption, receipt idempotency, overlapping batches, annexation, subject/controller transitions, government in exile, pure tag switch, and evolution timing lack accepted runtime traces.
6. Current event inspect/render evidence is partial and validation-false; event comparison remains blocked by `EVENT_REVISION_NOT_CACHED`.
7. Current doctrine inspect timed out, the doctrine render is non-source-accurate and validation-false with 1,425 blocking diagnostics, and doctrine comparison rejects the older artifact schema.
8. All 37 named probability scenarios remain unresolved; no complete current before/after probability comparison exists.
9. Largest native event pages, History/Event Log/Event Details, achievement positive/negative cases, and report/achievement assets lack final consumer evidence.
10. `docs\events\027_doctrine_research\overview.md:47` and `parent_transaction_followup_2026-08-31.md:23` overstate native-adoption recovery.
11. The final paragraphs of the overview and `docs\plans\027_doctrine_research_plans\mcp_evidence.md` are stale where they say the current event route still returns `Transport closed`, where they say no current technology render exists, and where they index older source hashes/revisions.
12. The current probability routing still relies on historical line ranges that no longer match the parsed AI source.

No undisclosed fallback reward, generic military-experience substitute, active-Grand-Doctrine replacement, technology-grant shortcut, multi-level mastery dump, copied portrait, custom 3D placeholder, or unlicensed audio package was found in Event 027 scope.

## Recommended next actions

1. The gameplay owner should gate the `native_adoption` recovery branch on `doctrine_research_selected_grand_doctrine_is_active`; a mismatch should become ambiguous and quarantine rather than clear the pending marker as accepted.
2. The owner should keep Event 027 out of default automatic selection until the receipt defect is fixed and the acceptance gate is deliberately reopened, or explicitly amend the design if default-enabled testing is intended.
3. After the owner patch, refresh `overview.md`, supersede the transaction follow-up claim, refresh `mcp_evidence.md`, and rerun current-revision event inspect, overview/options renders, and before/after event compare.
4. Restore a focused source-accurate doctrine inspect/render/compare path for all five domains, then obtain the owner-run engine traces for low/middle/final, fractional/banked, empty-track, native-completion, Special Forces, and Chaos Warfare cases.
5. Rebuild current source selectors and typed fixtures for DR-A01 through DR-G03, then rerun inspect, evaluate, sweep, sequence/simulation where the scenario contract calls for them, render, and current before/after compare through `chaosx_ai_probability_auditor`.
6. Capture owner-run persistence/lifecycle/evolution traces and final consumer evidence for pagination, dynamic mastery text, History/Event Log/Event Details, achievements, report art, and achievement icons.
7. Retain `Needs Testing` and do not issue a completion commit until the source defect and every mandatory evidence gap above are closed.

## Audit write scope

This handoff is the only file created by this audit.

No gameplay, localisation, asset, spreadsheet, specification, overview, existing handoff, or MCP evidence file was edited.

No commit was created.

## Parent resolution — 2026-08-31 continuation pass

This section records the parent's post-audit resolution against the current shared working tree and supersedes only the earlier finding that the `native_adoption` recovery branch lacked an active-Grand-Doctrine guard.

The verdict remains **source-playable but acceptance-incomplete**.

### Resolved source defect

The parent patch is present in `common\scripted_effects\027_doctrine_research_effects.txt:3208-3222`.

For a receipt in `constant:doctrine_research_receipt_state.native_adoption`, the recovery branch now requires `doctrine_research_selected_grand_doctrine_is_active = yes` at line 3211 before it clears `doctrine_research_transaction_receipt_pending` and records the terminal no-choice adoption result at lines 3212-3215.

If the recorded Grand Doctrine is no longer active, lines 3217-3220 set the receipt state to `ambiguous`, call `doctrine_research_record_ambiguous_transaction`, and call `doctrine_research_quarantine_active_batch`.

The pending marker is not cleared in that mismatch branch.

A bounded static extraction of this branch found exactly one active-doctrine check, one ambiguous-state assignment, one quarantine call, and one pending-marker clear confined to the successful branch.

The current effects file SHA-256 is `cb5f51fb295acfaf1815900d8ed4671528e8b27db977fd78cb77c3e575207112`, and the full file remains structurally balanced at 7,747 opening and 7,747 closing braces.

This closes the prior source defect and promotes the parent transaction follow-up's intended native-adoption recovery rule into current source.

It does not prove interruption/save/reload behavior in the game engine.

### Fresh Event Chain Viewer evidence

The MCP connection responded; `Transport closed` did not recur in this continuation pass.

Fresh read-only `hoi4.event_inspect` lint for `chaosx.nr27.1`, downstream depth 8 with `maxNodes: 240`, `maxEdges: 420`, helper expansion requested, and `refresh: true`, returned status `ok` with code `EVENT_INSPECTED_PARTIAL`.

The returned event revision is `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`, and the graph hash is `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`.

The authoritative lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51124d9c1ef13722c3f1e674c5e449fd861c321682c21750384686cab3ba759/dc4e06dd225ab711903c94dea37fc64df2af94eb9085fd210adde625686f035f/event-lint-2725045f62d1.json`.

The focused result reports no direct Event 027 blocker, but validation remains false because the large-workspace helper and lifecycle projections were deferred; helper count remains zero and the aggregate graph retains one blocking diagnostic.

The event revision did not change after the helper-only receipt patch, which demonstrates that this Event Viewer graph revision does not fingerprint or expand the patched scripted-effect body.

Fresh bounded `hoi4.event_render` for the `.7` confirmation event used the `state` view, both directions, depth 4, `maxNodes: 120`, and helper expansion requested.

It returned status `ok` with code `EVENT_RENDERED_PARTIAL` on the same revision and graph hash, selected 120 nodes, omitted 42,336 nodes, and remained validation-false for the same deferred-analysis reason.

The exact render artifacts are:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92fa0917b0b0d739f7fb633d993b590463064f74e1ca010fe42436d8c92c4dbe/07dba8c4a1c849565b220da4cf31fe090d8eaf9eae7a1de3681717fc6d3e6b5d/event-state-2725045f62d1-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f87004f1b38456c2e1fcdac2f9b8b3af8e5e3831b64f6fccb894daa6122c8e2/31e13aa314a271a02b6fbb78c696333758d382b0a61806ae724aaf5d756faeb2/event-state-2725045f62d1.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d51d11572fa44ae2a232ab0da083759bbb966a5566d5cdb823f38a8a6d36bf5e/89a2872be10315ea7fefec7362ad2217dcbf5ade1bf59677c696983743efb316/event-state-2725045f62d1.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96700de1f4e330a5ddaf771f47395dc26dea924fb0c4063b9b1761e6d0acdd18/2ea4d838899c803e0024565dc8f3ad2e0447b311da669ebbd83263b24f8231a5/event-state-2725045f62d1.png`

The mandatory comparison attempt still returned status `error`, code `EVENT_REVISION_NOT_CACHED`, and zero artifacts.

Because the viewer retained the same revision and omitted the helper body, neither the partial lint nor the partial state render is equivalent to runtime proof of the resolved receipt edge.

### Remaining acceptance blockers after parent resolution

- Owner-run interruption and save/reload evidence must still prove that successful `native_adoption` recovery clears the pending marker without consuming a choice and that a changed Grand Doctrine marks ambiguous and quarantines without clearing pending.
- Native low, middle, final, fractional, banked, empty-track, native-completion, Special Forces, and Chaos Warfare behavior still lacks accepted engine evidence.
- Event comparison remains unavailable, and the current Event Viewer evidence remains partial with helper expansion absent.
- Doctrine inspect/render/compare acceptance, all 37 named probability scenarios, lifecycle/evolution runtime traces, native-popup presentation, History/Event Log/Event Details, achievements, and final asset consumer evidence remain open as recorded above.

No gameplay file was edited by this continuation audit.

This dated section is the only documentation change made by the continuation audit, and no commit was created.

## Parent cluster resolution evidence — 2026-08-31

This section records the isolated current-tree MCP retry after the parent corrected the National Breakthroughs cluster registry and regenerated the workbook exports.

The verdict remains **source-playable but acceptance-incomplete**.

### Current patched-source identities

- `common\scripted_effects\027_doctrine_research_effects.txt` SHA-256: `cb5f51fb295acfaf1815900d8ed4671528e8b27db977fd78cb77c3e575207112`.
- `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt` SHA-256: `51b94513ddd690d7fd45e945f1a9c76e002ab527670117843cc6a176ebc1f525`.
- `common\scripted_effects\chaosx_event_cluster_effects.txt` SHA-256: `5a680f8a0896f0190830223def966d722c8509815a0b321f535b158226521e5a`.
- `docs\spreadsheets\chaos_redux_events_catalog.xlsx` SHA-256: `b80e62236ca6d01a3090d5f78f1e51b34590e105aad7fa641b471f41dd77aad9`.
- `docs\spreadsheets\chaos_redux_events_catalog.csv` SHA-256: `6f2d8a94aeaec24608dd4688fb64d294ec1d597db6799bb7a55361ae58c039a1`.
- `docs\spreadsheets\chaos_redux_clusters_catalog.csv` SHA-256: `9452fe5e616bb600a7c3e6d5af7b1168d0b54c8fbbe0e9e88c30de52af3e6a4d`.

### Current MCP retry results

Fresh read-only `hoi4.event_inspect` lint for `chaosx.nr27.1` used downstream direction, helper expansion, depth 8, `maxNodes: 240`, `maxEdges: 420`, and `refresh: true`.

The call timed out awaiting `tools/call` after 180 seconds.

It returned no status code, revision, graph hash, artifact id, or artifact hash.

Fresh focused `hoi4.tech_inspect` trace for `peoples_war` used both directions, subtechnology inclusion, depth 3, `maxNodes: 80`, and `refresh: true`.

That call also timed out awaiting `tools/call` after 180 seconds.

It returned no technology revision, graph hash, artifact id, or artifact hash.

A subsequent bounded `hoi4.event_render` overview for `chaosx.nr27.1` used downstream direction, depth 4, `maxNodes: 80`, no helper expansion, and the cached route.

The render returned `Transport closed` before producing a status code, revision, graph hash, or artifact.

Therefore **Event 027 does not have a post-cluster-patch MCP render revision or artifact in this pass**.

The earlier revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570` and its artifacts remain historical pre-cluster-patch evidence and are not relabeled as current.

### Native mastery inspectability disposition

The native `add_mastery` implementation remains present in 107 exact source adapters, but the focused doctrine/technology inspection produced no graph artifact in this pass.

Consequently **the native `add_mastery` path is not currently engine-inspectable through the required MCP route**.

Source presence and the installed effect documentation are not treated as equivalent engine evidence.

No gameplay file was edited by this evidence retry, and no commit was created.
