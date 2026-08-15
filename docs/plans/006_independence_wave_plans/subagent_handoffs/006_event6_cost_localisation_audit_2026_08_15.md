# Event 006 Cost Localisation Audit and Patch Handoff

## Scope

This pass audited Event 006 `custom_cost_text` consumers, patched the shared cost families in `localisation/english/006_independence_wave_decisions_l_english.yml`, and did not change gameplay, constants, effects, triggers, decisions, assets, the central admission system, or event documentation.

## Files changed

- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_cost_localisation_audit_2026_08_15.md`

## Exact surface and changed keys

The following active base families and their `_tooltip` and `_blocked` companions were rewritten as compact amount-plus-texticon rows:

- `independence_wave_cost_administration_light`
- `independence_wave_cost_administration_standard`
- `independence_wave_cost_administration_standard_factory`
- `independence_wave_cost_administration_major`
- `independence_wave_cost_diplomatic_light`
- `independence_wave_cost_diplomatic_standard`
- `independence_wave_cost_diplomatic_standard_factory`
- `independence_wave_cost_diplomatic_standard_factory_standard`
- `independence_wave_cost_patron_balance`
- `independence_wave_cost_security_light`
- `independence_wave_cost_security_light_factory`
- `independence_wave_cost_security_standard`
- `independence_wave_cost_security_standard_factory`
- `independence_wave_cost_security_major`
- `independence_wave_cost_strategic`
- `independence_wave_cost_strategic_major`
- `independence_wave_cost_agx_coastal_conference`
- `independence_wave_cost_corridor`
- `independence_wave_cost_safe_reserve`
- `independence_wave_cost_rescue_aid`
- `independence_wave_cost_border_ultimatum_major`
- `independence_wave_cost_integration_major`
- `independence_wave_cost_breakaway_sponsorship_standard_factory`
- `independence_wave_cost_reclamation_front`

The following active companion keys were also rewritten, while their base keys remain in their owning localisation files:

- `independence_wave_cost_pacific_island_strategic_tooltip`
- `independence_wave_cost_pacific_island_strategic_blocked`

The following retired, zero-consumer keys were removed:

- `independence_wave_cost_formable_proclamation`
- `independence_wave_cost_border_ultimatum`
- `independence_wave_cost_border_ultimatum_tooltip`
- `independence_wave_cost_border_ultimatum_blocked`
- `independence_wave_cost_breakaway_sponsorship`
- `independence_wave_cost_breakaway_sponsorship_tooltip`
- `independence_wave_cost_breakaway_sponsorship_blocked`
- `independence_wave_cost_integration`
- `independence_wave_cost_integration_tooltip`
- `independence_wave_cost_integration_blocked`

No localisation key whose name contains `pre_event`, `pre-event`, `crisis`, or `pressure` remains in the target file. The visible `Revisionist Pressure` category state is active league state, not a retired pre-event key, and was not changed.

## Before and after display

Before this patch, several active cost strings were English sentences beginning with `Commits`, `Requires`, or `Unavailable`, followed by long literal resource lists. Many compact strings also placed the icon before the amount.

After this patch, active shared costs show the amount followed by the matching texticon. Normal values use yellow and blocked values use red. Tooltips reuse their compact base key where no additional requirement must be shown. `independence_wave_cost_patron_balance` retains explicit `Initial` and `Repeat` rows, `independence_wave_cost_reclamation_front_tooltip` retains its three-member and three-owner requirements, and the Pacific strategic tooltip retains its strict `More than` threshold and completion-spend explanation.

## Dynamic localisation added or fixed

No new mechanic or value was invented. Existing script-constant tokens and formatters were preserved. Repeated tooltip text now references the corresponding compact base localisation key with `$key$`, so one dynamic value source controls both displays.

`independence_wave_cost_safe_reserve` now shows the four valid alternative reserve thresholds through their existing constants and icons instead of the vague phrase `safe surplus`.

`independence_wave_cost_selected_formable_commit_tooltip` still calls `[This.GetIndependenceWaveFormableCommitCostText]`. The defined-text block exists in `common/scripted_localisation/006_independence_wave_formable_registry_scripted_localisation.txt`. No broken scripted-localisation reference was found in the assigned file.

## Audit lists

### Missing keys

No active shared cost base in the target file is missing its base, `_tooltip`, or `_blocked` key.

A broader read-only scan of all Event 006 decision files found 34 current `custom_cost_text` base ids with no English base localisation. They are outside this assigned target-file patch:

- COG overlays: `independence_wave_iw_cog_cabinet_cost`, `independence_wave_iw_cog_charter_cost`, `independence_wave_iw_cog_depot_cost`, `independence_wave_iw_cog_force_cost`
- Regional overlays: `independence_wave_iw_region_cabinet_cost`, `independence_wave_iw_region_charter_cost`, `independence_wave_iw_region_depot_cost`, `independence_wave_iw_region_force_cost`
- IW022: `independence_wave_iw022_charter_cost`, `independence_wave_iw022_coastwatch_cost`, `independence_wave_iw022_guard_cost`, `independence_wave_iw022_ledger_cost`, `independence_wave_iw022_security_compact_cost`
- IW025: `independence_wave_iw025_charter_cost`, `independence_wave_iw025_depot_cost`, `independence_wave_iw025_federal_compact_cost`, `independence_wave_iw025_guard_cost`, `independence_wave_iw025_mounted_reserve_cost`
- IW035: `independence_wave_iw035_charter_cost`, `independence_wave_iw035_coastal_watch_cost`, `independence_wave_iw035_depot_cost`, `independence_wave_iw035_federal_compact_cost`, `independence_wave_iw035_guard_cost`
- IW059: `independence_wave_iw059_cabinet_cost`, `independence_wave_iw059_constitutional_cost`, `independence_wave_iw059_depot_cost`, `independence_wave_iw059_officer_cost`
- IW085: `independence_wave_iw085_assembly_cost`, `independence_wave_iw085_cavalry_cost`, `independence_wave_iw085_oasis_cost`, `independence_wave_iw085_regency_cost`
- Udmurtia: `independence_wave_udm_cost_administration_light`, `independence_wave_udm_cost_administration_standard`, `independence_wave_udm_cost_strategic`

Those 34 bases also lack their `_tooltip` and `_blocked` companions. `independence_wave_fer_cost_administration_standard` and `independence_wave_fer_cost_strategic` have base keys but lack both companions. This is a separate package-localisation gap and was not silently expanded into this bounded shared-file patch.

### Duplicate keys

No duplicate key exists in `006_independence_wave_decisions_l_english.yml`.

### Scripted localisation issues

No broken scripted-localisation call was found in the assigned target. The selected-formable cost branches remain mechanically resolved, but their returned prose is still bloated in `localisation/english/006_independence_wave_formable_registry_l_english.yml`.

### Dynamic text opportunities

- Convert the three `independence_wave_formable_commit_cost_*` branch strings in `006_independence_wave_formable_registry_l_english.yml` to the same amount-plus-icon format.
- Convert the base `independence_wave_cost_pacific_island_strategic` in `006_independence_wave_pacific_l_english.yml`. This pass compacted only its target-file tooltip and blocked companions.
- Add the missing package-specific base and companion keys listed above in their owning localisation files.

### Cross-surface mismatches

- The selected-formable dynamic cost base still returns literal prose from `006_independence_wave_formable_registry_l_english.yml`, while its target-file companion remains dynamic.
- The Pacific strategic base remains literal prose in `006_independence_wave_pacific_l_english.yml`, while its target-file tooltip and blocked displays are compact.
- Several current package decisions refer to missing package-local cost families as listed under missing keys.

### File encoding concerns

The target remains UTF-8 with BOM (`EF BB BF`). No encoding concern was found.

### Prose-quality issues and repairs

- Vagueness: `safe surplus` did not identify any qualifying reserve. It now shows all four existing alternatives and thresholds.
- Bloat: long `Commits`, `Requires`, and `Unavailable` sentences became compact icon rows.
- Obvious explanation: boilerplate that narrated the meaning of the cost display was removed.
- Repetition: normal tooltip strings reuse the compact base key instead of repeating the full list.
- Overcomplication: comma-heavy resource sentences were split into short visual rows.
- Style-rule repair: resource-name prose and filler conjunctions were removed from the assigned cost strings. No em dash, semicolon, staged contrast, or implementation-history wording was introduced.

### Sourced quotation preservation

No sourced or attributed quotation appears on the inspected cost surface. No quotation was changed.

## Remaining gameplay-design issue

Several active decisions still charge more than the four spendable cost types allowed by the decisions skill. A localisation-only patch cannot remove or hide those costs without misrepresenting gameplay. The affected shared families are `strategic`, `strategic_major`, `agx_coastal_conference`, `border_ultimatum_major`, `integration_major`, `breakaway_sponsorship_standard_factory`, `reclamation_front`, and the Pacific strategic family. The selected-formable dynamic branches also exceed the budget in some methods. The decision owner must simplify those costs or explicitly revise the design. This handoff does not alter them.

## MCP evidence and blocker

The installed HOI4 MCP exposes focus, event, technology, probability, named scripted-GUI, and map inspection routes. It exposes no ordinary-decision localisation inspector or ordinary-decision renderer. These costs use the vanilla decision interface rather than a named scripted-GUI window, so there is no valid decision-surface MCP artifact URI to record. Source and consumer validation is not presented as equivalent rendered evidence.

## Meaningful validation

- An exact anchored scan of every Event 006 `custom_cost_text` consumer confirmed that every base retained in the target has at least one current consumer and that all four removed families have zero consumers.
- The target-file active shared families have complete base, `_tooltip`, and `_blocked` coverage.
- The target contains no remaining prose-style cost string beginning with `Commits`, `Requires`, or `Unavailable`.
- The existing dynamic script-constant tokens, resource alternatives, requirement distinctions, and selected-formable scripted-localisation call remain present.

## Skipped meaningful validation

No ordinary-decision MCP render was possible because the installed server has no such route. No in-game validation was run because live HOI4 validation belongs to the user.

## Unresolved wording and follow-up

- The selected-formable and Pacific base cost strings need compact rewrites in their owning localisation files.
- The package-local missing cost keys need a separate bounded pass.
- The decision owner must resolve the active five-to-nine-type cost families instead of hiding extra costs in localisation.

No plan addendum was written beyond this required patch handoff. No simplification or fallback was introduced.
