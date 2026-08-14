# Event 006 Current Decision and Mission Gap Audit

Date: 2026-08-14

Mode: bounded read-only audit after the DM-01 material-cost repair and Komi lifecycle, cost, and tooltip repairs.

## Disposition

No new safe source patch was found. No gameplay source was edited by this audit.

The shared Event 006 decision and mission surface remains HOLD / PARTIAL because the central admission boundary and several MCP projections are incomplete, not because this audit found a locally provable decision defect.

The incident-disable concern is not an accepted defect. The accepted evolution contract says that the normal disabled-evolution flag is authoritative for each exact Event 6/type 21/stage row (`docs/events/006_independence_wave/evolutions.md:29`). The live source uses `events_log_disabled_evolution_6_21_1` through `_5` in both the five incident decisions and the five resolution-event triggers. There is no accepted identifier or definition for `events_log_disabled_evolution_6_21_stage`. Adding such a stage-wide guard would require an owner decision about settings semantics, writers, cleanup, and interaction with the Events Log registry; it is therefore not a safe local patch.

The already committed lifecycle repairs `b66899d16` and `7a4e0d7a9` are the correct bounded fix for the prior stale-pending risk. Each incident decision now hides and cancels when its exact evolution row is disabled, its removal endpoint clears the matching pending flag instead of firing a rejected event, and the matching resolution event rejects a stale pending flag while disabled.

## Severity-sorted findings

### P1 — No current accepted-matrix defect safe to patch

DM-01 through DM-10 and the shared incident family were checked against `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` and `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`. DM-01 now has the accepted material commitment at activation, tiered equipment and transport handling, dynamic founding timing, success/failure branches, and cleanup. The remaining shared missions use the existing administration, diplomatic, security, strategic, or material cost helpers and retain their accepted success, timeout, cancellation, and duplicate guards.

The prior safe evolution lifecycle defect is already repaired and has its own receipt at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_evolution_incident_disable_guard_patch_2026_08_14.md`. Repeating that edit would be duplicate work, not a new gap.

### P2 — Evolution disable semantics are a context mismatch, not a source defect

The accepted evolution documentation describes five visible stages, each with one exact Event Log row, and states that disabled stages are skipped without blocking later enabled stages (`docs/events/006_independence_wave/evolutions.md:17-29`). The decision file checks the matching `_1` through `_5` flag in `visible`, `cancel_trigger`, and the removal branch (`common/decisions/006_independence_wave_evolution_incident_decisions.txt:13-230`). The event file checks the same matching flag before each `chaosx.nr6.360` through `.364` option surface (`events/006_independence_wave_evolution_incidents.txt:19-137`). No source, accepted spec, or Event Log documentation defines a stage-wide `_stage` flag.

The parent should only revisit this if the Events Log owner supplies an explicit stage-wide disable contract. Until then, changing five exact flags into a new shared guard risks allowing a disabled row to remain visible or allowing one stage setting to suppress unrelated stages.

### P2 — MCP evidence remains partial and cannot authorize a balance patch

The current shared mission AI inspection returned `PROBABILITY_SOURCE_INSPECTED` with 54 mission candidates, 42 required inputs, zero available candidates, and `poolComplete = false`; the decision AI inspection returned 10 candidates, 79 required inputs, zero available candidates, and `poolComplete = false`. The current evolution option inspection returned 10 candidates, one unresolved item, zero available candidates, and `poolComplete = false`.

Current evolution evidence is also workspace-partial: `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics but deferred workspace-wide helper and lifecycle projections, and `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with the same limitation. These results support source-linked structure only and do not prove gameplay balance, same-tick decision cancellation order, or live Event Log behavior.

### P3 — DM-02 and DM-10 cancellation wording needs owner confirmation, not an isolated trigger edit

The accepted matrix describes DM-02 as ending after completion or government collapse and DM-10 as a one-time treasury chain that closes after its terminal result. Current source cancellation for both missions is `NOT = { is_independence_wave_active_country = yes }` (`common/decisions/006_independence_wave_decisions.txt:118` and `512`), while their availability checks control of `capital_scope` (`:89-97` and `:405-413`). Adding capital-loss or economic-anchor-loss cancellation would be a design choice because it must also select the correct failure effect, sunk-cost treatment, relocation/corruption consequence, and cleanup path. No safe trigger-only patch is authorized by the matrix.

The hidden `available = { always = no }` on DM-03 is intentional: its activation and starter effect make it an automatic founding mission rather than a free selectable decision (`common/decisions/006_independence_wave_decisions.txt:123-140`). It is not a missing reveal path.

### P3 — Shared status-window GUI is not a safe patch surface in this audit

The mandatory read-only GUI inspect for `independence_wave_status_window` found a complete model but global source-graph truncation, 75 visible-overlap diagnostics, one missing item, and unresolved/unsupported references outside the decision-owned status surface. The mandatory render returned a bounded SVG artifact but warned of response truncation. No GUI rewrite was attempted because the diagnostics are not isolated to an accepted decision defect and the shared window is not a new event-owned GUI.

## Decision category lifecycle notes

- Emergency Founding owns DM-01 through DM-05. DM-01 is a hidden starter mission whose material commitment is paid at activation; DM-02 is the selectable revenue-service mission; DM-03 is an automatic registration mission; DM-04 and DM-05 are route-opening missions.
- Government owns DM-06 through DM-10 plus the treasury-backed public-works continuation. The current blocks use centralized cost helpers, factory-use constants, dynamic duration constants, and explicit timeout or removal effects where the accepted matrix requires them.
- Recognition, Security, League, Formables, and High Chaos categories retain their existing targeted scopes, route locks, cooldowns, target validity checks, and cleanup helpers. No broad admission or package behavior was changed here.
- The five evolution incident decisions are paid timed country actions. Their pending flags are generation-scoped and cleared at cancellation, disabled removal, inactive-country removal, and Event 006 origin cleanup. Their resolution events each have two weighted options and use the shared ledger-backed effects.

## Mission quality notes

| Surface | Owner/category/region | Requirement and duration | Success/failure | Duplicate risk and status |
| --- | --- | --- | --- | --- |
| DM-01 `independence_wave_secure_provisional_capital` | Released country / Emergency Founding / capital and supply node | Capital control, supplied assigned divisions, tiered equipment and trains or motorized transport; dynamic fragile-to-armed founding timing | Capacity/security/idea on success; relocation, legitimacy, faction, and government failure on capital or garrison loss | Starter-only, hidden availability, one active founding gate, and cleanup; source-complete after material repair |
| DM-02 `independence_wave_establish_revenue_service` | Released country / Emergency Founding / capital as economic anchor | Capital control, standard administration cost and factory burden, no severe instability; founding duration constant currently 150 days | Revenue-service flags, capacity, and recurring tools on success; salary crisis and negative deltas on timeout | `fire_only_once`, established/crisis flags, and founding-mission gate prevent duplicates; cancellation wording remains owner-review only |
| DM-03 `independence_wave_register_population` | Released country / Emergency Founding / anchor territory and local peace | Auto-start activation after DM-02, light administration cost, hidden selectable state, founding duration | Registration, legitimacy, capacity, and manpower on completion; resistance/autonomy failure on cancellation | Registration/failure flags and one active founding gate; hidden availability is intentional |
| DM-10 `independence_wave_establish_treasury_and_currency` | Released country / Government / capital economic anchor | DM-02 complete, capital control, standard administration cost plus major factory burden, extended duration | Treasury/currency/capacity/construction effects on success; inflation, debt, and instability on timeout | Complete/crisis flags and `fire_only_once`; capital-loss failure semantics need owner decision before any trigger change |
| Evolution incidents `.360`–`.364` | Active Event 006 country / evolution incident category / country scope | Exact stage active, matching Event Log row enabled, paid administration/diplomatic/security/strategic package, standard-to-strategic timer | Two stage-specific ledger-backed options per event | Pending flags, exact disable guards, cancellation, removal cleanup, and generation reset prevent stale or duplicate resolutions |

## Cost and requirement clarity

The DM-01 material-cost repair is already source-complete and is not reopened here. Shared cost triggers and custom cost localisation remain centralized in `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `common/scripted_effects/006_independence_wave_decision_effects.txt`, `common/script_constants/006_independence_wave_decision_constants.txt`, and `localisation/english/006_independence_wave_decisions_l_english.yml`. The existing audit crosswalk reports every custom cost key present; no new missing tooltip or flat-political-power exchange was found in the current shared rows.

## AI validity and route-lock notes

All audited selectable timed missions retain an `ai_will_do` block and route or target checks appropriate to their owner. The five evolution event pools have positive source factors and retain their existing option ordering; the lifecycle guards change eligibility, not option weights. Probability normalization and scenario balance remain unresolved because the MCP candidate pools are incomplete.

## Localisation and tooltip gaps

The current decision localisation crosswalk reports all expected custom cost keys present. DM-01 text reflects its material commitment and transport requirement. No safe localisation-only correction was found. A stage-wide disable tooltip cannot be added without first defining the stage-wide setting contract, so no tooltip patch is recommended.

## Cleanup and exploit-risk notes

The current lifecycle closes the previously observed disabled-evolution stale-pending path: disabled or inactive removal clears the pending flag, and an already-queued resolution event fails its exact stage guard. Existing generation and origin cleanup remains defense in depth. DM-01 material is sunk at activation as specified, preventing refund loops. The remaining DM-02/DM-10 anchor-loss question is a failure-semantics decision, not a demonstrated exploit.

## Mandatory evidence

Required offline wiki pages, vanilla decision documentation, and relevant vanilla decision precedents were read before this audit. Required decision and mission probability inspection was performed against workspace `mod_chaos_redux_ea3b2d67c2c0`.

Current shared mission probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d2db102151e09ad515e867e2bfbb2df70069816741b21a6e23fd49281f30f88/bcd11c2ba12b48df9e9ad1b960b336a1467605d8900fe4a162d2d2317dd2d19c/probability-inspect-efc4d478e6f2.json`.

Current shared decision probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48e6446425d09136b75cd3aa37bed85cd8d35b1ce4f193c35391f304be801390/09c8965cfac37c4308892cd7a94fc25cb5a8ef8b98ff29729049e6087c14fc04/probability-inspect-efc4d478e6f2.json`.

Current evolution option probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44d33c21f6620974da1856ab9e845cb50699e12141fc52a9ed1b9ee16d4c84c0/6feb3afd698264fb03be76617dfa0f1c8bde73afe0a45f4d165d0471ee1abc75/probability-inspect-4e5be8dc153d.json`.

Current evolution event inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca32cab9c614e2698cdd1fc51eb8d16d7df31c840c61068ed6b2421052113457/eccb12ee5ede038cc1dcf9c34222447915aec6edfff01d7146a92c8b0b990a1c/event-scan-741883f50501.json`.

Current evolution event render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4e0dabe2498154aee2d47297b1a19666d0c00977fc978d8ca75d263f83410ad/23dbff61009bb3766827b4e1dc2defc856351aff06acc226417bc1c01d15964c/event-state-741883f50501-manifest.json`.

Shared status-window GUI inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/954534e7a8b94d69bd7237aa9e2f090653a43d8644f528541426177177f52633/b469a521dea730c750786d7608704203d0b16e0660d0d4dcd9fe3749ecb0860b/gui-inspect.057fc56363e52f92.json`.

Shared status-window GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7151f87950fd10f39ae7cf64c5dc04fee0744ed2835a3358531571452bcdae64/e5fce1901a1794d53c872a5e5aa50b0418c3742d6d39c4d66c78939fb7420f55/independence_wave_status_window-full.svg`.

## Validation and blockers

Static source review, matrix cross-check, offline wiki and vanilla documentation review, decision/mission probability inspection, event inspect/render, and GUI inspect/render were completed. Live HOI4 execution, save/load, and in-game Event Log observation were skipped because this repository delegates live consumer validation to the user and the MCP evidence is intentionally partial.

No source, localisation, GUI, admission, spreadsheet, asset, or central adapter files were changed by this audit. The only intended artifact is this handoff.

Recommended next step: if the product owner wants a stage-wide disable switch, first add the exact setting contract and migration/cleanup rules to the accepted evolution spec, then assign a dedicated Event Log owner to patch the shared registry and all five incident surfaces together. Until that authority exists, keep the current exact per-stage guards and do not widen admission.
