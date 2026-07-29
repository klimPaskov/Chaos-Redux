# Event005 Source Of Truth Map

Date: 2026-07-11
Scope: Event005 Soviet Collapse documentation, specs, plans, and handoffs.

This map tells the next parent agent which documents to trust first. It does not claim Event005 completion.

## 2026-07-11 Reconciliation

- The four active Event 005 focus files now contain 43 trees and 1,728 focuses. The 41-tree and 1,698-focus figures below describe the June 5 pre-UWR/KMB audit and are retained as historical audit evidence.
- `common/decisions/005_soviet_collapse_decisions.txt` defines 118 numbered Soviet crisis missions, classified exactly once as 37 Chain of Command, 21 Corridors and Depots, and 60 Republic Settlement missions. The July 11 tranche preserves the existing board, cap, refill event, and release scheduler.
- `005_soviet_collapse_unconventional_warfare_republic.md` and `005_soviet_collapse_kuznetsk_mining_board.md` are later supplemental country-package specs. Their shared crisis hooks and route AI are implemented, while their full decision, aftermath, treaty-competition, conquered-basin, and asset packages remain queued with core spec part 6.
- `2026_07_11_soviet_collapse_improvement_loop_addendum.md` is implemented for Command and Corridors and statically audited against its bounded acceptance scenarios. It does not supersede the partially implemented May 29 focus backlog and is not full Event 005 completion evidence.
- The five-case selected-target lifecycle has one statically verified shared dynamic path covering base republics, Tajikistan, dynamic non-base republics, high-chaos successors, and a post-Union-Unmade target. Selection controls display only; substantive availability, cooldown preservation, resolution cleanup, and terminal conversion are documented in the July 11 lifecycle handoff. The stale empty-panel finding is closed without tag-specific exceptions.

## Highest Authority

| Source | Use for | Notes |
| --- | --- | --- |
| `AGENTS.md` | Repository rules, no-fallback policy, validation and completion standards, no unsupported operators, required docs/references. | Always applies. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Subagent boundaries and handoff requirements. | Documentation curator may patch docs only. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_1_authority_completion.md` | Conflict resolution, completion contract, super-event scope, focus design stance. | Use as source design. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_2_core_threat_evolutions.md` | Core threat, event logs, evolution families, Union Unmade pacing. | Use as source design; check against current implementation handoffs before completion claims. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_3_decisions_missions_influence.md` | Decisions, missions, influence, balance rules. | Use for decision expansion and foreign patron work. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md` | Release model, local leagues, Union Unmade terminal logic. | Current accepted boundary: live releases are gradual and pressure-gated; terminal, maximum-intensity, and standalone chaos scenario paths can run all-possible release passes. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md` | Focus-tree route depth, reward quality, route visibility, completion proof. | Active focus work is not complete. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md` | Country packages, high-chaos splinters, factory states, ancient restorations. | Use for remaining custom splinter, OGB, and ancient tree depth. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md` | Assets, achievements, super-events, final validation. | Asset/flag requirements are no-touch future scope under the current parent correction. Do not route active Event005 cleanup into flags. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_collapse_unconventional_warfare_republic.md` | Later UWR country package, special-project identity, compact focus surface, shared-crisis contamination hook, and route AI. | Supplemental to core spec part 6. Shared hooks are implemented; dedicated decisions, conqueror aftermath, and final asset parity remain queued. |
| `docs/specs/005_soviet_collapse_specs/005_soviet_collapse_kuznetsk_mining_board.md` | Later KMB country package, resource sovereignty, coal-golem, treaty/concession crisis hooks, reusable target gates, and route AI. | Supplemental to core spec part 6. Shared hooks are implemented; treaty competition, conquered-basin depth, and final assets remain queued. |

## Current Event Overview

| Source | Use for | Caveat |
| --- | --- | --- |
| `docs/events/005_soviet_collapse/overview.md` | Compact current event overview, main systems, release behavior, focus reward policy, evolution families, current priority. | Do not treat as a final completion report. It now records gradual active releases, terminal/max release boundaries, standalone scenarios, pending evolution-detail parity, and no active flag work. |

## Current Working Ledgers

| Source | Use for | Notes |
| --- | --- | --- |
| `docs/plans/005_soviet_collapse_plans/documentation_state.md` | Current resumability ledger, accepted constraints, recent dispositions, contradictions, and next resume priorities. | Updated by documentation curator. |
| `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md` | This source map. | Updated by documentation curator. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md` | Full-event documentation cleanup handoff, validation, spreadsheet inspection notes, and remaining risks. | Latest documentation-curator handoff for this broad cleanup pass. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_153830_documentation_curator_release_focus_resume.md` | Documentation-curator handoff for release/focus resume constraints, no-flag boundary, and validation commands. | Superseded as latest curator handoff by the full-event cleanup handoff, but still valid for its scoped release/focus notes. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_current_state_handoff.md` | Documentation-curator validation and remaining parent decisions. | Created by documentation curator. |
| `docs/plans/005_soviet_collapse_plans/2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Implemented Command and Corridors loop, selected-target lifecycle, release-cause inheritance, UWR/KMB shared hooks, later aftermath tranches, and explicit anti-bloat boundaries. | Tranche one is implemented and audited. Later tranches and the May 29 focus backlog remain queued. |
| Six July 11 implementation and audit handoffs under `subagent_handoffs/` | Backend ownership, first-pass blocker audit, selected-target/UWR/KMB audit, lifecycle corrections, final completion audit, and localisation audit. | Current evidence for the bounded Command and Corridors tranche; none is a full Event 005 completion claim. |

## Doc Disposition Summary

### Accepted Current Docs

| Source | Why accepted |
| --- | --- |
| `docs/events/005_soviet_collapse/overview.md` | Current compact overview and urgent playability routing. It is a summary, not a completion report and not a blanket deletion of older evidence. |
| `docs/plans/005_soviet_collapse_plans/documentation_state.md` | Current resume/status packet, accepted constraints, known contradictions, queued work, and no-flag boundary. |
| `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md` | Current documentation routing map. |
| Nine core and supplemental files under `docs/specs/005_soviet_collapse_specs/` | Source design and final completion standards, including the UWR and KMB supplements, read through the current no-flag-touching boundary for urgent playability work. |
| `docs/plans/005_soviet_collapse_plans/2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Implemented source for the bounded Command and Corridors tranche and queued source for its later shared-mechanic tranches. |

### Queued Docs And Evidence

| Source | Queued use |
| --- | --- |
| `2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` | Focus-depth backlog. Some route-lock and CFR items are implemented; custom splinter identity, ancient restoration depth, OGB depth, helper-generic reward cleanup, and layout cleanup remain queued. |
| Later tranches in `2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Patron Rivalry, Successor Relations, Reconsolidation and Aftermath, and full UWR/KMB completion remain queued after the implemented Command and Corridors tranche. |
| `2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` | Current focus-risk baseline: 520 pathline risks and 1,127 helper-only or nearly helper-only reward findings remain queued for parent work. |
| Event-detail, evolution-detail, and spreadsheet parity notes | Queued until implementation facts are stable and wording can be mirrored exactly. XML inspection of `docs/spreadsheets/chaos_redux_events_catalog.xlsx` found Event005 row strings, but no safe workbook edit was made in this documentation pass. |
| Asset and flag requirements in spec part 7 | Final-validation scope only under the current correction. Do not route urgent playability work into flags or assets. |

### Superseded Current-State Findings

| Source | Superseded finding |
| --- | --- |
| `2026_05_28_decision_release_focus_reward_fix.md` | Early low-threat release-floor wording is superseded by June 5 live-pressure release gating. |
| `2026_06_04_focus_tree_auditor_all_soviet_collapse_audit.md` | Coordinate and route-lock specifics are superseded by June 5 patches and the post-CFR audit. |
| `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md` | Ukraine/Belarus route-lock finding is superseded by `2026_06_05_parent_ukraine_belarus_route_lock_tranche.md`; use the newer post-CFR audit for the current focus baseline. |
| `2026_06_05_145453_focus_tree_audit.md` | Its exact BLR coordinate, BLR/KAZ/GAC pathline, and broad starting-tension cleanup findings are superseded by later parent patches. Helper-generic reward and shallow-tree findings remain queued. |

### Known Contradictions To Preserve Or Resolve

| Subject | Current resolution |
| --- | --- |
| Active releases versus terminal release | Live crisis releases are gradual and pressure-gated. Terminal, maximum-intensity, and standalone chaos scenario rupture paths can run exhaustive release passes. |
| Completion claims | Event005 is not complete. Completed tranches, including CFR depth and route-lock cleanup, are not Event005 completion. |
| Flag requirements versus active no-touch scope | Final specs still require asset/flag validation, but the active user correction forbids touching flags and assets. Treat those requirements as future/final-validation scope. |
| Existing-country focus-tree eligibility | Event-created focus-tree loading appears gated by `soviet_collapse_event_created_republic`, but existing-country eligibility remains an urgent validation target before completion claims. |
| Intervention visibility | The July 11 lifecycle audit closes the stale empty-panel contradiction across base, Tajikistan, dynamic non-base, high-chaos, and post-terminal targets. Shared substantive gates, cooldown-preserving display, and symmetric cleanup are authoritative; no tag exception was added. |

## Recent Handoffs To Trust For Current State

| Source | Trust for | Supersedes or modifies |
| --- | --- | --- |
| `subagent_handoffs/2026_06_05_parent_dynamic_nonbase_release_gate_handoff.md` | Active preterminal non-base and pressure-successor release gating. | Supersedes older low-threat/floor release wording. |
| `subagent_handoffs/2026_06_05_parent_dynamic_release_pressure_and_focus_cleanup_visibility.md` | High-chaos pressure-successor burst budgets and hidden focus-helper cleanup. | Complements dynamic non-base gate handoff. |
| `subagent_handoffs/2026_06_05_parent_focus_helper_spam_cleanup_tranche.md` | Narrow PRA duplicate-helper cleanup and Ukraine League tooltip cleanup. | Confirms direct focus idea spam is cleaner, but broad helper-only reward cleanup remains queued. |
| `subagent_handoffs/2026_06_05_parent_focus_cleanup_layout_dsc_aggression_tranche.md` | Tag-specific starting-tension cleanup, named BLR/KAZ/GAC pathline fixes, DSC aggression payoffs. | Supersedes matching findings from `2026_06_05_145453_focus_tree_audit.md`. |
| `subagent_handoffs/2026_06_05_parent_ukraine_belarus_route_lock_tranche.md` | Ukraine and Belarus route locks and visible route-row signaling. | Supersedes route-lock findings in `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md`. |
| `subagent_handoffs/2026_06_05_parent_cfr_construction_focus_depth_tranche.md` | Latest CFR construction-directorate focus-depth work and validation. | Supersedes older CFR shallow-opening audit findings, but only for the scoped CFR tranche. |
| `subagent_handoffs/2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` | Full pre-UWR/KMB post-CFR audit baseline: 41 trees, 1698 focuses, 0 duplicate focus IDs, 0 coordinate duplicates, 0 direct focus idea effects, 520 pathline risks, and 1,127 helper-only or nearly helper-only reward findings. | Historical risk baseline. Current static counts are 43 trees and 1,728 focuses, so the old clean findings cannot prove the two later trees complete. |
| `subagent_handoffs/20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md` | Earlier full mechanical focus audit count baseline. | Superseded as current focus baseline by the post-CFR audit, but useful for comparing route-lock and pre-CFR state. |
| `subagent_handoffs/2026_06_05_145453_focus_tree_audit.md` | Helper-heavy reward, cloned splinter scaffold, compact high-chaos/ancient depth concerns. | Its exact BLR coordinate, BLR/KAZ/GAC pathline, and broad starting-tension cleanup findings are superseded by later parent patches. |
| `subagent_handoffs/2026_07_11_soviet_command_corridors_backend_handoff.md` | Mission classification, priority/refill integration, state-bound corridors, compromises, release causes, terminal desks, and UWR/KMB hooks. | Backend implementation evidence for tranche one. |
| `subagent_handoffs/2026_07_11_soviet_command_corridors_audit.md` | First-pass risks and blocker findings. | Superseded where the lifecycle patch and final audits record corrections; retain as audit history. |
| `subagent_handoffs/2026_07_11_soviet_selected_target_uwr_kmb_audit.md` | Selected-target, terminal conversion, UWR, KMB, and AI review. | Modified by the lifecycle correction handoff and final audits. |
| `subagent_handoffs/2026_07_11_soviet_selected_target_lifecycle_handoff.md` | Five-case shared lifecycle, substantive gates, cooldown preservation, invalidation cleanup, release-cause ordering, and sponsor AI. | Current selected-target and lifecycle evidence. |
| `subagent_handoffs/2026_07_11_soviet_command_corridors_completion_audit.md` | Final bounded gameplay audit and correction disposition. | Current completion evidence for tranche one only. |
| `subagent_handoffs/2026_07_11_soviet_localisation_audit.md` | Player-facing key coverage, tooltip accuracy, category state, and localisation encoding. | Current localisation evidence for tranche one only. |

## Historical Plans And Audits

| Source | Current use |
| --- | --- |
| `2026_05_28_decision_release_focus_reward_fix.md` | Historical evidence for decision economy, League deployment decisions, and earlier release-floor approach. Do not use its low-threat release-floor wording as current release design; June 5 gates require gradual dynamic release pressure. |
| `2026_05_28_foreign_influence_and_idea_consolidation.md` | Current design reference for consolidated external support and sponsor influence; future scripted GUI bars remain queued. |
| `2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` | Backlog for focus depth. Some route-lock/CFR items are implemented; custom splinter, ancient, OGB, and broad reward-depth work remain queued. |
| `2026_05_31_parent_focus_release_analysis.md` | Historical parent analysis. Use its remaining-work themes, not its older counts as current facts. |
| `2026_06_05_parent_dynamic_release_pacing_and_idea_cleanup_followup.md` | Current evidence that active non-base release pacing is pressure-gated and standalone triggerable scenarios keep exhaustive all-possible behavior. Do not read as a general all-release-off or all-release-instant rule. |
| `2026_06_04_focus_tree_auditor_all_soviet_collapse_audit.md` | Historical audit. Newer June 5 audits and patches replace its coordinate and route-lock specifics. |
| `2026_07_11_soviet_collapse_improvement_loop_addendum.md` | Implemented for Command and Corridors. Use its later-tranche sections as queued design, not as proof that Patron Rivalry, Successor Relations, Reconsolidation, or full UWR/KMB completion exists. |

## Documentation-Curator Boundary And Remaining Asset Scope

- `gfx/flags`
- flag sprite files
- route flags
- ideology flag variants
- assets and binary images
- gameplay files
- localisation files
- script, focus, decision, event, GUI, GFX, history, AI, spreadsheet, or asset edits by the documentation curator

The gameplay, localisation, script, focus, decision, event, GUI, history, AI, spreadsheet, and related editing bullets above describe the documentation curator's ownership boundary, not the completed Command and Corridors integration. The flag and binary-asset bullets remain the active asset boundary. Future asset work can return to spec part 7 only after the parent explicitly reopens it.

## Active Unresolved Implementation Items

- Gradual release pacing still needs proof across calm, high-pressure, chaos-tier, terminal, and maximum-intensity scenario starts.
- Dynamic release gates must keep extra non-base releases dependent on live crisis state, not static one-shot logic.
- Stronger republic initial divisions must remain dynamically scaled and need validation against large and small release candidates.
- Focus trees still need broad cleanup: political, industry, expansion branches; compact layouts; no overlapping lines; fewer pointless mutexes; no idea spam; and meaningful mechanics or regional payoffs.
- Evolution details remain pending and must match spreadsheet descriptions exactly after implementation facts are finalized.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` still contains Event005 wording that should be reviewed by the spreadsheet doc worker after gameplay facts settle. The row includes `To Be Reworked` status text and evolution wording that may need to mirror the current two-family event-log design exactly.
- Patron Rivalry, Successor Relations, Reconsolidation and Aftermath, and full UWR/KMB completion remain queued as later shared-mechanic tranches.
- UWR and KMB shared-crisis hooks and AI are reconciled; dedicated UWR decisions/conqueror aftermath and KMB treaty competition/conquered-basin policy remain incomplete. Their later compact trees raise the current static baseline to 43 trees and 1,728 focuses.
- Existing-country focus-tree eligibility remains an urgent validation target. Runtime focus-tree replacement must stay limited to Event005-created republics unless an explicit additive integration is designed.
