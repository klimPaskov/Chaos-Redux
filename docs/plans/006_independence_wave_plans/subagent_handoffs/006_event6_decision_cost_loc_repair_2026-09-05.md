# Event 006 decision-cost localisation repair

Date: 2026-09-05

Disposition: `implemented` as a bounded localisation-only display repair. No decision cost, payment effect, affordability predicate, AI weight, category gate, package admission, or pre-event surface changed.

## Accepted authority and references

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:9-15` requires an absolutely empty pre-event surface: no category, mission, pressure, cost, queue, history indication, or early request.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_player_surface_origin_gate_2026-09-03.md` records the implemented active-origin gate.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_dm35_patron_balance_affordability_repair_2026-09-03.md` establishes that DM-35 first use pays the diplomatic-standard bundle, while later uses pay the diplomatic-standard bundle plus the administration-light bundle; the combined later command-power threshold is `independence_wave_decision_cost.command_power_patron_balance_after_first`.
- Offline `Decision modding - Hearts of Iron 4 Wiki.md` documents the `custom_cost_text`, `_blocked`, and `_tooltip` contract. Offline `Localisation - Hearts of Iron 4 Wiki.md` and installed vanilla decision precedents confirm texticon-backed custom costs and UTF-8 BOM localisation.
- `chaos-redux-decisions-missions` requires compact amount-plus-texticon rows and no more than four spendable resource types.

## Changed files

- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`
- this handoff

`common/decisions/006_independence_wave_decisions.txt` was inspected but not changed.

## Changed keys and selectors

- Rewired `independence_wave_cost_patron_balance` to `[This.GetIndependenceWavePatronBalanceCostText]`.
- Rewired `independence_wave_cost_patron_balance_blocked` to `[This.GetIndependenceWavePatronBalanceCostBlockedText]`.
- Added `independence_wave_cost_patron_balance_first` and `_blocked`.
- Added `independence_wave_cost_patron_balance_repeat` and `_blocked`.
- Added scripted-localisation selectors `GetIndependenceWavePatronBalanceCostText` and `GetIndependenceWavePatronBalanceCostBlockedText`.
- Preserved `independence_wave_cost_patron_balance_tooltip` as the alias to the active base key.

## Before and after

Before, DM-35 always displayed two labelled lines: `Every use` repeated the standard diplomatic payment and `After the first` added the later surcharge. This was mechanically accurate but visibly dense, repeated information, and forced the player to interpret two prices when only one applied.

After, the cost row resolves only the current payment:

- First use: standard command power plus the current convoy-or-train transport branch. Two spendable resource types are displayed.
- Repeat use: the combined repeat command-power amount, the current convoy-or-train transport branch, and light manpower. Three spendable resource types are displayed.
- The blocked selector follows the same branch and uses the existing red blocked palette.

The later row uses the existing summed command-power constant rather than displaying the standard and light command-power deductions separately. The payment semantics, dynamic transport choice, constant tokens, colours, and texticons remain unchanged.

## Active-consumer trace

The repository-wide Event 006 scan covered 24 `006_independence_wave*.txt` decision files, 699 `custom_cost_text` consumers, and 191 unique custom-cost keys. Every consumer resolves a base, `_blocked`, and `_tooltip` key.

The repaired key has one direct consumer: `common/decisions/006_independence_wave_decisions.txt:1993`, decision `independence_wave_balance_patrons` (DM-35). Its tooltip consumer is the engine-defined `independence_wave_cost_patron_balance_tooltip` alias.

The transport and provisional-capital fragment keys that have no direct `custom_cost_text` caller remain active through existing scripted-localisation selectors. The newly added DM-35 first/repeat fragments are likewise selector-owned, not dead keys.

`independence_wave_cost_security_standard_factory` and its tooltip/blocked variants have no direct or scripted consumer. They retain the old labelled five-type wording as dead legacy localisation. They were deliberately not polished because doing so could misrepresent a five-type gameplay bundle and the user requires obsolete crisis/cost surfaces to remain absent rather than be revived.

## Audit lists

### Missing keys

None. All 699 Event 006 custom-cost consumers have complete normal, blocked, and tooltip triplets. All four added DM-35 fragment keys resolve.

### Duplicate keys

None. The dedicated Event 006 English localisation set contains no duplicate player key after excluding each file's required `l_english` header.

### Scripted-localisation issues

No unresolved result key was found. Each new selector name occurs once, each branch result exists once, and the repeat predicate matches the existing `independence_wave_patron_balance_count > independence_wave_value.minimum` payment branch.

### Dynamic-text opportunities

The active DM-35 opportunity was implemented. No other definite active cost-row problem in `006_independence_wave_decisions_l_english.yml` was safe to change without altering or concealing gameplay costs.

### Cross-surface mismatches

None introduced or found for DM-35. Its first and repeat displays match the current affordability/payment contract. Cost-only strings do not have a catalog wording consumer, so no spreadsheet handoff is required.

### File encoding concerns

None. `006_independence_wave_decisions_l_english.yml` retains UTF-8 BOM (`EF BB BF`), its `l_english:` header, unindented keys, and unversioned key syntax.

### Prose-quality findings and repairs

- Vagueness: no vague resource label was introduced; every charge remains amount plus its matching texticon.
- Bloat: removed the always-visible explanation of both payment stages.
- Obvious explanation: removed `Every use` and `After the first`; branch selection now communicates which price applies.
- Repetition: the standard diplomatic bundle is shown once per current use rather than repeated across two lines.
- Overcomplication: replaced the staged prose ledger with one state-aware row of two or three resource types.
- Style-rule repair: the active row is compact and label-free, with no filler conjunctions, implementation language, em dash, or sentence semicolon.

### Sourced-quotation preservation

No sourced or attributed quotation occurs in the inspected cost surface. No quotation-bearing localisation was changed. All pre-existing dynamic tokens and formatting codes in the repaired surface were preserved or replaced by semantically equivalent dynamic selectors.

## Meaningful validation

- `python -B .tools/audit_event6_allocator.py --strict` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, the exact `3 / 4 / 5 / 7 / 10` ladder, and `pre-event crisis surface: retired; no category, mission, cost, or queue`.
- A focused source scan found 699 Event 006 custom-cost consumers, 191 unique keys, zero missing cost triplet keys, zero duplicate Event 006 player keys, one DM-35 consumer, and zero callers for `independence_wave_cost_security_standard_factory`.
- The two new selector names each occur once, all four result keys resolve, and the localisation BOM remains intact.

## Skipped meaningful validation and exact blocker

The installed HOI4 MCP package exposes no read-only decision-list or decision-cost inspector/render route. Therefore the DM-35 decision row could not receive a production visual overflow/clipping render, and source/key validation is not treated as equivalent visual evidence. The event, focus, technology, GUI, probability, and map routes do not render the ordinary decision-list custom-cost consumer and were not used as substitutes.

Live-game display remains user-owned and was not attempted.

## Unresolved wording decisions

- The dead `independence_wave_cost_security_standard_factory` five-type legacy family remains intentionally untouched and unreferenced.
- No unresolved wording remains on the active DM-35 cost row.

## Simplifications, omissions, and blockers

No gameplay charge, cost type, transport alternative, dynamic token, route, or pre-event gate was simplified or omitted. No fallback was used. Visual decision-row proof remains blocked only by the absent MCP decision renderer described above.
