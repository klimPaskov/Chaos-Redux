# Event 016 technology provenance range checkpoint

## Scope and disposition

This parent-owned patch enforces the source-ID range already documented by the custom-technology API.
It does not extend the seven operational selectors, add a technology, alter an outcome, change random weights, or complete the conventional-portfolio parity work.
No model, GUI, localisation, Event Log, catalog, provider credit, or game runtime was touched.

## Defect and correction

The receipt formula is `selector * 1000000 + source`, but both writers previously checked only the lower source bound.
Portal family 1 with source 1000025 therefore produced the same receipt, 2000025, as clone family 2 with source 25.
The documentation already required sources below the stride, but the implementation did not enforce it.

`chaosx_custom_technology_source_is_valid` is a country-scope read-only query over the optional temporary or country source variable.
It requires an existing source at least `provenance_minimum_source` and strictly less than `provenance_stride`.
Both operational and upgrade provenance writers call this query before encoding or appending a receipt.
Missing or out-of-range provenance remains optional: it writes no receipt and does not block an otherwise valid technology grant.
Existing receipt arrays are not rewritten, deleted, decoded, or attributed to a guessed source.
The Event 025 and Event 036 source IDs remain valid.

## Changed files

- `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt`: shared source-range query.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`: two writer guards and input comments.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`: precise source contract, query scope/input/default/side effects, and usage example.
- `common/scripted_effects/chaosx_dynamic_effects.md`: owner index points to the explicit API contract and provenance query.
- This checkpoint.

## Review and meaningful checks

The required offline Data structures and Triggers references and installed `triggers_documentation.md` entries for `check_variable` and `has_variable` support the range query.
The source uses the existing shared minimum/stride constants; no tuning value or selector was added.

A direct before/after block comparison against source frozen at `f3725655256cf5e98374366c5b63c8d44a3fc6a0` found the operational core, public operational grant, public upgrade grant, random operational grant, and external alien-recovery grant byte-equivalent after newline normalization.
Only provenance writer guards changed their executable bodies.
The existing `is_in_array` membership guards still make repeated valid receipts idempotent.

The arithmetic boundary check rejected missing, -1, 0, 0.5, 1000000, and 1000025 sources, and accepted 1, 25, 36, and 999999.
Representative valid sources across all seven family IDs yielded 28 distinct receipts; the former cross-family collision is excluded at the input boundary.
This arithmetic/source check is not an HOI4 engine execution test.

The read-only probability owner retains the prepatch source for the existing random-grant and conventional-action baseline.
This patch changes no weighted expression or random candidate eligibility, but the broader API's required MCP and scenario comparisons remain open.
No whole-technology, Event 016, or live acceptance is claimed.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was changed and no fallback was introduced.
