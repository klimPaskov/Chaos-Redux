# Event 018 engine-compatibility correction handoff

Date: 2026-08-09

## Scope

This tranche corrects Event 018 source constructs that were incompatible with the current documented HOI4 script interfaces or that resolved in the wrong decision-target scope. It does not change the requested Event 018 balance targets or introduce a fallback.

The review used the offline `Decision modding`, `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, and `Character modding` wiki pages, the current vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`, and direct vanilla examples from `common/decisions`, `common/unit_leader`, and `common/ideas`.

## Corrected surfaces

- Replaced five legacy `while = {}` effects with current `while_loop_effect = {}` loops in field roll batching, captured-resource capacity division, starting-strength division, opening brood allocation, and world-end foothold spawning.
- Replaced the obsolete `add_army_experience` effect with documented `army_experience`.
- Replaced the obsolete `resources_to_market_factor` modifier with the current `min_export` modifier.
- Moved the three cave commander traits from `common/country_leader` to `common/unit_leader` and changed their declared type from `basic_terrain` to the vanilla `basic_terrain_trait` type.
- Added the consumed but previously undefined `resources_found_cave_containment_rivalry` opinion modifier and its localisation.
- Wrapped every Event 018 country-target and state-target `target_trigger` predicate in `FROM`, matching the offline decision documentation and vanilla targeted-decision examples. This repairs the foreign bidder, contract partner, border claimant, cave anchor, resource-denial, activation-window recapture, anchor cleanup, threat-cooperation, and restoration target filters.
- Replaced direct dynamic-variable comparison of `num_owned_states` in event options with documented `check_variable` syntax.
- Replaced script-constant tokens in effect fields that document literal values rather than scoped values with file-local mirrors of the authoritative Event 018 constants. The covered fields are building levels, building damage, border-war width/duration/province count/modifiers, division-count `size`, and technology bonus/uses.
- Preserved all requested values; the file-local mirrors exactly match the shared script constants and are present only where `constant:` injection is not documented.

## Cave brood weighted pool

The former random-list entries used nested country-scoped entry triggers. The implementation now calculates explicit zero-or-weight temporary variables before the pool and uses those five variables as the random-list weights. The selection remains one categorical roll and its probabilities are unchanged.

Final HOI4 MCP evidence:

- Source inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51172099c364dc9930d3cdee1c980e253de52730b123a9b832b0e0b5ff9bdaac/cd969586716f19bf3814fa8eb851a1ee6ec0320ecf90cb858f1c301b0a70a555/probability-inspect-4c8326d2b149.json`
- Semantic before/after comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d5873d070a7693af1476474e45b758f9c249cf88e01e63980293613ccb28733/1958aecba95553c375556a4bef2a80cd1bf484d92e48dd4bb46328f05c60ad1a/probability-bbe2a7826c7d17bc61f2e1ef.json`
- Comparison raster: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/deea4dbd781ee84766d15cfac98f07b593c29e4a14def9683d9d9d502dc21b60/probability-probability-bbe2a7826c7d17bc61f2e1ef-comparison.png`

The final comparison covers eight named scenarios, reports zero unresolved inputs and zero probability changes, and verifies:

| Scenario | War Brood | Route Brood | Feeding Guard |
| --- | ---: | ---: | ---: |
| No doctrine or guard | 100.000% | 0.000% | 0.000% |
| Stone, Burrow, or Scree doctrine | 76.923% | 23.077% | 0.000% |
| Stone, Burrow, or Scree doctrine plus guard | 71.429% | 21.429% | 7.143% |
| Guard only | 90.909% | 0.000% | 9.091% |

The sole design diagnostic is the intended 100% War Brood result when neither a doctrine brood nor the Feeding Guard is available.

## Ownership boundary

The concurrent Event 019 provider adapter in `018_resources_found_cave_effects.txt`, its provider metadata in `018_resources_found_cave_constants.txt`, and its `on_startup` registration in `018_resources_found_on_actions.txt` are not part of this Event 018 correction tranche. They remain untouched in the working tree and must not be included in the Event 018 engine-fix commit.

## Remaining proof

This handoff is not a final Event 018 completion claim. Independent final focus, decision, country, localisation, probability, and event-completion audits, the final scripted-GUI MCP render, the near-completion improvement-loop pass, and the consolidated acceptance reconciliation remain separate gates.
