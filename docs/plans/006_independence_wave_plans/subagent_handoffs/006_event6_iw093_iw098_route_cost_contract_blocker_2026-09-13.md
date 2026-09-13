# Event 006 IW-093/IW-098 route-opening cost audit — 2026-09-13

Status: NO-CHANGE / DESIGN BLOCKER for parent review. This bounded audit inspected the six IW-093/IW-098 route-opening decisions and made no gameplay, AI, scripted-effect, scripted-trigger, or localisation source change. The only write in this tranche is this handoff. Nothing was staged or committed.

## Scope and reviewed contract

The scope is limited to `independence_wave_iw093_royal_confederacy_conference`, `independence_wave_iw093_constitutional_cabinet_conference`, `independence_wave_iw093_veterans_emergency_conference`, `independence_wave_iw098_sultanic_federal_compact`, `independence_wave_iw098_northern_constitution_compact`, and `independence_wave_iw098_frontier_command_compact` in `common/decisions/006_independence_wave_iw093_iw098_decisions.txt:100-288` and `:697-857`.

Required references were read before review: `AGENTS.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; the accepted Event 006 Part 3 mechanics and decisions specification; the accepted IW-093/IW-098 decision/mission handoff; the offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, and AI; and relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

The generic Part 3 contract says that no major family should use one flat political-power cost and that costs should scale through concrete state, military, diplomatic, and legitimacy factors. The accepted IW-093/IW-098 handoff separately defines each route conference as a 70-day, 100-political-power action, with the Asante veterans emergency route also carrying a command-power ledger. The source and localisation currently implement the latter owner-defined contract.

## Severity-sorted findings

1. P1 — No safe compact-family replacement exists in the current owner-defined registry. The five ordinary route openings use only the native `cost = constant:...conference_political_power_cost` field, and the veterans route uses that same native PP cost plus its existing command-power ledger. The existing Event 006 decision-cost registry and compact families cover command power, equipment, trains, convoys, fuel, manpower, factory occupancy, stability, war support, and army experience, but no route-conference political-power row and no exact payment mapping for these six decisions. Converting the six actions would require inventing resource amounts, adding new debit and cleanup wiring, and changing accepted payment semantics.

2. P1 — Removing the native `cost` field or replacing it with a guessed existing row would silently delete or alter the accepted political-power payment. That would violate the explicit task constraint and could create a free route-opening action if no matching debit is added. No gameplay edit is authorized until the parent or design owner supplies a replacement amount and confirms the intended resource family.

3. P2 — The generic Part 3 “no flat political power” rule and the accepted IW-093/IW-098 route-conference contract are inconsistent. This is a specification ownership issue, not a local tooltip issue. The parent should either record the route conference as an accepted narrow PP exception or approve a new route-specific compact payment contract before asking for implementation.

4. P2 — The required `chaosx_ai_probability_auditor` route is not callable in this runtime. Direct `hoi4.probability_*` tools are exposed, but they are not a substitute for the named auditor route. No AI weight was changed and no probability comparison is claimed.

## Current decision contract

| Decision | Native cost | Custom cost and payment | Duration | Route and AI summary |
| --- | --- | --- | --- | --- |
| `independence_wave_iw093_royal_confederacy_conference` (`:100`, cost `:102`) | 100 PP through `independence_wave_iw093.conference_political_power_cost` | No `custom_cost_trigger` or `custom_cost_text`; native decision debit occurs once when selected | `independence_wave_iw093.conference_days` = 70 | Royal route lock helper; low base AI with a major factor at the royal balance threshold |
| `independence_wave_iw093_constitutional_cabinet_conference` (`:158`, cost `:160`) | 100 PP through the same IW-093 constant | No custom payment helper or custom cost row | 70 | Constitutional route lock helper; low base AI with balance and host-settlement gates |
| `independence_wave_iw093_veterans_emergency_conference` (`:217`, cost `:219`) | 100 PP through the same native field | Existing 50 command-power custom row `independence_wave_iw093_cost_veterans_conference`; `independence_wave_iw093_begin_paid_decision_transaction` debits and records it once | 70 | Severe host threat and emergency route lock; low base AI with a major severe-threat factor |
| `independence_wave_iw098_sultanic_federal_compact` (`:697`, cost `:699`) | 100 PP through `independence_wave_iw098.conference_political_power_cost` | No custom payment helper or custom cost row | `independence_wave_iw098.conference_days` = 70 | Sultanic route lock helper; low base AI with the sultanic balance gate |
| `independence_wave_iw098_northern_constitution_compact` (`:752`, cost `:754`) | 100 PP through the same IW-098 constant | No custom payment helper or custom cost row | 70 | Constitutional route lock helper; low base AI with civic-balance and frontier-security gates |
| `independence_wave_iw098_frontier_command_compact` (`:808`, cost `:810`) | 100 PP through the same native field | No custom payment helper or custom cost row | 70 | Severe host threat and emergency route lock; low base AI with a major severe-threat factor |

The IW-093 and IW-098 constants are declared in `common/script_constants/006_independence_wave_constants_registry.txt` as `conference_political_power_cost = 100` and `conference_days = 70`. The package route helpers in `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` mutually exclude the other route flags and allow only undecided or matching government-route inputs.

## Decision category lifecycle notes

The Asante and Sokoto categories are ordinary decision categories, not dedicated scripted-GUI windows. Their visibility is gated by the exact package setup predicate, package decision-unlock flags, mutually exclusive route flags, and the package-level cancellation flag. Each ordinary route has one shared active-conference guard, and each emergency route additionally checks its severe-host-threat gate. The decision `complete_effect` initializes package state and marks the conference active; `remove_effect` resolves the route and clears the active flag; `cancel_effect` clears the active flag and records cancellation. The native PP debit is handled by the decision engine before the effect body, so no second PP debit appears in the helper effects.

The IW-093 veterans path additionally opens and closes the existing paid transaction ledger. Its `remove_effect` and `cancel_effect` both call `independence_wave_iw093_close_paid_decision_transaction`, so the command-power commitment is cleaned without a refund. The other five route openings do not use a ledger because they have no custom material payment.

## Cognitive-load notes

- Visible primary actions: each category exposes three route-opening decisions plus the package's material and settlement actions. The route subset is below the six-action ceiling, and the shared active flag prevents concurrent conferences.
- Active missions: these six entries are timed decisions rather than separate missions. At most one route conference is active per package through `independence_wave_iw093_conference_active` or `independence_wave_iw098_compact_conference_active`.
- Player-facing values: the category descriptions expose four package values each, and route success tooltips name the balance/value change. The values have clear labels and route consequences.
- Text density: the route descriptions and start/success/failure/cancel tooltips are short and state the 70-day timer, route consequence, and non-refund behavior. No raw trigger wall is exposed.
- Cost significance: native PP is visible through the engine's built-in decision cost display and is named in the descriptions/start tooltips. The veterans custom row is icon-first and shows command power. A new compact row cannot be selected safely until its amounts and semantics are owner-defined.

## Mission and timed-action quality notes

These are timed decisions, so the table records their mission-equivalent lifecycle rather than inventing mission ids.

| Owner / category | Region and anchor | Requirement | Duration | Success | Failure / cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| IW-093 Asante Compact | Kumasi, state 274 | Exact IW-093 package, decision unlock, matching route helper, no active conference; veterans also requires severe host threat and command power | 70 days | Route lock helper records the selected government route and the result tooltip reports the balance/authority outcome | Route closure or lost emergency threat records failure; cancellation records the cancelled flag; native PP and command commitments are not refunded | Shared active flag plus mutually exclusive route flags and terminal cancellation flag |
| IW-098 Sokoto Compact | Sokoto, state 902 | Exact IW-098 package, decision unlock, matching route helper, no active conference; frontier command also requires severe host threat | 70 days | Route lock helper records the selected government route and the result tooltip reports the balance/security outcome | Route closure or lost emergency threat records failure; cancellation records the cancelled flag; native PP is not refunded | Shared active flag plus mutually exclusive route flags and terminal cancellation flag |

## Cost and requirement clarity

The spendable-cost count is one native PP type for royal, constitutional, sultanic, northern, and frontier route openings, and two types for the veterans route (native PP plus command power). No target exceeds the four-type ceiling. The veterans normal, blocked, and tooltip triplet is present at `localisation/english/006_independence_wave_iw093_iw098_l_english.yml:44-46` and uses `£command_power`; the native PP charge is not hidden in a secondary scripted effect. The five other route decisions have no custom-cost triplet because their only spendable cost is the engine-native PP field.

The existing shared compact family `independence_wave_cost_diplomatic_light` would charge command power plus a dynamic train/convoy burden and contains no PP. The security, strategic, administration, corridor, integration, and formable families likewise encode different resource sets and payment helpers. Reusing any of them would change the accepted payment rather than represent the current one. Reusing the veterans command-only row for all six would add an unapproved command-power charge to five routes. Therefore no cost, trigger, payment, tooltip, AI hint, or localisation edit was made.

## AI validity and route-lock notes

The six AI blocks use low base priorities and route-specific major modifiers. Royal and sultanic routes check the corresponding balance maximum; constitutional routes check the corresponding balance minimum plus host settlement or frontier security; emergency routes check severe host threat. The route-lock helpers enforce package identity, opposing-route exclusion, and undecided-or-matching government-route input. No dead-country target, country-target scan, closed route, or impossible border target is used.

No AI source change was made. The exact blocker for the mandatory audit route is the absence of a callable `chaosx_ai_probability_auditor`; the direct HOI4 probability tools visible in this runtime do not satisfy the required named-worker route, so no baseline/compare artifact is claimed here.

## Localisation and tooltip gaps

All six title, description, start, success, failure, and cancel keys are present in `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`. The start strings state the 70-day duration and that the political-power commitment is made at session start; the veterans start string also states the command commitment. The failure and cancellation strings state that commitments are not returned. No missing custom cost triplet was found for the only custom-cost decision.

The remaining localisation concern is contractual rather than missing-key: a future compact replacement must add normal, blocked, and tooltip rows with texticons for every spendable resource, and the start/failure/cancel text must match the new payment. It must not conceal native PP by simply deleting the native row from prose.

## Cleanup and exploit-risk notes

Native PP is consumed once by the decision engine at selection, with no duplicate debit in `complete_effect`, `remove_effect`, or `cancel_effect`. The veterans command ledger is debited once by the paid transaction helper and cleared on resolution/cancellation. Route locks and terminal cancellation/failure flags prevent repeat openings or overlapping conferences. No free-unit, equipment-farming, war-goal, core, or refund loop was found in the inspected six decisions.

Replacing the native field without an owner-defined payment helper would create a free-action or hidden-cost risk. A safe future conversion must keep the exact 70-day duration, duplicate the inclusive affordability predicate in `available` and `custom_cost_trigger`, debit exactly once in `complete_effect`, keep all custom cost rows icon-first, and preserve the existing route and cleanup lifecycle.

## Recommended fixes

1. Parent/design owner: resolve the Part 3 generic flat-PP rule against the accepted IW-093/IW-098 route-conference contract. Either document these six conferences as a narrow accepted PP exception or supply exact replacement resource amounts and the intended shared family.
2. If replacement is approved, update each decision's `available`, `custom_cost_trigger`, `custom_cost_text`, `complete_effect`, normal/blocked/start/failure/cancel tooltips, and AI hint together. Keep the 70-day constant and route-lock behavior unchanged.
3. Route any approved AI weight change through `chaosx_ai_probability_auditor` for baseline and same-scenario comparison. The current runtime lacks that callable route, so no AI patch is proposed.
4. Keep the shared `independence_wave_status_window` GUI outside this handoff. These six entries are ordinary decision surfaces and do not own a dedicated scripted GUI.

## Changes, validation, and blockers

Changed files in this tranche: only this handoff. Changed decision, mission, scripted-GUI, or localisation ids: none. Before behavior and after behavior: unchanged because no safe owner-defined payment replacement exists.

Meaningful validation run: focused source assertions confirmed all six native PP constants, all six 70-day constants, the veterans-only custom-cost/helper path, six AI blocks, and all title/description/start/success/failure/cancel localisation keys. `python .tools/audit_event6_allocator.py` passed and reported the Event 006 allocator, package adapter, pre-event, ordering, and reservation checks.

Skipped meaningful validation: `chaosx_ai_probability_auditor` baseline/compare was skipped because the named route is unavailable; direct probability tools were not treated as an equivalent fallback. `hoi4.gui_inspect` and `hoi4.gui_render` were not run because no dedicated scripted GUI is owned by these decisions; the shared status window is outside this bounded scope. No live game run was performed per repository instructions.

Simplifications, omissions, and blockers: no gameplay simplification or fallback was introduced. The six native PP costs remain an unresolved contract exception until the parent or design owner supplies an accepted replacement or explicitly preserves the exception. No plan handoff was written because implementation would be a broader cost-contract decision rather than a narrow local repair.
