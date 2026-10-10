# Event 093: validation report

Date: 2 October 2026, condensed in the 10 October 2026 spec audit.

## What the bundled tests cover

The [standalone design tests](093_treaty_of_tordesillas_restoration_validation_tests.py) ran **56 tests with 0 failures, 0 errors, and 0 skips** on 2 October 2026, recorded in the [results file](093_treaty_of_tordesillas_restoration_validation_results.json).
They check a simplified Python reference model of selected proposed rules, not the game engine, the actual map, AI behavior or balance.

| Group | Tests | What was exercised |
| --- | ---: | --- |
| Geography | 8 | Longitude wrapping, half-open boundaries, equal arc sampling, represented land majority, deterministic ties, and invalid input |
| Frozen weights | 7 | Normalization, proportions, immutable snapshots, duplicate-state protection, zero-industry handling, and rejection of duplicate identifiers |
| World-end readiness | 12 | Both crowns' independent thresholds, strict Chaos above 1000, political eligibility, joint consent, confidence, stage, scenario ownership, and sustained readiness |
| Civil-war aid | 7 | Promised versus delivered aid, earning threshold, minimum component delivery, oversupply limits, and invalid contracts |
| Regional projects | 9 | Population and state-count tiers, region-size rejection, recent-conquest adjustment, composed speed factors, duration rounding, and minimum duration |
| Transactions and ownership | 13 | Actual-paid refunds, no repeated refunds, nonrefundable components, ownership versus occupation, native-core consent, protected homelands, receiving sphere, and claim provenance |

The 10 October 2026 audit changed rules the suite does not model: quarter-package installments, the volunteer credit, per-state compliance without a regional average, the coercive settlement floor, and the concentrated-pace pause rule.
The existing tests remain valid for the rules they cover; the new rules are acceptance journeys in Part 18.
If the model and prose disagree, the specification is the design authority.

Run the suite from this folder with Python 3.10 or newer and the standard library:

```bash
python 093_treaty_of_tordesillas_restoration_validation_tests.py --json 093_treaty_of_tordesillas_restoration_validation_results.json
```

## Not yet verified

Installed-game checks remain implementation work: the map projection and state geometry, live Spanish Civil War identities and transitions, native focus-tree collisions, the Anarchist Spain coring benchmark, script support, AI probability, cost and debit parity, performance, GUI and focus rendering, and world-end framework integration.
Final media, quotations, audio and localization are research and production tasks.
Numerical parameters are proposed tuning; faster coring than Anarchist Spain is a design target, not a measured result.

Keep Event 093 at **To Be Reworked** until implementation and the user's live tests justify a status change.
