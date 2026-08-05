# Event 006 Iberian Localisation Audit Handoff

## Scope

Audited the current NAV and GLC Iberian package localisation against `common/decisions/006_independence_wave_iberian_decisions.txt`, `common/ideas/006_independence_wave_iberian_ideas.txt`, `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`, and `common/ai_strategy/006_independence_wave_iberian.txt`.

No gameplay, AI, scripted effect, idea, decision, or asset file was edited.

## Changed files

- `localisation/english/006_independence_wave_iberian_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/iberian_localisation_audit_current.md`

## Key coverage audit

- Missing before patch: `independence_wave_nav_iberian_category`, `independence_wave_nav_iberian_category_desc`, `independence_wave_glc_iberian_category`, and `independence_wave_glc_iberian_category_desc`.
- Missing after patch: none among the 73 localisation keys referenced by the two decision categories, their decisions, their custom costs and effect tooltips, and the 14 Iberian ideas.
- Duplicate keys: none in the assigned file and none among the referenced key set across `localisation/english/`.
- AI strategy localisation: no player-facing localisation keys are consumed by the eight AI strategy blocks. Their identifiers remain internal.

## Changed keys

Added:

- `independence_wave_nav_iberian_category`
- `independence_wave_nav_iberian_category_desc`
- `independence_wave_glc_iberian_category`
- `independence_wave_glc_iberian_category_desc`

Rewritten for requirement or consequence clarity:

- `independence_wave_nav_hold_fueros_together_desc`
- `independence_wave_glc_hold_council_together_desc`
- `independence_wave_nav_settle_former_host_ledgers`
- `independence_wave_nav_settle_former_host_ledgers_desc`
- `independence_wave_glc_settle_former_host_ledgers`
- `independence_wave_glc_settle_former_host_ledgers_desc`
- `independence_wave_nav_depots_effect_tt`
- `independence_wave_nav_factory_guards_effect_tt`
- `independence_wave_nav_assembly_effect_tt`
- `independence_wave_nav_host_ledgers_effect_tt`
- `independence_wave_nav_route_effect_tt`
- `independence_wave_nav_patron_route_effect_tt`
- `independence_wave_nav_network_effect_tt`
- `independence_wave_glc_depots_effect_tt`
- `independence_wave_glc_coastal_guards_effect_tt`
- `independence_wave_glc_council_effect_tt`
- `independence_wave_glc_host_ledgers_effect_tt`
- `independence_wave_glc_route_effect_tt`
- `independence_wave_glc_patron_route_effect_tt`
- `independence_wave_glc_network_effect_tt`
- `independence_wave_iberian_project_failure_effect_tt`
- `glc_atlantic_compact_desc`

## Dynamic localisation added

- The NAV category now displays current `independence_wave_nav_fueros_legitimacy` and `independence_wave_nav_industrial_capacity` values as integers.
- The GLC category now displays current `independence_wave_glc_council_legitimacy` and `independence_wave_glc_port_capacity` values as integers.
- Both former-host decisions and their completion tooltips now name `independence_wave_former_host` directly.
- Brackets, colour markers, and integer formatters are balanced in the final file.

## Display before and after

Before the patch, both categories could display raw category identifiers because their category name and description keys were absent. The founding mission descriptions did not state the two required measures or the capital-control failure condition. Several completion tooltips said only that a compact or ledger improved, and the former host remained unnamed.

After the patch, each category has an in-world name, a compact description, current live values, and the exact current stability threshold. The founding missions identify both success measures and the capital-control condition. Project tooltips name the affected measures and amounts, former-host text identifies the actual country, and network text names the systems it advances.

## Cross-surface consistency

- Depot, guard, assembly or council, route, patron, host, network, and failure wording was checked against the actual package effect calls.
- The displayed NAV and GLC compact gains match `independence_wave_iberian_pressure.minor_gain`, `standard_gain`, and `major_gain` in the current constants file.
- The displayed stability threshold of 60 matches `independence_wave_iberian_pressure.stable`.
- Idea names and descriptions cover all 14 idea identifiers in `common/ideas/006_independence_wave_iberian_ideas.txt`.
- No cross-surface contradiction remains in the assigned localisation set.

## Scripted localisation issues

No broken scripted localisation call was found. The new former-host scope tokens point to the country-scope variable assigned from `independence_wave_setup_former_host`, and the decisions are visible only while a living former host exists.

## Raw trigger-text risk

The decision `available` blocks still contain raw capital-control, active-project, stability, founding-settlement, and former-host conditions. The new category and mission text explains the founding stability and capital conditions, but localisation alone cannot suppress raw trigger expansion on every decision. A decision-owner follow-up should wrap those conditions in custom override tooltips if the current decision UI exposes the script-generated lines.

## Encoding

The localisation file remains UTF-8 with BOM. No replacement characters or versioned `:0` keys were found.

## Prose-quality repairs

- Vagueness: replaced `improves`, `changes ledgers`, and `clearer settlement` with named values and concrete institutional or diplomatic effects.
- Bloat: no widespread bloat was present. The revised tooltips lead with the gameplay consequence and retain only context that distinguishes the route.
- Obvious explanation: removed implementation-facing wording about a route being locked and an idea being installed.
- Repetition: retained parallel NAV and GLC structures because their distinct value names and regional institutions help players compare the packages. Repetitive generic ledger phrases were removed.
- Overcomplication: replaced Galicia's `one political conversation` phrasing with the two measurable requirements and the capital-control condition.
- Style-rule repair: removed the only sentence semicolon. No em dash, staged contrast, working label, prompt fragment, or staccato chain remains in the assigned file.

## Sourced quotations

No sourced or attributed quotation appears on the audited surfaces. No quotation text was changed.

## Meaningful validation

- Rebuilt a 73-key reference set from the current decision and idea sources and confirmed that every key resolves after the patch.
- Confirmed that none of those referenced keys is duplicated across the English localisation directory.
- Compared every rewritten numeric effect tooltip with the current Iberian package effects and constants.
- Confirmed balanced dynamic brackets and colour markers in the patched file.

## Skipped validation

No rendered decision-category view was available, so category line wrapping and tooltip width were not visually inspected.

## Remaining uncertainty

The stability threshold is shown as `60` because the engine-facing constant is not exposed as a localisation value. If `independence_wave_iberian_pressure.stable` changes, both category descriptions and founding mission descriptions must be updated with it.

The decision-category layout was not rendered, so it remains uncertain whether the new three-line live-value summaries need width or spacing adjustments.

## Simplifications and blockers

No localisation simplification or blocker remains within the assigned NAV and GLC scope. No broader mechanic plan was required.
