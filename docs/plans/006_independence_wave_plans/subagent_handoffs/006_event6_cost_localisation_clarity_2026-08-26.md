# Event 006 decision cost localisation clarity handoff

Date: 2026-08-26

## Scope and authority

This bounded pass audited active Event 006 custom decision-cost consumers in `common/decisions/006_independence_wave*.txt` and their English localisation in `localisation/english/006_independence_wave*.yml`.

The controlling acceptance requirement is that Event 006 exposes no crisis, pressure, category, mission, cost, queue, history row, or other indication before the public Event 006 report fires.

The pass followed `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, the offline Paradox Localisation, Decision modding, Effects, Triggers, Data structures, Modifiers, Scopes, On actions, Event modding, Idea modding, and AI modding pages, vanilla localisation and effect documentation, and vanilla `custom_cost_text` precedents.

## Audit results

### Missing keys

None.

The current 690 `custom_cost_text` consumers use 190 unique localisation keys, and every key resolves in the active Event 006 English localisation set.

### Duplicate keys

None found among the Event 006 English localisation files in the focused assertion.

### Scripted localisation issues

None found in the changed cost path.

`GetIndependenceWaveProvisionalCapitalCostText` and `GetIndependenceWaveProvisionalCapitalCostBlockedText` still resolve the supplied or isolated force-tier variants. Their dynamic selectors, branch triggers, localisation targets, constants, and fallback branches were not changed.

### Dynamic text opportunities

No new selector was needed.

The provisional-capital cost already selects the current force-tier and supply-state bundle dynamically. The patron-balance cost must show both the first-use and later-use bundles because the same repeatable decision changes payment after the first completion. The labels were shortened without hiding either bundle.

### Cross-surface mismatch and pre-event visibility

No pre-event localisation leak was found.

All 87 Event 006 category definitions in `common/decisions/categories/006_independence_wave_categories.txt` have an explicit `visible` block and an Event 006 state, package, setup, invitation, progression, or formable gate. The shared founding, government, security, host, evolution, and later-stage categories are gated by `is_independence_wave_active_country` or a stricter post-release trigger. Package categories use package identity and setup gates. Therefore their crisis, pressure, category, mission, and cost text is not exposed before Event 006 creates or activates the relevant country state.

The Event Chain Viewer trace succeeded only as partial evidence. It did not expose decision UI rendering or cost overflow, so source review is not treated as visual acceptance.

### File encoding concerns

None in the changed files. Both changed YAML files retain UTF-8 BOM and the `l_english:` header.

### Prose-quality issues

- Vagueness: `Initial` and `Repeat` described implementation phases less directly than `First` and `Later` for the repeatable patron-balance decision.
- Bloat: the provisional-capital cost repeated `Opening commitment` even though the decision cost field already provides that context. Six FORM-03 descriptions repeated resource commitments already displayed by their custom cost line.
- Obvious explanation: removed the provisional-capital cost label and cost-list sentences that merely narrated the adjacent cost display.
- Repetition: FORM-03 descriptions no longer duplicate civilian-factory, train, convoy, command, manpower, stability, or League Reserve entries shown by their cost keys.
- Overcomplication: the FORM-03 descriptions now lead with the project, duration, cancellation rule, threshold, or consequence instead of mixing those facts with a second prose rendering of the cost bundle.
- Style-rule repair: no em dash, semicolon sentence, implementation-history wording, staccato chain, or staged contrast was introduced.

### Sourced quotations

No sourced or attributed quotation appears in the changed decision-cost surfaces. No quote-bearing Event 006 localisation was changed.

## Patch

### Changed files

- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `localisation/english/006_independence_wave_form03_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_cost_localisation_clarity_2026-08-26.md`

### Changed keys

- `independence_wave_cost_patron_balance`
- `independence_wave_cost_patron_balance_blocked`
- `independence_wave_cost_provisional_capital`
- `independence_wave_cost_provisional_capital_blocked`
- `independence_wave_form03_convene_language_convention_desc`
- `independence_wave_form03_reconnect_sambre_meuse_corridor_desc`
- `independence_wave_form03_coordinate_frisian_waterway_standards_desc`
- `independence_wave_form03_request_development_compact_technical_mission_desc`
- `independence_wave_form03_reopen_charter_talks_desc`
- `independence_wave_form03_repair_industrial_compact_desc`

### Dynamic localisation added or fixed

None.

All existing dynamic selectors, constants, values, texticons, colour codes, and formatting tokens were preserved.

### Display before and after

- Patron balance previously used `Initial` and `Repeat`. It now uses the shorter, direct labels `First` and `Later`, while preserving both exact dynamic cost bundles and the red blocked variants.
- Provisional-capital costs previously began with `Opening commitment:`. They now display only the dynamically selected amount-icon bundle. The cost and blocked selectors are unchanged.
- Six FORM-03 descriptions previously repeated some or all of the exact resource bundle shown by `custom_cost_text`. They now state the project, duration, consequence, cancellation rule, threshold, or refund rule. No cost was removed from the actual cost display or payment logic.

### Prose before and after summary

- Vagueness: implementation-like phase labels became direct use-order labels.
- Bloat: removed one redundant cost prefix and six repeated prose cost disclosures.
- Obvious explanation: removed text that only announced that a cost field was an opening commitment.
- Repetition: one authoritative icon-first custom cost line now carries each FORM-03 spend bundle.
- Overcomplication: project descriptions separate action and consequences from payment presentation.
- Style repair: active, concrete project wording replaced administrative cost narration without changing route identity.

Dynamic tokens and sourced quotations were preserved without exception.

## Validation

### Meaningful checks run

- Enumerated all 690 active Event 006 `custom_cost_text` consumers and confirmed that all 190 unique keys resolve.
- Rechecked Event 006 localisation for duplicate keys after the patch and found none.
- Confirmed the two edited cost keys and all ten FORM-03 cost keys remain referenced by their intended decision consumers.
- Confirmed no FORM-03 description still contains an exact `independence_wave_decision_cost.*` resource disclosure after the patch.
- Parsed all 87 Event 006 decision category definitions and confirmed each has both an explicit visibility block and an Event 006 state or package gate.
- Confirmed both edited localisation files retain UTF-8 BOM.
- Ran the read-only Event Chain Viewer trace for `chaosx.nr6.1`. Result: `EVENT_INSPECTED_PARTIAL`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4304b28cf86ef175de906d32778e9e2fc5334fe925028efa244a1a47cf5f8250/1e3b3fd7f0b02473519901234d82e0c24f63226855f82a0af98da186804fa531/event-trace-744cd12bca3e.json`.

### Skipped meaningful validation

- The installed HOI4 MCP package exposes event, focus, technology, probability, GUI, and map routes, but no dedicated decision inspector or decision-cost renderer. No artifact-backed cost overflow or visual-fit check was available. The Event Chain Viewer artifact does not substitute for decision UI rendering.
- No scripted GUI was changed, so no GUI rewrite was appropriate.
- Hearts of Iron IV was not launched, as required by repository policy.

## Remaining risks and unresolved wording decisions

- Some older active Event 006 cost keys place icons before amounts rather than using the current amount-before-icon project standard. They are compact and mechanically legible, but a repository-wide order normalization is broader than this prose-bloat pass and should be handled as a separate mechanical localisation task.
- Alternative provisional-capital transport costs retain `or` because the actual isolated-capital payment accepts trains or motorized equipment. Removing it would conceal the alternative payment rule.
- Decision cost overflow and wrapping remain unverified because no read-only decision-cost render route is installed.

No gameplay costs, triggers, effects, AI weights, admission logic, package routes, category visibility, or sourced quotation text changed. No simplification or fallback was introduced.
