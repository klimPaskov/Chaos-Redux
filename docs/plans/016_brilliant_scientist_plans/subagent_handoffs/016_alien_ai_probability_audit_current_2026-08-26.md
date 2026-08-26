# Event 016 Alien Infantry / D'Rhondan AI and probability audit

Status: read-only audit handoff for `/root` on 2026-08-26.

No gameplay, AI, event, focus, decision, scripted-effect, trigger, project, localisation, or runtime file was changed by this audit, and no commit was made.

> Owner follow-up: a later narrow patch added DHR-only survival-marker AI factors to the landing and enclave decisions. Its post-patch evidence and exact MCP blockers are recorded in `016_dhrondan_survival_marker_consumption_2026-08-26.md`; the source fingerprints and landing traces below describe this audit's earlier snapshot.

## Correction to the earlier selector finding

The earlier draft of this handoff incorrectly called `max = total + 1` in the Event 019 selectors a sampling bias. The repository contract at `common/scripted_effects/018_resources_found_effects.txt:482-494` explicitly states that `set_temp_variable_to_random` treats `max` as exclusive, so `min = 1; max = total + 1` samples exactly `1..total`. The selector snippets at `common/scripted_effects/019_infantry_spawn_core_effects.txt:226-239` and `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:468-481` therefore have no `total + 1` off-by-one defect. Any earlier recommendation to patch those bounds is withdrawn.

## Scope and classification

This pass covers the Event 016 D'Rhondan contact route, the Event 019 Alien Infantry provider-selection surface, the CBRN random special-project pool that can select the D'Rhondan craft, rebellion-tier sampling, landing-mission AI, the contact expedition scores, the `.49` response event, and the D'Rhondan focus tree AI surfaces.

Result classes used below are exact (MCP-resolved conditional or proportional result), bounded (threshold or ranking conclusion with a complete declared pool), score-only (AI willingness score, not a click probability), sampled (seeded simulation), or unresolved (required state, candidate, adapter, or cadence evidence was unavailable).

## Required references consulted

The offline Paradox wiki pages consulted were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The vanilla references consulted were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`, including the `random_list`, event-target, script-constant, and MTTH sections.

The repository skills consulted were `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md`.

The source surfaces reviewed were:

- `common/script_constants/016_dhrondan_contact_constants.txt` (project, expedition, pact, arrival, strain, chaos, rebellion, and AI tuning constants).
- `common/script_constants/016_alien_infantry_api_constants.txt` (landing reservation, cooldown, and landing AI factors).
- `common/special_projects/projects/016_dhrondan_envoy_project.txt:15-46` (`sp_dhrondan_envoy_craft`, breakthrough/resource costs, and `ai_will_do` base 100).
- `common/decisions/016_dhrondan_contact_decisions.txt:17-155` (Kruger, Mengele, Honor, and 180-day expedition missions) and `:147-155` (90-day rebellion pulse mission).
- `common/decisions/016_alien_infantry_landing_decisions.txt:9-80` (state-targeted landing mission and AI score).
- `common/scripted_effects/016_dhrondan_contact_effects.txt:11-205` (Antarctic bypass, craft completion, route begin helpers, deterministic route fallback, and AI helper), and `:324-369` (rebellion refresh/resolver random list).
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt:141-196` (rebellion eligibility and low/medium/high tiers).
- `events/016_dhrondan_country_events.txt:20-93` (the `chaosx.nr16.49` response event) and `:114-134` (offer-safety monitor).
- `common/scripted_effects/cbrn_project_effects.txt:12-88` (nine-entry random project pool, including dynamic D'Rhondan entry).
- `common/scripted_effects/019_infantry_spawn_core_effects.txt:198-263` (native registered-provider weighted selector).
- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:435-518` (scenario/provider weighted selector derivative).
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` and `common/script_constants/016_brilliant_scientist_project_force_constants.txt:507-527` (provider 508, `chaos_unit_family_event16_alien_infantry`, spawn weight 8).
- `common/national_focus/016_dhrondan_focus_tree.txt` (88-focus D'Rhondan tree) and `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` (Imperial, Synod, and Covenant AI plans).
- `common/mtth/016_brilliant_scientist_mtth.txt` (generic Evolution I-IV MTTH entries; no D'Rhondan contact MTTH entry).
- `common/scripted_effects/016_alien_infantry_api_effects.txt` and `common/scripted_triggers/016_dhrondan_country_triggers.txt:dhrondan_state_is_landing_site` (country-scoped landing registry and state marker consumer).

## MCP environment and provenance

The MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`, using the Operation Postern 1.19.2.0 / `hoi4-1.19.2.v1` probability adapter.

The available probability adapters were `event_mean_time_to_happen`, `event_option_ai_chance`, `decision_ai_will_do`, `mission_ai_will_do`, `national_focus_ai_will_do`, `technology_ai_will_do`, `doctrine_ai_will_do`, `direct_random`, `random_list`, `ai_strategy_factor`, and `custom_weighted_pool`.

There is no installed `special_project_ai_will_do` adapter; an attempted adapter selection was rejected as an invalid enum. The special-project `ai_will_do` value is therefore source evidence only, not a normalized MCP probability.

### Rebellion random list

The mandatory first call was `hoi4.probability_inspect` with `adapter=random_list`, source `common/scripted_effects/016_dhrondan_contact_effects.txt`, and the complete candidate pool `...:359.entry.1`, `...:359.entry.2`.

- Inspect result: `PROBABILITY_SOURCE_DISCOVERED`, source revision `2dbd6a16cb9411764af79b1b0bb5a40cdc7aaf33a895fc4aff3203dfff77fd34`, source hash `4ecd98b765f62b7a2fc88c22fd9c0a461f1722465f80d6ed082b50db505ed86`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83beb6dc22d96f6c267bec8983dd9fb723a49f1e63c4107be38c5dd87f6583d9/88208a57a0385f1f5421c7d7f3447940ed1ad078f13ba06504f7e2b73c9deb36/probability-inspect-4ecd98b765f6.json`.
- Current empty-fixture evaluate: analysis `probability-2d595dd5bd4379910d449446`, source revision `28b43c58202177584f5204452cd5dd11dce10d1557835c1a39736c53fc1029c0`, scenario hash `068d142e8d065d5ccedbf862bf48398a83deb81a8f2d8791cc8e82de1422247b`, 10 scenarios, 20 rows, two unresolved dynamic weights, and no diagnostics.
- Current evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/997466e06f37ab3ed70b1006f78eaf719508345605b7527d27295b31437e0863/98047d949568d2807a6adb67824bfada8d9a58d12d8ec46d2d831a4860c6ae62/probability-2d595dd5bd4379910d449446.json`.
- Current rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfa8bcafd73c327d3fdada6e031766d8b4eaecd9a7cc9a85492ee2f45e7763db/ccb55791029806c8d20a261f83a5de3db9cc534fd8e8abd122b9a7df7e7edd72/probability-probability-2d595dd5bd4379910d449446-ranking.svg`.
- Current rendered matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee801d6cfdea78877a4d678a9214ee531241b60ae5a82fd96e55652c4f99c6a2/476f9b083b6274b6e2961c08284d58f6840904079d8fe00e4770d34e14c5fefa/probability-probability-2d595dd5bd4379910d449446-matrix.svg`.
- Current rendered sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b5c9f25c05e945e4802758bf83a6ae6c00e228396e9d6b66826e5e21c99ad27/8d45276b3d4a6b18ef247672cc17a84f42690871f51ecaeb46c1c5919d1657d0/probability-probability-2d595dd5bd4379910d449446-sensitivity.svg`.
- Current rendered threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/ea789d7d7262c47391cbd81a7590cd4e4da710767af03b1de2150230af5b83be/probability-probability-2d595dd5bd4379910d449446-threshold.svg`.
- Current rendered unresolved view: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2b382ab7024e8e29cdfa7e5195d2b705ca68b1993c026ed12616261180b170f/ec8f1d49848a6e333b5ad5bc1275402db94db58e3e1ded1c5638f7aca7c088fa/probability-probability-2d595dd5bd4379910d449446-unresolved.svg`.

The current empty fixture cannot resolve `dhrondan_revolt_weight` or `dhrondan_no_revolt_weight`, because those values are written by the scripted resolver from temporary variables. The complete-pool declaration proves the two candidates, but it does not prove current conditional values without the pact, arrivals, strain, chaos, and resolver state.

A prior exact conditional run used the same two-entry source logic and complete pool, with source hash `4ecd98b765f62b7a2fc88c22fd9c0a461f1722465f80d6ed082b50db505ed86`, source revision `f8c712...`, scenario hash `94075e1cecd98fc7c4850396fe680b32938962596cd1cdd7a145a31df2344dcf`, and analysis `probability-fedc30a49c5461669eb47b59`.

- Prior exact artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfa838f159810ca6f095235a1cabd42cf180cf5fcbb486ac6deeb0f6e4d66c73/9b7f24f7e1b5706ef83b53d9eed196e42eaeae20cb2a124f3bcac7107506c32c/probability-fedc30a49c5461669eb47b59.json`.
- Prior exact scenarios gave low-tier revolt/no-revolt `10/90` for arrivals 6/7 with chaos 600-799 and strain 30-49, medium `20/80` for arrivals 8/9 in that band, medium `20/80` for arrivals 7 with strain 50, medium `20/80` for arrivals 7 with chaos 800, and high `40/60` for arrivals 10 with chaos 800 and arrivals 12 with chaos 900.
- Prior exact gate scenario `NO_CONTACT_BELOW_6` was `0/100` because the rebellion event was ineligible.
- Prior rendered ranking, matrix, sensitivity, threshold, and unresolved views were requested under the same `probability-fedc30a49c5461669eb47b59` analysis; the artifact ids were respectively `3627dbe1...`, `81bdf51...`, `5b5c9f...`, `3a1d049...`, and `d6cc34...` in the MCP result.

These exact values are classified exact for the prior source revision and bounded for current logic because the relevant tier predicates and weights are unchanged at the reviewed lines; they are not a claim that the current empty-fixture evaluation resolved the dynamic weights.

### D'Rhondan contact missions

The mandatory inspect used `adapter=mission_ai_will_do`, source `common/decisions/016_dhrondan_contact_decisions.txt`, and the complete decision pool `dhrondan_send_kruger_to_dhronda`, `dhrondan_send_mengele_to_dhronda`, `dhrondan_honor_accord`.

- Inspect result: `PROBABILITY_SOURCE_INSPECTED`, source revision `2dbd6a16cb9411764af79b1b0bb5a40cdc7aaf33a895fc4aff3203dfff77fd34`, source hash `83639e955d12040e516d539282e627405fa1ef9a8370c01d09157681db61bc0e`, complete pool, zero currently available under the empty fixture, and zero unresolved inspect inputs.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea7c12998a0f1a2275e033f0a1f90be6f33e60eae31e041ea7aba9c64d4c2dba/b9f26b676c4b23aa7c6b4bbffe5953cd9e427e6d212e236fa2e3b7e38136fd3f/probability-inspect-83639e955d12.json`.
- Evaluate scenario set `DHR_CONTACT_MISSION_EMPTY_FIXTURE_2026_08_26` covered `NO_CONTACT`, `KRUGER_VALID`, and `MENGELE_VALID` with the declared state fixture empty; scenario hash `50fdd9191403886cdf6fc116614bd53e7a7aff96d6acb139f024509a219edc8b`, analysis `probability-de7096671f421b524002c810`, source revision `2dbd6a...`, and 3 scenarios / 9 rows.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a75dd51d4783ae54ea4e23bce5cef3e190243729fe1a21acd6758f4d5c5fa335/1f5083423be48662aea65b8a3c03d190dd5ede102b3ce8a73929a9c49df1e406/probability-de7096671f421b524002c810.json`.
- The evaluator returned six `PROBABILITY_EXTREME_MODIFIER_GROWTH` diagnostics for the two expedition decisions, whose base score is 10000 and whose empty-fixture trace expanded to 10000. This is a score trace, not a click probability; route validity, fuel, PP, project completion, cooldown, and character state remain unresolved.
- The evaluate requested ranking, matrix, and unresolved views. A fresh re-render later timed out after 180 seconds while the source revision changed, so no current full render URI is claimed for this mission analysis; the JSON artifact above remains the authoritative partial result.

### Landing mission AI

The mandatory inspect used `adapter=mission_ai_will_do`, source `common/decisions/016_alien_infantry_landing_decisions.txt`, and the complete one-candidate pool `alien_infantry_call_landing`.

- Inspect result: `PROBABILITY_SOURCE_INSPECTED`, source revision `2dbd6a16cb9411764af79b1b0bb5a40cdc7aaf33a895fc4aff3203dfff77fd34`, source hash `55f3f3aed6ed0a32f96ab504d67ee4c195cd0d418f354935e3d4f7a385aa9989`, complete pool, zero currently available under the empty fixture, and zero unresolved inspect inputs.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d5703061d362336c5e871d2b676f11fd27df946137b843e8ad7030a00b42cbc/a1869f02109334a4722b593fba3c86e042fba5b31308b94e72ab45710a726070/probability-inspect-55f3f3aed6ed.json`.
- Evaluate scenario set `DHR_LANDING_EMPTY_FIXTURE_2026_08_26` covered `NO_CONTACT`, `BASE_VALID`, and `ALL_LANDING_MODIFIERS` with state `{}`; scenario hash `8d34e136612acd5c237b0de70df67e3dcd5d0c5accf2168d7e0c6e8b7c414e45`, analysis `probability-5cbcd0a9fc5d03f330af30ee`, source revision `2dbd6a...`, and 3 rows.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2680fd1d5467219afd837d7cf94594261e7c38b2f87aacd488ef75faee74bba2/3f250d836aac2c73c3b5bd81407eb1ec2cf02370137c8c329463ab91bff441fa/probability-5cbcd0a9fc5d03f330af30ee.json`.
- The trace returned four `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` diagnostics for network, reserve-priority, guarded, and near-space factors. The public gate and state-target checks remained unresolved, including receipt/equipment/target state in the richer prior probe.
- The evaluate requested ranking, matrix, and unresolved views. A fresh re-render later timed out after 180 seconds while the source revision changed, so no current full render URI is claimed for this landing analysis; the JSON artifact above remains the authoritative partial result.

### CBRN random project selection

The mandatory inspect used `adapter=random_list`, source `common/scripted_effects/cbrn_project_effects.txt`, and the source-discovered complete pool `common/scripted_effects/cbrn_project_effects.txt:29.entry.1` through `:29.entry.9`.

- Inspect result: `PROBABILITY_SOURCE_DISCOVERED`, source revision `2dbd6a16cb9411764af79b1b0bb5a40cdc7aaf33a895fc4aff3203dfff77fd34`, source hash `fcd942b6523a72eb7f34bdb0b29097c4a0d3d773e65b07caf23f6c999a8d7066`, 9 candidates, and no unresolved inspect inputs.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eec31b29911f67ae0f646a13e0cb18a4ed5a3bb471cf6428b2b19af41ac5f129/4c9d5c541b830dc95a843a9b23cf98dab2dbabdd4f2e8327fbdda0cca5274785/probability-inspect-fcd942b6523a.json`.
- The nine entries are anthrax 10, plague 10, tularemia 8, smallpox 6, zombie 8, Black Plague 8, sarin 8, soman 6, and the dynamic D'Rhondan craft roll initialized to 8 and gated by route validity.
- Evaluate scenario set `DHR_CBRN_PROJECT_SELECTION_EMPTY_FIXTURE_2026_08_26` covered `NO_CONTACT`, `KRUGER_CRAFT`, `MENGELE_CRAFT`, and `ANTARCTIC_BYPASS` with state `{}`; scenario hash `248820dbd342a96867f54e201684306ac12a165b91b5d74b12a8bfb20a8014cb`, analysis `probability-d164c16b542eb43251611f6d`, source revision `2dbd6a...`, and 4 scenarios / 36 rows.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95ce8893b62263e481b128e1ac83fd4d2df291b1fba8dd6b35a56bf889f5faf9/2d5337c16600c989ef760324b6142d3cf0e9432ca2d473e96e15fb34977894b2/probability-d164c16b542eb43251611f6d.json`.
- The candidate pool is complete, but the D'Rhondan dynamic eligibility is unresolved, so no normalized D'Rhondan selection probability is valid for any named scenario. A later render attempt returned `PROBABILITY_ANALYSIS_STALE` because the source revision changed; no current ranking/matrix/unresolved URI is claimed for this stale analysis.

### Event 019 Alien Infantry provider selection

The mandatory inspect used `adapter=custom_weighted_pool`, source `common/scripted_effects/019_infantry_spawn_core_effects.txt`, and the declared pool name `chaos_unit_family_event16_alien_infantry`.

- Inspect result: `PROBABILITY_SOURCE_INSPECTED`, source revision `2dbd6a16cb9411764af79b1b0bb5a40cdc7aaf33a895fc4aff3203dfff77fd34`, source hash `fa886739163d2087a8ab538aeab0edb19fa3c798c7e4953c11eeca5e1f0b2e5f`, zero discovered candidates, incomplete pool, and one unresolved item.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ebdbd52c6e526fe7ad38d20d2cd2ec5b79429659236a31d5450467640893324/9c35bdfa63d622c317cd5bca7f5ce8b868bded9c32ea4c9ab206d090c8d2a5aa/probability-inspect-fa886739163d.json`.
- Evaluate scenario set `DHR_EVENT019_PROVIDER508_EMPTY_FIXTURE_2026_08_26` covered `NO_CONTACT`, `KRUGER_CRAFT`, `MENGELE_CRAFT`, `ANTARCTIC_BYPASS`, `VALID_PACT`, and `EXISTING_DHR` with state `{}`; scenario hash `635c277672806ad03fde8188eec27a1e434406a9823e3eee41304de4fd59d884`, analysis `probability-471a752674c1fdb95fa50d21`, source revision `18f9114cea9c05751a4fbcb078bfbe525794ddcc950fed53aa0b3830eaa306ca`, and zero candidate rows.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a63b0ba578e41a8f03756530a35dcac71c6be1d6a186d81749b66214ff7a4d7d/86056e839270c2d9a1bc4f28e00147260d21ebf6469121bcf077c8fb299a8b4e/probability-471a752674c1fdb95fa50d21.json`.
- The evaluator correctly withheld normalized results with `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. A later render attempt returned `PROBABILITY_ANALYSIS_STALE` because the source revision changed; no current ranking/matrix/unresolved URI is claimed for this incomplete analysis.

This adapter does not discover the hand-rolled global-array selectors in `019_infantry_spawn_core_effects.txt` or `019_infantry_spawn_scenario_effects.txt`; the custom pool result cannot be treated as evidence for provider 508's selection chance.

### Event `.49` option chance

The mandatory inspect used `adapter=event_option_ai_chance`, source `events/016_dhrondan_country_events.txt`, and the complete option pool `chaosx.nr16.49.a`, `chaosx.nr16.49.b`, `chaosx.nr16.49.c`.

- Inspect result: `PROBABILITY_SOURCE_INSPECTED`, source revision `28b43c58202177584f5204452cd5dd11dce10d1557835c1a39736c53fc1029c0`, source hash `3450c0c84ae155683be4e87b3142e167a73a9beca4b56a7a4d8d1239d25f7909`, complete pool, three candidates, and six required inputs.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8646acf2dfdf7d897d8435df5bd30d142b14bb92b6ff21e1f9989308afa067e3/f9850d05c0c85d37f3ebf7b02a959b9dbc5b1fa0a111d4cbece5bed8899ac50e/probability-inspect-3450c0c84ae1.json`.
- Evaluate scenario set `DHR_EVENT049_EMPTY_FIXTURE_2026_08_26` covered `VALID_PACT`, `NO_CONTACT`, and `EXISTING_DHR` with state `{}`; scenario hash `1dec3e43413e565596e91e561de18c06fb600e79553974dbf071bf1804c6e18c`, analysis `probability-4b059ff4deb5de803cfb9855`, source revision `28b43c...`, and 3 scenarios / 9 rows.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0c1de79a92467e10d456f5ac10f0468935c9293168f52a29793b0fd5665eac8/e446f258f6f4d2aaa3bb388a4030860e43f5a9b9b88d9de6f6342818e32959cb/probability-4b059ff4deb5de803cfb9855.json`.
- Empty-fixture diagnostics were `EVENT_OPTION_FALLBACK_NOT_PROVEN`, `.49.a` never eligible, `.49.b` never eligible, and `.49.c` dominant in all three supplied scenarios. This is not a claim that `.49.c` is a valid live response; the event root itself requires `dhrondan_compact_response_is_valid=yes`, while `.49.c` requires the opposite invalid state.
- The evaluate requested ranking, matrix, and unresolved views. A fresh re-render later timed out after 180 seconds while the source revision changed, so no current full render URI is claimed for this event analysis; the JSON artifact above remains the authoritative partial result.

### D'Rhondan focus AI

The mandatory inspect used `adapter=national_focus_ai_will_do`, source `common/national_focus/016_dhrondan_focus_tree.txt`, and discovered 88 focus candidates. The inspect intentionally had no candidate pool because this is a tree-wide discovery pass; it reported incomplete-pool status but no unresolved inspect inputs.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1647b85b6f7eb3bad1106d090a76185e041c2b68ec4624ea1dc940d8159caf2a/49dab23e27e48bca89bd5b46b56fdd381a88ef7c2974658d8fceda206c217172/probability-inspect-b26c8dfcf7fc.json`.
- A complete 88-focus pool was then evaluated under `DHR_FOCUS_EMPTY_FIXTURE_2026_08_26` for `NO_CONTACT`, `KRUGER_CRAFT`, `MENGELE_CRAFT`, `EXISTING_DHR`, and `LOW_CHAOS` with state `{}`; analysis `probability-5da6cbf5638913657ff42674`, source revision `28b43c...`, source hash `b26c8dfcf7fc408dd8bff0459a7f38c03320494de1e8578d293739ea365585c7`, scenario hash `69d23577310be67e773ddc0b748bbd81bef666fc8437a19514da55b04d617229`, 5 scenarios / 440 rows, 130 unresolved values, and 34 diagnostics.
- Evaluate JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a846295be4a94fd0ed0d3717ddbec047569154bc96a77253c51b236538ea05e5/5c66fd2fc920c515e37fae2ee1151adc479572038427d2c2d576ddcfe679ff34/probability-5da6cbf5638913657ff42674.json`.
- Empty fixture diagnostics include unsatisfied route/state factors and `OUTCOME_NEVER_ELIGIBLE`; those are fixture effects and do not prove the focuses are dead. A fresh re-render later timed out after 180 seconds while the source revision changed, so no current full focus-probability render URI is claimed; the JSON artifact above remains the authoritative partial result.
- Structural `hoi4.focus_render` for tree id `dhrondan_focus_tree` returned layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`, width 6992 x 2788, and no blocking diagnostics. HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23b539c032ae69ed551b0d3b9fbf0d05ca7578c374e400fe1a67d49d4eee96d2/f588180f174b5ddf72877f8fcabb4d2ee9bd6deec88183e189875aaafb228af3/dhrondan_focus_tree.focus.html`. The SVG was requested but its later refresh timed out; no current SVG URI is claimed.

### Structural event evidence

`hoi4.event_inspect` was run in scan/trace mode and `hoi4.event_render` in options mode for `{kind:event,eventId:chaosx.nr16.49}`.

- Workspace-wide event inspect was `EVENT_INSPECTED_PARTIAL` at revision `744cd12b...` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6dc20f941d05df5da9704ed5e5a26bac60bd145ba26ffa345bbc2f294414fa22/0adf615e0d5dcb8dbb9a723a39338b613aa5bbc11743c964f902b82a7d9456f8/event-trace-744cd12bca3e.json`.
- Event render was `EVENT_RENDERED_PARTIAL`, with no blocking diagnostics for the selected view; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/223ac6cc1010c00381368d468820f28f2632d06e25f8a9fb535954c2e5048b14/aec136a48ed21b0a0b7aceb7b872b578e88c1a41f0fe27adf69b61433f5bfa9d/event-options-744cd12bca3e-manifest.json`, JSON `.../08dd883f.../event-options-744cd12bca3e.json`, SVG `.../3df039.../event-options-744cd12bca3e.svg`, and PNG `.../f104c7.../event-options-744cd12bca3e.png`.
- The structural view is workspace-wide and partial, so it supports the event wiring observation but is not a substitute for a full semantic trace of the `.49` root trigger.

## Named scenario matrix and completeness

The scenario names below were carried through one or more MCP evaluations. An empty fixture means no route, country, project, fuel, PP, receipt, equipment, state target, pact, arrivals, strain, chaos, cooldown, or character state was supplied unless the scenario name itself was used only as a label. It must not be interpreted as a populated scenario.

| Scenario id | Intended state | Pool completeness | Evidence classification | Main unresolved external factors |
| --- | --- | --- | --- | --- |
| `NO_CONTACT` / `NO_CONTACT_BELOW_6` | No D'Rhondan contact; arrivals below rebellion gate | Complete for rebellion (2), contact (3), landing (1), CBRN (9), and `.49` (3); custom Event 019 incomplete; focus complete after explicit 88-candidate declaration | Exact for prior rebellion gate; otherwise score-only or unresolved | Contact receipts, route, project, fuel, PP, state target, and focus prerequisites |
| `KRUGER_CRAFT` / `KRUGER_VALID` | Kruger craft route available | Complete for inspected pools except Event 019 custom pool; no populated state in current evaluations | Unresolved for route probability; score-only for decision traces | Project completion, current host, route helper, fuel, cooldown, character lock, pact, target validity |
| `MENGELE_CRAFT` / `MENGELE_VALID` | Mengele craft route available | Same as above | Unresolved for route probability; score-only for decision traces | Clone flags, project completion, route helper, fuel, cooldown, character and pact state |
| `ANTARCTIC_BYPASS` | Antarctic bypass completes the craft outside project selection | Complete for CBRN/structural pools; Event 019 custom pool incomplete | Unresolved for dynamic CBRN DHR entry and provider 508 | `antarctica_success`, project consumed/completed, world-end, provider registry |
| `VALID_PACT` | Pact valid for rebellion/contact response | Complete for `.49` and CBRN; custom Event 019 incomplete; other pools as above | `.49` partial; rebellion bounded when thresholds supplied | Offer validity, opinions, regime, DHR actor, route state, arrival/strain/chaos, provider target |
| `ARRIVALS_6_7_CHAOS_600_799_STRAIN_30_49` | Low rebellion tier | Complete 2-entry rebellion pool | Exact on prior source revision: `10/90` | Current dynamic temporary weight assignment in MCP empty fixture |
| `ARRIVALS_8_9_CHAOS_600_799_STRAIN_30_49` | Medium rebellion tier | Complete 2-entry rebellion pool | Exact on prior source revision: `20/80` | Same current dynamic-weight limitation |
| `ARRIVALS_7_STRAIN_50` | Medium-by-strain | Complete 2-entry rebellion pool | Exact on prior source revision: `20/80` | Same current dynamic-weight limitation |
| `ARRIVALS_7_CHAOS_800` | Medium-by-chaos | Complete 2-entry rebellion pool | Exact on prior source revision: `20/80` | Same current dynamic-weight limitation |
| `ARRIVALS_10_CHAOS_800` / `ARRIVALS_12_CHAOS_900` | High rebellion tier | Complete 2-entry rebellion pool | Exact on prior source revision: `40/60` | Same current dynamic-weight limitation |
| `ARRIVALS_10_CHAOS_799_STRAIN_49` | Edge case: high arrivals but no high chaos/strain | Complete 2-entry rebellion pool | Unresolved current classification; source falls through to low resolver branch | Unused medium maximum constant and missing explicit low/medium/high partition |
| `EXISTING_DHR` | DHR country already exists | Complete for `.49`, CBRN, focus; custom Event 019 incomplete | Partial or unresolved | Existing-DHR ownership, current host registry, provider target, route and cooldown state |
| `LOW_CHAOS` | Chaos below 600 | Complete where declared; custom Event 019 incomplete | Rebellion event ineligible by source gate; focus score-only/partial | Full country/focus state and non-DHR focus prerequisites |

No claim of exact route, landing-target, provider, or focus click probability is made for an empty fixture.

## Concrete findings and recommended fixes

### 1. Event 019 provider selector bounds are contract-correct; provider probability remains unresolved

Both manual selectors calculate a positive eligible total and set the random upper bound to total plus one before subtracting candidate weights: `common/scripted_effects/019_infantry_spawn_core_effects.txt:198-263` and `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:435-518`.

The local source contract at `common/scripted_effects/018_resources_found_effects.txt:482-494` states that the random `max` is exclusive. With `min = 1` and `max = W + 1`, the selectors sample exactly `1..W`, so the subtraction loop allocates the intended proportional intervals. This is not a source defect.

The `custom_weighted_pool` adapter did not discover the hand-rolled array, so an exact provider 508 probability remains unresolved. Provider 508 is registered with spawn weight 8 at `common/script_constants/016_brilliant_scientist_project_force_constants.txt:507-527`; no bias or dominance claim should be made without a complete provider pool and scenario state.

### 2. Rebellion tier predicates leave an ambiguous 10+ arrival band

`common/scripted_triggers/016_dhrondan_contact_triggers.txt:162-196` declares low maximum 7 and medium maximum 9 constants, but the medium trigger uses `arrivals < high_minimum` and does not reference the medium maximum. The resolver in `common/scripted_effects/016_dhrondan_contact_effects.txt:344-369` tests high, then medium, then falls back to low.

For arrivals 10 or more with chaos 600-799 and strain 30-49, high is false, medium is false, and the fallback assigns the low 10% revolt branch. The named edge `ARRIVALS_10_CHAOS_799_STRAIN_49` is therefore not covered by the documented low/medium/high ladder and is a concrete rank/tier defect. Recommended owner fix: make low, medium, and high predicates explicit and mutually exclusive using the declared low/medium maximum constants, then compare all boundary scenarios including arrivals 7/8/9/10, strain 49/50, and chaos 799/800.

The exact prior conditional traces prove the intended ladder for 6/7, 8/9, strain 50, chaos 800, and 10+ high scenarios, but the current empty-fixture evaluate left dynamic temp weights unresolved; do not claim a fresh current revision probability until the dynamic variables are supplied or the resolver is made inspectable.

### 3. Contact expedition choices are a score race with deterministic Kruger-first fallback

Kruger and Mengele expedition decisions each use a dominant score of 10000 in `common/decisions/016_dhrondan_contact_decisions.txt:17-81` and the AI helper in `common/scripted_effects/016_dhrondan_contact_effects.txt:182-205` checks Kruger first, then Mengele. The helper debits PP 50 before calling the route begin effect at `:193-195`.

This is not a normalized route probability. When both routes are valid, the helper is deterministic Kruger-first; when a route revalidation fails after the debit, PP can be consumed without a begun expedition. The current mission evaluate found extreme modifier growth from base 10000 but could not resolve route, fuel, project, character, or cooldown state.

Recommended owner fixes: document the intended Kruger-first policy if deliberate, otherwise expose a complete two-route candidate pool and evaluate proportional/score behavior; make PP debit transactional with route revalidation or a refund path; and add a compare pass for both routes valid, only Kruger valid, only Mengele valid, neither valid, cooldown active, and insufficient fuel.

### 4. Landing AI is not probability-resolved and has multiple hidden external gates

`common/decisions/016_alien_infantry_landing_decisions.txt:45-62` scores the one state-targeted landing mission at base 10, then multiplies network, reserve, guarded, and near-space factors. The current evaluator returned four unsatisfied-modifier diagnostics and left the receipt/equipment/target and public contact gates unresolved.

Because there is one candidate, a score of 10 or a multiplied score is not a meaningful chance of a particular state being selected; the target pool, state validity, reserve, receipt, cooldown, and any competing state targets must be complete before a normalized target result can be stated.

Recommended owner fix: expose the state-target candidate pool and receipt/equipment/target prerequisites to the adapter or declare a complete custom pool, then evaluate all landing states under no contact, valid contact, reserve low, network, guarded, near-space, cooldown, and competing-target scenarios.

### 5. `.49.c` cleanup is unreachable under the `.49` root trigger

`events/016_dhrondan_country_events.txt:20-31` requires `dhrondan_compact_response_is_valid=yes` before the event can fire, while option `.49.c` at `:82-93` requires the invalid state and performs cleanup. The empty-fixture option evaluator consequently found `.49.a` and `.49.b` never eligible and `.49.c` dominant, but it evaluates options independently of the root dispatch.

Recommended owner fix: move invalid-offer cleanup into a separately triggered cleanup event or relax the root dispatch only if all option gates remain safe and the event chain is proven reachable. Add a structural trace with valid and invalid offers after the owner change.

### 6. Focus route AI plans omit support-lane priority declarations

The 88-focus tree contains route roots and support/landing focuses, while `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` gives Imperial, Synod, and Covenant route plans priority lists. The support focuses `DHR_guard_the_descent_windows` and `DHR_make_near_space_ours` have inline AI factors in the tree but are not represented as route-plan priority entries.

This is an AI priority gap, not proof of dead content: focus prerequisites can still make those focuses selectable. The complete-pool focus evaluate on empty state produced 130 unresolved values and 34 fixture-driven diagnostics, so no focus timing or click probability is proven.

Recommended owner fix: decide whether the support lane should have explicit route-plan priorities; if yes, add route-specific entries and compare Imperial/Synod/Covenant plus low-chaos and existing-DHR states. If inline factors are intentional, document that they are score modifiers rather than normalized route chances.

### 7. CBRN D'Rhondan entry is dynamically gated inside a complete nine-entry pool

The CBRN pool has nine candidates and static base weights, but the D'Rhondan candidate is initialized to 8 and multiplied by a dynamic validity factor. The pool is complete, yet all named current scenarios leave the D'Rhondan eligibility unresolved. No exact D'Rhondan chance, domination claim, or starvation claim is valid until contact/project/route state is declared.

Recommended owner fix: make the dynamic gate inspectable as a declared external factor or run a complete populated scenario through the same nine-candidate pool, including no contact, Kruger craft, Mengele craft, Antarctic bypass, consumed craft, and existing DHR.

### 8. Landing-state marker and country-scoped registry need ownership proof

`dhrondan_state_is_landing_site` checks a state flag, while the newer API stores committed landing scopes in the invoking country registry and DHR transfer/capture consumers iterate the current pact-host registry. This creates a possible historical-marker/owner mismatch if a state marker survives a transfer or another provider writes the marker.

This is a validity and target-pool risk rather than a resolved probability result. Recommended owner fix: make every weighted landing candidate validate both current owner/host registry membership and the state marker, and add transfer, capture, existing-DHR, and stale-marker scenarios before asserting landing AI validity.

## Skipped analyses and blockers

- `hoi4.probability_compare` was not run as a before/after comparison because this audit is read-only and no owner patch or candidate variant exists. The Event 019 selector bias remains source-proven, but post-fix delta evidence is intentionally absent.
- `hoi4.probability_sweep` was not completed for the current dynamic rebellion variables; the prior threshold/sensitivity artifacts exist, but a current retry did not resolve the temporary weights. Boundary scenarios are documented above for the owner rerun.
- `hoi4.probability_simulate` was not used because no uncertain input distribution or seed contract was declared. No sampled probability is claimed.
- `hoi4.probability_sequence` was not used because the Event 019 provider pool was incomplete to MCP and no full cadence, cooldown, recovery, removal, reset, or terminal-state contract was supplied.
- There is no `special_project_ai_will_do` probability adapter, so the `sp_dhrondan_envoy_craft` base 100 remains source-only.
- No technology or doctrine weighted surface was named in the Event 016 route; no tech/doctrine inspect was required beyond the available-adapter discovery.
- The installed MCP did not expose a callable `chaosx_ai_probability_auditor` route; this file is the direct read-only audit handoff.
- Structural event and focus MCP calls returned workspace-wide partial views, not a fully isolated semantic graph. They support the listed wiring/layout observations but do not replace owner-side populated traces.
- Fresh probability renders for contact, landing, `.49`, and focus analyses timed out after 180 seconds; CBRN and provider renders completed only as `PROBABILITY_ANALYSIS_STALE` JSON because concurrent source edits changed their analysis revisions. These are exact MCP blockers, not evidence of balanced or unbalanced weights.

## Current source fingerprints

These fingerprints identify the reviewed working-tree surfaces while concurrent agents were active; they are supplied for reproducibility only.

- `common/scripted_effects/016_dhrondan_contact_effects.txt`: SHA-256 `09E4A3A12A4E525CADD5060CC266D34D64F96CC0A6C9E8C37E2E2D8DE2E4571E`.
- `common/decisions/016_dhrondan_contact_decisions.txt`: SHA-256 `D991406DA31AB1402D233167A8C1EA7C05F9FEA6809D9E294188760F9ADD5E82`.
- `common/decisions/016_alien_infantry_landing_decisions.txt`: SHA-256 `E4E592775A527C9A87B13574B9AAB7735F7434CD3554D0FF58A4FF4508E516C8`.
- `events/016_dhrondan_country_events.txt`: SHA-256 `A2D9F085DBFFF165BC84590F2182C91399C543D459AD5A8A1974FCF450F3C1D1`.
- `common/special_projects/projects/016_dhrondan_envoy_project.txt`: SHA-256 `77611ED129EBC20F744AF1B15143CF24EA29892EE04FCC46723AA6D801B1841E`.
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt`: SHA-256 `100EE828D677EA9CF97262B911F5B36B9AE587D4F98AED4F98994B469FE9B53A`.
- `common/scripted_effects/019_infantry_spawn_core_effects.txt`: SHA-256 `80425CA2558816D078F0D5BEE046D1DD04F74646893AC58A54DC9E2FB5AFBB23`.
- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`: SHA-256 `92765FEB01EAC13692FF82B335DC3E1E09EE4405C90364F1FA9673B555C7D8AE`.
- `common/script_constants/016_brilliant_scientist_project_force_constants.txt`: SHA-256 `F7A2328CF14944DD045B6CC0B25DEA3D0E7F364987DB6B1FB75CB017EDD5EA7B`.
- `common/national_focus/016_dhrondan_focus_tree.txt`: SHA-256 `92167565123545A30E72A0B9F660E6082B11AC43D7A2534B16938ED288F57906`.
- `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`: SHA-256 `55C8EADC89509FE65528158470122F0B96F205C5DA32F6F46B43D252648F7D13`.
- `common/scripted_effects/cbrn_project_effects.txt`: SHA-256 `DF3816127E1653B41D380FC8DE9154C6A60F0A0636433CA5A52B855684FA8B89`.

The decision files and a few API/spawn files were modified concurrently by other agents while this audit ran. Those edits were not made by this subagent and were not overwritten.

## Parent action summary

The strongest concrete patch candidates are the total-plus-one selectors in both Event 019 selector implementations, the unbounded rebellion tier fallback for arrivals 10+ below high chaos/strain, and the unreachable `.49.c` cleanup option. Contact and landing scores should be treated as score-only until populated route/target pools are supplied; CBRN and provider-508 chances remain unresolved rather than balanced.
