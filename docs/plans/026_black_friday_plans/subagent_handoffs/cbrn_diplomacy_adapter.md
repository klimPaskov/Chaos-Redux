# Event 26 CBRN diplomacy adapter handoff

## Disposition

Status: REJECTED and BLOCKED.

The CBRN diplomacy Black Friday adapter is not installed. The predecessor's incomplete CBRN additions were removed from the assigned owner files so the owner remains coherent and ordinary behavior is unchanged.

The exact blocker is the hard decision/mission cost budget in `.agents/skills/chaos-redux-decisions-missions/SKILL.md:204-210`: `cbrn_sponsor_decontamination_mission` is one logical action that consumes six independently payable stockpile types and also commits civilian factories for the mission duration. Making it compliant would require changing the ordinary mechanic, hiding spendable values, or adding a broader transaction/commitment design outside this tranche. None is safe to assume.

## Owned files and cleanup

The only gameplay/localisation files inspected for this tranche were:

- `common/decisions/cbrn_diplomacy_decisions.txt`
- `common/script_constants/cbrn_diplomacy_constants.txt`
- `common/scripted_effects/cbrn_diplomacy_effects.txt`
- `common/scripted_triggers/cbrn_diplomacy_triggers.txt`
- `localisation/english/cbrn_diplomacy_l_english.yml`

The predecessor Black Friday changes were removed from those files. The uncommitted diff for each of them is empty after cleanup. The shared Event 26 files, universal-cost framework files, allowlists, inventories, registry, catalog, and other owners were not edited.

The handoff itself is the only new file from this closeout.

## Exact reachable rows

The CBRN category contains three reachable voluntary actions and one response mission.

| Logical action | Custom-cost pair | Ordinary payment callsites | Ordinary components | Primary family | Disposition |
| --- | --- | --- | --- | --- | --- |
| `cbrn_demand_inspections` | `common/decisions/cbrn_diplomacy_decisions.txt:37` and `:40` | `:45` to `cbrn_diplomacy_send_inspection_demand`; `common/scripted_effects/cbrn_diplomacy_effects.txt:252-261` | 2: CBRN instrument stock, then `support_equipment_1` | Diplomatic | Rejected as part of the all-row tranche; individually adapterable only after the shared owner contract is resolved |
| `cbrn_share_forensic_evidence` | `common/decisions/cbrn_diplomacy_decisions.txt:113` and `:116` | `:120-123`; `common/scripted_effects/cbrn_diplomacy_effects.txt:311-320` | 2: CBRN instrument stock, then `support_equipment_1`; plus a 1-civilian-factory active commitment | Diplomatic | Rejected as part of the all-row tranche; delayed refund/settlement would require a valid owner contract |
| `cbrn_sponsor_decontamination_mission` | `common/decisions/cbrn_diplomacy_decisions.txt:212` and `:215` | `:219-220`; `common/scripted_effects/cbrn_diplomacy_effects.txt:1183-1214` | 6: gas masks, decontamination equipment, CBRN instruments, `support_equipment_1`, `motorized_equipment_1`, and `convoy_1`; plus a 2-civilian-factory active commitment | Diplomatic | Exact blocker; cannot be accepted under the four-spendable-type cap without changing ordinary gameplay or hiding costs |
| `cbrn_answer_inspection_demand_mission` | No custom-cost pair | No purchase/commitment payment | No voluntary cost | N/A | Not a qualifying purchase; preserved |

The ordinary decision cost values are centralized in `common/script_constants/cbrn_diplomacy_constants.txt:cbrn_diplomacy_cost`. The ordinary factory commitments are file-scoped in `common/decisions/cbrn_diplomacy_decisions.txt:3-4`.

## Price examples if a future adapter is approved

All integer equipment, train, and convoy quanta are 1 and use deterministic upward rounding.

- Inspections: ordinary 10 instruments plus 10 support becomes 5 plus 5 at the 50 percent sale ratio, or 3 plus 3 at the 75 percent ratio.
- Forensic publication: ordinary 20 instruments plus 15 support becomes 10 plus 8 at 50 percent, or 5 plus 4 at 75 percent. The one-factory mission commitment remains a live commitment and is not discounted by the rejected code.
- Decontamination: ordinary 100 masks, 60 decontamination equipment, 30 instruments, 40 support, 25 motorized, and 10 convoys becomes 50, 30, 15, 20, 13, and 5 at 50 percent, or 25, 15, 8, 10, 7, and 3 at 75 percent. The two-factory mission commitment has no safe owner-side quote/payment/refund route in the current write set.

These are arithmetic acceptance examples only. No sale price is displayed or paid by the remaining owner code.

## Lifecycle, AI, and preservation notes

The ordinary inspection action pays immediately and then opens the target country's response mission.

The ordinary forensic and decontamination actions consume their ordinary material packages when started, retain their existing target and route gates, and preserve their existing cancellation, completion, cooldown, and factory-commitment behavior.

The rejected predecessor attempted delayed refundable receipts for forensic publication and decontamination, but those additions are no longer present. Therefore there is currently no CBRN Black Friday receipt, settlement, refund, or achievement confirmation/retraction path. A future accepted adapter must store actual paid values payer-scoped, refund each component once on cancellation, retract pending achievement credit on refund, and confirm only after irreversible completion.

AI formulas were not changed. The existing `ai_will_do` blocks remain at `common/decisions/cbrn_diplomacy_decisions.txt:48-62`, `:163-185`, and `:252-271`. Existing target, route, technology, state-control, reserve, cooldown, and active-mission checks remain in the ordinary scripted triggers and decisions. No discounted-affordability bridge is installed, so no claim is made that CBRN AI can evaluate a sale price.

## Validation performed

- Read-only source audit found exactly three paired `custom_cost_trigger`/`custom_cost_text` rows in the CBRN decision category and no unmatched CBRN cost-text row.
- Read-only callsite audit found the ordinary payment path for each qualifying row and no remaining `black_friday` or `universal_cost` reference in the five cleaned owner/localisation files.
- The cleaned owner files have no uncommitted gameplay diff; unrelated worktree changes were preserved.
- The required offline wiki, Vanilla documentation, and Vanilla decision precedents were consulted before the attempted closeout.
- The required `chaosx_ai_probability_auditor` route was started but stopped for closeout before analysis; its reported blocker was `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`, so no probability artifact, scenario hash, or comparison is claimed.
- The required `chaosx_decision_mission_auditor` route was also stopped for closeout before analysis; no subagent audit or live proof is claimed.
- No live HOI4 proof is claimed. No GUI rewrite was attempted, and no CBRN-owned dedicated scripted GUI exists in this tranche.

## Remaining blockers

1. Redesign or explicitly approve a four-type representation for decontamination without hiding or silently dropping its six ordinary physical payments.
2. Define an owner-side factory-commitment strategy that can quote, preserve, and refund the exact mission commitment without editing the shared framework or creating duplicate action variants.
3. After the design blocker is resolved, re-run the required baseline and comparison probability audit if any CBRN AI affordability or weight logic changes.
4. Re-open the tranche only with an approved design that preserves one logical action, truthful icon-first display, ordinary target/route/cooldown/reserve rules, payer-scoped receipts, exact refund-once behavior, and one diplomatic achievement family.

This tranche must remain blocked.
