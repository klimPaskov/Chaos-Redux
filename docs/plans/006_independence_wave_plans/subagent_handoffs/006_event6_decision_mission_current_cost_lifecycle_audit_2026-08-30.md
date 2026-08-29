# Event 006 current decision and mission cost/lifecycle audit

Date: 2026-08-30.

Status: bounded source repair applied; Event 006 as a whole remains HOLD / PARTIAL.

## Scope

This pass reviewed admitted Event 006 decision and mission surfaces for pre-event leakage, cost-versus-requirement mismatches, active-project serialization, and cleanup.

It did not admit a package, change resource amounts, alter AI weights, add a fallback, or redesign a GUI.

## Applied repair

`can_pay_independence_wave_strategic_cost` requires civilian-factory availability, but `independence_wave_decision_pay_strategic` spends only stability plus the diplomatic-standard command-power/transport palette.

Fourteen admitted one-shot decisions used the factory-inclusive `independence_wave_cost_strategic` string despite having no `days_remove`, `days_mission_timeout`, or `civilian_factory_use` modifier to reserve factory capacity.

Their `custom_cost_text` now uses `independence_wave_cost_strategic_instant`.

The new English key separates the three actual spends from the unchanged civilian-factory availability condition as `Capacity`, with the existing texticons and corresponding tooltip/blocked variants.

Changed identifiers:

- `independence_wave_axx_codify_banat_settlement`, `independence_wave_bos_codify_drina_settlement`, `independence_wave_bbx_codify_epirus_settlement`, `independence_wave_mac_codify_vardar_settlement`, `independence_wave_bax_codify_thrace_settlement`, and `independence_wave_tra_codify_danube_settlement` in `common/decisions/006_independence_wave_balkan_decisions.txt`.
- `independence_wave_kar_codify_durable_sovereignty` and `independence_wave_cri_codify_durable_sovereignty` in `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`.
- `independence_wave_rhi_codify_durable_independence`, `independence_wave_bay_codify_durable_independence`, `independence_wave_bay_choose_south_german_restoration`, and `independence_wave_ajx_codify_durable_independence` in `common/decisions/006_independence_wave_rhineland_bavaria_saar_decisions.txt`.
- `independence_wave_bri_codify_durable_independence` and `independence_wave_cat_codify_durable_sovereignty` in `common/decisions/006_independence_wave_western_decisions.txt`.
- `independence_wave_cost_strategic_instant`, `_tooltip`, and `_blocked` in `localisation/english/006_independence_wave_decisions_l_english.yml`.

Before the patch, the four displayed values read as one cost line.

After the patch, the player sees a compact three-value spend line and a separate factory-capacity requirement; gameplay requirements and payment remain identical.

The two unadmitted Iberian analogues remain untouched.

## Lifecycle and leakage findings

- SCN-008 publication remains closed: `chaosx.triggerable_scenarios.80`, the ledger category, and all three ledger controls require `independence_wave_scenario_committed` and reject both failure receipts. A relaunch clears `independence_wave_scenario_ledger_visible` before rebuilding its arrays.
- The five scoped Balkan active-project helpers retain their explicit founding-mission locks: AXX, BOS, BBX, MAC, and BAX each use `has_active_mission` for the named founding mission.
- RUT and KUB founding missions intentionally remain outside their active-project helpers. Their admitted handoffs explicitly define those helpers as the ten paid projects only; no extension was safe to infer here.
- The three FORM-01/02/04 automatic first-session missions omit `cancel_effect` by design: their cancellation condition is progression loss, and setup, ratification, and cleanup effects each remove the mission explicitly.

## Cost, UX, AI, and cleanup notes

- The static crosswalk found 153 generic administration cost rows, all with matching civilian-factory reservation modifiers.
- All 191 Event 006 `custom_cost_text` keys resolve to English localisation; the inspected localisation has a UTF-8 BOM. No literal resource-name fallback was found in Event 006 cost localisation.
- The repaired one-shot strategic actions expose three spendable values plus one separately labelled non-consumed capacity condition, staying within the four-spendable-value budget.
- No AI score or weight changed, so no new probability conclusion is made. Existing mission weights remain outside this cost-only repair.
- No category gained a visible action or simultaneous mission. The Statehood Ledger semantic matrix still reports five mutually exclusive tabs and its existing cleanup contract.

## Validation and MCP evidence

- A focused parser check found exactly 14 instant strategic display rows; all are `fire_only_once`, have no timed lifecycle, call `independence_wave_decision_pay_strategic`, and have no factory-reservation modifier.
- `python -B .tools/audit_event6_allocator.py`, `python -B .tools/audit_event6_scenario_matrix.py`, and `python -B .tools/audit_event6_gui_matrix.py` passed after the patch.
- `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, revision `7a11a434d50b51c80380e5eb8a3aa0d16c985c02f19a8139ac45256b6f72e712`, with its linked report at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79eb2413702a57ebc607c36007a8ed8a9fc1b4a85e882414294309168fdaddbd/abb1d28b425f46afc0abdb49f826157c25f474617295836719d42223f56109ac/event-lint-7a11a434d50b.json`. Workspace-wide helper and lifecycle projection was deferred.
- `hoi4.gui_inspect` and `hoi4.gui_render` were retried for `independence_wave_status_window` under `event6_statehood_ledger_current` and produced no result within 110 seconds and 60 seconds respectively; both calls were terminated. Therefore no fresh GUI layout acceptance or rejection is claimed.

No live game process was launched.

## Remaining issues and boundaries

The wider Event 006 GUI/probability evidence remains partial, and unadmitted packages remain fail-closed.

No simplification or fallback was introduced by this tranche.

Skills used: `chaos-redux-decisions-missions` and `chaos-redux-events`.
