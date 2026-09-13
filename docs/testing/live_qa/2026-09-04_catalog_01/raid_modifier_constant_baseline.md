# Event 016 native raid modifier constant baseline

Audit date: 2026-09-05.

Audit status: **Exact parser and source inventory; raid probability analysis unresolved because the installed HOI4 MCP has no raid weighted-surface adapter.**

This read-only baseline covers the 22 launch_08 malformed constant tokens in the four named raid files. The audited values are fictional game tuning fields. No gameplay, AI, outcome, target, route, or real-world mechanic was redesigned, and no source file was edited, staged, or committed by this audit.

## QA evidence

The fresh launch log is `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_08/logs/error.log`.

Launch 08 started at `2026-09-05T07:30:12.4471091Z`, stopped at `2026-09-05T07:32:29.6981649Z`, and recorded source checkpoint `ef354146d93ff2ba4022db5c5141878f95589c9b`.

The raid parser errors are lines 3 through 24 of that log and all use the form:

```text
[10:31:23][no_game_date][pdx_parser.h:1203]: Error: "Malformed token: constant:brilliant_scientist_biological_staging.native_success_bonus, near line: 182" in file: "common/raids/biological_battlefield_raids.txt" near line: 182
```

The exact log count is 22 malformed tokens: 14 `native_success_bonus`, 4 `native_critical_bonus`, and 4 `native_disaster_reduction` references.

The per-file error count is 4 in `common/raids/biological_battlefield_raids.txt`, 12 in `common/raids/biological_raids.txt`, 3 in `common/raids/zombie_weaponized_friendly_raids.txt`, and 3 in `common/raids/zombie_weaponized_raids.txt`.

The first two launch_08 lines are the earlier Event 021 `stability` parser error, and later launch_08 lines contain unrelated files. Those errors are outside this isolated raid baseline and were not folded into the findings.

## Exact source inventory

The malformed tokens are all `weight` fields inside `success_factors` custom outcome modifiers. Each modifier has `formula = { base = 0 modifier = { has_country_flag = brilliant_scientist_biological_staging_ready add = 1 } }`, `reference = 1`, `can_actor_affect = yes`, and `can_target_affect = no`.

| Source file | Raid identifiers and exact malformed locations | Field count |
| --- | --- | ---: |
| `common/raids/biological_battlefield_raids.txt` | `anthrax_battlefield_dissemination` success line 182; `plague_battlefield_dissemination` success line 324; `tularemia_battlefield_dissemination` success line 406; `smallpox_battlefield_dissemination` success line 488 | 4 |
| `common/raids/biological_raids.txt` | `anthrax_strike` success/critical/disaster lines 320/339/361; `plague_strike` success/critical/disaster lines 759/778/800; `tularemia_strike` success/critical/disaster lines 1198/1217/1239; `smallpox_strike` success/critical/disaster lines 1637/1656/1678 | 12 |
| `common/raids/zombie_weaponized_friendly_raids.txt` | `weaponized_zombie_strike_low_friendly` success line 92; `weaponized_zombie_strike_medium_friendly` success line 237; `weaponized_zombie_strike_high_friendly` success line 382 | 3 |
| `common/raids/zombie_weaponized_raids.txt` | `weaponized_zombie_strike_low` success line 134; `weaponized_zombie_strike_medium` success line 269; `weaponized_zombie_strike_high` success line 403 | 3 |

The current local SHA-256 values are `DDE40E3EAC91AD357DB5CB3C90AF36E0E3391BAA68D5E5D900241340EF3EDDD7` for `biological_battlefield_raids.txt`, `8EF5CEBC37F88862BC3F33DD07B0A307182EB792D5CBCC749CB3F858B8668267` for `biological_raids.txt`, `94FB7B740DAD22D71BD0D6884EA79FA44D510D4F4804E60C6D436827EE463F8C` for `zombie_weaponized_friendly_raids.txt`, and `37A26074261A93809117C16BAFA70751323018B0C06EDA6B057959B4C49787A6` for `zombie_weaponized_raids.txt`.

No file-local `@` alias for any of the three native staging values was present in the four audited files at baseline. The existing file-local aliases remain unrelated raid bases, costs, references, damage values, and experience values.

## Authoritative values and field semantics

The shared source is `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt:90-104`.

Its `brilliant_scientist_biological_staging` category declares `schema = { any_key = yes data = fixed_point }` and the exact values are:

| Constant identifier | Current value | Occurrence count | Native outcome use |
| --- | ---: | ---: | --- |
| `brilliant_scientist_biological_staging.native_success_bonus` | `0.15` | 14 | Additive success modifier when the staging flag is present |
| `brilliant_scientist_biological_staging.native_critical_bonus` | `0.10` | 4 | Additive conditional critical modifier when the staging flag is present |
| `brilliant_scientist_biological_staging.native_disaster_reduction` | `-0.08` | 4 | Additive disaster reduction when the staging flag is present |

The same category also contains `native_ai_factor = 4.0`. Its `factor = constant:brilliant_scientist_biological_staging.native_ai_factor` uses appear in raid `ai_will_do` blocks, but none of those references generated one of the 22 reported malformed `weight` errors and they are outside the proposed alias substitution.

The current source-wise native modifier trace is zero when `brilliant_scientist_biological_staging_ready` is absent and is respectively `+0.15`, `+0.10`, and `-0.08` when the flag is present. These are formula contributions, not complete raid outcome probabilities.

The installed vanilla raid documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md:66-78` defines raid `ai_will_do` as an AI score that must be greater than zero for the AI to want a raid.

The same documentation at `:209-325` defines `success_factors` as outcome formulas, requires a `weight` value for each modifier, and distinguishes success, conditional critical success, and disaster probability semantics.

The custom success modifier guidance at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md:411-429` shows a static numeric `weight` beside a separate MTTH `formula` block. It does not establish support for a `constant:` token in this native static `weight` consumer.

The installed script-constant documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md:1-32` states that only documented fields support `constant:` and that `@` aliases are a separate script form.

The installed script concept documentation `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md:216-244` likewise limits `constant:` to supported fields and documents file-local `@` macros as the alternative.

The offline wiki `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:42-53` documents file-local numeric `@` aliases and their use in static fields such as `cost = @CONSTANT_1`.

The offline wiki `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md:176-178` distinguishes static modifier definitions from the native raid formula fields. It does not provide a raid probability adapter or extend the documented static `weight` consumer with `constant:` support.

## Scoped owner correction

The approved owner repair is to add file-local `@` aliases equal to `0.15`, `0.10`, and `-0.08` in each affected raid file and replace only the 22 rejecting `weight = constant:brilliant_scientist_biological_staging.native_*` tokens with the corresponding aliases.

The repair must leave the shared `brilliant_scientist_biological_staging` category unchanged, preserve every formula gate, reference, outcome name, raid identifier, AI score block, target gate, and route condition, and keep the three numeric values byte-for-byte equivalent after expansion.

This baseline supplies no balance target. It supports a syntax compatibility correction only because launch_08 explicitly rejects the current token form and the documented alias form is the static numeric mechanism used by the surrounding files.

## HOI4 MCP probability inspection

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The mandatory read-only `hoi4.probability_inspect` source scans were run for one representative raid identifier in each audited file with `refresh: true` and no forced adapter.

| Source identifier | Source path | MCP result | MCP revision and source hash | Inspect artifact |
| --- | --- | --- | --- | --- |
| `anthrax_battlefield_dissemination` | `common/raids/biological_battlefield_raids.txt` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: no_weighted_surfaces`; candidates 0; available candidates 0; unresolved 0 | `6829d3d66e7252b21964bd2a3eaed1027ec7539cfc4c98a5d788f280f528b55c`; `37726cca2aa53261adf977f05a7583ed75c71c39f73a45b4547d997d3c11d7cd` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72a7ab8fa9ec67a11773c5c0326a08b3578befcd06afdbf51b3ac9cda4ed5059/a7cb4c480eaca85eda745dac378e9034f34de3791f3a59733d5c64909a57cb4c/probability-inspect-37726cca2aa5.json` |
| `anthrax_strike` | `common/raids/biological_raids.txt` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: no_weighted_surfaces`; candidates 0; available candidates 0; unresolved 0 | `2c1ade0ee0984929577462c6b0d039d7fcd6c82c8124201533f3778579167cb6`; `b19b94fe79899579cc900b9a94306da446bdd5bf4fc34e2ef17337c77cc3cc13` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed29de342612ea2c516080d447db99f45a3a16a4715190ebdb84f2b4b0b9c6b8/0e2ab2477fdd933aad519b6e345cbde4f46f2dfc3c3300c35b70fdb7169aa9e8/probability-inspect-b19b94fe7989.json` |
| `weaponized_zombie_strike_low_friendly` | `common/raids/zombie_weaponized_friendly_raids.txt` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: no_weighted_surfaces`; candidates 0; available candidates 0; unresolved 0 | `cfa87b618a68c3fb1d44771f9f95ce49c6743cfdc50c0bda62ebb2f5147e644e`; `c2ec9aa30b81b7ae2a0517ff5387f36be6c7800d76bbdcdbf562d8cadf11eee1` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8ee806e70ed09457cbc7a9ba8dd9bbfa53f0190179970b46507b8785adfc90a/37fa4fd4bbabaa3cf627e9d472c9781f29e1d818d84d03cfab617bebd85badf1/probability-inspect-c2ec9aa30b81.json` |
| `weaponized_zombie_strike_low` | `common/raids/zombie_weaponized_raids.txt` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: no_weighted_surfaces`; candidates 0; available candidates 0; unresolved 0 | `20ed680ee710d6423bdb00135fb32ba33fcf6b5703cfcd885e5aa72b55bf0eb3`; `f005970d08144f508624c2698e2eb0951bd748c340794a66d2b208aca4613519` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52b02b9361f355dcbe99c226d6cfdf696549f34a2ae5e9edc64a2d8db4eaea2f/932ea49b900337c6dc14a0adcd925212d8b979ced3615b0f6e02d0e948d3f67b/probability-inspect-f005970d0814.json` |

The source scans reported `adapters: 11` and `availableAdapters: []` for every raid file. The adapter inventory contains no raid-specific `success_factors`, raid outcome, or raid `ai_will_do` route.

Additional adapter probes used the ordinary source `anthrax_strike`:

| Adapter probe | MCP result and provenance |
| --- | --- |
| `direct_random` on `anthrax_strike` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: identifier_not_found`; candidates 0; revision `2e812299be0daaf1013435637303d07bca38105b5c9ba79314125167602b6c64`; source hash `b19b94fe79899579cc900b9a94306da446bdd5bf4fc34e2ef17337c77cc3cc13`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a6b94c1c0229746ea72fef18e713b4af0a1ef1fcccb802fe9a3da20381701f3/e22a6883288432db499dedaf404a8635ae608a96ec98c1cc5d89ab231f49103e/probability-inspect-b19b94fe7989.json` |
| `custom_weighted_pool` on `anthrax_strike` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: identifier_not_found`; candidates 0; revision `2e812299be0daaf1013435637303d07bca38105b5c9ba79314125167602b6c64`; source hash `b19b94fe79899579cc900b9a94306da446bdd5bf4fc34e2ef17337c77cc3cc13`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fa7557f49cfaa0f0e52678d7327df3a7af3516dd9714fd29094e301ed57e024/e523e3a92fe1c6312d68cd5d66eee7745797c60a5368b5a503bee7902eda5115/probability-inspect-b19b94fe7989.json` |
| `event_option_ai_chance` on `anthrax_strike` | `PROBABILITY_SOURCE_DISCOVERED`; `discoveryReason: identifier_not_found`; candidates 0; revision `2e812299be0daaf1013435637303d07bca38105b5c9ba79314125167602b6c64`; source hash `b19b94fe79899579cc900b9a94306da446bdd5bf4fc34e2ef17337c77cc3cc13`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e18c131d094a8b4fdf65b474020bebdbddd1460e30b69f549073234ae7560cd3/17a20956239b27d44ece9573423817b90850bf6546676a00f31b4a6470f9ef59/probability-inspect-b19b94fe7989.json` |
| `decision_ai_will_do` on `anthrax_strike` | `INTERNAL_ERROR`, message `Unexpected internal error`, no files scanned, no artifact, no revision, and no candidate result. This is not treated as raid evidence. |
| `direct_random` on `brilliant_scientist_biological_staging_success` | Same ordinary source hash and revision as the `direct_random` probe; `identifier_not_found`, zero candidates, and the direct-random artifact above. |
| `event_mean_time_to_happen` on `brilliant_scientist_biological_staging_success` | `INTERNAL_ERROR`, message `Unexpected internal error`, no files scanned, no artifact, no revision, and no candidate result. This is not treated as MTTH evidence. |

The inspect results establish an adapter and source-discovery limitation. They do not establish zero raid outcome probability, zero AI willingness, or any change in game behavior.

## Scenario and pool disposition

No named probability scenario was evaluated because every relevant source inspection returned zero weighted candidates or an adapter error before a scenario could bind.

The conceptual outcome set is `success`, `critical`, `disaster`, and `failure` for each raid type, but it is not a candidate pool exposed by the installed probability service. A normalized pool cannot be supplied without replacing the native raid engine with an invented manifest.

The external factors required for a meaningful native raid outcome fixture would include the raid type, actor and target scopes, readiness flag, preparation progress, assigned unit experience and relevant unit stats, target anti-air or resistance state, interception, radar, intel, target validity, launchability, equipment availability, and any competing raid or target context. None of those factors were evaluated by MCP for these native fields.

The raid `ai_will_do` blocks are separate score races over valid raid and target choices. They would require a complete competing raid/target pool and actor/target state before any rank or selection claim could be made. No such pool was exposed or declared.

No scenario ID, scenario hash, analysis ID, timing trace, sensitivity result, rank reversal, sampled result, or rendered probability artifact exists for this baseline.

## Findings and classifications

| Finding | Classification | Evidence |
| --- | --- | --- |
| The current `constant:brilliant_scientist_biological_staging.native_*` token form is rejected in the 22 native `weight` fields. | `exact` parser finding | Launch_08 `pdx_parser.h:1203` errors at all 22 listed locations. |
| The three referenced numeric values are exactly `0.15`, `0.10`, and `-0.08`. | `exact` source finding | `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt:90-104`. |
| A same-value file-local alias substitution is a scoped compatibility candidate. | `bounded` source recommendation | Installed constant docs and offline alias examples support file-local `@` values; owner must verify native load after patch. |
| Native raid success, critical, and disaster probabilities. | `unresolved` | No raid outcome adapter, no candidate pool, and no complete actor/unit/target fixture. |
| Raid `ai_will_do` rank, target selection, dominance, or starvation. | `unresolved` | No raid AI adapter and no complete competing raid/target pool. |
| Repetition, cooldown, cadence, sequence, or exploit risk. | `unresolved` | No sequence model or native raid runtime trace was exposed. |

The source-only modifier contribution is `0` when the staging flag is absent and the corresponding constant value when it is present. It must not be reported as an automatic raid probability or a click probability.

## Recommended owner action

In each of the four named raid files, add file-local aliases equal to the authoritative values and replace only the 22 malformed native `weight` tokens with those aliases.

Keep `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt` unchanged, and preserve every source identifier, formula gate, outcome branch, AI factor, target gate, and numeric value after alias expansion.

After the owner patch, the parent should repeat the launch parser check and, if a raid-specific MCP adapter becomes available, run `hoi4.probability_inspect`, named scenario evaluation, and same-scenario comparison using a complete native raid fixture. The present baseline has no valid analysis ID or before probability result to compare.

## Skipped analyses and blockers

`hoi4.probability_evaluate` was not run because all relevant source inspections returned zero candidates or adapter errors, so no supported raid scenario surface exists.

`hoi4.probability_sweep` was not run because there is no continuous raid outcome or AI score surface to vary and no complete candidate pool.

`hoi4.probability_render` was not run because no evaluate, sweep, simulation, sequence, or comparison analysis ID exists.

`hoi4.probability_simulate` was not run because no uncertain input distributions, seed, or complete native raid pool were available.

`hoi4.probability_sequence` was not run because no complete raid cadence, preparation transition, cooldown, recovery, removal, reset, or terminal-state manifest was available.

`hoi4.probability_compare` was not run because no baseline analysis ID or supported before/after raid probability surface exists; the owner patch remains pending.

The exact remaining blocker is adapter coverage: the installed HOI4 MCP exposes no native raid modifier, raid outcome, or raid AI `ai_will_do` adapter, and its generic routes do not discover these four raid files. No hand arithmetic or source-only formula was substituted for the missing MCP evidence.

No simplification or unapproved fallback was used.
