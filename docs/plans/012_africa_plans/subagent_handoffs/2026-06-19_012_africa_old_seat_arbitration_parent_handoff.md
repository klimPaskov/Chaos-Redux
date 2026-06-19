# Event 012 Africa Old-Seat Arbitration Parent Handoff

Date: 2026-06-19

## Scope

This tranche adds the Authority Atlas old-seat arbitration layer on top of settled historical dossiers.

## Gameplay Surface

- `africa_convene_old_seat_arbitration` starts the next eligible rivalry hearing after the required dossier settlements exist.
- `africa_old_seat_arbitration_mission` runs as a one-active-at-a-time 120-day mission. The 60-day convene decision cooldown is handled through `days_re_enable` and does not create a second active hearing because `africa_old_seat_arbitration_active` gates starts.
- Six rivalry cases are registered: Great Lakes, Central River, Western Crowns, Red Sea, Monsoon Rova, and Sahel Caravan.
- Starting a hearing spends political power, support equipment, manpower, command power, and army experience through `africa_pay_old_seat_arbitration_cost`.
- Success requires the stored old-seat state to remain controlled by the unifier or a loyal Charter-side actor and requires pair-specific value gates.
- Success records the settled pair, increments `africa_old_seat_arbitration_count`, moves pair-specific values, and fires `chaosx.nr12.51`.
- Failure leaves the pair retryable, applies pair-specific pressure plus sovereignty/debt pressure, and fires `chaosx.nr12.52` with `GetAfricaOldSeatArbitrationFailureSummary`.

## Subagent Audit Follow-Up

- `chaosx_decision_mission_auditor` changed the convene decision from a stale `days_remove` timer to `days_re_enable = constant:africa_decision_days.old_seat_arbitration` and aligned the decision description with the automatic next-eligible pair selection.
- `chaosx_scripted_system_architect` fixed the failure popup to use a failure-specific scripted localisation selector instead of reusing the success result summary.

## Files

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/ai_strategy/012_africa.txt`
- `events/012_african_union.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`

## Validation Notes

- Dynamic state-name localisation uses the supported `[?variable.GetName]` pattern documented by the offline Paradox wiki.
- The event picture `GFX_news_event_012_authority_atlas_archive_old_seats` is already registered in `interface/012_africa.gfx` and documented in the Event 012 asset manifest.
- The mission uses the same non-selectable mission pattern as the existing dossier resistance watch: `available` is the success gate and `timeout_effect` is the failure path.
- `days_re_enable = constant:...` has vanilla and local precedent, including vanilla SIA propaganda decisions and local Chaos Redux decision files.

## Remaining Event 012 Blockers

This tranche does not close the overall Event 012 goal. Remaining known blockers still include deeper package-specific historical dossier missions beyond settlement/resistance/arbitration value movement, fuller Continental Congress presentation families, targeted scenario validation, completion audits, final super-event sourcing/audio blockers, and spreadsheet alignment after implementation facts stabilize.
