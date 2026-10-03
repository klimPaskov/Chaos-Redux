# Event 021 ticket iteration baseline fixture

Disposition: baseline source and named edge fixture; no campaign probability or balance approval is claimed.

Use the unchanged named TGT/SCN cases from `event021_dynamicity_recovered_expected_pre_edit_2026-09-26/scenario_matrix_fixture.md` for the manual pool comparison.

Add `SCN-TICKET-1000`: a declared scope-array fixture has more than 1,000 ticket entries and includes the selected country in the prefix before its final 1,000 entries.
The removal helper must erase every selected-country entry, retain every other entry in its original order and multiplicity, and preserve the draw's base ticket weights.
This case tests array iteration and uniqueness only; it supplies no live world roster, observed selection probability, or campaign incidence.

The exact synthetic fixture has 2,005 entries indexed 0 through 2,004.
GER is the selected-country token at indices 0, 100, 1,004, and 2,004.
Every other even index is FRA and every odd index is BRA.
These are synthetic scope labels, not a declared campaign roster or eligibility state.
The before numeric-loop model visits only the final 1,000 positions, leaving three GER entries.
The repaired traversal leaves no GER entry and retains FRA's 999 and BRA's 1,002 entries in their original order.
The comparison must preserve the named fixture and base ladder; it must not infer a campaign repetition frequency from this model.

The archived parent-effects file is an immutable byte copy taken before this specific ticket-removal repair.
The earlier dynamicity snapshot remains a separate historical baseline for the larger front migration and must not be mislabeled as this repair's immediate baseline.

The candidate-effects snapshot additionally preserves the current region-score indexing surface as a regression check.
Add `SCN-REGION-SCORE-INDEX`: two aligned source states have scores 10 and 90, but only the second state satisfies the neighboring-state filter.
The filtered candidate must retain score 90 and source index 1.
The current source advances the source index outside its filtering `if`, which satisfies this relationship; moving the increment inside the filter would pair that state with score 10 and index 0.
This deterministic score-alignment fixture changes no balance value or country selection probability.
