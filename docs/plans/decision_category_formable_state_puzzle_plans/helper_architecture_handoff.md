# Formable state-puzzle helper architecture handoff

## Scope and outcome

This handoff covers the 21 fixed-state formation decisions listed below and the reusable scripted-trigger layer in `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt`.

The live decision availability blocks call one territory helper each, while every territory helper delegates to stable state and group wrappers that can be reused by decision presentation, scripted localisation, scripted GUI properties, and future summaries.

The Nordic League is intentionally outside this architecture because its Estonian route derives requirements through dynamic `all_country_of` and `all_core_state` logic rather than a fixed installed-state list.

## Original-to-helper mapping and counts

Counts are `state checks / unique state IDs / immediate group helpers`; repeated checks are counted in the first number so duplicate source behavior remains visible.

| Original formation decision | Live `available` helper | Immediate group helpers | State checks / unique IDs |
| --- | --- | --- | --- |
| `form_scandinavia` | `chaosx_formable_form_scandinavia_territory_qualifies` | `norway`, `sweden`, `denmark` | 29 / 29 |
| `form_north_sea_empire` | `chaosx_formable_form_north_sea_empire_territory_qualifies` | `norway`, `denmark`, `sweden`, `england` | 29 / 28 |
| `form_baltic_sea_empire` | `chaosx_formable_form_baltic_sea_empire_territory_qualifies` | `sweden`, `denmark`, `finland`, `estonia`, `latvia`, `lithuania` | 41 / 41 |
| `form_gran_colombia` | `chaosx_formable_form_gran_colombia_territory_qualifies` | `shared`, `ecuador`, `colombia`, `venezuela` | 11 / 11 |
| `form_commonwealth` | `chaosx_formable_form_commonwealth_territory_qualifies` | `lithuania`, `poland` | 17 / 17 |
| `form_united_netherlands` | `chaosx_formable_form_united_netherlands_territory_qualifies` | `shared`, `netherlands`, `belgium` | 8 / 8 |
| `form_baltic_federation` | `chaosx_formable_form_baltic_federation_territory_qualifies` | `estonia`, `latvia`, `lithuania` | 14 / 14 |
| `form_mutapa` | `chaosx_formable_form_mutapa_territory_qualifies` | `required_states` | 14 / 14 |
| `form_rattanakosin_kingdom` | `chaosx_formable_form_rattanakosin_kingdom_territory_qualifies` | `siam`, `cambodia`, `laos` | 9 / 9 |
| `form_turkestan` | `chaosx_formable_form_turkestan_territory_qualifies` | `kazakhstan`, `uzbekistan`, `required_states` | 23 / 21 |
| `form_mountainous_republic` | `chaosx_formable_form_mountainous_republic_territory_qualifies` | `required_states` | 5 / 5 |
| `form_idel_uralic_republic` | `chaosx_formable_form_idel_uralic_republic_territory_qualifies` | `required_states` | 5 / 5 |
| `proclaim_greater_italy` | `chaosx_formable_proclaim_greater_italy_territory_qualifies` | `required_states`, `required_other_states` | 25 / 25 |
| `proclaim_sweden_hungary` | `chaosx_formable_proclaim_sweden_hungary_territory_qualifies` | `required_states`, `required_other_states` | 18 / 18 |
| `unite_latin_africa` | `chaosx_formable_unite_latin_africa_territory_qualifies` | `required_states` | 18 / 18 |
| `neo_assyrian_empire_decision` | `chaosx_formable_neo_assyrian_empire_decision_territory_qualifies` | `required_states` | 21 / 21 |
| `neo_mesopotamia_decision` | `chaosx_formable_neo_mesopotamia_decision_territory_qualifies` | `required_states` | 21 / 21 |
| `unite_maghreb` | `chaosx_formable_unite_maghreb_territory_qualifies` | `required_states` | 18 / 18 |
| `unite_greater_mongolia` | `chaosx_formable_unite_greater_mongolia_territory_qualifies` | `required_states` | 21 / 21 |
| `unite_hui_states` | `chaosx_formable_unite_hui_states_territory_qualifies` | `required_states` | 9 / 9 |
| `GOE_form_hindustan` | `chaosx_formable_goe_form_hindustan_territory_qualifies` | `india`, `pakistan`, `required_states` | 39 / 39 |

The helper file contains 392 direct per-formable state wrappers, 47 group wrappers, 21 territory wrappers, and one shared state primitive.

Across the 21 territories there are 395 state-check references and 392 per-territory unique state IDs; North Sea state 931 is intentionally repeated once and Turkestan states 881 and 882 intentionally overlap the Kazakhstan group.

## Helper contract

`chaosx_formable_state_qualifies` is a STATE-scope primitive that evaluates `is_controlled_by = ROOT`, where ROOT is the prospective carrier country.

Each `chaosx_formable_<formable>_state_<id>_qualifies` wrapper enters the literal numeric state scope and calls the primitive, so the wrapper is a pure trigger with no variables, flags, event targets, effects, or world iteration.

Group helpers preserve the original nested `AND`, `OR`, repeated blocks, and `custom_trigger_tooltip` boundaries, including the existing tooltip keys and their order.

The runtime generator in `.tools/generate_formable_state_puzzle_runtime.mjs` emits descending `count_triggers` clauses for each formable's qualifying numerator and inserts every state wrapper directly into those clauses.

Because wrappers only enter a fixed state scope and return a boolean, they are safe inside `count_triggers`, scripted-localisation `defined_text` triggers, decision availability, and scripted-GUI live presentation without cached eligibility state.

## Special policies preserved

- Scandinavia excludes Iceland (100) and Greenland (101) by intent.
- North Sea keeps the original duplicate check for state 931, and the Denmark branch intentionally does not require the islands.
- The Baltic Sea Empire Finland group excludes Petsamo, Salla, and Karjala.
- Turkestan keeps the Kazakhstan overlap for states 881 and 882 and retains the separate required-state checks and source comments.
- Hui keeps states 283, 753, 287, 619, and 1045 excluded.
- Neo Mesopotamia keeps state 183 excluded.
- Greater Italy and Sweden-Hungary `required_other_states` wrappers preserve the original subject-control semantics: the prospective carrier itself or a country subject to that carrier may control each state.
- Commonwealth's compliance `OR` and every other non-state condition remain in the decision block rather than being folded into territory helpers.
- Existing subject gates, DLC gates, focus gates, country flags, comments, and tooltip groupings remain at their original decision surfaces.

## Files changed

- `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt` adds the complete fixed-state primitive, per-state wrappers, group wrappers, and 21 territory wrappers, with comments documenting intentional exclusions.
- `common/decisions/formable_nation_decisions.txt` routes exactly the 21 approved decisions' state requirements through their territory helpers while retaining each block's non-state logic.
- `docs/plans/decision_category_formable_state_puzzle_plans/helper_architecture_handoff.md` records this mapping, contract, validation, and risks.

No effects, script constants, event targets, on-actions, cached variables, scan helpers, or unrelated decision surfaces were added.

## Validation evidence

- A top-level brace parser found 461 helper definitions with zero unbalanced blocks and zero duplicate names.
- Name audit found all 461 helper names lowercase and unique, with exactly 21 `_territory_qualifies` helpers.
- The 21 decision call-site audit found exactly one territory helper call in each approved `available` block and no Nordic League call.
- Flattened state-ID comparison matches the original direct requirements for 19 decisions; the Greater Italy and Sweden-Hungary source parser double-counted nested subject alternatives, while the wrappers retain the intended single-state `OR` semantics.
- Tooltip-key comparison matches all preserved group tooltip sequences, including Norway/Sweden/Denmark, North Sea, Baltic, Gran Colombia, Commonwealth, United Netherlands, Baltic Federation, Turkestan, Greater Italy, Sweden-Hungary, and Hindustan groups.
- The required offline Paradox wiki pages, vanilla trigger/effects/script-constant documentation, and vanilla fixed numeric state-scope precedents were consulted before the helper design.
- `hoi4.gui_inspect` was attempted for the generated state-puzzle window, but the generated GUI source is not present until all reviewed manifests are available and the valid scenario invocation did not return an artifact; no GUI rewrite was performed and no GUI evidence is claimed here.
- No probability audit was required because this patch changes no AI weight, score, MTTH, random selection, or other weighted surface.

## Risks and unsupported analysis

- The runtime generator currently has reviewed manifests for 14 of the 21 selected categories, so generated GUI, scripted-GUI, scripted-localisation, and localisation outputs remain blocked until the seven missing manifests are supplied; helper availability is independent of that generation step.
- Numeric state scopes are tied to the installed map revision; map changes require the reviewed manifests, state wrappers, and generated assets to be rebuilt together.
- The Greater Italy and Sweden-Hungary subject alternatives preserve the source decisions' carrier-or-subject result through carrier-scoped `any_subject_country` checks. This bounds evaluation to the relevant carrier's subjects instead of repeating the source `any_country` world search for every state; no helper performs `all_country_of`, `all_core_state`, on-action iteration, or persistent scope caching.
- GUI MCP artifacts for the generated window are unavailable in this handoff because the generated source is not materialized; source inspection of the runtime generator proves the live `count_triggers` contract but does not substitute for later GUI render/compare evidence.

No gameplay simplifications were introduced within the approved 21-decision scope.
