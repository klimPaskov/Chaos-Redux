# Event 006 decision-cost localisation audit and patch

Date: 2026-08-26

## Scope

This pass audited the strategic decision-cost strings tied to the current uncommitted war-support trigger removals for Komi, Kosovo, Kuban, Ruthenia, and Udmurtia. It compared the player-facing cost keys with the package triggers, shared diplomatic transport trigger, shared strategic payment effect, and direct decision consumers. It did not edit gameplay, central package admission, event mechanics, assets, specs, the workbook, or unrelated localisation.

## Patch summary

### Changed files

- `localisation/english/006_independence_wave_komi_l_english.yml`
- `localisation/english/006_independence_wave_kosovo_l_english.yml`
- `localisation/english/006_independence_wave_frontier_l_english.yml`
- `localisation/english/006_independence_wave_ruthenia_l_english.yml`
- `localisation/english/006_independence_wave_udm_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_cost_localisation_audit_2026-08-26.md`

### Changed keys

- `independence_wave_komi_cost_strategic`
- `independence_wave_komi_cost_strategic_blocked`
- `independence_wave_komi_cost_strategic_tooltip`
- `independence_wave_kos_cost_strategic`
- `independence_wave_kos_cost_strategic_blocked`
- `independence_wave_kos_cost_strategic_tooltip`
- `independence_wave_kub_cost_strategic`
- `independence_wave_kub_cost_strategic_blocked`
- `independence_wave_kub_cost_strategic_tooltip`
- `independence_wave_rut_cost_strategic`
- `independence_wave_rut_cost_strategic_blocked`
- `independence_wave_rut_cost_strategic_tooltip`
- `independence_wave_udm_cost_strategic`
- `independence_wave_udm_cost_strategic_blocked`
- `independence_wave_udm_cost_strategic_tooltip`

### Behavior and display before and after

Before, each normal and blocked strategic string put the icon before the amount, displayed convoy and train icons without indicating that they are alternatives, and repeated the complete resource list in a prefaced tooltip such as `Strategic compact commitment:`. The underlying trigger and payment effect accept and spend either the convoy amount or the equal train amount, never both.

After, each entry uses amount-first cost presentation. The transport entry is `amount convoy-icon/train-icon`, which exposes the actual alternative payment route without filler prose. Each tooltip now reuses its normal cost key instead of repeating the same list. The normal and blocked colour states, four cost classes, constants, factory commitment, and line breaks are preserved.

No war-support token was removed from these five key families because none remained in their current localisation. The current trigger edits and player-facing strings therefore agree: Komi, Kosovo, Kuban, Ruthenia, and Udmurtia no longer require or display war support for these strategic decisions.

Transport remains correctly displayed. Each package strategic trigger calls `can_pay_independence_wave_diplomatic_standard_cost`, which requires command power and either convoys or trains. `independence_wave_decision_pay_diplomatic_standard` spends the available transport type, and `independence_wave_decision_pay_strategic` also spends stability.

### Dynamic localisation

No new scripted localisation was needed. All existing script-constant tokens were preserved. The tooltip keys now reference their corresponding dynamic normal-cost key, removing duplicated dynamic token lists.

## Audit lists

### Missing keys

None in the five changed strategic cost families. Their direct `custom_cost_text` consumers resolve to the audited normal-cost keys.

### Duplicate keys

None across `localisation/english/006_independence_wave*_l_english.yml` in the focused key scan.

### Scripted localisation issues

None found in the changed keys. They use direct constant substitutions and ordinary localisation-key substitution, not `defined_text` blocks.

### Dynamic text opportunities

Implemented: each repeated strategic tooltip now references its normal dynamic cost key.

No additional dynamic value was invented. The convoy and train thresholds are both 10 in `common/script_constants/006_independence_wave_constants_registry.txt`, so one shared amount before the alternative icons is accurate in the current source.

### Cross-surface mismatch notes

- The five current package triggers at `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:51`, `006_independence_wave_kosovo_package_triggers.txt:41`, `006_independence_wave_kuban_package_triggers.txt:43`, `006_independence_wave_ruthenia_package_triggers.txt:43`, and `006_independence_wave_udm_package_triggers.txt:50` do not contain a war-support gate. Their patched localisation does not display one.
- All five triggers delegate transport to `common/scripted_triggers/006_independence_wave_decision_triggers.txt:249`, which accepts either convoys or trains. The patched localisation retains and clarifies this requirement.
- The shared payment effects at `common/scripted_effects/006_independence_wave_decision_effects.txt:199` and `:350` spend command power, one transport type, and stability. The decision `civilian_factory_use` modifier supplies the fourth displayed commitment.
- Separate, unresolved families still present war support inside a strategic cost string while the shared payment effect does not deduct it: Bashkiria at `localisation/english/006_independence_wave_bashkiria_mari_l_english.yml:140`, the Far Eastern Republic at `006_independence_wave_far_eastern_l_english.yml:82`, Kurdistan at `006_independence_wave_frontier_l_english.yml:78`, Buryatia at `006_independence_wave_siberian_l_english.yml:141`, Khakassia at `:219`, and Sakha at `:354`. Their current package triggers do enforce a minimum war-support requirement, so this is not a phantom trigger requirement. It is a requirement-versus-payment presentation problem: the cost strings imply war support is consumed, but `independence_wave_decision_pay_strategic` does not consume it. I did not alter these unrelated package triggers or decide whether the intended repair is separate requirement text, removal of the gates, or a payment-effect change.

### File encoding concerns

None in the five changed localisation files. Each retained its UTF-8 BOM after patching.

### Prose-quality issues

- Vagueness: the adjacent convoy and train icons did not state whether both resources or either resource was needed. Repaired with an explicit icon separator that matches the OR trigger and payment branch.
- Bloat: the tooltip keys repeated the full dynamic cost expression. Repaired by referencing the normal cost key.
- Obvious explanation: removed generic `Strategic compact commitment:` and `Strategic commitment:` prefixes that added no information beyond the cost surface.
- Repetition: consolidated five duplicated tooltip resource lists into their existing normal-cost keys.
- Overcomplication: moved each entry to one consistent amount-plus-icon sequence while preserving the two existing intentional line breaks.
- Style-rule repair: changed the audited entries from icon-first to the repository skill's required amount-first cost format. No em dashes, semicolons, implementation history, or tuning notes were introduced into player-facing text.

### Sourced-quotation preservation

No sourced or attributed quotation appears in the audited cost surfaces. No quotation text was changed.

## Validation

- Confirmed every changed file still starts with the UTF-8 BOM.
- Parsed all Event 006 English localisation files for duplicate quoted keys; the focused scan found zero duplicates.
- Confirmed the fifteen changed keys contain no war-support token.
- Confirmed the five package strategic triggers call the shared diplomatic standard gate, whose OR block requires either 10 convoys or 10 trains.
- Confirmed the shared payment path deducts the same command-power, transport, and stability values displayed by the changed keys.
- Reviewed the direct decision consumers at `common/decisions/006_independence_wave_balkan_decisions.txt:1805`, `006_independence_wave_frontier_decisions.txt:1086`, and `006_independence_wave_siberian_decisions.txt:2401`, `:2502`, `:2638`, `:2778`, and `:3853`.

## Skipped meaningful validation

- No live or in-game validation was run or claimed; that belongs to the user.
- No HOI4 MCP decision/localisation inspection or rendering artifact is available. The installed `hoi4-agent-tools` surface exposes event-chain, focus, technology, probability, GUI, and map routes, but no read-only decision or localisation coverage/overflow route. Event-chain inspection would not be equivalent evidence for these decision cost strings, so no unrelated MCP artifact was substituted.
- No GUI render was run because these are ordinary decision cost strings, not a scripted GUI surface.

## Unresolved wording decisions

The six separate strategic families listed under cross-surface mismatches need an owner decision about whether war support is a non-consumed requirement or an intended spendable cost. A text-only removal would hide an enforced requirement, while retaining it inside the cost string misstates payment behavior. This pass leaves them unchanged.

## Simplifications and blockers

No fallback or gameplay simplification was introduced. Visual overflow could not be verified through a supported read-only decision/localisation renderer because that MCP route is absent.

## Confirmation

All existing dynamic tokens and formatting codes in the fifteen changed keys were preserved or referenced through the owning normal-cost key. No sourced quotation was altered. No gameplay source, workbook, asset, spec, central admission file, or unrelated localisation file was edited.
