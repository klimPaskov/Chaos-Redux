# Greenland Sale: source and decision register

Package checkpoint: `GS-092-D1`.
Date: 2 October 2026.
This is a complete parent-authored design draft with open tooling and engine-verification gates.
It is not user approval of every added tuning choice and is not an implemented or independently audited completion claim.

## Authority

The user's supplied Greenland Sale brief is the authority for the event's premise, catalog identity, high-bid rule, live value and ownership, four evolutions, continuing market, and named connections.
The current uploaded AGENTS and skill files govern planning method and delivery.
The 13 parts expand the brief within that requested planning scope.
Proposed additions are identified below and can be revised explicitly without changing what the user originally required.

The supplied CSV is an export-only catalog snapshot, not a workbook edit.
Its ID 92 row says Greenland Sale, Minor Fire-Once, Chaos level 1, no cluster, To Be Reworked, with empty evolution fields and the summary that countries compete to buy Greenland.
The user's detailed four evolutions supersede the empty export fields for this design.
The package does not change the CSV, workbook, repository status, or unrelated event catalog rows.

## Pinned repository evidence

Repository: `klimPaskov/Chaos-Redux`.
Inspected commit: `5212636eef9f9607691ddc1348bddade1bafe0dd`.
Read-only GitHub access was used.
No repository files were changed, staged, committed, or pushed.

| Evidence | Read extent | Finding used |
| --- | --- | --- |
| R01, `events/092_greenland_sale.txt`, blob `ff360c750670be9ca619228bbd220c2faf57aded` | Full | `chaosx.nr92.1` dispatches to Denmark, and offers go to majors or humans. This is legacy behavior to replace, not the new eligibility rule. |
| R02, `common/decisions/092_greenland_sale_decisions.txt`, blob `05acf34edf060ce16a6182f5982d8ad388168ec5` | Full | `buy_greenland` costs 250 PP, credits Denmark, and transfers state 101. It is an immediate purchase, not an auction. |
| R03, `common/decisions/categories/092_greenland_sale_categories.txt`, blob `06188cce8779e61b91e1f235e3161a45e4e9dd05` | Full | Existing `chaosx_greenland_sale_category` and `GFX_decision_cat_picture_greenland_sale` consumer. |
| R04, `localisation/english/092_greenland_sale_l_english.yml`, blob `0181c42c5cf76cee427b74f9f94f54bf573a6bbd` | Full | Existing seller description is blank and legacy result wording cannot describe every dynamic lot. |
| R05, `docs/systems/universal_cost_modifier.md`, blob `f053e8d76ef5d7232fd622a18b7ae7d9faa77e83` | Full | Quote, actual-paid receipt, refund, and settlement contracts exist in documentation. Factory commitments and unsupported resources need explicit adapters. The document does not claim universal live proof. |
| R06, native CIC and factory-use search matches | Snippets only | `events/066_cic.txt` has an `add_cic` use. Factory-use examples and an offline Effects wiki entry were found. These snippets do not establish a complete auction backend. |
| R07, `common/mtth/chaosx_mtth_variables.txt`, blob `54904ca88454809df5e5d1771634e597973a62f6` | Lines 1–150 only | Existing MTTH-entry style encountered. Full current reference reading and probability inspection remain open. |

The exact source URLs follow the pinned repository pattern below, substituting the recorded path.
They are references to retrieve, not a claim that a complete local repository was delivered.

```text
https://github.com/klimPaskov/Chaos-Redux/blob/5212636eef9f9607691ddc1348bddade1bafe0dd/<recorded-path>
```

## Choices made within the expansion request

| Decision | Basis and disposition | Design authority |
| --- | --- | --- |
| D01. Keep ID, name, Minor Fire-Once, level 1, no cluster and current status. | Explicit user requirement. | Part 01. |
| D02. Every eligible economic government may bid, without a major or historical-tag preference. | Explicit user requirement developed into symmetric rules. | Parts 01, 04, 05. |
| D03. Exact 240-hour unbeaten period and real higher-bid resets. | Resolves the user's approximate 10 days into a testable rule. | Part 01. |
| D04. 15-day inspection and 30-day no-first-bid window. | Parent proposal for funded preparation and a finite no-bid outcome. Not stated in the original brief. | Part 01. |
| D05. Fully prepaid, civilian-industry-backed Industrial Reserve with useful construction redemption. | Parent-selected economic design. Native production, debit, receipt and redemption proof remains blocked. | Part 02. |
| D06. No native market-bank conversion, no postpaid loan, no PP price fallback. | Parent choice to avoid unproved parity or unfunded principal. May change only through an explicit design revision with evidence. | Part 02. |
| D07. Founding reserve at 75 percent of assessed value, 5-point quantum, 5-percent minimum raises. | Proposed starting tuning, not measured balance. | Parts 01, 03. |
| D08. One seller for divided Greenland, selected by eligible land-province count, then assessed value, then stable identifier. | Resolves the user's requested split-ownership decision without forcing historical ownership. | Part 04. |
| D09. Protected capital and inhabited retained home, combined-sale check, actual ownership and full control. | Develops the user's no-extinction requirement and shared sovereignty constraints. | Part 04. |
| D10. Founding Greenland exception to ordinary core and strategic sale permissions. | Prevents an evolved-market restriction from blocking the user's original sale. Survival protections remain. | Parts 01, 04, 09. |
| D11. All four specified evolutions at 200, 400, 600 and 800. | Explicit user requirement. Separate permission combinations are a parent proposal honoring enable controls. | Parts 06–10. |
| D12. Market caps of 1 during the founding auction, then 2 or 3, with defined seller and state cooldowns. | Resolves the user's bounded-concurrency requirement. Exact pacing is proposed tuning. | Parts 06, 08, 10. |
| D13. Core sale costs 10 stability points, with a fixed prepublished construction pledge and a 5-point recovery. | Parent proposal making homeland disposal politically costly and giving proceeds a meaningful recovery use. | Part 09. |
| D14. Five bounded direct Chaos milestones, largest-only overlap, maximum positive total 35, one identified 5-point partial reversal. | Parent proposal required by the current event-planning skill's Chaos map. No routine bid or evolution charge. | Part 11. |
| D15. Four mastery achievements, compact native decision presentation, limited purposeful assets. | Parent additions required by the planning and presentation skills. | Parts 12–13. |
| D16. Single-state or coherent multi-state lots only, never arbitrary world parcels or a forced colonial tag. | Parent scope choice that deepens the market without unrelated country-package expansion. | Parts 04, 06–09. |
| D17. Exact numerical value weights and probability behavior remain calibration work. | Intentional planning-level boundary, not a hidden assertion that they are tested. | Parts 03, 05 and validation handoff. |

## Economic alternatives considered

A dynamic PP auction is easy to describe but does not provide the industrial cost and useful economic receipt requested by the brief.
It was rejected as the baseline rather than used as a silent approximation.
An equipment-barter basket can create genuine cost, but it introduces variant, conversion, stockpile, and military-transfer complications unrelated to buying land.
A postpaid factory lease makes the bid depend on future performance and requires extensive default and repossession rules.
Both were rejected in favor of paid principal.

Native economic-capacity banking is a plausible alternative, but this pass did not establish its complete current affordability, negative-debit, variable, escrow, refund, and DLC-neutral contracts.
The selected custom reserve keeps the gameplay unit explicit and makes the required native industrial cost and construction benefit testable.
That choice is not proof that its own adapter is already supported.
If the installed-engine spike shows a better fully equivalent native solution, record and accept a design amendment before changing the economic contract.
Do not call a missing adapter implemented or replace it with free reserve.

## Corrections made during parent review

C01 fixed the homeland reconstruction target to a prepublished achievable program worth 50–100 percent of the opening reserve.
The earlier draft scaled the target with the final winning receipt, which could make a higher winning bid unexpectedly impossible to reinvest within the mission.
C02 gave externally impossible reconstruction an explicit interrupted outcome with no success award, extra penalty, or rollback of a completed sale.
C03 made regional bundles require at least two connected states, with no fixed upper state count, so a disabled single-state permission is not bypassed by relabeling a one-state lot as a region.
C04 clarified receipt provenance and priority for the active homeland construction pledge, preventing one construction payment from satisfying several receipts.
C05 moved legacy repository details out of the idea-first territorial specification into this evidence register.
C06 made the seller explicitly ineligible to bid on its own lot and excluded engine test carriers, preventing self-sales from manufacturing a precedent.
C07 fixed published terms from publication, clarified draft-only voluntary withdrawal, and specified the three reserve policy ratios.
C08 limited founding-sale Chaos qualification to the founding milestone and made invalid forced founding attempts preserve the unused publication.
C09 bound an existing subject authorization to its published contract so a changed overlord alone cannot rewrite the bargain.

These are corrections to drafts authored in this response, not changes to previously approved Parts 01–13 or to the user's original brief.
No supplied source was rewritten.
