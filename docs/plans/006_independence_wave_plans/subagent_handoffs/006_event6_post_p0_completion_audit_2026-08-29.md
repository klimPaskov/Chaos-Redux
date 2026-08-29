# Event 006 post-P0 completion audit — 2026-08-29

Date: 2026-08-29 (Europe/Kyiv).

Mode: read-only completion audit at the Event 006 P0 snapshot `713306f2ec41102998b63a89e327fac844d4d1a6`, including P0 commits `3ce4b3468db6e037e4ce0ede54498dfc558990e2` and `713306f2ec41102998b63a89e327fac844d4d1a6`.
The later `57bcee4b2` commit is unrelated natural-disaster work and does not change the audited Event 006 files.

No gameplay, asset, localisation, spreadsheet, specification, source-of-truth, or catalog file was edited. This handoff is the only file added by the audit.

## Executive disposition

The SCN-008 publication P0 is **source/static closed**.

Event 006 as a whole remains **HOLD / PARTIAL**. The P0 repair does not close country-package breadth, portrait-consumer authority, decision and mission issues, localisation quality, non-portrait asset gates, formable and League reachability, super-event 23 rights/audio, probability evidence, current production GUI/event MCP evidence, or runtime observation.

No whole-event completion claim is made.

## P0 commit file boundary

Commit `3ce4b3468` changed:

- `common/decisions/006_independence_wave_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_publication_boundary_patch_2026-08-29.md`

Commit `713306f2e` changed:

- `events/006_independence_wave.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_scn008_publication_boundary_patch_2026-08-29.md`

The Event 006 source is clean relative to the audited P0 snapshot. The shared worktree has unrelated natural-disaster and dynamic-effect changes; this audit did not inspect or modify them.

## SCN-008 publication-boundary verification

### Global dispatch census

The current `events/` and `common/` source contains exactly one dispatch of `chaosx.triggerable_scenarios.80`:

- `common/scripted_effects/006_independence_wave_scenario_effects.txt:1390`

The definition at `events/006_independence_wave.txt:583` is not a dispatch.

The sole dispatch is inside the successful branch of `independence_wave_trigger_scenario`. Its order is:

1. committed phase, current plan ID, Independence Wave owner, no execution/scenario/finalization failure, and `liberation_release_joint_plan_executed` are required at `common/scripted_effects/006_independence_wave_scenario_effects.txt:1365-1379`;
2. `independence_wave_scenario_committed` is set at `:1380`;
3. the released and blocked summary is frozen at `:1387`;
4. public Event 006 report `chaosx.nr6.2` fires at `:1389`;
5. delayed `.80` fires at `:1390`.

Therefore every `.80` dispatch is success-only and occurs after `chaosx.nr6.2`.

### Failure paths

The transaction failure branch at `common/scripted_effects/006_independence_wave_scenario_effects.txt:1392-1438`:

- clears `independence_wave_scenario_committed`;
- sets `independence_wave_scenario_failed`;
- records failure/finalization state and performs rollback or abort handling;
- calls `independence_wave_scenario_reset_summary` before returning;
- contains no `chaosx.nr6.2` or `.80` dispatch.

The invalid queued-launch branch at `events/006_independence_wave.txt:552-576`:

- sets `independence_wave_scenario_failed`;
- clears `independence_wave_scenario_committed`;
- clears the queued country flag;
- resets the scenario summary;
- records the stale-plan reason;
- contains no `chaosx.nr6.2` or `.80` dispatch.

`independence_wave_scenario_reset_summary` clears the country ledger flag, both ledger indices, dates, released/blocked/country arrays, and counts at `common/scripted_effects/006_independence_wave_scenario_effects.txt:1104-1126`. A later invalid or failed generation therefore cannot expose a ledger left by a prior success.

### Result-event and setter census

There is exactly one setter of `independence_wave_scenario_ledger_visible`:

- `events/006_independence_wave.txt:600`, in option `.80.a`.

The `.80` event trigger requires committed, not scenario-failed, and not finalization-failed at `events/006_independence_wave.txt:588-592`. Option `.80.a` independently requires the committed receipt at `:594-600`. A delayed result scheduled by a successful generation will fail its event trigger if a newer failed generation clears the receipt before delivery.

The fallback `.80.b` option is unreachable under the new event-level committed trigger because it requires `NOT = { has_global_flag = independence_wave_scenario_committed }` at `events/006_independence_wave.txt:603-610`. It does not set ledger visibility and does not weaken the publication boundary. It is stale/dead fallback source, not a failure-side leak.

### Category and control visibility

The scenario ledger category at `common/decisions/categories/006_independence_wave_categories.txt:608-620` requires:

- `independence_wave_scenario_committed`;
- neither scenario failure flag;
- the country ledger-visible receipt;
- at least one blocked package row.

All three navigation decisions repeat committed, non-failed, and country-receipt gates:

- previous: `common/decisions/006_independence_wave_decisions.txt:938-945`;
- next: `:975-982`;
- close: `:1011-1018`.

The global census found no second category definition, second setter, or second `.80` dispatch. No failure-side Event 006-branded result or ledger category leak remains in current source.

## Strict validation

Every available maintained Event 006 validator passed at HEAD:

- `audit_event6_allocator.py`: 149 publishers, 126 automatic/high-chaos rows, 138 SCN-ranked rows, 40 adapters, eight adapter-only rows, 32 attestations, 29 groups, exact `3/4/5/7/10` ladder, protected remnants, and retired pre-event surface;
- `audit_event6_country_api.py`: 242 broad tags, 191 resolved carriers, 34 Soviet carriers, 45 African carriers, zero missing, zero duplicate carriers, IW-031 crosswalk pass;
- `audit_event6_flags.py`: 102 registered and 102 structurally complete flag families;
- `audit_event6_form16.py`: exact ARM/GEO/AZR member, state, consent/refusal, mutation, rollback, cleanup, and fail-closed contract;
- `audit_event6_gui_matrix.py`: five Statehood tabs and the accepted recognition, dependency, League, formable, cleanup, and static/animated semantic matrix; production render/save-load is not claimed;
- `audit_event6_scenario_matrix.py`: all 32 SCN-008 mode/intensity cells and eight edge cases.

A separate narrow source assertion passed the one-dispatch census, one-setter census, `nr6.2 -> delayed .80` order, zero failure-side `.80` dispatches, receipt cleanup, and category/control gate contract.

These are source/static checks. They do not replace required MCP event, GUI, focus, map, or probability evidence.

## Completion status after P0

| Surface | Current status | Remaining boundary |
| --- | --- | --- |
| SCN-008 publication | **Source/static closed** | Fresh event inspect/render/compare and production decision render are unavailable. |
| Exact allocator and no-pre-event boundary | **Source-strong for admitted packages** | Whole transaction is not content-complete for 161 unattested rows. |
| Country packages | **HOLD / PARTIAL** | Boundary remains 32 content-attested packages, 29 groups, 40 adapters, eight adapter-only rows, and 161 unattested selectable rows. IW-095 is package-local at state 776 but centrally blocked; IW-108, IW-136, IW-130, IW-086, and IW-073 remain research/ownership/source-gated. |
| Recruitment and portraits | **Committed source, stale authority, portrait handoff missing** | Current HEAD has 25 guarded recruitment blocks, 65 `recruit_character` calls, and 58 character portrait blocks. The source-of-truth map, resume packet, acceptance checklist, country audit, and portrait audit still use 54 calls and 47 resolved portrait references or describe the 65/58 extension as uncommitted. The eleven ideology-specific AXX/BOS/BBX/MAC/BAX/KOS consumers need a current `chaosx_portrait_creator` consumer/manifest handoff before authority promotion. |
| Decisions and missions | **Source broad; HOLD / PARTIAL** | The earlier SCN-008 failure-publication finding is superseded by P0. Remaining findings include 30 administration-factory requirements disclosed without matching reservation/consumption, DM-35's hidden always-paid base cost on its Later branch, founding missions missing from some active-project locks, unproved visible-density ceilings, and unavailable probability/production GUI evidence. |
| Five committed war-support eligibility changes | **Source committed; probability evidence incomplete** | Komi, Kosovo, Kuban, Ruthenia, and Udmurt strategic gates now match the accepted four-group source palette and current cost localisation, but the changes landed in `11f0757a7` without the mandatory same-named-scenario probability comparison. They cannot support a quantitative balance claim. |
| Join achievement hook | **Source committed; owner evidence partial** | `humanitarian_achievement_record_tag_switch` now wraps the Event 006 Join tag change. The Event 006 authority still describes it as uncommitted, and no Event 006-specific idempotence/reachability handoff was found. |
| Localisation | **Materially improved; still partial** | The prior 1,880 leading-whitespace defect is closed at HEAD: the nine named files now contain zero indented key rows. Event Details is premise-only at `localisation/english/chaosx_gui_l_english.yml:1074`. Remaining player-facing process wording includes “package” in Scotland/Wales, Asante/Sokoto, and Rhineland/Bavaria strings, while a current audit indicator still finds 95 cost-key rows containing numeric literals without a dynamic constant token. Current production render and exact visible-consumer review remain unavailable. |
| Documentation and catalog | **Catalog aligned; authority stale** | Export rows are Event 006 `Needs Testing`, SCN-008 `Needs Testing`, and Liberations `Partially Available`; cluster members are exactly `5, 6`, and Event Details matches C7 premise text. The source-of-truth map/resume packet do not cite the two P0 commits and still call the 65-call/58-portrait source uncommitted. The P0 handoff retains a now-stale “parent must patch” paragraph before its later completion addendum. |
| Focus tree | **Bounded geometry closed; whole-focus partial** | Retained evidence is 184 focuses and 195 connectors with zero Event 006 geometry diagnostics. Package breadth, route differentiation, AI, reward/idea lifecycle, and fresh MCP evidence remain partial. |
| Statehood and formable GUIs | **Source semantic pass; visual acceptance blocked** | Statehood retains the recorded `GUI_TAB_STATE_CONFLICT`; formable renders lack family-isolated state, hierarchy, click-region, resolution, and comparison evidence. Current GUI MCP routes are unavailable. |
| Formables | **HOLD / PARTIAL** | Fourteen of 48 families have runtime-authored state-puzzle consumers; 34 remain fail-closed. FORM-42 remains blocked and FORM-48 remains unreachable while FSM is unadmitted. Revolutionary/military commit methods still exceed the accepted four-spendable-group ceiling, and generic commit factory handling/terminal category cleanup remain open. |
| League and evolutions | **Source-present; acceptance partial** | Five evolutions and the informal/formal League plus rival-bloc state machine are source-wired. Current event/probability MCP, end-to-end reachability, and optional live save/load observation remain absent. |
| Super-event 23 | **Blocked** | The accepted London Brass Players recording lacks verified United States/worldwide redistribution clearance. Audio ID 23, wrappers, catalog rights row, and firing assignment remain absent. Research candidates are not approved substitutes. |
| Super-event 24 | **Source-wired; reachability partial** | Text/image/audio/wrapper and factual predicates exist; package, League, and formable gates still constrain end-to-end reachability. |
| Non-portrait assets | **Partial** | The current asset audit retains ASSET-004 strict-grayscale, AEX cross-event basename ownership, NWE ideology-alias approval, ASSET-046 emblem coverage, BWX/chunk-3 flag rights, animation-manifest, and super-event 23 rights gaps. Structural flag validation does not clear provenance. |

## MCP, probability, and live evidence

The current tool catalog exposes no `hoi4_agent_tools` event, focus, GUI, probability, or map method. The only matching HOI4-named method is an unrelated Blender texture-processing route.

Accordingly, this audit could not run:

- `hoi4.event_inspect`, `hoi4.event_render`, or `hoi4.event_compare` for the P0 revision;
- focus inspect/render;
- Statehood or formable GUI inspect/render/compare;
- map inspection for package anchors;
- probability inspect/evaluate/sweep/sequence/compare through `chaosx_ai_probability_auditor`.

Prior artifacts remain dated evidence and are not current P0 proof. Source inspection is not treated as equivalent MCP evidence.

The accepted 24 AI-profile contract, central allocator scenarios, event options, evolution timing, decisions, missions, focus selection, AI strategies, and custom weighted pools still lack complete typed eligible pools, normalized results, and same-scenario comparisons. The five now-committed strategic eligibility changes particularly require a current probability baseline and compare.

HOI4 was not launched. Live transaction, save/load, decision presentation, GUI behavior, and end-to-end reachability remain unobserved. Under the controlling Event 006 acceptance decision, live play is optional future QA rather than a substitute for required source/static/MCP evidence; this audit therefore makes no runtime claim.

## Accepted-plan disposition

- Exact `3/4/5/7/10`, reservation-first transaction, host survival, and no-pre-event presentation: **implemented for the admitted boundary**.
- SCN-008 32-cell matrix: **source/static implemented for the admitted boundary**.
- SCN-008 success-only publication: **source/static closed by `3ce4b3468` and `713306f2e`**.
- IW-095 first-footprint tranche: **package-local implemented, central admission blocked**.
- Remaining first-footprint queue and 161 unattested rows: **queued, research-gated, or genuinely missing; not admitted**.
- 80-row decision/mission crosswalk: **source implemented; behavior, UI, exploit, and probability acceptance partial**.
- Focus geometry: **implemented; whole-focus completion partial**.
- 48-family formable design: **14 runtime-authored consumers, 34 missing/fail-closed**.
- League/evolutions/achievements: **source-wired in bounded tranches; reachability and evidence partial**.
- Super-event 23: **rights/audio/firing blocked with no approved fallback**.
- Super-event 24: **source-wired, reachability partial**.

## Required next actions

1. Reconcile P0 commits `3ce4b3468` and `713306f2e` into the source-of-truth map, resume packet, overview, acceptance checklist, and P0 handoff disposition.
2. Promote the now-committed 25-block/65-call recruitment source only after a fresh portrait-creator consumer/manifest audit covers all 58 portrait blocks and eleven new character consumers.
3. Route the committed strategic eligibility changes and other weighted surfaces through `chaosx_ai_probability_auditor` once the MCP route is available; use exact named before/after scenarios and a same-scenario compare.
4. Resolve the remaining decision/mission cost, active-project-lock, density, and tooltip findings without reopening the SCN-008 P0 boundary.
5. Continue package admission one exact identity/rights/map/force/decision/focus/AI/asset/cleanup packet at a time; retain the 32-package boundary meanwhile.
6. Keep 34 formable families fail-closed until their exact member, state, identity, integration, GUI, and AI contracts exist; do not weaken FORM-42 or FORM-48 gates.
7. Keep super-event 23 unwired until the accepted recording is rights-cleared or the user explicitly reopens selection.
8. Restore current event, GUI, focus, map, and probability MCP evidence before any whole-event completion claim.

## Files changed by this audit

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_post_p0_completion_audit_2026-08-29.md`

No other file was changed, staged, or committed by this auditor. No fallback or simplification was introduced. Event 006 remains **HOLD / PARTIAL** and no completion claim is made.
