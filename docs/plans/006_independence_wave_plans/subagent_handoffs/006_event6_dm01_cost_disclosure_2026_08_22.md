# Event 006 DM-01 cost disclosure handoff — 2026-08-22

## Scope

The automatic `independence_wave_secure_provisional_capital` mission now exposes its opening material commitment through the normal decision custom-cost surface after the commitment has been reserved.

## Files changed

- `common/decisions/006_independence_wave_decisions.txt`
  - Added `custom_cost_trigger` keyed to `independence_wave_dm01_costs_reserved`.
  - Added `custom_cost_text = independence_wave_cost_provisional_capital`.
  - The text is explicitly disclosure-only; payment remains in `independence_wave_start_provisional_capital_mission`.
- `common/scripted_localisation/006_independence_wave_decision_cost_localisation.txt`
  - Added force-tier and supply-node branches for the dynamic custom-cost text and blocked text.
  - The fallback is the viable tier, matching the existing payment trigger/effect fallback when no force level is published.
- `localisation/english/006_independence_wave_decisions_l_english.yml`
  - Added the main, tooltip, blocked, and six exact tier/basing cost strings.

## Behavior contract

The display shows infantry and support equipment for the published force tier. If the capital lacks a supply node it also shows the accepted transport alternative of 10 trains or 100 trucks. Existing payment logic still chooses one available alternative and reserves the bundle before mission activation; no second payment path was added.

## Evidence

- Offline Decision Modding wiki confirms missions share the regular decision attributes and supports `custom_cost_trigger`/`custom_cost_text`.
- Vanilla precedents use the same custom-cost fields and the existing Event 006 decisions already use the same localisation contract.
- Fresh `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, zero blocking diagnostics. The report remains partial because workspace-wide helper projections are deferred.
- Event 006 allocator, country API, strict flags, SCN-008, FORM-16, and Statehood Ledger semantic audits remain passing; runtime GUI rendering/save-load is still not claimed.

## Remaining risk

The mission is auto-activated rather than player-selected, so live tooltip rendering must still be checked by the user. No gameplay runtime was launched by the agent. The overall Event 006 package remains HOLD/PARTIAL because central package admission, weighted evidence, formable consumers, super-event 23 audio rights, and other documented gaps remain unresolved.
