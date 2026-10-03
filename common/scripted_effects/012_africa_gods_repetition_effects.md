# Gods recent demand repetition

Repetition tracks actual committed consecutive contracts of the same family, including the exact truck/artillery subtype, within the configured interval from the previous contract's creation.
The interval is `gods_of_africa_timing.repetition_window_days = 365`.
The existing threshold and ten-percentage-point surcharge remain unchanged.
Three recent matching prior contracts satisfy the threshold for the fourth; unrelated history entries never establish repetition.

`gods_of_africa_is_repeating_demand = yes` is a COUNTRY trigger.
The caller initializes temporary `gods_of_africa_repetition_family` and `gods_of_africa_repetition_mobile_type` before invoking it.
Non-mobile callers supply zero for the optional type, which is not interpreted as a valid truck/artillery subtype.
The trigger requires normal last-demand family/day, matching family, matching last subtype for family 2, and nonnegative age no greater than the configured window.
Its temporary age is internal scratch, not an output or country-scoped variable.
Missing previous receipt fails closed.

`gods_of_africa_repetition_scale_applies = yes` adds the existing normal repetition-count threshold to that same receipt predicate.
The owner quote initializes the temporary inputs from its selected family/type in participant scope and uses the resulting boolean before existing quantity caps and affordability checks.
No quote or failed capacity check changes repetition state.

`gods_of_africa_remember_demand_repetition = yes` is a participant COUNTRY effect called only after genuine contract family, optional type, identity, generation, deadline and open status are written.
It requires a current legal contract, valid family, and a contract ID/generation different from its prior recorded pair.
Matching recent family/type increments normal `gods_of_africa_repetition_count`; otherwise it starts at one.
It stores normal last family, optional type, creation day, recorded contract ID and generation.
A non-mobile contract clears the previous optional type.
Repeated invocation for the same contract is a no-op.
Ordinary response, extension, partial payment, accepted substitute and aid cannot advance or retype this original demand receipt.

History initialization already initializes the repetition count only once.
Re-entry and contract cleanup preserve these private receipts, while the age and family comparison prevent obsolete history from generating a surcharge.
Changing the family/type or exceeding the window resets the streak on the next actual contract.
No array, event, meter, clock, price, AI score, or asset is introduced.

Example before participant quote evaluation:

```text
set_temp_variable = { gods_of_africa_repetition_family = event_target:africa_host.gods_of_africa_selected_family }
set_temp_variable = { gods_of_africa_repetition_mobile_type = constant:gods_of_africa_value.zero }
# For family 2, copy the valid selected subtype before invoking the trigger.
gods_of_africa_repetition_scale_applies = yes
```

The existing family-capacity and immutable transaction rules remain authoritative after the percentage adjustment.
Useful acceptance cases are first through fourth consecutive demands, a family change, a truck/artillery change, age 365 versus 366, negotiation-only history, a failed quote, replay of a committed contract, and preserved history after re-entry.
The independent source audit and runtime limits are recorded under `docs/plans/012_africa_plans/subagent_handoffs/`.
Native trigger arithmetic and conditional-trigger syntax use the installed trigger sections and offline Data structures references already retained by the equipment helper contracts.
No engine execution or complete balance/goal acceptance is inferred from a source case calculation.
