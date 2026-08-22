# Event 011 Secret Alliance documentation curator handoff

Date: 2026-07-10

## Scope and current verdict

This pass reconciles Event 011 implementation documentation through engine-compatible gameplay commit `407b9a05eb7024dd1728c4092fba2f1162efde9c`, atop high-impact balance freeze `1c87d9235319781c871c2948813ab55693eb8618`, lifecycle commit `a1f47c0c`, callback isolation `7563648f`, and wording/catalog commit `97a2da80`. It does not replace the accepted five-part specification or change the workbook.

DM-15 through DM-20 are resolved, and the independent decision specialist returned CLEAN for the decision and mission surface. CA-01 through CA-13 are resolved on the completion-audit rescan. The final localisation and workbook audit is FINAL CLEAN, and the high-impact balance pass is frozen at `1c87d923`. The holistic verdict is now present at `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this curation handoff does not replace it.

## Implementation chronology

| Commit | Disposition |
| --- | --- |
| `abc70f55` | Causal gameplay closure added dynamic roster and sponsor gates, Evidence-aware AI, state-matched protection, stage-gated operation breadth, rare `chaosx.nr11.21`, Evolution III state outcomes, Preparedness-driven delayed calls, factual Resolve, role-front AI, broad hidden-state bands, Evidence-scaled preemption, conditional invitations, and the weakened reveal route. |
| `6a33976e` | First final reveal wording freeze for the attempted assassination and weakened super-event route. |
| `3a48a344` | Dynamic candidate capacity began counting valid human recruits without treating capacity as consent. |
| `690dae0e` | Reveal-time member casualty snapshots made war-burden Resolve count only Event 011 post-reveal casualties. |
| `a1f47c0c` | Main lifecycle closure resolved DM-15 through DM-20 and CA-01 through CA-13, including presentation snapshots, direct-AI ownership, GUI border-pair reconciliation, and automatic-only history. |
| `7563648f` | Counted `.50` delayed-call and `.51` through `.53` commitment callbacks, released annexed owners, and completed automatic/manual relaunch isolation. |
| `97a2da80` | Finalized Event 011 and achievement wording and synchronized the catalog workbook. |
| `1c87d923` | Froze high-impact dynamic costs, one protection and one emergency slot, longer mission and commitment durations, 65 percent preemption, 120/180/120-day AI cooldowns, and a 730-day retained-counterintelligence ceiling. |
| `407b9a05` | Replaced eight unsupported country-tension trigger calls and moved 39 unchanged idea values into file-local constants accepted by the idea database. |

## Source-of-truth map

| Question | Current authority | Use |
| --- | --- | --- |
| Accepted design and completion boundary | `docs/specs/011_secret_alliance_specs/specs/` parts 1-5 | Historical source design and required behavior. The design remains authoritative where it does not conflict with verified engine constraints or the accepted later SCN-009 direction. |
| Detailed accepted design maps | `docs/specs/011_secret_alliance_specs/matrices/` | Event chain, decisions, missions, AI, tuning, assets, and achievement intent. |
| Final gameplay behavior | Event 011 gameplay files at `407b9a05` | Authoritative for implemented facts. SHA-256 prefixes are recorded below. |
| Final balance behavior | Event 011 tuning at `1c87d923` | Authoritative for the high-impact values retained by the compatibility correction. |
| Current mechanic overview | `docs/events/011_secret_alliance/overview.md` | Canonical implementation summary and file map. |
| Improvement-loop closure | `docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_resolution.md` | Itemized disposition of tranches A-G, mandatory architecture carryover, and all seventeen acceptance scenarios. |
| Holistic completion evidence | `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md` | Final static verdict, CA and DM disposition, frozen hashes, assets, audio, achievements, workbook, and plan disposition. |
| Source-package audit chronology | `docs/specs/011_secret_alliance_specs/handoffs/completion_audit.md` | Historical source-package audit reconciled to the final freeze. |
| Super-event text and sources | `docs/super_events/011_secret_alliance/research.md` | Slot `73`, five route packages, durable presentation context, quote, remark, image, and audio map. |
| Historical super-event research | `subagent_handoffs/super_event_text_research.md` | Preserves candidate selection and sourcing while marking superseded wording and wiring notes as chronology. |
| Assets | `docs/assets/011_secret_alliance/asset_register.md`, `manifest.md`, `manifest_icons_ui_animation.md`, and `notes/validation.md` | Final paths, sprites, source ledgers, animation frames, 57-DDS validator, achievement triplets, and explicit `chaosx.nr11.21` art reuse. |
| Achievements | `docs/achievements/011_secret_alliance/achievements.md` and live definitions | Six implemented achievement contracts with origin and anti-farming snapshots. |
| Manual scenario | `docs/systems/event_system/triggerable_scenarios.md`, accepted spec part 4, and live SCN-009 implementation | Five AI-only compositions, four intensities, manual bypasses, retained safety gates, and workbook status. |
| Workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | SHA-256 `597E71A1307958135BA1B34A8E60741320CD9E2753FA2EBDDBC1ED83403E1D59`; `Events!M12` and `Scenarios!F9` are `Implemented`; no formula error cells or formula error tokens. |
| Audio | `docs/super_events/super_event_audio_packages.md` and `subagent_handoffs/super_event_audio_research.md` | Audio ID `43`, final `Revelation` WAV, exact duration `86.101746` seconds, 44.1 kHz, and separate public-domain evidence for the composition and federal-government recording. |

## Immutable audit hashes

| Surface | SHA-256 prefix |
| --- | --- |
| Decisions | `B22CC92A` |
| Script constants | `2A635EE5` |
| Scripted effects | `10B03E94` |
| Scripted triggers | `A228DC3B` |
| Ideas | `D9C0C4D8` |
| MTTH | `8CE980BF` |
| Scripted localisation | `51F25FE3` |
| Events | `02046301` |
| Event 011 localisation | `6A42CEFE` |
| Achievement localisation | `6EE16E2B` |
| Scripted GUI | `C07907E2` |

## Current implementation facts promoted into documentation

- Automatic and scenario relaunches require counted `.50` delayed-call callbacks, counted `.51` through `.53` commitment callbacks, and pending `.190`, `.201`, and `.202` callback state to drain. Annexation releases a delayed-call owner's pending slot. Each callback family owns explicit pending state and its required target or owner.
- Delayed `.4` and `.5` notices require the exact target and current evolution phase. Invitations and sponsor approaches require their live pending transaction, watchdog, and notification scope.
- Automatic Event Log names and details use durable target-owned coordinated-interference and public-reveal history flags. Scenario, debug, forced, and AI-test origins do not create automatic-run history or normal-route achievement credit.
- The reveal presentation snapshots route, target, leader, member count, and faction-name grammar. News and super-event localisation use the presentation scopes and `GetSecretAlliancePresentationFactionName`, not live runtime faction state.
- Super-event slot `73` remains visible for 14 days. Hidden `.202` closes the slot, audio identity, and presentation context on day 15, or lifecycle invalidation closes them earlier.
- The direct AI controller uniquely owns eight protection projects, Turn Member, and three wartime actions. Engine weights are blocked for those actions. The controller uses exact state selectors and applies 120-day protection, 180-day Turn Member, and 120-day wartime cooldowns.
- Live family caps are two investigations, one protection, one diplomacy, one offensive action, one border action, and one emergency commitment. Mission timeouts are 150/135/190/150/190/100/140 days. Retained counterintelligence is capped at 730 days.
- The maximum live mixed capacity profile uses scale `2.2425`. Its rounded 168 PP maximum is covered by a 170 PP AI planning hint. Preemption requires 65 percent War Support and spends 15, 10, or 6 percent according to Evidence. No repeat-use cost multiplier remains.
- Scripted-GUI suspect selection and clearing refresh the exact suspect-bound border pair and cannot change it during an unresolved conflict. The border route pays only after a valid pair exists and the crossing mission receives its reinforced-patrol completion state.
- Route-aware reveal leadership excludes planned exiters. Wartime fractures perform white peace, faction exit, active-member removal, and outcome counting.
- Preemption preserves turned, delayed, and fractured planned-route outcomes. A hostile-war reveal force-calls every valid active member.
- The weakened and fractured reveal routes each have explicit presentation text. Sponsor Accountability is per-run rather than permanent history.
- All six achievement packages, five SCN-009 scenario compositions, four scenario intensities, eight authored animation frames plus static fallback, and 57 runtime DDS targets remain wired.

## Audit disposition

| Finding range | Current disposition |
| --- | --- |
| DM-15 through DM-20 | Resolved and preserved through `407b9a05`: public-war-start gating, mission-aware phase cleanup, current suspect-bound border pairs, valid envoy objective state, revealed cost refresh, and exact AI protection-state selection. |
| CA-01 through CA-13 | Resolved and preserved through `407b9a05`: leader and exit validity, exact border transaction, repeat-turn guard, preemption handling, fractured wording, pending-transaction safety, delayed-event gates, origin-safe achievements and Event Log, durable presentation context, per-run Sponsor Accountability, and counted callback draining through `.50` to `.53`, `.190`, `.201`, and `.202`. |
| Holistic completion verdict | Owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this scoped documentation pass does not replace it. |

## Plan and handoff dispositions

| Document | Disposition | Current use |
| --- | --- | --- |
| `011_secret_alliance_improvement_addendum.md` | Folded and historical | Accepted design was promoted into the five-part spec. Its no-scenario direction was superseded by the later accepted SCN-009 design. |
| `011_secret_alliance_implementation_improvement_addendum.md` | Accepted and fully disposed | No mandatory item remains queued. |
| `011_secret_alliance_improvement_resolution.md` | Current mandatory-plan closure | Closes the addendum, not the whole event. |
| `011_secret_alliance_high_impact_balance.md` | Implemented final balance plan | Frozen at `1c87d923`; no balance item remains queued. |
| `011_secret_alliance_decision_mission_handoff.md` | Superseded historical planning | The final decision matrix, scoped audit, and holistic audit replace its proposed caps, durations, and implementation instructions. |
| `011_secret_alliance_scripted_system_architecture.md` | Superseded historical planning | The promoted architecture pass and frozen runtime replace its early no-scenario and pending-implementation state. |
| `011_secret_alliance_super_event_text_research.md` | Superseded candidate | Luke 8:17 and `In battalions.` remain rejected candidate history. |
| `subagent_handoffs/repo_explorer_implementation_map.md` | Superseded historical scout | Its provisional file map and required actions describe pre-implementation chronology. |
| `subagent_handoffs/scripted_system_architecture_pass.md` | Promoted architecture history | Its ownership and safety model remains useful, while provisional-file findings are resolved. |
| `subagent_handoffs/improvement_loop_implementation_pass.md` | Implemented historical handoff | Its accepted gap is closed by the implementation addendum and resolution. |
| `subagent_handoffs/super_event_text_research.md` | Promoted and reconciled | Sun Tzu and Artemidorus sourcing remains valid; four-route and live-faction wording is superseded by the five-package presentation-snapshot implementation. |
| `subagent_handoffs/super_event_audio_research.md` | Promoted and resolved | Final files, audio ID, duration, source, and rights are implemented. Old wiring instructions are historical. |
| `subagent_handoffs/decision_mission_audit.md` | Historical CLEAN scoped freeze | Its `b7965b7e` verdict and earlier findings are valuable causal evidence. Final gameplay facts and the holistic verdict are owned by the `407b9a05` completion audit. |
| `subagent_handoffs/localisation_audit.md` | Current FINAL CLEAN report | Preserves `087d66ab` as historical chronology and confirms that `407b9a05` leaves localisation `6A42CEFE`, achievement localisation `6EE16E2B`, and workbook `597E71A1` unchanged. |
| `subagent_handoffs/completion_audit.md` | Current holistic verdict | Created as the final evidence-backed report and source-of-truth verdict owner named by the documentation map. |
| Source-package handoffs under `docs/specs/011_secret_alliance_specs/handoffs/` | Reconciled implementation records | Planning-era pending statements are superseded, while source-design chronology is preserved. |

## Contradictions and stale-instruction closure

- Runtime and documentation now agree on two investigation slots, one protection slot, and one emergency slot.
- Runtime and documentation now agree on the 65 percent preemption gate, 15/10/6 percent strain bands, 8 percent false-case Stability cost, 120/180/120-day direct-AI cooldowns, exact mission timeouts, and the 730-day aftermath ceiling.
- The cost model no longer claims a repeat-use multiplier. It records capacity, action-family, resource, and Evidence scaling, including mixed-profile scale `2.2425` and the 170 PP AI hint.
- Current authority identifies compatibility commit `407b9a05`, balance freeze `1c87d923`, and the matching final hashes.
- The missing plan-level holistic completion report now exists and every current source-of-truth map points to it.
- Source-package prompts are marked fulfilled. Planning manifests and reading inventories are marked historical so their original hashes, catalog statuses, and work orders cannot be mistaken for current state.
- Asset and super-event facts remain intact. The original 165.746939-second audio source duration is intentional source evidence, while the final derivative duration remains 86.101746 seconds.

No contradiction or parent decision remains open. Historical uses of `provisional` are confined to documents explicitly marked as pre-implementation chronology.

## Files changed by this curation pass

- `docs/assets/011_secret_alliance/asset_register.md`
- `docs/assets/011_secret_alliance/manifest.md`
- `docs/assets/011_secret_alliance/notes/validation.md`
- `docs/events/011_secret_alliance/overview.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_decision_mission_handoff.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_high_impact_balance.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_implementation_improvement_addendum.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_resolution.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_scripted_system_architecture.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/decision_mission_audit.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/documentation_curator_handoff.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/improvement_loop_implementation_pass.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/localisation_audit.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/repo_explorer_implementation_map.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/scripted_system_architecture_pass.md`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_text_research.md`
- `docs/specs/011_secret_alliance_specs/README.md`
- `docs/specs/011_secret_alliance_specs/handoffs/asset_routing_handoff.md`
- `docs/specs/011_secret_alliance_specs/handoffs/completion_audit.md`
- `docs/specs/011_secret_alliance_specs/handoffs/decision_mission_audit_handoff.md`
- `docs/specs/011_secret_alliance_specs/handoffs/documentation_state.md`
- `docs/specs/011_secret_alliance_specs/handoffs/improvement_loop_closure.md`
- `docs/specs/011_secret_alliance_specs/handoffs/localisation_audit_handoff.md`
- `docs/specs/011_secret_alliance_specs/handoffs/repo_explorer_style_handoff.md`
- `docs/specs/011_secret_alliance_specs/handoffs/scripted_system_architecture_plan.md`
- `docs/specs/011_secret_alliance_specs/handoffs/spreadsheet_handoff.md`
- `docs/specs/011_secret_alliance_specs/handoffs/subagent_role_application.md`
- `docs/specs/011_secret_alliance_specs/manifest.md`
- `docs/specs/011_secret_alliance_specs/matrices/011_secret_alliance_decision_mission_matrix.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_achievement_prompt.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_asset_prompt.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_coding_prompt.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_decision_mission_prompt.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_goal_prompt.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_super_event_prompt.md`
- `docs/specs/011_secret_alliance_specs/research/011_secret_alliance_super_event_text_research.md`
- `docs/specs/011_secret_alliance_specs/source_inventory.md`
- `docs/super_events/011_secret_alliance/research.md`

No gameplay, localisation, scripted localisation, GUI, GFX, visual asset, audio file, workbook, binary, achievement definition, scenario implementation, or five-part source specification was edited. No commit was created.

## Remaining issues

No documentation blocker, unresolved accepted plan, stale current audit owner, fallback, omitted route, or scope reduction remains. Optional future ideas remain outside the accepted completion boundary.

The documentation evidence is static. An in-engine playtest is outside this pass and is not claimed.
