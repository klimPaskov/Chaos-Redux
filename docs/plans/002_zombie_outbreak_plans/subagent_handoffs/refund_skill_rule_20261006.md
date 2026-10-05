# Refund receipt skill maintenance handoff

Disposition: `implemented` for the bounded reusable skill addition.
Acceptance basis: the parent assigned this exact skill and handoff scope on 2026-10-06 to capture the production receipt contract and tested cancellation behavior.
Parent review and commit ownership remain with the parent.

## Changed surfaces and reason

- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`: inserted only `Refundable native political-power credit receipts` immediately before `Paid finite-registry release receipts`.
- `docs/plans/002_zombie_outbreak_plans/subagent_handoffs/refund_skill_rule_20261006.md`: this handoff.

The skill covered financial refunds and finite-registry receipts but lacked the separate sale-sequence receipt contract for refundable native political-power decisions.
The addition captures actual credited output, exact paid quote, matching-index withdrawal, idempotent cancellation cleanup, and completion retaining earned credit.
No new skill was needed because this belongs to decision costs and lifecycle guidance.
Other skills, AGENTS.md, runtime registrations, gameplay, localisation, and balance were left unchanged; no routing update is required.

## Read sources

Read `AGENTS.md`, OpenAI `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md` routing/ownership/handoff sections, and the decision skill's cost, receipt, lifecycle, and production-contract-test guidance.
Read production `black_friday_credit_political_power_purchase_with_receipt` and `black_friday_withdraw_political_power_purchase_with_receipt` in `common/scripted_effects/026_black_friday_effects.txt`, lines 5148-5196, their preceding comments, and legacy helper calls.
Read the receipt API table and `Refundable native Political Power decisions` section in `common/scripted_effects/026_black_friday_simple_cost_api.md`, lines 25-83.
The API file resides beside the production scripted effects, rather than directly under `docs/`.

| Read artifact | SHA-256 at handoff |
| --- | --- |
| `common/scripted_effects/026_black_friday_effects.txt` | `20ba11b134820703fefae9731e1671a9a74d65babf860f4929a33b208fb7c266` |
| `common/scripted_effects/026_black_friday_simple_cost_api.md` | `293b144a4580be55a2a4399d82459e5baf2cf4efef81233a9b007692c2a47d0c` |
| `docs/plans/002_zombie_outbreak_plans/subagent_handoffs/refund_receipt_scenarios_20261005.py` | `7f633586859daad18b4bb9c4d3a6d278fe8d1308b7b3325c21adf98983208cd6` |

## Meaningful validation and limits

Executed `python docs\plans\002_zombie_outbreak_plans\subagent_handoffs\refund_receipt_scenarios_20261005.py`; all five scenario groups passed across the fixture's 25 refundable owners.
Coverage includes same-sale refunds, older/outside-sale purchases preserving a later index, excluded eligibility, duplicate cancellation, successful completion retaining earned credit, generation reset, retained expired-sale index, and rejected settlement refund.
The test executes production receipt APIs and their credit/count/eligibility dependencies plus owners' financial projections, with native primitives and eligibility inputs mocked.
Nonfinancial gameplay, timers, UI, and achievement runtime behavior are outside that test's certification; source contract evidence does not establish native engine execution.
No additional MCP or live-game validation was performed for this prose-only assignment; the parent retains implementation evidence obligations.

The official skill validator passed using `python -X utf8 C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-decisions-missions`.
Its first invocation without `-X utf8` failed when Windows selected cp1252 for the existing UTF-8 skill; rerunning in UTF-8 mode resolved the route without changing encoding.
Reviewed the insertion against the API, confirmed linked paths and heading, and verified it contains no owning-event ID, task-specific filename, or event-specific decision name.

## Isolated insertion for parent commit

The shared skill already contained other agents' uncommitted fractional-quote and finite-registry receipt paragraphs before this worker edited it.
Those bytes were preserved by re-reading immediately before the single byte replacement; the whole current skill diff is not this worker's change.

Exact old anchor:

```markdown
### Paid finite-registry release receipts
```

Exact replacement is the inserted block below followed by that unchanged old anchor:

```markdown
### Refundable native political-power credit receipts

For refundable native political-power decisions using the sale price table, read the [receipt API contract](../../../common/scripted_effects/026_black_friday_simple_cost_api.md#refundable-native-political-power-decisions) and its [production helpers](../../../common/scripted_effects/026_black_friday_effects.txt).
Keep the exact paid quote in an owner normal variable for currency refunds; achievement credit is a separate receipt and must never be inferred from the price or sale activity.

Clear the previous owner receipt before crediting, initialize both `black_friday_political_power_receipt_credited` and `black_friday_political_power_receipt_sale_sequence` temps to zero in the caller chain, then invoke `black_friday_credit_political_power_purchase_with_receipt` once after payment.
Persist a positive credited output as an owner country flag and its sale sequence as an owner normal variable, with separate pairs for decisions whose timers can overlap.

On cancellation, load that flag and saved sequence into the receipt temps and call `black_friday_withdraw_political_power_purchase_with_receipt`; it withdraws only when the positive receipt sequence matches both the global sale sequence and the payer's retained achievement index.
Refund the recorded paid quote once and clear the persistent receipt pair and paid marker, so repeated cancellation cannot refund currency or withdraw another purchase's credit.
Successful completion clears the receipt and paid marker without withdrawing earned credit.
Do not invent a historical credit ledger, reverse an older sale through a newer index, or revoke an awarded achievement.

Verify same-sale refunds, purchases made outside a sale, older-sale refunds after a newer purchase, excluded credit eligibility, repeated cancellation, and successful completion through the actual helper chain.

### Paid finite-registry release receipts
```

## Dispositions and remaining work

- `implemented`: the reusable subsection and this handoff, supported by the source reads and checks above.
- Parent review/commit: parent-owned under the explicit no-index/no-commit delegation constraint.
- Blockers, simplifications, omissions, or unresolved design changes in this bounded skill assignment: none.
- Native runtime confidence remains limited to the source-test evidence; no new engine completion claim is made.
