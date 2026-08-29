# Event 006 Cost Tooltip Completion Handoff

Date: 2026-08-29

Owner: bounded Event 006 localisation audit and patch

Status: COMPLETE IN SOURCE / PRODUCTION RENDER UNAVAILABLE

## Outcome

The remaining Event 006 decision and mission cost text now delegates repeated tooltip amounts to its authoritative base cost key. Blocked cost rows show the same charge in red without the redundant `Unavailable:` or `Unavailable: requires` wrapper. The Reclamation Front requirement no longer hardcodes `3`; both displayed thresholds read `constant:independence_wave_decision_gate.formation_member_minimum`, which is the same constant used by its decision checks.

No gameplay payment amount, trigger, AI weight, route gate, category visibility rule, pre-event behavior, identifier, or fallback changed.

## The stale 95-row indicator

The post-P0 handoff reported 95 cost-key rows containing a numeral without a dynamic constant token. Reproducing that scan before this patch showed that 94 rows were nested aliases such as `$independence_wave_form05_delegation_cost$`; the scan was counting digits in identifiers such as `form05`, `iw043`, and `iw098`, not visible hardcoded amounts. The only player-visible static numerals were the two `3` values in `independence_wave_cost_reclamation_front_tooltip`.

After the patch, a value-aware scan strips nested `$...$` aliases before inspecting displayed text and reports zero visible raw numeric cost values without a `[?constant:...]` token. The old 95-row indicator is therefore superseded rather than evidence for 95 forced rewrites.

## Changed files and keys

- `localisation/english/006_independence_wave_decisions_l_english.yml`: `independence_wave_cost_reclamation_front_tooltip`.
- `localisation/english/006_independence_wave_form01_02_04_l_english.yml`: `independence_wave_form0124_administrative_diplomatic_cost_blocked`.
- `localisation/english/006_independence_wave_form05_l_english.yml`: removed the blocked wrapper from the delegation, shipping, opening, customs, capital, shipping-board, customs-clearinghouse, and first-board-ratification cost families.
- `localisation/english/006_independence_wave_frontier_l_english.yml`: nested the Kuban light and standard administration tooltip keys.
- `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`: nested seven IW-093 and six IW-098 tooltip keys covering their project, settlement, and formable-congress costs.
- `localisation/english/006_independence_wave_karelia_crimea_l_english.yml`: nested the four IW-033 and four IW-041 project-cost tooltip keys.
- `localisation/english/006_independence_wave_komi_l_english.yml`: nested the standard administration tooltip key.
- `localisation/english/006_independence_wave_kosovo_l_english.yml`: nested the light and standard administration tooltip keys.
- `localisation/english/006_independence_wave_minor_overlay_l_english.yml`: nested 28 tooltip keys in the IW-005, IW-022, IW-025, IW-085, Congo-overlay, and regional-overlay families; removed blocked wrappers from 27 rows in the IW-022, IW-025, IW-035, IW-085, Congo-overlay, and regional-overlay families; corrected blocked IW-022, IW-025, and IW-085 values from yellow to red while preserving every token and amount.
- `localisation/english/006_independence_wave_pacific_l_english.yml`: removed blocked wrappers from seven FORM-48 invitation, carrier, and member cost rows.
- `localisation/english/006_independence_wave_ruthenia_l_english.yml`: nested the light and standard administration tooltip keys.
- `localisation/english/006_independence_wave_tatarstan_l_english.yml`: nested the light, standard, and strategic cost tooltip keys.
- `localisation/english/006_independence_wave_udm_l_english.yml`: nested the light and standard administration tooltip keys.

The committed diff contains 36 tooltip aliases, 43 blocked-row wrapper removals, and one dynamic threshold repair. The apparent difference from the earlier 61-row working count reflects concurrent Event 006 changes committed to the shared branch while this bounded pass was in progress; the final figures above are measured against the current commit parent.

## Audit results

### Missing and duplicate keys

- Missing keys for the 191 Event 006 `custom_cost_text` consumers: none. Every consumer has its base, `_tooltip`, and `_blocked` key.
- Duplicate keys across the 37 dedicated Event 006 English localisation files: none among 8,810 parsed keys.

### Scripted localisation and dynamic text

- Broken scripted-localisation reference introduced by this patch: none.
- The expected normal/blocked selector pair in `independence_wave_form0124_administrative_diplomatic_cost` remains `GetIndependenceWaveDiplomaticStandardTransportCostText` / `GetIndependenceWaveDiplomaticStandardTransportCostBlockedText`.
- Dynamic localisation added: `independence_wave_cost_reclamation_front_tooltip` now reads `independence_wave_decision_gate.formation_member_minimum` twice.
- Remaining approved non-alias cost tooltips are `independence_wave_cost_reclamation_front_tooltip`, which adds a real requirement line, and `independence_wave_cost_selected_formable_commit_tooltip`, which is an intentional dynamic formable selector.

### Cross-surface charge comparison

The 43 changed blocked rows retain the same icon, constant, and scripted-selector charge tokens as their base cost rows. The only textual token-name difference is the intentional normal/blocked transport selector pair described above. No mismatched charge was found.

### Encoding

All 37 dedicated Event 006 English localisation files retain UTF-8 BOM. No encoding concern was found in the changed files.

## Prose-quality repairs

- Vagueness: generic statements such as “Commit the displayed...” were removed where the cost row already provides the complete concrete charge.
- Bloat: narrative prefixes such as “Port-ledger commitment:” and “Cyrenaican assembly commitment:” no longer duplicate the adjacent decision title and cost display.
- Obvious explanation: 43 blocked rows no longer announce `Unavailable` before an already-red blocked cost.
- Repetition: 36 tooltip copies now resolve through one base key, preventing visible, blocked, and explanatory variants from drifting.
- Overcomplication: `Unavailable: requires` wrappers and sentence-form equipment enumerations were reduced to the icon-first charge itself.
- Style-rule repair: blocked IW-022, IW-025, and IW-085 amounts now use the established red blocked-state presentation rather than yellow normal-state emphasis.

No sourced or attributed quotation was edited. All pre-existing dynamic tokens and formatting codes in changed charge rows were preserved, except for the intentional addition of the formation-member constant and the intentional yellow-to-red blocked-state color repair.

## Meaningful validation

- Cost-family coverage scan: 191 `custom_cost_text` values, zero missing base/tooltip/blocked keys, zero unapproved descriptive tooltip copies, and zero visible raw numeric cost values without a script-constant token.
- Changed blocked-row charge-token comparison: 43 rows, zero charge mismatches; the normal/blocked transport selector pair was recognized as intentional.
- Dedicated localisation scan: 37 files, 8,810 keys, zero duplicates, zero BOM failures.
- `python .tools/audit_event6_allocator.py`: passed; 149 publishers, 126 automatic/high-chaos selectable packages, and the retired pre-event crisis surface remained absent.
- `python .tools/audit_event6_gui_matrix.py`: passed the semantic source matrix for all five tabs and four static/animated sibling pairs; it does not establish production rendering.
- `python .tools/audit_event6_scenario_matrix.py`: passed all 32 named SCN-008 cells.
- `python .tools/audit_event6_form16.py`: passed the FORM-16 admission, mutation, rollback, and readiness contract.

## Skipped validation and unresolved limits

The required HOI4 MCP Event and GUI inspection/render routes were not callable from this subagent's current tool registry. No Event inspect artifact, production decision render, overflow evidence, or in-game display claim is provided. Source review and static validators are not treated as equivalent visual evidence.

No unresolved wording decision, new mechanic, fallback, simplification, or separate plan handoff remains in this bounded surface.
