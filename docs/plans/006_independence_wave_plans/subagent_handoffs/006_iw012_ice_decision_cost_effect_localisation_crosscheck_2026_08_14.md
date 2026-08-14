# IW-012 ICE decision and mission cost/effect/localisation cross-check

Date: 2026-08-14.

## Scope and disposition

Superseding owner pass: the two ICE `modifier.civilian_factory_use` fields now use file-scoped `@` mirrors for the shared light and standard values, matching the established Event 006 decision pattern because this field rejects the shared `constant:` form. The Shipping Registers tooltip also names the Coastwatch Readiness ledger already changed by its effect.

This was a bounded, read-only cross-check of the current IW-012 ICE decision and mission source against the accepted package specification, current shared material-cost helpers, package effects, and English localisation.

No central admission, shared decision, or gameplay effect/trigger/AI source was changed in this pass; the selector compatibility and tooltip disclosure are the two narrow owner-applied corrections recorded below.

The six ICE project selectors and the harbour mission remain source-backed. The only selector change is parser compatibility for the two administrative factory modifiers; cost values, payment effects, timing, AI scores, and admission are unchanged.

The Shipping Registers tooltip omission is resolved by naming Coastwatch Readiness alongside the four already-disclosed ledgers.

## Source crosswalk

| ID | Cost selector and factory burden | Payment effect | Duration | Contract result |
| --- | --- | --- | --- | --- |
| `independence_wave_ice_reconcile_shipping_registers` | `can_pay_independence_wave_administration_light_cost`, `independence_wave_cost_administration_light`, one civilian factory | `independence_wave_decision_pay_administration_light` | `independence_wave_ice_duration.short_project` = 120 | Matches the administrative light contract. |
| `independence_wave_ice_charter_municipal_council` | `can_pay_independence_wave_administration_standard_cost`, `independence_wave_cost_administration_standard`, two civilian factories | `independence_wave_decision_pay_administration_standard` | `standard_project` = 180 | Matches the administrative standard contract. |
| `independence_wave_ice_expand_coastwatch` | `can_pay_independence_wave_security_standard_cost`, `independence_wave_cost_security_standard`, no factory modifier | `independence_wave_decision_pay_security_standard` | `standard_project` = 180 | Matches the security standard contract. |
| `independence_wave_ice_negotiate_north_atlantic_compact` | `can_pay_independence_wave_diplomatic_standard_cost`, `independence_wave_cost_diplomatic_standard`, convoy-or-train payment | `independence_wave_decision_pay_diplomatic_standard` | `compact_treaty` = 300 | Matches the diplomatic standard contract. |
| `independence_wave_ice_settle_former_host_charter` | `can_pay_independence_wave_diplomatic_standard_cost`, `independence_wave_cost_diplomatic_standard`, convoy-or-train payment | `independence_wave_decision_pay_diplomatic_standard` | `long_project` = 270 | Matches the diplomatic standard contract and host-target gate. |
| `independence_wave_ice_declare_armed_neutrality` | `can_pay_independence_wave_security_major_cost`, `independence_wave_cost_security_major`, no factory modifier | `independence_wave_decision_pay_security_major` | `standard_project` = 180 | Matches the security major contract and route-lock guard. |

The persistent `independence_wave_ice_hold_the_harbour` mission has no material payment selector, uses `independence_wave_ice_duration.harbour_crisis` = 1,440 days, and resolves on the stable-state predicate or fails on package loss, capital loss, former-host loss, or timeout.

All five current ICE cost selectors have the generic base, `_tooltip`, and `_blocked` localisation keys in `localisation/english/006_independence_wave_decisions_l_english.yml`.

The package constants and project durations match the IW-012 package document and the accepted registry/research rows for `ICE`, anchor state 100, and reservation group `RG-100`.

## Constant-macro receipt

The current file-scoped macro additions are source-backed mirrors, not new tuning.

`common/decisions/006_independence_wave_ice_decisions.txt` maps its factory-use macros to the shared decision constants: light = 1 and standard = 2, matching `independence_wave_decision_cost.civilian_factory_light` and `civilian_factory_standard`.

`common/scripted_effects/006_independence_wave_ice_package_effects.txt` maps its host-AI strategy macros to the ICE constants: trade = 25, diplomacy = 35, war preparation = 20, compact diplomacy = 40, and compact relations = 30, with cleanup values of -25, -35, -20, -40, and -30.

These values match `independence_wave_ice_ai` in `common/script_constants/006_independence_wave_ice_constants.txt` and preserve the existing target-scoped AI behavior; no balance target or selector was invented.

The package narrative at `docs/events/006_independence_wave/iw012_ice_package.md:26` says that Coastwatch expansion spends Command Power, but the current security-standard trigger, payment effect, and localisation contract charge manpower, Army Experience, infantry equipment, and support equipment only.

This is a documentation discrepancy, not a gameplay mismatch: the accepted IW-012 specification delegates to the existing security-standard cost, and the current source consistently implements that contract.

## One concrete safe local finding

`independence_wave_ice_reconcile_shipping_registers` adds `independence_wave_ice_coastwatch_delta = constant:independence_wave_ice_value.minor_gain` at [common/decisions/006_independence_wave_ice_decisions.txt:77](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_ice_decisions.txt:77).

Its custom effect text at [localisation/english/006_independence_wave_ice_l_english.yml:16](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\localisation\english\006_independence_wave_ice_l_english.yml:16) names Port Authority, Civic Cohesion, Shipping Security, and Compact Support, but omits Coastwatch Readiness.

Owner-applied one-line localisation-only repair: `Coastwatch Readiness` was added to `independence_wave_ice_shipping_registers_effect_tt`.

This is safe without a design choice because it discloses an already executed ledger delta, changes no trigger, payment, AI weight, effect, or admission path, and requires no new key.

The municipal tooltip also summarizes only part of its multiple ledger changes, but expanding that text would be a broader wording decision; it is recorded as a non-blocking clarity follow-up rather than a second patch recommendation here.

## Lifecycle and mission notes

The ICE category contains one persistent survival mission and six one-at-a-time material projects.

`has_independence_wave_ice_active_package_project` intentionally excludes the harbour mission so the six paid projects can run while the survival deadline remains visible.

The shared `has_independence_wave_active_founding_mission` helper currently names `independence_wave_ice_hold_the_harbour`, so downstream founding missions see the ICE deadline as active.

The shared DM-01 automatic-start gate in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` does not itself consume that helper before starting the provisional-capital mission.

Whether this can overlap the harbour mission on the same refresh depends on the shared activation order and remains a central lifecycle/runtime owner issue from the earlier IW-012 audit.

It is not a safe ICE-local patch and is intentionally not changed here; resolving it requires choosing whether the harbour deadline replaces or coexists with DM-01.

The local project cancellation guards cover package removal and capital loss, the former-host charter additionally covers former-host disappearance and war, and Armed Neutrality additionally cancels after a government route lock.

ICE cleanup removes the harbour mission, all six decisions, package ideas, lifecycle flags, and five ICE ledger variables.

## AI, GUI, and evidence boundary

No AI weight or probability-bearing source was changed or rebalanced in this cross-check.

The separate IW-012 package audit owns any new probability MCP pass; no duplicate broad probability inspection was run here.

The prior ICE decision-AI re-audit remains the relevant source receipt, but it is not a new current probability result.

No decision-owned scripted GUI is attached to these surfaces, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable.

Static checks covered the seven ICE decision/mission IDs, cost/effect selector pairing, duration constants, direct and generic localisation key resolution, and current shared founding-mission references.

No live game, save/load, allocator, or runtime activation-order validation was run.

## Current MCP refresh

The current read-only map inspection for state `100` returned `MAP_INSPECTED` with state membership, geometry, and network checks passing. The aggregate locator check remains false because the workspace contains unrelated building/port-position diagnostics; this is not an ICE-state failure. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7164e6928fcc259dc675de2607ec5604fb42ce3d8ef47b937e3ffc6649e11a91/e07a0ab2e2f07b551e70418bb3e430ed46e183134c8cf9704bc43113f0934a75/map-inspect.2bbb0ec306dc6906.json`.

The current `iceland_tree` focus inspection returned `FOCUS_INSPECTED` for the preserved vanilla carrier, with 89 focuses and 104 connectors. The result is not a focus PASS because the viewer reports missing vanilla icon references and 193 aggregate diagnostics; those are broader carrier/workspace issues, not new ICE overlay nodes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2682740392515224f41380c7f851fdf4aacc609b0f4a3a7bf990355f44c4866/458ac01963430ce2b5a9136c029a630be9e5f5bc5faaf0454700d42d3b86cf3b/focus-inspect.464595bb80570dc8.json`.

The current focused Event 006 state-flow inspection for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`. Helper/lifecycle projection remains deferred in the large workspace, so this is structural evidence only. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9a1cb21e545f652c0834806605d617135593fa24be7d2e30881be34a0b3cd74/83201ffd5066e07d8aea6834e7fe87e6bffd1255602c7e369824791e4cc7fa3e/event-state_flow-741883f50501.json`.

The paired current renders completed as `MAP_RENDERED`, `FOCUS_RENDERED`, and `EVENT_RENDERED_PARTIAL`. The map state render passed its offline artifact checks (`map-state.png` SHA `0550658fb9a890f6226150e4b0ff98fd5cfcbdbe6a75da2372173d4cf4d8dacc`). The Iceland focus render retained layout hash `519ea6ed46008ccdaca74b3938aa42abcd45a1b88feb080bf224a21ed17b3e8c` but inherited the missing vanilla-icon diagnostics. The Event state render remains structural-only for the same deferred workspace projection; its revision-matched SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6467bda29743f52ac99d589a1b4082ad57cebe08c46426b35ba735beae82f741/ea38c9286e0143ebb2ba898b4b2e0254ef12b31fb68387ee825e86213cada8fe/event-state-741883f50501.svg`.

## Final disposition

The bounded owner corrections are complete: two parser-compatible factory modifiers and the one-line Shipping Registers tooltip disclosure. No gameplay effect, trigger, AI, central adapter, attestation, or Join behavior changed.

The ICE package remains statically covered but runtime-unproven. The DM-01/harbour activation-order question remains explicitly blocked on shared lifecycle ownership and runtime evidence, not on an ICE cost or effect contract.
