# IW-050 Komi localisation recovery handoff

Date: 2026-08-14

Scope: Recover the bounded English localisation package for the IW-050 Komi decisions, category, national spirits, party names, public compact ledgers, and decision effect tooltips.

## Files changed

- `localisation/english/006_independence_wave_komi_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_localisation_recovery_2026_08_14.md`

No central gameplay, localisation, GUI, GFX, focus, event, scripted localisation, or asset file was edited.

## Key coverage

The new localisation file contains 59 package-owned keys.

### Party names and long names

- `KOM_independence_wave_constitutional_party`
- `KOM_independence_wave_constitutional_party_long`
- `KOM_independence_wave_socialist_party`
- `KOM_independence_wave_socialist_party_long`
- `KOM_independence_wave_taiga_party`
- `KOM_independence_wave_taiga_party_long`
- `KOM_independence_wave_emergency_party`
- `KOM_independence_wave_emergency_party_long`

### National spirit names and descriptions

- `komi_fragmented_taiga_mandate` and `komi_fragmented_taiga_mandate_desc`
- `komi_northern_republic_compact` and `komi_northern_republic_compact_desc`
- `komi_taiga_congress_charter` and `komi_taiga_congress_charter_desc`
- `komi_rail_councils` and `komi_rail_councils_desc`
- `komi_community_register` and `komi_community_register_desc`
- `komi_taiga_land_compact` and `komi_taiga_land_compact_desc`
- `komi_taiga_emergency_command` and `komi_taiga_emergency_command_desc`

### Category and public ledger labels

- `independence_wave_komi_northern_compact_category`
- `independence_wave_komi_northern_compact_category_desc`
- `independence_wave_komi_congress_cohesion`
- `independence_wave_komi_taiga_readiness`

The category description displays both live ledger values, their package-local maximum, the stable threshold, the route-government requirement, and the Syktyvkar security requirement. The standalone ledger labels follow the canonical variable identifiers and add no stale alias.

### Decision and mission names and descriptions

- `independence_wave_komi_hold_northern_council` and `independence_wave_komi_hold_northern_council_desc`
- `independence_wave_komi_secure_taiga_depots` and `independence_wave_komi_secure_taiga_depots_desc`
- `independence_wave_komi_integrate_rail_guards` and `independence_wave_komi_integrate_rail_guards_desc`
- `independence_wave_komi_register_komi_communities` and `independence_wave_komi_register_komi_communities_desc`
- `independence_wave_komi_settle_former_host_ledgers` and `independence_wave_komi_settle_former_host_ledgers_desc`
- `independence_wave_komi_ratify_constitutional_autonomy` and `independence_wave_komi_ratify_constitutional_autonomy_desc`
- `independence_wave_komi_adopt_taiga_land_compact` and `independence_wave_komi_adopt_taiga_land_compact_desc`
- `independence_wave_komi_convene_rail_councils` and `independence_wave_komi_convene_rail_councils_desc`
- `independence_wave_komi_establish_taiga_emergency_command` and `independence_wave_komi_establish_taiga_emergency_command_desc`
- `independence_wave_komi_codify_durable_sovereignty` and `independence_wave_komi_codify_durable_sovereignty_desc`
- `independence_wave_komi_open_northern_ural_corridor` and `independence_wave_komi_open_northern_ural_corridor_desc`

### Effect tooltips

- `independence_wave_komi_project_failure_effect_tt`
- `independence_wave_komi_depots_effect_tt`
- `independence_wave_komi_guards_effect_tt`
- `independence_wave_komi_communities_effect_tt`
- `independence_wave_komi_host_ledgers_effect_tt`
- `independence_wave_komi_constitutional_effect_tt`
- `independence_wave_komi_taiga_effect_tt`
- `independence_wave_komi_rail_councils_effect_tt`
- `independence_wave_komi_emergency_effect_tt`
- `independence_wave_komi_sovereignty_effect_tt`
- `independence_wave_komi_corridor_effect_tt`

## Before and after

Before this patch, all 59 canonical Komi strings were absent from a package-local English localisation file, so decisions, ideas, party names, the category, and effect tooltips could display raw keys.

After this patch, every mapped consumer in the four assigned source files resolves to package-local English text. The founding mission names Syktyvkar and prints the live 420-day tuning value, the category prints both ledgers and the stable threshold, and effect tooltips print the package-local ledger changes through script constants.

No focus-localisation aliases were added. The five shared focus anchors call Komi helpers but do not consume new Komi localisation keys.

## Dynamic localisation

The category and mission descriptions use the existing Komi variables and script constants for current ledger values, maximum, stable threshold, and founding-crisis duration.

The eleven effect tooltips use the existing Komi pressure constants for gains and losses. No scripted localisation block or new gameplay value was added.

## Prose-quality changes

- Vagueness: Missing raw keys were replaced with concrete references to Syktyvkar, rail depots, forest districts, mine workers, community registers, and the Pechora and Northern Ural routes.
- Bloat: Decision descriptions state the public action or requirement in one or two direct sentences without implementation history.
- Obvious explanation: Tooltips do not repeat button titles. They identify the ledger movement, government change, institutional result, or network consequence.
- Repetition: Route descriptions distinguish elected congress rule, the land compact, workers' councils, and emergency command instead of reusing a generic state-building paragraph.
- Overcomplication: Long administrative phrases were reduced to direct subjects and active verbs. Requirements appear before atmosphere.
- Style-rule repair: The text contains no em dash, sentence semicolon, prompt fragment, tuning note, update-history phrasing, or hidden-mechanic explanation.

## Audit findings after patch

- Missing key list: none among the 59 mapped package keys.
- Duplicate key list: none within the file and none for the 59 owned keys across `localisation/english`.
- Scripted localisation issues: none. This package uses supported inline variable and script-constant substitutions and introduces no scripted localisation references.
- Dynamic text opportunities: completed for the live ledgers, thresholds, duration, and tooltip deltas. Party, idea, and action names are correctly static.
- Cross-surface mismatches: none found between the assigned decisions, category, ideas, effects, and the new localisation. No focus alias was invented for helper-only calls.
- File encoding concerns: resolved. The file begins with the UTF-8 BOM bytes `EF-BB-BF`.
- Prose-quality issues: no remaining in-scope vagueness, bloat, obvious explanation, repetition, overcomplication, or listed writing-style violation was found.

## Sourced quotations and token preservation

No inspected Komi surface contains a sourced or attributed quotation, so there was no quotation text to alter or preserve.

All dynamic variable tokens, script-constant tokens, colour markers, and key identifiers used in the final text were preserved exactly. No consumer key was renamed.

## Meaningful validation

A source-to-localisation comparison extracted the 11 decision titles, 11 decision descriptions, 11 custom effect tooltips, category title and description, seven idea title-description pairs, eight unique Independence Wave party keys, and two public ledger labels. It found 59 expected keys, 59 supplied keys, no missing keys, and no extra keys.

A repository English-localisation scan found no duplicate among those 59 owned keys. A formatting scan found no `:0` version markers, em dashes, sentence semicolons, update-history phrases, or unbalanced colour markers.

The linked shared focus tree was inspected through the HOI4 MCP after the localisation patch. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/070a64a43748b1f98b0465153ded3b42d7977cc02e4422bf31dee3c30f1eec57/ee9a2f663685892420d67b5cfe755975761ac6da3fdefd61f5243739f83e1231/focus-inspect.89fb5f89aedbe202.json`. The inspection resolved all 184 shared focus titles. Its failed validation reflects installed-vanilla continuous-focus sprite diagnostics and six existing layout warnings, not Komi localisation or the five helper calls.

## Skipped meaningful validation and blockers

The installed HOI4 MCP exposes no decision inspection or decision rendering route. Therefore the Komi category and decisions could not receive MCP localisation-coverage or overflow evidence. Source key extraction is recorded above but is not treated as equivalent MCP evidence.

No GUI inspection was needed because this package adds no scripted GUI surface. No technology-tree viewer is installed, and no technology is in scope.

Live in-game display validation was not performed because it belongs to the user workflow.

## Unresolved wording decisions and follow-up

There are no unresolved wording decisions in this bounded localisation set.

The package remains subject to its separate identity, flag, portrait, admission, and runtime gates. This localisation patch does not change or bypass those blockers.

## Simplifications and omissions

No requested localisation key or text surface was simplified or omitted. The only unavailable evidence is decision-surface MCP rendering because the installed server has no corresponding route.
