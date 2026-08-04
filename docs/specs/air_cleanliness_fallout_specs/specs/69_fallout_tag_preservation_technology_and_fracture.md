# Fallout tag preservation, regression, and fracture contract

## Status

The preservation, technology-regression, and thirty-tag fracture contract is implemented as a static core surface. It preserves every live tag, regresses the reviewed technology families, and keeps the universal Fallout focus and decision package as the post-map-return consumer. Dynamic-country readback, random materialization, multiplayer synchronization, and live HOI4 behavior remain runtime gates outside this tranche.

Fallout preserves every country tag that exists when the request snapshot is captured. Country ownership, government, technology, capital, state category, buildings, population, and borders may change. A tag is not removed merely because it loses every original state. The map-return gate requires `fallout_pretransition_tags_are_preserved`, which checks every frozen country scope still resolves to a live tag in the same transition generation.

The diplomacy phase white-peaces every war, removes civil-war targets, recalls volunteers, ends exile and subjects, dismantles factions, and records `fallout_transition_wars_stopped_complete`. The receipt is generation-bound and is required by the old-world diplomacy validator and map-return gate. Later post-Fallout wars are allowed after the blackout is complete.

Every live country receives `fallout_regress_country_technology` before successor allocation. The effect unresearches the reviewed advanced air, armour, artillery, industry, electronics, naval, nuclear, Chaos Redux project, and CBRN technology families. It then restores a four-technology survival floor of basic infantry weapons, the first infantry weapons model, basic machine tools, and first construction. Majors and `is_special_chaos_country` tags receive the additional emergency support, engineer, recon, radio, transport, artillery, and motorised floor. No Independence Wave focus tree is loaded by this effect.

The technology rows are generation-bound. `fallout_technology_regression_complete` and `fallout_all_live_country_technology_rows_are_current` are required before map return. The offline wiki confirms that `set_technology = { token = 0 }` unresearches a researchable technology. Mutually exclusive technologies and technologies that unlock database objects can resist unresearching, so those surfaces remain part of the live consumer audit.

The fractured border contract is Fallout-owned and uses thirty reserved Independence Wave country definitions as dynamic templates only. A live conflict ledger classifies each reserved tag as blocked when the tag already exists and safe when it is available. The release-gated fracture selects a random war-scarred multi-state source, selects a random non-capital severe state, and copies one safe template. The output receives neutral emergency politics, the Fallout package receipts, the technology regression, one state, one core, and a capital. It never loads the Independence Wave focus tree. The random selection is performed after blackout work and is generation/date-seeded by the engine.

`fallout_fracture_release_enabled` is intentionally unset in ordinary saves. Exact dynamic-country availability, random border variation, ownership readback, successor ledger interaction, and no-delete preservation require live engine proof. If the gate is enabled without a safe template or eligible source, the transition records `fracture_conflict_ledger_incomplete` and remains blacked out rather than substituting a static border.

## Proof surfaces

- `common/scripted_effects/fallout_consolidated_effects.txt` owns the war-stop receipt, tag-preservation receipt, technology phase, and map-return ordering.
- `common/scripted_effects/fallout_consolidated_effects.txt` owns the reviewed technology regression and emergency floor.
- `common/scripted_effects/fallout_consolidated_effects.txt` owns the conflict ledger, random source and state selection, and reserved-template dynamic output.
- `common/scripted_triggers/fallout_consolidated_triggers.txt` owns the no-delete, war-stop, technology, and map-return postconditions.
- `common/scripted_triggers/fallout_consolidated_triggers.txt` owns source eligibility and the release gate.
- `common/script_constants/fallout_consolidated_constants.txt` owns the regression schema, fracture pool tuning, and transition error codes.

The exact 10,154-province native sweep and seven-day barrier, host-authoritative blackout, dynamic tag readback, and mutating random border result have static source contracts but remain runtime proof gates. Hearts of Iron IV was not run.
