# Current system completion re-audit — 2026-08-26

## Verdict

The current working-tree implementation is **partial and blocked, not complete**.

The source audit initially found two high-severity current-source defects: eight route-damage checks referenced an undefined `constant:migration_core_reconciliation.route_damage_threshold`, and destination-history traversal referenced an undefined `constant:migration_destination_selection_runtime.array_index_increment`. The parent corrected both while this audit was running by reusing the existing neutral constants `constant:civilian_transfer_route_projection.damage_threshold` and `constant:humanitarian_runtime.array_index_increment`. The post-patch census found zero remaining references to either undefined name. These findings are therefore classified **already closed/superseded**, not open defects, and this auditor made no gameplay edit.

No other actionable current-source defect was confirmed before the parent-imposed completion boundary. Source presence is not treated as runtime proof. Exact-owner receipt gaps, installed MCP limitations, and user-owned live validation remain completion blockers.

## Scope and authority reviewed

This read-only audit reviewed `AGENTS.md`; the current `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions`, and workbook guidance; the required offline wiki core pages plus Interface Modding, Scripted GUI Modding, and Map Modding; relevant installed vanilla effects, triggers, script-concept, script-constant, event, decision, AI, GUI, and map documentation and precedents; all eight specification parts; the specification README; coding, goal, decision, asset, and achievement prompts; integration, death, decision, asset, historical, probability, input, and output matrices; implementation surface map; bibliography; routing/status files; improvement-loop closure; current source; and the current source-of-truth, completion, disposition, probability, mapmode, namespace, improvement, and blocker handoffs named in the parent task.

The latest user decisions were treated as binding: famine and migration remain separate mechanics, categories, and mapmodes; each exposes exactly three canonical player-facing values; each category remains hidden until its own problem exists while both mapmode buttons are visible from campaign start; combined `famine_migration_*` and `fm_*` runtime identifiers are forbidden; and shared contracts are limited to narrow neutral `civilian_transfer_*` and `humanitarian_*` seams. This audit does not propose an event ID, event-pool row, event-log row, or pacing pulse.

## Complete requirement evidence matrix

| Requirement | Current evidence | Completion status | Classification / limit |
|---|---|---|---|
| Separate mechanic ownership | `common/decisions/famine_decisions.txt`, `common/decisions/migration_decisions.txt`, separate constants/effects/triggers, and `namespace_separation_validation.md` | Finished in source | No combined runtime owner accepted. |
| Namespace separation | Fresh runtime census across `common`, `events`, `interface`, `localisation`, and `history` found zero `famine_migration_` and zero word-boundary `fm_` hits; no forbidden filename was found | Finished in source | CBRN-local `cbrn_action_civilian_response_exposure_mult` is unrelated to this package and is not a combined famine/migration owner. |
| Exactly three canonical values each | Completion/localisation evidence records Famine Stage, Food Reserves, Relief Access and Displacement Load, Reception Capacity, Border Policy | Finished in source | Extra flags, receipts, phase strings, and mapmode context are not presented as extra canonical meters. |
| Independent category reveal and dormancy | `common/decisions/categories/famine_decision_category.txt:3-15` uses `famine_decision_problem_is_active`; `migration_decision_category.txt:3-22` uses only migration/corridor-emergency state; both use `visible_when_empty = no` | Finished in source | Live reveal/dormancy behavior remains user-owned validation. |
| Independent action density | Current completion evidence records 10 famine and 18 migration weighted actions, six missions, and a maximum of six compatible primary actions per mechanic state | Finished in source; probability partial | Exact runtime density and AI selection remain subject to probability/tool and live limits below. |
| Dynamic famine stages and formula | `famine_core_effects.txt` and `famine_core_constants.txt`; completion report records the weighted, clamped formula and 25/50/75/100 entry with 20/40/60/80 recovery thresholds | Finished in source | Runtime stage transitions remain user-owned live validation. |
| Population-scaled famine mortality | `common/scripted_effects/famine_core_effects.txt:2401+`; completion report lines 36-38 record live-population scaling, protected floor, stage-specific pulse rates, and one `apply_exact_state_civilian_population_loss` debit | Finished in source | Live cadence and exact displayed totals remain user-owned validation. |
| `From famine` ownership | Exact debit is recorded once to `constant:chaos_meter_deaths_reason.famine`; English localisation is `From famine` | Finished in source | No fixed historical casualty total accepted. |
| Death-reason ownership and no double count | Death matrix, `civilian_transfer_effects.txt`, famine core, migration adapters, and Chaos Meter seams separate famine mortality from forced-displacement route deaths | Finished in source review | Live cross-system ledger reconciliation remains user-owned validation. |
| Exact transfer conservation | Canonical `civilian_transfer_execute_transaction` exists at `common/scripted_effects/civilian_transfer_effects.txt:1022`; current completion evidence records one origin debit, exact route deaths, exact survivor credit, final receipt, rollback, and quarantine | Finished in source | Live transaction/reload proof remains user-owned validation. |
| Every required movement/outcome | Forced, spontaneous, evacuation, return, repatriation, resettlement, corridor, trapped, overcrowded, transit, and integration paths are represented in migration effects/decisions and the output matrix | Finished in source review | Generic war/peace and scenario owners still lack exact cohort facts/people receipts. |
| Blockade conjunction | Famine blockade trigger/effect contracts require the accepted multi-clause proof; mapmode reads only the verified receipt | Finished in source | No proxy route logic accepted; live conjunction remains user-owned validation. |
| Exact adapters and owner callsites | Exact/local owners exist for Air Winter/Fallout, camps/Gulags/forced labor, chemical aftermath, plague/outbreaks, Event 013 disaster, nuclear, deportation, persecution, and condemnation seams | Partial | Generic state-control, bombing, war/peace, cluster/scenario, and relief-obstruction owners remain externally blocked. |
| Ideology override ordering | Destination selection applies safety/eligibility exclusions before bounded ideology scoring, as documented in `migration_destination_selection_constants.txt:37-40` and the probability/source evidence | Finished in source | Dynamic candidate discovery and exact ranking are not tool-certified. |
| Closed-border consequences | Migration decisions, spontaneous movement, trapped-population, reception, corridor, and mapmode contracts expose consequences rather than silently deleting movement | Finished in source | Live consequence/cadence proof remains user-owned validation. |
| Sparse registries/hooks/jobs | `humanitarian_runtime_on_actions.txt:12-40`; sparse state/country arrays and exact enqueue/invalidate callbacks | Finished in source | Only the one-time `on_startup` country baseline pass and `on_daily_CXT` repair remain; no recurring world scan was found or accepted. |
| Event 149 retirement | No event source or replacement ID; negative MCP selectors below; workbook/CSV row says retired and absorbed into the two mechanics | Finished | Do not reintroduce an event, alias, event pool, log row, or pulse. |
| Events 118/120/131 adapter request | Current source and Git-history evidence contain no such roots | Blocked | **External-owner blocker**; absence is not permission to fabricate aliases or proxy events. |
| Eight achievements | Eight registry entries, predicates/producers, localisation, icon triplets, sprites, and documented asset consumers are present | Finished in source/static assets | Unlock, save/reload, and live consumer validation are user-owned. |
| Static assets and consumers | Authoritative manifests document exactly 61 final DDS assets: 50 root-system, seven report images, four mapmode buttons; category, decision, modifier, achievement, death, report, and mapmode sprites are wired | Finished in source/static evidence | Runtime render/consumer acceptance remains user-owned. |
| Character portraits / custom 3D units | No in-scope character portrait or custom 3D unit is required by the binding package | Not applicable | No portrait, unit-audio, counter, or 3D handoff gap is created by this system audit. |
| Localisation | Split famine, migration, mission, humanitarian-cost, achievement, death, report, and mapmode localisation covers both categories and 34 decisions/missions; current prose uses separate mechanic language | Finished in source | Live truncation/substitution remains user-owned. |
| Permanent docs | Separate famine, migration, and neutral transfer documentation plus current source-of-truth, disposition, mapmode, namespace, probability, and completion reports exist | Finished/current, with blockers disclosed | `improvement_review_addendum.md` is historical pre-separation provenance and is explicitly superseded where it conflicts with current specs. |
| Workbook and CSV alignment | Editable workbook is authoritative; current completion report records regenerated event/cluster/scenario exports and Event 149 retirement with no replacement row | Finished in documented export evidence | This read-only audit did not rerun the exporter because it would write export files. |
| Exactly two comprehensive mapmodes | `common/map_modes/chaosx_state_map_modes.txt:390` and `:571`; four selected/deselected button DDS consumers; no combined or third mode | Finished in source/static layout | Dynamic scripted color/tooltip execution and active-button injection are MCP/tool blocked; live behavior is user-owned. |
| Mapmode buttons visible from start | Button/interface wiring is unconditional while decision-category visibility is problem-gated | Finished in source/static layout | Live click and selected-state proof remains user-owned. |
| Dedicated event-owned scripted GUI requirement | No named event introduces a dedicated mechanic window; compact famine/migration category report headers are system/category surfaces | Not applicable | A `chaosx_event_ui_worker` handoff is not required for this non-event system or existing shared/system UI surfaces. |
| AI parity and weights | Humans and AI share source gates; declared pools contain 10 famine and 18 migration candidates; named flat-fact matrices and distinct before/current comparisons exist | Partial | Installed tooling cannot certify special `FROM`, scoped/compound triggers, dynamic pools, normalized probabilities, timing, dominance, repetition, or exploit safety. |
| Improvement-loop closure | Binding addenda are dispositioned into specs/current implementation, superseded, queued with blockers, or rejected; no unresolved broad expansion is silently claimed complete | Finished as disposition work | Improvement closure does not override exact-owner/tool/live blockers. |

## Prioritized findings

### P0 — discovered and closed during this audit

1. **Undefined neutral route-damage threshold reference — already closed/superseded.** Initial evidence was `humanitarian_corridor_triggers.txt:102` plus `migration_destination_selection_triggers.txt:138,171,198,228,245,265,286`, all referencing nonexistent `constant:migration_core_reconciliation.route_damage_threshold`. The parent changed all eight to the already-defined neutral `constant:civilian_transfer_route_projection.damage_threshold` (`common/script_constants/civilian_transfer_constants.txt:22`). Post-patch census: zero old references.
2. **Undefined destination-history increment reference — already closed/superseded.** Initial evidence was `migration_destination_selection_effects.txt:65` referencing nonexistent `constant:migration_destination_selection_runtime.array_index_increment`. The parent changed it to the already-defined shared `constant:humanitarian_runtime.array_index_increment` (`common/script_constants/humanitarian_runtime_constants.txt:19`). Post-patch census: zero old references.

These were parent-owned gameplay corrections. This audit handoff is the auditor's only file change.

### Remaining completion blockers

1. **High — external-owner blocker:** `state_control_occupation_adapter_0826.md` shows the generic control callback lacks hostile-transfer cause, exact affected-people amount, and replay identity. Current fail-closed cleanup/reassessment is correct.
2. **High — external-owner blocker:** `relief_obstruction_receipt_0826.md` shows no people-denominated obstruction receipt. Reserve units, trapped counts, survivor totals, and route status cannot be converted or substituted.
3. **High — external-owner blocker:** generic strategic bombing lacks exact attacker, state, and affected-people amount; country war/peace lacks state/cohort facts; generic cluster/scenario dispatch lacks people receipts.
4. **High — external-owner blocker:** Events 118, 120, and 131 are absent from current source and Git history. No alias or replacement event may be invented.
5. **High — MCP/tool blocker:** installed probability adapters cannot bind special `FROM`, fully resolve scoped/compound triggers, or discover dynamic destination, opposition, and relief-donor pools.
6. **Medium — MCP/tool blocker:** installed map/GUI routes cannot execute or inject active scripted-mapmode state and therefore cannot prove dynamic state colors, tooltip branches, selected-button state, or live click regions.
7. **Medium — user-owned live validation:** live HOI4 category reveal/dormancy, transaction conservation across runtime/reload, death-ledger display, achievements, assets, mapmode behavior, AI behavior, and save/reload behavior remain user-owned.

No fabricated population fraction, event alias, proxy route logic, reserve-to-people conversion, placeholder final art, combined category/mapmode, recurring world scan, or source-only runtime closure is recommended.

## Rejected and superseded findings

- The original shared `famine_migration_*`, `fm_*`, shared-category, shared-mapmode, incident-event, and compatibility-alias proposals are superseded by the binding separation decision.
- A generic `civilian_response` replacement owner is rejected; only neutral narrow `civilian_transfer_*` and `humanitarian_*` contracts are authorized.
- Event 149 reimplementation, a replacement event ID, event-pool row, event-log row, or event pacing pulse is rejected.
- Historical probability claims for the deleted incident-option layer are non-current and do not block the present event-free architecture.
- Earlier completion claims that omitted exact-owner, probability, active-mapmode, or live validation limits are superseded by `completion_report.md` and the current blocker handoffs.
- The two undefined-constant findings above were valid against the initial audit snapshot but are closed by the parent's current-source patch.

## Accepted-plan disposition

The eight spec parts and their matrices/prompts remain binding. Accepted implementation and improvement addenda are represented in current separate famine/migration sources or explicitly dispositioned in `handoff_dispositions.md`. The improvement-loop closure is accepted only as design/disposition closure. It does not promote external-owner blockers, MCP/tool blockers, or user-owned live checks to completion. `source_of_truth_map.md` and `completion_report.md` remain the current summary authorities; blocker-specific handoffs control where they are narrower and newer.

## Validation and census evidence

Read-only checks used during this audit included:

```powershell
rg -n --glob '*.txt' --glob '*.gui' --glob '*.gfx' --glob '*.yml' 'famine_migration_|\bfm_' common events interface localisation history
rg --files common events interface localisation history | Where-Object { $_ -match '(^|[\\/])(fm_|famine_migration_)' }
rg -n -F 'constant:migration_core_reconciliation.route_damage_threshold' common events interface localisation
rg -n -F 'constant:migration_destination_selection_runtime.array_index_increment' common events interface localisation
rg -n 'civilian_transfer_execute_transaction|apply_exact_state_civilian_population_loss|famine_apply_mortality' common
rg -n 'every_country|every_state|on_daily|on_weekly|on_monthly|on_startup' common/on_actions/humanitarian_runtime_on_actions.txt common/scripted_effects/famine_* common/scripted_effects/migration_* common/scripted_effects/civilian_transfer_effects.txt
rg -n 'famine_state_map_mode|migration_state_map_mode' common/map_modes interface localisation
rg -n 'chaosx\.nr149\.1|famine_incident\.1|migration_incident\.1' common events interface localisation history
```

A read-only parser census of every `constant:category.key` reference across `common`, `events`, `interface`, and `localisation` initially isolated the two relevant missing keys above. After the parent patch, both old-reference counts were zero. A separate `helper = yes` census against all top-level scripted effect/trigger definitions found zero unresolved famine, migration, civilian-transfer, or humanitarian helper calls. These are source checks, not engine/runtime proof.

## Mandatory MCP evidence and limits

Fresh narrow negative-selector calls were completed for `famine_incident.1`, `migration_incident.1`, and `chaosx.nr149.1`, using selector `{ kind: event, eventId: <id> }`:

- all three `hoi4.event_inspect` trace calls returned `status=ok`, `code=EVENT_INSPECTED_PARTIAL`, and one artifact;
- all three matching `hoi4.event_render` overview calls returned `status=ok`, `code=EVENT_RENDERED_PARTIAL`, and four artifacts;
- the qualified result agrees with the current `event_free_validation.md`: there is no renderable in-scope chain for the deliberately absent IDs, but workspace-wide truncation/global diagnostics prevent treating the result as a clean global event validation;
- `hoi4.event_compare` is not applicable because there is no in-scope event baseline or changed event revision.

Current map/GUI MCP artifacts in `mapmode_validation.md` and `completion_report.md` remain the applicable evidence because this auditor made no mapmode or GUI source change. They prove map substrate and static layout inspection/rendering, not active scripted-mapmode execution. The installed routes expose no active-mapmode injection/evaluation surface; that exact missing capability remains a tool blocker.

The required `chaosx_ai_probability_auditor` child was started read-only and then interrupted at the parent's completion boundary before returning final evidence. It made no edit and contributes **no new final probability conclusion**. The current authoritative evidence therefore remains `ai_probability_current.md` and its accepted handoffs: complete declared lists of 10 famine and 18 migration candidates; current flat-fact matrices of 40 rows/15 unresolved and 198 rows/60 unresolved; and distinct before/current comparison evidence with 46 famine and 134 migration unresolved items. Those artifacts are partial score evidence only and do not certify exact eligibility, normalized probability, timing, ranking, dominance, starvation, repetition, cleanup sequence, or exploit safety.

## Recommended next actions

1. Preserve the parent's two constant-reference corrections and include them in the owning implementation review/commit; do not add duplicate constants.
2. Keep every currently blocked adapter fail-closed until its real owner publishes exact causal, people-denominated, replay-safe receipts.
3. Re-run the named probability matrices and same-scenario comparison only after the installed tool can bind special/scoped triggers and dynamic pools, or after a real weighted-source change; do not invent weights to satisfy the analyzer.
4. Use map/GUI tooling again only when it gains active scripted-mapmode execution/injection or when the source changes; retain current static-layout/substrate limits.
5. Leave live HOI4 validation to the user and keep the completion claim **incomplete** until external-owner, MCP/tool, and live-validation blockers are genuinely closed.

## Audit file boundary

This handoff is the only file authored by this auditor. No gameplay, localisation, asset, spreadsheet, specification, permanent documentation, or existing handoff file was edited.
