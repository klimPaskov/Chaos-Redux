# Fallout Empty Ward chain proof

Status: dormant, statically reconciled, not release-floor credit.

## Contract proof

- Candidate 296 uses transaction key 710016 and route 7116.
- Events 296 through 302 are defined once. The seven blocks are one human
  opening, one hidden-AI opening, one human delayed result, one hidden-AI
  delayed result, one human callback, one hidden-AI callback, and cleanup.
- The candidate gate requires the closed School memory, one Fever Dormitory
  outcome memory, the 500 through 1199 campaign window, Cohesion at least 30,
  Medicine at least 15, Shelter at least 30, and one affordable policy.
- Candidate severity is a clamped recorded-Deaths score. Mechanic pressure is
  zero. Medicine supplies the state value and survival-resource pressure source.
- The opening freezes Medicine, Shelter, Cohesion, Recognition, generation
  count, ward capacity, research, trust, and durable exposure before the
  delayed result is reserved.
- Four manually authored policies have separate costs, success thresholds,
  partial thresholds, failure outcomes, durable institution flags, and timed
  modifiers.
- Result and callback failure requests use
  `apply_exact_state_civilian_population_loss` through the shared Deaths
  contract. The result rate is 0.001 and the callback rate is 0.0005.
- History 9121 has fifteen payloads and is registered in the shared Event Log
  type, detail, and name selectors.
- Cleanup releases exact result and callback receipts, then clears transaction
  variables and transient flags while retaining ward capacity, research, trust,
  durable exposure, and policy memory.
- A dedicated report image is registered as
  `GFX_report_event_fallout_empty_ward`.

## Static audit

The chain source is checked for balanced braces, unique event ids, unique
localisation keys, defined constant groups, dedicated asset references, and no
unsupported `<=` or `>=` operators. Hearts of Iron IV was not run. The
scheduler activation flags remain without setters, so the chain earns no
release-floor credit.

Two read-only `hoi4.event_inspect` lint requests targeted
`chaosx.fallout.296` with helper expansion disabled and bounded traversal. The
first request ended with a closed inspection transport and the retry returned
the same transport failure. No runtime result is claimed from this service.
Direct source inspection remains the authoritative audit for this dormant
chain, and the transport failure is an engine-sensitive proof limitation.
