# Event 037 implementation acceptance criteria

## Purpose

This file lists the pass or fail checks for the design in the spec parts.
Each check points to the section that owns the rule.
Reference reading, MCP use and retry limits, completion reporting, and live testing ownership follow `CLAUDE.md` and are not repeated here.

## 1. Identity and legacy retirement (Part 1)

- `chaosx.nr37.1` runs the world transaction and nothing else.
- The legacy recruit grant, the enslavement option, and the alien news headline are gone, and `chaosx.news.42` is rewritten for the first manifestation only.
- One firing produces one pacing update, one history entry, and one world transaction, including after reload and through a future Sudden Abundance cluster call.
- Event Details, history, evolution previews, and debug names are wired together.

## 2. World transaction and grant (Parts 1 and 2)

- Only states passing `humanitarian_state_is_valid` with at least the inhabited threshold receive a grant.
- Each valid state receives exactly one grant from the stage table, measured through the neutral gain helper.
- The helper removes the instant recruitable gain for owner and controller and is documented in `chaosx_dynamic_effects.md`.
- The state share, unsettled backlog, country counts, and world count change by exactly the measured amount.
- A state that becomes invalid mid-pass is untouched.

## 3. Ledger (Part 2)

- The newcomer count never exceeds real population and never falls below zero, including after famine, bombing, and disaster losses in a newcomer-majority state.
- The civilian transfer hook blends destination share and reduces origin backlog by measured departures only.
- Ownership change moves the state's newcomers and backlog between country counts without changing the state.
- The monthly host pulse touches only registered countries and at most `3` hotspots each.
- Everything persists across save and reload, and no grant or milestone repeats.

## 4. Pressure and consequences (Part 3)

- State and national pressure follow the Part 3 formulas, and the worst-hotspot term cannot push a huge country to Breakdown from one tiny state.
- The header shows exactly the newcomers, pressure with stage, and stance.
- The Newcomers modifier is one modifier whose values follow pressure and settled share, with no stacking.
- Hotspots at `60+` submit one refreshed food-need component, and hotspots at `80+` request flight, through the public Famine and Migration entry points only.
- A pressure fall caused by deaths or flight is named as hunger or flight in the hotspot tooltip.

## 5. Evolutions (Part 3)

- Thresholds `200`, `400`, `600`, MTTH factors, zero Chaos, disabled-stage behaviour, and the first-firing rule work as specified.
- Each evolution changes the grant scale, and Evolution III unlocks Build a New City and the origin register event.

## 6. Decisions and mission (Part 4)

- The category appears and hides by the Part 4 lifecycle and respects the visibility budget.
- Stances cost, lock, and modify settlement as specified.
- Every action uses at most two spendable cost types with texticons, respects its availability, and fails closed on owner or controller change.
- Absorb the Newcomers starts, completes, and fails as specified, with one active at a time.

## 7. Events (Part 5)

- One manifestation report per human country per firing, three evolution reports, and no per-state popups.
- Flavour selection respects validity and the four-event diversity memory.
- Every option's effect matches Part 5.
- No text confirms an origin, and the writing follows the event skill.

## 8. Shared systems (Part 6)

- No Event 037 food value, famine decision, movement decision, death record, or Condemnation source exists.
- No Event 037 action targets people by origin.
- Countries outside normal civilian systems get no grant, category, or action.

## 9. Chaos (Part 1)

- The four milestones fire once each at the end of a firing, and nothing else adds Event 037 Chaos.

## 10. Assets, achievements, catalog (Part 7)

- Every inventory asset exists with its own source art, final DDS, and `.gfx` registration.
- The three achievements trigger, reset, and persist as specified, with complete triplets and localisation.
- The workbook row matches final localisation and the CSV exports are regenerated.

## Validation scenarios

1. Baseline firing in a 1936 start.
2. Tiny inhabited state and a capped very large state.
3. Three repeated firings with compounding.
4. First firing at `650` Chaos, and a disabled lower evolution.
5. Ownership and control change of a hotspot with a running project.
6. Famine mortality and bombing in a newcomer-majority state.
7. Breakdown hotspot flight through Migration, including a closed border.
8. Country outside normal civilian systems.
9. Save and reload after a firing, a project completion, and a flight transfer.
10. Event Logs and Event Details.
11. Each achievement's success, reset, and duplicate-count protection.
12. Probability scenarios before and after any weight change.
