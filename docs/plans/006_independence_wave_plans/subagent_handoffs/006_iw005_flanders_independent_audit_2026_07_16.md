# IW-005 Flanders independent gameplay audit

Date: 2026-07-16
Auditor: independent read-only gameplay audit subagent
Scope: the IW-005 Flanders overlay files listed by `006_iw005_flanders_overlay_implementation_2026_07_16.md`, plus their directly referenced sprites, states, source rows, offline wiki pages, official documentation, and vanilla precedents.

## Initial verdict (superseded): PASS WITH REQUIRED FIXES

> Re-audit status on 2026-07-16: **PASS**. F-01 through F-04 were corrected and independently rechecked against the live workspace. See the dated addendum at the end of this report.

The package has the right overlay-only architecture and most of its gameplay is internally coherent. It is **not ready for acceptance in its audited form**. Four bounded defects must be corrected:

1. route suspension restarts the 150-day mission instead of pausing its remaining timeout;
2. all six custom-cost localisation families omit the engine-required blocked and hover variants;
3. every affordability trigger rejects exact payment because it uses strict `>` against the displayed and spent value;
4. two Army Experience checks use the undocumented trigger name `army_experience` instead of `has_army_experience`.

The proposed keep-active timeout correction is substantially safer than removal/reactivation, but official documentation does not define whether mission timeout decrement happens before or after `on_daily_BEL`. The one-day-remaining transition edge therefore remains unproved and is recorded below.

No gameplay, localisation, asset, shared-document, or spreadsheet file was edited by this audit. No commit was created.

## Required fixes

### F-01 — Suspension resets the mission deadline instead of pausing it

Severity: blocking mission-semantics defect.

Evidence in the audited implementation:

- `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:246-267` marks an active guard as interrupted, removes the mission at lines 257-260, and clears the running flag.
- `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:269-280` resumes by calling `activate_mission` at line 278.
- `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:314-320` also reconstructs a missing active mission by calling `activate_mission`.
- `common/decisions/006_independence_wave_iw005_flanders_decisions.txt:23` defines a 150-day mission timeout.

`remove_mission` removes a mission without executing completion or timeout effects, while `activate_mission` starts a mission anew and ignores its normal activation trigger. Nothing stores or restores `days_mission_timeout@independence_wave_iw005_hold_scheldt_guard_line`. Consequently, every suspend/resume cycle restores the full 150-day deadline. Repeated cosmetic-route toggling can extend the mission indefinitely. The 60-day hold counter itself is preserved, and the guard cost and reward are not duplicated, but the binding deadline is not paused.

The proposed correction—keep the mission and running flag active while the cosmetic route is absent, freeze the hold counter through the inactive-overlay gate, and add one day to the timeout on every suspended `on_daily_BEL` tick—is the correct bounded direction, subject to all of these conditions:

- remove route loss from the mission `cancel_trigger`;
- do not clear `independence_wave_iw005_factory_rail_guard_running` during suspension, otherwise the surviving `NOT = { has_country_flag = ...running }` cancellation condition still cancels the mission;
- do not call `remove_mission` or `activate_mission` on normal suspension/resume;
- apply the one-day extension on the **first route-loss detection tick inside the suspension path**, not only on later already-suspended ticks, or each transition consumes one mission day;
- remove the current missing-mission reconstruction at lines 314-320. Treating an unexpected missing mission while the running flag is set as failure is conservative and prevents a fresh-deadline exploit;
- if that integrity failure can occur while the overlay is suspended, do not call the present `independence_wave_iw005_fail_guard_mission` unchanged: its lines 170-178 are gated by `is_independence_wave_iw005_flanders_overlay_active = yes` and would silently do nothing. Either defer the failure until route resumption or use an integrity-failure path that can set the failed state while suspended.

Official effect syntax is country-scoped:

```txt
set_temp_variable = {
	independence_wave_iw005_guard_pause_extension_days = constant:independence_wave_iw005_flanders_duration.guard_pause_extension_days
}
add_days_mission_timeout = {
	mission = independence_wave_iw005_hold_scheldt_guard_line
	days = independence_wave_iw005_guard_pause_extension_days
}
```

The official effect documentation defines `mission = <mission>` and `days = <integer>`, and the offline effect reference explicitly permits `days = <int> / <variable>`. Vanilla also passes country variables to `days`. The official script-constant documentation says constants are accepted only where support is declared, and the repository rules specifically require duration fields that reject constants to receive a normal or temporary variable. Therefore the intermediate unscoped temporary variable is the safe form; do not pass `constant:...` directly to this `days` field.

Day-order caveat: neither the official on-action documentation nor the offline wiki specifies the ordering between mission timeout decrement and `on_daily_TAG`. Adding one day on every suspended tick is net zero regardless of order after suspension is established, but a route loss detected when only one day remains could theoretically time out before the first extension if mission processing runs first. The conservative missing-mission failure prevents a reset exploit but would still be a failure rather than a pure pause in that edge. Exact pause cannot be certified from documentation alone until engine order is established or an immediate route-change hook protects the transition.

### F-02 — Six custom-cost localisation contracts are incomplete

Severity: required player-facing/UI fix.

`common/decisions/006_independence_wave_iw005_flanders_decisions.txt:52-53,75-76,101-102,134-135,167-168,201-202` declares these six `custom_cost_text` keys:

- `independence_wave_iw005_ledger_cost`
- `independence_wave_iw005_depot_cost`
- `independence_wave_iw005_officer_cost`
- `independence_wave_iw005_guard_cost`
- `independence_wave_iw005_civic_institution_cost`
- `independence_wave_iw005_security_institution_cost`

Repository-wide exact-key counts found one base key and zero `_blocked` and `_tooltip` keys for every family. The decision-modding contract is exact:

- when `custom_cost_trigger` is true, the engine uses `<key>`;
- when it is false, the engine uses `<key>_blocked`;
- while hovering over the cost, it uses `<key>_tooltip`.

Add all twelve missing keys to the UTF-8-with-BOM localisation file. The blocked forms should communicate the same amounts in an unavailable/red presentation; the tooltip forms should state that taking the action spends those resources. Custom-cost text does not spend anything by itself, so the existing negative payment effects must remain.

### F-03 — Affordability requires one unit more than the displayed cost

Severity: required cost-correctness fix.

`common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt:63-99` uses strict `>` for every Command Power, manpower, Army Experience, train, infantry-equipment, and support-equipment requirement. Those right-hand constants are the exact numbers displayed in localisation and subtracted by the payment effects. A player with exactly 500 infantry equipment is therefore blocked from a displayed 500-equipment action; the same off-by-one/exact-boundary defect affects every resource.

Equality-safe syntax, without unsupported `>=`, is:

```txt
NOT = { command_power < constant:independence_wave_iw005_flanders_cost.guard_command_power }
NOT = { has_manpower < constant:independence_wave_iw005_flanders_cost.guard_manpower }
NOT = { has_army_experience < constant:independence_wave_iw005_flanders_cost.security_institution_army_experience }
NOT = {
	has_equipment = {
		infantry_equipment < constant:independence_wave_iw005_flanders_cost.guard_infantry_equipment
	}
}
```

Use the same outer-negation pattern separately for trains and support equipment. A separate `cost_minus_one` threshold is also valid for integer-only stocks, and vanilla commonly uses `> 499` for a cost of 500, but the negated-less-than form keeps displayed, checked, and spent values sourced from one constant.

### F-04 — Army Experience affordability uses the wrong trigger name

Severity: required script-correctness fix.

`common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt:76,96` uses `army_experience > ...`. The official trigger documentation and offline trigger reference define `has_army_experience`, and the vanilla decision set consistently uses `has_army_experience`; no vanilla `army_experience >` trigger precedent was found. Replace both with the equality-safe form shown under F-03:

```txt
NOT = { has_army_experience < constant:independence_wave_iw005_flanders_cost.officer_army_experience }
```

and the corresponding security-institution constant.

## Binding proof matrix

| Requirement | Result | Evidence |
|---|---|---|
| Living exact Belgian carrier only | PASS | `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt:9-13` requires `exists = yes`, `original_tag = BEL`, and `has_cosmetic_tag = BEL_flanders`. Vanilla `common/countries/cosmetic.txt:1545` defines `BEL_flanders`; vanilla `common/decisions/GER.txt:20117` applies it to Belgium. |
| Overlay only; preserve Belgium and Event 6 origin | PASS | The package adds decisions, variables, flags, and ideas only. It contains no tag creation/release, cosmetic-tag mutation, focus-tree load/replacement, country-history edit, leader/character replacement, capital/state/core transfer, autonomy mutation, Event 6 origin edit, FORM03 mutation, or Soviet reference/coupling. Vanilla Belgium retains its `BEL_flanders_ascendant` focus route (`common/national_focus/belgium.txt:3853+`). |
| Idempotent initial activation | PASS | `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:229-244` initializes only on the exact route and only without the permanent `...overlay_ever_activated` flag. Starting values and the idea lifecycle are assigned once. |
| Suspension and resume | FAIL, F-01 | Variables and progress survive and ideas are removed/restored, but the active mission is removed and restarted with a fresh deadline. |
| No world iteration | PASS | `common/on_actions/006_independence_wave_iw005_flanders_on_actions.txt:9-12` uses legal `on_daily_BEL` and calls one BEL-scoped refresh effect. No `on_daily`, `every_country`, weekly, or monthly iterator appears in the package. Official and offline references both define `on_daily_TAG` as a specified-country hook. |
| 60 continuous successful days | PASS | `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:206-227` increments only while active, running, and satisfying the full objective, clamps at 60, and resets to zero on any active-running objective break. `common/decisions/006_independence_wave_iw005_flanders_decisions.txt:15-26` auto-completes the non-selectable mission at 60 and fires the success effect. |
| 150-day ordinary timeout failure | PASS outside suspension | `common/decisions/006_independence_wave_iw005_flanders_decisions.txt:23,35-38` uses a 150-day timeout and distinct failure effect. `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:170-178` marks failure, clears running/interrupted state, resets hold, and applies -5% Stability while the overlay is active. Suspension breaks exact deadline semantics per F-01. |
| No duplicate guard charge or reward | PASS | Guard payment occurs only in `...start_guard_mission` at effects lines 151-157. Resume does not call payment. Success sets a completion flag and applies its gains once at lines 160-168. A genuine failed retry is charged again, as presented. |
| Flanders/Antwerp ownership, control, and garrison | PASS | `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt:33-49` requires ownership and control of state 6 and state 977 plus more than zero current-country divisions in each. Official docs define `divisions_in_state` in country scope as the current country's divisions. Vanilla state histories identify state 6 and state 977 as Belgian-owned/core states; state-name localisation identifies them as Flanders and Antwerp. |
| Idea lifecycle | PASS | Effects lines 13-42 remove the entire four-idea family and add exactly one of contested, coordinated, civic-final, or security-final in priority order. Suspension removes all four; route resume restores the state-derived one. `common/ideas/006_independence_wave_iw005_flanders_ideas.txt:10-57` defines all four and limits them to `original_tag = BEL`. |
| AI behavior | PASS with bounded risk | Every selectable action has nonzero, state-aware weights. The guard action has zero weight without the two-state garrison and is weighted more strongly at peace, so AI will not pay for an immediately impossible objective. No explicit unit-movement strategy forces one division into each state, so AI completion is opportunistic rather than guaranteed; this is a risk, not a false-success or resource-waste path. |
| Localisation encoding and ordinary coverage | PASS except F-02 | The target file begins `EF BB BF`, has 43 keys, and has no duplicate key within the file. Category, ideas, actions, mission, effects, and status strings are present and avoid implementation-history wording. The six custom-cost families are incomplete. |
| Sprite registration and assets | PASS | The referenced shared sprites are registered once in `interface/006_independence_wave.gfx:33,35,39,44-45,54`. All six DDS targets exist with valid `DDS ` headers: three idea textures are 64x64 and three decision textures are 32x32. |
| Duplicate gameplay IDs | PASS | Exact declaration scans found each of seven decision/mission IDs in one decision file and each of four idea IDs in one idea file. Target localisation has no internal duplicate key, and the six referenced sprite names each resolve once. |
| No free military or political stores | PASS | All nine `add_equipment_to_stockpile` calls in effects lines 72-126 use negative spend constants. Manpower, Command Power, and Army Experience payment effects are also negative. No unit/OOB creation, positive equipment grant, or Political Power grant/store appears. |

## Arithmetic and balance proof

### Mandatory route reachability

| Step | Civic-Industrial Coordination | Scheldt Security | Gate result |
|---|---:|---:|---|
| Initial values | 30 | 25 | — |
| Municipal/factory ledgers (`+25/+5`) | 55 | 30 | — |
| Scheldt rail depots (`+5/+25`) | 60 | 55 | Guard prerequisites reached |
| Successful guard (`+15/+25`) | 75 | 80 | Civic gate `65/55`: pass; security gate `55/65`: pass |
| Civic institution (`+10/-5`) | 85 | 75 | Within 0-100 clamp |
| Security institution (`-5/+10`) | 70 | 90 | Within 0-100 clamp |

The optional officer action does not gate completion. If taken after the two foundations, it changes `60/55` to `55/75`; successful guard then reaches `70/100`. Both institution gates still pass. Civic final becomes `80/95`; security final becomes `65/100` after clamping. Both institution choices are therefore reachable through the mandatory route with or without the optional action.

### Cost totals

The mandatory shared sequence (ledgers, depots, successful guard start) spends 40 Command Power, 7,500 manpower, 10 trains, 500 infantry equipment, and 200 support equipment. The civic ending totals 60 Command Power, 17,500 manpower, 20 trains, 500 infantry equipment, and 200 support equipment. The security ending totals 40 Command Power, 12,500 manpower, 35 Army Experience, 10 trains, 1,500 infantry equipment, and 400 support equipment. The optional officer action adds 5,000 manpower, 20 Army Experience, 500 infantry equipment, and 100 support equipment.

These amounts are staged behind separate actions rather than demanded simultaneously, fit the relevant Command Power and Army Experience caps, and are credible medium-term Belgian commitments. The contested idea is meaningfully adverse, coordinated state is modestly positive, and the final civic/security ideas have distinct civilian-versus-military tradeoffs. Cost execution is sound once F-03/F-04 make the affordability checks match the displayed payments.

## References and precedents consulted

- Required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Official vanilla documentation: `common/decisions/_documentation.md`, `common/on_actions/_documentation.md`, `common/script_constants/documentation.md`, `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `documentation/dynamic_variables_documentation.md`, and `documentation/loc_formatter_documentation.md`.
- Vanilla precedents: `on_daily_SWE`/`on_daily_GER`; `CHI_holding_state_mission`; `add_days_mission_timeout` uses in AST/CHI; 500-equipment threshold in `common/decisions/AUS.txt:1643`; Belgium's `BEL_flanders` cosmetic route and focus tree.
- Event 6 sources: IW-005 research and force-mapping rows, the FORM03 addendum, the implementation handoff, and the Flanders overlay system document.

Skills used: `chaos-redux-subagents`, `hoi4-decisions-missions`, and `chaos-redux-events`.

## Simplifications, omissions, and blockers

No audit surface was intentionally skipped and no fallback was used. F-01 through F-04 are required fixes. The undocumented daily ordering at the one-day mission boundary is the remaining proof blocker for the proposed keep-active pause implementation; it must not be represented as fully certified by documentation.

## Re-audit addendum: 2026-07-16

### Verdict: PASS

The current shared-workspace implementation resolves F-01 through F-04. The result is a static source and documentation pass, not a claim that the undocumented ordering between mission-timeout decrement and `on_daily_BEL` has been established by an executable trace.

### Correction verification

| Finding | Result | Current evidence |
|---|---|---|
| F-01: mission deadline reset on suspension | PASS | `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:245-258` marks a running mission interrupted, removes the overlay ideas, and suspends the overlay without clearing the running flag or removing the mission. Lines 261-274 require suspended, interrupted, running, and active-mission state, load `constant:independence_wave_iw005_flanders_duration.guard_pause_daily_extension` into an unscoped temporary variable, and pass that variable to `add_days_mission_timeout`. The centralized duration constant is `1` at `common/script_constants/006_independence_wave_iw005_flanders_constants.txt:57`. |
| First and later suspended tick extension | PASS | In `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt:352-358`, the inactive-route branch first suspends an active overlay and then calls the pause helper on the same tick. The same helper is called on every later inactive-route tick. |
| Hold counter freezes while suspended | PASS | The inactive-route branch does not call the hold updater. Independently, `...flanders_effects.txt:205-226` can increment or reset the counter only while the overlay-active proof and running flag are both true. Suspension clears overlay active, so it can neither advance nor reset the stored hold count. |
| Route loss no longer cancels the mission | PASS | `common/decisions/006_independence_wave_iw005_flanders_decisions.txt:28-31` cancels only when the persistent running flag is absent. Route activity is no longer a cancellation condition, and suspension preserves that flag. |
| No suspension/resume reconstruction | PASS | Exact scans find no `remove_mission` in the IW-005 package and one `activate_mission`, used only by the paid initial start at `...flanders_effects.txt:151-157`. Normal suspend/resume does not remove, activate, or recreate the mission. |
| Missing mission fails instead of restarting | PASS | `...flanders_effects.txt:277-295` clears interruption only when both running and the original active mission are present. Otherwise it calls the failure effect after the route has restored overlay-active state. Lines 329-334 also treat a running mission that disappears during ordinary active-route refresh as failure. No fresh timeout is created. |
| F-02: custom-cost localisation | PASS | Each of the six cost families has exactly one base, one `_blocked`, and one `_tooltip` key at localisation lines 21-23, 28-30, 35-37, 42-44, 54-56, and 61-63. Repository-wide exact-key counts are `1/1/1` for all six families. |
| F-03: exact-balance affordability | PASS | `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt:63-99` uses `NOT = { resource < cost }`, including outer negation around equipment checks. Exact Command Power, manpower, train, infantry-equipment, support-equipment, and Army Experience totals now satisfy the same constants displayed and spent. No cost check retains the old strict `> cost` form. |
| F-04: Army Experience trigger | PASS | Trigger lines 76 and 96 use documented `has_army_experience` in the equality-safe negated-less-than form. No bare `army_experience` affordability trigger remains. The payment effects continue to use the documented `army_experience = negative_value` effect form. |

The official `add_days_mission_timeout` contract remains satisfied: it is used in country scope with `mission = <mission>` and a variable-backed `days` input. The offline effect reference explicitly permits an integer or variable. The implementation does not pass a script-constant token directly to the duration field.

### Documentation verification

- `docs/systems/006_independence_wave_iw005_flanders_overlay.md:36-51` accurately describes preservation of the same mission and running flag, first-and-later suspended-tick extension, frozen hold progress, and continuation without a restart. Line 51 explicitly states that official documentation does not establish timeout-versus-on-action order, identifies the one-day-remaining edge, and states that no fresh-deadline fallback is used.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw005_flanders_overlay_implementation_2026_07_16.md:115-132` matches the implemented lifecycle and carries the same ordering limitation. Lines 200-204 repeat it under remaining risks rather than claiming executable engine certification.
- The implementation handoff's refreshed validation counts match the live source: 40 unique scripted trigger/effect definitions and 91 unique referenced constant keys.

### Regression proof

- Exact carrier and preservation rules still pass: the route trigger remains `exists = yes`, `original_tag = BEL`, and `has_cosmetic_tag = BEL_flanders`; no tag creation, release, origin assignment, focus-tree load/replacement, Belgian history mutation, territory/core/autonomy/capital/leader/character change, FORM03 mutation, or Soviet coupling appears.
- Runtime scope still passes: the package uses only `on_daily_BEL`, with no world-iterating daily, weekly, monthly, or `every_country` hook.
- State and mission semantics still pass: state 6 and state 977 ownership, control, and current-country garrison checks are unchanged; the mission still requires 60 continuous qualifying days within a 150-day active-route deadline, uses distinct completion and timeout effects, and cannot duplicate its paid start or success gains.
- Arithmetic still passes: the mandatory sequence reaches `75/80`, opening both `65/55` and `55/65` institution gates. The optional officer route reaches `70/100` before the institution choice and also opens both gates.
- Costs, ideas, and AI still pass the prior audit. All equipment, manpower, Command Power, and Army Experience payments are negative; no units, free equipment, Political Power store, factory, territory, or core is granted. The four-idea lifecycle remains exclusive. AI remains safely gated but opportunistic about placing the two required garrisons.
- Localisation remains UTF-8 with BOM (`EF BB BF`), now contains 55 keys with no duplicate key in the file, and includes the complete six custom-cost contracts.
- All 40 target scripted trigger/effect definitions are unique in `common/`; all 91 unique IW-005 constant references resolve; all seven decision/mission IDs and four idea IDs remain unique.
- The three reused idea DDS files remain valid 64x64 DDS assets, the three reused decision DDS files remain valid 32x32 DDS assets, and all six sprite names still resolve through `interface/006_independence_wave.gfx`.

### Remaining risks

1. Official documentation does not specify whether mission timeout decrement or `on_daily_BEL` executes first. The implementation makes the required extension call on the first observed suspended tick and every later tick, but a route loss observed with one day remaining cannot be ordered conclusively without an executable engine trace. If the mission disappears in that edge, the code fails it on active-route return instead of exploiting a fresh 150-day restart.
2. No callable HOI4 MCP domain tool or executable game trace was available in this subagent session. The verdict covers current source, official syntax, vanilla precedents, arithmetic, localisation, identifiers, assets, and documentation consistency.
3. AI does not install an explicit unit-movement strategy for states 6 and 977. It will not start the mission without the required garrisons, so this is a completion-likelihood risk rather than an invalid-action or resource-loss path.

The re-audit changed only this audit report. It did not edit gameplay, localisation, assets, the system document, the implementation handoff, shared Event 6 documentation, or the spreadsheet, and it created no commit.
