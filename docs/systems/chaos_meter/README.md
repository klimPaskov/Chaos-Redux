# Chaos Meter documentation

This directory documents the shared Chaos Meter, deaths accounting, war-declaration counting, nuclear-use escalation, and meter-window behavior.

## Navigation

- [`chaos_meter_popup_window.md`](chaos_meter_popup_window.md) is the shared meter-window and source-ledger presentation contract.
- [`chaos_meter_deaths_mechanic.md`](chaos_meter_deaths_mechanic.md) defines the deaths accounting model and its Chaos conversion.
- [`chaos_meter_combat_contamination_occupation_deaths.md`](chaos_meter_combat_contamination_occupation_deaths.md) defines combat, contamination, and occupation death sources.
- [`chaos_meter_deaths_and_events_log_ui.md`](chaos_meter_deaths_and_events_log_ui.md) defines the deaths data exposed to the Chaos Meter and Event Logs surfaces.
- [`chaos_meter_war_declaration_counting.md`](chaos_meter_war_declaration_counting.md) defines the qualifying war-relation contributions.
- [`nuclear_chaos_ladder.md`](nuclear_chaos_ladder.md) defines direct Chaos gains, escalation tiers, and the shared non-yield Event 23 test-accident consequence endpoint.

Atmospheric contamination belongs in [air_cleanliness/](../air_cleanliness/README.md).
Condemnation and CBRN consequences belong in [cbrn_warfare/](../cbrn_warfare/README.md).

## Unresolved presentation contract

The [deaths/UI pass record](chaos_meter_deaths_and_events_log_ui.md) describes a per-country details overlay.
The [popup contract](chaos_meter_popup_window.md) and [deaths mechanic](chaos_meter_deaths_mechanic.md) describe that overlay as disabled or absent.
These are conflicting recorded interface states, and this documentation pass does not select either as current behavior.
Reconcile the linked GUI consumers and matching MCP state fixtures before promoting one description or superseding the other.
The pass record retains its historical cache, sorting, and selection findings.

## Meter contributions

The first qualified human-major pulse of an observed continuous justification against an existing human target contributes +1, and major human democratic elections contribute -1.
Ruling-party changes contribute the configured democratic or non-democratic value on every change, including changes between two non-democratic governments.
Puppeting contributes +3, release as free contributes -5, subject freedom contributes -3, and a major leaving a non-democratic faction contributes -5.
These values remain centralized in `common/script_constants/chaos_meter_constants.txt`.
Justification and election contributions use the existing engine on-actions and record actor-attributed history.
Their helper boundaries revalidate those qualifications and clear temporary change/reason outputs on rejected calls, preventing a stale contribution from another callback.
Justification observation continues during disabled, nonmajor and nonhuman intervals without contributing Chaos or history.
Each actor-target pair stores its last native calendar pulse day and a counted flag; duplicate and contiguous daily pulses cannot contribute again, while a full day without an observed pulse rearms the pair.
Immediate restarts and parallel goals against the same target are one observable threat signal because the native API exposes no justification identity or cancellation callback.
The COUNTRY helper stores `chaos_meter_justification_last_seen_day_@FROM` and `chaos_meter_justification_counted_@FROM`; no event target or global registry is created for this receipt.
It uses the native `num_days` calendar getter and `chaos_meter_justification.contiguous_gap_days = 1`, so a same-day duplicate or next-day pulse retains the receipt and a later pulse after a full missing day clears the counted flag before qualification.
Cleanup is lazy at the next valid pair pulse: overwrite the last-seen day and rearm only on that observed gap.
Observation-only calls leave temporary change/reason outputs at zero and make no actor history, Chaos contribution or human-penalty changes.
War relation counting suppresses faction follow-ups and limits each actor's minor-war contribution to 5 per day while preserving the configured 1/5 minor/major anchors.
Military casualty contributions use the pre-March direct scaling while Deaths keeps military accounting without double conversion.
The nuclear ladder, Event 23 distinctions, missile integrations, slight disabled-default crisis pressure, and tier-based UI fractures keep their separate behavior.
