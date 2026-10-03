# Humanitarian custom-cost parent-key closure, 2026-10-03

Disposition: implemented source localisation closure, parent review and native evidence remain separate.
Authorization: the parent explicitly assigned missing blocked and hover aliases for current famine and migration custom-cost consumers.
Only the two assigned YML files were appended, this handoff was added, and the auditor's original prospective report received a parent-patch disposition note.
No existing YML lines were changed by this auditor.
No staging or commit was performed.

## Changed files and exact ownership

- `localisation/english/famine_l_english.yml`: 20 keys added for 10 cost families.
- `localisation/english/migration_l_english.yml`: 30 keys added for 15 cost families.
- `migration_cost_open_reception_blocked` and `migration_cost_open_reception_tooltip` already existed from the parent's patch and were preserved.

Each added value is the exact existing base-key alias, `"$base_key$"`.
The aliases reuse the same per-resource getters, colours, icons, and integer amounts.
They introduce no fees, stockpiles, metrics, mechanics, or new getters.

Exact 50 added keys:

```text
famine_cost_release_reserves_blocked
famine_cost_release_reserves_tooltip
famine_cost_emergency_imports_blocked
famine_cost_emergency_imports_tooltip
famine_cost_repair_relief_route_blocked
famine_cost_repair_relief_route_tooltip
famine_cost_escorted_relief_convoy_blocked
famine_cost_escorted_relief_convoy_tooltip
famine_cost_emergency_airlift_blocked
famine_cost_emergency_airlift_tooltip
famine_cost_invite_relief_blocked
famine_cost_invite_relief_tooltip
famine_cost_evacuation_blocked
famine_cost_evacuation_tooltip
famine_cost_requisition_safer_state_blocked
famine_cost_requisition_safer_state_tooltip
famine_cost_conceal_crisis_blocked
famine_cost_conceal_crisis_tooltip
famine_cost_maintain_extraction_blocked
famine_cost_maintain_extraction_tooltip
migration_cost_prepare_evacuation_blocked
migration_cost_prepare_evacuation_tooltip
migration_cost_open_departure_routes_blocked
migration_cost_open_departure_routes_tooltip
migration_cost_restrict_departure_blocked
migration_cost_restrict_departure_tooltip
migration_cost_close_border_blocked
migration_cost_close_border_tooltip
migration_cost_evacuate_vulnerable_blocked
migration_cost_evacuate_vulnerable_tooltip
migration_cost_evacuate_workers_blocked
migration_cost_evacuate_workers_tooltip
migration_cost_negotiate_corridor_blocked
migration_cost_negotiate_corridor_tooltip
migration_cost_controlled_medical_reception_blocked
migration_cost_controlled_medical_reception_tooltip
migration_cost_distribute_arrivals_blocked
migration_cost_distribute_arrivals_tooltip
migration_cost_transit_only_blocked
migration_cost_transit_only_tooltip
migration_cost_enforce_closure_blocked
migration_cost_enforce_closure_tooltip
migration_cost_local_integration_blocked
migration_cost_local_integration_tooltip
migration_cost_third_country_resettlement_blocked
migration_cost_third_country_resettlement_tooltip
migration_cost_voluntary_return_blocked
migration_cost_voluntary_return_tooltip
migration_cost_forced_repatriation_blocked
migration_cost_forced_repatriation_tooltip
```

## Consumer pairs

All 10 `famine_*` decisions in `common/decisions/famine_decisions.txt` map to their correspondingly named `famine_cost_*` bases.
The inspected pairs are release_reserves, emergency_imports, repair_relief_route, escorted_relief_convoy, emergency_airlift, invite_relief, evacuation, requisition_safer_state, conceal_crisis, and maintain_extraction.

All 16 `migration_*` decisions in `common/decisions/migration_decisions.txt` map to their correspondingly named `migration_cost_*` bases.
The inspected pairs are prepare_evacuation, open_departure_routes, restrict_departure, close_border, evacuate_vulnerable, evacuate_workers, negotiate_corridor, open_reception, controlled_medical_reception, distribute_arrivals, transit_only, enforce_closure, local_integration, third_country_resettlement, voluntary_return, and forced_repatriation.
Open Reception's parent-owned pair is counted in total coverage and excluded from added-key ownership.

Every current consumer has exactly one base, blocked, and tooltip key after the patch.
All getters called by these base keys resolve to either the existing neutral humanitarian cost selector file or the parent's reception preparation cost selector file.
The associated literal ready/blocked outputs are supplied by existing humanitarian cost YML or migration YML.
No duplicate cost keys or missing consumer/getter references were found in the bounded final source checks.

## Before and after

Before, 25 cost families lacked the engine-selected blocked and hover parent keys.
After, all 26 current families resolve base, blocked, and hover names through existing dynamic cost text.
This repairs localisation wiring and does not establish that native raw identifiers were observed before the patch.

Existing-file preservation was checked against pre-append content after removing only the 50 owned alias lines from the result.
Both files retained every previous line, including the parent's revised descriptions, Open Reception aliases, cost values, dynamic tokens, and flag text.
UTF-8 BOMs were preserved.
No quote-bearing surface was edited.

Vagueness, bloat, obvious explanation, repetition, overcomplication, and style rules: the new aliases contain no new prose and no new sentence punctuation.
The parent's three accepted prospective prose corrections were verified separately in final source.
No new quotation, historical claim, route promise, or payment explanation was introduced.

## Remaining affordability and presentation concerns, outside patch scope

The unchanged neutral `humanitarian_cost_scripted_localisation.txt` selectors use strict `>` comparisons at their nominal amounts, including political power, equipment, fuel, and air XP.
This closure deliberately does not retune those selectors or the corresponding decision affordability/payment gates.
The parent-owned Open Reception family uses the separate inclusive constant-based selectors and shared affordability predicate.
A parent alias cannot correct an existing exact-holdings affordability rule or prove that a resource colour matches a different decision gate.

The unchanged escorted-relief-convoy, emergency-airlift, and third-country-resettlement base strings each contain four displayed resource entries.
The decision skill's compact inline display limit is three values, but changing those existing strings is outside this append-only assignment.
Their base fees and payment contracts were preserved and this concern is a follow-up presentation review, not a claim of native clipping.

## Reference evidence

- Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:311`–329 documents the base, blocked, and tooltip key contract.
Its SHA-256 from the same-agent review is `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/toa_decisions_l_english.yml:340`–341 defines `BRA_decision_cost_cangaceiro` and its blocked form.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt:490`–496 consumes that exact base through `custom_cost_text` under a custom command-power affordability gate.
- Installed decision documentation scope and cadence references remain in the original prospective handoff.

Skills used: chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-subagents.
No skills were changed.

## Validation limits

Meaningful validation covered all 26 current custom-cost consumers, their existing bases and getter names, the 52 total suffix keys, exact alias targets, and preservation of previous YML content.
The source checks found no unresolved missing or duplicate keys in this assigned cost family.
No engine, raw-key runtime, GUI wrapping, overflow, colour rendering, affordability retuning, AI, or physical-transfer result is claimed.
The parent's task authorized source-only closure and the earlier connected route timeouts remain documented in the prospective handoff.
No duplicate heavy MCP or GUI request was made, and no new artifact URI was returned.
No game was launched, no logs were read, and the workbook/export-only CSVs were untouched.
No simplification was made within the requested alias closure.

