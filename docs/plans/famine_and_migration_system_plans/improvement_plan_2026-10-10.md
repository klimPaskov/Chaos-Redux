# Famine and migration improvement plan

Date: 2026-10-10.
Disposition: accepted and implemented in this pass under the user's 10 October brief (section 3.2), which authorizes redesigning weak mechanics, removing repetitive decisions and bloated values, and fixing every defect found.
This document is the single current plan and status record for both systems.
It supersedes [takeover_status_2026-10-06.md](takeover_status_2026-10-06.md) for current status and [the 3 October simplification package](2026-10-03_full_system_simplification_package/IMPROVEMENT_PLAN.md) as the active proposal; both remain historical evidence.
Older plans already marked superseded keep their notes.

## 1. Audit summary

The audit read the decision files, the famine and migration cores, the adapters, the runtime coordinator, the localisation and the Hunger Lines launch path, and inspected the three live QA saves of scenario #010 (`qa_scn010`, `qa_scn010b`, `qa_scn010c`, HOI4 1.19.2, USA, 1936).

### What works

- Food security is a real state model: production, transport, extraction, need, environment, vulnerability, governance and relief feed one score, five stages move one step at a time with warning windows, stocks run down before famine, and mortality uses real population loss recorded as `From famine`.
- Migration moves real population between states through one exact transfer, records route deaths separately, and keeps cohorts, reception load and capacity.
- Wars feed both systems: a hostile capture queues a food assessment and war flight, local war adds transport and need pressure, wartime islands are watched for blockade, and nuclear strikes, outbreaks (Black Plague), natural disasters, Acid Rain, Air Cleanliness, camps, CBRN occupation, the Great Depression and Event 012 reception services already call the adapters.
- Player-facing headline values are already limited to three per system (Food Security, Food Reserves, Relief Access; Displacement Load, Reception Capacity, Border Policy).

### Defects and weaknesses found

| # | Finding | Effect on play |
| --- | --- | --- |
| A1 | **B040.** All three Hunger Lines QA launches failed inside Event 014's setup (`cannibalism_manual_scenario_setup_failed`, no node states); the famine hook only runs after a successful setup. When it does run, the node states start with half their stores and only drift toward supply strain over a week and famine over six weeks. | The scenario named after hunger shows no famine. |
| A2 | The famine decision phase (`famine_decision_emerging/active/resolution/dormant`) is refreshed only from the migration country registry. | A country with a famine but no refugees never moves to resolution or dormant; once a famine action was taken the category stays open for the rest of the game. |
| A3 | Ordinary famine has no national consequence: state modifiers and deaths only. Stability is touched only by catastrophic famine under active extraction. | Ignoring a famine costs the government nothing politically, so relief is optional. |
| A4 | Conceal Hunger adds 1,000 and Continue Requisitions 2,000 to a food shock clamped at 100. | One click maxes the shock and pushes the state toward catastrophic famine. Concealment otherwise only gave +2% stability. |
| A5 | Request Relief only creates the donor contract that Import Food would create itself, then needs Import Food to deliver. | Two payments and two waits for one shipment. |
| A6 | Four "role selectors" hide whole decisions country-wide: Request Relief while any state has stores, Airlift while any state has a sea route, Requisition while any state can be evacuated, Continue Requisitions while any state could be concealed (almost always for non-democracies). | Decisions vanish for reasons unrelated to the selected state; Continue Requisitions was practically unreachable. |
| A7 | Migration's Prepare Evacuation is a paid step with no effect except unlocking the two evacuation decisions. It and both departure policies hide as soon as `migration_decision_active` is set. | Busywork, and after the first migration action no further state can be prepared or evacuated and the departure policy can never be changed again during the crisis. |
| A8 | Evacuate the Vulnerable and Evacuate Workers move exactly the same number of people through the same transfer; only the price differs. | A false choice whose text promises effects that do not exist. |
| A9 | Evacuations require zero national reception load. Internal evacuations create load, so the first evacuation blocks every later one until integration. | Only one evacuation per crisis. |
| A10 | Close the Border requires spare reception capacity. | The border can be closed only when the country is not overwhelmed, the one time a closure is pointless. |
| A11 | AI weights contain dead or inverted factors: imports ×0.1 when trapped people need food, reserve release ×0.5 at war, workers ×2 for any country with a civilian factory, and the migration AI table duplicates thirty famine keys nobody reads. | AI skips food relief exactly when it matters. |
| A12 | A state taken by a special Chaos Redux power (zombies, rats, ZIN, Death, revolutionary or terror commands) fails the shared state validity and drops out of both systems. | The most frightening fronts in the mod create no refugees at all. |
| A13 | The migration phase flags lock whole decision families: corridor, screening, distribution, transit and enforcement need the active phase; integration, return and resettlement need resolution and no active crisis. | A receiving country in resolution cannot distribute or close its border; a country with its own displaced people cannot integrate arrivals. |

### Accepted remaining scope limits (not changed here)

- Strategic bombing has no documented engine callback, so it still has no adapter.
- The Event 149 retirement, the event-free design, the separate namespaces and the exact population accounting stay as they are.
- State-targeted decisions are still listed once per affected state; the engine has no grouped selection, and this pass reduces the count of decision types instead.

## 2. Implementation

### 2.1 Hunger Lines visibly starts a famine (A1)

- Event 014 setup failure: traced in section 3; the cause is already repaired in source.
- `famine_apply_hunger_lines_scenario_pressure` now seizes each node state's food stores (the drained amount is recorded as depleted stock), applies the food shock and context, and commits the starting stage immediately: acute shortage at Low, famine at Medium and above.
  The owner sees the Famine category, the famine map colours and the famine report header on the day of the launch.
- The context values hold the committed stage for the 120-day context window without relief (section 4 shows the arithmetic), and relief, imports, requisition or evacuation bring it down through the ordinary recovery windows.

### 2.2 Famine country registry, phase and national crisis (A2, A3)

- New sparse `global.famine_active_countries` registry: a country joins when one of its states registers, and leaves once its phase is dormant with no visible food problem and no famine mission.
- The daily coordinator processes that registry with `famine_process_registered_country`, which refreshes the famine phase (independently of migration) and the national food crisis.
- `famine_national_food_crisis` country modifier: stability and war support fall with each acute, famine and catastrophic state the public can see, with caps.
  A concealed state does not count until its concealment ends, which gives Conceal Hunger its real purpose: national calm bought with worse local hunger and condemnation when deaths are exposed.

### 2.3 Famine decisions (A4–A6)

- Request Relief is removed; Import Food arranges and delivers in one decision.
- The four country-wide hiding selectors are removed; every decision is shown by its own state conditions.
- Conceal Hunger adds a shock of 10 and Continue Requisitions 15 instead of 1,000 and 2,000.

Famine actions after the pass: Release Food Stores, Import Food, Restore Relief, Escort Relief, Airlift Relief, Requisition Food, Evacuate (famine), Conceal Hunger, Continue Requisitions, and the two relief missions.

### 2.4 Migration decisions (A7–A10, A13)

- Prepare Evacuation and Evacuate Workers are merged into one **Evacuate Civilians** decision (former `migration_evacuate_vulnerable`, now `migration_evacuate_civilians`), visible for any state with sustained flight, trapped people or food insecurity, priced as the former vulnerable evacuation.
- The emerging/active/resolution phase flags become presentation only (category header text and missions). No ordinary decision is locked by them, so departure policy can be reversed during a crisis, a corridor can be requested without first buying another action, and a country that both shelters arrivals and has its own displaced people can act on both.
- Evacuations and famine evacuation are blocked only when national reception is already over capacity, not by any hosted group.
- Every action that relieves a host (Close the Border, Enforce the Closure, Distribute Arrivals, Permit Transit, Local Integration, Help Families Return, Force Repatriation) is available to an overloaded host; actions that admit more people (Open Emergency Reception, Screen Incoming Civilians) still need spare capacity.

Migration actions after the pass: Open Departure, Restrict Departure, Evacuate Civilians, Request Passage, Accept/Refuse Passage, Open Emergency Reception, Screen Incoming Civilians, Distribute Arrivals, Permit Transit, Close the Border, Enforce the Closure, Local Integration, Resettle Abroad, Help Families Return, Force Repatriation, and the four missions.

### 2.5 Links to Chaos Redux powers (A12)

A state captured by a special Chaos Redux power that runs no civilian system (the walking dead, a rat swarm, ZIN, Death, a revolutionary or terror command) left both mechanics with no refugees at all.
`humanitarian_handle_special_front_capture` now sends 2% (4% for a nonhuman captor) of each neighbouring state the former owner still holds into flight, with the ordinary population gate and cooldown, so Zombie Outbreak, Black Plague, Death, ZIN and similar fronts create refugee waves ahead of them.

### 2.6 AI (A11)

- Reserve release rises by half at war instead of halving; Import Food rises by half when trapped people add need instead of dropping to a tenth, and carries the stage urgency (×1.5, ×2.5, ×4) and the democratic ×2 that the removed Request Relief had.
- Evacuate Civilians: base 13, ×4 when people are trapped, ×2 at war.
- The duplicated famine keys and the removed decisions' keys are deleted from `migration_decision_ai`.
- Conceal Hunger and Continue Requisitions keep their low weights and their fall-off at famine and catastrophic stages.
- Source calculation by the AI probability auditor (MCP probability inspection failed twice, so scores are hand-computed willingness scores, not probabilities): in a wartime acute shortage Release Food Stores scores 162 and Evacuate 80 against Continue Requisitions 0.6; at famine with 20,000 trapped people Evacuate scores 240, Evacuate Civilians 104 and Import Food 40.5 before the added stage and democratic factors and about 200 after, against 0.3 for extraction and 0 for forced return.

## 3. Event 014 launch trace

All three QA saves carry only `cannibalism_manual_scenario_setup_failed` (dated 1936.1.1.12) and no Event 014 global flag, so the manual preflight `cannibalism_scenario_build_manual_preflight_plan` returned failure before `cannibalism_scenario_launch_active` was set.
Before commit `abacbd845` the wrapper read `cannibalism_scenario_preflight_result`, `cannibalism_scenario_source_found` and the required-state counts after they had been created inside the helpers, the temporary-variable lifetime the offline wiki warns about (`paradox_wiki/Data structures`, Variable types).
`abacbd845` makes every caller own those outputs; `qa_scn010` predates it and the two later saves were most likely run on a build loaded before it.
A source trace of the current chain for type 1 (Broken Ranks) at Low, Medium and Maximum from a 1936 USA start reaches `cannibalism_scenario_preflight_result = 1` and a successful setup; no Event 014 edit was needed.
Remaining uncertainty: the five planned temp arrays are cleared by the wrapper and filled inside the preflight helper; if the engine does not keep helper-filled temp arrays, types with extra actors or island/siege/march hosts would still fail. Only a fresh live launch settles this.

The SCN-010 impact text (`chaosx.scenarios.cannibalism.impact.*`) now tells the player that the seized regions lose their stores and fall into acute shortage or famine.

## 4. Balance check (source arithmetic)

Score = (1.15 production + 1.10 transport + 1.25 extraction + need + 0.80 environment + 0.90 vulnerability + 0.95 governance − 1.20 relief) / 2.5.
A Hunger Lines node with seized stores has 55 exhaustion need; the scenario context P applies to production, transport, governance and vulnerability (weight 4.10), and the shock S adds to need (decays 0.25 per day).

| Intensity | P | S | Day-0 score | Day-60 score | Committed start | Recovery threshold |
| --- | --- | --- | --- | --- | --- | --- |
| Low | 14 | 35 | 59.0 | 53.0 | Acute shortage | below 40 for 21 days |
| Medium | 24 | 45 | 79.4 | 73.4 | Famine | below 60 for 21 days |
| High | 28 | 50 | 85.9 | 81.9 | Famine | below 60 for 21 days |
| Maximum | 32 | 60 | 92.5 | 92.5 | Famine | below 60 for 21 days |

Without relief the starting stage holds for the 120-day window; a delivered import (35 relief points, −16.8 score) or restored stores bring Low below 40 and Medium below 60 within the recovery window, so relief visibly ends the crisis.
Famine mortality without relief removes roughly 1–4% of a node state's population over the window, reported under `From famine`.

National crisis: −1% stability per visible acute state, −2% stability and −1% war support per famine state, −4% stability and −2% war support per catastrophic state, capped at −15% stability and −10% war support.
A single famine state costs about as much as an ordinary unpopular decision; five famine states reach the cap, which is a serious but survivable wartime penalty.

## 5. Future depth (not part of this pass)

- Attach Restore Relief to the delivery operation as its physical objective instead of a separate payment.
- A real worker-cohort identity, if a production-recovery consumer is ever added, could bring back a priority choice inside Evacuate Civilians.
- Show "Famine in N states" in the category header once a cheap per-country count is published.

## 6. Status and validation

Implemented in this pass: every item in section 2.
The two new cases in `.tools/test_famine_takeover_20261006.py` run the real `famine_apply_hunger_lines_scenario_pressure` chain (pressure request, stores seizure, stage commit) at Low, Medium and Maximum and a relaunch inside the window, and the real `famine_refresh_national_food_crisis` (visible versus concealed states, foreign states, caps, clearing); all 11 cases pass.
`hoi4.script_validate` checked the command kinds and scopes of the new country and state effect bodies against the installed documentation; argument blocks remain unchecked by that tool.
Not verified here: native launch of SCN-010 (see section 3), campaign timing of the national crisis and of front flight, and AI choice frequencies; these are user-run live checks.

Queued: the SCN-010 catalog row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` ([catalog_changes_pending.md](catalog_changes_pending.md)); the workbook carries another agent's uncommitted edits, so this pass did not touch it.

Simplifications and omissions: none of the requested surfaces was dropped. Two decision types were merged rather than given new distinct mechanics (Evacuate Workers into Evacuate Civilians, Request Relief into Import Food), because the removed versions had no distinct effect. Strategic bombing still has no adapter because the engine exposes no bombing callback.
