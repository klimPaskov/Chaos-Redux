# Medical reserve batch cost and presentation

**Acceptance basis:** The September 2026 CBRN simplification and presentation request requires a readable medical-reserve decision row, upfront payments shown once, and the displayed requirements to match actual deductions. This correction applies that accepted direction to Event 020's existing Stock Reserves decision.

Each medical-reserve batch consumes 150 support equipment and 1,000 fuel when started. Three civilian factories and two response-capacity slots remain committed for 42 days. The batch also requires 2,500 available personnel and 60 trucks in stock; these are readiness requirements and are not spent. The batch must fit the remaining reserve capacity.

The inline cost row shows the support-equipment, fuel, and civilian-factory commitments with their matching icons. The ordinary requirement tooltip explains the personnel and truck requirements, response-capacity commitment, duration, and reserve-capacity limit. A shared inclusive predicate gates both the displayed cost and the action; an exact stockpile match qualifies. The payment effect debits only the two immediate material costs, once at start. Canceling a batch does not refund material already used.

Implementation: `common/decisions/020_black_plague_response_decisions.txt`, `common/scripted_triggers/020_black_plague_response_triggers.txt`, `common/scripted_effects/020_black_plague_response_action_effects.txt`, `common/script_constants/020_black_plague_response_constants.txt`, and `localisation/english/020_black_plague_response_l_english.yml`. The shared response payment helper remains unchanged for other actions.

This correction covers one decision's cost presentation. Event 020's wider state-response cost rows and native decision-list rendering still require separate review.
