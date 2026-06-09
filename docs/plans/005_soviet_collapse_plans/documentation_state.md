# Event005 Documentation State

Date: 2026-06-05
Role: `chaosx_documentation_curator`
Scope: documentation-only current-state ledger for Event005 Soviet Collapse.

This file is a resumability aid, not an Event005 completion claim. Event005 remains incomplete.

## Current Resume State

- Latest reliable event overview: `docs/events/005_soviet_collapse.md`, after the June 5 documentation-curator update that records gradual active-crisis releases, terminal/max exhaustive-release boundaries, standalone triggerable scenarios, pending evolution-detail parity, and the no-flag boundary.
- Source design remains the seven files under `docs/specs/005_soviet_collapse_specs/`.
- Working implementation evidence remains in `docs/plans/005_soviet_collapse_plans/` and `docs/plans/005_soviet_collapse_plans/subagent_handoffs/`.
- Flags and flag assets are out of scope for the active parent task. Do not edit `gfx/flags`, flag GFX, route flags, ideology flags, or other assets until the parent explicitly reopens asset work.
- The latest completed CFR evidence found by this curator is `subagent_handoffs/2026_06_05_parent_cfr_construction_focus_depth_tranche.md`; it records validation and no flag edits. Treat CFR depth as a completed tranche, not as Event005 completion.
- The latest focus audit evidence found by this curator is `subagent_handoffs/2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md`. It keeps the 41-tree/1698-focus mechanical baseline, reports 0 duplicate IDs and 0 coordinate duplicates after one CFR coordinate patch, and still reports 520 pathline risks plus 1,127 helper-only or nearly helper-only reward findings.

## Urgent Playability Resume Packet

The active parent priority is urgent playability, not final Event005 completion. Resume in this order unless the user redirects:

1. Release pacing and scenario sanity: preserve gradual live-crisis releases, keep non-base releases tied to live pressure, and keep standalone triggerable scenarios separate from unrelated live-crisis settings.
2. Union Unmade sanity: keep terminal and maximum-intensity paths exhaustive enough to rupture the former Union, while ordinary monthly progression stays pressure-gated.
3. Focus-tree layout cleanup: prioritize visible line/path clutter, compact branch organization, route-row clarity, and the remaining 520 pathline-risk baseline from the post-CFR audit.
4. Focus reward quality: reduce helper-only or nearly helper-only rewards with mechanics, decisions, war goals, cores, units, templates, factions, state work, or regional interactions; do not claim broad focus completion while the 1,127 shallow-reward baseline remains unresolved.
5. Intervention visibility: fix selected-breakaway intervention panels dynamically so Tajikistan-style targets do not reveal an empty panel. Do not use hardcoded tag lists.
6. Existing-country focus-tree eligibility: preserve the `soviet_collapse_event_created_republic` gating pattern for runtime focus-tree loading. Existing countries with meaningful trees should receive crisis integration or additive hooks, not blind focus-tree replacement.
7. No flag touching: do not edit `gfx/flags`, flag sprites, flag files, flag interface entries, route flags, ideology flag assets, or other asset files unless the user explicitly reopens that scope.

## Accepted Current Constraints

- Event005 is not complete.
- Active Soviet Collapse releases must be gradual. Calm worlds release only the base Soviet republics. Higher dynamic release pressure and chaos tiers unlock vanilla regional republics. Chaos tier and above can unlock custom chaos/special splinters. Terminal or maximum-intensity paths can release all possible former-Union candidates.
- Extra releases beyond base republics must depend on live dynamic state such as Union Collapse Threat, progressive release pressure, failed-objective pressure, regional cascade pressure, war pressure, severe component pressure, urgency, or chaos-tier pressure. Do not describe or implement them as a static one-shot release.
- Triggerable Soviet Collapse scenarios are standalone starts. They must not inherit unrelated live-crisis settings.
- Stronger republics should spawn with more initial divisions through dynamic scaling from controlled states, civilian factories, military factories, existing divisions, chaos, war pressure, depot access, foreign access, and terminal/scenario intensity.
- Focus trees remain under cleanup. Required direction: clear political, industry, and expansion branches; compact layouts; no overlapping lines; fewer pointless mutual exclusions; no idea spam; and meaningful decisions, war goals, cores, units, templates, factions, or regional-interaction rewards.
- Evolution-detail and event-detail wording remains pending. It must match the spreadsheet descriptions exactly after implementation facts are finalized.
- The selected-breakaway intervention visibility bug remains a dynamic-system priority. Showing breakaway decisions must not expose an empty intervention panel for dynamic tags such as Tajikistan, and the fix must not use hardcoded tag lists.
- Runtime focus-tree replacement must stay event-created-gated. Current script evidence uses `soviet_collapse_event_created_republic` in Event005 focus-tree country blocks and loader paths, but existing-country eligibility still needs playability validation before this can be treated as done.
- Flag and flag-asset work is closed for the current task. If older docs require flag work, treat that requirement as future/no-touch scope until the parent explicitly reopens it.

## Current Implementation Facts From Recent Handoffs

| Area | Current evidence | State |
| --- | --- | --- |
| Focus-tree mechanical baseline | `2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` parsed 41 trees, 1698 focuses, 0 duplicate focus IDs, 0 coordinate duplicates, 0 missing/recursive relative positions, 0 parent-at/below-child issues, 0 continuous-panel risks, 0 direct focus idea effects, and 0 unsupported `<=`/`>=` operators. | Latest post-CFR audit baseline. It made one bounded CFR coordinate patch before recording the final numbers. |
| Focus-tree remaining risks | `2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` reports 520 pathline-through-focus heuristic risks and 1,127 helper-only or nearly helper-only reward findings, led by custom splinters, republics, and MFR. | Queued/in progress. No focus-tree completion claim is supported. |
| Ukraine and Belarus route locks | `2026_06_05_parent_ukraine_belarus_route_lock_tranche.md` added route-completed triggers and adjacent visible mutual-exclusion links. | Implemented tranche. Broader Ukraine/Belarus depth remains queued. |
| BLR/KAZ/GAC pathline cleanup and DSC aggression | `2026_06_05_parent_focus_cleanup_layout_dsc_aggression_tranche.md` fixed named pathline clutter and made broad starting-tension cleanup tag-specific. | Implemented tranche. Broader helper-heavy reward design remains queued. |
| Dynamic non-base release gating | `2026_06_05_parent_dynamic_nonbase_release_gate_handoff.md` tightened preterminal non-base and pressure-successor release gates around live crisis pressure. | Implemented tranche for active crisis gates. Terminal, maximum-intensity, and standalone chaos-scenario paths remain the exhaustive rupture paths. |
| Dynamic release pressure budgets and focus helper visibility | `2026_06_05_parent_dynamic_release_pressure_and_focus_cleanup_visibility.md` raised high-chaos pressure-successor budgets while preserving pressure gates and hid internal helper calls in focus rewards. | Implemented tranche. |
| CFR construction depth | `2026_06_05_parent_cfr_construction_focus_depth_tranche.md` adds early CFR map-visible construction payloads, new scripted effects, decision visibility fixes, and localisation. | Implemented tranche. Event005 still incomplete. |
| Focus helper spam cleanup | `2026_06_05_parent_focus_helper_spam_cleanup_tranche.md` removed one PRA duplicate helper call and hid noisy shared helper payloads behind bespoke Ukraine League tooltips. | Implemented narrow tranche. The broad helper-only reward problem remains queued. |
| Evolution detail parity | `docs/events/005_soviet_collapse.md` records that event-detail/evolution body text must match the spreadsheet after implementation facts are finalized, but that parity is not yet proven. XML inspection of `docs/spreadsheets/chaos_redux_events_catalog.xlsx` found Event005 row strings, including `To Be Reworked` status text. | In progress unless a later spreadsheet/event-detail completion handoff is produced. |
| Triggerable scenarios | `2026_05_31_parent_focus_release_analysis.md`, `2026_06_04_parent_release_pacing_tranche.md`, and later release handoffs describe standalone scenario suppression, exhaustive scenario release passes, and scaled opening forces. | In progress; docs must keep scenario starts separate from unrelated live-crisis settings. |
| Existing-country focus-tree eligibility | Current script evidence shows Event005 runtime focus-tree country blocks and loader paths using `soviet_collapse_event_created_republic`; see `common/national_focus/005_soviet_collapse_republics.txt` and `common/scripted_effects/005_soviet_collapse_effects.txt` read-only inspection. | In progress. Validate that existing republic tags are not overwritten unless Event005 actually created them. |
| Dynamic decision expansion and visibility | Recent handoffs cover foreign selected-target robustness and CFR/DSC/PRA decision hooks, but no final all-decision expansion audit was found. The known Tajikistan-style empty-panel bug remains a dynamic visibility priority. | In progress. Do not solve with hardcoded tag lists. |
| Focus depth and cleanup | Many tranches are implemented, but audits still cite generic helper rewards, cloned splinter scaffolds, shallow compact/ancient trees, and route-depth gaps. | Queued/in progress. |

## Recent Plan And Handoff Disposition

| File | Disposition | Evidence |
| --- | --- | --- |
| `2026_05_28_decision_release_focus_reward_fix.md` | Partially superseded | Early release-floor and low-threat wording is superseded by later dynamic live-pressure gating. League deployment and emergency mobilization notes remain historical implementation evidence. |
| `2026_05_28_foreign_influence_and_idea_consolidation.md` | Implemented with future extension queued | Current event overview describes selected patron desks, expanded target normalization, and consolidated external support. Scripted GUI sponsor bars remain a future extension. |
| `2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md` | Partially implemented, mostly queued | Ukraine/Belarus route locks and CFR depth have later implemented tranches. Custom splinter identity, ancient restoration depth, OGB depth, and broad reward cleanup remain queued. |
| `2026_05_31_parent_focus_release_analysis.md` | Partially implemented and partly superseded | Later handoffs implement several release/focus fixes. Remaining work section still matches current queued focus-depth work, but counts/layout specifics are superseded by June 5 audits. |
| `2026_06_04_focus_tree_auditor_all_soviet_collapse_audit.md` | Superseded as current audit baseline | Later June 5 audits and parent patches replace its coordinate/route-lock findings. Keep as historical evidence of earlier broad focus-quality concerns. |
| `2026_06_05_parent_dynamic_release_pacing_and_idea_cleanup_followup.md` | Implemented and clarified by current accepted constraints | Use it as evidence that active non-base releases are pressure-gated and that standalone triggerable scenarios keep exhaustive all-possible behavior. Do not read it as permission for static or instant live-crisis release sweeps. |
| `2026_06_05_141828_parent_focus_release_layout_depth_tranche.md` | Implemented and partly superseded | Later focus audit was collected, then later parent handoffs addressed route locks and CFR depth. |
| `2026_06_05_parent_dynamic_release_focus_layout_followup.md` | Implemented, release-gate note partly superseded | Its focus layout changes stand. Its "no release-script change" note is superseded by the later dynamic non-base release gate handoff. |
| `2026_06_05_parent_dynamic_nonbase_release_gate_handoff.md` | Implemented | Current evidence for active preterminal non-base and pressure-successor gates. |
| `2026_06_05_parent_focus_reward_idea_spam_helper_cleanup.md` | Implemented | Current evidence that PRA/DSC focus helper calls no longer add those national spirits; remaining helper-generic rewards are queued. |
| `2026_06_05_parent_dynamic_release_pressure_and_focus_cleanup_visibility.md` | Implemented | Current evidence for pressure-successor burst budgets and hidden internal focus-helper cleanup. |
| `2026_06_05_145453_focus_tree_audit.md` | Partly superseded, partly queued | Its BLR coordinate collision and BLR/KAZ/GAC pathline findings were addressed later. Its helper-generic rewards, cloned splinter scaffolds, and shallow trees remain queued. |
| `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md` | Partly superseded current-state audit | Keep its 41-tree/1698-focus mechanical baseline. Its Ukraine/Belarus route-lock finding is superseded by `2026_06_05_parent_ukraine_belarus_route_lock_tranche.md`. |
| `2026_06_05_parent_focus_cleanup_layout_dsc_aggression_tranche.md` | Implemented | Current evidence for tag-specific starting-tension cleanup, BLR/KAZ/GAC pathline fixes, and two DSC aggression payoffs. |
| `2026_06_05_parent_ukraine_belarus_route_lock_tranche.md` | Implemented | Current evidence for Ukraine/Belarus route lock behavior. |
| `2026_06_05_parent_cfr_construction_focus_depth_tranche.md` | Implemented | Current evidence for latest CFR construction-directorate depth pass. |
| `2026_06_05_parent_focus_helper_spam_cleanup_tranche.md` | Implemented | Narrow evidence for PRA duplicate-helper cleanup and Ukraine League tooltip cleanup. Broad helper-only reward cleanup remains queued. |
| `2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` | Current audit baseline | Latest focus-tree count/risk baseline after the CFR tranche and one bounded CFR coordinate patch. |

## Contradictions And Stale Documentation To Resolve

| Subject | Evidence | Required parent decision |
| --- | --- | --- |
| Active release pacing versus terminal release | Older handoffs can sound like broad release is either fully removed or always exhaustive. The accepted current boundary is narrower: live crisis releases are staged and pressure-gated; terminal, maximum-intensity, and standalone chaos scenario paths can run all-possible release passes. | Keep this distinction in every future doc/spec/spreadsheet edit. |
| "All republics release instantly" risk | Current overview and recent gate handoffs say ordinary progression is staged and pressure-gated; older release-floor wording in `2026_05_28_decision_release_focus_reward_fix.md` is no longer the active release model. | Use staged, pressure-gated language for active crisis releases. Exhaustive release language belongs only to terminal, maximum-intensity, and standalone scenario rupture paths. |
| Flags and assets | Spec part 7 requires flag and route-flag asset coverage, but the active parent task explicitly forbids flag edits. | Treat asset/flag requirements as future scope only. Do not route active focus/release cleanup into flags. |
| Focus-tree completion | Spec part 5 defines focus completion proof, but recent audits and parent handoffs repeatedly say broad focus-depth work remains incomplete. | Do not claim focus-tree completion until a final full-tree audit clears route depth, reward depth, AI behavior, localisation, icons, and layout. |
| Evolution detail parity | Current overview and parent context both treat event-detail/evolution text parity as active work. | Require a later spreadsheet/event-detail handoff before marking this complete. |
| Triggerable scenario inheritance | Scenario docs can blur live-crisis and forced-scenario paths. | Record triggerable Soviet Collapse scenarios as standalone; they should not inherit unrelated crisis settings. |
| Selected-breakaway decision visibility | Prior handoffs improved selected-target visibility, but the current known bug says some tags such as Tajikistan can reveal no intervention decisions. | Keep the fix dynamic through selected-target/breakaway classification and targeted-decision scope handling. Do not hardcode tag lists. |
| Existing-country focus-tree replacement | The event skill warns against blind runtime focus-tree replacement for already-existing countries with meaningful trees. Current scripts appear to gate event-created trees through `soviet_collapse_event_created_republic`, but this is not yet a completed validation scenario. | Treat existing-country focus-tree eligibility as an urgent playability check before completion claims. |

## Next Resume Priorities

1. Continue release-pacing validation around gradual live releases, dynamic pressure gates, stronger-republic force scaling, and exhaustive terminal/max/scenario rupture paths.
2. Continue focus-depth tranches with the queued high-impact gaps: custom splinter bespoke openings, ancient restoration depth, OGB depth, compact high-chaos aggression, pathline cleanup, and helper-generic rewards.
3. Fix selected-breakaway intervention visibility dynamically, with the Tajikistan-style empty-panel case as a regression target and no hardcoded tag lists.
4. Validate existing-country focus-tree eligibility and ensure runtime focus-tree loads only apply to Event005-created republics unless a deliberate additive integration exists.
5. Produce a decision/evolution detail parity handoff before claiming the dynamic decision expansion or spreadsheet-aligned evolution detail work is complete.
6. Keep flag and asset work closed unless the parent explicitly reopens it.
