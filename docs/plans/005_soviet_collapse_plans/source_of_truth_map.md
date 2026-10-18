# Event005 Source Of Truth Map

Original date: 2026-08-09
Updated: 2026-10-05
Scope: Event005 Soviet Collapse documentation, specs, plans, and handoffs.

This map routes Event 005 documentation and distinguishes current evidence from older implementation snapshots. The 2026-08-09 reconciliation below predates the 2026-10-05 audit and must be read as historical.

## 2026-10-05 Current Reconciliation

- `docs/plans/005_soviet_collapse_plans/implementation_audit_2026-10-05.md` is the current implementation and validation-status report. It separates user-authorized work, source facts, historical evidence, unaccepted design, and current blockers.
- `chaosx.nr5.1` now guards its normal opening dispatch with SOV existence, non-capitulation, and owned-state checks, then routes absent, capitulated, or state-less SOV to `chaosx.nr5.138` in the Settings-selected root country. The event and localization keys are present in source; this narrow implementation fact does not establish completion of the full event chain.
- The latest focus audit reports seven of 43 trees with authored-layout failures: Ukraine, generic breakaway, internal republic, Caucasus, Central Asia, Moldova, and NLC. It also leaves the eligible fallback-country set unresolved for `soviet_collapse_breakaway_focus_tree` because the release pool is dynamic. The detailed 2026-08-21 geometry handoff remains useful historical evidence, not a current MCP artifact.
- The 2026-08-09 probability handoff remains historical scenario evidence. A fresh `hoi4.probability_inspect` timed out after 600 seconds without an artifact or revision, so current probability status is blocked. Event inspect/render/compare and decision inspect likewise returned no current artifacts or revisions.
- The final localization handoff records 10,600 unique keys, no duplicates, UTF-8 BOM/CRLF, 159 report/news rewrites, three `.138` keys, 60 broad G3 rewrites, and 19 additional source-backed rewrites. One hundred initial G3 candidates have no consumers across 2,536 current source files and remain dormant; 232 other matches were reviewed and retained as in-world or grammatical. Color audit: zero keys. Its exact-key inventory and per-string before/after rationale cover all 159/60/19 changes.
- The required manifest `docs/assets/005_soviet_union_collapse/manifest.md` is absent from the current checkout; the replacement `docs/assets/005_soviet_collapse/` directory contains only `source_audio/`. Older documents claim the archive was deleted by commit `79bb425aa6`, but the parent's Git check reports an invalid commit object and no `git log --all --oneline` path history, so deletion and contents are unverified. The current animation evidence archive is also absent.
- The 2026-10-05 country and portrait audits verify 57 consumed runtime portrait files at 156x210: 56 new Event 005 portraits plus UWR's reused SOV Velikanov portrait. Source provenance remains unresolved: the portrait workspace has 23 PNGs and 66 identical generic prompt files, six PNGs are stale IDs, 15 active-ID PNGs match runtime pixels, and CFR/MFR do not. Six successor capital setup paths lack map confirmation (`IJX`, `INX`, `ANX`, `ABX`, `AEX`, `IMX`), and byte-identical flag variants remain undocumented for KMB, FEV, IJX, and AAX. These are provenance and verification risks, not confirmed runtime defects.
- Current source implements one `chaosx.nr5.95` internal-republic summary news event and one `chaosx.nr5.48` regional-faction growth news event per crisis, followed by local `chaosx.nr5.38` notices. `soviet_collapse_initialize_crisis_values` resets both global aggregation flags; exact source locations are in the implementation audit.
- `subagent_handoffs/2026_10_05_event005_popup_news_matrix.md` inventories all 21 direct news-event call sites in the event/effect/decision sources and records the parent-supplied opening popup counts; the full 43-tree chain remains source-only because event MCP rendering stalled.
- The parent applied the accepted Event Details body at `localisation/english/chaosx_gui_l_english.yml:693`; `Events!C6` remains queued. The USA GUI inspect/render had a generated-fixture transform and fidelity/click diagnostics. The artifact reader opened the Fury empty-details fixture, but it contains no Event 005 body; the populated Event Details before-render timed out after 600 seconds without a valid PNG. Exact fixture parameters and blockers are in the implementation audit.
- Final decision-cost handoff covers 12 cost surfaces and 13 decisions with aligned affordability/debits, emergency command power 60, at most three cost values, and 21 complete icon-first hover strings; scenario-level decision evidence remains unavailable.
- Audio provenance remains unresolved for wired IDs 14, 15, 17, and 18; IDs 16 and 19-22 are dormant. See the dated audio handoff.

- These findings do not promote any unaccepted plan or spec proposal. Preserve the user's 2026-10-05 authorization for Event 005 design rewrites as task scope, and record a specific acceptance basis before marking a proposed design accepted.

## Historical 2026-08-09 Reconciliation Snapshot

- The four active Event 005 focus files contain 43 trees and 1,760 focuses: 515 republic, 1,035 custom-splinter, 134 factory-successor, and 76 ancient-restoration focuses.
- The former 520 pathline heuristic and 1,127 helper-only or nearly helper-only reward counts are historical audit metrics, not active implementation blockers. The 2026-08-09 recursive reward audit checked all 1,760 completion rewards and reports zero semantic shallow-leaf risks.
- UWR and KMB package implementation is complete, including dedicated decisions, route-aware AI, conquered-basin and aftermath handling, and final focus, decision, idea, and UWR flag assets. The 2026-08-09 package and asset handoffs are current evidence.
- Successor Relations is implemented as three distinct post-collapse alignments: the Black International, Free Soviet Congress, and Iron Production Bloc. Their founding decisions, route-sensitive AI, faction creation and joining helpers, membership cleanup, and charter events `chaosx.nr5.33`, `chaosx.nr5.34`, and `chaosx.nr5.37` are current source, and the 2026-08-09 resolution handoff is authoritative.
- Event 005 workbook, event-detail, evolution-detail, and generated CSV wording parity is complete. The editable workbook remains the catalog source, and the 2026-08-09 parity handoff confirms the exports were regenerated without direct CSV edits.
- `events/005_soviet_collapse.txt` contains every requested Patron Rivalry ID from `chaosx.nr5.50` through `chaosx.nr5.70` and both Reconsolidation and Aftermath IDs `chaosx.nr5.96` and `chaosx.nr5.97`.
- The bounded Event 005 map inspection covered states 247, 569, 570, 571, 572, 578, 583, 585, 586, and 827 with no unknown province IDs, missing geometry, or state, region, adjacency, supply, or railway blockers. The global MCP run still reports 2,654 omitted diagnostics, consisting of 1,323 building-position and 1,331 port-adjacency findings for `floating_harbor` rows that match the installed vanilla rows exactly. These are validator false positives and not Event 005 map defects.
- Probability completion is resolved by `subagent_handoffs/2026_08_09_event005_probability_completion.md`. Decision AI, mission AI, every multi-option event pool, every `random_list` pool, and all 1,760 focus AI blocks were evaluated under explicit named scenarios with complete candidate pools and zero unresolved inputs.
- Events `chaosx.nr5.30`, `.31`, `.32`, `.33`, `.34`, `.35`, and `.37` use distinct `.a`, `.b`, and `.c` option identifiers, eliminating the former categorical-pool collision. Event `chaosx.nr5.96` sets exactly one aftermath flag before `.97`; focused MCP state-flow evidence confirms `.97` reads those three exclusive flags with zero blocking diagnostics, so no fallback option is required.
- Read-only MCP evidence is retained in the current map, event, focus, and probability handoffs. The terminal compact `hoi4.focus_rewrite` batch is deliberately reserved as the final source mutation after this documentation snapshot; only read-only post-rewrite inspection, rendering, probability evaluation, semantic-hash verification, staging, and commit may follow it.

## Historical 2026-07-11 Reconciliation

- The four active Event 005 focus files then contained 43 trees and 1,728 focuses. The 41-tree and 1,698-focus figures below describe the June 5 pre-UWR/KMB audit and are retained as historical audit evidence. The current package is 43 trees and 1,760 focuses.
- `common/decisions/005_soviet_collapse_decisions.txt` defines 118 numbered Soviet crisis missions, classified exactly once as 37 Chain of Command, 21 Corridors and Depots, and 60 Republic Settlement missions. The July 11 tranche preserves the existing board, cap, refill event, and release scheduler.
- `005_soviet_collapse_unconventional_warfare_republic.md` and `005_soviet_collapse_kuznetsk_mining_board.md` are later supplemental country-package specs. Their crisis hooks, route AI, package decisions, conquered-basin and aftermath outcomes, and bounded icon/flag outputs are recorded in 2026-08-09 handoffs. The 2026-10-05 audit leaves portrait provenance and overall asset evidence unresolved.
- `2026_07_11_soviet_collapse_improvement_loop_addendum.md` is implemented for Command and Corridors, Patron Rivalry, Reconsolidation and Aftermath, Successor Relations, and UWR/KMB completion. The current probability handoff closes its former probability boundary.
- The five-case selected-target lifecycle has one statically verified shared dynamic path covering base republics, Tajikistan, dynamic non-base republics, high-chaos successors, and a post-Union-Unmade target. Selection controls display only; substantive availability, cooldown preservation, resolution cleanup, and terminal conversion are documented in the July 11 lifecycle handoff. The stale empty-panel finding is closed without tag-specific exceptions.

## Historical 2026-08-05 Focus Selector Repair

- The regional focus loader now accepts the active Event 005 breakaway path only when `soviet_collapse_breakaway` is paired with `soviet_collapse_active_origin`, while retaining the `soviet_collapse_event_created_republic` guard.
- The nine regional tree selectors now use the same event-created or active-breakaway-origin contract, preventing the loader and tree headers from disagreeing about eligible countries.
- UWR, KMB, PRA, ILX, IKX, DSC, NRF, and ICD now require `soviet_collapse_high_chaos_successor` in their custom tree selectors.
- The seven case-colliding idea/focus localisation pairs in the custom splinter file now use explicit vanilla-style `text = <focus>_focus` keys, and the case-insensitive localisation audit reports zero duplicate keys.
- MCP re-rendered the changed UWR, generic breakaway, ILX, and NRF trees successfully with no render blockers; the changed custom file also returned `FOCUS_INSPECTED`.
- MCP map inspection resolved the twelve sampled successor setup state IDs. The older 2,654-error wording is superseded by the 2026-08-09 map resolution, which identifies the global findings as vanilla-identical `floating_harbor` false positives and leaves the scoped Event 005 consumers clean.
- This repair closed selector safety at that time. The 2026-08-09 focus-depth, final-icon, UWR/KMB package, and UWR flag handoffs supersede its active claims about reward depth, unique icons, country-package depth, and protected binary assets.

## Historical 2026-08-05 Country Package and Weighted Audit Repair

- UWR's Tver pathogen directorate, experiment-camp registry, and field-release focuses now unlock dedicated decisions in `soviet_collapse_uwr_blacksite_category`. The decisions reuse existing special-project, facility, payload, assault-column, expansion-claim, and crisis-pressure helpers, with centralized costs and existing decision icons.
- KMB's concession-treaty focus now unlocks `kmb_integrate_conquered_basin`. When KMB owns and controls states 570, 571, 572, and 578, the decision cores and improves the basin states, advances the existing resource-expansion programme, and raises depot control.
- The four ancient charter focuses now unlock `soviet_collapse_write_restored_charter`, which requires the existing Returned Names banner stage and seals the restoration through legal recognition, foreign-channel, and League-support effects.
- Route-specific AI strategy overlays now exist for the symbolic and expansionist routes of INX, SOG, ANX, and ABX. The strategy adapter was attempted after the patch but returned `PROBABILITY_SURFACE_EMPTY` for `common/ai_strategy/005_soviet_collapse.txt`, so no normalized strategy-factor or before/after comparison claim is made.
- The protected country-tag audit reports 136 Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions. The source-only repair itself created no flags, portraits, or binary assets, but the 2026-08-09 UWR flag and UWR/KMB final-icon handoffs now record the completed final asset package.
- Focus MCP spot checks after the package repair returned `FOCUS_INSPECTED` for NLC, CFR, and INX, while the prior UWR and KMB checks remain source-clean. The remaining diagnostics are the known vanilla continuous-focus palette errors and authored layout warnings, not missing Event 005 focus IDs, localisation, or icon definitions.
- The historical 1,728-focus probability snapshot covered complete candidate pools of 515 republic, 1,021 custom-splinter, 128 factory-successor, and 64 ancient focuses. Its partial evaluations are superseded by the current 1,760-focus scenario analyses, which declare actor tags, completed-focus state, scoped country checks, stability, global flags, custom wrappers, candidate ownership, and external factors explicitly and report zero unresolved inputs.
- The ancient national-focus sweep completed across three explicit prerequisite-multiplier states with zero unresolved inputs and one informational inactive-modifier diagnostic; artifact `probability-047328b6997b518558dcf0e7.json` is the authoritative sweep result.
- The post-change map inspection covered states 247, 569, 583, 585, 586, 827, 570, 571, 572, and 578 with no unknown province IDs or missing geometry. The 2026-08-09 map resolution confirms these Event 005 consumers are clean, while the global position/locator diagnostics are the known vanilla-identical `floating_harbor` false positives.
- Focused `hoi4.event_inspect` lint for `chaosx.nr5.1` returned `EVENT_INSPECTED_PARTIAL`, no blockers, and zero blocking diagnostics, while deferring the known workspace-wide helper and lifecycle projections.
- The required independent `chaosx_focus_tree_auditor` handoff could not initialize because the external `blender_hoi4` and `meshy` MCP servers timed out during `tools/list`; parent evidence remains the available audit record.
- The final layout rewrite gate was attempted after all source and evidence repairs. MCP rejected both the NLC compact proposal and the INX compact proposal, changed no files, and no unsafe coordinate edit was retained; NLC reduced crossings from 23 to 14 but increased node intersections from 16 to 18, while INX reduced crossings from 2 to 0 but introduced one node intersection and sibling-anchor regressions.

## Highest Authority

| Source | Use for | Notes |
| --- | --- | --- |
| `AGENTS.md` | Repository rules, no-fallback policy, validation and completion standards, no unsupported operators, required docs/references. | Always applies. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Subagent boundaries and handoff requirements. | Documentation curator may patch docs only. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_1_authority_completion.md` | Conflict resolution, completion contract, super-event scope, focus design stance. | Use as source design. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_2_core_threat_evolutions.md` | Core threat, event logs, evolution families, Union Unmade pacing. | Use as source design; check against current implementation handoffs before completion claims. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_3_decisions_missions_influence.md` | Decisions, missions, influence, balance rules. | Use for decision expansion and foreign patron work. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md` | Release model, local leagues, Union Unmade terminal logic. | Current accepted boundary: live releases are gradual and pressure-gated; terminal, maximum-intensity, and standalone chaos scenario paths can run all-possible release passes. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md` | Focus-tree route depth, reward quality, route visibility, completion proof. | The 2026-08-09 semantic reward audit remains historical evidence; the 2026-10-05 audit reports seven unresolved authored layouts and unresolved fallback-country eligibility. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md` | Country packages, high-chaos splinters, factory states, ancient restorations. | Use for remaining custom splinter, OGB, and ancient tree depth. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md` | Assets, achievements, super-events, final validation. | The 2026-08-09 asset handoffs are historical. The required asset manifest/source-evidence path is missing in the 2026-10-05 checkout. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_collapse_unconventional_warfare_republic.md` | Later UWR country package, special-project identity, compact focus surface, shared-crisis contamination hook, route AI, and aftermath. | Supplemental to core spec part 6. The package and final UWR flag/icon assets are implemented; use the 2026-08-09 handoffs for current evidence. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_collapse_kuznetsk_mining_board.md` | Later KMB country package, resource sovereignty, coal-golem, treaty/concession crisis hooks, reusable target gates, route AI, and conquered-basin outcomes. | Supplemental to core spec part 6. The package and final UWR/KMB icon assets are implemented; use the 2026-08-09 handoffs for current evidence. |

## Current Event Overview

| Source | Use for | Caveat |
| --- | --- | --- |
| `docs/events/005_soviet_collapse/overview.md` | Compact event overview, main systems, release behavior, focus reward policy, evolution families, and evidence links. | It now points to the 2026-10-05 audit; its 2026-08-09 claims are dated historical evidence, not current completion proof. |

## Current Working Ledgers

| Source | Use for | Notes |
| --- | --- | --- |
| `docs/plans/005_soviet_collapse_plans/documentation_state.md` | Current resumability ledger, accepted constraints, recent dispositions, contradictions, and next resume priorities. | Updated by documentation curator. |
| `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md` | This source map. | Updated by documentation curator. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md` | Historical full-event documentation cleanup handoff, validation, spreadsheet inspection notes, and remaining risks. | Superseded as the current ledger by this 2026-08-09 reconciliation. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_153830_documentation_curator_release_focus_resume.md` | Historical documentation-curator handoff for release/focus resume constraints and validation commands. | Retained for scoped historical notes, but its no-flag and focus-risk dispositions are superseded by the 2026-08-09 handoffs. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_current_state_handoff.md` | Historical documentation-curator validation and remaining parent decisions. | Retained as historical evidence. |
| `docs/plans/005_soviet_collapse_plans/2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Implemented Command and Corridors loop, selected-target lifecycle, release-cause inheritance, Patron Rivalry, Reconsolidation and Aftermath, UWR/KMB completion, Successor Relations, and explicit anti-bloat boundaries. | Its former probability boundary is closed by the 2026-08-09 probability handoff. |
| Six July 11 implementation and audit handoffs under `subagent_handoffs/` | Backend ownership, first-pass blocker audit, selected-target/UWR/KMB audit, lifecycle corrections, final completion audit, and localisation audit. | Historical evidence for the implemented bounded systems, not a full Event 005 completion claim. |

## Doc Disposition Summary

### Accepted Current Docs

| Source | Why accepted |
| --- | --- |
| `docs/events/005_soviet_collapse/overview.md` | Current compact overview and completion boundary. It is a summary, not a blanket deletion of older evidence. |
| `docs/plans/005_soviet_collapse_plans/implementation_audit_2026-10-05.md` | Current 2026-10-05 source, audit, and route-status report. |
| `docs/events/005_soviet_collapse/patron_rivalry_and_reconsolidation.md` | Current implementation note for Patron Rivalry and Reconsolidation and Aftermath. It records that no further implementation is required for these chains. |
| `docs/plans/005_soviet_collapse_plans/documentation_state.md` | Current resume/status packet, accepted constraints, known contradictions, completed design labels, and terminal rewrite boundary. |
| `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md` | Current documentation routing map. |
| Nine core and supplemental files under `docs/specs/005_soviet_collapse_specs/` | Source design and final completion standards, including the UWR and KMB supplements, reconciled against current implementation handoffs. |
| `docs/plans/005_soviet_collapse_plans/2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Implemented source for Command and Corridors, Patron Rivalry, Reconsolidation and Aftermath, and UWR/KMB completion. |

### Historical Docs And Evidence

| Source | Retained use |
| --- | --- |
| `2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` | Historical focus-design evidence. The current 43-tree package and zero semantic shallow-leaf risk are implemented; retain this plan for provenance and any separately chosen visual-layout work. |
| `subagent_handoffs/2026_08_09_event005_probability_completion.md` | Historical probability evidence for decisions, missions, event options, random lists, and focus AI blocks. Current revalidation is blocked by the 2026-10-05 timeout recorded in the implementation audit. |

### Superseded Current-State Findings

| Source | Superseded finding |
| --- | --- |
| `2026_05_28_decision_release_focus_reward_fix.md` | Early low-threat release-floor wording is superseded by June 5 live-pressure release gating. |
| `2026_06_04_focus_tree_auditor_all_soviet_collapse_audit.md` | Coordinate and route-lock specifics are superseded by June 5 patches and the post-CFR audit. |
| `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md` | Ukraine/Belarus route-lock finding is superseded by `2026_06_05_parent_ukraine_belarus_route_lock_tranche.md`; use the newer post-CFR audit for the current focus baseline. |
| `2026_06_05_145453_focus_tree_audit.md` | Its exact BLR coordinate, BLR/KAZ/GAC pathline, and broad starting-tension cleanup findings are superseded by later parent patches. Its helper-generic and shallow-tree findings are historical evidence, while current semantic reward depth is resolved and any authored-layout work is separately scoped. |

### Known Contradictions To Preserve Or Resolve

| Subject | Current resolution |
| --- | --- |
| Active releases versus terminal release | Live crisis releases are gradual and pressure-gated. Terminal, maximum-intensity, and standalone chaos scenario rupture paths can run exhaustive release passes. |
| Completion claims | Event005 is incomplete. The 2026-10-05 implementation audit records seven authored focus-layout failures, unresolved fallback eligibility, blocked current probability/event/decision MCP evidence, unresolved portrait/flag provenance and map checks, and a missing required asset manifest/source-evidence path. The report/news and three linked focus-description localization edits are complete for their audited scope; older package-completion wording is historical. |
| Former focus-risk counts | The 520 pathline heuristic and 1,127 shallow-reward count remain historical metrics. The 2026-08-09 semantic reward audit does not establish current visual layout completion; the 2026-10-05 audit reports seven unresolved layouts. |
| Flag requirements versus active no-touch scope | The 2026-08-09 UWR flag and UWR/KMB icon handoffs remain historical runtime-asset evidence. The required general Event 005 manifest and source-evidence path is missing in the 2026-10-05 checkout, so overall asset documentation is unresolved. |
| Workbook and CSV parity | The former parity backlog is resolved by the 2026-08-09 workbook/export handoff, which confirms exact Event 005 wording parity and regenerated CSV exports. |
| Event 005 map diagnostics | Event 005 state consumers are clean. The remaining global count of 2,654 is explained by vanilla-identical `floating_harbor` rows that the MCP validator misclassifies. |
| Patron Rivalry and Reconsolidation | Earlier docs queued these chains, but the current source contains events `chaosx.nr5.50` through `chaosx.nr5.70` and `chaosx.nr5.96` through `chaosx.nr5.97`, and their implementation handoff is current. |
| Successor Relations | The former queued label is implemented through the Black International, Free Soviet Congress, and Iron Production Bloc decisions, helpers, membership lifecycle, and charter events `chaosx.nr5.33`, `chaosx.nr5.34`, and `chaosx.nr5.37`. |
| Local event probability versus overall probability | The 2026-08-09 probability handoff records scenario results for its then-current source. A fresh probability inspection timed out after 600 seconds without a current artifact or revision, so current probability completion is unresolved. |
| Existing-country and fallback focus-tree eligibility | Named regional selectors and the `soviet_collapse_event_created_republic` gate have historical source evidence. The 2026-10-05 focus audit leaves the eligible dynamic release-pool tags for `soviet_collapse_breakaway_focus_tree` unresolved; no exact eligible-tag list or current MCP artifact was returned. |
| Invalid-SOV root dispatch | `chaosx.nr5.1` now routes missing, capitulated, or state-less SOV to `chaosx.nr5.138`; the event and localization keys are present. This is a narrow repair, not full event completion. |
| Event and decision MCP coverage | Fresh event inspect/render/compare and decision inspect calls stalled without artifacts or revisions. | Blocked; source review is not equivalent engine evidence. |
| Localization | The final handoff records 10,600 unique keys, no duplicates, BOM/CRLF, 159 report/news rewrites, `.138` keys, 60 broad G3 rewrites, and 19 additional source-backed rewrites. One hundred initial G3 candidates had no consumers across 2,536 current source files and remain dormant; 232 other matches were reviewed and retained as in-world or grammatical. | Implemented for the audited scope; the full key inventory and per-string before/after rationale are authoritative in `subagent_handoffs/2026_10_05_event005_report_news_prose_patch.md`. |
| Intervention visibility | The July 11 lifecycle audit closes the stale empty-panel contradiction across base, Tajikistan, dynamic non-base, high-chaos, and post-terminal targets. Shared substantive gates, cooldown-preserving display, and symmetric cleanup are authoritative; no tag exception was added. |

## Recent Handoffs To Trust For Current State

| Source | Trust for | Supersedes or modifies |
| --- | --- | --- |
| `subagent_handoffs/2026_10_05_event005_docs_reconciliation.md` | Current documentation dispositions, focus/country asset risks, and MCP blockers. | Reconciles the 2026-08-09/2026-08-21 snapshots against the fresh 2026-10-05 reports; it does not supersede source design or establish game behavior. |
| `subagent_handoffs/2026_10_05_event005_report_news_prose_patch.md` | Final static report/news localization coverage, new `.138` keys, three updated focus descriptions, and zero-color result. | Completes the earlier 25-key patch, resolves all 26 additional candidates, and supersedes the handoff's earlier pending concerns. |
| `subagent_handoffs/2026_06_05_parent_dynamic_nonbase_release_gate_handoff.md` | Active preterminal non-base and pressure-successor release gating. | Supersedes older low-threat/floor release wording. |
| `subagent_handoffs/2026_06_05_parent_dynamic_release_pressure_and_focus_cleanup_visibility.md` | High-chaos pressure-successor burst budgets and hidden focus-helper cleanup. | Complements dynamic non-base gate handoff. |
| `subagent_handoffs/2026_06_05_parent_focus_helper_spam_cleanup_tranche.md` | Narrow PRA duplicate-helper cleanup and Ukraine League tooltip cleanup. | Historical evidence for a partial cleanup; the broad helper-only reward interpretation is superseded by the 2026-08-09 recursive semantic audit. |
| `subagent_handoffs/2026_06_05_parent_focus_cleanup_layout_dsc_aggression_tranche.md` | Tag-specific starting-tension cleanup, named BLR/KAZ/GAC pathline fixes, DSC aggression payoffs. | Supersedes matching findings from `2026_06_05_145453_focus_tree_audit.md`. |
| `subagent_handoffs/2026_06_05_parent_ukraine_belarus_route_lock_tranche.md` | Ukraine and Belarus route locks and visible route-row signaling. | Supersedes route-lock findings in `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md`. |
| `subagent_handoffs/2026_06_05_parent_cfr_construction_focus_depth_tranche.md` | Latest CFR construction-directorate focus-depth work and validation. | Supersedes older CFR shallow-opening audit findings, but only for the scoped CFR tranche. |
| `subagent_handoffs/2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` | Full pre-UWR/KMB post-CFR audit baseline: 41 trees, 1698 focuses, 0 duplicate focus IDs, 0 coordinate duplicates, 0 direct focus idea effects, 520 pathline risks, and 1,127 helper-only or nearly helper-only reward findings. | Historical risk baseline. The 520 and 1,127 metrics are superseded by the 2026-08-09 recursive audit, which reports zero semantic shallow-leaf risks across the current 1,760 focuses. |
| `subagent_handoffs/20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md` | Earlier full mechanical focus audit count baseline. | Superseded as current focus baseline by the post-CFR audit, but useful for comparing route-lock and pre-CFR state. |
| `subagent_handoffs/2026_06_05_145453_focus_tree_audit.md` | Helper-heavy reward, cloned splinter scaffold, compact high-chaos/ancient depth concerns. | Its exact BLR coordinate, BLR/KAZ/GAC pathline, broad starting-tension cleanup, helper-generic reward, and shallow-tree findings are superseded by later source and recursive audit evidence. |
| `subagent_handoffs/2026_07_11_soviet_command_corridors_backend_handoff.md` | Mission classification, priority/refill integration, state-bound corridors, compromises, release causes, terminal desks, and UWR/KMB hooks. | Backend implementation evidence for tranche one. |
| `subagent_handoffs/2026_07_11_soviet_command_corridors_audit.md` | First-pass risks and blocker findings. | Superseded where the lifecycle patch and final audits record corrections; retain as audit history. |
| `subagent_handoffs/2026_07_11_soviet_selected_target_uwr_kmb_audit.md` | Selected-target, terminal conversion, UWR, KMB, and AI review. | Modified by the lifecycle correction handoff and final audits. |
| `subagent_handoffs/2026_07_11_soviet_selected_target_lifecycle_handoff.md` | Five-case shared lifecycle, substantive gates, cooldown preservation, invalidation cleanup, release-cause ordering, and sponsor AI. | Current selected-target and lifecycle evidence. |
| `subagent_handoffs/2026_07_11_soviet_command_corridors_completion_audit.md` | Final bounded gameplay audit and correction disposition. | Current completion evidence for tranche one only. |
| `subagent_handoffs/2026_07_11_soviet_localisation_audit.md` | Player-facing key coverage, tooltip accuracy, category state, and localisation encoding. | Current localisation evidence for tranche one only. |
| `subagent_handoffs/2026_08_09_event005_focus_depth_reward_resolution.md` | Historical 43-tree/1,760-focus package count, recursive reward audit, zero semantic shallow-leaf risks, and icon review. | Historical semantic evidence; the 2026-10-05 audit separately reports seven incomplete authored layouts. |
| `subagent_handoffs/2026_08_09_event005_final_focus_icon_handoff.md` | Historical unique focus-icon assignments and 43-tree contact-sheet review. | Runtime icon evidence is historical; current portrait/asset provenance remains unresolved. |
| `subagent_handoffs/2026_08_09_uwr_kmb_followup_package_resolution.md` | Implemented UWR/KMB package decisions, route AI, aftermath, and conquered-basin outcomes. | Supersedes the queued UWR/KMB implementation claims. |
| `subagent_handoffs/2026_08_09_uwr_kmb_final_icon_asset_handoff.md` | Bounded UWR/KMB focus, decision, and idea icon handoff. | Historical runtime icon evidence; overall asset provenance remains unresolved. |
| `subagent_handoffs/2026_08_09_uwr_final_flag_asset_handoff.md` | UWR flag family handoff at runtime sizes. | Historical runtime flag evidence; provenance and broader asset coverage remain unresolved. |
| `subagent_handoffs/2026_08_09_parent_spreadsheet_parity_resolution.md` | Exact workbook, event-detail, evolution-detail, and CSV parity. | Supersedes the queued parity claim. |
| `subagent_handoffs/2026_08_09_parent_global_map_position_diagnostic_resolution.md` | Clean Event 005 state consumers and the vanilla-identical `floating_harbor` explanation for the global diagnostic count. | Supersedes the active Event 005 map-position blocker claim. |
| `subagent_handoffs/2026_08_09_patron_rivalry_reconsolidation_resolution.md` | Implemented Patron Rivalry events 50-70 and Reconsolidation/Aftermath events 96-97, with no further implementation required for those chains. | Supersedes the former later-tranche claim; the complete probability handoff supersedes its narrower local evidence. |
| `subagent_handoffs/2026_08_09_successor_relations_resolution.md` | Implemented Black International, Free Soviet Congress, and Iron Production Bloc founding decisions, faction helpers, membership cleanup, route-aware AI, and charter events 33, 34, and 37. | Supersedes the queued Successor Relations design label. |

## Historical Plans And Audits

| Source | Current use |
| --- | --- |
| `2026_05_28_decision_release_focus_reward_fix.md` | Historical evidence for decision economy, League deployment decisions, and earlier release-floor approach. Do not use its low-threat release-floor wording as current release design; June 5 gates require gradual dynamic release pressure. |
| `2026_05_28_foreign_influence_and_idea_consolidation.md` | Current design reference for consolidated external support and sponsor influence; scripted GUI sponsor bars are an unaccepted optional concept, not queued Event005 work. |
| `2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` | Historical focus-design plan. The 2026-08-09 semantic reward audit remains historical evidence; seven authored layouts and fallback eligibility remain unresolved in the 2026-10-05 audit. |
| `2026_05_31_parent_focus_release_analysis.md` | Historical parent analysis. Use its remaining-work themes, not its older counts as current facts. |
| `2026_06_05_parent_dynamic_release_pacing_and_idea_cleanup_followup.md` | Current evidence that active non-base release pacing is pressure-gated and standalone triggerable scenarios keep exhaustive all-possible behavior. Do not read as a general all-release-off or all-release-instant rule. |
| `2026_06_04_focus_tree_auditor_all_soviet_collapse_audit.md` | Historical audit. Newer June 5 audits and patches replace its coordinate and route-lock specifics. |
| `2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Implemented for its scoped Command and Corridors, Patron Rivalry, Reconsolidation and Aftermath, UWR/KMB, and Successor Relations tranches. Its historical probability-completion wording does not close current MCP blockers. |

## Documentation-Curator Boundary

- `gfx/flags`
- flag sprite files
- route flags
- ideology flag variants
- assets and binary images
- gameplay files
- localisation files
- script, focus, decision, event, GUI, GFX, history, AI, spreadsheet, or asset edits by the documentation curator

The gameplay, localisation, script, focus, decision, event, GUI, history, AI, spreadsheet, and asset bullets above describe the documentation curator's ownership boundary. Runtime assets remain unchanged by this documentation pass; the required Event 005 manifest/source-evidence path is currently unresolved.

## Terminal Action And Tool-Coverage Notes

- The prior snapshot proposed a compact `hoi4.focus_rewrite` batch across 43 trees, but the 2026-10-05 focus audit still reports seven authored-layout failures. The rewrite has no retained proof of completion; exact layout repair and post-change MCP evidence remain unresolved.
- The 2026-08-09 probability handoff contains historical scenario evaluations. The fresh `hoi4.probability_inspect` timeout prevents a current claim that the AI-strategy, focus, decision, mission, event-option, and random-list surfaces were revalidated.
- The `event_mean_time_to_happen` adapter correctly reports no event `mean_time_to_happen` block for the named reusable definitions in `common/mtth/005_soviet_collapse_mtth.txt`; this is not a partial evaluation.
- Dynamic release gates continue to depend on live crisis state, and initial divisions continue to scale from current territorial and industrial strength.
- The named-tree event-created gates retain their historical source evidence. The dynamic eligibility of tags that fall through to `soviet_collapse_breakaway_focus_tree` remains unresolved.
