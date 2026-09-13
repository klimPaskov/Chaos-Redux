# Event 021 Random Civil War — Current Completion Audit — 2026-09-12

Audit mode: read-only completion audit against the current checkout.

Scope: Event 021, its Event 006 adapter and admitted 32-package matrix, the Wars-cluster Event 004/Event 007 precedents, SCN-018, AI and weighted logic, decisions and missions, Event Log and Event Details integration, assets, achievements, cleanup, catalogs, accepted plans, and required validation evidence.

No gameplay, localisation, workbook, asset, configuration, or existing report file was edited. This handoff is the audit's only repository write.

## Executive disposition

Event 021 is not complete. The checkout contains a large, coherent source implementation, the 2026-09-12 regional-exposure presentation-marker repair is present, Event 021-owned static assets resolve, the six achievements and their eighteen icon states exist, the authoritative workbook/CSV rows are current, and fresh event inspection/rendering was obtained at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`.

Completion is independently prevented by current source defects, unresolved design authority, missing specialist acceptance, incomplete Event 006 package/assets proof, partial MCP projections, unavailable changed-revision comparisons, incomplete probability evaluation, and absent engine/live/performance evidence. The fail-closed release state is therefore correct and must not be promoted.

The two highest-confidence current source defects are:

1. `random_civil_war_authority_is_collapsed` is unreachable for an initialized country. `common/scripted_triggers/021_random_civil_war_triggers.txt:331-346` first requires the authority variable not to exist and then compares that same variable. A live initialized country at authority 0–14 fails the first condition. This breaks the accepted Collapse band, its scripted-localisation branch at `common/scripted_localisation/021_random_civil_war_localisation.txt:23`, and any collapse-trigger consumers.
2. Event 021-created Event 006 actors cannot use the required full Event 006 player-facing national content. `common/scripted_triggers/006_independence_wave_triggers.txt:20-23` defines `is_independence_wave_event6_local_content_active` only for a real active Event 006 origin. Event 021 deliberately records an origin-neutral adapter at `common/scripted_effects/021_random_civil_war_parent_effects.txt:2867-2877,2957` and does not set `independence_wave_active_origin`. The shared focus selector at `common/national_focus/006_independence_wave_focus.txt:45`, decision categories beginning at `common/decisions/categories/006_independence_wave_categories.txt:10`, and package decisions beginning at `common/decisions/006_independence_wave_decisions.txt:44` depend on the closed local-content trigger. The internal package predicate at `common/scripted_triggers/006_independence_wave_triggers.txt:25-48` permits setup, but the explicit comments and player-surface predicate at lines 51-60 intentionally keep Event 006 player surfaces closed. This contradicts the accepted requirement to preserve the full Event 006 tree, decisions, formables, AI, and long-term package play.

## Authorities and references reviewed

The audit read and applied `AGENTS.md`, the complete Event 021 specification/prompt directory, Event 006 specifications and current completion evidence, and the repository skills `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and `chaos-redux-mtth`. The `xlsx` skill was used only to inspect the authoritative workbook without mutation.

The required offline wiki references were consulted from `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding. Installed vanilla documentation and source precedents were consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation` and the installed game tree, including event, effect, trigger, script-concept/script-constant, decision, focus, localisation, scope, on-action, idea, and AI behavior relevant to this audit. Key engine rules retained in the assessment include regular event-target lifetime, explicit global-event-target cleanup, `on_civil_war_end`/`on_civil_war_end_before_annexation` scopes, tag-scoped on-actions, documented dynamic-value limits, focus-tree assignment scoring, and civil-war focus inheritance/re-evaluation.

The Event 021 spec inventory consists of the README, compiled master, ten numbered parts, goal/coding and specialist prompts, event/story/decision/achievement/asset prompts, package/role/overlap/revision matrices, and every file under `subagent_prompts/`. The compiled master was treated as a convenience copy; the numbered parts and explicit prompts controlled where wording was more specific.

Spec integrity is stale: all 41 manifest entries exist, but `docs/specs/021_random_civil_war_specs/MANIFEST.sha256` mismatches two current files. `021_random_civil_war_overlap_and_catalog_reconciliation.md` currently hashes to `B32C8C8E63DEC3A87BBAF27AD558EBFA68328D024A2ED78AD6498C537A465534`, and `README.md` currently hashes to `E484A60B29BEBB08A649D54131312D52A78C3193A09508A13F655CE6E05CC88E`.

## Completion status by surface

| Surface | Status | Evidence and limit |
|---|---|---|
| Event identity, category, root, and disabled release state | Implemented in source; not released | `events/021_random_civil_war.txt:12-21` defines hidden triggered-only `chaosx.nr21.1`; the event catalog identifies Event 021 as Minor Repeatable, chaos tier 1, Wars/Medium. `common/scripted_triggers/021_random_civil_war_triggers.txt:150,198` requires `random_civil_war_rework_ready`; initialization clears it at `common/scripted_effects/021_random_civil_war_parent_effects.txt:27-39`, and no setter exists. |
| Event chain and callbacks | Substantial source implementation; MCP partial | Nineteen Event 021 events are defined and each has a current internal caller. The visible presentation family, hidden callbacks, no-target callback, and news entries are present in `events/021_random_civil_war.txt`. Fresh MCP evidence still expands zero helpers and defers lifecycle projection. |
| Target eligibility and universal exclusion | Implemented in source; runtime unverified | Normal targeting is fail-closed, requires a normal human country, excludes `is_actual_nonhuman_country`, and carries safety/route checks in `common/scripted_triggers/021_random_civil_war_triggers.txt:36-39,146-198`. No live candidate-pool proof exists. |
| Fracture Pressure | Implemented in source; probability/runtime partial | Hidden pressure inputs, bands, target score, and route modifiers exist across `common/script_constants/021_random_civil_war_constants.txt`, `common/scripted_triggers/021_random_civil_war_triggers.txt`, and `common/scripted_effects/021_random_civil_war_effects.txt`. Exact TGT scenario evaluation is missing. |
| State Authority | Partial; source defect | The variable, update effects, display, and accepted 70–100/40–69/15–39/0–14 bands exist, but the Collapse predicate is logically impossible for initialized state at `common/scripted_triggers/021_random_civil_war_triggers.txt:331-346`. |
| Six opening archetypes | Implemented in source; selection not accepted | Ideological uprising, rival legal government, regional secession, Event 006 actor, command schism, and same-tag paths have evidence/validity/selection helpers in `common/scripted_effects/021_random_civil_war_parent_effects.txt:847-1140`. Conditional ARC probabilities and live route viability are unresolved. |
| Severity | Source behavior implemented; design authority unresolved | `event021_prepare_opening_severity` is a deterministic ladder at `common/scripted_effects/021_random_civil_war_effects.txt:541-570`, with one-state routes forced Limited. `docs/plans/021_random_civil_war_plans/subagent_handoffs/improvement_loop_disposition_2026-09-06.md` leaves severity design unresolved, while `docs/021_random_civil_war/overview.md:94` says deterministic and line 326 describes a four-entry pool. This conflict blocks SEV acceptance. |
| Territory, connected regions, capital, and remnant | Implemented in source; engine behavior unverified | Dynamic connected-state planning, capital/remnant safeguards, validation, rollback, and same-tag fallback are implemented in `common/scripted_effects/021_random_civil_war_parent_effects.txt:1180-1620,3380-3483`. There is no engine-backed proof that every opening transfers a viable connected region and leaves a viable remnant. |
| Forces and stockpiles | Implemented in source; engine behavior unverified | Dynamic force/stockpile preparation and validation are present at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1390-1620`; no blind static half split was found. Unit allocation, equipment conservation, and rollback have no live receipt. |
| Leaders and actor identity | Partial | Ordinary actor and Event 006 package setup paths exist at `common/scripted_effects/021_random_civil_war_parent_effects.txt:2127-3380`. Duplicate-character/tag avoidance and all 32 admitted identities are not proven in engine, and the required country-package auditor handoff is absent. |
| Event 006 complete package reuse | Blocked by source and evidence | Setup adapters and a 32-package registry exist, but player-facing Event 006 content is gated off as described in the executive findings. The shared 184-focus tree itself passes current MCP structural inspection/rendering, so the blocker is actor eligibility and package integration rather than an absent tree. This violates `docs/specs/021_random_civil_war_specs/README.md:41`, `021_random_civil_war_goal_prompt.md:15`, `021_random_civil_war_country_package_matrix.md:11,75`, and the country-package auditor prompt's full-package requirement. |
| Event 006 state isolation | Implemented in source; runtime unverified | The adapter records Event 021 origin and avoids setting the Event 006 active-origin flag, firing/count/evolution state, and league enrollment. This preserves isolation but currently also closes required long-term package content. Live proof of no Event 006 weight/cap/evolution mutation is absent. |
| Event 006 32-package matrix | Source-attested only | The adapter registry contains exactly `iw_001, iw_002, iw_004, iw_006, iw_007, iw_008, iw_009, iw_010, iw_012, iw_014, iw_017, iw_018, iw_019, iw_023, iw_024, iw_026, iw_027, iw_028, iw_029, iw_030, iw_031, iw_033, iw_038, iw_040, iw_041, iw_044, iw_045, iw_070, iw_071, iw_072, iw_173, iw_184`. Current Event 006 audits classify these as content-attested, not engine-proven complete packages; Event 006 itself remains HOLD/PARTIAL. |
| Event 006 broader matrix | Out of Event 021 admission scope, but relevant dependency risk | Current Event 006 evidence reports 193 selectable rows, 32 content-attested rows, 29 compatible reservation groups, 40 adapters, and 161 unattested selectable rows. The 161-row backlog is not promoted into Event 021 scope; only the admitted 32 are required here. |
| Ordinary and regional claimants | Implemented in source; lifecycle partial | Ordinary civil war, temporary regional, command, legal, and same-tag setup/settlement paths exist. Existing national-content preservation, safe route blocking, and all successor transitions lack country-package/focus and live validation. |
| Normal decision category and phased presentation | Implemented in source; specialist acceptance missing | `common/decisions/021_random_civil_war_decisions.txt` contains 18 actions and three missions across government, opposition, Event 006 emergency, neighbor, settlement, and reconstruction phases. A static category picture/icon is wired. The mandated `decision_mission_auditor_handoff.md` does not exist. |
| Decision count, mission count, and costs | Source-conformant; balance/live unverified | Phase visibility is designed around three-to-five actions and one-to-three missions; no action was found spending more than four resource types. Costs use political power, command power, experience, manpower/equipment, factories/supply/diplomacy/unit commitment/state/time according to action. No live UI count, hidden-cost, stale-decision, free-unit-loop, or timeout proof exists. |
| Decision and mission AI | Implemented in source; weighted acceptance missing | Every current Event 021 action/mission has an AI block, and three missions have timeouts. Exact ranking, starvation, exploit, and state-transition results are unresolved. |
| Settlements, treaties, outcomes, and reconstruction | Implemented in source; engine/lifecycle unverified | Settlement selection, treaty/achievement callbacks, seven settlement families, reconstruction, successor, and cleanup helpers are present at `common/scripted_effects/021_random_civil_war_parent_effects.txt:3484-4547`. Separate-front resolution, actor death, annexation scopes, recurrence memory, and postwar content require engine proof. |
| Recurrence | Implemented in source; timing acceptance missing | Grace, memory, earliest/latest dates, recurrence targeting, and cleanup exist. REC scenarios and save/load timing have not been completed through the probability/runtime workflow. |
| Evolution I | Implemented in source; runtime unverified | Multi-front escalation, additional actors, major rarity gates, Event 006 fronts, independent settlements, and prevention/action hooks are present in parent helpers around `524-645` and `5309+`. Front validity, maximum concurrent fronts, and separate resolution lack live proof. |
| Evolution II | Implemented in source; current marker repair present | Neighbor exposure, military aid, separate relief, sponsor/mediator/containment hooks, border pressure, and rare strange incidents exist. The 2026-09-12 repair sets both `random_civil_war_exposure_active` and `random_civil_war_neighbor_exposure` at `common/scripted_effects/021_random_civil_war_effects.txt:966-983`; cleanup clears them at `common/scripted_effects/021_random_civil_war_parent_effects.txt:5604,5610`. Propagation and sponsor pools remain unverified. |
| Evolution III | Implemented in source; performance/lifecycle unverified | Stable/Exposed/Fractured/Critical state, persistent registry, critical queue, bounded cursor/budget/caps/nesting/generation, successors, reactions, and cleanup are implemented around `common/scripted_effects/021_random_civil_war_parent_effects.txt:348-517,4548-4905,5309-5632`. GLB sequence, starvation, save/load, and performance evidence are missing. |
| Bounded scheduler | Source-conformant; runtime unverified | The scheduler is bounded and driven through existing global-host cadence in `common/on_actions/chaosx_on_actions_chaos_meter.txt:32,55,79`, not a newly introduced all-country daily loop. Queue ordering, cumulative launch chance, and timing drift are unverified. |
| Wars cluster | Implemented in source; probability/runtime partial | Events 004, 007, and 021 are registered with danger, participation, reservation, collision, cooldown, skip, and pending metadata. Event 021 is Medium at `common/scripted_effects/chaosx_event_cluster_effects.txt:1345-1351`; cluster row identity is defined at `common/script_constants/chaosx_event_cluster_constants.txt:128-130`. CLU scenarios and one-pacing-event behavior are not engine-proven. |
| SCN-018 identity and four modes/intensities | Implemented in source/catalog; runtime unverified | The verified raw scenario ID is 18 at `common/script_constants/chaosx_triggerable_scenarios_constants.txt:32`; shared registration and launch exist at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:205,1334-1338`. Event 021 setup is in `common/scripted_effects/021_random_civil_war_parent_effects.txt:4738-5069`. Current catalogs call it `SCN-018: The Fracture Cascade`. |
| SCN-018 Maximum | Implemented in source; performance/live blocked | Maximum freezes and commits every currently eligible normal-human country at `common/scripted_effects/021_random_civil_war_parent_effects.txt:4933-4951`; lower intensities use weighted ticket pools. Setup is synchronous, so the measured-stall-only seven-day fallback is not active. There is no frame-time proof that immediate Maximum is acceptable, nor a live every-eligible-country receipt. |
| Eleven AI roles | Implemented in source; behavior unverified | `common/ai_strategy/021_random_civil_war_ai_strategy.txt:9-139` contains the eleven accepted role profiles; a global-prevention overlay begins at line 142. Role activation and behavior are not engine-proven. |
| Weighted/probability matrix | Blocked/partial | The accepted matrix covers TGT, ARC, SEV, EVO, FRT, SPN, STR, SET, REC, GLB, CLU, and SCN. The current mandated `chaosx_ai_probability_auditor` run did not return a final result or artifact: it remained `running` through repeated bounded waits, remained running after an explicit conclude request, and was closed in that state. The strongest dated evidence remains `docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_audit_2026-09-06.md`, which is source revision/hash stale and classifies every family as unresolved or score-only. |
| Event Log | Implemented in source/localisation; live UI unverified | Event-start, settlement, and evolution snapshots are called from parent helpers around `1910,1952,1997`; actor and result text is present in `localisation/english/021_random_civil_war_l_english.yml` and shared log/detail surfaces. Delivery, actor scoping, ordering, and save/load display are not live-proven. |
| Event Details and evolution details | Implemented in source/localisation/catalog; live UI unverified | Event Details and all three evolution descriptions are registered and match the authoritative catalog wording. The shared Event Details framework is not an Event 021-owned scripted GUI and therefore does not require `chaosx_event_ui_worker`; live rendering remains the user's validation domain. |
| Localisation and player-facing writing | Broadly implemented; final acceptance partial | Event, news, decisions, missions, ideas, authority/pressure bands, Event Log, Event Details, evolutions, scenario, cluster, achievements, and asset labels are present. The collapse-band trigger defect makes one accepted player-facing state unreachable. A prior localisation handoff exists, but current engine display is unverified. |
| Event 021-owned static assets | Source/GFX complete; live consumer pending | `docs/assets/021_random_civil_war/manifest.md:5-7` records 40 references resolving; `interface/021_random_civil_war.gfx:13-173` wires report/news/category/decision/mission/idea/achievement assets. Source, processed, DDS, comparison, contact-sheet, and alpha-repair records exist. No live consumer screenshot/receipt exists. |
| Event 006 reused assets | Blocked | `docs/assets/021_random_civil_war/validation/reused_event006_asset_audit_2026-09-02.md:3-57` remains incomplete: all 32 admitted packages have unresolved portrait/flag/focus/idea/decision/formable/status-panel provenance or review coverage, ten admitted packages have no mod portrait row, 46 current portrait rows are review-pending, and ARX has orphaned portrait assets. RHI/BAY grounded portrait handoffs remain source-placeholder/promotion blocked; no replacement DDS evidence closes them. |
| Achievements | Implemented in source/assets; runtime unverified | Exactly six Event 021 achievements are defined at `common/achievements/chaos_redux_achievements.txt:713-808`, names/descriptions at `localisation/english/021_random_civil_war_l_english.yml:334-365`, and eighteen normal/grey/not-eligible sprites at `interface/021_random_civil_war.gfx:104-173`. Trigger firing, Event 006 milestones, lineage, and multiplayer/ironman behavior are unverified. |
| Custom scripted GUI | Not applicable by accepted design | The accepted design explicitly requires a normal decision category and forbids a dedicated scripted GUI. No Event 021-owned GUI was introduced. Consequently no `chaosx_event_ui_worker`, reference-image contract, GUI MCP comparison, or decision-layout-contract handoff is required. Shared Event Log, Event Details, settings, and super-event frameworks are expressly excluded from that worker route. |
| Animation, super-event, portrait, 3D model, unit audio, and counters | Not applicable by accepted design | The specs explicitly exclude animation, super-event, custom 3D, and Event 021-owned character portraits. Event 006-owned portraits/assets remain a reused-package dependency and are separately blocked as above. No custom-unit audio/counter gate is introduced by Event 021. |
| Documentation and catalog | Partial/stale | Current gameplay overview, acceptance evidence, source-of-truth map, repair ledger, asset manifests, and workbook rows exist. Several documents still describe old MCP revisions/hashes or conflicting severity behavior. Required final specialist handoffs remain absent. |
| Cleanup and save/load | Implemented in source; engine proof missing | Parent, actor, exposure, scheduler, settlement, event-target/flag/variable, and Event 006 adapter cleanup paths exist. `on_civil_war_end` precedents and cleanup helpers were inspected. No live win/loss/annexation/capitulation/peace/concurrent-front/save/reload matrix proves cleanup or idempotence. |
| Performance | Blocked | Static bounded-loop structure exists, but there is no measured one-frame SCN-018 Maximum result, global-registry cadence result, large Event 006 population result, or long-run queue/recurrence profile. |

## Requirement-by-requirement disposition

The following rows consolidate duplicate statements from the master, numbered parts, prompts, matrices, and subagent prompts. A row is only marked implemented where the current source directly establishes the behavior; that wording does not imply engine or live acceptance.

| Requirement family | Disposition | Current evidence or exact gap |
|---|---|---|
| Event 021 ID/name/root/category/chaos tier/Wars Medium/no target weight | Implemented in source/catalog | Root `chaosx.nr21.1`; workbook Event row 22 and cluster row 2 align. |
| Disabled until the complete package is accepted | Implemented | Release flag is cleared and never set; status remains Needs Testing. |
| Repeatable after grace and memory, not a one-off | Implemented in source; unverified | Recurrence dates/memory/cleanup exist; REC timing/save-load evidence missing. |
| Normal targets are eligible human countries; actual nonhuman countries are universally immune | Implemented in source; unverified | Trigger uses `is_actual_nonhuman_country`, not blanket `is_special_chaos_country`; no complete live pool. |
| Hidden Fracture Pressure with specified political, war, occupation, administration, regional, and military inputs | Implemented in source; probability partial | Inputs/score helpers exist; TGT scenarios incomplete. |
| Visible State Authority with Cohesive 70–100, Contested 40–69, Failing 15–39, Collapse 0–14 | Partial/defective | Value and upper bands exist; Collapse predicate is unreachable for initialized state. |
| Stable targets receive compact/limited crises; weak targets can receive severe crises | Source behavior present; design/runtime unresolved | Deterministic severity ladder exists, but severity authority conflicts and SEV scenarios are not evaluated. |
| Weighted target selection with cooldown, reservation, skip, and no-target behavior | Implemented in source; probability blocked | Pool and callback exist; exact TGT ranks/probabilities and collision outcomes absent. |
| Six opening actor families | Implemented in source; engine unverified | All six route helpers and dispatch branches exist. |
| Authentic leader/institution selection; no duplicate tag/character | Partial | Setup helpers exist; all identities and collisions lack country-package/live proof. |
| Connected support region, viable capital/supply, protected remnant, rollback | Implemented in source; engine unverified | Dynamic planner/validator/rollback exists; no complete state-transfer matrix. |
| Dynamic defecting forces, militia, and bounded stockpiles; no blind half split | Implemented in source; engine unverified | Dynamic allocation exists; conservation and unit validity unproven live. |
| One-state/all-island countries use a safe same-tag or limited route | Implemented in source; engine unverified | Same-tag branch and Limited severity override exist. |
| Complete Event 006 package may be created without Independence Wave firing | Partial/blocking defect | Setup can create origin-neutral adapter actors, but full player-facing package content is closed. |
| Reuse Event 006 carrier, identity, leaders, flags, tree, politics, ideas, forces, reinforcement, formables, decisions, AI, and assets | Incomplete | Setup receipts cover part of the package; focus/decision gate defect and reused-asset audit prevent completion. |
| Do not mark Event 006 fired, change weight/cap/evolutions, duplicate identity, create incomplete/nonhuman package, or auto-enroll league | Source-conformant; live unverified | Origin-neutral path and adapter gates avoid Event 006 lifecycle state; no live mutation/idempotence proof. |
| Existing human Event 006 countries remain eligible after grace | Implemented in trigger design; unverified | Actual-nonhuman exclusion is narrow; recurrence/live nested-crisis proof absent. |
| Event 006 actors keep package decisions; Event 021 adds emergency actions without erasing identity | Not implemented as accepted | Event 021 actions exist, but Event 006 local-content trigger closes the package decision surface. |
| Normal decision category, static picture, dynamic summary, one Authority value, three-to-five actions, one-to-three missions | Implemented in source/assets; live UI unverified | Category, picture, dynamic text, 18 phased actions, and 3 missions exist; specialist/live acceptance absent. |
| Each action spends no more than four resource types and has clear effects/tooltips | Source-conformant; specialist/live unverified | No over-four action found; no final decision auditor handoff. |
| Government, opposition, Event 006 emergency, neighbor, settlement, reconstruction phases | Implemented in source; specialist/live unverified | Phase entries exist; stale visibility/cleanup/exploit matrix missing. |
| Evolution I adds valid multi-front escalation, rare majors, Event 006 fronts, independent settlements | Implemented in source; runtime unverified | Helpers/caps/actions exist; no full front matrix or separate-resolution live proof. |
| Evolution II exposes neighbors; relief differs from military aid; sponsor/mediator/containment play; rare strange incidents | Implemented in source; weighted/runtime partial | Marker repair is present; SPN/STR pools and live propagation unresolved. |
| Evolution III creates nonterminal country bands and bounded global scheduling with caps/nesting/generation | Implemented in source; sequence/performance unverified | Registry/queue/cursor/budget/caps exist; GLB evidence absent. |
| Wars cluster includes Events 004/007/021, one pacing event, reservations/collisions/skip reasons | Implemented in source/catalog; probability/runtime partial | Registry and fresh partial precedent graphs exist; CLU scenarios and pacing behavior unproven. |
| The Fracture Cascade uses verified free SCN-018 and four types/four intensities | Implemented in source/catalog; runtime unverified | ID 18 and setup helpers exist; SCN analysis/live completion missing. |
| Maximum commits every eligible normal-human country | Implemented in source; live/performance blocked | Frozen eligible-pool commit exists; no realized-country or frame-time evidence. |
| Immediate scenario setup; seven-day deterministic fallback only after measured stall | Implemented as immediate source path; acceptance blocked | No fallback is active, but no measured performance evidence establishes whether immediate setup is acceptable. |
| Eleven named AI roles and package-specific Event 006 behavior | Implemented in source; behavior unverified | Eleven profiles exist; Event 006 content gate prevents the accepted full package behavior. |
| Probability matrices TGT/ARC/SEV/EVO/FRT/SPN/STR/SET/REC/GLB/CLU/SCN | Incomplete/blocked | Dated partial source inspections exist; no current complete scenarios, normalized outcomes, or same-scenario changed-revision compare. |
| Events/news use concise, actor-aware presentation and hidden callbacks | Implemented in source/localisation; live unverified | Visible `.2-.9`, hidden `.10-.17`, and news `.211-.212` exist; display and delivery not tested live. |
| Event Log actor mapping, result snapshots, skip/failure reasons | Implemented in source/localisation; live unverified | Snapshot effects and actor/result text exist; live ordering/scopes absent. |
| Event Details plus Evolution I/II/III details align with catalog | Implemented in source/workbook; live unverified | Current workbook and CSV wording aligns; UI consumer proof absent. |
| Six exact achievements with three icon states each | Implemented in source/assets; runtime unverified | Six definitions, exact localisation, and eighteen sprites exist. |
| Static asset family has source/processed/DDS/GFX/manifest/comparison evidence | Implemented for Event 021-owned assets; live pending | Forty GFX textures resolve; alpha repairs are disclosed fallbacks; no live consumer receipt. |
| Event 006 identity assets remain Event 006-owned and complete for admitted packages | Blocked | Reused Event 006 audit remains incomplete for all 32 admitted packages. |
| No dedicated scripted GUI, animation, super-event, portrait, or custom 3D | Conformant/N/A | None introduced; no Event 021 UI-worker/portrait/3D handoff required. |
| Cleanup covers victory, defeat, annexation, settlement, actor disappearance, exposure, queues, reservations, and adapter state | Implemented in source; engine unverified | Cleanup hooks exist; lifecycle projection and live matrix missing. |
| Documentation, details, logs, evolutions, workbook, cluster/scenario rows remain aligned | Partial/stale | Current workbook/CSV rows align, but overview/acceptance/source-map revisions and hashes are stale and severity text conflicts. |
| Required final decision/mission, country-package, localisation, asset, probability, completion audits | Partial | Localisation/asset/older probability/completion materials exist; final decision and country-package handoffs are absent; current probability specialist did not return. |
| User live validation, save/load, multi-war, performance, and Maximum-scenario evidence | Missing | No valid live or performance receipt exists; source/MCP evidence is not treated as equivalent. |

## Authoritative workbook and generated CSV state

The workbook was inspected read-only as the source of truth.

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` SHA-256: `AFC4C95D041A2AC15493D48E76B31C10F811DFB79746E86F1CF6F56AC20E5E49`.
- `docs/spreadsheets/chaos_redux_events_catalog.csv` SHA-256: `2513570A9DCBA604101D6258549882BA33740E56D7DBA005CFBF424DA83261B4`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv` SHA-256: `A5B37060DD4063F10EB326C21CA8B4B3F557B2BE2BE48DC2C3C0CBE60FF28E`.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` SHA-256: `8B944DE19817B3887EAC22E3D12437E62990273C8B0DB1C6F27928F349D4B2E7`.
- Events row 22 identifies Event 021 as `Random Civil War`, Minor Repeatable, chaos 1, Wars cluster, `Needs Testing`, with current Event Details and all three evolution descriptions.
- Clusters row 2 contains the Wars membership sequence `4, 4, 4, 4, 7, 7, 21, 45, 62`; Event 021 is Medium and the cluster status is `Partially Available`. The generated cluster CSV omits a Status column by export schema, not by manual divergence.
- Scenarios row 16 identifies `SCN-018`, `The Fracture Cascade`, all four types/intensities, and `Needs Testing`.
- Current CSV rows match the authoritative workbook fields. Older hashes in acceptance/source-map documents are stale and must not supersede these current files.

## MCP event evidence and limits

All calls were read-only against workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Event 021

- Fresh `hoi4.event_inspect(mode = lint)` for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL`, revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, zero helper expansion, one aggregate blocking diagnostic, and `validation.passed = false` because large-workspace helper projections and lifecycle passes were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96824cc5114dd2610dd086ab3c03a7595b7d15391a147acf26426894b107b6bd/04435a13a288a781d3c967903cd78ebad58297b1271a14c89b6a7cb47ecb7488/event-lint-4bccb6ec7fe1.json`.
- Fresh `hoi4.event_render(view = overview)` returned `EVENT_RENDERED_PARTIAL`, the same revision/hash, layout hash `3cf23da1fa05f76b7c4361d9fc375759010e2528fb44bd24566df7de8387ecf8`, two selected nodes, and 42,570 omitted nodes. Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/246b83387c42ec9424dc1bc06401386096317d21158ef01b162769663f41d9b8/af0eaf204cd46be9239b4696c52394de6cafc01c343f11b873ceb01ce2f77cbd/event-overview-4bccb6ec7fe1.json`.
- Required compare from prior Event 021 revision `23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646` to current returned the exact blocker `EVENT_REVISION_NOT_CACHED — Requested event graph revision is not cached`, with no comparison artifact. A source diff is not substituted.

### Event 006 dependency

- Fresh `hoi4.event_inspect(mode = lint)` for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at the same revision/graph hash with the same deferred helper/lifecycle limitation. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35c597e6ed1589a9da5c8f4db185b29c17f6dc02160f21ac2c2f4f9d99e61f34/3f447ac50fa116f227ca73089beba58db68156f6a5b27e0bc8c857747beacea9/event-lint-4bccb6ec7fe1.json`.
- Fresh `hoi4.event_render(view = overview)` returned `EVENT_RENDERED_PARTIAL`, layout hash `340071ffd5797720635ee88ef724d794ec40a8b419d505221944ec59b8ab1bb8`, five selected nodes, and 42,567 omitted nodes. Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc0a6c74a838f6d9727157d534d8195c33b9ff544be2a4c70f49d1fb8eafe223/e27e35b73ccc197e468960c8b68d5604abb9b1561c59cea39c300982cab306f6/event-overview-4bccb6ec7fe1.json`.
- Required compare from prior Event 006 revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8` to current returned `EVENT_REVISION_NOT_CACHED — Requested event graph revision is not cached`, with no comparison artifact.

### Event 006 focus-tree dependency

- Fresh `hoi4.focus_inspect` for `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED`, validation passed, revision `00f1f3aa64d4c4cb716c26af11d1606a1625b0f71d37a7ccc96b8cebe6dda838`, 184 resolved focuses, no crossing or node-intersecting connectors, and no blocking diagnostics. It reported one mod warning: the accepted connector from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine` spans ten columns; the other localisation warning belongs to vanilla `continuous_restrict_freedom`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/457f2898adc9174bead7471e640fb9d887c7341a0d9e37ce3745c145d93c5a37/e20fd39acb7e73397142c3e6fa32dbcaae1686cff728a58a6c7ec7584c546ed5/focus-inspect.00f1f3aa64d4c4cb.json`.
- Fresh `hoi4.focus_render` returned `FOCUS_RENDERED`, validation passed, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. Authoritative JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e40d7bffd70e2530e888d825101629c15ea64856e4676919fa6fffe1f4eb656/9265ce129c5056001b41315e4b09b855094af407efb0a11bac4af59847b91f13/independence_wave_focus_tree.focus.json`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/d3edf0dcc1b77abfc05c52d90ccb6201e9415a6a316792ac23f2b653d2e730f3/independence_wave_focus_tree.focus.svg`.
- This proves the current shared tree is structurally available to the parser and renderer. It does not prove that an Event 021-created actor can select or receive it: the tree's `country` modifier at `common/national_focus/006_independence_wave_focus.txt:41-46` requires `is_independence_wave_event6_local_content_active`, which the origin-neutral Event 021 adapter cannot satisfy. It also does not replace focus-selection probability or live focus-loading evidence.

### Wars-cluster Event 004 and Event 007 precedents

- Fresh lint inspection for `chaosx.nr4.1` returned `EVENT_INSPECTED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec1e79feca7400091c7457e02cd2609cb4a82506295de52646eb42936087bfbe/5b476d9b3c1efa8043a869d144cb96898d0a4423856e1428595c826c04a00afe/event-lint-4bccb6ec7fe1.json`. Its overview render also returned partial, two selected nodes, layout hash `9242f3d44439e1d524731e94b99f1304de3910c1f3a91e9924fac2d5e4541dca`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f22928ff3319ab7c01f84ebe69b602a3b746ae1531616fe32321ffca380a730/b54b306a29e96839b6ee72bac0b2182b7b51a600e744450a50d46f941d40e057/event-overview-4bccb6ec7fe1.json`.
- Fresh lint inspection for `chaosx.nr7.1` returned `EVENT_INSPECTED_PARTIAL` at the same revision; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f0a5f3799cac0c6f2437ea0518f1755767a1671c0edcafd81f6df6362590e51/004e6c85755836c4f721a5a12a666448c1db4757859189ec4957d6a4281e361b/event-lint-4bccb6ec7fe1.json`. Its overview render also returned partial, two selected nodes, layout hash `9f8e8a5d2f382edbc24c567b3be0575bbcf91bb819e7575c858d3fd944c47264`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4df375344e2c8c632ba1248c063176bccf908cb5572d9f944176539320be3aa/b7648c725b0c7f903eb7f2339ba76b92f6505497d97a88c39d94cfd0d9c77c64/event-overview-4bccb6ec7fe1.json`.
- No Event 021-owned before/after revision was identified for the unchanged Event 004/Event 007 precedent roots, so no comparison claim is made for them.

These artifacts establish current parser/index visibility and narrow structural connectivity only. They do not prove helper semantics, event-target lifetime, country/state transfer, war creation, focus loading, decision availability, cleanup, save/load, presentation delivery, AI behavior, probability, or performance.

## Probability evidence

Every weighted Event 021 surface was routed to `chaosx_ai_probability_auditor` with `fork_context=false` and a read-only prompt covering TGT, ARC, SEV, EVO, FRT, SPN, STR, SET, REC, GLB, CLU, and SCN, plus event options, decisions, missions, random lists, MTTH, AI strategy, custom pools, and Event 006/Wars dependencies.

The current specialist did not return a final response or durable artifact. It remained `running` through four bounded waits totaling twelve minutes, remained running after an explicit instruction to conclude without further calls, and was then closed with previous status `running`. This is the exact current specialist-route blocker; no fresh analysis ID, scenario hash, evaluate/sweep/simulate/sequence result, probability render, or compare receipt can be claimed.

The strongest existing handoff is `docs/plans/021_random_civil_war_plans/subagent_handoffs/ai_probability_audit_2026-09-06.md`. It is useful historical evidence but is not current-revision acceptance. Its dispositions remain:

| Matrix | Strongest available disposition |
|---|---|
| TGT-01–TGT-10 | Score-only source trace; incomplete live candidate pool; no exact target probability. |
| ARC-01–ARC-08 | Six route weights visible; aggregate random-list pool incomplete; conditional selection unresolved. |
| SEV-01–SEV-06 | Deterministic source mapping, not a weighted result; fixtures and design authority unresolved. |
| EVO1-01–EVO3-02 | MTTH adapter exposed no executable candidates; timing unresolved. |
| FRT-01–FRT-05 | Front/cap structure visible in source; no complete front candidate/sequence result. |
| SPN-01–SPN-05 | Exposure/sponsor pool incomplete; no ranking/probability result. |
| STR-01–STR-05 | Strange-incident inspect timed out in the dated audit; no current exact 8/92 evaluation/compare. |
| SET-01–SET-06 | Settlement source trace only; no complete postwar fixture or weighted outcome acceptance. |
| REC-01–REC-06 | Recurrence source trace only; date/state competition and timing unresolved. |
| GLB-01–GLB-07 | Bounded source structure only; queue ordering, starvation, launch chance, and drift unresolved. |
| CLU-01–CLU-05 | Cluster rows visible; member availability, collisions, rerolls, pacing, and normalized selection unresolved. |
| SCN-01–SCN-07 | SCN-018 source shares/identity visible; custom scenario inspect returned zero candidates; realized share/completion unresolved. |

No current same-scenario `hoi4.probability_compare` result exists for the full changed weighted surface. Older recurrence- or sponsor-specific receipts do not close the current matrix.

## Accepted-plan disposition

The principal accepted design remains in the numbered Event 021 specs and prompts. Implementation evidence does not establish acceptance where the design record is missing or conflicting.

| Plan/addendum item | Current disposition |
|---|---|
| Base Event 021 specification | Accepted design, partially implemented, not accepted complete. |
| B01 Event 006 local-content integration | Prior `implemented` disposition is stale/incorrect against current source. Reopen as incomplete: Event 021 adapter actors cannot satisfy the Event 006 local-content gate used by focus and decision surfaces. |
| B02 sponsor bridge | Implemented in source; probability and live behavior remain unverified. |
| B03 fixed-target helper | Blocked as documented; no accepted complete helper/runtime receipt. It must remain a visible dependency if a final acceptance scenario still requires it. |
| B04 admitted 32-package visual/provenance closure | Blocked; reused Event 006 audit remains incomplete. |
| B05 probability completion | Accepted and queued previously; currently blocked by incomplete dated evidence and a non-returning fresh specialist route. |
| B06 severity selection authority | Unresolved design gap. Deterministic implementation and weighted-pool documentation conflict. |
| B07 lifecycle/save-load acceptance | Accepted and queued; no engine/live evidence. |
| B08 complete MCP/runtime evidence | Accepted and queued; current event evidence remains partial and changed-revision compares are not cached. |
| B09 event-owned scripted GUI | Not applicable/rejected by the accepted normal-decision-category design. |
| B10 final specialist audits and documentation reconciliation | Accepted and queued; decision/country-package handoffs are absent and current docs are stale. |
| B11 custom 3D/portrait/animation/super-event expansion | Not applicable under the accepted exclusions. Event 006-owned portrait dependencies remain within B04. |

No unresolved proposal was silently promoted into an accepted specification during this audit.

## Documentation and evidence gaps

- `docs/021_random_civil_war/overview.md:314-320` records older MCP revisions as current; line 326 conflicts with line 94 and current deterministic severity source.
- `docs/021_random_civil_war/acceptance_evidence.md:16-24` mixes the current `4bcc...` lint with older render artifacts; lines 180, 188, 190, 192, and 194 correctly retain package, render, live, portrait, and release blockers.
- `docs/021_random_civil_war/source_of_truth_map.md` predates current MCP revisions and workbook/CSV hashes.
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/late_source_repairs_2026-09-12.md` correctly records the regional-exposure marker repair, but its partial MCP limitation remains.
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/late_source_repairs_2026-09-06.md` and `improvement_loop_disposition_2026-09-06.md` overstate B01 Event 006 local-content completion relative to current source.
- Required durable final handoffs for `chaosx_decision_mission_auditor` and `chaosx_country_package_auditor` are absent from the Event 021 handoff directory. The conditional focus audit became applicable because Event 006 focus loading is part of the accepted adapter contract and is currently implicated by the gate defect; no current focus acceptance handoff closes it.
- Event 021-owned asset documentation is comparatively complete, but live consumer validation is pending. Reused Event 006 assets remain a release blocker, not an optional polish item.
- Spec manifest hashes are stale for two files, as recorded above.

## Meaningful validation performed and missing

Performed read-only in this audit:

- Compared every Event 021 spec/prompt family against current source, plans, handoffs, docs, assets, and catalogs.
- Read Event 006 specs/current implementation evidence and reconciled the exact 32 admitted package IDs against the adapter registry.
- Traced the Event 006 package-content and player-surface gates into actual focus, category, and decision consumers, exposing the local-content blocker.
- Traced State Authority predicates into scripted localisation, exposing the unreachable Collapse band.
- Verified all nineteen Event 021 event definitions have current internal callers.
- Verified 40 Event 021 GFX texture references resolve, six achievements exist, eighteen achievement sprite states exist, twelve AI strategy entries comprise eleven accepted roles plus the global overlay, the adapter registry contains exactly 32 admitted packages, and the decision file contains 18 actions plus three missions.
- Verified the regional exposure setter/consumer/cleanup chain after the 2026-09-12 repair.
- Read the authoritative XLSX and generated CSV exports and recorded current hashes/rows without modifying them.
- Ran current read-only `hoi4.event_inspect` and `hoi4.event_render` for Event 021, Event 006, Event 004, and Event 007; attempted required Event 021/Event 006 comparisons and retained exact cache blockers.
- Ran current read-only `hoi4.focus_inspect` and `hoi4.focus_render` for the shared Event 006 tree implicated by the Event 021 adapter; separated its clean structural result from the failing actor-eligibility contract.
- Routed all weighted families through `chaosx_ai_probability_auditor`; retained the exact non-returning specialist status and did not substitute source-only analysis.

Still missing or not equivalent to performed checks:

- Complete helper expansion and lifecycle state-flow evidence for all Event 021/Event 006 callbacks and cleanup paths.
- Valid changed-revision `hoi4.event_compare` artifacts for Event 021 and Event 006.
- Current complete probability inspect/evaluate/sweep/simulate/sequence/render/compare evidence for every named matrix family.
- Current decision/mission, country-package, and implicated focus specialist audit handoffs.
- Live Event 021-origin focus assignment and focus-selection probability evidence; current structural focus inspection cannot establish actor eligibility.
- Engine/live evidence for opening archetypes, viable region/capital/remnant, unit/equipment allocation, same-tag fallback, multi-front wars, settlements, recurrence, exposure, sponsors, nesting, successor creation, cleanup, Event Log/Details delivery, achievement triggers, and Event 006 package play.
- Save/load and concurrent-war lifecycle evidence.
- SCN-018 Low/Medium/High/Maximum realized selection evidence, including Maximum every-eligible coverage and immediate-setup performance.
- Live consumer evidence for Event 021 assets and closure of all reused Event 006 asset/provenance blockers.

## Recommended next actions

1. The gameplay owner should correct the Collapse-band predicate and add a bounded source regression check that proves initialized authority 0–14 reaches Collapse while 15+ does not.
2. The Event 006/Event 021 integration owner must resolve the accepted full-package contract: Event 021-origin actors need the package tree, formation/formable decisions, AI, and national content without mutating Event 006 firing/count/evolution/league state. The solution must be audited for focus loading, duplicate rewards, lifecycle identity, and cleanup; this auditor does not prescribe or apply the patch.
3. Re-run `chaosx_country_package_auditor`, `chaosx_decision_mission_auditor`, and the conditional focus auditor with `fork_context=false`; require durable handoffs and mandatory focus MCP evidence for the implicated Event 006 selector.
4. Resolve severity authority explicitly: accept the deterministic ladder and reconcile all pool language, or accept a weighted model with balance targets and require a baseline/owner patch/same-scenario probability compare. Do not infer approval from current source.
5. Complete the admitted 32-package Event 006 runtime/content matrix and reused-asset/provenance audit, including all portrait placeholder/final states and package-specific focus/decision/formable/flag/idea consumers.
6. Re-run the probability specialist only with bounded, typed fixtures and exact candidate manifests for every matrix family; retain inspect-first, analysis IDs, scenario hashes, renders, and same-scenario comparisons.
7. Obtain fresh Event 021/Event 006 inspect/render evidence with helper/lifecycle coverage and preserve a cacheable baseline for changed-revision compare.
8. Complete the user-owned live and performance acceptance matrix, then update overview, acceptance evidence, source-of-truth map, plan dispositions, workbook status, CSV exports, and spec manifest hashes only after the evidence exists.
9. Keep `random_civil_war_rework_ready` unset and Event 021 catalog status at Needs Testing until every blocker is closed.

## Final disposition

Remaining omissions, simplifications, placeholders, fallbacks, and evidence gaps:

- Source defect: live Collapse State Authority band is unreachable.
- Source/contract defect: Event 021-created Event 006 actors are denied the required full Event 006 focus/decision player surfaces.
- Design gap: deterministic severity source conflicts with weighted-pool documentation and B06 remains unresolved.
- Missing specialist handoffs: current country-package, decision/mission, implicated focus, and complete probability acceptance.
- Blocked dependency: all 32 admitted Event 006 packages lack complete runtime/content/asset/provenance proof; grounded portrait placeholders/replacements remain unresolved.
- MCP gaps: helper/lifecycle projections are partial; Event 021/Event 006 baseline revisions are not cached for compare.
- Probability gap: no current complete scenario analyses or same-scenario compares for TGT/ARC/SEV/EVO/FRT/SPN/STR/SET/REC/GLB/CLU/SCN; the fresh required specialist remained running and returned no result.
- Live gaps: no engine/save-load/concurrency/cleanup/Event Log/Event Details/achievement/asset-consumer acceptance.
- Performance gap: no SCN-018 Maximum or long-run scheduler measurement.
- Disclosed fallback: Event 021 alpha-edge repairs were used and documented; live visual acceptance is pending.
- Preserved legacy assets: fifteen unused legacy Event 021 achievement DDS files remain documented orphans, not current wired achievement states.
- Documentation gaps: stale MCP/workbook hashes, conflicting severity wording, stale B01 disposition, and two stale spec-manifest hashes.

Overall status: INCOMPLETE
