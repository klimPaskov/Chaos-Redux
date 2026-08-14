# Event 006 Pacific decision factory-field repair handoff

Date: 2026-08-14

## Disposition

Implemented a narrow parser-compatibility repair in the Pacific decision source. The decision timer `modifier.civilian_factory_use` field now receives file-scoped `@` constants, matching the established Event 006 decision pattern and the value already defined by the shared decision constants. No cost amount, affordability trigger, AI score, duration, effect, cleanup, admission, Join, or localization behavior changed.

## Source change

Changed file: `common/decisions/006_independence_wave_pacific_decisions.txt`.

Added the two file-scoped mirrors required by the Pacific decision file:

- `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT = 1`
- `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_STANDARD = 2`

Replaced six `modifier = { civilian_factory_use = constant:independence_wave_decision_cost... }` values with the matching `@` mirrors in the HBX and FIJ project categories. The replacements are value-preserving: light remains `1` and standard remains `2`.

## Evidence and safety

- The offline Decision Modding reference documents decision `modifier` blocks and the local repository already uses file-scoped `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_*` values in the shared, evolution, formable, Catalonia, Brittany, Iceland, and IW-043/IW-058 decision files.
- The shared constants source remains authoritative for the values; the local mirrors exist only because this decision field does not accept the `constant:` token form used by other duration/trigger fields.
- The patch does not alter any `custom_cost_text`, `custom_cost_trigger`, `complete_effect`, `remove_effect`, `days_remove`, `ai_will_do`, or package gate.
- No new localization key is needed. Existing cost text continues to describe the same factory commitment and resource burden.
- The patch does not widen central adapter, content-attestation, preflight, reservation, scenario, or Join surfaces.

## Validation

- Confirmed all six replacements map one-to-one to the original light/standard values.
- Confirmed the Pacific decision source remains balanced and the changed lines are the only gameplay diff in that file.
- Confirmed `git diff --check` is clean for the source and this handoff.
- No probability compare is claimed because AI weights and candidate eligibility are unchanged; the current Event 006 probability evidence remains partial/score-only elsewhere.

## Remaining boundary

Event 006 remains HOLD/PARTIAL at the current authority boundary. This parser-field repair does not promote any package, resolve portrait/flag rights, or change the 32-attested / 161-unattested package boundary.
