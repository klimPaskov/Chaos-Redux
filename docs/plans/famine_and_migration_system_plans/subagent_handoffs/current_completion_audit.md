# Current Famine and Migration Completion Audit

Date: 2026-08-25  
Mode: read-only completion audit  
Verdict: **INCOMPLETE**

The current source implements famine and migration as separate mechanics with explicit adapters and a neutral exact-transfer primitive. The event-free design is correct: no famine or migration incident event object, event ID, event-pool entry, replacement Event 149, or pacing event is required. Completion still cannot be certified because accepted owner integrations, probability evidence, mapmode/runtime visual evidence, and catalog wording remain unresolved.

## P0 findings

No P0 implementation defect was confirmed from the current source and authoritative handoffs. In particular, the audit found no current evidence of a second population debit, survivor duplication, route-death double counting, a combined runtime namespace, or a replacement random-event layer.

## P1 findings

### P1-1 — Accepted integrations remain fail-closed because exact owner facts do not exist

This is an implementation-completion blocker, but the unavailable facts must not be replaced with proxies. [completion_report.md](../completion_report.md) and [remaining_owner_receipts.md](remaining_owner_receipts.md) record that generic occupation-law transitions, generic strategic bombing, country-level war/peace callbacks, generic cluster/scenario dispatch, and several event owners do not expose the exact state, actor, positive people/pressure amount, route, cohort, generation, revision, and replay-safe receipt required by `famine_*` or `migration_*` adapters. The Event 005/006, 014/015, 021/033, and 043/050/051/095 handoffs retain the same blocker; Events 118, 120, and 131 have no recoverable source and were not fabricated. This is correctly fail-closed behavior, not evidence that the accepted connections are complete.

Recommended next action: owner packages must expose exact transaction receipts at their authoritative mutation points, after which the existing `famine_adapter_effects.txt` and `migration_adapter_effects.txt` contracts can be exercised without inventing population facts.

### P1-2 — Weighted AI and custom-pool balance is not certified

[ai_probability_current.md](../ai_probability_current.md) and `subagent_handoffs/current_probability_recovery.md` are authoritative. Current MCP discovery found 10 famine and 18 migration score-only candidates, but the installed scenario adapter could not resolve the typed `FROM`, requester, destination, government, war, equipment, compound-trigger, and nested-variable scopes used by the decisions. All rendered scores consequently collapsed to `0.00000`; famine opposition, famine relief-donor selection, and migration destination selection also produced incomplete zero-candidate pool evidence. No valid before/after revision pair or owner-applied weight patch exists, so `hoi4.probability_compare` was correctly not run. This is an MCP fixture/schema and baseline limitation, not proof that AI willingness is zero and not an event-layer gap.

Recommended next action: add supported typed scenario fixtures and declared-pool state mappings, rerun the same named scenarios, then run a same-scenario compare only after a real owner patch creates a valid before/after pair.

### P1-3 — Mandatory event-tool negative evidence is incomplete

Repository source and catalog inspection confirms the intended absence of `famine_incident.1`, `migration_incident.1`, and `chaosx.nr149.1`; the only similar current identifier found was the migration accounting variable `migration_incident_count`, which is not an event object. However, this audit did not obtain a successful `hoi4.event_inspect` plus `hoi4.event_render` artifact for those negative selectors. Initial inspect calls were rejected while discovering the selector schema, and the corrected call was interrupted by the parent-imposed completion boundary; render was therefore not executed. `hoi4.event_compare` is not applicable because no event baseline/changed revision exists. Under the mandatory MCP rule, source-only absence proof is not equivalent evidence.

Recommended next action: run narrow negative `event_inspect` and `event_render` queries for the three retired/nonexistent IDs and retain the resulting no-chain artifacts. Do not add event objects merely to satisfy the tooling.

### P1-4 — Final mapmode and asset runtime evidence remains unavailable

[mapmode_validation.md](../mapmode_validation.md) records `MAP_INSPECTED` evidence for representative states 1, 64, 282, 290, and 452, but the installed map route cannot execute scripted mapmode colors or tooltips. Hardcoded-mapmode GUI inspection modelled no usable dynamic elements and therefore does not certify the two modes' rendered colors, near/far text, hover state, or click regions. Source inspection does confirm exactly two definitions in `common/map_modes/chaosx_state_map_modes.txt`: `famine_state_map_mode` at line 390 and `migration_state_map_mode` at line 571.

The authoritative asset closure records 61 declared final DDS consumers: 50 root-manifest assets, seven report images, and four mapmode buttons. All eight achievements have normal, grey, and not-eligible consumers. Nevertheless, [completion_report.md](../completion_report.md), [category_asset_closure.md](category_asset_closure.md), and [final_asset_audit.md](final_asset_audit.md) leave parent visual review and live runtime consumer validation open. This is unavailable owner/user evidence, not a confirmed DDS or sprite defect.

Recommended next action: retain user-owned live consumer validation and record final parent visual acceptance for categories, report headers, mapmode buttons, achievement triplets, and Deaths presentation.

### P1-5 — Event 149 catalog wording contradicts the binding separation contract

`docs/spreadsheets/chaos_redux_events_catalog.csv:233` currently says: `Retired and absorbed into the shared dynamic famine and migration system.` Event 149 is correctly unavailable and no replacement event row exists, but “shared dynamic ... system” contradicts the binding design that famine and migration are separate mechanics joined only through explicit adapters. [handoff_dispositions.md](../handoff_dispositions.md) marks `final_event_free_spreadsheet_alignment.md` accepted/current, so this stale wording also makes that disposition inaccurate.

Recommended next action: update the authoritative workbook row to describe retirement into the separate famine and migration mechanics through explicit adapters, then regenerate all three export-only CSV files with the repository exporter. Do not edit the CSV directly.

## P2 findings

### P2-1 — The handoff ledger retains a stale probability-route statement

The final “Required project-subagent route blocker” section of [handoff_dispositions.md](../handoff_dispositions.md) says that no callable `chaosx_ai_probability_auditor` route is installed and that direct MCP evidence cannot be represented as independent-auditor sign-off. This conflicts with [completion_report.md](../completion_report.md) and [ai_probability_current.md](../ai_probability_current.md), which identify the fresh isolated probability recovery handoff as authoritative. The probability result remains partial, but the reason is typed-fixture/dynamic-pool resolution and missing before/after evidence, not absence of the audit route.

Recommended next action: reconcile the final ledger paragraph to the current recovery handoff while preserving the partial probability verdict.

### P2-2 — Successful source evidence must remain qualified as source-level

The following surfaces are present and internally aligned, but must not be promoted to live-runtime proof:

- Namespace separation: a scan of `common`, `events`, `interface`, `localisation`, and `history` found no `famine_migration_*` or `fm_*` runtime identifier. Current public names are `famine_*`, `migration_*`, `civilian_transfer_*`, and narrow `humanitarian_*` helpers.
- Independent visibility: `common/decisions/categories/famine_decision_category.txt` and `migration_decision_category.txt` use separate predicates and `visible_when_empty = no`. Famine exposes Food Security, Food Reserves, and Relief Access; migration exposes Displacement Load, Reception Capacity, and Border Policy.
- Exact population accounting: `civilian_transfer_civilians_exact` in `common/scripted_effects/civilian_transfer_effects.txt` measures the actual origin debit, separates route deaths, credits survivors, restores residual credit failure, and commits only exact finalized receipts. `famine_apply_mortality` uses the same one-debit ownership and records `constant:chaos_meter_deaths_reason.famine` as `From famine`; migration route mortality uses `constant:chaos_meter_deaths_reason.forced_displacement` as `From forced displacement` without a second debit.
- Sparse runtime: `common/on_actions/humanitarian_runtime_on_actions.txt` and `common/scripted_effects/humanitarian_runtime_effects.txt` use bounded registered arrays and callbacks; the only broad pass documented is the one-time startup achievement baseline. No recurring whole-world daily/weekly/monthly scan was accepted.
- Eight achievement roots exist in `common/achievements/chaos_redux_achievements.txt`: `famine_break_the_blockade`, `migration_no_one_left_at_the_gate`, `migration_roads_home`, `famine_bread_across_the_front`, `migration_hungry_not_contagious`, `migration_a_place_at_the_table`, `famine_the_grain_stayed_home`, and `migration_the_country_did_not_empty`. Corresponding predicates, localisation, sprites, and asset triplets are present.
- Permanent documentation is split into `docs/systems/famine_system.md`, `docs/systems/migration_system.md`, and `docs/systems/civilian_transfer_system.md`. The accepted improvement review correctly rejects a third mapmode, shared full GUI, replacement event, and extra mechanic family.

These are finished at source/handoff level, not substitutes for the missing MCP, owner-receipt, visual, or live-consumer evidence above.

## Accepted-plan disposition

Accepted/current at source level: namespace separation; two independent hidden decision categories; exactly two always-visible mapmodes; famine severity and population-scaled mortality; exact transfer conservation and Deaths-reason ownership; sparse cohort/reception registries; explicit famine-to-migration and other narrow adapters; Event 149 retirement without replacement event; fifteen historical profiles; six canonical player-facing values; eight achievements; split permanent docs; event-free localisation; and the 61-item declared asset package.

Accepted but not complete: exact-owner integration coverage, weighted AI/custom pools, scripted-mapmode runtime rendering, final asset consumer review, and workbook wording. No accepted improvement item authorizes a combined namespace, combined category, third mapmode, shared full GUI, replacement event, or fabricated owner receipt.

## Completion verdict

**INCOMPLETE.** The current source is substantially implemented and the event-free separation is correct, but completion is blocked by missing exact-owner integrations, partial probability evidence, missing mandatory negative event inspect/render artifacts, incomplete mapmode/asset runtime evidence, and stale Event 149 catalog wording. No P0 conservation or namespace failure was confirmed; the outstanding P1 items are sufficient to prevent a completion claim.
