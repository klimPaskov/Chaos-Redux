# Event 35 late Industrial Boom supplier entry

Disposition: source implementation under the full Event 35 supplier-adapter acceptance contract.
This repairs the late-entry dependency recorded in D34 of `agent_decisions_2026-10-05.md`.
Full Event 35 acceptance remains open.

The selected country in `chaosx.nr34.1` calls `great_depression_event34_supplier_adapter` immediately after `industrial_boom_active` is set when the worldwide depression is active.
The adapter initializes the same dynamic material quote used by existing reconstruction guests and records the supplier context on that country.
An ordinary boom outside the worldwide episode does not enter that response path.
The existing supplier-risk helper admits an at-risk country once within its cap.
The activation hook performs no material debit.

Changed source is `events/034_industrial_boom.txt`.
The source regression coverage is `LateBoomSupplierEntryTests` in `.tools/test_event035_reports.py`.
It executes the actual parsed activation slice and its production adapter, quote and risk helpers under a foreign ROOT.
The fourteen-test report suite passes, including the existing exact/below/above material affordability and actual conference payment cases.
The activation cases cover the late contractless supplier, ordinary boom, and supplier-risk replay.
Native event selection, UI rendering and delayed engine execution remain outside those fixtures.

The immutable before source is `audit_inputs/supplier_entry_2026_10_07/034_industrial_boom_before.txt`, SHA-256 `75707B53B4F29F0259620529E4BC3B4B3EE54949E865B3BC199B71D4824705EC`.
The four saved source cases are `SUP-LATE-WORLD-ACTIVE`, `SUP-ORDINARY-BOOM`, `SUP-RISK-REPLAY`, and `SUP-QUOTE-AFFORDABILITY`.
The isolated probability audit is `late_supplier_probability_2026-10-07.md`.
Its definition-level inventory and source scenarios must not be reported as campaign click probabilities.

The connected source lookup returned the complete adapter definition at `common/scripted_effects/035_great_depression_effects.txt:6798-6818`, revision `cc73412e7c5f3acad2241efa29c7c27a2a6eb9a2b3f7d99abc8696d4f8d1f68c`.
Its two dependency bodies were inspected directly: quote preparation and bounded supplier-risk registration.
Installed `set_variable` documentation at lines 7888-7895 was read through the reference service at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline scope rules at `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:253-268` establish THIS and the enclosing ROOT distinction.
The installed supplier adapter check in declared COUNTRY scope returned `SCRIPT_CHECK_PARTIAL`, valid null, nine checked commands, two unresolved scripted dependency calls, and one unchecked variable argument block.
The primary command kinds and country scopes are supported, while dependency and parameter review remain separate evidence.

The read-only event comparison uses the real frozen Event 34 source as an in-memory overlay against the current source.
Its orientation is current-to-proposed-before and must be inverted when reporting chronology.
The four-node comparison with `refresh = true` timed out after 600 seconds, and the one-node retry with `refresh = false` returned the same timeout.
Neither request returned a revision or artifact, so structural comparison remains unresolved.
The isolated probability owner's two same-scenario before/after comparisons also timed out, including its narrower retry.
Its narrowed after-source evaluation returned a 100% conditional share for the single later popup option `chaosx.nr34.2.a` in all four cases, with a complete one-option pool.
This result measures neither event firing nor supplier selection or eligibility, and no numerical before/after delta is available.
The conference decision pool and its declared conference, quote, reserve and profile inputs remain incomplete in that native audit.

This hook introduces no event ID, visible text, asset, quote rate, evolution charge, or scheduler.
The existing Event 34 report, supplier response decisions, icons, and cost localisation remain its consumers.
The catalog's player-facing detail wording is unchanged by this activation dependency.
