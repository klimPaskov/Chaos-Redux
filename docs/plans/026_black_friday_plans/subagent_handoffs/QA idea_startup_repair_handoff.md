# QA idea startup repair handoff

Date: 2026-09-05.

Disposition: implemented within the assigned startup-repair scope, including the parent-authorized Event 016 addendum below.

## Scope and safety

The original exclusive gameplay write set was `common/ideas/021_random_civil_war_ideas.txt`, `common/ideas/026_black_friday_ideas.txt`, `common/ideas/031_random_terror_ideas.txt`, `common/ideas/032_missiles_ideas.txt`, and `common/ideas/035_great_depression_ideas.txt`.

A subsequent parent-authorized addendum changed only `common/ideas/016_brilliant_scientist_external_rewards_ideas.txt` to repair its three logged malformed modifier values.

The only documentation write is this handoff.

Backups were created before editing under `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_ideas/common/ideas/` with the original relative filenames.

No scripts, schema files, event files, decisions, focuses, countries, map data, AI weights, probability values, balance targets, localisation, assets, or other protected Event 016 external reward ideas were edited.

No game or desktop process was started.

## QA source evidence

The source log is `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_07/logs/error.log`.

The assigned error lines were 34-36, 41-51, and 52, for 15 total errors across the five files.

| Log lines | File and identifiers | Before | After | Evidence basis |
| --- | --- | --- | --- | --- |
| 34, 52 | `021_random_civil_war_ideas.txt:event021_war_torn_administration`; `035_great_depression_ideas.txt:great_depression_legacy_public_works` | `infrastructure_construction_speed` | `production_speed_infrastructure_factor` | Installed `modifiers_documentation.md` documents `production_speed_<Building>_factor` with `infrastructure` as a modified type, and vanilla construction-speed precedents use the same field. |
| 35-36 | `021_random_civil_war_ideas.txt:event021_secured_front_depot` | `constant:event021_action_tuning.depot_supply_consumption`; `constant:event021_action_tuning.depot_army_organization` | File-local `@EVENT021_DEPOT_SUPPLY_CONSUMPTION`; `@EVENT021_DEPOT_ARMY_ORGANIZATION` | Values remain `-0.10` and `0.10`, matching `common/script_constants/021_random_civil_war_constants.txt:event021_action_tuning`. |
| 41-42 | `026_black_friday_ideas.txt:black_friday_sale`; `black_friday_sale_evolution_i` | `academy_cost_factor` | `academy_spirit_cost_factor` | Installed `modifiers_documentation.md` defines `<IdeaGroup>_cost_factor` and lists `academy_spirit`; the offline Ideas page documents the same cost-factor construction. |
| 43 | `031_random_terror_ideas.txt:random_terror_improvised_command` | `reinforce_rate` | `land_reinforce_rate` | Installed `modifiers_documentation.md` documents `land_reinforce_rate`, and vanilla idea files use this exact modifier. |
| 44-51 | `032_missiles_ideas.txt:missiles_program_experimental`, `missiles_program_operational`, `missiles_program_compromised` | Eight `constant:missiles_modifier.*` values inside idea modifier blocks | Eight file-local `@MISSILES_PROGRAM_*` values | Values remain `0.02`, `0.03`, `0.04`, `0.08`, `0.02`, `-0.04`, `-0.05`, and `-0.10`, matching `common/script_constants/032_missiles_constants.txt:missiles_modifier`. |

## Exact source changes

`common/ideas/021_random_civil_war_ideas.txt` adds `@EVENT021_DEPOT_SUPPLY_CONSUMPTION = -0.10` and `@EVENT021_DEPOT_ARMY_ORGANIZATION = 0.10` at lines 11-12, changes the infrastructure field at line 35, and uses the aliases at lines 55-56.

`common/ideas/026_black_friday_ideas.txt` changes the army academy cost field to `academy_spirit_cost_factor` at lines 35 and 90 while preserving the existing `@BLACK_FRIDAY_BASE_FACTOR` and `@BLACK_FRIDAY_EVOLUTION_I_FACTOR` values.

`common/ideas/031_random_terror_ideas.txt` changes `reinforce_rate` to `land_reinforce_rate` at line 18 and leaves the other existing reinforcement modifiers unchanged.

`common/ideas/032_missiles_ideas.txt` adds eight file-local aliases at lines 10-17 and replaces the eight malformed `constant:` values at lines 25-26, 34-36, and 44-46.

`common/ideas/035_great_depression_ideas.txt` changes the public-works field to `production_speed_infrastructure_factor` at line 48 and preserves the `0.08` value.

The file-local aliases are deliberate because the installed constants documentation permits `constant:` only where the consuming field documents support, while the launch log reports those tokens as malformed in idea modifier blocks.

## Coverage checklist

| Surface | Result |
| --- | --- |
| Country tag, history, ownership, cores, claims, capital, victory points, supply, railways, ports, resources, and buildings | Out of scope; no country or map surface was changed. |
| Politics, leaders, portraits, flags, advisors, parties, diplomacy, subjects, and cosmetic tags | Out of scope; no country identity surface was changed. |
| Focus trees, decisions, missions, events, event options, and event-owned GUI | Read-only event linkage inspected where affected; no gameplay source was changed. |
| Ideas and national-spirit modifier fields | Repaired in the five assigned files; all 15 assigned launch errors have corresponding source fixes. |
| Assets and localisation | Out of scope; no displayed identifier or asset reference changed. |
| Starting military, technology, industry, production, and supply setup | Out of scope; no starting setup or technology surface was changed. |
| AI and probability | No weights or probability surfaces changed, so the probability-auditor route was not required. |

## Required source and engine evidence

The required offline wiki pages were consulted: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.

The installed references consulted were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`.

Vanilla precedents included `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ideas/finland.txt` for idea modifier syntax and `land_reinforce_rate`, `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_leader/taog_traits.txt` for `production_speed_infrastructure_factor`, and the vanilla `common/idea_tags/00_idea.txt` academy slot definitions.

## MCP evidence

Read-only focused Event Chain Viewer lint was run for `chaosx.nr21.1`, `chaosx.nr26.1`, `chaosx.nr31.1`, `chaosx.nr32.1`, and `chaosx.nr35.1` after the source patch.

Each route returned `EVENT_INSPECTED_PARTIAL` with workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `4520c3ceb2ac2ff2148d4a7228cd8878f66ba12464a692526456f94fa064899f`, and graph hash `5e3d139e6f05e68b3a6113d31899826893cdcd622d7328cf49b05b1daa10c66f`.

The useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d56f629fac5a7cba8f1d4c5098c8d1569ec18b3adc6bcf539131b5f738783ab8/58146285b1aef9fae7b271bff8a6f21d1789b5cd1ec8d25eb46ff59a1fd9b3ab/event-lint-4520c3ceb2ac.json` for Event 021, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1582c85187bc038eaf2f11bfbbbf27468b8b202716759f5b3bd44257078bce8/4ea3e54e72d990dcc12182bdb04fdfa0d7e6868ee99c2c9da29d476c55c257e8/event-lint-4520c3ceb2ac.json` for Event 026, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ff83c87fd1812b9857728fd4da147391524f4236fa8680979a5faf3ebfeaa7f/fb0bc0df700013d26f9a2ecfc19b8af5e3971029437e6afa23ccb7f29dd2a799/event-lint-4520c3ceb2ac.json` for Event 031, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a6a6f4fd2da7ff2742fc5c139a48011b9b15bd4782552db9968c2091aad0f28/82fd5ec1f0c678938653e5074e766c9deb281f9da76af577e8979b40c6bff929/event-lint-4520c3ceb2ac.json` for Event 032, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53c90009e21d1b19d75db4c2c6372cea242de2996960e4de4c9ed7f42c68ba2f/c19106aa601795da88849fd006c7fdf74243c786a77ffbc3e260ecfd1e382efe/event-lint-4520c3ceb2ac.json` for Event 035.

The MCP route reported no blockers in its returned `blockers` arrays, but validation remained partial because workspace-wide helper and lifecycle projections were deferred.

The broad lint payload reports one blocking diagnostic in its aggregate graph without attributing that diagnostic to these five idea files, so this handoff does not claim whole-workspace event validation.

The standalone Technology Tree Viewer was not exercised because this repair has no technology or doctrine surface.

## Validation

A focused source scan found zero remaining `infrastructure_construction_speed`, `academy_cost_factor`, standalone `reinforce_rate`, or `= constant:` values in the five assigned files.

A one-off syntax check confirmed balanced braces and quotes in all five files and verified every new alias's numeric value and use count.

The focused backup diff contains only the listed modifier replacements, alias declarations, alias substitutions, and linkage comments.

The pre-patch files remain available at `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_ideas/common/ideas/021_random_civil_war_ideas.txt`, `026_black_friday_ideas.txt`, `031_random_terror_ideas.txt`, `032_missiles_ideas.txt`, and `035_great_depression_ideas.txt`.

## Skipped validation and remaining risks

No new launch was run because the parent requested review of this repair tranche before the next startup attempt, and agents do not perform live-game validation.

The historical launch log necessarily still contains the old error lines; it was not edited.

The parent should run the next startup QA pass and inspect the idea parser output after integrating this tranche.

No simplification or fallback was introduced.

## Event 016 addendum

Date: 2026-09-05.

The parent authorized one isolated parse repair in `common/ideas/016_brilliant_scientist_external_rewards_ideas.txt`, despite the broader Event 016 protection boundary.

Launch 07 log lines 31-33 reported malformed `constant:chaosx_custom_technology_tuning.integration_research_speed`, `constant:chaosx_custom_technology_tuning.integration_special_project_speed`, and `constant:chaosx_custom_technology_tuning.integration_air_attack` values in the `brilliant_scientist_alien_systems_integration` modifier block.

The file now defines `@BRILLIANT_SCIENTIST_INTEGRATION_RESEARCH_SPEED = 0.06`, `@BRILLIANT_SCIENTIST_INTEGRATION_SPECIAL_PROJECT_SPEED = 0.04`, and `@BRILLIANT_SCIENTIST_INTEGRATION_AIR_ATTACK = 0.02` and uses those aliases for the existing `research_speed_factor`, `special_project_speed_factor`, and `air_attack_factor` fields.

The values were verified against `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt:chaosx_custom_technology_tuning` at `integration_research_speed = 0.06`, `integration_special_project_speed = 0.04`, and `integration_air_attack = 0.02`.

The pre-edit Event 016 file is archived at `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_ideas/common/ideas/016_brilliant_scientist_external_rewards_ideas.txt`.

The focused Event 016 read-only lint returned `EVENT_INSPECTED_PARTIAL` with workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `524f2937a47d4d31bd89ec3b5e6185825935909d15ff955e2e35187522458d75`, graph hash `b8d24cd3ea64f7679b3ca2c99b73959b345d24e0c38c1243babcd61552d8a9b6`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebf764423de44478a58452063b3f49ecbf5689ca5207eec07e28ba2e4fc133f7/800d2b1d3ac7ebb7a3ae9f06c28cf6540774ad9de5f42e51ee78e16da97ef0da/event-lint-524f2937a47d.json`.

The focused source validation found balanced braces and quotes, zero remaining `constant:` values, zero old integration field tokens, and exact alias numeric parity.

No Event 016 schema, scripts, effects, IDs, numeric tuning, or other protected files were changed, and no game launch or commit was performed.

The Event 016 MCP result remains partial because workspace-wide helper and lifecycle projections were deferred; its blockers array was empty, while the aggregate payload carried one unattributed blocking diagnostic.
