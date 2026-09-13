# Event 031 country package handoff

Status: The eight dormant Event 031 territorial carrier packages are implemented in the allowed country, history, tag, and character surfaces, and no commit was created.

## Changed files

- `common\country_tags\031_random_terror_countries.txt`
- `common\countries\031_random_terror_JHX.txt` through `common\countries\031_random_terror_JPX.txt`
- `common\characters\031_random_terror_characters.txt`
- `history\countries\031_random_terror_JHX - Local Cell.txt`
- `history\countries\031_random_terror_JIX - Regional Insurgent.txt`
- `history\countries\031_random_terror_JKX - Transnational Network.txt`
- `history\countries\031_random_terror_JLX - Jihadist International.txt`
- `history\countries\031_random_terror_JMX - Final Command.txt`
- `history\countries\031_random_terror_JNX - Local Cell II.txt`
- `history\countries\031_random_terror_JOX - Regional Insurgent II.txt`
- `history\countries\031_random_terror_JPX - Transnational Network II.txt`

No `common\ai_strategy\031_random_terror_country_ai.txt` was added because Event 031 selects dynamic parents, states, sponsors, and route profiles that cannot be represented safely by a static carrier-target strategy file.

## Carrier matrix

| Tag | Profile | Fallback capital state | Research slots | Leader and portrait GFX |
| --- | --- | ---: | ---: | --- |
| `JHX` | Local Cell | `104` | `2` | `JHX_random_terror_shadow_council` · `GFX_Portrait_Random_Terror_Council_01` |
| `JIX` | Regional Insurgent | `47` | `3` | `JIX_random_terror_war_directorate` · `GFX_Portrait_Random_Terror_Council_02` |
| `JKX` | Transnational Network | `112` | `3` | `JKX_random_terror_ideological_secretariat` · `GFX_Portrait_Random_Terror_Council_03` |
| `JLX` | Jihadist International | `49` | `3` | `JLX_random_terror_rasim_vey` · `GFX_Portrait_Random_Terror_Jihadist_01` |
| `JMX` | Final Revelation | `64` | `5` | `JMX_random_terror_unanswered_presence` · `GFX_Portrait_Random_Terror_Entity` |
| `JNX` | Local Cell II | `107` | `2` | `JNX_random_terror_nera_vos` · `GFX_Portrait_Random_Terror_Clandestine_01` |
| `JOX` | Regional Insurgent II | `46` | `3` | `JOX_random_terror_liora_vask` · `GFX_Portrait_Random_Terror_Military_01` |
| `JPX` | Transnational Network II | `141` | `3` | `JPX_random_terror_arel_venn` · `GFX_Portrait_Random_Terror_Revolutionary_01` |

The capitals are valid fallback state IDs only; Event 031 transfers the selected state, adds the carrier core, and replaces the capital at activation.

## Setup and dependencies

Each history uses only vanilla `infantry` and `recon` components in the locked `Infantry Division` template expected by `random_terror_initialize_actor`.

Each carrier has the vanilla baseline `infantry_weapons`, `infantry_weapons1`, `tech_support`, `tech_recon`, `basic_machine_tools`, `construction1`, `dispersed_industry`, and `radio` technologies.

Each history provides `12000` manpower, `1200` infantry equipment, `180` support equipment, `0.45` stability, `0.85` war support, neutral ruling politics, no elections, and `100` neutrality popularity.

JHX, JIX, JKX, JLX, JNX, JOX, and JPX start with `random_terror_improvised_command`, `random_terror_captured_economy`, and `random_terror_contested_legitimacy`; JMX starts with the three terminal ideas `random_terror_presence_of_the_entity`, `random_terror_world_in_revolt`, and `random_terror_supply_through_ruin`.

The packages contain no state ownership, cores, claims, navy, air force, custom unit, Event 019 provider, model, sound, counter, or out-of-band history-unit reference.

## Validation evidence

- Fresh exact-token collision scan found no live definition of `JHX`, `JIX`, `JKX`, `JLX`, `JMX`, `JNX`, `JOX`, or `JPX` in the vanilla install, sibling local mods, Workshop content, or the current package `common\country_tags` before this patch; pre-existing current-source hits were Event 031 runtime references and archival audit documentation only.
- `hoi4_map_inspect` inspected all eight fallback states with no unknown state IDs; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/800a2deb0cfb713fccb072b83f620c7f05a5a45940bc9032f794aa807522cdd7/0384db71eeae758201e52dd6f7623b5938e5b8367ece27b72707f3f0e7003a19/map-inspect.2a34f1f2aef539ef.json`.
- `hoi4_map_render` produced a validated state/ownership/VP/supply/railway overview for the selected states; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd8b53eb2549add50b207cbe2fd618aafa44f6729a7363de31f02dba24b7b466/de5a82c47fe84b9fffae6cf225df3e909a81d68400765b153661b10266f0cea1/map-state.png`.
- `hoi4_event_inspect` and `hoi4_event_render` traced `chaosx.nr31.1` and its actor initializer; the bounded render is partial but has no blockers; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4de2dc31a31b02d9981de15570062583d2cdf479a333efd18d859fd7beafb25f/273a99bb01e183be7520fb5800fa4606d31e9d09e1fb78861b0703b6f7674e26/event-overview-5bc99dc6d959.json`.
- The Event 031 source trace confirms the exact `Infantry Division` template name, the eight vanilla technologies, and the runtime profile counts; the runtime initializer also unconditionally sets `3` research slots and repeats the manpower/equipment/starting-idea setup.
- `hoi4_focus_inspect` found the current `random_terror_actor_focus_tree` with 47 focuses and 181 diagnostics, including 100 blocking diagnostics for missing focus sprites and a duplicate `(4,6)` coordinate; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3a792dd2f42ec39fcd381d26ddb0665aaea2d7d5ada067b2225fd0c63ffffba/ab34617331f468d6f0a6466ece23a140603ec5e117c338a28786c8f55967a980/focus-inspect.28be5218f55733cb.json`.
- `hoi4_focus_render` rendered the same tree but reported 125 blocking diagnostics; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f8b19e15efadc9df00cd7c0140d7adc4b926ae216553402599bb00ad304efc/de26db7fe61a92e5fc88abbbf94541f994e609c527342b25ed7151f0658bf64d/random_terror_actor_focus_tree.focus.json`; no focus file was edited because focus surfaces are outside this task.
- `hoi4_tech_inspect` traced all eight vanilla technology IDs and `hoi4_tech_render` produced a bounded technology view for `infantry_weapons1`; the dependency aggregate render was blocked by the fixed render budget, and the installed package exposes no separate full Technology Tree Viewer completion route.
- Local source validation resolved all eight tag-to-country paths, all eight history files and capitals, all eight recruited characters, all referenced technology and idea IDs, and all eight portrait DDS-derived texture names from `docs/assets/031_random_terror/portraits/manifest.md`.
- `chaosx_country_package_auditor` confirmed the eight tags, capitals, leaders, portrait names, template, technologies, ideas, and runtime transfer wiring, and identified missing country localisation, portrait/flag sprite registrations, incomplete focus routes, and the shared setup mismatches recorded below.
- `chaosx_ai_probability_auditor` completed the mandatory read-only pass; `hoi4.probability_inspect` found the Event 031 singleton `ai_chance` options and the complete 24-entry incident pool, while `hoi4.probability_evaluate` classified `chaosx.nr31.2.a` as a singleton under scenarios `P01`, `P02`, `P04`, `P06`, and `P10`; artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d968a35acfca56fb8ab67c6403bb32bac64483cfd163ac786c1e58da98a768fb/a0c9e2af74683bddd78a6ffe31f06e8aa0aca24c1b8e0b2a12f09f9e35e53054/probability-inspect-dd9bdd340f7a.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf2db880cb7ebaf0b90cabc973945270f1578979faaa307702efefce29f454fe/9f58708fe2cc26b59b31a17e1efe78b1033e275ef8c3ea8b199d3d16523460ad/probability-47122b0bd1baf14cb781d855.json`.
- No live game launch was performed, as required by repository instructions.

## Risks and parent-owned follow-up

- The runtime initializer overwrites the local `2`-slot and final `5`-slot history values with `set_research_slots = 3`; this is a shared Event 031 behavior outside the disjoint package scope and must be reconciled by the parent if the matrix values must survive activation.
- Runtime setup repeats history manpower, equipment, and starting ideas, so activation must remain idempotent and must not double-count the fallback package values.
- Country name, adjective, party, leader display, focus, decision, idea localisation, flags, and GFX sprite definitions were deliberately not edited because the user excluded localisation, focus, decision, idea, GFX, and shared-registry surfaces; the portrait DDS files exist, but their sprite registration remains parent-owned.
- No package-local AI strategy was added, and no new weighted surface was patched; the probability auditor found no meaningful before/after target for `probability_compare`, so dynamic actor AI and any probability changes remain parent-owned.
- The country auditor found that the current focus tree has only Shadow Council, War Directorate, and Ideological Secretariat leadership routes, with no proven Jihadist, Final Jihad, or False Revelation route or actor focus-tree assignment; these are outside this package scope.
- The country auditor found no dedicated country names/adjectives/party localisation beyond the event text in `localisation\\english\\031_terrorist_attack_l_english.yml`, no portrait GFX sprite registrations in `interface\\`, and no country flags for these tags; the portrait DDS files remain parent-owned assets awaiting consumer registration.
- The Event MCP and technology MCP analyses report workspace-wide partial diagnostics, including inline-source truncation and unrelated existing map/building and localisation diagnostics; these were not changed by this package.
- The country inspection/render route is not exposed as a separate installed HOI4 MCP capability, so country syntax and wiring were validated through source checks, vanilla precedents, and the event/map/technology MCP dependency routes; the country auditor supplied the additional read-only package review.

## Simplifications and omissions

The package is intentionally a dormant carrier/base-setup handoff, not a claim of complete Event 031 country content.

The omitted AI, focus, decisions, localisation, flags, GFX registration, shared registries, OOB placements, and broader economy/production wiring are scope-mandated omissions, not unapproved fallbacks.
