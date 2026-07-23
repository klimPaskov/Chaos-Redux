# School in the Vent Room chain proof

Status: dormant, statically reconciled, not release-floor credit.

## Contract proof

- Candidate 289 uses transaction key 710015 and route 7115.
- Events 289 through 295 are defined once. The seven blocks are one human
  opening, one hidden-AI opening, one human delayed result, one hidden-AI
  delayed result, one human callback, one hidden-AI callback, and cleanup.
- The candidate gate requires the durable First Safe Birth memory, one recorded
  generation change, the 360 through 899 campaign window, Cohesion at least 35,
  Food at least 25, Shelter at least 35, and one affordable curriculum.
- Candidate severity is a clamped generation-count score. Mechanic pressure is
  zero. Food supplies the state value and the survival-resource pressure source.
- The opening freezes Cohesion, Food, Shelter, Recognition, generation count,
  education, and exposure before the delayed result is reserved.
- Four manually authored curricula have separate costs, success thresholds,
  partial thresholds, failure outcomes, memory flags, and timed modifiers.
- Result and callback failure requests use
  `apply_exact_state_civilian_population_loss` through the shared Deaths
  contract. The result rate is 0.0012 and the callback rate is 0.0006.
- History 9120 has fifteen payloads and is registered in the shared Event Log
  type, detail, and name selectors.
- Cleanup releases exact result and callback receipts, then clears transaction
  variables and transient flags while retaining curriculum and cohort memory.
- A dedicated report image is registered as
  `GFX_report_event_fallout_school_vent_room`.

## Static audit

The chain source is checked for balanced braces, unique event ids, unique
localisation keys, defined constant groups, dedicated asset references, and no
unsupported `<=` or `>=` operators. Hearts of Iron IV was not run. The
scheduler activation flags remain without setters, so the chain earns no
release-floor credit.

A refreshed read-only `hoi4.event_inspect` lint request targeted
`chaosx.fallout.289` with helper expansion disabled and traversal bounded to 40
nodes, 80 edges, and depth 2. The installed service returned status `ok` with
code `EVENT_INSPECTED_PARTIAL`. It reported no source-specific diagnostic, but
the workspace-wide artifact contained 17,709 issues, 1,969 blocking diagnostics,
an inline source inventory truncation notice, and a 200,000 derived-edge
ceiling. This is tooling evidence only. Direct source inspection remains the
authoritative audit for this dormant chain.
