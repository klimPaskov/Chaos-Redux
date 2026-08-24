# Event 014 seven-decision cost contract handoff

Date: 2026-08-24.

Scope: the seven over-budget Event 014 decisions identified by `event014_decision_gui_audit_2026-08-24.md`.

This tranche changes only decision availability presentation, the matching transaction wrappers, and matching Event-014 English semantic strings. It does not change AI weights, probability logic, missions, categories, GUIs, assets, shared event surfaces, or tuning constants.

## Changed files and identifiers

- `common/decisions/014_cannibalism_decisions.txt`: wrapped `cannibalism_wendigo_press_terminal_hunt` and `cannibalism_muster_wendigo_pack_from_enemy_death_receipt` availability checks in custom requirement tooltips, matching the existing hidden triggers and vanilla decision syntax.
- `common/scripted_effects/014_cannibalism_effects.txt`: changed only the seven transaction call sites listed below; the shared payment helpers and the concurrent custom-unit edits in this file were not normalized or rewritten.
- `localisation/english/014_cannibalism_l_english.yml`: removed readiness-only inputs from the seven cost lines, added two missing requirement keys, and aligned descriptions/effect tooltips with the actual payment paths. Final icon-first presentation remains a separate localisation tranche.
- `common/scripted_triggers/014_cannibalism_triggers.txt`: inspected but intentionally unchanged because every route, target, reserve, receipt, and equipment-held gate remains required.
- `common/script_constants/014_cannibalism_constants.txt`: inspected but intentionally unchanged because existing dynamic cost and gate constants still provide the route-specific difficulty and readiness thresholds.

## Before and after contracts

| Decision | Before | After consumed costs | Retained non-consumed requirements and rationale |
| --- | --- | --- | --- |
| `cannibalism_unified_mobile_consumption` | State population, Command Power, trucks, trains, support equipment, convoys, and fuel were all presented and passed into the shared state-consumption payment helper. | State population, Command Power, trucks, and trains. | The existing dynamic support-equipment, convoy, and fuel gates remain in `cannibalism_unified_can_pay_mobile_consumption`; the wrapper passes zero for those three payment temps. This preserves mobile-route readiness and host/oceanic reserve checks without charging a fifth through prose. |
| `cannibalism_unified_build_silent_anchorage` | Manpower, support equipment, convoys, fuel, and Navy Experience. | Manpower, support equipment, convoys, and Navy Experience. | The existing fuel gate remains in `cannibalism_unified_can_pay_silent_anchorage`; the anchorage effect no longer calls the fuel payment helper. Coastal ownership/control and inactive-anchorage checks remain target requirements. |
| `cannibalism_unified_launch_air_interdiction` | Small airframes, transport aircraft, support equipment, fuel, and Air Experience. | Small airframes, transport aircraft, support equipment, and Air Experience. | The air-program foundation, capacity stage, aircraft-held checks, and fuel readiness gate remain in `cannibalism_unified_can_pay_air_operation`; only the fuel payment call was removed. |
| `cannibalism_unified_destroy_coalition_hub` | Support equipment, trucks, fuel, Command Power, and Army Experience. | Support equipment, trucks, Command Power, and Army Experience. | Coalition-route, live-war target, target-capitulation, target cooldown, and fuel readiness checks remain in `cannibalism_unified_can_pay_counterwar_operation` and its target trigger. The effect no longer pays fuel. |
| `cannibalism_unified_convert_counterwar_pressure` | Support equipment, trucks, fuel, Command Power, and Army Experience. | Support equipment, trucks, Command Power, and Army Experience. | Counterwar route, hostility threshold, equipment-held checks, and fuel readiness remain in `cannibalism_unified_can_pay_counterwar_conversion`; the effect no longer pays fuel. |
| `cannibalism_wendigo_press_terminal_hunt` | Larder, Command Power, infantry equipment, support equipment, and fuel. | Larder, Command Power, infantry equipment, and support equipment. | Active terminal target, press cooldown, and fuel readiness remain in `cannibalism_wendigo_can_pay_terminal_hunt_press_cost`; the press effect no longer pays fuel. The decision now exposes a concise requirement tooltip instead of a raw availability block. |
| `cannibalism_muster_wendigo_pack_from_enemy_death_receipt` | Enemy-loss receipt, state population, Larder, infantry equipment, and support equipment. | Enemy-loss receipt ledger payment, state population, Larder, and infantry equipment. | Wendigo route, pack-training flags, live template, anchor target, population, cooldown, capacity, and support-equipment reserve remain checked. The receipt is deliberately still consumed by the ledger after exact population consumption; making it a permanently non-consumed requirement would let one receipt create a new pack after each cooldown. The requirement tooltip states this distinction explicitly. |

Every row now has no more than four truly consumed resource types. Route, target, reserve, template, capacity, and equipment-held conditions are not passed through a hidden fifth payment path.

## Transaction evidence

- `cannibalism_unified_execute_mobile_consumption` still delegates exact state population handling to `cannibalism_unified_execute_state_consumption`, but sets support, convoy, and fuel payment temps to the existing zero constant.
- `cannibalism_unified_execute_silent_anchorage`, `cannibalism_unified_execute_air_operation`, `cannibalism_unified_execute_counterwar_operation`, and `cannibalism_unified_execute_counterwar_conversion` retain their direct payment helpers for the four selected inputs and no longer set or pay the fuel temp.
- `cannibalism_wendigo_press_active_terminal_hunt` retains the same four payment helpers and no longer sets or pays the fuel temp.
- `cannibalism_muster_wendigo_pack_from_enemy_death_receipt_effect` still requires exact Deaths population application before subtracting one receipt and paying Larder and infantry equipment. Support equipment is checked by the affordability trigger but is not paid.
- The two Wendigo decisions now use `custom_trigger_tooltip` with `hidden_trigger`, matching the vanilla `common/decisions/BUL.txt` pattern and keeping the actual scripted trigger authoritative.

## Balance and exploit rationale

Fuel was selected as the readiness-only input for the five applicable operations because each route already has a dedicated fuel affordability gate and the transaction formerly paid it directly. Retaining the gate preserves operational readiness while removing the fifth consumed type from the contract.

Mobile support and convoy values are dynamic route-profile reserves, so their checks remain in place even when their payment temps are zeroed. This preserves host transport and oceanic-hulk readiness without changing route flags, surcharges, or constants.

The Wendigo enemy-loss receipt is not treated as a readiness reserve. It is a bounded ledger payment with a per-enemy cap, pool cap, state cooldown, and receipt cooldown. Removing its subtraction without adding a per-receipt consumption ledger would create a repeatable empty-pack acquisition loop, so this tranche removes support equipment instead and documents the intentional receipt consumption.

## Validation

Source review traced each decision to its scripted trigger and completion effect, then counted the payment helpers in each transaction wrapper. The post-change count is four for every listed decision.

The retained trigger contracts were re-read at `common/scripted_triggers/014_cannibalism_triggers.txt:500-512`, `:620-640`, `:4311-4475`, and the mobile block at `:4137-4145`; no route, target, reserve, receipt, or equipment-held check was removed.

The exact-effect scan confirmed that only the intended fuel/support payment calls were removed or zeroed in the seven wrappers, while `cannibalism_unified_execute_state_consumption` and all unrelated transaction helpers remain untouched.

The new `custom_trigger_tooltip` blocks were checked against the vanilla `BUL.txt` decision precedent and the local Decision Modding, Triggers, Effects, Localisation, Modifiers, Scopes, Data Structures, and AI Modding wiki pages, plus vanilla `documentation/triggers_documentation.md`, `effects_documentation.md`, and `script_concept_documentation.md`.

No AI or probability surface changed, so no `chaosx_ai_probability_auditor` or `hoi4.probability_compare` pass was required for this tranche. No GUI, mission, category, or live HOI4 validation was performed because those surfaces are explicitly out of scope and concurrent GUI work must remain isolated.

## Remaining issues and follow-up

- The later localisation tranche must convert the remaining seven cost lines and requirement text to icon-first presentation, including valid icons for custom Larder, population, and receipt values; this handoff intentionally leaves that presentation work separate.
- Current GUI MCP timeout evidence, shared GUI surfaces, category density, and mission concurrency remain outside this tranche. The emergency-reinforcement workshop contradiction was resolved separately in commit `3c211a256` and is not part of this seven-cost commit.
- If the parent design requires enemy-loss receipts to be permanently non-consumed requirements, a separate ledger design must add one-use receipt identity or an equivalent monotonic usage counter before changing the subtraction; simply deleting it is unsafe.

Simplifications: five routes deliberately convert fuel readiness from a payment into a non-consumed gate, mobile additionally converts dynamic support/convoy reserves the same way, and muster converts support equipment while retaining its bounded receipt ledger payment. No numeric constants, AI weights, route locks, mission behavior, category density, GUI, or unrelated decisions were changed.
