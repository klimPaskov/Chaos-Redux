# Event 012 fixed political-power saving hints

Acceptance basis: the complete-Gods AI requirement and the accepted fixed-custom-cost repair in `012_gods_decision_repairs_2026-10-07.md`.
Disposition: implemented source metadata, with native saving behavior and complete probability conclusions outside source proof.

## Implemented scope

Nine decisions advertise their existing fixed political-power charge through `ai_hint_pp_cost`.
The protection decision retains its existing hint.
Every hint uses a file-local numeric constant, and every actual charge remains owned by the existing shared script constant and payment helper.
No affordability predicate, debit, recipient credit, willingness expression, timer, outcome or displayed price changes.

| Decision suffix after `gods_of_africa_` | PP hint | Authoritative shared constant |
| --- | ---: | --- |
| `ultimatum_pay_settlement` | 150 | `gods_of_africa_ultimatum.settlement_pp` |
| `council_speech` | 25 | `gods_of_africa_council.speech_pp` |
| `prepare_defensive_defiance` | 15 | `gods_of_africa_transaction.defensive_preparation_pp_cost` |
| `harden_stockpiles` | 15 | `gods_of_africa_transaction.defensive_stockpile_pp_cost` |
| `secure_transport` | 15 | `gods_of_africa_transaction.defensive_transport_pp_cost` |
| `prepare_countermeasures` | 15 | `gods_of_africa_transaction.defensive_countermeasure_pp_cost` |
| `protect_partner` | 10 | `gods_of_africa_transaction.protection_pp_cost` |
| `arm_offender_enemies` | 25 | `gods_of_africa_coalition.pp_cost` |
| `send_expedition` | 25 | `gods_of_africa_expedition.pp_cost` |
| `coerce_occupier` | 50 | `gods_of_africa_occupier_coercion.pp_cost` |

`seek_reconciliation` offers either free victor recognition or a 10 PP reparations payment.
Its canonical effect selects free recognition first, and its affordability predicate accepts that route without political power.
A static 10 PP hint would misstate the free branch, so this mixed-price decision retains no fixed hint.
Dynamic tribute and substitute quotes also retain their existing affordability logic.
This correction covers fixed-price decisions without changing the accepted free route or assuming a dynamic hint field.

## Files and checks

`common/decisions/012_africa_gods_decisions.txt` contains the nine fields and file-local literals with their shared-charge references.
The existing `.tools/validation/test_012_gods_response_phases.js` checks all ten hints against their shared constants and rejects a fixed hint on the mixed free/paid row.
Its remaining checks still compare the 49 original decisions' prices, willingness blocks, mission fields and gameplay bodies against the frozen phase baseline.
All 21 groups passed after this patch, with ten matching fixed PP hints.
The result is `012_gods_ai_budget_hints_source_model_2026-10-08.json`.
No new test framework or gameplay helper was added.

The probability specialist owns the BEFORE snapshot, bounded same-scenario comparison and adapter-coverage limits in `012_gods_ai_budget_hints_review_2026-10-08.md` and its evidence directory.
Its source inspection completed and the independently reviewed nine hint mappings agree with their payment and affordability owners.
The wider evaluation remained pending, and the final narrowed comparison for ultimatum settlement at exactly 150 PP returned no receipt during a 30-second bounded wait.
The server-side result is unknown, so this is an unresolved comparison rather than a claim that the route failed.
Willingness-score results cannot establish the native AI's saving behavior or purchase timing.
No new artwork, localisation key, catalog field or public value is required because all prices and player choices are unchanged.
Existing icons and cost text remain attached to the same decisions.

## References

Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:325–336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, was read through MCP.
It documents that custom costs do not teach the AI to reserve PP and that `ai_hint_pp_cost` accepts a constant amount, not a variable.
Installed `common/script_constants/documentation.md:1–34`, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`, restricts `constant:` access to documented fields.
Installed `common/decisions/_documentation.md:1–46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, establishes decision trigger scope and cadence.
Vanilla `common/decisions/CHI_decisions.txt:7922–7927` pairs a static 125 PP hint with custom affordability and cost text in `CHI_press_warlord_to_become_puppet`.
MCP source lookup located that decision at source revision `e539c52bcd4fb3347f84819379d207b431f5502346e8f703706cd8cea6f02e66`, and the exact surrounding source was read locally.
The existing Gods protection hint supplies the repository's file-local literal precedent.

## Remaining acceptance

Native reserve planning, competing purchases and actual purchase timing remain unverified.
No gameplay simplification, substitute price, skipped fixed-price row or paid-route deletion is adopted.
The full Gods goal remains incomplete while its broader native, AI and asset acceptance items remain open.
